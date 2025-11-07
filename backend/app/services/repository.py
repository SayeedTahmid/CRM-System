from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, Iterable, MutableMapping
from uuid import uuid4

from loguru import logger
from supabase import Client, create_client

from ..core.config import settings


class BaseRepository:
    """Abstract repository interface for persistence operations."""

    async def list(self, table: str, filters: Dict[str, Any] | None = None) -> list[dict]:  # pragma: no cover - interface
        raise NotImplementedError

    async def get(self, table: str, record_id: str) -> dict | None:  # pragma: no cover - interface
        raise NotImplementedError

    async def create(self, table: str, data: Dict[str, Any]) -> dict:  # pragma: no cover - interface
        raise NotImplementedError

    async def update(self, table: str, record_id: str, data: Dict[str, Any]) -> dict:  # pragma: no cover - interface
        raise NotImplementedError

    async def delete(self, table: str, record_id: str) -> None:  # pragma: no cover - interface
        raise NotImplementedError


class SupabaseRepository(BaseRepository):
    """Repository backed by Supabase REST queries."""

    def __init__(self, client: Client | None = None) -> None:
        self._client = client or create_client(settings.supabase_url, settings.supabase_service_key)

    async def list(self, table: str, filters: Dict[str, Any] | None = None) -> list[dict]:
        def _execute() -> list[dict]:
            query = self._client.table(table).select("*")
            for key, value in (filters or {}).items():
                if isinstance(value, Iterable) and not isinstance(value, (str, bytes)):
                    query = query.in_(key, list(value))
                else:
                    query = query.eq(key, value)
            response = query.execute()
            return response.data or []

        return await asyncio.to_thread(_execute)

    async def get(self, table: str, record_id: str) -> dict | None:
        items = await self.list(table, {"id": record_id})
        return items[0] if items else None

    async def create(self, table: str, data: Dict[str, Any]) -> dict:
        def _execute() -> dict:
            response = self._client.table(table).insert(data).execute()
            if not response.data:
                raise RuntimeError("Supabase insert failed")
            return response.data[0]

        return await asyncio.to_thread(_execute)

    async def update(self, table: str, record_id: str, data: Dict[str, Any]) -> dict:
        def _execute() -> dict:
            response = self._client.table(table).update(data).eq("id", record_id).execute()
            if not response.data:
                raise RuntimeError("Supabase update failed")
            return response.data[0]

        return await asyncio.to_thread(_execute)

    async def delete(self, table: str, record_id: str) -> None:
        def _execute() -> None:
            self._client.table(table).delete().eq("id", record_id).execute()

        await asyncio.to_thread(_execute)


@dataclass
class InMemoryRepository(BaseRepository):
    """Simple repository used for unit tests and local development."""

    tables: MutableMapping[str, Dict[str, Dict[str, Any]]] = field(default_factory=dict)

    def _table(self, name: str) -> Dict[str, Dict[str, Any]]:
        return self.tables.setdefault(name, {})

    async def list(self, table: str, filters: Dict[str, Any] | None = None) -> list[dict]:
        records = list(self._table(table).values())
        if not filters:
            return records

        result = []
        for record in records:
            matches = True
            for key, value in filters.items():
                if isinstance(value, Iterable) and not isinstance(value, (str, bytes)):
                    if record.get(key) not in value:
                        matches = False
                        break
                elif record.get(key) != value:
                    matches = False
                    break
            if matches:
                result.append(record)
        return result

    async def get(self, table: str, record_id: str) -> dict | None:
        return self._table(table).get(record_id)

    async def create(self, table: str, data: Dict[str, Any]) -> dict:
        identifier = data.get("id", str(uuid4()))
        now = datetime.utcnow().isoformat()
        record = {**data, "id": identifier, "created_at": data.get("created_at") or now, "updated_at": data.get("updated_at") or now}
        self._table(table)[identifier] = record
        logger.debug("Created %s/%s", table, identifier)
        return record

    async def update(self, table: str, record_id: str, data: Dict[str, Any]) -> dict:
        table_data = self._table(table)
        if record_id not in table_data:
            raise KeyError(f"Record {record_id} not found in {table}")
        now = datetime.utcnow().isoformat()
        table_data[record_id].update(data)
        table_data[record_id]["updated_at"] = now
        logger.debug("Updated %s/%s", table, record_id)
        return table_data[record_id]

    async def delete(self, table: str, record_id: str) -> None:
        self._table(table).pop(record_id, None)
        logger.debug("Deleted %s/%s", table, record_id)

    def reset(self) -> None:
        self.tables.clear()
