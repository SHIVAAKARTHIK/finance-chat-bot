---
name: fact_cust_trans_opens
schema: silver
layer: silver
domain: ar
type: table
status: active
purpose: Open customer transactions (unsettled customer balances).
grain: one row per DATA_AREA_ID (one open customer transaction; table has only 1 row)
primary_key:
- DATA_AREA_ID
entity_column: DATA_AREA_ID
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues: []
row_count: 1
proposed_fields:
- grain
- primary_key
reviewed: false
---

# fact_cust_trans_opens

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `DATA_AREA_ID` | string |  |  | `DATA_AREA_ID` |
| `SYS_REC_ID` | string |  |  | `SYS_REC_ID` |
| `TDS_AMOUNT_IN` | string |  |  | `TDS_AMOUNT_IN` |
| `ACCOUNT_NUM` | string |  |  | `ACCOUNT_NUM` |
| `USE_CASH_DISC` | string |  |  | `USE_CASH_DISC` |
| `SETTLED_TOTAL_AMOUNT_IN` | string |  |  | `SETTLED_TOTAL_AMOUNT_IN` |
| `SETTLED_LINE_PERCENT_IN` | string |  |  | `SETTLED_LINE_PERCENT_IN` |
| `SYS_DATA_AREA_ID` | string |  |  | `SYS_DATA_AREA_ID` |
| `TAX_WITHHOLD_AMOUNT_ORIGIN_IN` | string |  |  | `TAX_WITHHOLD_AMOUNT_ORIGIN_IN` |
| `COLLECTION_LETTER_CODE` | string |  |  | `COLLECTION_LETTER_CODE` |
| `LAST_INTEREST_DATE` | string |  |  | `LAST_INTEREST_DATE` |
| `EXCH_ADJ_UNREALIZED` | string |  |  | `EXCH_ADJ_UNREALIZED` |
| `REPORTING_CURRENCY_AMOUNT` | string |  |  | `REPORTING_CURRENCY_AMOUNT` |
| `CASH_DISC_DATE` | string |  |  | `CASH_DISC_DATE` |
| `FINE_AMOUNT_PAYM_CUR_BR` | string |  |  | `FINE_AMOUNT_PAYM_CUR_BR` |
| `TRANS_DATE` | string |  |  | `TRANS_DATE` |
| `REF_REC_ID` | string |  |  | `REF_REC_ID` |
| `POSSIBLE_CASH_DISC` | string |  |  | `POSSIBLE_CASH_DISC` |
| `FINE_AMOUNT_BR` | string |  |  | `FINE_AMOUNT_BR` |
| `AMOUNT_CUR` | string |  |  | `AMOUNT_CUR` |
| `COLLECTION_LETTER` | string |  |  | `COLLECTION_LETTER` |
| `INTEREST_AMOUNT_BR` | string |  |  | `INTEREST_AMOUNT_BR` |
| `COV_STATUS` | string |  |  | `COV_STATUS` |
| `BANK_DISC_NOTICE_DEADLINE` | string |  |  | `BANK_DISC_NOTICE_DEADLINE` |
| `AMOUNT_MST` | string |  |  | `AMOUNT_MST` |
| `SETTLEMENT_PRIORITY_CASH_DISC_DATE` | string |  |  | `SETTLEMENT_PRIORITY_CASH_DISC_DATE` |
| `DUE_DATE` | string |  |  | `DUE_DATE` |
| `EXCH_ADJ_UNREALIZED_REPORTING` | string |  |  | `EXCH_ADJ_UNREALIZED_REPORTING` |
| `INTEREST_CODE_BR` | string |  |  | `INTEREST_CODE_BR` |
| `FINE_CODE_BR` | string |  |  | `FINE_CODE_BR` |
| `INTEREST_AMOUNT_PAYM_CUR_BR` | string |  |  | `INTEREST_AMOUNT_PAYM_CUR_BR` |
| `TCS_AMOUNT_IN` | string |  |  | `TCS_AMOUNT_IN` |
| `TAX_DISTRIBUTION` | string |  |  | `TAX_DISTRIBUTION` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**SYS_REC_ID**
- `5637145326`: 1 rows

**TDS_AMOUNT_IN**
- `0`: 1 rows

**ACCOUNT_NUM**
- `100-000001`: 1 rows

**USE_CASH_DISC**
- `Normal`: 1 rows

**SETTLED_TOTAL_AMOUNT_IN**
- `0`: 1 rows

**SETTLED_LINE_PERCENT_IN**
- `0`: 1 rows

**TAX_WITHHOLD_AMOUNT_ORIGIN_IN**
- `0`: 1 rows

**COLLECTION_LETTER_CODE**
- `None`: 1 rows

**LAST_INTEREST_DATE**
- `1900-01-01 12:00:00.0000000 +00:00`: 1 rows

**EXCH_ADJ_UNREALIZED**
- `0`: 1 rows

**REPORTING_CURRENCY_AMOUNT**
- `1000`: 1 rows

**CASH_DISC_DATE**
- `1900-01-01 12:00:00.0000000 +00:00`: 1 rows

**FINE_AMOUNT_PAYM_CUR_BR**
- `0`: 1 rows

**TRANS_DATE**
- `2026-10-26 12:00:00.0000000 +00:00`: 1 rows

**REF_REC_ID**
- `5637145326`: 1 rows

**POSSIBLE_CASH_DISC**
- `0`: 1 rows

**FINE_AMOUNT_BR**
- `0`: 1 rows

**AMOUNT_CUR**
- `1000`: 1 rows

**COLLECTION_LETTER**
- `Yes`: 1 rows

**INTEREST_AMOUNT_BR**
- `0`: 1 rows

**COV_STATUS**
- `0`: 1 rows

**BANK_DISC_NOTICE_DEADLINE**
- `1900-01-01 12:00:00.0000000 +00:00`: 1 rows

**AMOUNT_MST**
- `1000`: 1 rows

**SETTLEMENT_PRIORITY_CASH_DISC_DATE**
- `1900-01-01 12:00:00.0000000 +00:00`: 1 rows

**DUE_DATE**
- `2026-10-26 12:00:00.0000000 +00:00`: 1 rows

**EXCH_ADJ_UNREALIZED_REPORTING**
- `0`: 1 rows

**INTEREST_CODE_BR**
- `None`: 1 rows

**FINE_CODE_BR**
- `None`: 1 rows

**INTEREST_AMOUNT_PAYM_CUR_BR**
- `0`: 1 rows

**TCS_AMOUNT_IN**
- `0`: 1 rows

**TAX_DISTRIBUTION**
- `Proportional`: 1 rows

**SOURCE_FILE_NAME**
- `custtransopens__20261116_105417.csv`: 1 rows

**MDP_CREATED_DATE**
- `2026-11-16 11:42:18.216749+00:00`: 1 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 11:42:18.216749+00:00`: 1 rows

## Profile

Rows in the latest export: 1.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `DATA_AREA_ID` | STRING | 1 | 0 |  |  |
| `SYS_REC_ID` | STRING | 1 | 0 | 5637145326 | 5637145326 |
| `TDS_AMOUNT_IN` | STRING | 1 | 0 | 0 | 0 |
| `ACCOUNT_NUM` | STRING | 1 | 0 | 100-000001 | 100-000001 |
| `USE_CASH_DISC` | STRING | 1 | 0 | Normal | Normal |
| `SETTLED_TOTAL_AMOUNT_IN` | STRING | 1 | 0 | 0 | 0 |
| `SETTLED_LINE_PERCENT_IN` | STRING | 1 | 0 | 0 | 0 |
| `SYS_DATA_AREA_ID` | STRING | 1 | 0 |  |  |
| `TAX_WITHHOLD_AMOUNT_ORIGIN_IN` | STRING | 1 | 0 | 0 | 0 |
| `COLLECTION_LETTER_CODE` | STRING | 1 | 0 | None | None |
| `LAST_INTEREST_DATE` | STRING | 1 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `EXCH_ADJ_UNREALIZED` | STRING | 1 | 0 | 0 | 0 |
| `REPORTING_CURRENCY_AMOUNT` | STRING | 1 | 0 | 1000 | 1000 |
| `CASH_DISC_DATE` | STRING | 1 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `FINE_AMOUNT_PAYM_CUR_BR` | STRING | 1 | 0 | 0 | 0 |
| `TRANS_DATE` | STRING | 1 | 0 | 2026-10-26 12:00:00.0000000 +00:00 | 2026-10-26 12:00:00.0000000 +00:00 |
| `REF_REC_ID` | STRING | 1 | 0 | 5637145326 | 5637145326 |
| `POSSIBLE_CASH_DISC` | STRING | 1 | 0 | 0 | 0 |
| `FINE_AMOUNT_BR` | STRING | 1 | 0 | 0 | 0 |
| `AMOUNT_CUR` | STRING | 1 | 0 | 1000 | 1000 |
| `COLLECTION_LETTER` | STRING | 1 | 0 | Yes | Yes |
| `INTEREST_AMOUNT_BR` | STRING | 1 | 0 | 0 | 0 |
| `COV_STATUS` | STRING | 1 | 0 | 0 | 0 |
| `BANK_DISC_NOTICE_DEADLINE` | STRING | 1 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `AMOUNT_MST` | STRING | 1 | 0 | 1000 | 1000 |
| `SETTLEMENT_PRIORITY_CASH_DISC_DATE` | STRING | 1 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `DUE_DATE` | STRING | 1 | 0 | 2026-10-26 12:00:00.0000000 +00:00 | 2026-10-26 12:00:00.0000000 +00:00 |
| `EXCH_ADJ_UNREALIZED_REPORTING` | STRING | 1 | 0 | 0 | 0 |
| `INTEREST_CODE_BR` | STRING | 0 | 1 |  |  |
| `FINE_CODE_BR` | STRING | 0 | 1 |  |  |
| `INTEREST_AMOUNT_PAYM_CUR_BR` | STRING | 1 | 0 | 0 | 0 |
| `TCS_AMOUNT_IN` | STRING | 1 | 0 | 0 | 0 |
| `TAX_DISTRIBUTION` | STRING | 1 | 0 | Proportional | Proportional |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | custtransopens__20261116_105417.csv | custtransopens__20261116_105417.csv |
| `HASH_KEY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:42:18.217000 | 2026-11-16 11:42:18.217000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:42:18.217000 | 2026-11-16 11:42:18.217000 |

## Sample rows

| SYS_REC_ID | TDS_AMOUNT_IN | ACCOUNT_NUM | USE_CASH_DISC | SETTLED_TOTAL_AMOUNT_IN | SETTLED_LINE_PERCENT_IN | TAX_WITHHOLD_AMOUNT_ORIGIN_IN | COLLECTION_LETTER_CODE | LAST_INTEREST_DATE | EXCH_ADJ_UNREALIZED | REPORTING_CURRENCY_AMOUNT | CASH_DISC_DATE | FINE_AMOUNT_PAYM_CUR_BR | TRANS_DATE | REF_REC_ID | POSSIBLE_CASH_DISC | FINE_AMOUNT_BR | AMOUNT_CUR | COLLECTION_LETTER | INTEREST_AMOUNT_BR | COV_STATUS | BANK_DISC_NOTICE_DEADLINE | AMOUNT_MST | SETTLEMENT_PRIORITY_CASH_DISC_DATE | DUE_DATE | EXCH_ADJ_UNREALIZED_REPORTING | INTEREST_CODE_BR | FINE_CODE_BR | INTEREST_AMOUNT_PAYM_CUR_BR | TCS_AMOUNT_IN | TAX_DISTRIBUTION | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5637145326 | 0 | 100-000001 | Normal | 0 | 0 | 0 | None | 1900-01-01 12:00:00.0000000 +00:00 | 0 | 1000 | 1900-01-01 12:00:00.0000000 +00:00 | 0 | 2026-10-26 12:00:00.0000000 +00:00 | 5637145326 | 0 | 0 | 1000 | Yes | 0 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1000 | 1900-01-01 12:00:00.0000000 +00:00 | 2026-10-26 12:00:00.0000000 +00:00 | 0 | NULL | NULL | 0 | 0 | Proportional | custtransopens__20261116_105417.csv | <masked> | 2026-11-16 11:42:18.217000 | <masked> | 2026-11-16 11:42:18.217000 |
