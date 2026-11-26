"""The input check (one model call on the current message only) and the output check (code) around an answer."""
from __future__ import annotations

import asyncio
from typing import Any

from pydantic import BaseModel

from ..llm.types import LLMError, Message, ModelHandle, ToolSpec
from ..runtime.llm_call import traced_complete
from ..runtime.tools import RunContext
from ..tracing.events import utcnow
from .filters import Scrubber
from .loader import Guardrails

DEFAULT_CONFIDENTIALITY = "I can't share that. I can help with your finance questions."
DEFAULT_OUT_OF_SCOPE = "I can only help with finance questions."
DEFAULT_DISALLOWED = "I can't help with that request."
COULD_NOT_ANSWER_TEXT = ("I couldn't find approved information to answer that. Try naming the entity, period or business "
                         "area you mean.")

# refusal kind -> (pack that must be enabled, value holding the reply, reply when the value is not set)
REFUSALS: dict[str, tuple[str, str, str]] = {
    "injection": ("prompt_injection_shield", "CONFIDENTIALITY_MESSAGE", DEFAULT_CONFIDENTIALITY),
    "confidential": ("system_prompt_confidentiality", "CONFIDENTIALITY_MESSAGE", DEFAULT_CONFIDENTIALITY),
    "confidentiality": ("system_prompt_confidentiality", "CONFIDENTIALITY_MESSAGE", DEFAULT_CONFIDENTIALITY),
    "out_of_scope": ("scope_enforcement", "OUT_OF_SCOPE_MESSAGE", DEFAULT_OUT_OF_SCOPE),
    "disallowed": ("disallowed_capabilities", "DISALLOWED_CAPABILITY_MESSAGE", DEFAULT_DISALLOWED),
}

VERDICT_TOOL = "guard_verdict"
VERDICT_SPEC = ToolSpec(
    name=VERDICT_TOOL,
    description="Give the verdict for the user message.",
    input_schema={
        "type": "object",
        "properties": {
            "verdict": {"type": "string", "enum": ["allow", "injection", "confidential", "out_of_scope", "disallowed"]},
            "reason": {"type": "string", "description": "A few words."},
        },
        "required": ["verdict"],
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


def refusal_message(guardrails: Guardrails, kind: str) -> str:
    """The fixed reply for a refusal kind, or "" when that rule is switched off or the kind is unknown."""
    entry = REFUSALS.get(kind)
    if entry is None:
        return ""
    pack, value, default = entry
    return guardrails.value(value, default) if guardrails.enabled(pack) else ""


async def _log(ctx: RunContext, name: str, output: str, status: str = "ok") -> None:
    now = utcnow()
    await ctx.tracer.emit("tool_call", agent="guardrails", step=0, name=name, status=status, started_at=now,
                          ended_at=now, payload={"output": output})


async def check_input(message: str, guardrails: Guardrails, llm: ModelHandle, ctx: RunContext, system: str) -> Verdict:
    """Judge the current message only (never the history). Fails closed: if no verdict comes back, nothing runs."""
    rules = guardrails.prompt_for("input_check")
    if not rules:
        return Verdict()
    try:
        result = await traced_complete(
            llm, ctx, agent="guardrails", step=1, system=f"{system}\n\n---\n\n{rules}",
            messages=[Message.user(f"<user_message>\n{message}\n</user_message>")], tools=[VERDICT_SPEC], max_tokens=300)
    except (LLMError, TimeoutError, asyncio.TimeoutError) as exc:
        await _log(ctx, "input_check", f"failed: {type(exc).__name__}", "error")
        return Verdict(failed=True, reason=type(exc).__name__)
    call = next((c for c in result.tool_calls if c.name == VERDICT_TOOL), None)
    kind = str(call.input.get("verdict") or "") if call else _from_text(guardrails, result.text or "")
    if kind != "allow" and kind not in REFUSALS:
        await _log(ctx, "input_check", "failed: no verdict", "error")
        return Verdict(failed=True, reason="no verdict")
    reason = str(call.input.get("reason") or "") if call else ""
    await _log(ctx, "input_check", f"{kind}: {reason}".rstrip(": "))
    return Verdict(verdict=kind, reason=reason, message=refusal_message(guardrails, kind))


def _from_text(guardrails: Guardrails, text: str) -> str:
    """Some packs say "respond only with <message>": a model that does so instead of calling the tool still blocks."""
    for kind in ("confidential", "out_of_scope", "disallowed"):
        message = refusal_message(guardrails, kind)
        if message and _norm(message) in _norm(text):
            return kind
    return ""


def _norm(text: str) -> str:
    return " ".join(text.replace("’", "'").replace('"', "").split()).casefold()


async def check_output(env: Any, guardrails: Guardrails, scrubber: Scrubber, ctx: RunContext) -> None:
    """Applied to every answer before it leaves: fixed replies are made exact, the could-not-answer marker never
    reaches the user, and disallowed content is removed from all text and table values."""
    actions: list[str] = []
    answer = _norm(env.answer or "")
    for kind in ("confidential", "out_of_scope", "disallowed"):
        message = refusal_message(guardrails, kind)
        if message and _norm(message) in answer:
            _decline(env, message)
            await _log(ctx, "output_check", f"fixed reply: {kind}")
            return

    marker = guardrails.value("COULD_NOT_ANSWER_MARKER")
    if marker and marker in f"{env.answer}\n{env.how_calculated}":
        env.answer = env.answer.replace(marker, "").strip(" \n\"'")
        env.how_calculated = env.how_calculated.replace(marker, "").strip()
        if len(env.answer) < 20:  # nothing but the marker
            env.answer, env.how_calculated, env.tables, env.suggestions = COULD_NOT_ANSWER_TEXT, "", [], []
        if env.status == "answered":
            env.status = "partial"
        actions.append("could_not_answer")

    removed: set[str] = set()

    def clean(text: str) -> str:
        out, kinds = scrubber.text(text)
        removed.update(kinds)
        return out

    env.answer = clean(env.answer)
    env.how_calculated = clean(env.how_calculated)
    env.suggestions = [clean(s) for s in env.suggestions]
    env.notices = [clean(n) for n in env.notices]
    env.options = [clean(o) for o in env.options]
    for table in env.tables:
        if scrubber.rows([str(c) for c in table.get("columns") or []], table.get("rows") or []):
            removed.add("table_value")
    if removed:
        actions.append("removed: " + ", ".join(sorted(removed)))
    if actions:
        await _log(ctx, "output_check", "; ".join(actions))


def _decline(env: Any, message: str) -> None:
    env.status, env.answer = "declined", message
    env.how_calculated = ""
    env.tables, env.files, env.suggestions, env.notices, env.options = [], [], [], [], []
