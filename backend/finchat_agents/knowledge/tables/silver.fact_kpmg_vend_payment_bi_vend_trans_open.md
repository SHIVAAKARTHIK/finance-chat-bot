---
name: fact_kpmg_vend_payment_bi_vend_trans_open
schema: silver
layer: silver
domain: ap
type: table
status: active
purpose: Open vendor transactions (unpaid invoices) with due dates.
grain: one row per REF_REC_ID (one open vendor invoice)
primary_key:
- REF_REC_ID
entity_column: DATA_AREA_ID
period_columns:
- DUE_DATE
- TRANS_DATE
- CASH_DISC_DATE
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues: []
row_count: 118
proposed_fields:
- grain
- primary_key
reviewed: false
---

# fact_kpmg_vend_payment_bi_vend_trans_open

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `DATA_AREA_ID` | string |  |  | `DATA_AREA_ID` |
| `REF_REC_ID` | string |  |  | `REF_REC_ID` |
| `INVOICE` | string |  |  | `INVOICE` |
| `AMOUNT_CUR` | string |  |  | `AMOUNT_CUR` |
| `DUE_DATE` | string |  |  | `DUE_DATE` |
| `CASH_DISC_DATE` | string |  |  | `CASH_DISC_DATE` |
| `AMOUNT_MST` | string |  |  | `AMOUNT_MST` |
| `ACCOUNT_NUM` | string |  |  | `ACCOUNT_NUM` |
| `TRANS_DATE` | string |  |  | `TRANS_DATE` |
| `CASH_DISC_AMOUNT_CUR` | string |  |  | `CASH_DISC_AMOUNT_CUR` |
| `CASH_DISC_CALCULATION_DATE` | string |  |  | `CASH_DISC_CALCULATION_DATE` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**CASH_DISC_DATE**
- `1900-01-01 12:00:00.0000000 +00:00`: 118 rows

**CASH_DISC_AMOUNT_CUR**
- `0`: 118 rows

**CASH_DISC_CALCULATION_DATE**
- `1900-01-01 12:00:00.0000000 +00:00`: 118 rows

**SOURCE_FILE_NAME**
- `kpmg_vendpaymentbivendtransopen__20261116_105417.csv`: 118 rows

**MDP_CREATED_DATE**
- `2026-11-16 11:43:23.516910+00:00`: 118 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 11:43:23.516910+00:00`: 118 rows

## Profile

Rows in the latest export: 118.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `DATA_AREA_ID` | STRING | 1 | 0 |  |  |
| `REF_REC_ID` | STRING | 120 | 0 | 5637167077 | 5637169327 |
| `INVOICE` | STRING | 118 | 1 | INV2003 | Inv-056 |
| `AMOUNT_CUR` | STRING | 118 | 0 | -10000 | -8950 |
| `DUE_DATE` | STRING | 108 | 0 | 2025-01-18 12:00:00.0000000 +00:00 | 2026-10-28 12:00:00.0000000 +00:00 |
| `CASH_DISC_DATE` | STRING | 1 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `AMOUNT_MST` | STRING | 118 | 0 | -10000 | -8950 |
| `ACCOUNT_NUM` | STRING | 110 | 0 | 100-000001 | 100-000115 |
| `TRANS_DATE` | STRING | 68 | 0 | 2025-02-16 12:00:00.0000000 +00:00 | 2026-10-18 12:00:00.0000000 +00:00 |
| `CASH_DISC_AMOUNT_CUR` | STRING | 1 | 0 | 0 | 0 |
| `CASH_DISC_CALCULATION_DATE` | STRING | 1 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | kpmg_vendpaymentbivendtransopen__2026... | kpmg_vendpaymentbivendtransopen__2026... |
| `HASH_KEY` | STRING | 115 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:43:23.517000 | 2026-11-16 11:43:23.517000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:43:23.517000 | 2026-11-16 11:43:23.517000 |

## Sample rows

| REF_REC_ID | INVOICE | AMOUNT_CUR | DUE_DATE | CASH_DISC_DATE | AMOUNT_MST | ACCOUNT_NUM | TRANS_DATE | CASH_DISC_AMOUNT_CUR | CASH_DISC_CALCULATION_DATE | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5637167077 | Inv-002 | -2100 | 2026-10-28 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 | -2100 | 100-000062 | 2026-10-18 12:00:00.0000000 +00:00 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | kpmg_vendpaymentbivendtransopen__2026... | <masked> | 2026-11-16 11:43:23.517000 | <masked> | 2026-11-16 11:43:23.517000 |
| 5637167078 | Inv-003 | -2200 | 2025-01-18 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 | -2200 | 100-000063 | 2026-10-18 12:00:00.0000000 +00:00 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | kpmg_vendpaymentbivendtransopen__2026... | <masked> | 2026-11-16 11:43:23.517000 | <masked> | 2026-11-16 11:43:23.517000 |
| 5637167079 | Inv-004 | -2300 | 2025-01-24 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 | -2300 | 100-000064 | 2026-10-18 12:00:00.0000000 +00:00 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | kpmg_vendpaymentbivendtransopen__2026... | <masked> | 2026-11-16 11:43:23.517000 | <masked> | 2026-11-16 11:43:23.517000 |
| 5637167080 | Inv-005 | -2400 | 2025-01-26 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 | -2400 | 100-000065 | 2026-10-18 12:00:00.0000000 +00:00 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | kpmg_vendpaymentbivendtransopen__2026... | <masked> | 2026-11-16 11:43:23.517000 | <masked> | 2026-11-16 11:43:23.517000 |
| 5637167082 | Inv-006 | -2500 | 2025-02-28 12:00:00.0000000 +00:00 | 1900-01-01 12:00:00.0000000 +00:00 | -2500 | 100-000066 | 2026-10-18 12:00:00.0000000 +00:00 | 0 | 1900-01-01 12:00:00.0000000 +00:00 | kpmg_vendpaymentbivendtransopen__2026... | <masked> | 2026-11-16 11:43:23.517000 | <masked> | 2026-11-16 11:43:23.517000 |
