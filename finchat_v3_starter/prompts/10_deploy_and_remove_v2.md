Task 10: deploy v3. Read CLAUDE.md and docs/SPEC.md first.

This branch (finance-agentic, created from development) contains no v2 finance code; v2 stays on feature/finance-kpi
as the fallback. Nothing to delete here.

1. Docker: add finchat_agents requirements to the backend image; warm-up (MCP query + Bedrock ping) on startup;
   health endpoint /v3/health reporting MCP, Bedrock and aiops connectivity (no secrets in output).
2. VM: list the environment variables needed (names only) and the docker compose changes to deploy the
   finance-agentic build instead of the feature/finance-kpi build, plus how to switch back if needed.
3. Point the UI's chat call at /v3/chat (or document the change for the UI owner).
4. If any file on this branch still references v2 finance modules (imports, routes, config), list them for Karthik.

Acceptance: container starts on the VM, /v3/health green, smoke questions answered, rollback steps written.
