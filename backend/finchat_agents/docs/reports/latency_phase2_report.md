# Latency phase 2 report (21 Nov 2026)

Items 2.1, 2.2, 2.4, 2.5. Tests: 348 passed, 30 skipped. Not measured here (no live calls); measure on the laptop.

| # | Change | Files | Expected effect |
|---|---|---|---|
| 2.1 | Shorter SQL-writer output: one-sentence explanation (max 25 words), only needed columns, no comments | `agents/prompts/fast_sql.md`, `agents/fast_path.py` | Fewer output tokens on every data question (output tokens dominate the SQL step) |
| 2.2 | `standalone_question` is optional in the route call; only filled when the request refers to earlier turns. Falls back to the user's own text | `agents/supervisor.py`, `agents/prompts/supervisor.md` | Route call about 1-2 s shorter on first questions |
| 2.4 | When the number check forces a rewrite, a trace event `number_check_rewrite` (agent `answer_writer`) records the numbers and about 40 characters around each | `agents/answer.py` | Shows why 2 of 6 questions were rewritten (about 2.4 s each) |
| 2.5 | At startup, entity values and period lists are preloaded into the cache using the same functions and cache keys as the resolvers; cache lifetime raised from 1 h to 6 h | `tools/resolve.py` (`prewarm_lookups`), `api/service.py` (`warm_up`), `config.py` | First question no longer pays about 1.3 s for lookup queries. Failures are skipped and bounded by `warm_up_timeout_seconds` |

Preloading only reads (guarded SELECTs through the normal path). The result of `warm_up()` now has a `preloaded` entry with counts.

## How to check
- `finance_chat_message_events`: look for `name = 'number_check_rewrite'`; the input column has the numbers, output the context.
- Startup log: `preloaded` counts (entities, periods, failed).
- Compare route and SQL-writer step durations against the phase 1 run.

## Assumptions
- Preloading uses a service-level role with all domains (no user data is returned to anyone; it only fills the cache).
- 2.3 (comparisons in one query) and the history-cache tweak are not included.
