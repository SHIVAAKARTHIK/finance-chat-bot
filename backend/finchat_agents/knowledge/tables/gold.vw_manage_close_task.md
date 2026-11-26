---
name: vw_manage_close_task
schema: gold
layer: gold
domain: recon
type: view
status: active
purpose: Shows close tasks by legal entity; state; status and period.
grain: one row per TASK_KEY (one close task)
primary_key:
- TASK_KEY
entity_column: LEGAL_ENTITY
period_columns:
- PERIOD_NAME
pii_columns: []
synonyms: []
built_from:
- manage_close_task_facts
- manage_close_task_settings
known_issues: []
proposed_fields:
- grain
- primary_key
reviewed:
- superseded_by
superseded_by:
- silver.adra_tasks_task_facts
---

# vw_manage_close_task

> Superseded: this table is a copy of ADRA data. Answers use the source of truth `silver.adra_tasks_task_facts` (decision 21 Nov 2026).

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `TASK_KEY` | string |  |  | `TASK_KEY` |
| `TASK_SETTINGS_KEY` | string |  |  | `TASK_SETTINGS_KEY` |
| `TASK_FOLDER_NAME` | string |  |  | `TASK_FOLDER_NAME` |
| `TASK_STATUS` | string |  |  | `TASK_STATUS` |
| `TASK_IS_FINALIZED` | string |  |  | `TASK_IS_FINALIZED` |
| `TASK_STATE` | string |  |  | `TASK_STATE` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `PERIOD_NAME` | string |  |  | `PERIOD_NAME` |

## Values

**TASK_FOLDER_NAME**
- `Adjustments`
- `Pre-Close`
- `Sign-off`
- `Sub-ledgers`
- `Review`
- `Pre-close`
- `Reconciliation`
- `Management Reporting`
- `Accounts Receivable`
- `Accounts Payable`
- `Revenue`

**TASK_STATUS**
- `Not Started`
- `Approved`
- `Prepared`
- `In Progress`

**TASK_IS_FINALIZED**
- `False`
- `True`

**TASK_STATE**
- `Upcoming`
- `Done`
- `In Progress`

**PERIOD_NAME**
- `None`
