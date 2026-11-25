---
name: adra_tasks_company_dimension
schema: silver
layer: silver
domain: recon
type: table
status: active
purpose: Companies that close tasks belong to in ADRA.
grain: one row per COMPANY_KEY (one company)
primary_key:
- COMPANY_KEY
entity_column: COMPANY_KEY
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues: []
row_count: 12
proposed_fields:
- grain
- primary_key
reviewed: false
---

# adra_tasks_company_dimension

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `COMPANY_KEY` | string |  |  | `COMPANY_KEY` |
| `ENGAGEMENT_KEY` | string |  |  | `ENGAGEMENT_KEY` |
| `COMPANY_NAME` | string |  |  | `COMPANY_NAME` |
| `COMPANY_CODE` | string |  |  | `COMPANY_CODE` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**SOURCE_FILE_NAME**
- `companydimension__20261116_174302.csv`: 12 rows

**MDP_CREATED_DATE**
- `2026-11-16 17:52:12.136372+00:00`: 12 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 17:52:12.136372+00:00`: 12 rows

## Profile

Rows in the latest export: 12.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `COMPANY_KEY` | STRING | 12 | 0 |  |  |
| `ENGAGEMENT_KEY` | STRING | 1 | 0 |  |  |
| `COMPANY_NAME` | STRING | 12 | 0 |  |  |
| `COMPANY_CODE` | STRING | 11 | 0 |  |  |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | companydimension__20261116_174302.csv | companydimension__20261116_174302.csv |
| `HASH_KEY` | STRING | 12 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 17:52:12.136000 | 2026-11-16 17:52:12.136000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 17:52:12.136000 | 2026-11-16 17:52:12.136000 |

## Sample rows

| SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|
| companydimension__20261116_174302.csv | <masked> | 2026-11-16 17:52:12.136000 | <masked> | 2026-11-16 17:52:12.136000 |
| companydimension__20261116_174302.csv | <masked> | 2026-11-16 17:52:12.136000 | <masked> | 2026-11-16 17:52:12.136000 |
| companydimension__20261116_174302.csv | <masked> | 2026-11-16 17:52:12.136000 | <masked> | 2026-11-16 17:52:12.136000 |
| companydimension__20261116_174302.csv | <masked> | 2026-11-16 17:52:12.136000 | <masked> | 2026-11-16 17:52:12.136000 |
| companydimension__20261116_174302.csv | <masked> | 2026-11-16 17:52:12.136000 | <masked> | 2026-11-16 17:52:12.136000 |
