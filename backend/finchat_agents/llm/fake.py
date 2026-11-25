"""Scripted fake provider for unit tests (no network)."""
from __future__ import annotations

import asyncio
import itertools
from typing import Any, Callable, Union

from .types import LLMResult, Message, ToolCall, ToolSpec, Usage

_ids = itertools.count(1)

Step = Union[LLMResult, Exception, Callable[[dict[str, Any]], Union[LLMResult, Exception]]]


def text(t: str, *, input_tokens: int = 10, output_tokens: int = 5) -> LLMResult:
    return LLMResult(text=t, usage=Usage(input_tokens=input_tokens, output_tokens=output_tokens), stop_reason="end_turn")


def tool_call(name: str, args: dict[str, Any] | None = None, *, call_id: str | None = None, say: str = "") -> LLMResult:
    return tool_calls([(name, args or {})], ids=[call_id] if call_id else None, say=say)


def tool_calls(
    calls: list[tuple[str, dict[str, Any]]], *, ids: list[str] | None = None, say: str = ""
) -> LLMResult:
    ids = ids or [f"call_{next(_ids)}" for _ in calls]
    return LLMResult(
        text=say,
        tool_calls=[ToolCall(id=i, name=n, input=a) for i, (n, a) in zip(ids, calls)],
        usage=Usage(input_tokens=10, output_tokens=5),
        stop_reason="tool_use",
    )


class FakeProvider:
    """Returns scripted results in order. A step may be an LLMResult, an Exception (raised), or a callable that
    receives the call record and returns either. `calls` records every request for assertions."""

    name = "fake"

    def __init__(self, script: list[Step], *, delay: float = 0.0):
        self.script = list(script)
        self.delay = delay
        self.calls: list[dict[str, Any]] = []

    async def complete(
        self,
        system: str,
        messages: list[Message],
        tools: list[ToolSpec],
        model: str,
        max_tokens: int,
        temperature: float,
    ) -> LLMResult:
        record = {
            "system": system,
            "messages": [m.model_copy(deep=True) for m in messages],
            "tools": [t.name for t in tools],
            "model": model,
        }
        self.calls.append(record)
        if self.delay:
            await asyncio.sleep(self.delay)
        if not self.script:
            raise AssertionError(f"FakeProvider script exhausted after {len(self.calls) - 1} calls")
        step = self.script.pop(0)
        if callable(step) and not isinstance(step, (LLMResult, Exception)):
            step = step(record)
        if isinstance(step, Exception):
            raise step
        return step
