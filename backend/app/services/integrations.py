from __future__ import annotations

from datetime import datetime
from typing import Any, Dict

import httpx
from loguru import logger

from ..core.config import settings


class CalendarIntegration:
    """Integration helper for pushing CRM activities to external calendars."""

    def __init__(self, client: httpx.AsyncClient | None = None) -> None:
        self._client = client or httpx.AsyncClient(timeout=10)

    async def push_event(self, payload: Dict[str, Any]) -> None:
        if not settings.calendar_webhook_url:
            logger.debug("Calendar webhook URL not set; skipping push")
            return
        try:  # pragma: no cover - network
            await self._client.post(settings.calendar_webhook_url, json=payload)
        except Exception as exc:
            logger.exception("Failed to push calendar event: %s", exc)


async def build_calendar_payload(activity: dict) -> Dict[str, Any]:
    return {
        "summary": activity.get("subject"),
        "description": activity.get("description"),
        "start": activity.get("due_date"),
        "metadata": {"id": activity.get("id"), "type": activity.get("type")},
    }
