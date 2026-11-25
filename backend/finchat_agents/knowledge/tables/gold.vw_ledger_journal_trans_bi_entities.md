---
name: vw_ledger_journal_trans_bi_entities
schema: gold
layer: gold
domain: gl
type: view
status: active
purpose: Shows intercompany elimination transactions and amounts by legal entity.
grain: one row per elimination transaction
primary_key:
- LEGAL_ENTITY
- Elimination ID
- Transaction Type
entity_column: LEGAL_ENTITY
period_columns: []
pii_columns: []
synonyms: []
built_from:
- fact_ledger_journal_trans_bi_entities
known_issues:
- code: duplicates
  note: 5 exact duplicate rows in the latest export (55.6%). Check duplicates at the grain before counting or summing; warn
    the user.
row_count: 9
proposed_fields: []
reviewed: false
---

# vw_ledger_journal_trans_bi_entities

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `Elimination ID` | string |  |  | `Elimination ID` |
| `Transaction Type` | string |  |  | `Transaction Type` |
| `Amount` | string |  |  | `Amount` |

## Values

**Elimination ID**
- `ELM-000000001`: 6 rows
- `103-000000001`: 3 rows

**Transaction Type**
- `Intercompany payable - Due to/from`: 4 rows
- `Intercompany payable - Due to / from`: 2 rows
- `Intercompany - Due to/from`: 2 rows
- `Intercompany - Due to / from`: 1 rows

**Amount**
- `576000`: 6 rows
- `341414.82`: 3 rows

## Profile

Rows in the latest export: 9.
Exact duplicate rows: 5.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `LEGAL_ENTITY` | STRING | 2 | 0 |  |  |
| `Elimination ID` | STRING | 2 | 0 | 103-000000001 | ELM-000000001 |
| `Transaction Type` | STRING | 4 | 0 | Intercompany - Due to / from | Intercompany payable - Due to/from |
| `Amount` | STRING | 2 | 0 | 341414.82 | 576000 |

## Sample rows

| Elimination ID | Transaction Type | Amount |
|---|---|---|
| 103-000000001 | Intercompany - Due to / from | 341414.82 |
| ELM-000000001 | Intercompany payable - Due to / from | 576000 |
| ELM-000000001 | Intercompany payable - Due to / from | 576000 |
| 103-000000001 | Intercompany - Due to/from | 341414.82 |
| ELM-000000001 | Intercompany payable - Due to/from | 576000 |
