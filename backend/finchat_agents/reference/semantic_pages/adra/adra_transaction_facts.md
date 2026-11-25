# adra_transaction_facts

**Domain:** ADRA  
**Type:** fact table  
**Full name:** `lakehouse_mvpai.silver.adra_transaction_facts`  
**Grain:** one row per (HASH_KEY)  
**Also called:** transactions, reconciling items, open items  

Reconciling items (transactions) per account, legal entity and period: type, status, amount and age.

> All columns are stored as text (STRING). Cast numbers and dates as shown in *SQL expression*; compare text with `trim()` and `lower()`.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `HASH_KEY` | string | Row key (one row per transaction). |  | `trim(HASH_KEY)` |
| `ACCOUNT_KEY` | string | Account key (FK to adra_account_dimensions). |  | `trim(ACCOUNT_KEY)` |
| `ENGAGEMENT_KEY` | string | Engagement key. |  | `trim(ENGAGEMENT_KEY)` |
| `LEGAL_ENTITY_KEY` | string | Legal entity key. |  | `trim(LEGAL_ENTITY_KEY)` |
| `PERIOD_KEY` | string | Period key. |  | `trim(PERIOD_KEY)` |
| `TRANSACTION_TYPE` | string | Transaction type (not the status). | transaction type, type | `trim(TRANSACTION_TYPE)` |
| `TRANSACTION_STATUS` | string | Transaction status. 'Not Set' is a placeholder, not a real status. | transaction status | `trim(TRANSACTION_STATUS)` |
| `AMOUNT` | decimal | Signed transaction amount. | amount, transaction amount | `TRY_CAST(AMOUNT AS DECIMAL(38,2))` |
| `AMOUNT_ABS` | decimal | Absolute transaction amount (gross). | absolute amount, gross amount | `TRY_CAST(AMOUNT_ABS AS DECIMAL(38,2))` |
| `AGE_DAYS` | integer | Age of the item in days (use MAX for 'oldest'). | age, age in days, days old | `TRY_CAST(AGE_DAYS AS INT)` |
| `AGE_GROUP` | string | Ageing bucket. | age group, aging bucket, ageing | `trim(AGE_GROUP)` |
| `ITEM_CREATED_DATE` | timestamp | When the item was created. |  | `TRY_CAST(ITEM_CREATED_DATE AS TIMESTAMP)` |
| `ITEM_ADDED_BY_NAME` | string | Person who added the item. **PII: mask unless the user may view personal data; never filter or group by it.** | added by | `trim(ITEM_ADDED_BY_NAME)` |
| `CURRENCY` | string | Transaction currency code (identifier, not a number). |  | `trim(CURRENCY)` |

## Values

**TRANSACTION_TYPE**
- `Ledger transaction`: posted in the ledger
- `Subledger transaction`: from a subledger

**TRANSACTION_STATUS**
- `Required adjustment`: needs an adjusting entry
- `Not Set`: no status recorded

## Joins (approved, use the full key)

| Join | To table | Cardinality | Condition |
|---|---|---|---|
| `transaction_fact_to_account` | `adra_account_dimensions` | many-to-one | `adra_transaction_facts.ACCOUNT_KEY = adra_account_dimensions.ACCOUNT_KEY AND adra_transaction_facts.ENGAGEMENT_KEY = adra_account_dimensions.ENGAGEMENT_KEY AND adra_transaction_facts.LEGAL_ENTITY_KEY = adra_account_dimensions.LEGAL_ENTITY_KEY` |
| `transaction_fact_to_period` | `adra_period_dimensions` | many-to-one | `adra_transaction_facts.PERIOD_KEY = adra_period_dimensions.PERIOD_KEY AND adra_transaction_facts.ENGAGEMENT_KEY = adra_period_dimensions.ENGAGEMENT_KEY AND adra_transaction_facts.LEGAL_ENTITY_KEY = adra_period_dimensions.LEGAL_ENTITY_KEY` |
| `transaction_fact_to_legal_entity` | `adra_legal_entity_dimensions` | many-to-one | `adra_transaction_facts.LEGAL_ENTITY_KEY = adra_legal_entity_dimensions.LEGAL_ENTITY_KEY AND adra_transaction_facts.ENGAGEMENT_KEY = adra_legal_entity_dimensions.ENGAGEMENT_KEY` |

## Named metrics

| Metric | Meaning | SQL | Additivity |
|---|---|---|---|
| `transaction_count` | Number of reconciling items. | `COUNT(*)` | additive |
| `total_amount_abs` | Gross amount of items. | `SUM(TRY_CAST(AMOUNT_ABS AS DECIMAL(38,2)))` | additive |
| `oldest_item_age_days` | Age in days of the oldest item. | `MAX(TRY_CAST(AGE_DAYS AS INT))` | non additive |
