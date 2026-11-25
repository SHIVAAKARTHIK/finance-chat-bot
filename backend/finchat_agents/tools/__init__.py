"""Data tools for the agents. Every query goes through run_sql's guardrails (tools/sql_guard.py)."""
from __future__ import annotations

import time
from typing import Any

from ..runtime.tools import Tool
from .calculate import make_calculate_tool
from .catalog import make_catalog_tools
from .deps import DataDeps, TTLCache, access_of, build_mcp_client
from .resolve import make_resolve_tools
from .run_sql import SqlResult, execute_guarded, make_run_sql_tool


def build_data_tools(deps: DataDeps) -> dict[str, Tool]:
    """All data tools by name: run_sql, search_tables, describe_table, get_join_path, get_column_values,
    get_glossary, resolve_period, resolve_entity, calculate. Agents pick the subset they need."""
    tools = [make_run_sql_tool(deps), *make_catalog_tools(deps), *make_resolve_tools(deps), make_calculate_tool()]
    return {t.name: t for t in tools}


async def warm_up(deps: DataDeps) -> dict[str, Any]:
    """Run one cheap query at app start so the SQL warehouse is awake before the first question."""
    t0 = time.monotonic()
    ok = await deps.mcp.warm_up() if hasattr(deps.mcp, "warm_up") else False
    return {"mcp": "ok" if ok else "unavailable", "seconds": round(time.monotonic() - t0, 2)}


__all__ = [
    "DataDeps",
    "SqlResult",
    "TTLCache",
    "access_of",
    "build_data_tools",
    "build_mcp_client",
    "execute_guarded",
    "warm_up",
]
