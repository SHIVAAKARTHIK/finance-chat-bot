# Databricks DBSQL MCP server: tested facts (20 Nov 2026)

Endpoint: `https://<workspace-host>/api/2.0/mcp/sql` (value in `DATABRICKS_MCP_URL`).
Transport: JSON-RPC 2.0 over HTTP POST (streamable HTTP).
Headers: `Authorization: Bearer <token>`, `Content-Type: application/json`,
`Accept: application/json, text/event-stream`.

## Auth (tested, works)
- Entra client credentials: POST `https://login.microsoftonline.com/{AZURE_TENANT_ID}/oauth2/v2.0/token`
  with `grant_type=client_credentials`, `client_id`, `client_secret`,
  `scope=2ff814a6-3304-4ab8-85cb-cd0e6f879c1d/.default`.
- `SELECT current_user()` returns the service principal's client id: queries run as the service principal.
- Token expires after about 1 hour (we saw "Token is expired"). Cache it and refresh about 5 minutes early.

## Tools
| Tool | Use in v3 |
|---|---|
| `execute_sql` | **Never.** Marked destructive (INSERT, UPDATE, CREATE...). |
| `execute_sql_read_only` | All agent queries. Argument: `{"query": "<sql>"}` |
| `poll_sql_result` | When a query returns a `statement_id` without a finished state. Argument: `{"statement_id": "..."}` |

Calls: `{"jsonrpc":"2.0","id":N,"method":"tools/call","params":{"name":"execute_sql_read_only","arguments":{"query":"..."}}}`.
`tools/list` works too.

## Response shape (observed)
```
result.content[0].text      -> a JSON string (parse it)
result.structuredContent    -> the same data as an object (prefer this when present)
  statement_id
  status.state              -> "SUCCEEDED" (else poll; handle FAILED / CANCELED with the error message)
  manifest.schema.columns[] -> {name, type_text, type_name, position}
  result.data_typed_array[] -> rows: {"values": [{"str": "97"}, ...]}
  total_row_count, truncated
result.isError              -> false on success
```
All values arrive as strings (`{"str": ...}`); convert using `type_name` (LONG, INT, DECIMAL, DOUBLE,
BOOLEAN, DATE, TIMESTAMP, STRING). A missing `str` key means NULL. Respect `truncated`.

## Verified
- `SELECT COUNT(*) FROM lakehouse_mvpai.silver.adra_account_facts` -> 97
- `SHOW SCHEMAS IN lakehouse_mvpai` -> aiops, bronze, default, gold, governance, information_schema, silver
- The first query of the day can be slow if the SQL warehouse is stopped (warm-up on app start).
