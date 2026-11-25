Task 01: setup and agent runtime. Read CLAUDE.md, docs/SPEC.md and docs/MCP_NOTES.md first.

Scope: only the package skeleton and the agent loop. No data tools, agents or API yet.

1. Create backend/finchat_agents/ with: config.py, llm/, runtime/, tools/, agents/, knowledge/, storage/,
   tracing/, api/, tests/. Copy CLAUDE.md and docs/ from the starter pack into it.
2. config.py (pydantic-settings) reads the variables in config/.env.example. Copy .env.example in (names only).
3. Check latest versions (`pip index versions anthropic openai boto3 sqlglot databricks-sql-connector pydantic httpx`)
   and add a requirements file for this package.
4. llm/: one interface `complete(system, messages, tools, model, max_tokens, temperature) -> LLMResult(text, tool_calls, usage, stop_reason)`.
   - ClaudeBedrockProvider: anthropic SDK, AnthropicBedrock, tool use, prompt caching on system + tool definitions.
   - GptOssBedrockProvider: test whether gpt-oss-120b supports tool calling via the openai SDK on Bedrock's
     OpenAI-compatible endpoint in AWS_REGION. If yes use it; if not use boto3 Converse. Report the choice.
   - Tools defined once as JSON Schema; providers convert.
5. runtime/loop.py: ReAct loop. Model call -> tool calls (parallel when independent, asyncio) -> append results ->
   repeat until final or a budget is hit (AGENT_MAX_STEPS, AGENT_MAX_SECONDS, AGENT_MAX_SQL_CALLS).
   On a budget stop return a partial answer stating what is missing; never empty. Retry with backoff on throttling / 5xx.
6. runtime/agent.py: Agent(name, system_prompt, model, tools). `as_tool()` exposes an agent to another agent
   (ask_<name>(task) -> structured result). Fresh context per call.
7. tracing/: event model (run_id, message_id, agent, step, type, started/ended, tokens, payload) and a sink
   interface with a JSON-lines file sink now. The aiops table sink comes in task 05.

Acceptance
- Unit tests with a fake provider: tool loop, parallel tools, budget stop returns a partial answer, agent-as-tool, event order.
- Live smoke test (only when RUN_LIVE=1): each Bedrock model answers "2+2" and calls a toy add(a, b) tool once.
- Report: files, provider choice for gpt-oss and why, how to run tests, assumptions.
