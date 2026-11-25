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
row_count: 69
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
- `8`: 10 rows
- `4`: 10 rows
- `1`: 9 rows
- `10`: 8 rows
- `11`: 8 rows
- `7`: 7 rows
- `6`: 6 rows
- `2`: 4 rows
- `5`: 3 rows
- `9`: 2 rows
- `3`: 2 rows

**effective_from**
- `2025-11-01 09:00:00+00:00`: 69 rows

**effective_to**
- `None`: 69 rows

**source_batch_id**
- `BATCH-20251101-01`: 69 rows

**created_at**
- `2026-11-18 15:44:51.589648+00:00`: 40 rows
- `2026-11-20 06:14:43.701720+00:00`: 15 rows
- `2026-11-19 11:02:23.608233+00:00`: 14 rows

**updated_at**
- `2026-11-18 15:44:51.589648+00:00`: 40 rows
- `2026-11-20 06:14:43.701720+00:00`: 15 rows
- `2026-11-19 11:02:23.608233+00:00`: 14 rows

## Profile

Rows in the latest export: 69.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `access_id` | LONG | 72 | 0 | 1 | 96 |
| `employee_email` | STRING | 11 | 0 |  |  |
| `legal_entity_id` | LONG | 3 | 0 |  |  |
| `role_id` | LONG | 11 | 0 | 1 | 11 |
| `effective_from` | TIMESTAMP | 1 | 0 | 2025-11-01 09:00:00 | 2025-11-01 09:00:00 |
| `effective_to` | TIMESTAMP | 0 | 69 |  |  |
| `source_batch_id` | STRING | 1 | 0 | BATCH-20251101-01 | BATCH-20251101-01 |
| `created_at` | TIMESTAMP | 3 | 0 | 2026-11-18 15:44:51.590000 | 2026-11-20 06:14:43.702000 |
| `updated_at` | TIMESTAMP | 3 | 0 | 2026-11-18 15:44:51.590000 | 2026-11-20 06:14:43.702000 |

## Sample rows

| access_id | employee_email | role_id | effective_from | effective_to | source_batch_id | created_at | updated_at |
|---|---|---|---|---|---|---|---|
| 1 | <masked> | 3 | 2025-11-01 09:00:00 | NULL | BATCH-20251101-01 | 2026-11-18 15:44:51.590000 | 2026-11-18 15:44:51.590000 |
| 2 | <masked> | 4 | 2025-11-01 09:00:00 | NULL | BATCH-20251101-01 | 2026-11-18 15:44:51.590000 | 2026-11-18 15:44:51.590000 |
| 3 | <masked> | 8 | 2025-11-01 09:00:00 | NULL | BATCH-20251101-01 | 2026-11-18 15:44:51.590000 | 2026-11-18 15:44:51.590000 |
| 4 | <masked> | 4 | 2025-11-01 09:00:00 | NULL | BATCH-20251101-01 | 2026-11-18 15:44:51.590000 | 2026-11-18 15:44:51.590000 |
| 5 | <masked> | 2 | 2025-11-01 09:00:00 | NULL | BATCH-20251101-01 | 2026-11-18 15:44:51.590000 | 2026-11-18 15:44:51.590000 |
