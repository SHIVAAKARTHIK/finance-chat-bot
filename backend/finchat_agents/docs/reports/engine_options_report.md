# Options report: SQL connector, Anthropic API key, Anthropic SDK ReAct engine (24 Nov 2026)

Three switches, all off by default. With none set, behaviour is exactly as before. Tests: 361 passed, 30 skipped (real SDK
runner and real SDK clients against an in-process fake network). Not run live (needs your laptop).

| Setting (env var) | Values | Default | What it changes |
|---|---|---|---|
| `DATA_ACCESS` | `mcp`, `sql_connector` | `mcp` | How data is read: Databricks MCP bridge, or databricks-sql-connector with the same service principal |
| `CLAUDE_PROVIDER` | `bedrock`, `anthropic_api` | `bedrock` | Where Claude runs. `anthropic_api` reads `ANTHROPIC_API_KEY` from the environment; model id from `ANTHROPIC_MODEL_SQL` (default `claude-sonnet-4-5`). gpt-oss stays on Bedrock |
| `REACT_ENGINE` | `own`, `anthropic_sdk` | `own` | Who runs the ReAct loop of the Claude agents: our loop, or the Anthropic SDK tool runner (works on Bedrock and on the API key) |

## SQL connector (`DATA_ACCESS=sql_connector`)
- Needs `DATABRICKS_SERVER_HOSTNAME`, `DATABRICKS_HTTP_PATH` and the existing `AZURE_*` values. Clear error if one is missing.
- Same `query()` interface, so `run_sql`, the guardrails, retries in the agents and the number check are unchanged.
- Connections are pooled (a new one costs seconds). Typed values come from the driver (decimals stay decimals).
- Read-only: the client accepts only SELECT / WITH. The MCP server's own read-only layer is gone, so give the service principal SELECT-only on silver and gold.

## Anthropic API key (`CLAUDE_PROVIDER=anthropic_api`)
- Same request and response handling and prompt caching as Bedrock. The key is read only from the environment.
- Trace and message records show `anthropic-api` as the provider for `claude-*` models.

## Anthropic SDK ReAct engine (`REACT_ENGINE=anthropic_sdk`)
- Uses `client.beta.messages.tool_runner` with our tools wrapped, so every guardrail inside the tools, the SQL-call budget,
  the step limit (max iterations), the run deadline, the finish tool and tracing still apply. The trace event `agent_start`
  and each `llm_call` carry `engine`.
- Differences to know: the SDK runs one reply's tool calls one after another (our loop runs safe ones in parallel); our
  conversation cache point is not set (system prompt and tools are still cached); retries are the SDK's (2); a budget stop
  returns the deterministic partial answer. Models without an SDK client (gpt-oss) always use our loop.
- The SDK tool runner is a beta feature of the SDK. Note: CLAUDE.md says orchestration is plain Python and no agent
  framework. This is an optional engine you asked for, our loop stays the default, and the routing, guardrails and checks are
  still ours. Remove the option if you want the rule to hold strictly.

## How to compare (on your laptop)
Set one switch at a time, ask the same 10 questions, and compare time and answers: look at `engine` in `agent_start`, the
`llm_call` durations and `cache_read_tokens`, and the `run_sql` step durations.

## Assumptions
- `ANTHROPIC_MODEL_SQL` default `claude-sonnet-4-5` is the API id of the same model family; change it if your key uses another.
- The SQL connector has no server-side timeout; the client stops waiting after `SQL_TIMEOUT_SECONDS`.
