"""User memory: frequent entities and periods from the user's last 30 answered questions.

Used only as a hint when the user omits an entity and has a clear habit; the answer then says which one it assumed.
"""
from __future__ import annotations

import json
from collections import Counter
from typing import Any

from pydantic import BaseModel, Field

WINDOW = 30
HABIT_MIN_COUNT = 5  # asked at least this often in the window ...
HABIT_MIN_SHARE = 0.6  # ... and in at least this share of the questions that named an entity


class UserMemory(BaseModel):
    user_id: str
    frequent_entities: list[dict[str, Any]] = Field(default_factory=list)  # [{"entity": "...", "count": n}]
    default_entity: str | None = None
    default_period: str | None = None
    recent_window_size: int = WINDOW


def build_memory(user_id: str, plans: list[Any], window: int = WINDOW) -> UserMemory:
    """`plans`: the `plan` JSON of the user's last answered questions (newest first)."""
    entity_counts: Counter[str] = Counter()
    period_counts: Counter[str] = Counter()
    with_entity = with_period = 0
    for raw in plans[:window]:
        try:
            plan = json.loads(raw) if isinstance(raw, str) else (raw or {})
        except ValueError:
            continue
        ents = {str(e).strip() for e in plan.get("entities", []) if str(e).strip()}
        pers = {str(p).strip() for p in plan.get("periods", []) if str(p).strip()}
        if ents:
            with_entity += 1
            entity_counts.update(ents)
        if pers:
            with_period += 1
            period_counts.update(pers)

    def habit(counts: Counter[str], total: int) -> str | None:
        if not counts:
            return None
        value, n = counts.most_common(1)[0]
        return value if n >= HABIT_MIN_COUNT and n / max(total, 1) >= HABIT_MIN_SHARE else None

    return UserMemory(
        user_id=user_id,
        frequent_entities=[{"entity": e, "count": n} for e, n in entity_counts.most_common(5)],
        default_entity=habit(entity_counts, with_entity),
        default_period=habit(period_counts, with_period),
        recent_window_size=window,
    )


def memory_hint(mem: UserMemory | None) -> str | None:
    """Text for the supervisor / fast path. None when there is no clear habit."""
    if mem is None or not mem.default_entity:
        return None
    count = next((f["count"] for f in mem.frequent_entities if f["entity"] == mem.default_entity), 0)
    return (f"User habit (hint only): when the question names no entity, this user usually means "
            f"'{mem.default_entity}' ({count} of their last {mem.recent_window_size} questions). Use it only if the "
            f"question names no entity, and say in the answer that you assumed it.")


def assumed_entity_notice(mem: UserMemory | None, used_entities: list[str], question: str) -> str | None:
    """Fixed wording, added in code when the habit was applied to a question that did not name an entity."""
    if mem is None or not mem.default_entity:
        return None
    from ..tools.resolve import entity_score

    default = mem.default_entity
    if not any(entity_score(e, default) >= 0.85 for e in used_entities):
        return None  # the answer did not use the habitual entity
    if entity_score(question, default) >= 0.7:
        return None  # the user named it
    return (f"I assumed {default}, the entity you usually ask about, because the question did not name one. "
            "Ask again with another entity if you meant something else.")


def memory_row(mem: UserMemory, now: Any) -> dict[str, Any]:
    return {
        "user_id": mem.user_id,
        "frequent_kpis": None,
        "frequent_entities": json.dumps(mem.frequent_entities),
        "default_entity": mem.default_entity,
        "default_period": mem.default_period,
        "recent_window_size": mem.recent_window_size,
        "updated_at": now,
    }
