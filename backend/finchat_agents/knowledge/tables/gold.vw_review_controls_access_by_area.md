---
name: vw_review_controls_access_by_area
schema: gold
layer: gold
domain: null
type: view
status: active
purpose: Shows access permissions by role and product area.
grain: one row per HASH_KEY (one product-area permission record)
primary_key:
- HASH_KEY
entity_column: null
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from:
- review_controls_access_by_area
known_issues: []
proposed_fields:
- grain
- primary_key
reviewed: false
---

# vw_review_controls_access_by_area

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `Area` | string |  |  | `Area` |
| `CFO` | string |  |  | `CFO` |
| `Controller` | string |  |  | `Controller` |
| `AR_Clerk` | string |  |  | `AR_Clerk` |
| `AP_Clerk` | string |  |  | `AP_Clerk` |
| `source_file_name` | string |  |  | `source_file_name` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**Area**
- `Manage Collections`
- `Intelligence Hub`
- `Manage and Pay Vendors`
- `Provide Audit Artifacts`
- `Platform & AI Agents`
- `Manage Cash`
- `Manage Fixed Assets`
- `Manage the Business`
- `Manage the close`
- `Review Controls`

**CFO**
- `View · Edit · Approve · Export`

**Controller**
- `View · Edit · Approve · Export`

**AR_Clerk**
- `—`
- `View · Edit · Approve · Export`

**AP_Clerk**
- `—`
- `View · Edit · Approve · Export`

**source_file_name**
- `access_by_area.csv`

**MDP_CREATED_DATE**
- `2026-11-04 10:51:22.576010+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-04 10:51:22.576010+00:00`
