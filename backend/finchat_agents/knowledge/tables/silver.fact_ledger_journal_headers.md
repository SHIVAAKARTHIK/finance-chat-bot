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
row_count: 140
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
- `USD`: 101 rows
- `GBP`: 27 rows
- `EUR`: 12 rows

**JOURNAL_NAME**
- `GJV`: 86 rows
- `FYNAPSE`: 44 rows
- `GJV_S`: 7 rows
- `InterCom`: 2 rows
- `Intercom`: 1 rows

**POSTING_LAYER**
- `Current`: 134 rows
- `Operations`: 6 rows

**IS_POSTED**
- `Yes`: 109 rows
- `No`: 31 rows

**WORKFLOW_APPROVAL_STATUS**
- `None`: 123 rows
- `Approved`: 12 rows
- `PendingApproval`: 3 rows
- `NotSubmitted`: 2 rows

**SOURCE_FILE_NAME**
- `ledgerjournalheaders__20261116_105417.csv`: 140 rows

**MDP_CREATED_DATE**
- `2026-11-16 11:42:09.155715+00:00`: 140 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 11:42:09.155715+00:00`: 140 rows

## Profile

Rows in the latest export: 140.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `DATA_AREA_ID` | STRING | 16 | 0 |  |  |
| `JOURNAL_BATCH_NUMBER` | STRING | 146 | 0 | 100-000001 | UK17-000016 |
| `ACCOUNTING_CURRENCY` | STRING | 3 | 0 | EUR | USD |
| `JOURNAL_NAME` | STRING | 5 | 0 | FYNAPSE | Intercom |
| `INTEGRATION_KEY` | STRING | 0 | 140 |  |  |
| `DESCRIPTION` | STRING | 70 | 0 | 201-2025 transactions | in_01a1aa807abb7c30803c92551e5884c5 |
| `POSTING_LAYER` | STRING | 2 | 0 | Current | Operations |
| `IS_POSTED` | STRING | 2 | 0 | No | Yes |
| `JOURNAL_TOTAL_CREDIT` | STRING | 99 | 0 | 0 | 79516 |
| `JOURNAL_TOTAL_DEBIT` | STRING | 99 | 0 | 0 | 79516 |
| `WORKFLOW_APPROVAL_STATUS` | STRING | 4 | 0 | Approved | PendingApproval |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | ledgerjournalheaders__20261116_105417... | ledgerjournalheaders__20261116_105417... |
| `HASH_KEY` | STRING | 133 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:42:09.156000 | 2026-11-16 11:42:09.156000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:42:09.156000 | 2026-11-16 11:42:09.156000 |

## Sample rows

| JOURNAL_BATCH_NUMBER | ACCOUNTING_CURRENCY | JOURNAL_NAME | DESCRIPTION | POSTING_LAYER | IS_POSTED | JOURNAL_TOTAL_CREDIT | JOURNAL_TOTAL_DEBIT | WORKFLOW_APPROVAL_STATUS | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 100-000001 | USD | FYNAPSE | FYNAPSE | Current | Yes | 1655952 | 1655952 | None | ledgerjournalheaders__20261116_105417... | <masked> | 2026-11-16 11:42:09.156000 | <masked> | 2026-11-16 11:42:09.156000 |
| 100-000002 | USD | GJV | General Journal | Current | Yes | 395076872.53 | 395076872.53 | Approved | ledgerjournalheaders__20261116_105417... | <masked> | 2026-11-16 11:42:09.156000 | <masked> | 2026-11-16 11:42:09.156000 |
| 100-000134 | USD | GJV | Test Bank Transaction | Current | Yes | 51760 | 51760 | Approved | ledgerjournalheaders__20261116_105417... | <masked> | 2026-11-16 11:42:09.156000 | <masked> | 2026-11-16 11:42:09.156000 |
| 100-000171 | USD | GJV | Transaction - JAN 2 2025 | Current | Yes | 70379 | 70379 | None | ledgerjournalheaders__20261116_105417... | <masked> | 2026-11-16 11:42:09.156000 | <masked> | 2026-11-16 11:42:09.156000 |
| 100-000172 | USD | GJV | Transaction - JAN 3 2025 | Current | Yes | 54197 | 54197 | None | ledgerjournalheaders__20261116_105417... | <masked> | 2026-11-16 11:42:09.156000 | <masked> | 2026-11-16 11:42:09.156000 |
