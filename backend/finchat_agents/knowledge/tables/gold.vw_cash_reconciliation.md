---
name: vw_cash_reconciliation
schema: gold
layer: gold
domain: cash
type: view
status: active
purpose: Cash reconciliation between Fynapse SLR journals and the general ledger, by entity, month, cash account and ledger
  dimensions
grain: one row per entity; posting month; account and ledger-dimension combination
primary_key:
- ENTITY
- POSTING_MONTH
- MAIN_ACCOUNT
- LEDGER_ACCOUNT
- COST_CENTER
- PROFIT_CENTER
- BUSINESS_INDICATOR
- CHANNEL
entity_column: ENTITY
period_columns:
- POSTING_MONTH
- POSTING_YEAR
- POSTING_PERIOD
pii_columns: []
synonyms: []
built_from:
- fact_fynapse_slr_journals
- fact_kpmg_general_journal_account_entries
- fact_ledger_journal_lines
- dim_main_accounts
known_issues: []
proposed_fields: []
reviewed: false
---

# vw_cash_reconciliation

Cash reconciliation between Fynapse SLR journals and the general ledger, by entity, month, cash account and ledger dimensions

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `ENTITY` | string |  |  | `ENTITY` |
| `POSTING_MONTH` | date |  |  | `POSTING_MONTH` |
| `POSTING_YEAR` | int |  |  | `POSTING_YEAR` |
| `POSTING_PERIOD` | int |  |  | `POSTING_PERIOD` |
| `MAIN_ACCOUNT` | string |  |  | `MAIN_ACCOUNT` |
| `BANK_ACCOUNT_NAME` | string |  |  | `BANK_ACCOUNT_NAME` |
| `CASH_CATEGORY` | string |  |  | `CASH_CATEGORY` |
| `LEDGER_ACCOUNT` | string |  |  | `LEDGER_ACCOUNT` |
| `COST_CENTER` | string |  |  | `COST_CENTER` |
| `PROFIT_CENTER` | string |  |  | `PROFIT_CENTER` |
| `BUSINESS_INDICATOR` | string |  |  | `BUSINESS_INDICATOR` |
| `CHANNEL` | string |  |  | `CHANNEL` |
| `SLR_BUSINESS_EVENTS` | string |  |  | `SLR_BUSINESS_EVENTS` |
| `GL_JOURNAL_CATEGORIES` | string |  |  | `GL_JOURNAL_CATEGORIES` |
| `SLR_AMOUNT` | decimal |  |  | `SLR_AMOUNT` |
| `GL_FYNAPSE_AMOUNT` | decimal |  |  | `GL_FYNAPSE_AMOUNT` |
| `GL_OTHER_AMOUNT` | decimal |  |  | `GL_OTHER_AMOUNT` |
| `GL_TOTAL_AMOUNT` | decimal |  |  | `GL_TOTAL_AMOUNT` |
| `SLR_VS_GL_VARIANCE` | decimal |  |  | `SLR_VS_GL_VARIANCE` |
| `SLR_LINE_COUNT` | long |  |  | `SLR_LINE_COUNT` |
| `GL_FYNAPSE_LINE_COUNT` | long |  |  | `GL_FYNAPSE_LINE_COUNT` |
| `GL_OTHER_LINE_COUNT` | long |  |  | `GL_OTHER_LINE_COUNT` |
| `RECON_STATUS` | string |  |  | `RECON_STATUS` |

## Values

**POSTING_MONTH**
- `2024-12-01 00:00:00`
- `2025-01-01 00:00:00`
- `2025-04-01 00:00:00`
- `2025-02-01 00:00:00`
- `2025-11-01 00:00:00`
- `2025-03-01 00:00:00`
- `2025-12-01 00:00:00`
- `2025-08-01 00:00:00`
- `2025-07-01 00:00:00`
- `2025-05-01 00:00:00`
- `2025-06-01 00:00:00`
- `2025-10-01 00:00:00`
- `2025-09-01 00:00:00`
- `2026-05-01 00:00:00`
- `2026-09-01 00:00:00`
- `2026-03-01 00:00:00`
- `2026-08-01 00:00:00`
- `2026-01-01 00:00:00`
- `2026-06-01 00:00:00`
- `2026-04-01 00:00:00`
- `2026-07-01 00:00:00`
- `2026-02-01 00:00:00`
- `2026-10-01 00:00:00`

**POSTING_YEAR**
- `2025`
- `2026`
- `2024`

**POSTING_PERIOD**
- `12`
- `1`
- `3`
- `4`
- `5`
- `2`
- `9`
- `11`
- `8`
- `6`
- `7`
- `10`

**CASH_CATEGORY**
- `Cash and equivalents - corporate`
- `Cash equivalents`
- `Cash and short term investments`
- `Cash and equivalents - fiduciary`
- `Cash, cash equivalent and short-term investments`

**COST_CENTER**
- `None`
- `0`
- `Health Provider Management`
- `Life Operations`
- `Accident Assessment`
- `Health Claims Processing`
- `Underwriting`
- `P&C Claims`
- `Finance`
- `Risk Assessment`
- `Portfolio Management`
- `701`
- `Procurement`
- `Marketing`
- `Wealth Advisory Services`
- `Investment Operations`
- `Human Resources`
- `Information Technology`
- `Internal Audit`

**PROFIT_CENTER**
- `None`
- `Health Insurance`
- `Life Insurance`
- `Auto Insurance`
- `Property & Casualty Insurance`
- `Commercial`
- `Investment & Wealth Management`
- `Personal`
- `0`

**BUSINESS_INDICATOR**
- `None`
- `Claims Activity`
- `New Business`
- `Customer Retention`
- `DIRECT`
- `Policy Renewal`
- `Cross`

**CHANNEL**
- `None`
- `Direct_Customer`
- `Broker`
- `Corporate`
- `Sell / Up`
- `Reinsurance`
- `Individual`

**SLR_BUSINESS_EVENTS**
- `None`
- `INSPECTION FEES`
- `MANAGEMENT FEES RECEIPT`
- `INSPECTION FEES, MANAGEMENT FEES RECEIPT`
- `DIRECT_PAID_LOSS_LAE`
- `DIRECT_PAID_LOSS`

**GL_JOURNAL_CATEGORIES**
- `GeneralJournal`
- `None`
- `Payment`

**SLR_AMOUNT**
- `0`
- `6880`
- `2078`
- `-2609`
- `472`
- `1664`
- `1028`
- `1101`
- `1626`
- `1072`
- `-1717`
- `875`
- `1618`
- `894`
- `-2420`
- `-3658`
- `1384`
- `1891`
- `2073`
- `1030`

**SLR_LINE_COUNT**
- `0`
- `2`
- `4`

**GL_FYNAPSE_LINE_COUNT**
- `0`
- `2`
- `1`
- `4`
- `6`

**GL_OTHER_LINE_COUNT**
- `1`
- `0`
- `2`
- `3`
- `4`
- `5`
- `16`
- `62`
- `10`
- `32`
- `122`
- `6`
- `8`
- `28`
- `9`
- `17`
- `11`
- `96`
- `93`
- `25`
- `190`
- `271`
- `100`
- `279`
- `26`
- `283`
- `269`
- `94`
- `92`
- `285`
- `18`
- `95`
- `7`
- `24`
- `31`
- `15`
- `260`
- `65`
- `34`
- `276`
- `259`
- `350`
- `27`
- `196`
- `477`
- `322`
- `63`
- `273`
- `473`

**RECON_STATUS**
- `GL non-Fynapse activity`
- `GL Fynapse only - missing in SLR`
- `Matched`
