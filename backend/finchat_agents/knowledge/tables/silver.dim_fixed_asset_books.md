---
name: dim_fixed_asset_books
schema: silver
layer: silver
domain: fa
type: dim
status: active
purpose: 'Fixed asset books: one row per asset per book with status, acquisition price, asset group and acquisition date.
  Use for asset counts, invested capital (acquisition price) and asset status.'
grain: one row per asset per book (DATA_AREA_ID, FIXED_ASSET_NUMBER, BOOK_ID)
primary_key:
- DATA_AREA_ID
- FIXED_ASSET_NUMBER
- BOOK_ID
entity_column: DATA_AREA_ID
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms:
- assets
- fixed assets
- asset books
- asset book
- portfolio
- invested capital
- acquisition price
- asset status
- asset count
known_issues:
- code: duplicates
  note: 'The source is loaded twice (about twice the expected rows). Before counting or summing, check duplicates at the grain:
    SELECT DATA_AREA_ID, FIXED_ASSET_NUMBER, BOOK_ID, COUNT(*) ... GROUP BY 1,2,3 HAVING COUNT(*) > 1. If duplicates exist,
    warn the user, and deduplicate on the grain only if the answer says so.'
reviewed: true
proposed_fields: []
---

# dim_fixed_asset_books

Fixed asset books: one row per asset per book with status, acquisition price, asset group and acquisition date.
Use for asset counts, invested capital (acquisition price) and asset status.

> Duplicate loads: see known issues. A deduplicated count is
> `COUNT(DISTINCT struct(DATA_AREA_ID, FIXED_ASSET_NUMBER, BOOK_ID))`; say in the answer that duplicates were removed.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `DATA_AREA_ID` | string | Company (data area) the asset belongs to. This is the entity column. | company, data area, legal entity | `DATA_AREA_ID` |
| `FIXED_ASSET_NUMBER` | string | Asset number. | asset number, asset id, asset | `FIXED_ASSET_NUMBER` |
| `BOOK_ID` | string | Asset book (e.g. a tax or accounting book). | book | `BOOK_ID` |
| `STATUS` | string | Asset status in the book. | asset status, status | `STATUS` |
| `ACQUISITION_PRICE` | decimal | Acquisition price (cost). | acquisition price, acquisition value, invested capital, cost | `ACQUISITION_PRICE` |
| `FIXED_ASSET_GROUP_ID` | string | Asset group (category). | asset group, asset category, category, group | `FIXED_ASSET_GROUP_ID` |
| `ACQUISITION_DATE` | date | Date the asset was acquired. | acquisition date, acquired | `ACQUISITION_DATE` |
| `MDP_MODIFIED_DATE` | timestamp | Load audit timestamp (not a business date). |  | `MDP_MODIFIED_DATE` |
| `ACQUISITION_METHOD_DESCRIPTION` | string |  |  | `ACQUISITION_METHOD_DESCRIPTION` |
| `ACQUISITION_METHOD_ID` | string |  |  | `ACQUISITION_METHOD_ID` |
| `ACQUISITION_PRICE_REPORTING_CURRENCY` | string |  |  | `ACQUISITION_PRICE_REPORTING_CURRENCY` |
| `ACTUAL_ACQUISITION_DATE` | string |  |  | `ACTUAL_ACQUISITION_DATE` |
| `ALLOW_DEPRECIATION_WHEN_PLACED_IN_SERVICE_AND_DISPOSAL_ARE_IN_THE_SAME_FISCAL_YEAR` | string |  |  | `ALLOW_DEPRECIATION_WHEN_PLACED_IN_SERVICE_AND_DISPOSAL_ARE_IN_THE_SAME_FISCAL_YEAR` |
| `ALLOW_NEGATIVE_NET_BOOK_VALUE` | string |  |  | `ALLOW_NEGATIVE_NET_BOOK_VALUE` |
| `ALLOW_NET_BOOK_VALUE_HIGHER_THAN_ACQUISITION_COSTS` | string |  |  | `ALLOW_NET_BOOK_VALUE_HIGHER_THAN_ACQUISITION_COSTS` |
| `ALTERNATIVE_DEPRECIATION_PROFILE_ID` | string |  |  | `ALTERNATIVE_DEPRECIATION_PROFILE_ID` |
| `ASSET_LEASE_LEASE_BOOK_TYPE` | string |  |  | `ASSET_LEASE_LEASE_BOOK_TYPE` |
| `ASSET_LEASE_LEASE_ID` | string |  |  | `ASSET_LEASE_LEASE_ID` |
| `CALC_ADJ_IN_RB_DEPRECIATIONS` | string |  |  | `CALC_ADJ_IN_RB_DEPRECIATIONS` |
| `CALCULATE_DEPRECIATION` | string |  |  | `CALCULATE_DEPRECIATION` |
| `CONSUMPTION_ESTIMATED` | string |  |  | `CONSUMPTION_ESTIMATED` |
| `CONSUMPTION_FACTOR_ID` | string |  |  | `CONSUMPTION_FACTOR_ID` |
| `CONSUMPTION_UNIT_DEPRECIATION` | string |  |  | `CONSUMPTION_UNIT_DEPRECIATION` |
| `CONSUMPTION_UNIT_DEPRECIATION_REPORTING_CURRENCY` | string |  |  | `CONSUMPTION_UNIT_DEPRECIATION_REPORTING_CURRENCY` |
| `CONSUMPTION_UNIT_ID` | string |  |  | `CONSUMPTION_UNIT_ID` |
| `CREATE_DEPRECIATION_ADJUSTMENTS_WITH_BASIS_ADJUSTMENTS` | string |  |  | `CREATE_DEPRECIATION_ADJUSTMENTS_WITH_BASIS_ADJUSTMENTS` |
| `CUSTOMER_ACCOUNT` | string |  |  | `CUSTOMER_ACCOUNT` |
| `CUSTOMER_INVOICE` | string |  |  | `CUSTOMER_INVOICE` |
| `DEPRECIATION_CONVENTION` | string |  |  | `DEPRECIATION_CONVENTION` |
| `DEPRECIATION_LAST_RUN_DATE` | string |  |  | `DEPRECIATION_LAST_RUN_DATE` |
| `DEPRECIATION_PERIODS` | string |  |  | `DEPRECIATION_PERIODS` |
| `DEPRECIATION_PERIODS_REMAINING` | string |  |  | `DEPRECIATION_PERIODS_REMAINING` |
| `DEPRECIATION_PROFILE_ID` | string |  |  | `DEPRECIATION_PROFILE_ID` |
| `DEPRECIATION_RUN_DATE` | string |  |  | `DEPRECIATION_RUN_DATE` |
| `DIMENSION_DISPLAY_VALUE` | string |  |  | `DIMENSION_DISPLAY_VALUE` |
| `DISPOSAL_DATE` | string |  |  | `DISPOSAL_DATE` |
| `EXPECTED_SCRAP_VALUE` | string |  |  | `EXPECTED_SCRAP_VALUE` |
| `EXPECTED_SCRAP_VALUE_REPORTING_CURRENCY` | string |  |  | `EXPECTED_SCRAP_VALUE_REPORTING_CURRENCY` |
| `EXTRAORDINARY_DEPRECIATION_LAST_RUN_DATE` | string |  |  | `EXTRAORDINARY_DEPRECIATION_LAST_RUN_DATE` |
| `EXTRAORDINARY_DEPRECIATION_PROFILE_ID` | string |  |  | `EXTRAORDINARY_DEPRECIATION_PROFILE_ID` |
| `IS_ALLOW_DEPRECIATION_ADJ_SAME_DATE` | string |  |  | `IS_ALLOW_DEPRECIATION_ADJ_SAME_DATE` |
| `IS_MIGRATED_ASSET` | string |  |  | `IS_MIGRATED_ASSET` |
| `IS_POSITIVE_DEPRECIATION` | string |  |  | `IS_POSITIVE_DEPRECIATION` |
| `PLACED_IN_SERVICE` | string |  |  | `PLACED_IN_SERVICE` |
| `POSTING_PROFILE_ID` | string |  |  | `POSTING_PROFILE_ID` |
| `PROVISION_TYPE` | string |  |  | `PROVISION_TYPE` |
| `PURCHASE_ORDER` | string |  |  | `PURCHASE_ORDER` |
| `REPLACEMENT_DATE` | string |  |  | `REPLACEMENT_DATE` |
| `SALES_VALUE` | string |  |  | `SALES_VALUE` |
| `SERVICE_LIFE` | string |  |  | `SERVICE_LIFE` |
| `SORT_FIELD_1_ID` | string |  |  | `SORT_FIELD_1_ID` |
| `SORT_FIELD_2_ID` | string |  |  | `SORT_FIELD_2_ID` |
| `SORT_FIELD_3_ID` | string |  |  | `SORT_FIELD_3_ID` |
| `VENDOR_ACCOUNT` | string |  |  | `VENDOR_ACCOUNT` |
| `VENDOR_INVOICE` | string |  |  | `VENDOR_INVOICE` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |

## Values

**STATUS**
- `NoAcquisition`: not yet financially activated (acquisition price 0)
- `Open`: active, capitalized
- `Sold`: inactive, sold
- `Scrapped`: inactive, scrapped
- `Closed`: inactive, closed

**BOOK_ID**
- `GAAP`

**ACQUISITION_DATE**
- `2026-01-01 12:00:00.0000000 +00:00`
- `2026-10-16 12:00:00.0000000 +00:00`
- `2026-10-23 12:00:00.0000000 +00:00`
- `2026-10-01 12:00:00.0000000 +00:00`

**ACQUISITION_METHOD_DESCRIPTION**
- `None`

**ACQUISITION_METHOD_ID**
- `None`

**ACTUAL_ACQUISITION_DATE**
- `2026-01-01 12:00:00.0000000 +00:00`
- `2026-10-16 12:00:00.0000000 +00:00`
- `2026-10-23 12:00:00.0000000 +00:00`
- `2026-10-01 12:00:00.0000000 +00:00`

**ALLOW_DEPRECIATION_WHEN_PLACED_IN_SERVICE_AND_DISPOSAL_ARE_IN_THE_SAME_FISCAL_YEAR**
- `Yes`

**ALLOW_NEGATIVE_NET_BOOK_VALUE**
- `No`

**ALLOW_NET_BOOK_VALUE_HIGHER_THAN_ACQUISITION_COSTS**
- `No`

**ALTERNATIVE_DEPRECIATION_PROFILE_ID**
- `None`

**ASSET_LEASE_LEASE_BOOK_TYPE**
- `None`

**ASSET_LEASE_LEASE_ID**
- `None`

**CALC_ADJ_IN_RB_DEPRECIATIONS**
- `No`

**CALCULATE_DEPRECIATION**
- `Yes`

**CONSUMPTION_ESTIMATED**
- `0`

**CONSUMPTION_FACTOR_ID**
- `None`

**CONSUMPTION_UNIT_DEPRECIATION**
- `0`

**CONSUMPTION_UNIT_DEPRECIATION_REPORTING_CURRENCY**
- `0`

**CONSUMPTION_UNIT_ID**
- `None`

**CREATE_DEPRECIATION_ADJUSTMENTS_WITH_BASIS_ADJUSTMENTS**
- `No`

**CUSTOMER_ACCOUNT**
- `None`

**CUSTOMER_INVOICE**
- `None`

**DEPRECIATION_CONVENTION**
- `FullMonth`
- `None`

**DEPRECIATION_LAST_RUN_DATE**
- `2026-09-30 12:00:00.0000000 +00:00`
- `1900-01-01 12:00:00.0000000 +00:00`
- `2026-08-31 12:00:00.0000000 +00:00`
- `2026-10-31 12:00:00.0000000 +00:00`
- `2026-10-20 12:00:00.0000000 +00:00`

**DEPRECIATION_PERIODS**
- `1826`
- `3653`
- `14245`
- `3652`

**DEPRECIATION_PERIODS_REMAINING**
- `1553`
- `1826`
- `3653`
- `13972`
- `3380`
- `1583`
- `1522`
- `100`
- `330`
- `10`
- `310`
- `14245`

**DEPRECIATION_PROFILE_ID**
- `SLM`

**DEPRECIATION_RUN_DATE**
- `2026-01-01 12:00:00.0000000 +00:00`
- `2026-10-16 12:00:00.0000000 +00:00`
- `2026-10-23 12:00:00.0000000 +00:00`
- `2026-10-01 12:00:00.0000000 +00:00`

**DIMENSION_DISPLAY_VALUE**
- `None`

**DISPOSAL_DATE**
- `1900-01-01 12:00:00.0000000 +00:00`
- `2026-10-20 12:00:00.0000000 +00:00`
- `2026-10-22 12:00:00.0000000 +00:00`

**EXPECTED_SCRAP_VALUE**
- `0`

**EXPECTED_SCRAP_VALUE_REPORTING_CURRENCY**
- `0`

**EXTRAORDINARY_DEPRECIATION_LAST_RUN_DATE**
- `1900-01-01 12:00:00.0000000 +00:00`

**EXTRAORDINARY_DEPRECIATION_PROFILE_ID**
- `None`

**FIXED_ASSET_GROUP_ID**
- `SOFTWARE`
- `FURNITURE`
- `COMPUTER`
- `LHI`
- `AUTO`
- `BUILDINGS`

**IS_ALLOW_DEPRECIATION_ADJ_SAME_DATE**
- `No`

**IS_MIGRATED_ASSET**
- `No`

**IS_POSITIVE_DEPRECIATION**
- `No`

**PLACED_IN_SERVICE**
- `2026-01-01 12:00:00.0000000 +00:00`
- `2026-10-16 12:00:00.0000000 +00:00`
- `1900-01-01 12:00:00.0000000 +00:00`
- `2026-10-23 12:00:00.0000000 +00:00`
- `2026-10-01 12:00:00.0000000 +00:00`

**POSTING_PROFILE_ID**
- `FAPP`

**PROVISION_TYPE**
- `None`

**PURCHASE_ORDER**
- `None`

**REPLACEMENT_DATE**
- `1900-01-01 12:00:00.0000000 +00:00`

**SALES_VALUE**
- `0`
- `100`
- `-20000`
- `-12000`

**SERVICE_LIFE**
- `5`
- `10`
- `39`

**SORT_FIELD_1_ID**
- `None`

**SORT_FIELD_2_ID**
- `None`

**SORT_FIELD_3_ID**
- `None`

**VENDOR_ACCOUNT**
- `None`

**VENDOR_INVOICE**
- `None`

**SOURCE_FILE_NAME**
- `fixedassetbooksv2__20261116_105417.csv`

**MDP_CREATED_DATE**
- `2026-11-16 11:42:09.396727+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 11:42:09.396727+00:00`

## Empty columns

Empty in every row: `ACQUISITION_METHOD_DESCRIPTION`, `ACQUISITION_METHOD_ID`, `ALTERNATIVE_DEPRECIATION_PROFILE_ID`, `ASSET_LEASE_LEASE_BOOK_TYPE`, `ASSET_LEASE_LEASE_ID`, `CONSUMPTION_FACTOR_ID`, `CONSUMPTION_UNIT_ID`, `CUSTOMER_ACCOUNT`, `CUSTOMER_INVOICE`, `DIMENSION_DISPLAY_VALUE`, `EXTRAORDINARY_DEPRECIATION_PROFILE_ID`, `PROVISION_TYPE`, `PURCHASE_ORDER`, `SORT_FIELD_1_ID`, `SORT_FIELD_2_ID`, `SORT_FIELD_3_ID`, `VENDOR_ACCOUNT`, `VENDOR_INVOICE`. Do not filter or group on them.

## Joins (approved, use the full key)

| Join | To table | Cardinality |
|---|---|---|
| `asset_book_to_asset` | `dim_fixed_assets` | many-to-one |

Never join on DATA_AREA_ID alone (blocked: every asset would match every asset).

## Notes

- "Inactive" assets = STATUS Sold, Scrapped or Closed. "Not financially activated" = STATUS NoAcquisition.
- Column types other than those listed were not profiled yet; confirm with the catalog export (task 08).
