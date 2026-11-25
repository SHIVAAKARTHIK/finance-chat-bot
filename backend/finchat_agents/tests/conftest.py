from __future__ import annotations

import asyncio
from typing import Any

import pytest

from finchat_agents.llm.fake import FakeProvider
from finchat_agents.llm.types import ModelHandle
from finchat_agents.runtime.tools import Budget, RunContext, Tool, ToolContext, tool
from finchat_agents.tracing import MemorySink, Tracer


@pytest.fixture
def sink() -> MemorySink:
    return MemorySink()


@pytest.fixture
def make_ctx(sink: MemorySink):
    def _make(**budget: Any) -> RunContext:
        return RunContext(tracer=Tracer([sink], message_id="msg-1"), budget=Budget(**budget))

    return _make


def handle(provider: FakeProvider, model: str = "fake-model") -> ModelHandle:
    return ModelHandle(provider=provider, model=model)


ADD_SCHEMA = {
    "type": "object",
    "properties": {"a": {"type": "number"}, "b": {"type": "number"}},
    "required": ["a", "b"],
}


@tool("add", "Add two numbers.", ADD_SCHEMA)
async def add_tool(args: dict[str, Any], ctx: ToolContext) -> dict[str, Any]:
    return {"sum": args["a"] + args["b"]}


def sleeper(name: str, seconds: float, *, parallel_safe: bool = True, log: list[str] | None = None) -> Tool:
    @tool(name, f"Sleep {seconds}s.", {"type": "object", "properties": {}}, parallel_safe=parallel_safe)
    async def _t(args: dict[str, Any], ctx: ToolContext) -> str:
        if log is not None:
            log.append(f"start:{name}")
        await asyncio.sleep(seconds)
        if log is not None:
            log.append(f"end:{name}")
        return f"{name} done"

    return _t


def fake_sql_tool() -> Tool:
    @tool("run_sql", "Run a query.", {"type": "object", "properties": {"sql": {"type": "string"}}}, counts_as_sql=True)
    async def _t(args: dict[str, Any], ctx: ToolContext) -> dict[str, Any]:
        return {"rows": [[97]], "columns": ["n"]}

    return _t
