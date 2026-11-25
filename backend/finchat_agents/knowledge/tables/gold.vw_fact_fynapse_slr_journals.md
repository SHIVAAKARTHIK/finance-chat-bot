---
name: vw_fact_fynapse_slr_journals
schema: gold
layer: gold
domain: subledger
type: view
status: active
purpose: Fynapse subledger journal lines enriched with policy; claim; business and accounting dimensions.
grain: one row per JOURNAL_LINE_ID (one Fynapse journal line)
primary_key:
- JOURNAL_LINE_ID
entity_column: PARENT_ENTITY
period_columns:
- CORE_DATE
- TRANSACTION_DATE
- FISCAL_YEAR
- PERIOD
pii_columns: []
synonyms: []
built_from:
- fact_fynapse_slr_journals
known_issues: []
row_count: 1200
proposed_fields:
- grain
- primary_key
reviewed: false
---

# vw_fact_fynapse_slr_journals

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `JOURNAL_ID` | string |  |  | `JOURNAL_ID` |
| `ORIGIN_JOURNAL_ID` | string |  |  | `ORIGIN_JOURNAL_ID` |
| `CORE_DATE` | date |  |  | `CORE_DATE` |
| `JOURNAL_TYPE` | string |  |  | `JOURNAL_TYPE` |
| `ACCOUNTING_CONFIG` | string |  |  | `ACCOUNTING_CONFIG` |
| `ACCOUNT` | string |  |  | `ACCOUNT` |
| `TRANSACTION_AMOUNT` | decimal |  |  | `TRANSACTION_AMOUNT` |
| `TRANSACTION_CURRENCY` | string |  |  | `TRANSACTION_CURRENCY` |
| `JOURNAL_LINE_ID` | string |  |  | `JOURNAL_LINE_ID` |
| `JOURNAL_LINE_NO` | int |  |  | `JOURNAL_LINE_NO` |
| `ORIGIN_JOURNAL_LINE_ID` | string |  |  | `ORIGIN_JOURNAL_LINE_ID` |
| `REVERSES` | string |  |  | `REVERSES` |
| `REVERSED_BY` | string |  |  | `REVERSED_BY` |
| `INGESTION_ID` | string |  |  | `INGESTION_ID` |
| `FISCAL_YEAR` | int |  |  | `FISCAL_YEAR` |
| `PERIOD` | int |  |  | `PERIOD` |
| `FUNCTIONAL_AMOUNT` | decimal |  |  | `FUNCTIONAL_AMOUNT` |
| `FUNCTIONAL_CURRENCY` | string |  |  | `FUNCTIONAL_CURRENCY` |
| `PARENT_ENTITY` | string |  |  | `PARENT_ENTITY` |
| `CHILD_ENTITY` | string |  |  | `CHILD_ENTITY` |
| `BUSINESS_EVENT` | string |  |  | `BUSINESS_EVENT` |
| `COST_CENTER` | string |  |  | `COST_CENTER` |
| `PROFIT_CENTER` | string |  |  | `PROFIT_CENTER` |
| `ASLOB` | string |  |  | `ASLOB` |
| `LOB` | string |  |  | `LOB` |
| `STATE` | string |  |  | `STATE` |
| `TREATY_BUSINESS_TYPE` | string |  |  | `TREATY_BUSINESS_TYPE` |
| `REINSURER_ID` | string |  |  | `REINSURER_ID` |
| `TREATY_ID` | string |  |  | `TREATY_ID` |
| `ACCIDENT_YEAR` | int |  |  | `ACCIDENT_YEAR` |
| `TAX_YEAR` | int |  |  | `TAX_YEAR` |
| `COVERAGE_NUMBER` | string |  |  | `COVERAGE_NUMBER` |
| `POLICY_VERSION` | string |  |  | `POLICY_VERSION` |
| `CAT_CODE` | string |  |  | `CAT_CODE` |
| `INVOICE_NUMBER` | string |  |  | `INVOICE_NUMBER` |
| `CHECK_NUMBER` | string |  |  | `CHECK_NUMBER` |
| `CARRIER_CODE` | string |  |  | `CARRIER_CODE` |
| `INTERCOMPANY` | string |  |  | `INTERCOMPANY` |
| `SUBLINE_CODE` | string |  |  | `SUBLINE_CODE` |
| `SUBLINE_TYPE` | string |  |  | `SUBLINE_TYPE` |
| `SOURCE_SYSTEM` | string |  |  | `SOURCE_SYSTEM` |
| `BUSINESS_INDICATOR` | string |  |  | `BUSINESS_INDICATOR` |
| `CLAIM_NUMBER` | string |  |  | `CLAIM_NUMBER` |
| `REINSURANCE_LAYER` | string |  |  | `REINSURANCE_LAYER` |
| `LOSS_TYPE` | string |  |  | `LOSS_TYPE` |
| `CAUSE_OF_LOSS` | string |  |  | `CAUSE_OF_LOSS` |
| `EXPENSE_TYPE` | string |  |  | `EXPENSE_TYPE` |
| `CATEGORIES` | string |  |  | `CATEGORIES` |
| `SOURCE_TRANSACTION_ID` | string |  |  | `SOURCE_TRANSACTION_ID` |
| `JOURNAL_LINE_DEF` | string |  |  | `JOURNAL_LINE_DEF` |
| `REPORTING_CURRENCY` | string |  |  | `REPORTING_CURRENCY` |
| `REPORTING_AMOUNT` | decimal |  |  | `REPORTING_AMOUNT` |
| `TXT1` | string |  |  | `TXT1` |
| `TXT2` | string |  |  | `TXT2` |
| `TXT3` | string |  |  | `TXT3` |
| `TXT4` | string |  |  | `TXT4` |
| `TXT5` | string |  |  | `TXT5` |
| `AMT1` | decimal |  |  | `AMT1` |
| `AMT2` | decimal |  |  | `AMT2` |
| `AMT3` | decimal |  |  | `AMT3` |
| `DATE1` | date |  |  | `DATE1` |
| `DATE2` | date |  |  | `DATE2` |
| `DATE3` | date |  |  | `DATE3` |
| `TXT6` | string |  |  | `TXT6` |
| `TXT7` | string |  |  | `TXT7` |
| `TXT8` | string |  |  | `TXT8` |
| `TXT9` | string |  |  | `TXT9` |
| `TXT10` | string |  |  | `TXT10` |
| `AMT4` | decimal |  |  | `AMT4` |
| `AMT5` | decimal |  |  | `AMT5` |
| `AMT6` | decimal |  |  | `AMT6` |
| `DATE4` | date |  |  | `DATE4` |
| `DATE5` | date |  |  | `DATE5` |
| `DATE6` | date |  |  | `DATE6` |
| `TRANSACTION_DATE` | date |  |  | `TRANSACTION_DATE` |

## Values

**CORE_DATE**
- `2025-02-28 00:00:00`: 1200 rows

**JOURNAL_TYPE**
- `PERM`: 1200 rows

**ACCOUNTING_CONFIG**
- `US_GAAP`: 1200 rows

**ACCOUNT**
- `145100`: 140 rows
- `141121`: 120 rows
- `522110`: 100 rows
- `192200`: 88 rows
- `411100`: 80 rows
- `141111`: 80 rows
- `512110`: 48 rows
- `511110`: 48 rows
- `102100`: 40 rows
- `521120`: 40 rows
- `412100`: 40 rows
- `212100`: 40 rows
- `521124`: 40 rows
- `412200`: 40 rows
- `521310`: 40 rows
- `411200`: 40 rows
- `212200`: 40 rows
- `146100`: 20 rows
- `522210`: 20 rows
- `222110`: 20 rows
- `529061`: 20 rows
- `211211`: 8 rows
- `511210`: 8 rows
- `102403`: 8 rows
- `512210`: 8 rows
- `211111`: 8 rows
- `211221`: 4 rows
- `512310`: 4 rows
- `211121`: 4 rows
- `511310`: 4 rows

**TRANSACTION_CURRENCY**
- `USD`: 1200 rows

**JOURNAL_LINE_NO**
- `1`: 600 rows
- `2`: 600 rows

**ORIGIN_JOURNAL_LINE_ID**
- `None`: 1200 rows

**REVERSES**
- `None`: 1200 rows

**REVERSED_BY**
- `None`: 1200 rows

**INGESTION_ID**
- `in_01a1623bd60375bcaf6a5e553589f894`: 1200 rows

**FISCAL_YEAR**
- `None`: 1200 rows

**PERIOD**
- `None`: 1200 rows

**FUNCTIONAL_CURRENCY**
- `USD`: 1200 rows

**BUSINESS_EVENT**
- `DIRECT WRITTEN PREMIUM`: 160 rows
- `DIRECT_UPR_CHANGE`: 80 rows
- `DIRECT_LOSS_RECOVERIES_LAE`: 80 rows
- `DIRECT_COMMISSIONS`: 80 rows
- `ASSUMED UPR CHANGE`: 80 rows
- `ASSUMED COMMISSIONS`: 80 rows
- `SERVICE FEE DIRECT`: 80 rows
- `ASSUMED BROKERAGE`: 80 rows
- `ASSUMED WRITTEN PREMIUM`: 80 rows
- `PREMIUM WRITE OFFS`: 80 rows
- `DIRECT_LOSS_RECOVERIES`: 80 rows
- `MANAGEMENT FEES RECEIPT`: 40 rows
- `DEFERRED_PREMIUM_TAXES`: 40 rows
- `INSPECTION FEES`: 40 rows
- `PREMIUM_TAXES`: 40 rows
- `DIRECT SALVAGE SUBRO RECOVERABLE LOSSES`: 8 rows
- `DIRECT CASE CHANGE LAE`: 8 rows
- `DIRECT SALVAGE SUBRO RECOVERABLE LAE`: 8 rows
- `DIRECT CASE CHANGE LOSS`: 8 rows
- `DIRECT_PAID_LOSS_LAE`: 8 rows
- `DIRECT_CASE_CHANGE_RESERVE_LOSS_LAE`: 8 rows
- `DIRECT IBNR CHANGE LOSS`: 8 rows
- `DIRECT IBNR CHANGE LAE`: 8 rows
- `DIRECT_PAID_LOSS`: 8 rows
- `DIRECT_CASE_CHANGE_RESERVE_LOSS`: 8 rows

**COST_CENTER**
- `Underwriting`: 424 rows
- `P&C Claims`: 226 rows
- `Health Provider Management`: 166 rows
- `Accident Assessment`: 136 rows
- `Health Claims Processing`: 126 rows
- `Life Operations`: 122 rows

**PROFIT_CENTER**
- `Health Insurance`: 350 rows
- `Property & Casualty Insurance`: 336 rows
- `Auto Insurance`: 260 rows
- `Life Insurance`: 254 rows

**ASLOB**
- `Property & Casualty`: 596 rows
- `Health Insurance`: 350 rows
- `Life Insurance`: 254 rows

**LOB**
- `Broker`: 608 rows
- `Direct_Customer`: 532 rows
- `Corporate`: 60 rows

**STATE**
- `New Jersey`: 142 rows
- `Indiana`: 136 rows
- `Michigan`: 132 rows
- `Massachusetts`: 130 rows
- `Illinois`: 124 rows
- `Minnesota`: 122 rows
- `Ohio`: 110 rows
- `Florida`: 102 rows
- `Texas`: 102 rows
- `Oregon`: 100 rows

**TREATY_BUSINESS_TYPE**
- `None`: 1200 rows

**REINSURER_ID**
- `None`: 1200 rows

**TREATY_ID**
- `None`: 1200 rows

**ACCIDENT_YEAR**
- `None`: 960 rows
- `2025`: 240 rows

**TAX_YEAR**
- `2025`: 1200 rows

**COVERAGE_NUMBER**
- `None`: 1200 rows

**CAT_CODE**
- `None`: 960 rows
- `CAT-014`: 28 rows
- `CAT-015`: 26 rows
- `CAT-002`: 24 rows
- `CAT-004`: 20 rows
- `NON CAT`: 20 rows
- `CAT-009`: 18 rows
- `CAT-011`: 18 rows
- `CAT-005`: 16 rows
- `CAT-001`: 14 rows
- `CAT-007`: 14 rows
- `CAT-008`: 10 rows
- `CAT-006`: 10 rows
- `CAT-003`: 8 rows
- `CAT-010`: 8 rows
- `CAT-013`: 4 rows
- `CAT-012`: 2 rows

**INVOICE_NUMBER**
- `None`: 1200 rows

**CHECK_NUMBER**
- `None`: 1200 rows

**CARRIER_CODE**
- `CAR-002`: 220 rows
- `CAR-005`: 212 rows
- `CAR-003`: 210 rows
- `CAR-004`: 190 rows
- `CAR-007`: 188 rows
- `CAR-001`: 180 rows

**SUBLINE_CODE**
- `PC04`: 336 rows
- `HLT02`: 238 rows
- `PC02`: 148 rows
- `LIF01`: 128 rows
- `LIF05`: 126 rows
- `PC01`: 112 rows
- `HLT01`: 112 rows

**SUBLINE_TYPE**
- `Commercial Property`: 336 rows
- `Group Health`: 238 rows
- `Commercial Auto`: 148 rows
- `Term Life`: 128 rows
- `Group Life`: 126 rows
- `Personal Auto`: 112 rows
- `Individual Health`: 112 rows

**SOURCE_SYSTEM**
- `DAG`: 1200 rows

**BUSINESS_INDICATOR**
- `New Business`: 546 rows
- `Claims Activity`: 488 rows
- `Customer Retention`: 166 rows

**CLAIM_NUMBER**
- `None`: 1120 rows
- `29308-CLM`: 2 rows
- `95378-CLM`: 2 rows
- `24268-CLM`: 2 rows
- `52731-CLM`: 2 rows
- `67644-CLM`: 2 rows
- `14424-CLM`: 2 rows
- `90447-CLM`: 2 rows
- `46350-CLM`: 2 rows
- `91239-CLM`: 2 rows
- `43502-CLM`: 2 rows
- `60241-CLM`: 2 rows
- `20079-CLM`: 2 rows
- `27183-CLM`: 2 rows
- `16358-CLM`: 2 rows
- `26396-CLM`: 2 rows
- `99986-CLM`: 2 rows
- `76742-CLM`: 2 rows
- `14672-CLM`: 2 rows
- `35044-CLM`: 2 rows
- `97066-CLM`: 2 rows
- `93734-CLM`: 2 rows
- `16093-CLM`: 2 rows
- `54801-CLM`: 2 rows
- `48815-CLM`: 2 rows
- `14027-CLM`: 2 rows
- `52043-CLM`: 2 rows
- `75337-CLM`: 2 rows
- `14315-CLM`: 2 rows
- `61402-CLM`: 2 rows
- `24239-CLM`: 2 rows
- `93557-CLM`: 2 rows
- `59768-CLM`: 2 rows
- `48398-CLM`: 2 rows
- `31242-CLM`: 2 rows
- `42866-CLM`: 2 rows
- `61016-CLM`: 2 rows
- `42716-CLM`: 2 rows
- `68213-CLM`: 2 rows
- `76634-CLM`: 2 rows
- `12737-CLM`: 2 rows

**REINSURANCE_LAYER**
- `None`: 1200 rows

**LOSS_TYPE**
- `None`: 476 rows
- `Health`: 382 rows
- `P&C`: 218 rows
- `Auto`: 124 rows

**CAUSE_OF_LOSS**
- `None`: 476 rows
- `Illness`: 238 rows
- `Accidental Injury`: 144 rows
- `Accidental Damage`: 124 rows
- `Fire`: 114 rows
- `Windstorm`: 104 rows

**EXPENSE_TYPE**
- `PREMIUM`: 400 rows
- `RECOVERIES`: 160 rows
- `UNDER WRITING`: 80 rows
- `FEES`: 80 rows
- `CLAIM`: 80 rows
- `TAXES`: 80 rows
- `BROKERAGE`: 80 rows
- `DIRECT`: 80 rows
- `COMMISSION`: 80 rows
- `COMMISSIONS`: 80 rows

**CATEGORIES**
- `None`: 1200 rows

**JOURNAL_LINE_DEF**
- `None`: 1200 rows

**REPORTING_CURRENCY**
- `USD`: 1200 rows

**TXT1**
- `Commercial Property`: 336 rows
- `Group Health`: 238 rows
- `Commercial Auto`: 148 rows
- `Term Life`: 128 rows
- `Group Life`: 126 rows
- `Personal Auto`: 112 rows
- `Individual Health`: 112 rows

**TXT2**
- `None`: 1200 rows

**TXT3**
- `None`: 1200 rows

**TXT4**
- `None`: 1200 rows

**TXT5**
- `None`: 1200 rows

**AMT1**
- `0`: 1200 rows

**AMT2**
- `0`: 1200 rows

**AMT3**
- `0`: 1200 rows

**DATE1**
- `None`: 1200 rows

**DATE2**
- `None`: 1200 rows

**DATE3**
- `None`: 1200 rows

**TXT6**
- `None`: 1200 rows

**TXT7**
- `None`: 1200 rows

**TXT8**
- `None`: 1200 rows

**TXT9**
- `None`: 1200 rows

**TXT10**
- `None`: 1200 rows

**AMT4**
- `0`: 1200 rows

**AMT5**
- `0`: 1200 rows

**AMT6**
- `0`: 1200 rows

**DATE4**
- `None`: 1200 rows

**DATE5**
- `None`: 1200 rows

**DATE6**
- `None`: 1200 rows

**TRANSACTION_DATE**
- `2025-02-28 00:00:00`: 1200 rows

## Profile

Rows in the latest export: 1200.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `JOURNAL_ID` | STRING | 589 | 0 | 01a1623d-cb47-73bf-951e-45f8af88ea18 | 01a1623d-cf01-7ad9-9b58-da5ffc82381b |
| `ORIGIN_JOURNAL_ID` | STRING | 599 | 0 | 0040a466-4f4e-49cb-9469-d23c97a9386e | ff61d583-8954-4e19-9dd0-70d1a05cf84b |
| `CORE_DATE` | DATE | 1 | 0 | 2025-02-28 00:00:00 | 2025-02-28 00:00:00 |
| `JOURNAL_TYPE` | STRING | 1 | 0 | PERM | PERM |
| `ACCOUNTING_CONFIG` | STRING | 1 | 0 | US_GAAP | US_GAAP |
| `ACCOUNT` | STRING | 28 | 0 | 102100 | 529061 |
| `TRANSACTION_AMOUNT` | DECIMAL | 1098 | 0 | -199122 | 199122 |
| `TRANSACTION_CURRENCY` | STRING | 1 | 0 | USD | USD |
| `JOURNAL_LINE_ID` | STRING | 1191 | 0 | 01a1623d-cb47-7032-9e15-e5ad3af31628 | 01a1623d-cf01-7b93-8951-0e59b5098638 |
| `JOURNAL_LINE_NO` | INT | 2 | 0 | 1 | 2 |
| `ORIGIN_JOURNAL_LINE_ID` | STRING | 0 | 1200 |  |  |
| `REVERSES` | STRING | 0 | 1200 |  |  |
| `REVERSED_BY` | STRING | 0 | 1200 |  |  |
| `INGESTION_ID` | STRING | 1 | 0 | in_01a1623bd60375bcaf6a5e553589f894 | in_01a1623bd60375bcaf6a5e553589f894 |
| `FISCAL_YEAR` | INT | 0 | 1200 |  |  |
| `PERIOD` | INT | 0 | 1200 |  |  |
| `FUNCTIONAL_AMOUNT` | DECIMAL | 1098 | 0 | -199122 | 199122 |
| `FUNCTIONAL_CURRENCY` | STRING | 1 | 0 | USD | USD |
| `PARENT_ENTITY` | STRING | 1 | 0 |  |  |
| `CHILD_ENTITY` | STRING | 3 | 0 |  |  |
| `BUSINESS_EVENT` | STRING | 26 | 0 | ASSUMED BROKERAGE | SERVICE FEE DIRECT |
| `COST_CENTER` | STRING | 6 | 0 | Accident Assessment | Underwriting |
| `PROFIT_CENTER` | STRING | 4 | 0 | Auto Insurance | Property & Casualty Insurance |
| `ASLOB` | STRING | 3 | 0 | Health Insurance | Property & Casualty |
| `LOB` | STRING | 3 | 0 | Broker | Direct_Customer |
| `STATE` | STRING | 10 | 0 | Florida | Texas |
| `TREATY_BUSINESS_TYPE` | STRING | 0 | 1200 |  |  |
| `REINSURER_ID` | STRING | 0 | 1200 |  |  |
| `TREATY_ID` | STRING | 0 | 1200 |  |  |
| `ACCIDENT_YEAR` | INT | 1 | 960 | 2025 | 2025 |
| `TAX_YEAR` | INT | 1 | 0 | 2025 | 2025 |
| `COVERAGE_NUMBER` | STRING | 0 | 1200 |  |  |
| `POLICY_VERSION` | STRING | 550 | 0 | ABC101056097-461608-721145-POLTAX-DD-65 | ABC998460277-963699-884761-POLTAX-DD-91 |
| `CAT_CODE` | STRING | 16 | 960 | CAT-001 | NON CAT |
| `INVOICE_NUMBER` | STRING | 0 | 1200 |  |  |
| `CHECK_NUMBER` | STRING | 0 | 1200 |  |  |
| `CARRIER_CODE` | STRING | 6 | 0 | CAR-001 | CAR-007 |
| `INTERCOMPANY` | STRING | 1 | 0 |  |  |
| `SUBLINE_CODE` | STRING | 7 | 0 | HLT01 | PC04 |
| `SUBLINE_TYPE` | STRING | 7 | 0 | Commercial Auto | Term Life |
| `SOURCE_SYSTEM` | STRING | 1 | 0 | DAG | DAG |
| `BUSINESS_INDICATOR` | STRING | 3 | 0 | Claims Activity | New Business |
| `CLAIM_NUMBER` | STRING | 39 | 1120 | 12737-CLM | 99986-CLM |
| `REINSURANCE_LAYER` | STRING | 0 | 1200 |  |  |
| `LOSS_TYPE` | STRING | 3 | 476 | Auto | P&C |
| `CAUSE_OF_LOSS` | STRING | 5 | 476 | Accidental Damage | Windstorm |
| `EXPENSE_TYPE` | STRING | 10 | 0 | BROKERAGE | UNDER WRITING |
| `CATEGORIES` | STRING | 0 | 1200 |  |  |
| `SOURCE_TRANSACTION_ID` | STRING | 615 | 0 | 10431-TXN | 99923-TXN |
| `JOURNAL_LINE_DEF` | STRING | 0 | 1200 |  |  |
| `REPORTING_CURRENCY` | STRING | 1 | 0 | USD | USD |
| `REPORTING_AMOUNT` | DECIMAL | 1098 | 0 | -199122 | 199122 |
| `TXT1` | STRING | 7 | 0 | Commercial Auto | Term Life |
| `TXT2` | STRING | 0 | 1200 |  |  |
| `TXT3` | STRING | 0 | 1200 |  |  |
| `TXT4` | STRING | 0 | 1200 |  |  |
| `TXT5` | STRING | 0 | 1200 |  |  |
| `AMT1` | DECIMAL | 1 | 0 | 0 | 0 |
| `AMT2` | DECIMAL | 1 | 0 | 0 | 0 |
| `AMT3` | DECIMAL | 1 | 0 | 0 | 0 |
| `DATE1` | DATE | 0 | 1200 |  |  |
| `DATE2` | DATE | 0 | 1200 |  |  |
| `DATE3` | DATE | 0 | 1200 |  |  |
| `TXT6` | STRING | 0 | 1200 |  |  |
| `TXT7` | STRING | 0 | 1200 |  |  |
| `TXT8` | STRING | 0 | 1200 |  |  |
| `TXT9` | STRING | 0 | 1200 |  |  |
| `TXT10` | STRING | 0 | 1200 |  |  |
| `AMT4` | DECIMAL | 1 | 0 | 0 | 0 |
| `AMT5` | DECIMAL | 1 | 0 | 0 | 0 |
| `AMT6` | DECIMAL | 1 | 0 | 0 | 0 |
| `DATE4` | DATE | 0 | 1200 |  |  |
| `DATE5` | DATE | 0 | 1200 |  |  |
| `DATE6` | DATE | 0 | 1200 |  |  |
| `TRANSACTION_DATE` | DATE | 1 | 0 | 2025-02-28 00:00:00 | 2025-02-28 00:00:00 |

## Sample rows

| JOURNAL_ID | ORIGIN_JOURNAL_ID | CORE_DATE | JOURNAL_TYPE | ACCOUNTING_CONFIG | ACCOUNT | TRANSACTION_AMOUNT | TRANSACTION_CURRENCY | JOURNAL_LINE_ID | JOURNAL_LINE_NO | ORIGIN_JOURNAL_LINE_ID | REVERSES | REVERSED_BY | INGESTION_ID | FISCAL_YEAR | PERIOD | FUNCTIONAL_AMOUNT | FUNCTIONAL_CURRENCY | BUSINESS_EVENT | COST_CENTER | PROFIT_CENTER | ASLOB | LOB | STATE | TREATY_BUSINESS_TYPE | REINSURER_ID | TREATY_ID | ACCIDENT_YEAR | TAX_YEAR | COVERAGE_NUMBER | POLICY_VERSION | CAT_CODE | INVOICE_NUMBER | CHECK_NUMBER | CARRIER_CODE | SUBLINE_CODE | SUBLINE_TYPE | SOURCE_SYSTEM | BUSINESS_INDICATOR | CLAIM_NUMBER | REINSURANCE_LAYER | LOSS_TYPE | CAUSE_OF_LOSS | EXPENSE_TYPE | CATEGORIES | SOURCE_TRANSACTION_ID | JOURNAL_LINE_DEF | REPORTING_CURRENCY | REPORTING_AMOUNT | TXT1 | TXT2 | TXT3 | TXT4 | TXT5 | AMT1 | AMT2 | AMT3 | DATE1 | DATE2 | DATE3 | TXT6 | TXT7 | TXT8 | TXT9 | TXT10 | AMT4 | AMT5 | AMT6 | DATE4 | DATE5 | DATE6 | TRANSACTION_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01a1623d-ccb0-79d1-ad13-f3fbe55f79a5 | 00aa0fc8-3542-49e5-bb55-2d3f769e7860 | 2025-02-28 00:00:00 | PERM | US_GAAP | 102100 | 661 | USD | 01a1623d-ccb0-7fbf-a83b-5e3ff6ada247 | 1 | NULL | NULL | NULL | in_01a1623bd60375bcaf6a5e553589f894 | NULL | NULL | 661 | USD | INSPECTION FEES | Health Provider Management | Health Insurance | Health Insurance | Broker | Illinois | NULL | NULL | NULL | NULL | 2025 | NULL | ABC465929652-370725-821818-POLTAX-DD-28 | NULL | NULL | NULL | CAR-007 | HLT02 | Group Health | DAG | Customer Retention | NULL | NULL | Health | Accidental Injury | FEES | NULL | 86866-TXN | NULL | USD | 661 | Group Health | NULL | NULL | NULL | NULL | 0 | 0 | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | NULL | NULL | NULL | 2025-02-28 00:00:00 |
| 01a1623d-ccb0-7bd8-b2e5-b9532fb01c68 | fe8d6ff6-4aa3-4894-b4bb-cc2510ba53f2 | 2025-02-28 00:00:00 | PERM | US_GAAP | 102100 | 592 | USD | 01a1623d-ccb0-7286-942f-399b9a06ca6b | 1 | NULL | NULL | NULL | in_01a1623bd60375bcaf6a5e553589f894 | NULL | NULL | 592 | USD | MANAGEMENT FEES RECEIPT | Underwriting | Auto Insurance | Property & Casualty | Broker | Minnesota | NULL | NULL | NULL | NULL | 2025 | NULL | ABC632577373-958679-124133-POLTAX-DD-96 | NULL | NULL | NULL | CAR-003 | PC02 | Commercial Auto | DAG | New Business | NULL | NULL | NULL | NULL | FEES | NULL | 49683-TXN | NULL | USD | 592 | Commercial Auto | NULL | NULL | NULL | NULL | 0 | 0 | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | NULL | NULL | NULL | 2025-02-28 00:00:00 |
| 01a1623d-ccbf-758c-a89a-61aaeebe84d9 | 722d3ab5-e249-4035-b276-66a92ad48d1c | 2025-02-28 00:00:00 | PERM | US_GAAP | 102100 | 294 | USD | 01a1623d-ccbf-7a7f-8bc1-0e2416c2365a | 1 | NULL | NULL | NULL | in_01a1623bd60375bcaf6a5e553589f894 | NULL | NULL | 294 | USD | INSPECTION FEES | Underwriting | Property & Casualty Insurance | Property & Casualty | Broker | Florida | NULL | NULL | NULL | NULL | 2025 | NULL | ABC125692476-430646-684863-POLTAX-DD-12 | NULL | NULL | NULL | CAR-005 | PC04 | Commercial Property | DAG | New Business | NULL | NULL | NULL | NULL | FEES | NULL | 61487-TXN | NULL | USD | 294 | Commercial Property | NULL | NULL | NULL | NULL | 0 | 0 | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | NULL | NULL | NULL | 2025-02-28 00:00:00 |
| 01a1623d-ccc0-7335-999a-462219fba70a | bbaa5436-68d0-4a44-b2b2-62097c59a7fb | 2025-02-28 00:00:00 | PERM | US_GAAP | 102100 | 760 | USD | 01a1623d-ccc0-7724-a8ee-8a1c416cc7a1 | 1 | NULL | NULL | NULL | in_01a1623bd60375bcaf6a5e553589f894 | NULL | NULL | 760 | USD | MANAGEMENT FEES RECEIPT | P&C Claims | Property & Casualty Insurance | Property & Casualty | Broker | New Jersey | NULL | NULL | NULL | NULL | 2025 | NULL | ABC767607682-881648-735386-POLTAX-DD-14 | NULL | NULL | NULL | CAR-002 | PC04 | Commercial Property | DAG | Claims Activity | NULL | NULL | P&C | Windstorm | FEES | NULL | 98062-TXN | NULL | USD | 760 | Commercial Property | NULL | NULL | NULL | NULL | 0 | 0 | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | NULL | NULL | NULL | 2025-02-28 00:00:00 |
| 01a1623d-ccc0-792e-aaa7-21c678822030 | 1ac258db-d090-42e4-acea-6f22c46419f2 | 2025-02-28 00:00:00 | PERM | US_GAAP | 102100 | 627 | USD | 01a1623d-ccc0-7078-b973-aaccba4db84c | 1 | NULL | NULL | NULL | in_01a1623bd60375bcaf6a5e553589f894 | NULL | NULL | 627 | USD | MANAGEMENT FEES RECEIPT | Accident Assessment | Auto Insurance | Property & Casualty | Broker | Oregon | NULL | NULL | NULL | NULL | 2025 | NULL | ABC404128011-861483-226339-POLTAX-DD-68 | NULL | NULL | NULL | CAR-004 | PC02 | Commercial Auto | DAG | Claims Activity | NULL | NULL | Auto | Accidental Damage | FEES | NULL | 21688-TXN | NULL | USD | 627 | Commercial Auto | NULL | NULL | NULL | NULL | 0 | 0 | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | NULL | NULL | NULL | 2025-02-28 00:00:00 |
