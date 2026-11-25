# Task 01 report: setup and agent runtime (21 Nov 2026)

## Files
- `config.py`: pydantic-settings, all names from `.env.example` (+ `GPT_OSS_TRANSPORT`, `LLM_TIMEOUT_SECONDS`, `TRACE_DIR`). Reads `backend/.env`; empty values count as unset; secret is `SecretStr`.
- `requirements.txt`: latest versions on 21 Nov 2026 (later merged into the single `requirements.txt`, now ranges).
- `llm/types.py`: `ToolSpec` (JSON Schema, defined once), neutral `Message` blocks, `LLMResult(text, tool_calls, usage, stop_reason)`, `LLMError(retryable)`, `LLMProvider.complete(system, messages, tools, model, max_tokens, temperature)`, `ModelHandle`.
- `llm/claude_bedrock.py`: `AsyncAnthropicBedrock`, tool use, `cache_control` on system + last tool definition.
- `llm/gpt_oss_bedrock.py`: two transports, `converse` (boto3) and `openai` (openai SDK `providers.bedrock(endpoint="runtime")`, SigV4). Strips `<reasoning>` / reasoning blocks.
- `llm/factory.py`, `llm/fake.py` (scripted fake provider for tests).
- `runtime/loop.py`: ReAct loop, parallel tools (`asyncio.gather`; `parallel_safe=False` runs serially), budgets (steps, seconds, SQL calls shared across nested agents), partial answer on any stop (model-written after a step stop, deterministic otherwise), optional finish tool for structured output.
- `runtime/retry.py`: exponential backoff + jitter on throttling / timeouts / 5xx, deadline-aware.
- `runtime/agent.py`: `Agent`, `AgentResult`, `as_tool()` -> `ask_<name>(task, context?)`, fresh context per call.
- `runtime/tools.py`: `Tool`, `@tool`, `ToolError`, `Budget`, `RunContext`, `Counters`.
- `tracing/`: `TraceEvent` (run_id, message_id, agent, step, type, started/ended, duration, tokens, payload), `Tracer`, `JsonlFileSink`, `MemorySink`.
- Empty packages: `tools/`, `agents/`, `knowledge/`, `storage/`, `api/`. Copied `CLAUDE.md`, `docs/`, `.env.example`.

## gpt-oss provider choice
Default is **`converse` (boto3)**. The openai SDK has a Bedrock provider that signs requests with the normal AWS chain,
so both are implemented and switchable with `GPT_OSS_TRANSPORT`. Tool calling on the OpenAI-compatible endpoint could
not be tested here: this machine has no AWS credentials or `backend/.env`. Converse supports tool use for gpt-oss and
uses the same credentials as Claude, so it is the safe default. The live test runs both transports; switch to `openai`
if both pass and you prefer it.

## Tests
From `backend/finchat_agents`: `..\.venv\Scripts\python -m pytest -q` -> 40 passed, 2 skipped (live).
Live: `$env:RUN_LIVE="1"; ..\.venv\Scripts\python -m pytest tests/live -v` (not run: no credentials here).

## Assumptions
- The package lives at `D:\Finance chat bot\backend\finchat_agents\`; venv at `backend\.venv`.
- `max_steps` counts model calls per agent; the time deadline and SQL count are per question, shared by nested agents.
- A sub-agent sees only its task + optional context; the caller sees `{agent, status, answer, data?, stop_reason?, tool_errors?}`.
- Tool output to the model is capped at 20,000 characters.

## Open questions
- Which AWS region? Claude uses the `us.` cross-region profile; gpt-oss availability depends on the region.
- Should the default switch to the `openai` transport if the live test shows it works?
