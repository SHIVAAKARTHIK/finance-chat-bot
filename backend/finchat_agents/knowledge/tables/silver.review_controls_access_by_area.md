---
name: review_controls_access_by_area
schema: silver
layer: silver
domain: null
type: table
status: active
purpose: Shows which role (CFO; Controller; AR/AP Clerk) can do what in each product area.
grain: one row per HASH_KEY (one product area)
primary_key:
- HASH_KEY
entity_column: null
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues: []
row_count: 10
proposed_fields:
- grain
- primary_key
reviewed: false
---

# review_controls_access_by_area

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
- `Manage Collections`: 1 rows
- `Intelligence Hub`: 1 rows
- `Manage and Pay Vendors`: 1 rows
- `Provide Audit Artifacts`: 1 rows
- `Platform & AI Agents`: 1 rows
- `Manage Cash`: 1 rows
- `Manage Fixed Assets`: 1 rows
- `Manage the Business`: 1 rows
- `Manage the close`: 1 rows
- `Review Controls`: 1 rows

**CFO**
- `View · Edit · Approve · Export`: 10 rows

**Controller**
- `View · Edit · Approve · Export`: 10 rows

**AR_Clerk**
- `—`: 9 rows
- `View · Edit · Approve · Export`: 1 rows

**AP_Clerk**
- `—`: 9 rows
- `View · Edit · Approve · Export`: 1 rows

**source_file_name**
- `access_by_area.csv`: 10 rows

**MDP_CREATED_DATE**
- `2026-11-04 10:51:22.576010+00:00`: 10 rows

**MDP_MODIFIED_DATE**
- `2026-11-04 10:51:22.576010+00:00`: 10 rows

## Profile

Rows in the latest export: 10.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `Area` | STRING | 10 | 0 | Intelligence Hub | Review Controls |
| `CFO` | STRING | 1 | 0 | View · Edit · Approve · Export | View · Edit · Approve · Export |
| `Controller` | STRING | 1 | 0 | View · Edit · Approve · Export | View · Edit · Approve · Export |
| `AR_Clerk` | STRING | 2 | 0 | View · Edit · Approve · Export | — |
| `AP_Clerk` | STRING | 2 | 0 | View · Edit · Approve · Export | — |
| `source_file_name` | STRING | 1 | 0 | access_by_area.csv | access_by_area.csv |
| `HASH_KEY` | STRING | 10 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-04 10:51:22.576000 | 2026-11-04 10:51:22.576000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-04 10:51:22.576000 | 2026-11-04 10:51:22.576000 |

## Sample rows

| Area | CFO | Controller | AR_Clerk | AP_Clerk | source_file_name | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|
| Manage the Business | View · Edit · Approve · Export | View · Edit · Approve · Export | — | — | access_by_area.csv | <masked> | 2026-11-04 10:51:22.576000 | <masked> | 2026-11-04 10:51:22.576000 |
| Manage Cash | View · Edit · Approve · Export | View · Edit · Approve · Export | — | — | access_by_area.csv | <masked> | 2026-11-04 10:51:22.576000 | <masked> | 2026-11-04 10:51:22.576000 |
| Manage the close | View · Edit · Approve · Export | View · Edit · Approve · Export | — | — | access_by_area.csv | <masked> | 2026-11-04 10:51:22.576000 | <masked> | 2026-11-04 10:51:22.576000 |
| Manage and Pay Vendors | View · Edit · Approve · Export | View · Edit · Approve · Export | View · Edit · Approve · Export | — | access_by_area.csv | <masked> | 2026-11-04 10:51:22.576000 | <masked> | 2026-11-04 10:51:22.576000 |
| Manage Collections | View · Edit · Approve · Export | View · Edit · Approve · Export | — | View · Edit · Approve · Export | access_by_area.csv | <masked> | 2026-11-04 10:51:22.576000 | <masked> | 2026-11-04 10:51:22.576000 |
