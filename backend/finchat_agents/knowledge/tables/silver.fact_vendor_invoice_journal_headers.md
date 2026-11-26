---
name: fact_vendor_invoice_journal_headers
schema: silver
layer: silver
domain: ap
type: table
status: active
purpose: Header of each vendor invoice journal batch.
grain: one row per HASH_KEY (one vendor invoice journal batch)
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

# fact_vendor_invoice_journal_headers

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `DATA_AREA_ID` | string |  |  | `DATA_AREA_ID` |
| `JOURNAL_BATCH_NUMBER` | string |  |  | `JOURNAL_BATCH_NUMBER` |
| `JOURNAL_NAME` | string |  |  | `JOURNAL_NAME` |
| `OVERRIDE_SALES_TAX` | string |  |  | `OVERRIDE_SALES_TAX` |
| `DESCRIPTION` | string |  |  | `DESCRIPTION` |
| `TAX_OBLIGATION_COMPANY` | string |  |  | `TAX_OBLIGATION_COMPANY` |
| `IS_POSTED` | string |  |  | `IS_POSTED` |
| `SALES_TAX_INCLUDED` | string |  |  | `SALES_TAX_INCLUDED` |
| `JOURNAL_TOTAL_CREDIT` | string |  |  | `JOURNAL_TOTAL_CREDIT` |
| `JOURNAL_TOTAL_DEBIT` | string |  |  | `JOURNAL_TOTAL_DEBIT` |
| `WORKFLOW_APPROVAL_STATUS` | string |  |  | `WORKFLOW_APPROVAL_STATUS` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**JOURNAL_NAME**
- `VIJ`

**OVERRIDE_SALES_TAX**
- `No`

**DESCRIPTION**
- `Vendor invoice journal`

**IS_POSTED**
- `Yes`
- `No`

**SALES_TAX_INCLUDED**
- `No`

**WORKFLOW_APPROVAL_STATUS**
- `Approved`
- `NotSubmitted`
- `Rejected`
- `PendingApproval`

**SOURCE_FILE_NAME**
- `vendinvoicejournalheaders__20261116_105417.csv`

**MDP_CREATED_DATE**
- `2026-11-16 11:41:51.305364+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 11:41:51.305364+00:00`
