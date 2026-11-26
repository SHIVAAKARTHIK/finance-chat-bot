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
- `100-000126`
- `100-000125`
- `100-000124`
- `100-000121`
- `100-000220`
- `100-000221`
- `100-000243`

**JOURNAL_NAME**
- `VPJ`

**CHARGE_BEARER**
- `0`

**OVERRIDE_SALES_TAX**
- `No`

**DESCRIPTION**
- `Vendor payment journal`
- `Test 001 10/20/2026`
- `Test 002 10/20/2026`

**CATEGORY_PURPOSE**
- `0`

**IS_POSTED**
- `Yes`
- `No`

**LOCAL_INSTRUMENT**
- `0`

**SERVICE_LEVEL**
- `0`

**SOURCE_FILE_NAME**
- `vendorpaymentjournalheaders__20261116_105417.csv`

**MDP_CREATED_DATE**
- `2026-11-16 11:41:47.820632+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 11:41:47.820632+00:00`
