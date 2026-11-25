# Task 07 report: conversation summaries and the 30-question limit (21 Nov 2026)

## What was built
- **Context per question:** the rolling summary (if any) plus the last 5 turns verbatim (`HISTORY_TURNS`), loaded from
  aiops for the user's own conversation (the last 50 turns are read to decide on summarising).
- **Rolling summary** (`memory/summary.py`, prompt `agents/prompts/summary.md`, gpt-oss): when the summary plus the
  turns not yet summarised pass `SUMMARY_TOKEN_THRESHOLD` (default 6,000 tokens, estimated at ~4 characters per token),
  the summary is rewritten with headings Entities / Periods / Topics and data / Open threads / Key numbers (each number
  with its source question, copied from the answers). It runs **after** the answer, in the background writer, and is
  stored with a guarded `UPDATE ... finance_chat_conversations SET summary, summary_through_turn, summary_updated_at`
  (aiops only). The answer never waits for it.
- **Follow-ups:** the supervisor gets the summary and recent turns and writes a complete `standalone_question` (prompt
  rule added, with an example); the fast path and SQL work on the rewrite; `standalone_question` is stored per message.
  Numbers from earlier turns are context only: the number check still requires the current question's results.
- **30-question limit** (`CONVERSATION_QUESTION_LIMIT`): question 30 is answered with the notice "This conversation has
  reached the 30-question limit ..." and its summary is refreshed even below the threshold. The next message starts a
  new conversation (new `conversation_id` returned) seeded with that summary (or, if the summary is not ready, the old
  summary plus the last questions), with the notice "The previous conversation reached the 30-question limit, so this
  question starts a new conversation. A summary ... was carried over."
- **User memory** (`memory/user_memory.py`, `memory/filters.py`):
  - The entity and period filters an answer used are read **from its final SQL in code** (literals compared to the
    pages' entity / entity-name / period columns) and stored in `finance_chat_messages.plan` as
    `{"entities": [...], "periods": [...]}` (the column was unused in v3).
  - After each answered data question, `finance_chat_user_memory` is recomputed from the user's last 30 answered
    questions: `frequent_entities` (top 5 with counts), `default_entity` / `default_period` only for a clear habit
    (at least 5 times and at least 60% of the questions that named one). `frequent_kpis` stays NULL.
  - The habit is passed to the supervisor and the fast path as a hint, to be used only when the question names no
    entity. When the answer's SQL used the habitual entity and the question did not name it, a fixed notice is added
    in code: "I assumed <entity>, the entity you usually ask about, because the question did not name one. Ask again
    with another entity if you meant something else."

## Files changed
`memory/` (new: summary.py, filters.py, user_memory.py), `agents/prompts/summary.md` (new), `api/service.py`
(rewritten flow: load summary + turns, rollover, memory hint, notices, background summary and memory jobs),
`storage/aiops.py` (user-memory table columns, summary UPDATE, reads for plans and memory), `storage/records.py` (plan
JSON, seeded summary on a new conversation), `agents/orchestrator.py` (`debug.filters`, `user_hint` in the context),
`agents/fast_path.py` (extra hints), `agents/prompts/supervisor.md` (follow-up and habit rules).

## Tests
`..\.venv\Scripts\python -m pytest -q`: 271 passed, 30 skipped (live). New in `test_memory.py`: token estimate and
threshold; summary written (UPDATE with the right through-turn) only above the threshold; summary and last 5 turns reach
the supervisor; summarizer prompt carries the previous summary and turns; summary UPDATE refuses non-aiops targets;
follow-up rewrite used by the fast path and stored; question 30 gets the limit notice and a forced summary; question 31
gets a new conversation id, the seeded summary, the rollover notice and turn 1; fallback seed; filters read from SQL
(entity code, LIKE name, Fynapse fiscal year/period); habit thresholds; exact hint and notice wording; end to end the
hint reaches supervisor and fast path, the notice is added, plan and memory rows are written.

## Assumptions
- Summaries cover all turns up to the current one; the last 5 turns are still shown verbatim (small overlap, simpler).
- The summary job runs after the answer; if the user sends the next question very quickly it may not be ready yet
  (the next turn then uses the previous summary plus the recent turns). At the limit, the rollover uses a plain seed if
  the model summary is not stored yet.
- "Clear habit" = at least 5 of the last 30 questions and at least 60% of those that named an entity.
- The period habit is stored but not used as a hint yet (the task asks for entities); it is ready if wanted.

## Open questions
1. Is 60% / 5 questions the right bar for a "clear habit"?
2. Should the period habit also be used as a hint (e.g. "latest period you usually ask about")?
