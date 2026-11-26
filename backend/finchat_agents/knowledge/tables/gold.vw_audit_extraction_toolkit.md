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
- `Subledger Detail`

**Source_system**
- `Fynapse`

**Format**
- `CSV`

**Action**
- `https://web-use-journalviewer-dev.azurewebsites.net/home`

**source_file_name**
- `audit_extraction_toolkit.csv`

**MDP_CREATED_DATE**
- `2026-11-04 10:50:56.004614+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-04 10:50:56.004614+00:00`
