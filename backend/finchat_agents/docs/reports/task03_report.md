# Task 03 report: data tools and guardrails over the DBSQL MCP server (21 Nov 2026)

## Files
- `tools/mcp_client.py`: async JSON-RPC client. Hard allowlist (`execute_sql_read_only`, `poll_sql_result`); Entra
  client-credentials token cached and refreshed 5 minutes before expiry; one retry with a fresh token on 401; polls
  until SUCCEEDED / FAILED / CANCELED / timeout; structuredContent first, `content[0].text` fallback; SSE responses;
  typed conversion (LONG/INT -> int, DECIMAL -> Decimal, DOUBLE -> float, BOOLEAN, DATE, TIMESTAMP; missing `str` = NULL);
  `truncated` kept; `warm_up()`.
- `access/rbac.py`: loads `config/rbac.v3.yaml`; `resolve_role(user_id, groups)` (object id first, then groups, unknown =
  no access); validates role/domain references; service role for scheduled jobs.
- `tools/sql_guard.py`: guardrails in order: one read-only SELECT/WITH (sqlglot, databricks) -> tables fully qualified,
  in the catalog, not broken -> every table in an allowed domain -> personal-data checks -> LIMIT added or capped.
- `tools/run_sql.py`: guard -> MCP -> PII masking -> notes (masked columns, duplicate loads at the grain, row limit,
  empty result hint) -> `{result_id, columns, rows (50 to the model), row_count, truncated, notes}`; counts against the
  SQL budget; full rows (up to SQL_ROW_LIMIT) kept per question for `calculate`.
- `tools/catalog.py`: search_tables (user's domains only), describe_table, get_join_path (full conditions),
  get_column_values (via the guardrails, cached 1 hour, PII refused), get_glossary.
- `tools/resolve.py`: resolve_period (Feb 25, February 2025, 2025-02, FY2026 P9, Q3 2026, latest, last month/quarter/year)
  and resolve_entity (fuzzy: UK3 = UK03, punctuation and LLC ignored). Both follow the page's period/entity columns and,
  for key-only tables, an approved join to the label dimension. Suggestions only.
- `tools/calculate.py`: AST-walking evaluator (no eval): arithmetic, comparisons, comprehensions, a fixed function list;
  earlier results available as r1, r2, ...; attributes, imports, dunders, lambdas, huge powers refused.
- `tools/__init__.py`: `build_data_tools(deps)`, `warm_up(deps)`; `tools/deps.py`: DataDeps, TTL cache, MCP client factory.
- `config.py` / `.env.example`: SQL_TIMEOUT_SECONDS, MCP_POLL_INTERVAL_SECONDS, COLUMN_VALUES_CACHE_SECONDS, AZURE_DATABRICKS_SCOPE.
- Tests: `tests/fakes.py` (fake MCP server on httpx.MockTransport), `test_mcp_client.py`, `test_access.py`,
  `test_data_tools.py`, `tests/live/test_databricks_live.py`.

## Tests
`..\.venv\Scripts\python -m pytest -q` from `backend/finchat_agents`: 170 passed, 27 skipped (live).
Covered with the fake server: DROP / INSERT / DELETE / UPDATE / MERGE / CREATE AS / SELECT INTO / SHOW / two statements /
table functions refused (and never sent); unknown table refused with a suggestion; unqualified name -> fully qualified
suggestion; out-of-domain and no-role refused; LIMIT added, capped at 1000, kept when smaller, on UNION too; PII masked
(direct, alias, subquery, SELECT *) and refused in WHERE / GROUP BY / ORDER BY / window; PII role sees names; poll path;
poll timeout; FAILED statement -> fixable message; token refresh before expiry and on 401; NULL and number conversion;
SSE and text-only responses; duplicate hint; column-values cache (and access still checked on cache hits);
period and entity resolution; calculate safety; SQL budget through the agent loop.

Live (`$env:RUN_LIVE="1"`), not run here (no credentials on this machine):
- warm-up; COUNT of adra_account_facts = 97; current Fynapse PARENT_ENTITY values (printed);
- ADRA ENTITY_CODE contains '100' and '561' (task 02 question 5);
- every example in `examples.yaml` with expected numbers is run and its numbers checked (verifies the rewritten ADRA examples).

## Assumptions
- get_column_values, resolve_period and resolve_entity run their lookups through the same guardrails but do not count
  against AGENT_MAX_SQL_CALLS (they are small metadata queries; get_column_values is cached).
- PII: a role without PII may select person columns (values come back masked; NULL stays NULL so "is it populated" still
  works) but may not filter, group, sort, join or partition by them. If the guard cannot trace where personal data
  flows (lineage fails), the query is refused rather than risk a leak.
- A user in several groups gets the union of the roles' domains; PII if any matched role allows it.
- Tables without a domain are never queryable, even for `finance_all` (`*`).
- Relative periods ("last quarter") count from today's calendar date (the legacy calendar file says the fiscal calendar
  is not approved).
- DECIMAL values stay Decimal in results (exact); calculate converts them to float.

## Open questions
1. Group-to-role mapping: kept as in `rbac.v3.yaml` (the corrected mapping from the template). The shifted mapping in
   rbac.silver.yaml still needs your confirmation, and the `users` block is empty.
2. Should resolve_period's "last month / last quarter" use the latest closed period instead of today's date?
3. Should a PII-allowed role also be able to list person-name values with get_column_values? It is refused for everyone now.
