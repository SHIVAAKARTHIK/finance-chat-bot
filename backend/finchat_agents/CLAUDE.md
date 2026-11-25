# Finance Chat v3: rules for Claude Code

Read `docs/SPEC.md` and `docs/MCP_NOTES.md` before any task. SPEC.md is the source of truth.

## Never
- Make git commits, push, or change branches. Karthik commits manually.
- Put secrets in code, prompts, tests, logs, fixtures or docs. Read them from environment variables only.
- Use LangGraph, LangChain or any agent framework. Orchestration is plain Python (our loop, asyncio, pydantic).
- Add KPI search, a KPI registry or KPI routing.
- Call the MCP tool `execute_sql`, or run INSERT / UPDATE / DELETE / MERGE / ALTER / DROP / CREATE against
  `silver` or `gold`. App writes go only to `lakehouse_mvpai.aiops.finance_chat_*` through the SQL connector.
- Add row-level entity filters (engagement, legal entity, parent entity, data area) or KPI code.
- Hardcode table names, entity values or question-specific logic in runtime code. Table knowledge lives in
  `knowledge/` Markdown and YAML.
- Read, copy or use any hold-out question set.
- Import from the v2 code. Copy what you need into `finchat_agents/` and adapt it.

## Always
- Work inside `backend/finchat_agents/` unless the task says otherwise.
- Keep guardrails in code inside tools (see SPEC section 4), with tests.
- Every number in an answer must come from a tool result.
- Write unit tests with fake providers and a fake MCP server; live tests run only when `RUN_LIVE=1`.
- Fix wrong answers generically (table pages, glossary, examples, prompts), never per question.
- End each task with a short report: files changed, tests run and results, open questions.
- If a decision is not in SPEC.md, choose the simplest safe option, write it under "Assumptions" in the report.
