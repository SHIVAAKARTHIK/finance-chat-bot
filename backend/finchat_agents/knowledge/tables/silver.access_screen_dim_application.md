---
name: access_screen_dim_application
schema: silver
layer: silver
domain: null
type: table
status: active
purpose: Lists the applications (D365; Fynapse; Power BI; UI) covered by the user access review.
grain: one row per application_id (one application in scope)
primary_key:
- application_id
entity_column: null
period_columns: []
pii_columns: []
synonyms: []
built_from: []
known_issues: []
proposed_fields:
- grain
reviewed: false
---

# access_screen_dim_application

Access screen: applications in scope.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `application_id` | int |  |  | `application_id` |
| `application_name` | string |  |  | `application_name` |
| `source_system_code` | string |  |  | `source_system_code` |
| `created_at` | timestamp |  |  | `created_at` |

## Values

**application_id**
- `1`
- `3`
- `2`
- `4`

**application_name**
- `D365`
- `Fynapse`
- `Power BI`
- `UI`

**source_system_code**
- `D365`
- `FYNAPSE`
- `UI`
- `POWERBI`

**created_at**
- `2026-11-18 15:44:35.503623+00:00`
