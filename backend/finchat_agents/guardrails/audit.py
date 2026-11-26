"""Every guardrail decision is a trace event (stored with the message events). Never the removed content itself."""
from __future__ import annotations

from ..runtime.tools import RunContext
from ..tracing.events import utcnow


async def log_check(ctx: RunContext, name: str, output: str, status: str = "ok") -> None:
    now = utcnow()
    await ctx.tracer.emit("tool_call", agent="guardrails", step=0, name=name, status=status, started_at=now,
                          ended_at=now, payload={"output": output})
