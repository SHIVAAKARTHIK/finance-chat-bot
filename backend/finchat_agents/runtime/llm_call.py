"""One traced, retried, deadline-bounded model call. Used by the ReAct loop, the fast path and the orchestrator,
so every LLM call is counted (Counters.llm_calls) and becomes an `llm_call` trace event."""
from __future__ import annotations

import asyncio

from ..llm.types import LLMError, LLMResult, Message, ModelHandle, ToolSpec
from ..tracing.events import utcnow
from ..tracing.tracer import preview
from .retry import call_with_retry
from .tools import RunContext


async def traced_complete(
    llm: ModelHandle,
    ctx: RunContext,
    *,
    agent: str,
    step: int,
    system: str,
    messages: list[Message],
    tools: list[ToolSpec],
    max_tokens: int = 4096,
    temperature: float = 0.0,
    retry_attempts: int = 4,
    retry_base_delay: float = 1.0,
) -> LLMResult:
    """Raises LLMError (provider failure after retries) or TimeoutError (run deadline reached)."""
    started = utcnow()
    remaining = ctx.deadline - ctx.clock()
    try:
        result = await asyncio.wait_for(
            call_with_retry(
                lambda: llm.complete(system, messages, tools, max_tokens, temperature),
                attempts=retry_attempts,
                base_delay=retry_base_delay,
                deadline=ctx.deadline,
                clock=ctx.clock,
            ),
            timeout=max(remaining, 0.001),
        )
    except (LLMError, TimeoutError, asyncio.TimeoutError) as exc:
        await ctx.tracer.emit(
            "llm_call", agent=agent, step=step, name=llm.model, status="error", started_at=started, ended_at=utcnow(),
            payload={"error": preview(str(exc) or type(exc).__name__, 500)},
        )
        raise
    ctx.counters.llm_calls += 1
    ctx.counters.input_tokens += result.usage.input_tokens
    ctx.counters.output_tokens += result.usage.output_tokens
    if llm.model not in ctx.counters.models:
        ctx.counters.models.append(llm.model)
    await ctx.tracer.emit(
        "llm_call", agent=agent, step=step, name=llm.model, started_at=started, ended_at=utcnow(),
        input_tokens=result.usage.input_tokens, output_tokens=result.usage.output_tokens,
        cache_read_tokens=result.usage.cache_read_tokens, cache_write_tokens=result.usage.cache_write_tokens,
        payload={"stop_reason": result.stop_reason, "text": preview(result.text, 500), "tool_calls": [c.name for c in result.tool_calls]},
    )
    return result
