---
name: fact_asset_master_transactions
schema: silver
layer: silver
domain: fa
type: fact
status: active
purpose: Fixed asset transactions (acquisition, depreciation, disposal and others) with transaction type, book type, amount
  and posting date.
grain: one row per asset transaction (HASH_KEY; business key not confirmed)
primary_key:
- HASH_KEY
entity_column: ENTITY_ID
period_columns:
- POSTING_DATE
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms:
- asset transactions
- fixed asset transactions
- depreciation
- acquisitions
- disposals
- retirements
- asset movements
known_issues:
- code: duplicates
  note: The source is loaded twice. HASH_KEY cannot detect the duplicate loads; check for repeated business rows (ENTITY_ID,
    ASSET_ID, TRANSACTION_TYPE, BOOK_TYPE, POSTING_DATE, AMOUNT) before summing, warn the user, and deduplicate only if the
    answer says so.
reviewed: true
proposed_fields: []
---

# fact_asset_master_transactions

Fixed asset transactions (acquisition, depreciation, disposal and others) with transaction type, book type,
amount and posting date.

> Period filters use POSTING_DATE. Check current TRANSACTION_TYPE values with `get_column_values` before filtering.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `HASH_KEY` | string | Technical row key (does not detect duplicate loads). |  | `HASH_KEY` |
| `ENTITY_ID` | string | Company (data area) of the asset. This is the entity column. | company, entity, data area | `ENTITY_ID` |
| `ASSET_ID` | string | Asset number (joins to dim_fixed_assets.FIXED_ASSET_NUMBER with ENTITY_ID). | asset id, asset number, asset | `ASSET_ID` |
| `TRANSACTION_TYPE` | string | Transaction type (acquisition, depreciation, disposal ...). | transaction type, type | `TRANSACTION_TYPE` |
| `AMOUNT` | decimal | Transaction amount. | amount, value | `AMOUNT` |
| `POSTING_DATE` | date | Posting date. | posting date, date | `POSTING_DATE` |
| `BOOK_TYPE` | string | Book type. | book type, book | `BOOK_TYPE` |
| `ENTITY` | string |  |  | `ENTITY` |
| `ASSET_CONVENTION` | string |  |  | `ASSET_CONVENTION` |
| `BASELINE_TREATMENT_CODE` | string |  |  | `BASELINE_TREATMENT_CODE` |
| `CITY` | string |  |  | `CITY` |
| `CLIENT_ASSET_CLASS` | string |  |  | `CLIENT_ASSET_CLASS` |
| `COUNTRY_REGION_ID` | string |  |  | `COUNTRY_REGION_ID` |
| `COUNTY` | string |  |  | `COUNTY` |
| `DESCRIPTION` | string |  |  | `DESCRIPTION` |
| `ENTITY_NAME` | string |  |  | `ENTITY_NAME` |
| `FINANCIAL_CALENDAR` | string |  |  | `FINANCIAL_CALENDAR` |
| `INITIAL_ACQUISITION_DATE` | string |  |  | `INITIAL_ACQUISITION_DATE` |
| `LIFE` | string |  |  | `LIFE` |
| `LOCATION` | string |  |  | `LOCATION` |
| `DEPRECIATION_METHOD` | string |  |  | `DEPRECIATION_METHOD` |
| `DEPRECIATION_METHOD_NAME` | string |  |  | `DEPRECIATION_METHOD_NAME` |
| `PLACE_IN_SERVICE_DATE` | string |  |  | `PLACE_IN_SERVICE_DATE` |
| `RATE` | string |  |  | `RATE` |
| `STATE` | string |  |  | `STATE` |
| `STATUS` | string |  |  | `STATUS` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**BOOK_TYPE**
- `GAAP`

**ASSET_CONVENTION**
- `Full month`
- `None`

**BASELINE_TREATMENT_CODE**
- `None`

**CITY**
- `None`

**CLIENT_ASSET_CLASS**
- `AUTO`
- `BUILDINGS`
- `FURNITURE`
- `COMPUTER`
- `SOFTWARE`

**COUNTRY_REGION_ID**
- `None`

**COUNTY**
- `None`

**DESCRIPTION**
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

**FINANCIAL_CALENDAR**
- `2026`

**INITIAL_ACQUISITION_DATE**
- `2026-01-01 12:00:00.0000000 +00:00`
- `2026-10-23 12:00:00.0000000 +00:00`
- `2026-10-01 12:00:00.0000000 +00:00`

**LIFE**
- `1826`
- `14245`
- `3652`

**LOCATION**
- `HQ`
- `None`

**DEPRECIATION_METHOD**
- `SLM`

**DEPRECIATION_METHOD_NAME**
- `Straight line service life`

**PLACE_IN_SERVICE_DATE**
- `2026-01-01 12:00:00.0000000 +00:00`
- `2026-10-23 12:00:00.0000000 +00:00`
- `2026-10-01 12:00:00.0000000 +00:00`

**POSTING_DATE**
- `2026-05-31 12:00:00.0000000 +00:00`
- `2026-01-01 12:00:00.0000000 +00:00`
- `2026-06-30 12:00:00.0000000 +00:00`
- `2026-07-31 12:00:00.0000000 +00:00`
- `2026-03-31 12:00:00.0000000 +00:00`
- `2026-08-31 12:00:00.0000000 +00:00`
- `2026-02-28 12:00:00.0000000 +00:00`
- `2026-04-30 12:00:00.0000000 +00:00`
- `2026-01-31 12:00:00.0000000 +00:00`
- `2026-09-30 12:00:00.0000000 +00:00`
- `2026-10-20 12:00:00.0000000 +00:00`
- `2026-10-22 12:00:00.0000000 +00:00`
- `2026-10-31 12:00:00.0000000 +00:00`
- `2026-10-23 12:00:00.0000000 +00:00`
- `2026-10-01 12:00:00.0000000 +00:00`

**RATE**
- `0`

**STATE**
- `None`

**STATUS**
- `Open`
- `Scrapped`
- `Sold`
- `Closed`

**TRANSACTION_TYPE**
- `Depreciation`
- `Acquisition`
- `Depreciation (this year)`
- `Acquisition (this year)`
- `Net book value`
- `Profit/Loss`
- `Disposal - scrap`
- `Disposal - sale`

**SOURCE_FILE_NAME**
- `assetmastertransactions__20261116_105417.csv`

**MDP_CREATED_DATE**
- `2026-11-16 11:42:15.801774+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 11:42:15.801774+00:00`

## Empty columns

Empty in every row: `BASELINE_TREATMENT_CODE`, `CITY`, `COUNTRY_REGION_ID`, `COUNTY`, `STATE`. Do not filter or group on them.

## Joins (approved, use the full key)

| Join | To table | Cardinality |
|---|---|---|
| `asset_transaction_to_asset` | `dim_fixed_assets` | many-to-one |

## Notes

- Transaction workload = row count by TRANSACTION_TYPE (after the duplicate check).
