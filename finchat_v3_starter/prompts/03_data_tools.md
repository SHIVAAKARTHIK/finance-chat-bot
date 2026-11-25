Task 03: data tools and guardrails over the DBSQL MCP server. Read CLAUDE.md, docs/SPEC.md section 4 and docs/MCP_NOTES.md first.

Reusable reference code (copy and adapt, do not import): reference/code/fincore_phase1.zip
(fincore/query/guard.py, fincore/query/lookup.py period resolution, fincore/exec/databricks_exec.py warm-up,
fincore/access/models.py) and reference/code/finance_react_agent.zip (verifier).

1. tools/mcp_client.py: async JSON-RPC client for DATABRICKS_MCP_URL. Service-principal token cache with refresh
   about 5 minutes before expiry; retry once on 401 with a fresh token. Only `execute_sql_read_only` and
   `poll_sql_result` are callable (hard allowlist). Poll until SUCCEEDED / FAILED / timeout. Parse
   structuredContent (fallback: content[0].text JSON); convert typed values by type_name; NULL handling; truncated flag.
2. access/: load config/rbac.v3.yaml. resolve_role(user_id, groups) -> Role(domains, pii_allowed) using explicit
   object ids first, then group names; unknown -> no access. Table -> domain from the knowledge front matter.
3. tools/run_sql.py, guardrails in this order, each with a clear fixable error message:
   read-only single SELECT/WITH (sqlglot, databricks dialect) -> all tables fully qualified and in the catalog index ->
   every table in an allowed domain for the role -> add LIMIT if missing (ROW_LIMIT) -> execute -> mask pii columns
   unless role.pii_allowed -> duplicate-at-grain hint when the query reads a table with known_issues: duplicates ->
   return {columns, rows_sample (max 50), row_count, truncated, notes}. Count SQL calls against the budget.
4. tools/catalog.py: search_tables(query) [filtered to the user's domains], describe_table(name), get_join_path(a, b),
   get_column_values(table, column, search?) [via run_sql, cached 1 hour, PII columns refused], get_glossary(term).
5. tools/resolve.py: resolve_period(text) -> filter values for the table's period columns (Feb 25, February 2025,
   2025-02, FY2026 P9, latest, last quarter) using values that exist; resolve_entity(text) -> matching entity values
   from get_column_values (fuzzy: UK3 -> UK03, punctuation / LLC ignored). Suggestions only; no access filtering.
6. tools/calculate.py: restricted Python evaluator over returned rows (no imports, attributes, files, network).
7. Warm-up function: one cheap query at app start.

Acceptance
- Unit tests with a fake MCP server: DROP / INSERT / two statements refused; unknown table refused with suggestion;
  out-of-domain table refused; PII masked; LIMIT added; poll path; token refresh on expiry; NULL and number conversion.
- Live tests (RUN_LIVE=1): count of lakehouse_mvpai.silver.adra_account_facts returns 97; get_column_values on a
  Fynapse entity column returns current values.
- Report.
