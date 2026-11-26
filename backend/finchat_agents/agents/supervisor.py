"""Supervisor agent: classifies in its first call (route tool), delegates to agents, submits a structured result."""
from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field

from ..llm.types import LLMResult, ModelHandle, ToolSpec
from ..runtime.agent import Agent
from ..runtime.tools import Tool, ToolContext
from .specialists import load_prompt

Classification = Literal["general", "simple_data", "complex", "workflow"]
ROUTE_TOOL = "route"

ROUTE_SPEC = ToolSpec(
    name=ROUTE_TOOL,
    description="Classify the request. Call this in your first response: general (no company data), simple_data "
                "(one simple data question), complex (comparisons, several questions, mixed, files, unclear) or workflow "
                "(the user lists steps to carry out).",
    input_schema={
        "type": "object",
        "properties": {
            "classification": {"type": "string", "enum": ["general", "simple_data", "complex", "workflow"]},
            "standalone_question": {"type": "string", "description": "Only when the request refers to earlier turns ('that', 'same period'): the request rewritten to stand alone. Otherwise leave empty."},
            "options": {"type": "array", "items": {"type": "string"},
                        "description": "Only when the request could belong to two or more topics of this conversation and "
                                       "nothing decides it (it names no topic and is not a follow-up of the current one): "
                                       "the request rewritten once per topic, each starting with the topic name, e.g. "
                                       "'Fixed assets: total additions in Oct 2026'. The user is asked to choose. "
                                       "Otherwise leave it out."},
            "refusal": {"type": "string", "enum": ["confidentiality", "out_of_scope", "disallowed"],
                        "description": "Only when a company guardrail rule requires a fixed reply to this request. "
                                       "Otherwise leave it out."},
            "reason": {"type": "string"},
        },
        "required": ["classification"],
    },
)

SUPERVISOR_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"type": "string", "enum": ["answered", "partial", "clarification", "declined"]},
        "answer": {"type": "string", "description": "The facts, numbers exactly as the agents returned them."},
        "how_calculated": {"type": "string", "description": "Business-language explanation; empty for general knowledge."},
        "result_ids": {"type": "array", "items": {"type": "string"}},
        "caveats": {"type": "array", "items": {"type": "string"}},
        "alternatives": {"type": "array", "items": {"type": "string"}},
        "steps": {
            "type": "array",
            "description": "Workflows only: every planned step with its outcome.",
            "items": {"type": "object", "properties": {
                "step": {"type": "string"},
                "status": {"type": "string", "enum": ["done", "done_with_caveat", "not_done"]},
                "detail": {"type": "string"}}, "required": ["step", "status"]},
        },
    },
    "required": ["status", "answer"],
}


class Route(BaseModel):
    classification: Classification = "complex"
    standalone_question: str = ""
    reason: str = ""
    options: list[str] = Field(default_factory=list)  # topic choices when the request is ambiguous between topics
    refusal: str = ""  # guardrail refusal kind: the request gets the fixed reply
    found: bool = False  # False when the model did not call route (then we treat the request as complex)


def parse_route(result: LLMResult, question: str) -> Route:
    call = next((c for c in result.tool_calls if c.name == ROUTE_TOOL), None)
    if call is None:
        return Route(standalone_question=question)
    cls = call.input.get("classification")
    return Route(
        classification=cls if cls in ("general", "simple_data", "complex", "workflow") else "complex",
        standalone_question=str(call.input.get("standalone_question") or question).strip() or question,
        reason=str(call.input.get("reason") or ""),
        options=[str(o).strip() for o in (call.input.get("options") or []) if str(o).strip()][:4]
        if isinstance(call.input.get("options"), list) else [],
        refusal=str(call.input.get("refusal") or "").strip(),
        found=True,
    )


class WorkflowStep(BaseModel):
    step: str
    status: Literal["done", "done_with_caveat", "not_done"] = "not_done"
    detail: str = ""


class SupervisorDraft(BaseModel):
    """What the supervisor (or the fast path) hands to the answer writer."""

    status: Literal["answered", "partial", "clarification", "declined", "failed"] = "answered"
    answer: str = ""
    how_calculated: str = ""
    result_ids: list[str] = Field(default_factory=list)
    caveats: list[str] = Field(default_factory=list)
    alternatives: list[str] = Field(default_factory=list)
    steps: list[WorkflowStep] = Field(default_factory=list)

    @classmethod
    def from_data(cls, data: dict[str, Any] | None, fallback_text: str, partial: bool) -> "SupervisorDraft":
        if not data:
            return cls(status="partial" if partial else "answered", answer=fallback_text)
        clean = {k: v for k, v in data.items() if k in cls.model_fields and v is not None}
        if clean.get("status") not in ("answered", "partial", "clarification", "declined"):
            clean["status"] = "partial" if partial else "answered"
        for key in ("result_ids", "caveats", "alternatives"):
            if isinstance(clean.get(key), str):
                clean[key] = [clean[key]]
        steps = []
        for s in clean.pop("steps", None) or []:
            if isinstance(s, dict) and s.get("step"):
                status = s.get("status") if s.get("status") in ("done", "done_with_caveat", "not_done") else "not_done"
                steps.append(WorkflowStep(step=str(s["step"]), status=status, detail=str(s.get("detail") or "")))
        clean["steps"] = steps
        draft = cls(**clean)
        if partial and draft.status == "answered":
            draft.status = "partial"
        return draft


def route_tool() -> Tool:
    async def handler(args: dict[str, Any], tctx: ToolContext) -> str:
        return f"Classification recorded: {args.get('classification')}. Continue with the agents."

    return Tool(spec=ROUTE_SPEC, handler=handler)


PLAN_KEY = "plan"  # RunContext.extras: the recorded workflow plan


def record_plan_tool() -> Tool:
    spec = ToolSpec(
        name="record_plan",
        description="Workflows: record the numbered plan before carrying it out (shown to the user with per-step status).",
        input_schema={"type": "object", "properties": {"steps": {"type": "array", "items": {"type": "string"}}},
                      "required": ["steps"]},
    )

    async def handler(args: dict[str, Any], tctx: ToolContext) -> str:
        steps = [str(s).strip() for s in (args.get("steps") or []) if str(s).strip()]
        if not steps:
            from ..runtime.tools import ToolError

            raise ToolError("Give the plan as a list of steps.")
        tctx.run.extras[PLAN_KEY] = steps
        await tctx.run.tracer.emit("plan", agent=tctx.agent, step=tctx.step, payload={"steps": steps})
        return f"Plan recorded ({len(steps)} steps). Carry them out in order and report each step's status at the end."

    return Tool(spec=spec, handler=handler, parallel_safe=False)


def build_supervisor(llm: ModelHandle, agent_tools: list[Tool], **kw: Any) -> Agent:
    return Agent(
        "supervisor",
        load_prompt("supervisor"),
        llm,
        [route_tool(), record_plan_tool(), *agent_tools],
        output_schema=SUPERVISOR_SCHEMA,
        **kw,
    )
