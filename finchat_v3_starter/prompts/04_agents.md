Task 04: supervisor, catalog, SQL and knowledge agents. Read CLAUDE.md and docs/SPEC.md sections 2-4 first.

Prompts live as Markdown files in agents/prompts/ (versioned, no code in them). Keep each prompt focused.

1. Catalog agent (Sonnet): find tables and columns for a task, prefer gold, return table names, relevant columns,
   join path and caveats. Tools: search_tables, describe_table, get_join_path, get_column_values, get_glossary.
2. SQL agent (Sonnet): write Databricks SQL from the catalog result; run_sql; on error or empty result read the message,
   check values with get_column_values, repair and rerun (max AGENT_MAX_SQL_CALLS). Follow rules.md (balances not summed
   across periods; composite joins in full; fully qualified names). Return rows, the final SQL, and a one-paragraph
   business explanation of the calculation (filters, grouping, period) without SQL words.
   Few-shot: top 3 similar examples from knowledge/examples.yaml.
3. Knowledge agent (gpt-oss): general questions on any topic from model knowledge, no web; start the answer with a
   short "General knowledge:" label; add a date caveat for things that change (rates, standards, laws). Can call get_glossary.
4. Supervisor (Sonnet): classify the request (data / general / mixed); for data call catalog then SQL; for general call
   knowledge; for mixed do both in order. Ambiguity rule: answer the most likely reading, then offer the alternative.
   "Hook or crook": if a route fails try another (gold then silver, wider period, split the question) before giving a
   partial answer that states what is missing. Never invent numbers.
4b. Two modes (SPEC section 3, "Two modes in one runtime"), plain Python, no LangGraph, no KPI search:
   - The supervisor's first model call returns a classification (general | simple_data | complex) together with its
     first action; do not add a separate router LLM call.
   - agents/fast_path.py: for simple_data run search_tables -> SQL agent (single write) -> run_sql -> one repair on
     error or empty result -> final answer step. Return None if still failing.
   - If fast_path returns None or the question is complex, run the full supervisor ReAct loop, passing a
     FastPathAttempt (tables found, SQL tried, error) into its context so it does not start from scratch.
   - Trace each answer's mode: fast | react | fast->react.
5. Final answer step: gpt-oss writes the user-facing answer from the supervisor's result (business tone, short,
   tables when rows > 3) plus `how_calculated` (business language, no SQL). Then the number check from SPEC section 4.6.
6. agents/orchestrator.py: `answer(message, user, conversation_context) -> AnswerEnvelope` matching SPEC section 7
   (without API wiring), emitting trace events.

Acceptance
- Unit tests with fake LLM responses for routing, repair loop, partial answer on budget, number check, fast path
  success, fast path failure escalating to ReAct with the attempt passed in, and no KPI code anywhere.
- The scorecard also shows mode and latency per question, and average LLM calls for fast vs react answers.
- Live run (RUN_LIVE=1) of reference/question_bank ADRA and Fynapse questions through answer(); write a scorecard
  (correct / partial / could-not-answer / wrong / error, latency per question) to backend/finchat_agents/eval_reports/.
  Scoring compares numbers in the answer with expected values in code.
- Report: scorecard summary, the wrong answers with their traces, and suggested generic fixes (page / glossary / example).
