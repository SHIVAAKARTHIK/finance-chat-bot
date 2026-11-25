# adra_legal_entity_dimensions

**Domain:** ADRA  
**Type:** dimension table  
**Full name:** `lakehouse_mvpai.silver.adra_legal_entity_dimensions`  
**Grain:** one row per (LEGAL_ENTITY_KEY, ENGAGEMENT_KEY)  
**Also called:** legal entity, entity, company  

ADRA legal entities: one row per legal entity within an engagement (code, name, status, country, currency).

> All columns are stored as text (STRING). Cast numbers and dates as shown in *SQL expression*; compare text with `trim()` and `lower()`.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `LEGAL_ENTITY_KEY` | string | Surrogate key of the legal entity (e.g. 14781 = 100-Northwind). |  | `trim(LEGAL_ENTITY_KEY)` |
| `ENGAGEMENT_KEY` | string | Engagement (client tenant) the entity belongs to. |  | `trim(ENGAGEMENT_KEY)` |
| `ENTITY_CODE` | string | Short entity code shown to users, e.g. 100 or 561. | entity code | `trim(ENTITY_CODE)` |
| `ENTITY_NAME` | string | Entity name, e.g. 100-Northwind, Cars USA Shipping, LLC. | entity name, company name | `trim(ENTITY_NAME)` |
| `STATUS` | string | Entity status. | entity status | `trim(STATUS)` |
| `COUNTRY` | string | Country of the legal entity. |  | `trim(COUNTRY)` |
| `ENTITY_CURRENCY_CODE` | string | Functional currency code of the entity. | entity currency | `trim(ENTITY_CURRENCY_CODE)` |
## Joins (approved, use the full key)

| Join | To table | Cardinality | Condition |
|---|---|---|---|
| `account_fact_to_legal_entity` | `adra_account_facts` | many-to-one | `adra_account_facts.LEGAL_ENTITY_KEY = adra_legal_entity_dimensions.LEGAL_ENTITY_KEY AND adra_account_facts.ENGAGEMENT_KEY = adra_legal_entity_dimensions.ENGAGEMENT_KEY` |
| `transaction_fact_to_legal_entity` | `adra_transaction_facts` | many-to-one | `adra_transaction_facts.LEGAL_ENTITY_KEY = adra_legal_entity_dimensions.LEGAL_ENTITY_KEY AND adra_transaction_facts.ENGAGEMENT_KEY = adra_legal_entity_dimensions.ENGAGEMENT_KEY` |
| `legal_entity_to_engagement` | `adra_engagement_dimensions` | many-to-one | `adra_legal_entity_dimensions.ENGAGEMENT_KEY = adra_engagement_dimensions.Engagement_Key` |
