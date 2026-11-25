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
row_count: 228
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
- `Adjustments`: 74 rows
- `Pre-Close`: 35 rows
- `Sign-off`: 15 rows
- `Sub-ledgers`: 13 rows
- `Reconcile Revenue`: 12 rows
- `CS Invoices`: 10 rows
- `Review`: 10 rows
- `Pre-close`: 9 rows
- `Journal Entries`: 7 rows
- `None`: 7 rows
- `Close AP`: 6 rows
- `AP Invoices`: 6 rows
- `Accounts Receivable`: 6 rows
- `Close General Ledger`: 4 rows
- `Reconciliation`: 3 rows
- `Management Reporting`: 3 rows
- `Payroll`: 3 rows
- `0`: 2 rows
- `Accounts Payable`: 2 rows
- `Revenue`: 1 rows

**TASK_FOLDER_PATH**
- `Monthly Close/US001-United States/Adjustments`: 64 rows
- `Monthly Close/US001-United States/Pre-Close`: 34 rows
- `Month End Close/Reconcile Revenue`: 12 rows
- `KF Month End Close/Sign-off`: 11 rows
- `Month End Close/CS Invoices`: 10 rows
- `KF Month End Close/Pre-close`: 9 rows
- `KF Month End Close/Review`: 8 rows
- `KF Month End Close/Adjustments`: 8 rows
- `Month End Close/Journal Entries`: 7 rows
- `KF Month End Close/Sub-ledgers`: 7 rows
- `Month End Close/Close AP`: 6 rows
- `Month End Close/AP Invoices`: 6 rows
- `None`: 6 rows
- `Monthly Close/US001-United States/Accounts Receivable`: 5 rows
- `Monthly Close/US001-United States/Sub-ledgers`: 5 rows
- `Month End Close/Close General Ledger`: 4 rows
- `Monthly Close/US001-United States/Sign-off`: 4 rows
- `Monthly Close/US001-United States/Reconciliation`: 3 rows
- `Monthly Close/US001-United States/Management Reporting`: 3 rows
- `Monthly Close/US001-United States/Payroll`: 3 rows
- `0`: 2 rows
- `Monthly Close/G002-Germany/Accounts Payable`: 2 rows
- `Monthly Close/US001-United States/Review`: 2 rows
- `Monthly Close/UK003-United Kingdom/Sub-ledgers`: 1 rows
- `Monthly Close/G002-Germany/Accounts Receivable`: 1 rows
- `Monthly Close/G002-Germany/Adjustments`: 1 rows
- `20`: 1 rows
- `Monthly Close/UK003-United Kingdom/Adjustments`: 1 rows
- `Monthly Close/US001-United States/Revenue`: 1 rows
- `Monthly Close/UK003-United Kingdom/Pre-Close`: 1 rows

**TASK_PROCEDURE**
- `None`: 115 rows
- `1. Run the report of the status at period end 2. Check the balance agrees with the previous period reconciled amount ...`: 30 rows
- `1. Download prior month's schedule 2. Pull Fixed Asset register from ERP 3. Add new Fixed Assets to schedule 4. Tie t...`: 30 rows
- `CS reports & NS report`: 7 rows
- `NS`: 5 rows
- `NS Reports`: 3 rows
- `0`: 2 rows
- `NS - All Countries Finance Directors`: 2 rows
- `System Administration`: 2 rows
- `Save to the Accounting/Finance Drive`: 2 rows
- `CLOSE GL for posting - System Administration`: 2 rows
- `Package includes financials for US001 - United States. Produce Drafts for CFO review ensure these are signed by CFO a...`: 2 rows
- `Source-system AP transactions received, validated and interfaced into NetSuite`: 1 rows
- `Local Subsidiaries systems - load via CSV`: 1 rows
- `HR report & ADT`: 1 rows
- `Contracts/Schedules`: 1 rows
- `Via email to Regional Finance Heads`: 1 rows
- `Fixed Asset Register/Reconciliation`: 1 rows
- `Local Subsidiaries systems - load via CSV (Ensure 3rd Party Order Is referenced)`: 1 rows
- `CS & NS - Do not include IC payable invoices`: 1 rows
- `Payroll files received, validated and journal entries generated for upload`: 1 rows
- `CS reports/local system & NS report`: 1 rows
- `Package includes final financials for all legal entities. Produce Drafts for CFO review ensure these are signed by CF...`: 1 rows
- `Datarails`: 1 rows
- `Perform AR/AP/FA subledger-to-GL interface completeness and accuracy checks`: 1 rows
- `After Intercompany statement reconciled`: 1 rows
- `Extract, transform and load subsidiary trial balances from source ERPs into consolidation environment`: 1 rows
- `Revenue pushed to NS from CS or local system (non-transacting Subs) via CSV`: 1 rows
- `CLOSE AP for posting - System Administration`: 1 rows
- `Confirm subledgers tie-out to the GL`: 1 rows
- `Bank Statements - NS`: 1 rows
- `Produce clean copy of final draft produced in task`: 1 rows
- `Balance Sheet Reconciliation`: 1 rows
- `Log in to NetSuiteGo to Fixed Asset module (Look at attachment for detailed print screens)Add new fixed assetsUpdate ...`: 1 rows
- `Per new Debt schedule`: 1 rows
- `- Attach all legal checklists ensuring completeness of report.`: 1 rows
- `NetSuite - Post to ledger from reconciliation`: 1 rows
- `Contracts - Payroll`: 1 rows

**TASK_TYPE**
- `Periodic`: 126 rows
- `Daily`: 90 rows
- `None`: 12 rows

**TASK_IS_INTERNAL_CONTROL**
- `False`: 216 rows
- `None`: 12 rows

**TASK_NUMBER_OF_APPROVALS**
- `1`: 109 rows
- `0`: 107 rows
- `None`: 12 rows

**TASK_REMINDER_DAYS**
- `0`: 212 rows
- `None`: 16 rows

**TASK_EXPECTED_COMPLETION_TIME**
- `0`: 178 rows
- `None`: 12 rows
- `60`: 8 rows
- `120`: 6 rows
- `480`: 6 rows
- `240`: 5 rows
- `20`: 4 rows
- `180`: 4 rows
- `90`: 2 rows
- `10`: 1 rows
- `30`: 1 rows
- `45`: 1 rows

**TASK_LIBRARY_ATTACHMENTS**
- `0`: 216 rows
- `None`: 12 rows

**SOURCE_FILE_NAME**
- `tasksettingsdimension__20261116_174302.csv`: 228 rows

**MDP_CREATED_DATE**
- `2026-11-16 17:52:11.402925+00:00`: 228 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 17:52:11.402925+00:00`: 228 rows

## Profile

Rows in the latest export: 228.
Exact duplicate rows: 2.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `TASK_SETTING_KEY` | STRING | 231 | 0 |  |  |
| `ENGAGEMENT_KEY` | STRING | 2 | 8 |  |  |
| `TASK_NAME` | STRING | 116 | 6 | 401k Employer Match Entries - End of ... | Validate required FCA / regulatory re... |
| `TASK_CODE` | STRING | 124 | 6 | 0 | US001-50 |
| `TASK_FOLDER_NAME` | STRING | 18 | 7 | 0 | Sub-ledgers |
| `TASK_FOLDER_PATH` | STRING | 30 | 6 | 0 | Monthly Close/US001-United States/Sub... |
| `TASK_DESCRIPTION` | STRING | 65 | 53 | 0 | Verify that required reconciliations,... |
| `TASK_PROCEDURE` | STRING | 37 | 115 | - Attach all legal checklists ensurin... | Via email to Regional Finance Heads |
| `TASK_TYPE` | STRING | 2 | 12 | Daily | Periodic |
| `TASK_IS_INTERNAL_CONTROL` | STRING | 1 | 12 | False | False |
| `TASK_NUMBER_OF_APPROVALS` | STRING | 2 | 12 | 0 | 1 |
| `TASK_REMINDER_DAYS` | STRING | 1 | 16 | 0 | 0 |
| `TASK_EXPECTED_COMPLETION_TIME` | STRING | 11 | 12 | 0 | 90 |
| `TASK_LIBRARY_ATTACHMENTS` | STRING | 1 | 12 | 0 | 0 |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | tasksettingsdimension__20261116_17430... | tasksettingsdimension__20261116_17430... |
| `HASH_KEY` | STRING | 226 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 17:52:11.403000 | 2026-11-16 17:52:11.403000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 17:52:11.403000 | 2026-11-16 17:52:11.403000 |

## Sample rows

| TASK_NAME | TASK_CODE | TASK_FOLDER_NAME | TASK_FOLDER_PATH | TASK_DESCRIPTION | TASK_PROCEDURE | TASK_TYPE | TASK_IS_INTERNAL_CONTROL | TASK_NUMBER_OF_APPROVALS | TASK_REMINDER_DAYS | TASK_EXPECTED_COMPLETION_TIME | TASK_LIBRARY_ATTACHMENTS | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US Payroll Entries - End of Month | US001-09 | Payroll | Monthly Close/US001-United States/Pay... | Enter Payroll JEs | NULL | Periodic | False | 0 | 0 | 240 | 0 | tasksettingsdimension__20261116_17430... | <masked> | 2026-11-16 17:52:11.403000 | <masked> | 2026-11-16 17:52:11.403000 |
| 401k Employer Match Entries - End of ... | US001-10 | Payroll | Monthly Close/US001-United States/Pay... | Book the Employer 401k Match using th... | NULL | Periodic | False | 1 | 0 | 60 | 0 | tasksettingsdimension__20261116_17430... | <masked> | 2026-11-16 17:52:11.403000 | <masked> | 2026-11-16 17:52:11.403000 |
| International Payroll | US001-12 | Payroll | Monthly Close/US001-United States/Pay... | Book entries for all non-USD payroll | NULL | Periodic | False | 1 | 0 | 240 | 0 | tasksettingsdimension__20261116_17430... | <masked> | 2026-11-16 17:52:11.403000 | <masked> | 2026-11-16 17:52:11.403000 |
| Apply Customer Payments | US001-06 | Accounts Receivable | Monthly Close/US001-United States/Acc... | Applying payments received in all Tri... | NULL | Periodic | False | 0 | 0 | 120 | 0 | tasksettingsdimension__20261116_17430... | <masked> | 2026-11-16 17:52:11.403000 | <masked> | 2026-11-16 17:52:11.403000 |
| Customer Billing - Monthly | US001-16 | Accounts Receivable | Monthly Close/US001-United States/Acc... | Bill all SaaS customers that are on a... | NULL | Periodic | False | 0 | 0 | 90 | 0 | tasksettingsdimension__20261116_17430... | <masked> | 2026-11-16 17:52:11.403000 | <masked> | 2026-11-16 17:52:11.403000 |
