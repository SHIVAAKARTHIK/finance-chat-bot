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
- `BS`
- `PY`
- `CY`

**BS_LEVEL_1**
- `Equity`
- `Asset`
- `Liability`

**BS_LEVEL_2**
- `Retained Earnings`
- `Receivables and Recoverables`
- `Cash Equivalents`
- `Operational Liabilities`
- `Underwriting Liabilities`
- `Insurance Policy Liabilities`
- `Other assets`
- `Property and Equipment`
- `Invested Assets`
- `Short Term Investments`
- `Other Assets`
- `Financing and Debt`
- `Additional paid in capital`
- `Federal Tax Assets`
- `Company Stock`
- `Other Liabilities`
- `Federal Tax Liabilities`
- `Outstanding loss and loss adjustment expense (Loss Adjustment Expense outstanding)`
- `Capital Assets`

**BS_LEVEL_1_SORT**
- `3`
- `1`
- `2`

**BS_LEVEL_2_SORT**
- `330000`
- `141000`
- `100004`
- `229110`
- `221000`
- `211111`
- `191100`
- `161100`
- `131100`
- `121100`
- `176100`
- `241201`
- `320000`
- `151100`
- `310100`
- `251000`
- `291000`
- `211212`
- `171000`

**BS_SIDE**
- `Liabilities & Equity`
- `Assets`

**COA_MAPPING_STATUS**
- `Mapped`
- `Inherited (4-digit prefix)`

**STAT_OR_MGA**
- `MGA`
- `STAT`

**SOURCE_LEVEL_0**
- `Income Statement`
- `Balance Sheet`

**SOURCE_LEVEL_1**
- `Expense`
- `Asset`
- `Revenue`
- `Liability`
- `Equity`

**FISCAL_YEAR**
- `2025`
- `2026`
- `2024`

**FISCAL_MONTH**
- `12`
- `1`
- `11`
- `4`
- `3`
- `2`
- `9`
- `8`
- `7`
- `6`
- `5`
- `10`

**POSTING_LAYER**
- `Current`
- `Operations`

**PROFIT_CENTER**
- `None`
- `Personal`
- `Health Insurance`
- `Property & Casualty Insurance`
- `Specialty`
- `Auto Insurance`
- `Life Insurance`
- `Commercial`
- `Investment & Wealth Management`
- `0`
- `MAR`
- `CAI`
- `SLM`
- `SLA`
- `FLI`
- `SLO`
- `FLM`
- `PRI`
- `PRN`
- `SLP`
- `TRP`
- `FLN`

**LOB**
- `None`
- `Direct_Customer`
- `Broker`
- `0`
- `Corporate`
- `10`
- `Individual`
- `Reinsurance`
- `18`

**TRANSACTION_CURRENCY**
- `USD`
- `GBP`
- `EUR`
- `CAD`
- `SEK`
- `AUD`
- `ZAR`
- `NOK`
