"""Catalog tools: search_tables, describe_table, get_join_path, get_column_values, get_glossary."""
from __future__ import annotations

import difflib
import re
from typing import Any

from ..access.rbac import UserAccess
from ..knowledge.models import TablePage
from ..llm.types import ToolSpec
from ..runtime.tools import GuardrailRefusal, Tool, ToolContext, ToolError
from .deps import DataDeps, access_of
from .run_sql import execute_guarded

COLUMN_VALUES_LIMIT = 100
VALUES_PER_COLUMN = 12  # in a compact page; get_column_values gives the full list


def _compact_values(section: str) -> str:
    """Keep the first VALUES_PER_COLUMN stored values of each column."""
    out: list[str] = []
    kept = dropped = 0
    for ln in section.splitlines():
        if ln.startswith("**"):
            if dropped:
                out.append(f"- ... {dropped} more: use get_column_values")
            kept = dropped = 0
            out.append(ln)
        elif ln.startswith("- "):
            if kept < VALUES_PER_COLUMN:
                out.append(ln)
                kept += 1
            else:
                dropped += 1
        else:
            out.append(ln)
    if dropped:
        out.append(f"- ... {dropped} more: use get_column_values")
    return "\n".join(out) + "\n"


def compact_page(body: str) -> str:
    """A table page with at most VALUES_PER_COLUMN stored values per column; everything else stays whole. Smaller
    pages make every following step of the agent loop faster, since each step resends the conversation."""
    parts = re.split(r"(?m)^(?=## )", body)
    return "".join(_compact_values(p) if p.startswith("## Values") else p for p in parts).strip()


def _schema(props: dict[str, Any], required: list[str]) -> dict[str, Any]:
    return {"type": "object", "properties": props, "required": required}


def visible_table(deps: DataDeps, access: UserAccess, name: str) -> TablePage:
    """A table the user may see; plain errors for unknown, broken or out-of-domain tables."""
    page = deps.kb.resolve_table(str(name or ""))
    if page is None:
        hits = deps.kb.search_tables(str(name).replace("_", " "), k=3, domains=access.domains)
        hint = f" Similar tables: {', '.join(h.fqn for h in hits)}." if hits else " Use search_tables to find tables."
        raise ToolError(f"Table '{name}' is not in the catalog.{hint}")
    if not access.role.allows_domain(page.meta.domain):  # type: ignore[union-attr]
        raise GuardrailRefusal(f"Access denied: {page.meta.fqn} is outside this user's domains. Tell the user it is not available to them.")
    if page.meta.superseded_by:
        targets = ", ".join(deps.kb.tables[t].meta.fqn for t in page.meta.superseded_by if t in deps.kb.tables)
        raise ToolError(f"{page.meta.fqn} is a copy; use the source of truth {targets} instead.")
    if page.meta.status == "broken":
        raise ToolError(f"{page.meta.fqn} cannot be queried right now (marked broken: {page.meta.broken_error or 'unknown error'}).")
    return page


def _column(page: TablePage, column: str):
    col = page.column(str(column or ""))
    if col is None:
        close = difflib.get_close_matches(str(column).upper(), [c.name.upper() for c in page.columns], n=3, cutoff=0.5)
        hint = f" Did you mean {', '.join(close)}?" if close else ""
        raise ToolError(f"Column '{column}' is not in {page.meta.fqn}.{hint} Use describe_table to see the columns.")
    return col


_SAFE_SEARCH = re.compile(r"[^\w\s\-.,&/]")


async def column_values(
    deps: DataDeps, access: UserAccess, table: str, column: str, search: str | None = None, limit: int = COLUMN_VALUES_LIMIT
) -> dict[str, Any]:
    page = visible_table(deps, access, table)
    col = _column(page, column)
    if col.pii:
        raise ToolError(f"Column {col.name} holds personal data; its values cannot be listed.")
    term = _SAFE_SEARCH.sub("", (search or "")).strip().lower()[:100]
    key = ("values", page.id, col.name, term, limit)
    cached = deps.cache.get(key)
    if cached is not None:
        return cached
    where = f" WHERE lower(CAST(`{col.name}` AS STRING)) LIKE '%{term}%'" if term else ""
    sql = (
        f"SELECT `{col.name}` AS value, COUNT(*) AS row_count FROM {page.meta.fqn}{where} "
        f"GROUP BY `{col.name}` ORDER BY row_count DESC LIMIT {int(limit)}"
    )
    result = await execute_guarded(sql, deps, access)
    out = {
        "table": page.meta.fqn,
        "column": col.name,
        "values": [{"value": r[0], "rows": r[1]} for r in result.rows],
        "complete": len(result.rows) < limit,
    }
    if search:
        out["search"] = term
    if not result.rows:
        out["note"] = "No matching values." if term else "The column has no values."
    deps.cache.set(key, out)
    return out


def make_catalog_tools(deps: DataDeps) -> list[Tool]:
    kb = deps.kb

    async def search_tables(args: dict[str, Any], tctx: ToolContext) -> dict[str, Any]:
        access = access_of(tctx)
        query = str(args.get("query") or "").strip()
        if not query:
            raise ToolError("Give a search query, e.g. 'reconciliation status by account'.")
        k = max(1, min(int(args.get("k") or 5), 10))
        hits = kb.search_tables(query, k=k, domains=access.domains)
        if not hits:
            return {"tables": [], "note": "No accessible table matches. Try other words, or the data is outside this user's domains."}
        return {"tables": [h.model_dump(exclude={"table"}) for h in hits]}

    async def describe_table(args: dict[str, Any], tctx: ToolContext) -> dict[str, Any]:
        page = visible_table(deps, access_of(tctx), args.get("table", ""))
        m = page.meta
        return {
            "table": m.fqn,
            "domain": m.domain,
            "layer": m.layer,
            "type": m.type,
            "grain": m.grain,
            "primary_key": m.primary_key,
            "entity_column": m.entity_column,
            "period_columns": m.period_columns,
            "pii_columns": m.pii_columns,
            "known_issues": [i.model_dump() for i in m.known_issues],
            "page": page.body if str(args.get("detail") or "").lower() == "full" else compact_page(page.body),
        }

    async def get_join_path(args: dict[str, Any], tctx: ToolContext) -> dict[str, Any]:
        access = access_of(tctx)
        a = visible_table(deps, access, args.get("from_table", ""))
        b = visible_table(deps, access, args.get("to_table", ""))
        path = kb.join_path(a.id, b.id)
        if path is None:
            return {"joins": [], "note": f"No approved join between {a.meta.fqn} and {b.meta.fqn}. Do not join them; "
                    "answer from one table or say they cannot be combined."}
        steps = []
        for j in path:
            f, t = kb.tables[j.from_].meta, kb.tables[j.to].meta
            steps.append({
                "join": j.id,
                "from": f.fqn,
                "to": t.fqn,
                "cardinality": j.cardinality,
                "condition": j.condition(f.fqn, t.fqn),
                **({"note": j.note} if j.note else {}),
            })
        return {"joins": steps, "note": "Use every key column in each condition (replace table names with your aliases)."}

    async def get_column_values(args: dict[str, Any], tctx: ToolContext) -> dict[str, Any]:
        return await column_values(deps, access_of(tctx), args.get("table", ""), args.get("column", ""), args.get("search"))

    async def get_glossary(args: dict[str, Any], tctx: ToolContext) -> dict[str, Any]:
        term = str(args.get("term") or "").strip()
        if not term:
            raise ToolError("Give a term or the user's question.")
        entries = kb.glossary_lookup(term)
        if not entries:
            low = term.lower()
            entries = [g for g in kb.glossary if any(low in n.lower() for n in g.names)]
        if not entries:
            return {"entries": [], "note": f"No glossary entry for '{term}'. Use the table pages and rules instead."}
        return {"entries": [g.model_dump() for g in entries[:8]]}

    return [
        Tool(ToolSpec(
            name="search_tables",
            description="Find catalog tables for a question (BM25 over names, purposes, synonyms and columns). "
                        "Only tables in the user's domains are returned. Returns fqn, domain, layer, purpose and score.",
            input_schema=_schema({"query": {"type": "string"}, "k": {"type": "integer", "description": "Max results (default 5)."}}, ["query"]),
        ), search_tables),
        Tool(ToolSpec(
            name="describe_table",
            description="Page of one table: grain, keys, entity and period columns, PII columns, known issues, columns "
                        "with meanings and SQL expressions, stored values (first few per column), empty columns, joins and "
                        "notes. detail='full' shows every stored value (rarely needed).",
            input_schema=_schema({"table": {"type": "string", "description": "Table name, schema.table or full name."},
                                  "detail": {"type": "string", "enum": ["compact", "full"],
                                             "description": "compact (default) or full."}}, ["table"]),
        ), describe_table),
        Tool(ToolSpec(
            name="get_join_path",
            description="Approved join path between two tables with the full join conditions. Never join tables without one.",
            input_schema=_schema({"from_table": {"type": "string"}, "to_table": {"type": "string"}}, ["from_table", "to_table"]),
        ), get_join_path),
        Tool(ToolSpec(
            name="get_column_values",
            description="Distinct values of a column with row counts (top 100, cached 1 hour). Use before filtering on "
                        "status words, entity codes or period labels. Optional 'search' filters values containing the text. "
                        "Personal-data columns are refused.",
            input_schema=_schema({"table": {"type": "string"}, "column": {"type": "string"}, "search": {"type": "string"}}, ["table", "column"]),
        ), get_column_values),
        Tool(ToolSpec(
            name="get_glossary",
            description="Business definitions for terms in a question (e.g. 'pending closure', 'net amount'): which "
                        "table, column and filter to use. Pass a term or the whole question.",
            input_schema=_schema({"term": {"type": "string"}}, ["term"]),
        ), get_glossary),
    ]
