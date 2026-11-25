# Task 10 report: deploy v3 (21 Nov 2026)

The existing backend app, its Dockerfile, docker-compose file and the UI are not in this workspace (only
`backend/finchat_agents/` is). So the image and compose changes are delivered as ready-to-merge files plus exact
instructions, and the UI change is documented for the UI owner. Nothing was built or run against Docker, AWS or
Databricks here: Docker is not installed on this machine, and live runs happen on the company laptop / VM.

## What was built
- **Health** (`api/health.py`, `GET /v3/health`):
  - checks MCP (`SELECT 1` through the DBSQL MCP client), `bedrock_sql` (Claude ping), `bedrock_response` (gpt-oss
    ping) and `aiops` (one read of `finance_chat_conversations`, or `disabled` when the warehouse settings are missing);
  - checks run in parallel, each with a timeout;
  - returns `200` only when every enabled check is ok, otherwise `503` with `degraded` / `down`;
  - results are cached for `HEALTH_CACHE_SECONDS` (60), and `?refresh=true` re-runs the checks;
  - the output holds only status, time taken and the error type: no hosts, URLs, tokens or messages (a test asserts this).
- **Liveness** `GET /v3/health/live`: calls nothing external; used by the Docker healthcheck.
- **Warm-up on startup** (`ChatService.warm_up`, `api/app.py:mount_v3`):
  - `mount_v3(app, identity=...)` mounts `/v3` on the existing backend app and wraps its lifespan;
  - after the app's own startup it runs the health checks with a long timeout (`WARM_UP_TIMEOUT_SECONDS` 180, for a
    stopped warehouse), logs the result per check, and primes the health cache;
  - a failed warm-up never blocks startup;
  - shutdown flushes pending aiops writes;
  - `create_app` (standalone) now uses the same path.
- **Docker** (`deploy/Dockerfile.v3`, `deploy/Dockerfile.v3.dockerignore`):
  - python:3.13-slim, non-root user, port 8010, HEALTHCHECK on `/v3/health/live`;
  - the lines to copy into the existing backend Dockerfile are marked;
  - excluded from the image: `.env*`, traces, outputs, tests, eval, reference (the question banks), docs, `.venv`;
  - no secrets baked in: settings come from `env_file` at run time.
- **Compose** (`deploy/docker-compose.v3.yml`):
  - image tag `${BACKEND_IMAGE_TAG}` selects `finance-agentic` (v3) or `finance-kpi` (v2);
  - `env_file`, volumes for traces and outputs, `rbac.v3.yaml` mounted read-only, healthcheck with a 240 s start period.
- **Smoke test** (`deploy/smoke.py`): `python -m finchat_agents.deploy.smoke --base-url ... --user-id <test id>`.
  It checks live, health green and 4 generic questions (not from any question bank). It prints statuses and timings
  only, and exits 0 when all pass.
- **Docs** (`docs/DEPLOY.md`): options A and B, environment variable names, compose changes, deploy commands, health
  format, rollback steps and the UI change. `.env.example` gained the new names (`OUTPUT_DIR`,
  `SUMMARY_METRICS_FILE`, `WARM_UP_ON_START`, `WARM_UP_TIMEOUT_SECONDS`, `HEALTH_CACHE_SECONDS`).

## v2 references on this branch (prompt step 4)
No imports, routes or config that point at v2 modules (searched for langgraph, langchain, KPI, finance_react, fincore
and v2 across all runtime `.py` files). Remaining mentions, all harmless:
- `storage/aiops.py`, `storage/records.py`, `memory/user_memory.py`: columns `kpi_ids`, `frequent_kpis`, and the
  `answer_path` value `kpi`. These columns are in the shared aiops table schema; v3 writes NULL and never uses them.
  Keep them unless the tables are redesigned.
- `knowledge/joins_proposed.yaml` / table pages: gold tables whose *names* contain "kpi" (for example
  `vw_kpi_pipeline_success`). That is data, not KPI code.
- `knowledge/joins.yaml` comment: names the fincore join recipes as a source.
- I could not check the existing backend app, the UI or the VM compose file (not in this workspace). Please search them
  for v2 finance imports or routes when merging (for example the v2 chat route and LangGraph imports).

## Tests
`..\.venv\Scripts\python -m pytest -q`: 295 passed, 30 skipped (live); 302 after the task 09 superseding change. New `test_deploy.py` (12 tests):
- green / degraded / down, disabled checks, timeout, and a check that returns False;
- error output shows the type only, never the message (secret-like strings and hosts are absent);
- cache and refresh;
- a real ChatService pings both models with no tools, MCP `SELECT 1` and an aiops read, and never writes;
- `/v3/health` returns 200 when green and 503 when a check is down; `/v3/health/live` works;
- `mount_v3` runs after the existing lifespan's startup, mounts `/v3`, warms up, and flushes on shutdown;
- a failed warm-up does not block startup;
- smoke pass and fail paths;
- the dockerignore excludes secrets and local data, and runtime code never imports the excluded folders.

Not verified here: `docker build`, the container on the VM, live `/v3/health` and the smoke questions (acceptance
items). They need the VM; the steps are in `docs/DEPLOY.md` section 3.

## Assumptions
- **Option A** (mount v3 in the existing backend app) is the default, because SPEC says the existing app and UI stay.
  Option B (a separate container on 8010) is documented as an alternative.
- The compose service is called `backend` and the image `finchat-backend`. These are placeholders, to be replaced
  with the VM's names.
- `/v3/health` is readiness (503 unless green) and is cached, so a probe costs at most one Bedrock ping per model per minute.
  Docker uses the liveness route, so a Bedrock outage does not restart the container.
- Bedrock credentials on the VM should come from an instance role or a non-personal role, not personal keys.
- The image excludes `eval/`. Scorecards and workflow evaluations run on the laptop, not in the container.

## Open questions
1. **Option A or B?** Can the existing backend take `finchat_agents/requirements.txt`? Send me any version conflicts.
2. What are the service and image names in the VM's compose file? Is `finance-kpi` already tagged there for rollback?
3. Who owns the UI change to `/v3/chat`? When will the backend pass its Entra identity to `mount_v3(identity=...)`, so
   the temporary `user_id` in the body and query can go?
