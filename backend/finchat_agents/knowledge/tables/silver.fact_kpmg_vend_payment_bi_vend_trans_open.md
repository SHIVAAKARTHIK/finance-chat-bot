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
- `1900-01-01 12:00:00.0000000 +00:00`

**CASH_DISC_AMOUNT_CUR**
- `0`

**CASH_DISC_CALCULATION_DATE**
- `1900-01-01 12:00:00.0000000 +00:00`

**SOURCE_FILE_NAME**
- `kpmg_vendpaymentbivendtransopen__20261116_105417.csv`

**MDP_CREATED_DATE**
- `2026-11-16 11:43:23.516910+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 11:43:23.516910+00:00`
