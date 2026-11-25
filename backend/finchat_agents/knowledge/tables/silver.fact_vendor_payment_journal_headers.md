---
name: fact_vendor_payment_journal_headers
schema: silver
layer: silver
domain: ap
type: table
status: active
purpose: Header of each vendor payment journal batch.
grain: one row per HASH_KEY (one vendor payment journal batch)
primary_key:
- HASH_KEY
entity_column: DATA_AREA_ID
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues: []
row_count: 7
proposed_fields:
- grain
- primary_key
reviewed: false
---

# fact_vendor_payment_journal_headers

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `DATA_AREA_ID` | string |  |  | `DATA_AREA_ID` |
| `JOURNAL_BATCH_NUMBER` | string |  |  | `JOURNAL_BATCH_NUMBER` |
| `JOURNAL_NAME` | string |  |  | `JOURNAL_NAME` |
| `CHARGE_BEARER` | string |  |  | `CHARGE_BEARER` |
| `OVERRIDE_SALES_TAX` | string |  |  | `OVERRIDE_SALES_TAX` |
| `DESCRIPTION` | string |  |  | `DESCRIPTION` |
| `CATEGORY_PURPOSE` | string |  |  | `CATEGORY_PURPOSE` |
| `IS_POSTED` | string |  |  | `IS_POSTED` |
| `LOCAL_INSTRUMENT` | string |  |  | `LOCAL_INSTRUMENT` |
| `SERVICE_LEVEL` | string |  |  | `SERVICE_LEVEL` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**JOURNAL_BATCH_NUMBER**
- `100-000126`: 1 rows
- `100-000125`: 1 rows
- `100-000124`: 1 rows
- `100-000121`: 1 rows
- `100-000220`: 1 rows
- `100-000221`: 1 rows
- `100-000243`: 1 rows

**JOURNAL_NAME**
- `VPJ`: 7 rows

**CHARGE_BEARER**
- `0`: 7 rows

**OVERRIDE_SALES_TAX**
- `No`: 7 rows

**DESCRIPTION**
- `Vendor payment journal`: 5 rows
- `Test 001 10/20/2026`: 1 rows
- `Test 002 10/20/2026`: 1 rows

**CATEGORY_PURPOSE**
- `0`: 7 rows

**IS_POSTED**
- `Yes`: 5 rows
- `No`: 2 rows

**LOCAL_INSTRUMENT**
- `0`: 7 rows

**SERVICE_LEVEL**
- `0`: 7 rows

**SOURCE_FILE_NAME**
- `vendorpaymentjournalheaders__20261116_105417.csv`: 7 rows

**MDP_CREATED_DATE**
- `2026-11-16 11:41:47.820632+00:00`: 7 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 11:41:47.820632+00:00`: 7 rows

## Profile

Rows in the latest export: 7.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `DATA_AREA_ID` | STRING | 1 | 0 |  |  |
| `JOURNAL_BATCH_NUMBER` | STRING | 7 | 0 | 100-000121 | 100-000243 |
| `JOURNAL_NAME` | STRING | 1 | 0 | VPJ | VPJ |
| `CHARGE_BEARER` | STRING | 1 | 0 | 0 | 0 |
| `OVERRIDE_SALES_TAX` | STRING | 1 | 0 | No | No |
| `DESCRIPTION` | STRING | 3 | 0 | Test 001 10/20/2026 | Vendor payment journal |
| `CATEGORY_PURPOSE` | STRING | 1 | 0 | 0 | 0 |
| `IS_POSTED` | STRING | 2 | 0 | No | Yes |
| `LOCAL_INSTRUMENT` | STRING | 1 | 0 | 0 | 0 |
| `SERVICE_LEVEL` | STRING | 1 | 0 | 0 | 0 |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | vendorpaymentjournalheaders__20261116... | vendorpaymentjournalheaders__20261116... |
| `HASH_KEY` | STRING | 7 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:41:47.821000 | 2026-11-16 11:41:47.821000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:41:47.821000 | 2026-11-16 11:41:47.821000 |

## Sample rows

| JOURNAL_BATCH_NUMBER | JOURNAL_NAME | CHARGE_BEARER | OVERRIDE_SALES_TAX | DESCRIPTION | CATEGORY_PURPOSE | IS_POSTED | LOCAL_INSTRUMENT | SERVICE_LEVEL | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 100-000121 | VPJ | 0 | No | Vendor payment journal | 0 | Yes | 0 | 0 | vendorpaymentjournalheaders__20261116... | <masked> | 2026-11-16 11:41:47.821000 | <masked> | 2026-11-16 11:41:47.821000 |
| 100-000124 | VPJ | 0 | No | Test 001 10/20/2026 | 0 | Yes | 0 | 0 | vendorpaymentjournalheaders__20261116... | <masked> | 2026-11-16 11:41:47.821000 | <masked> | 2026-11-16 11:41:47.821000 |
| 100-000125 | VPJ | 0 | No | Test 002 10/20/2026 | 0 | Yes | 0 | 0 | vendorpaymentjournalheaders__20261116... | <masked> | 2026-11-16 11:41:47.821000 | <masked> | 2026-11-16 11:41:47.821000 |
| 100-000126 | VPJ | 0 | No | Vendor payment journal | 0 | No | 0 | 0 | vendorpaymentjournalheaders__20261116... | <masked> | 2026-11-16 11:41:47.821000 | <masked> | 2026-11-16 11:41:47.821000 |
| 100-000220 | VPJ | 0 | No | Vendor payment journal | 0 | Yes | 0 | 0 | vendorpaymentjournalheaders__20261116... | <masked> | 2026-11-16 11:41:47.821000 | <masked> | 2026-11-16 11:41:47.821000 |
