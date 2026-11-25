# Task 06 report: analyst agent, action agent, workflows (21 Nov 2026)

## What was built
- **Analyst agent** (`agents/prompts/analyst.md`, Sonnet): splits a multi-step question into sub-questions, asks the
  SQL agent once per sub-question (so every query passes the guardrails), combines results with `calculate`, and
  returns the answer, the steps in business language, result ids, status and caveats.
- **Action agent** (`agents/prompts/action.md`, Sonnet) with two tools (`tools/actions.py`):
  - `export_excel(title, tables)`: one sheet per table; tables are referenced by result_id, rows are built in code
    (never typed by the model; personal data already masked).
  - `save_report(title, sections)`: Markdown, plus Excel when sections include result tables. Section text is
    number-checked: a number that is not in this question's results or calculations is refused with a fixable message.
  - Files go to `OUTPUT_DIR/<conversation_id>/` (default `finchat_agents/outputs/`, git-ignored) and appear in the
    envelope `files` as `{name, path}`. Nothing is emailed, shared or sent; the prompt says so and there is no tool for it.
  - **Idempotent:** the file name comes from the message id, the action and the title, and files are written
    atomically, so a retried step overwrites the same file instead of creating a second one.
- **Workflows:** a new route `workflow` (the supervisor's first call). The supervisor calls `record_plan` first (a
  `plan` trace event), runs each step through the right agent carrying results forward, and reports every step as
  done / done_with_caveat / not_done with a detail. The per-step list is appended to the answer **in code**, so a
  planned step can never be silently dropped (missing ones show as "not done"). Any not-done step makes the status
  `partial`. User instructions can change steps, format and tone, never permissions: an "email it" or "mark as
  finalized" step is reported not done.
- Supervisor now has: route, record_plan, ask_catalog_agent, ask_sql_agent, ask_analyst_agent, ask_knowledge_agent,
  ask_action_agent. aiops `intent = 'workflow'` for workflows.
- **10 sample workflows** (`eval/workflows.yaml`, ADRA and Fynapse; two contain a not-allowed step) and a live runner
  `python -m finchat_agents.eval.workflows` that checks in code: every planned step reported, minimum step count,
  required file types saved and opening, not-allowed steps reported as not done, no claim that anything was sent.
  Report: `eval_reports/workflows_<time>.md`. Added to `docs/LIVE_RUN.md`.

## Tests
`..\.venv\Scripts\python -m pytest -q`: 258 passed, 30 skipped (live). New in `test_workflows.py`: a full workflow with
fakes (plan event, SQL, Excel export that opens with the right rows, a not-done email step, status partial, file in the
conversation folder, runner check passes); idempotent export on retry (one file; a new message gets its own);
export refuses unknown result ids and typed rows; save_report refuses an invented number and writes Markdown + Excel;
the analyst runs two queries through the SQL agent and calculates the change; step formatting reports every planned step.

Live (company laptop): the 10 workflows (`eval.workflows`) and the analyst questions in the scorecard that need two
queries (e.g. the period comparisons) are not run here.

## File downloads: GET /v3/files/{conversation}/{file_name}
- The envelope's `files[].path` is now the download URL (e.g. `/v3/files/<conversation_id>/<name>.xlsx`), never a server
  path; the server path stays in the trace/debug data only.
- Only the user who created a file can download it: each file has an owner record (`<name>.meta.json`) and anyone
  else gets 404, so the route does not reveal whether a file exists. The user must still have a role.
- Names are validated (letters, digits, `_`, `-`; `.xlsx` or `.md` only) and resolved strictly inside the outputs
  folder: path traversal and owner records are refused. Responses are `attachment` downloads with `no-store` caching.
- Identity: like /v3/chat, the router's `identity=` dependency (the app's Entra auth) wins; until then a `user_id`
  query parameter is accepted. UI: `GET {files[].path}?user_id=<Entra object id>` (drop the parameter once auth is wired).
- Tests (`test_files_api.py`): owner download, other user / no role / missing file -> 404, no identity -> 401,
  traversal and odd names -> 404, auth identity cannot be overridden by the query.

## Assumptions
- Report text may only contain numbers from the question's results, calculations or the question itself (the same
  rule as answers).
- The action agent runs on Sonnet (structured tool use matters more than wording here).

## Open questions
1. File retention: files are kept until removed. Should old outputs be cleaned up after N days?
2. Should saved reports also be listed per conversation (an aiops table), or are the files enough for now?
