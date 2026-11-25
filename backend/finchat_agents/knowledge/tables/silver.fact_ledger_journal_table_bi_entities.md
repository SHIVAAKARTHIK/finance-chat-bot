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
row_count: 459
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
- `No`: 290 rows
- `None`: 99 rows
- `0`: 26 rows
- `240376449.16`: 1 rows
- `1000`: 1 rows
- `9050`: 1 rows
- `899`: 1 rows
- `11550`: 1 rows
- `303.8`: 1 rows
- `9350`: 1 rows
- `10350`: 1 rows
- `9950`: 1 rows
- `11650`: 1 rows
- `11750`: 1 rows
- `10250`: 1 rows
- `11150`: 1 rows
- `10050`: 1 rows
- `9850`: 1 rows
- `3044965260.94`: 1 rows
- `450`: 1 rows
- `10550`: 1 rows
- `10450`: 1 rows
- `10650`: 1 rows
- `10150`: 1 rows
- `11050`: 1 rows
- `9150`: 1 rows
- `298.84`: 1 rows
- `9450`: 1 rows
- `11850`: 1 rows
- `11950`: 1 rows
- `35865`: 1 rows
- `12350`: 1 rows
- `12250`: 1 rows
- `10950`: 1 rows
- `9550`: 1 rows
- `12050`: 1 rows
- `9750`: 1 rows
- `11250`: 1 rows
- `9250`: 1 rows
- `12550`: 1 rows
- `11450`: 1 rows
- `11350`: 1 rows
- `10750`: 1 rows
- `12150`: 1 rows
- `9650`: 1 rows
- `10850`: 1 rows
- `12450`: 1 rows

**JOURNAL_NAME**
- `None`: 108 rows
- `VIJ`: 102 rows
- `GJV`: 86 rows
- `FYNAPSE`: 44 rows
- `FAJ`: 34 rows
- `GJV_S`: 7 rows
- `VPJ`: 7 rows
- `Elimina`: 2 rows
- `Allocation`: 2 rows
- `CPJ`: 2 rows
- `InterCom`: 2 rows
- `Intercom`: 1 rows
- `ELM`: 1 rows

**OFFSET_ACCOUNT_TYPE**
- `Ledger`: 290 rows
- `None`: 160 rows
- `0`: 9 rows

**BANK_REMITTANCE_TYPE**
- `None`: 290 rows
- `0`: 61 rows
- `No`: 9 rows

**REVERSE_DATE**
- `1900-01-01 12:00:00.0000000 +00:00`: 290 rows
- `None`: 108 rows
- `No`: 61 rows

**RETAIL_STATEMENT_ID**
- `None`: 450 rows
- `0`: 9 rows

**JOURNAL_TYPE**
- `Daily`: 140 rows
- `VendInvoiceRegister`: 102 rows
- `None`: 99 rows
- `0`: 61 rows
- `Assets`: 34 rows
- `No`: 9 rows
- `Payment`: 7 rows
- `Elimination`: 3 rows
- `CustPayment`: 2 rows
- `Allocation`: 2 rows

**JOURNAL_BALANCE**
- `0`: 283 rows
- `None`: 99 rows
- `No`: 61 rows
- `1000000`: 2 rows
- `-35155389.96`: 1 rows
- `-16207`: 1 rows
- `-11.79`: 1 rows
- `11.79`: 1 rows
- `120953`: 1 rows
- `100`: 1 rows
- `-23958`: 1 rows
- `-0.01`: 1 rows
- `1000`: 1 rows
- `-2637690`: 1 rows
- `633534`: 1 rows
- `-30647`: 1 rows
- `-48663`: 1 rows
- `788697`: 1 rows

**VOUCHER_ALLOCATED_AT_POSTING**
- `No`: 299 rows
- `None`: 99 rows
- `0`: 61 rows

**EURO_TRIANGULATION**
- `No`: 351 rows
- `None`: 104 rows
- `USD`: 4 rows

**FIN_TAG**
- `0`: 290 rows
- `None`: 156 rows
- `Detail`: 9 rows
- `USD`: 4 rows

**IS_LEDGER_DIMENSION_NAME_UPDATED**
- `No`: 292 rows
- `None`: 99 rows
- `Detail`: 60 rows
- `Yes`: 7 rows
- `Summary`: 1 rows

**CUST_VEND_NEG_INST_PROTEST_PROCESS**
- `OpenPaym`: 290 rows
- `None`: 99 rows
- `No`: 61 rows
- `balaji`: 5 rows
- `nilishajaiswal`: 3 rows
- `breddy17`: 1 rows

**REPORTING_CURRENCY_FIXED_EXCH_RATE**
- `No`: 290 rows
- `None`: 99 rows
- `balaji`: 48 rows
- `0`: 9 rows
- `Pratik`: 6 rows
- `Admin`: 5 rows
- `nilishajaiswal`: 1 rows
- `Vaishnavi`: 1 rows

**IN_USE_BY**
- `None`: 398 rows
- `0`: 61 rows

**OFFSET_LEDGER_DIMENSION**
- `0`: 290 rows
- `None`: 160 rows
- `No`: 9 rows

**ASSET_TRANSFER_TYPE_LT**
- `NotTransfer`: 290 rows
- `None`: 108 rows
- `Current`: 60 rows
- `Operations`: 1 rows

**EXCH_RATE**
- `0`: 290 rows
- `None`: 169 rows

**REPORTED_AS_READY_BY**
- `None`: 459 rows

**POSTED**
- `Yes`: 208 rows
- `None`: 169 rows
- `No`: 82 rows

**SESSION_LOGIN_DATE_TIME**
- `1900-01-01 00:00:00.0000000 +00:00`: 290 rows
- `None`: 169 rows

**DEFAULT_DIMENSION**
- `0`: 290 rows
- `None`: 169 rows

**NUMBER_SEQUENCE_TABLE**
- `None`: 169 rows
- `5637198577`: 102 rows
- `5637198525`: 48 rows
- `5637198576`: 34 rows
- `5637253331`: 16 rows
- `5637251926`: 12 rows
- `5637219576`: 10 rows
- `5637253328`: 8 rows
- `5637199326`: 7 rows
- `5637251925`: 6 rows
- `5637198526`: 5 rows
- `5637219577`: 4 rows
- `5637253332`: 4 rows
- `5637212076`: 4 rows
- `5637253327`: 3 rows
- `5637212827`: 3 rows
- `5637252579`: 3 rows
- `5637200079`: 3 rows
- `5637253329`: 2 rows
- `5637200076`: 2 rows
- `5637200826`: 2 rows
- `5637200077`: 2 rows
- `5637253330`: 2 rows
- `5637196139`: 2 rows
- `5637252576`: 2 rows
- `5637252578`: 1 rows
- `5637253780`: 1 rows
- `5637200078`: 1 rows
- `5637253326`: 1 rows

**BANK_TRANS_SUMMARIZATION_ENABLED**
- `No`: 290 rows
- `None`: 169 rows

**PROTEST_SETTLED_BILL**
- `No`: 290 rows
- `None`: 169 rows

**REMOVE_LINE_AFTER_POSTING**
- `No`: 290 rows
- `None`: 169 rows

**DOCUMENT_NUM**
- `None`: 459 rows

**LEDGER_JOURNAL_INCL_TAX**
- `No`: 169 rows
- `None`: 169 rows
- `Yes`: 121 rows

**ASSET_LEASE_PROCESS_ID**
- `00000000-0000-0000-0000-000000000000`: 290 rows
- `None`: 169 rows

**WORKFLOW_APPROVAL_STATUS**
- `None`: 169 rows
- `Approved`: 109 rows
- `NotSubmitted`: 34 rows
- `PendingApproval`: 7 rows
- `Rejected`: 3 rows

**BANK_TRANS_SUMMARIZATION_CRITERIA**
- `NoSummarization`: 290 rows
- `None`: 169 rows

**REPORTING_CURRENCY_EXCH_RATE**
- `0`: 290 rows
- `None`: 169 rows

**NUM_OF_LINES**
- `None`: 169 rows
- `1`: 107 rows
- `0`: 96 rows
- `10`: 8 rows
- `197`: 8 rows
- `2`: 7 rows
- `16`: 6 rows
- `4`: 4 rows
- `49`: 3 rows
- `28`: 3 rows
- `600`: 3 rows
- `52`: 3 rows
- `3`: 2 rows
- `67`: 2 rows
- `194`: 2 rows
- `134`: 2 rows
- `247`: 1 rows
- `72`: 1 rows
- `30`: 1 rows
- `25`: 1 rows
- `53`: 1 rows
- `501`: 1 rows
- `68`: 1 rows
- `12`: 1 rows
- `143`: 1 rows
- `15`: 1 rows
- `37`: 1 rows
- `8611`: 1 rows
- `1094`: 1 rows
- `30356`: 1 rows
- `250`: 1 rows
- `66368`: 1 rows
- `1513`: 1 rows
- `32`: 1 rows
- `35`: 1 rows
- `310`: 1 rows
- `44`: 1 rows
- `38959`: 1 rows
- `96`: 1 rows
- `1159`: 1 rows
- `103`: 1 rows
- `6655`: 1 rows
- `20`: 1 rows
- `1055`: 1 rows
- `3805`: 1 rows
- `1000`: 1 rows
- `8480`: 1 rows
- `5748`: 1 rows
- `24`: 1 rows
- `28190`: 1 rows

**ORIGINAL_JOURNAL_NUM**
- `None`: 442 rows
- `214-000005`: 12 rows
- `201-000016`: 3 rows
- `201-000017`: 1 rows
- `100-000209`: 1 rows

**LINES_LIMIT_BEFORE_DISTRIBUTION**
- `1000`: 244 rows
- `None`: 169 rows
- `0`: 36 rows
- `30000`: 9 rows
- `10000`: 1 rows

**PAYMENTS_GENERATED_IT**
- `No`: 290 rows
- `None`: 169 rows

**USER_BLOCK_ID**
- `None`: 459 rows

**SYSTEM_BLOCKED**
- `No`: 290 rows
- `None`: 169 rows

**LOG**
- `None`: 397 rows
- `No vouchers in the journal can be posted or checked.`: 46 rows
- `Post journalsPosting results for journal batch number 201-000016Voucher PUQ061904898Voucher PUQ061904898The transacti...`: 2 rows
- `Posting results for journal batch number 100-000089Voucher VIJ-000000072Employee to approve the line is not specified.`: 1 rows
- `Posting results for journal batch number 233-000002Voucher GJV_S-000000002The transactions on voucher GJV_S-000000002...`: 1 rows
- `Posting results for journal batch number 201-000015Voucher 201-000000008Voucher 201-000000008The transactions on vouc...`: 1 rows
- `Posting results for journal batch number 100-000214Voucher FAJ-000001973Acquisition for fixed asset BUILD-000001, boo...`: 1 rows
- `Posting results for journal batch number 208-000001Voucher GJV-000000001Voucher GJV-000000001The transactions on vouc...`: 1 rows
- `Posting results for journal batch number UK03-000004Voucher FYNAPSE-000000016Voucher FYNAPSE-000000016Account number ...`: 1 rows
- `Posting results for journal batch number 100-000084Voucher VIJ-000000067Employee to approve the line is not specified.`: 1 rows
- `Posting results for journal batch number 230-000002Voucher GJV-000000001Voucher GJV-000000001The transactions on vouc...`: 1 rows
- `Posting results for journal batch number 100-000234Voucher CPJ-000000002Voucher CPJ-000000002The transactions on vouc...`: 1 rows
- `Posting results for journal batch number 100-000202Voucher GJV-000006Voucher GJV-000006Voucher GJV-000006 is already ...`: 1 rows
- `Posting results for journal batch number 100-000088Voucher VIJ-000000071Employee to approve the line is not specified.`: 1 rows
- `Post journalsPosting results for journal batch number 201-000017Voucher PUQ357536883Voucher PUQ357536883The transacti...`: 1 rows
- `Posting results for journal batch number 201-000020Voucher PUQ357536883Voucher PUQ357536883The transactions on vouche...`: 1 rows
- `Posting results for journal batch number 103-000003Voucher 103-000000001Voucher 103-000000001The transactions on vouc...`: 1 rows

**GROUP_BLOCK_ID**
- `None`: 459 rows

**SYSTEM_BLOCKED_REASON**
- `None`: 231 rows

**BANK_ACCOUNT_ID**
- `None`: 459 rows

**END_BALANCE**
- `None`: 231 rows
- `0`: 228 rows

**OVERRIDE_SALES_TAX**
- `None`: 231 rows
- `No`: 228 rows

**OFFSET_LEDGER_DIMENSION_VALUES_JSON**
- `None`: 459 rows

**EXCHRATE_SECONDARY**
- `None`: 231 rows
- `0`: 228 rows

**FIXED_OFFSET_ACCOUNT**
- `None`: 231 rows
- `No`: 228 rows

**REPORTING_CURRENCY_EXCH_RATE_SECONDARY**
- `None`: 231 rows
- `0`: 228 rows

**FIXED_EXCH_RATE**
- `None`: 231 rows
- `No`: 228 rows

**CURRENCY_CODE**
- `None`: 459 rows

**DETAIL_SUMMARY_POSTING**
- `None`: 231 rows
- `Detail`: 228 rows

**DELAY_TAX_CALCULATION**
- `None`: 231 rows
- `No`: 228 rows

**SESSION_ID**
- `None`: 231 rows
- `0`: 228 rows

**IS_ADJUSTMENT_JOURNAL**
- `None`: 231 rows
- `No`: 228 rows

**CURRENT_OPERATIONS_TAX**
- `None`: 231 rows
- `Current`: 223 rows
- `Operations`: 5 rows

**SOURCE_FILE_NAME**
- `ledgerjournaltablebientities__20261116_105417.csv`: 459 rows

**MDP_CREATED_DATE**
- `2026-11-16 11:42:40.753303+00:00`: 459 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 11:42:40.753303+00:00`: 459 rows

## Profile

Rows in the latest export: 459.
Exact duplicate rows: 92.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `DATA_AREA_ID` | STRING | 39 | 0 |  |  |
| `JOURNAL_NUM` | STRING | 316 | 156 | see the message center for more details. | UK17-000016 |
| `REV_REC_REALLOCATION_ID` | STRING | 65 | 389 | 0 | 984056966 |
| `REVERSE_ENTRY` | STRING | 45 | 99 | 0 | No |
| `POSTED_DATE_TIME` | STRING | 210 | 99 | 0 | 9950 |
| `SIMULATION_POSTED_IT` | STRING | 65 | 99 | 5637149840 | None |
| `JOURNAL_NAME` | STRING | 13 | 108 | Allocation | VPJ |
| `OFFSET_ACCOUNT_TYPE` | STRING | 2 | 160 | 0 | Ledger |
| `BANK_REMITTANCE_TYPE` | STRING | 3 | 99 | 0 | None |
| `REVERSE_DATE` | STRING | 2 | 108 | 1900-01-01 12:00:00.0000000 +00:00 | No |
| `RETAIL_STATEMENT_ID` | STRING | 1 | 450 | 0 | 0 |
| `JOURNAL_TYPE` | STRING | 9 | 99 | 0 | VendInvoiceRegister |
| `JOURNAL_BALANCE` | STRING | 17 | 99 | -0.01 | No |
| `VOUCHER_ALLOCATED_AT_POSTING` | STRING | 2 | 99 | 0 | No |
| `EURO_TRIANGULATION` | STRING | 2 | 104 | No | USD |
| `FIN_TAG` | STRING | 3 | 156 | 0 | USD |
| `IS_LEDGER_DIMENSION_NAME_UPDATED` | STRING | 4 | 99 | Detail | Yes |
| `CUST_VEND_NEG_INST_PROTEST_PROCESS` | STRING | 5 | 99 | No | nilishajaiswal |
| `REPORTING_CURRENCY_FIXED_EXCH_RATE` | STRING | 7 | 99 | 0 | nilishajaiswal |
| `IN_USE_BY` | STRING | 1 | 398 | 0 | 0 |
| `OFFSET_LEDGER_DIMENSION` | STRING | 2 | 160 | 0 | No |
| `REJECTED_BY` | STRING | 2 | 389 |  |  |
| `ASSET_TRANSFER_TYPE_LT` | STRING | 3 | 108 | Current | Operations |
| `EXCH_RATE` | STRING | 1 | 169 | 0 | 0 |
| `REPORTED_AS_READY_BY` | STRING | 0 | 459 |  |  |
| `POSTED` | STRING | 2 | 169 | No | Yes |
| `SESSION_LOGIN_DATE_TIME` | STRING | 1 | 169 | 1900-01-01 00:00:00.0000000 +00:00 | 1900-01-01 00:00:00.0000000 +00:00 |
| `SYS_CREATED_BY` | STRING | 7 | 169 |  |  |
| `DEFAULT_DIMENSION` | STRING | 1 | 169 | 0 | 0 |
| `JOURNAL_TOTAL_DEBIT` | STRING | 220 | 169 | 0 | 9950 |
| `PARENT_JOURNAL_NUM` | STRING | 282 | 169 | 100-000001 | UK17-000016 |
| `NUMBER_SEQUENCE_TABLE` | STRING | 28 | 169 | 5637196139 | 5637253780 |
| `JOURNAL_TOTAL_OFFSET_BALANCE` | STRING | 176 | 169 | -0.01 | 8450 |
| `BANK_TRANS_SUMMARIZATION_ENABLED` | STRING | 1 | 169 | No | No |
| `PROTEST_SETTLED_BILL` | STRING | 1 | 169 | No | No |
| `REMOVE_LINE_AFTER_POSTING` | STRING | 1 | 169 | No | No |
| `DOCUMENT_NUM` | STRING | 0 | 459 |  |  |
| `LEDGER_JOURNAL_INCL_TAX` | STRING | 2 | 169 | No | Yes |
| `ASSET_LEASE_PROCESS_ID` | STRING | 1 | 169 | 00000000-0000-0000-0000-000000000000 | 00000000-0000-0000-0000-000000000000 |
| `ORIGINAL_COMPANY` | STRING | 1 | 458 |  |  |
| `APPROVER` | STRING | 1 | 169 |  |  |
| `WORKFLOW_APPROVAL_STATUS` | STRING | 5 | 169 | Approved | Rejected |
| `NAME` | STRING | 97 | 169 | 201-2025 transactions | in_01a1aa807abb7c30803c92551e5884c5 |
| `BANK_TRANS_SUMMARIZATION_CRITERIA` | STRING | 1 | 169 | NoSummarization | NoSummarization |
| `REPORTING_CURRENCY_EXCH_RATE` | STRING | 1 | 169 | 0 | 0 |
| `NUM_OF_LINES` | STRING | 50 | 169 | 0 | 96 |
| `ORIGINAL_JOURNAL_NUM` | STRING | 4 | 442 | 100-000209 | 214-000005 |
| `LINES_LIMIT_BEFORE_DISTRIBUTION` | STRING | 4 | 169 | 0 | 30000 |
| `TAX_OBLIGATION_COMPANY` | STRING | 1 | 169 |  |  |
| `PAYMENTS_GENERATED_IT` | STRING | 1 | 169 | No | No |
| `SYS_DATA_AREA_ID` | STRING | 18 | 169 |  |  |
| `USER_BLOCK_ID` | STRING | 0 | 459 |  |  |
| `SYSTEM_BLOCKED` | STRING | 1 | 169 | No | No |
| `JOURNAL_TOTAL_CREDIT_REPORTING_CURRENCY` | STRING | 222 | 169 | 0 | 9950 |
| `LOG` | STRING | 16 | 397 | No vouchers in the journal can be pos... | Posting results for journal batch num... |
| `GROUP_BLOCK_ID` | STRING | 0 | 459 |  |  |
| `SYS_REC_VERSION` | STRING | 236 | 231 | 1 | 998983828 |
| `JOURNAL_TOTAL_DEBIT_REPORTING_CURRENCY` | STRING | 182 | 231 | 0 | 8950 |
| `JOURNAL_TOTAL_CREDIT` | STRING | 182 | 231 | 0 | 8950 |
| `SOURCE_KEY` | STRING | 217 | 231 |  |  |
| `SYSTEM_BLOCKED_REASON` | STRING | 1 | 231 | None | None |
| `BANK_ACCOUNT_ID` | STRING | 0 | 459 |  |  |
| `END_BALANCE` | STRING | 1 | 231 | 0 | 0 |
| `OVERRIDE_SALES_TAX` | STRING | 1 | 231 | No | No |
| `OFFSET_LEDGER_DIMENSION_VALUES_JSON` | STRING | 0 | 459 |  |  |
| `EXCHRATE_SECONDARY` | STRING | 1 | 231 | 0 | 0 |
| `FIXED_OFFSET_ACCOUNT` | STRING | 1 | 231 | No | No |
| `REPORTING_CURRENCY_EXCH_RATE_SECONDARY` | STRING | 1 | 231 | 0 | 0 |
| `FIXED_EXCH_RATE` | STRING | 1 | 231 | No | No |
| `CURRENCY_CODE` | STRING | 0 | 459 |  |  |
| `DETAIL_SUMMARY_POSTING` | STRING | 1 | 231 | Detail | Detail |
| `DELAY_TAX_CALCULATION` | STRING | 1 | 231 | No | No |
| `SYS_MODIFIED_BY` | STRING | 8 | 231 |  |  |
| `SESSION_ID` | STRING | 1 | 231 | 0 | 0 |
| `INTEGRATION_KEY` | STRING | 0 | 459 |  |  |
| `IS_ADJUSTMENT_JOURNAL` | STRING | 1 | 231 | No | No |
| `CURRENT_OPERATIONS_TAX` | STRING | 2 | 231 | Current | Operations |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | ledgerjournaltablebientities__2026111... | ledgerjournaltablebientities__2026111... |
| `HASH_KEY` | STRING | 349 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:42:40.753000 | 2026-11-16 11:42:40.753000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:42:40.753000 | 2026-11-16 11:42:40.753000 |

## Sample rows

| JOURNAL_NUM | REV_REC_REALLOCATION_ID | REVERSE_ENTRY | POSTED_DATE_TIME | SIMULATION_POSTED_IT | JOURNAL_NAME | OFFSET_ACCOUNT_TYPE | BANK_REMITTANCE_TYPE | REVERSE_DATE | RETAIL_STATEMENT_ID | JOURNAL_TYPE | JOURNAL_BALANCE | VOUCHER_ALLOCATED_AT_POSTING | EURO_TRIANGULATION | FIN_TAG | IS_LEDGER_DIMENSION_NAME_UPDATED | CUST_VEND_NEG_INST_PROTEST_PROCESS | REPORTING_CURRENCY_FIXED_EXCH_RATE | IN_USE_BY | OFFSET_LEDGER_DIMENSION | REJECTED_BY | ASSET_TRANSFER_TYPE_LT | EXCH_RATE | REPORTED_AS_READY_BY | POSTED | SESSION_LOGIN_DATE_TIME | SYS_CREATED_BY | DEFAULT_DIMENSION | JOURNAL_TOTAL_DEBIT | PARENT_JOURNAL_NUM | NUMBER_SEQUENCE_TABLE | JOURNAL_TOTAL_OFFSET_BALANCE | BANK_TRANS_SUMMARIZATION_ENABLED | PROTEST_SETTLED_BILL | REMOVE_LINE_AFTER_POSTING | DOCUMENT_NUM | LEDGER_JOURNAL_INCL_TAX | ASSET_LEASE_PROCESS_ID | APPROVER | WORKFLOW_APPROVAL_STATUS | NAME | BANK_TRANS_SUMMARIZATION_CRITERIA | REPORTING_CURRENCY_EXCH_RATE | NUM_OF_LINES | ORIGINAL_JOURNAL_NUM | LINES_LIMIT_BEFORE_DISTRIBUTION | PAYMENTS_GENERATED_IT | USER_BLOCK_ID | SYSTEM_BLOCKED | JOURNAL_TOTAL_CREDIT_REPORTING_CURRENCY | LOG | GROUP_BLOCK_ID | SYS_REC_VERSION | JOURNAL_TOTAL_DEBIT_REPORTING_CURRENCY | JOURNAL_TOTAL_CREDIT | SYSTEM_BLOCKED_REASON | BANK_ACCOUNT_ID | END_BALANCE | OVERRIDE_SALES_TAX | OFFSET_LEDGER_DIMENSION_VALUES_JSON | EXCHRATE_SECONDARY | FIXED_OFFSET_ACCOUNT | REPORTING_CURRENCY_EXCH_RATE_SECONDARY | FIXED_EXCH_RATE | CURRENCY_CODE | DETAIL_SUMMARY_POSTING | DELAY_TAX_CALCULATION | SYS_MODIFIED_BY | SESSION_ID | IS_ADJUSTMENT_JOURNAL | CURRENT_OPERATIONS_TAX | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| see the message center for more details. | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | ledgerjournaltablebientities__2026111... | <masked> | 2026-11-16 11:42:40.753000 | <masked> | 2026-11-16 11:42:40.753000 |
| 2113441029 | 0 | 450 | 5637146828 | None | NULL | 0 | No | NULL | 0 | No | 0 | No | USD | Detail | No | nilishajaiswal | 0 | NULL | No | <masked> | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | ledgerjournaltablebientities__2026111... | <masked> | 2026-11-16 11:42:40.753000 | <masked> | 2026-11-16 11:42:40.753000 |
| see the message center for more details. | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | ledgerjournaltablebientities__2026111... | <masked> | 2026-11-16 11:42:40.753000 | <masked> | 2026-11-16 11:42:40.753000 |
| 2102427328 | 0 | 0 | 5637148329 | None | NULL | 0 | No | NULL | 0 | No | 0 | No | USD | Detail | No | nilishajaiswal | 0 | NULL | No | <masked> | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | ledgerjournaltablebientities__2026111... | <masked> | 2026-11-16 11:42:40.753000 | <masked> | 2026-11-16 11:42:40.753000 |
| see the message center for more details. | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | <masked> | NULL | NULL | NULL | ledgerjournaltablebientities__2026111... | <masked> | 2026-11-16 11:42:40.753000 | <masked> | 2026-11-16 11:42:40.753000 |
