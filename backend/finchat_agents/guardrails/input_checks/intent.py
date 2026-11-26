"""The input check: one model call that judges the current message only (never the history), plus the optional Bedrock
Guardrail on the same message, both at once. Fails closed: if a check does not work, nothing runs."""
from __future__ import annotations

import asyncio

from pydantic import BaseModel

from ...llm.types import LLMError, Message, ModelHandle, ToolSpec
from ...runtime.llm_call import traced_complete
from ...runtime.tools import RunContext
from ..audit import log_decision
from ..bedrock import ContentFilterError
from ..loader import Guardrails
from ..replies import REFUSALS, refusal_message

VERDICT_TOOL = "guard_verdict"
VERDICTS = ["allow", "injection", "confidential", "out_of_scope", "disallowed", "harmful", "support"]
VERDICT_SPEC = ToolSpec(
    name=VERDICT_TOOL,
    description="Give the verdict for the user message.",
    input_schema={
        "type": "object",
        "properties": {"verdict": {"type": "string", "enum": VERDICTS},
                       "reason": {"type": "string", "description": "Why, in a few words (kept for audit)."}},
        "required": ["verdict", "reason"],
    },
)


class Verdict(BaseModel):
    verdict: str = "allow"
    reason: str = ""
    message: str = ""  # the fixed reply when blocked
    failed: bool = False  # the check itself did not work: the request is not processed

    @property
    def blocked(self) -> bool:
        return self.failed or bool(self.message)


async def check_input(message: str, guardrails: Guardrails, llm: ModelHandle, ctx: RunContext, system: str) -> Verdict:
    intent, content = await asyncio.gather(_intent(message, guardrails, llm, ctx, system),
                                           _content(message, guardrails, ctx))
    if intent.verdict == "support" and not intent.failed:  # a person who may be in danger gets that reply first
        return intent
    for verdict in (content, intent):
        if verdict is not None and verdict.failed:
            return verdict
    return content if content is not None and content.blocked else intent


async def _intent(message: str, guardrails: Guardrails, llm: ModelHandle, ctx: RunContext, system: str) -> Verdict:
    rules = guardrails.prompt_for("input_check")
    try:
        result = await traced_complete(
            llm, ctx, agent="guardrails", step=1, system=f"{system}\n\n---\n\n{rules}" if rules else system,
            messages=[Message.user(f"<user_message>\n{message}\n</user_message>")], tools=[VERDICT_SPEC], max_tokens=300)
    except (LLMError, TimeoutError, asyncio.TimeoutError) as exc:
        await log_decision(ctx, "input_check", "error", "model_check", f"check failed: {type(exc).__name__}")
        return Verdict(failed=True, reason=type(exc).__name__)
    call = next((c for c in result.tool_calls if c.name == VERDICT_TOOL), None)
    kind = str(call.input.get("verdict") or "") if call else _from_text(guardrails, result.text or "")
    if kind != "allow" and kind not in REFUSALS:
        await log_decision(ctx, "input_check", "error", "model_check", "the check returned no verdict")
        return Verdict(failed=True, reason="no verdict")
    reason = str(call.input.get("reason") or "") if call else "the model replied with the fixed message"
    message = refusal_message(guardrails, kind)
    note = " (this rule is switched off)" if kind != "allow" and not message else ""
    await log_decision(ctx, "input_check", "block" if message else "allow", kind, (reason or "no reason given") + note)
    return Verdict(verdict=kind, reason=reason, message=message)


async def _content(message: str, guardrails: Guardrails, ctx: RunContext) -> Verdict | None:
    if guardrails.content_filter is None:
        return None
    try:
        result = await guardrails.content_filter.apply(message, "INPUT")
    except ContentFilterError as exc:
        await log_decision(ctx, "content_filter_input", "error", "bedrock_guardrail", f"check failed: {exc}")
        return Verdict(failed=True, reason=f"content filter {exc}")
    await log_decision(ctx, "content_filter_input", "block" if result.blocked else "allow", "bedrock_guardrail",
                       ", ".join(result.categories) or ("intervened" if result.blocked else "nothing found"))
    if not result.blocked:
        return Verdict()
    return Verdict(verdict="harmful", message=result.text or refusal_message(guardrails, "harmful"))


def _norm(text: str) -> str:
    return " ".join(text.replace("’", "'").replace('"', "").split()).casefold()


def _from_text(guardrails: Guardrails, text: str) -> str:
    """Some packs say "respond only with <message>": a model that does so instead of calling the tool still blocks."""
    for kind in ("confidential", "out_of_scope", "disallowed"):
        message = refusal_message(guardrails, kind)
        if message and _norm(message) in _norm(text):
            return kind
    return ""
