"""Records every data call to Databricks made while a question is answered, wherever in the code it is made, and every
lookup served from the cache instead.

Events (stored with the other message events):
- `databricks_query`  one real query: start, end, duration, SQL, rows, failed or not
- `lookup_cache_hit`  a lookup answered from the cache (no query)
The event's agent is who asked, e.g. "sql_agent:run_sql" or "fast_path:resolve_entity". Work done outside a question
(warm-up, summary job) is not recorded.
"""
from __future__ import annotations

from contextlib import contextmanager
from contextvars import ContextVar
from datetime import datetime
from typing import Iterator

from .events import utcnow
from .tracer import Tracer, preview

QUERY_EVENT = "databricks_query"
CACHE_EVENT = "lookup_cache_hit"

# set per question; asyncio tasks started for the question inherit them
_tracer: ContextVar[Tracer | None] = ContextVar("finchat_tracer", default=None)
_caller: ContextVar[str] = ContextVar("finchat_caller", default="data")


@contextmanager
def traced_question(tracer: Tracer) -> Iterator[None]:
    token = _tracer.set(tracer)
    try:
        yield
    finally:
        _tracer.reset(token)


@contextmanager
def called_by(name: str) -> Iterator[None]:
    token = _caller.set(name)
    try:
        yield
    finally:
        _caller.reset(token)


async def record_query(sql: str, started: datetime, outcome: str, *, failed: bool = False) -> None:
    tracer = _tracer.get()
    if tracer is not None:
        await tracer.emit("tool_call", agent=_caller.get(), name=QUERY_EVENT, status="error" if failed else "ok",
                          started_at=started, ended_at=utcnow(),
                          payload={"input": preview(sql, 2000), "output": preview(outcome, 300)})


async def record_cache_hit(what: str) -> None:
    tracer = _tracer.get()
    if tracer is not None:
        now = utcnow()
        await tracer.emit("tool_call", agent=_caller.get(), name=CACHE_EVENT, started_at=now, ended_at=now,
                          payload={"input": preview(what, 500), "output": "served from the cache, no query"})
