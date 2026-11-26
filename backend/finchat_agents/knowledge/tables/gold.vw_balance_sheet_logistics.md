---
name: vw_balance_sheet_logistics
schema: gold
layer: gold
domain: gl
type: view
status: active
purpose: Logistics balance sheet at month-end snapshot grain (entity x account x region x business line). Cumulative GL balances
  mapped to gold.dim_coa_logistics (Assets / Liabilities / Equity, current vs non-current, BS lines and sort orders). P&L
  is rolled into Current Year Earnings and Retained Earnings so the balance sheet balances. Built for Power BI.
grain: one row per entity; account; month-end; region and business line
primary_key:
- LEGAL_ENTITY_CODE
- MAIN_ACCOUNT
- PERIOD_END_DATE
- REGION
- BUSINESS_LINE
entity_column: LEGAL_ENTITY_CODE
period_columns:
- PERIOD_END_DATE
- FISCAL_YEAR
- FISCAL_QUARTER
- FISCAL_MONTH
- FISCAL_YEAR_MONTH
pii_columns: []
synonyms: []
built_from:
- fact_kpmg_general_journal_account_entries
- dim_coa_logistics
known_issues: []
proposed_fields: []
reviewed: false
---

# vw_balance_sheet_logistics

Logistics balance sheet at month-end snapshot grain (entity x account x region x business line). Cumulative GL balances mapped to gold.dim_coa_logistics (Assets / Liabilities / Equity, current vs non-current, BS lines and sort orders). P&L is rolled into Current Year Earnings and Retained Earnings so the balance sheet balances. Built for Power BI.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `PERIOD_END_DATE` | date |  |  | `PERIOD_END_DATE` |
| `FISCAL_YEAR` | int |  |  | `FISCAL_YEAR` |
| `FISCAL_QUARTER` | int |  |  | `FISCAL_QUARTER` |
| `FISCAL_MONTH` | int |  |  | `FISCAL_MONTH` |
| `FISCAL_MONTH_NAME` | string |  |  | `FISCAL_MONTH_NAME` |
| `FISCAL_YEAR_MONTH` | string |  |  | `FISCAL_YEAR_MONTH` |
| `FISCAL_PERIOD_KEY` | int |  |  | `FISCAL_PERIOD_KEY` |
| `AS_OF_DATE` | date |  |  | `AS_OF_DATE` |
| `IS_LATEST_PERIOD` | boolean |  |  | `IS_LATEST_PERIOD` |
| `IS_YEAR_END` | boolean |  |  | `IS_YEAR_END` |
| `RELATIVE_YEAR` | int |  |  | `RELATIVE_YEAR` |
| `LEGAL_ENTITY_CODE` | string |  |  | `LEGAL_ENTITY_CODE` |
| `LEGAL_ENTITY_NAME` | string |  |  | `LEGAL_ENTITY_NAME` |
| `INDUSTRY` | string |  |  | `INDUSTRY` |
| `MAIN_ACCOUNT` | int |  |  | `MAIN_ACCOUNT` |
| `ACCOUNT_NAME` | string |  |  | `ACCOUNT_NAME` |
| `ACCOUNT_LABEL` | string |  |  | `ACCOUNT_LABEL` |
| `COA_MAPPING_STATUS` | string |  |  | `COA_MAPPING_STATUS` |
| `COA_LEVEL_0` | string |  |  | `COA_LEVEL_0` |
| `COA_LEVEL_1` | string |  |  | `COA_LEVEL_1` |
| `COA_LEVEL_2` | string |  |  | `COA_LEVEL_2` |
| `IS_PL_ROLLFORWARD` | boolean |  |  | `IS_PL_ROLLFORWARD` |
| `BS_CLASS` | string |  |  | `BS_CLASS` |
| `BS_CLASS_SORT` | int |  |  | `BS_CLASS_SORT` |
| `BS_SECTION` | string |  |  | `BS_SECTION` |
| `BS_SECTION_SORT` | int |  |  | `BS_SECTION_SORT` |
| `BS_LINE` | string |  |  | `BS_LINE` |
| `BS_LINE_SORT` | int |  |  | `BS_LINE_SORT` |
| `REGION` | string |  |  | `REGION` |
| `BUSINESS_LINE` | string |  |  | `BUSINESS_LINE` |
| `CLOSING_BALANCE_GL` | decimal |  |  | `CLOSING_BALANCE_GL` |
| `BALANCE` | decimal |  |  | `BALANCE` |
| `PERIOD_MOVEMENT_GL` | decimal |  |  | `PERIOD_MOVEMENT_GL` |
| `PERIOD_MOVEMENT` | decimal |  |  | `PERIOD_MOVEMENT` |

## Empty columns

Empty in every row: `PERIOD_END_DATE`, `FISCAL_YEAR`, `FISCAL_QUARTER`, `FISCAL_MONTH`, `FISCAL_MONTH_NAME`, `FISCAL_YEAR_MONTH`, `FISCAL_PERIOD_KEY`, `AS_OF_DATE`, `IS_LATEST_PERIOD`, `IS_YEAR_END`, `RELATIVE_YEAR`, `LEGAL_ENTITY_CODE`, `LEGAL_ENTITY_NAME`, `INDUSTRY`, `MAIN_ACCOUNT`, `ACCOUNT_NAME`, `ACCOUNT_LABEL`, `COA_MAPPING_STATUS`, `COA_LEVEL_0`, `COA_LEVEL_1`, `COA_LEVEL_2`, `IS_PL_ROLLFORWARD`, `BS_CLASS`, `BS_CLASS_SORT`, `BS_SECTION`, `BS_SECTION_SORT`, `BS_LINE`, `BS_LINE_SORT`, `REGION`, `BUSINESS_LINE`, `CLOSING_BALANCE_GL`, `BALANCE`, `PERIOD_MOVEMENT_GL`, `PERIOD_MOVEMENT`. Do not filter or group on them.
