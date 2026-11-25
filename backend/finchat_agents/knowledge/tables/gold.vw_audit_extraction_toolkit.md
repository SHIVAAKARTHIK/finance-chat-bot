---
name: vw_audit_extraction_toolkit
schema: gold
layer: gold
domain: null
type: view
status: active
purpose: Lists audit extracts; source systems; formats and links.
grain: one row per HASH_KEY (one audit extract option)
primary_key:
- HASH_KEY
entity_column: null
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from:
- audit_extraction_toolkit
known_issues: []
row_count: 1
proposed_fields:
- grain
- primary_key
reviewed: false
---

# vw_audit_extraction_toolkit

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `Extract` | string |  |  | `Extract` |
| `Source_system` | string |  |  | `Source_system` |
| `Format` | string |  |  | `Format` |
| `Action` | string |  |  | `Action` |
| `source_file_name` | string |  |  | `source_file_name` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**Extract**
- `Subledger Detail`: 1 rows

**Source_system**
- `Fynapse`: 1 rows

**Format**
- `CSV`: 1 rows

**Action**
- `https://web-use-journalviewer-dev.azurewebsites.net/home`: 1 rows

**source_file_name**
- `audit_extraction_toolkit.csv`: 1 rows

**MDP_CREATED_DATE**
- `2026-11-04 10:50:56.004614+00:00`: 1 rows

**MDP_MODIFIED_DATE**
- `2026-11-04 10:50:56.004614+00:00`: 1 rows

## Profile

Rows in the latest export: 1.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `Extract` | STRING | 1 | 0 | Subledger Detail | Subledger Detail |
| `Source_system` | STRING | 1 | 0 | Fynapse | Fynapse |
| `Format` | STRING | 1 | 0 | CSV | CSV |
| `Action` | STRING | 1 | 0 | https://web-use-journalviewer-dev.azu... | https://web-use-journalviewer-dev.azu... |
| `source_file_name` | STRING | 1 | 0 | audit_extraction_toolkit.csv | audit_extraction_toolkit.csv |
| `HASH_KEY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-04 10:50:56.005000 | 2026-11-04 10:50:56.005000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-04 10:50:56.005000 | 2026-11-04 10:50:56.005000 |

## Sample rows

| Extract | Source_system | Format | Action | source_file_name | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|
| Subledger Detail | Fynapse | CSV | https://web-use-journalviewer-dev.azu... | audit_extraction_toolkit.csv | <masked> | 2026-11-04 10:50:56.005000 | <masked> | 2026-11-04 10:50:56.005000 |
