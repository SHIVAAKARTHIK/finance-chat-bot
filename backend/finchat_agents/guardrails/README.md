# Guardrails folder

By default the app reads its guardrail content from this folder (`GUARDRAILS_DIR=guardrails`).

| Item | Comes from |
|---|---|
| `packs/` | **You add it:** the company guardrails repository's `packs/` folder, unchanged |
| `guardrail.yaml` | **You add it:** your project's values file from that repository, renamed |
| `overrides/` | In the code: finance versions that replace the company packs with the same `id` |
| `application_notes.md` | In the code: notes about this application, added after the packs |

Do not edit or copy files over the company packs: `overrides/` replaces them while loading. Delete a file in
`overrides/` to apply the company pack as written. The overrides and notes need the guardrail owner's approval before
production.

The app does not start until `packs/` and `guardrail.yaml` are there. Check from the `backend` folder:

```
python -m finchat_agents.guardrails.check
```

`packs/` and `guardrail.yaml` are excluded from the public repository (`.gitignore`). Code folders here
(`input_checks/`, `output_checks/`, `evals/`) are not read as packs. When updating the code, copy over this folder; do
not delete it.
