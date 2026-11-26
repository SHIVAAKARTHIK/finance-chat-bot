---
name: review_controls
schema: silver
layer: silver
domain: null
type: table
status: active
purpose: List of review controls (reference; requirement; owner; report link).
grain: one row per HASH_KEY (one control)
primary_key:
- HASH_KEY
entity_column: null
period_columns: []
pii_columns:
- Owner
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

# review_controls

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `Ref` | string |  |  | `Ref` |
| `Requirement` | string |  |  | `Requirement` |
| `Owner` | string |  |  | `Owner` |
| `Action` | string |  |  | `Action` |
| `source_file_name` | string |  |  | `source_file_name` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**Ref**
- `CUEC-03`
- `CUEC-04`
- `CUEC-05`

**Requirement**
- `Role based access log`
- `Reconcile source data loaded to Digital Finance`
- `Review exception reports and follow up`

**Action**
- `https://app.powerbi.com/view?r=eyJrIjoiZGY4Mjc2YWEtNWI2Yy00NTZlLThkMWMtOWQ5MGJlZjJmODA2IiwidCI6ImM4N2I4OWJhLTU0ZTItND...`
- `https://app.powerbi.com/view?r=eyJrIjoiMjAzNjE2MzItMTY5OS00NTY0LTk5MDctM2RlNmZjOWJiZWU0IiwidCI6ImM4N2I4OWJhLTU0ZTItND...`
- `https://app.powerbi.com/view?r=eyJrIjoiYjlmODQ0YTQtOWVjOS00OWFjLTk3NjctZmE0Y2IxN2Y1NmU4IiwidCI6ImM4N2I4OWJhLTU0ZTItND...`

**source_file_name**
- `controls.csv`

**MDP_CREATED_DATE**
- `2026-11-04 10:51:29.512959+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-04 10:51:29.512959+00:00`
