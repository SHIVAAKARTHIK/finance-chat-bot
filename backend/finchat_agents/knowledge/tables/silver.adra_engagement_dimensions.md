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
- `KPMG Digital Finance Demo`

**EngagementCurrencyCode**
- `USD`

**EngagementCurrencyName**
- `US Dollar`

**EngagementGuid**
- `949e65cb-7216-4cb5-9840-4bc138a1921b`

**ShortGuid**
- `y2WelBZytUyYQEvBOKGSGw`

**source_file_name**
- `engagementdimensions__20261116_194202.csv`

**MDP_CREATED_DATE**
- `2026-11-16 19:45:18.855041+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 19:45:18.855041+00:00`

## Joins (approved, use the full key)

| Join | To table | Cardinality |
|---|---|---|
| `legal_entity_to_engagement` | `adra_legal_entity_dimensions` | many-to-one (from the entity) |
