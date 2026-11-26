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
- `2025`

**POSTING_QUARTER**
- `1`

**POSTING_MONTH**
- `2`

**PERIOD_END_DATE**
- `2025-02-28 00:00:00`

**ACCOUNT_NUMBER**
- `141121`
- `521124`
- `521120`
- `521310`
- `145100`

**ACCOUNT_NAME**
- `Premium Receivable - Current - Assumed`
- `Not in COA - 521124`
- `Commissions Expense - Assumed`
- `Deferred policy acquisition costs - Direct`
- `Amortization DPAC - Direct`

**ACCOUNT_DISPLAY**
- `141121 - Premium Receivable - Current - Assumed`
- `521124 - Not in COA`
- `521120 - Commissions Expense - Assumed`
- `521310 - Amortization DPAC - Direct`
- `145100 - Deferred policy acquisition costs - Direct`

**IN_COA**
- `True`
- `False`

**STAT_OR_MGA**
- `STAT`
- `NVS`

**ACCOUNT_TYPE**
- `Asset`
- `Expense`

**FINANCIAL_STATEMENT**
- `Balance Sheet`
- `Income Statement`

**COA_LEVEL_1**
- `Asset`
- `Expense`
- `None`

**COA_LEVEL_2**
- `Receivables and Recoverables`
- `Underwriting expenses (Commissions)`
- `None`
- `Underwriting expenses`

**COA_LEVEL_3**
- `Premium and Agent Balances Receivable`
- `None`
- `Regular`
- `Deferred policy acquisition costs`
- `Commissions expense`

**COA_LEVEL_4**
- `Current`
- `None`
- `Assumed`
- `Amortization (deferral) of acquisition costs`
- `Direct`

**COA_LEVEL_5**
- `Assumed`
- `None`
- `Direct`

**COA_LEVEL_6**
- `None`
- `Admitted`

**COMMISSION_SCOPE**
- `Commission-Related Event`
- `Commission Account`

**IS_COMMISSION_ACCOUNT**
- `True`
- `False`

**COMMISSION_GROUP**
- `Commission Offset`
- `Commission Expense`

**COMMISSION_GROUP_SORT**
- `2`
- `8`

**COMMISSION_TYPE**
- `Regular Commission`
- `Brokerage`
- `DPAC Amortization`

**BUSINESS_TYPE**
- `Assumed`
- `Direct`

**PROFIT_CENTER**
- `Health Insurance`
- `Property & Casualty Insurance`
- `Auto Insurance`
- `Life Insurance`

**COST_CENTER**
- `Underwriting`
- `P&C Claims`
- `Health Claims Processing`
- `Life Operations`
- `Health Provider Management`
- `Accident Assessment`

**LOB**
- `Broker`
- `Direct_Customer`
- `Corporate`

**ASLOB**
- `Property & Casualty`
- `Health Insurance`
- `Life Insurance`

**BUSINESS_INDICATOR**
- `New Business`
- `Claims Activity`
- `Customer Retention`

**BUSINESS_EVENT**
- `ASSUMED BROKERAGE`
- `ASSUMED COMMISSIONS`
- `DIRECT_COMMISSIONS`

**POSTING_LAYER**
- `US_GAAP`

**CAT_CODE**
- `NVS`

**STATE**
- `Michigan`
- `Indiana`
- `Texas`
- `Massachusetts`
- `Illinois`
- `Florida`
- `New Jersey`
- `Ohio`
- `Minnesota`
- `Oregon`

**TREATY_BUSINESS_TYPE**
- `NVS`

**REINSURER_ID**
- `NVS`

**ACCIDENT_YEAR**
- `NVS`

**TAX_YEAR**
- `2025`

**CATEGORIES**
- `NVS`

**SUBLINE_TYPE**
- `Commercial Property`
- `Group Health`
- `Group Life`
- `Commercial Auto`
- `Term Life`
- `Personal Auto`
- `Individual Health`

**SOURCE_SYSTEM**
- `DAG`

**SOURCE_TYPE**
- `SLR`
