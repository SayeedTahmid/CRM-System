from fastapi import APIRouter, Depends

from ...core.security import get_current_user
from ...dependencies import get_auth_service
from ...models.schemas import AuthTokens, LoginRequest, RegisterRequest, RefreshRequest, UserContext
from ...services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=AuthTokens)
async def register(payload: RegisterRequest, auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.register(payload)


@router.post("/login", response_model=AuthTokens)
async def login(payload: LoginRequest, auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.login(payload)


@router.post("/refresh", response_model=AuthTokens)
async def refresh(payload: RefreshRequest, auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.refresh(payload.refresh_token)


@router.get("/me", response_model=UserContext)
async def me(user: UserContext = Depends(get_current_user)):
    return user
