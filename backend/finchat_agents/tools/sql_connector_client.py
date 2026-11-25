"""Read-only data access through databricks-sql-connector (service principal), as an alternative to the MCP bridge.

Same interface as `DatabricksMcpClient` (`query`, `warm_up`, `aclose`), so the guarded `run_sql` path is unchanged.
Selected with DATA_ACCESS=sql_connector (default: mcp). Differences to keep in mind:
- the MCP tool `execute_sql_read_only` refuses writes on the server; here only this client does, so it accepts SELECT / WITH
  statements only, and the service principal should have SELECT-only grants on silver and gold;
- no polling and no extra hop: connections are pooled (opening one costs seconds), results come back typed by the driver.
"""
from __future__ import annotations

import asyncio
import re
from typing import Any

from ..storage.aiops import DatabricksSqlExecutor
from .mcp_client import ColumnInfo, McpError, McpQueryError, McpTimeout, QueryResult

_READ_ONLY = re.compile(r"^\s*(\(\s*)*(select|with)\b", re.I)
_TYPE_NAMES = {"int": "INT", "bigint": "LONG", "smallint": "SHORT", "tinyint": "BYTE", "decimal": "DECIMAL", "double": "DOUBLE",
               "float": "FLOAT", "string": "STRING", "boolean": "BOOLEAN", "date": "DATE", "timestamp": "TIMESTAMP"}


def _type_name(code: Any) -> str:
    t = str(code or "string").strip().lower()
    return _TYPE_NAMES.get(t, t.upper())


class SqlConnectorClient:
    def __init__(self, executor: DatabricksSqlExecutor, *, timeout_s: float = 60.0):
        self._executor = executor
        self.timeout_s = timeout_s

    async def aclose(self) -> None:
        await self._executor.aclose()

    async def query(self, sql: str, *, timeout_s: float | None = None) -> QueryResult:
        if not _READ_ONLY.match(sql or ""):
            raise McpQueryError("Only SELECT or WITH statements can be run here (read-only).")
        limit = timeout_s or self.timeout_s
        try:
            columns, rows = await asyncio.wait_for(self._executor.query_typed(sql), timeout=limit)
        except (TimeoutError, asyncio.TimeoutError) as exc:
            raise McpTimeout(f"query did not finish within {limit:.0f} seconds") from exc
        except McpError:
            raise
        except (OSError, ConnectionError) as exc:
            raise McpError(f"SQL connection failed: {type(exc).__name__}") from exc
        except Exception as exc:  # noqa: BLE001 - the driver's error text is what the SQL writer repairs from
            raise McpQueryError(str(exc).strip()[:1000] or type(exc).__name__) from exc
        return QueryResult(columns=[ColumnInfo(name=n, type=_type_name(t)) for n, t in columns],
                           rows=rows, total_row_count=len(rows), truncated=False)

    async def warm_up(self) -> bool:
        """One cheap query so the warehouse starts and a connection is opened before the first question."""
        try:
            await self.query("SELECT 1 AS warm_up", timeout_s=max(self.timeout_s, 120))
            return True
        except McpError:
            return False
