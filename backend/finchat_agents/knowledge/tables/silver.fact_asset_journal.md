---
name: fact_asset_journal
schema: silver
layer: silver
domain: fa
type: table
status: active
purpose: Fixed asset journal lines (acquisitions and depreciation postings) by batch.
grain: one row per HASH_KEY (one fixed asset journal line)
primary_key:
- HASH_KEY
entity_column: DATA_AREA_ID
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues: []
row_count: 1980
proposed_fields:
- grain
- primary_key
reviewed: false
---

# fact_asset_journal

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `DATA_AREA_ID` | string |  |  | `DATA_AREA_ID` |
| `JOURNAL_BATCH_NUMBER` | string |  |  | `JOURNAL_BATCH_NUMBER` |
| `LINE_NUMBER` | string |  |  | `LINE_NUMBER` |
| `ACCOUNT_DISPLAY_VALUE` | string |  |  | `ACCOUNT_DISPLAY_VALUE` |
| `ACCOUNT_TYPE` | string |  |  | `ACCOUNT_TYPE` |
| `BOOK_ID` | string |  |  | `BOOK_ID` |
| `CONSUMPTION_UNITS` | string |  |  | `CONSUMPTION_UNITS` |
| `CREDIT_AMOUNT` | string |  |  | `CREDIT_AMOUNT` |
| `CREDIT_AMOUNT_REPORTING_CURRENCY` | string |  |  | `CREDIT_AMOUNT_REPORTING_CURRENCY` |
| `CURRENCY_CODE` | string |  |  | `CURRENCY_CODE` |
| `DEBIT_AMOUNT` | string |  |  | `DEBIT_AMOUNT` |
| `DEBIT_AMOUNT_REPORTING_CURRENCY` | string |  |  | `DEBIT_AMOUNT_REPORTING_CURRENCY` |
| `DEFAULT_DIMENSION_DISPLAY_VALUE` | string |  |  | `DEFAULT_DIMENSION_DISPLAY_VALUE` |
| `DESCRIPTION` | string |  |  | `DESCRIPTION` |
| `EXCHANGE_RATE` | string |  |  | `EXCHANGE_RATE` |
| `EXCHANGE_RATE_SECONDARY` | string |  |  | `EXCHANGE_RATE_SECONDARY` |
| `IS_POSTED` | string |  |  | `IS_POSTED` |
| `JOURNAL_NAME_ID` | string |  |  | `JOURNAL_NAME_ID` |
| `OFFSET_ACCOUNT_DISPLAY_VALUE` | string |  |  | `OFFSET_ACCOUNT_DISPLAY_VALUE` |
| `OFFSET_ACCOUNT_TYPE` | string |  |  | `OFFSET_ACCOUNT_TYPE` |
| `POSTING_LAYER` | string |  |  | `POSTING_LAYER` |
| `REPORTING_CURRENCY_EXCHANGE_RATE` | string |  |  | `REPORTING_CURRENCY_EXCHANGE_RATE` |
| `REPORTING_CURRENCY_EXCHANGE_RATE_SECONDARY` | string |  |  | `REPORTING_CURRENCY_EXCHANGE_RATE_SECONDARY` |
| `JOURNAL_TEXT` | string |  |  | `JOURNAL_TEXT` |
| `TRANSACTION_TYPE` | string |  |  | `TRANSACTION_TYPE` |
| `TRANS_DATE` | string |  |  | `TRANS_DATE` |
| `VOUCHER` | string |  |  | `VOUCHER` |
| `WORKFLOW_APPROVAL_STATUS` | string |  |  | `WORKFLOW_APPROVAL_STATUS` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**JOURNAL_BATCH_NUMBER**
- `100-000008`: 197 rows
- `100-000010`: 197 rows
- `100-000003`: 197 rows
- `100-000009`: 197 rows
- `100-000006`: 197 rows
- `100-000011`: 197 rows
- `100-000007`: 197 rows
- `100-000012`: 197 rows
- `100-000004`: 197 rows
- `100-000204`: 49 rows
- `100-000205`: 49 rows
- `100-000203`: 49 rows
- `100-000013`: 35 rows
- `100-000129`: 2 rows
- `100-000127`: 2 rows
- `100-000123`: 2 rows
- `100-000128`: 2 rows
- `100-000131`: 1 rows
- `100-000224`: 1 rows
- `100-000225`: 1 rows
- `100-000226`: 1 rows
- `100-000215`: 1 rows
- `100-000132`: 1 rows
- `100-000217`: 1 rows
- `100-000213`: 1 rows
- `100-000212`: 1 rows
- `100-000214`: 1 rows
- `100-000206`: 1 rows
- `100-000216`: 1 rows
- `100-000219`: 1 rows
- `100-000135`: 1 rows
- `100-000211`: 1 rows
- `100-000218`: 1 rows
- `100-000210`: 1 rows

**ACCOUNT_TYPE**
- `FixedAssets`: 1980 rows

**BOOK_ID**
- `GAAP`: 1980 rows

**CONSUMPTION_UNITS**
- `0`: 1980 rows

**CURRENCY_CODE**
- `USD`: 1980 rows

**DEBIT_AMOUNT_REPORTING_CURRENCY**
- `0`: 1980 rows

**DEFAULT_DIMENSION_DISPLAY_VALUE**
- `None`: 1980 rows

**DESCRIPTION**
- `Fixed asset journal`: 1026 rows
- `Depreciation for June 2026`: 197 rows
- `Depreciation for January 2026`: 197 rows
- `Depreciation journal for July 2026`: 197 rows
- `Depreciation journal for August`: 197 rows
- `Depreciation for the month of September - Furniture`: 49 rows
- `Depreciation for the month of Septermber - Buildings`: 49 rows
- `Depreciation for the month of September - Computer`: 49 rows
- `Disposal`: 6 rows
- `Fixed Asset Sale`: 2 rows
- `Disposal pending`: 2 rows
- `Depreciation for AUTO-000020`: 1 rows
- `Depreciation for AUTO-000021`: 1 rows
- `SOFT-000050 - Aquisition`: 1 rows
- `SOFT-000048 - Aquisition`: 1 rows
- `AUTO-000029 - Depreciation`: 1 rows
- `Depreciation for AUTO-000022`: 1 rows
- `SOFT-000049 - Aquisition`: 1 rows
- `Depreciation for AUTO-000023`: 1 rows
- `Depreciation for AUTO-000024`: 1 rows

**EXCHANGE_RATE**
- `100`: 1980 rows

**EXCHANGE_RATE_SECONDARY**
- `0`: 1980 rows

**IS_POSTED**
- `Yes`: 1971 rows
- `No`: 9 rows

**JOURNAL_NAME_ID**
- `FAJ`: 1980 rows

**OFFSET_ACCOUNT_DISPLAY_VALUE**
- `551200---------`: 1766 rows
- `142000---------`: 201 rows
- `552600---------`: 12 rows
- `None`: 1 rows

**OFFSET_ACCOUNT_TYPE**
- `Ledger`: 1980 rows

**POSTING_LAYER**
- `Current`: 1980 rows

**REPORTING_CURRENCY_EXCHANGE_RATE**
- `100`: 1980 rows

**REPORTING_CURRENCY_EXCHANGE_RATE_SECONDARY**
- `0`: 1980 rows

**JOURNAL_TEXT**
- `None`: 216 rows
- `Depr. from 5/1/2026 to 5/31/2026`: 197 rows
- `Depr. from 8/1/2026 to 8/31/2026`: 197 rows
- `Depr. from 6/1/2026 to 6/30/2026`: 197 rows
- `Depr. from 2/1/2026 to 2/28/2026`: 197 rows
- `Depr. from 1/1/2026 to 1/31/2026`: 197 rows
- `Depr. from 3/1/2026 to 3/31/2026`: 197 rows
- `Depr. from 7/1/2026 to 7/31/2026`: 197 rows
- `Depr. from 4/1/2026 to 4/30/2026`: 197 rows
- `Depr. from 9/1/2026 to 9/30/2026`: 182 rows
- `Depr. from 10/1/2026 to 10/31/2026`: 6 rows

**TRANSACTION_TYPE**
- `Depreciation`: 1766 rows
- `Acquisition`: 202 rows
- `DisposalScrap`: 8 rows
- `DisposalSale`: 4 rows

**TRANS_DATE**
- `2026-05-31 12:00:00.0000000 +00:00`: 197 rows
- `2026-01-31 12:00:00.0000000 +00:00`: 197 rows
- `2026-02-28 12:00:00.0000000 +00:00`: 197 rows
- `2026-07-31 12:00:00.0000000 +00:00`: 197 rows
- `2026-01-01 12:00:00.0000000 +00:00`: 197 rows
- `2026-06-30 12:00:00.0000000 +00:00`: 197 rows
- `2026-03-31 12:00:00.0000000 +00:00`: 197 rows
- `2026-04-30 12:00:00.0000000 +00:00`: 197 rows
- `2026-08-31 12:00:00.0000000 +00:00`: 197 rows
- `2026-09-30 12:00:00.0000000 +00:00`: 182 rows
- `2026-10-20 12:00:00.0000000 +00:00`: 8 rows
- `2026-10-31 12:00:00.0000000 +00:00`: 6 rows
- `2026-10-22 12:00:00.0000000 +00:00`: 5 rows
- `2026-10-23 12:00:00.0000000 +00:00`: 2 rows
- `2026-10-21 12:00:00.0000000 +00:00`: 1 rows
- `2026-10-01 12:00:00.0000000 +00:00`: 1 rows
- `2026-11-09 12:00:00.0000000 +00:00`: 1 rows
- `2026-10-14 12:00:00.0000000 +00:00`: 1 rows

**WORKFLOW_APPROVAL_STATUS**
- `Approved`: 1974 rows
- `NotSubmitted`: 3 rows
- `PendingApproval`: 3 rows

**SOURCE_FILE_NAME**
- `assetjournalv2__20261116_105417.csv`: 1980 rows

**MDP_CREATED_DATE**
- `2026-11-16 11:41:41.319882+00:00`: 1980 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 11:41:41.319882+00:00`: 1980 rows

## Profile

Rows in the latest export: 1980.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `DATA_AREA_ID` | STRING | 1 | 0 |  |  |
| `JOURNAL_BATCH_NUMBER` | STRING | 34 | 0 | 100-000003 | 100-000226 |
| `LINE_NUMBER` | STRING | 201 | 0 | -1 | 99 |
| `ACCOUNT_DISPLAY_VALUE` | STRING | 201 | 0 | AUTO\-000001 | SOFT\-000050 |
| `ACCOUNT_TYPE` | STRING | 1 | 0 | FixedAssets | FixedAssets |
| `BOOK_ID` | STRING | 1 | 0 | GAAP | GAAP |
| `CONSUMPTION_UNITS` | STRING | 1 | 0 | 0 | 0 |
| `CREDIT_AMOUNT` | STRING | 390 | 0 | 0 | 98.58 |
| `CREDIT_AMOUNT_REPORTING_CURRENCY` | STRING | 386 | 0 | 0 | 98.58 |
| `CURRENCY_CODE` | STRING | 1 | 0 | USD | USD |
| `DEBIT_AMOUNT` | STRING | 205 | 0 | 0 | 9900 |
| `DEBIT_AMOUNT_REPORTING_CURRENCY` | STRING | 1 | 0 | 0 | 0 |
| `DEFAULT_DIMENSION_DISPLAY_VALUE` | STRING | 0 | 1980 |  |  |
| `DESCRIPTION` | STRING | 20 | 0 | AUTO-000029 - Depreciation | SOFT-000050 - Aquisition |
| `EXCHANGE_RATE` | STRING | 1 | 0 | 100 | 100 |
| `EXCHANGE_RATE_SECONDARY` | STRING | 1 | 0 | 0 | 0 |
| `IS_POSTED` | STRING | 2 | 0 | No | Yes |
| `JOURNAL_NAME_ID` | STRING | 1 | 0 | FAJ | FAJ |
| `OFFSET_ACCOUNT_DISPLAY_VALUE` | STRING | 3 | 1 | 142000--------- | 552600--------- |
| `OFFSET_ACCOUNT_TYPE` | STRING | 1 | 0 | Ledger | Ledger |
| `POSTING_LAYER` | STRING | 1 | 0 | Current | Current |
| `REPORTING_CURRENCY_EXCHANGE_RATE` | STRING | 1 | 0 | 100 | 100 |
| `REPORTING_CURRENCY_EXCHANGE_RATE_SECONDARY` | STRING | 1 | 0 | 0 | 0 |
| `JOURNAL_TEXT` | STRING | 10 | 216 | Depr. from 1/1/2026 to 1/31/2026 | Depr. from 9/1/2026 to 9/30/2026 |
| `TRANSACTION_TYPE` | STRING | 4 | 0 | Acquisition | DisposalScrap |
| `TRANS_DATE` | STRING | 17 | 0 | 2026-01-01 12:00:00.0000000 +00:00 | 2026-11-09 12:00:00.0000000 +00:00 |
| `VOUCHER` | STRING | 1880 | 0 | FAJ-000000001 | FAJ-000001984 |
| `WORKFLOW_APPROVAL_STATUS` | STRING | 3 | 0 | Approved | PendingApproval |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | assetjournalv2__20261116_105417.csv | assetjournalv2__20261116_105417.csv |
| `HASH_KEY` | STRING | 1971 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:41:41.320000 | 2026-11-16 11:41:41.320000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:41:41.320000 | 2026-11-16 11:41:41.320000 |

## Sample rows

| JOURNAL_BATCH_NUMBER | LINE_NUMBER | ACCOUNT_DISPLAY_VALUE | ACCOUNT_TYPE | BOOK_ID | CONSUMPTION_UNITS | CREDIT_AMOUNT | CREDIT_AMOUNT_REPORTING_CURRENCY | CURRENCY_CODE | DEBIT_AMOUNT | DEBIT_AMOUNT_REPORTING_CURRENCY | DEFAULT_DIMENSION_DISPLAY_VALUE | DESCRIPTION | EXCHANGE_RATE | EXCHANGE_RATE_SECONDARY | IS_POSTED | JOURNAL_NAME_ID | OFFSET_ACCOUNT_DISPLAY_VALUE | OFFSET_ACCOUNT_TYPE | POSTING_LAYER | REPORTING_CURRENCY_EXCHANGE_RATE | REPORTING_CURRENCY_EXCHANGE_RATE_SECONDARY | JOURNAL_TEXT | TRANSACTION_TYPE | TRANS_DATE | VOUCHER | WORKFLOW_APPROVAL_STATUS | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 100-000003 | 1 | AUTO\-000001 | FixedAssets | GAAP | 0 | 0 | 0 | USD | 1000 | 0 | NULL | Fixed asset journal | 100 | 0 | Yes | FAJ | 142000--------- | Ledger | Current | 100 | 0 | NULL | Acquisition | 2026-01-01 12:00:00.0000000 +00:00 | FAJ-000000001 | Approved | assetjournalv2__20261116_105417.csv | <masked> | 2026-11-16 11:41:41.320000 | <masked> | 2026-11-16 11:41:41.320000 |
| 100-000003 | 149 | AUTO\-000002 | FixedAssets | GAAP | 0 | 0 | 0 | USD | 15800 | 0 | NULL | Fixed asset journal | 100 | 0 | Yes | FAJ | 142000--------- | Ledger | Current | 100 | 0 | NULL | Acquisition | 2026-01-01 12:00:00.0000000 +00:00 | FAJ-000000149 | Approved | assetjournalv2__20261116_105417.csv | <masked> | 2026-11-16 11:41:41.320000 | <masked> | 2026-11-16 11:41:41.320000 |
| 100-000003 | 150 | AUTO\-000003 | FixedAssets | GAAP | 0 | 0 | 0 | USD | 15900 | 0 | NULL | Fixed asset journal | 100 | 0 | Yes | FAJ | 142000--------- | Ledger | Current | 100 | 0 | NULL | Acquisition | 2026-01-01 12:00:00.0000000 +00:00 | FAJ-000000150 | Approved | assetjournalv2__20261116_105417.csv | <masked> | 2026-11-16 11:41:41.320000 | <masked> | 2026-11-16 11:41:41.320000 |
| 100-000003 | 151 | AUTO\-000004 | FixedAssets | GAAP | 0 | 0 | 0 | USD | 16000 | 0 | NULL | Fixed asset journal | 100 | 0 | Yes | FAJ | 142000--------- | Ledger | Current | 100 | 0 | NULL | Acquisition | 2026-01-01 12:00:00.0000000 +00:00 | FAJ-000000151 | Approved | assetjournalv2__20261116_105417.csv | <masked> | 2026-11-16 11:41:41.320000 | <masked> | 2026-11-16 11:41:41.320000 |
| 100-000003 | 152 | AUTO\-000005 | FixedAssets | GAAP | 0 | 0 | 0 | USD | 16100 | 0 | NULL | Fixed asset journal | 100 | 0 | Yes | FAJ | 142000--------- | Ledger | Current | 100 | 0 | NULL | Acquisition | 2026-01-01 12:00:00.0000000 +00:00 | FAJ-000000152 | Approved | assetjournalv2__20261116_105417.csv | <masked> | 2026-11-16 11:41:41.320000 | <masked> | 2026-11-16 11:41:41.320000 |
