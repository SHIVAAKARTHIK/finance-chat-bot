"""Summary agent storage: finance_chat_summary_runs and finance_chat_summary_cards (aiops).

The tables are created by Karthik from reference/aiops/finance_chat_summary_cards.sql. This code checks that they
exist and stops with a clear message if not; it never creates them.
"""
from __future__ import annotations

from typing import Any

from .aiops import ALLOWED_SCHEMA, AiopsStore, SqlExecutor, Statement, build_merge, check_target

RUNS = "finance_chat_summary_runs"
CARDS = "finance_chat_summary_cards"
DDL_HINT = "finchat_v3_starter/reference/aiops/finance_chat_summary_cards.sql"
CARD_COLUMNS_FOR_UI = (
    "card_id, run_id, domain, card_type, rank, period_label, comparison_label, metric_name, current_value, "
    "previous_value, change_abs, change_pct, is_flagged, title, card_text, explanation, explanation_status, created_at"
)


class SummaryTablesMissing(RuntimeError):
    pass


def _missing(exc: Exception) -> bool:
    text = str(exc).upper()
    return any(k in text for k in ("TABLE_OR_VIEW_NOT_FOUND", "NOT FOUND", "DOES NOT EXIST", "CANNOT BE FOUND"))


def build_supersede(catalog: str, schema: str, domain: str, run_id: str) -> Statement:
    """Every older active card of `domain` becomes superseded, whatever its metric (so stale key-change cards whose
    metric no longer passes the thresholds disappear). Only for a domain the run completed without errors; the new
    run's own cards (same run_id) stay active. An UPDATE of the status only: cards are never deleted."""
    target = check_target(catalog, schema, CARDS)
    sql = (f"UPDATE {target} SET status = 'superseded' WHERE status = 'active' AND domain = CAST(:domain AS STRING) "
           f"AND run_id <> CAST(:run_id AS STRING)")
    return sql, {"domain": domain, "run_id": run_id}


class SummaryStore:
    def __init__(self, executor: SqlExecutor, *, catalog: str = "lakehouse_mvpai", schema: str = ALLOWED_SCHEMA):
        self.base = AiopsStore(executor, catalog=catalog, schema=schema)
        self.executor = executor
        self.catalog, self.schema = catalog, schema

    @classmethod
    def from_store(cls, store: AiopsStore) -> "SummaryStore":
        return cls(store.executor, catalog=store.catalog, schema=store.schema)

    async def check_tables(self) -> None:
        missing = []
        for table in (RUNS, CARDS):
            try:
                await self.executor.query(f"SELECT 1 FROM {self.base.fqn(table)} LIMIT 0", {})
            except Exception as exc:
                if not _missing(exc):
                    raise
                missing.append(f"{self.catalog}.{self.schema}.{table}")
        if missing:
            raise SummaryTablesMissing(
                f"Summary tables not found: {', '.join(missing)}. Create them in Databricks from {DDL_HINT} "
                "(after review); the summary agent never creates tables. Use --dry-run to preview cards without writing."
            )

    async def upsert_run(self, row: dict[str, Any]) -> None:
        await self.base.upsert(RUNS, [row])

    async def save_domain(self, domain: str, rows: list[dict[str, Any]], run_id: str) -> None:
        """A domain the run completed without errors: MERGE its new cards, then supersede all its older active cards,
        in one batch (the UPDATE runs only if the MERGE succeeded). Call it only for completed domains; a failed or
        partly processed domain keeps its previous active cards."""
        if any(r["domain"] != domain or r["run_id"] != run_id for r in rows):
            raise ValueError("save_domain: every card must belong to this domain and run")
        statements = [build_merge(self.catalog, self.schema, CARDS, rows)] if rows else []
        statements.append(build_supersede(self.catalog, self.schema, domain, run_id))
        await self.executor.execute(statements)

    async def active_cards(self, domains: list[str] | None, limit: int = 50) -> list[dict[str, Any]]:
        """Active cards; `domains` None means every domain (role '*'). Filtered again by the caller."""
        params: dict[str, Any] = {}
        where = "status = 'active'"
        if domains is not None:
            if not domains:
                return []
            marks = []
            for i, d in enumerate(domains):
                params[f"d{i}"] = d
                marks.append(f"CAST(:d{i} AS STRING)")
            where += f" AND domain IN ({', '.join(marks)})"
        sql = (f"SELECT {CARD_COLUMNS_FOR_UI} FROM {self.base.fqn(CARDS)} WHERE {where} "
               f"ORDER BY domain, rank, created_at DESC LIMIT {int(limit)}")
        return await self.executor.query(sql, params)
