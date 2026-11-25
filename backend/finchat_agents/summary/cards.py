"""Card text (gpt-oss, number-checked) and the investigator for flagged changes (v3 SQL agent, 2 queries)."""
from __future__ import annotations

import json
from decimal import Decimal
from typing import Any

from pydantic import BaseModel, Field

from ..access.rbac import UserAccess
from ..agents.number_check import allowed_numbers, unsupported_numbers
from ..agents.specialists import load_prompt
from ..llm.types import ModelHandle
from ..runtime.agent import Agent
from ..runtime.tools import Budget, Counters, RunContext
from ..tools.run_sql import RESULTS_KEY
from ..tracing.tracer import Tracer
from .facts import Fact

INVESTIGATOR_SQL_BUDGET = 2
NO_CAUSE = "No cause found in 2 queries."

CARDS_SCHEMA = {
    "type": "object",
    "properties": {"cards": {"type": "array", "items": {"type": "object", "properties": {
        "fact_id": {"type": "string"}, "title": {"type": "string"}, "card_text": {"type": "string"}},
        "required": ["fact_id", "title", "card_text"]}}},
    "required": ["cards"],
}


class CardText(BaseModel):
    title: str
    card_text: str
    fallback: bool = False  # True when the model text failed the number check (plain wording used instead)


class Investigation(BaseModel):
    status: str  # explained | no_cause_found | failed
    explanation: str
    sql: list[str] = Field(default_factory=list)


def _fmt(v: Decimal | None) -> str:
    if v is None:
        return "n/a"
    q = v.quantize(Decimal("0.01")) if v != v.to_integral_value() else v.quantize(Decimal(1))
    return f"{q:,}"


def fact_numbers(f: Fact) -> list[Decimal]:
    texts = [f.metric_name, f.period_label or "", f.comparison_label or ""]
    extras = [v for v in (f.current_value, f.previous_value, f.change_abs, f.change_pct) if v is not None]
    return allowed_numbers([], extras, texts)


def plain_card(f: Fact) -> CardText:
    """Deterministic wording built from the fact only (used when the model text fails the number check)."""
    title = f.metric_name if len(f.metric_name) <= 60 else f.metric_name[:57] + "..."
    if f.change_abs is not None and f.previous_value is not None:
        pct = f" ({f.change_pct:+}%)" if f.change_pct is not None else ""
        text = (f"{f.metric_name} was {_fmt(f.current_value)} in {f.period_label}, compared with "
                f"{_fmt(f.previous_value)} in {(f.comparison_label or '').removeprefix('vs ')}{pct}.")
    else:
        text = f"{f.metric_name} was {_fmt(f.current_value)} in {f.period_label}."
    if f.notes:
        text += " The source has duplicate loads, so the figure may include duplicates."
    return CardText(title=title, card_text=text, fallback=True)


def _fact_payload(f: Fact) -> dict[str, Any]:
    return {
        "fact_id": f.fact_id, "name": f.metric_name, "period": f.period_label, "comparison": f.comparison_label,
        "current": f.current_value, "previous": f.previous_value, "change": f.change_abs, "change_pct": f.change_pct,
        "card_type": f.card_type, "notes": f.notes,
    }


class CardWriter:
    def __init__(self, llm: ModelHandle):
        self.agent = Agent("summary_card_writer", load_prompt("summary_cards"), llm, [], output_schema=CARDS_SCHEMA,
                           max_steps=2, max_tokens=3000, temperature=0.2)

    async def write(self, facts: list[Fact], ctx: RunContext) -> dict[str, CardText]:
        out: dict[str, CardText] = {}
        if not facts:
            return out
        try:
            result = await self.agent.run(
                "Write one card per fact:\n" + json.dumps([_fact_payload(f) for f in facts], default=str, indent=1), ctx)
            cards = (result.data or {}).get("cards") or []
        except Exception:  # the model is unavailable: plain cards keep the run going
            cards = []
        by_id = {f.fact_id: f for f in facts}
        for c in cards:
            f = by_id.get(str(c.get("fact_id")))
            if f is None or f.fact_id in out:
                continue
            title, text = str(c.get("title") or "").strip(), str(c.get("card_text") or "").strip()
            if title and text and not unsupported_numbers(f"{title}\n{text}", fact_numbers(f)):
                out[f.fact_id] = CardText(title=title[:120], card_text=text)
        for f in facts:
            out.setdefault(f.fact_id, plain_card(f))
        return out


def investigation_task(f: Fact) -> str:
    return (
        f"Explain this change. {f.metric_name}: {_fmt(f.current_value)} in {f.period_label}, "
        f"{_fmt(f.previous_value)} {f.comparison_label or ''} (change {_fmt(f.change_abs)}, {f.change_pct}%). "
        f"Find which accounts, sources or entities drove it. Source tables: {', '.join(f.source_tables)}. "
        f"You may run at most {INVESTIGATOR_SQL_BUDGET} queries. If they do not show a clear cause, set status to "
        "no_data and say no cause was found."
    )


async def investigate(sql_agent: Agent, f: Fact, access: UserAccess, tracer: Tracer) -> Investigation:
    ctx = RunContext(tracer=tracer, budget=Budget(max_sql_calls=INVESTIGATOR_SQL_BUDGET, max_steps=6, max_seconds=180),
                     counters=Counters(), user=access)
    try:
        result = await sql_agent.run(investigation_task(f), ctx)
    except Exception as exc:
        return Investigation(status="failed", explanation=f"The investigation could not run ({type(exc).__name__}).")
    sql = [r.sql for r in ctx.extras.get(RESULTS_KEY, {}).values()][:INVESTIGATOR_SQL_BUDGET]
    data = result.data or {}
    answer = str(data.get("answer") or "").strip()
    if result.status != "final" or data.get("status") != "ok" or not answer:
        return Investigation(status="no_cause_found", explanation=NO_CAUSE, sql=sql)
    allowed = allowed_numbers(ctx.extras.get(RESULTS_KEY, {}).values(), [], [investigation_task(f)])
    if unsupported_numbers(answer, allowed):
        return Investigation(status="failed", explanation="The explanation could not be checked against the data.", sql=sql)
    return Investigation(status="explained", explanation=answer, sql=sql)
