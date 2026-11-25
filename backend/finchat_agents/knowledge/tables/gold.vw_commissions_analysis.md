---
name: vw_commissions_analysis
schema: gold
layer: gold
domain: gl
type: view
status: active
purpose: 'Commission analysis for Power BI. Source: gold.fact_journal_entry_subledger_summary_balance (monthly MTD/QTD/YTD/LTD)
  + gold.dim_coa. Commission accounts are identified dynamically from dim_coa (name/Level 2-6 contains commission or brokerage);
  accounts 521100-521399 missing from dim_coa are kept with IN_COA = false. COMMISSION_SCOPE = Commission Account | Commission-Related
  Event (non-commission accounts carrying commission/brokerage business events; these offset the commission accounts). *_AMOUNT
  = ledger sign (debit +); *_AMOUNT_NATURAL = sign flipped for Revenue/Liability.'
grain: one row per period; entity; account; commission scope and business dimensions
primary_key:
- PERIOD_KEY
- LEGAL_ENTITY_CODE
- ACCOUNT_NUMBER
- COMMISSION_SCOPE
- BUSINESS_EVENT
- PROFIT_CENTER
- COST_CENTER
- LOB
entity_column: LEGAL_ENTITY_CODE
period_columns:
- PERIOD_KEY
- PERIOD_END_DATE
- POSTING_YEAR
- POSTING_QUARTER
- POSTING_MONTH
pii_columns: []
synonyms: []
built_from:
- fact_journal_entry_subledger_summary_balance
- dim_coa
known_issues: []
row_count: 214
proposed_fields: []
reviewed: false
---

# vw_commissions_analysis

Commission analysis for Power BI. Source: gold.fact_journal_entry_subledger_summary_balance (monthly MTD/QTD/YTD/LTD) + gold.dim_coa. Commission accounts are identified dynamically from dim_coa (name/Level 2-6 contains commission or brokerage); accounts 521100-521399 missing from dim_coa are kept with IN_COA = false. COMMISSION_SCOPE = Commission Account | Commission-Related Event (non-commission accounts carrying commission/brokerage business events; these offset the commission accounts). *_AMOUNT = ledger sign (debit +); *_AMOUNT_NATURAL = sign flipped for Revenue/Liability.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `POSTING_YEAR` | int |  |  | `POSTING_YEAR` |
| `POSTING_QUARTER` | int |  |  | `POSTING_QUARTER` |
| `POSTING_MONTH` | int |  |  | `POSTING_MONTH` |
| `PERIOD_KEY` | int |  |  | `PERIOD_KEY` |
| `PERIOD_END_DATE` | date |  |  | `PERIOD_END_DATE` |
| `PERIOD_LABEL` | string |  |  | `PERIOD_LABEL` |
| `LEGAL_ENTITY_CODE` | string |  |  | `LEGAL_ENTITY_CODE` |
| `ACCOUNT_NUMBER` | string |  |  | `ACCOUNT_NUMBER` |
| `ACCOUNT_NAME` | string |  |  | `ACCOUNT_NAME` |
| `ACCOUNT_DISPLAY` | string |  |  | `ACCOUNT_DISPLAY` |
| `IN_COA` | boolean |  |  | `IN_COA` |
| `STAT_OR_MGA` | string |  |  | `STAT_OR_MGA` |
| `ACCOUNT_TYPE` | string |  |  | `ACCOUNT_TYPE` |
| `FINANCIAL_STATEMENT` | string |  |  | `FINANCIAL_STATEMENT` |
| `COA_LEVEL_1` | string |  |  | `COA_LEVEL_1` |
| `COA_LEVEL_2` | string |  |  | `COA_LEVEL_2` |
| `COA_LEVEL_3` | string |  |  | `COA_LEVEL_3` |
| `COA_LEVEL_4` | string |  |  | `COA_LEVEL_4` |
| `COA_LEVEL_5` | string |  |  | `COA_LEVEL_5` |
| `COA_LEVEL_6` | string |  |  | `COA_LEVEL_6` |
| `COMMISSION_SCOPE` | string |  |  | `COMMISSION_SCOPE` |
| `IS_COMMISSION_ACCOUNT` | boolean |  |  | `IS_COMMISSION_ACCOUNT` |
| `COMMISSION_GROUP` | string |  |  | `COMMISSION_GROUP` |
| `COMMISSION_GROUP_SORT` | int |  |  | `COMMISSION_GROUP_SORT` |
| `COMMISSION_TYPE` | string |  |  | `COMMISSION_TYPE` |
| `BUSINESS_TYPE` | string |  |  | `BUSINESS_TYPE` |
| `PROFIT_CENTER` | string |  |  | `PROFIT_CENTER` |
| `COST_CENTER` | string |  |  | `COST_CENTER` |
| `LOB` | string |  |  | `LOB` |
| `ASLOB` | string |  |  | `ASLOB` |
| `BUSINESS_INDICATOR` | string |  |  | `BUSINESS_INDICATOR` |
| `BUSINESS_EVENT` | string |  |  | `BUSINESS_EVENT` |
| `POSTING_LAYER` | string |  |  | `POSTING_LAYER` |
| `INTERCOMPANY` | string |  |  | `INTERCOMPANY` |
| `CAT_CODE` | string |  |  | `CAT_CODE` |
| `STATE` | string |  |  | `STATE` |
| `TREATY_BUSINESS_TYPE` | string |  |  | `TREATY_BUSINESS_TYPE` |
| `PARENT_ENTITY` | string |  |  | `PARENT_ENTITY` |
| `REINSURER_ID` | string |  |  | `REINSURER_ID` |
| `ACCIDENT_YEAR` | string |  |  | `ACCIDENT_YEAR` |
| `TAX_YEAR` | string |  |  | `TAX_YEAR` |
| `CATEGORIES` | string |  |  | `CATEGORIES` |
| `SUBLINE_TYPE` | string |  |  | `SUBLINE_TYPE` |
| `SOURCE_SYSTEM` | string |  |  | `SOURCE_SYSTEM` |
| `SOURCE_TYPE` | string |  |  | `SOURCE_TYPE` |
| `MTD_AMOUNT` | decimal |  |  | `MTD_AMOUNT` |
| `QTD_AMOUNT` | decimal |  |  | `QTD_AMOUNT` |
| `YTD_AMOUNT` | decimal |  |  | `YTD_AMOUNT` |
| `LTD_AMOUNT` | decimal |  |  | `LTD_AMOUNT` |
| `MTD_AMOUNT_NATURAL` | decimal |  |  | `MTD_AMOUNT_NATURAL` |
| `QTD_AMOUNT_NATURAL` | decimal |  |  | `QTD_AMOUNT_NATURAL` |
| `YTD_AMOUNT_NATURAL` | decimal |  |  | `YTD_AMOUNT_NATURAL` |
| `LTD_AMOUNT_NATURAL` | decimal |  |  | `LTD_AMOUNT_NATURAL` |

## Values

**POSTING_YEAR**
- `2025`: 214 rows

**POSTING_QUARTER**
- `1`: 214 rows

**POSTING_MONTH**
- `2`: 214 rows

**PERIOD_END_DATE**
- `2025-02-28 00:00:00`: 214 rows

**ACCOUNT_NUMBER**
- `141121`: 74 rows
- `521124`: 37 rows
- `521120`: 37 rows
- `521310`: 33 rows
- `145100`: 33 rows

**ACCOUNT_NAME**
- `Premium Receivable - Current - Assumed`: 74 rows
- `Not in COA - 521124`: 37 rows
- `Commissions Expense - Assumed`: 37 rows
- `Deferred policy acquisition costs - Direct`: 33 rows
- `Amortization DPAC - Direct`: 33 rows

**ACCOUNT_DISPLAY**
- `141121 - Premium Receivable - Current - Assumed`: 74 rows
- `521124 - Not in COA`: 37 rows
- `521120 - Commissions Expense - Assumed`: 37 rows
- `521310 - Amortization DPAC - Direct`: 33 rows
- `145100 - Deferred policy acquisition costs - Direct`: 33 rows

**IN_COA**
- `True`: 177 rows
- `False`: 37 rows

**STAT_OR_MGA**
- `STAT`: 177 rows
- `NVS`: 37 rows

**ACCOUNT_TYPE**
- `Asset`: 107 rows
- `Expense`: 107 rows

**FINANCIAL_STATEMENT**
- `Balance Sheet`: 107 rows
- `Income Statement`: 107 rows

**COA_LEVEL_1**
- `Asset`: 107 rows
- `Expense`: 70 rows
- `None`: 37 rows

**COA_LEVEL_2**
- `Receivables and Recoverables`: 107 rows
- `Underwriting expenses (Commissions)`: 37 rows
- `None`: 37 rows
- `Underwriting expenses`: 33 rows

**COA_LEVEL_3**
- `Premium and Agent Balances Receivable`: 74 rows
- `None`: 37 rows
- `Regular`: 37 rows
- `Deferred policy acquisition costs`: 33 rows
- `Commissions expense`: 33 rows

**COA_LEVEL_4**
- `Current`: 74 rows
- `None`: 37 rows
- `Assumed`: 37 rows
- `Amortization (deferral) of acquisition costs`: 33 rows
- `Direct`: 33 rows

**COA_LEVEL_5**
- `Assumed`: 111 rows
- `None`: 70 rows
- `Direct`: 33 rows

**COA_LEVEL_6**
- `None`: 140 rows
- `Admitted`: 74 rows

**COMMISSION_SCOPE**
- `Commission-Related Event`: 107 rows
- `Commission Account`: 107 rows

**IS_COMMISSION_ACCOUNT**
- `True`: 107 rows
- `False`: 107 rows

**COMMISSION_GROUP**
- `Commission Offset`: 107 rows
- `Commission Expense`: 107 rows

**COMMISSION_GROUP_SORT**
- `2`: 107 rows
- `8`: 107 rows

**COMMISSION_TYPE**
- `Regular Commission`: 107 rows
- `Brokerage`: 74 rows
- `DPAC Amortization`: 33 rows

**BUSINESS_TYPE**
- `Assumed`: 148 rows
- `Direct`: 66 rows

**PROFIT_CENTER**
- `Health Insurance`: 62 rows
- `Property & Casualty Insurance`: 60 rows
- `Auto Insurance`: 46 rows
- `Life Insurance`: 46 rows

**COST_CENTER**
- `Underwriting`: 70 rows
- `P&C Claims`: 38 rows
- `Health Claims Processing`: 28 rows
- `Life Operations`: 28 rows
- `Health Provider Management`: 26 rows
- `Accident Assessment`: 24 rows

**LOB**
- `Broker`: 116 rows
- `Direct_Customer`: 96 rows
- `Corporate`: 2 rows

**ASLOB**
- `Property & Casualty`: 106 rows
- `Health Insurance`: 62 rows
- `Life Insurance`: 46 rows

**BUSINESS_INDICATOR**
- `New Business`: 98 rows
- `Claims Activity`: 90 rows
- `Customer Retention`: 26 rows

**BUSINESS_EVENT**
- `ASSUMED BROKERAGE`: 74 rows
- `ASSUMED COMMISSIONS`: 74 rows
- `DIRECT_COMMISSIONS`: 66 rows

**POSTING_LAYER**
- `US_GAAP`: 214 rows

**CAT_CODE**
- `NVS`: 214 rows

**STATE**
- `Michigan`: 28 rows
- `Indiana`: 28 rows
- `Texas`: 24 rows
- `Massachusetts`: 24 rows
- `Illinois`: 22 rows
- `Florida`: 22 rows
- `New Jersey`: 22 rows
- `Ohio`: 16 rows
- `Minnesota`: 14 rows
- `Oregon`: 14 rows

**TREATY_BUSINESS_TYPE**
- `NVS`: 214 rows

**REINSURER_ID**
- `NVS`: 214 rows

**ACCIDENT_YEAR**
- `NVS`: 214 rows

**TAX_YEAR**
- `2025`: 214 rows

**CATEGORIES**
- `NVS`: 214 rows

**SUBLINE_TYPE**
- `Commercial Property`: 60 rows
- `Group Health`: 42 rows
- `Group Life`: 24 rows
- `Commercial Auto`: 24 rows
- `Term Life`: 22 rows
- `Personal Auto`: 22 rows
- `Individual Health`: 20 rows

**SOURCE_SYSTEM**
- `DAG`: 214 rows

**SOURCE_TYPE**
- `SLR`: 214 rows

## Profile

Rows in the latest export: 214.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `POSTING_YEAR` | INT | 1 | 0 | 2025 | 2025 |
| `POSTING_QUARTER` | INT | 1 | 0 | 1 | 1 |
| `POSTING_MONTH` | INT | 1 | 0 | 2 | 2 |
| `PERIOD_KEY` | INT | 1 | 0 |  |  |
| `PERIOD_END_DATE` | DATE | 1 | 0 | 2025-02-28 00:00:00 | 2025-02-28 00:00:00 |
| `PERIOD_LABEL` | STRING | 1 | 0 |  |  |
| `LEGAL_ENTITY_CODE` | STRING | 1 | 0 |  |  |
| `ACCOUNT_NUMBER` | STRING | 5 | 0 | 141121 | 521310 |
| `ACCOUNT_NAME` | STRING | 4 | 0 | Amortization DPAC - Direct | Premium Receivable - Current - Assumed |
| `ACCOUNT_DISPLAY` | STRING | 5 | 0 | 141121 - Premium Receivable - Current... | 521310 - Amortization DPAC - Direct |
| `IN_COA` | BOOLEAN | 2 | 0 | False | True |
| `STAT_OR_MGA` | STRING | 2 | 0 | NVS | STAT |
| `ACCOUNT_TYPE` | STRING | 2 | 0 | Asset | Expense |
| `FINANCIAL_STATEMENT` | STRING | 2 | 0 | Balance Sheet | Income Statement |
| `COA_LEVEL_1` | STRING | 2 | 37 | Asset | Expense |
| `COA_LEVEL_2` | STRING | 3 | 37 | Receivables and Recoverables | Underwriting expenses (Commissions) |
| `COA_LEVEL_3` | STRING | 4 | 37 | Commissions expense | Regular |
| `COA_LEVEL_4` | STRING | 4 | 37 | Amortization (deferral) of acquisitio... | Direct |
| `COA_LEVEL_5` | STRING | 2 | 70 | Assumed | Direct |
| `COA_LEVEL_6` | STRING | 1 | 140 | Admitted | Admitted |
| `COMMISSION_SCOPE` | STRING | 2 | 0 | Commission Account | Commission-Related Event |
| `IS_COMMISSION_ACCOUNT` | BOOLEAN | 2 | 0 | False | True |
| `COMMISSION_GROUP` | STRING | 2 | 0 | Commission Expense | Commission Offset |
| `COMMISSION_GROUP_SORT` | INT | 2 | 0 | 2 | 8 |
| `COMMISSION_TYPE` | STRING | 3 | 0 | Brokerage | Regular Commission |
| `BUSINESS_TYPE` | STRING | 2 | 0 | Assumed | Direct |
| `PROFIT_CENTER` | STRING | 4 | 0 | Auto Insurance | Property & Casualty Insurance |
| `COST_CENTER` | STRING | 6 | 0 | Accident Assessment | Underwriting |
| `LOB` | STRING | 3 | 0 | Broker | Direct_Customer |
| `ASLOB` | STRING | 3 | 0 | Health Insurance | Property & Casualty |
| `BUSINESS_INDICATOR` | STRING | 3 | 0 | Claims Activity | New Business |
| `BUSINESS_EVENT` | STRING | 3 | 0 | ASSUMED BROKERAGE | DIRECT_COMMISSIONS |
| `POSTING_LAYER` | STRING | 1 | 0 | US_GAAP | US_GAAP |
| `INTERCOMPANY` | STRING | 1 | 0 |  |  |
| `CAT_CODE` | STRING | 1 | 0 | NVS | NVS |
| `STATE` | STRING | 10 | 0 | Florida | Texas |
| `TREATY_BUSINESS_TYPE` | STRING | 1 | 0 | NVS | NVS |
| `PARENT_ENTITY` | STRING | 1 | 0 |  |  |
| `REINSURER_ID` | STRING | 1 | 0 | NVS | NVS |
| `ACCIDENT_YEAR` | STRING | 1 | 0 | NVS | NVS |
| `TAX_YEAR` | STRING | 1 | 0 | 2025 | 2025 |
| `CATEGORIES` | STRING | 1 | 0 | NVS | NVS |
| `SUBLINE_TYPE` | STRING | 7 | 0 | Commercial Auto | Term Life |
| `SOURCE_SYSTEM` | STRING | 1 | 0 | DAG | DAG |
| `SOURCE_TYPE` | STRING | 1 | 0 | SLR | SLR |
| `MTD_AMOUNT` | DECIMAL | 217 | 0 | -62501 | 62501 |
| `QTD_AMOUNT` | DECIMAL | 217 | 0 | -62501 | 62501 |
| `YTD_AMOUNT` | DECIMAL | 217 | 0 | -62501 | 62501 |
| `LTD_AMOUNT` | DECIMAL | 217 | 0 | -62501 | 62501 |
| `MTD_AMOUNT_NATURAL` | DECIMAL | 217 | 0 | -62501 | 62501 |
| `QTD_AMOUNT_NATURAL` | DECIMAL | 217 | 0 | -62501 | 62501 |
| `YTD_AMOUNT_NATURAL` | DECIMAL | 217 | 0 | -62501 | 62501 |
| `LTD_AMOUNT_NATURAL` | DECIMAL | 217 | 0 | -62501 | 62501 |

## Sample rows

| POSTING_YEAR | POSTING_QUARTER | POSTING_MONTH | PERIOD_END_DATE | PERIOD_LABEL | ACCOUNT_NUMBER | ACCOUNT_NAME | ACCOUNT_DISPLAY | IN_COA | STAT_OR_MGA | ACCOUNT_TYPE | FINANCIAL_STATEMENT | COA_LEVEL_1 | COA_LEVEL_2 | COA_LEVEL_3 | COA_LEVEL_4 | COA_LEVEL_5 | COA_LEVEL_6 | COMMISSION_SCOPE | IS_COMMISSION_ACCOUNT | COMMISSION_GROUP | COMMISSION_GROUP_SORT | COMMISSION_TYPE | BUSINESS_TYPE | PROFIT_CENTER | COST_CENTER | LOB | ASLOB | BUSINESS_INDICATOR | BUSINESS_EVENT | POSTING_LAYER | CAT_CODE | STATE | TREATY_BUSINESS_TYPE | REINSURER_ID | ACCIDENT_YEAR | TAX_YEAR | CATEGORIES | SUBLINE_TYPE | SOURCE_SYSTEM | SOURCE_TYPE | MTD_AMOUNT | QTD_AMOUNT | YTD_AMOUNT | LTD_AMOUNT | MTD_AMOUNT_NATURAL | QTD_AMOUNT_NATURAL | YTD_AMOUNT_NATURAL | LTD_AMOUNT_NATURAL |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2025 | 1 | 2 | 2025-02-28 00:00:00 | (altered in export) | 141121 | Premium Receivable - Current - Assumed | 141121 - Premium Receivable - Current... | True | STAT | Asset | Balance Sheet | Asset | Receivables and Recoverables | Premium and Agent Balances Receivable | Current | Assumed | Admitted | Commission-Related Event | False | Commission Offset | 8 | Brokerage | Assumed | Auto Insurance | Accident Assessment | Broker | Property & Casualty | Claims Activity | ASSUMED BROKERAGE | US_GAAP | NVS | Florida | NVS | NVS | NVS | 2025 | NVS | Commercial Auto | DAG | SLR | -5436 | -5436 | -5436 | -5436 | -5436 | -5436 | -5436 | -5436 |
| 2025 | 1 | 2 | 2025-02-28 00:00:00 | (altered in export) | 141121 | Premium Receivable - Current - Assumed | 141121 - Premium Receivable - Current... | True | STAT | Asset | Balance Sheet | Asset | Receivables and Recoverables | Premium and Agent Balances Receivable | Current | Assumed | Admitted | Commission-Related Event | False | Commission Offset | 8 | Brokerage | Assumed | Auto Insurance | Accident Assessment | Direct_Customer | Property & Casualty | Claims Activity | ASSUMED BROKERAGE | US_GAAP | NVS | Illinois | NVS | NVS | NVS | 2025 | NVS | Personal Auto | DAG | SLR | -3826 | -3826 | -3826 | -3826 | -3826 | -3826 | -3826 | -3826 |
| 2025 | 1 | 2 | 2025-02-28 00:00:00 | (altered in export) | 141121 | Premium Receivable - Current - Assumed | 141121 - Premium Receivable - Current... | True | STAT | Asset | Balance Sheet | Asset | Receivables and Recoverables | Premium and Agent Balances Receivable | Current | Assumed | Admitted | Commission-Related Event | False | Commission Offset | 8 | Brokerage | Assumed | Auto Insurance | Accident Assessment | Broker | Property & Casualty | Claims Activity | ASSUMED BROKERAGE | US_GAAP | NVS | New Jersey | NVS | NVS | NVS | 2025 | NVS | Commercial Auto | DAG | SLR | -6789 | -6789 | -6789 | -6789 | -6789 | -6789 | -6789 | -6789 |
| 2025 | 1 | 2 | 2025-02-28 00:00:00 | (altered in export) | 141121 | Premium Receivable - Current - Assumed | 141121 - Premium Receivable - Current... | True | STAT | Asset | Balance Sheet | Asset | Receivables and Recoverables | Premium and Agent Balances Receivable | Current | Assumed | Admitted | Commission-Related Event | False | Commission Offset | 8 | Regular Commission | Assumed | Auto Insurance | Accident Assessment | Direct_Customer | Property & Casualty | Claims Activity | ASSUMED COMMISSIONS | US_GAAP | NVS | Florida | NVS | NVS | NVS | 2025 | NVS | Personal Auto | DAG | SLR | -1448 | -1448 | -1448 | -1448 | -1448 | -1448 | -1448 | -1448 |
| 2025 | 1 | 2 | 2025-02-28 00:00:00 | (altered in export) | 141121 | Premium Receivable - Current - Assumed | 141121 - Premium Receivable - Current... | True | STAT | Asset | Balance Sheet | Asset | Receivables and Recoverables | Premium and Agent Balances Receivable | Current | Assumed | Admitted | Commission-Related Event | False | Commission Offset | 8 | Regular Commission | Assumed | Auto Insurance | Accident Assessment | Direct_Customer | Property & Casualty | Claims Activity | ASSUMED COMMISSIONS | US_GAAP | NVS | Illinois | NVS | NVS | NVS | 2025 | NVS | Personal Auto | DAG | SLR | -950 | -950 | -950 | -950 | -950 | -950 | -950 | -950 |
