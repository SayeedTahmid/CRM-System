from functools import lru_cache
from typing import List

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    project_name: str = "Supabase CRM"
    api_v1_prefix: str = "/api"
    supabase_url: str = ""
    supabase_service_key: str = ""
    supabase_anon_key: str = ""
    supabase_jwt_secret: str = "change-me"
    access_token_expire_minutes: int = 60
    refresh_token_expire_minutes: int = 60 * 24 * 7
    allowed_origins: List[AnyHttpUrl] | List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]
    environment: str = "development"
    testing: bool = False
    email_from: str = "noreply@crm.local"
    email_provider_url: str = ""
    calendar_webhook_url: str = ""

    class Config:
        env_file = ".env"
        env_prefix = "CRM_"
        case_sensitive = False


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Cached settings instance to avoid re-parsing environment variables."""

    return Settings()


settings = get_settings()
