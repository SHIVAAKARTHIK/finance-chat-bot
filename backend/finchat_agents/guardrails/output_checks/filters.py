"""Checks in code (they do not depend on the model following the prompt): contact details, credentials, internal
paths, model names and internal table names are removed from what the user reads (patterns in ../patterns.py)."""
from __future__ import annotations

import re
from typing import Any, Iterable

from ..patterns import EMAIL, MODEL, PATH, PHONE, REMOVED, SECRET

INTERNAL_DATA = "finance data"
PHONE_COLUMN = re.compile(r"phone|mobile|telephone", re.I)


class Scrubber:
    def __init__(self, table_ids: Iterable[str] = ()):
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
