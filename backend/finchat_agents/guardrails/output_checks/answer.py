"""The answer check, applied to every answer before it leaves: fixed replies are made exact, the could-not-answer
marker never reaches the user, disallowed content is removed from all text and table values (in code), and the
optional Bedrock Guardrail judges the answer text."""
from __future__ import annotations

import asyncio
from typing import Any

from ...runtime.tools import RunContext
from ..audit import log_check
from ..bedrock import ContentFilterError
from ..loader import Guardrails
from ..replies import COULD_NOT_ANSWER_TEXT, UNAVAILABLE_TEXT, refusal_message
from .filters import UNMASK, Scrubber

MODEL_TEXT_STATUSES = ("answered", "partial", "clarification")  # others hold only fixed replies


def _norm(text: str) -> str:
    return " ".join(text.replace("’", "'").replace('"', "").split()).casefold()


async def check_output(env: Any, guardrails: Guardrails, scrubber: Scrubber, ctx: RunContext) -> None:
    actions: list[str] = []
    answer = _norm(env.answer or "")
    for kind in ("confidential", "out_of_scope", "disallowed"):
        message = refusal_message(guardrails, kind)
        if message and _norm(message) in answer:
            _decline(env, message)
            await log_check(ctx, "output_check", f"fixed reply: {kind}")
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
    offered = [s for s in env.suggestions if not UNMASK.search(s)]
    if len(offered) != len(env.suggestions):
        removed.add("suggestion")
    env.suggestions = [clean(s) for s in offered]
    env.notices = [clean(n) for n in env.notices]
    env.options = [clean(o) for o in env.options]
    for table in env.tables:
        if scrubber.rows([str(c) for c in table.get("columns") or []], table.get("rows") or []):
            removed.add("table_value")
    if removed:
        actions.append("removed: " + ", ".join(sorted(removed)))
    if actions:
        await log_check(ctx, "output_check", "; ".join(actions))
    await _content(env, guardrails, ctx)


async def _content(env: Any, guardrails: Guardrails, ctx: RunContext) -> None:
    """Bedrock Guardrail on the answer and its explanation. Fails closed: an unchecked answer is not shown."""
    if guardrails.content_filter is None or env.status not in MODEL_TEXT_STATUSES:
        return
    fields = [name for name in ("answer", "how_calculated") if getattr(env, name)]
    try:
        results = await asyncio.gather(*(guardrails.content_filter.apply(getattr(env, n), "OUTPUT") for n in fields))
    except ContentFilterError as exc:
        _decline(env, UNAVAILABLE_TEXT)
        env.status = "failed"
        await log_check(ctx, "content_filter_output", f"failed: {exc}", "error")
        return
    blocked = next((r for r in results if r.blocked), None)
    if blocked is not None:
        _decline(env, blocked.text or refusal_message(guardrails, "harmful"))
        await log_check(ctx, "content_filter_output", "blocked")
        return
    for name, result in zip(fields, results):
        if result.changed:
            setattr(env, name, result.text)
    await log_check(ctx, "content_filter_output", "masked" if any(r.changed for r in results) else "allow")


def _decline(env: Any, message: str) -> None:
    env.status, env.answer = "declined", message
    env.how_calculated = ""
    env.tables, env.files, env.suggestions, env.notices, env.options = [], [], [], [], []
