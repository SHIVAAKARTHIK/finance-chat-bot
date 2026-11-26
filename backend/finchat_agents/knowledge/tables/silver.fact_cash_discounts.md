---
name: fact_cash_discounts
schema: silver
layer: silver
domain: ap
type: table
status: active
purpose: Cash discount terms (code; percent) for vendor and customer payments.
grain: one row per DATA_AREA_ID + CASH_DISCOUNT_CODE (one discount term)
primary_key: []
entity_column: DATA_AREA_ID
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues:
- code: empty_column
  note: table is empty (0 rows)
proposed_fields: []
reviewed: false
---

# fact_cash_discounts

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `DATA_AREA_ID` | string |  |  | `DATA_AREA_ID` |
| `CASH_DISCOUNT_CODE` | string |  |  | `CASH_DISCOUNT_CODE` |
| `PERCENT` | string |  |  | `PERCENT` |
| `OFFSET_METHOD_FOR_VENDOR_DISCOUNTS` | string |  |  | `OFFSET_METHOD_FOR_VENDOR_DISCOUNTS` |
| `NEXT_CASH_DISCOUNT_CODE` | string |  |  | `NEXT_CASH_DISCOUNT_CODE` |
| `NUMBER_OF_MONTHS` | string |  |  | `NUMBER_OF_MONTHS` |
| `DESCRIPTION` | string |  |  | `DESCRIPTION` |
| `MAIN_ACCOUNT_ID_FOR_CUSTOMER_DISCOUNTS_DISPLAY_VALUE` | string |  |  | `MAIN_ACCOUNT_ID_FOR_CUSTOMER_DISCOUNTS_DISPLAY_VALUE` |
| `DISCOUNT_METHOD` | string |  |  | `DISCOUNT_METHOD` |
| `MAIN_ACCOUNT_ID_FOR_VENDOR_DISCOUNTS_DISPLAY_VALUE` | string |  |  | `MAIN_ACCOUNT_ID_FOR_VENDOR_DISCOUNTS_DISPLAY_VALUE` |
| `NUMBER_OF_DAYS` | string |  |  | `NUMBER_OF_DAYS` |
| `DESCRIPTION_QR_BILL` | string |  |  | `DESCRIPTION_QR_BILL` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Empty columns

Empty in every row: `DATA_AREA_ID`, `CASH_DISCOUNT_CODE`, `PERCENT`, `OFFSET_METHOD_FOR_VENDOR_DISCOUNTS`, `NEXT_CASH_DISCOUNT_CODE`, `NUMBER_OF_MONTHS`, `DESCRIPTION`, `MAIN_ACCOUNT_ID_FOR_CUSTOMER_DISCOUNTS_DISPLAY_VALUE`, `DISCOUNT_METHOD`, `MAIN_ACCOUNT_ID_FOR_VENDOR_DISCOUNTS_DISPLAY_VALUE`, `NUMBER_OF_DAYS`, `DESCRIPTION_QR_BILL`, `SOURCE_FILE_NAME`, `HASH_KEY`, `MDP_CREATED_BY`, `MDP_CREATED_DATE`, `MDP_MODIFIED_BY`, `MDP_MODIFIED_DATE`. Do not filter or group on them.
