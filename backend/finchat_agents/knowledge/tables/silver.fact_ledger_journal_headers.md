---
name: fact_ledger_journal_headers
schema: silver
layer: silver
domain: gl
type: table
status: active
purpose: Header of each D365 ledger journal batch (name; totals; posted; approval).
grain: one row per HASH_KEY (one journal batch)
primary_key:
- HASH_KEY
entity_column: DATA_AREA_ID
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues:
- code: empty_column
  note: INTEGRATION_KEY all null
proposed_fields:
- grain
- primary_key
reviewed: false
---

# fact_ledger_journal_headers

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `DATA_AREA_ID` | string |  |  | `DATA_AREA_ID` |
| `JOURNAL_BATCH_NUMBER` | string |  |  | `JOURNAL_BATCH_NUMBER` |
| `ACCOUNTING_CURRENCY` | string |  |  | `ACCOUNTING_CURRENCY` |
| `JOURNAL_NAME` | string |  |  | `JOURNAL_NAME` |
| `INTEGRATION_KEY` | string |  |  | `INTEGRATION_KEY` |
| `DESCRIPTION` | string |  |  | `DESCRIPTION` |
| `POSTING_LAYER` | string |  |  | `POSTING_LAYER` |
| `IS_POSTED` | string |  |  | `IS_POSTED` |
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

**ACCOUNTING_CURRENCY**
- `USD`
- `GBP`
- `EUR`

**JOURNAL_NAME**
- `GJV`
- `FYNAPSE`
- `GJV_S`
- `InterCom`
- `Intercom`

**POSTING_LAYER**
- `Current`
- `Operations`

**IS_POSTED**
- `Yes`
- `No`

**WORKFLOW_APPROVAL_STATUS**
- `None`
- `Approved`
- `PendingApproval`
- `NotSubmitted`

**SOURCE_FILE_NAME**
- `ledgerjournalheaders__20261116_105417.csv`

**MDP_CREATED_DATE**
- `2026-11-16 11:42:09.155715+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 11:42:09.155715+00:00`

## Empty columns

Empty in every row: `INTEGRATION_KEY`. Do not filter or group on them.
