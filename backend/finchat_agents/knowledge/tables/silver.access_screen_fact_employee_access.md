---
name: access_screen_fact_employee_access
schema: silver
layer: silver
domain: null
type: table
status: active
purpose: Shows which access type each employee holds on which legal entity.
grain: one row per access_id (one employee-role-entity access grant)
primary_key:
- access_id
entity_column: legal_entity_id
period_columns:
- effective_from
- effective_to
pii_columns:
- employee_email
synonyms: []
built_from: []
known_issues:
- code: empty_column
  note: effective_to is null on all rows (all current)
proposed_fields:
- grain
reviewed: false
---

# access_screen_fact_employee_access

Access screen: who (email) has which access type on which legal entity, SCD2.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `access_id` | long |  |  | `access_id` |
| `employee_email` | string |  |  | `employee_email` |
| `legal_entity_id` | long |  |  | `legal_entity_id` |
| `role_id` | long |  |  | `role_id` |
| `effective_from` | timestamp |  |  | `effective_from` |
| `effective_to` | timestamp |  |  | `effective_to` |
| `source_batch_id` | string |  |  | `source_batch_id` |
| `created_at` | timestamp |  |  | `created_at` |
| `updated_at` | timestamp |  |  | `updated_at` |

## Values

**role_id**
- `8`
- `4`
- `1`
- `10`
- `11`
- `7`
- `6`
- `2`
- `5`
- `9`
- `3`

**effective_from**
- `2025-11-01 09:00:00+00:00`

**effective_to**
- `None`

**source_batch_id**
- `BATCH-20251101-01`

**created_at**
- `2026-11-18 15:44:51.589648+00:00`
- `2026-11-20 06:14:43.701720+00:00`
- `2026-11-19 11:02:23.608233+00:00`

**updated_at**
- `2026-11-18 15:44:51.589648+00:00`
- `2026-11-20 06:14:43.701720+00:00`
- `2026-11-19 11:02:23.608233+00:00`

## Empty columns

Empty in every row: `effective_to`. Do not filter or group on them.
