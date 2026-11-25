---
name: adra_engagement_dimensions
schema: silver
layer: silver
domain: recon
type: dim
status: active
purpose: ADRA engagements (client tenants) that legal entities belong to, with name and reporting currency.
grain: one row per engagement (Engagement_Key)
primary_key:
- Engagement_Key
entity_column: null
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms:
- engagement
- engagements
- tenant
- client tenant
- engagement currency
known_issues:
- code: all_string_columns
  note: Every column is stored as STRING. Note the mixed-case column names.
reviewed: true
proposed_fields: []
row_count: 1
---

# adra_engagement_dimensions

ADRA engagements (client tenants) that legal entities belong to, with name and reporting currency.

> Column names here are mixed case (`Engagement_Key`, `EngagementName`); they join to `ENGAGEMENT_KEY` elsewhere.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `Engagement_Key` | string | Engagement key. |  | `trim(Engagement_Key)` |
| `EngagementName` | string | Engagement name. | engagement name, client | `trim(EngagementName)` |
| `EngagementCurrencyCode` | string | Engagement reporting currency code. | engagement currency, reporting currency | `trim(EngagementCurrencyCode)` |
| `EngagementCurrencyName` | string |  |  | `EngagementCurrencyName` |
| `EngagementGuid` | string |  |  | `EngagementGuid` |
| `ShortGuid` | string |  |  | `ShortGuid` |
| `source_file_name` | string |  |  | `source_file_name` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**EngagementName**
- `KPMG Digital Finance Demo`: 1 rows

**EngagementCurrencyCode**
- `USD`: 1 rows

**EngagementCurrencyName**
- `US Dollar`: 1 rows

**EngagementGuid**
- `949e65cb-7216-4cb5-9840-4bc138a1921b`: 1 rows

**ShortGuid**
- `y2WelBZytUyYQEvBOKGSGw`: 1 rows

**source_file_name**
- `engagementdimensions__20261116_194202.csv`: 1 rows

**MDP_CREATED_DATE**
- `2026-11-16 19:45:18.855041+00:00`: 1 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 19:45:18.855041+00:00`: 1 rows

## Joins (approved, use the full key)

| Join | To table | Cardinality |
|---|---|---|
| `legal_entity_to_engagement` | `adra_legal_entity_dimensions` | many-to-one (from the entity) |

## Profile

Rows in the latest export: 1.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `Engagement_Key` | STRING | 1 | 0 |  |  |
| `EngagementName` | STRING | 1 | 0 | KPMG Digital Finance Demo | KPMG Digital Finance Demo |
| `EngagementCurrencyCode` | STRING | 1 | 0 | USD | USD |
| `EngagementCurrencyName` | STRING | 1 | 0 | US Dollar | US Dollar |
| `EngagementGuid` | STRING | 1 | 0 | 949e65cb-7216-4cb5-9840-4bc138a1921b | 949e65cb-7216-4cb5-9840-4bc138a1921b |
| `ShortGuid` | STRING | 1 | 0 | y2WelBZytUyYQEvBOKGSGw | y2WelBZytUyYQEvBOKGSGw |
| `source_file_name` | STRING | 1 | 0 | engagementdimensions__20261116_194202... | engagementdimensions__20261116_194202... |
| `HASH_KEY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 19:45:18.855000 | 2026-11-16 19:45:18.855000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 19:45:18.855000 | 2026-11-16 19:45:18.855000 |

## Sample rows

| EngagementName | EngagementCurrencyCode | EngagementCurrencyName | EngagementGuid | ShortGuid | source_file_name | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|
| KPMG Digital Finance Demo | USD | US Dollar | 949e65cb-7216-4cb5-9840-4bc138a1921b | y2WelBZytUyYQEvBOKGSGw | engagementdimensions__20261116_194202... | <masked> | 2026-11-16 19:45:18.855000 | <masked> | 2026-11-16 19:45:18.855000 |
