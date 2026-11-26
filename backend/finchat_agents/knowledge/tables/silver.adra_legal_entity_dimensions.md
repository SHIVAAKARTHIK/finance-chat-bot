---
name: adra_legal_entity_dimensions
schema: silver
layer: silver
domain: recon
type: dim
status: active
purpose: 'ADRA legal entities: one row per legal entity within an engagement (entity code, name, status, country, currency).
  Use it to turn the entity a user names into LEGAL_ENTITY_KEY values.'
grain: one row per legal entity within an engagement (LEGAL_ENTITY_KEY, ENGAGEMENT_KEY)
primary_key:
- LEGAL_ENTITY_KEY
- ENGAGEMENT_KEY
entity_column: ENTITY_CODE
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms:
- legal entity
- entity
- company
- entity code
- entity name
- country
- entity currency
known_issues:
- code: all_string_columns
  note: Every column is stored as STRING. Compare text with trim() and lower().
- code: orphans
  note: Fact rows with LEGAL_ENTITY_KEY 9819 have no row here.
reviewed: true
proposed_fields: []
---

# adra_legal_entity_dimensions

ADRA legal entities: one row per legal entity within an engagement (entity code, name, status, country, currency).
Use it to turn the entity a user names into LEGAL_ENTITY_KEY values.

> All columns are stored as text (STRING). Users name an entity by code ("561"), name ("Cars USA Shipping") or both
> ("561 - Cars USA Shipping, LLC"). Check current values with `get_column_values` / `resolve_entity`; do not assume them.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `LEGAL_ENTITY_KEY` | string | Surrogate key of the legal entity (internal, never shown to users). |  | `trim(LEGAL_ENTITY_KEY)` |
| `ENGAGEMENT_KEY` | string | Engagement (client tenant) the entity belongs to. |  | `trim(ENGAGEMENT_KEY)` |
| `ENTITY_CODE` | string | Short entity code shown to users (a number). | entity code, company code | `trim(ENTITY_CODE)` |
| `ENTITY_NAME` | string | Entity name as users know it; may include the code and suffixes such as LLC. | entity name, company name, legal entity | `trim(ENTITY_NAME)` |
| `STATUS` | string | Entity status. | entity status | `trim(STATUS)` |
| `COUNTRY` | string | Country of the legal entity. | country | `trim(COUNTRY)` |
| `ENTITY_CURRENCY_CODE` | string | Functional currency code of the entity. | entity currency, functional currency | `trim(ENTITY_CURRENCY_CODE)` |
| `ADDRESS_1` | string |  |  | `ADDRESS_1` |
| `ADDRESS_2` | string |  |  | `ADDRESS_2` |
| `ZIP_CODE` | string |  |  | `ZIP_CODE` |
| `CITY` | string |  |  | `CITY` |
| `IS_CROSS_ENTITY` | string |  |  | `IS_CROSS_ENTITY` |
| `ENTITY_CURRENCY_NAME` | string |  |  | `ENTITY_CURRENCY_NAME` |
| `ENTITY_INFORMATION` | string |  |  | `ENTITY_INFORMATION` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**STATUS**
- `Deactivated`
- `Active`

**ADDRESS_1**
- `None`

**ADDRESS_2**
- `None`

**ZIP_CODE**
- `None`

**CITY**
- `None`

**COUNTRY**
- `240`
- `239`

**SOURCE_FILE_NAME**
- `legalentitydimensions__20261116_194202.csv`

**MDP_CREATED_DATE**
- `2026-11-16 19:45:18.855503+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 19:45:18.855503+00:00`

## Empty columns

Empty in every row: `ADDRESS_1`, `ADDRESS_2`, `ZIP_CODE`, `CITY`, `IS_CROSS_ENTITY`, `ENTITY_INFORMATION`. Do not filter or group on them.

## Joins (approved, use the full key)

| Join | To table | Cardinality |
|---|---|---|
| `account_fact_to_legal_entity` | `adra_account_facts` | many-to-one (from the fact) |
| `transaction_fact_to_legal_entity` | `adra_transaction_facts` | many-to-one (from the fact) |
| `legal_entity_to_engagement` | `adra_engagement_dimensions` | many-to-one |

## Notes

- Match entity names loosely (ignore case, punctuation, "LLC"): `lower(ENTITY_NAME) LIKE '%cars usa shipping%'`, or
  filter on ENTITY_CODE when the user gives the code.
- If an entity has no rows for the requested period, say so; do not silently use another entity or period.
