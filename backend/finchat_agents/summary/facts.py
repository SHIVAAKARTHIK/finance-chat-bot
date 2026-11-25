"""Collect facts (code, config-driven) and rank / select them.

Each metric SQL runs for the current and the previous period of every scope (e.g. entity) through run_sql's
guardrails with the service role. A fact = one metric (or one group of it) for one scope: current and previous value,
change and its labels. Ranking and flagging are plain code with thresholds from config.
"""
from __future__ import annotations

import datetime as dt
import re
import uuid
from decimal import Decimal
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field

from ..access.rbac import UserAccess
from ..runtime.tools import ToolError
from ..tools.deps import DataDeps
from ..tools.run_sql import execute_guarded


class Thresholds(BaseModel):
    min_change_pct: float = 10
    flag_change_pct: float = 25
    min_abs: float = 1
    top_n: int = 5


class MetricSpec(BaseModel):
    id: str
    domain: str
    name: str
    periods: str
    tables: list[str] = Field(default_factory=list)
    sql: str
    min_abs: float | None = None
    min_change_pct: float | None = None
    flag_change_pct: float | None = None


class SummaryConfig(BaseModel):
    defaults: Thresholds = Field(default_factory=Thresholds)
    period_sets: dict[str, dict[str, str]]
    metrics: list[MetricSpec]

    def thresholds(self, m: MetricSpec) -> Thresholds:
        d = self.defaults
        return Thresholds(
            min_change_pct=m.min_change_pct if m.min_change_pct is not None else d.min_change_pct,
            flag_change_pct=m.flag_change_pct if m.flag_change_pct is not None else d.flag_change_pct,
            min_abs=m.min_abs if m.min_abs is not None else d.min_abs,
            top_n=d.top_n,
        )

    @property
    def domains(self) -> list[str]:
        return list(dict.fromkeys(m.domain for m in self.metrics))


def load_config(path: Path | str) -> SummaryConfig:
    cfg = SummaryConfig.model_validate(yaml.safe_load(Path(path).read_text(encoding="utf-8")))
    missing = [m.id for m in cfg.metrics if m.periods not in cfg.period_sets]
    if missing:
        raise ValueError(f"metrics refer to unknown period sets: {missing}")
    return cfg


class Fact(BaseModel):
    fact_id: str = Field(default_factory=lambda: uuid.uuid4().hex[:8])
    metric_id: str
    domain: str
    metric_name: str  # business name incl. scope and group, e.g. "Reconciliations not finalized: Cars USA Shipping, LLC"
    scope: str | None = None
    group: str | None = None
    period_label: str | None = None
    comparison_label: str | None = None
    current_value: Decimal | None = None
    previous_value: Decimal | None = None
    change_abs: Decimal | None = None
    change_pct: Decimal | None = None
    source_tables: list[str] = Field(default_factory=list)
    notes: list[str] = Field(default_factory=list)
    selected: bool = False
    flagged: bool = False
    card_type: str = "status"  # key_change | status | highlight
    rank: int = 0


_PLACEHOLDER = re.compile(r"\{(\w+)\}")


def sql_literal(v: Any) -> str:
    if v is None:
        return "NULL"
    if isinstance(v, bool):
        return "TRUE" if v else "FALSE"
    if isinstance(v, (int, Decimal)) or (isinstance(v, float) and v == v):
        return str(v)
    if isinstance(v, (dt.date, dt.datetime)):
        return "'" + v.isoformat()[:10 if type(v) is dt.date else 19] + "'"
    return "'" + str(v).replace("'", "''") + "'"


def render(template: str, values: dict[str, Any]) -> str:
    def sub(m: re.Match) -> str:
        key = m.group(1)
        if key not in values:
            raise KeyError(f"placeholder {{{key}}} has no value (period columns: {sorted(values)})")
        return sql_literal(values[key])

    return _PLACEHOLDER.sub(sub, template)


def _num(v: Any) -> Decimal | None:
    if v is None:
        return None
    try:
        return Decimal(str(v))
    except Exception:
        return None


async def _periods(sql: str, deps: DataDeps, access: UserAccess) -> dict[str | None, list[dict[str, Any]]]:
    """Newest two periods per scope."""
    res = await execute_guarded(sql, deps, access)
    by_scope: dict[str | None, list[dict[str, Any]]] = {}
    for rec in res.records():
        by_scope.setdefault(rec.get("scope"), []).append(rec)
    for scope, rows in by_scope.items():
        rows.sort(key=lambda r: str(r.get("sort_key") or ""), reverse=True)
        by_scope[scope] = rows[:2]
    return by_scope


async def _values(sql: str, deps: DataDeps, access: UserAccess) -> tuple[dict[str | None, Decimal | None], list[str]]:
    res = await execute_guarded(sql, deps, access)
    out: dict[str | None, Decimal | None] = {}
    for rec in res.records():
        out[str(rec["grp"]) if "grp" in rec and rec["grp"] is not None else None] = _num(rec.get("value"))
    notes = [n for n in res.notes if "duplicate" in n.lower()]
    return out, notes


async def collect_facts(cfg: SummaryConfig, deps: DataDeps, access: UserAccess, domains: list[str] | None = None,
                        errors: list[str] | None = None) -> list[Fact]:
    errors = errors if errors is not None else []
    facts: list[Fact] = []
    period_cache: dict[str, dict[str | None, list[dict[str, Any]]]] = {}
    for m in cfg.metrics:
        if domains and m.domain not in domains:
            continue
        try:
            if m.periods not in period_cache:
                period_cache[m.periods] = await _periods(cfg.period_sets[m.periods]["sql"], deps, access)
            if not period_cache[m.periods]:  # nothing to compare: not a quiet "complete" (the old cards would be replaced by nothing)
                raise ToolError("no periods with data (check the period query and the data)")
            for scope, rows in period_cache[m.periods].items():
                current, previous = rows[0], (rows[1] if len(rows) > 1 else None)
                cur_vals, notes = await _values(render(m.sql, current), deps, access)
                prev_vals: dict[str | None, Decimal | None] = {}
                if previous is not None:
                    prev_vals, more = await _values(render(m.sql, previous), deps, access)
                    notes += more
                for grp in dict.fromkeys([*cur_vals, *prev_vals]):
                    cur, prev = cur_vals.get(grp), prev_vals.get(grp) if previous is not None else None
                    if grp in cur_vals and cur is None:
                        continue  # no value for this period (e.g. SUM over no rows): no card instead of "not available"
                    if previous is not None and grp not in prev_vals:
                        prev = Decimal(0)  # the group did not exist in the previous period
                    name = m.name + (f": {grp}" if grp else "") + (f" ({scope})" if scope else "")
                    fact = Fact(metric_id=m.id, domain=m.domain, metric_name=name, scope=scope, group=grp,
                                period_label=str(current.get("label") or ""), source_tables=m.tables,
                                comparison_label=f"vs {previous.get('label')}" if previous is not None else None,
                                current_value=cur if grp in cur_vals else Decimal(0), previous_value=prev,
                                notes=list(dict.fromkeys(notes)))
                    if fact.previous_value is not None and fact.current_value is not None:
                        fact.change_abs = fact.current_value - fact.previous_value
                        if fact.previous_value != 0:
                            fact.change_pct = (fact.change_abs / abs(fact.previous_value) * 100).quantize(Decimal("0.1"))
                    facts.append(fact)
        except (ToolError, KeyError) as exc:  # one broken metric must not stop the run
            errors.append(f"{m.id}: {exc}")
    return facts


def rank_and_select(facts: list[Fact], cfg: SummaryConfig) -> list[Fact]:
    """Key changes above the thresholds first, then status facts to fill top_n per domain. Key-change order: flagged real
    changes (largest |change_pct| first), then values new from zero (no percentage), then the smaller real changes."""
    specs = {m.id: m for m in cfg.metrics}
    selected: list[Fact] = []
    for domain in dict.fromkeys(f.domain for f in facts):
        changes, status = [], []
        for f in (f for f in facts if f.domain == domain):
            th = cfg.thresholds(specs[f.metric_id])
            if f.change_abs is None:
                status.append(f)
                continue
            big_abs = abs(f.change_abs) >= Decimal(str(th.min_abs))
            pct = abs(f.change_pct) if f.change_pct is not None else None
            if big_abs and (pct is None or pct >= Decimal(str(th.min_change_pct))):
                f.card_type = "key_change"
                f.flagged = pct is not None and pct >= Decimal(str(th.flag_change_pct))
                changes.append(f)
        changes.sort(key=lambda f: (0 if f.flagged else (1 if f.change_pct is None else 2),
                                    -(abs(f.change_pct) if f.change_pct is not None else Decimal(0)), -abs(f.change_abs or 0)))
        status.sort(key=lambda f: (f.metric_id, f.metric_name))
        top_n = cfg.defaults.top_n
        chosen = changes[:top_n] + status[: max(0, top_n - len(changes[:top_n]))]
        for rank, f in enumerate(chosen, 1):
            f.selected, f.rank = True, rank
            if f.card_type != "key_change":
                f.card_type = "status"
        selected += chosen
    return selected
