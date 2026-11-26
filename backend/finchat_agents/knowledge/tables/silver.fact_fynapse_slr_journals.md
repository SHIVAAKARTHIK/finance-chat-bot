---
name: fact_fynapse_slr_journals
schema: silver
layer: silver
domain: subledger
type: fact
status: active
purpose: 'Fynapse subledger journal lines: one row per journal line with parent entity, fiscal year and period, source system,
  journal type, business event, account and amounts in transaction, functional and reporting currency.'
grain: one row per journal line (JOURNAL_LINE_ID)
primary_key:
- JOURNAL_LINE_ID
entity_column: PARENT_ENTITY
period_columns:
- FISCAL_YEAR
- PERIOD
- CORE_DATE
pii_columns: []
synonyms:
- fynapse
- subledger
- sub ledger
- slr
- journal lines
- journal line
- journals
- slr journals
- source system
- business event
known_issues:
- code: entity_values_changing
  note: PARENT_ENTITY values were recently changed by the data team (being confirmed). Never assume entity values; check current
    values with get_column_values on PARENT_ENTITY before filtering, and say so if a requested entity is not present.
- code: empty_column
  note: LOB is empty on all lines and REVERSES is not populated; say so instead of inventing categories.
- code: empty_column
  note: FISCAL_YEAR and PERIOD are NULL on all 1200 lines in the current data (checked in Databricks). A filter on them returns
    no rows. Use CORE_DATE for every period or month question and tell the user the fiscal period columns are empty.
reviewed: true
proposed_fields: []
---

# fact_fynapse_slr_journals

Fynapse subledger journal lines: one row per journal line with parent entity, fiscal year and period, source system,
journal type, business event, account and amounts in transaction, functional and reporting currency.

> Columns have real types here (numbers are numbers, CORE_DATE is a date); no casting needed.
> Entity = PARENT_ENTITY. Check its current values with `get_column_values`; they changed recently.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `JOURNAL_LINE_ID` | string | Unique journal line id (grain). | journal line | `JOURNAL_LINE_ID` |
| `JOURNAL_ID` | string | Journal id; a journal has several lines. "How many journals" = COUNT(DISTINCT JOURNAL_ID). | journal, journals, journal id | `JOURNAL_ID` |
| `JOURNAL_LINE_NO` | integer | Line number within the journal. | line number | `JOURNAL_LINE_NO` |
| `PARENT_ENTITY` | string | Legal entity code. This is THE entity column. | entity, legal entity, parent entity, company | `PARENT_ENTITY` |
| `CHILD_ENTITY` | string | Sub-unit within the entity, often empty. Not the legal entity. | child entity, sub entity, sub-unit | `CHILD_ENTITY` |
| `FISCAL_YEAR` | integer | Fiscal year, e.g. 2026. | fiscal year, year | `FISCAL_YEAR` |
| `PERIOD` | integer | Fiscal period number within FISCAL_YEAR (map a month via CORE_DATE). | fiscal period, period | `PERIOD` |
| `CORE_DATE` | date | Period month-end date; use it to map a month name to FISCAL_YEAR + PERIOD. | date, posting date, month | `CORE_DATE` |
| `SOURCE_SYSTEM` | string | Upstream source system. | source system, source, integration | `SOURCE_SYSTEM` |
| `JOURNAL_TYPE` | string | Journal type. | journal type | `JOURNAL_TYPE` |
| `ACCOUNT` | string | GL account. | account, gl account | `ACCOUNT` |
| `BUSINESS_EVENT` | string | Business event that created the line. | business event, event | `BUSINESS_EVENT` |
| `LOB` | string | Line of business (currently empty on all lines). | line of business, lob | `LOB` |
| `COST_CENTER` | string | Cost center. | cost center, cost centre | `COST_CENTER` |
| `REVERSES` | string | Populated when this line reverses another line. | reversal, reversals, reverses | `REVERSES` |
| `TRANSACTION_CURRENCY` | string | Transaction currency. | transaction currency, currency | `TRANSACTION_CURRENCY` |
| `TRANSACTION_AMOUNT` | decimal | Amount in transaction currency. | transaction amount | `TRANSACTION_AMOUNT` |
| `FUNCTIONAL_CURRENCY` | string | Functional currency of the entity. | functional currency | `FUNCTIONAL_CURRENCY` |
| `FUNCTIONAL_AMOUNT` | decimal | Amount in functional currency. | functional amount | `FUNCTIONAL_AMOUNT` |
| `REPORTING_CURRENCY` | string | Reporting currency. | reporting currency | `REPORTING_CURRENCY` |
| `REPORTING_AMOUNT` | decimal | Amount in reporting currency (signed). "Net" = SUM; "gross" = SUM(ABS()). | reporting amount, amount, net amount, net, gross amount | `REPORTING_AMOUNT` |
| `ORIGIN_JOURNAL_ID` | string |  |  | `ORIGIN_JOURNAL_ID` |
| `ACCOUNTING_CONFIG` | string |  |  | `ACCOUNTING_CONFIG` |
| `ORIGIN_JOURNAL_LINE_ID` | string |  |  | `ORIGIN_JOURNAL_LINE_ID` |
| `REVERSED_BY` | string |  |  | `REVERSED_BY` |
| `INGESTION_ID` | string |  |  | `INGESTION_ID` |
| `PROFIT_CENTER` | string |  |  | `PROFIT_CENTER` |
| `ASLOB` | string |  |  | `ASLOB` |
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
| `BUSINESS_INDICATOR` | string |  |  | `BUSINESS_INDICATOR` |
| `CLAIM_NUMBER` | string |  |  | `CLAIM_NUMBER` |
| `REINSURANCE_LAYER` | string |  |  | `REINSURANCE_LAYER` |
| `LOSS_TYPE` | string |  |  | `LOSS_TYPE` |
| `CAUSE_OF_LOSS` | string |  |  | `CAUSE_OF_LOSS` |
| `EXPENSE_TYPE` | string |  |  | `EXPENSE_TYPE` |
| `CATEGORIES` | string |  |  | `CATEGORIES` |
| `SOURCE_TRANSACTION_ID` | string |  |  | `SOURCE_TRANSACTION_ID` |
| `JOURNAL_LINE_DEF` | string |  |  | `JOURNAL_LINE_DEF` |
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

**SOURCE_SYSTEM**
- `NOVIDEA`: brokerage accounting
- `ACCRUAL`: accrued brokerage
- `Concur`: expenses
- `DAG`

**CORE_DATE**
- `2025-02-28 00:00:00`

**JOURNAL_TYPE**
- `PERM`

**ACCOUNTING_CONFIG**
- `US_GAAP`

**ACCOUNT**
- `145100`
- `141121`
- `522110`
- `192200`
- `411100`
- `141111`
- `512110`
- `511110`
- `102100`
- `521120`
- `412100`
- `212100`
- `521124`
- `412200`
- `521310`
- `411200`
- `212200`
- `146100`
- `522210`
- `222110`
- `529061`
- `211211`
- `511210`
- `102403`
- `512210`
- `211111`
- `211221`
- `512310`
- `211121`
- `511310`

**TRANSACTION_CURRENCY**
- `USD`

**JOURNAL_LINE_NO**
- `1`
- `2`

**ORIGIN_JOURNAL_LINE_ID**
- `None`

**REVERSES**
- `None`

**REVERSED_BY**
- `None`

**INGESTION_ID**
- `in_01a1623bd60375bcaf6a5e553589f894`

**FISCAL_YEAR**
- `None`

**PERIOD**
- `None`

**FUNCTIONAL_CURRENCY**
- `USD`

**BUSINESS_EVENT**
- `DIRECT WRITTEN PREMIUM`
- `DIRECT_UPR_CHANGE`
- `DIRECT_LOSS_RECOVERIES_LAE`
- `DIRECT_COMMISSIONS`
- `ASSUMED UPR CHANGE`
- `ASSUMED COMMISSIONS`
- `SERVICE FEE DIRECT`
- `ASSUMED BROKERAGE`
- `ASSUMED WRITTEN PREMIUM`
- `PREMIUM WRITE OFFS`
- `DIRECT_LOSS_RECOVERIES`
- `MANAGEMENT FEES RECEIPT`
- `DEFERRED_PREMIUM_TAXES`
- `INSPECTION FEES`
- `PREMIUM_TAXES`
- `DIRECT SALVAGE SUBRO RECOVERABLE LOSSES`
- `DIRECT CASE CHANGE LAE`
- `DIRECT SALVAGE SUBRO RECOVERABLE LAE`
- `DIRECT CASE CHANGE LOSS`
- `DIRECT_PAID_LOSS_LAE`
- `DIRECT_CASE_CHANGE_RESERVE_LOSS_LAE`
- `DIRECT IBNR CHANGE LOSS`
- `DIRECT IBNR CHANGE LAE`
- `DIRECT_PAID_LOSS`
- `DIRECT_CASE_CHANGE_RESERVE_LOSS`

**COST_CENTER**
- `Underwriting`
- `P&C Claims`
- `Health Provider Management`
- `Accident Assessment`
- `Health Claims Processing`
- `Life Operations`

**PROFIT_CENTER**
- `Health Insurance`
- `Property & Casualty Insurance`
- `Auto Insurance`
- `Life Insurance`

**ASLOB**
- `Property & Casualty`
- `Health Insurance`
- `Life Insurance`

**LOB**
- `Broker`
- `Direct_Customer`
- `Corporate`

**STATE**
- `New Jersey`
- `Indiana`
- `Michigan`
- `Massachusetts`
- `Illinois`
- `Minnesota`
- `Ohio`
- `Florida`
- `Texas`
- `Oregon`

**TREATY_BUSINESS_TYPE**
- `None`

**REINSURER_ID**
- `None`

**TREATY_ID**
- `None`

**ACCIDENT_YEAR**
- `None`
- `2025`

**TAX_YEAR**
- `2025`

**COVERAGE_NUMBER**
- `None`

**CAT_CODE**
- `None`
- `CAT-014`
- `CAT-015`
- `CAT-002`
- `CAT-004`
- `NON CAT`
- `CAT-009`
- `CAT-011`
- `CAT-005`
- `CAT-001`
- `CAT-007`
- `CAT-008`
- `CAT-006`
- `CAT-003`
- `CAT-010`
- `CAT-013`
- `CAT-012`

**INVOICE_NUMBER**
- `None`

**CHECK_NUMBER**
- `None`

**CARRIER_CODE**
- `CAR-002`
- `CAR-005`
- `CAR-003`
- `CAR-004`
- `CAR-007`
- `CAR-001`

**SUBLINE_CODE**
- `PC04`
- `HLT02`
- `PC02`
- `LIF01`
- `LIF05`
- `PC01`
- `HLT01`

**SUBLINE_TYPE**
- `Commercial Property`
- `Group Health`
- `Commercial Auto`
- `Term Life`
- `Group Life`
- `Personal Auto`
- `Individual Health`

**BUSINESS_INDICATOR**
- `New Business`
- `Claims Activity`
- `Customer Retention`

**CLAIM_NUMBER**
- `None`
- `29308-CLM`
- `95378-CLM`
- `24268-CLM`
- `52731-CLM`
- `67644-CLM`
- `14424-CLM`
- `90447-CLM`
- `46350-CLM`
- `91239-CLM`
- `43502-CLM`
- `60241-CLM`
- `20079-CLM`
- `27183-CLM`
- `16358-CLM`
- `26396-CLM`
- `99986-CLM`
- `76742-CLM`
- `14672-CLM`
- `35044-CLM`
- `97066-CLM`
- `93734-CLM`
- `16093-CLM`
- `54801-CLM`
- `48815-CLM`
- `14027-CLM`
- `52043-CLM`
- `75337-CLM`
- `14315-CLM`
- `61402-CLM`
- `24239-CLM`
- `93557-CLM`
- `59768-CLM`
- `48398-CLM`
- `31242-CLM`
- `42866-CLM`
- `61016-CLM`
- `42716-CLM`
- `68213-CLM`
- `76634-CLM`
- `12737-CLM`

**REINSURANCE_LAYER**
- `None`

**LOSS_TYPE**
- `None`
- `Health`
- `P&C`
- `Auto`

**CAUSE_OF_LOSS**
- `None`
- `Illness`
- `Accidental Injury`
- `Accidental Damage`
- `Fire`
- `Windstorm`

**EXPENSE_TYPE**
- `PREMIUM`
- `RECOVERIES`
- `UNDER WRITING`
- `FEES`
- `CLAIM`
- `TAXES`
- `BROKERAGE`
- `DIRECT`
- `COMMISSION`
- `COMMISSIONS`

**CATEGORIES**
- `None`

**JOURNAL_LINE_DEF**
- `None`

**REPORTING_CURRENCY**
- `USD`

**TXT1**
- `Commercial Property`
- `Group Health`
- `Commercial Auto`
- `Term Life`
- `Group Life`
- `Personal Auto`
- `Individual Health`

**TXT2**
- `None`

**TXT3**
- `None`

**TXT4**
- `None`

**TXT5**
- `None`

**AMT1**
- `0`

**AMT2**
- `0`

**AMT3**
- `0`

**DATE1**
- `None`

**DATE2**
- `None`

**DATE3**
- `None`

**TXT6**
- `None`

**TXT7**
- `None`

**TXT8**
- `None`

**TXT9**
- `None`

**TXT10**
- `None`

**AMT4**
- `0`

**AMT5**
- `0`

**AMT6**
- `0`

**DATE4**
- `None`

**DATE5**
- `None`

**DATE6**
- `None`

**TRANSACTION_DATE**
- `2025-02-28 00:00:00`

## Empty columns

Empty in every row: `ORIGIN_JOURNAL_LINE_ID`, `REVERSES`, `REVERSED_BY`, `FISCAL_YEAR`, `PERIOD`, `TREATY_BUSINESS_TYPE`, `REINSURER_ID`, `TREATY_ID`, `COVERAGE_NUMBER`, `INVOICE_NUMBER`, `CHECK_NUMBER`, `REINSURANCE_LAYER`, `CATEGORIES`, `JOURNAL_LINE_DEF`, `TXT2`, `TXT3`, `TXT4`, `TXT5`, `DATE1`, `DATE2`, `DATE3`, `TXT6`, `TXT7`, `TXT8`, `TXT9`, `TXT10`, `DATE4`, `DATE5`, `DATE6`. Do not filter or group on them.

## Named metrics

| Metric | Meaning | SQL | Additivity |
|---|---|---|---|
| `journal_line_count` | Number of journal lines. | `COUNT(*)` | additive |
| `journal_count` | Number of distinct journals. | `COUNT(DISTINCT JOURNAL_ID)` | non additive |
| `net_reporting_amount` | Net amount in reporting currency; a balanced subledger nets to about zero. | `SUM(REPORTING_AMOUNT)` | additive |
| `gross_reporting_amount` | Gross amount in reporting currency. | `SUM(ABS(REPORTING_AMOUNT))` | additive |

## Notes

- Period: FISCAL_YEAR and PERIOD are NULL on every row in the current data, so do NOT filter on them. Filter on CORE_DATE
  (for a month: `CORE_DATE >= DATE '2026-09-01' AND CORE_DATE < DATE '2026-10-01'`) and say that the fiscal period columns
  are empty. If a later load fills them, `SELECT DISTINCT FISCAL_YEAR, PERIOD, CORE_DATE` shows the mapping; never guess a period number.
- Revenue, P&L and trial-balance questions are not answerable from this subledger; say so instead of substituting
  journal amounts.
- Share of total only for counts or non-negative amounts.
- No approved joins to other tables yet.
