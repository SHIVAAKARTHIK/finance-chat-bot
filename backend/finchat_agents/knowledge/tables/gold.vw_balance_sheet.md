---
name: vw_balance_sheet
schema: gold
layer: gold
domain: gl
type: view
status: active
purpose: 'Balance sheet fact for Power BI. Grain: entity x account x accounting date x dimensions x transaction currency x
  RE_BUCKET. BS accounts (COA level_0 = Balance Sheet) carry cumulative balances; P&L accounts (4/5/6-series, COA level_0
  = Income Statement, plus any 6-series account even if unmapped) are rolled into Equity > Retained Earnings twice (RE_BUCKET
  CY / PY) so DAX can split current-year earnings from prior-year unclosed earnings. 9-series memo accounts excluded. GL_AMOUNT/BS_AMOUNT
  are in accounting currency; GL_TC_AMOUNT/BS_TC_AMOUNT are in TRANSACTION_CURRENCY (only additive within a single currency).
  COA: lakehouse_hsbc.mdm_ind_pc_insurance.coa_mdm. Sort keys are 1:1 with level names (Power BI Sort by Column safe).'
grain: one row per entity; account; accounting date; dimensions; currency and retained-earnings bucket
primary_key:
- ENTITY_ID
- MAIN_ACCOUNT
- ACCOUNTING_DATE
- RE_BUCKET
- TRANSACTION_CURRENCY
- COST_CENTER
- PROFIT_CENTER
- LOB
- BUSINESS_INDICATOR
- INTERCOMPANY
entity_column: ENTITY_ID
period_columns:
- ACCOUNTING_DATE
- FISCAL_YEAR
- FISCAL_MONTH
pii_columns: []
synonyms: []
built_from:
- fact_kpmg_general_journal_account_entries
- dim_main_accounts
- dim_ledger_bi_entities
known_issues: []
row_count: 20931
proposed_fields: []
reviewed: false
---

# vw_balance_sheet

Balance sheet fact for Power BI. Grain: entity x account x accounting date x dimensions x transaction currency x RE_BUCKET. BS accounts (COA level_0 = Balance Sheet) carry cumulative balances; P&L accounts (4/5/6-series, COA level_0 = Income Statement, plus any 6-series account even if unmapped) are rolled into Equity > Retained Earnings twice (RE_BUCKET CY / PY) so DAX can split current-year earnings from prior-year unclosed earnings. 9-series memo accounts excluded. GL_AMOUNT/BS_AMOUNT are in accounting currency; GL_TC_AMOUNT/BS_TC_AMOUNT are in TRANSACTION_CURRENCY (only additive within a single currency). COA: lakehouse_hsbc.mdm_ind_pc_insurance.coa_mdm. Sort keys are 1:1 with level names (Power BI Sort by Column safe).

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `RE_BUCKET` | string |  |  | `RE_BUCKET` |
| `BS_LEVEL_1` | string |  |  | `BS_LEVEL_1` |
| `BS_LEVEL_2` | string |  |  | `BS_LEVEL_2` |
| `BS_LEVEL_3` | string |  |  | `BS_LEVEL_3` |
| `BS_LEVEL_1_SORT` | int |  |  | `BS_LEVEL_1_SORT` |
| `BS_LEVEL_2_SORT` | long |  |  | `BS_LEVEL_2_SORT` |
| `BS_LEVEL_3_SORT` | long |  |  | `BS_LEVEL_3_SORT` |
| `BS_SIDE` | string |  |  | `BS_SIDE` |
| `ENTITY_ID` | string |  |  | `ENTITY_ID` |
| `MAIN_ACCOUNT` | string |  |  | `MAIN_ACCOUNT` |
| `ACCOUNT_NAME` | string |  |  | `ACCOUNT_NAME` |
| `COA_MAPPING_STATUS` | string |  |  | `COA_MAPPING_STATUS` |
| `STAT_OR_MGA` | string |  |  | `STAT_OR_MGA` |
| `SOURCE_LEVEL_0` | string |  |  | `SOURCE_LEVEL_0` |
| `SOURCE_LEVEL_1` | string |  |  | `SOURCE_LEVEL_1` |
| `ACCOUNTING_DATE` | date |  |  | `ACCOUNTING_DATE` |
| `FISCAL_YEAR` | int |  |  | `FISCAL_YEAR` |
| `FISCAL_MONTH` | int |  |  | `FISCAL_MONTH` |
| `POSTING_LAYER` | string |  |  | `POSTING_LAYER` |
| `PROFIT_CENTER` | string |  |  | `PROFIT_CENTER` |
| `COST_CENTER` | string |  |  | `COST_CENTER` |
| `LOB` | string |  |  | `LOB` |
| `BUSINESS_INDICATOR` | string |  |  | `BUSINESS_INDICATOR` |
| `INTERCOMPANY` | string |  |  | `INTERCOMPANY` |
| `TRANSACTION_CURRENCY` | string |  |  | `TRANSACTION_CURRENCY` |
| `GL_AMOUNT` | decimal |  |  | `GL_AMOUNT` |
| `BS_AMOUNT` | decimal |  |  | `BS_AMOUNT` |
| `GL_TC_AMOUNT` | decimal |  |  | `GL_TC_AMOUNT` |
| `BS_TC_AMOUNT` | decimal |  |  | `BS_TC_AMOUNT` |

## Values

**RE_BUCKET**
- `BS`: 7475 rows
- `PY`: 6728 rows
- `CY`: 6728 rows

**BS_LEVEL_1**
- `Equity`: 13858 rows
- `Asset`: 4842 rows
- `Liability`: 2231 rows

**BS_LEVEL_2**
- `Retained Earnings`: 13835 rows
- `Receivables and Recoverables`: 1993 rows
- `Cash Equivalents`: 1967 rows
- `Operational Liabilities`: 1343 rows
- `Underwriting Liabilities`: 454 rows
- `Insurance Policy Liabilities`: 398 rows
- `Other assets`: 314 rows
- `Property and Equipment`: 221 rows
- `Invested Assets`: 194 rows
- `Short Term Investments`: 82 rows
- `Other Assets`: 55 rows
- `Financing and Debt`: 27 rows
- `Additional paid in capital`: 16 rows
- `Federal Tax Assets`: 14 rows
- `Company Stock`: 7 rows
- `Other Liabilities`: 3 rows
- `Federal Tax Liabilities`: 3 rows
- `Outstanding loss and loss adjustment expense (Loss Adjustment Expense outstanding)`: 3 rows
- `Capital Assets`: 2 rows

**BS_LEVEL_1_SORT**
- `3`: 13858 rows
- `1`: 4842 rows
- `2`: 2231 rows

**BS_LEVEL_2_SORT**
- `330000`: 13835 rows
- `141000`: 1993 rows
- `100004`: 1967 rows
- `229110`: 1343 rows
- `221000`: 454 rows
- `211111`: 398 rows
- `191100`: 314 rows
- `161100`: 221 rows
- `131100`: 194 rows
- `121100`: 82 rows
- `176100`: 55 rows
- `241201`: 27 rows
- `320000`: 16 rows
- `151100`: 14 rows
- `310100`: 7 rows
- `251000`: 3 rows
- `291000`: 3 rows
- `211212`: 3 rows
- `171000`: 2 rows

**BS_SIDE**
- `Liabilities & Equity`: 16089 rows
- `Assets`: 4842 rows

**COA_MAPPING_STATUS**
- `Mapped`: 20075 rows
- `Inherited (4-digit prefix)`: 856 rows

**STAT_OR_MGA**
- `MGA`: 15558 rows
- `STAT`: 5373 rows

**SOURCE_LEVEL_0**
- `Income Statement`: 13456 rows
- `Balance Sheet`: 7475 rows

**SOURCE_LEVEL_1**
- `Expense`: 9466 rows
- `Asset`: 4842 rows
- `Revenue`: 3990 rows
- `Liability`: 2231 rows
- `Equity`: 402 rows

**FISCAL_YEAR**
- `2025`: 10003 rows
- `2026`: 7033 rows
- `2024`: 3895 rows

**FISCAL_MONTH**
- `12`: 4753 rows
- `1`: 2921 rows
- `11`: 1914 rows
- `4`: 1604 rows
- `3`: 1597 rows
- `2`: 1576 rows
- `9`: 1470 rows
- `8`: 1373 rows
- `7`: 1010 rows
- `6`: 1006 rows
- `5`: 975 rows
- `10`: 732 rows

**POSTING_LAYER**
- `Current`: 20614 rows
- `Operations`: 317 rows

**PROFIT_CENTER**
- `None`: 12244 rows
- `Personal`: 2416 rows
- `Health Insurance`: 1314 rows
- `Property & Casualty Insurance`: 1005 rows
- `Specialty`: 1002 rows
- `Auto Insurance`: 1000 rows
- `Life Insurance`: 901 rows
- `Commercial`: 394 rows
- `Investment & Wealth Management`: 303 rows
- `0`: 182 rows
- `MAR`: 27 rows
- `CAI`: 25 rows
- `SLM`: 22 rows
- `SLA`: 22 rows
- `FLI`: 20 rows
- `SLO`: 14 rows
- `FLM`: 12 rows
- `PRI`: 10 rows
- `PRN`: 8 rows
- `SLP`: 4 rows
- `TRP`: 4 rows
- `FLN`: 2 rows

**LOB**
- `None`: 15179 rows
- `Direct_Customer`: 1907 rows
- `Broker`: 1407 rows
- `0`: 773 rows
- `Corporate`: 654 rows
- `10`: 454 rows
- `Individual`: 301 rows
- `Reinsurance`: 254 rows
- `18`: 2 rows

**TRANSACTION_CURRENCY**
- `USD`: 20433 rows
- `GBP`: 309 rows
- `EUR`: 107 rows
- `CAD`: 43 rows
- `SEK`: 16 rows
- `AUD`: 15 rows
- `ZAR`: 4 rows
- `NOK`: 4 rows

## Profile

Rows in the latest export: 20931.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `RE_BUCKET` | STRING | 3 | 0 | BS | PY |
| `BS_LEVEL_1` | STRING | 3 | 0 | Asset | Liability |
| `BS_LEVEL_2` | STRING | 19 | 0 | Additional paid in capital | Underwriting Liabilities |
| `BS_LEVEL_3` | STRING | 74 | 0 | Accounts payable - insurance companies | Unrealized Gains (Losses) |
| `BS_LEVEL_1_SORT` | INT | 3 | 0 | 1 | 3 |
| `BS_LEVEL_2_SORT` | LONG | 19 | 0 | 100004 | 330000 |
| `BS_LEVEL_3_SORT` | LONG | 73 | 0 | 100004 | 339999 |
| `BS_SIDE` | STRING | 2 | 0 | Assets | Liabilities & Equity |
| `ENTITY_ID` | STRING | 18 | 0 |  |  |
| `MAIN_ACCOUNT` | STRING | 435 | 0 | 101100 | 650200 |
| `ACCOUNT_NAME` | STRING | 369 | 0 | 401k Contribution | Written Premium - Direct |
| `COA_MAPPING_STATUS` | STRING | 2 | 0 | Inherited (4-digit prefix) | Mapped |
| `STAT_OR_MGA` | STRING | 2 | 0 | MGA | STAT |
| `SOURCE_LEVEL_0` | STRING | 2 | 0 | Balance Sheet | Income Statement |
| `SOURCE_LEVEL_1` | STRING | 5 | 0 | Asset | Revenue |
| `ACCOUNTING_DATE` | DATE | 410 | 0 | 2024-12-31 00:00:00 | 2026-11-02 00:00:00 |
| `FISCAL_YEAR` | INT | 3 | 0 | 2024 | 2026 |
| `FISCAL_MONTH` | INT | 12 | 0 | 1 | 12 |
| `POSTING_LAYER` | STRING | 2 | 0 | Current | Operations |
| `PROFIT_CENTER` | STRING | 21 | 12244 | 0 | TRP |
| `COST_CENTER` | STRING | 97 | 7891 | 0 | Wealth Advisory Services |
| `LOB` | STRING | 8 | 15179 | 0 | Reinsurance |
| `BUSINESS_INDICATOR` | STRING | 180 | 1915 | ---- | Up_sell |
| `INTERCOMPANY` | STRING | 2 | 19103 |  |  |
| `TRANSACTION_CURRENCY` | STRING | 7 | 0 | AUD | ZAR |
| `GL_AMOUNT` | DECIMAL | 10082 | 0 | -745479757.25 | 640782957.75 |
| `BS_AMOUNT` | DECIMAL | 9292 | 0 | -617867698.63 | 745479757.25 |
| `GL_TC_AMOUNT` | DECIMAL | 9987 | 0 | -745479757.25 | 640782957.75 |
| `BS_TC_AMOUNT` | DECIMAL | 9146 | 0 | -617867698.63 | 745479757.25 |

## Sample rows

| RE_BUCKET | BS_LEVEL_1 | BS_LEVEL_2 | BS_LEVEL_3 | BS_LEVEL_1_SORT | BS_LEVEL_2_SORT | BS_LEVEL_3_SORT | BS_SIDE | MAIN_ACCOUNT | ACCOUNT_NAME | COA_MAPPING_STATUS | STAT_OR_MGA | SOURCE_LEVEL_0 | SOURCE_LEVEL_1 | ACCOUNTING_DATE | FISCAL_YEAR | FISCAL_MONTH | POSTING_LAYER | PROFIT_CENTER | COST_CENTER | LOB | BUSINESS_INDICATOR | TRANSACTION_CURRENCY | GL_AMOUNT | BS_AMOUNT | GL_TC_AMOUNT | BS_TC_AMOUNT |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BS | Asset | Other assets | Intangible Assets | 1 | 191100 | 194200 | Assets | 194220 | Renewal right assets - Non - Admitted | Mapped | STAT | Balance Sheet | Asset | 2024-12-31 00:00:00 | 2024 | 12 | Operations | NULL | NULL | NULL | ----- | USD | -1500000 | -1500000 | -1500000 | -1500000 |
| BS | Equity | Retained Earnings | Dividends | 3 | 330000 | 334000 | Liabilities & Equity | 334000 | Dividends to Parent | Mapped | STAT | Balance Sheet | Equity | 2024-12-31 00:00:00 | 2024 | 12 | Current | NULL | NULL | NULL | ----- | USD | 25625000 | -25625000 | 25625000 | -25625000 |
| BS | Asset | Receivables and Recoverables | Intercompany | 1 | 141000 | 146100 | Assets | 146420 | Intercompany - Loans Receivable - Int... | Mapped | MGA | Balance Sheet | Asset | 2025-11-02 00:00:00 | 2025 | 11 | Current | Investment & Wealth Management | Finance | Direct_Customer | Policy Renewal | USD | 1628.76 | 1628.76 | 1628.76 | 1628.76 |
| BS | Asset | Property and Equipment | Building and Improvements | 1 | 161100 | 161100 | Assets | 161200 | Building Improvements | Mapped | MGA | Balance Sheet | Asset | 2025-11-02 00:00:00 | 2025 | 11 | Current | Health Insurance | P&C Claims | Corporate | Customer Retention | USD | 504165.39 | 504165.39 | 504165.39 | 504165.39 |
| BS | Asset | Cash Equivalents | Other Banks | 1 | 100004 | 109011 | Assets | 109052 | Petty Cash - Corporate | Inherited (4-digit prefix) | MGA | Balance Sheet | Asset | 2025-01-31 00:00:00 | 2025 | 1 | Current | NULL | NULL | NULL | NULL | USD | 1329 | 1329 | 1329 | 1329 |
