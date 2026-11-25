# adra_engagement_dimensions

**Domain:** ADRA  
**Type:** dimension table  
**Full name:** `lakehouse_mvpai.silver.adra_engagement_dimensions`  
**Grain:** one row per (Engagement_Key)  
**Also called:** engagement, tenant  

ADRA engagements (client tenants) that legal entities belong to.

> All columns are stored as text (STRING). Cast numbers and dates as shown in *SQL expression*; compare text with `trim()` and `lower()`.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `Engagement_Key` | string | Engagement key. |  | `trim(Engagement_Key)` |
| `EngagementName` | string | Engagement name. | engagement name | `trim(EngagementName)` |
| `EngagementCurrencyCode` | string | Engagement reporting currency code. |  | `trim(EngagementCurrencyCode)` |
## Joins (approved, use the full key)

| Join | To table | Cardinality | Condition |
|---|---|---|---|
| `legal_entity_to_engagement` | `adra_legal_entity_dimensions` | many-to-one | `adra_legal_entity_dimensions.ENGAGEMENT_KEY = adra_engagement_dimensions.Engagement_Key` |
