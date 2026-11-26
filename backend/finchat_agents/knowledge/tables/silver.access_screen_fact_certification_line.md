---
name: access_screen_fact_certification_line
schema: silver
layer: silver
domain: null
type: table
status: active
purpose: Links each manager certification to the access rows it covered.
grain: one row per certification_line_id (one access row covered by one certification)
primary_key:
- certification_line_id
entity_column: null
period_columns: []
pii_columns: []
synonyms: []
built_from: []
known_issues:
- code: empty_column
  note: table is empty (0 rows)
proposed_fields:
- grain
reviewed: false
---

# access_screen_fact_certification_line

Access screen: access rows covered by each certification (append-only).

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `certification_line_id` | long |  |  | `certification_line_id` |
| `certification_id` | long |  |  | `certification_id` |
| `access_id` | long |  |  | `access_id` |
| `created_at` | timestamp |  |  | `created_at` |

## Empty columns

Empty in every row: `certification_line_id`, `certification_id`, `access_id`, `created_at`. Do not filter or group on them.
