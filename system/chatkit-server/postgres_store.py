"""PostgreSQL-backed ChatKit store for production.

Replaces InMemoryChatKitStore so history survives restarts and
multiple replicas share state. Requires the pgvector extension for
embeddings (not used directly by ChatKit but needed for ksor).
"""

import json
import os
import uuid
from contextlib import asynccontextmanager
from datetime import datetime
from typing import Any

import asyncpg
from chatkit.store import NotFoundError, Store
from chatkit.types import (
    Attachment,
    FileAttachment,
    ImageAttachment,
    Page,
    ThreadItem,
    ThreadMetadata,
    ThreadStatus,
    ActiveStatus,
)


# Database connection pool - initialized on first use
_pool: asyncpg.Pool | None = None


async def get_pool() -> asyncpg.Pool:
    """Get or create the database connection pool."""
    global _pool
    if _pool is None:
        dsn = os.environ.get("KSOR_DB_URL") or os.environ.get("DATABASE_URL")
        if not dsn:
            raise RuntimeError(
                "KSOR_DB_URL or DATABASE_URL environment variable not set"
            )
        _pool = await asyncpg.create_pool(dsn, min_size=1, max_size=10)
        await _init_schema(_pool)
    return _pool


async def _init_schema(pool: asyncpg.Pool) -> None:
    """Create tables if they don't exist."""
    async with pool.acquire() as conn:
        # Threads table
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS chatkit_threads (
                id TEXT PRIMARY KEY,
                title TEXT,
                created_at TIMESTAMPTZ NOT NULL,
                status JSONB NOT NULL DEFAULT '{"active": {}}',
                metadata JSONB NOT NULL DEFAULT '{}'
            )
        """)
        
        # Thread items table
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS chatkit_items (
                id TEXT PRIMARY KEY,
                thread_id TEXT NOT NULL REFERENCES chatkit_threads(id) ON DELETE CASCADE,
                type TEXT NOT NULL,
                content JSONB NOT NULL DEFAULT '{}',
                created_at TIMESTAMPTZ NOT NULL,
                metadata JSONB NOT NULL DEFAULT '{}'
            )
        """)
        
        # Attachments table
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS chatkit_attachments (
                id TEXT PRIMARY KEY,
                thread_id TEXT NOT NULL REFERENCES chatkit_threads(id) ON DELETE CASCADE,
                name TEXT NOT NULL,
                mime_type TEXT NOT NULL,
                type TEXT NOT NULL,  -- 'file' or 'image'
                metadata JSONB NOT NULL DEFAULT '{}'
            )
        """)
        
        # Indexes for common queries
        await conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_chatkit_items_thread_id 
            ON chatkit_items(thread_id)
        """)
        await conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_chatkit_items_created_at 
            ON chatkit_items(created_at)
        """)
        await conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_chatkit_threads_created_at 
            ON chatkit_threads(created_at)
        """)


def _serialize_thread_status(status: ThreadStatus) -> dict[str, Any]:
    """Serialize ThreadStatus to JSON."""
    if hasattr(status, 'model_dump'):
        return status.model_dump(mode="json")
    return {"active": {}}


def _deserialize_thread_status(data: dict[str, Any]) -> ThreadStatus:
    """Deserialize ThreadStatus from JSON."""
    # For simplicity, just return ActiveStatus
    # In production you might want to handle other statuses
    return ActiveStatus()


def _serialize_thread(thread: ThreadMetadata) -> dict[str, Any]:
    """Serialize ThreadMetadata to dict for database."""
    return {
        "id": thread.id,
        "title": thread.title,
        "created_at": thread.created_at,
        "status": _serialize_thread_status(thread.status),
        "metadata": thread.metadata,
    }


def _deserialize_thread(row: asyncpg.Record) -> ThreadMetadata:
    """Deserialize ThreadMetadata from database row.

    asyncpg has no type codec registered for jsonb here, so jsonb columns
    come back as raw JSON text, not parsed dicts — json.loads() them before
    use (matches the write side, which deliberately writes json.dumps()
    strings without a codec too).
    """
    return ThreadMetadata(
        id=row["id"],
        title=row["title"],
        created_at=row["created_at"],
        status=_deserialize_thread_status(json.loads(row["status"])),
        metadata=json.loads(row["metadata"]),
    )


def _serialize_item(item: ThreadItem) -> dict[str, Any]:
    """Serialize ThreadItem to dict for database."""
    # mode="json" is required, not cosmetic: every ThreadItem carries a
    # `created_at: datetime`, and plain model_dump() leaves that as a raw
    # datetime object, which json.dumps() below rejects with a TypeError on
    # every single save. mode="json" coerces datetimes/enums to their
    # JSON-safe (str) form first.
    if hasattr(item, 'model_dump'):
        data = item.model_dump(mode="json")
    else:
        data = dict(item)
    return {
        "id": item.id,
        "thread_id": getattr(item, 'thread_id', None),  # May not be on the item itself
        "type": item.type,
        "content": data,
        "created_at": getattr(item, 'created_at', datetime.now()),
        "metadata": getattr(item, 'metadata', {}),
    }


def _deserialize_item(row: asyncpg.Record) -> ThreadItem:
    """Deserialize ThreadItem from database row."""
    # Reconstruct the item from the content JSON. row["content"] is raw JSON
    # text (no asyncpg codec registered for jsonb) — parse it before
    # treating it as a dict, or the item-assignment below raises TypeError.
    content = json.loads(row["content"])
    content["id"] = row["id"]
    content["created_at"] = content.get("created_at", row["created_at"].isoformat())
    content["metadata"] = content.get("metadata") or json.loads(row["metadata"])
    
    item_type = row["type"]
    if item_type == "user_message":
        from chatkit.types import UserMessageItem
        return UserMessageItem(**content)
    elif item_type == "assistant_message":
        from chatkit.types import AssistantMessageItem
        return AssistantMessageItem(**content)
    elif item_type == "client_tool_call":
        from chatkit.types import ClientToolCallItem
        return ClientToolCallItem(**content)
    elif item_type == "widget":
        from chatkit.types import WidgetItem
        return WidgetItem(**content)
    elif item_type == "workflow":
        from chatkit.types import WorkflowItem
        return WorkflowItem(**content)
    elif item_type == "task":
        from chatkit.types import TaskItem
        return TaskItem(**content)
    elif item_type == "hidden_context":
        from chatkit.types import HiddenContextItem
        return HiddenContextItem(**content)
    elif item_type == "sdk_hidden_context":
        from chatkit.types import SDKHiddenContextItem
        return SDKHiddenContextItem(**content)
    elif item_type == "end_of_turn":
        from chatkit.types import EndOfTurnItem
        return EndOfTurnItem(**content)
    else:
        # Fallback: try to construct a generic ThreadItem
        # This shouldn't happen with known types
        raise NotFoundError(f"Unknown item type: {item_type}")


def _serialize_attachment(attachment: Attachment) -> dict[str, Any]:
    """Serialize Attachment to dict for database."""
    if isinstance(attachment, FileAttachment):
        return {
            "id": attachment.id,
            "thread_id": attachment.metadata.get("thread_id") if attachment.metadata else None,
            "name": attachment.name,
            "mime_type": attachment.mime_type,
            "type": "file",
            "metadata": attachment.metadata or {},
        }
    elif isinstance(attachment, ImageAttachment):
        return {
            "id": attachment.id,
            "thread_id": attachment.metadata.get("thread_id") if attachment.metadata else None,
            "name": attachment.name,
            "mime_type": attachment.mime_type,
            "type": "image",
            "metadata": attachment.metadata or {},
        }
    else:
        raise ValueError(f"Unknown attachment type: {type(attachment)}")


def _deserialize_attachment(row: asyncpg.Record) -> Attachment:
    """Deserialize Attachment from database row. row["metadata"] is raw JSON
    text (no asyncpg jsonb codec registered) — json.loads() before use."""
    if row["type"] == "file":
        return FileAttachment(
            id=row["id"],
            name=row["name"],
            mime_type=row["mime_type"],
            metadata=json.loads(row["metadata"]),
        )
    elif row["type"] == "image":
        return ImageAttachment(
            id=row["id"],
            name=row["name"],
            mime_type=row["mime_type"],
            metadata=json.loads(row["metadata"]),
        )
    else:
        raise ValueError(f"Unknown attachment type: {row['type']}")


class PostgresChatKitStore(Store[dict]):
    """PostgreSQL-backed ChatKit store implementation."""
    
    def __init__(self) -> None:
        self._pool: asyncpg.Pool | None = None
    
    async def _get_pool(self) -> asyncpg.Pool:
        if self._pool is None:
            self._pool = await get_pool()
        return self._pool
    
    async def load_thread(self, thread_id: str, context: dict) -> ThreadMetadata:
        pool = await self._get_pool()
        async with pool.acquire() as conn:
            row = await conn.fetchrow(
                "SELECT * FROM chatkit_threads WHERE id = $1",
                thread_id
            )
            if not row:
                raise NotFoundError(f"Thread {thread_id} not found")
            return _deserialize_thread(row)
    
    async def save_thread(self, thread: ThreadMetadata, context: dict) -> None:
        pool = await self._get_pool()
        async with pool.acquire() as conn:
            data = _serialize_thread(thread)
            await conn.execute("""
                INSERT INTO chatkit_threads (id, title, created_at, status, metadata)
                VALUES ($1, $2, $3, $4, $5)
                ON CONFLICT (id) DO UPDATE SET
                    title = EXCLUDED.title,
                    status = EXCLUDED.status,
                    metadata = EXCLUDED.metadata
            """, data["id"], data["title"], data["created_at"], 
                json.dumps(data["status"]), json.dumps(data["metadata"]))
    
    async def load_threads(
        self, limit: int, after: str | None, order: str, context: dict
    ) -> Page[ThreadMetadata]:
        pool = await self._get_pool()
        async with pool.acquire() as conn:
            # Build query with cursor-based pagination
            if order == "desc":
                order_clause = "created_at DESC, id DESC"
                if after:
                    cursor_condition = "AND (created_at, id) < (SELECT created_at, id FROM chatkit_threads WHERE id = $3)"
                else:
                    cursor_condition = ""
            else:
                order_clause = "created_at ASC, id ASC"
                if after:
                    cursor_condition = "AND (created_at, id) > (SELECT created_at, id FROM chatkit_threads WHERE id = $3)"
                else:
                    cursor_condition = ""
            
            query = f"""
                SELECT * FROM chatkit_threads
                WHERE 1=1 {cursor_condition}
                ORDER BY {order_clause}
                LIMIT $1
            """
            
            params = [limit + 1]  # Fetch one extra to check has_more
            if after:
                params.append(after)
            
            rows = await conn.fetch(query, *params)
            
            has_more = len(rows) > limit
            if has_more:
                rows = rows[:limit]
            
            data = [_deserialize_thread(row) for row in rows]
            next_after = data[-1].id if has_more and data else None
            
            return Page(data=data, has_more=has_more, after=next_after)
    
    async def load_thread_items(
        self, thread_id: str, after: str | None, limit: int, order: str, context: dict
    ) -> Page[ThreadItem]:
        pool = await self._get_pool()
        async with pool.acquire() as conn:
            if order == "desc":
                order_clause = "created_at DESC, id DESC"
                if after:
                    cursor_condition = "AND (created_at, id) < (SELECT created_at, id FROM chatkit_items WHERE id = $3)"
                else:
                    cursor_condition = ""
            else:
                order_clause = "created_at ASC, id ASC"
                if after:
                    cursor_condition = "AND (created_at, id) > (SELECT created_at, id FROM chatkit_items WHERE id = $3)"
                else:
                    cursor_condition = ""
            
            query = f"""
                SELECT * FROM chatkit_items
                WHERE thread_id = $1 {cursor_condition}
                ORDER BY {order_clause}
                LIMIT $2
            """
            
            params = [thread_id, limit + 1]
            if after:
                params.append(after)
            
            rows = await conn.fetch(query, *params)
            
            has_more = len(rows) > limit
            if has_more:
                rows = rows[:limit]
            
            data = [_deserialize_item(row) for row in rows]
            next_after = data[-1].id if has_more and data else None
            
            return Page(data=data, has_more=has_more, after=next_after)
    
    async def add_thread_item(self, thread_id: str, item: ThreadItem, context: dict) -> None:
        await self.save_item(thread_id, item, context)
    
    async def save_item(self, thread_id: str, item: ThreadItem, context: dict) -> None:
        pool = await self._get_pool()
        async with pool.acquire() as conn:
            # Ensure thread exists
            await conn.execute(
                "INSERT INTO chatkit_threads (id, created_at) VALUES ($1, $2) ON CONFLICT DO NOTHING",
                thread_id, datetime.now()
            )
            
            data = _serialize_item(item)
            data["thread_id"] = thread_id
            await conn.execute("""
                INSERT INTO chatkit_items (id, thread_id, type, content, created_at, metadata)
                VALUES ($1, $2, $3, $4, $5, $6)
                ON CONFLICT (id) DO UPDATE SET
                    content = EXCLUDED.content,
                    metadata = EXCLUDED.metadata
            """, data["id"], data["thread_id"], data["type"],
                json.dumps(data["content"]), data["created_at"],
                json.dumps(data["metadata"]))
    
    async def load_item(self, thread_id: str, item_id: str, context: dict) -> ThreadItem:
        pool = await self._get_pool()
        async with pool.acquire() as conn:
            row = await conn.fetchrow(
                "SELECT * FROM chatkit_items WHERE id = $1 AND thread_id = $2",
                item_id, thread_id
            )
            if not row:
                raise NotFoundError(f"Item {item_id} not found in thread {thread_id}")
            return _deserialize_item(row)
    
    async def delete_thread(self, thread_id: str, context: dict) -> None:
        pool = await self._get_pool()
        async with pool.acquire() as conn:
            await conn.execute("DELETE FROM chatkit_threads WHERE id = $1", thread_id)
            # Items and attachments cascade delete via FK
    
    async def delete_thread_item(self, thread_id: str, item_id: str, context: dict) -> None:
        pool = await self._get_pool()
        async with pool.acquire() as conn:
            await conn.execute(
                "DELETE FROM chatkit_items WHERE id = $1 AND thread_id = $2",
                item_id, thread_id
            )
    
    # Attachment methods
    async def save_attachment(self, attachment: Attachment, context: dict) -> None:
        pool = await self._get_pool()
        async with pool.acquire() as conn:
            data = _serialize_attachment(attachment)
            await conn.execute("""
                INSERT INTO chatkit_attachments (id, thread_id, name, mime_type, type, metadata)
                VALUES ($1, $2, $3, $4, $5, $6)
                ON CONFLICT (id) DO UPDATE SET
                    name = EXCLUDED.name,
                    mime_type = EXCLUDED.mime_type,
                    metadata = EXCLUDED.metadata
            """, data["id"], data["thread_id"], data["name"], 
                data["mime_type"], data["type"], json.dumps(data["metadata"]))
    
    async def load_attachment(self, attachment_id: str, context: dict) -> Attachment:
        pool = await self._get_pool()
        async with pool.acquire() as conn:
            row = await conn.fetchrow(
                "SELECT * FROM chatkit_attachments WHERE id = $1",
                attachment_id
            )
            if not row:
                raise NotFoundError(f"Attachment {attachment_id} not found")
            return _deserialize_attachment(row)
    
    async def delete_attachment(self, attachment_id: str, context: dict) -> None:
        pool = await self._get_pool()
        async with pool.acquire() as conn:
            await conn.execute("DELETE FROM chatkit_attachments WHERE id = $1", attachment_id)
    
    async def close(self) -> None:
        """Close the connection pool."""
        global _pool
        if _pool:
            await _pool.close()
            _pool = None
            self._pool = None