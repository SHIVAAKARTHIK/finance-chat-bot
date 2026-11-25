# Backend integration report (21 Nov 2026)

Based on Karthik's Copilot report of the company backend (routes, SSE contract, response shape, auth, app setup,
storage, tests). Built from the backend's app code and the UI contract only: no code or logic from the previous agent,
no KPI data.

## Files
- `integration/ui_contract.py`: v3 envelope to UI response object; delta chunking.
- `integration/stream.py`: SSE in the UI format (`status` / `delta` / `complete` / `error`), stages from v3 trace
  events, a keep-alive every 15 s (the current stage re-sent), generic errors.
- `integration/backend.py`:
  - request model (query max 4000 characters, session/conversation id max 128);
  - identity from `get_current_user` + `agent_roles`;
  - the 3 routes (chat, stream, history) with an optional rate limit;
  - `install_backend()`, which also mounts `/v3` with the same identity, warms up and flushes on shutdown.
- `storage/aiops.py`: `user_history()` (the caller's own recent exchanges, filtered by `user_id` in SQL).
- `requirements.txt`: ranges compatible with the backend's pins; one file for runtime and tests (the separate dev and tested-version files were merged into it).
- `docs/BACKEND_INTEGRATION.md`: steps for `main.py`, rbac, env, Docker, stream and mapping.
- `tests/test_integration_backend.py`: 13 tests.

## Tests
- Main venv (latest packages): 316 passed, 30 skipped (live).
- Scratch venv with the backend's versions (FastAPI 0.115.2, Starlette 0.40, uvicorn 0.32.0, pydantic-settings 2.6.0,
  httpx 0.27.2): 316 passed, 30 skipped.
- New tests:
  - the stream contract, mirroring the backend's own test (status, delta, complete; the joined deltas equal the
    answer; stages only from the UI's list; no SQL; `kpi` null; identity from the token, not the body);
  - the non-stream body; 422 limits; 401 and declined; generic stream error with no internals;
  - keep-alive; rate limit on every route;
  - field mapping, chunking and clarifications; stage mapping;
  - history scoped to the caller and grouped by conversation;
  - `install_backend` order with the existing lifespan.

Not verified: the backend itself and the UI (not in this workspace); live runs happen on the company laptop.

## Assumptions
- `table.rows` are objects keyed by column `key`.
- `breakdown` is always `"[]"` (v3 shows results as a table).
- `answered` and `partial` both map to `success`; partial notices go to `explanation.caveats`.
- `clarifications` are appended to the question as text.
- The history response shape (see the doc, section 9).
- File links are added to the answer as Markdown links.
- `BEDROCK_MODEL_*` in the shared env must hold v3 model ids. `DATABRICKS_SCHEMA` (the backend uses `silver`) is ignored by v3, which always writes to `aiops`.

## Answered by the backend's UI code (21 Nov 2026)
History is a flat array of wire items; table rows are objects with string values; a null `kpi` makes the UI hide the
explanation (notices now also go into the answer text); the 7 role labels are mapped in `rbac.v3.yaml`; clarifications are
`Record<string, string>`; the backend's `DATABRICKS_SCHEMA` is `silver`, so v3 now ignores that variable.

## Open questions
1. History order and the meaning of `threads=true` (v3: newest first; the newest `limit` conversations).
2. Role mapping in `rbac.v3.yaml` (Controller -> gl_reader etc.): confirm, and fill in the `users` block if needed.
3. Optional UI change: show the explanation (steps, filters, caveats) when `kpi` is null.
4. File downloads need the UI's authenticated API client.
