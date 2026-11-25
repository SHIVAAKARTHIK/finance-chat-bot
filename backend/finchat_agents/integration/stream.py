"""SSE stream in the UI's existing format: `status {"stage"}` while working, `delta {"text"}` pieces of the answer,
then `complete <ui body>`, or `error {"message", "status_code"}`. No named end event: the stream ends after
`complete`/`error` (as the UI expects).

Progress stages come from v3 trace events (only the stage names the UI already knows). While nothing changes, the
current stage is re-sent every `heartbeat_s` seconds so the Nginx 120 s read timeout never fires on a long question.
"""
from __future__ import annotations

import asyncio
import json
import logging
import time
from typing import Any, AsyncIterator, Awaitable, Callable

from ..api.service import ChatService, Identity
from ..tracing.events import TraceEvent
from .ui_contract import chunk_text, to_ui_body

log = logging.getLogger(__name__)

HEARTBEAT_S = 15.0
EXPLORATION_TOOLS = {"search_tables", "describe_table", "get_join_path", "get_column_values", "get_glossary",
                     "resolve_period", "resolve_entity"}
AGENT_STAGE = {"catalog_agent": "exploration", "knowledge_agent": "exploration", "sql_agent": "sql",
               "fast_path": "sql", "analyst_agent": "sql", "action_agent": "results", "answer_writer": "answer"}


def sse(event: str, data: Any) -> str:
    return f"event: {event}\ndata: {json.dumps(data, default=str, ensure_ascii=False)}\n\n"


def stage_of(event: TraceEvent) -> str | None:
    """Map one v3 trace event to a UI progress stage (None = no change)."""
    if event.type == "route":
        return "intent"
    if event.type == "agent_start":
        return AGENT_STAGE.get(event.agent or "")
    if event.type == "tool_call":
        if event.name == "run_sql":
            return "results" if event.status == "ok" else "database"
        if event.name in EXPLORATION_TOOLS:
            return "exploration"
    return None


class StageSink:
    """Trace sink that queues stage changes (never payloads, SQL or names)."""

    def __init__(self) -> None:
        self.queue: asyncio.Queue[str] = asyncio.Queue()
        self.current = "processing"

    async def write(self, event: TraceEvent) -> None:
        stage = stage_of(event)
        if event.type == "tool_call" and event.name == "run_sql" and stage == "results" and self.current != "database":
            await self._set("database")  # the UI shows database before results
        if stage:
            await self._set(stage)

    async def _set(self, stage: str) -> None:
        if stage != self.current:
            self.current = stage
            await self.queue.put(stage)


async def stream_chat(
    service: ChatService,
    *,
    query: str,
    identity: Identity,
    display_query: str | None = None,
    conversation_id: str | None,
    session_id: str | None,
    is_disconnected: Callable[[], Awaitable[bool]] | None = None,
    heartbeat_s: float = HEARTBEAT_S,
) -> AsyncIterator[str]:
    sink = StageSink()
    started = time.monotonic()
    yield sse("status", {"stage": "processing"})
    task = asyncio.create_task(service.chat(query, identity, conversation_id=conversation_id, extra_sinks=[sink]))
    last_sent = time.monotonic()
    try:
        while not task.done() or not sink.queue.empty():
            try:
                stage = await asyncio.wait_for(sink.queue.get(), timeout=0.25)
                yield sse("status", {"stage": stage})
                last_sent = time.monotonic()
            except asyncio.TimeoutError:
                if is_disconnected is not None and await is_disconnected():
                    task.cancel()
                    return
                if time.monotonic() - last_sent >= heartbeat_s:
                    yield sse("status", {"stage": sink.current})  # keep-alive the UI already understands
                    last_sent = time.monotonic()
        try:
            env = await task
        except Exception as exc:  # noqa: BLE001 - the UI gets a generic error; details go to the log
            log.exception("finance chat failed: %s", type(exc).__name__)
            yield sse("error", {"message": "The finance assistant could not answer this question. Please try again.",
                                "status_code": 500})
            return
        body = to_ui_body(env, query=display_query or query, user_id=identity.user_id, session_id=session_id,
                          total_ms=(time.monotonic() - started) * 1000, domain_labels=service.access.domains)
        if env.status == "clarification":
            yield sse("status", {"stage": "clarification"})
        elif sink.current != "answer":
            yield sse("status", {"stage": "answer"})
        for piece in chunk_text(body["answer"]):
            yield sse("delta", {"text": piece})
        yield sse("complete", body)
    finally:
        if not task.done():
            task.cancel()
