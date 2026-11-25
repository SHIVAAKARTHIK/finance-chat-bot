---
name: access_screen_rel_manager_reportee
schema: silver
layer: silver
domain: null
type: table
status: active
purpose: Maps each manager to their reportees for access certification.
grain: one row per relationship_id (one manager-reportee link)
primary_key:
- relationship_id
entity_column: null
period_columns:
- effective_from
- effective_to
pii_columns:
- manager_email
- reportee_email
synonyms: []
built_from: []
known_issues:
- code: empty_column
  note: effective_to is null on all rows (all current)
row_count: 13
proposed_fields:
- grain
reviewed: false
---

# access_screen_rel_manager_reportee

Access screen: manager -> reportee link (email), SCD2.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `relationship_id` | long |  |  | `relationship_id` |
| `manager_email` | string |  |  | `manager_email` |
| `reportee_email` | string |  |  | `reportee_email` |
| `effective_from` | timestamp |  |  | `effective_from` |
| `effective_to` | timestamp |  |  | `effective_to` |
| `source_batch_id` | string |  |  | `source_batch_id` |
| `created_at` | timestamp |  |  | `created_at` |
| `updated_at` | timestamp |  |  | `updated_at` |

## Values

**relationship_id**
- `17`: 1 rows
- `5`: 1 rows
- `3`: 1 rows
- `6`: 1 rows
- `4`: 1 rows
- `12`: 1 rows
- `15`: 1 rows
- `13`: 1 rows
- `1`: 1 rows
- `2`: 1 rows
- `8`: 1 rows
- `7`: 1 rows
- `10`: 1 rows

**effective_from**
- `2025-11-01 09:00:00+00:00`: 13 rows

**effective_to**
- `None`: 13 rows

**source_batch_id**
- `BATCH-20251101-01`: 13 rows

**created_at**
- `2026-11-18 15:44:47.999243+00:00`: 7 rows
- `2026-11-20 06:14:38.815602+00:00`: 3 rows
- `2026-11-19 11:02:17.233564+00:00`: 3 rows

**updated_at**
- `2026-11-18 15:44:47.999243+00:00`: 7 rows
- `2026-11-20 06:14:38.815602+00:00`: 3 rows
- `2026-11-19 11:02:17.233564+00:00`: 3 rows

## Profile

Rows in the latest export: 13.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `relationship_id` | LONG | 13 | 0 | 1 | 17 |
| `manager_email` | STRING | 5 | 0 |  |  |
| `reportee_email` | STRING | 12 | 0 |  |  |
| `effective_from` | TIMESTAMP | 1 | 0 | 2025-11-01 09:00:00 | 2025-11-01 09:00:00 |
| `effective_to` | TIMESTAMP | 0 | 13 |  |  |
| `source_batch_id` | STRING | 1 | 0 | BATCH-20251101-01 | BATCH-20251101-01 |
| `created_at` | TIMESTAMP | 3 | 0 | 2026-11-18 15:44:47.999000 | 2026-11-20 06:14:38.816000 |
| `updated_at` | TIMESTAMP | 3 | 0 | 2026-11-18 15:44:47.999000 | 2026-11-20 06:14:38.816000 |

## Sample rows

| relationship_id | manager_email | reportee_email | effective_from | effective_to | source_batch_id | created_at | updated_at |
|---|---|---|---|---|---|---|---|
| 1 | <masked> | <masked> | 2025-11-01 09:00:00 | NULL | BATCH-20251101-01 | 2026-11-18 15:44:47.999000 | 2026-11-18 15:44:47.999000 |
| 2 | <masked> | <masked> | 2025-11-01 09:00:00 | NULL | BATCH-20251101-01 | 2026-11-18 15:44:47.999000 | 2026-11-18 15:44:47.999000 |
| 3 | <masked> | <masked> | 2025-11-01 09:00:00 | NULL | BATCH-20251101-01 | 2026-11-18 15:44:47.999000 | 2026-11-18 15:44:47.999000 |
| 4 | <masked> | <masked> | 2025-11-01 09:00:00 | NULL | BATCH-20251101-01 | 2026-11-18 15:44:47.999000 | 2026-11-18 15:44:47.999000 |
| 5 | <masked> | <masked> | 2025-11-01 09:00:00 | NULL | BATCH-20251101-01 | 2026-11-18 15:44:47.999000 | 2026-11-18 15:44:47.999000 |
