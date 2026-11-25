"""Trace event model. One event per LLM call, tool call and agent start/end.

Maps to lakehouse_mvpai.aiops.finance_chat_message_events in task 05. Payloads hold previews, never secrets.
"""
from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Any, Literal

from pydantic import BaseModel, Field

EventType = Literal["agent_start", "agent_end", "llm_call", "tool_call", "budget_stop", "error", "route", "answer", "plan"]


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class TraceEvent(BaseModel):
    event_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    run_id: str
    message_id: str | None = None
    agent: str
    step: int = 0
    type: EventType
    name: str | None = None  # model id for llm_call, tool name for tool_call
    status: Literal["ok", "error"] = "ok"
    started_at: datetime = Field(default_factory=utcnow)
    ended_at: datetime | None = None
    duration_ms: float | None = None
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_tokens: int = 0
    cache_write_tokens: int = 0
    payload: dict[str, Any] = Field(default_factory=dict)
