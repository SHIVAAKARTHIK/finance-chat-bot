---
name: vw_fact_kpmg_general_journals_entries
schema: gold
layer: gold
domain: gl
type: view
status: active
purpose: D365 general journal account entries enriched with accounting; entity and financial-dimension fields.
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
built_from:
- fact_kpmg_general_journal_account_entries
known_issues: []
row_count: 62216
proposed_fields:
- grain
- primary_key
reviewed: false
---

# vw_fact_kpmg_general_journals_entries

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
- `Current`: 61930 rows
- `Operations`: 286 rows

**ACCOUNTING_YEAR**
- `2026`: 30269 rows
- `2025`: 28942 rows
- `2024`: 3005 rows

**ACCOUNTING_MONTH**
- `12`: 10998 rows
- `9`: 7834 rows
- `1`: 6905 rows
- `6`: 5869 rows
- `8`: 5084 rows
- `3`: 4951 rows
- `7`: 4526 rows
- `5`: 4416 rows
- `4`: 4321 rows
- `2`: 3926 rows
- `11`: 2144 rows
- `10`: 1242 rows

**JOURNAL_CATEGORY**
- `GeneralJournal`: 51922 rows
- `None`: 6068 rows
- `FixedAssets`: 3966 rows
- `Vend`: 132 rows
- `Purch`: 110 rows
- `Payment`: 12 rows
- `Allocation`: 6 rows

**TRANSACTION_CURRENCY_CODE**
- `USD`: 61124 rows
- `GBP`: 750 rows
- `EUR`: 235 rows
- `CAD`: 60 rows
- `SEK`: 25 rows
- `AUD`: 14 rows
- `ZAR`: 4 rows
- `NOK`: 4 rows

**IS_CREDIT**
- `No`: 34081 rows
- `Yes`: 28135 rows

**IS_CORRECTION**
- `No`: 62120 rows
- `Yes`: 96 rows

**POSTING_TYPE**
- `LedgerJournal`: 53105 rows
- `None`: 6054 rows
- `FixedAssetsCredit`: 1784 rows
- `Bank`: 851 rows
- `FixedAssetsDebit`: 218 rows
- `VendBalance`: 127 rows
- `PurchExpense`: 55 rows
- `VendSettlement`: 10 rows
- `InterCompany`: 4 rows
- `MSTDiffSecond`: 4 rows
- `MSTDiff`: 3 rows
- `CustBalance`: 1 rows

**LEDGER_NAME**
- `214`: 21465 rows
- `100`: 11227 rows
- `228`: 10170 rows
- `201`: 8916 rows
- `299`: 4097 rows
- `103`: 1957 rows
- `236`: 1159 rows
- `101`: 768 rows
- `UK07`: 718 rows
- `UK03`: 409 rows
- `UK14`: 260 rows
- `233`: 250 rows
- `UK17`: 249 rows
- `208`: 247 rows
- `UK06`: 140 rows
- `238`: 100 rows
- `UK13`: 80 rows
- `230`: 4 rows

**QUANTITY**
- `0`: 62216 rows

**SOURCE_FILE_NAME**
- `kpmggeneraljournalaccountentries__20261116_105417.csv`: 62216 rows

**MDP_CREATED_DATE**
- `2026-11-16 11:42:42.223406+00:00`: 62216 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 11:42:42.223406+00:00`: 62216 rows

**PROFIT_CENTER**
- `None`: 42308 rows
- `Personal`: 10225 rows
- `Health Insurance`: 2120 rows
- `Property & Casualty Insurance`: 1749 rows
- `Life Insurance`: 1497 rows
- `Auto Insurance`: 1481 rows
- `Specialty`: 1023 rows
- `MAR`: 599 rows
- `Commercial`: 407 rows
- `0`: 336 rows
- `Investment & Wealth Management`: 292 rows
- `SLM`: 41 rows
- `CAI`: 35 rows
- `SLA`: 33 rows
- `SLO`: 28 rows
- `FLI`: 14 rows
- `FLM`: 9 rows
- `PRI`: 7 rows
- `PRN`: 5 rows
- `SLP`: 3 rows
- `TRP`: 3 rows
- `FLN`: 1 rows

**LOB**
- `None`: 51807 rows
- `Direct_Customer`: 3098 rows
- `0`: 2868 rows
- `Broker`: 2679 rows
- `Corporate`: 816 rows
- `10`: 400 rows
- `Individual`: 296 rows
- `Reinsurance`: 250 rows
- `18`: 2 rows

## Profile

Rows in the latest export: 62216.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `DATA_AREA_ID` | STRING | 18 | 0 |  |  |
| `GENERAL_JOURNAL_ACCOUNT_ENTRY_REC_ID` | STRING | 65844 | 0 | 5637211376 | 5637313876 |
| `POSTING_LAYER` | STRING | 2 | 0 | Current | Operations |
| `ACCOUNTING_DATE` | DATE | 410 | 0 | 2024-12-31 00:00:00 | 2026-11-02 00:00:00 |
| `ACCOUNTING_YEAR` | INT | 3 | 0 | 2024 | 2026 |
| `ACCOUNTING_MONTH` | INT | 12 | 0 | 1 | 12 |
| `ACCOUNT_DISPLAY_VALUE` | STRING | 2725 | 0 | 101100--------- | 999900--------- |
| `TRANSACTION_CURRENCY_CREDIT_AMOUNT` | STRING | 13311 | 0 | -100 | 9999.6 |
| `DOCUMENT_DATE` | STRING | 111 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 2026-10-18 12:00:00.0000000 +00:00 |
| `DESCRIPTION` | STRING | 20149 | 19312 | 000019\|Vys 5660 Lifefpa Mkwfocz Agahqd | soft drink on Monte Carlo business trip |
| `REPORTING_CURRENCY_AMOUNT` | STRING | 28286 | 0 | -0.01 | 9999.6 |
| `TRANSACTION_CURRENCY_AMOUNT` | STRING | 28819 | 0 | -0.03 | 9999.6 |
| `JOURNAL_CATEGORY` | STRING | 7 | 0 | Allocation | Vend |
| `TRANSACTION_CURRENCY_DEBIT_AMOUNT` | STRING | 15197 | 0 | -100 | 9999.6 |
| `LEDGER_ACCOUNT` | STRING | 4196 | 0 | 101100---------- | 999900----- |
| `TRANSACTION_CURRENCY_CODE` | STRING | 7 | 0 | AUD | ZAR |
| `IS_CREDIT` | STRING | 2 | 0 | No | Yes |
| `ACCOUNTING_CURRENCY_AMOUNT` | STRING | 28880 | 0 | -0.01 | 9999.6 |
| `IS_CORRECTION` | STRING | 2 | 0 | No | Yes |
| `DOCUMENT_NUMBER` | STRING | 54 | 62106 | Inv-001 | Inv-056 |
| `VOUCHER` | STRING | 13912 | 6054 | 100-000000001 | YMH957678142 |
| `POSTING_TYPE` | STRING | 12 | 0 | Bank | VendSettlement |
| `LEDGER_NAME` | STRING | 18 | 0 | 100 | UK17 |
| `JOURNAL_NUMBER` | STRING | 15363 | 0 | 100-000097 | UK17-000066 |
| `ACKNOWLEDGEMENT_DATE` | STRING | 399 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 2026-11-02 12:00:00.0000000 +00:00 |
| `QUANTITY` | STRING | 1 | 0 | 0 | 0 |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | kpmggeneraljournalaccountentries__202... | kpmggeneraljournalaccountentries__202... |
| `HASH_KEY` | STRING | 62739 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:42:42.223000 | 2026-11-16 11:42:42.223000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:42:42.223000 | 2026-11-16 11:42:42.223000 |
| `MAIN_ACCOUNT` | STRING | 437 | 0 | 101100 | 999900 |
| `COST_CENTER` | STRING | 97 | 18882 | 0 | Wealth Advisory Services |
| `PROFIT_CENTER` | STRING | 21 | 42308 | 0 | TRP |
| `BUSINESS_INDICATOR` | STRING | 180 | 6809 | ---- | Up_sell |
| `LOB` | STRING | 8 | 51807 | 0 | Reinsurance |
| `INTERCOMPANY` | STRING | 2 | 57100 |  |  |

## Sample rows

| GENERAL_JOURNAL_ACCOUNT_ENTRY_REC_ID | POSTING_LAYER | ACCOUNTING_DATE | ACCOUNTING_YEAR | ACCOUNTING_MONTH | ACCOUNT_DISPLAY_VALUE | TRANSACTION_CURRENCY_CREDIT_AMOUNT | DOCUMENT_DATE | DESCRIPTION | REPORTING_CURRENCY_AMOUNT | TRANSACTION_CURRENCY_AMOUNT | JOURNAL_CATEGORY | TRANSACTION_CURRENCY_DEBIT_AMOUNT | LEDGER_ACCOUNT | TRANSACTION_CURRENCY_CODE | IS_CREDIT | ACCOUNTING_CURRENCY_AMOUNT | IS_CORRECTION | DOCUMENT_NUMBER | VOUCHER | POSTING_TYPE | LEDGER_NAME | JOURNAL_NUMBER | ACKNOWLEDGEMENT_DATE | QUANTITY | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE | MAIN_ACCOUNT | COST_CENTER | PROFIT_CENTER | BUSINESS_INDICATOR | LOB |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5637271100 | Current | 2026-06-01 00:00:00 | 2026 | 6 | 910000-000-Personal-DIRECT-170--0000--- | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 573701\|Htb 8330 Ztadyfl Hqnsjqk Rnsuow | 96930 | 96930 | GeneralJournal | 96930 | 910000-000-Personal-DIRECT-170--0000---- | USD | No | 96930 | No | NULL | GJV-000000001 | LedgerJournal | 228 | 228-000048 | 1900-01-01 12:00:00.0000000 +00:00 | 0 | kpmggeneraljournalaccountentries__202... | <masked> | 2026-11-16 11:42:42.223000 | <masked> | 2026-11-16 11:42:42.223000 | 910000 | 0 | Personal | DIRECT-170--0000-- | NULL |
| 5637271101 | Current | 2026-06-01 00:00:00 | 2026 | 6 | 910000-000-Personal-DIRECT-270--0000--- | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 941247\|Htb 8330 Ztadyfl Hqnsjqk Rnsuow | 14842.5 | 14842.5 | GeneralJournal | 14842.5 | 910000-000-Personal-DIRECT-270--0000---- | USD | No | 14842.5 | No | NULL | GJV-000000001 | LedgerJournal | 228 | 228-000048 | 1900-01-01 12:00:00.0000000 +00:00 | 0 | kpmggeneraljournalaccountentries__202... | <masked> | 2026-11-16 11:42:42.223000 | <masked> | 2026-11-16 11:42:42.223000 | 910000 | 0 | Personal | DIRECT-270--0000-- | NULL |
| 5637271102 | Current | 2026-06-01 00:00:00 | 2026 | 6 | 911000-000-Personal-DIRECT-010--0000--- | 414240 | 1900-01-01 12:00:00.0000000 +00:00 | 794983\|Htb 8330 Ztadyfl Hqnsjqk Rnsuow | -414240 | -414240 | GeneralJournal | 0 | 911000-000-Personal-DIRECT-010--0000---- | USD | Yes | -414240 | No | NULL | GJV-000000001 | LedgerJournal | 228 | 228-000048 | 1900-01-01 12:00:00.0000000 +00:00 | 0 | kpmggeneraljournalaccountentries__202... | <masked> | 2026-11-16 11:42:42.223000 | <masked> | 2026-11-16 11:42:42.223000 | 911000 | 0 | Personal | DIRECT-010--0000-- | NULL |
| 5637271103 | Current | 2026-06-01 00:00:00 | 2026 | 6 | 911000-000-Personal-DIRECT-021--0000--- | 2476440 | 1900-01-01 12:00:00.0000000 +00:00 | 584000\|Htb 8330 Ztadyfl Hqnsjqk Rnsuow | -2476440 | -2476440 | GeneralJournal | 0 | 911000-000-Personal-DIRECT-021--0000---- | USD | Yes | -2476440 | No | NULL | GJV-000000001 | LedgerJournal | 228 | 228-000048 | 1900-01-01 12:00:00.0000000 +00:00 | 0 | kpmggeneraljournalaccountentries__202... | <masked> | 2026-11-16 11:42:42.223000 | <masked> | 2026-11-16 11:42:42.223000 | 911000 | 0 | Personal | DIRECT-021--0000-- | NULL |
| 5637271104 | Current | 2026-06-01 00:00:00 | 2026 | 6 | 911000-000-Personal-DIRECT-025--0000--- | 9927.5 | 1900-01-01 12:00:00.0000000 +00:00 | 132262\|Htb 8330 Ztadyfl Hqnsjqk Rnsuow | -9927.5 | -9927.5 | GeneralJournal | 0 | 911000-000-Personal-DIRECT-025--0000---- | USD | Yes | -9927.5 | No | NULL | GJV-000000001 | LedgerJournal | 228 | 228-000048 | 1900-01-01 12:00:00.0000000 +00:00 | 0 | kpmggeneraljournalaccountentries__202... | <masked> | 2026-11-16 11:42:42.223000 | <masked> | 2026-11-16 11:42:42.223000 | 911000 | 0 | Personal | DIRECT-025--0000-- | NULL |
