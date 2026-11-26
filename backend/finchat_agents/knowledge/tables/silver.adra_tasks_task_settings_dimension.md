---
name: adra_tasks_task_settings_dimension
schema: silver
layer: silver
domain: recon
type: table
status: active
purpose: Task definitions (name; code; folder; procedure) for close tasks.
grain: one row per TASK_SETTING_KEY (one task definition, probably)
primary_key: []
entity_column: null
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues:
- code: duplicates
  note: 2 exact duplicate rows in the latest export (0.9%). Check duplicates at the grain before counting or summing; warn
    the user.
proposed_fields: []
reviewed: false
---

# adra_tasks_task_settings_dimension

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `TASK_SETTING_KEY` | string |  |  | `TASK_SETTING_KEY` |
| `ENGAGEMENT_KEY` | string |  |  | `ENGAGEMENT_KEY` |
| `TASK_NAME` | string |  |  | `TASK_NAME` |
| `TASK_CODE` | string |  |  | `TASK_CODE` |
| `TASK_FOLDER_NAME` | string |  |  | `TASK_FOLDER_NAME` |
| `TASK_FOLDER_PATH` | string |  |  | `TASK_FOLDER_PATH` |
| `TASK_DESCRIPTION` | string |  |  | `TASK_DESCRIPTION` |
| `TASK_PROCEDURE` | string |  |  | `TASK_PROCEDURE` |
| `TASK_TYPE` | string |  |  | `TASK_TYPE` |
| `TASK_IS_INTERNAL_CONTROL` | string |  |  | `TASK_IS_INTERNAL_CONTROL` |
| `TASK_NUMBER_OF_APPROVALS` | string |  |  | `TASK_NUMBER_OF_APPROVALS` |
| `TASK_REMINDER_DAYS` | string |  |  | `TASK_REMINDER_DAYS` |
| `TASK_EXPECTED_COMPLETION_TIME` | string |  |  | `TASK_EXPECTED_COMPLETION_TIME` |
| `TASK_LIBRARY_ATTACHMENTS` | string |  |  | `TASK_LIBRARY_ATTACHMENTS` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**TASK_FOLDER_NAME**
- `Adjustments`
- `Pre-Close`
- `Sign-off`
- `Sub-ledgers`
- `Reconcile Revenue`
- `CS Invoices`
- `Review`
- `Pre-close`
- `Journal Entries`
- `None`
- `Close AP`
- `AP Invoices`
- `Accounts Receivable`
- `Close General Ledger`
- `Reconciliation`
- `Management Reporting`
- `Payroll`
- `0`
- `Accounts Payable`
- `Revenue`

**TASK_FOLDER_PATH**
- `Monthly Close/US001-United States/Adjustments`
- `Monthly Close/US001-United States/Pre-Close`
- `Month End Close/Reconcile Revenue`
- `KF Month End Close/Sign-off`
- `Month End Close/CS Invoices`
- `KF Month End Close/Pre-close`
- `KF Month End Close/Review`
- `KF Month End Close/Adjustments`
- `Month End Close/Journal Entries`
- `KF Month End Close/Sub-ledgers`
- `Month End Close/Close AP`
- `Month End Close/AP Invoices`
- `None`
- `Monthly Close/US001-United States/Accounts Receivable`
- `Monthly Close/US001-United States/Sub-ledgers`
- `Month End Close/Close General Ledger`
- `Monthly Close/US001-United States/Sign-off`
- `Monthly Close/US001-United States/Reconciliation`
- `Monthly Close/US001-United States/Management Reporting`
- `Monthly Close/US001-United States/Payroll`
- `0`
- `Monthly Close/G002-Germany/Accounts Payable`
- `Monthly Close/US001-United States/Review`
- `Monthly Close/UK003-United Kingdom/Sub-ledgers`
- `Monthly Close/G002-Germany/Accounts Receivable`
- `Monthly Close/G002-Germany/Adjustments`
- `20`
- `Monthly Close/UK003-United Kingdom/Adjustments`
- `Monthly Close/US001-United States/Revenue`
- `Monthly Close/UK003-United Kingdom/Pre-Close`

**TASK_PROCEDURE**
- `None`
- `1. Run the report of the status at period end 2. Check the balance agrees with the previous period reconciled amount ...`
- `1. Download prior month's schedule 2. Pull Fixed Asset register from ERP 3. Add new Fixed Assets to schedule 4. Tie t...`
- `CS reports & NS report`
- `NS`
- `NS Reports`
- `0`
- `NS - All Countries Finance Directors`
- `System Administration`
- `Save to the Accounting/Finance Drive`
- `CLOSE GL for posting - System Administration`
- `Package includes financials for US001 - United States. Produce Drafts for CFO review ensure these are signed by CFO a...`
- `Source-system AP transactions received, validated and interfaced into NetSuite`
- `Local Subsidiaries systems - load via CSV`
- `HR report & ADT`
- `Contracts/Schedules`
- `Via email to Regional Finance Heads`
- `Fixed Asset Register/Reconciliation`
- `Local Subsidiaries systems - load via CSV (Ensure 3rd Party Order Is referenced)`
- `CS & NS - Do not include IC payable invoices`
- `Payroll files received, validated and journal entries generated for upload`
- `CS reports/local system & NS report`
- `Package includes final financials for all legal entities. Produce Drafts for CFO review ensure these are signed by CF...`
- `Datarails`
- `Perform AR/AP/FA subledger-to-GL interface completeness and accuracy checks`
- `After Intercompany statement reconciled`
- `Extract, transform and load subsidiary trial balances from source ERPs into consolidation environment`
- `Revenue pushed to NS from CS or local system (non-transacting Subs) via CSV`
- `CLOSE AP for posting - System Administration`
- `Confirm subledgers tie-out to the GL`
- `Bank Statements - NS`
- `Produce clean copy of final draft produced in task`
- `Balance Sheet Reconciliation`
- `Log in to NetSuiteGo to Fixed Asset module (Look at attachment for detailed print screens)Add new fixed assetsUpdate ...`
- `Per new Debt schedule`
- `- Attach all legal checklists ensuring completeness of report.`
- `NetSuite - Post to ledger from reconciliation`
- `Contracts - Payroll`

**TASK_TYPE**
- `Periodic`
- `Daily`
- `None`

**TASK_IS_INTERNAL_CONTROL**
- `False`
- `None`

**TASK_NUMBER_OF_APPROVALS**
- `1`
- `0`
- `None`

**TASK_REMINDER_DAYS**
- `0`
- `None`

**TASK_EXPECTED_COMPLETION_TIME**
- `0`
- `None`
- `60`
- `120`
- `480`
- `240`
- `20`
- `180`
- `90`
- `10`
- `30`
- `45`

**TASK_LIBRARY_ATTACHMENTS**
- `0`
- `None`

**SOURCE_FILE_NAME**
- `tasksettingsdimension__20261116_174302.csv`

**MDP_CREATED_DATE**
- `2026-11-16 17:52:11.402925+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 17:52:11.402925+00:00`
