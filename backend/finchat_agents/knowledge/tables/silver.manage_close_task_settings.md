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
- `2688677`
- `2677500`
- `2677484`
- `2677503`
- `2688678`
- `2677498`
- `2688667`
- `2677488`
- `2677502`
- `2688674`
- `2677491`
- `2688681`
- `2677492`
- `2677489`
- `2677487`
- `2688675`
- `2688671`
- `2677485`
- `2688680`
- `2688676`
- `2688679`
- `2688673`
- `2677501`
- `2688672`
- `2688685`
- `2677486`
- `2688683`
- `2688684`
- `2688682`

**EngagementKey**
- `949e65cb-7216-4cb5-9840-4bc138a1921b`

**TaskName**
- `Review Open PO's`
- `Update Fixed Assets Schedule`
- `Fixed Assets - Close Prior Month`
- `Review Income Statement`
- `Accrued Revenue Review`
- `Bonus Accrual`
- `Fixed Asset Depreciation`
- `Review AP Aging, Open Invoice, & Pending Approval Reports`
- `Run Draft Financial Statements`
- `Review Balance Sheet`
- `Produce Drafts for Internal Management Review`
- `Review AP Aging, Open Invoice, & Pending Approval reports`
- `Finance Approvals for Invoice Exceptions`

**TaskCode**
- `US001-23R`
- `US001-04R`
- `US001-24R`
- `US001-22`
- `UK003-03`
- `US001-25`
- `US001-07`
- `US001-18`
- `US001-21`
- `US001-03`
- `G002-03`
- `US001-17`
- `UK003-02`
- `US001-11`
- `UK003-01`
- `US001-04`
- `US001-27`

**TaskFolderName**
- `Adjustments`
- `Pre-Close`
- `Sign-off`
- `Sub-ledgers`
- `Review`

**TaskFolderPath**
- `Monthly Close/US001-United States/Adjustments`
- `Monthly Close/US001-United States/Pre-Close`
- `Monthly Close/US001-United States/Review`
- `Monthly Close/US001-United States/General Ledger`
- `Monthly Close/US001-United States/Sub-ledgers`
- `Monthly Close/G002-Germany/General Ledger`
- `Monthly Close/UK003-United Kingdom/Sub-ledgers`
- `Monthly Close/UK003-United Kingdom/Pre-Close`
- `Monthly Close/UK003-United Kingdom/General Ledger`

**TaskDescription**
- `Close out any PO's that are still open that can be closed`
- `Updating schedule for Fixed Assets`
- `The period-end closing routine for General Ledger has to be completed before starting the next period year.`
- `Review comparative income statement for variances, research variances`
- `Review the accrued revenue activity for the month. Record a JE for any significant changes.`
- `Review the AP Aging, Open Invoice, and Pending Approval reports for any items that should have been paid, research wh...`
- `This is for the legal entity US001 - United States`
- `Book entry to accrual bonus`
- `None`
- `Update Fixed Asset schedules with New Additions and Create Depreciation JEs`
- `Review balance sheet for abnormal variances, research variances`

**TaskProcedure**
- `None`
- `1. Download prior month's schedule 2. Pull Fixed Asset register from ERP 3. Add new Fixed Assets to schedule 4. Tie t...`
- `1. Run the report of the status at period end 2. Check the balance agrees with the previous period reconciled amount ...`
- `Log in to NetSuiteGo to Fixed Asset module (Look at attachment for detailed print screens)Add new fixed assetsUpdate ...`
- `- Attach all legal checklists ensuring completeness of report. - Cast to final Trial Balance and ensure correct class...`
- `Produce clean copy of final draft produced in task`

**TaskType**
- `Daily`
- `Periodic`

**TaskIsInternalControl**
- `False`

**TaskNumberOfApprovals**
- `1`
- `0`

**TaskReminderDays**
- `0`
- `None`

**TaskExpectedCompletionTime**
- `0`
- `480`
- `60`
- `20`
- `180`
- `120`

**TaskLibraryAttachments**
- `0`

**MDP_CREATED_DATE**
- `2026-10-23 10:51:53.854944+00:00`

**MDP_MODIFIED_DATE**
- `2026-10-23 10:51:53.854944+00:00`
