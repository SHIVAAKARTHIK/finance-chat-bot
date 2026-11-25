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
row_count: 102
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
- `VIJ`: 102 rows

**OVERRIDE_SALES_TAX**
- `No`: 102 rows

**DESCRIPTION**
- `Vendor invoice journal`: 102 rows

**IS_POSTED**
- `Yes`: 66 rows
- `No`: 36 rows

**SALES_TAX_INCLUDED**
- `No`: 102 rows

**WORKFLOW_APPROVAL_STATUS**
- `Approved`: 69 rows
- `NotSubmitted`: 29 rows
- `Rejected`: 3 rows
- `PendingApproval`: 1 rows

**SOURCE_FILE_NAME**
- `vendinvoicejournalheaders__20261116_105417.csv`: 102 rows

**MDP_CREATED_DATE**
- `2026-11-16 11:41:51.305364+00:00`: 102 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 11:41:51.305364+00:00`: 102 rows

## Profile

Rows in the latest export: 102.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `DATA_AREA_ID` | STRING | 1 | 0 |  |  |
| `JOURNAL_BATCH_NUMBER` | STRING | 103 | 0 | 100-000018 | 100-000119 |
| `JOURNAL_NAME` | STRING | 1 | 0 | VIJ | VIJ |
| `OVERRIDE_SALES_TAX` | STRING | 1 | 0 | No | No |
| `DESCRIPTION` | STRING | 1 | 0 | Vendor invoice journal | Vendor invoice journal |
| `TAX_OBLIGATION_COMPANY` | STRING | 1 | 0 |  |  |
| `IS_POSTED` | STRING | 2 | 0 | No | Yes |
| `SALES_TAX_INCLUDED` | STRING | 1 | 0 | No | No |
| `JOURNAL_TOTAL_CREDIT` | STRING | 101 | 0 | 10050 | 9950 |
| `JOURNAL_TOTAL_DEBIT` | STRING | 101 | 0 | 10050 | 9950 |
| `WORKFLOW_APPROVAL_STATUS` | STRING | 4 | 0 | Approved | Rejected |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | vendinvoicejournalheaders__20261116_1... | vendinvoicejournalheaders__20261116_1... |
| `HASH_KEY` | STRING | 105 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:41:51.305000 | 2026-11-16 11:41:51.305000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:41:51.305000 | 2026-11-16 11:41:51.305000 |

## Sample rows

| JOURNAL_BATCH_NUMBER | JOURNAL_NAME | OVERRIDE_SALES_TAX | DESCRIPTION | IS_POSTED | SALES_TAX_INCLUDED | JOURNAL_TOTAL_CREDIT | JOURNAL_TOTAL_DEBIT | WORKFLOW_APPROVAL_STATUS | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 100-000018 | VIJ | No | Vendor invoice journal | Yes | No | 2450 | 2450 | Approved | vendinvoicejournalheaders__20261116_1... | <masked> | 2026-11-16 11:41:51.305000 | <masked> | 2026-11-16 11:41:51.305000 |
| 100-000019 | VIJ | No | Vendor invoice journal | Yes | No | 2550 | 2550 | Approved | vendinvoicejournalheaders__20261116_1... | <masked> | 2026-11-16 11:41:51.305000 | <masked> | 2026-11-16 11:41:51.305000 |
| 100-000020 | VIJ | No | Vendor invoice journal | Yes | No | 2650 | 2650 | Approved | vendinvoicejournalheaders__20261116_1... | <masked> | 2026-11-16 11:41:51.305000 | <masked> | 2026-11-16 11:41:51.305000 |
| 100-000021 | VIJ | No | Vendor invoice journal | Yes | No | 2750 | 2750 | Approved | vendinvoicejournalheaders__20261116_1... | <masked> | 2026-11-16 11:41:51.305000 | <masked> | 2026-11-16 11:41:51.305000 |
| 100-000022 | VIJ | No | Vendor invoice journal | Yes | No | 2850 | 2850 | Approved | vendinvoicejournalheaders__20261116_1... | <masked> | 2026-11-16 11:41:51.305000 | <masked> | 2026-11-16 11:41:51.305000 |
