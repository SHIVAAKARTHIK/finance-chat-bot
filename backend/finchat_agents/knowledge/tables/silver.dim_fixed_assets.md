---
name: dim_fixed_assets
schema: silver
layer: silver
domain: fa
type: dim
status: active
purpose: Fixed asset master, one row per asset per company with asset name, asset group and asset type.
grain: one row per asset per company (DATA_AREA_ID, FIXED_ASSET_NUMBER)
primary_key:
- DATA_AREA_ID
- FIXED_ASSET_NUMBER
entity_column: DATA_AREA_ID
period_columns: []
pii_columns:
- CONTACT_NAME
- RESPONSIBLE_NAME
- MDP_CREATED_BY
- MDP_MODIFIED_BY
- CONTACT_PERSONNEL_NUMBER
- RESPONSIBLE_PERSONNEL_NUMBER
synonyms:
- fixed asset master
- asset master
- asset name
- asset type
- assets
known_issues:
- code: duplicates
  note: The source is loaded twice. Check duplicates at the grain (DATA_AREA_ID, FIXED_ASSET_NUMBER) before counting; warn
    the user and deduplicate only if the answer says so.
reviewed: true
proposed_fields: []
row_count: 301
---

# dim_fixed_assets

Fixed asset master: one row per asset per company with asset name, asset group and asset type.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `DATA_AREA_ID` | string | Company (data area). This is the entity column. | company, data area | `DATA_AREA_ID` |
| `FIXED_ASSET_NUMBER` | string | Asset number. | asset number, asset id, asset | `FIXED_ASSET_NUMBER` |
| `ASSET_NAME` | string | Asset name. | asset name, asset description | `ASSET_NAME` |
| `FIXED_ASSET_GROUP_ID` | string | Asset group (category). | asset group, asset category | `FIXED_ASSET_GROUP_ID` |
| `ASSET_TYPE` | string | Asset type. | asset type | `ASSET_TYPE` |
| `CONTACT_NAME` | string | Contact person. PII. | contact | `CONTACT_NAME` |
| `RESPONSIBLE_NAME` | string | Responsible person. PII. | responsible, owner | `RESPONSIBLE_NAME` |
| `ACTIVITY_CODE` | string |  |  | `ACTIVITY_CODE` |
| `AGENT` | string |  |  | `AGENT` |
| `ASSET_CONDITION_ID` | string |  |  | `ASSET_CONDITION_ID` |
| `ASSET_LEASE_LEASE_ID` | string |  |  | `ASSET_LEASE_LEASE_ID` |
| `ASSET_LOCATION_ID` | string |  |  | `ASSET_LOCATION_ID` |
| `BAR_CODE` | string |  |  | `BAR_CODE` |
| `COMMENTS` | string |  |  | `COMMENTS` |
| `CONTACT_PERSONNEL_NUMBER` | string |  |  | `CONTACT_PERSONNEL_NUMBER` |
| `DEPARTMENT_OPERATING_UNIT_NUMBER` | string |  |  | `DEPARTMENT_OPERATING_UNIT_NUMBER` |
| `DEPARTMENT_SEARCH_NAME` | string |  |  | `DEPARTMENT_SEARCH_NAME` |
| `DISPOSAL_RESTRICTIONS` | string |  |  | `DISPOSAL_RESTRICTIONS` |
| `DOCUMENT_LOCATION` | string |  |  | `DOCUMENT_LOCATION` |
| `GIS_REFERENCE_NUMBER` | string |  |  | `GIS_REFERENCE_NUMBER` |
| `GUARANTEE_DATE` | string |  |  | `GUARANTEE_DATE` |
| `INFORMATION_1` | string |  |  | `INFORMATION_1` |
| `INFORMATION_2` | string |  |  | `INFORMATION_2` |
| `INFORMATION_3` | string |  |  | `INFORMATION_3` |
| `INSURANCE_DATE_1` | string |  |  | `INSURANCE_DATE_1` |
| `INSURANCE_DATE_2` | string |  |  | `INSURANCE_DATE_2` |
| `INSURANCE_VENDOR` | string |  |  | `INSURANCE_VENDOR` |
| `INSURED_AT_FAIR_MARKET_VALUE` | string |  |  | `INSURED_AT_FAIR_MARKET_VALUE` |
| `INSURED_VALUE` | string |  |  | `INSURED_VALUE` |
| `LAST_MAINTENANCE` | string |  |  | `LAST_MAINTENANCE` |
| `LAST_PERIODIC_VALUE_COST_UPDATE` | string |  |  | `LAST_PERIODIC_VALUE_COST_UPDATE` |
| `LEASE_NOTE` | string |  |  | `LEASE_NOTE` |
| `LOCATION_MEMO` | string |  |  | `LOCATION_MEMO` |
| `MAIN_ASSET_ID` | string |  |  | `MAIN_ASSET_ID` |
| `MAJOR_TYPE_ID` | string |  |  | `MAJOR_TYPE_ID` |
| `MAKE` | string |  |  | `MAKE` |
| `MISSING_ASSET` | string |  |  | `MISSING_ASSET` |
| `MODEL` | string |  |  | `MODEL` |
| `MODEL_YEAR` | string |  |  | `MODEL_YEAR` |
| `NEXT_MAINTENANCE` | string |  |  | `NEXT_MAINTENANCE` |
| `PARCEL_ID` | string |  |  | `PARCEL_ID` |
| `PHYSICAL_INVENTORY` | string |  |  | `PHYSICAL_INVENTORY` |
| `POLICY_AMOUNT` | string |  |  | `POLICY_AMOUNT` |
| `POLICY_EXPIRATION_DATE` | string |  |  | `POLICY_EXPIRATION_DATE` |
| `POLICY_NUMBER` | string |  |  | `POLICY_NUMBER` |
| `PROPERTY_GROUP_ID` | string |  |  | `PROPERTY_GROUP_ID` |
| `PROPERTY_TYPE` | string |  |  | `PROPERTY_TYPE` |
| `QUANTITY` | string |  |  | `QUANTITY` |
| `REFERENCE` | string |  |  | `REFERENCE` |
| `REPLACEMENT_COST` | string |  |  | `REPLACEMENT_COST` |
| `RESPONSIBLE_PERSONNEL_NUMBER` | string |  |  | `RESPONSIBLE_PERSONNEL_NUMBER` |
| `ROOM_NUMBER` | string |  |  | `ROOM_NUMBER` |
| `SEARCH_NAME` | string |  |  | `SEARCH_NAME` |
| `SERIAL_NUMBER` | string |  |  | `SERIAL_NUMBER` |
| `SORT_FIELD_1_ID` | string |  |  | `SORT_FIELD_1_ID` |
| `SORT_FIELD_2_ID` | string |  |  | `SORT_FIELD_2_ID` |
| `SORT_FIELD_3_ID` | string |  |  | `SORT_FIELD_3_ID` |
| `TECHNICAL_INFORMATION_1` | string |  |  | `TECHNICAL_INFORMATION_1` |
| `TECHNICAL_INFORMATION_2` | string |  |  | `TECHNICAL_INFORMATION_2` |
| `TECHNICAL_INFORMATION_3` | string |  |  | `TECHNICAL_INFORMATION_3` |
| `TITLE_HOLDER` | string |  |  | `TITLE_HOLDER` |
| `UNIT_COST` | string |  |  | `UNIT_COST` |
| `UNIT_OF_MEASURE` | string |  |  | `UNIT_OF_MEASURE` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**ACTIVITY_CODE**
- `None`: 301 rows

**AGENT**
- `None`: 301 rows

**ASSET_CONDITION_ID**
- `None`: 301 rows

**ASSET_LEASE_LEASE_ID**
- `None`: 301 rows

**ASSET_LOCATION_ID**
- `HQ`: 297 rows
- `None`: 4 rows

**BAR_CODE**
- `None`: 301 rows

**COMMENTS**
- `None`: 301 rows

**DEPARTMENT_OPERATING_UNIT_NUMBER**
- `None`: 301 rows

**DEPARTMENT_SEARCH_NAME**
- `None`: 301 rows

**DISPOSAL_RESTRICTIONS**
- `None`: 301 rows

**DOCUMENT_LOCATION**
- `None`: 301 rows

**FIXED_ASSET_GROUP_ID**
- `SOFTWARE`: 50 rows
- `BUILDINGS`: 50 rows
- `COMPUTER`: 50 rows
- `LHI`: 50 rows
- `AUTO`: 50 rows
- `FURNITURE`: 50 rows
- `None`: 1 rows

**GIS_REFERENCE_NUMBER**
- `None`: 301 rows

**GUARANTEE_DATE**
- `1900-01-01 12:00:00.0000000 +00:00`: 301 rows

**INFORMATION_1**
- `None`: 301 rows

**INFORMATION_2**
- `None`: 301 rows

**INFORMATION_3**
- `None`: 301 rows

**INSURANCE_DATE_1**
- `1900-01-01 12:00:00.0000000 +00:00`: 301 rows

**INSURANCE_DATE_2**
- `1900-01-01 12:00:00.0000000 +00:00`: 301 rows

**INSURANCE_VENDOR**
- `None`: 301 rows

**INSURED_AT_FAIR_MARKET_VALUE**
- `No`: 301 rows

**INSURED_VALUE**
- `0`: 301 rows

**LAST_MAINTENANCE**
- `1900-01-01 12:00:00.0000000 +00:00`: 301 rows

**LAST_PERIODIC_VALUE_COST_UPDATE**
- `1900-01-01 12:00:00.0000000 +00:00`: 301 rows

**LEASE_NOTE**
- `None`: 301 rows

**LOCATION_MEMO**
- `None`: 301 rows

**MAIN_ASSET_ID**
- `None`: 301 rows

**MAJOR_TYPE_ID**
- `None`: 301 rows

**MAKE**
- `None`: 301 rows

**MISSING_ASSET**
- `No`: 301 rows

**MODEL**
- `None`: 301 rows

**MODEL_YEAR**
- `None`: 301 rows

**NEXT_MAINTENANCE**
- `1900-01-01 12:00:00.0000000 +00:00`: 301 rows

**PARCEL_ID**
- `None`: 301 rows

**PHYSICAL_INVENTORY**
- `1900-01-01 12:00:00.0000000 +00:00`: 301 rows

**POLICY_AMOUNT**
- `0`: 301 rows

**POLICY_EXPIRATION_DATE**
- `1900-01-01 12:00:00.0000000 +00:00`: 301 rows

**POLICY_NUMBER**
- `None`: 301 rows

**PROPERTY_GROUP_ID**
- `None`: 301 rows

**PROPERTY_TYPE**
- `FixedAsset`: 301 rows

**QUANTITY**
- `0`: 295 rows
- `1`: 6 rows

**REFERENCE**
- `None`: 301 rows

**REPLACEMENT_COST**
- `0`: 301 rows

**ROOM_NUMBER**
- `None`: 301 rows

**SERIAL_NUMBER**
- `None`: 301 rows

**SORT_FIELD_1_ID**
- `None`: 301 rows

**SORT_FIELD_2_ID**
- `None`: 301 rows

**SORT_FIELD_3_ID**
- `None`: 301 rows

**TECHNICAL_INFORMATION_1**
- `None`: 301 rows

**TECHNICAL_INFORMATION_2**
- `None`: 301 rows

**TECHNICAL_INFORMATION_3**
- `None`: 301 rows

**TITLE_HOLDER**
- `None`: 301 rows

**ASSET_TYPE**
- `Tangible`: 301 rows

**UNIT_COST**
- `0`: 301 rows

**UNIT_OF_MEASURE**
- `None`: 301 rows

**SOURCE_FILE_NAME**
- `fixedassetsv2__20261116_105417.csv`: 301 rows

**MDP_CREATED_DATE**
- `2026-11-16 11:42:01.917258+00:00`: 301 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 11:42:01.917258+00:00`: 301 rows

## Joins (approved, use the full key)

| Join | To table | Cardinality |
|---|---|---|
| `asset_book_to_asset` | `dim_fixed_asset_books` | many-to-one (from the book) |
| `asset_transaction_to_asset` | `fact_asset_master_transactions` | many-to-one (from the transaction) |

## Profile

Rows in the latest export: 301.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `DATA_AREA_ID` | STRING | 2 | 0 |  |  |
| `FIXED_ASSET_NUMBER` | STRING | 300 | 0 | AUT000024 | SOFT-000050 |
| `ACTIVITY_CODE` | STRING | 0 | 301 |  |  |
| `AGENT` | STRING | 0 | 301 |  |  |
| `ASSET_CONDITION_ID` | STRING | 0 | 301 |  |  |
| `ASSET_LEASE_LEASE_ID` | STRING | 0 | 301 |  |  |
| `ASSET_LOCATION_ID` | STRING | 1 | 4 | HQ | HQ |
| `BAR_CODE` | STRING | 0 | 301 |  |  |
| `COMMENTS` | STRING | 0 | 301 |  |  |
| `CONTACT_NAME` | STRING | 0 | 301 |  |  |
| `CONTACT_PERSONNEL_NUMBER` | STRING | 0 | 301 |  |  |
| `DEPARTMENT_OPERATING_UNIT_NUMBER` | STRING | 0 | 301 |  |  |
| `DEPARTMENT_SEARCH_NAME` | STRING | 0 | 301 |  |  |
| `DISPOSAL_RESTRICTIONS` | STRING | 0 | 301 |  |  |
| `DOCUMENT_LOCATION` | STRING | 0 | 301 |  |  |
| `FIXED_ASSET_GROUP_ID` | STRING | 6 | 1 | AUTO | SOFTWARE |
| `GIS_REFERENCE_NUMBER` | STRING | 0 | 301 |  |  |
| `GUARANTEE_DATE` | STRING | 1 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `INFORMATION_1` | STRING | 0 | 301 |  |  |
| `INFORMATION_2` | STRING | 0 | 301 |  |  |
| `INFORMATION_3` | STRING | 0 | 301 |  |  |
| `INSURANCE_DATE_1` | STRING | 1 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `INSURANCE_DATE_2` | STRING | 1 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `INSURANCE_VENDOR` | STRING | 0 | 301 |  |  |
| `INSURED_AT_FAIR_MARKET_VALUE` | STRING | 1 | 0 | No | No |
| `INSURED_VALUE` | STRING | 1 | 0 | 0 | 0 |
| `LAST_MAINTENANCE` | STRING | 1 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `LAST_PERIODIC_VALUE_COST_UPDATE` | STRING | 1 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `LEASE_NOTE` | STRING | 0 | 301 |  |  |
| `LOCATION_MEMO` | STRING | 0 | 301 |  |  |
| `MAIN_ASSET_ID` | STRING | 0 | 301 |  |  |
| `MAJOR_TYPE_ID` | STRING | 0 | 301 |  |  |
| `MAKE` | STRING | 0 | 301 |  |  |
| `MISSING_ASSET` | STRING | 1 | 0 | No | No |
| `MODEL` | STRING | 0 | 301 |  |  |
| `MODEL_YEAR` | STRING | 0 | 301 |  |  |
| `ASSET_NAME` | STRING | 315 | 1 | Accounts Payable Automation Suite | Workflow Automation Suite |
| `NEXT_MAINTENANCE` | STRING | 1 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `PARCEL_ID` | STRING | 0 | 301 |  |  |
| `PHYSICAL_INVENTORY` | STRING | 1 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `POLICY_AMOUNT` | STRING | 1 | 0 | 0 | 0 |
| `POLICY_EXPIRATION_DATE` | STRING | 1 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `POLICY_NUMBER` | STRING | 0 | 301 |  |  |
| `PROPERTY_GROUP_ID` | STRING | 0 | 301 |  |  |
| `PROPERTY_TYPE` | STRING | 1 | 0 | FixedAsset | FixedAsset |
| `QUANTITY` | STRING | 2 | 0 | 0 | 1 |
| `REFERENCE` | STRING | 0 | 301 |  |  |
| `REPLACEMENT_COST` | STRING | 1 | 0 | 0 | 0 |
| `RESPONSIBLE_NAME` | STRING | 0 | 301 |  |  |
| `RESPONSIBLE_PERSONNEL_NUMBER` | STRING | 0 | 301 |  |  |
| `ROOM_NUMBER` | STRING | 0 | 301 |  |  |
| `SEARCH_NAME` | STRING | 293 | 1 | ACCOUNTS_PAYABLE_AUT | WORKFLOW_AUTOMATION_ |
| `SERIAL_NUMBER` | STRING | 0 | 301 |  |  |
| `SORT_FIELD_1_ID` | STRING | 0 | 301 |  |  |
| `SORT_FIELD_2_ID` | STRING | 0 | 301 |  |  |
| `SORT_FIELD_3_ID` | STRING | 0 | 301 |  |  |
| `TECHNICAL_INFORMATION_1` | STRING | 0 | 301 |  |  |
| `TECHNICAL_INFORMATION_2` | STRING | 0 | 301 |  |  |
| `TECHNICAL_INFORMATION_3` | STRING | 0 | 301 |  |  |
| `TITLE_HOLDER` | STRING | 0 | 301 |  |  |
| `ASSET_TYPE` | STRING | 1 | 0 | Tangible | Tangible |
| `UNIT_COST` | STRING | 1 | 0 | 0 | 0 |
| `UNIT_OF_MEASURE` | STRING | 0 | 301 |  |  |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | fixedassetsv2__20261116_105417.csv | fixedassetsv2__20261116_105417.csv |
| `HASH_KEY` | STRING | 296 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:42:01.917000 | 2026-11-16 11:42:01.917000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:42:01.917000 | 2026-11-16 11:42:01.917000 |

## Sample rows

| FIXED_ASSET_NUMBER | ACTIVITY_CODE | AGENT | ASSET_CONDITION_ID | ASSET_LEASE_LEASE_ID | ASSET_LOCATION_ID | BAR_CODE | COMMENTS | CONTACT_NAME | CONTACT_PERSONNEL_NUMBER | DEPARTMENT_OPERATING_UNIT_NUMBER | DEPARTMENT_SEARCH_NAME | DISPOSAL_RESTRICTIONS | DOCUMENT_LOCATION | FIXED_ASSET_GROUP_ID | GIS_REFERENCE_NUMBER | GUARANTEE_DATE | INFORMATION_1 | INFORMATION_2 | INFORMATION_3 | INSURANCE_DATE_1 | INSURANCE_DATE_2 | INSURANCE_VENDOR | INSURED_AT_FAIR_MARKET_VALUE | INSURED_VALUE | LAST_MAINTENANCE | LAST_PERIODIC_VALUE_COST_UPDATE | LEASE_NOTE | LOCATION_MEMO | MAIN_ASSET_ID | MAJOR_TYPE_ID | MAKE | MISSING_ASSET | MODEL | MODEL_YEAR | ASSET_NAME | NEXT_MAINTENANCE | PARCEL_ID | PHYSICAL_INVENTORY | POLICY_AMOUNT | POLICY_EXPIRATION_DATE | POLICY_NUMBER | PROPERTY_GROUP_ID | PROPERTY_TYPE | QUANTITY | REFERENCE | REPLACEMENT_COST | RESPONSIBLE_NAME | RESPONSIBLE_PERSONNEL_NUMBER | ROOM_NUMBER | SEARCH_NAME | SERIAL_NUMBER | SORT_FIELD_1_ID | SORT_FIELD_2_ID | SORT_FIELD_3_ID | TECHNICAL_INFORMATION_1 | TECHNICAL_INFORMATION_2 | TECHNICAL_INFORMATION_3 | TITLE_HOLDER | ASSET_TYPE | UNIT_COST | UNIT_OF_MEASURE | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BUILD-000039 | NULL | NULL | NULL | NULL | HQ | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | BUILDINGS | NULL | 1900-01-01 12:00:00.0000000 +00:00 | NULL | NULL | NULL | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 | NULL | No | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 | NULL | NULL | NULL | NULL | NULL | No | NULL | NULL | Phoenix Training Academy Building | 1900-01-01 12:00:00.0000000 +00:00 | NULL | 1900-01-01 12:00:00.0000000 +00:00 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | NULL | NULL | FixedAsset | 0 | NULL | 0 | <masked> | NULL | NULL | PHOENIX_TRAINING_ACA | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Tangible | 0 | NULL | fixedassetsv2__20261116_105417.csv | <masked> | 2026-11-16 11:42:01.917000 | <masked> | 2026-11-16 11:42:01.917000 |
| BUILD-000040 | NULL | NULL | NULL | NULL | HQ | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | BUILDINGS | NULL | 1900-01-01 12:00:00.0000000 +00:00 | NULL | NULL | NULL | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 | NULL | No | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 | NULL | NULL | NULL | NULL | NULL | No | NULL | NULL | Phoenix Records Storage Facility | 1900-01-01 12:00:00.0000000 +00:00 | NULL | 1900-01-01 12:00:00.0000000 +00:00 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | NULL | NULL | FixedAsset | 0 | NULL | 0 | <masked> | NULL | NULL | PHOENIX_RECORDS_STOR | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Tangible | 0 | NULL | fixedassetsv2__20261116_105417.csv | <masked> | 2026-11-16 11:42:01.917000 | <masked> | 2026-11-16 11:42:01.917000 |
| BUILD-000041 | NULL | NULL | NULL | NULL | HQ | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | BUILDINGS | NULL | 1900-01-01 12:00:00.0000000 +00:00 | NULL | NULL | NULL | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 | NULL | No | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 | NULL | NULL | NULL | NULL | NULL | No | NULL | NULL | Los Angeles Corporate Office Building | 1900-01-01 12:00:00.0000000 +00:00 | NULL | 1900-01-01 12:00:00.0000000 +00:00 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | NULL | NULL | FixedAsset | 0 | NULL | 0 | <masked> | NULL | NULL | LOS_ANGELES_CORPORAT | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Tangible | 0 | NULL | fixedassetsv2__20261116_105417.csv | <masked> | 2026-11-16 11:42:01.917000 | <masked> | 2026-11-16 11:42:01.917000 |
| BUILD-000042 | NULL | NULL | NULL | NULL | HQ | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | BUILDINGS | NULL | 1900-01-01 12:00:00.0000000 +00:00 | NULL | NULL | NULL | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 | NULL | No | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 | NULL | NULL | NULL | NULL | NULL | No | NULL | NULL | Los Angeles Claims Operations Center | 1900-01-01 12:00:00.0000000 +00:00 | NULL | 1900-01-01 12:00:00.0000000 +00:00 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | NULL | NULL | FixedAsset | 0 | NULL | 0 | <masked> | NULL | NULL | LOS_ANGELES_CLAIMS_O | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Tangible | 0 | NULL | fixedassetsv2__20261116_105417.csv | <masked> | 2026-11-16 11:42:01.917000 | <masked> | 2026-11-16 11:42:01.917000 |
| BUILD-000043 | NULL | NULL | NULL | NULL | HQ | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | BUILDINGS | NULL | 1900-01-01 12:00:00.0000000 +00:00 | NULL | NULL | NULL | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 | NULL | No | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 | NULL | NULL | NULL | NULL | NULL | No | NULL | NULL | Los Angeles Regional Administration B... | 1900-01-01 12:00:00.0000000 +00:00 | NULL | 1900-01-01 12:00:00.0000000 +00:00 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | NULL | NULL | FixedAsset | 0 | NULL | 0 | <masked> | NULL | NULL | LOS_ANGELES_REGIONAL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Tangible | 0 | NULL | fixedassetsv2__20261116_105417.csv | <masked> | 2026-11-16 11:42:01.917000 | <masked> | 2026-11-16 11:42:01.917000 |
