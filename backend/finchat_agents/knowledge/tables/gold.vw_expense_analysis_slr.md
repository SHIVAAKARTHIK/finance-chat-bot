---
name: vw_expense_analysis_slr
schema: gold
layer: gold
domain: subledger
type: view
status: broken
purpose: 'Expense analysis (line grain) over lakehouse_mvpai.silver.fact_fynapse_slr_journals. No filters applied: all source
  systems and all lines, including offsetting control account 176100 (Credit Card - Expenses Control). Use LINE_TYPE = ''Expense''
  (or IS_EXPENSE_LINE = true) to avoid netting expenses against the control account. Amounts in GBP from REPORTING_AMOUNT.
  Account descriptions from lakehouse_hsbc.mdm_ind_pc_insurance.coa_mdm.'
grain: one row per Fynapse subledger journal line
primary_key:
- JOURNAL_LINE_ID
entity_column: ENTITY
period_columns:
- POSTING_DATE
- TRANSACTION_DATE
- POSTING_MONTH
- FISCAL_YEAR
- PERIOD
pii_columns: []
synonyms: []
built_from:
- fact_fynapse_slr_journals
known_issues: []
row_count: null
proposed_fields: []
reviewed: false
broken_error: the profiling query failed in the catalog export (no row count); the error text is not in the workbook
---

# vw_expense_analysis_slr

Expense analysis (line grain) over lakehouse_mvpai.silver.fact_fynapse_slr_journals. No filters applied: all source systems and all lines, including offsetting control account 176100 (Credit Card - Expenses Control). Use LINE_TYPE = 'Expense' (or IS_EXPENSE_LINE = true) to avoid netting expenses against the control account. Amounts in GBP from REPORTING_AMOUNT. Account descriptions from lakehouse_hsbc.mdm_ind_pc_insurance.coa_mdm.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `ENTITY` | string |  |  | `ENTITY` |
| `COST_CENTER` | string |  |  | `COST_CENTER` |
| `ACCOUNT` | string |  |  | `ACCOUNT` |
| `ACCOUNT_DESCRIPTION` | string |  |  | `ACCOUNT_DESCRIPTION` |
| `ACCOUNT_LABEL` | string |  |  | `ACCOUNT_LABEL` |
| `LINE_TYPE` | string |  |  | `LINE_TYPE` |
| `IS_EXPENSE_LINE` | boolean |  |  | `IS_EXPENSE_LINE` |
| `EXPENSE_TYPE` | string |  |  | `EXPENSE_TYPE` |
| `POSTING_DATE` | date |  |  | `POSTING_DATE` |
| `TRANSACTION_DATE` | date |  |  | `TRANSACTION_DATE` |
| `POSTING_MONTH` | date |  |  | `POSTING_MONTH` |
| `FISCAL_YEAR` | int |  |  | `FISCAL_YEAR` |
| `PERIOD` | int |  |  | `PERIOD` |
| `SOURCE_TRANSACTION_ID` | string |  |  | `SOURCE_TRANSACTION_ID` |
| `JOURNAL_ID` | string |  |  | `JOURNAL_ID` |
| `JOURNAL_LINE_ID` | string |  |  | `JOURNAL_LINE_ID` |
| `JOURNAL_LINE_NO` | int |  |  | `JOURNAL_LINE_NO` |
| `LINE_DESCRIPTION` | string |  |  | `LINE_DESCRIPTION` |
| `AMOUNT_GBP` | decimal |  |  | `AMOUNT_GBP` |
| `REPORTING_CURRENCY` | string |  |  | `REPORTING_CURRENCY` |
| `TRANSACTION_AMOUNT` | decimal |  |  | `TRANSACTION_AMOUNT` |
| `TRANSACTION_CURRENCY` | string |  |  | `TRANSACTION_CURRENCY` |
| `FUNCTIONAL_AMOUNT` | decimal |  |  | `FUNCTIONAL_AMOUNT` |
| `FUNCTIONAL_CURRENCY` | string |  |  | `FUNCTIONAL_CURRENCY` |
| `SOURCE_SYSTEM` | string |  |  | `SOURCE_SYSTEM` |
| `BUSINESS_EVENT` | string |  |  | `BUSINESS_EVENT` |
| `JOURNAL_TYPE` | string |  |  | `JOURNAL_TYPE` |

## Profile

Rows in the latest export: unknown.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `ENTITY` | STRING |  |  |  |  |
| `COST_CENTER` | STRING |  |  |  |  |
| `ACCOUNT` | STRING |  |  |  |  |
| `ACCOUNT_DESCRIPTION` | STRING |  |  |  |  |
| `ACCOUNT_LABEL` | STRING |  |  |  |  |
| `LINE_TYPE` | STRING |  |  |  |  |
| `IS_EXPENSE_LINE` | BOOLEAN |  |  |  |  |
| `EXPENSE_TYPE` | STRING |  |  |  |  |
| `POSTING_DATE` | DATE |  |  |  |  |
| `TRANSACTION_DATE` | DATE |  |  |  |  |
| `POSTING_MONTH` | DATE |  |  |  |  |
| `FISCAL_YEAR` | INT |  |  |  |  |
| `PERIOD` | INT |  |  |  |  |
| `SOURCE_TRANSACTION_ID` | STRING |  |  |  |  |
| `JOURNAL_ID` | STRING |  |  |  |  |
| `JOURNAL_LINE_ID` | STRING |  |  |  |  |
| `JOURNAL_LINE_NO` | INT |  |  |  |  |
| `LINE_DESCRIPTION` | STRING |  |  |  |  |
| `AMOUNT_GBP` | DECIMAL |  |  |  |  |
| `REPORTING_CURRENCY` | STRING |  |  |  |  |
| `TRANSACTION_AMOUNT` | DECIMAL |  |  |  |  |
| `TRANSACTION_CURRENCY` | STRING |  |  |  |  |
| `FUNCTIONAL_AMOUNT` | DECIMAL |  |  |  |  |
| `FUNCTIONAL_CURRENCY` | STRING |  |  |  |  |
| `SOURCE_SYSTEM` | STRING |  |  |  |  |
| `BUSINESS_EVENT` | STRING |  |  |  |  |
| `JOURNAL_TYPE` | STRING |  |  |  |  |
