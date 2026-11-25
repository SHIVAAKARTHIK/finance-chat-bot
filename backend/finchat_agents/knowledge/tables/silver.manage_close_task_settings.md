---
name: manage_close_task_settings
schema: silver
layer: silver
domain: recon
type: table
status: active
purpose: Close task definitions (name; code; folder; procedure) for the Manage the Close screen.
grain: one row per HASH_KEY (one task definition)
primary_key:
- HASH_KEY
entity_column: null
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from:
- adra_tasks_task_settings_dimension (likely)
known_issues: []
row_count: 29
proposed_fields:
- grain
- primary_key
reviewed:
- superseded_by
superseded_by:
- silver.adra_tasks_task_settings_dimension
---

# manage_close_task_settings

> Superseded: this table is a copy of ADRA data. Answers use the source of truth `silver.adra_tasks_task_settings_dimension` (decision 21 Nov 2026).

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `TaskSettingKey` | long |  |  | `TaskSettingKey` |
| `EngagementKey` | string |  |  | `EngagementKey` |
| `TaskName` | string |  |  | `TaskName` |
| `TaskCode` | string |  |  | `TaskCode` |
| `TaskFolderName` | string |  |  | `TaskFolderName` |
| `TaskFolderPath` | string |  |  | `TaskFolderPath` |
| `TaskDescription` | string |  |  | `TaskDescription` |
| `TaskProcedure` | string |  |  | `TaskProcedure` |
| `TaskType` | string |  |  | `TaskType` |
| `TaskIsInternalControl` | boolean |  |  | `TaskIsInternalControl` |
| `TaskNumberOfApprovals` | int |  |  | `TaskNumberOfApprovals` |
| `TaskReminderDays` | int |  |  | `TaskReminderDays` |
| `TaskExpectedCompletionTime` | int |  |  | `TaskExpectedCompletionTime` |
| `TaskLibraryAttachments` | int |  |  | `TaskLibraryAttachments` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**TaskSettingKey**
- `2688677`: 1 rows
- `2677500`: 1 rows
- `2677484`: 1 rows
- `2677503`: 1 rows
- `2688678`: 1 rows
- `2677498`: 1 rows
- `2688667`: 1 rows
- `2677488`: 1 rows
- `2677502`: 1 rows
- `2688674`: 1 rows
- `2677491`: 1 rows
- `2688681`: 1 rows
- `2677492`: 1 rows
- `2677489`: 1 rows
- `2677487`: 1 rows
- `2688675`: 1 rows
- `2688671`: 1 rows
- `2677485`: 1 rows
- `2688680`: 1 rows
- `2688676`: 1 rows
- `2688679`: 1 rows
- `2688673`: 1 rows
- `2677501`: 1 rows
- `2688672`: 1 rows
- `2688685`: 1 rows
- `2677486`: 1 rows
- `2688683`: 1 rows
- `2688684`: 1 rows
- `2688682`: 1 rows

**EngagementKey**
- `949e65cb-7216-4cb5-9840-4bc138a1921b`: 29 rows

**TaskName**
- `Review Open PO's`: 6 rows
- `Update Fixed Assets Schedule`: 5 rows
- `Fixed Assets - Close Prior Month`: 5 rows
- `Review Income Statement`: 3 rows
- `Accrued Revenue Review`: 2 rows
- `Bonus Accrual`: 1 rows
- `Fixed Asset Depreciation`: 1 rows
- `Review AP Aging, Open Invoice, & Pending Approval Reports`: 1 rows
- `Run Draft Financial Statements`: 1 rows
- `Review Balance Sheet`: 1 rows
- `Produce Drafts for Internal Management Review`: 1 rows
- `Review AP Aging, Open Invoice, & Pending Approval reports`: 1 rows
- `Finance Approvals for Invoice Exceptions`: 1 rows

**TaskCode**
- `US001-23R`: 5 rows
- `US001-04R`: 5 rows
- `US001-24R`: 5 rows
- `US001-22`: 1 rows
- `UK003-03`: 1 rows
- `US001-25`: 1 rows
- `US001-07`: 1 rows
- `US001-18`: 1 rows
- `US001-21`: 1 rows
- `US001-03`: 1 rows
- `G002-03`: 1 rows
- `US001-17`: 1 rows
- `UK003-02`: 1 rows
- `US001-11`: 1 rows
- `UK003-01`: 1 rows
- `US001-04`: 1 rows
- `US001-27`: 1 rows

**TaskFolderName**
- `Adjustments`: 12 rows
- `Pre-Close`: 8 rows
- `Sign-off`: 4 rows
- `Sub-ledgers`: 3 rows
- `Review`: 2 rows

**TaskFolderPath**
- `Monthly Close/US001-United States/Adjustments`: 12 rows
- `Monthly Close/US001-United States/Pre-Close`: 7 rows
- `Monthly Close/US001-United States/Review`: 2 rows
- `Monthly Close/US001-United States/General Ledger`: 2 rows
- `Monthly Close/US001-United States/Sub-ledgers`: 2 rows
- `Monthly Close/G002-Germany/General Ledger`: 1 rows
- `Monthly Close/UK003-United Kingdom/Sub-ledgers`: 1 rows
- `Monthly Close/UK003-United Kingdom/Pre-Close`: 1 rows
- `Monthly Close/UK003-United Kingdom/General Ledger`: 1 rows

**TaskDescription**
- `Close out any PO's that are still open that can be closed`: 6 rows
- `Updating schedule for Fixed Assets`: 5 rows
- `The period-end closing routine for General Ledger has to be completed before starting the next period year.`: 5 rows
- `Review comparative income statement for variances, research variances`: 3 rows
- `Review the accrued revenue activity for the month. Record a JE for any significant changes.`: 2 rows
- `Review the AP Aging, Open Invoice, and Pending Approval reports for any items that should have been paid, research wh...`: 2 rows
- `This is for the legal entity US001 - United States`: 2 rows
- `Book entry to accrual bonus`: 1 rows
- `None`: 1 rows
- `Update Fixed Asset schedules with New Additions and Create Depreciation JEs`: 1 rows
- `Review balance sheet for abnormal variances, research variances`: 1 rows

**TaskProcedure**
- `None`: 16 rows
- `1. Download prior month's schedule 2. Pull Fixed Asset register from ERP 3. Add new Fixed Assets to schedule 4. Tie t...`: 5 rows
- `1. Run the report of the status at period end 2. Check the balance agrees with the previous period reconciled amount ...`: 5 rows
- `Log in to NetSuiteGo to Fixed Asset module (Look at attachment for detailed print screens)Add new fixed assetsUpdate ...`: 1 rows
- `- Attach all legal checklists ensuring completeness of report. - Cast to final Trial Balance and ensure correct class...`: 1 rows
- `Produce clean copy of final draft produced in task`: 1 rows

**TaskType**
- `Daily`: 15 rows
- `Periodic`: 14 rows

**TaskIsInternalControl**
- `False`: 29 rows

**TaskNumberOfApprovals**
- `1`: 22 rows
- `0`: 7 rows

**TaskReminderDays**
- `0`: 27 rows
- `None`: 2 rows

**TaskExpectedCompletionTime**
- `0`: 15 rows
- `480`: 5 rows
- `60`: 3 rows
- `20`: 2 rows
- `180`: 2 rows
- `120`: 2 rows

**TaskLibraryAttachments**
- `0`: 29 rows

**MDP_CREATED_DATE**
- `2026-10-23 10:51:53.854944+00:00`: 29 rows

**MDP_MODIFIED_DATE**
- `2026-10-23 10:51:53.854944+00:00`: 29 rows

## Profile

Rows in the latest export: 29.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `TaskSettingKey` | LONG | 29 | 0 | 2677484 | 2688685 |
| `EngagementKey` | STRING | 1 | 0 | 949e65cb-7216-4cb5-9840-4bc138a1921b | 949e65cb-7216-4cb5-9840-4bc138a1921b |
| `TaskName` | STRING | 13 | 0 | Accrued Revenue Review | Update Fixed Assets Schedule |
| `TaskCode` | STRING | 17 | 0 | G002-03 | US001-27 |
| `TaskFolderName` | STRING | 5 | 0 | Adjustments | Sub-ledgers |
| `TaskFolderPath` | STRING | 9 | 0 | Monthly Close/G002-Germany/General Le... | Monthly Close/US001-United States/Sub... |
| `TaskDescription` | STRING | 10 | 1 | Book entry to accrual bonus | Updating schedule for Fixed Assets |
| `TaskProcedure` | STRING | 5 | 16 | - Attach all legal checklists ensurin... | Produce clean copy of final draft pro... |
| `TaskType` | STRING | 2 | 0 | Daily | Periodic |
| `TaskIsInternalControl` | BOOLEAN | 1 | 0 | False | False |
| `TaskNumberOfApprovals` | INT | 2 | 0 | 0 | 1 |
| `TaskReminderDays` | INT | 1 | 2 | 0 | 0 |
| `TaskExpectedCompletionTime` | INT | 6 | 0 | 0 | 480 |
| `TaskLibraryAttachments` | INT | 1 | 0 | 0 | 0 |
| `HASH_KEY` | STRING | 30 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-10-23 10:51:53.855000 | 2026-10-23 10:51:53.855000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-10-23 10:51:53.855000 | 2026-10-23 10:51:53.855000 |

## Sample rows

| TaskSettingKey | EngagementKey | TaskName | TaskCode | TaskFolderName | TaskFolderPath | TaskDescription | TaskProcedure | TaskType | TaskIsInternalControl | TaskNumberOfApprovals | TaskReminderDays | TaskExpectedCompletionTime | TaskLibraryAttachments | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2677484 | 949e65cb-7216-4cb5-9840-4bc138a1921b | Review AP Aging, Open Invoice, & Pend... | UK003-01 | Pre-Close | Monthly Close/UK003-United Kingdom/Pr... | Review the AP Aging, Open Invoice, an... | NULL | Periodic | False | 0 | 0 | 60 | 0 | <masked> | 2026-10-23 10:51:53.855000 | <masked> | 2026-10-23 10:51:53.855000 |
| 2677485 | 949e65cb-7216-4cb5-9840-4bc138a1921b | Accrued Revenue Review | UK003-02 | Sub-ledgers | Monthly Close/UK003-United Kingdom/Su... | Review the accrued revenue activity f... | NULL | Periodic | False | 0 | 0 | 180 | 0 | <masked> | 2026-10-23 10:51:53.855000 | <masked> | 2026-10-23 10:51:53.855000 |
| 2677486 | 949e65cb-7216-4cb5-9840-4bc138a1921b | Review Income Statement | UK003-03 | Sign-off | Monthly Close/UK003-United Kingdom/Ge... | Review comparative income statement f... | NULL | Periodic | False | 0 | 0 | 480 | 0 | <masked> | 2026-10-23 10:51:53.855000 | <masked> | 2026-10-23 10:51:53.855000 |
| 2677487 | 949e65cb-7216-4cb5-9840-4bc138a1921b | Review Income Statement | G002-03 | Sign-off | Monthly Close/G002-Germany/General Le... | Review comparative income statement f... | NULL | Periodic | False | 0 | 0 | 480 | 0 | <masked> | 2026-10-23 10:51:53.855000 | <masked> | 2026-10-23 10:51:53.855000 |
| 2677488 | 949e65cb-7216-4cb5-9840-4bc138a1921b | Review AP Aging, Open Invoice, & Pend... | US001-03 | Pre-Close | Monthly Close/US001-United States/Pre... | Review the AP Aging, Open Invoice, an... | NULL | Periodic | False | 1 | 0 | 60 | 0 | <masked> | 2026-10-23 10:51:53.855000 | <masked> | 2026-10-23 10:51:53.855000 |
