---
name: vw_income_statement_logistics
schema: gold
layer: gold
domain: gl
type: view
status: active
purpose: Logistics income statement (P&L) at GL journal-line grain. 4xxxxx/5xxxxx accounts of logistics entities mapped to
  gold.dim_coa_logistics with a derived hierarchy, logistics IS lines (Revenue, Cost of Sales, Operating Expenses, Other Income/Expense),
  sort orders, KPI flags (Gross Profit, EBIT, EBITDA) and sign-normalised amounts. Built for Power BI.
grain: one row per logistics GL journal line
primary_key:
- ENTRY_REC_ID
entity_column: LEGAL_ENTITY_CODE
period_columns:
- ACCOUNTING_DATE
- FISCAL_YEAR
- FISCAL_QUARTER
- FISCAL_YEAR_QUARTER
- FISCAL_MONTH
- FISCAL_YEAR_MONTH
- FISCAL_PERIOD_KEY
- PERIOD_START_DATE
- PERIOD_END_DATE
pii_columns: []
synonyms: []
built_from:
- fact_kpmg_general_journal_account_entries
- dim_coa_logistics
known_issues: []
row_count: 0
proposed_fields: []
reviewed: false
---

# vw_income_statement_logistics

Logistics income statement (P&L) at GL journal-line grain. 4xxxxx/5xxxxx accounts of logistics entities mapped to gold.dim_coa_logistics with a derived hierarchy, logistics IS lines (Revenue, Cost of Sales, Operating Expenses, Other Income/Expense), sort orders, KPI flags (Gross Profit, EBIT, EBITDA) and sign-normalised amounts. Built for Power BI.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `ENTRY_REC_ID` | string |  |  | `ENTRY_REC_ID` |
| `LEGAL_ENTITY_CODE` | string |  |  | `LEGAL_ENTITY_CODE` |
| `LEGAL_ENTITY_NAME` | string |  |  | `LEGAL_ENTITY_NAME` |
| `INDUSTRY` | string |  |  | `INDUSTRY` |
| `LEDGER_NAME` | string |  |  | `LEDGER_NAME` |
| `POSTING_LAYER` | string |  |  | `POSTING_LAYER` |
| `ACCOUNTING_DATE` | date |  |  | `ACCOUNTING_DATE` |
| `FISCAL_YEAR` | int |  |  | `FISCAL_YEAR` |
| `FISCAL_QUARTER` | int |  |  | `FISCAL_QUARTER` |
| `FISCAL_YEAR_QUARTER` | string |  |  | `FISCAL_YEAR_QUARTER` |
| `FISCAL_MONTH` | int |  |  | `FISCAL_MONTH` |
| `FISCAL_MONTH_NAME` | string |  |  | `FISCAL_MONTH_NAME` |
| `FISCAL_YEAR_MONTH` | string |  |  | `FISCAL_YEAR_MONTH` |
| `FISCAL_PERIOD_KEY` | int |  |  | `FISCAL_PERIOD_KEY` |
| `PERIOD_START_DATE` | date |  |  | `PERIOD_START_DATE` |
| `PERIOD_END_DATE` | date |  |  | `PERIOD_END_DATE` |
| `DOCUMENT_DATE` | date |  |  | `DOCUMENT_DATE` |
| `AS_OF_DATE` | date |  |  | `AS_OF_DATE` |
| `RELATIVE_YEAR` | int |  |  | `RELATIVE_YEAR` |
| `YEAR_COMPARISON` | string |  |  | `YEAR_COMPARISON` |
| `IS_YTD_COMPARABLE` | boolean |  |  | `IS_YTD_COMPARABLE` |
| `IS_MTD_COMPARABLE` | boolean |  |  | `IS_MTD_COMPARABLE` |
| `MAIN_ACCOUNT` | int |  |  | `MAIN_ACCOUNT` |
| `ACCOUNT_NAME` | string |  |  | `ACCOUNT_NAME` |
| `ACCOUNT_DETAIL` | string |  |  | `ACCOUNT_DETAIL` |
| `ACCOUNT_LABEL` | string |  |  | `ACCOUNT_LABEL` |
| `COA_MAPPING_STATUS` | string |  |  | `COA_MAPPING_STATUS` |
| `COA_SOURCE` | string |  |  | `COA_SOURCE` |
| `COA_LEVEL_0` | string |  |  | `COA_LEVEL_0` |
| `COA_LEVEL_1` | string |  |  | `COA_LEVEL_1` |
| `COA_LEVEL_2` | string |  |  | `COA_LEVEL_2` |
| `COA_LEVEL_3` | string |  |  | `COA_LEVEL_3` |
| `COA_LEVEL_4` | string |  |  | `COA_LEVEL_4` |
| `IS_SECTION` | string |  |  | `IS_SECTION` |
| `IS_SECTION_SORT` | int |  |  | `IS_SECTION_SORT` |
| `IS_LINE` | string |  |  | `IS_LINE` |
| `IS_LINE_SORT` | int |  |  | `IS_LINE_SORT` |
| `IS_SUB_LINE` | string |  |  | `IS_SUB_LINE` |
| `KPI_COMPONENT` | string |  |  | `KPI_COMPONENT` |
| `IS_GROSS_PROFIT_ITEM` | boolean |  |  | `IS_GROSS_PROFIT_ITEM` |
| `IS_OPERATING_ITEM` | boolean |  |  | `IS_OPERATING_ITEM` |
| `IS_EBITDA_ITEM` | boolean |  |  | `IS_EBITDA_ITEM` |
| `IS_INTERCOMPANY` | boolean |  |  | `IS_INTERCOMPANY` |
| `DIMENSION_ENTITY` | string |  |  | `DIMENSION_ENTITY` |
| `REGION` | string |  |  | `REGION` |
| `BUSINESS_LINE` | string |  |  | `BUSINESS_LINE` |
| `FINANCIAL_DIMENSIONS` | string |  |  | `FINANCIAL_DIMENSIONS` |
| `LEDGER_ACCOUNT` | string |  |  | `LEDGER_ACCOUNT` |
| `JOURNAL_NUMBER` | string |  |  | `JOURNAL_NUMBER` |
| `VOUCHER` | string |  |  | `VOUCHER` |
| `DOCUMENT_NUMBER` | string |  |  | `DOCUMENT_NUMBER` |
| `LINE_DESCRIPTION` | string |  |  | `LINE_DESCRIPTION` |
| `JOURNAL_CATEGORY` | string |  |  | `JOURNAL_CATEGORY` |
| `POSTING_TYPE` | string |  |  | `POSTING_TYPE` |
| `IS_CREDIT` | string |  |  | `IS_CREDIT` |
| `IS_CORRECTION` | string |  |  | `IS_CORRECTION` |
| `TRANSACTION_CURRENCY_CODE` | string |  |  | `TRANSACTION_CURRENCY_CODE` |
| `GL_AMOUNT` | decimal |  |  | `GL_AMOUNT` |
| `PL_AMOUNT` | decimal |  |  | `PL_AMOUNT` |
| `REPORT_AMOUNT` | decimal |  |  | `REPORT_AMOUNT` |
| `DEBIT_AMOUNT` | decimal |  |  | `DEBIT_AMOUNT` |
| `CREDIT_AMOUNT` | decimal |  |  | `CREDIT_AMOUNT` |
| `CY_PL_AMOUNT` | decimal |  |  | `CY_PL_AMOUNT` |
| `PY_PL_AMOUNT` | decimal |  |  | `PY_PL_AMOUNT` |
| `PL_AMOUNT_REPORTING_CCY` | decimal |  |  | `PL_AMOUNT_REPORTING_CCY` |
| `REPORTING_CURRENCY_AMOUNT` | decimal |  |  | `REPORTING_CURRENCY_AMOUNT` |
| `TRANSACTION_CURRENCY_AMOUNT` | decimal |  |  | `TRANSACTION_CURRENCY_AMOUNT` |
| `QUANTITY` | decimal |  |  | `QUANTITY` |
| `LAST_REFRESHED` | timestamp |  |  | `LAST_REFRESHED` |

## Profile

Rows in the latest export: 0.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `ENTRY_REC_ID` | STRING | 0 | 0 |  |  |
| `LEGAL_ENTITY_CODE` | STRING | 0 | 0 |  |  |
| `LEGAL_ENTITY_NAME` | STRING | 0 | 0 |  |  |
| `INDUSTRY` | STRING | 0 | 0 |  |  |
| `LEDGER_NAME` | STRING | 0 | 0 |  |  |
| `POSTING_LAYER` | STRING | 0 | 0 |  |  |
| `ACCOUNTING_DATE` | DATE | 0 | 0 |  |  |
| `FISCAL_YEAR` | INT | 0 | 0 |  |  |
| `FISCAL_QUARTER` | INT | 0 | 0 |  |  |
| `FISCAL_YEAR_QUARTER` | STRING | 0 | 0 |  |  |
| `FISCAL_MONTH` | INT | 0 | 0 |  |  |
| `FISCAL_MONTH_NAME` | STRING | 0 | 0 |  |  |
| `FISCAL_YEAR_MONTH` | STRING | 0 | 0 |  |  |
| `FISCAL_PERIOD_KEY` | INT | 0 | 0 |  |  |
| `PERIOD_START_DATE` | DATE | 0 | 0 |  |  |
| `PERIOD_END_DATE` | DATE | 0 | 0 |  |  |
| `DOCUMENT_DATE` | DATE | 0 | 0 |  |  |
| `AS_OF_DATE` | DATE | 0 | 0 |  |  |
| `RELATIVE_YEAR` | INT | 0 | 0 |  |  |
| `YEAR_COMPARISON` | STRING | 0 | 0 |  |  |
| `IS_YTD_COMPARABLE` | BOOLEAN | 0 | 0 |  |  |
| `IS_MTD_COMPARABLE` | BOOLEAN | 0 | 0 |  |  |
| `MAIN_ACCOUNT` | INT | 0 | 0 |  |  |
| `ACCOUNT_NAME` | STRING | 0 | 0 |  |  |
| `ACCOUNT_DETAIL` | STRING | 0 | 0 |  |  |
| `ACCOUNT_LABEL` | STRING | 0 | 0 |  |  |
| `COA_MAPPING_STATUS` | STRING | 0 | 0 |  |  |
| `COA_SOURCE` | STRING | 0 | 0 |  |  |
| `COA_LEVEL_0` | STRING | 0 | 0 |  |  |
| `COA_LEVEL_1` | STRING | 0 | 0 |  |  |
| `COA_LEVEL_2` | STRING | 0 | 0 |  |  |
| `COA_LEVEL_3` | STRING | 0 | 0 |  |  |
| `COA_LEVEL_4` | STRING | 0 | 0 |  |  |
| `IS_SECTION` | STRING | 0 | 0 |  |  |
| `IS_SECTION_SORT` | INT | 0 | 0 |  |  |
| `IS_LINE` | STRING | 0 | 0 |  |  |
| `IS_LINE_SORT` | INT | 0 | 0 |  |  |
| `IS_SUB_LINE` | STRING | 0 | 0 |  |  |
| `KPI_COMPONENT` | STRING | 0 | 0 |  |  |
| `IS_GROSS_PROFIT_ITEM` | BOOLEAN | 0 | 0 |  |  |
| `IS_OPERATING_ITEM` | BOOLEAN | 0 | 0 |  |  |
| `IS_EBITDA_ITEM` | BOOLEAN | 0 | 0 |  |  |
| `IS_INTERCOMPANY` | BOOLEAN | 0 | 0 |  |  |
| `DIMENSION_ENTITY` | STRING | 0 | 0 |  |  |
| `REGION` | STRING | 0 | 0 |  |  |
| `BUSINESS_LINE` | STRING | 0 | 0 |  |  |
| `FINANCIAL_DIMENSIONS` | STRING | 0 | 0 |  |  |
| `LEDGER_ACCOUNT` | STRING | 0 | 0 |  |  |
| `JOURNAL_NUMBER` | STRING | 0 | 0 |  |  |
| `VOUCHER` | STRING | 0 | 0 |  |  |
| `DOCUMENT_NUMBER` | STRING | 0 | 0 |  |  |
| `LINE_DESCRIPTION` | STRING | 0 | 0 |  |  |
| `JOURNAL_CATEGORY` | STRING | 0 | 0 |  |  |
| `POSTING_TYPE` | STRING | 0 | 0 |  |  |
| `IS_CREDIT` | STRING | 0 | 0 |  |  |
| `IS_CORRECTION` | STRING | 0 | 0 |  |  |
| `TRANSACTION_CURRENCY_CODE` | STRING | 0 | 0 |  |  |
| `GL_AMOUNT` | DECIMAL | 0 | 0 |  |  |
| `PL_AMOUNT` | DECIMAL | 0 | 0 |  |  |
| `REPORT_AMOUNT` | DECIMAL | 0 | 0 |  |  |
| `DEBIT_AMOUNT` | DECIMAL | 0 | 0 |  |  |
| `CREDIT_AMOUNT` | DECIMAL | 0 | 0 |  |  |
| `CY_PL_AMOUNT` | DECIMAL | 0 | 0 |  |  |
| `PY_PL_AMOUNT` | DECIMAL | 0 | 0 |  |  |
| `PL_AMOUNT_REPORTING_CCY` | DECIMAL | 0 | 0 |  |  |
| `REPORTING_CURRENCY_AMOUNT` | DECIMAL | 0 | 0 |  |  |
| `TRANSACTION_CURRENCY_AMOUNT` | DECIMAL | 0 | 0 |  |  |
| `QUANTITY` | DECIMAL | 0 | 0 |  |  |
| `LAST_REFRESHED` | TIMESTAMP | 0 | 0 |  |  |
