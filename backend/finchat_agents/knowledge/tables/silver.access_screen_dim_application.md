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
row_count: 4
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
- `1`: 1 rows
- `3`: 1 rows
- `2`: 1 rows
- `4`: 1 rows

**application_name**
- `D365`: 1 rows
- `Fynapse`: 1 rows
- `Power BI`: 1 rows
- `UI`: 1 rows

**source_system_code**
- `D365`: 1 rows
- `FYNAPSE`: 1 rows
- `UI`: 1 rows
- `POWERBI`: 1 rows

**created_at**
- `2026-11-18 15:44:35.503623+00:00`: 4 rows

## Profile

Rows in the latest export: 4.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `application_id` | INT | 4 | 0 | 1 | 4 |
| `application_name` | STRING | 4 | 0 | D365 | UI |
| `source_system_code` | STRING | 4 | 0 | D365 | UI |
| `created_at` | TIMESTAMP | 1 | 0 | 2026-11-18 15:44:35.504000 | 2026-11-18 15:44:35.504000 |

## Sample rows

| application_id | application_name | source_system_code | created_at |
|---|---|---|---|
| 1 | D365 | D365 | 2026-11-18 15:44:35.504000 |
| 2 | Fynapse | FYNAPSE | 2026-11-18 15:44:35.504000 |
| 3 | Power BI | POWERBI | 2026-11-18 15:44:35.504000 |
| 4 | UI | UI | 2026-11-18 15:44:35.504000 |
