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
row_count: 165
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
- `Adjustments`: 74 rows
- `Pre-Close`: 35 rows
- `Sign-off`: 15 rows
- `Sub-ledgers`: 13 rows
- `Review`: 10 rows
- `Pre-close`: 9 rows
- `Reconciliation`: 3 rows
- `Management Reporting`: 3 rows
- `Accounts Receivable`: 1 rows
- `Accounts Payable`: 1 rows
- `Revenue`: 1 rows

**TASK_STATUS**
- `Not Started`: 128 rows
- `Approved`: 15 rows
- `Prepared`: 15 rows
- `In Progress`: 7 rows

**TASK_IS_FINALIZED**
- `False`: 136 rows
- `True`: 29 rows

**TASK_STATE**
- `Upcoming`: 128 rows
- `Done`: 29 rows
- `In Progress`: 8 rows

**PERIOD_NAME**
- `None`: 90 rows

## Profile

Rows in the latest export: 165.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `TASK_KEY` | STRING | 168 | 0 |  |  |
| `TASK_SETTINGS_KEY` | STRING | 168 | 0 |  |  |
| `TASK_FOLDER_NAME` | STRING | 11 | 0 | Accounts Payable | Sub-ledgers |
| `TASK_STATUS` | STRING | 4 | 0 | Approved | Prepared |
| `TASK_IS_FINALIZED` | STRING | 2 | 0 | False | True |
| `TASK_STATE` | STRING | 3 | 0 | Done | Upcoming |
| `LEGAL_ENTITY` | STRING | 8 | 0 |  |  |
| `PERIOD_NAME` | STRING | 2 | 90 |  |  |

## Sample rows

| TASK_FOLDER_NAME | TASK_STATUS | TASK_IS_FINALIZED | TASK_STATE | PERIOD_NAME |
|---|---|---|---|---|
| Accounts Payable | Prepared | True | Done | (altered in export) |
| Accounts Receivable | Prepared | True | Done | (altered in export) |
| Pre-Close | Prepared | True | Done | (altered in export) |
| Sub-ledgers | Prepared | True | Done | (altered in export) |
| Adjustments | Not Started | False | Upcoming | (altered in export) |
