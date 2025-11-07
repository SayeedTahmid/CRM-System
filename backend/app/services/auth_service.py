from __future__ import annotations

from datetime import timedelta
from typing import Dict, Optional
from uuid import uuid4

from fastapi import HTTPException, status
from jose import JWTError
from loguru import logger
from passlib.context import CryptContext
from supabase import Client, create_client

from ..core.config import settings
from ..core.security import create_access_token, decode_token
from ..models.schemas import AuthTokens, LoginRequest, RegisterRequest, User, UserContext
from .repository import BaseRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    async def register(self, payload: RegisterRequest) -> AuthTokens:  # pragma: no cover - interface
        raise NotImplementedError

    async def login(self, payload: LoginRequest) -> AuthTokens:  # pragma: no cover - interface
        raise NotImplementedError

    async def refresh(self, refresh_token: str) -> AuthTokens:  # pragma: no cover - interface
        raise NotImplementedError


class InMemoryAuthService(AuthService):
    def __init__(self, repository: BaseRepository) -> None:
        self.repository = repository

    async def register(self, payload: RegisterRequest) -> AuthTokens:
        company = await self.repository.create("companies", {"id": str(uuid4()), "name": payload.company_name})
        user_id = str(uuid4())
        hashed_password = pwd_context.hash(payload.password)
        user_record = {
            "id": user_id,
            "email": payload.email,
            "full_name": payload.full_name,
            "role": "admin",
            "company_id": company["id"],
            "password_hash": hashed_password,
            "is_active": True,
        }
        await self.repository.create("users", user_record)
        await self.repository.create(
            "company_users",
            {"id": str(uuid4()), "company_id": company["id"], "user_id": user_id, "role": "admin"},
        )
        return self._issue_tokens(user_record)

    async def login(self, payload: LoginRequest) -> AuthTokens:
        users = await self.repository.list("users", {"email": payload.email})
        if not users:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        user = users[0]
        if not pwd_context.verify(payload.password, user.get("password_hash", "")):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return self._issue_tokens(user)

    async def refresh(self, refresh_token: str) -> AuthTokens:
        payload = decode_token(refresh_token)
        users = await self.repository.list("users", {"id": payload.get("id")})
        if not users:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
        return self._issue_tokens(users[0])

    def _issue_tokens(self, user: Dict) -> AuthTokens:
        user_payload = {
            "id": user["id"],
            "email": user["email"],
            "company_id": user["company_id"],
            "role": user.get("role", "sales"),
            "full_name": user.get("full_name"),
        }
        access = create_access_token(user_payload)
        refresh = create_access_token(user_payload, timedelta(minutes=settings.refresh_token_expire_minutes))
        return AuthTokens(
            access_token=access,
            refresh_token=refresh,
            user=User(id=user["id"], company_id=user["company_id"], email=user["email"], full_name=user.get("full_name"), role=user.get("role", "sales"), is_active=user.get("is_active", True)),
        )


class SupabaseAuthService(AuthService):
    def __init__(self, client: Client | None = None) -> None:
        self._client = client or create_client(settings.supabase_url, settings.supabase_service_key)

    async def register(self, payload: RegisterRequest) -> AuthTokens:  # pragma: no cover - requires Supabase
        response = self._client.auth.sign_up({"email": payload.email, "password": payload.password, "data": {"full_name": payload.full_name}})
        if response.user is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unable to register user")
        await self._client.table("companies").insert({"name": payload.company_name}).execute()
        auth_user = response.user
        user = User(id=auth_user.id, email=auth_user.email or payload.email, company_id="", role="admin", full_name=payload.full_name, is_active=True)
        return AuthTokens(access_token=response.session.access_token, refresh_token=response.session.refresh_token, user=user)

    async def login(self, payload: LoginRequest) -> AuthTokens:  # pragma: no cover - requires Supabase
        response = self._client.auth.sign_in_with_password({"email": payload.email, "password": payload.password})
        if response.user is None or response.session is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        metadata = response.user.user_metadata or {}
        user = User(
            id=response.user.id,
            email=response.user.email or payload.email,
            company_id=metadata.get("company_id", ""),
            role=metadata.get("role", "sales"),
            full_name=metadata.get("full_name"),
            is_active=True,
        )
        return AuthTokens(access_token=response.session.access_token, refresh_token=response.session.refresh_token, user=user)

    async def refresh(self, refresh_token: str) -> AuthTokens:  # pragma: no cover - requires Supabase
        response = self._client.auth.refresh_session({"refresh_token": refresh_token})
        if response.user is None or response.session is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
        metadata = response.user.user_metadata or {}
        user = User(
            id=response.user.id,
            email=response.user.email or "",
            company_id=metadata.get("company_id", ""),
            role=metadata.get("role", "sales"),
            full_name=metadata.get("full_name"),
            is_active=True,
        )
        return AuthTokens(access_token=response.session.access_token, refresh_token=response.session.refresh_token, user=user)
