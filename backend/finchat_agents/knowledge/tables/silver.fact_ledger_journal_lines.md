---
name: fact_ledger_journal_lines
schema: silver
layer: silver
domain: gl
type: table
status: active
purpose: Lines of D365 ledger journals.
grain: one row per DATA_AREA_ID + JOURNAL_BATCH_NUMBER + LINE_NUMBER (one journal line)
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
  note: ITEM_SALES_TAX_GROUP all null; CASH_DISCOUNT_DATE and REVERSE_DATE are the 1900-01-01 placeholder in all rows
proposed_fields: []
reviewed: false
---

# fact_ledger_journal_lines

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `DATA_AREA_ID` | string |  |  | `DATA_AREA_ID` |
| `JOURNAL_BATCH_NUMBER` | string |  |  | `JOURNAL_BATCH_NUMBER` |
| `LINE_NUMBER` | string |  |  | `LINE_NUMBER` |
| `REVERSE_ENTRY` | string |  |  | `REVERSE_ENTRY` |
| `ITEM_SALES_TAX_GROUP` | string |  |  | `ITEM_SALES_TAX_GROUP` |
| `CASH_DISCOUNT_DATE` | string |  |  | `CASH_DISCOUNT_DATE` |
| `VOUCHER` | string |  |  | `VOUCHER` |
| `TEXT` | string |  |  | `TEXT` |
| `OFFSET_ACCOUNT_TYPE` | string |  |  | `OFFSET_ACCOUNT_TYPE` |
| `IS_WITHHOLDING_CALCULATION_ENABLED` | string |  |  | `IS_WITHHOLDING_CALCULATION_ENABLED` |
| `REVERSE_DATE` | string |  |  | `REVERSE_DATE` |
| `TRANS_DATE` | string |  |  | `TRANS_DATE` |
| `DEFAULT_DIMENSION_DISPLAY_VALUE` | string |  |  | `DEFAULT_DIMENSION_DISPLAY_VALUE` |
| `PAYMENT_REFERENCE` | string |  |  | `PAYMENT_REFERENCE` |
| `DOCUMENT` | string |  |  | `DOCUMENT` |
| `CASH_DISCOUNT_AMOUNT` | string |  |  | `CASH_DISCOUNT_AMOUNT` |
| `EXCHANGE_RATE` | string |  |  | `EXCHANGE_RATE` |
| `CHINESE_VOUCHER_TYPE` | string |  |  | `CHINESE_VOUCHER_TYPE` |
| `DEBIT_AMOUNT` | string |  |  | `DEBIT_AMOUNT` |
| `SALES_TAX_CODE` | string |  |  | `SALES_TAX_CODE` |
| `DOCUMENT_DATE` | string |  |  | `DOCUMENT_DATE` |
| `OFFSET_ACCOUNT_DISPLAY_VALUE` | string |  |  | `OFFSET_ACCOUNT_DISPLAY_VALUE` |
| `ACCOUNT_DISPLAY_VALUE` | string |  |  | `ACCOUNT_DISPLAY_VALUE` |
| `CASH_DISCOUNT` | string |  |  | `CASH_DISCOUNT` |
| `OFFSET_DEFAULT_DIMENSION_DISPLAY_VALUE` | string |  |  | `OFFSET_DEFAULT_DIMENSION_DISPLAY_VALUE` |
| `OFFSET_FIN_TAG_DISPLAY_VALUE` | string |  |  | `OFFSET_FIN_TAG_DISPLAY_VALUE` |
| `SALES_TAX_GROUP` | string |  |  | `SALES_TAX_GROUP` |
| `ACCOUNT_TYPE` | string |  |  | `ACCOUNT_TYPE` |
| `INVOICE` | string |  |  | `INVOICE` |
| `DUE_DATE` | string |  |  | `DUE_DATE` |
| `REPORTING_CURRENCY_EXCH_RATE` | string |  |  | `REPORTING_CURRENCY_EXCH_RATE` |
| `FIN_TAG_DISPLAY_VALUE` | string |  |  | `FIN_TAG_DISPLAY_VALUE` |
| `PAYMENT_METHOD` | string |  |  | `PAYMENT_METHOD` |
| `PAYMENT_ID` | string |  |  | `PAYMENT_ID` |
| `POSTING_PROFILE` | string |  |  | `POSTING_PROFILE` |
| `EXCHANGE_RATE_SECOND` | string |  |  | `EXCHANGE_RATE_SECOND` |
| `CREDIT_AMOUNT` | string |  |  | `CREDIT_AMOUNT` |
| `OVERRIDE_SALES_TAX` | string |  |  | `OVERRIDE_SALES_TAX` |
| `OFFSET_COMPANY` | string |  |  | `OFFSET_COMPANY` |
| `QUANTITY` | string |  |  | `QUANTITY` |
| `ITEM_WITHHOLDING_TAX_GROUP_CODE` | string |  |  | `ITEM_WITHHOLDING_TAX_GROUP_CODE` |
| `TAX_EXEMPT_NUMBER` | string |  |  | `TAX_EXEMPT_NUMBER` |
| `REPORTING_CURRENCY_EXCH_RATE_SECONDARY` | string |  |  | `REPORTING_CURRENCY_EXCH_RATE_SECONDARY` |
| `CURRENCY_CODE` | string |  |  | `CURRENCY_CODE` |
| `COMPANY` | string |  |  | `COMPANY` |
| `CHINESE_VOUCHER` | string |  |  | `CHINESE_VOUCHER` |
| `DISCOUNT_PERCENTAGE` | string |  |  | `DISCOUNT_PERCENTAGE` |
| `OFFSET_TEXT` | string |  |  | `OFFSET_TEXT` |
| `KPMG_DELIVERY_CODE` | string |  |  | `KPMG_DELIVERY_CODE` |
| `KPMG_CUSTOMER_ACCOUNT_NUMBER` | string |  |  | `KPMG_CUSTOMER_ACCOUNT_NUMBER` |
| `SHIFT_ID` | string |  |  | `SHIFT_ID` |
| `WITHHOLDING_SET_ID` | string |  |  | `WITHHOLDING_SET_ID` |
| `LTM_DOCUMENT_DATE` | string |  |  | `LTM_DOCUMENT_DATE` |
| `LEDGER_JOURNAL_TYPE` | string |  |  | `LEDGER_JOURNAL_TYPE` |
| `CAICAE_DUE_DATE` | string |  |  | `CAICAE_DUE_DATE` |
| `LEDGER_JOURNAL_TRANS_ID` | string |  |  | `LEDGER_JOURNAL_TRANS_ID` |
| `SALES_POINT_PREFIX` | string |  |  | `SALES_POINT_PREFIX` |
| `COUNTRY_REGION_ID` | string |  |  | `COUNTRY_REGION_ID` |
| `WITHHOLD_ACCRUED_BASE_MST` | string |  |  | `WITHHOLD_ACCRUED_BASE_MST` |
| `STATE_DOC_NUM` | string |  |  | `STATE_DOC_NUM` |
| `LIST_FIELD_CODE_10` | string |  |  | `LIST_FIELD_CODE_10` |
| `TAX_PAYER_TYPE_ID` | string |  |  | `TAX_PAYER_TYPE_ID` |
| `BUSSINESS_NAME` | string |  |  | `BUSSINESS_NAME` |
| `CPD_CUST_POSTING_PROFILE` | string |  |  | `CPD_CUST_POSTING_PROFILE` |
| `AMOUNT_CUR` | string |  |  | `AMOUNT_CUR` |
| `WITHHOLDING_EFFECTIVE_RATE` | string |  |  | `WITHHOLDING_EFFECTIVE_RATE` |
| `TREASURY_ENTER` | string |  |  | `TREASURY_ENTER` |
| `DOCUMENT_NUM` | string |  |  | `DOCUMENT_NUM` |
| `CPD_ACTION` | string |  |  | `CPD_ACTION` |
| `COMPLETE_DOCUMENT_NUM` | string |  |  | `COMPLETE_DOCUMENT_NUM` |
| `COUNTRY_DOC_TYPE_ID` | string |  |  | `COUNTRY_DOC_TYPE_ID` |
| `EXCHANGE_RATE_TYPE_ALT` | string |  |  | `EXCHANGE_RATE_TYPE_ALT` |
| `CONTROL_CODE` | string |  |  | `CONTROL_CODE` |
| `CONCEPT_1` | string |  |  | `CONCEPT_1` |
| `CONCEPT_3` | string |  |  | `CONCEPT_3` |
| `IS_COLLECT_PAYM_DOC` | string |  |  | `IS_COLLECT_PAYM_DOC` |
| `CONCEPT_2` | string |  |  | `CONCEPT_2` |
| `LIST_FIELD_10` | string |  |  | `LIST_FIELD_10` |
| `WITHHOLDING_BASE_MST` | string |  |  | `WITHHOLDING_BASE_MST` |
| `CPD_TRX_HISTORY_ID` | string |  |  | `CPD_TRX_HISTORY_ID` |
| `BANK_ACCOUNT_NUM` | string |  |  | `BANK_ACCOUNT_NUM` |
| `HOLDER_ACCOUNT_NUM` | string |  |  | `HOLDER_ACCOUNT_NUM` |
| `COUNTRY_DOC_NUM` | string |  |  | `COUNTRY_DOC_NUM` |
| `WITHHOLD_ACCRUED_AMOUNT_MST` | string |  |  | `WITHHOLD_ACCRUED_AMOUNT_MST` |
| `AMOUNT_MST` | string |  |  | `AMOUNT_MST` |
| `LINE_NUM` | string |  |  | `LINE_NUM` |
| `BENEFICIARY` | string |  |  | `BENEFICIARY` |
| `SALES_POINT_ID` | string |  |  | `SALES_POINT_ID` |
| `STATE_ID` | string |  |  | `STATE_ID` |
| `STATE_DOC_TYPE_ID` | string |  |  | `STATE_DOC_TYPE_ID` |
| `BANK_GROUP_ID` | string |  |  | `BANK_GROUP_ID` |
| `DOCUMENT_CLASSIFICATION_ID` | string |  |  | `DOCUMENT_CLASSIFICATION_ID` |
| `CPD_SOURCE` | string |  |  | `CPD_SOURCE` |
| `ACCOUNT_NUM` | string |  |  | `ACCOUNT_NUM` |
| `PAYMENT_TERM_ID` | string |  |  | `PAYMENT_TERM_ID` |
| `TREASURY_ACTUAL` | string |  |  | `TREASURY_ACTUAL` |
| `CAICAE` | string |  |  | `CAICAE` |
| `CPD_TRX_OPEN_ID` | string |  |  | `CPD_TRX_OPEN_ID` |
| `IS_CONCEPT` | string |  |  | `IS_CONCEPT` |
| `LIST_FIELD_CODE_08` | string |  |  | `LIST_FIELD_CODE_08` |
| `LIST_FIELD_CODE_09` | string |  |  | `LIST_FIELD_CODE_09` |
| `JOURNAL_NUM` | string |  |  | `JOURNAL_NUM` |
| `LIST_FIELD_CODE_01` | string |  |  | `LIST_FIELD_CODE_01` |
| `LIST_FIELD_CODE_02` | string |  |  | `LIST_FIELD_CODE_02` |
| `LIST_FIELD_05` | string |  |  | `LIST_FIELD_05` |
| `LIST_FIELD_CODE_03` | string |  |  | `LIST_FIELD_CODE_03` |
| `LIST_FIELD_04` | string |  |  | `LIST_FIELD_04` |
| `LIST_FIELD_CODE_04` | string |  |  | `LIST_FIELD_CODE_04` |
| `LIST_FIELD_07` | string |  |  | `LIST_FIELD_07` |
| `LIST_FIELD_CODE_05` | string |  |  | `LIST_FIELD_CODE_05` |
| `LIST_FIELD_06` | string |  |  | `LIST_FIELD_06` |
| `LIST_FIELD_CODE_06` | string |  |  | `LIST_FIELD_CODE_06` |
| `LIST_FIELD_01` | string |  |  | `LIST_FIELD_01` |
| `LIST_FIELD_CODE_07` | string |  |  | `LIST_FIELD_CODE_07` |
| `LIST_FIELD_03` | string |  |  | `LIST_FIELD_03` |
| `LIST_FIELD_02` | string |  |  | `LIST_FIELD_02` |
| `BANK_CHEQUE_NUM` | string |  |  | `BANK_CHEQUE_NUM` |
| `LIST_FIELD_09` | string |  |  | `LIST_FIELD_09` |
| `LIST_FIELD_08` | string |  |  | `LIST_FIELD_08` |
| `DUE_DATE_AW` | string |  |  | `DUE_DATE_AW` |
| `PRESERVE_NUM` | string |  |  | `PRESERVE_NUM` |
| `ORIG_EXCHANGE_RATE` | string |  |  | `ORIG_EXCHANGE_RATE` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**REVERSE_ENTRY**
- `No`

**ITEM_SALES_TAX_GROUP**
- `None`

**CASH_DISCOUNT_DATE**
- `1900-01-01 12:00:00.0000000 +00:00`

**OFFSET_ACCOUNT_TYPE**
- `Ledger`
- `Bank`
- `Vend`

**IS_WITHHOLDING_CALCULATION_ENABLED**
- `No`

**REVERSE_DATE**
- `1900-01-01 12:00:00.0000000 +00:00`

**DEFAULT_DIMENSION_DISPLAY_VALUE**
- `None`
- `---------`

**PAYMENT_REFERENCE**
- `None`

**DOCUMENT**
- `None`

**CASH_DISCOUNT_AMOUNT**
- `0`

**EXCHANGE_RATE**
- `100`
- `75.48309178744`
- `88.347027122537`
- `85.448175681449`
- `52.985746834102`
- `53.126494182649`
- `8.814300320841`
- `52.44663554833`
- `116.84`
- `1.847783306756`
- `7.533694448421`
- `4.593857094294`
- `117.03`

**CHINESE_VOUCHER_TYPE**
- `None`

**SALES_TAX_CODE**
- `None`

**CASH_DISCOUNT**
- `None`

**OFFSET_DEFAULT_DIMENSION_DISPLAY_VALUE**
- `None`
- `---------`

**OFFSET_FIN_TAG_DISPLAY_VALUE**
- `None`
- `Concur`

**SALES_TAX_GROUP**
- `None`

**ACCOUNT_TYPE**
- `Ledger`
- `FixedAssets`
- `Vend`
- `Cust`

**REPORTING_CURRENCY_EXCH_RATE**
- `100`
- `75.48309178744`
- `132.48`
- `85.448175681449`
- `52.985746834102`
- `70.190215483962`
- `53.126494182649`
- `85.587127695995`
- `113.19`
- `0`
- `52.44663554833`
- `85.4481756814492`
- `113.9`
- `7.533694448421`
- `7.686217842786`
- `69.48`
- `6.084390496182`
- `7.82962730974`
- `4.593857094294`
- `9.97695323802`

**FIN_TAG_DISPLAY_VALUE**
- `MANUAL`
- `CLAIMS_ADMIN`
- `None`
- `POLICY_ADMIN`
- `CONCUR`
- `PAYROLL`
- `CEDED`
- `ACTUARIAL`
- `AP`
- `TREASURY`
- `INVESTMENT`
- `Novedia`
- `Concur`
- `MANUAL|||||||||||`
- `Novidea`
- `ACTUARIAL|||||||||||`
- `CLAIMS_ADMIN|||||||||||`
- `NVS`
- `POLICY_ADMIN|||||||||||`
- `NVS|||||||||||`

**PAYMENT_METHOD**
- `None`

**PAYMENT_ID**
- `None`

**POSTING_PROFILE**
- `None`
- `FAPP`
- `GEN`

**EXCHANGE_RATE_SECOND**
- `0`

**OVERRIDE_SALES_TAX**
- `No`

**QUANTITY**
- `0`

**ITEM_WITHHOLDING_TAX_GROUP_CODE**
- `None`

**TAX_EXEMPT_NUMBER**
- `None`

**REPORTING_CURRENCY_EXCH_RATE_SECONDARY**
- `0`

**CURRENCY_CODE**
- `USD`
- `GBP`
- `EUR`
- `CAD`
- `SEK`
- `AUD`
- `ZAR`
- `NOK`

**CHINESE_VOUCHER**
- `None`

**DISCOUNT_PERCENTAGE**
- `0`

**OFFSET_TEXT**
- `None`

**KPMG_DELIVERY_CODE**
- `None`

**KPMG_CUSTOMER_ACCOUNT_NUMBER**
- `None`

**SHIFT_ID**
- `None`

**WITHHOLDING_SET_ID**
- `None`

**LTM_DOCUMENT_DATE**
- `1900-01-01 12:00:00.0000000 +00:00`

**LEDGER_JOURNAL_TYPE**
- `Ledger`

**CAICAE_DUE_DATE**
- `1900-01-01 12:00:00.0000000 +00:00`

**LEDGER_JOURNAL_TRANS_ID**
- `0`

**SALES_POINT_PREFIX**
- `None`

**COUNTRY_REGION_ID**
- `None`

**WITHHOLD_ACCRUED_BASE_MST**
- `0`

**STATE_DOC_NUM**
- `None`

**LIST_FIELD_CODE_10**
- `None`

**TAX_PAYER_TYPE_ID**
- `None`

**BUSSINESS_NAME**
- `None`

**CPD_CUST_POSTING_PROFILE**
- `None`

**AMOUNT_CUR**
- `0`

**WITHHOLDING_EFFECTIVE_RATE**
- `0`

**TREASURY_ENTER**
- `None`

**DOCUMENT_NUM**
- `None`

**CPD_ACTION**
- `Entry`

**COMPLETE_DOCUMENT_NUM**
- `None`

**COUNTRY_DOC_TYPE_ID**
- `None`

**EXCHANGE_RATE_TYPE_ALT**
- `0`

**CONTROL_CODE**
- `None`

**CONCEPT_1**
- `None`

**CONCEPT_3**
- `None`

**IS_COLLECT_PAYM_DOC**
- `No`

**CONCEPT_2**
- `None`

**LIST_FIELD_10**
- `None`

**WITHHOLDING_BASE_MST**
- `0`

**CPD_TRX_HISTORY_ID**
- `0`

**BANK_ACCOUNT_NUM**
- `None`

**HOLDER_ACCOUNT_NUM**
- `None`

**COUNTRY_DOC_NUM**
- `None`

**WITHHOLD_ACCRUED_AMOUNT_MST**
- `0`

**AMOUNT_MST**
- `0`

**LINE_NUM**
- `0`

**BENEFICIARY**
- `None`

**SALES_POINT_ID**
- `None`

**STATE_ID**
- `None`

**STATE_DOC_TYPE_ID**
- `None`

**BANK_GROUP_ID**
- `None`

**DOCUMENT_CLASSIFICATION_ID**
- `None`

**CPD_SOURCE**
- `Own`

**ACCOUNT_NUM**
- `None`

**PAYMENT_TERM_ID**
- `None`

**TREASURY_ACTUAL**
- `None`

**CAICAE**
- `None`

**CPD_TRX_OPEN_ID**
- `0`

**IS_CONCEPT**
- `No`

**LIST_FIELD_CODE_08**
- `None`

**LIST_FIELD_CODE_09**
- `None`

**JOURNAL_NUM**
- `None`

**LIST_FIELD_CODE_01**
- `None`

**LIST_FIELD_CODE_02**
- `None`

**LIST_FIELD_05**
- `None`

**LIST_FIELD_CODE_03**
- `None`

**LIST_FIELD_04**
- `None`

**LIST_FIELD_CODE_04**
- `None`

**LIST_FIELD_07**
- `None`

**LIST_FIELD_CODE_05**
- `None`

**LIST_FIELD_06**
- `None`

**LIST_FIELD_CODE_06**
- `None`

**LIST_FIELD_01**
- `None`

**LIST_FIELD_CODE_07**
- `None`

**LIST_FIELD_03**
- `None`

**LIST_FIELD_02**
- `None`

**BANK_CHEQUE_NUM**
- `None`

**LIST_FIELD_09**
- `None`

**LIST_FIELD_08**
- `None`

**DUE_DATE_AW**
- `1900-01-01 12:00:00.0000000 +00:00`

**PRESERVE_NUM**
- `No`

**ORIG_EXCHANGE_RATE**
- `0`

**SOURCE_FILE_NAME**
- `ledgerjournallines__20261116_105417.csv`

**MDP_CREATED_DATE**
- `2026-11-16 11:41:50.326198+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 11:41:50.326198+00:00`

## Empty columns

Empty in every row: `ITEM_SALES_TAX_GROUP`, `PAYMENT_REFERENCE`, `DOCUMENT`, `CHINESE_VOUCHER_TYPE`, `SALES_TAX_CODE`, `CASH_DISCOUNT`, `SALES_TAX_GROUP`, `PAYMENT_METHOD`, `PAYMENT_ID`, `ITEM_WITHHOLDING_TAX_GROUP_CODE`, `TAX_EXEMPT_NUMBER`, `CHINESE_VOUCHER`, `OFFSET_TEXT`, `KPMG_DELIVERY_CODE`, `KPMG_CUSTOMER_ACCOUNT_NUMBER`, `SHIFT_ID`, `WITHHOLDING_SET_ID`, `SALES_POINT_PREFIX`, `COUNTRY_REGION_ID`, `STATE_DOC_NUM`, `LIST_FIELD_CODE_10`, `TAX_PAYER_TYPE_ID`, `BUSSINESS_NAME`, `CPD_CUST_POSTING_PROFILE`, `TREASURY_ENTER`, `DOCUMENT_NUM`, `COMPLETE_DOCUMENT_NUM`, `COUNTRY_DOC_TYPE_ID`, `CONTROL_CODE`, `CONCEPT_1`, `CONCEPT_3`, `CONCEPT_2`, `LIST_FIELD_10`, `BANK_ACCOUNT_NUM`, `HOLDER_ACCOUNT_NUM`, `COUNTRY_DOC_NUM`, `BENEFICIARY`, `SALES_POINT_ID`, `STATE_ID`, `STATE_DOC_TYPE_ID`, `BANK_GROUP_ID`, `DOCUMENT_CLASSIFICATION_ID`, `ACCOUNT_NUM`, `PAYMENT_TERM_ID`, `TREASURY_ACTUAL`, `CAICAE`, `LIST_FIELD_CODE_08`, `LIST_FIELD_CODE_09`, `JOURNAL_NUM`, `LIST_FIELD_CODE_01`, `LIST_FIELD_CODE_02`, `LIST_FIELD_05`, `LIST_FIELD_CODE_03`, `LIST_FIELD_04`, `LIST_FIELD_CODE_04`, `LIST_FIELD_07`, `LIST_FIELD_CODE_05`, `LIST_FIELD_06`, `LIST_FIELD_CODE_06`, `LIST_FIELD_01`, `LIST_FIELD_CODE_07`, `LIST_FIELD_03`, `LIST_FIELD_02`, `BANK_CHEQUE_NUM`, `LIST_FIELD_09`, `LIST_FIELD_08`. Do not filter or group on them.
