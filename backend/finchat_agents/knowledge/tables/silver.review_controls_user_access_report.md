---
name: review_controls_user_access_report
schema: silver
layer: silver
domain: null
type: table
status: active
purpose: Summary of each user's role and number of areas they can access or change.
grain: one row per HASH_KEY (one user)
primary_key:
- HASH_KEY
entity_column: null
period_columns: []
pii_columns:
- User
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues: []
row_count: 4
proposed_fields:
- grain
- primary_key
reviewed: false
---

# review_controls_user_access_report

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `User` | string |  |  | `User` |
| `Role` | string |  |  | `Role` |
| `Areas_with_access` | int |  |  | `Areas_with_access` |
| `Areas_they_can_change` | int |  |  | `Areas_they_can_change` |
| `Access` | string |  |  | `Access` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**Role**
- `AR Clerk`: 1 rows
- `CFO`: 1 rows
- `Controller`: 1 rows
- `AP Clerk`: 1 rows

**Areas_with_access**
- `10`: 2 rows
- `1`: 2 rows

**Areas_they_can_change**
- `10`: 2 rows
- `1`: 2 rows

**Access**
- `Review Access`: 4 rows

**MDP_CREATED_DATE**
- `2026-11-04 10:51:39.204030+00:00`: 4 rows

**MDP_MODIFIED_DATE**
- `2026-11-04 10:51:39.204030+00:00`: 4 rows

## Profile

Rows in the latest export: 4.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `User` | STRING | 4 | 0 |  |  |
| `Role` | STRING | 4 | 0 | AP Clerk | Controller |
| `Areas_with_access` | INT | 2 | 0 | 1 | 10 |
| `Areas_they_can_change` | INT | 2 | 0 | 1 | 10 |
| `Access` | STRING | 1 | 0 | Review Access | Review Access |
| `HASH_KEY` | STRING | 4 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-04 10:51:39.204000 | 2026-11-04 10:51:39.204000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-04 10:51:39.204000 | 2026-11-04 10:51:39.204000 |

## Sample rows

| User | Role | Areas_with_access | Areas_they_can_change | Access | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|
| <masked> | CFO | 10 | 10 | Review Access | <masked> | 2026-11-04 10:51:39.204000 | <masked> | 2026-11-04 10:51:39.204000 |
| <masked> | Controller | 10 | 10 | Review Access | <masked> | 2026-11-04 10:51:39.204000 | <masked> | 2026-11-04 10:51:39.204000 |
| <masked> | AR Clerk | 1 | 1 | Review Access | <masked> | 2026-11-04 10:51:39.204000 | <masked> | 2026-11-04 10:51:39.204000 |
| <masked> | AP Clerk | 1 | 1 | Review Access | <masked> | 2026-11-04 10:51:39.204000 | <masked> | 2026-11-04 10:51:39.204000 |
