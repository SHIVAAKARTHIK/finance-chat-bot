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
- `5`
- `6`
- `9`
- `3`
- `2`
- `11`
- `1`
- `8`
- `7`
- `4`
- `10`

**application_id**
- `1`
- `3`
- `2`
- `4`

**source_role_id**
- `None`
- `D365-NA`
- `UI-USER`
- `D365-AP`
- `D365-RW`
- `PBI-VIEW`
- `UI-ADMIN`
- `PBI-ADMIN`
- `D365-R01`
- `PBI-CONTRIB`

**source_role_name**
- `Admin`
- `Approver`
- `Read`
- `Read / Write`
- `User`
- `Contributor`
- `No Access`
- `Viewer`

**role_description**
- `None`
- `Approve invoices`
- `Standard UI user`
- `Read and post AP data`
- `Edit and publish reports`
- `Read-only AP data`
- `View reports`
- `No access granted`
- `UI administrator`
- `Workspace admin`

**created_at**
- `2026-11-18 15:44:45.729642+00:00`
