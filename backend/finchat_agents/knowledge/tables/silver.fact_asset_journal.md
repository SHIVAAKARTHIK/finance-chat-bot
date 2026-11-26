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
- `100-000008`
- `100-000010`
- `100-000003`
- `100-000009`
- `100-000006`
- `100-000011`
- `100-000007`
- `100-000012`
- `100-000004`
- `100-000204`
- `100-000205`
- `100-000203`
- `100-000013`
- `100-000129`
- `100-000127`
- `100-000123`
- `100-000128`
- `100-000131`
- `100-000224`
- `100-000225`
- `100-000226`
- `100-000215`
- `100-000132`
- `100-000217`
- `100-000213`
- `100-000212`
- `100-000214`
- `100-000206`
- `100-000216`
- `100-000219`
- `100-000135`
- `100-000211`
- `100-000218`
- `100-000210`

**ACCOUNT_TYPE**
- `FixedAssets`

**BOOK_ID**
- `GAAP`

**CONSUMPTION_UNITS**
- `0`

**CURRENCY_CODE**
- `USD`

**DEBIT_AMOUNT_REPORTING_CURRENCY**
- `0`

**DEFAULT_DIMENSION_DISPLAY_VALUE**
- `None`

**DESCRIPTION**
- `Fixed asset journal`
- `Depreciation for June 2026`
- `Depreciation for January 2026`
- `Depreciation journal for July 2026`
- `Depreciation journal for August`
- `Depreciation for the month of September - Furniture`
- `Depreciation for the month of Septermber - Buildings`
- `Depreciation for the month of September - Computer`
- `Disposal`
- `Fixed Asset Sale`
- `Disposal pending`
- `Depreciation for AUTO-000020`
- `Depreciation for AUTO-000021`
- `SOFT-000050 - Aquisition`
- `SOFT-000048 - Aquisition`
- `AUTO-000029 - Depreciation`
- `Depreciation for AUTO-000022`
- `SOFT-000049 - Aquisition`
- `Depreciation for AUTO-000023`
- `Depreciation for AUTO-000024`

**EXCHANGE_RATE**
- `100`

**EXCHANGE_RATE_SECONDARY**
- `0`

**IS_POSTED**
- `Yes`
- `No`

**JOURNAL_NAME_ID**
- `FAJ`

**OFFSET_ACCOUNT_DISPLAY_VALUE**
- `551200---------`
- `142000---------`
- `552600---------`
- `None`

**OFFSET_ACCOUNT_TYPE**
- `Ledger`

**POSTING_LAYER**
- `Current`

**REPORTING_CURRENCY_EXCHANGE_RATE**
- `100`

**REPORTING_CURRENCY_EXCHANGE_RATE_SECONDARY**
- `0`

**JOURNAL_TEXT**
- `None`
- `Depr. from 5/1/2026 to 5/31/2026`
- `Depr. from 8/1/2026 to 8/31/2026`
- `Depr. from 6/1/2026 to 6/30/2026`
- `Depr. from 2/1/2026 to 2/28/2026`
- `Depr. from 1/1/2026 to 1/31/2026`
- `Depr. from 3/1/2026 to 3/31/2026`
- `Depr. from 7/1/2026 to 7/31/2026`
- `Depr. from 4/1/2026 to 4/30/2026`
- `Depr. from 9/1/2026 to 9/30/2026`
- `Depr. from 10/1/2026 to 10/31/2026`

**TRANSACTION_TYPE**
- `Depreciation`
- `Acquisition`
- `DisposalScrap`
- `DisposalSale`

**TRANS_DATE**
- `2026-05-31 12:00:00.0000000 +00:00`
- `2026-01-31 12:00:00.0000000 +00:00`
- `2026-02-28 12:00:00.0000000 +00:00`
- `2026-07-31 12:00:00.0000000 +00:00`
- `2026-01-01 12:00:00.0000000 +00:00`
- `2026-06-30 12:00:00.0000000 +00:00`
- `2026-03-31 12:00:00.0000000 +00:00`
- `2026-04-30 12:00:00.0000000 +00:00`
- `2026-08-31 12:00:00.0000000 +00:00`
- `2026-09-30 12:00:00.0000000 +00:00`
- `2026-10-20 12:00:00.0000000 +00:00`
- `2026-10-31 12:00:00.0000000 +00:00`
- `2026-10-22 12:00:00.0000000 +00:00`
- `2026-10-23 12:00:00.0000000 +00:00`
- `2026-10-21 12:00:00.0000000 +00:00`
- `2026-10-01 12:00:00.0000000 +00:00`
- `2026-11-09 12:00:00.0000000 +00:00`
- `2026-10-14 12:00:00.0000000 +00:00`

**WORKFLOW_APPROVAL_STATUS**
- `Approved`
- `NotSubmitted`
- `PendingApproval`

**SOURCE_FILE_NAME**
- `assetjournalv2__20261116_105417.csv`

**MDP_CREATED_DATE**
- `2026-11-16 11:41:41.319882+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 11:41:41.319882+00:00`

## Empty columns

Empty in every row: `DEFAULT_DIMENSION_DISPLAY_VALUE`. Do not filter or group on them.
