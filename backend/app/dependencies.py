from __future__ import annotations

from functools import lru_cache

from fastapi import Depends

from .core.config import settings
from .services.auth_service import InMemoryAuthService, SupabaseAuthService
from .services.crm_service import CRMService
from .services.email import ConsoleEmailService
from .services.integrations import CalendarIntegration
from .services.repository import InMemoryRepository, SupabaseRepository, BaseRepository


@lru_cache(maxsize=1)
def get_repository() -> BaseRepository:
    if settings.testing:
        return InMemoryRepository()
    return SupabaseRepository()


def get_email_service():
    return ConsoleEmailService()


def get_calendar_integration():
    return CalendarIntegration()


def get_crm_service(
    repository: BaseRepository = Depends(get_repository),
    email_service=Depends(get_email_service),
    calendar_integration=Depends(get_calendar_integration),
) -> CRMService:
    return CRMService(repository, email_service, calendar_integration)


def get_auth_service(repository: BaseRepository = Depends(get_repository)):
    if settings.testing:
        return InMemoryAuthService(repository)
    return SupabaseAuthService()
