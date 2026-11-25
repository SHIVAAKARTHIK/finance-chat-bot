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
row_count: 692
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
- `2024-12-01 00:00:00`: 69 rows
- `2025-01-01 00:00:00`: 64 rows
- `2025-04-01 00:00:00`: 50 rows
- `2025-02-01 00:00:00`: 50 rows
- `2025-11-01 00:00:00`: 48 rows
- `2025-03-01 00:00:00`: 48 rows
- `2025-12-01 00:00:00`: 40 rows
- `2025-08-01 00:00:00`: 36 rows
- `2025-07-01 00:00:00`: 34 rows
- `2025-05-01 00:00:00`: 33 rows
- `2025-06-01 00:00:00`: 33 rows
- `2025-10-01 00:00:00`: 33 rows
- `2025-09-01 00:00:00`: 32 rows
- `2026-05-01 00:00:00`: 26 rows
- `2026-09-01 00:00:00`: 23 rows
- `2026-03-01 00:00:00`: 16 rows
- `2026-08-01 00:00:00`: 11 rows
- `2026-01-01 00:00:00`: 10 rows
- `2026-06-01 00:00:00`: 10 rows
- `2026-04-01 00:00:00`: 10 rows
- `2026-07-01 00:00:00`: 8 rows
- `2026-02-01 00:00:00`: 6 rows
- `2026-10-01 00:00:00`: 2 rows

**POSTING_YEAR**
- `2025`: 501 rows
- `2026`: 122 rows
- `2024`: 69 rows

**POSTING_PERIOD**
- `12`: 109 rows
- `1`: 74 rows
- `3`: 64 rows
- `4`: 60 rows
- `5`: 59 rows
- `2`: 56 rows
- `9`: 55 rows
- `11`: 48 rows
- `8`: 47 rows
- `6`: 43 rows
- `7`: 42 rows
- `10`: 35 rows

**CASH_CATEGORY**
- `Cash and equivalents - corporate`: 337 rows
- `Cash equivalents`: 183 rows
- `Cash and short term investments`: 119 rows
- `Cash and equivalents - fiduciary`: 49 rows
- `Cash, cash equivalent and short-term investments`: 4 rows

**COST_CENTER**
- `None`: 362 rows
- `0`: 122 rows
- `Health Provider Management`: 48 rows
- `Life Operations`: 37 rows
- `Accident Assessment`: 31 rows
- `Health Claims Processing`: 28 rows
- `Underwriting`: 23 rows
- `P&C Claims`: 10 rows
- `Finance`: 5 rows
- `Risk Assessment`: 3 rows
- `Portfolio Management`: 3 rows
- `701`: 3 rows
- `Procurement`: 3 rows
- `Marketing`: 3 rows
- `Wealth Advisory Services`: 3 rows
- `Investment Operations`: 2 rows
- `Human Resources`: 2 rows
- `Information Technology`: 2 rows
- `Internal Audit`: 2 rows

**PROFIT_CENTER**
- `None`: 459 rows
- `Health Insurance`: 79 rows
- `Life Insurance`: 53 rows
- `Auto Insurance`: 42 rows
- `Property & Casualty Insurance`: 21 rows
- `Commercial`: 16 rows
- `Investment & Wealth Management`: 10 rows
- `Personal`: 6 rows
- `0`: 6 rows

**BUSINESS_INDICATOR**
- `None`: 465 rows
- `Claims Activity`: 67 rows
- `New Business`: 65 rows
- `Customer Retention`: 53 rows
- `DIRECT`: 22 rows
- `Policy Renewal`: 10 rows
- `Cross`: 10 rows

**CHANNEL**
- `None`: 487 rows
- `Direct_Customer`: 74 rows
- `Broker`: 70 rows
- `Corporate`: 38 rows
- `Sell / Up`: 10 rows
- `Reinsurance`: 8 rows
- `Individual`: 5 rows

**SLR_BUSINESS_EVENTS**
- `None`: 673 rows
- `INSPECTION FEES`: 6 rows
- `MANAGEMENT FEES RECEIPT`: 5 rows
- `INSPECTION FEES, MANAGEMENT FEES RECEIPT`: 4 rows
- `DIRECT_PAID_LOSS_LAE`: 2 rows
- `DIRECT_PAID_LOSS`: 2 rows

**GL_JOURNAL_CATEGORIES**
- `GeneralJournal`: 487 rows
- `None`: 203 rows
- `Payment`: 2 rows

**SLR_AMOUNT**
- `0`: 673 rows
- `6880`: 1 rows
- `2078`: 1 rows
- `-2609`: 1 rows
- `472`: 1 rows
- `1664`: 1 rows
- `1028`: 1 rows
- `1101`: 1 rows
- `1626`: 1 rows
- `1072`: 1 rows
- `-1717`: 1 rows
- `875`: 1 rows
- `1618`: 1 rows
- `894`: 1 rows
- `-2420`: 1 rows
- `-3658`: 1 rows
- `1384`: 1 rows
- `1891`: 1 rows
- `2073`: 1 rows
- `1030`: 1 rows

**SLR_LINE_COUNT**
- `0`: 673 rows
- `2`: 14 rows
- `4`: 5 rows

**GL_FYNAPSE_LINE_COUNT**
- `0`: 577 rows
- `2`: 52 rows
- `1`: 43 rows
- `4`: 13 rows
- `6`: 7 rows

**GL_OTHER_LINE_COUNT**
- `1`: 274 rows
- `0`: 115 rows
- `2`: 101 rows
- `3`: 59 rows
- `4`: 33 rows
- `5`: 19 rows
- `16`: 10 rows
- `62`: 8 rows
- `10`: 7 rows
- `32`: 6 rows
- `122`: 5 rows
- `6`: 5 rows
- `8`: 4 rows
- `28`: 3 rows
- `9`: 3 rows
- `17`: 2 rows
- `11`: 2 rows
- `96`: 2 rows
- `93`: 2 rows
- `25`: 2 rows
- `190`: 2 rows
- `271`: 1 rows
- `100`: 1 rows
- `279`: 1 rows
- `26`: 1 rows
- `283`: 1 rows
- `269`: 1 rows
- `94`: 1 rows
- `92`: 1 rows
- `285`: 1 rows
- `18`: 1 rows
- `95`: 1 rows
- `7`: 1 rows
- `24`: 1 rows
- `31`: 1 rows
- `15`: 1 rows
- `260`: 1 rows
- `65`: 1 rows
- `34`: 1 rows
- `276`: 1 rows
- `259`: 1 rows
- `350`: 1 rows
- `27`: 1 rows
- `196`: 1 rows
- `477`: 1 rows
- `322`: 1 rows
- `63`: 1 rows
- `273`: 1 rows
- `473`: 1 rows

**RECON_STATUS**
- `GL non-Fynapse activity`: 577 rows
- `GL Fynapse only - missing in SLR`: 96 rows
- `Matched`: 19 rows

## Profile

Rows in the latest export: 692.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `ENTITY` | STRING | 15 | 0 |  |  |
| `POSTING_MONTH` | DATE | 24 | 0 | 2024-12-01 00:00:00 | 2026-10-01 00:00:00 |
| `POSTING_YEAR` | INT | 3 | 0 | 2024 | 2026 |
| `POSTING_PERIOD` | INT | 12 | 0 | 1 | 12 |
| `MAIN_ACCOUNT` | STRING | 65 | 0 | 101100 | 121610 |
| `BANK_ACCOUNT_NAME` | STRING | 63 | 0 | BMO - Claims ZBA - Omega | Wells Fargo Bank |
| `CASH_CATEGORY` | STRING | 5 | 0 | Cash and equivalents - corporate | Cash, cash equivalent and short-term ... |
| `LEDGER_ACCOUNT` | STRING | 199 | 0 | 101100---------- | 121610-Life Operations-Life Insurance... |
| `COST_CENTER` | STRING | 18 | 362 | 0 | Wealth Advisory Services |
| `PROFIT_CENTER` | STRING | 8 | 459 | 0 | Property & Casualty Insurance |
| `BUSINESS_INDICATOR` | STRING | 6 | 465 | Claims Activity | Policy Renewal |
| `CHANNEL` | STRING | 6 | 487 | Broker | Sell / Up |
| `SLR_BUSINESS_EVENTS` | STRING | 5 | 673 | DIRECT_PAID_LOSS | MANAGEMENT FEES RECEIPT |
| `GL_JOURNAL_CATEGORIES` | STRING | 3 | 0 | GeneralJournal | Payment |
| `SLR_AMOUNT` | DECIMAL | 20 | 0 | -3658 | 6880 |
| `GL_FYNAPSE_AMOUNT` | DECIMAL | 73 | 0 | -105883.37 | 3774154.59 |
| `GL_OTHER_AMOUNT` | DECIMAL | 432 | 0 | -51342086.02 | 316035793 |
| `GL_TOTAL_AMOUNT` | DECIMAL | 510 | 0 | -51342086.02 | 316035793 |
| `SLR_VS_GL_VARIANCE` | DECIMAL | 55 | 0 | -3774154.59 | 105883.37 |
| `SLR_LINE_COUNT` | LONG | 3 | 0 | 0 | 4 |
| `GL_FYNAPSE_LINE_COUNT` | LONG | 5 | 0 | 0 | 6 |
| `GL_OTHER_LINE_COUNT` | LONG | 50 | 0 | 0 | 477 |
| `RECON_STATUS` | STRING | 3 | 0 | GL Fynapse only - missing in SLR | Matched |

## Sample rows

| POSTING_MONTH | POSTING_YEAR | POSTING_PERIOD | MAIN_ACCOUNT | BANK_ACCOUNT_NAME | CASH_CATEGORY | LEDGER_ACCOUNT | COST_CENTER | PROFIT_CENTER | BUSINESS_INDICATOR | CHANNEL | SLR_BUSINESS_EVENTS | GL_JOURNAL_CATEGORIES | SLR_AMOUNT | GL_FYNAPSE_AMOUNT | GL_OTHER_AMOUNT | GL_TOTAL_AMOUNT | SLR_VS_GL_VARIANCE | SLR_LINE_COUNT | GL_FYNAPSE_LINE_COUNT | GL_OTHER_LINE_COUNT | RECON_STATUS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2025-07-01 00:00:00 | 2025 | 7 | 109050 | Central Bank CD | Cash equivalents | 109050-Health Provider Management-Hea... | Health Provider Management | Health Insurance | Customer Retention | Corporate | NULL | GeneralJournal | 0 | 0 | 9445 | 9445 | 0 | 0 | 0 | 1 | GL non-Fynapse activity |
| 2025-10-01 00:00:00 | 2025 | 10 | 109053 | CITI Bank | Cash equivalents | 109053----- | NULL | NULL | NULL | NULL | NULL | GeneralJournal | 0 | 0 | 4692 | 4692 | 0 | 0 | 0 | 2 | GL non-Fynapse activity |
| 2026-05-01 00:00:00 | 2026 | 5 | 102100 | Regions - Operating | Cash and equivalents - corporate | 102100-Internal Audit-Property & Casu... | Internal Audit | Property & Casualty Insurance | Customer Retention | Reinsurance | NULL | GeneralJournal | 0 | 545 | 0 | 545 | -545 | 0 | 1 | 0 | GL Fynapse only - missing in SLR |
| 2025-05-01 00:00:00 | 2025 | 5 | 103100 | Wells Fargo - Operating | Cash and equivalents - corporate | 103100-701-----0000---- | 701 | NULL | NULL | NULL | NULL | GeneralJournal | 0 | 0 | -0.01 | -0.01 | 0 | 0 | 0 | 190 | GL non-Fynapse activity |
| 2026-06-01 00:00:00 | 2026 | 6 | 103703 | Wells Fargo - Trade Payables ZBA - THIG | Cash and equivalents - corporate | 103703-----214-0000---- | NULL | NULL | NULL | NULL | NULL | None | 0 | 0 | -2500 | -2500 | 0 | 0 | 0 | 1 | GL non-Fynapse activity |
