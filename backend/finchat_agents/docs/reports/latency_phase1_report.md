# Latency phase 1 report (21 Nov 2026)

Safe speed-ups that do not change how answers are produced: same agents, same SQL checks, same number check.

## What changed

| # | Change | File | Expected effect (estimate until measured) |
|---|---|---|---|
| 1 | **Reused Databricks connections.** A pool of up to 4 open connections instead of opening a new one for every aiops read and write. Reopened when the token is refreshed or after 45 minutes; a dropped connection is retried once on a fresh one | `storage/aiops.py` | 1–3 s saved per aiops query (the health check showed about 3 s for one query on a new connection) |
| 2 | **Context reads in parallel.** The conversation, its recent turns and the user's habits are read at the same time, not one after another. The turns query now also filters on the user | `api/service.py`, `storage/aiops.py` | Context loading takes as long as the slowest single read |
| 3 | **User habits cached** for 10 minutes per user (refreshed right after they are recomputed) | `api/service.py` | One aiops read fewer on most questions |
| 4 | **Faster SQL polling.** The first waits are 0.25 s and 0.5 s, then every 1 s as before | `tools/mcp_client.py` | 0.5–1 s per query that needs polling |
| 5 | **Conversation cached in Claude's prompt cache.** A third cache point at the end of the conversation, so each step of an agent loop reads the earlier steps from the cache | `llm/claude_bedrock.py` | Faster later steps on complex questions; check `cache_read_tokens` |
| 6 | **Compact table pages.** `describe_table` leaves out sample rows, shrinks the profile to "columns empty in every row" and keeps at most 12 stored values per column. Columns, joins, metrics and notes stay whole. `detail='full'` still returns the whole page | `tools/catalog.py` | 47% less text across all 143 pages (for example `adra_account_facts` 21,840 to 12,549 characters); smaller requests on every later step |
| 7 | **Context loading is measured.** Recorded as its own step (`load_context`) in the message events, and included in `total_latency_ms` | `api/service.py`, `agents/orchestrator.py`, `storage/records.py` | Lets you see the gap that was not measured before |

## Tests

`345 passed, 30 skipped` on the latest packages and on the backend's versions (FastAPI 0.115.2, pytest 8.3.3). New tests:
- the pool reuses one connection until the token changes, reopens old connections, retries a dropped pooled connection once, and does not retry a real error;
- the context reads run together, the turns query filters on the user, and user habits are cached;
- the cache point is on the last block only and the caller's messages are not modified;
- compact pages are at least 30% smaller and keep columns, values for filters, joins, metrics, notes and the empty columns;
- `describe_table` is compact by default and full on request;
- the new polling waits.

Not tested here: real Databricks and Bedrock timings. Measure on the laptop or the VM.

## How to measure

Ask the same 10 questions before and after (simple and comparison, from `docs/TEST_QUESTIONS.md`), then run the two queries
from the latency plan. Also check:
- the `load_context` step's `duration_ms` in `finance_chat_message_events`;
- on later steps of a complex question, the Claude calls should show `cache_read_tokens` above zero in the trace file
  (`finchat_agents/traces/events.jsonl`).

## Infrastructure (no code, your side)

- **Keep the SQL warehouse warm** during working hours: a serverless SQL warehouse, or a longer auto-stop. A cold
  warehouse adds minutes to the first question.
- **Host the backend VM in the same region as Bedrock and Databricks.** Testing from a laptop over VPN adds network time
  to every call.

## Not in phase 1

Fewer model calls (one query for both periods of a comparison, skipping the catalog agent when the search is confident,
merging routing and SQL writing) is phase 2. Streaming the answer is phase 3.
