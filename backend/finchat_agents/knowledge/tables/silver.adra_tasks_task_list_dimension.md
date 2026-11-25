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
row_count: 5
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
- `Month End Payroll`: 1 rows
- `KF MEC 2026 November`: 1 rows
- `Month End Close`: 1 rows
- `Month End AR`: 1 rows
- `October 2026 MEC Tasks`: 1 rows

**TASK_LIST_ZERO_DAY**
- `2026-10-30 00:00:00.0000000 +00:00`: 3 rows
- `2026-11-30 00:00:00.0000000 +00:00`: 1 rows
- `2026-10-31 00:00:00.0000000 +00:00`: 1 rows

**TASK_LIST_STATUS**
- `2`: 3 rows
- `4`: 2 rows

**TASK_LIST_STATUS_TEXT**
- `Open`: 3 rows
- `Archived`: 2 rows

**TASK_LIST_FINALIZED_PERCENTAGE**
- `100`: 3 rows
- `9.3`: 1 rows
- `46.88`: 1 rows

**TASK_LIST_CREATED_DATE_TIME**
- `2026-10-17 16:00:56.0000000 +00:00`: 1 rows
- `2026-10-26 08:00:41.0000000 +00:00`: 1 rows
- `2026-10-17 15:58:42.0000000 +00:00`: 1 rows
- `2026-10-19 07:52:01.0000000 +00:00`: 1 rows
- `2026-11-13 07:00:41.0000000 +00:00`: 1 rows

**SOURCE_FILE_NAME**
- `tasklistdimension__20261116_174302.csv`: 5 rows

**MDP_CREATED_DATE**
- `2026-11-16 17:52:11.402798+00:00`: 5 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 17:52:11.402798+00:00`: 5 rows

## Profile

Rows in the latest export: 5.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `TASK_LIST_KEY` | STRING | 5 | 0 |  |  |
| `ENGAGEMENT_KEY` | STRING | 1 | 0 |  |  |
| `TASK_LIST_NAME` | STRING | 5 | 0 | KF MEC 2026 November | October 2026 MEC Tasks |
| `TASK_LIST_ZERO_DAY` | STRING | 3 | 0 | 2026-10-30 00:00:00.0000000 +00:00 | 2026-11-30 00:00:00.0000000 +00:00 |
| `TASK_LIST_STATUS` | STRING | 2 | 0 | 2 | 4 |
| `TASK_LIST_STATUS_TEXT` | STRING | 2 | 0 | Archived | Open |
| `TASK_LIST_FINALIZED_PERCENTAGE` | STRING | 3 | 0 | 100 | 9.3 |
| `TASK_LIST_CREATED_DATE_TIME` | STRING | 5 | 0 | 2026-10-17 15:58:42.0000000 +00:00 | 2026-11-13 07:00:41.0000000 +00:00 |
| `TASK_LIST_CREATED_BY_USER_NAME` | STRING | 2 | 0 |  |  |
| `TASK_LIST_CREATED_BY_NAME` | STRING | 2 | 0 |  |  |
| `PERIOD_KEY` | STRING | 1 | 1 |  |  |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | tasklistdimension__20261116_174302.csv | tasklistdimension__20261116_174302.csv |
| `HASH_KEY` | STRING | 5 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 17:52:11.403000 | 2026-11-16 17:52:11.403000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 17:52:11.403000 | 2026-11-16 17:52:11.403000 |

## Sample rows

| TASK_LIST_NAME | TASK_LIST_ZERO_DAY | TASK_LIST_STATUS | TASK_LIST_STATUS_TEXT | TASK_LIST_FINALIZED_PERCENTAGE | TASK_LIST_CREATED_DATE_TIME | TASK_LIST_CREATED_BY_USER_NAME | TASK_LIST_CREATED_BY_NAME | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Month End Payroll | 2026-10-30 00:00:00.0000000 +00:00 | 4 | Archived | 100 | 2026-10-17 15:58:42.0000000 +00:00 | <masked> | <masked> | tasklistdimension__20261116_174302.csv | <masked> | 2026-11-16 17:52:11.403000 | <masked> | 2026-11-16 17:52:11.403000 |
| Month End AR | 2026-10-30 00:00:00.0000000 +00:00 | 4 | Archived | 100 | 2026-10-17 16:00:56.0000000 +00:00 | <masked> | <masked> | tasklistdimension__20261116_174302.csv | <masked> | 2026-11-16 17:52:11.403000 | <masked> | 2026-11-16 17:52:11.403000 |
| Month End Close | 2026-10-30 00:00:00.0000000 +00:00 | 2 | Open | 46.88 | 2026-10-19 07:52:01.0000000 +00:00 | <masked> | <masked> | tasklistdimension__20261116_174302.csv | <masked> | 2026-11-16 17:52:11.403000 | <masked> | 2026-11-16 17:52:11.403000 |
| October 2026 MEC Tasks | 2026-10-31 00:00:00.0000000 +00:00 | 2 | Open | 100 | 2026-10-26 08:00:41.0000000 +00:00 | <masked> | <masked> | tasklistdimension__20261116_174302.csv | <masked> | 2026-11-16 17:52:11.403000 | <masked> | 2026-11-16 17:52:11.403000 |
| KF MEC 2026 November | 2026-11-30 00:00:00.0000000 +00:00 | 2 | Open | 9.3 | 2026-11-13 07:00:41.0000000 +00:00 | <masked> | <masked> | tasklistdimension__20261116_174302.csv | <masked> | 2026-11-16 17:52:11.403000 | <masked> | 2026-11-16 17:52:11.403000 |
