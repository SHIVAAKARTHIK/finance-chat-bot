"""What the agents see of the conversation, chosen by tokens (not by a fixed number of questions), plus topic state.

- Recent turns: the newest turns that fit `budget` tokens, newest kept first (at least one turn). Long answers are
  shortened first, so one big table does not push every other turn out.
- Topic state: per business area (the domain of the tables an answer used, from the access file), which turns asked
  about it and the entities and periods those answers filtered on. Built in code from the stored message rows (domain
  and filters), so it costs no model call. The supervisor uses it to decide which earlier topic a follow-up belongs to.
"""
from __future__ import annotations

from pydantic import BaseModel, Field

from .summary import TurnRecord, estimate_tokens

ANSWER_CHARS = 1200  # an answer is shortened to this before it is shown again (tables are in the stored result anyway)
MAX_VALUES = 5  # entities / periods listed per topic


def shorten(text: str, chars: int = ANSWER_CHARS) -> str:
    text = (text or "").strip()
    return text if len(text) <= chars else text[:chars].rstrip() + " ..."


def turn_tokens(turn: TurnRecord) -> int:
    return estimate_tokens(turn.question) + estimate_tokens(shorten(turn.answer))


def select_recent(turns: list[TurnRecord], budget: int) -> list[TurnRecord]:
    """The newest turns whose total fits `budget` tokens, oldest first. The newest turn is always kept."""
    chosen: list[TurnRecord] = []
    used = 0
    for t in reversed(turns):
        cost = turn_tokens(t)
        if chosen and used + cost > budget:
            break
        chosen.append(t)
        used += cost
    return list(reversed(chosen))


class TopicState(BaseModel):
    domain: str
    label: str
    first_turn: int
    last_turn: int
    turns: int = 0
    entities: list[str] = Field(default_factory=list)
    periods: list[str] = Field(default_factory=list)
    last_question: str = ""


def _add(values: list[str], new: list[str]) -> list[str]:
    """Most recent first, no duplicates (case-insensitive), at most MAX_VALUES."""
    out = list(values)
    for v in new:
        key = v.strip().lower()
        if not key:
            continue
        out = [x for x in out if x.strip().lower() != key]
        out.insert(0, v.strip())
    return out[:MAX_VALUES]


def topic_states(turns: list[TurnRecord], labels: dict[str, str] | None = None) -> list[TopicState]:
    """One entry per domain asked about in `turns`, the most recently asked topic first."""
    labels = labels or {}
    states: dict[str, TopicState] = {}
    for t in sorted(turns, key=lambda x: x.turn_index):
        for d in t.domains:
            s = states.get(d)
            if s is None:
                s = states[d] = TopicState(domain=d, label=labels.get(d, d), first_turn=t.turn_index, last_turn=t.turn_index)
            s.last_turn = t.turn_index
            s.turns += 1
            s.last_question = t.question
            s.entities = _add(s.entities, t.entities)
            s.periods = _add(s.periods, t.periods)
    return sorted(states.values(), key=lambda s: s.last_turn, reverse=True)


def topics_text(states: list[TopicState]) -> str:
    if not states:
        return ""
    lines = ["Topics in this conversation (most recent first):"]
    for i, s in enumerate(states):
        span = f"turn {s.first_turn}" if s.first_turn == s.last_turn else f"turns {s.first_turn}-{s.last_turn}"
        parts = [f"- {s.label} [{s.domain}]" + (" (current topic)" if i == 0 else ""), span]
        if s.entities:
            parts.append("entities: " + ", ".join(s.entities))
        if s.periods:
            parts.append("periods: " + ", ".join(s.periods))
        parts.append(f"last question: {shorten(s.last_question, 200)}")
        lines.append("; ".join(parts))
    return "\n".join(lines)


def topic_label(turn: TurnRecord, labels: dict[str, str] | None = None) -> str:
    return ", ".join((labels or {}).get(d, d) for d in turn.domains)
