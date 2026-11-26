# Deploying Finance Chat v3 (branch `finance-agentic`)

v2 stays on `feature/finance-kpi` and is the fallback. This branch has no v2 finance code, so nothing is deleted;
switching is choosing which image the VM runs.

## 1. Image

**Option A (recommended, SPEC: the existing backend serves `/v3`)**: add v3 to the existing backend image and app.

1. In the existing backend `Dockerfile`, add the lines between the `v3 lines` markers in
   [`deploy/Dockerfile.v3`](../deploy/Dockerfile.v3): install `finchat_agents/requirements.txt`, copy
   `finchat_agents/`, create `traces/` and `outputs/`. If the image runs as a non-root user, that user needs write access to those two folders.
2. Add the exclusions in [`deploy/Dockerfile.v3.dockerignore`](../deploy/Dockerfile.v3.dockerignore) to the
   backend's `.dockerignore`. In particular, `.env`, `traces/`, `outputs/`, `tests/`, `eval/` and `reference/` never go into the image.
3. In the backend's FastAPI entry point (where `app = FastAPI(...)` is created):
   ```python
   from finchat_agents.api.app import mount_v3
   mount_v3(app, identity=<existing Entra identity dependency>)   # required: without it /v3 answers 401
   ```
   `mount_v3` adds the `/v3` routes, then runs the warm-up after the app's own startup:
   - one MCP query;
   - a ping to both Bedrock models;
   - one aiops read.

   It also flushes pending aiops writes on shutdown. A failed warm-up is logged and never blocks startup.
4. Python: requirements are tested on 3.13 and should also work on 3.11 or later. If the backend's dependencies clash with `requirements.txt`,
   tell me which packages clash.

**Option B: a separate v3 container.** Build `deploy/Dockerfile.v3` (port 8010) and route `/v3/*` to it from the
reverse proxy (or point the UI at it). Use this if the backend's dependencies cannot be changed. **This container has no
login of its own, so since 2026-11-27 its chat, file and card routes answer 401.** Add an identity dependency (validate
the Entra token) before using it. `ALLOW_REQUEST_IDENTITY=true` trusts the user id in the request and is for local
testing only: anyone who can reach the port could then act as any user.

Build (context = `backend/`):
```
docker build -f finchat_agents/deploy/Dockerfile.v3 -t finchat-backend:finance-agentic backend
```

## 2. Environment variables (names only; values go in the VM's `backend/.env`, never in git or the image)

Required:

| Name | Purpose |
|---|---|
| `AWS_REGION` | Bedrock region |
| AWS credentials | Prefer the VM's instance role / a non-personal role. Otherwise `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, (`AWS_SESSION_TOKEN`) or `AWS_PROFILE` with `~/.aws` mounted read-only |
| `DATABRICKS_MCP_URL` | DBSQL MCP endpoint (data reads) |
| `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET` | service principal (MCP and aiops) |
| `DATABRICKS_SERVER_HOSTNAME`, `DATABRICKS_HTTP_PATH` | SQL warehouse for aiops writes (if missing, answers still work but nothing is saved) |

Optional (defaults in `config.py`):
- models: `BEDROCK_MODEL_SQL`, `BEDROCK_MODEL_RESPONSE`, `GPT_OSS_TRANSPORT`, `LLM_TIMEOUT_SECONDS`;
- Databricks: `DATABRICKS_CATALOG`, `DATABRICKS_AUTH`, `AZURE_DATABRICKS_SCOPE`,
  `SQL_TIMEOUT_SECONDS`, `MCP_POLL_INTERVAL_SECONDS`, `COLUMN_VALUES_CACHE_SECONDS`;
- agent limits: `AGENT_MAX_STEPS`, `AGENT_MAX_SECONDS`, `AGENT_MAX_SQL_CALLS`, `SQL_ROW_LIMIT`, `SQL_ROWS_TO_MODEL`,
  `CONVERSATION_QUESTION_LIMIT`, `SUMMARY_TOKEN_THRESHOLD`;
- files and paths: `RBAC_FILE`, `TRACE_DIR`, `OUTPUT_DIR`, `SUMMARY_METRICS_FILE`;
- deploy (new in task 10): `WARM_UP_ON_START`, `WARM_UP_TIMEOUT_SECONDS`, `HEALTH_CACHE_SECONDS`;
- `RUN_LIVE` must be `0` on the VM.

## 3. docker compose changes

See [`deploy/docker-compose.v3.yml`](../deploy/docker-compose.v3.yml); use the service and image names from the VM's compose file.
- `image: finchat-backend:${BACKEND_IMAGE_TAG:-finance-agentic}`: one variable decides v3 or v2.
- `env_file: ./backend/.env`.
- Named volumes for `finchat_agents/traces` and `finchat_agents/outputs` (exported files survive restarts).
- `rbac.v3.yaml` mounted read-only (change roles without rebuilding).
- Healthcheck on `/v3/health/live` with a 240 s start period. A stopped SQL warehouse can take a few minutes to start during warm-up.

Deploy:
```
cd <repo>                     # on the VM
git fetch && git checkout finance-agentic && git pull     (Karthik)
docker compose build backend
# in the compose .env: BACKEND_IMAGE_TAG=finance-agentic
docker compose up -d backend
docker compose logs -f backend          # look for "finchat v3 warm-up: {'mcp': 'ok', 'bedrock_sql': 'ok', ...}"
curl -s http://localhost:<port>/v3/health
docker compose exec backend python -m finchat_agents.deploy.smoke --base-url http://127.0.0.1:<port> --user-id <test user id>
```

The smoke script sends the user id in the request, so it works only against a local test instance started with
`ALLOW_REQUEST_IDENTITY=true`. Behind the backend's Entra login, test through the UI instead.

## 4. Health

- `GET /v3/health/live`: the process answers (Docker healthcheck; calls nothing external).
- `GET /v3/health`: readiness. Returns `200` when every enabled check is ok, otherwise `503`:
  ```json
  {"status": "ok|degraded|down", "cached": false,
   "checks": {"mcp": {"status": "ok", "ms": 412}, "bedrock_sql": {"status": "ok", "ms": 820},
              "bedrock_response": {"status": "ok", "ms": 650}, "aiops": {"status": "ok|disabled", "ms": 0}},
   "storage": "enabled", "write_failures": 0}
  ```
  A failed check shows only `"error": "<error type>"` or `"timeout"`. It never shows hosts, URLs, tokens or messages; the full error
  is in the server log. Results are cached for `HEALTH_CACHE_SECONDS` (60 s), so probes don't call Bedrock each
  time. Use `?refresh=true` to re-run the checks.
  - **Green** means `"status": "ok"`.
  - `aiops: disabled` means the warehouse settings are missing. Chat still works but nothing is saved.

## 5. Rollback to v2

1. In the VM's compose `.env`, set `BACKEND_IMAGE_TAG=finance-kpi`. If that image is no longer on the VM, check out
   `feature/finance-kpi` and run `docker compose build backend` first.
2. `docker compose up -d backend`.
3. If the UI was switched to `/v3/chat`, switch it back to the v2 chat URL (see section 6), or keep both routes (see the note below).
4. Check the v2 health or a question as usual.

v3 writes only to `lakehouse_mvpai.aiops.finance_chat_*`. The rows stay and do no harm. Nothing in `silver`/`gold`
changes, so no data rollback is needed. To return to v3, set `BACKEND_IMAGE_TAG=finance-agentic` and run `up -d` again.

## 6. UI change (for the UI owner)

The UI only changes the chat call:
- **Endpoint:** the v2 chat URL becomes `POST /v3/chat`.
- **Request:** `{"conversation_id": "<id or omit for a new chat>", "message": "..."}` with the user's login token.
  The caller comes from `mount_v3(identity=...)`; `user_id`/`groups` in a request are ignored (they are used only with
  `ALLOW_REQUEST_IDENTITY=true`, local testing).
- **Response** (SPEC section 7): `conversation_id`, `message_id`, `status` (`answered|partial|clarification|declined|failed`),
  `answer` (Markdown), `how_calculated`, `tables[{title, columns, rows}]`, `files[{name, path}]`, `suggestions[]`,
  `notices[]`. Render `answer`, then show `notices`, `tables`, `files` and `suggestions` (as clickable follow-ups).
  Send the returned `conversation_id` with the next message.
- **Files:** `files[].path` is a relative URL like `/v3/files/<conversation>/<name>`, fetched with the same login.
  Only the creator can download a file; anyone else gets 404.
- **Optional:**
  - `POST /v3/chat/stream` (SSE `step` events, then one `final` event with the same envelope) for progress;
  - `GET /v3/cards` for the summary cards.

Keep the v2 URL as a config value in the UI so rollback is a config change.
