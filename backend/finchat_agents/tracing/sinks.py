"""Trace sinks. JSON-lines file sink now; the aiops table sink comes in task 05."""
from __future__ import annotations

import asyncio
from pathlib import Path
from typing import Protocol

from .events import TraceEvent


class TraceSink(Protocol):
    async def write(self, event: TraceEvent) -> None: ...


class MemorySink:
    """Keeps events in a list (tests, streaming later)."""

    def __init__(self) -> None:
        self.events: list[TraceEvent] = []

    async def write(self, event: TraceEvent) -> None:
        self.events.append(event)


class JsonlFileSink:
    """Appends one JSON object per line. Safe for concurrent writers within one event loop."""

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self._lock = asyncio.Lock()

    async def write(self, event: TraceEvent) -> None:
        line = event.model_dump_json() + "\n"
        async with self._lock:
            await asyncio.to_thread(self._append, line)

    def _append(self, line: str) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(line)
