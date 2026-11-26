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
- `None`

**AGENT**
- `None`

**ASSET_CONDITION_ID**
- `None`

**ASSET_LEASE_LEASE_ID**
- `None`

**ASSET_LOCATION_ID**
- `HQ`
- `None`

**BAR_CODE**
- `None`

**COMMENTS**
- `None`

**DEPARTMENT_OPERATING_UNIT_NUMBER**
- `None`

**DEPARTMENT_SEARCH_NAME**
- `None`

**DISPOSAL_RESTRICTIONS**
- `None`

**DOCUMENT_LOCATION**
- `None`

**FIXED_ASSET_GROUP_ID**
- `SOFTWARE`
- `BUILDINGS`
- `COMPUTER`
- `LHI`
- `AUTO`
- `FURNITURE`
- `None`

**GIS_REFERENCE_NUMBER**
- `None`

**GUARANTEE_DATE**
- `1900-01-01 12:00:00.0000000 +00:00`

**INFORMATION_1**
- `None`

**INFORMATION_2**
- `None`

**INFORMATION_3**
- `None`

**INSURANCE_DATE_1**
- `1900-01-01 12:00:00.0000000 +00:00`

**INSURANCE_DATE_2**
- `1900-01-01 12:00:00.0000000 +00:00`

**INSURANCE_VENDOR**
- `None`

**INSURED_AT_FAIR_MARKET_VALUE**
- `No`

**INSURED_VALUE**
- `0`

**LAST_MAINTENANCE**
- `1900-01-01 12:00:00.0000000 +00:00`

**LAST_PERIODIC_VALUE_COST_UPDATE**
- `1900-01-01 12:00:00.0000000 +00:00`

**LEASE_NOTE**
- `None`

**LOCATION_MEMO**
- `None`

**MAIN_ASSET_ID**
- `None`

**MAJOR_TYPE_ID**
- `None`

**MAKE**
- `None`

**MISSING_ASSET**
- `No`

**MODEL**
- `None`

**MODEL_YEAR**
- `None`

**NEXT_MAINTENANCE**
- `1900-01-01 12:00:00.0000000 +00:00`

**PARCEL_ID**
- `None`

**PHYSICAL_INVENTORY**
- `1900-01-01 12:00:00.0000000 +00:00`

**POLICY_AMOUNT**
- `0`

**POLICY_EXPIRATION_DATE**
- `1900-01-01 12:00:00.0000000 +00:00`

**POLICY_NUMBER**
- `None`

**PROPERTY_GROUP_ID**
- `None`

**PROPERTY_TYPE**
- `FixedAsset`

**QUANTITY**
- `0`
- `1`

**REFERENCE**
- `None`

**REPLACEMENT_COST**
- `0`

**ROOM_NUMBER**
- `None`

**SERIAL_NUMBER**
- `None`

**SORT_FIELD_1_ID**
- `None`

**SORT_FIELD_2_ID**
- `None`

**SORT_FIELD_3_ID**
- `None`

**TECHNICAL_INFORMATION_1**
- `None`

**TECHNICAL_INFORMATION_2**
- `None`

**TECHNICAL_INFORMATION_3**
- `None`

**TITLE_HOLDER**
- `None`

**ASSET_TYPE**
- `Tangible`

**UNIT_COST**
- `0`

**UNIT_OF_MEASURE**
- `None`

**SOURCE_FILE_NAME**
- `fixedassetsv2__20261116_105417.csv`

**MDP_CREATED_DATE**
- `2026-11-16 11:42:01.917258+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 11:42:01.917258+00:00`

## Empty columns

Empty in every row: `ACTIVITY_CODE`, `AGENT`, `ASSET_CONDITION_ID`, `ASSET_LEASE_LEASE_ID`, `BAR_CODE`, `COMMENTS`, `CONTACT_NAME`, `CONTACT_PERSONNEL_NUMBER`, `DEPARTMENT_OPERATING_UNIT_NUMBER`, `DEPARTMENT_SEARCH_NAME`, `DISPOSAL_RESTRICTIONS`, `DOCUMENT_LOCATION`, `GIS_REFERENCE_NUMBER`, `INFORMATION_1`, `INFORMATION_2`, `INFORMATION_3`, `INSURANCE_VENDOR`, `LEASE_NOTE`, `LOCATION_MEMO`, `MAIN_ASSET_ID`, `MAJOR_TYPE_ID`, `MAKE`, `MODEL`, `MODEL_YEAR`, `PARCEL_ID`, `POLICY_NUMBER`, `PROPERTY_GROUP_ID`, `REFERENCE`, `RESPONSIBLE_NAME`, `RESPONSIBLE_PERSONNEL_NUMBER`, `ROOM_NUMBER`, `SERIAL_NUMBER`, `SORT_FIELD_1_ID`, `SORT_FIELD_2_ID`, `SORT_FIELD_3_ID`, `TECHNICAL_INFORMATION_1`, `TECHNICAL_INFORMATION_2`, `TECHNICAL_INFORMATION_3`, `TITLE_HOLDER`, `UNIT_OF_MEASURE`. Do not filter or group on them.

## Joins (approved, use the full key)

| Join | To table | Cardinality |
|---|---|---|
| `asset_book_to_asset` | `dim_fixed_asset_books` | many-to-one (from the book) |
| `asset_transaction_to_asset` | `fact_asset_master_transactions` | many-to-one (from the transaction) |
