---
name: vw_expense_analysis_gl
schema: gold
layer: gold
domain: gl
type: view
status: active
purpose: 'Monthly expense summary for Power BI expense analysis. Source: gold.vw_fact_kpmg_general_journals_entries filtered
  to 5-series (expense) main accounts, enriched with lakehouse_hsbc.mdm_ind_pc_insurance.coa_mdm hierarchy and silver.dim_companies
  entity names. Grain: month x entity x account x cost center x profit center x business indicator x LOB x journal category.
  Amounts in accounting currency, debit positive.'
grain: one row per month; entity; account; cost center; profit center; business indicator; LOB and journal category
primary_key:
- MONTH_START_DATE
- ENTITY_ID
- MAIN_ACCOUNT
- COST_CENTER
- PROFIT_CENTER
- BUSINESS_INDICATOR
- LOB
- JOURNAL_CATEGORY
entity_column: ENTITY_ID
period_columns:
- MONTH_START_DATE
- MONTH_END_DATE
- FISCAL_YEAR
- FISCAL_QUARTER
- FISCAL_MONTH
- YEAR_MONTH
pii_columns: []
synonyms: []
built_from:
- fact_kpmg_general_journal_account_entries
- dim_companies
- dim_main_accounts
known_issues: []
proposed_fields: []
reviewed: false
---

# vw_expense_analysis_gl

Monthly expense summary for Power BI expense analysis. Source: gold.vw_fact_kpmg_general_journals_entries filtered to 5-series (expense) main accounts, enriched with lakehouse_hsbc.mdm_ind_pc_insurance.coa_mdm hierarchy and silver.dim_companies entity names. Grain: month x entity x account x cost center x profit center x business indicator x LOB x journal category. Amounts in accounting currency, debit positive.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `MONTH_START_DATE` | date |  |  | `MONTH_START_DATE` |
| `MONTH_END_DATE` | date |  |  | `MONTH_END_DATE` |
| `FISCAL_YEAR` | int |  |  | `FISCAL_YEAR` |
| `FISCAL_QUARTER` | int |  |  | `FISCAL_QUARTER` |
| `FISCAL_MONTH` | int |  |  | `FISCAL_MONTH` |
| `YEAR_MONTH` | string |  |  | `YEAR_MONTH` |
| `ENTITY_ID` | string |  |  | `ENTITY_ID` |
| `ENTITY_NAME` | string |  |  | `ENTITY_NAME` |
| `MAIN_ACCOUNT` | string |  |  | `MAIN_ACCOUNT` |
| `ACCOUNT_NAME` | string |  |  | `ACCOUNT_NAME` |
| `IS_COA_MAPPED` | string |  |  | `IS_COA_MAPPED` |
| `STAT_OR_MGA` | string |  |  | `STAT_OR_MGA` |
| `EXPENSE_CATEGORY` | string |  |  | `EXPENSE_CATEGORY` |
| `EXPENSE_SUBCATEGORY` | string |  |  | `EXPENSE_SUBCATEGORY` |
| `EXPENSE_DETAIL_L4` | string |  |  | `EXPENSE_DETAIL_L4` |
| `EXPENSE_DETAIL_L5` | string |  |  | `EXPENSE_DETAIL_L5` |
| `EXPENSE_DETAIL_L6` | string |  |  | `EXPENSE_DETAIL_L6` |
| `COST_CENTER` | string |  |  | `COST_CENTER` |
| `PROFIT_CENTER` | string |  |  | `PROFIT_CENTER` |
| `BUSINESS_INDICATOR` | string |  |  | `BUSINESS_INDICATOR` |
| `LOB` | string |  |  | `LOB` |
| `JOURNAL_CATEGORY` | string |  |  | `JOURNAL_CATEGORY` |
| `CURRENCY_CODE` | string |  |  | `CURRENCY_CODE` |
| `EXPENSE_AMOUNT` | decimal |  |  | `EXPENSE_AMOUNT` |
| `DEBIT_AMOUNT` | decimal |  |  | `DEBIT_AMOUNT` |
| `CREDIT_AMOUNT` | decimal |  |  | `CREDIT_AMOUNT` |
| `LINE_COUNT` | long |  |  | `LINE_COUNT` |
| `VOUCHER_COUNT` | long |  |  | `VOUCHER_COUNT` |

## Values

**MONTH_START_DATE**
- `2024-12-01 00:00:00`
- `2025-11-01 00:00:00`
- `2025-03-01 00:00:00`
- `2025-02-01 00:00:00`
- `2025-01-01 00:00:00`
- `2025-04-01 00:00:00`
- `2026-09-01 00:00:00`
- `2026-08-01 00:00:00`
- `2025-12-01 00:00:00`
- `2025-08-01 00:00:00`
- `2025-09-01 00:00:00`
- `2026-02-01 00:00:00`
- `2026-04-01 00:00:00`
- `2026-01-01 00:00:00`
- `2025-10-01 00:00:00`
- `2025-07-01 00:00:00`
- `2026-05-01 00:00:00`
- `2026-03-01 00:00:00`
- `2026-06-01 00:00:00`
- `2025-06-01 00:00:00`
- `2026-07-01 00:00:00`
- `2025-05-01 00:00:00`
- `2026-11-01 00:00:00`
- `2026-10-01 00:00:00`

**MONTH_END_DATE**
- `2024-12-31 00:00:00`
- `2025-11-30 00:00:00`
- `2025-03-31 00:00:00`
- `2025-02-28 00:00:00`
- `2025-01-31 00:00:00`
- `2025-04-30 00:00:00`
- `2026-09-30 00:00:00`
- `2026-08-31 00:00:00`
- `2025-12-31 00:00:00`
- `2025-08-31 00:00:00`
- `2025-09-30 00:00:00`
- `2026-02-28 00:00:00`
- `2026-01-31 00:00:00`
- `2026-04-30 00:00:00`
- `2025-10-31 00:00:00`
- `2025-07-31 00:00:00`
- `2026-05-31 00:00:00`
- `2026-06-30 00:00:00`
- `2026-03-31 00:00:00`
- `2026-07-31 00:00:00`
- `2025-06-30 00:00:00`
- `2025-05-31 00:00:00`
- `2026-11-30 00:00:00`
- `2026-10-31 00:00:00`

**FISCAL_YEAR**
- `2025`
- `2024`
- `2026`

**FISCAL_QUARTER**
- `4`
- `1`
- `3`
- `2`

**FISCAL_MONTH**
- `12`
- `11`
- `2`
- `1`
- `3`
- `4`
- `9`
- `8`
- `7`
- `5`
- `6`
- `10`

**IS_COA_MAPPED**
- `Y`
- `N`

**STAT_OR_MGA**
- `MGA`
- `STAT`
- `Unmapped`

**EXPENSE_CATEGORY**
- `General and Administrative`
- `Underwriting expenses`
- `Loss and loss adjustment expenses`
- `Unmapped`
- `Underwriting expenses (Commissions)`
- `Other Expenses`
- `Investment expense`
- `Interest expense`
- `Provision for Federal Taxes`
- `Commissions Expense`

**EXPENSE_SUBCATEGORY**
- `Personnel expenses`
- `Marketing and travel expenses`
- `Commissions expense`
- `Office expenses`
- `Corporate expenses`
- `Other Underwriting Expenses`
- `Taxes, licenses, and fees`
- `Losses incurred`
- `Loss Adjustment Expense incurred`
- `Computer service expenses`
- `Unmapped`
- `Regular`
- `Management fees`
- `FX Gain/Loss`
- `STAT Exp Allocation`
- `Notes payable`
- `Investment Expense (Excl. Surplus Notes)`
- `Current`
- `Surplus Note Interest (STAT)`
- `Senior notes`

**EXPENSE_DETAIL_L6**
- `None`
- `Ground`
- `Travel`
- `Non Travel`
- `Air`
- `Profit`
- `Sliding Scale Commissions`
- `Mine Subsidence`
- `Brokerage Expense`

**PROFIT_CENTER**
- `Unassigned`
- `Health Insurance`
- `Personal`
- `Auto Insurance`
- `Life Insurance`
- `Property & Casualty Insurance`
- `Investment & Wealth Management`
- `Specialty`
- `Commercial`
- `0`
- `CAI`
- `MAR`

**LOB**
- `Unassigned`
- `Direct_Customer`
- `Broker`
- `Corporate`
- `0`
- `Individual`
- `Reinsurance`
- `10`
- `18`

**JOURNAL_CATEGORY**
- `GeneralJournal`
- `None`
- `Vend`
- `FixedAssets`
- `Allocation`

**CURRENCY_CODE**
- `USD`
- `GBP`
- `EUR`
- `CAD`
- `AUD`
- `SEK`
- `NOK`

**VOUCHER_COUNT**
- `1`
- `0`
- `2`
- `4`
- `3`
- `5`
- `6`
- `8`
- `7`
- `197`
- `9`
- `19`
- `10`
- `18`
- `15`
- `23`
- `16`
- `38`
- `25`
- `31`
- `22`
- `40`
- `12`
- `26`
- `13`
- `244`
- `191`
- `20`
- `196`
- `29`
- `63`
- `28`
- `39`
- `50`
- `164`
- `216`
- `200`
- `34`
- `54`
- `17`
- `274`
- `182`
- `46`
- `30`
- `189`
- `202`
