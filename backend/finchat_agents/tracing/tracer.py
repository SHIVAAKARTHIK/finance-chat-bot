"""Tracer: stamps run/message ids on events and fans them out to sinks. Never raises into the answer path."""
from __future__ import annotations

import logging
import uuid
from datetime import datetime
from typing import Any

from .events import EventType, TraceEvent, utcnow
from .sinks import TraceSink

log = logging.getLogger(__name__)

PREVIEW_CHARS = 1000


def preview(value: Any, limit: int = PREVIEW_CHARS) -> Any:
    """Shorten long strings for payloads; leave small values as they are."""
    if isinstance(value, str) and len(value) > limit:
        return value[:limit] + f"... [{len(value) - limit} more chars]"
    return value


class Tracer:
    def __init__(self, sinks: list[TraceSink] | None = None, *, run_id: str | None = None, message_id: str | None = None):
        self.sinks = list(sinks or [])
        self.run_id = run_id or str(uuid.uuid4())
        self.message_id = message_id

    async def emit(
        self,
        type: EventType,
        *,
        agent: str,
        step: int = 0,
        name: str | None = None,
        status: str = "ok",
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        input_tokens: int = 0,
        output_tokens: int = 0,
        cache_read_tokens: int = 0,
        cache_write_tokens: int = 0,
        payload: dict[str, Any] | None = None,
    ) -> TraceEvent:
        started = started_at or utcnow()
        duration = (ended_at - started).total_seconds() * 1000 if ended_at else None
        event = TraceEvent(
            run_id=self.run_id,
            message_id=self.message_id,
            agent=agent,
            step=step,
            type=type,
            name=name,
            status=status,  # type: ignore[arg-type]
            started_at=started,
            ended_at=ended_at,
            duration_ms=round(duration, 1) if duration is not None else None,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            cache_read_tokens=cache_read_tokens,
            cache_write_tokens=cache_write_tokens,
            payload=payload or {},
        )
        for sink in self.sinks:
            try:
                await sink.write(event)
            except Exception:  # a broken sink must not break the answer
                log.exception("trace sink %s failed", sink.__class__.__name__)
        return event
