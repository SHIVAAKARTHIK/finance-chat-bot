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
row_count: 9
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
- `10`: 3 rows
- `3`: 3 rows
- `6`: 1 rows
- `4`: 1 rows
- `116`: 1 rows

**FINALIZED_TASKS**
- `2`: 4 rows
- `0`: 4 rows
- `21`: 1 rows

**COMPLETION_PERCENTAGE**
- `0`: 4 rows
- `20`: 2 rows
- `67`: 2 rows
- `18`: 1 rows

## Profile

Rows in the latest export: 9.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `TOTAL_OPEN_TASKS` | LONG | 5 | 0 | 3 | 116 |
| `FINALIZED_TASKS` | LONG | 3 | 0 | 0 | 21 |
| `COMPLETION_PERCENTAGE` | INT | 3 | 0 | 0 | 67 |
| `LEGAL_ENTITY` | STRING | 8 | 0 |  |  |

## Sample rows

| TOTAL_OPEN_TASKS | FINALIZED_TASKS | COMPLETION_PERCENTAGE |
|---|---|---|
| 3 | 0 | 0 |
| 10 | 0 | 0 |
| 10 | 2 | 20 |
| 116 | 21 | 18 |
| 6 | 0 | 0 |
