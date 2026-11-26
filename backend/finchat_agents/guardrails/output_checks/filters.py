"""Checks in code (they do not depend on the model following the prompt): contact details, credentials, internal
paths, model names and internal table names are removed from what the user reads (patterns in ../patterns.py)."""
from __future__ import annotations

import re
from typing import Any, Iterable

from ..patterns import EMAIL, MODEL, PATH, PHONE, REMOVED, SECRET

INTERNAL_DATA = "finance data"
WORD_BOUNDARY = re.compile(r"(?<=[a-z0-9])(?=[A-Z])|_+")
# an SQL function written out, e.g. COUNT(*) or SUM(NET_AMOUNT); upper case only, so ordinary words are not touched
SQL_CALL = re.compile(r"\b(?:COUNT|SUM|AVG|MIN|MAX)\s*\(\s*(?:DISTINCT\s+)?(?:\*|[\w.]+)\s*\)")
# follow-up suggestions that ask to see what is masked or restricted are never offered
UNMASK = re.compile(
    r"unmask|without (?:the )?mask|remov\w+ (?:the )?mask|\bactual (?:preparer|approver|reviewer|user|employee|person)"
    r"|\b(?:real|full) names?\b|\bpersonal (?:data|details)\b",
    re.I,
)


def _words(identifier: str) -> str:
    return " ".join(WORD_BOUNDARY.sub(" ", identifier).split()).lower()


def _any_of(names: list[str], flags: int = 0) -> re.Pattern[str] | None:
    ordered = sorted(names, key=len, reverse=True)
    return re.compile(r"\b(?:" + "|".join(re.escape(n) for n in ordered) + r")\b", flags) if ordered else None
PHONE_COLUMN = re.compile(r"phone|mobile|telephone", re.I)


class Scrubber:
    def __init__(self, table_ids: Iterable[str] = (), column_names: Iterable[str] = ()):
        columns = {c for c in column_names if len(c) >= 6}
        # only names that are clearly identifiers: with an underscore, or CamelCase such as TaskPreparerName
        self._columns = [p for p in (
            _any_of([c for c in columns if "_" in c], re.I),
            _any_of([c for c in columns if "_" not in c and re.search(r"[a-z][A-Z]", c)]),
        ) if p is not None]
        # short names with an underscore are certainly identifiers; single words ("joins") could be normal language
        short = sorted({t.split(".")[-1] for t in table_ids if "_" in t.split(".")[-1]}, key=len, reverse=True)
        names = [r"\blakehouse_mvpai(?:\.\w+)*", r"\b(?:silver|gold|aiops)\.\w+_\w+"]
        if short:
            names.append(r"\b(?:" + "|".join(re.escape(s) for s in short) + r")\b")
        self._tables = re.compile("|".join(names), re.I)

    def text(self, value: str) -> tuple[str, list[str]]:
        """Free text the user reads. Returns (clean text, kinds of content removed)."""
        removed: list[str] = []
        for kind, pattern, replacement in (
            ("credential", SECRET, REMOVED), ("email", EMAIL, REMOVED), ("phone", PHONE, REMOVED), ("path", PATH, REMOVED),
            ("model", MODEL, REMOVED), ("table_name", self._tables, INTERNAL_DATA),
        ):
            value, n = pattern.subn(replacement, value)
            if n:
                removed.append(kind)
        value, calls = SQL_CALL.subn("a calculation", value)
        if calls:
            removed.append("sql")
        for pattern in self._columns:  # column names become ordinary words: ACCOUNT_STATUS -> account status
            value, n = pattern.subn(lambda m: _words(m.group(0)), value)
            if n and "column_name" not in removed:
                removed.append("column_name")
        return value, removed

    @staticmethod
    def cell(value: Any, column: str = "") -> Any:
        """One value returned by a query: contact details, credentials and storage paths are removed. Table and model
        names stay (they can be real data, for example in pipeline logs)."""
        if not isinstance(value, str) or not value:
            return value
        if PHONE_COLUMN.search(column or ""):
            return REMOVED
        for pattern in (SECRET, EMAIL, PHONE, PATH):
            value = pattern.sub(REMOVED, value)
        return value

    def rows(self, columns: list[str], rows: list[list[Any]]) -> int:
        """Clean query rows in place; returns how many values changed."""
        changed = 0
        for row in rows:
            for i, value in enumerate(row):
                clean = self.cell(value, columns[i] if i < len(columns) else "")
                if clean != value:
                    row[i] = clean
                    changed += 1
        return changed
