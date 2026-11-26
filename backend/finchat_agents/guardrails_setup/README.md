# Setting up `guardrails_local/`

The company packs and values are not in this repository. Build `finchat_agents/guardrails_local/` on your machine:

| Put there | Take it from |
|---|---|
| `packs/` | The company guardrails repository, unchanged |
| `guardrail.yaml` | Your project's values file from that repository, renamed |
| `overrides/` | `guardrails_setup/overrides/` (this folder) |
| `application_notes.md` | `guardrails_setup/application_notes.md` |

The two overrides replace the company packs with the same id, so general finance knowledge, calculations and Excel or
report files keep working. They need the guardrail owner's approval; without them the company packs apply as written.

Check the result from the `backend` folder: `python -m finchat_agents.guardrails.check`
