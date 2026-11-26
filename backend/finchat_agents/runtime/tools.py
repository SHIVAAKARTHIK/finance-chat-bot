"""Tool and run-context types shared by the loop and agents."""
from __future__ import annotations

import time
from dataclasses import dataclass, field, replace
from typing import Any, Awaitable, Callable

from pydantic import BaseModel

from ..config import Settings
from ..llm.types import ToolSpec
from ..tracing.tracer import Tracer


class Budget(BaseModel):
    max_steps: int = 15
    max_seconds: float = 300.0
    max_sql_calls: int = 10

    @classmethod
    def from_settings(cls, s: Settings) -> "Budget":
        return cls(max_steps=s.agent_max_steps, max_seconds=s.agent_max_seconds, max_sql_calls=s.agent_max_sql_calls)


@dataclass
class Counters:
    """Shared by every agent working on one question (nested agents count against the same SQL budget)."""

    sql_calls: int = 0
    llm_calls: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    models: list[str] = field(default_factory=list)


@dataclass
class RunContext:
    """Per-question context passed down to every agent and tool."""

    tracer: Tracer
    budget: Budget = field(default_factory=Budget)
    deadline: float = 0.0  # time.monotonic() value; 0 means "set from budget at first use"
    counters: Counters = field(default_factory=Counters)
    user: Any = None  # resolved user/role (task 03)
    extras: dict[str, Any] = field(default_factory=dict)
    clock: Callable[[], float] = time.monotonic

    def __post_init__(self) -> None:
        if not self.deadline:
            self.deadline = self.clock() + self.budget.max_seconds

    @property
    def run_id(self) -> str:
        return self.tracer.run_id

    def remaining(self) -> float:
        return self.deadline - self.clock()

    def child(self, max_seconds: float | None = None) -> "RunContext":
        """Same tracer, counters, user and deadline; optionally a tighter deadline for a sub-agent."""
        deadline = self.deadline
        if max_seconds is not None:
            deadline = min(deadline, self.clock() + max_seconds)
        return replace(self, deadline=deadline)


@dataclass
class ToolContext:
    run: RunContext
    agent: str
    step: int
    call_id: str


class ToolError(Exception):
    """Raise from a tool handler for a plain, fixable message the model should read (guardrail refusals etc.)."""


class GuardrailRefusal(ToolError):
    """A data guardrail refused (read-only, allowed tables, business area, personal data, no access): audited."""


ToolHandler = Callable[[dict[str, Any], ToolContext], Awaitable[Any]]


@dataclass
class Tool:
    spec: ToolSpec
    handler: ToolHandler
    counts_as_sql: bool = False  # counted against Budget.max_sql_calls before it runs
    parallel_safe: bool = True  # may run concurrently with other calls from the same model turn

    @property
    def name(self) -> str:
        return self.spec.name


def tool(
    name: str,
    description: str,
    input_schema: dict[str, Any],
    *,
    counts_as_sql: bool = False,
    parallel_safe: bool = True,
) -> Callable[[ToolHandler], Tool]:
    """Decorator: turn an async handler(args, ctx) into a Tool."""

    def wrap(fn: ToolHandler) -> Tool:
        spec = ToolSpec(name=name, description=description, input_schema=input_schema)
        return Tool(spec=spec, handler=fn, counts_as_sql=counts_as_sql, parallel_safe=parallel_safe)

    return wrap
