# Plugging v3 into the company backend

v3 takes over the backend's existing finance-chat URLs. The UI does not change: it keeps calling
`POST /api/invoke/finance-chat/stream` and gets the same event names and response fields. Behind those URLs everything
is v3 (`finchat_agents`). No code or logic comes from the previous agent, and no KPI data is produced (`explanation.kpi`
is always `null`).

## 1. Copy the package
Copy `finchat_agents/` into `backend/`, next to `app/`. Leave out `.venv`, `traces/`, `outputs/`, `.pytest_cache/` and
`reference/`.

## 2. Requirements
Add this line to `backend/requirements.txt`:
```
-r finchat_agents/requirements.txt
```
v3 requirements are ranges that accept the backend's pins: FastAPI 0.115.2, uvicorn 0.32.0, pydantic-settings 2.6.0
and httpx 0.27.2. The full offline suite passes both with those versions and with the latest ones.

## 3. Mount it in `app/main.py`
Delete the old finance router registration and the old finance runtime code from the lifespan. Then add, after
`app = FastAPI(...)`:
```python
from finchat_agents.integration import install_backend
from app.dependencies import get_current_user
from app.auth.permissions import agent_roles      # wherever agent_roles(user) lives
from app.middleware import limiter

install_backend(
    app,
    get_current_user=get_current_user,            # validated Entra user dict (oid/sub, groups, ...)
    agent_roles=agent_roles,                      # group ids -> role labels
    rate_limit=limiter.limit("10/minute"),        # same limit as today
)
```
This one call does the following:

| What | Details |
|---|---|
| Routes at `/api/invoke` | `POST /finance-chat`, `POST /finance-chat/stream`, `GET /finance-chat/history?limit=&threads=` |
| Routes at `/v3` | `/v3/health`, `/v3/health/live`, `/v3/cards`, `/v3/files/...`, using the same Entra identity |
| Startup | After the backend's own startup, warms up MCP, both Bedrock models and the aiops tables. A failure is logged and never blocks startup. |
| Shutdown | Flushes pending aiops writes. |

If `app/routers/finance_chat.py` and its line in `app/api.py` are no longer needed, delete them.

`/api/insights/summary`: if it should show the v3 summary cards, read them with
`SummaryStore.from_store(service.store).active_cards(domains)`. `install_backend` returns the `service`.

## 4. Identity and roles
- **User id:** the Entra object id (`oid`, else `sub`) from `get_current_user`. Fields like `user_id` or `roles` in the
  request body are ignored.
- **Roles:** `agent_roles(user)` labels are passed to v3 as groups. In `finchat_agents/config/rbac.v3.yaml`, map each
  label under `group_roles` to a v3 role:
  ```yaml
  group_roles:
    <label from agent_roles>: finance_all     # e.g. the CFO / admin label
    <AP analyst label>: <role with the AP domains>
  ```
- **Unmapped users:** a user whose labels don't map to any role gets `status: "declined"`.

## 5. Environment variables (shared `backend/.env`)
v3 reads `backend/.env`, the same file as the backend. Several names are shared, and v3 will use their values:

| Name | Required value for v3 |
|---|---|
| `DATABRICKS_SCHEMA` | **Ignored by v3.** The backend uses `silver` here; v3 always writes to `lakehouse_mvpai.aiops.finance_chat_*` (fixed in code) and its queries use full table names, so no change is needed. |
| `DATABRICKS_CATALOG` | `lakehouse_mvpai` |
| `BEDROCK_MODEL_SQL` / `BEDROCK_MODEL_RESPONSE` | Claude Sonnet 4.5 / gpt-oss-120b model ids. If the old values point at other models, change them. |
| `DATABRICKS_SERVER_HOSTNAME`, `DATABRICKS_HTTP_PATH`, `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`, `DATABRICKS_AUTH`, `AWS_*` | Same meaning in both. v3 uses the service principal only and never `DATABRICKS_ACCESS_TOKEN`. |

New names that v3 needs: `DATABRICKS_MCP_URL`. Optional names with defaults are listed in `docs/DEPLOY.md` section 2.

## 6. Docker
- In the backend `Dockerfile`, copy `finchat_agents/`. Installing `requirements.txt` already includes v3's requirements
  through the `-r` line.
- Keep `.env`, `finchat_agents/traces`, `finchat_agents/outputs`, `finchat_agents/tests` and
  `finchat_agents/reference` out of the image (see `deploy/Dockerfile.v3.dockerignore`).
- The image runs as the `app` user, so `finchat_agents/traces` and `finchat_agents/outputs` must be writable by `app`.
- One uvicorn worker, as today, is fine.

## 7. Stream behaviour

| Event | Behaviour |
|---|---|
| `status {"stage"}` | Only stage names the UI already knows: processing, intent, exploration, sql, database, results, answer, clarification. |
| Keep-alive | Every 15 s without a new stage, the current stage is sent again, so Nginx's 120 s read timeout never fires. No Nginx change is needed, but `proxy_buffering off;` on the API location is still recommended. |
| `delta {"text"}` | The final answer is sent in pieces of up to 64 characters, then `complete`. v3 writes the answer in one step, so pieces arrive together just before `complete`. |
| `complete` | The UI response object. |
| `error {"message","status_code"}` | A generic message; details go only to the server log. |

v3's own time limit is `AGENT_MAX_SECONDS` (300 by default). Set it **below the UI's 180 s abort**, for example
`AGENT_MAX_SECONDS=150`.

## 8. Response mapping (v3 to UI fields)

| UI field | From v3 |
|---|---|
| `status` | `answered` / `partial` become `success`; `clarification`, `declined` and `failed` become `clarification`, `declined` and `error` |
| `answer`, `message` | the answer (Markdown), plus a `Files:` line with links when files were created |
| `table` | the first result table: `columns[{key,label,numeric}]`, rows as objects keyed by column with **string** values (empty string for nulls, as the UI type requires), `total_rows`, `truncated` |
| `breakdown`, `breakdown_title` | `"[]"`, `null` |
| `follow_up_questions` | the suggestions, as a JSON string |
| `source`, `source_label`, `source_used`, `source_message` | the tables used, row count, and how it was calculated (never SQL) |
| `explanation` | `kpi: null` plus steps, filters, caveats. **The UI hides the whole explanation when `kpi` is null** (`normalizeExplanation`), so v3 notices are also added to the answer as `Note: ...` lines and `source_message` carries how it was calculated |
| `verification` | `verified` when answered and every number matched a tool result, otherwise `unverified` |
| `trace_id`, `timing` | the v3 message id; `total_ms` and `total_seconds` (the other timing fields are `null`) |

## 9. Confirmed with the UI code (Copilot, 21 Nov 2026) and what is still open
- **History:** `GET /api/invoke/finance-chat/history` returns a flat JSON array of `FinanceChatHistoryWireItem`
  (`conversation_id`, `message_time`, `user_question`, `answer`, `source_used`, `resolved_question`, `generated_sql`,
  `category`, `citation`, `data_row_count`, `status`, optional `table` / `explanation`). The UI groups the items itself.
  v3 sends exactly that: newest first, `generated_sql` always `null`, `explanation` and `table` omitted.
- **Table rows:** objects keyed by column `key`, values are strings. Done.
- **Explanation without a KPI:** the UI shows nothing (`normalizeExplanation` returns null). Notices are added to the
  answer text instead. Optional UI change: let `chat-explanation.tsx` render steps, filters and caveats when `kpi` is null.
- **Role labels:** Admin, CFO, Controller, AP analyst, AR analyst, Treasurer, Fixed asset analyst. All seven are mapped in
  `rbac.v3.yaml` (`group_roles`). The mapping needs Karthik's confirmation (see the TODOs in that file).
- **Clarifications:** `Record<string, string>` such as `{"period": "Q3 FY2026", "entity": "US"}`; v3 appends it to the question as text.
- **Still open:**
  - history order (v3 sends newest first), and what `threads=true` means in the UI (v3 returns the newest `limit` conversations);
  - `source_used` in history is `null` (the messages table doesn't store the tables used);
  - file links: a plain browser link carries no Bearer token, so the UI must download files through its API client.
