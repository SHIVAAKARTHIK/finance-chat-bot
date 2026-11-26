---
name: access_screen_fact_certification
schema: silver
layer: silver
domain: null
type: table
status: active
purpose: Monthly certification by a manager that their reportees' access was reviewed.
grain: one row per certification_id (one manager certification for a month)
primary_key:
- certification_id
entity_column: null
period_columns:
- certification_month
- certified_timestamp
pii_columns:
- manager_email
- certified_by_login
synonyms: []
built_from: []
known_issues:
- code: empty_column
  note: table is empty (0 rows)
proposed_fields:
- grain
reviewed: false
---

# access_screen_fact_certification

Access screen: monthly manager certifications (append-only).

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `certification_id` | long |  |  | `certification_id` |
| `manager_email` | string |  |  | `manager_email` |
| `certification_month` | date |  |  | `certification_month` |
| `certified_timestamp` | timestamp |  |  | `certified_timestamp` |
| `certified_by_login` | string |  |  | `certified_by_login` |
| `created_at` | timestamp |  |  | `created_at` |

## Empty columns

Empty in every row: `certification_id`, `manager_email`, `certification_month`, `certified_timestamp`, `certified_by_login`, `created_at`. Do not filter or group on them.
