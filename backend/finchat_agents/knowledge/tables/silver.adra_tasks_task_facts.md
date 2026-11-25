---
name: adra_tasks_task_facts
schema: silver
layer: silver
domain: recon
type: table
status: active
purpose: Month-end close tasks with status; preparer; approver and due dates.
grain: one row per TASK_KEY (one close task)
primary_key:
- TASK_KEY
entity_column: COMPANY_KEY
period_columns:
- TASK_DUE_DATE_TIME
- TASK_REMINDER_DATE_TIME
- TASK_PREPARED_DATE_TIME
- TASK_FINALIZED
pii_columns:
- TASK_PREPARER
- TASK_PREPARER_NAME
- TASK_APPROVER
- TASK_APPROVER_NAME
- TASK_PREPARED_BY_NAME
- TASK_PREPARED_BY_USERNAME
- TASK_LAST_APPROVED_BY_NAME
- TASK_LAST_APPROVED_BY_USERNAME
- TASK_ADDED_BY_NAME
- TASK_ADDED_BY_USERNAME
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues: []
row_count: 219
proposed_fields:
- grain
- primary_key
reviewed: false
---

# adra_tasks_task_facts

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `TASK_KEY` | string |  |  | `TASK_KEY` |
| `ENGAGEMENT_KEY` | string |  |  | `ENGAGEMENT_KEY` |
| `COMPANY_KEY` | string |  |  | `COMPANY_KEY` |
| `DEPARTMENT_KEY` | string |  |  | `DEPARTMENT_KEY` |
| `FREQUENCY_KEY` | string |  |  | `FREQUENCY_KEY` |
| `EXTRA_FIELDS_KEY` | string |  |  | `EXTRA_FIELDS_KEY` |
| `TASK_LIST_KEY` | string |  |  | `TASK_LIST_KEY` |
| `TASK_SETTINGS_KEY` | string |  |  | `TASK_SETTINGS_KEY` |
| `TEAM_KEY` | string |  |  | `TEAM_KEY` |
| `TASK_ID` | string |  |  | `TASK_ID` |
| `TASK_CHECKLIST_ITEM_FACT_KEY` | string |  |  | `TASK_CHECKLIST_ITEM_FACT_KEY` |
| `TASK_PREPARER` | string |  |  | `TASK_PREPARER` |
| `TASK_PREPARER_NAME` | string |  |  | `TASK_PREPARER_NAME` |
| `TASK_APPROVER` | string |  |  | `TASK_APPROVER` |
| `TASK_APPROVER_NAME` | string |  |  | `TASK_APPROVER_NAME` |
| `TASK_STATUS` | string |  |  | `TASK_STATUS` |
| `TASK_APPROVAL_STATUS` | string |  |  | `TASK_APPROVAL_STATUS` |
| `TASK_IS_FINALIZED` | string |  |  | `TASK_IS_FINALIZED` |
| `TASK_FINALIZED` | string |  |  | `TASK_FINALIZED` |
| `TASK_DUE_DATE_TIME` | string |  |  | `TASK_DUE_DATE_TIME` |
| `TASK_REMINDER_DATE_TIME` | string |  |  | `TASK_REMINDER_DATE_TIME` |
| `TASK_PREPARED_BY_NAME` | string |  |  | `TASK_PREPARED_BY_NAME` |
| `TASK_PREPARED_BY_USERNAME` | string |  |  | `TASK_PREPARED_BY_USERNAME` |
| `TASK_PREPARED_DATE_TIME` | string |  |  | `TASK_PREPARED_DATE_TIME` |
| `TASK_LAST_APPROVED_BY_NAME` | string |  |  | `TASK_LAST_APPROVED_BY_NAME` |
| `TASK_LAST_APPROVED_BY_USERNAME` | string |  |  | `TASK_LAST_APPROVED_BY_USERNAME` |
| `TASK_APPROVED_DATE_TIME` | string |  |  | `TASK_APPROVED_DATE_TIME` |
| `TASK_NUMBER_OF_REJECTS` | string |  |  | `TASK_NUMBER_OF_REJECTS` |
| `TASK_ADDED_BY_NAME` | string |  |  | `TASK_ADDED_BY_NAME` |
| `TASK_ADDED_BY_USERNAME` | string |  |  | `TASK_ADDED_BY_USERNAME` |
| `TASK_ADDED_DATE_TIME` | string |  |  | `TASK_ADDED_DATE_TIME` |
| `PRECEDING_TASKS` | string |  |  | `PRECEDING_TASKS` |
| `SUCCEEDING_TASKS` | string |  |  | `SUCCEEDING_TASKS` |
| `NOT_FINALIZED_PRECEDING_TASKS` | string |  |  | `NOT_FINALIZED_PRECEDING_TASKS` |
| `NOT_FINALIZED_SUCCEEDING_TASKS` | string |  |  | `NOT_FINALIZED_SUCCEEDING_TASKS` |
| `TASK_ACTUAL_COMPLETION_TIME` | string |  |  | `TASK_ACTUAL_COMPLETION_TIME` |
| `TASK_NUMBER_OF_ATTACHMENTS` | string |  |  | `TASK_NUMBER_OF_ATTACHMENTS` |
| `TASK_IS_CHECKLIST` | string |  |  | `TASK_IS_CHECKLIST` |
| `TASK_CHECKLIST_COMPLETENESS` | string |  |  | `TASK_CHECKLIST_COMPLETENESS` |
| `OFFSET_ZERO_DAYS` | string |  |  | `OFFSET_ZERO_DAYS` |
| `TASK_LINK` | string |  |  | `TASK_LINK` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**TASK_STATUS**
- `Not Started`: 128 rows
- `Closed`: 54 rows
- `Prepared`: 15 rows
- `Approved`: 15 rows
- `In Progress`: 7 rows

**TASK_APPROVAL_STATUS**
- `Approval not needed`: 110 rows
- `Not approved`: 94 rows
- `Approved`: 15 rows

**TASK_IS_FINALIZED**
- `False`: 136 rows
- `True`: 83 rows

**TASK_PREPARED_DATE_TIME**
- `None`: 177 rows
- `2026-10-26 10:16:37.0000000 +00:00`: 1 rows
- `2026-10-26 10:21:18.0000000 +00:00`: 1 rows
- `2026-10-23 06:08:32.0000000 +00:00`: 1 rows
- `2026-10-23 06:06:01.0000000 +00:00`: 1 rows
- `2026-10-29 10:27:33.0000000 +00:00`: 1 rows
- `2026-10-19 09:45:56.0000000 +00:00`: 1 rows
- `2026-10-23 06:10:02.0000000 +00:00`: 1 rows
- `2026-10-23 06:04:35.0000000 +00:00`: 1 rows
- `2026-10-23 06:15:00.0000000 +00:00`: 1 rows
- `2026-10-29 08:52:19.0000000 +00:00`: 1 rows
- `2026-10-23 06:10:56.0000000 +00:00`: 1 rows
- `2026-10-23 06:17:36.0000000 +00:00`: 1 rows
- `2026-10-29 10:30:42.0000000 +00:00`: 1 rows
- `2026-10-29 08:56:31.0000000 +00:00`: 1 rows
- `2026-10-29 10:32:49.0000000 +00:00`: 1 rows
- `2026-10-23 06:12:25.0000000 +00:00`: 1 rows
- `2026-10-29 10:29:52.0000000 +00:00`: 1 rows
- `2026-10-19 08:59:13.0000000 +00:00`: 1 rows
- `2026-10-23 06:09:39.0000000 +00:00`: 1 rows
- `2026-10-23 06:13:28.0000000 +00:00`: 1 rows
- `2026-10-23 06:19:09.0000000 +00:00`: 1 rows
- `2026-10-23 06:10:28.0000000 +00:00`: 1 rows
- `2026-10-23 06:16:33.0000000 +00:00`: 1 rows
- `2026-10-23 06:08:17.0000000 +00:00`: 1 rows
- `2026-10-29 10:31:51.0000000 +00:00`: 1 rows
- `2026-11-13 07:34:55.0000000 +00:00`: 1 rows
- `2026-10-29 08:54:10.0000000 +00:00`: 1 rows
- `2026-10-19 08:58:30.0000000 +00:00`: 1 rows
- `2026-11-13 07:40:10.0000000 +00:00`: 1 rows
- `2026-10-23 06:11:21.0000000 +00:00`: 1 rows
- `2026-10-23 06:08:04.0000000 +00:00`: 1 rows
- `2026-10-23 06:05:21.0000000 +00:00`: 1 rows
- `2026-10-23 06:05:07.0000000 +00:00`: 1 rows
- `2026-10-23 06:17:11.0000000 +00:00`: 1 rows
- `2026-10-19 09:45:07.0000000 +00:00`: 1 rows
- `2026-10-29 10:28:28.0000000 +00:00`: 1 rows
- `2026-11-13 07:39:31.0000000 +00:00`: 1 rows
- `2026-11-13 07:35:30.0000000 +00:00`: 1 rows
- `2026-10-29 00:48:36.0000000 +00:00`: 1 rows
- `2026-10-23 06:05:47.0000000 +00:00`: 1 rows
- `2026-10-23 06:18:25.0000000 +00:00`: 1 rows
- `2026-10-29 00:49:23.0000000 +00:00`: 1 rows

**TASK_APPROVED_DATE_TIME**
- `None`: 204 rows
- `2026-10-23 06:31:46.0000000 +00:00`: 1 rows
- `2026-10-23 06:31:53.0000000 +00:00`: 1 rows
- `2026-10-23 06:31:23.0000000 +00:00`: 1 rows
- `2026-10-23 06:31:42.0000000 +00:00`: 1 rows
- `2026-10-23 06:31:49.0000000 +00:00`: 1 rows
- `2026-10-23 06:31:19.0000000 +00:00`: 1 rows
- `2026-10-22 09:03:18.0000000 +00:00`: 1 rows
- `2026-10-23 06:31:57.0000000 +00:00`: 1 rows
- `2026-10-23 06:31:35.0000000 +00:00`: 1 rows
- `2026-10-22 09:03:13.0000000 +00:00`: 1 rows
- `2026-10-23 06:31:28.0000000 +00:00`: 1 rows
- `2026-10-23 06:31:31.0000000 +00:00`: 1 rows
- `2026-10-23 06:31:10.0000000 +00:00`: 1 rows
- `2026-10-23 06:31:15.0000000 +00:00`: 1 rows
- `2026-10-23 06:31:39.0000000 +00:00`: 1 rows

**TASK_NUMBER_OF_REJECTS**
- `0`: 219 rows

**TASK_ADDED_DATE_TIME**
- `2026-11-13 07:00:42.0000000 +00:00`: 43 rows
- `2026-10-26 08:00:42.0000000 +00:00`: 41 rows
- `2026-10-19 07:59:31.0000000 +00:00`: 30 rows
- `2026-10-22 10:42:52.0000000 +00:00`: 5 rows
- `2026-10-22 10:37:00.0000000 +00:00`: 5 rows
- `2026-10-22 10:40:27.0000000 +00:00`: 5 rows
- `2026-10-17 16:01:20.0000000 +00:00`: 5 rows
- `2026-11-07 06:30:08.0000000 +00:00`: 3 rows
- `2026-10-23 06:30:08.0000000 +00:00`: 3 rows
- `2026-11-11 06:30:06.0000000 +00:00`: 3 rows
- `2026-11-12 06:30:00.0000000 +00:00`: 3 rows
- `2026-11-04 06:30:06.0000000 +00:00`: 3 rows
- `2026-11-10 06:30:08.0000000 +00:00`: 3 rows
- `2026-11-15 06:30:09.0000000 +00:00`: 3 rows
- `2026-11-03 06:30:04.0000000 +00:00`: 3 rows
- `2026-10-26 06:30:02.0000000 +00:00`: 3 rows
- `2026-10-25 06:30:06.0000000 +00:00`: 3 rows
- `2026-10-29 06:30:02.0000000 +00:00`: 3 rows
- `2026-11-16 06:30:01.0000000 +00:00`: 3 rows
- `2026-10-30 06:30:09.0000000 +00:00`: 3 rows
- `2026-10-24 06:30:04.0000000 +00:00`: 3 rows
- `2026-11-02 06:30:01.0000000 +00:00`: 3 rows
- `2026-11-01 06:30:02.0000000 +00:00`: 3 rows
- `2026-11-08 06:30:03.0000000 +00:00`: 3 rows
- `2026-10-31 06:30:07.0000000 +00:00`: 3 rows
- `2026-10-17 15:59:24.0000000 +00:00`: 3 rows
- `2026-11-13 06:30:01.0000000 +00:00`: 3 rows
- `2026-11-05 06:30:03.0000000 +00:00`: 3 rows
- `2026-11-14 06:30:02.0000000 +00:00`: 3 rows
- `2026-11-06 06:30:02.0000000 +00:00`: 3 rows
- `2026-10-27 06:30:05.0000000 +00:00`: 3 rows
- `2026-11-09 06:30:00.0000000 +00:00`: 3 rows
- `2026-10-28 06:30:08.0000000 +00:00`: 3 rows
- `2026-10-27 07:38:28.0000000 +00:00`: 1 rows
- `2026-10-27 07:32:33.0000000 +00:00`: 1 rows
- `2026-10-27 07:36:43.0000000 +00:00`: 1 rows
- `2026-10-19 08:52:49.0000000 +00:00`: 1 rows
- `2026-10-27 07:34:26.0000000 +00:00`: 1 rows
- `2026-10-22 09:15:10.0000000 +00:00`: 1 rows
- `2026-10-19 07:02:28.0000000 +00:00`: 1 rows

**PRECEDING_TASKS**
- `0`: 215 rows
- `1`: 3 rows
- `2`: 1 rows

**SUCCEEDING_TASKS**
- `0`: 215 rows
- `1`: 3 rows
- `2`: 1 rows

**NOT_FINALIZED_PRECEDING_TASKS**
- `0`: 218 rows
- `1`: 1 rows

**NOT_FINALIZED_SUCCEEDING_TASKS**
- `0`: 218 rows
- `1`: 1 rows

**TASK_ACTUAL_COMPLETION_TIME**
- `0`: 219 rows

**TASK_NUMBER_OF_ATTACHMENTS**
- `0`: 219 rows

**TASK_IS_CHECKLIST**
- `False`: 219 rows

**TASK_CHECKLIST_COMPLETENESS**
- `0`: 219 rows

**OFFSET_ZERO_DAYS**
- `0`: 95 rows
- `1`: 24 rows
- `5`: 20 rows
- `7`: 16 rows
- `2`: 14 rows
- `4`: 11 rows
- `3`: 8 rows
- `12`: 6 rows
- `6`: 5 rows
- `-2`: 4 rows
- `9`: 4 rows
- `8`: 4 rows
- `-1`: 3 rows
- `10`: 2 rows
- `13`: 1 rows
- `-5`: 1 rows
- `11`: 1 rows

**SOURCE_FILE_NAME**
- `taskfacts__20261116_174302.csv`: 219 rows

**MDP_CREATED_DATE**
- `2026-11-16 17:52:11.406889+00:00`: 219 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 17:52:11.406889+00:00`: 219 rows

## Profile

Rows in the latest export: 219.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `TASK_KEY` | STRING | 223 | 0 |  |  |
| `ENGAGEMENT_KEY` | STRING | 1 | 0 |  |  |
| `COMPANY_KEY` | STRING | 10 | 0 |  |  |
| `DEPARTMENT_KEY` | STRING | 7 | 88 |  |  |
| `FREQUENCY_KEY` | STRING | 2 | 0 |  |  |
| `EXTRA_FIELDS_KEY` | STRING | 223 | 0 |  |  |
| `TASK_LIST_KEY` | STRING | 5 | 90 |  |  |
| `TASK_SETTINGS_KEY` | STRING | 223 | 0 |  |  |
| `TEAM_KEY` | STRING | 5 | 0 |  |  |
| `TASK_ID` | STRING | 223 | 0 | 2676905 | 2740946 |
| `TASK_CHECKLIST_ITEM_FACT_KEY` | STRING | 223 | 0 |  |  |
| `TASK_PREPARER` | STRING | 4 | 0 |  |  |
| `TASK_PREPARER_NAME` | STRING | 4 | 0 |  |  |
| `TASK_APPROVER` | STRING | 2 | 110 |  |  |
| `TASK_APPROVER_NAME` | STRING | 2 | 110 |  |  |
| `TASK_STATUS` | STRING | 5 | 0 | Approved | Prepared |
| `TASK_APPROVAL_STATUS` | STRING | 3 | 0 | Approval not needed | Not approved |
| `TASK_IS_FINALIZED` | STRING | 2 | 0 | False | True |
| `TASK_FINALIZED` | STRING | 52 | 95 | 2026-10-19 07:38:10.0000000 +00:00 | 2026-11-13 07:40:10.0000000 +00:00 |
| `TASK_DUE_DATE_TIME` | STRING | 79 | 0 | 2026-10-23 06:30:00.0000000 +00:00 | 2026-12-08 18:00:00.0000000 +00:00 |
| `TASK_REMINDER_DATE_TIME` | STRING | 74 | 5 | 2026-10-23 06:30:00.0000000 +00:00 | 2026-12-08 18:00:00.0000000 +00:00 |
| `TASK_PREPARED_BY_NAME` | STRING | 2 | 177 |  |  |
| `TASK_PREPARED_BY_USERNAME` | STRING | 2 | 177 |  |  |
| `TASK_PREPARED_DATE_TIME` | STRING | 42 | 177 | 2026-10-19 08:58:30.0000000 +00:00 | 2026-11-13 07:40:10.0000000 +00:00 |
| `TASK_LAST_APPROVED_BY_NAME` | STRING | 1 | 204 |  |  |
| `TASK_LAST_APPROVED_BY_USERNAME` | STRING | 1 | 204 |  |  |
| `TASK_APPROVED_DATE_TIME` | STRING | 15 | 204 | 2026-10-22 09:03:13.0000000 +00:00 | 2026-10-23 06:31:57.0000000 +00:00 |
| `TASK_NUMBER_OF_REJECTS` | STRING | 1 | 0 | 0 | 0 |
| `TASK_ADDED_BY_NAME` | STRING | 2 | 90 |  |  |
| `TASK_ADDED_BY_USERNAME` | STRING | 2 | 90 |  |  |
| `TASK_ADDED_DATE_TIME` | STRING | 39 | 0 | 2026-10-17 15:59:24.0000000 +00:00 | 2026-11-16 06:30:01.0000000 +00:00 |
| `PRECEDING_TASKS` | STRING | 3 | 0 | 0 | 2 |
| `SUCCEEDING_TASKS` | STRING | 3 | 0 | 0 | 2 |
| `NOT_FINALIZED_PRECEDING_TASKS` | STRING | 2 | 0 | 0 | 1 |
| `NOT_FINALIZED_SUCCEEDING_TASKS` | STRING | 2 | 0 | 0 | 1 |
| `TASK_ACTUAL_COMPLETION_TIME` | STRING | 1 | 0 | 0 | 0 |
| `TASK_NUMBER_OF_ATTACHMENTS` | STRING | 1 | 0 | 0 | 0 |
| `TASK_IS_CHECKLIST` | STRING | 1 | 0 | False | False |
| `TASK_CHECKLIST_COMPLETENESS` | STRING | 1 | 0 | 0 | 0 |
| `OFFSET_ZERO_DAYS` | STRING | 17 | 0 | -1 | 9 |
| `TASK_LINK` | STRING | 214 | 0 | https://taskmanager.adra.com/engageme... | https://taskmanager.adra.com/engageme... |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | taskfacts__20261116_174302.csv | taskfacts__20261116_174302.csv |
| `HASH_KEY` | STRING | 214 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 17:52:11.407000 | 2026-11-16 17:52:11.407000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 17:52:11.407000 | 2026-11-16 17:52:11.407000 |

## Sample rows

| TASK_ID | TASK_PREPARER | TASK_PREPARER_NAME | TASK_APPROVER | TASK_APPROVER_NAME | TASK_STATUS | TASK_APPROVAL_STATUS | TASK_IS_FINALIZED | TASK_FINALIZED | TASK_DUE_DATE_TIME | TASK_REMINDER_DATE_TIME | TASK_PREPARED_BY_NAME | TASK_PREPARED_BY_USERNAME | TASK_PREPARED_DATE_TIME | TASK_LAST_APPROVED_BY_NAME | TASK_LAST_APPROVED_BY_USERNAME | TASK_APPROVED_DATE_TIME | TASK_NUMBER_OF_REJECTS | TASK_ADDED_BY_NAME | TASK_ADDED_BY_USERNAME | TASK_ADDED_DATE_TIME | PRECEDING_TASKS | SUCCEEDING_TASKS | NOT_FINALIZED_PRECEDING_TASKS | NOT_FINALIZED_SUCCEEDING_TASKS | TASK_ACTUAL_COMPLETION_TIME | TASK_NUMBER_OF_ATTACHMENTS | TASK_IS_CHECKLIST | TASK_CHECKLIST_COMPLETENESS | OFFSET_ZERO_DAYS | TASK_LINK | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2676905 | <masked> | <masked> | <masked> | <masked> | Closed | Approval not needed | True | 2026-10-19 07:47:50.0000000 +00:00 | 2026-11-03 22:00:00.0000000 +00:00 | 2026-11-03 22:00:00.0000000 +00:00 | <masked> | <masked> | NULL | <masked> | <masked> | NULL | 0 | <masked> | <masked> | 2026-10-17 15:59:24.0000000 +00:00 | 0 | 0 | 0 | 0 | 0 | 0 | False | 0 | 1 | https://taskmanager.adra.com/engageme... | taskfacts__20261116_174302.csv | <masked> | 2026-11-16 17:52:11.407000 | <masked> | 2026-11-16 17:52:11.407000 |
| 2676906 | <masked> | <masked> | <masked> | <masked> | Closed | Not approved | True | 2026-10-19 07:38:10.0000000 +00:00 | 2026-11-03 22:00:00.0000000 +00:00 | 2026-11-03 22:00:00.0000000 +00:00 | <masked> | <masked> | NULL | <masked> | <masked> | NULL | 0 | <masked> | <masked> | 2026-10-17 15:59:24.0000000 +00:00 | 0 | 0 | 0 | 0 | 0 | 0 | False | 0 | 1 | https://taskmanager.adra.com/engageme... | taskfacts__20261116_174302.csv | <masked> | 2026-11-16 17:52:11.407000 | <masked> | 2026-11-16 17:52:11.407000 |
| 2676907 | <masked> | <masked> | <masked> | <masked> | Closed | Not approved | True | 2026-10-19 07:48:26.0000000 +00:00 | 2026-11-04 22:00:00.0000000 +00:00 | 2026-11-04 22:00:00.0000000 +00:00 | <masked> | <masked> | NULL | <masked> | <masked> | NULL | 0 | <masked> | <masked> | 2026-10-17 15:59:24.0000000 +00:00 | 0 | 0 | 0 | 0 | 0 | 0 | False | 0 | 2 | https://taskmanager.adra.com/engageme... | taskfacts__20261116_174302.csv | <masked> | 2026-11-16 17:52:11.407000 | <masked> | 2026-11-16 17:52:11.407000 |
| 2676918 | <masked> | <masked> | <masked> | <masked> | Closed | Approval not needed | True | 2026-10-19 07:48:58.0000000 +00:00 | 2026-11-03 22:00:00.0000000 +00:00 | 2026-11-03 22:00:00.0000000 +00:00 | <masked> | <masked> | NULL | <masked> | <masked> | NULL | 0 | <masked> | <masked> | 2026-10-17 16:01:20.0000000 +00:00 | 0 | 1 | 0 | 0 | 0 | 0 | False | 0 | 1 | https://taskmanager.adra.com/engageme... | taskfacts__20261116_174302.csv | <masked> | 2026-11-16 17:52:11.407000 | <masked> | 2026-11-16 17:52:11.407000 |
| 2676919 | <masked> | <masked> | <masked> | <masked> | Closed | Approval not needed | True | 2026-10-19 07:48:34.0000000 +00:00 | 2026-11-06 22:00:00.0000000 +00:00 | 2026-11-06 22:00:00.0000000 +00:00 | <masked> | <masked> | NULL | <masked> | <masked> | NULL | 0 | <masked> | <masked> | 2026-10-17 16:01:20.0000000 +00:00 | 1 | 0 | 0 | 0 | 0 | 0 | False | 0 | 4 | https://taskmanager.adra.com/engageme... | taskfacts__20261116_174302.csv | <masked> | 2026-11-16 17:52:11.407000 | <masked> | 2026-11-16 17:52:11.407000 |
