"""App storage in lakehouse_mvpai.aiops.finance_chat_* (MCP is read-only, so writes use databricks-sql-connector with
the same service principal). Every write is a MERGE on the primary key with typed, named parameters.

Hard guard: this module can only write to tables named finance_chat_* in the aiops schema.
"""
from __future__ import annotations

import asyncio
import datetime as dt
import logging
import re
import time
from pathlib import Path
from typing import Any, Callable, Protocol

from ..config import Settings

log = logging.getLogger(__name__)

DDL_FILE = Path(__file__).resolve().parent / "aiops_ddl.sql"
MISSING_CONTEXT_COLUMN = (
    "Column context_start_turn is missing on lakehouse_mvpai.aiops.finance_chat_conversations, so 'clear context' "
    "cannot be saved. Ask the Databricks admin to run: ALTER TABLE lakehouse_mvpai.aiops.finance_chat_conversations "
    "ADD COLUMNS (context_start_turn INT COMMENT 'Turns up to this index are ignored as context (clear context)')")
ALLOWED_SCHEMA = "aiops"
TABLE_PREFIX = "finance_chat_"

# Column types from aiops_ddl.sql (used to CAST every parameter, so NULLs and numbers are typed).
COLUMNS: dict[str, dict[str, str]] = {
    "finance_chat_conversations": {
        "conversation_id": "STRING", "user_id": "STRING", "title": "STRING", "domain": "STRING", "visibility": "STRING",
        "turn_count": "INT", "summary": "STRING", "summary_through_turn": "INT", "summary_updated_at": "TIMESTAMP",
        "created_at": "TIMESTAMP", "last_message_at": "TIMESTAMP", "context_start_turn": "INT",
    },
    "finance_chat_messages": {
        "message_id": "STRING", "conversation_id": "STRING", "user_id": "STRING", "turn_index": "INT",
        "question_text": "STRING", "standalone_question": "STRING", "intent": "STRING", "answer_path": "STRING",
        "domain": "STRING", "kpi_ids": "ARRAY<STRING>", "plan": "STRING", "sql_text": "STRING", "sql_source": "STRING",
        "result_row_count": "INT", "result_preview": "STRING", "answer_text": "STRING", "trust_label": "STRING",
        "clarification_text": "STRING", "status": "STRING", "visibility": "STRING", "hidden_reason": "STRING",
        "error_code": "STRING", "error_message": "STRING", "retry_count": "SMALLINT", "llm_call_count": "SMALLINT",
        "input_tokens": "INT", "output_tokens": "INT", "models_used": "ARRAY<STRING>", "first_token_ms": "INT",
        "total_latency_ms": "INT", "created_at": "TIMESTAMP", "completed_at": "TIMESTAMP",
    },
    "finance_chat_message_events": {
        "event_id": "STRING", "message_id": "STRING", "conversation_id": "STRING", "step_name": "STRING",
        "step_order": "SMALLINT", "attempt": "SMALLINT", "status": "STRING", "started_at": "TIMESTAMP",
        "ended_at": "TIMESTAMP", "duration_ms": "INT", "input_payload": "STRING", "output_payload": "STRING",
        "error_message": "STRING", "model_provider": "STRING", "model_name": "STRING", "prompt_version": "STRING",
        "temperature": "DECIMAL(3,2)", "input_tokens": "INT", "output_tokens": "INT", "cache_read_tokens": "INT",
        "created_at": "TIMESTAMP",
    },
}
COLUMNS["finance_chat_user_memory"] = {
    "user_id": "STRING", "frequent_kpis": "STRING", "frequent_entities": "STRING", "default_entity": "STRING",
    "default_period": "STRING", "recent_window_size": "SMALLINT", "updated_at": "TIMESTAMP",
}
# Summary agent tables (reference/aiops/finance_chat_summary_cards.sql). Karthik creates them; this code never does.
COLUMNS["finance_chat_summary_runs"] = {
    "run_id": "STRING", "trigger_type": "STRING", "status": "STRING", "domains": "ARRAY<STRING>", "cards_created": "INT",
    "cards_flagged": "INT", "llm_call_count": "INT", "input_tokens": "INT", "output_tokens": "INT", "error_message": "STRING",
    "started_at": "TIMESTAMP", "completed_at": "TIMESTAMP",
}
COLUMNS["finance_chat_summary_cards"] = {
    "card_id": "STRING", "run_id": "STRING", "domain": "STRING", "card_type": "STRING", "rank": "SMALLINT",
    "period_label": "STRING", "comparison_label": "STRING", "metric_name": "STRING", "source_tables": "ARRAY<STRING>",
    "current_value": "DECIMAL(38,6)", "previous_value": "DECIMAL(38,6)", "change_abs": "DECIMAL(38,6)",
    "change_pct": "DECIMAL(18,6)", "is_flagged": "BOOLEAN", "title": "STRING", "card_text": "STRING",
    "explanation": "STRING", "explanation_status": "STRING", "investigator_sql": "ARRAY<STRING>", "status": "STRING",
    "created_at": "TIMESTAMP",
}
KEYS = {
    "finance_chat_summary_runs": ["run_id"],
    "finance_chat_summary_cards": ["card_id"],
    "finance_chat_user_memory": ["user_id"],
    "finance_chat_conversations": ["conversation_id"],
    "finance_chat_messages": ["message_id"],
    "finance_chat_message_events": ["event_id"],
}
# Insert-only columns (kept from the first write). The rolling summary is updated by its own statement (task 07).
NEVER_UPDATE = {
    "finance_chat_conversations": {"created_at", "title", "summary_through_turn"},
    "finance_chat_messages": {"created_at"},
    "finance_chat_message_events": {"created_at"},
    "finance_chat_user_memory": set(),
    "finance_chat_summary_runs": {"started_at", "trigger_type"},
    "finance_chat_summary_cards": {"created_at"},
}

CHECKS: dict[str, dict[str, set[str | None]]] = {
    "finance_chat_conversations": {"visibility": {"visible", "hidden", "deleted"}},
    "finance_chat_messages": {
        "status": {"processing", "answered", "clarification", "declined", "failed"},
        "visibility": {"visible", "hidden", "deleted"},
        "answer_path": {None, "kpi", "adhoc", "clarify", "declined"},
    },
    "finance_chat_message_events": {"status": {"ok", "failed", "skipped"}},
    "finance_chat_summary_runs": {"status": {"running", "succeeded", "partial", "failed"}, "trigger_type": {"schedule", "manual"}},
    "finance_chat_summary_cards": {
        "status": {"active", "superseded", "hidden"},
        "card_type": {"key_change", "status", "highlight"},
        "explanation_status": {None, "explained", "no_cause_found", "not_flagged", "failed"},
    },
}

Statement = tuple[str, dict[str, Any]]


class StorageError(Exception):
    pass


class SqlExecutor(Protocol):
    async def execute(self, statements: list[Statement]) -> None: ...

    async def query(self, sql: str, params: dict[str, Any]) -> list[dict[str, Any]]: ...


def utcnow() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def check_target(catalog: str, schema: str, table: str) -> str:
    if schema != ALLOWED_SCHEMA or not table.startswith(TABLE_PREFIX) or not re.fullmatch(r"\w+", f"{catalog}{schema}{table}"):
        raise StorageError(f"writes are only allowed to {catalog}.{ALLOWED_SCHEMA}.{TABLE_PREFIX}* (got {catalog}.{schema}.{table})")
    return f"{catalog}.{schema}.{table}"


def validate_row(table: str, row: dict[str, Any]) -> None:
    cols = COLUMNS[table]
    unknown = set(row) - set(cols)
    if unknown:
        raise StorageError(f"{table}: unknown columns {sorted(unknown)}")
    for col, allowed in CHECKS.get(table, {}).items():
        if col in row and row[col] not in allowed:
            raise StorageError(f"{table}.{col}: value {row[col]!r} violates the check constraint ({sorted(v for v in allowed if v)})")


def _param_expr(name: str, sql_type: str, value: Any, params: dict[str, Any]) -> str:
    if sql_type.startswith("ARRAY"):
        if value is None:
            return f"CAST(NULL AS {sql_type})"
        items = []
        for i, item in enumerate(value):
            params[f"{name}_{i}"] = str(item)
            items.append(f":{name}_{i}")
        return f"array({', '.join(items)})" if items else f"CAST(array() AS {sql_type})"
    params[name] = value
    return f"CAST(:{name} AS {sql_type})"


def build_merge(catalog: str, schema: str, table: str, rows: list[dict[str, Any]]) -> Statement:
    """MERGE INTO target USING (SELECT ... UNION ALL SELECT ...) ON key: insert new rows, update existing ones."""
    target = check_target(catalog, schema, table)
    if not rows:
        raise StorageError("nothing to write")
    cols = list(COLUMNS[table])
    keys = KEYS[table]
    params: dict[str, Any] = {}
    selects = []
    for r_i, row in enumerate(rows):
        validate_row(table, row)
        missing = [k for k in keys if row.get(k) in (None, "")]
        if missing:
            raise StorageError(f"{table}: key column(s) {missing} missing")
        exprs = [f"{_param_expr(f'r{r_i}_{c}', COLUMNS[table][c], row.get(c), params)} AS {c}" for c in cols]
        selects.append("SELECT " + ", ".join(exprs))
    on = " AND ".join(f"tgt.{k} = src.{k}" for k in keys)
    # update only the columns this write provides (so a partial update never blanks other columns)
    provided = [c for c in cols if any(c in row for row in rows)]
    updates = ", ".join(f"tgt.{c} = src.{c}" for c in provided if c not in keys and c not in NEVER_UPDATE[table])
    insert_cols = ", ".join(cols)
    insert_vals = ", ".join(f"src.{c}" for c in cols)
    sql = (
        f"MERGE INTO {target} AS tgt USING ({' UNION ALL '.join(selects)}) AS src ON {on} "
        + (f"WHEN MATCHED THEN UPDATE SET {updates} " if updates else "")
        + f"WHEN NOT MATCHED THEN INSERT ({insert_cols}) VALUES ({insert_vals})"
    )
    return sql, params


def build_summary_update(catalog: str, schema: str, conversation_id: str, summary: str, through_turn: int,
                         now: Any) -> Statement:
    """The rolling summary is the only conversation field updated outside the per-turn MERGE."""
    target = check_target(catalog, schema, "finance_chat_conversations")
    sql = (f"UPDATE {target} SET summary = CAST(:summary AS STRING), summary_through_turn = CAST(:through AS INT), "
           f"summary_updated_at = CAST(:now AS TIMESTAMP) WHERE conversation_id = CAST(:cid AS STRING)")
    return sql, {"summary": summary, "through": int(through_turn), "now": now, "cid": conversation_id}


def ddl_statements(catalog: str = "lakehouse_mvpai", schema: str = ALLOWED_SCHEMA) -> list[str]:
    """CREATE TABLE IF NOT EXISTS + constraint statements from aiops_ddl.sql, only for aiops.finance_chat_* tables."""
    text = "\n".join(line for line in DDL_FILE.read_text(encoding="utf-8").splitlines() if not line.strip().startswith("--"))
    out = []
    for stmt in (s.strip() for s in text.split(";")):
        if not stmt:
            continue
        m = re.match(r"(CREATE TABLE IF NOT EXISTS|ALTER TABLE)\s+([\w.]+)", stmt, re.I)
        if not m:
            continue
        cat, sch, tbl = m.group(2).split(".")
        check_target(catalog, sch, tbl)
        out.append(stmt.replace(f"{cat}.{sch}.", f"{catalog}.{schema}."))
    return out


class AiopsStore:
    def __init__(self, executor: SqlExecutor, *, catalog: str = "lakehouse_mvpai", schema: str = ALLOWED_SCHEMA):
        if schema != ALLOWED_SCHEMA:
            raise StorageError(f"app storage must be the '{ALLOWED_SCHEMA}' schema")
        self.executor = executor
        self.catalog = catalog
        self.schema = schema

    def fqn(self, table: str) -> str:
        return check_target(self.catalog, self.schema, table)

    async def upsert(self, table: str, rows: list[dict[str, Any]]) -> None:
        await self.executor.execute([build_merge(self.catalog, self.schema, table, rows)])

    async def ensure_tables(self) -> None:
        """Create the tables only if they do not exist (constraints that already exist are skipped)."""
        for stmt in ddl_statements(self.catalog, self.schema):
            try:
                await self.executor.execute([(stmt, {})])
            except Exception as exc:  # ALTER ... ADD CONSTRAINT fails when the constraint exists
                if stmt.upper().startswith("ALTER") and "exist" in str(exc).lower():
                    continue
                raise

    async def conversation(self, conversation_id: str) -> dict[str, Any] | None:
        base = "conversation_id, user_id, title, turn_count, summary, summary_through_turn"
        where = f"FROM {self.fqn('finance_chat_conversations')} WHERE conversation_id = :cid LIMIT 1"
        if getattr(self, "_has_context_column", True):
            try:
                rows = await self.executor.query(f"SELECT {base}, context_start_turn {where}", {"cid": conversation_id})
                return rows[0] if rows else None
            except Exception as exc:
                if "context_start_turn" not in str(exc).lower():
                    raise
                self._has_context_column = False  # keep answering with history; only "clear context" needs the column
                log.error(MISSING_CONTEXT_COLUMN)
        rows = await self.executor.query(f"SELECT {base} {where}", {"cid": conversation_id})
        return rows[0] if rows else None

    async def set_context_start(self, conversation_id: str, turn: int) -> None:
        """Clear context: later questions ignore every turn up to `turn` (the history itself stays visible)."""
        target = check_target(self.catalog, self.schema, "finance_chat_conversations")
        sql = (f"UPDATE {target} SET context_start_turn = CAST(:turn AS INT), last_message_at = CAST(:now AS TIMESTAMP) "
               f"WHERE conversation_id = CAST(:cid AS STRING)")
        try:
            await self.executor.execute([(sql, {"turn": int(turn), "now": utcnow(), "cid": conversation_id})])
        except Exception as exc:
            if "context_start_turn" in str(exc).lower():
                raise RuntimeError(MISSING_CONTEXT_COLUMN) from exc
            raise
        self._has_context_column = True

    async def update_summary(self, conversation_id: str, summary: str, through_turn: int) -> None:
        await self.executor.execute([build_summary_update(self.catalog, self.schema, conversation_id, summary, through_turn, utcnow())])

    async def user_plans(self, user_id: str, limit: int = 30) -> list[Any]:
        rows = await self.executor.query(
            f"SELECT plan FROM {self.fqn('finance_chat_messages')} WHERE user_id = :uid AND visibility = 'visible' "
            f"AND status = 'answered' AND plan IS NOT NULL ORDER BY created_at DESC LIMIT {int(limit)}",
            {"uid": user_id},
        )
        return [r.get("plan") for r in rows]

    async def user_memory(self, user_id: str) -> dict[str, Any] | None:
        rows = await self.executor.query(
            f"SELECT user_id, frequent_entities, default_entity, default_period, recent_window_size "
            f"FROM {self.fqn('finance_chat_user_memory')} WHERE user_id = :uid LIMIT 1",
            {"uid": user_id},
        )
        return rows[0] if rows else None

    async def recent_turns(self, conversation_id: str, limit: int = 5, user_id: str | None = None) -> list[dict[str, Any]]:
        """Recent turns, oldest first. With `user_id` only that user's turns are read, so this can run in parallel with
        the conversation ownership check."""
        user_filter = " AND user_id = :uid" if user_id else ""
        params = {"cid": conversation_id, **({"uid": user_id} if user_id else {})}
        rows = await self.executor.query(
            f"SELECT turn_index, question_text, standalone_question, left(answer_text, 1500) AS answer_start, domain, plan "
            f"FROM {self.fqn('finance_chat_messages')} WHERE conversation_id = :cid{user_filter} AND visibility = 'visible' "
            f"AND status IN ('answered', 'clarification') ORDER BY turn_index DESC LIMIT {int(limit)}",
            params,
        )
        return list(reversed(rows))

    async def user_history(self, user_id: str, limit: int = 20) -> list[dict[str, Any]]:
        """The user's own most recent visible exchanges, newest first (filtered by user_id in SQL)."""
        return await self.executor.query(
            f"SELECT message_id, conversation_id, turn_index, question_text, standalone_question, "
            f"left(answer_text, 8000) AS answer_text, result_row_count, status, created_at FROM {self.fqn('finance_chat_messages')} WHERE user_id = :uid AND visibility = 'visible' "
            f"AND status IN ('answered', 'partial', 'clarification') ORDER BY created_at DESC LIMIT {int(limit)}",
            {"uid": user_id},
        )


# ---------------------------------------------------------------- databricks-sql-connector executor

POOL_SIZE = 4  # connections kept open for reuse (aiops reads and background writes)
MAX_CONNECTION_AGE_S = 45 * 60  # reopen well before the service-principal token (about 1 hour) expires


class DatabricksSqlExecutor:
    """Runs statements with databricks-sql-connector on a small pool of reused connections. Opening a connection costs
    seconds, so it is done once and reused instead of once per query. A pooled connection is reopened when the token
    changes (the token provider refreshes it before expiry) or when it is older than MAX_CONNECTION_AGE_S; a reused
    connection that fails is closed and the work is retried once on a fresh one. Each connection is used by one thread
    at a time. Blocking calls run in a worker thread."""

    def __init__(self, server_hostname: str, http_path: str, token: Callable[[], Any], *, connect: Callable[..., Any] | None = None,
                 pool_size: int = POOL_SIZE, max_age_s: float = MAX_CONNECTION_AGE_S, clock: Callable[[], float] = time.monotonic):
        self.server_hostname = server_hostname
        self.http_path = http_path
        self._token = token  # async () -> str
        self._connect = connect
        self._pool_size = pool_size
        self._max_age_s = max_age_s
        self._clock = clock
        self._idle: list[tuple[Any, str, float]] = []  # (connection, token it was opened with, opened at)
        self._slots: asyncio.Semaphore | None = None

    def _connection(self, token: str) -> Any:
        if self._connect is not None:
            return self._connect(server_hostname=self.server_hostname, http_path=self.http_path, access_token=token)
        from databricks import sql

        return sql.connect(server_hostname=self.server_hostname, http_path=self.http_path, access_token=token)

    @staticmethod
    def _close(conn: Any) -> None:
        try:
            conn.close()
        except Exception:  # noqa: BLE001 - closing a dead connection may fail; nothing to do
            pass

    def _take_idle(self, token: str) -> tuple[Any, str, float] | None:
        """A pooled connection opened with the current token and not too old; stale ones are closed."""
        now = self._clock()
        while self._idle:
            conn, tok, opened = self._idle.pop()
            if tok == token and now - opened < self._max_age_s:
                return conn, tok, opened
            self._close(conn)
        return None

    async def _with_connection(self, work: Callable[[Any], Any]) -> Any:
        if self._slots is None:
            self._slots = asyncio.Semaphore(self._pool_size)
        token = await self._token()
        async with self._slots:
            entry = self._take_idle(token)
            reused = entry is not None
            while True:
                if entry is None:
                    entry = (await asyncio.to_thread(self._connection, token), token, self._clock())
                try:
                    result = await asyncio.to_thread(work, entry[0])
                except Exception:
                    self._close(entry[0])
                    if reused:  # a pooled connection may have gone stale: retry once on a fresh one
                        entry, reused = None, False
                        continue
                    raise
                self._idle.append(entry)
                return result

    async def execute(self, statements: list[Statement]) -> None:
        def run(conn: Any) -> None:
            with conn.cursor() as cur:
                for sql_text, params in statements:
                    cur.execute(sql_text, params or None)

        await self._with_connection(run)

    async def query(self, sql_text: str, params: dict[str, Any]) -> list[dict[str, Any]]:
        def run(conn: Any) -> list[dict[str, Any]]:
            with conn.cursor() as cur:
                cur.execute(sql_text, params or None)
                cols = [d[0] for d in cur.description or []]
                return [dict(zip(cols, r)) for r in cur.fetchall()]

        return await self._with_connection(run)

    async def query_typed(self, sql_text: str) -> tuple[list[tuple[str, Any]], list[list[Any]]]:
        """Like `query`, but returns ((column name, driver type), rows) so callers can keep the column types."""
        def run(conn: Any) -> tuple[list[tuple[str, Any]], list[list[Any]]]:
            with conn.cursor() as cur:
                cur.execute(sql_text)
                cols = [(d[0], d[1] if len(d) > 1 else "string") for d in cur.description or []]
                return cols, [list(r) for r in cur.fetchall()]

        return await self._with_connection(run)

    async def aclose(self) -> None:
        """Close the pooled connections (app shutdown)."""
        idle, self._idle = self._idle, []
        for conn, _, _ in idle:
            await asyncio.to_thread(self._close, conn)


def build_store(settings: Settings) -> AiopsStore | None:
    """Store from settings, or None when the SQL warehouse settings are missing (answers still work, nothing is saved)."""
    if not (settings.databricks_server_hostname and settings.databricks_http_path and settings.azure_tenant_id
            and settings.azure_client_id and settings.azure_client_secret):
        log.warning("aiops storage disabled: DATABRICKS_SERVER_HOSTNAME / DATABRICKS_HTTP_PATH / AZURE_* not set")
        return None
    from ..tools.mcp_client import EntraTokenProvider

    tokens = EntraTokenProvider(settings.azure_tenant_id, settings.azure_client_id, settings.azure_client_secret,
                                settings.azure_databricks_scope)
    executor = DatabricksSqlExecutor(settings.databricks_server_hostname, settings.databricks_http_path, tokens.get_token)
    return AiopsStore(executor, catalog=settings.databricks_catalog, schema=ALLOWED_SCHEMA)  # never the shared DATABRICKS_SCHEMA


def main() -> None:
    """python -m finchat_agents.storage.aiops --create-tables   (CREATE TABLE IF NOT EXISTS, aiops only)"""
    import argparse

    ap = argparse.ArgumentParser(description=main.__doc__)
    ap.add_argument("--create-tables", action="store_true", help="create the finance_chat_* tables if they do not exist")
    ap.add_argument("--print-ddl", action="store_true", help="print the statements without running them")
    args = ap.parse_args()
    if args.print_ddl:
        print(";\n\n".join(ddl_statements()) + ";")
        return
    if args.create_tables:
        from ..config import get_settings

        store = build_store(get_settings())
        if store is None:
            raise SystemExit("storage settings missing (DATABRICKS_SERVER_HOSTNAME, DATABRICKS_HTTP_PATH, AZURE_*)")
        asyncio.run(store.ensure_tables())
        print("aiops tables exist")


if __name__ == "__main__":
    main()
