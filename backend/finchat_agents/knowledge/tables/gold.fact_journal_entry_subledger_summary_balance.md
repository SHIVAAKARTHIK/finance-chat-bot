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
row_count: 1072
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
- `145100`: 125 rows
- `141121`: 107 rows
- `522110`: 91 rows
- `192200`: 86 rows
- `141111`: 60 rows
- `411100`: 60 rows
- `511110`: 47 rows
- `512110`: 47 rows
- `102100`: 40 rows
- `521120`: 37 rows
- `521124`: 37 rows
- `212100`: 35 rows
- `412100`: 35 rows
- `212200`: 33 rows
- `521310`: 33 rows
- `411200`: 33 rows
- `412200`: 33 rows
- `529061`: 20 rows
- `146100`: 20 rows
- `522210`: 19 rows
- `222110`: 18 rows
- `512210`: 8 rows
- `211211`: 8 rows
- `511210`: 8 rows
- `102403`: 8 rows
- `211111`: 8 rows
- `211221`: 4 rows
- `512310`: 4 rows
- `211121`: 4 rows
- `511310`: 4 rows

**PROFIT_CENTER**
- `Health Insurance`: 308 rows
- `Property & Casualty Insurance`: 304 rows
- `Auto Insurance`: 232 rows
- `Life Insurance`: 228 rows

**BUSINESS_INDICATOR**
- `New Business`: 488 rows
- `Claims Activity`: 440 rows
- `Customer Retention`: 144 rows

**ASLOB**
- `Property & Casualty`: 536 rows
- `Health Insurance`: 308 rows
- `Life Insurance`: 228 rows

**POSTING_LAYER**
- `US_GAAP`: 1072 rows

**BUSINESS_EVENT**
- `DIRECT WRITTEN PREMIUM`: 120 rows
- `DIRECT_LOSS_RECOVERIES`: 78 rows
- `DIRECT_LOSS_RECOVERIES_LAE`: 78 rows
- `SERVICE FEE DIRECT`: 74 rows
- `ASSUMED BROKERAGE`: 74 rows
- `ASSUMED COMMISSIONS`: 74 rows
- `PREMIUM WRITE OFFS`: 72 rows
- `DIRECT_UPR_CHANGE`: 70 rows
- `ASSUMED UPR CHANGE`: 66 rows
- `ASSUMED WRITTEN PREMIUM`: 66 rows
- `DIRECT_COMMISSIONS`: 66 rows
- `MANAGEMENT FEES RECEIPT`: 40 rows
- `INSPECTION FEES`: 40 rows
- `DEFERRED_PREMIUM_TAXES`: 38 rows
- `PREMIUM_TAXES`: 36 rows
- `DIRECT CASE CHANGE LOSS`: 8 rows
- `DIRECT CASE CHANGE LAE`: 8 rows
- `DIRECT_PAID_LOSS`: 8 rows
- `DIRECT SALVAGE SUBRO RECOVERABLE LAE`: 8 rows
- `DIRECT_PAID_LOSS_LAE`: 8 rows
- `DIRECT_CASE_CHANGE_RESERVE_LOSS_LAE`: 8 rows
- `DIRECT SALVAGE SUBRO RECOVERABLE LOSSES`: 8 rows
- `DIRECT IBNR CHANGE LOSS`: 8 rows
- `DIRECT IBNR CHANGE LAE`: 8 rows
- `DIRECT_CASE_CHANGE_RESERVE_LOSS`: 8 rows

**CAT_CODE**
- `NVS`: 836 rows
- `CAT-014`: 28 rows
- `CAT-015`: 26 rows
- `CAT-002`: 24 rows
- `NON CAT`: 20 rows
- `CAT-004`: 18 rows
- `CAT-009`: 18 rows
- `CAT-011`: 18 rows
- `CAT-005`: 16 rows
- `CAT-007`: 14 rows
- `CAT-001`: 14 rows
- `CAT-006`: 10 rows
- `CAT-008`: 10 rows
- `CAT-003`: 8 rows
- `CAT-010`: 8 rows
- `CAT-013`: 2 rows
- `CAT-012`: 2 rows

**STATE**
- `New Jersey`: 132 rows
- `Michigan`: 120 rows
- `Indiana`: 118 rows
- `Illinois`: 112 rows
- `Massachusetts`: 108 rows
- `Minnesota`: 106 rows
- `Florida`: 96 rows
- `Ohio`: 96 rows
- `Texas`: 94 rows
- `Oregon`: 90 rows

**TREATY_BUSINESS_TYPE**
- `NVS`: 1072 rows

**COST_CENTER**
- `Underwriting`: 374 rows
- `P&C Claims`: 200 rows
- `Health Provider Management`: 144 rows
- `Accident Assessment`: 124 rows
- `Health Claims Processing`: 116 rows
- `Life Operations`: 114 rows

**LOB**
- `Broker`: 536 rows
- `Direct_Customer`: 484 rows
- `Corporate`: 52 rows

**REINSURER_ID**
- `NVS`: 1072 rows

**ACCIDENT_YEAR**
- `NVS`: 836 rows
- `2025`: 236 rows

**TAX_YEAR**
- `2025`: 1072 rows

**CATEGORIES**
- `NVS`: 1072 rows

**SUBLINE_TYPE**
- `Commercial Property`: 304 rows
- `Group Health`: 208 rows
- `Commercial Auto`: 132 rows
- `Term Life`: 120 rows
- `Group Life`: 108 rows
- `Personal Auto`: 100 rows
- `Individual Health`: 100 rows

**SOURCE_SYSTEM**
- `DAG`: 1072 rows

**SOURCE_TYPE**
- `SLR`: 1072 rows

**JL_POSTING_MONTH**
- `2`: 1072 rows

**JL_POSTING_YEAR**
- `2025`: 1072 rows

**JL_POSTING_QUARTER**
- `1`: 1072 rows

## Profile

Rows in the latest export: 1072.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `LEGAL_ENTITY_CODE` | STRING | 1 | 0 |  |  |
| `ACCOUNT_NUMBER` | STRING | 28 | 0 | 102100 | 529061 |
| `PROFIT_CENTER` | STRING | 4 | 0 | Auto Insurance | Property & Casualty Insurance |
| `INTERCOMPANY` | STRING | 1 | 0 |  |  |
| `BUSINESS_INDICATOR` | STRING | 3 | 0 | Claims Activity | New Business |
| `ASLOB` | STRING | 3 | 0 | Health Insurance | Property & Casualty |
| `POSTING_LAYER` | STRING | 1 | 0 | US_GAAP | US_GAAP |
| `BUSINESS_EVENT` | STRING | 26 | 0 | ASSUMED BROKERAGE | SERVICE FEE DIRECT |
| `CAT_CODE` | STRING | 17 | 0 | CAT-001 | NVS |
| `STATE` | STRING | 10 | 0 | Florida | Texas |
| `TREATY_BUSINESS_TYPE` | STRING | 1 | 0 | NVS | NVS |
| `COST_CENTER` | STRING | 6 | 0 | Accident Assessment | Underwriting |
| `PARENT_ENTITY` | STRING | 1 | 0 |  |  |
| `LOB` | STRING | 3 | 0 | Broker | Direct_Customer |
| `REINSURER_ID` | STRING | 1 | 0 | NVS | NVS |
| `ACCIDENT_YEAR` | STRING | 2 | 0 | 2025 | NVS |
| `TAX_YEAR` | STRING | 1 | 0 | 2025 | 2025 |
| `CATEGORIES` | STRING | 1 | 0 | NVS | NVS |
| `SUBLINE_TYPE` | STRING | 7 | 0 | Commercial Auto | Term Life |
| `SOURCE_SYSTEM` | STRING | 1 | 0 | DAG | DAG |
| `SOURCE_TYPE` | STRING | 1 | 0 | SLR | SLR |
| `JL_POSTING_MONTH` | INT | 1 | 0 | 2 | 2 |
| `JL_POSTING_YEAR` | INT | 1 | 0 | 2025 | 2025 |
| `JL_POSTING_QUARTER` | DECIMAL | 1 | 0 | 1 | 1 |
| `MTD_AMOUNT` | DECIMAL | 1057 | 0 | -199122 | 199122 |
| `QTD_AMOUNT` | DECIMAL | 1057 | 0 | -199122 | 199122 |
| `YTD_AMOUNT` | DECIMAL | 1057 | 0 | -199122 | 199122 |
| `LTD_AMOUNT` | DECIMAL | 1057 | 0 | -199122 | 199122 |

## Sample rows

| ACCOUNT_NUMBER | PROFIT_CENTER | BUSINESS_INDICATOR | ASLOB | POSTING_LAYER | BUSINESS_EVENT | CAT_CODE | STATE | TREATY_BUSINESS_TYPE | COST_CENTER | LOB | REINSURER_ID | ACCIDENT_YEAR | TAX_YEAR | CATEGORIES | SUBLINE_TYPE | SOURCE_SYSTEM | SOURCE_TYPE | JL_POSTING_MONTH | JL_POSTING_YEAR | JL_POSTING_QUARTER | MTD_AMOUNT | QTD_AMOUNT | YTD_AMOUNT | LTD_AMOUNT |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 102100 | Auto Insurance | Claims Activity | Property & Casualty | US_GAAP | INSPECTION FEES | NVS | Indiana | NVS | Accident Assessment | Direct_Customer | NVS | NVS | 2025 | NVS | Personal Auto | DAG | SLR | 2 | 2025 | 1 | 224 | 224 | 224 | 224 |
| 102100 | Auto Insurance | Claims Activity | Property & Casualty | US_GAAP | INSPECTION FEES | NVS | New Jersey | NVS | Accident Assessment | Direct_Customer | NVS | NVS | 2025 | NVS | Personal Auto | DAG | SLR | 2 | 2025 | 1 | 806 | 806 | 806 | 806 |
| 102100 | Auto Insurance | Claims Activity | Property & Casualty | US_GAAP | MANAGEMENT FEES RECEIPT | NVS | Illinois | NVS | Accident Assessment | Broker | NVS | NVS | 2025 | NVS | Commercial Auto | DAG | SLR | 2 | 2025 | 1 | 697 | 697 | 697 | 697 |
| 102100 | Auto Insurance | Claims Activity | Property & Casualty | US_GAAP | MANAGEMENT FEES RECEIPT | NVS | Minnesota | NVS | Accident Assessment | Broker | NVS | NVS | 2025 | NVS | Commercial Auto | DAG | SLR | 2 | 2025 | 1 | 248 | 248 | 248 | 248 |
| 102100 | Auto Insurance | Claims Activity | Property & Casualty | US_GAAP | MANAGEMENT FEES RECEIPT | NVS | Ohio | NVS | Accident Assessment | Broker | NVS | NVS | 2025 | NVS | Commercial Auto | DAG | SLR | 2 | 2025 | 1 | 501 | 501 | 501 | 501 |
