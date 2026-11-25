"""Rolling conversation summary (gpt-oss), triggered when the turns not yet in the summary pass a token threshold.

The summary is written per topic (business area), so an earlier topic is not lost when the user moves to another one."""
from __future__ import annotations

import json
from typing import Any

from pydantic import BaseModel, Field

from ..llm.types import Message, ModelHandle
from ..runtime.retry import call_with_retry

ANSWER_CHARS = 1500
SUMMARY_MAX_TOKENS = 1000


class TurnRecord(BaseModel):
    turn_index: int
    question: str
    answer: str = ""
    domains: list[str] = Field(default_factory=list)  # business areas of the tables the answer used
    entities: list[str] = Field(default_factory=list)  # entity / period filters the answer's SQL used
    periods: list[str] = Field(default_factory=list)


def estimate_tokens(text: str) -> int:
    """Rough token count (about 4 characters per token); good enough for a threshold."""
    return (len(text) + 3) // 4


def context_tokens(summary: str | None, turns: list[TurnRecord]) -> int:
    return estimate_tokens(summary or "") + sum(estimate_tokens(t.question) + estimate_tokens(t.answer) for t in turns)


def needs_summary(summary: str | None, unsummarised: list[TurnRecord], threshold: int) -> bool:
    return bool(unsummarised) and context_tokens(summary, unsummarised) > threshold


def _filters(plan: Any) -> dict[str, list[str]]:
    if isinstance(plan, dict):
        data = plan
    else:
        try:
            data = json.loads(plan) if plan else {}
        except (TypeError, ValueError):
            data = {}
    if not isinstance(data, dict):
        return {}
    return {k: [str(v) for v in (data.get(k) or []) if str(v).strip()] for k in ("entities", "periods")}


def turns_from_rows(rows: list[dict[str, Any]]) -> list[TurnRecord]:
    out = []
    for r in rows:
        q = str(r.get("standalone_question") or r.get("question_text") or "").strip()
        if q:
            f = _filters(r.get("plan"))
            domains = [d.strip() for d in str(r.get("domain") or "").split(",") if d.strip()]
            out.append(TurnRecord(turn_index=int(r.get("turn_index") or 0), question=q, answer=str(r.get("answer_start") or ""),
                                  domains=domains, entities=f.get("entities", []), periods=f.get("periods", [])))
    return out


class ConversationSummarizer:
    def __init__(self, llm: ModelHandle, labels: dict[str, str] | None = None):
        from ..agents.specialists import load_prompt

        self.llm = llm
        self.labels = labels or {}  # domain -> business name (from the access file)
        self.system = load_prompt("summary")

    async def summarize(self, previous: str | None, turns: list[TurnRecord]) -> str:
        lines = [f"Previous summary:\n{previous.strip() if previous else '(none)'}", "", "Newer turns:"]
        for t in turns:
            topic = ", ".join(self.labels.get(d, d) for d in t.domains) or "general (no company data)"
            lines += [f"[{t.turn_index}] Topic: {topic}", f"[{t.turn_index}] User: {t.question}", f"[{t.turn_index}] Assistant: {t.answer[:ANSWER_CHARS]}", ""]
        result = await call_with_retry(
            lambda: self.llm.complete(self.system, [Message.user("\n".join(lines))], [], SUMMARY_MAX_TOKENS, 0.0)
        )
        return result.text.strip()


def fallback_seed(previous: str | None, turns: list[TurnRecord], limit: int = 5) -> str:
    """Seed for a new conversation when no model summary is available yet: the old summary plus recent questions."""
    parts = [previous.strip()] if previous else []
    recent = [f"- {t.question}" for t in turns[-limit:]]
    if recent:
        parts.append("Recent questions in the previous conversation:\n" + "\n".join(recent))
    return "\n\n".join(parts)
