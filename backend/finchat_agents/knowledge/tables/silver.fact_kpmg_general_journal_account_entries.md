---
name: fact_kpmg_general_journal_account_entries
schema: silver
layer: silver
domain: gl
type: table
status: active
purpose: D365 general journal account entries (posted GL lines).
grain: one row per GENERAL_JOURNAL_ACCOUNT_ENTRY_REC_ID (one GL posting line)
primary_key:
- GENERAL_JOURNAL_ACCOUNT_ENTRY_REC_ID
entity_column: DATA_AREA_ID
period_columns:
- ACCOUNTING_DATE
- ACCOUNTING_YEAR
- ACCOUNTING_MONTH
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues: []
proposed_fields:
- grain
- primary_key
reviewed: false
---

# fact_kpmg_general_journal_account_entries

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `DATA_AREA_ID` | string |  |  | `DATA_AREA_ID` |
| `GENERAL_JOURNAL_ACCOUNT_ENTRY_REC_ID` | string |  |  | `GENERAL_JOURNAL_ACCOUNT_ENTRY_REC_ID` |
| `POSTING_LAYER` | string |  |  | `POSTING_LAYER` |
| `ACCOUNTING_DATE` | date |  |  | `ACCOUNTING_DATE` |
| `ACCOUNTING_YEAR` | int |  |  | `ACCOUNTING_YEAR` |
| `ACCOUNTING_MONTH` | int |  |  | `ACCOUNTING_MONTH` |
| `ACCOUNT_DISPLAY_VALUE` | string |  |  | `ACCOUNT_DISPLAY_VALUE` |
| `TRANSACTION_CURRENCY_CREDIT_AMOUNT` | string |  |  | `TRANSACTION_CURRENCY_CREDIT_AMOUNT` |
| `DOCUMENT_DATE` | string |  |  | `DOCUMENT_DATE` |
| `DESCRIPTION` | string |  |  | `DESCRIPTION` |
| `REPORTING_CURRENCY_AMOUNT` | string |  |  | `REPORTING_CURRENCY_AMOUNT` |
| `TRANSACTION_CURRENCY_AMOUNT` | string |  |  | `TRANSACTION_CURRENCY_AMOUNT` |
| `JOURNAL_CATEGORY` | string |  |  | `JOURNAL_CATEGORY` |
| `TRANSACTION_CURRENCY_DEBIT_AMOUNT` | string |  |  | `TRANSACTION_CURRENCY_DEBIT_AMOUNT` |
| `LEDGER_ACCOUNT` | string |  |  | `LEDGER_ACCOUNT` |
| `TRANSACTION_CURRENCY_CODE` | string |  |  | `TRANSACTION_CURRENCY_CODE` |
| `IS_CREDIT` | string |  |  | `IS_CREDIT` |
| `ACCOUNTING_CURRENCY_AMOUNT` | string |  |  | `ACCOUNTING_CURRENCY_AMOUNT` |
| `IS_CORRECTION` | string |  |  | `IS_CORRECTION` |
| `DOCUMENT_NUMBER` | string |  |  | `DOCUMENT_NUMBER` |
| `VOUCHER` | string |  |  | `VOUCHER` |
| `POSTING_TYPE` | string |  |  | `POSTING_TYPE` |
| `LEDGER_NAME` | string |  |  | `LEDGER_NAME` |
| `JOURNAL_NUMBER` | string |  |  | `JOURNAL_NUMBER` |
| `ACKNOWLEDGEMENT_DATE` | string |  |  | `ACKNOWLEDGEMENT_DATE` |
| `QUANTITY` | string |  |  | `QUANTITY` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |
| `MAIN_ACCOUNT` | string |  |  | `MAIN_ACCOUNT` |
| `COST_CENTER` | string |  |  | `COST_CENTER` |
| `PROFIT_CENTER` | string |  |  | `PROFIT_CENTER` |
| `BUSINESS_INDICATOR` | string |  |  | `BUSINESS_INDICATOR` |
| `LOB` | string |  |  | `LOB` |
| `INTERCOMPANY` | string |  |  | `INTERCOMPANY` |

## Values

**POSTING_LAYER**
- `Current`
- `Operations`

**ACCOUNTING_YEAR**
- `2026`
- `2025`
- `2024`

**ACCOUNTING_MONTH**
- `12`
- `9`
- `1`
- `6`
- `8`
- `3`
- `7`
- `5`
- `4`
- `2`
- `11`
- `10`

**JOURNAL_CATEGORY**
- `GeneralJournal`
- `None`
- `FixedAssets`
- `Vend`
- `Purch`
- `Payment`
- `Allocation`

**TRANSACTION_CURRENCY_CODE**
- `USD`
- `GBP`
- `EUR`
- `CAD`
- `SEK`
- `AUD`
- `ZAR`
- `NOK`

**IS_CREDIT**
- `No`
- `Yes`

**IS_CORRECTION**
- `No`
- `Yes`

**POSTING_TYPE**
- `LedgerJournal`
- `None`
- `FixedAssetsCredit`
- `Bank`
- `FixedAssetsDebit`
- `VendBalance`
- `PurchExpense`
- `VendSettlement`
- `InterCompany`
- `MSTDiffSecond`
- `MSTDiff`
- `CustBalance`

**LEDGER_NAME**
- `214`
- `100`
- `228`
- `201`
- `299`
- `103`
- `236`
- `101`
- `UK07`
- `UK03`
- `UK14`
- `233`
- `UK17`
- `208`
- `UK06`
- `238`
- `UK13`
- `230`

**QUANTITY**
- `0`

**SOURCE_FILE_NAME**
- `kpmggeneraljournalaccountentries__20261116_105417.csv`

**MDP_CREATED_DATE**
- `2026-11-16 11:42:42.223406+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 11:42:42.223406+00:00`

**PROFIT_CENTER**
- `None`
- `Personal`
- `Health Insurance`
- `Property & Casualty Insurance`
- `Life Insurance`
- `Auto Insurance`
- `Specialty`
- `MAR`
- `Commercial`
- `0`
- `Investment & Wealth Management`
- `SLM`
- `CAI`
- `SLA`
- `SLO`
- `FLI`
- `FLM`
- `PRI`
- `PRN`
- `SLP`
- `TRP`
- `FLN`

**LOB**
- `None`
- `Direct_Customer`
- `0`
- `Broker`
- `Corporate`
- `10`
- `Individual`
- `Reinsurance`
- `18`
