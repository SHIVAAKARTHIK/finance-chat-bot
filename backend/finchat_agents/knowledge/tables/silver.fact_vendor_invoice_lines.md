---
name: fact_vendor_invoice_lines
schema: silver
layer: silver
domain: ap
type: table
status: active
purpose: Vendor invoice lines with procurement category.
grain: one row per DATA_AREA_ID + HEADER_REFERENCE + INVOICE_LINE_NUMBER (one invoice line)
primary_key: []
entity_column: DATA_AREA_ID
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues: []
row_count: 5
proposed_fields: []
reviewed: false
---

# fact_vendor_invoice_lines

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `DATA_AREA_ID` | string |  |  | `DATA_AREA_ID` |
| `HEADER_REFERENCE` | string |  |  | `HEADER_REFERENCE` |
| `INVOICE_LINE_NUMBER` | string |  |  | `INVOICE_LINE_NUMBER` |
| `PROCUREMENT_CATEGORY_HIERARCHY_NAME` | string |  |  | `PROCUREMENT_CATEGORY_HIERARCHY_NAME` |
| `TAX_1099_S_ADDRESS_OR_LEGAL_DESCRIPTION` | string |  |  | `TAX_1099_S_ADDRESS_OR_LEGAL_DESCRIPTION` |
| `PRICE_UNIT` | string |  |  | `PRICE_UNIT` |
| `TAX_1099_G_TAX_YEAR` | string |  |  | `TAX_1099_G_TAX_YEAR` |
| `INVOICE_ACCOUNT` | string |  |  | `INVOICE_ACCOUNT` |
| `ITEM_NUMBER` | string |  |  | `ITEM_NUMBER` |
| `ITEM_NAME` | string |  |  | `ITEM_NAME` |
| `MULTILINE_DISCOUNT_PERCENTAGE` | string |  |  | `MULTILINE_DISCOUNT_PERCENTAGE` |
| `INVENT_NOW` | string |  |  | `INVENT_NOW` |
| `ITEM_SALES_TAX` | string |  |  | `ITEM_SALES_TAX` |
| `MAIN_ACCOUNT_DISPLAY_VALUE` | string |  |  | `MAIN_ACCOUNT_DISPLAY_VALUE` |
| `WITHHOLDING_TAX_GROUP` | string |  |  | `WITHHOLDING_TAX_GROUP` |
| `REMAIN_AFTER_INVENT` | string |  |  | `REMAIN_AFTER_INVENT` |
| `PROCUREMENT_CATEGORY_NAME` | string |  |  | `PROCUREMENT_CATEGORY_NAME` |
| `IS_TAX_1099_S_PROPERTY_OR_SERVICES` | string |  |  | `IS_TAX_1099_S_PROPERTY_OR_SERVICES` |
| `PRODUCT_STYLE_ID` | string |  |  | `PRODUCT_STYLE_ID` |
| `RELEASE_ALL_RETAINED_AMOUNT` | string |  |  | `RELEASE_ALL_RETAINED_AMOUNT` |
| `TAX_WITHHOLD_GROUP` | string |  |  | `TAX_WITHHOLD_GROUP` |
| `PRODUCT_CONFIGURATION_ID` | string |  |  | `PRODUCT_CONFIGURATION_ID` |
| `PARTY_ID` | string |  |  | `PARTY_ID` |
| `TAX_1099_G_VENDOR_STATE_ID` | string |  |  | `TAX_1099_G_VENDOR_STATE_ID` |
| `DISCOUNT_PERCENT` | string |  |  | `DISCOUNT_PERCENT` |
| `ADJUSTED_UNIT_PRICE` | string |  |  | `ADJUSTED_UNIT_PRICE` |
| `TAX_1099_TYPE` | string |  |  | `TAX_1099_TYPE` |
| `MULTILINE_DISCOUNT` | string |  |  | `MULTILINE_DISCOUNT` |
| `ITEM_BATCH_NUMBER` | string |  |  | `ITEM_BATCH_NUMBER` |
| `CHANGE_QUANTITY_MANUALLY` | string |  |  | `CHANGE_QUANTITY_MANUALLY` |
| `PORT` | string |  |  | `PORT` |
| `TRANSACTION_CODE` | string |  |  | `TRANSACTION_CODE` |
| `IS_TAX_1099_G_TRADE_OR_BUSINESS_INCOME` | string |  |  | `IS_TAX_1099_G_TRADE_OR_BUSINESS_INCOME` |
| `INVENTORY_WAREHOUSE_ID` | string |  |  | `INVENTORY_WAREHOUSE_ID` |
| `TOTAL_RETAINED_AMOUNT` | string |  |  | `TOTAL_RETAINED_AMOUNT` |
| `TAX_1099_S_BUYER_PART_OF_REAL_ESTATE_TAX_AMOUNT` | string |  |  | `TAX_1099_S_BUYER_PART_OF_REAL_ESTATE_TAX_AMOUNT` |
| `DIMENSION_DISPLAY_VALUE` | string |  |  | `DIMENSION_DISPLAY_VALUE` |
| `PRODUCT_SIZE_ID` | string |  |  | `PRODUCT_SIZE_ID` |
| `ORIGINAL_DELIVER_REMAINDER` | string |  |  | `ORIGINAL_DELIVER_REMAINDER` |
| `TAX_1099_S_CLOSING_DATE` | string |  |  | `TAX_1099_S_CLOSING_DATE` |
| `UNIT` | string |  |  | `UNIT` |
| `VENDOR_INVOICE_LINE_REVIEW_STATUS` | string |  |  | `VENDOR_INVOICE_LINE_REVIEW_STATUS` |
| `RECEIVE_NOW` | string |  |  | `RECEIVE_NOW` |
| `TRANSPORT` | string |  |  | `TRANSPORT` |
| `BUDGET_RESERVATION_LINE_NUMBER` | string |  |  | `BUDGET_RESERVATION_LINE_NUMBER` |
| `AMOUNT` | string |  |  | `AMOUNT` |
| `STATE_OF_ORIGIN` | string |  |  | `STATE_OF_ORIGIN` |
| `REMAIN_BEFORE` | string |  |  | `REMAIN_BEFORE` |
| `LINE_TYPE` | string |  |  | `LINE_TYPE` |
| `CURRENCY` | string |  |  | `CURRENCY` |
| `DATA_AREA_COMPANY` | string |  |  | `DATA_AREA_COMPANY` |
| `PURCH_LINE_NUMBER` | string |  |  | `PURCH_LINE_NUMBER` |
| `ORDERED_INVENTORY_STATUS_ID` | string |  |  | `ORDERED_INVENTORY_STATUS_ID` |
| `COUNTY_ORIG_DEST` | string |  |  | `COUNTY_ORIG_DEST` |
| `RETAINAGE_AMOUNT` | string |  |  | `RETAINAGE_AMOUNT` |
| `PERCENTAGE` | string |  |  | `PERCENTAGE` |
| `NET_AMOUNT` | string |  |  | `NET_AMOUNT` |
| `CW_UPDATE` | string |  |  | `CW_UPDATE` |
| `PURCHASE_ORDER` | string |  |  | `PURCHASE_ORDER` |
| `ORDERING` | string |  |  | `ORDERING` |
| `PRODUCT_VERSION_ID` | string |  |  | `PRODUCT_VERSION_ID` |
| `TAX_1099_G_STATE_TAX_WITHHELD_AMOUNT` | string |  |  | `TAX_1099_G_STATE_TAX_WITHHELD_AMOUNT` |
| `ORIG_COUNTRY_REGION_ID` | string |  |  | `ORIG_COUNTRY_REGION_ID` |
| `OVERRIDE_SALES_TAX` | string |  |  | `OVERRIDE_SALES_TAX` |
| `LINE_DESCRIPTION` | string |  |  | `LINE_DESCRIPTION` |
| `RETAIN_PERCENTAGE` | string |  |  | `RETAIN_PERCENTAGE` |
| `REMAIN_BEFORE_INVENT` | string |  |  | `REMAIN_BEFORE_INVENT` |
| `PACKED_EXTENSIONS` | string |  |  | `PACKED_EXTENSIONS` |
| `IMPORTED_TAX_RATE` | string |  |  | `IMPORTED_TAX_RATE` |
| `DELIVERY_NAME` | string |  |  | `DELIVERY_NAME` |
| `TAX_1099_BOX` | string |  |  | `TAX_1099_BOX` |
| `CW_DELIVERY_REMAINDER` | string |  |  | `CW_DELIVERY_REMAINDER` |
| `TAX_SERVICE_CODE` | string |  |  | `TAX_SERVICE_CODE` |
| `VENDOR_ACCOUNT` | string |  |  | `VENDOR_ACCOUNT` |
| `CLOSE_FOR_RECEIPT` | string |  |  | `CLOSE_FOR_RECEIPT` |
| `REMAIN_AFTER` | string |  |  | `REMAIN_AFTER` |
| `LINE_NUMBER` | string |  |  | `LINE_NUMBER` |
| `UNIT_PRICE` | string |  |  | `UNIT_PRICE` |
| `BUDGET_RESERVATION_DOCUMENT_NUMBER` | string |  |  | `BUDGET_RESERVATION_DOCUMENT_NUMBER` |
| `SALES_TAX_GROUP` | string |  |  | `SALES_TAX_GROUP` |
| `CHARGES_ON_PURCHASES` | string |  |  | `CHARGES_ON_PURCHASES` |
| `PRODUCT_COLOR_ID` | string |  |  | `PRODUCT_COLOR_ID` |
| `TAX_WITHHOLD_ITEM_GROUP_NAME` | string |  |  | `TAX_WITHHOLD_ITEM_GROUP_NAME` |
| `CFOP_CODE` | string |  |  | `CFOP_CODE` |
| `TAX_1099_STATE_AMOUNT` | string |  |  | `TAX_1099_STATE_AMOUNT` |
| `ACCOUNTING_DISTRIBUTION_TEMPLATE_ID` | string |  |  | `ACCOUNTING_DISTRIBUTION_TEMPLATE_ID` |
| `STATISTICS_PROCEDURE` | string |  |  | `STATISTICS_PROCEDURE` |
| `CW_REMAINING_QUANTITY` | string |  |  | `CW_REMAINING_QUANTITY` |
| `DIMENSION_NUMBER` | string |  |  | `DIMENSION_NUMBER` |
| `TAX_1099_AMOUNT` | string |  |  | `TAX_1099_AMOUNT` |
| `FIN_TAG_DISPLAY_VALUE` | string |  |  | `FIN_TAG_DISPLAY_VALUE` |
| `PDS_CALCULATION_ID` | string |  |  | `PDS_CALCULATION_ID` |
| `TAX_1099_G_VENDOR_STATE_TAX_ID` | string |  |  | `TAX_1099_G_VENDOR_STATE_TAX_ID` |
| `WITHHOLDING_TAX_ITEM_GROUP` | string |  |  | `WITHHOLDING_TAX_ITEM_GROUP` |
| `IMPORTED_TAX` | string |  |  | `IMPORTED_TAX` |
| `DISCOUNT` | string |  |  | `DISCOUNT` |
| `DELIVERY_STATE` | string |  |  | `DELIVERY_STATE` |
| `INVENTORY_SITE_ID` | string |  |  | `INVENTORY_SITE_ID` |
| `COMMODITY` | string |  |  | `COMMODITY` |
| `DIOT_OPERATION_TYPE` | string |  |  | `DIOT_OPERATION_TYPE` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**HEADER_REFERENCE**
- `100-000456`: 1 rows
- `100-000431`: 1 rows
- `100-000546`: 1 rows
- `100-000460`: 1 rows
- `100-000543`: 1 rows

**INVOICE_LINE_NUMBER**
- `1`: 5 rows

**PROCUREMENT_CATEGORY_HIERARCHY_NAME**
- `Procurement Category`: 3 rows
- `Expense Category`: 2 rows

**TAX_1099_S_ADDRESS_OR_LEGAL_DESCRIPTION**
- `None`: 5 rows

**PRICE_UNIT**
- `1`: 5 rows

**TAX_1099_G_TAX_YEAR**
- `0`: 5 rows

**INVOICE_ACCOUNT**
- `100-000117`: 1 rows
- `100-000002`: 1 rows
- `100-000001`: 1 rows
- `100-000118`: 1 rows
- `100-000116`: 1 rows

**ITEM_NUMBER**
- `None`: 5 rows

**ITEM_NAME**
- `None`: 5 rows

**MULTILINE_DISCOUNT_PERCENTAGE**
- `0`: 5 rows

**INVENT_NOW**
- `0`: 5 rows

**ITEM_SALES_TAX**
- `None`: 5 rows

**MAIN_ACCOUNT_DISPLAY_VALUE**
- `None`: 5 rows

**WITHHOLDING_TAX_GROUP**
- `None`: 5 rows

**REMAIN_AFTER_INVENT**
- `0`: 5 rows

**PROCUREMENT_CATEGORY_NAME**
- `Office Rent`: 2 rows
- `Building`: 1 rows
- `Computer/Laptop`: 1 rows
- `Furniture`: 1 rows

**IS_TAX_1099_S_PROPERTY_OR_SERVICES**
- `No`: 5 rows

**PRODUCT_STYLE_ID**
- `None`: 5 rows

**RELEASE_ALL_RETAINED_AMOUNT**
- `No`: 5 rows

**TAX_WITHHOLD_GROUP**
- `None`: 5 rows

**PRODUCT_CONFIGURATION_ID**
- `None`: 5 rows

**PARTY_ID**
- `None`: 5 rows

**TAX_1099_G_VENDOR_STATE_ID**
- `None`: 5 rows

**DISCOUNT_PERCENT**
- `0`: 5 rows

**ADJUSTED_UNIT_PRICE**
- `0`: 5 rows

**TAX_1099_TYPE**
- `None`: 5 rows

**MULTILINE_DISCOUNT**
- `0`: 5 rows

**ITEM_BATCH_NUMBER**
- `None`: 5 rows

**CHANGE_QUANTITY_MANUALLY**
- `No`: 5 rows

**PORT**
- `None`: 5 rows

**TRANSACTION_CODE**
- `None`: 5 rows

**IS_TAX_1099_G_TRADE_OR_BUSINESS_INCOME**
- `No`: 5 rows

**INVENTORY_WAREHOUSE_ID**
- `None`: 5 rows

**TOTAL_RETAINED_AMOUNT**
- `0`: 5 rows

**TAX_1099_S_BUYER_PART_OF_REAL_ESTATE_TAX_AMOUNT**
- `0`: 5 rows

**DIMENSION_DISPLAY_VALUE**
- `None`: 5 rows

**PRODUCT_SIZE_ID**
- `None`: 5 rows

**ORIGINAL_DELIVER_REMAINDER**
- `0`: 5 rows

**TAX_1099_S_CLOSING_DATE**
- `1900-01-01 12:00:00.0000000 +00:00`: 5 rows

**UNIT**
- `None`: 5 rows

**VENDOR_INVOICE_LINE_REVIEW_STATUS**
- `Draft`: 5 rows

**RECEIVE_NOW**
- `1`: 4 rows
- `10`: 1 rows

**TRANSPORT**
- `None`: 5 rows

**BUDGET_RESERVATION_LINE_NUMBER**
- `0`: 5 rows

**AMOUNT**
- `0`: 5 rows

**STATE_OF_ORIGIN**
- `None`: 5 rows

**REMAIN_BEFORE**
- `1`: 3 rows
- `0`: 2 rows

**LINE_TYPE**
- `Standard`: 5 rows

**CURRENCY**
- `USD`: 5 rows

**PURCH_LINE_NUMBER**
- `1`: 3 rows
- `0`: 2 rows

**ORDERED_INVENTORY_STATUS_ID**
- `None`: 5 rows

**COUNTY_ORIG_DEST**
- `None`: 5 rows

**RETAINAGE_AMOUNT**
- `0`: 5 rows

**PERCENTAGE**
- `0`: 5 rows

**NET_AMOUNT**
- `1200`: 1 rows
- `200`: 1 rows
- `7500`: 1 rows
- `7700`: 1 rows
- `7600`: 1 rows

**CW_UPDATE**
- `0`: 5 rows

**PURCHASE_ORDER**
- `None`: 2 rows
- `100-000059`: 1 rows
- `100-000057`: 1 rows
- `100-000058`: 1 rows

**ORDERING**
- `None`: 5 rows

**PRODUCT_VERSION_ID**
- `None`: 5 rows

**TAX_1099_G_STATE_TAX_WITHHELD_AMOUNT**
- `0`: 5 rows

**ORIG_COUNTRY_REGION_ID**
- `None`: 5 rows

**OVERRIDE_SALES_TAX**
- `No`: 5 rows

**LINE_DESCRIPTION**
- `None`: 3 rows
- `Office Rent`: 2 rows

**RETAIN_PERCENTAGE**
- `0`: 5 rows

**REMAIN_BEFORE_INVENT**
- `0`: 5 rows

**PACKED_EXTENSIONS**
- `None`: 5 rows

**IMPORTED_TAX_RATE**
- `0`: 5 rows

**DELIVERY_NAME**
- `Busines`: 3 rows
- `Evergreen Solutions`: 2 rows

**TAX_1099_BOX**
- `None`: 5 rows

**CW_DELIVERY_REMAINDER**
- `0`: 5 rows

**TAX_SERVICE_CODE**
- `None`: 5 rows

**VENDOR_ACCOUNT**
- `100-000117`: 1 rows
- `100-000002`: 1 rows
- `100-000001`: 1 rows
- `100-000118`: 1 rows
- `100-000116`: 1 rows

**CLOSE_FOR_RECEIPT**
- `No`: 5 rows

**REMAIN_AFTER**
- `0`: 5 rows

**LINE_NUMBER**
- `1`: 3 rows
- `0`: 2 rows

**UNIT_PRICE**
- `200`: 1 rows
- `7700`: 1 rows
- `7500`: 1 rows
- `120`: 1 rows
- `7600`: 1 rows

**BUDGET_RESERVATION_DOCUMENT_NUMBER**
- `None`: 5 rows

**SALES_TAX_GROUP**
- `None`: 5 rows

**CHARGES_ON_PURCHASES**
- `0`: 5 rows

**PRODUCT_COLOR_ID**
- `None`: 5 rows

**TAX_WITHHOLD_ITEM_GROUP_NAME**
- `None`: 5 rows

**CFOP_CODE**
- `None`: 5 rows

**TAX_1099_STATE_AMOUNT**
- `0`: 5 rows

**ACCOUNTING_DISTRIBUTION_TEMPLATE_ID**
- `None`: 5 rows

**STATISTICS_PROCEDURE**
- `None`: 5 rows

**CW_REMAINING_QUANTITY**
- `0`: 5 rows

**DIMENSION_NUMBER**
- `AllBlank`: 5 rows

**TAX_1099_AMOUNT**
- `0`: 5 rows

**FIN_TAG_DISPLAY_VALUE**
- `None`: 5 rows

**PDS_CALCULATION_ID**
- `None`: 5 rows

**TAX_1099_G_VENDOR_STATE_TAX_ID**
- `None`: 5 rows

**WITHHOLDING_TAX_ITEM_GROUP**
- `None`: 5 rows

**IMPORTED_TAX**
- `0`: 5 rows

**DISCOUNT**
- `0`: 5 rows

**DELIVERY_STATE**
- `None`: 5 rows

**INVENTORY_SITE_ID**
- `None`: 5 rows

**COMMODITY**
- `None`: 5 rows

**DIOT_OPERATION_TYPE**
- `Blank`: 5 rows

**SOURCE_FILE_NAME**
- `vendorinvoicelines__20261116_105417.csv`: 5 rows

**MDP_CREATED_DATE**
- `2026-11-16 11:41:50.989379+00:00`: 5 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 11:41:50.989379+00:00`: 5 rows

## Profile

Rows in the latest export: 5.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `DATA_AREA_ID` | STRING | 1 | 0 |  |  |
| `HEADER_REFERENCE` | STRING | 5 | 0 | 100-000431 | 100-000546 |
| `INVOICE_LINE_NUMBER` | STRING | 1 | 0 | 1 | 1 |
| `PROCUREMENT_CATEGORY_HIERARCHY_NAME` | STRING | 2 | 0 | Expense Category | Procurement Category |
| `TAX_1099_S_ADDRESS_OR_LEGAL_DESCRIPTION` | STRING | 0 | 5 |  |  |
| `PRICE_UNIT` | STRING | 1 | 0 | 1 | 1 |
| `TAX_1099_G_TAX_YEAR` | STRING | 1 | 0 | 0 | 0 |
| `INVOICE_ACCOUNT` | STRING | 5 | 0 | 100-000001 | 100-000118 |
| `ITEM_NUMBER` | STRING | 0 | 5 |  |  |
| `ITEM_NAME` | STRING | 0 | 5 |  |  |
| `MULTILINE_DISCOUNT_PERCENTAGE` | STRING | 1 | 0 | 0 | 0 |
| `INVENT_NOW` | STRING | 1 | 0 | 0 | 0 |
| `ITEM_SALES_TAX` | STRING | 0 | 5 |  |  |
| `MAIN_ACCOUNT_DISPLAY_VALUE` | STRING | 0 | 5 |  |  |
| `WITHHOLDING_TAX_GROUP` | STRING | 0 | 5 |  |  |
| `REMAIN_AFTER_INVENT` | STRING | 1 | 0 | 0 | 0 |
| `PROCUREMENT_CATEGORY_NAME` | STRING | 4 | 0 | Building | Office Rent |
| `IS_TAX_1099_S_PROPERTY_OR_SERVICES` | STRING | 1 | 0 | No | No |
| `PRODUCT_STYLE_ID` | STRING | 0 | 5 |  |  |
| `RELEASE_ALL_RETAINED_AMOUNT` | STRING | 1 | 0 | No | No |
| `TAX_WITHHOLD_GROUP` | STRING | 0 | 5 |  |  |
| `PRODUCT_CONFIGURATION_ID` | STRING | 0 | 5 |  |  |
| `PARTY_ID` | STRING | 0 | 5 |  |  |
| `TAX_1099_G_VENDOR_STATE_ID` | STRING | 0 | 5 |  |  |
| `DISCOUNT_PERCENT` | STRING | 1 | 0 | 0 | 0 |
| `ADJUSTED_UNIT_PRICE` | STRING | 1 | 0 | 0 | 0 |
| `TAX_1099_TYPE` | STRING | 0 | 5 |  |  |
| `MULTILINE_DISCOUNT` | STRING | 1 | 0 | 0 | 0 |
| `ITEM_BATCH_NUMBER` | STRING | 0 | 5 |  |  |
| `CHANGE_QUANTITY_MANUALLY` | STRING | 1 | 0 | No | No |
| `PORT` | STRING | 0 | 5 |  |  |
| `TRANSACTION_CODE` | STRING | 0 | 5 |  |  |
| `IS_TAX_1099_G_TRADE_OR_BUSINESS_INCOME` | STRING | 1 | 0 | No | No |
| `INVENTORY_WAREHOUSE_ID` | STRING | 0 | 5 |  |  |
| `TOTAL_RETAINED_AMOUNT` | STRING | 1 | 0 | 0 | 0 |
| `TAX_1099_S_BUYER_PART_OF_REAL_ESTATE_TAX_AMOUNT` | STRING | 1 | 0 | 0 | 0 |
| `DIMENSION_DISPLAY_VALUE` | STRING | 0 | 5 |  |  |
| `PRODUCT_SIZE_ID` | STRING | 0 | 5 |  |  |
| `ORIGINAL_DELIVER_REMAINDER` | STRING | 1 | 0 | 0 | 0 |
| `TAX_1099_S_CLOSING_DATE` | STRING | 1 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `UNIT` | STRING | 0 | 5 |  |  |
| `VENDOR_INVOICE_LINE_REVIEW_STATUS` | STRING | 1 | 0 | Draft | Draft |
| `RECEIVE_NOW` | STRING | 2 | 0 | 1 | 10 |
| `TRANSPORT` | STRING | 0 | 5 |  |  |
| `BUDGET_RESERVATION_LINE_NUMBER` | STRING | 1 | 0 | 0 | 0 |
| `AMOUNT` | STRING | 1 | 0 | 0 | 0 |
| `STATE_OF_ORIGIN` | STRING | 0 | 5 |  |  |
| `REMAIN_BEFORE` | STRING | 2 | 0 | 0 | 1 |
| `LINE_TYPE` | STRING | 1 | 0 | Standard | Standard |
| `CURRENCY` | STRING | 1 | 0 | USD | USD |
| `DATA_AREA_COMPANY` | STRING | 0 | 5 |  |  |
| `PURCH_LINE_NUMBER` | STRING | 2 | 0 | 0 | 1 |
| `ORDERED_INVENTORY_STATUS_ID` | STRING | 0 | 5 |  |  |
| `COUNTY_ORIG_DEST` | STRING | 0 | 5 |  |  |
| `RETAINAGE_AMOUNT` | STRING | 1 | 0 | 0 | 0 |
| `PERCENTAGE` | STRING | 1 | 0 | 0 | 0 |
| `NET_AMOUNT` | STRING | 5 | 0 | 1200 | 7700 |
| `CW_UPDATE` | STRING | 1 | 0 | 0 | 0 |
| `PURCHASE_ORDER` | STRING | 3 | 2 | 100-000057 | 100-000059 |
| `ORDERING` | STRING | 1 | 0 | None | None |
| `PRODUCT_VERSION_ID` | STRING | 0 | 5 |  |  |
| `TAX_1099_G_STATE_TAX_WITHHELD_AMOUNT` | STRING | 1 | 0 | 0 | 0 |
| `ORIG_COUNTRY_REGION_ID` | STRING | 0 | 5 |  |  |
| `OVERRIDE_SALES_TAX` | STRING | 1 | 0 | No | No |
| `LINE_DESCRIPTION` | STRING | 1 | 3 | Office Rent | Office Rent |
| `RETAIN_PERCENTAGE` | STRING | 1 | 0 | 0 | 0 |
| `REMAIN_BEFORE_INVENT` | STRING | 1 | 0 | 0 | 0 |
| `PACKED_EXTENSIONS` | STRING | 0 | 5 |  |  |
| `IMPORTED_TAX_RATE` | STRING | 1 | 0 | 0 | 0 |
| `DELIVERY_NAME` | STRING | 2 | 0 | Busines | Evergreen Solutions |
| `TAX_1099_BOX` | STRING | 0 | 5 |  |  |
| `CW_DELIVERY_REMAINDER` | STRING | 1 | 0 | 0 | 0 |
| `TAX_SERVICE_CODE` | STRING | 0 | 5 |  |  |
| `VENDOR_ACCOUNT` | STRING | 5 | 0 | 100-000001 | 100-000118 |
| `CLOSE_FOR_RECEIPT` | STRING | 1 | 0 | No | No |
| `REMAIN_AFTER` | STRING | 1 | 0 | 0 | 0 |
| `LINE_NUMBER` | STRING | 2 | 0 | 0 | 1 |
| `UNIT_PRICE` | STRING | 5 | 0 | 120 | 7700 |
| `BUDGET_RESERVATION_DOCUMENT_NUMBER` | STRING | 0 | 5 |  |  |
| `SALES_TAX_GROUP` | STRING | 0 | 5 |  |  |
| `CHARGES_ON_PURCHASES` | STRING | 1 | 0 | 0 | 0 |
| `PRODUCT_COLOR_ID` | STRING | 0 | 5 |  |  |
| `TAX_WITHHOLD_ITEM_GROUP_NAME` | STRING | 0 | 5 |  |  |
| `CFOP_CODE` | STRING | 0 | 5 |  |  |
| `TAX_1099_STATE_AMOUNT` | STRING | 1 | 0 | 0 | 0 |
| `ACCOUNTING_DISTRIBUTION_TEMPLATE_ID` | STRING | 0 | 5 |  |  |
| `STATISTICS_PROCEDURE` | STRING | 0 | 5 |  |  |
| `CW_REMAINING_QUANTITY` | STRING | 1 | 0 | 0 | 0 |
| `DIMENSION_NUMBER` | STRING | 1 | 0 | AllBlank | AllBlank |
| `TAX_1099_AMOUNT` | STRING | 1 | 0 | 0 | 0 |
| `FIN_TAG_DISPLAY_VALUE` | STRING | 0 | 5 |  |  |
| `PDS_CALCULATION_ID` | STRING | 0 | 5 |  |  |
| `TAX_1099_G_VENDOR_STATE_TAX_ID` | STRING | 0 | 5 |  |  |
| `WITHHOLDING_TAX_ITEM_GROUP` | STRING | 0 | 5 |  |  |
| `IMPORTED_TAX` | STRING | 1 | 0 | 0 | 0 |
| `DISCOUNT` | STRING | 1 | 0 | 0 | 0 |
| `DELIVERY_STATE` | STRING | 0 | 5 |  |  |
| `INVENTORY_SITE_ID` | STRING | 0 | 5 |  |  |
| `COMMODITY` | STRING | 0 | 5 |  |  |
| `DIOT_OPERATION_TYPE` | STRING | 1 | 0 | Blank | Blank |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | vendorinvoicelines__20261116_105417.csv | vendorinvoicelines__20261116_105417.csv |
| `HASH_KEY` | STRING | 5 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:41:50.989000 | 2026-11-16 11:41:50.989000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:41:50.989000 | 2026-11-16 11:41:50.989000 |

## Sample rows

| HEADER_REFERENCE | INVOICE_LINE_NUMBER | PROCUREMENT_CATEGORY_HIERARCHY_NAME | TAX_1099_S_ADDRESS_OR_LEGAL_DESCRIPTION | PRICE_UNIT | TAX_1099_G_TAX_YEAR | INVOICE_ACCOUNT | ITEM_NUMBER | ITEM_NAME | MULTILINE_DISCOUNT_PERCENTAGE | INVENT_NOW | ITEM_SALES_TAX | MAIN_ACCOUNT_DISPLAY_VALUE | WITHHOLDING_TAX_GROUP | REMAIN_AFTER_INVENT | PROCUREMENT_CATEGORY_NAME | IS_TAX_1099_S_PROPERTY_OR_SERVICES | PRODUCT_STYLE_ID | RELEASE_ALL_RETAINED_AMOUNT | TAX_WITHHOLD_GROUP | PRODUCT_CONFIGURATION_ID | PARTY_ID | TAX_1099_G_VENDOR_STATE_ID | DISCOUNT_PERCENT | ADJUSTED_UNIT_PRICE | TAX_1099_TYPE | MULTILINE_DISCOUNT | ITEM_BATCH_NUMBER | CHANGE_QUANTITY_MANUALLY | PORT | TRANSACTION_CODE | IS_TAX_1099_G_TRADE_OR_BUSINESS_INCOME | INVENTORY_WAREHOUSE_ID | TOTAL_RETAINED_AMOUNT | TAX_1099_S_BUYER_PART_OF_REAL_ESTATE_TAX_AMOUNT | DIMENSION_DISPLAY_VALUE | PRODUCT_SIZE_ID | ORIGINAL_DELIVER_REMAINDER | TAX_1099_S_CLOSING_DATE | UNIT | VENDOR_INVOICE_LINE_REVIEW_STATUS | RECEIVE_NOW | TRANSPORT | BUDGET_RESERVATION_LINE_NUMBER | AMOUNT | STATE_OF_ORIGIN | REMAIN_BEFORE | LINE_TYPE | CURRENCY | PURCH_LINE_NUMBER | ORDERED_INVENTORY_STATUS_ID | COUNTY_ORIG_DEST | RETAINAGE_AMOUNT | PERCENTAGE | NET_AMOUNT | CW_UPDATE | PURCHASE_ORDER | ORDERING | PRODUCT_VERSION_ID | TAX_1099_G_STATE_TAX_WITHHELD_AMOUNT | ORIG_COUNTRY_REGION_ID | OVERRIDE_SALES_TAX | LINE_DESCRIPTION | RETAIN_PERCENTAGE | REMAIN_BEFORE_INVENT | PACKED_EXTENSIONS | IMPORTED_TAX_RATE | DELIVERY_NAME | TAX_1099_BOX | CW_DELIVERY_REMAINDER | TAX_SERVICE_CODE | VENDOR_ACCOUNT | CLOSE_FOR_RECEIPT | REMAIN_AFTER | LINE_NUMBER | UNIT_PRICE | BUDGET_RESERVATION_DOCUMENT_NUMBER | SALES_TAX_GROUP | CHARGES_ON_PURCHASES | PRODUCT_COLOR_ID | TAX_WITHHOLD_ITEM_GROUP_NAME | CFOP_CODE | TAX_1099_STATE_AMOUNT | ACCOUNTING_DISTRIBUTION_TEMPLATE_ID | STATISTICS_PROCEDURE | CW_REMAINING_QUANTITY | DIMENSION_NUMBER | TAX_1099_AMOUNT | FIN_TAG_DISPLAY_VALUE | PDS_CALCULATION_ID | TAX_1099_G_VENDOR_STATE_TAX_ID | WITHHOLDING_TAX_ITEM_GROUP | IMPORTED_TAX | DISCOUNT | DELIVERY_STATE | INVENTORY_SITE_ID | COMMODITY | DIOT_OPERATION_TYPE | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 100-000431 | 1 | Procurement Category | NULL | 1 | 0 | 100-000116 | NULL | NULL | 0 | 0 | NULL | NULL | NULL | 0 | Building | No | NULL | No | NULL | NULL | NULL | NULL | 0 | 0 | NULL | 0 | NULL | No | NULL | NULL | No | NULL | 0 | 0 | NULL | NULL | 0 | 1900-01-01 12:00:00.0000000 +00:00 | NULL | Draft | 1 | NULL | 0 | 0 | NULL | 1 | Standard | USD | 1 | NULL | NULL | 0 | 0 | 7500 | 0 | 100-000057 | None | NULL | 0 | NULL | No | NULL | 0 | 0 | NULL | 0 | Busines | NULL | 0 | NULL | 100-000116 | No | 0 | 1 | 7500 | NULL | NULL | 0 | NULL | NULL | NULL | 0 | NULL | NULL | 0 | AllBlank | 0 | NULL | NULL | NULL | NULL | 0 | 0 | NULL | NULL | NULL | Blank | vendorinvoicelines__20261116_105417.csv | <masked> | 2026-11-16 11:41:50.989000 | <masked> | 2026-11-16 11:41:50.989000 |
| 100-000456 | 1 | Procurement Category | NULL | 1 | 0 | 100-000117 | NULL | NULL | 0 | 0 | NULL | NULL | NULL | 0 | Computer/Laptop | No | NULL | No | NULL | NULL | NULL | NULL | 0 | 0 | NULL | 0 | NULL | No | NULL | NULL | No | NULL | 0 | 0 | NULL | NULL | 0 | 1900-01-01 12:00:00.0000000 +00:00 | NULL | Draft | 1 | NULL | 0 | 0 | NULL | 1 | Standard | USD | 1 | NULL | NULL | 0 | 0 | 7600 | 0 | 100-000058 | None | NULL | 0 | NULL | No | NULL | 0 | 0 | NULL | 0 | Busines | NULL | 0 | NULL | 100-000117 | No | 0 | 1 | 7600 | NULL | NULL | 0 | NULL | NULL | NULL | 0 | NULL | NULL | 0 | AllBlank | 0 | NULL | NULL | NULL | NULL | 0 | 0 | NULL | NULL | NULL | Blank | vendorinvoicelines__20261116_105417.csv | <masked> | 2026-11-16 11:41:50.989000 | <masked> | 2026-11-16 11:41:50.989000 |
| 100-000460 | 1 | Procurement Category | NULL | 1 | 0 | 100-000118 | NULL | NULL | 0 | 0 | NULL | NULL | NULL | 0 | Furniture | No | NULL | No | NULL | NULL | NULL | NULL | 0 | 0 | NULL | 0 | NULL | No | NULL | NULL | No | NULL | 0 | 0 | NULL | NULL | 0 | 1900-01-01 12:00:00.0000000 +00:00 | NULL | Draft | 1 | NULL | 0 | 0 | NULL | 1 | Standard | USD | 1 | NULL | NULL | 0 | 0 | 7700 | 0 | 100-000059 | None | NULL | 0 | NULL | No | NULL | 0 | 0 | NULL | 0 | Busines | NULL | 0 | NULL | 100-000118 | No | 0 | 1 | 7700 | NULL | NULL | 0 | NULL | NULL | NULL | 0 | NULL | NULL | 0 | AllBlank | 0 | NULL | NULL | NULL | NULL | 0 | 0 | NULL | NULL | NULL | Blank | vendorinvoicelines__20261116_105417.csv | <masked> | 2026-11-16 11:41:50.989000 | <masked> | 2026-11-16 11:41:50.989000 |
| 100-000543 | 1 | Expense Category | NULL | 1 | 0 | 100-000002 | NULL | NULL | 0 | 0 | NULL | NULL | NULL | 0 | Office Rent | No | NULL | No | NULL | NULL | NULL | NULL | 0 | 0 | NULL | 0 | NULL | No | NULL | NULL | No | NULL | 0 | 0 | NULL | NULL | 0 | 1900-01-01 12:00:00.0000000 +00:00 | NULL | Draft | 1 | NULL | 0 | 0 | NULL | 0 | Standard | USD | 0 | NULL | NULL | 0 | 0 | 200 | 0 | NULL | None | NULL | 0 | NULL | No | Office Rent | 0 | 0 | NULL | 0 | Evergreen Solutions | NULL | 0 | NULL | 100-000002 | No | 0 | 0 | 200 | NULL | NULL | 0 | NULL | NULL | NULL | 0 | NULL | NULL | 0 | AllBlank | 0 | NULL | NULL | NULL | NULL | 0 | 0 | NULL | NULL | NULL | Blank | vendorinvoicelines__20261116_105417.csv | <masked> | 2026-11-16 11:41:50.989000 | <masked> | 2026-11-16 11:41:50.989000 |
| 100-000546 | 1 | Expense Category | NULL | 1 | 0 | 100-000001 | NULL | NULL | 0 | 0 | NULL | NULL | NULL | 0 | Office Rent | No | NULL | No | NULL | NULL | NULL | NULL | 0 | 0 | NULL | 0 | NULL | No | NULL | NULL | No | NULL | 0 | 0 | NULL | NULL | 0 | 1900-01-01 12:00:00.0000000 +00:00 | NULL | Draft | 10 | NULL | 0 | 0 | NULL | 0 | Standard | USD | 0 | NULL | NULL | 0 | 0 | 1200 | 0 | NULL | None | NULL | 0 | NULL | No | Office Rent | 0 | 0 | NULL | 0 | Evergreen Solutions | NULL | 0 | NULL | 100-000001 | No | 0 | 0 | 120 | NULL | NULL | 0 | NULL | NULL | NULL | 0 | NULL | NULL | 0 | AllBlank | 0 | NULL | NULL | NULL | NULL | 0 | 0 | NULL | NULL | NULL | Blank | vendorinvoicelines__20261116_105417.csv | <masked> | 2026-11-16 11:41:50.989000 | <masked> | 2026-11-16 11:41:50.989000 |
