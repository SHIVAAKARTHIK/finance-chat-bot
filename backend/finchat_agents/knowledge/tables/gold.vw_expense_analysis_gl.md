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
row_count: 3952
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
- `2024-12-01 00:00:00`: 1430 rows
- `2025-11-01 00:00:00`: 567 rows
- `2025-03-01 00:00:00`: 195 rows
- `2025-02-01 00:00:00`: 194 rows
- `2025-01-01 00:00:00`: 188 rows
- `2025-04-01 00:00:00`: 185 rows
- `2026-09-01 00:00:00`: 142 rows
- `2026-08-01 00:00:00`: 97 rows
- `2025-12-01 00:00:00`: 86 rows
- `2025-08-01 00:00:00`: 81 rows
- `2025-09-01 00:00:00`: 77 rows
- `2026-02-01 00:00:00`: 74 rows
- `2026-04-01 00:00:00`: 71 rows
- `2026-01-01 00:00:00`: 71 rows
- `2025-10-01 00:00:00`: 67 rows
- `2025-07-01 00:00:00`: 66 rows
- `2026-05-01 00:00:00`: 65 rows
- `2026-03-01 00:00:00`: 61 rows
- `2026-06-01 00:00:00`: 61 rows
- `2025-06-01 00:00:00`: 57 rows
- `2026-07-01 00:00:00`: 57 rows
- `2025-05-01 00:00:00`: 54 rows
- `2026-11-01 00:00:00`: 4 rows
- `2026-10-01 00:00:00`: 2 rows

**MONTH_END_DATE**
- `2024-12-31 00:00:00`: 1430 rows
- `2025-11-30 00:00:00`: 567 rows
- `2025-03-31 00:00:00`: 195 rows
- `2025-02-28 00:00:00`: 194 rows
- `2025-01-31 00:00:00`: 188 rows
- `2025-04-30 00:00:00`: 185 rows
- `2026-09-30 00:00:00`: 142 rows
- `2026-08-31 00:00:00`: 97 rows
- `2025-12-31 00:00:00`: 86 rows
- `2025-08-31 00:00:00`: 81 rows
- `2025-09-30 00:00:00`: 77 rows
- `2026-02-28 00:00:00`: 74 rows
- `2026-01-31 00:00:00`: 71 rows
- `2026-04-30 00:00:00`: 71 rows
- `2025-10-31 00:00:00`: 67 rows
- `2025-07-31 00:00:00`: 66 rows
- `2026-05-31 00:00:00`: 65 rows
- `2026-06-30 00:00:00`: 61 rows
- `2026-03-31 00:00:00`: 61 rows
- `2026-07-31 00:00:00`: 57 rows
- `2025-06-30 00:00:00`: 57 rows
- `2025-05-31 00:00:00`: 54 rows
- `2026-11-30 00:00:00`: 4 rows
- `2026-10-31 00:00:00`: 2 rows

**FISCAL_YEAR**
- `2025`: 1817 rows
- `2024`: 1430 rows
- `2026`: 705 rows

**FISCAL_QUARTER**
- `4`: 2156 rows
- `1`: 783 rows
- `3`: 520 rows
- `2`: 493 rows

**FISCAL_MONTH**
- `12`: 1516 rows
- `11`: 571 rows
- `2`: 268 rows
- `1`: 259 rows
- `3`: 256 rows
- `4`: 256 rows
- `9`: 219 rows
- `8`: 178 rows
- `7`: 123 rows
- `5`: 119 rows
- `6`: 118 rows
- `10`: 69 rows

**IS_COA_MAPPED**
- `Y`: 3880 rows
- `N`: 72 rows

**STAT_OR_MGA**
- `MGA`: 2958 rows
- `STAT`: 922 rows
- `Unmapped`: 72 rows

**EXPENSE_CATEGORY**
- `General and Administrative`: 2547 rows
- `Underwriting expenses`: 904 rows
- `Loss and loss adjustment expenses`: 344 rows
- `Unmapped`: 72 rows
- `Underwriting expenses (Commissions)`: 61 rows
- `Other Expenses`: 8 rows
- `Investment expense`: 6 rows
- `Interest expense`: 5 rows
- `Provision for Federal Taxes`: 3 rows
- `Commissions Expense`: 2 rows

**EXPENSE_SUBCATEGORY**
- `Personnel expenses`: 1294 rows
- `Marketing and travel expenses`: 544 rows
- `Commissions expense`: 476 rows
- `Office expenses`: 327 rows
- `Corporate expenses`: 246 rows
- `Other Underwriting Expenses`: 217 rows
- `Taxes, licenses, and fees`: 185 rows
- `Losses incurred`: 173 rows
- `Loss Adjustment Expense incurred`: 171 rows
- `Computer service expenses`: 136 rows
- `Unmapped`: 72 rows
- `Regular`: 61 rows
- `Management fees`: 22 rows
- `FX Gain/Loss`: 8 rows
- `STAT Exp Allocation`: 6 rows
- `Notes payable`: 4 rows
- `Investment Expense (Excl. Surplus Notes)`: 4 rows
- `Current`: 3 rows
- `Surplus Note Interest (STAT)`: 2 rows
- `Senior notes`: 1 rows

**EXPENSE_DETAIL_L6**
- `None`: 3605 rows
- `Ground`: 118 rows
- `Travel`: 93 rows
- `Non Travel`: 70 rows
- `Air`: 59 rows
- `Profit`: 3 rows
- `Sliding Scale Commissions`: 2 rows
- `Mine Subsidence`: 1 rows
- `Brokerage Expense`: 1 rows

**PROFIT_CENTER**
- `Unassigned`: 2486 rows
- `Health Insurance`: 276 rows
- `Personal`: 271 rows
- `Auto Insurance`: 227 rows
- `Life Insurance`: 218 rows
- `Property & Casualty Insurance`: 216 rows
- `Investment & Wealth Management`: 106 rows
- `Specialty`: 57 rows
- `Commercial`: 55 rows
- `0`: 38 rows
- `CAI`: 1 rows
- `MAR`: 1 rows

**LOB**
- `Unassigned`: 2734 rows
- `Direct_Customer`: 360 rows
- `Broker`: 341 rows
- `Corporate`: 145 rows
- `0`: 118 rows
- `Individual`: 104 rows
- `Reinsurance`: 93 rows
- `10`: 56 rows
- `18`: 1 rows

**JOURNAL_CATEGORY**
- `GeneralJournal`: 3129 rows
- `None`: 744 rows
- `Vend`: 65 rows
- `FixedAssets`: 11 rows
- `Allocation`: 3 rows

**CURRENCY_CODE**
- `USD`: 3852 rows
- `GBP`: 70 rows
- `EUR`: 20 rows
- `CAD`: 5 rows
- `AUD`: 3 rows
- `SEK`: 1 rows
- `NOK`: 1 rows

**VOUCHER_COUNT**
- `1`: 2605 rows
- `0`: 743 rows
- `2`: 247 rows
- `4`: 117 rows
- `3`: 63 rows
- `5`: 53 rows
- `6`: 30 rows
- `8`: 13 rows
- `7`: 8 rows
- `197`: 8 rows
- `9`: 7 rows
- `19`: 5 rows
- `10`: 5 rows
- `18`: 4 rows
- `15`: 3 rows
- `23`: 2 rows
- `16`: 2 rows
- `38`: 2 rows
- `25`: 2 rows
- `31`: 2 rows
- `22`: 2 rows
- `40`: 2 rows
- `12`: 2 rows
- `26`: 2 rows
- `13`: 2 rows
- `244`: 1 rows
- `191`: 1 rows
- `20`: 1 rows
- `196`: 1 rows
- `29`: 1 rows
- `63`: 1 rows
- `28`: 1 rows
- `39`: 1 rows
- `50`: 1 rows
- `164`: 1 rows
- `216`: 1 rows
- `200`: 1 rows
- `34`: 1 rows
- `54`: 1 rows
- `17`: 1 rows
- `274`: 1 rows
- `182`: 1 rows
- `46`: 1 rows
- `30`: 1 rows
- `189`: 1 rows
- `202`: 1 rows

## Profile

Rows in the latest export: 3952.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `MONTH_START_DATE` | DATE | 25 | 0 | 2024-12-01 00:00:00 | 2026-11-01 00:00:00 |
| `MONTH_END_DATE` | DATE | 24 | 0 | 2024-12-31 00:00:00 | 2026-11-30 00:00:00 |
| `FISCAL_YEAR` | INT | 3 | 0 | 2024 | 2026 |
| `FISCAL_QUARTER` | INT | 4 | 0 | 1 | 4 |
| `FISCAL_MONTH` | INT | 12 | 0 | 1 | 12 |
| `YEAR_MONTH` | STRING | 22 | 0 |  |  |
| `ENTITY_ID` | STRING | 17 | 0 |  |  |
| `ENTITY_NAME` | STRING | 17 | 0 |  |  |
| `MAIN_ACCOUNT` | STRING | 106 | 0 | 511110 | 591000 |
| `ACCOUNT_NAME` | STRING | 123 | 0 | 401k Contribution | Utilities |
| `IS_COA_MAPPED` | STRING | 2 | 0 | N | Y |
| `STAT_OR_MGA` | STRING | 3 | 0 | MGA | Unmapped |
| `EXPENSE_CATEGORY` | STRING | 10 | 0 | Commissions Expense | Unmapped |
| `EXPENSE_SUBCATEGORY` | STRING | 20 | 0 | Commissions expense | Unmapped |
| `EXPENSE_DETAIL_L4` | STRING | 60 | 80 | Accumulated depreciation | Underwriting Expense |
| `EXPENSE_DETAIL_L5` | STRING | 55 | 1587 | 401k Contribution | Workers Comp |
| `EXPENSE_DETAIL_L6` | STRING | 8 | 3605 | Air | Travel |
| `COST_CENTER` | STRING | 92 | 0 | 0 | Wealth Advisory Services |
| `PROFIT_CENTER` | STRING | 12 | 0 | 0 | Unassigned |
| `BUSINESS_INDICATOR` | STRING | 114 | 0 | ---- | Up_sell |
| `LOB` | STRING | 9 | 0 | 0 | Unassigned |
| `JOURNAL_CATEGORY` | STRING | 5 | 0 | Allocation | Vend |
| `CURRENCY_CODE` | STRING | 7 | 0 | AUD | USD |
| `EXPENSE_AMOUNT` | DECIMAL | 3165 | 0 | -372053100.48 | 316580476 |
| `DEBIT_AMOUNT` | DECIMAL | 2646 | 0 | 0 | 523388273.95 |
| `CREDIT_AMOUNT` | DECIMAL | 639 | 0 | 0 | 523388273.95 |
| `LINE_COUNT` | LONG | 70 | 0 | 1 | 702 |
| `VOUCHER_COUNT` | LONG | 44 | 0 | 0 | 274 |

## Sample rows

| MONTH_START_DATE | MONTH_END_DATE | FISCAL_YEAR | FISCAL_QUARTER | FISCAL_MONTH | YEAR_MONTH | MAIN_ACCOUNT | ACCOUNT_NAME | IS_COA_MAPPED | STAT_OR_MGA | EXPENSE_CATEGORY | EXPENSE_SUBCATEGORY | EXPENSE_DETAIL_L4 | EXPENSE_DETAIL_L5 | EXPENSE_DETAIL_L6 | COST_CENTER | PROFIT_CENTER | BUSINESS_INDICATOR | LOB | JOURNAL_CATEGORY | CURRENCY_CODE | EXPENSE_AMOUNT | DEBIT_AMOUNT | CREDIT_AMOUNT | LINE_COUNT | VOUCHER_COUNT |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2025-01-01 00:00:00 | 2025-01-31 00:00:00 | 2025 | 1 | 1 | (altered in export) | 555300 | Contract Labor | Y | MGA | General and Administrative | Personnel expenses | Contract Labor | NULL | NULL | 811 | Unassigned | ---0000-- | Unassigned | GeneralJournal | USD | 859490.57 | 859490.57 | 0 | 106 | 1 |
| 2025-01-01 00:00:00 | 2025-01-31 00:00:00 | 2025 | 1 | 1 | (altered in export) | 555300 | Contract Labor | Y | MGA | General and Administrative | Personnel expenses | Contract Labor | NULL | NULL | 811 | Unassigned | ---CAT1-- | Unassigned | GeneralJournal | USD | 23952.5 | 23952.5 | 0 | 11 | 1 |
| 2025-01-01 00:00:00 | 2025-01-31 00:00:00 | 2025 | 1 | 1 | (altered in export) | 555300 | Contract Labor | Y | MGA | General and Administrative | Personnel expenses | Contract Labor | NULL | NULL | 811 | Unassigned | ---CAT8-- | Unassigned | GeneralJournal | USD | 562.5 | 562.5 | 0 | 1 | 1 |
| 2025-01-01 00:00:00 | 2025-01-31 00:00:00 | 2025 | 1 | 1 | (altered in export) | 555300 | Contract Labor | Y | MGA | General and Administrative | Personnel expenses | Contract Labor | NULL | NULL | 811 | Unassigned | ---CAT9-- | Unassigned | GeneralJournal | USD | 32368.13 | 32368.13 | 0 | 10 | 1 |
| 2025-01-01 00:00:00 | 2025-01-31 00:00:00 | 2025 | 1 | 1 | (altered in export) | 555300 | Contract Labor | Y | MGA | General and Administrative | Personnel expenses | Contract Labor | NULL | NULL | 811 | Unassigned | ---CT00-- | Unassigned | GeneralJournal | USD | 3495 | 3495 | 0 | 3 | 1 |
