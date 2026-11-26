---
name: adra_tasks_task_list_dimension
schema: silver
layer: silver
domain: recon
type: table
status: active
purpose: Named task lists (e.g. Month End Close) that group close tasks.
grain: one row per TASK_LIST_KEY (one task list)
primary_key:
- TASK_LIST_KEY
entity_column: null
period_columns:
- TASK_LIST_ZERO_DAY
pii_columns:
- TASK_LIST_CREATED_BY_USER_NAME
- TASK_LIST_CREATED_BY_NAME
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues: []
proposed_fields:
- grain
- primary_key
reviewed: false
---

# adra_tasks_task_list_dimension

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `TASK_LIST_KEY` | string |  |  | `TASK_LIST_KEY` |
| `ENGAGEMENT_KEY` | string |  |  | `ENGAGEMENT_KEY` |
| `TASK_LIST_NAME` | string |  |  | `TASK_LIST_NAME` |
| `TASK_LIST_ZERO_DAY` | string |  |  | `TASK_LIST_ZERO_DAY` |
| `TASK_LIST_STATUS` | string |  |  | `TASK_LIST_STATUS` |
| `TASK_LIST_STATUS_TEXT` | string |  |  | `TASK_LIST_STATUS_TEXT` |
| `TASK_LIST_FINALIZED_PERCENTAGE` | string |  |  | `TASK_LIST_FINALIZED_PERCENTAGE` |
| `TASK_LIST_CREATED_DATE_TIME` | string |  |  | `TASK_LIST_CREATED_DATE_TIME` |
| `TASK_LIST_CREATED_BY_USER_NAME` | string |  |  | `TASK_LIST_CREATED_BY_USER_NAME` |
| `TASK_LIST_CREATED_BY_NAME` | string |  |  | `TASK_LIST_CREATED_BY_NAME` |
| `PERIOD_KEY` | string |  |  | `PERIOD_KEY` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**TASK_LIST_NAME**
- `Month End Payroll`
- `KF MEC 2026 November`
- `Month End Close`
- `Month End AR`
- `October 2026 MEC Tasks`

**TASK_LIST_ZERO_DAY**
- `2026-10-30 00:00:00.0000000 +00:00`
- `2026-11-30 00:00:00.0000000 +00:00`
- `2026-10-31 00:00:00.0000000 +00:00`

**TASK_LIST_STATUS**
- `2`
- `4`

**TASK_LIST_STATUS_TEXT**
- `Open`
- `Archived`

**TASK_LIST_FINALIZED_PERCENTAGE**
- `100`
- `9.3`
- `46.88`

**TASK_LIST_CREATED_DATE_TIME**
- `2026-10-17 16:00:56.0000000 +00:00`
- `2026-10-26 08:00:41.0000000 +00:00`
- `2026-10-17 15:58:42.0000000 +00:00`
- `2026-10-19 07:52:01.0000000 +00:00`
- `2026-11-13 07:00:41.0000000 +00:00`

**SOURCE_FILE_NAME**
- `tasklistdimension__20261116_174302.csv`

**MDP_CREATED_DATE**
- `2026-11-16 17:52:11.402798+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 17:52:11.402798+00:00`
