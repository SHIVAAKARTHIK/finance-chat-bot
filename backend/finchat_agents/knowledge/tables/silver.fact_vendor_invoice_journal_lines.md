---
name: fact_vendor_invoice_journal_lines
schema: silver
layer: silver
domain: ap
type: table
status: active
purpose: Lines of vendor invoice journals.
grain: one row per DATA_AREA_ID + JOURNAL_BATCH_NUMBER + LINE_NUMBER (one invoice journal line)
primary_key: []
entity_column: DATA_AREA_ID
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
- APPROVER_NUMBER
synonyms: []
built_from: []
known_issues:
- code: duplicates
  note: 158 exact duplicate rows in the latest export (55.4%). Check duplicates at the grain before counting or summing; warn
    the user.
proposed_fields: []
reviewed: false
---

# fact_vendor_invoice_journal_lines

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `DATA_AREA_ID` | string |  |  | `DATA_AREA_ID` |
| `JOURNAL_BATCH_NUMBER` | string |  |  | `JOURNAL_BATCH_NUMBER` |
| `LINE_NUMBER` | string |  |  | `LINE_NUMBER` |
| `ACCOUNT_DISPLAY_VALUE` | string |  |  | `ACCOUNT_DISPLAY_VALUE` |
| `INVOICE_DECLARATION_ID` | string |  |  | `INVOICE_DECLARATION_ID` |
| `CASH_DISCOUNT_AMOUNT` | string |  |  | `CASH_DISCOUNT_AMOUNT` |
| `UUID` | string |  |  | `UUID` |
| `OFFSET_FIN_TAG_DISPLAY_VALUE` | string |  |  | `OFFSET_FIN_TAG_DISPLAY_VALUE` |
| `POSTING_PROFILE` | string |  |  | `POSTING_PROFILE` |
| `LIST_CODE` | string |  |  | `LIST_CODE` |
| `OFFSET_DEFAULT_DIMENSION_DISPLAY_VALUE` | string |  |  | `OFFSET_DEFAULT_DIMENSION_DISPLAY_VALUE` |
| `REPORTING_CURRENCY_EXCH_RATE` | string |  |  | `REPORTING_CURRENCY_EXCH_RATE` |
| `PAYMENT_ID` | string |  |  | `PAYMENT_ID` |
| `ACCOUNT_TYPE` | string |  |  | `ACCOUNT_TYPE` |
| `TERMS_OF_PAYMENT` | string |  |  | `TERMS_OF_PAYMENT` |
| `REMITTANCE_ADDRESS_STREET` | string |  |  | `REMITTANCE_ADDRESS_STREET` |
| `REMITTANCE_ADDRESS_DISTRICT_NAME` | string |  |  | `REMITTANCE_ADDRESS_DISTRICT_NAME` |
| `EXCHANGE_RATE_SECOND` | string |  |  | `EXCHANGE_RATE_SECOND` |
| `TRANSACTION_TYPE` | string |  |  | `TRANSACTION_TYPE` |
| `CHINESE_VOUCHER` | string |  |  | `CHINESE_VOUCHER` |
| `TAX_1099_FIELDS` | string |  |  | `TAX_1099_FIELDS` |
| `METHOD_OF_PAYMENT` | string |  |  | `METHOD_OF_PAYMENT` |
| `CHINESE_VOUCHER_TYPE` | string |  |  | `CHINESE_VOUCHER_TYPE` |
| `ASSET_ID` | string |  |  | `ASSET_ID` |
| `REMITTANCE_ADDRESS_CITY` | string |  |  | `REMITTANCE_ADDRESS_CITY` |
| `EXCHANGE_RATE` | string |  |  | `EXCHANGE_RATE` |
| `DOCUMENT` | string |  |  | `DOCUMENT` |
| `DESCRIPTION` | string |  |  | `DESCRIPTION` |
| `REMITTANCE_ADDRESS_STATE` | string |  |  | `REMITTANCE_ADDRESS_STATE` |
| `REMITTANCE_ADDRESS_ZIP_CODE` | string |  |  | `REMITTANCE_ADDRESS_ZIP_CODE` |
| `INVOICE` | string |  |  | `INVOICE` |
| `DELIVERY_DATE` | string |  |  | `DELIVERY_DATE` |
| `OVERRIDE_SALES_TAX_BR` | string |  |  | `OVERRIDE_SALES_TAX_BR` |
| `REMITTANCE_ADDRESS_COUNTY` | string |  |  | `REMITTANCE_ADDRESS_COUNTY` |
| `DATE` | string |  |  | `DATE` |
| `REMITTANCE_ADDRESS_LOCATION_ID` | string |  |  | `REMITTANCE_ADDRESS_LOCATION_ID` |
| `VOUCHER` | string |  |  | `VOUCHER` |
| `APPROVER_NUMBER` | string |  |  | `APPROVER_NUMBER` |
| `APPROVED` | string |  |  | `APPROVED` |
| `CASH_DISCOUNT` | string |  |  | `CASH_DISCOUNT` |
| `TAX_EXEMPT_NUMBER` | string |  |  | `TAX_EXEMPT_NUMBER` |
| `CURRENCY` | string |  |  | `CURRENCY` |
| `ITEM_WITHHOLDING_TAX_GROUP_CODE` | string |  |  | `ITEM_WITHHOLDING_TAX_GROUP_CODE` |
| `OFFSET_ACCOUNT_TYPE` | string |  |  | `OFFSET_ACCOUNT_TYPE` |
| `INVOICE_DATE` | string |  |  | `INVOICE_DATE` |
| `BANK_ACCOUNT_ID` | string |  |  | `BANK_ACCOUNT_ID` |
| `REMITTANCE_ADDRESS_COUNTRY_ISO_CODE` | string |  |  | `REMITTANCE_ADDRESS_COUNTRY_ISO_CODE` |
| `CASH_DISCOUNT_DATE` | string |  |  | `CASH_DISCOUNT_DATE` |
| `DEBIT` | string |  |  | `DEBIT` |
| `IMPORTED_SALES_TAX` | string |  |  | `IMPORTED_SALES_TAX` |
| `OFFSET_COMPANY` | string |  |  | `OFFSET_COMPANY` |
| `TAX_GROUP_BR` | string |  |  | `TAX_GROUP_BR` |
| `DUE_DATE` | string |  |  | `DUE_DATE` |
| `OVERRIDE_SALES_TAX` | string |  |  | `OVERRIDE_SALES_TAX` |
| `REMITTANCE_ADDRESS_TIME_ZONE` | string |  |  | `REMITTANCE_ADDRESS_TIME_ZONE` |
| `REMITTANCE_ADDRESS_DESCRIPTION` | string |  |  | `REMITTANCE_ADDRESS_DESCRIPTION` |
| `CREDIT` | string |  |  | `CREDIT` |
| `GST_HST_TAX_TYPE` | string |  |  | `GST_HST_TAX_TYPE` |
| `ASSET_TRANS_TYPE` | string |  |  | `ASSET_TRANS_TYPE` |
| `TAX_ITEM_GROUP_BR` | string |  |  | `TAX_ITEM_GROUP_BR` |
| `COMPANY` | string |  |  | `COMPANY` |
| `REMITTANCE_ADDRESS_VALID_FROM` | string |  |  | `REMITTANCE_ADDRESS_VALID_FROM` |
| `CUST_VEND_BANK_ACCOUNT_ID` | string |  |  | `CUST_VEND_BANK_ACCOUNT_ID` |
| `IS_WITHHOLDING_TAX_CALCULATE` | string |  |  | `IS_WITHHOLDING_TAX_CALCULATE` |
| `REMITTANCE_ADDRESS_VALID_TO` | string |  |  | `REMITTANCE_ADDRESS_VALID_TO` |
| `OFFSET_ACCOUNT_DISPLAY_VALUE` | string |  |  | `OFFSET_ACCOUNT_DISPLAY_VALUE` |
| `SALES_TAX_GROUP` | string |  |  | `SALES_TAX_GROUP` |
| `DEFAULT_DIMENSION_DISPLAY_VALUE` | string |  |  | `DEFAULT_DIMENSION_DISPLAY_VALUE` |
| `REMITTANCE_ADDRESS_LATITUDE` | string |  |  | `REMITTANCE_ADDRESS_LATITUDE` |
| `SALES_TAX_CODE` | string |  |  | `SALES_TAX_CODE` |
| `FULL_PRIMARY_REMITTANCE_ADDRESS` | string |  |  | `FULL_PRIMARY_REMITTANCE_ADDRESS` |
| `ITEM_SALES_TAX_GROUP` | string |  |  | `ITEM_SALES_TAX_GROUP` |
| `REMITTANCE_ADDRESS_COUNTRY` | string |  |  | `REMITTANCE_ADDRESS_COUNTRY` |
| `FIN_TAG_DISPLAY_VALUE` | string |  |  | `FIN_TAG_DISPLAY_VALUE` |
| `OFFSET_TRANSACTION_TEXT` | string |  |  | `OFFSET_TRANSACTION_TEXT` |
| `TYPE_OF_OPERATION` | string |  |  | `TYPE_OF_OPERATION` |
| `BOOK_ID` | string |  |  | `BOOK_ID` |
| `PAYMENT_SPECIFICATION` | string |  |  | `PAYMENT_SPECIFICATION` |
| `REMITTANCE_ADDRESS_LONGITUDE` | string |  |  | `REMITTANCE_ADDRESS_LONGITUDE` |
| `ITM_COST_TYPE_ID` | string |  |  | `ITM_COST_TYPE_ID` |
| `ITM_COST_AREA` | string |  |  | `ITM_COST_AREA` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**LINE_NUMBER**
- `1`
- `USA`
- `None`
- `NJ 07058`

**INVOICE_DECLARATION_ID**
- `None`

**CASH_DISCOUNT_AMOUNT**
- `0`
- `Blank`
- `None`

**UUID**
- `None`

**OFFSET_FIN_TAG_DISPLAY_VALUE**
- `None`

**POSTING_PROFILE**
- `GEN`
- `0`
- `None`

**LIST_CODE**
- `None`
- `IncludeNot`

**OFFSET_DEFAULT_DIMENSION_DISPLAY_VALUE**
- `None`
- `Shipment`

**REPORTING_CURRENCY_EXCH_RATE**
- `None`
- `100`

**PAYMENT_ID**
- `None`

**ACCOUNT_TYPE**
- `None`
- `Vend`

**TERMS_OF_PAYMENT**
- `None`
- `N10`

**REMITTANCE_ADDRESS_STREET**
- `None`

**REMITTANCE_ADDRESS_DISTRICT_NAME**
- `None`

**EXCHANGE_RATE_SECOND**
- `None`
- `0`

**TRANSACTION_TYPE**
- `None`
- `Vend`

**CHINESE_VOUCHER**
- `None`

**TAX_1099_FIELDS**
- `None`
- `0`

**METHOD_OF_PAYMENT**
- `None`

**CHINESE_VOUCHER_TYPE**
- `None`

**ASSET_ID**
- `None`

**REMITTANCE_ADDRESS_CITY**
- `None`

**EXCHANGE_RATE**
- `None`
- `100`

**DOCUMENT**
- `None`

**DESCRIPTION**
- `None`

**REMITTANCE_ADDRESS_STATE**
- `None`
- `CA`

**REMITTANCE_ADDRESS_ZIP_CODE**
- `None`

**DELIVERY_DATE**
- `None`
- `1900-01-01 12:00:00.0000000 +00:00`

**OVERRIDE_SALES_TAX_BR**
- `None`
- `No`

**REMITTANCE_ADDRESS_COUNTY**
- `None`

**REMITTANCE_ADDRESS_LOCATION_ID**
- `None`
- `7502`

**APPROVED**
- `None`
- `Yes`

**CASH_DISCOUNT**
- `None`

**TAX_EXEMPT_NUMBER**
- `None`

**CURRENCY**
- `None`
- `USD`

**ITEM_WITHHOLDING_TAX_GROUP_CODE**
- `None`

**OFFSET_ACCOUNT_TYPE**
- `None`
- `Ledger`

**BANK_ACCOUNT_ID**
- `None`

**REMITTANCE_ADDRESS_COUNTRY_ISO_CODE**
- `None`
- `US`

**CASH_DISCOUNT_DATE**
- `None`
- `1900-01-01 12:00:00.0000000 +00:00`

**DEBIT**
- `None`
- `0`

**IMPORTED_SALES_TAX**
- `None`
- `0`

**TAX_GROUP_BR**
- `None`

**OVERRIDE_SALES_TAX**
- `None`
- `No`

**REMITTANCE_ADDRESS_TIME_ZONE**
- `None`

**REMITTANCE_ADDRESS_DESCRIPTION**
- `None`
- `ShieldPro Claims Agency`

**GST_HST_TAX_TYPE**
- `None`

**ASSET_TRANS_TYPE**
- `None`

**TAX_ITEM_GROUP_BR**
- `None`

**REMITTANCE_ADDRESS_VALID_FROM**
- `None`
- `1900-01-01 00:00:00.0000000 +00:00`
- `2026-10-15 15:52:58.0000000 +00:00`

**CUST_VEND_BANK_ACCOUNT_ID**
- `None`

**IS_WITHHOLDING_TAX_CALCULATE**
- `None`
- `No`

**REMITTANCE_ADDRESS_VALID_TO**
- `None`
- `1900-01-01 00:00:00.0000000 +00:00`
- `2154-12-31 23:59:59.0000000 +00:00`

**OFFSET_ACCOUNT_DISPLAY_VALUE**
- `None`
- `551310---------`
- `552310---------`
- `552200---------`
- `552320---------`
- `551600---------`
- `551420---------`
- `551320---------`
- `551500---------`
- `551430---------`
- `551440---------`
- `551450---------`
- `552100---------`
- `551410---------`
- `555530---------`
- `555610---------`
- `555700---------`
- `555620---------`
- `555800---------`
- `552410---------`
- `555600---------`
- `555611---------`

**SALES_TAX_GROUP**
- `None`

**DEFAULT_DIMENSION_DISPLAY_VALUE**
- `None`
- `---------`

**REMITTANCE_ADDRESS_LATITUDE**
- `None`
- `0`

**SALES_TAX_CODE**
- `None`

**FULL_PRIMARY_REMITTANCE_ADDRESS**
- `None`
- `CA`

**ITEM_SALES_TAX_GROUP**
- `None`

**REMITTANCE_ADDRESS_COUNTRY**
- `None`

**FIN_TAG_DISPLAY_VALUE**
- `None`

**OFFSET_TRANSACTION_TEXT**
- `None`

**TYPE_OF_OPERATION**
- `None`
- `Blank`

**BOOK_ID**
- `None`

**PAYMENT_SPECIFICATION**
- `None`

**REMITTANCE_ADDRESS_LONGITUDE**
- `None`
- `0`

**ITM_COST_TYPE_ID**
- `None`

**ITM_COST_AREA**
- `None`
- `Shipment`

**SOURCE_FILE_NAME**
- `vendinvoicejournallines__20261116_105417.csv`

**MDP_CREATED_DATE**
- `2026-11-16 11:42:04.854621+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 11:42:04.854621+00:00`

## Empty columns

Empty in every row: `INVOICE_DECLARATION_ID`, `UUID`, `OFFSET_FIN_TAG_DISPLAY_VALUE`, `PAYMENT_ID`, `REMITTANCE_ADDRESS_STREET`, `REMITTANCE_ADDRESS_DISTRICT_NAME`, `CHINESE_VOUCHER`, `METHOD_OF_PAYMENT`, `CHINESE_VOUCHER_TYPE`, `ASSET_ID`, `REMITTANCE_ADDRESS_CITY`, `DOCUMENT`, `DESCRIPTION`, `REMITTANCE_ADDRESS_ZIP_CODE`, `REMITTANCE_ADDRESS_COUNTY`, `CASH_DISCOUNT`, `TAX_EXEMPT_NUMBER`, `ITEM_WITHHOLDING_TAX_GROUP_CODE`, `BANK_ACCOUNT_ID`, `TAX_GROUP_BR`, `REMITTANCE_ADDRESS_TIME_ZONE`, `TAX_ITEM_GROUP_BR`, `CUST_VEND_BANK_ACCOUNT_ID`, `SALES_TAX_GROUP`, `SALES_TAX_CODE`, `ITEM_SALES_TAX_GROUP`, `REMITTANCE_ADDRESS_COUNTRY`, `FIN_TAG_DISPLAY_VALUE`, `OFFSET_TRANSACTION_TEXT`, `BOOK_ID`, `PAYMENT_SPECIFICATION`, `ITM_COST_TYPE_ID`. Do not filter or group on them.
