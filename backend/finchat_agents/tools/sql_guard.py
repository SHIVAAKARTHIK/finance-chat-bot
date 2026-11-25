"""SQL guardrails, applied in code before anything reaches Databricks (SPEC section 4).

Order: one read-only SELECT/WITH statement -> every table fully qualified and in the catalog (and not broken)
-> every table in a domain the role allows -> personal-data checks -> LIMIT added / capped.
Each refusal is a plain message the agent can act on.
"""
from __future__ import annotations

import difflib
from dataclasses import dataclass, field

import sqlglot
from sqlglot import exp
from sqlglot.lineage import lineage
from sqlglot.optimizer.qualify import qualify
from sqlglot.optimizer.scope import traverse_scope

from ..access.rbac import UserAccess
from ..knowledge.loader import Knowledge
from ..knowledge.models import TablePage

DIALECT = "databricks"

_FORBIDDEN = tuple(
    getattr(exp, n)
    for n in (
        "Insert", "Update", "Delete", "Drop", "Create", "Alter", "Merge", "Command", "Grant", "Revoke",
        "TruncateTable", "Use", "Set", "Copy", "Into", "Transaction", "Commit", "Rollback", "Cache", "Uncache",
        "Refresh", "LoadData", "Pragma", "Describe", "Show",
    )
    if hasattr(exp, n)
)


class GuardError(Exception):
    """Refusal with a fixable message."""


@dataclass
class GuardedQuery:
    sql: str  # what will run (LIMIT applied)
    tables: list[TablePage]
    masked_columns: set[str] = field(default_factory=set)  # output column names (lowercase) to mask
    limit_added: bool = False


def _table_name(t: exp.Table) -> str:
    return ".".join(p for p in (t.catalog, t.db, t.name) if p).lower()


def _suggest(kb: Knowledge, name: str) -> str:
    short = name.split(".")[-1].lower()
    names = {p.meta.name.lower(): p.meta.fqn for p in kb.tables.values() if p.meta.status == "active"}
    close = difflib.get_close_matches(short, list(names), n=3, cutoff=0.6)
    return f" Did you mean {', '.join(names[c] for c in close)}?" if close else " Use search_tables to find the right table."


def parse_single_select(sql: str) -> exp.Query:
    try:
        statements = [s for s in sqlglot.parse(sql, read=DIALECT) if s is not None]
    except sqlglot.errors.ParseError as exc:
        raise GuardError(f"The SQL does not parse: {str(exc).splitlines()[0][:300]}") from exc
    if len(statements) != 1:
        raise GuardError(f"Send exactly one SQL statement (got {len(statements)}).")
    root = statements[0]
    if not isinstance(root, exp.Query):
        raise GuardError(f"Only read-only SELECT queries (optionally WITH ... SELECT) are allowed; got {root.key.upper()}.")
    for node in root.walk():
        if isinstance(node, _FORBIDDEN):
            raise GuardError(f"Only read-only SELECT queries are allowed; {node.key.upper()} is not permitted.")
    return root


def check_tables(root: exp.Query, kb: Knowledge) -> list[TablePage]:
    ctes = {c.alias_or_name.lower() for c in root.find_all(exp.CTE)}
    problems: list[str] = []
    pages: dict[str, TablePage] = {}
    for t in root.find_all(exp.Table):
        if not isinstance(t.this, exp.Identifier):
            problems.append("Table functions (for example read_files) are not allowed; query catalog tables only.")
            continue
        name = _table_name(t)
        if not t.db and t.name.lower() in ctes:
            continue
        page = kb.resolve_table(name)
        if not (t.catalog and t.db):
            if page is not None:
                problems.append(f"Use the fully qualified name {page.meta.fqn} instead of '{name}'.")
            else:
                problems.append(f"Table '{name}' is not in the catalog.{_suggest(kb, name)}")
            continue
        if page is None or page.meta.fqn.lower() != name:
            problems.append(f"Table {name} is not in the catalog.{_suggest(kb, name)}")
            continue
        if page.meta.superseded_by:
            targets = ", ".join(kb.tables[t].meta.fqn for t in page.meta.superseded_by if t in kb.tables)
            problems.append(f"Table {page.meta.fqn} is a copy; the source of truth is {targets}. Query that instead.")
            continue
        if page.meta.status == "broken":
            problems.append(f"Table {page.meta.fqn} cannot be queried right now (it is marked broken: {page.meta.broken_error or 'see REVIEW.md'}).")
            continue
        pages[page.id] = page
    if problems:
        raise GuardError(" ".join(dict.fromkeys(problems)))
    if not pages:
        raise GuardError("The query must read at least one catalog table.")
    return list(pages.values())


def check_access(pages: list[TablePage], access: UserAccess | None) -> None:
    if access is None or not access.has_access:
        raise GuardError("Access denied: your account has no data access configured. Ask an administrator for a role.")
    denied = [p for p in pages if not access.role.allows_domain(p.meta.domain)]  # type: ignore[union-attr]
    if denied:
        parts = [f"{p.meta.fqn} (domain '{p.meta.domain or 'none'}')" for p in denied]
        raise GuardError(
            "Access denied: your role does not include " + ", ".join(parts) + ". Tell the user this data is outside their access."
        )


def _schema(pages: list[TablePage]) -> dict:
    schema: dict = {}
    for p in pages:
        m = p.meta
        schema.setdefault(m.catalog, {}).setdefault(m.schema_, {})[m.name] = {c.name: "STRING" for c in p.columns}
    return schema


def pii_masks(root: exp.Query, pages: list[TablePage]) -> set[str]:
    """Output columns that carry personal data. Refuses filtering, grouping, sorting or joining on PII columns."""
    pii = {(p.meta.fqn.lower(), c.name.lower()) for p in pages for c in p.columns if c.pii}
    if not pii:
        return set()
    pii_names = {c for _, c in pii}
    uses_star = any(  # SELECT * / t.* (COUNT(*) does not count)
        isinstance(e, exp.Star) or (isinstance(e, exp.Column) and isinstance(e.this, exp.Star))
        for sel in root.find_all(exp.Select)
        for e in sel.expressions
    )
    if not uses_star and not any(c.name.lower() in pii_names for c in root.find_all(exp.Column)):
        return set()
    try:
        schema = _schema(pages)
        q = qualify(root.copy(), schema=schema, dialect=DIALECT, validate_qualify_columns=False)
        for scope in traverse_scope(q):
            for col in scope.columns:
                src = scope.sources.get(col.table)
                if isinstance(src, exp.Table) and (_table_name(src), col.name.lower()) in pii:
                    anc = col.find_ancestor(exp.Where, exp.Group, exp.Order, exp.Having, exp.Join, exp.Window, exp.Select)
                    if not isinstance(anc, exp.Select):
                        raise GuardError(
                            f"Column {col.name.upper()} holds personal data; your role may not filter, group, sort or join "
                            "by it. Remove it from WHERE / GROUP BY / ORDER BY / JOIN, or answer by team or role instead."
                        )
        masked: set[str] = set()
        for name in q.named_selects:
            node = lineage(name, q, schema=schema, dialect=DIALECT)
            for n in node.walk():
                if isinstance(n.source, exp.Table):
                    col_name = n.name.split(".")[-1].strip('"`').lower()
                    if (_table_name(n.source), col_name) in pii:
                        masked.add(name.lower())
        return masked
    except GuardError:
        raise
    except Exception as exc:  # cannot prove where personal data flows: refuse rather than leak
        cols = ", ".join(sorted(n.upper() for n in pii_names))
        raise GuardError(
            f"This query reads personal-data columns ({cols}) in a way that cannot be checked. "
            "Leave them out, or select them directly from the table."
        ) from exc


def apply_limit(root: exp.Query, row_limit: int) -> tuple[exp.Query, bool]:
    limit = root.args.get("limit")
    if limit is None:
        return root.limit(row_limit), True
    value = limit.expression if isinstance(limit, exp.Limit) else None
    try:
        n = int(value.name) if value is not None else None
    except (TypeError, ValueError):
        n = None
    if n is None or n > row_limit:
        return root.limit(row_limit), True
    return root, False


def guard_sql(sql: str, kb: Knowledge, access: UserAccess | None, row_limit: int) -> GuardedQuery:
    root = parse_single_select(sql)
    pages = check_tables(root, kb)
    check_access(pages, access)
    masked = set() if access is not None and access.pii_allowed else pii_masks(root, pages)
    limited, added = apply_limit(root, row_limit)
    return GuardedQuery(sql=limited.sql(dialect=DIALECT), tables=pages, masked_columns=masked, limit_added=added)
