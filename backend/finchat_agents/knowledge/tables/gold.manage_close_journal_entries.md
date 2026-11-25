---
name: manage_close_journal_entries
schema: gold
layer: gold
domain: gl
type: view
status: active
purpose: Lists manual and automated journal entries with amounts; dates and posting status.
grain: one row per journal entry
primary_key:
- LEGAL_ENTITY
- JOURNAL_ID
- DATE
entity_column: LEGAL_ENTITY
period_columns:
- DATE
pii_columns: []
synonyms: []
built_from:
- fact_ledger_journal_headers
- fact_ledger_journal_lines
- fact_ledger_journal_trans_bi_entities
known_issues: []
row_count: 2196
proposed_fields: []
reviewed: false
---

# manage_close_journal_entries

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `JOURNAL_ID` | string |  |  | `JOURNAL_ID` |
| `TYPE` | string |  |  | `TYPE` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `DESCRIPTION` | string |  |  | `DESCRIPTION` |
| `AMOUNT` | decimal |  |  | `AMOUNT` |
| `DATE` | date |  |  | `DATE` |
| `STATUS` | string |  |  | `STATUS` |

## Values

**TYPE**
- `Manual`: 2078 rows
- `Automated`: 118 rows

**STATUS**
- `Yes`: 1449 rows
- `Not Posted`: 747 rows

## Profile

Rows in the latest export: 2196.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `JOURNAL_ID` | STRING | 146 | 0 | 100-000001 | UK17-000016 |
| `TYPE` | STRING | 2 | 0 | Automated | Manual |
| `LEGAL_ENTITY` | STRING | 16 | 0 |  |  |
| `DESCRIPTION` | STRING | 70 | 0 | 201-2025 transactions | in_01a1aa807abb7c30803c92551e5884c5 |
| `AMOUNT` | DECIMAL | 2105 | 15 | 0 | 15594589302.56 |
| `DATE` | DATE | 459 | 15 | 2024-12-31 00:00:00 | 2026-11-16 00:00:00 |
| `STATUS` | STRING | 2 | 0 | Not Posted | Yes |

## Sample rows

| JOURNAL_ID | TYPE | DESCRIPTION | AMOUNT | DATE | STATUS |
|---|---|---|---|---|---|
| 214-000012 | Manual | 214-2026 transactions | 51281.26 | 2026-01-02 00:00:00 | Yes |
| 214-000012 | Manual | 214-2026 transactions | 89055 | 2026-01-05 00:00:00 | Yes |
| 214-000012 | Manual | 214-2026 transactions | 84154.92 | 2026-01-14 00:00:00 | Yes |
| 214-000012 | Manual | 214-2026 transactions | 160640.62 | 2026-01-20 00:00:00 | Yes |
| 214-000012 | Manual | 214-2026 transactions | 48495.42 | 2026-01-21 00:00:00 | Yes |
