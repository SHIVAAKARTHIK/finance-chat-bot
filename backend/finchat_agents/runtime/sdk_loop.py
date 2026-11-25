"""ReAct loop run by the Anthropic SDK tool runner (`client.beta.messages.tool_runner`), as an alternative to `run_loop`.

Selected with REACT_ENGINE=anthropic_sdk (default: own). Same inputs and the same `LoopResult`, so agents, tools, the
guardrails inside the tools, the SQL-call budget, the run deadline, the step limit, tracing and the finish tool all work
as before. What differs from our own loop:
- the SDK runs the tool calls of one reply one after another (our loop runs safe ones in parallel);
- our history cache point is not set on the conversation (the system prompt and tool definitions are still cached);
- retries are the SDK's (2 attempts) instead of runtime/retry.py, and a budget stop returns the deterministic partial
  answer (no extra model call to write it).
Only Claude providers expose `sdk_client()`; other models, and any provider without it, use `run_loop`.
"""
from __future__ import annotations

import asyncio
import itertools
import json
from typing import Any

from ..llm.claude_bedrock import _CACHE, map_anthropic_error, messages_to_anthropic, parse_anthropic_response
from ..llm.types import LLMError, LLMResult, Message, ModelHandle, ToolCall, ToolResultBlock, ToolSpec, Usage
from ..tracing.events import utcnow
from ..tracing.tracer import preview
from .loop import LoopResult, ToolCallRecord, _fallback_partial, execute_tool
from .tools import RunContext, Tool


def sdk_engine_available(llm: ModelHandle) -> bool:
    return hasattr(llm.provider, "sdk_client")


class _SdkTool:
    """A tool the SDK runner can list and call. It is built per run so every call is traced and recorded by us."""

    def __new__(cls, *args: Any, **kwargs: Any) -> Any:  # base class is imported lazily (the SDK is optional at import time)
        from anthropic.lib.tools import BetaAsyncBuiltinFunctionTool

        class Impl(BetaAsyncBuiltinFunctionTool):
            def __init__(self, spec: ToolSpec, run: Any, cached: bool):
                self.spec, self._run, self._cached = spec, run, cached

            def to_dict(self) -> Any:
                out = {"name": self.spec.name, "description": self.spec.description, "input_schema": self.spec.input_schema}
                if self._cached:
                    out["cache_control"] = _CACHE
                return out

            async def call(self, input: object) -> Any:
                return await self._run(self.spec.name, dict(input) if isinstance(input, dict) else {})

        return Impl(*args, **kwargs)


async def run_loop_sdk(
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
    retry_attempts: int = 4,  # accepted for interface parity; the SDK client retries on its own
    retry_base_delay: float = 1.0,
    initial: LLMResult | None = None,
) -> LoopResult:
    from anthropic.lib.tools import ToolError as SdkToolError

    tool_map = {t.name: t for t in tools}
    records: list[ToolCallRecord] = []
    usage = Usage()
    llm_calls = 0
    step = 0
    clock = ctx.clock
    ids = itertools.count(1)
    state: dict[str, Any] = {"last": None, "last_activity": utcnow()}

    def done(status: str, text: str, reason: str, data: dict[str, Any] | None = None) -> LoopResult:
        return LoopResult(status=status, text=text, data=data, stop_reason=reason, steps=step,  # type: ignore[arg-type]
                          llm_calls=llm_calls, usage=usage, tool_calls=records, messages=messages)

    async def partial(reason: str) -> LoopResult:
        await ctx.tracer.emit("budget_stop", agent=agent, step=step, payload={"reason": reason})
        return done("partial", _fallback_partial(reason, messages, records), reason)

    async def record_call(result: LLMResult, started: Any) -> None:
        nonlocal usage, llm_calls
        llm_calls += 1
        usage = usage + result.usage
        ctx.counters.llm_calls += 1
        ctx.counters.input_tokens += result.usage.input_tokens
        ctx.counters.output_tokens += result.usage.output_tokens
        if llm.model not in ctx.counters.models:
            ctx.counters.models.append(llm.model)
        await ctx.tracer.emit(
            "llm_call", agent=agent, step=step, name=llm.model, started_at=started, ended_at=utcnow(),
            input_tokens=result.usage.input_tokens, output_tokens=result.usage.output_tokens,
            cache_read_tokens=result.usage.cache_read_tokens, cache_write_tokens=result.usage.cache_write_tokens,
            payload={"stop_reason": result.stop_reason, "text": preview(result.text, 500),
                     "tool_calls": [c.name for c in result.tool_calls], "engine": "anthropic_sdk"})

    async def run_tool(name: str, args: dict[str, Any]) -> str:
        call = ToolCall(id=f"sdk_{next(ids)}", name=name, input=args)
        rec = await execute_tool(call, step, tool_map=tool_map, ctx=ctx, agent=agent)
        records.append(rec)
        state["last_activity"] = utcnow()
        if rec.is_error:
            raise SdkToolError(rec.output)
        return rec.output

    def flush_tool_results(upto_step: int) -> None:
        mine = [r for r in records if r.step == upto_step]
        if mine:
            messages.append(Message(role="user", content=[ToolResultBlock(tool_use_id=r.call_id, content=r.output, is_error=r.is_error)
                                                          for r in mine]))

    def finished(call: ToolCall, result: LLMResult) -> LoopResult:
        data = dict(call.input)
        return done("final", str(data.get("answer") or data.get("summary") or result.text or ""), "finish_tool", data)

    # step 1 already made by the caller (the supervisor's route call): run its tool calls here, then hand over to the runner
    if initial is not None:
        step = 1
        llm_calls += 1  # counted and traced by whoever made the call
        usage = usage + initial.usage
        messages.append(initial.to_message())
        if not initial.tool_calls:
            return done("final", initial.text, "final") if initial.text else await partial("empty")
        fin = next((c for c in initial.tool_calls if finish_tool and c.name == finish_tool.name), None)
        if fin is not None:
            return finished(fin, initial)
        for c in initial.tool_calls:
            rec = await execute_tool(c, step, tool_map=tool_map, ctx=ctx, agent=agent)
            rec = rec.model_copy(update={"call_id": c.id})
            records.append(rec)
        flush_tool_results(step)

    if step >= max_steps:
        return await partial("max_steps")
    if ctx.deadline - clock() <= 0:
        return await partial("max_seconds")

    async def _never(name: str, args: dict[str, Any]) -> str:  # the loop stops before the runner would call the finish tool
        return "ok"

    entries = [(t.spec, run_tool) for t in tools] + ([(finish_tool, _never)] if finish_tool is not None else [])
    # the last tool definition carries the cache point, which caches all tool definitions
    sdk_tools = [_SdkTool(spec, run, i == len(entries) - 1) for i, (spec, run) in enumerate(entries)]
    params: dict[str, Any] = {"model": llm.model, "max_tokens": max_tokens, "messages": messages_to_anthropic(messages),
                              "max_iterations": max_steps - step}
    if system:
        params["system"] = [{"type": "text", "text": system, "cache_control": _CACHE}]
    if sdk_tools:
        params["tools"] = sdk_tools
    client = llm.provider.sdk_client().with_options(max_retries=2)  # type: ignore[attr-defined]

    async def drive() -> LoopResult | None:
        nonlocal step
        runner = client.beta.messages.tool_runner(**params)
        async for message in runner:
            started = state["last_activity"]
            if step:
                flush_tool_results(step)
            step += 1
            result = parse_anthropic_response(message)
            await record_call(result, started)
            state["last_activity"] = utcnow()
            state["last"] = result
            messages.append(result.to_message())
            if not result.tool_calls:
                return done("final", result.text, "final") if result.text else await partial("empty")
            fin = next((c for c in result.tool_calls if finish_tool and c.name == finish_tool.name), None)
            if fin is not None:
                await ctx.tracer.emit("tool_call", agent=agent, step=step, name=fin.name,
                                      payload={"call_id": fin.id, "input": preview(json.dumps(fin.input, default=str), 2000)})
                return finished(fin, result)
            # the runner runs the tool calls of this reply when the loop asks for the next one
        return None

    remaining = ctx.deadline - clock()
    try:
        outcome = await asyncio.wait_for(drive(), timeout=max(remaining, 0.001))
    except (TimeoutError, asyncio.TimeoutError):
        return await partial("max_seconds")
    except Exception as exc:  # noqa: BLE001 - an SDK or API error ends the run with a partial answer
        err = exc if isinstance(exc, LLMError) else map_anthropic_error(exc)
        await ctx.tracer.emit("llm_call", agent=agent, step=step + 1, name=llm.model, status="error",
                              payload={"error": preview(str(err), 500), "engine": "anthropic_sdk"})
        return await partial("model_error")
    if outcome is not None:
        return outcome
    return await partial("max_steps")  # the runner stopped at max_iterations with tool calls still pending
