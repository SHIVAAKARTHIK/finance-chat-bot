# Task 05 report: v3 API endpoint and aiops storage (21 Nov 2026)

## Files
- `storage/aiops.py`: typed MERGE builder (one or many rows, `UNION ALL` source, `CAST(:param AS <type>)` for every
  column from the DDL, arrays as `array(:p0, ...)`); updates only the columns a write provides; insert-only columns
  (created_at; conversation title and summary_through_turn); check-constraint validation before writing; hard guard
  that only `lakehouse_mvpai.aiops.finance_chat_*` can be written; `ensure_tables()` = the reference DDL
  (`storage/aiops_ddl.sql`), CREATE TABLE IF NOT EXISTS only, existing constraints skipped; reads for follow-ups;
  `DatabricksSqlExecutor` (databricks-sql-connector, fresh service-principal token per batch, worker thread);
  CLI `python -m finchat_agents.storage.aiops --create-tables | --print-ddl` (run from `backend`).
- `storage/writer.py`: background writer (one ordered queue; failures logged and kept for /health; never blocks).
- `storage/records.py`: v3 -> aiops mapping. `storage/trace_sink.py`: the aiops trace sink (one row per LLM call and
  tool call, written when the answer is done).
- `api/service.py`: ChatService: identity -> role, last 5 visible turns + summary of the user's own conversation,
  `processing` row, answer, final row, conversation update, all in the background.
- `api/router.py`: `create_router(service, identity=...)` with `POST /chat`, `POST /chat/stream` (SSE), `GET /health`.
- `api/app.py`: `build_service()` from settings, and a minimal standalone app (`uvicorn finchat_agents.api.app:app`).
- `requirements.txt`: fastapi 0.165.0, uvicorn 0.54.0. Orchestrator debug now carries tokens, models, row count,
  preview, domains.
- Tests: `test_storage_api.py`, `tests/live/test_api_live.py`. v2 untouched.

## aiops mapping
| Column | v3 value |
|---|---|
| messages.status | answered / clarification / declined / failed; **partial is stored as `answered` with `error_code = 'partial_answer'`** (the constraint has no partial); a `processing` row is written first |
| intent | data / general / mixed (workflow comes with task 06) |
| answer_path | `adhoc` for data, `declined`, `clarify`; NULL for general knowledge |
| sql_text / sql_source | all SQL of the question joined with `;` (audit only) / `generated` |
| result_row_count / result_preview | last query result; first 5 rows as JSON, capped at 2,000 chars |
| answer_text | answer + "How this was calculated: ..." |
| kpi_ids, plan, trust_label, first_token_ms | NULL |
| message_events | step_name = agent (LLM call) or tool name; step_order per question; attempt 1; status ok / failed; model_provider `aws-bedrock`; payloads are the trace previews (capped 8,000 chars) |
| conversations | turn_count, last_message_at, domain updated each turn; title (first question) set once |

## Tests
`..\.venv\Scripts\python -m pytest -q`: 212 passed, 30 skipped (live). With a fake connector: MERGE shape (keys, casts,
arrays, NULL arrays, update list, insert-only columns), multi-row event MERGE, refusal of any non-aiops /
non-finance_chat target (including an injection attempt in the table name), DDL only targets aiops, existing
constraints skipped, constraint values (partial -> answered), executor uses a fresh token per batch; end to end:
conversation + processing + events + final + conversation update in order, background write failure does not fail the
request, follow-up loads the last turns oldest first and sets turn_index, another user's conversation is never
continued, unknown user declined; API: SPEC envelope only (no debug, no SQL), 401 without identity, 422 on empty
message, SSE steps then one final event (no payloads in steps), auth identity wins over the body.

Live (`$env:RUN_LIVE="1"`, not run here): one ADRA question through /v3/chat, then reads back one conversation row, one
message row (answered, adhoc) and event rows. Add `$env:AIOPS_CREATE_TABLES="1"` to create the tables first if needed.

## Steps for the UI team
1. The backend mounts the router once (`app.include_router(create_router(service, identity=...), prefix="/v3")`).
2. Call `POST /v3/chat` with JSON:
   ```json
   {"conversation_id": null, "message": "How many Northwind accounts are pending closure for Feb 25?",
    "user_id": "<Entra object id>", "groups": ["Controller"]}
   ```
   `user_id` / `groups` are needed **only until the backend passes its Entra identity** to the router; then drop them.
3. Response (render `answer`; show `how_calculated` under it; render each `tables[]` entry as a table; `notices` as a
   warning line; `suggestions` as clickable follow-ups):
   ```json
   {"conversation_id": "...", "message_id": "...", "status": "answered|partial|clarification|declined|failed",
    "answer": "...", "how_calculated": "...", "tables": [{"title": "Details", "columns": [], "rows": []}],
    "files": [], "suggestions": [], "notices": []}
   ```
4. Send the returned `conversation_id` with the next message for follow-ups; omit it to start a new chat.
5. Optional: `POST /v3/chat/stream` (same body) returns `text/event-stream`: `event: step` lines while working
   (`{"type", "agent", "tool"?, "status"}`), then one `event: final` with the same envelope as above.
6. Timeouts: allow up to 5 minutes per request (SPEC latency targets: analysis < 2 min, workflows < 5 min).

## Assumptions
- **Identity:** there is no existing app in this workspace to read the Entra identity from, so the body's `user_id` /
  `groups` are accepted for now; `create_router(..., identity=dep)` switches to the app's auth without changing the router.
- Reads for follow-ups happen before answering (timeout 5 s; on failure the question is answered without history).
- A conversation id that exists for another user starts a new conversation (new id returned).
- If the load fails, turn_index falls back to 1 (logged).
- Storage is optional: without DATABRICKS_SERVER_HOSTNAME / HTTP_PATH the API still answers and logs a warning.
- Tables are created only via the CLI or the live test flag, never automatically at app start.

## Open questions
1. Which header / dependency in the existing backend carries the Entra object id and groups?
2. Is `partial -> answered + error_code 'partial_answer'` acceptable, or should the constraint get a `partial` value?
3. Should event payloads (prompt previews, tool inputs/outputs up to 8,000 chars) be redacted further before going to aiops?
