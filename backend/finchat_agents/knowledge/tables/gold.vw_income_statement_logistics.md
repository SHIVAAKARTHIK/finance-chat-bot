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

## Empty columns

Empty in every row: `ENTRY_REC_ID`, `LEGAL_ENTITY_CODE`, `LEGAL_ENTITY_NAME`, `INDUSTRY`, `LEDGER_NAME`, `POSTING_LAYER`, `ACCOUNTING_DATE`, `FISCAL_YEAR`, `FISCAL_QUARTER`, `FISCAL_YEAR_QUARTER`, `FISCAL_MONTH`, `FISCAL_MONTH_NAME`, `FISCAL_YEAR_MONTH`, `FISCAL_PERIOD_KEY`, `PERIOD_START_DATE`, `PERIOD_END_DATE`, `DOCUMENT_DATE`, `AS_OF_DATE`, `RELATIVE_YEAR`, `YEAR_COMPARISON`, `IS_YTD_COMPARABLE`, `IS_MTD_COMPARABLE`, `MAIN_ACCOUNT`, `ACCOUNT_NAME`, `ACCOUNT_DETAIL`, `ACCOUNT_LABEL`, `COA_MAPPING_STATUS`, `COA_SOURCE`, `COA_LEVEL_0`, `COA_LEVEL_1`, `COA_LEVEL_2`, `COA_LEVEL_3`, `COA_LEVEL_4`, `IS_SECTION`, `IS_SECTION_SORT`, `IS_LINE`, `IS_LINE_SORT`, `IS_SUB_LINE`, `KPI_COMPONENT`, `IS_GROSS_PROFIT_ITEM`, `IS_OPERATING_ITEM`, `IS_EBITDA_ITEM`, `IS_INTERCOMPANY`, `DIMENSION_ENTITY`, `REGION`, `BUSINESS_LINE`, `FINANCIAL_DIMENSIONS`, `LEDGER_ACCOUNT`, `JOURNAL_NUMBER`, `VOUCHER`, `DOCUMENT_NUMBER`, `LINE_DESCRIPTION`, `JOURNAL_CATEGORY`, `POSTING_TYPE`, `IS_CREDIT`, `IS_CORRECTION`, `TRANSACTION_CURRENCY_CODE`, `GL_AMOUNT`, `PL_AMOUNT`, `REPORT_AMOUNT`, `DEBIT_AMOUNT`, `CREDIT_AMOUNT`, `CY_PL_AMOUNT`, `PY_PL_AMOUNT`, `PL_AMOUNT_REPORTING_CCY`, `REPORTING_CURRENCY_AMOUNT`, `TRANSACTION_CURRENCY_AMOUNT`, `QUANTITY`, `LAST_REFRESHED`. Do not filter or group on them.
