---
name: fact_ledger_journal_table_bi_entities
schema: silver
layer: silver
domain: gl
type: table
status: active
purpose: Ledger journal table extract (posting results; journal numbers).
grain: one row per journal (key unknown)
primary_key: []
entity_column: DATA_AREA_ID
period_columns: []
pii_columns:
- REJECTED_BY
- SYS_CREATED_BY
- APPROVER
- SYS_MODIFIED_BY
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues:
- code: duplicates
  note: 92 exact duplicate rows in the latest export (20.0%). Check duplicates at the grain before counting or summing; warn
    the user.
proposed_fields: []
reviewed: false
---

# fact_ledger_journal_table_bi_entities

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `DATA_AREA_ID` | string |  |  | `DATA_AREA_ID` |
| `JOURNAL_NUM` | string |  |  | `JOURNAL_NUM` |
| `REV_REC_REALLOCATION_ID` | string |  |  | `REV_REC_REALLOCATION_ID` |
| `REVERSE_ENTRY` | string |  |  | `REVERSE_ENTRY` |
| `POSTED_DATE_TIME` | string |  |  | `POSTED_DATE_TIME` |
| `SIMULATION_POSTED_IT` | string |  |  | `SIMULATION_POSTED_IT` |
| `JOURNAL_NAME` | string |  |  | `JOURNAL_NAME` |
| `OFFSET_ACCOUNT_TYPE` | string |  |  | `OFFSET_ACCOUNT_TYPE` |
| `BANK_REMITTANCE_TYPE` | string |  |  | `BANK_REMITTANCE_TYPE` |
| `REVERSE_DATE` | string |  |  | `REVERSE_DATE` |
| `RETAIL_STATEMENT_ID` | string |  |  | `RETAIL_STATEMENT_ID` |
| `JOURNAL_TYPE` | string |  |  | `JOURNAL_TYPE` |
| `JOURNAL_BALANCE` | string |  |  | `JOURNAL_BALANCE` |
| `VOUCHER_ALLOCATED_AT_POSTING` | string |  |  | `VOUCHER_ALLOCATED_AT_POSTING` |
| `EURO_TRIANGULATION` | string |  |  | `EURO_TRIANGULATION` |
| `FIN_TAG` | string |  |  | `FIN_TAG` |
| `IS_LEDGER_DIMENSION_NAME_UPDATED` | string |  |  | `IS_LEDGER_DIMENSION_NAME_UPDATED` |
| `CUST_VEND_NEG_INST_PROTEST_PROCESS` | string |  |  | `CUST_VEND_NEG_INST_PROTEST_PROCESS` |
| `REPORTING_CURRENCY_FIXED_EXCH_RATE` | string |  |  | `REPORTING_CURRENCY_FIXED_EXCH_RATE` |
| `IN_USE_BY` | string |  |  | `IN_USE_BY` |
| `OFFSET_LEDGER_DIMENSION` | string |  |  | `OFFSET_LEDGER_DIMENSION` |
| `REJECTED_BY` | string |  |  | `REJECTED_BY` |
| `ASSET_TRANSFER_TYPE_LT` | string |  |  | `ASSET_TRANSFER_TYPE_LT` |
| `EXCH_RATE` | string |  |  | `EXCH_RATE` |
| `REPORTED_AS_READY_BY` | string |  |  | `REPORTED_AS_READY_BY` |
| `POSTED` | string |  |  | `POSTED` |
| `SESSION_LOGIN_DATE_TIME` | string |  |  | `SESSION_LOGIN_DATE_TIME` |
| `SYS_CREATED_BY` | string |  |  | `SYS_CREATED_BY` |
| `DEFAULT_DIMENSION` | string |  |  | `DEFAULT_DIMENSION` |
| `JOURNAL_TOTAL_DEBIT` | string |  |  | `JOURNAL_TOTAL_DEBIT` |
| `PARENT_JOURNAL_NUM` | string |  |  | `PARENT_JOURNAL_NUM` |
| `NUMBER_SEQUENCE_TABLE` | string |  |  | `NUMBER_SEQUENCE_TABLE` |
| `JOURNAL_TOTAL_OFFSET_BALANCE` | string |  |  | `JOURNAL_TOTAL_OFFSET_BALANCE` |
| `BANK_TRANS_SUMMARIZATION_ENABLED` | string |  |  | `BANK_TRANS_SUMMARIZATION_ENABLED` |
| `PROTEST_SETTLED_BILL` | string |  |  | `PROTEST_SETTLED_BILL` |
| `REMOVE_LINE_AFTER_POSTING` | string |  |  | `REMOVE_LINE_AFTER_POSTING` |
| `DOCUMENT_NUM` | string |  |  | `DOCUMENT_NUM` |
| `LEDGER_JOURNAL_INCL_TAX` | string |  |  | `LEDGER_JOURNAL_INCL_TAX` |
| `ASSET_LEASE_PROCESS_ID` | string |  |  | `ASSET_LEASE_PROCESS_ID` |
| `ORIGINAL_COMPANY` | string |  |  | `ORIGINAL_COMPANY` |
| `APPROVER` | string |  |  | `APPROVER` |
| `WORKFLOW_APPROVAL_STATUS` | string |  |  | `WORKFLOW_APPROVAL_STATUS` |
| `NAME` | string |  |  | `NAME` |
| `BANK_TRANS_SUMMARIZATION_CRITERIA` | string |  |  | `BANK_TRANS_SUMMARIZATION_CRITERIA` |
| `REPORTING_CURRENCY_EXCH_RATE` | string |  |  | `REPORTING_CURRENCY_EXCH_RATE` |
| `NUM_OF_LINES` | string |  |  | `NUM_OF_LINES` |
| `ORIGINAL_JOURNAL_NUM` | string |  |  | `ORIGINAL_JOURNAL_NUM` |
| `LINES_LIMIT_BEFORE_DISTRIBUTION` | string |  |  | `LINES_LIMIT_BEFORE_DISTRIBUTION` |
| `TAX_OBLIGATION_COMPANY` | string |  |  | `TAX_OBLIGATION_COMPANY` |
| `PAYMENTS_GENERATED_IT` | string |  |  | `PAYMENTS_GENERATED_IT` |
| `SYS_DATA_AREA_ID` | string |  |  | `SYS_DATA_AREA_ID` |
| `USER_BLOCK_ID` | string |  |  | `USER_BLOCK_ID` |
| `SYSTEM_BLOCKED` | string |  |  | `SYSTEM_BLOCKED` |
| `JOURNAL_TOTAL_CREDIT_REPORTING_CURRENCY` | string |  |  | `JOURNAL_TOTAL_CREDIT_REPORTING_CURRENCY` |
| `LOG` | string |  |  | `LOG` |
| `GROUP_BLOCK_ID` | string |  |  | `GROUP_BLOCK_ID` |
| `SYS_REC_VERSION` | string |  |  | `SYS_REC_VERSION` |
| `JOURNAL_TOTAL_DEBIT_REPORTING_CURRENCY` | string |  |  | `JOURNAL_TOTAL_DEBIT_REPORTING_CURRENCY` |
| `JOURNAL_TOTAL_CREDIT` | string |  |  | `JOURNAL_TOTAL_CREDIT` |
| `SOURCE_KEY` | string |  |  | `SOURCE_KEY` |
| `SYSTEM_BLOCKED_REASON` | string |  |  | `SYSTEM_BLOCKED_REASON` |
| `BANK_ACCOUNT_ID` | string |  |  | `BANK_ACCOUNT_ID` |
| `END_BALANCE` | string |  |  | `END_BALANCE` |
| `OVERRIDE_SALES_TAX` | string |  |  | `OVERRIDE_SALES_TAX` |
| `OFFSET_LEDGER_DIMENSION_VALUES_JSON` | string |  |  | `OFFSET_LEDGER_DIMENSION_VALUES_JSON` |
| `EXCHRATE_SECONDARY` | string |  |  | `EXCHRATE_SECONDARY` |
| `FIXED_OFFSET_ACCOUNT` | string |  |  | `FIXED_OFFSET_ACCOUNT` |
| `REPORTING_CURRENCY_EXCH_RATE_SECONDARY` | string |  |  | `REPORTING_CURRENCY_EXCH_RATE_SECONDARY` |
| `FIXED_EXCH_RATE` | string |  |  | `FIXED_EXCH_RATE` |
| `CURRENCY_CODE` | string |  |  | `CURRENCY_CODE` |
| `DETAIL_SUMMARY_POSTING` | string |  |  | `DETAIL_SUMMARY_POSTING` |
| `DELAY_TAX_CALCULATION` | string |  |  | `DELAY_TAX_CALCULATION` |
| `SYS_MODIFIED_BY` | string |  |  | `SYS_MODIFIED_BY` |
| `SESSION_ID` | string |  |  | `SESSION_ID` |
| `INTEGRATION_KEY` | string |  |  | `INTEGRATION_KEY` |
| `IS_ADJUSTMENT_JOURNAL` | string |  |  | `IS_ADJUSTMENT_JOURNAL` |
| `CURRENT_OPERATIONS_TAX` | string |  |  | `CURRENT_OPERATIONS_TAX` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**REVERSE_ENTRY**
- `No`
- `None`
- `0`
- `240376449.16`
- `1000`
- `9050`
- `899`
- `11550`
- `303.8`
- `9350`
- `10350`
- `9950`
- `11650`
- `11750`
- `10250`
- `11150`
- `10050`
- `9850`
- `3044965260.94`
- `450`
- `10550`
- `10450`
- `10650`
- `10150`
- `11050`
- `9150`
- `298.84`
- `9450`
- `11850`
- `11950`
- `35865`
- `12350`
- `12250`
- `10950`
- `9550`
- `12050`
- `9750`
- `11250`
- `9250`
- `12550`
- `11450`
- `11350`
- `10750`
- `12150`
- `9650`
- `10850`
- `12450`

**JOURNAL_NAME**
- `None`
- `VIJ`
- `GJV`
- `FYNAPSE`
- `FAJ`
- `GJV_S`
- `VPJ`
- `Elimina`
- `Allocation`
- `CPJ`
- `InterCom`
- `Intercom`
- `ELM`

**OFFSET_ACCOUNT_TYPE**
- `Ledger`
- `None`
- `0`

**BANK_REMITTANCE_TYPE**
- `None`
- `0`
- `No`

**REVERSE_DATE**
- `1900-01-01 12:00:00.0000000 +00:00`
- `None`
- `No`

**RETAIL_STATEMENT_ID**
- `None`
- `0`

**JOURNAL_TYPE**
- `Daily`
- `VendInvoiceRegister`
- `None`
- `0`
- `Assets`
- `No`
- `Payment`
- `Elimination`
- `CustPayment`
- `Allocation`

**JOURNAL_BALANCE**
- `0`
- `None`
- `No`
- `1000000`
- `-35155389.96`
- `-16207`
- `-11.79`
- `11.79`
- `120953`
- `100`
- `-23958`
- `-0.01`
- `1000`
- `-2637690`
- `633534`
- `-30647`
- `-48663`
- `788697`

**VOUCHER_ALLOCATED_AT_POSTING**
- `No`
- `None`
- `0`

**EURO_TRIANGULATION**
- `No`
- `None`
- `USD`

**FIN_TAG**
- `0`
- `None`
- `Detail`
- `USD`

**IS_LEDGER_DIMENSION_NAME_UPDATED**
- `No`
- `None`
- `Detail`
- `Yes`
- `Summary`

**CUST_VEND_NEG_INST_PROTEST_PROCESS**
- `OpenPaym`
- `None`
- `No`
- `balaji`
- `nilishajaiswal`
- `breddy17`

**REPORTING_CURRENCY_FIXED_EXCH_RATE**
- `No`
- `None`
- `balaji`
- `0`
- `Pratik`
- `Admin`
- `nilishajaiswal`
- `Vaishnavi`

**IN_USE_BY**
- `None`
- `0`

**OFFSET_LEDGER_DIMENSION**
- `0`
- `None`
- `No`

**ASSET_TRANSFER_TYPE_LT**
- `NotTransfer`
- `None`
- `Current`
- `Operations`

**EXCH_RATE**
- `0`
- `None`

**REPORTED_AS_READY_BY**
- `None`

**POSTED**
- `Yes`
- `None`
- `No`

**SESSION_LOGIN_DATE_TIME**
- `1900-01-01 00:00:00.0000000 +00:00`
- `None`

**DEFAULT_DIMENSION**
- `0`
- `None`

**NUMBER_SEQUENCE_TABLE**
- `None`
- `5637198577`
- `5637198525`
- `5637198576`
- `5637253331`
- `5637251926`
- `5637219576`
- `5637253328`
- `5637199326`
- `5637251925`
- `5637198526`
- `5637219577`
- `5637253332`
- `5637212076`
- `5637253327`
- `5637212827`
- `5637252579`
- `5637200079`
- `5637253329`
- `5637200076`
- `5637200826`
- `5637200077`
- `5637253330`
- `5637196139`
- `5637252576`
- `5637252578`
- `5637253780`
- `5637200078`
- `5637253326`

**BANK_TRANS_SUMMARIZATION_ENABLED**
- `No`
- `None`

**PROTEST_SETTLED_BILL**
- `No`
- `None`

**REMOVE_LINE_AFTER_POSTING**
- `No`
- `None`

**DOCUMENT_NUM**
- `None`

**LEDGER_JOURNAL_INCL_TAX**
- `No`
- `None`
- `Yes`

**ASSET_LEASE_PROCESS_ID**
- `00000000-0000-0000-0000-000000000000`
- `None`

**WORKFLOW_APPROVAL_STATUS**
- `None`
- `Approved`
- `NotSubmitted`
- `PendingApproval`
- `Rejected`

**BANK_TRANS_SUMMARIZATION_CRITERIA**
- `NoSummarization`
- `None`

**REPORTING_CURRENCY_EXCH_RATE**
- `0`
- `None`

**NUM_OF_LINES**
- `None`
- `1`
- `0`
- `10`
- `197`
- `2`
- `16`
- `4`
- `49`
- `28`
- `600`
- `52`
- `3`
- `67`
- `194`
- `134`
- `247`
- `72`
- `30`
- `25`
- `53`
- `501`
- `68`
- `12`
- `143`
- `15`
- `37`
- `8611`
- `1094`
- `30356`
- `250`
- `66368`
- `1513`
- `32`
- `35`
- `310`
- `44`
- `38959`
- `96`
- `1159`
- `103`
- `6655`
- `20`
- `1055`
- `3805`
- `1000`
- `8480`
- `5748`
- `24`
- `28190`

**ORIGINAL_JOURNAL_NUM**
- `None`
- `214-000005`
- `201-000016`
- `201-000017`
- `100-000209`

**LINES_LIMIT_BEFORE_DISTRIBUTION**
- `1000`
- `None`
- `0`
- `30000`
- `10000`

**PAYMENTS_GENERATED_IT**
- `No`
- `None`

**USER_BLOCK_ID**
- `None`

**SYSTEM_BLOCKED**
- `No`
- `None`

**LOG**
- `None`
- `No vouchers in the journal can be posted or checked.`
- `Post journalsPosting results for journal batch number 201-000016Voucher PUQ061904898Voucher PUQ061904898The transacti...`
- `Posting results for journal batch number 100-000089Voucher VIJ-000000072Employee to approve the line is not specified.`
- `Posting results for journal batch number 233-000002Voucher GJV_S-000000002The transactions on voucher GJV_S-000000002...`
- `Posting results for journal batch number 201-000015Voucher 201-000000008Voucher 201-000000008The transactions on vouc...`
- `Posting results for journal batch number 100-000214Voucher FAJ-000001973Acquisition for fixed asset BUILD-000001, boo...`
- `Posting results for journal batch number 208-000001Voucher GJV-000000001Voucher GJV-000000001The transactions on vouc...`
- `Posting results for journal batch number UK03-000004Voucher FYNAPSE-000000016Voucher FYNAPSE-000000016Account number ...`
- `Posting results for journal batch number 100-000084Voucher VIJ-000000067Employee to approve the line is not specified.`
- `Posting results for journal batch number 230-000002Voucher GJV-000000001Voucher GJV-000000001The transactions on vouc...`
- `Posting results for journal batch number 100-000234Voucher CPJ-000000002Voucher CPJ-000000002The transactions on vouc...`
- `Posting results for journal batch number 100-000202Voucher GJV-000006Voucher GJV-000006Voucher GJV-000006 is already ...`
- `Posting results for journal batch number 100-000088Voucher VIJ-000000071Employee to approve the line is not specified.`
- `Post journalsPosting results for journal batch number 201-000017Voucher PUQ357536883Voucher PUQ357536883The transacti...`
- `Posting results for journal batch number 201-000020Voucher PUQ357536883Voucher PUQ357536883The transactions on vouche...`
- `Posting results for journal batch number 103-000003Voucher 103-000000001Voucher 103-000000001The transactions on vouc...`

**GROUP_BLOCK_ID**
- `None`

**SYSTEM_BLOCKED_REASON**
- `None`

**BANK_ACCOUNT_ID**
- `None`

**END_BALANCE**
- `None`
- `0`

**OVERRIDE_SALES_TAX**
- `None`
- `No`

**OFFSET_LEDGER_DIMENSION_VALUES_JSON**
- `None`

**EXCHRATE_SECONDARY**
- `None`
- `0`

**FIXED_OFFSET_ACCOUNT**
- `None`
- `No`

**REPORTING_CURRENCY_EXCH_RATE_SECONDARY**
- `None`
- `0`

**FIXED_EXCH_RATE**
- `None`
- `No`

**CURRENCY_CODE**
- `None`

**DETAIL_SUMMARY_POSTING**
- `None`
- `Detail`

**DELAY_TAX_CALCULATION**
- `None`
- `No`

**SESSION_ID**
- `None`
- `0`

**IS_ADJUSTMENT_JOURNAL**
- `None`
- `No`

**CURRENT_OPERATIONS_TAX**
- `None`
- `Current`
- `Operations`

**SOURCE_FILE_NAME**
- `ledgerjournaltablebientities__20261116_105417.csv`

**MDP_CREATED_DATE**
- `2026-11-16 11:42:40.753303+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 11:42:40.753303+00:00`

## Empty columns

Empty in every row: `REPORTED_AS_READY_BY`, `DOCUMENT_NUM`, `USER_BLOCK_ID`, `GROUP_BLOCK_ID`, `BANK_ACCOUNT_ID`, `OFFSET_LEDGER_DIMENSION_VALUES_JSON`, `CURRENCY_CODE`, `INTEGRATION_KEY`. Do not filter or group on them.
