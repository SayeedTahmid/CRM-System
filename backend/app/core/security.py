from datetime import datetime, timedelta
from typing import Iterable

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt

from ..core.config import settings
from ..models.schemas import Role, UserContext

security_scheme = HTTPBearer(auto_error=False)


def create_access_token(subject: dict, expires_delta: timedelta | None = None) -> str:
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.access_token_expire_minutes))
    to_encode = subject.copy()
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.supabase_jwt_secret, algorithm="HS256")


def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, settings.supabase_jwt_secret, algorithms=["HS256"])
    except JWTError as exc:  # pragma: no cover - defensive
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token") from exc


async def get_current_user(credentials: HTTPAuthorizationCredentials | None = Depends(security_scheme)) -> UserContext:
    if not credentials:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

    payload = decode_token(credentials.credentials)
    try:
        return UserContext.model_validate(payload)
    except Exception as exc:  # pragma: no cover - defensive
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid auth payload") from exc


def require_roles(*allowed_roles: Iterable[Role]):
    allowed = {role.value if isinstance(role, Role) else role for role in allowed_roles}

    async def dependency(user: UserContext = Depends(get_current_user)) -> UserContext:
        if allowed and user.role not in allowed:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")
        return user

    return dependency
