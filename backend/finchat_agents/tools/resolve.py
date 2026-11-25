"""resolve_period / resolve_entity: turn what the user typed into filter values that exist in the data.

Suggestions only: they never filter by access (the domain check still applies to the lookups themselves).
Period and entity columns come from the table pages; when a table only holds a key (PERIOD_KEY, LEGAL_ENTITY_KEY),
the lookup follows an approved join to the dimension that holds the labels.
"""
from __future__ import annotations

import asyncio
import calendar
import datetime as dt
import difflib
import re
from dataclasses import dataclass, field
from typing import Any

from ..access.rbac import UserAccess
from ..knowledge.models import TablePage
from ..llm.types import ToolSpec
from ..runtime.tools import Tool, ToolContext, ToolError
from .catalog import column_values, visible_table
from .deps import DataDeps, access_of
from .run_sql import execute_guarded

MONTHS = {name.lower(): i for i, name in enumerate(calendar.month_abbr) if name}
MONTHS.update({name.lower(): i for i, name in enumerate(calendar.month_name) if name})
MONTHS["sept"] = 9
_MONTH_RE = "|".join(sorted(MONTHS, key=len, reverse=True))
DATE_TYPES = ("date", "timestamp")
PERIOD_ROWS_LIMIT = 2000


def _is_key(col: str) -> bool:
    return col.upper().endswith("_KEY")


def _year(y: str) -> int:
    n = int(y)
    return 2000 + n if n < 100 else n


# ---------------------------------------------------------------- period text parsing

@dataclass
class PeriodSpec:
    kind: str  # latest | months | fiscal | label | unknown
    months: set[tuple[int, int]] = field(default_factory=set)
    fiscal: tuple[int, int] | None = None
    text: str = ""
    interpretation: str = ""


def _quarter_months(year: int, q: int) -> set[tuple[int, int]]:
    return {(year, m) for m in range(3 * q - 2, 3 * q + 1)}


def _prev_month(d: dt.date) -> tuple[int, int]:
    return (d.year - 1, 12) if d.month == 1 else (d.year, d.month - 1)


def parse_period(text: str, today: dt.date) -> PeriodSpec:
    t = " ".join(text.lower().replace(",", " ").split())
    if re.search(r"\b(latest|current|most recent|this period)\b", t):
        return PeriodSpec("latest", text=text, interpretation="latest period with data")
    if re.search(r"\b(last|previous|prior) month\b", t):
        m = _prev_month(today)
        return PeriodSpec("months", {m}, text=text, interpretation=f"{calendar.month_abbr[m[1]]} {m[0]} (calendar month before today)")
    if re.search(r"\bthis month\b", t):
        return PeriodSpec("months", {(today.year, today.month)}, text=text, interpretation="this calendar month")
    if re.search(r"\b(last|previous|prior) quarter\b", t):
        q = (today.month - 1) // 3 + 1
        y, q = (today.year - 1, 4) if q == 1 else (today.year, q - 1)
        return PeriodSpec("months", _quarter_months(y, q), text=text, interpretation=f"Q{q} {y} (calendar quarter before today)")
    if re.search(r"\bthis quarter\b", t):
        q = (today.month - 1) // 3 + 1
        return PeriodSpec("months", _quarter_months(today.year, q), text=text, interpretation=f"Q{q} {today.year}")
    if re.search(r"\b(last|previous|prior) year\b", t):
        y = today.year - 1
        return PeriodSpec("months", {(y, m) for m in range(1, 13)}, text=text, interpretation=f"calendar year {y}")
    if re.search(r"\b(this year|ytd|year to date)\b", t):
        return PeriodSpec("months", {(today.year, m) for m in range(1, today.month + 1)}, text=text,
                          interpretation=f"{today.year} up to {calendar.month_abbr[today.month]}")
    if m := re.search(r"\bfy\s*'?(\d{2,4})\s*[-/ ]?\s*p(?:eriod)?\s*(\d{1,2})\b", t):
        fy, p = _year(m.group(1)), int(m.group(2))
        return PeriodSpec("fiscal", fiscal=(fy, p), text=text, interpretation=f"fiscal year {fy}, period {p}")
    if m := re.search(r"\bp(?:eriod)?\s*(\d{1,2})\s*(?:of\s*)?(?:fy)?\s*'?(\d{4}|\d{2})\b", t):
        fy, p = _year(m.group(2)), int(m.group(1))
        return PeriodSpec("fiscal", fiscal=(fy, p), text=text, interpretation=f"fiscal year {fy}, period {p}")
    if m := re.search(r"\bq([1-4])\s*'?(\d{4}|\d{2})\b", t) or re.search(r"\b(\d{4})\s*q([1-4])\b", t):
        a, b = m.group(1), m.group(2)
        q, y = (int(a), _year(b)) if len(a) == 1 else (int(b), _year(a))
        return PeriodSpec("months", _quarter_months(y, q), text=text, interpretation=f"Q{q} {y}")
    if m := re.search(r"\b(\d{4})-(\d{1,2})\b", t):
        y, mo = int(m.group(1)), int(m.group(2))
        if 1 <= mo <= 12:
            return PeriodSpec("months", {(y, mo)}, text=text, interpretation=f"{calendar.month_abbr[mo]} {y}")
    if m := re.search(r"\b(\d{1,2})/(\d{4})\b", t):
        mo, y = int(m.group(1)), int(m.group(2))
        if 1 <= mo <= 12:
            return PeriodSpec("months", {(y, mo)}, text=text, interpretation=f"{calendar.month_abbr[mo]} {y}")
    if m := re.search(rf"\b({_MONTH_RE})\.?\s*'?(\d{{4}}|\d{{2}})\b", t):
        mo, y = MONTHS[m.group(1)], _year(m.group(2))
        return PeriodSpec("months", {(y, mo)}, text=text, interpretation=f"{calendar.month_abbr[mo]} {y}")
    if m := re.search(r"\b(20\d{2})\b", t):
        y = int(m.group(1))
        return PeriodSpec("months", {(y, mo) for mo in range(1, 13)}, text=text, interpretation=f"calendar year {y}")
    return PeriodSpec("label", text=text, interpretation="matched against period labels")


# ---------------------------------------------------------------- period rows from the data

def _period_table(deps: DataDeps, page: TablePage) -> TablePage:
    cols = page.meta.period_columns
    if cols and not all(_is_key(c) for c in cols):
        return page
    for j in deps.kb.joins:
        if j.status != "approved" or page.id not in (j.from_, j.to):
            continue
        other = deps.kb.tables[j.other(page.id)]
        if other.meta.period_columns and not all(_is_key(c) for c in other.meta.period_columns):
            return other
    raise ToolError(f"{page.meta.fqn} has no period columns; it cannot be filtered by period.")


def _as_date(v: Any) -> dt.date | None:
    if isinstance(v, dt.datetime):
        return v.date()
    if isinstance(v, dt.date):
        return v
    if v is None:
        return None
    try:
        return dt.date.fromisoformat(str(v)[:10])
    except ValueError:
        return None


def _as_int(v: Any) -> int | None:
    try:
        return int(str(v).strip())
    except (TypeError, ValueError):
        return None


@dataclass
class PeriodRow:
    values: dict[str, Any]
    month: tuple[int, int] | None
    fiscal: tuple[int, int] | None
    label: str


async def _period_rows(deps: DataDeps, access: UserAccess, page: TablePage) -> list[PeriodRow]:
    key = ("periods", page.id)
    cached = deps.cache.get(key)
    if cached is not None:
        return cached
    cols = [c for c in page.meta.period_columns if not _is_key(c)]
    types = {c: (page.column(c).type if page.column(c) else "string").lower() for c in cols}
    select = []
    for c in cols:
        if types[c].startswith(DATE_TYPES):
            select.append(f"CAST(date_trunc('MONTH', TRY_CAST(`{c}` AS DATE)) AS DATE) AS `{c}`")
        else:
            select.append(f"`{c}`")
    sql = f"SELECT DISTINCT {', '.join(select)} FROM {page.meta.fqn} LIMIT {PERIOD_ROWS_LIMIT}"
    result = await execute_guarded(sql, deps, access)
    date_cols = [c for c in cols if types[c].startswith(DATE_TYPES)]
    year_col = next((c for c in cols if "YEAR" in c.upper() and not types[c].startswith(DATE_TYPES)), None)
    num_col = next((c for c in cols if re.fullmatch(r"(.*_)?PERIOD(_NUMBER|_NO)?", c.upper()) and c != year_col), None)
    label_col = next((c for c in cols if c not in date_cols and c not in (year_col, num_col)), None)
    rows: list[PeriodRow] = []
    seen = set()
    for r in result.rows:
        values = dict(zip(result.columns, r))
        month = None
        for c in date_cols:
            d = _as_date(values.get(c))
            if d:
                month = (d.year, d.month)
                break
        fiscal = None
        if year_col and num_col:
            fy, p = _as_int(values.get(year_col)), _as_int(values.get(num_col))
            if fy is not None and p is not None:
                fiscal = (fy, p)
        if label_col and values.get(label_col) not in (None, ""):
            label = str(values[label_col]).strip()
        elif fiscal:
            label = f"FY{fiscal[0]} P{fiscal[1]}"
        elif month:
            label = f"{calendar.month_abbr[month[1]]} {month[0]}"
        else:
            continue
        sig = (label, month, fiscal)
        if sig in seen:
            continue
        seen.add(sig)
        rows.append(PeriodRow(values, month, fiscal, label))
    deps.cache.set(key, rows)
    return rows


def _norm(s: str) -> str:
    return " ".join(re.sub(r"[^a-z0-9]+", " ", s.lower()).split())


def _filters(row: PeriodRow, page: TablePage) -> dict[str, str]:
    out = {}
    for c in page.meta.period_columns:
        if _is_key(c) or c not in row.values:
            continue
        col = page.column(c)
        if col and col.type.lower().startswith(DATE_TYPES) and row.month:
            y, m = row.month
            last = calendar.monthrange(y, m)[1]
            out[c] = f"between {y}-{m:02d}-01 and {y}-{m:02d}-{last}"
        else:
            out[c] = str(row.values[c]).strip()
    return out


async def resolve_period(deps: DataDeps, access: UserAccess, text: str, table: str) -> dict[str, Any]:
    page = visible_table(deps, access, table)
    ptable = _period_table(deps, page)
    if not access.role.allows_domain(ptable.meta.domain):  # type: ignore[union-attr]
        raise ToolError(f"Access denied: period labels live in {ptable.meta.fqn}, outside this user's domains.")
    today = deps.today() if deps.today else dt.date.today()
    spec = parse_period(text, today)
    rows = await _period_rows(deps, access, ptable)
    ordered = sorted(rows, key=lambda r: (r.month or (0, 0), r.fiscal or (0, 0)))
    if spec.kind == "latest":
        top = ordered[-1:] if ordered else []
        key = (top[0].month, top[0].fiscal) if top else None
        matches = [r for r in ordered if (r.month, r.fiscal) == key]
    elif spec.kind == "fiscal":
        matches = [r for r in ordered if r.fiscal == spec.fiscal]
    elif spec.kind == "months":
        matches = [r for r in ordered if r.month in spec.months]
    else:
        matches = []
    if not matches:  # also try the raw text against labels ("Feb 25", "FY2026 P9")
        nt = _norm(text)
        matches = [r for r in ordered if _norm(r.label) == nt]
    available = list(dict.fromkeys(r.label for r in reversed(ordered)))[:12]
    out: dict[str, Any] = {
        "table": page.meta.fqn,
        "period_table": ptable.meta.fqn,
        "interpretation": spec.interpretation,
        "matches": [{"label": r.label, "filters": _filters(r, ptable)} for r in matches][:24],
        "available_latest_first": available,
    }
    if ptable.id != page.id:
        out["note"] = f"Filter through {ptable.meta.fqn} with the approved join (get_join_path)."
    if not matches:
        out["note"] = f"No data for '{text}'. Say so to the user and offer the available periods; do not substitute another period."
    return out


# ---------------------------------------------------------------- entities

_SUFFIXES = {"llc", "inc", "ltd", "plc", "the", "co", "corp", "corporation", "limited", "company", "gmbh", "sa", "bv"}


def norm_entity(s: str) -> str:
    s = re.sub(r"[^a-z0-9]+", " ", str(s).lower())
    s = re.sub(r"(?<=[a-z])0+(?=\d)", "", s)  # uk03 -> uk3
    s = re.sub(r"\b0+(\d)", r"\1", s)  # 0561 -> 561
    return " ".join(w for w in s.split() if w not in _SUFFIXES)


def entity_score(text: str, value: str) -> float:
    t, v = norm_entity(text), norm_entity(value)
    if not t or not v:
        return 0.0
    if t == v:
        return 1.0
    tw, vw = set(t.split()), set(v.split())
    if vw <= tw or tw <= vw:  # "561 - Cars USA Shipping, LLC" contains "Cars USA Shipping" / code "561"
        return 0.9 if len(vw) > 1 or len(tw) == 1 else 0.85
    if f" {v} " in f" {t} " or f" {t} " in f" {v} ":
        return 0.8
    words = {w for w in vw if not w.isdigit()}
    if words and words <= tw:  # "Northwind accounts in Feb 25" names "100-Northwind" without its code
        return 0.7
    ratio = difflib.SequenceMatcher(None, t, v).ratio()
    return round(ratio * 0.75, 3) if ratio >= 0.8 else 0.0


def _entity_table(deps: DataDeps, page: TablePage) -> TablePage:
    ec = page.meta.entity_column
    if ec and not _is_key(ec):
        return page
    for j in deps.kb.joins:
        if j.status != "approved" or page.id not in (j.from_, j.to):
            continue
        other = deps.kb.tables[j.other(page.id)]
        if other.meta.entity_column and not _is_key(other.meta.entity_column):
            return other
    raise ToolError(f"{page.meta.fqn} has no entity column; it cannot be filtered by entity.")


def _entity_columns(page: TablePage) -> list[str]:
    cols = [page.meta.entity_column] if page.meta.entity_column else []
    for c in page.columns:
        text = " ".join([c.meaning, *c.synonyms]).lower()
        if c.name not in cols and not c.pii and "NAME" in c.name.upper() and ("entity" in text or "company" in text):
            cols.append(c.name)
    return cols  # type: ignore[return-value]


async def resolve_entity(deps: DataDeps, access: UserAccess, text: str, table: str) -> dict[str, Any]:
    page = visible_table(deps, access, table)
    etable = _entity_table(deps, page)
    matches = []
    for col in _entity_columns(etable):
        vals = await column_values(deps, access, etable.id, col, limit=500)
        for v in vals["values"]:
            if v["value"] in (None, ""):
                continue
            score = entity_score(text, str(v["value"]))
            if score > 0:
                matches.append({"column": col, "value": str(v["value"]).strip(), "score": score, "rows": v["rows"]})
    matches.sort(key=lambda m: (-m["score"], m["column"], m["value"]))
    out: dict[str, Any] = {"table": page.meta.fqn, "entity_table": etable.meta.fqn, "matches": matches[:10]}
    if etable.id != page.id:
        out["note"] = f"Filter on {etable.meta.fqn} and join it with the approved join (get_join_path)."
    if not matches:
        out["note"] = f"No entity matches '{text}'. Tell the user it was not found; list values with get_column_values."
    elif len({(m['column'], m['value']) for m in matches if m['score'] >= matches[0]['score']}) > 1 and matches[0]["score"] < 1:
        out["ambiguous"] = True
    return out


# ---------------------------------------------------------------- preload

async def prewarm_lookups(deps: DataDeps, access: UserAccess, *, concurrency: int = 4) -> dict[str, int]:
    """Fill the entity-value and period caches for every table that has them, with the same functions and cache keys the
    resolvers use, so the first question does not pay for these queries. Failures are skipped (the resolvers will retry)."""
    entity_jobs: dict[str, list[str]] = {}
    period_tables: dict[str, TablePage] = {}
    for page in deps.kb.tables.values():
        try:
            etable = _entity_table(deps, page)
            entity_jobs.setdefault(etable.id, _entity_columns(etable))
        except ToolError:
            pass
        try:
            ptable = _period_table(deps, page)
            if access.role.allows_domain(ptable.meta.domain):
                period_tables.setdefault(ptable.id, ptable)
        except ToolError:
            pass
    sem = asyncio.Semaphore(concurrency)
    done = {"entities": 0, "periods": 0, "failed": 0}

    async def run(kind: str, coro: Any) -> None:
        async with sem:
            try:
                await coro
                done[kind] += 1
            except Exception:  # noqa: BLE001 - preloading is best effort
                done["failed"] += 1

    jobs = [run("entities", column_values(deps, access, tid, col, limit=500))
            for tid, cols in entity_jobs.items() for col in cols]
    jobs += [run("periods", _period_rows(deps, access, t)) for t in period_tables.values()]
    await asyncio.gather(*jobs)
    return done


# ---------------------------------------------------------------- tools

def make_resolve_tools(deps: DataDeps) -> list[Tool]:
    async def period_handler(args: dict[str, Any], tctx: ToolContext) -> dict[str, Any]:
        text = str(args.get("text") or "").strip()
        if not text:
            raise ToolError("Give the period text the user wrote, e.g. 'Feb 25' or 'last quarter'.")
        return await resolve_period(deps, access_of(tctx), text, str(args.get("table") or ""))

    async def entity_handler(args: dict[str, Any], tctx: ToolContext) -> dict[str, Any]:
        text = str(args.get("text") or "").strip()
        if not text:
            raise ToolError("Give the entity text the user wrote, e.g. 'Cars USA Shipping' or 'UK3'.")
        return await resolve_entity(deps, access_of(tctx), text, str(args.get("table") or ""))

    schema = {
        "type": "object",
        "properties": {
            "text": {"type": "string", "description": "What the user wrote."},
            "table": {"type": "string", "description": "The table you will query."},
        },
        "required": ["text", "table"],
    }
    return [
        Tool(ToolSpec(
            name="resolve_period",
            description="Map a period the user wrote (Feb 25, February 2025, 2025-02, FY2026 P9, latest, last quarter) "
                        "to filter values that exist for the table. Returns matching periods with column filters, "
                        "and the latest available periods. Relative periods count from today's date.",
            input_schema=schema,
        ), period_handler),
        Tool(ToolSpec(
            name="resolve_entity",
            description="Match an entity the user wrote (code or name, fuzzy: 'UK3' = 'UK03', punctuation and LLC "
                        "ignored) to stored entity values for the table. Returns candidate column/value pairs with scores.",
            input_schema=schema,
        ), entity_handler),
    ]
