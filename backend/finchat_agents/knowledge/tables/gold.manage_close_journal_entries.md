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
- `Manual`
- `Automated`

**STATUS**
- `Yes`
- `Not Posted`
