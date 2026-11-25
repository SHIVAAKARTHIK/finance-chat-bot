---
name: vw_commission_analysis_slr_mga
schema: gold
layer: gold
domain: subledger
type: view
status: broken
purpose: Commission (brokerage) income analysis (actuals only), line grain, over lakehouse_mvpai.silver.fact_fynapse_slr_journals
  filtered to ACCOUNT 430000 (Commissions Income). All source systems (NOVIDEA, ACCRUAL). COMMISSION_INCOME_GBP = -REPORTING_AMOUNT
  and COMMISSION_INCOME_TXN = -TRANSACTION_AMOUNT (credits shown as positive income). COMPANY_CODE from CHILD_ENTITY, falling
  back to the legal entity default broker for accrual lines. Count transactions with DISTINCT SOURCE_TRANSACTION_ID.
grain: one row per Fynapse journal line for commission account 430000
primary_key:
- JOURNAL_LINE_ID
- SOURCE_TRANSACTION_ID
entity_column: LEGAL_ENTITY
period_columns:
- POSTING_DATE
- TRANSACTION_DATE
- FISCAL_YEAR
- PERIOD
- MONTH_YEAR
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

# vw_commission_analysis_slr_mga

Commission (brokerage) income analysis (actuals only), line grain, over lakehouse_mvpai.silver.fact_fynapse_slr_journals filtered to ACCOUNT 430000 (Commissions Income). All source systems (NOVIDEA, ACCRUAL). COMMISSION_INCOME_GBP = -REPORTING_AMOUNT and COMMISSION_INCOME_TXN = -TRANSACTION_AMOUNT (credits shown as positive income). COMPANY_CODE from CHILD_ENTITY, falling back to the legal entity default broker for accrual lines. Count transactions with DISTINCT SOURCE_TRANSACTION_ID.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `POSTING_DATE` | date |  |  | `POSTING_DATE` |
| `TRANSACTION_DATE` | date |  |  | `TRANSACTION_DATE` |
| `FISCAL_YEAR` | int |  |  | `FISCAL_YEAR` |
| `PERIOD` | int |  |  | `PERIOD` |
| `PERIOD_START_DATE` | date |  |  | `PERIOD_START_DATE` |
| `MONTH_NAME` | string |  |  | `MONTH_NAME` |
| `MONTH_YEAR` | string |  |  | `MONTH_YEAR` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `COMPANY_CODE` | string |  |  | `COMPANY_CODE` |
| `COMPANY_NAME` | string |  |  | `COMPANY_NAME` |
| `COMPANY_LABEL` | string |  |  | `COMPANY_LABEL` |
| `PROFIT_CENTER` | string |  |  | `PROFIT_CENTER` |
| `PROFIT_CENTER_NAME` | string |  |  | `PROFIT_CENTER_NAME` |
| `PROFIT_CENTER_LABEL` | string |  |  | `PROFIT_CENTER_LABEL` |
| `ACCOUNT` | string |  |  | `ACCOUNT` |
| `ACCOUNT_DESCRIPTION` | string |  |  | `ACCOUNT_DESCRIPTION` |
| `COMMISSION_INCOME_GBP` | decimal |  |  | `COMMISSION_INCOME_GBP` |
| `REPORTING_CURRENCY` | string |  |  | `REPORTING_CURRENCY` |
| `COMMISSION_INCOME_TXN` | decimal |  |  | `COMMISSION_INCOME_TXN` |
| `TRANSACTION_CURRENCY` | string |  |  | `TRANSACTION_CURRENCY` |
| `COMMISSION_INCOME_FUNCTIONAL` | decimal |  |  | `COMMISSION_INCOME_FUNCTIONAL` |
| `FUNCTIONAL_CURRENCY` | string |  |  | `FUNCTIONAL_CURRENCY` |
| `SOURCE_TRANSACTION_ID` | string |  |  | `SOURCE_TRANSACTION_ID` |
| `POLICY_REFERENCE` | string |  |  | `POLICY_REFERENCE` |
| `POLICY_NAME` | string |  |  | `POLICY_NAME` |
| `NOVIDEA_REFERENCE` | string |  |  | `NOVIDEA_REFERENCE` |
| `LINE_DESCRIPTION` | string |  |  | `LINE_DESCRIPTION` |
| `ENTRY_TYPE` | string |  |  | `ENTRY_TYPE` |
| `SOURCE_SYSTEM` | string |  |  | `SOURCE_SYSTEM` |
| `BUSINESS_EVENT` | string |  |  | `BUSINESS_EVENT` |
| `JOURNAL_TYPE` | string |  |  | `JOURNAL_TYPE` |
| `JOURNAL_ID` | string |  |  | `JOURNAL_ID` |
| `JOURNAL_LINE_ID` | string |  |  | `JOURNAL_LINE_ID` |
| `JOURNAL_LINE_NO` | int |  |  | `JOURNAL_LINE_NO` |

## Profile

Rows in the latest export: unknown.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `POSTING_DATE` | DATE |  |  |  |  |
| `TRANSACTION_DATE` | DATE |  |  |  |  |
| `FISCAL_YEAR` | INT |  |  |  |  |
| `PERIOD` | INT |  |  |  |  |
| `PERIOD_START_DATE` | DATE |  |  |  |  |
| `MONTH_NAME` | STRING |  |  |  |  |
| `MONTH_YEAR` | STRING |  |  |  |  |
| `LEGAL_ENTITY` | STRING |  |  |  |  |
| `COMPANY_CODE` | STRING |  |  |  |  |
| `COMPANY_NAME` | STRING |  |  |  |  |
| `COMPANY_LABEL` | STRING |  |  |  |  |
| `PROFIT_CENTER` | STRING |  |  |  |  |
| `PROFIT_CENTER_NAME` | STRING |  |  |  |  |
| `PROFIT_CENTER_LABEL` | STRING |  |  |  |  |
| `ACCOUNT` | STRING |  |  |  |  |
| `ACCOUNT_DESCRIPTION` | STRING |  |  |  |  |
| `COMMISSION_INCOME_GBP` | DECIMAL |  |  |  |  |
| `REPORTING_CURRENCY` | STRING |  |  |  |  |
| `COMMISSION_INCOME_TXN` | DECIMAL |  |  |  |  |
| `TRANSACTION_CURRENCY` | STRING |  |  |  |  |
| `COMMISSION_INCOME_FUNCTIONAL` | DECIMAL |  |  |  |  |
| `FUNCTIONAL_CURRENCY` | STRING |  |  |  |  |
| `SOURCE_TRANSACTION_ID` | STRING |  |  |  |  |
| `POLICY_REFERENCE` | STRING |  |  |  |  |
| `POLICY_NAME` | STRING |  |  |  |  |
| `NOVIDEA_REFERENCE` | STRING |  |  |  |  |
| `LINE_DESCRIPTION` | STRING |  |  |  |  |
| `ENTRY_TYPE` | STRING |  |  |  |  |
| `SOURCE_SYSTEM` | STRING |  |  |  |  |
| `BUSINESS_EVENT` | STRING |  |  |  |  |
| `JOURNAL_TYPE` | STRING |  |  |  |  |
| `JOURNAL_ID` | STRING |  |  |  |  |
| `JOURNAL_LINE_ID` | STRING |  |  |  |  |
| `JOURNAL_LINE_NO` | INT |  |  |  |  |
