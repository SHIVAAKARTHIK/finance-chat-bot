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
row_count: 2003
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
- `GAAP`: 2003 rows

**ASSET_CONVENTION**
- `Full month`: 1511 rows
- `None`: 492 rows

**BASELINE_TREATMENT_CODE**
- `None`: 2003 rows

**CITY**
- `None`: 2003 rows

**CLIENT_ASSET_CLASS**
- `AUTO`: 516 rows
- `BUILDINGS`: 505 rows
- `FURNITURE`: 490 rows
- `COMPUTER`: 490 rows
- `SOFTWARE`: 2 rows

**COUNTRY_REGION_ID**
- `None`: 2003 rows

**COUNTY**
- `None`: 2003 rows

**DESCRIPTION**
- `None`: 242 rows
- `Depr. from 5/1/2026 to 5/31/2026`: 197 rows
- `Depr. from 8/1/2026 to 8/31/2026`: 197 rows
- `Depr. from 6/1/2026 to 6/30/2026`: 197 rows
- `Depr. from 2/1/2026 to 2/28/2026`: 197 rows
- `Depr. from 1/1/2026 to 1/31/2026`: 197 rows
- `Depr. from 3/1/2026 to 3/31/2026`: 197 rows
- `Depr. from 7/1/2026 to 7/31/2026`: 197 rows
- `Depr. from 4/1/2026 to 4/30/2026`: 197 rows
- `Depr. from 9/1/2026 to 9/30/2026`: 182 rows
- `Depr. from 10/1/2026 to 10/31/2026`: 3 rows

**FINANCIAL_CALENDAR**
- `2026`: 2003 rows

**INITIAL_ACQUISITION_DATE**
- `2026-01-01 12:00:00.0000000 +00:00`: 2001 rows
- `2026-10-23 12:00:00.0000000 +00:00`: 1 rows
- `2026-10-01 12:00:00.0000000 +00:00`: 1 rows

**LIFE**
- `1826`: 1008 rows
- `14245`: 505 rows
- `3652`: 490 rows

**LOCATION**
- `HQ`: 1983 rows
- `None`: 20 rows

**DEPRECIATION_METHOD**
- `SLM`: 2003 rows

**DEPRECIATION_METHOD_NAME**
- `Straight line service life`: 2003 rows

**PLACE_IN_SERVICE_DATE**
- `2026-01-01 12:00:00.0000000 +00:00`: 2001 rows
- `2026-10-23 12:00:00.0000000 +00:00`: 1 rows
- `2026-10-01 12:00:00.0000000 +00:00`: 1 rows

**POSTING_DATE**
- `2026-05-31 12:00:00.0000000 +00:00`: 197 rows
- `2026-01-01 12:00:00.0000000 +00:00`: 197 rows
- `2026-06-30 12:00:00.0000000 +00:00`: 197 rows
- `2026-07-31 12:00:00.0000000 +00:00`: 197 rows
- `2026-03-31 12:00:00.0000000 +00:00`: 197 rows
- `2026-08-31 12:00:00.0000000 +00:00`: 197 rows
- `2026-02-28 12:00:00.0000000 +00:00`: 197 rows
- `2026-04-30 12:00:00.0000000 +00:00`: 197 rows
- `2026-01-31 12:00:00.0000000 +00:00`: 197 rows
- `2026-09-30 12:00:00.0000000 +00:00`: 182 rows
- `2026-10-20 12:00:00.0000000 +00:00`: 28 rows
- `2026-10-22 12:00:00.0000000 +00:00`: 15 rows
- `2026-10-31 12:00:00.0000000 +00:00`: 3 rows
- `2026-10-23 12:00:00.0000000 +00:00`: 1 rows
- `2026-10-01 12:00:00.0000000 +00:00`: 1 rows

**RATE**
- `0`: 2003 rows

**STATE**
- `None`: 2003 rows

**STATUS**
- `Open`: 1867 rows
- `Scrapped`: 69 rows
- `Sold`: 58 rows
- `Closed`: 9 rows

**TRANSACTION_TYPE**
- `Depreciation`: 1763 rows
- `Acquisition`: 199 rows
- `Depreciation (this year)`: 9 rows
- `Acquisition (this year)`: 9 rows
- `Net book value`: 7 rows
- `Profit/Loss`: 7 rows
- `Disposal - scrap`: 5 rows
- `Disposal - sale`: 4 rows

**SOURCE_FILE_NAME**
- `assetmastertransactions__20261116_105417.csv`: 2003 rows

**MDP_CREATED_DATE**
- `2026-11-16 11:42:15.801774+00:00`: 2003 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 11:42:15.801774+00:00`: 2003 rows

## Joins (approved, use the full key)

| Join | To table | Cardinality |
|---|---|---|
| `asset_transaction_to_asset` | `dim_fixed_assets` | many-to-one |

## Notes

- Transaction workload = row count by TRANSACTION_TYPE (after the duplicate check).

## Profile

Rows in the latest export: 2003.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `ENTITY` | STRING | 1 | 0 |  |  |
| `ASSET_ID` | STRING | 202 | 0 | AUTO-000001 | SOFT-000049 |
| `BOOK_TYPE` | STRING | 1 | 0 | GAAP | GAAP |
| `ENTITY_ID` | STRING | 1 | 0 |  |  |
| `AMOUNT` | STRING | 568 | 0 | -100.13 | 9900 |
| `ASSET_CONVENTION` | STRING | 2 | 0 | Full month | None |
| `BASELINE_TREATMENT_CODE` | STRING | 0 | 2003 |  |  |
| `CITY` | STRING | 0 | 2003 |  |  |
| `CLIENT_ASSET_CLASS` | STRING | 5 | 0 | AUTO | SOFTWARE |
| `COUNTRY_REGION_ID` | STRING | 0 | 2003 |  |  |
| `COUNTY` | STRING | 0 | 2003 |  |  |
| `DESCRIPTION` | STRING | 10 | 242 | Depr. from 1/1/2026 to 1/31/2026 | Depr. from 9/1/2026 to 9/30/2026 |
| `ENTITY_NAME` | STRING | 1 | 0 |  |  |
| `FINANCIAL_CALENDAR` | STRING | 1 | 0 | 2026 | 2026 |
| `INITIAL_ACQUISITION_DATE` | STRING | 3 | 0 | 2026-01-01 12:00:00.0000000 +00:00 | 2026-10-23 12:00:00.0000000 +00:00 |
| `LIFE` | STRING | 3 | 0 | 14245 | 3652 |
| `LOCATION` | STRING | 1 | 20 | HQ | HQ |
| `DEPRECIATION_METHOD` | STRING | 1 | 0 | SLM | SLM |
| `DEPRECIATION_METHOD_NAME` | STRING | 1 | 0 | Straight line service life | Straight line service life |
| `PLACE_IN_SERVICE_DATE` | STRING | 3 | 0 | 2026-01-01 12:00:00.0000000 +00:00 | 2026-10-23 12:00:00.0000000 +00:00 |
| `POSTING_DATE` | STRING | 14 | 0 | 2026-01-01 12:00:00.0000000 +00:00 | 2026-10-31 12:00:00.0000000 +00:00 |
| `RATE` | STRING | 1 | 0 | 0 | 0 |
| `STATE` | STRING | 0 | 2003 |  |  |
| `STATUS` | STRING | 4 | 0 | Closed | Sold |
| `TRANSACTION_TYPE` | STRING | 8 | 0 | Acquisition | Profit/Loss |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | assetmastertransactions__20261116_105... | assetmastertransactions__20261116_105... |
| `HASH_KEY` | STRING | 1958 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:42:15.802000 | 2026-11-16 11:42:15.802000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:42:15.802000 | 2026-11-16 11:42:15.802000 |

## Sample rows

| ASSET_ID | BOOK_TYPE | AMOUNT | ASSET_CONVENTION | BASELINE_TREATMENT_CODE | CITY | CLIENT_ASSET_CLASS | COUNTRY_REGION_ID | COUNTY | DESCRIPTION | FINANCIAL_CALENDAR | INITIAL_ACQUISITION_DATE | LIFE | LOCATION | DEPRECIATION_METHOD | DEPRECIATION_METHOD_NAME | PLACE_IN_SERVICE_DATE | POSTING_DATE | RATE | STATE | STATUS | TRANSACTION_TYPE | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AUTO-000001 | GAAP | 1000 | Full month | NULL | NULL | AUTO | NULL | NULL | NULL | 2026 | 2026-01-01 12:00:00.0000000 +00:00 | 1826 | HQ | SLM | Straight line service life | 2026-01-01 12:00:00.0000000 +00:00 | 2026-01-01 12:00:00.0000000 +00:00 | 0 | NULL | Scrapped | Acquisition | assetmastertransactions__20261116_105... | <masked> | 2026-11-16 11:42:15.802000 | <masked> | 2026-11-16 11:42:15.802000 |
| AUTO-000001 | GAAP | -31 | Full month | NULL | NULL | AUTO | NULL | NULL | Depr. from 1/1/2026 to 1/31/2026 | 2026 | 2026-01-01 12:00:00.0000000 +00:00 | 1826 | HQ | SLM | Straight line service life | 2026-01-01 12:00:00.0000000 +00:00 | 2026-01-31 12:00:00.0000000 +00:00 | 0 | NULL | Scrapped | Depreciation | assetmastertransactions__20261116_105... | <masked> | 2026-11-16 11:42:15.802000 | <masked> | 2026-11-16 11:42:15.802000 |
| AUTO-000001 | GAAP | -28 | Full month | NULL | NULL | AUTO | NULL | NULL | Depr. from 2/1/2026 to 2/28/2026 | 2026 | 2026-01-01 12:00:00.0000000 +00:00 | 1826 | HQ | SLM | Straight line service life | 2026-01-01 12:00:00.0000000 +00:00 | 2026-02-28 12:00:00.0000000 +00:00 | 0 | NULL | Scrapped | Depreciation | assetmastertransactions__20261116_105... | <masked> | 2026-11-16 11:42:15.802000 | <masked> | 2026-11-16 11:42:15.802000 |
| AUTO-000001 | GAAP | -31 | Full month | NULL | NULL | AUTO | NULL | NULL | Depr. from 3/1/2026 to 3/31/2026 | 2026 | 2026-01-01 12:00:00.0000000 +00:00 | 1826 | HQ | SLM | Straight line service life | 2026-01-01 12:00:00.0000000 +00:00 | 2026-03-31 12:00:00.0000000 +00:00 | 0 | NULL | Scrapped | Depreciation | assetmastertransactions__20261116_105... | <masked> | 2026-11-16 11:42:15.802000 | <masked> | 2026-11-16 11:42:15.802000 |
| AUTO-000001 | GAAP | -30 | Full month | NULL | NULL | AUTO | NULL | NULL | Depr. from 4/1/2026 to 4/30/2026 | 2026 | 2026-01-01 12:00:00.0000000 +00:00 | 1826 | HQ | SLM | Straight line service life | 2026-01-01 12:00:00.0000000 +00:00 | 2026-04-30 12:00:00.0000000 +00:00 | 0 | NULL | Scrapped | Depreciation | assetmastertransactions__20261116_105... | <masked> | 2026-11-16 11:42:15.802000 | <masked> | 2026-11-16 11:42:15.802000 |
