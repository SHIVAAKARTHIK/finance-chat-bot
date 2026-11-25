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
row_count: 3
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
- `CUEC-03`: 1 rows
- `CUEC-04`: 1 rows
- `CUEC-05`: 1 rows

**Requirement**
- `Role based access log`: 1 rows
- `Reconcile source data loaded to Digital Finance`: 1 rows
- `Review exception reports and follow up`: 1 rows

**Action**
- `https://app.powerbi.com/view?r=eyJrIjoiZGY4Mjc2YWEtNWI2Yy00NTZlLThkMWMtOWQ5MGJlZjJmODA2IiwidCI6ImM4N2I4OWJhLTU0ZTItND...`: 1 rows
- `https://app.powerbi.com/view?r=eyJrIjoiMjAzNjE2MzItMTY5OS00NTY0LTk5MDctM2RlNmZjOWJiZWU0IiwidCI6ImM4N2I4OWJhLTU0ZTItND...`: 1 rows
- `https://app.powerbi.com/view?r=eyJrIjoiYjlmODQ0YTQtOWVjOS00OWFjLTk3NjctZmE0Y2IxN2Y1NmU4IiwidCI6ImM4N2I4OWJhLTU0ZTItND...`: 1 rows

**source_file_name**
- `controls.csv`: 3 rows

**MDP_CREATED_DATE**
- `2026-11-04 10:51:29.512959+00:00`: 3 rows

**MDP_MODIFIED_DATE**
- `2026-11-04 10:51:29.512959+00:00`: 3 rows

## Profile

Rows in the latest export: 3.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `Ref` | STRING | 3 | 0 | CUEC-03 | CUEC-05 |
| `Requirement` | STRING | 3 | 0 | Reconcile source data loaded to Digit... | Role based access log |
| `Owner` | STRING | 2 | 0 |  |  |
| `Action` | STRING | 3 | 0 | https://app.powerbi.com/view?r=eyJrIj... | https://app.powerbi.com/view?r=eyJrIj... |
| `source_file_name` | STRING | 1 | 0 | controls.csv | controls.csv |
| `HASH_KEY` | STRING | 3 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-04 10:51:29.513000 | 2026-11-04 10:51:29.513000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-04 10:51:29.513000 | 2026-11-04 10:51:29.513000 |

## Sample rows

| Ref | Requirement | Owner | Action | source_file_name | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|
| CUEC-03 | Role based access log | <masked> | https://app.powerbi.com/view?r=eyJrIj... | controls.csv | <masked> | 2026-11-04 10:51:29.513000 | <masked> | 2026-11-04 10:51:29.513000 |
| CUEC-05 | Review exception reports and follow up | <masked> | https://app.powerbi.com/view?r=eyJrIj... | controls.csv | <masked> | 2026-11-04 10:51:29.513000 | <masked> | 2026-11-04 10:51:29.513000 |
| CUEC-04 | Reconcile source data loaded to Digit... | <masked> | https://app.powerbi.com/view?r=eyJrIj... | controls.csv | <masked> | 2026-11-04 10:51:29.513000 | <masked> | 2026-11-04 10:51:29.513000 |
