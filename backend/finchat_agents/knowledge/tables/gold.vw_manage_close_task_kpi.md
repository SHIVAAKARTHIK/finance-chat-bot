---
name: vw_manage_close_task_kpi
schema: gold
layer: gold
domain: recon
type: view
status: active
purpose: Summarizes open and finalized close tasks and completion percentage by legal entity.
grain: one row per legal entity task KPI
primary_key:
- LEGAL_ENTITY
entity_column: LEGAL_ENTITY
period_columns: []
pii_columns: []
synonyms: []
built_from:
- manage_close_task_facts
- manage_close_task_settings
known_issues: []
proposed_fields: []
reviewed:
- superseded_by
superseded_by:
- silver.adra_tasks_task_facts
---

# vw_manage_close_task_kpi

> Superseded: this table is a copy of ADRA data. Answers use the source of truth `silver.adra_tasks_task_facts` (decision 21 Nov 2026).

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `TOTAL_OPEN_TASKS` | long |  |  | `TOTAL_OPEN_TASKS` |
| `FINALIZED_TASKS` | long |  |  | `FINALIZED_TASKS` |
| `COMPLETION_PERCENTAGE` | int |  |  | `COMPLETION_PERCENTAGE` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |

## Values

**TOTAL_OPEN_TASKS**
- `10`
- `3`
- `6`
- `4`
- `116`

**FINALIZED_TASKS**
- `2`
- `0`
- `21`

**COMPLETION_PERCENTAGE**
- `0`
- `20`
- `67`
- `18`
