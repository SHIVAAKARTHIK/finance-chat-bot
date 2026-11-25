---
name: dim_vendors
schema: silver
layer: silver
domain: ap
type: table
status: broken
purpose: Vendor master (account; party; name; group).
grain: one row per VENDOR_ACCOUNT_NUMBER within DATA_AREA_ID (one vendor)
primary_key: []
entity_column: DATA_AREA_ID
period_columns: []
pii_columns:
- PRIMARY_EMAIL_ADDRESS
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues:
- code: empty_column
  note: table has no statistics (empty or not profiled)
row_count: null
proposed_fields: []
reviewed: false
broken_error: the profiling query failed in the catalog export (no row count); the error text is not in the workbook
---

# dim_vendors

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `DATA_AREA_ID` | string |  |  | `DATA_AREA_ID` |
| `VENDOR_ACCOUNT_NUMBER` | string |  |  | `VENDOR_ACCOUNT_NUMBER` |
| `VENDOR_PARTY_NUMBER` | string |  |  | `VENDOR_PARTY_NUMBER` |
| `VENDOR_ORGANIZATION_NAME` | string |  |  | `VENDOR_ORGANIZATION_NAME` |
| `VENDOR_KNOWN_AS_NAME` | string |  |  | `VENDOR_KNOWN_AS_NAME` |
| `VENDOR_SEARCH_NAME` | string |  |  | `VENDOR_SEARCH_NAME` |
| `VENDOR_GROUP_ID` | string |  |  | `VENDOR_GROUP_ID` |
| `VENDOR_TYPE` | string |  |  | `VENDOR_TYPE` |
| `VENDOR_PARTY_TYPE` | string |  |  | `VENDOR_PARTY_TYPE` |
| `ADDRESS_STREET` | string |  |  | `ADDRESS_STREET` |
| `ADDRESS_CITY` | string |  |  | `ADDRESS_CITY` |
| `ADDRESS_STATE_ID` | string |  |  | `ADDRESS_STATE_ID` |
| `ADDRESS_COUNTY_ID` | string |  |  | `ADDRESS_COUNTY_ID` |
| `ADDRESS_ZIP_CODE` | string |  |  | `ADDRESS_ZIP_CODE` |
| `ADDRESS_COUNTRY_REGION_ID` | string |  |  | `ADDRESS_COUNTRY_REGION_ID` |
| `FORMATTED_PRIMARY_ADDRESS` | string |  |  | `FORMATTED_PRIMARY_ADDRESS` |
| `PRIMARY_EMAIL_ADDRESS` | string |  |  | `PRIMARY_EMAIL_ADDRESS` |
| `PRIMARY_PHONE_NUMBER` | string |  |  | `PRIMARY_PHONE_NUMBER` |
| `PRIMARY_FAX_NUMBER` | string |  |  | `PRIMARY_FAX_NUMBER` |
| `PRIMARY_URL` | string |  |  | `PRIMARY_URL` |
| `CURRENCY_CODE` | string |  |  | `CURRENCY_CODE` |
| `DEFAULT_PAYMENT_TERMS_NAME` | string |  |  | `DEFAULT_PAYMENT_TERMS_NAME` |
| `DEFAULT_VENDOR_PAYMENT_METHOD_NAME` | string |  |  | `DEFAULT_VENDOR_PAYMENT_METHOD_NAME` |
| `PAYMENT_ID` | string |  |  | `PAYMENT_ID` |
| `BANK_ACCOUNT_ID` | string |  |  | `BANK_ACCOUNT_ID` |
| `CREDIT_LIMIT` | string |  |  | `CREDIT_LIMIT` |
| `EXCHANGE_RATE` | string |  |  | `EXCHANGE_RATE` |
| `FIXED_EXCHANGE_RATE` | string |  |  | `FIXED_EXCHANGE_RATE` |
| `SALES_TAX_GROUP_CODE` | string |  |  | `SALES_TAX_GROUP_CODE` |
| `TAX_1099_TYPE` | string |  |  | `TAX_1099_TYPE` |
| `TAX_1099_FEDERAL_TAX_ID` | string |  |  | `TAX_1099_FEDERAL_TAX_ID` |
| `TAX_1099_BOX_ID` | string |  |  | `TAX_1099_BOX_ID` |
| `PAN_NUMBER` | string |  |  | `PAN_NUMBER` |
| `PAN_STATUS` | string |  |  | `PAN_STATUS` |
| `ON_HOLD_STATUS` | string |  |  | `ON_HOLD_STATUS` |
| `IS_W9_RECEIVED` | string |  |  | `IS_W9_RECEIVED` |
| `IS_REPORTING_TAX_1099` | string |  |  | `IS_REPORTING_TAX_1099` |
| `VENDOR_HOLD_RELEASE_DATE` | string |  |  | `VENDOR_HOLD_RELEASE_DATE` |
| `VENDOR_LEAD_TIME` | string |  |  | `VENDOR_LEAD_TIME` |
| `ADDRESS_VALID_FROM` | string |  |  | `ADDRESS_VALID_FROM` |
| `ADDRESS_VALID_TO` | string |  |  | `ADDRESS_VALID_TO` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Profile

Rows in the latest export: unknown.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `DATA_AREA_ID` | STRING |  |  |  |  |
| `VENDOR_ACCOUNT_NUMBER` | STRING |  |  |  |  |
| `VENDOR_PARTY_NUMBER` | STRING |  |  |  |  |
| `VENDOR_ORGANIZATION_NAME` | STRING |  |  |  |  |
| `VENDOR_KNOWN_AS_NAME` | STRING |  |  |  |  |
| `VENDOR_SEARCH_NAME` | STRING |  |  |  |  |
| `VENDOR_GROUP_ID` | STRING |  |  |  |  |
| `VENDOR_TYPE` | STRING |  |  |  |  |
| `VENDOR_PARTY_TYPE` | STRING |  |  |  |  |
| `ADDRESS_STREET` | STRING |  |  |  |  |
| `ADDRESS_CITY` | STRING |  |  |  |  |
| `ADDRESS_STATE_ID` | STRING |  |  |  |  |
| `ADDRESS_COUNTY_ID` | STRING |  |  |  |  |
| `ADDRESS_ZIP_CODE` | STRING |  |  |  |  |
| `ADDRESS_COUNTRY_REGION_ID` | STRING |  |  |  |  |
| `FORMATTED_PRIMARY_ADDRESS` | STRING |  |  |  |  |
| `PRIMARY_EMAIL_ADDRESS` | STRING |  |  |  |  |
| `PRIMARY_PHONE_NUMBER` | STRING |  |  |  |  |
| `PRIMARY_FAX_NUMBER` | STRING |  |  |  |  |
| `PRIMARY_URL` | STRING |  |  |  |  |
| `CURRENCY_CODE` | STRING |  |  |  |  |
| `DEFAULT_PAYMENT_TERMS_NAME` | STRING |  |  |  |  |
| `DEFAULT_VENDOR_PAYMENT_METHOD_NAME` | STRING |  |  |  |  |
| `PAYMENT_ID` | STRING |  |  |  |  |
| `BANK_ACCOUNT_ID` | STRING |  |  |  |  |
| `CREDIT_LIMIT` | STRING |  |  |  |  |
| `EXCHANGE_RATE` | STRING |  |  |  |  |
| `FIXED_EXCHANGE_RATE` | STRING |  |  |  |  |
| `SALES_TAX_GROUP_CODE` | STRING |  |  |  |  |
| `TAX_1099_TYPE` | STRING |  |  |  |  |
| `TAX_1099_FEDERAL_TAX_ID` | STRING |  |  |  |  |
| `TAX_1099_BOX_ID` | STRING |  |  |  |  |
| `PAN_NUMBER` | STRING |  |  |  |  |
| `PAN_STATUS` | STRING |  |  |  |  |
| `ON_HOLD_STATUS` | STRING |  |  |  |  |
| `IS_W9_RECEIVED` | STRING |  |  |  |  |
| `IS_REPORTING_TAX_1099` | STRING |  |  |  |  |
| `VENDOR_HOLD_RELEASE_DATE` | STRING |  |  |  |  |
| `VENDOR_LEAD_TIME` | STRING |  |  |  |  |
| `ADDRESS_VALID_FROM` | STRING |  |  |  |  |
| `ADDRESS_VALID_TO` | STRING |  |  |  |  |
| `SOURCE_FILE_NAME` | STRING |  |  |  |  |
| `HASH_KEY` | STRING |  |  |  |  |
| `MDP_CREATED_BY` | STRING |  |  |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP |  |  |  |  |
| `MDP_MODIFIED_BY` | STRING |  |  |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP |  |  |  |  |
