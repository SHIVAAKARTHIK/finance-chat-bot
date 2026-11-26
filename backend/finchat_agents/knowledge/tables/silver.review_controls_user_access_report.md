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
- `AR Clerk`
- `CFO`
- `Controller`
- `AP Clerk`

**Areas_with_access**
- `10`
- `1`

**Areas_they_can_change**
- `10`
- `1`

**Access**
- `Review Access`

**MDP_CREATED_DATE**
- `2026-11-04 10:51:39.204030+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-04 10:51:39.204030+00:00`
