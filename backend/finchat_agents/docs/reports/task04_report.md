# Task 04 report: supervisor, catalog, SQL and knowledge agents (21 Nov 2026)

## Scorecard
**Not run.** This machine has no AWS credentials and no `backend/.env`, so the live question-bank run could not
happen here. Run it on the machine with Bedrock and the service principal:

```
cd "D:\Finance chat bot\backend"
$env:RUN_LIVE="1"
.venv\Scripts\python -m pytest finchat_agents/tests/live -v -s          # smoke tests first
.venv\Scripts\python -m finchat_agents.eval.scorecard --banks adra fynapse
```
The report lands in `eval_reports/scorecard_<time>.md` (+ `.json`): category counts, per-question category / status /
mode / latency / LLM calls, averages per mode (fast vs react), and for every wrong, error or partial answer the question,
expected values, answer, how_calculated, SQL and the trace file. `--repeat 3 --limit 5` gives the consistency check.
Wrong answers and suggested generic fixes can only be reported after that run.

## Files
- `agents/prompts/`: `supervisor.md`, `catalog.md`, `sql.md`, `knowledge.md`, `answer_writer.md`, `fast_sql.md`
  (Markdown, no code). The SQL agent, catalog agent and fast path also get `knowledge/rules.md`.
- `agents/specialists.py`: catalog agent (search_tables, describe_table, get_join_path, get_column_values, get_glossary),
  SQL agent (describe_table, get_join_path, get_column_values, resolve_period, resolve_entity, run_sql, calculate; top-3
  similar examples added to every task), knowledge agent (gpt-oss, get_glossary). Structured results via a
  `submit_result` finish tool.
- `agents/supervisor.py`: `route` tool (general | simple_data | complex + standalone question) in the first call;
  agents as tools; structured draft (status, answer, how_calculated, result_ids, caveats, alternatives).
- `agents/fast_path.py`: search_tables -> entity/period hints (cached lookups) -> SQL writer (1 call) -> run_sql ->
  one repair on error or empty result -> success, or `None` + `FastPathAttempt` (tables, SQL tried, errors).
- `agents/answer.py`: gpt-oss answer writer + `how_calculated`; number check -> one rewrite -> caveat notice; envelope
  tables built in code from query results with more than 3 rows.
- `agents/number_check.py`: numbers in the answer must match result cells, row counts, column totals, calculate outputs,
  general-knowledge texts or the question, to the precision shown (millions, %, signs handled).
- `agents/orchestrator.py`: `Orchestrator.answer(message, user, conversation_context) -> AnswerEnvelope` (SPEC section 7
  fields; `debug` with mode, classification, latency, LLM/SQL calls, SQL, fast-path attempt is excluded from the
  JSON). Modes: general | fast | fast->react | react; `route` and `answer` trace events.
- `runtime/llm_call.py`: one traced, retried model call (used by the loop, fast path and first supervisor call);
  `run_loop(initial=...)` continues from the classification call; `Agent.extra_context()` hook.
- `eval/scoring.py`, `eval/scorecard.py`: question-bank loader (paraphrases as separate cases, PII cases scored for the
  standard role), code scoring (numbers with tolerance incl. table cells, required text, not-found / cannot-compare /
  masking rules), runner and report writer.
- Tests: `test_agents.py`, `test_scorecard.py`, `tests/live/test_orchestrator_live.py`.

## Tests
`..\.venv\Scripts\python -m pytest -q`: 194 passed, 27 skipped (live). With fake LLMs and the fake MCP server:
routing to knowledge; fast path success in 3 LLM calls; fast path failure (error, repair, cannot_answer) escalating to
the supervisor with the attempt in its context; complex request reusing the first call (no second classification call)
and delegating catalog -> SQL with few-shot examples; SQL agent repair after a database error; partial answer on the step
budget; number check rewrite and caveat; no-access user declined without LLM calls; supervisor decline; conversation
context; tables only above 3 rows; model failure -> failed envelope; no "kpi" in any agent, tool, knowledge or eval file.

## Assumptions
- A user without a role is declined before any LLM call, also for general questions (simplest safe reading of
  "unknown user = no access").
- `simple_data` that the fast path cannot answer (including an empty result, which may be a valid "not found") goes to
  the full loop; latency was accepted for answer quality.
- The supervisor (not the user-facing writer) sees all agent output; the writer only gets the draft and up to 20 rows per
  result, and may not add numbers.
- General-knowledge answers skip the number check (labelled "General knowledge:"); numbers from the knowledge agent are
  accepted in mixed answers.
- Scoring: a not-found / cannot-compare answer is wrong if it states a figure not in the question (years and numbers
  up to 31 ignored); PII cases need masking wording or "not approved" wording for the standard role.

## Open questions
1. Please run the live scorecard (commands above) and send me the report; I will analyse wrong answers and propose
   generic fixes (pages, glossary, examples, prompts).
2. Should general questions be allowed for users without a data role?
3. Close-task questions (close_recon.yaml task items) are not in the scorecard: the task tables are not modelled.
