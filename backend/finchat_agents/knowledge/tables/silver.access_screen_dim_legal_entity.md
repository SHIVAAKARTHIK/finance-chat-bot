---
name: access_screen_dim_legal_entity
schema: silver
layer: silver
domain: null
type: table
status: active
purpose: Master list of legal entities used in the access review.
grain: one row per legal_entity_id (one legal entity)
primary_key:
- legal_entity_id
entity_column: legal_entity_id
period_columns: []
pii_columns: []
synonyms: []
built_from: []
known_issues: []
proposed_fields:
- grain
reviewed: false
---

# access_screen_dim_legal_entity

Access screen: legal entity master.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `legal_entity_id` | long |  |  | `legal_entity_id` |
| `legal_entity_code` | string |  |  | `legal_entity_code` |
| `legal_entity_name` | string |  |  | `legal_entity_name` |
| `created_at` | timestamp |  |  | `created_at` |

## Values

**created_at**
- `2026-11-18 15:44:43.735301+00:00`
