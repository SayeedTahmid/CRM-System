from __future__ import annotations

import json
from typing import Iterable

from loguru import logger

from ..core.config import settings
from ..models.schemas import Activity, ActivityNotification


class EmailService:
    """Abstract email service."""

    async def send_activity_notification(self, notification: ActivityNotification) -> None:  # pragma: no cover - interface
        raise NotImplementedError


class ConsoleEmailService(EmailService):
    """Simple email service that logs outgoing emails for development/testing."""

    async def send_activity_notification(self, notification: ActivityNotification) -> None:
        logger.info("Email notification to %s about activity %s", notification.recipients, notification.activity.id)
        logger.debug(json.dumps(notification.model_dump(), default=str))


class ExternalEmailService(EmailService):
    """Email service integrating with an external HTTP provider."""

    def __init__(self, http_client) -> None:
        self._http_client = http_client

    async def send_activity_notification(self, notification: ActivityNotification) -> None:  # pragma: no cover - network
        payload = notification.model_dump()
        if not settings.email_provider_url:
            logger.warning("Email provider URL not configured; skipping notification")
            return
        await self._http_client.post(settings.email_provider_url, json=payload)
