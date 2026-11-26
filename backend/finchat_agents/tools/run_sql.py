"""run_sql: guardrails -> MCP execute_sql_read_only -> PII masking -> notes. Counts against the SQL budget."""
from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from ..access.rbac import UserAccess
from ..guardrails.filters import Scrubber
from ..runtime.tools import RunContext, Tool, ToolContext, ToolError
from .deps import DataDeps, access_of
from .mcp_client import McpError, McpQueryError, McpTimeout
from .sql_guard import GuardError, guard_sql

MASK = "<masked>"
RESULTS_KEY = "sql_results"  # RunContext.extras[RESULTS_KEY] = {result_id: SqlResult}


class SqlResult(BaseModel):
    result_id: str = ""
    columns: list[str] = Field(default_factory=list)
    column_types: list[str] = Field(default_factory=list)
    rows: list[list[Any]] = Field(default_factory=list)  # all returned rows (<= SQL_ROW_LIMIT)
    row_count: int = 0
    truncated: bool = False
    notes: list[str] = Field(default_factory=list)
    sql: str = ""
    tables: list[str] = Field(default_factory=list)
    rows_to_model: int = 50

    def records(self) -> list[dict[str, Any]]:
        return [dict(zip(self.columns, r)) for r in self.rows]

    def for_model(self) -> dict[str, Any]:
        out: dict[str, Any] = {
            "result_id": self.result_id,
            "columns": self.columns,
            "rows": self.rows[: self.rows_to_model],
            "row_count": self.row_count,
        }
        if self.row_count > self.rows_to_model:
            out["rows_shown"] = self.rows_to_model
        if self.truncated:
            out["truncated"] = True
        if self.notes:
            out["notes"] = self.notes
        return out


def _duplicate_note(page) -> str:
    grain = ", ".join(page.meta.primary_key) or "the grain"
    issue = next(i for i in page.meta.known_issues if i.code == "duplicates")
    return (
        f"{page.meta.fqn} has duplicate loads ({issue.note.split('.')[0].strip()}). Check duplicates at the grain "
        f"({grain}) before trusting counts or sums; warn the user, and deduplicate only if the answer says so."
    )


async def execute_guarded(sql: str, deps: DataDeps, access: UserAccess | None) -> SqlResult:
    """Run one query through every guardrail. Raises ToolError with a fixable message on refusal or failure."""
    s = deps.settings
    try:
        guarded = guard_sql(sql, deps.kb, access, s.sql_row_limit)
    except GuardError as exc:
        raise ToolError(str(exc)) from exc
    try:
        qr = await deps.mcp.query(guarded.sql, timeout_s=s.sql_timeout_seconds)
    except McpQueryError as exc:
        raise ToolError(f"Databricks rejected the query: {exc} Fix the SQL and try again.") from exc
    except McpTimeout as exc:
        raise ToolError(f"The query did not finish within {s.sql_timeout_seconds:.0f} seconds; narrow it and retry.") from exc
    except McpError as exc:
        raise ToolError(f"The data service is not reachable right now ({exc}). Try again later; do not guess numbers.") from exc

    columns = [c.name for c in qr.columns]
    rows = [list(r) for r in qr.rows]
    masked_idx = [i for i, c in enumerate(columns) if c.lower() in guarded.masked_columns]
    for r in rows:
        for i in masked_idx:
            if r[i] is not None:
                r[i] = MASK
    notes: list[str] = []
    # company content safety: contact details, credentials and storage paths never reach the model, tables or files
    if deps.guardrails is not None and deps.guardrails.enabled("content_safety") and Scrubber().rows(columns, rows):
        notes.append("Some contact details or internal values were removed from the results.")
    if masked_idx:
        notes.append(f"Personal data in {', '.join(columns[i] for i in masked_idx)} is masked for this user's role.")
    for page in guarded.tables:
        if page.meta.has_issue("duplicates"):
            notes.append(_duplicate_note(page))
    if qr.truncated or len(rows) >= s.sql_row_limit:
        notes.append(f"Result limited to {len(rows)} rows; aggregate in SQL instead of reading raw rows.")
    if not rows:
        notes.append(
            "No rows returned. Before concluding there is no data, check the filter values with get_column_values "
            "(spelling, spaces, case, period labels)."
        )
    return SqlResult(
        columns=columns,
        column_types=[c.type for c in qr.columns],
        rows=rows,
        row_count=len(rows),
        truncated=bool(qr.truncated or len(rows) >= s.sql_row_limit),
        notes=notes,
        sql=guarded.sql,
        tables=[p.meta.fqn for p in guarded.tables],
        rows_to_model=s.sql_rows_to_model,
    )


def register_result(run: RunContext, result: SqlResult) -> SqlResult:
    """Keep the result for this question (calculate, answer tables, number check) and give it an id (r1, r2, ...)."""
    store = run.extras.setdefault(RESULTS_KEY, {})
    result.result_id = f"r{len(store) + 1}"
    store[result.result_id] = result
    return result


def make_run_sql_tool(deps: DataDeps) -> Tool:
    from ..llm.types import ToolSpec

    spec = ToolSpec(
        name="run_sql",
        description=(
            "Run ONE read-only Databricks SQL query (SELECT or WITH ... SELECT) against catalog tables. "
            "Use fully qualified names (lakehouse_mvpai.<schema>.<table>) and approved joins with the full key. "
            "Returns columns, up to 50 rows, row_count, notes and a result_id usable in calculate. "
            "Refusals and database errors come back as plain messages: read them, fix the SQL and retry."
        ),
        input_schema={
            "type": "object",
            "properties": {
                "sql": {"type": "string", "description": "A single SELECT statement."},
                "purpose": {"type": "string", "description": "One line: what this query answers (for the audit trail)."},
            },
            "required": ["sql"],
        },
    )

    async def handler(args: dict[str, Any], tctx: ToolContext) -> SqlResult:
        sql = str(args.get("sql") or "").strip()
        if not sql:
            raise ToolError("Provide the SQL to run in the 'sql' argument.")
        result = await execute_guarded(sql, deps, access_of(tctx))
        return register_result(tctx.run, result)

    return Tool(spec=spec, handler=handler, counts_as_sql=True)
