# Running the live tests (company laptop)

Development and offline tests happen elsewhere; all live runs (Bedrock, Databricks) happen on the company laptop.

## 1. Copy the code
Copy the folder `backend/finchat_agents/` into the repo's `backend/` folder. Skip these if present:
`__pycache__/`, `.pytest_cache/`, `traces/`, `eval_reports/traces/`. Never copy a `.env` file between machines.

## 2. Python environment (once)
```powershell
cd <repo>\backend
python -m venv .venv
.venv\Scripts\python -m pip install -r finchat_agents\requirements-dev.txt
.venv\Scripts\python -m pytest finchat_agents -q        # offline tests: all should pass, live ones skipped
```

## 3. backend/.env (on the laptop only, never committed)
Copy `finchat_agents/.env.example` to `backend/.env` and fill in:
- Bedrock: `AWS_REGION`, and either `AWS_ACCESS_KEY_ID` + `AWS_SECRET_ACCESS_KEY` (read from `backend/.env`; add `AWS_SESSION_TOKEN` for temporary keys) or `AWS_PROFILE`. Use keys of a non-personal app user/role so your name stays out of CloudTrail.
  Access keys, if used, go in the shell environment, not in `.env`.
- Databricks MCP: `DATABRICKS_MCP_URL`, `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`.
- aiops writes (task 05): `DATABRICKS_SERVER_HOSTNAME`, `DATABRICKS_HTTP_PATH`.
Check the repo's `.gitignore` covers `backend/.env`.

## 4. Live runs, in this order
```powershell
cd <repo>\backend
$env:RUN_LIVE="1"
.venv\Scripts\python -m pytest finchat_agents/tests/live -v -s
.venv\Scripts\python -m finchat_agents.eval.scorecard --banks adra fynapse
.venv\Scripts\python -m finchat_agents.eval.workflows          # task 06: 10 sample workflows
.venv\Scripts\python -m finchat_agents.summary.run --dry-run   # task 09: prints cards, writes nothing
```
- Summary agent real run (after you create the two tables from `reference/aiops/finance_chat_summary_cards.sql`):
  `.venv\Scripts\python -m finchat_agents.summary.run --trigger manual`. Without the tables it stops with a clear message.
- aiops tables missing? Add `$env:AIOPS_CREATE_TABLES="1"` before the pytest line (creates them only if absent, aiops schema only).
- Quick check first: `... -m finchat_agents.eval.scorecard --limit 5 --no-paraphrases`.
- gpt-oss tool test: if only the `openai` variant passes, set `GPT_OSS_TRANSPORT=openai` in `.env`.

## 5. What to send back
- `finchat_agents/eval_reports/scorecard_<time>.md` and `workflows_<time>.md`
- the console output of any failing live test (the Fynapse entity values line too)
- for wrong answers: the matching files in `eval_reports/traces/<time>/` (they contain data values: share internally only)

What the services see: Databricks shows the service principal; the aiops test rows use `user_id = live-test-user`;
AWS CloudTrail shows whichever AWS identity `.env` / the shell uses.

## Deploy check (task 10, on the VM)
See `docs/DEPLOY.md`. After `docker compose up -d backend`:
```
curl -s http://localhost:<port>/v3/health            # expect "status": "ok" (HTTP 200)
docker compose exec backend python -m finchat_agents.deploy.smoke --base-url http://127.0.0.1:<port> --user-id <test user id>
```
Send me the health JSON and the smoke output (statuses and timings only; no secrets in either).
