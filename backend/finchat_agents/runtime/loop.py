"""The ReAct loop: model call -> tool calls (parallel when safe) -> append results -> repeat.

Stops on a final answer (no tool calls), on the optional finish tool, or on a budget:
max steps (model calls), the run deadline (seconds), or a model error. A budget stop always returns a
partial answer that says what is missing; never an empty one. The SQL-call budget is enforced per tool call:
an over-budget SQL tool call gets an error result telling the model to answer with what it has.
"""
from __future__ import annotations

import asyncio
import json
import logging
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field

from ..llm.types import (
    LLMError,
    LLMResult,
    Message,
    ModelHandle,
    TextBlock,
    ToolCall,
    ToolResultBlock,
    ToolSpec,
    Usage,
)
from ..tracing.events import utcnow
from ..tracing.tracer import preview
from .llm_call import traced_complete
from .tools import GuardrailRefusal, RunContext, Tool, ToolContext, ToolError

log = logging.getLogger(__name__)

TOOL_OUTPUT_CHARS = 20_000  # cap on what one tool result adds to the model context
FINAL_SUMMARY_MIN_SECONDS = 10.0  # time needed to ask the model for a partial answer after a step-budget stop

StopReason = Literal["final", "finish_tool", "max_steps", "max_seconds", "model_error", "empty"]

_REASON_TEXT = {
    "max_steps": "the step limit was reached",
    "max_seconds": "the time limit was reached",
    "model_error": "the language model could not be reached",
    "empty": "the model returned no answer",
}


class ToolCallRecord(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    step: int
    call_id: str
    name: str
    input: dict[str, Any]
    output: str  # what the model saw
    is_error: bool = False
    duration_ms: float = 0.0
    raw: Any = Field(default=None, exclude=True)  # the handler's Python return value, for callers


class LoopResult(BaseModel):
    status: Literal["final", "partial"]
    text: str
    data: dict[str, Any] | None = None  # input of the finish tool, when used
    stop_reason: StopReason
    steps: int
    llm_calls: int
    usage: Usage = Field(default_factory=Usage)
    tool_calls: list[ToolCallRecord] = Field(default_factory=list)
    messages: list[Message] = Field(default_factory=list)


def serialize_output(value: Any, limit: int = TOOL_OUTPUT_CHARS) -> str:
    if hasattr(value, "for_model"):
        value = value.for_model()
    if isinstance(value, str):
        text = value
    elif isinstance(value, BaseModel):
        text = value.model_dump_json()
    else:
        text = json.dumps(value, default=str, ensure_ascii=False)
    if len(text) > limit:
        text = text[:limit] + f"\n... [output truncated, {len(text) - limit} more characters]"
    return text


def _fallback_partial(reason: str, messages: list[Message], records: list[ToolCallRecord]) -> str:
    """Deterministic partial answer when the model cannot be asked for one."""
    parts = [f"Partial answer: I stopped before finishing because {_REASON_TEXT.get(reason, reason)}."]
    last_text = next((m.text for m in reversed(messages) if m.role == "assistant" and m.text), "")
    if last_text:
        parts.append(f"Progress so far: {last_text}")
    ok = [r.name for r in records if not r.is_error]
    failed = [r.name for r in records if r.is_error]
    if ok:
        parts.append(f"Completed steps: {', '.join(dict.fromkeys(ok))} ({len(ok)} call(s)).")
    if failed:
        parts.append(f"Steps that failed: {', '.join(dict.fromkeys(failed))}.")
    parts.append("Missing: a complete, checked answer to the request.")
    return " ".join(parts)


async def execute_tool(call: ToolCall, step_no: int, *, tool_map: dict[str, Tool], ctx: RunContext, agent: str) -> ToolCallRecord:
    """Run one tool call with the SQL budget, the run deadline and tracing; always returns a record (errors become
    readable output for the model). Shared by the own loop and the Anthropic SDK engine."""
    clock = ctx.clock
    started = utcnow()
    t0 = clock()
    is_error = False
    raw: Any = None
    tool = tool_map.get(call.name)
    if tool is None:
        is_error = True
        output = f"Unknown tool '{call.name}'. Available tools: {', '.join(tool_map) or 'none'}."
    elif tool.counts_as_sql and ctx.counters.sql_calls >= ctx.budget.max_sql_calls:
        is_error = True
        output = (
            f"SQL call budget reached ({ctx.budget.max_sql_calls} queries for this question). "
            "Do not run more queries; answer with the results you already have and say what is missing."
        )
    else:
        if tool.counts_as_sql:
            ctx.counters.sql_calls += 1
        tctx = ToolContext(run=ctx, agent=agent, step=step_no, call_id=call.id)
        try:
            remaining = ctx.deadline - clock()
            raw = await asyncio.wait_for(tool.handler(call.input, tctx), timeout=max(remaining, 0.001))
            output = serialize_output(raw)
        except ToolError as exc:
            is_error, output = True, str(exc)
            if isinstance(exc, GuardrailRefusal):
                from ..guardrails.audit import log_decision  # imported here: audit itself uses the runtime

                await log_decision(ctx, "data_check", "block", "data_access", str(exc))
        except (TimeoutError, asyncio.TimeoutError):
            is_error, output = True, f"Tool '{call.name}' did not finish within the time limit."
        except Exception as exc:  # unexpected tool failure becomes a readable error for the model
            log.exception("tool %s failed", call.name)
            is_error, output = True, f"Tool '{call.name}' failed: {type(exc).__name__}: {str(exc)[:300]}"
    record = ToolCallRecord(
        step=step_no, call_id=call.id, name=call.name, input=call.input, output=output,
        is_error=is_error, duration_ms=round((clock() - t0) * 1000, 1), raw=raw,
    )
    await ctx.tracer.emit(
        "tool_call", agent=agent, step=step_no, name=call.name, status="error" if is_error else "ok",
        started_at=started, ended_at=utcnow(),
        payload={"call_id": call.id, "input": preview(json.dumps(call.input, default=str), 2000),
                 "output": preview(output, 1000)},
    )
    return record


async def run_loop(
    *,
    llm: ModelHandle,
    system: str,
    messages: list[Message],
    tools: list[Tool],
    ctx: RunContext,
    agent: str,
    max_steps: int,
    max_tokens: int = 4096,
    temperature: float = 0.0,
    finish_tool: ToolSpec | None = None,
    retry_attempts: int = 4,
    retry_base_delay: float = 1.0,
    initial: LLMResult | None = None,
) -> LoopResult:
    """`initial`: a model result already obtained for step 1 (e.g. the supervisor's classification call);
    the loop continues from it instead of calling the model again. `messages` must not yet contain it."""
    tool_map = {t.name: t for t in tools}
    specs = [t.spec for t in tools] + ([finish_tool] if finish_tool else [])
    records: list[ToolCallRecord] = []
    usage = Usage()
    llm_calls = 0
    step = 0
    clock = ctx.clock
    pending_initial = initial

    async def call_model(msgs: list[Message], step_no: int) -> LLMResult:
        nonlocal usage, llm_calls, pending_initial
        if pending_initial is not None:
            result, pending_initial = pending_initial, None
            llm_calls += 1  # counted and traced by whoever made the call
            usage = usage + result.usage
            return result
        result = await traced_complete(
            llm, ctx, agent=agent, step=step_no, system=system, messages=msgs, tools=specs,
            max_tokens=max_tokens, temperature=temperature, retry_attempts=retry_attempts, retry_base_delay=retry_base_delay,
        )
        llm_calls += 1
        usage = usage + result.usage
        return result

    def done(status: str, text: str, reason: StopReason, data: dict[str, Any] | None = None) -> LoopResult:
        return LoopResult(
            status=status,  # type: ignore[arg-type]
            text=text, data=data, stop_reason=reason, steps=step, llm_calls=llm_calls,
            usage=usage, tool_calls=records, messages=messages,
        )

    async def partial(reason: StopReason) -> LoopResult:
        await ctx.tracer.emit("budget_stop", agent=agent, step=step, payload={"reason": reason})
        text = ""
        # After a step-limit stop, ask the model once (tools still listed, but not executed) to write the partial.
        if reason in ("max_steps", "empty") and ctx.deadline - clock() > FINAL_SUMMARY_MIN_SECONDS:
            note = (
                f"STOP: {_REASON_TEXT[reason]}. Do not call any more tools. Using only the tool results above, "
                "write your best partial answer now. Say clearly what you found and what is still missing. "
                "Do not invent numbers."
            )
            msgs = list(messages)
            if msgs and msgs[-1].role == "user":
                msgs[-1] = Message(role="user", content=[*msgs[-1].content, TextBlock(text=note)])
            else:
                msgs.append(Message.user(note))
            try:
                result = await call_model(msgs, step + 1)
                text = result.text
            except (LLMError, TimeoutError, asyncio.TimeoutError):
                text = ""
        if not text:
            text = _fallback_partial(reason, messages, records)
        return done("partial", text, reason)

    async def run_one(call: ToolCall, step_no: int) -> ToolCallRecord:
        return await execute_tool(call, step_no, tool_map=tool_map, ctx=ctx, agent=agent)

    async def run_tools(calls: list[ToolCall], step_no: int) -> list[ToolCallRecord]:
        results: dict[str, ToolCallRecord] = {}
        parallel = [c for c in calls if c.name not in tool_map or tool_map[c.name].parallel_safe]
        serial = [c for c in calls if c not in parallel]
        if parallel:
            for rec in await asyncio.gather(*(run_one(c, step_no) for c in parallel)):
                results[rec.call_id] = rec
        for c in serial:
            results[c.id] = await run_one(c, step_no)
        return [results[c.id] for c in calls]  # results go back in call order

    while True:
        if step >= max_steps:
            return await partial("max_steps")
        if ctx.deadline - clock() <= 0:
            return await partial("max_seconds")
        step += 1
        try:
            result = await call_model(messages, step)
        except (TimeoutError, asyncio.TimeoutError):
            return await partial("max_seconds")
        except LLMError:
            return await partial("model_error")
        messages.append(result.to_message())

        if not result.tool_calls:
            if result.text:
                return done("final", result.text, "final")
            return await partial("empty")

        if finish_tool:
            finish = next((c for c in result.tool_calls if c.name == finish_tool.name), None)
            if finish is not None:
                data = dict(finish.input)
                text = str(data.get("answer") or data.get("summary") or result.text or "")
                await ctx.tracer.emit("tool_call", agent=agent, step=step, name=finish.name,
                                      payload={"call_id": finish.id, "input": preview(json.dumps(data, default=str), 2000)})
                return done("final", text, "finish_tool", data)

        step_records = await run_tools(result.tool_calls, step)
        records.extend(step_records)
        messages.append(
            Message(
                role="user",
                content=[ToolResultBlock(tool_use_id=r.call_id, content=r.output, is_error=r.is_error) for r in step_records],
            )
        )
