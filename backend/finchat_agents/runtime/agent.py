"""Agent = name + system prompt + model + tools, run with our ReAct loop.

`as_tool()` exposes an agent to another agent as `ask_<name>(task, context?)`. Every call starts a fresh context
(new message list) and returns a structured AgentResult. Only the supervisor talks to the user.
"""
from __future__ import annotations

import json
import re
from typing import Any, Literal

from pydantic import BaseModel, Field

from ..llm.types import LLMResult, Message, ModelHandle, ToolSpec, Usage
from ..tracing.events import utcnow
from ..tracing.tracer import preview
from .loop import LoopResult, ToolCallRecord, run_loop
from .sdk_loop import run_loop_sdk, sdk_engine_available
from .tools import RunContext, Tool, ToolContext

FINISH_TOOL_NAME = "submit_result"


def recover_structured(text: str, schema: dict[str, Any] | None) -> dict[str, Any] | None:
    """A model sometimes writes the structured result as plain JSON text (maybe inside a ```json fence, or with a sentence
    around it) instead of calling the finish tool. Accept it when it is a JSON object with the schema's required keys, so
    raw JSON never reaches a user as the answer."""
    if not text or not schema:
        return None
    s = text.strip()
    fence = re.search(r"```(?:json)?\s*(.*?)```", s, re.DOTALL)
    if fence:
        s = fence.group(1).strip()
    start, end = s.find("{"), s.rfind("}")
    if start < 0 or end <= start:
        return None
    try:
        obj = json.loads(s[start:end + 1])
    except ValueError:
        return None
    if not isinstance(obj, dict):
        return None
    required = schema.get("required") or list((schema.get("properties") or {}))[:1]
    return obj if required and all(k in obj for k in required) else None


class AgentResult(BaseModel):
    agent: str
    status: Literal["final", "partial"]
    answer: str
    data: dict[str, Any] | None = None  # structured output from the finish tool (when the agent has a schema)
    stop_reason: str
    steps: int
    llm_calls: int
    usage: Usage = Field(default_factory=Usage)
    tool_calls: list[ToolCallRecord] = Field(default_factory=list)

    def for_model(self) -> dict[str, Any]:
        """What a calling agent sees: the result, not the sub-agent's whole transcript."""
        out: dict[str, Any] = {"agent": self.agent, "status": self.status, "answer": self.answer}
        if self.data is not None:
            out["data"] = self.data
        if self.status == "partial":
            out["stop_reason"] = self.stop_reason
        errors = [r.output for r in self.tool_calls if r.is_error]
        if errors:
            out["tool_errors"] = [preview(e, 300) for e in errors[-3:]]
        return out


class Agent:
    def __init__(
        self,
        name: str,
        system_prompt: str,
        llm: ModelHandle,
        tools: list[Tool] | None = None,
        *,
        description: str = "",
        max_steps: int | None = None,
        max_seconds: float | None = None,
        max_tokens: int = 4096,
        temperature: float = 0.0,
        output_schema: dict[str, Any] | None = None,
    ):
        self.name = name
        self.system_prompt = system_prompt
        self.llm = llm
        self.tools = list(tools or [])
        self.description = description or f"Ask the {name} agent to do a task."
        self.max_steps = max_steps
        self.max_seconds = max_seconds
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.finish_tool = (
            ToolSpec(
                name=FINISH_TOOL_NAME,
                description="Submit your final structured result. Call this once, when you are done.",
                input_schema=output_schema,
            )
            if output_schema
            else None
        )

    async def run(
        self,
        task: str,
        ctx: RunContext,
        *,
        context: str | None = None,
        history: list[Message] | None = None,
        parent_call_id: str | None = None,
        initial: LLMResult | None = None,
    ) -> AgentResult:
        run_ctx = ctx.child(self.max_seconds)
        use_sdk = ctx.extras.get("react_engine", "own") == "anthropic_sdk" and sdk_engine_available(self.llm)
        extra = await self.extra_context(task, ctx)
        context = "\n\n".join(c for c in (context, extra) if c) or None
        user_text = task if not context else f"{task}\n\n<context>\n{context}\n</context>"
        messages = [*(m.model_copy(deep=True) for m in (history or [])), Message.user(user_text)]
        started = utcnow()
        await ctx.tracer.emit(
            "agent_start", agent=self.name, started_at=started,
            payload={"task": preview(task, 2000), "parent_call_id": parent_call_id, "model": self.llm.model,
                     "engine": "anthropic_sdk" if use_sdk else "own"},
        )
        loop_fn = run_loop_sdk if use_sdk else run_loop
        loop_result: LoopResult = await loop_fn(
            llm=self.llm,
            system=self.system_prompt,
            messages=messages,
            tools=self.tools,
            ctx=run_ctx,
            agent=self.name,
            max_steps=self.max_steps or ctx.budget.max_steps,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            finish_tool=self.finish_tool,
            initial=initial,
        )
        data, answer = loop_result.data, loop_result.text
        if data is None and self.finish_tool is not None and loop_result.status == "final":
            data = recover_structured(loop_result.text, self.finish_tool.input_schema)
            if data is not None and isinstance(data.get("answer"), str) and data["answer"].strip():
                answer = data["answer"].strip()
        result = AgentResult(
            agent=self.name,
            status=loop_result.status,
            answer=answer,
            data=data,
            stop_reason=loop_result.stop_reason,
            steps=loop_result.steps,
            llm_calls=loop_result.llm_calls,
            usage=loop_result.usage,
            tool_calls=loop_result.tool_calls,
        )
        await ctx.tracer.emit(
            "agent_end", agent=self.name, step=loop_result.steps, started_at=started, ended_at=utcnow(),
            input_tokens=result.usage.input_tokens, output_tokens=result.usage.output_tokens,
            payload={"status": result.status, "stop_reason": result.stop_reason, "llm_calls": result.llm_calls,
                     "answer": preview(result.answer, 1000)},
        )
        return result

    async def extra_context(self, task: str, ctx: RunContext) -> str | None:
        """Override to add facts to every task (e.g. few-shot examples). Default: nothing."""
        return None

    def as_tool(self, *, name: str | None = None, description: str | None = None) -> Tool:
        spec = ToolSpec(
            name=name or f"ask_{self.name}",
            description=description or self.description,
            input_schema={
                "type": "object",
                "properties": {
                    "task": {"type": "string", "description": "What the agent should do, in plain words."},
                    "context": {"type": "string", "description": "Optional facts it needs (tables found, SQL tried, errors)."},
                },
                "required": ["task"],
            },
        )

        async def handler(args: dict[str, Any], tctx: ToolContext) -> AgentResult:
            return await self.run(
                str(args.get("task", "")), tctx.run, context=args.get("context"), parent_call_id=tctx.call_id
            )

        return Tool(spec=spec, handler=handler)
