Task 06 (after Monday): analyst agent, action agent, user workflows. Read CLAUDE.md and docs/SPEC.md first.

1. Analyst agent (Sonnet): multi-step questions (comparisons, trends, variances, ratios, top-N with context). Breaks the
   question into sub-tasks, calls ask_sql_agent per sub-task (so every query passes the guardrails), combines results
   with calculate. Returns rows, the steps taken in business language, and caveats.
2. Action agent: export_excel(title, tables) -> .xlsx in an outputs folder with a download path in the envelope `files`;
   save_report(title, sections) -> saved report (Markdown + Excel) linked to the conversation. Nothing is emailed or sent.
3. Workflows: when the user pastes multi-step instructions, the supervisor writes a numbered plan (emitted as an event
   and included in the answer), runs each step through the right agent, carries results forward, and reports per step:
   done / done with caveat / not done and why. User instructions change steps, format and tone, never permissions.
4. Idempotent actions: a retried step does not create a second file.

Acceptance
- 10 sample workflows (write them, using ADRA and Fynapse) complete end to end with per-step status; files open.
- Analyst questions from the question bank that need two queries are answered correctly.
