"""Numbers in the final answer must come from tool results (SPEC 4.6). Rounding is allowed to the precision shown.

Allowed sources: every cell of the question's query results (and row counts, and column totals), calculate outputs,
general-knowledge texts the supervisor received, and the user's question (account numbers, years, "top 5").
"""
from __future__ import annotations

import datetime as dt
import re
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from typing import Any, Iterable

_NUM = re.compile(
    r"(?<![\w.])(?P<sign>[-−])?\(?(?P<num>\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)\)?"
    r"(?P<pct>\s?%)?(?:\s?(?P<scale>million|billion|thousand|mn|bn|m|k)\b)?",
    re.IGNORECASE,
)
_SCALES = {"thousand": 1_000, "k": 1_000, "million": 1_000_000, "mn": 1_000_000, "m": 1_000_000,
           "billion": 1_000_000_000, "bn": 1_000_000_000}


@dataclass
class FoundNumber:
    text: str
    value: Decimal
    decimals: int
    is_pct: bool


def extract_numbers(text: str) -> list[FoundNumber]:
    found = []
    for m in _NUM.finditer(text or ""):
        raw = m.group("num")
        try:
            value = Decimal(raw.replace(",", ""))
        except InvalidOperation:
            continue
        decimals = len(raw.split(".")[1]) if "." in raw else 0
        scale = (m.group("scale") or "").lower()
        if scale:
            value *= _SCALES[scale]
            decimals -= len(str(_SCALES[scale])) - 1  # "22.8 million" is precise to 0.1 million
        whole = m.group(0).strip()
        if m.group("sign") or (whole.startswith("(") and whole.endswith(")")):
            value = -value
        found.append(FoundNumber(whole, value, decimals, bool(m.group("pct"))))
    return found


def _cell_numbers(v: Any) -> list[Decimal]:
    if v is None or isinstance(v, bool):
        return []
    if isinstance(v, (int, float, Decimal)):
        try:
            return [Decimal(str(v))]
        except InvalidOperation:
            return []
    if isinstance(v, (dt.date, dt.datetime)):
        v = v.isoformat()
    if isinstance(v, (list, tuple)):
        return [x for item in v for x in _cell_numbers(item)]
    if isinstance(v, dict):
        return [x for item in v.values() for x in _cell_numbers(item)]
    return [n.value for n in extract_numbers(str(v))]


def allowed_numbers(results: Iterable[Any], extras: Iterable[Any] = (), texts: Iterable[str] = ()) -> list[Decimal]:
    """`results`: SqlResult-like objects (columns, rows); `extras`: calculate outputs; `texts`: question etc."""
    allowed: list[Decimal] = []
    for r in results:
        pct_cols = {i for i, c in enumerate(r.columns) if any(k in c.lower() for k in ("pct", "percent", "share", "ratio", "rate"))}
        for row in r.rows:
            for i, cell in enumerate(row):
                nums = _cell_numbers(cell)
                allowed += nums
                if i in pct_cols:
                    allowed += [x * 100 for x in nums if abs(x) <= 1]
        allowed.append(Decimal(len(r.rows)))
        if len(r.rows) > 1:  # column totals the answer may state
            for i in range(len(r.columns)):
                col = [_cell_numbers(row[i]) for row in r.rows if i < len(row) and not isinstance(row[i], str)]
                if col and len(col) == len(r.rows) and all(len(c) == 1 for c in col):
                    allowed.append(sum((c[0] for c in col), Decimal(0)))
    for e in extras:
        allowed += _cell_numbers(e)
    for t in texts:
        allowed += [n.value for n in extract_numbers(t or "")]
    return allowed


def _matches(n: FoundNumber, allowed: list[Decimal]) -> bool:
    tol = Decimal(5) * (Decimal(10) ** (-(n.decimals + 1)))
    for a in allowed:
        if abs(n.value - a) <= tol or abs(abs(n.value) - abs(a)) <= tol:
            return True
    return False


def unsupported_numbers(text: str, allowed: list[Decimal]) -> list[str]:
    return [n.text for n in extract_numbers(text) if not _matches(n, allowed)]
