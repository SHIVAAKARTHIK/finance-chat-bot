"""Read the entity and period filters an answer actually used, from its final SQL (code, not the model).

Entity columns come from the table pages: the entity column (when it is not a surrogate *_KEY) and entity/company
name columns. Period columns are the pages' period columns (not keys). Values are the literals compared to them.
"""
from __future__ import annotations

import re
from typing import Any

import sqlglot
from sqlglot import exp

from ..knowledge.loader import Knowledge
from ..knowledge.models import TablePage


def _entity_columns(page: TablePage) -> set[str]:
    cols = set()
    ec = page.meta.entity_column
    if ec and not ec.upper().endswith("_KEY"):
        cols.add(ec.lower())
    for c in page.columns:
        text = " ".join([c.meaning, *c.synonyms]).lower()
        if not c.pii and "NAME" in c.name.upper() and ("entity" in text or "company" in text):
            cols.add(c.name.lower())
    return cols


def _period_columns(page: TablePage) -> set[str]:
    return {c.lower() for c in page.meta.period_columns if not c.upper().endswith("_KEY")}


def _literal(node: exp.Expression) -> str | None:
    if isinstance(node, exp.Literal):
        return node.name
    if isinstance(node, (exp.Neg,)) and isinstance(node.this, exp.Literal):
        return "-" + node.this.name
    return None


def extract_filters(sql_texts: list[str], kb: Knowledge) -> dict[str, list[str]]:
    entities: list[str] = []
    periods: list[str] = []
    for sql in sql_texts:
        try:
            tree = sqlglot.parse_one(sql, read="databricks")
        except Exception:
            continue
        alias_pages: dict[str, TablePage] = {}
        for t in tree.find_all(exp.Table):
            page = kb.resolve_table(".".join(p for p in (t.catalog, t.db, t.name) if p))
            if page is not None:
                alias_pages[(t.alias or t.name).lower()] = page
        if not alias_pages:
            continue
        ent_cols = {c for p in alias_pages.values() for c in _entity_columns(p)}
        per_cols = {c for p in alias_pages.values() for c in _period_columns(p)}
        for cmp in tree.find_all(exp.EQ, exp.Like, exp.ILike, exp.In):
            left = cmp.this
            col = left if isinstance(left, exp.Column) else left.find(exp.Column) if left is not None else None
            if col is None:
                continue
            name = col.name.lower()
            values: list[Any] = []
            if isinstance(cmp, exp.In):
                values = [_literal(e) for e in cmp.expressions]
            else:
                values = [_literal(cmp.expression)]
            values = [re.sub(r"^%|%$", "", v).strip() for v in values if v]
            if name in ent_cols:
                entities += [v for v in values if v]
            elif name in per_cols:
                periods += [f"{col.name}={v}" if re.fullmatch(r"\d+", v) else v for v in values if v]
    return {"entities": list(dict.fromkeys(entities)), "periods": list(dict.fromkeys(periods))}
