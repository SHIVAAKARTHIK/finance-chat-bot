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
- `17`
- `5`
- `3`
- `6`
- `4`
- `12`
- `15`
- `13`
- `1`
- `2`
- `8`
- `7`
- `10`

**effective_from**
- `2025-11-01 09:00:00+00:00`

**effective_to**
- `None`

**source_batch_id**
- `BATCH-20251101-01`

**created_at**
- `2026-11-18 15:44:47.999243+00:00`
- `2026-11-20 06:14:38.815602+00:00`
- `2026-11-19 11:02:17.233564+00:00`

**updated_at**
- `2026-11-18 15:44:47.999243+00:00`
- `2026-11-20 06:14:38.815602+00:00`
- `2026-11-19 11:02:17.233564+00:00`

## Empty columns

Empty in every row: `effective_to`. Do not filter or group on them.
