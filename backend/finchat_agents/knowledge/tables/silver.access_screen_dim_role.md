---
name: access_screen_dim_role
schema: silver
layer: silver
domain: null
type: table
status: active
purpose: Access types (roles) available per application in the access review.
grain: one row per role_id (one role of one application)
primary_key:
- role_id
entity_column: null
period_columns: []
pii_columns: []
synonyms: []
built_from: []
known_issues: []
row_count: 11
proposed_fields:
- grain
reviewed: false
---

# access_screen_dim_role

Access screen: access types (roles) per application.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `role_id` | long |  |  | `role_id` |
| `application_id` | int |  |  | `application_id` |
| `source_role_id` | string |  |  | `source_role_id` |
| `source_role_name` | string |  |  | `source_role_name` |
| `role_description` | string |  |  | `role_description` |
| `created_at` | timestamp |  |  | `created_at` |

## Values

**role_id**
- `5`: 1 rows
- `6`: 1 rows
- `9`: 1 rows
- `3`: 1 rows
- `2`: 1 rows
- `11`: 1 rows
- `1`: 1 rows
- `8`: 1 rows
- `7`: 1 rows
- `4`: 1 rows
- `10`: 1 rows

**application_id**
- `1`: 4 rows
- `3`: 3 rows
- `2`: 2 rows
- `4`: 2 rows

**source_role_id**
- `None`: 2 rows
- `D365-NA`: 1 rows
- `UI-USER`: 1 rows
- `D365-AP`: 1 rows
- `D365-RW`: 1 rows
- `PBI-VIEW`: 1 rows
- `UI-ADMIN`: 1 rows
- `PBI-ADMIN`: 1 rows
- `D365-R01`: 1 rows
- `PBI-CONTRIB`: 1 rows

**source_role_name**
- `Admin`: 3 rows
- `Approver`: 2 rows
- `Read`: 1 rows
- `Read / Write`: 1 rows
- `User`: 1 rows
- `Contributor`: 1 rows
- `No Access`: 1 rows
- `Viewer`: 1 rows

**role_description**
- `None`: 2 rows
- `Approve invoices`: 1 rows
- `Standard UI user`: 1 rows
- `Read and post AP data`: 1 rows
- `Edit and publish reports`: 1 rows
- `Read-only AP data`: 1 rows
- `View reports`: 1 rows
- `No access granted`: 1 rows
- `UI administrator`: 1 rows
- `Workspace admin`: 1 rows

**created_at**
- `2026-11-18 15:44:45.729642+00:00`: 11 rows

## Profile

Rows in the latest export: 11.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `role_id` | LONG | 11 | 0 | 1 | 11 |
| `application_id` | INT | 4 | 0 | 1 | 4 |
| `source_role_id` | STRING | 9 | 2 | D365-AP | UI-USER |
| `source_role_name` | STRING | 8 | 0 | Admin | Viewer |
| `role_description` | STRING | 9 | 2 | Approve invoices | Workspace admin |
| `created_at` | TIMESTAMP | 1 | 0 | 2026-11-18 15:44:45.730000 | 2026-11-18 15:44:45.730000 |

## Sample rows

| role_id | application_id | source_role_id | source_role_name | role_description | created_at |
|---|---|---|---|---|---|
| 1 | 1 | D365-R01 | Read | Read-only AP data | 2026-11-18 15:44:45.730000 |
| 2 | 1 | D365-RW | Read / Write | Read and post AP data | 2026-11-18 15:44:45.730000 |
| 3 | 1 | D365-NA | No Access | No access granted | 2026-11-18 15:44:45.730000 |
| 4 | 1 | D365-AP | Approver | Approve invoices | 2026-11-18 15:44:45.730000 |
| 5 | 3 | PBI-CONTRIB | Contributor | Edit and publish reports | 2026-11-18 15:44:45.730000 |
