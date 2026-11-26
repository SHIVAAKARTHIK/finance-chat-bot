---
name: fact_journal_entry_subledger_summary_balance
schema: gold
layer: gold
domain: subledger
type: view
status: active
purpose: Monthly MTD/QTD/YTD/LTD balance summary of Fynapse subledger journal activity by account and finance dimensions.
grain: one row per account; entity; posting period and business dimension combination
primary_key:
- LEGAL_ENTITY_CODE
- ACCOUNT_NUMBER
- JL_POSTING_YEAR
- JL_POSTING_MONTH
- PROFIT_CENTER
- COST_CENTER
- BUSINESS_INDICATOR
- LOB
- BUSINESS_EVENT
entity_column: LEGAL_ENTITY_CODE
period_columns:
- JL_POSTING_YEAR
- JL_POSTING_MONTH
- JL_POSTING_QUARTER
pii_columns: []
synonyms: []
built_from:
- fact_fynapse_slr_journals
known_issues: []
proposed_fields: []
reviewed: false
---

# fact_journal_entry_subledger_summary_balance

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `LEGAL_ENTITY_CODE` | string |  |  | `LEGAL_ENTITY_CODE` |
| `ACCOUNT_NUMBER` | string |  |  | `ACCOUNT_NUMBER` |
| `PROFIT_CENTER` | string |  |  | `PROFIT_CENTER` |
| `INTERCOMPANY` | string |  |  | `INTERCOMPANY` |
| `BUSINESS_INDICATOR` | string |  |  | `BUSINESS_INDICATOR` |
| `ASLOB` | string |  |  | `ASLOB` |
| `POSTING_LAYER` | string |  |  | `POSTING_LAYER` |
| `BUSINESS_EVENT` | string |  |  | `BUSINESS_EVENT` |
| `CAT_CODE` | string |  |  | `CAT_CODE` |
| `STATE` | string |  |  | `STATE` |
| `TREATY_BUSINESS_TYPE` | string |  |  | `TREATY_BUSINESS_TYPE` |
| `COST_CENTER` | string |  |  | `COST_CENTER` |
| `PARENT_ENTITY` | string |  |  | `PARENT_ENTITY` |
| `LOB` | string |  |  | `LOB` |
| `REINSURER_ID` | string |  |  | `REINSURER_ID` |
| `ACCIDENT_YEAR` | string |  |  | `ACCIDENT_YEAR` |
| `TAX_YEAR` | string |  |  | `TAX_YEAR` |
| `CATEGORIES` | string |  |  | `CATEGORIES` |
| `SUBLINE_TYPE` | string |  |  | `SUBLINE_TYPE` |
| `SOURCE_SYSTEM` | string |  |  | `SOURCE_SYSTEM` |
| `SOURCE_TYPE` | string |  |  | `SOURCE_TYPE` |
| `JL_POSTING_MONTH` | int |  |  | `JL_POSTING_MONTH` |
| `JL_POSTING_YEAR` | int |  |  | `JL_POSTING_YEAR` |
| `JL_POSTING_QUARTER` | decimal |  |  | `JL_POSTING_QUARTER` |
| `MTD_AMOUNT` | decimal |  |  | `MTD_AMOUNT` |
| `QTD_AMOUNT` | decimal |  |  | `QTD_AMOUNT` |
| `YTD_AMOUNT` | decimal |  |  | `YTD_AMOUNT` |
| `LTD_AMOUNT` | decimal |  |  | `LTD_AMOUNT` |

## Values

**ACCOUNT_NUMBER**
- `145100`
- `141121`
- `522110`
- `192200`
- `141111`
- `411100`
- `511110`
- `512110`
- `102100`
- `521120`
- `521124`
- `212100`
- `412100`
- `212200`
- `521310`
- `411200`
- `412200`
- `529061`
- `146100`
- `522210`
- `222110`
- `512210`
- `211211`
- `511210`
- `102403`
- `211111`
- `211221`
- `512310`
- `211121`
- `511310`

**PROFIT_CENTER**
- `Health Insurance`
- `Property & Casualty Insurance`
- `Auto Insurance`
- `Life Insurance`

**BUSINESS_INDICATOR**
- `New Business`
- `Claims Activity`
- `Customer Retention`

**ASLOB**
- `Property & Casualty`
- `Health Insurance`
- `Life Insurance`

**POSTING_LAYER**
- `US_GAAP`

**BUSINESS_EVENT**
- `DIRECT WRITTEN PREMIUM`
- `DIRECT_LOSS_RECOVERIES`
- `DIRECT_LOSS_RECOVERIES_LAE`
- `SERVICE FEE DIRECT`
- `ASSUMED BROKERAGE`
- `ASSUMED COMMISSIONS`
- `PREMIUM WRITE OFFS`
- `DIRECT_UPR_CHANGE`
- `ASSUMED UPR CHANGE`
- `ASSUMED WRITTEN PREMIUM`
- `DIRECT_COMMISSIONS`
- `MANAGEMENT FEES RECEIPT`
- `INSPECTION FEES`
- `DEFERRED_PREMIUM_TAXES`
- `PREMIUM_TAXES`
- `DIRECT CASE CHANGE LOSS`
- `DIRECT CASE CHANGE LAE`
- `DIRECT_PAID_LOSS`
- `DIRECT SALVAGE SUBRO RECOVERABLE LAE`
- `DIRECT_PAID_LOSS_LAE`
- `DIRECT_CASE_CHANGE_RESERVE_LOSS_LAE`
- `DIRECT SALVAGE SUBRO RECOVERABLE LOSSES`
- `DIRECT IBNR CHANGE LOSS`
- `DIRECT IBNR CHANGE LAE`
- `DIRECT_CASE_CHANGE_RESERVE_LOSS`

**CAT_CODE**
- `NVS`
- `CAT-014`
- `CAT-015`
- `CAT-002`
- `NON CAT`
- `CAT-004`
- `CAT-009`
- `CAT-011`
- `CAT-005`
- `CAT-007`
- `CAT-001`
- `CAT-006`
- `CAT-008`
- `CAT-003`
- `CAT-010`
- `CAT-013`
- `CAT-012`

**STATE**
- `New Jersey`
- `Michigan`
- `Indiana`
- `Illinois`
- `Massachusetts`
- `Minnesota`
- `Florida`
- `Ohio`
- `Texas`
- `Oregon`

**TREATY_BUSINESS_TYPE**
- `NVS`

**COST_CENTER**
- `Underwriting`
- `P&C Claims`
- `Health Provider Management`
- `Accident Assessment`
- `Health Claims Processing`
- `Life Operations`

**LOB**
- `Broker`
- `Direct_Customer`
- `Corporate`

**REINSURER_ID**
- `NVS`

**ACCIDENT_YEAR**
- `NVS`
- `2025`

**TAX_YEAR**
- `2025`

**CATEGORIES**
- `NVS`

**SUBLINE_TYPE**
- `Commercial Property`
- `Group Health`
- `Commercial Auto`
- `Term Life`
- `Group Life`
- `Personal Auto`
- `Individual Health`

**SOURCE_SYSTEM**
- `DAG`

**SOURCE_TYPE**
- `SLR`

**JL_POSTING_MONTH**
- `2`

**JL_POSTING_YEAR**
- `2025`

**JL_POSTING_QUARTER**
- `1`
