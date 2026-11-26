---
name: adra_transaction_facts
schema: silver
layer: silver
domain: recon
type: fact
status: active
purpose: 'ADRA reconciling items (transactions) per account, legal entity and period: transaction type, status, amount, age
  in days and ageing bucket.'
grain: one row per reconciling item (HASH_KEY)
primary_key:
- HASH_KEY
entity_column: LEGAL_ENTITY_KEY
period_columns:
- PERIOD_KEY
pii_columns:
- ITEM_ADDED_BY_NAME
- ITEM_ADDED_BY_USERNAME
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms:
- transactions
- transaction
- reconciling items
- open items
- items
- ageing
- aging
- transaction age
- oldest item
known_issues:
- code: all_string_columns
  note: Every column is stored as STRING. Cast numbers and dates; CURRENCY is a code, not a number.
reviewed: true
proposed_fields: []
---

# adra_transaction_facts

ADRA reconciling items (transactions) per account, legal entity and period: transaction type, status, amount,
age in days and ageing bucket.

> All columns are stored as text (STRING). Filter entity and period through `adra_legal_entity_dimensions` and
> `adra_period_dimensions`, and account number through `adra_account_dimensions`, always with the full key.

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `HASH_KEY` | string | Row key (one row per transaction). |  | `trim(HASH_KEY)` |
| `ACCOUNT_KEY` | string | Account key (join to adra_account_dimensions with the full key). |  | `trim(ACCOUNT_KEY)` |
| `ENGAGEMENT_KEY` | string | Engagement key. |  | `trim(ENGAGEMENT_KEY)` |
| `LEGAL_ENTITY_KEY` | string | Legal entity key. |  | `trim(LEGAL_ENTITY_KEY)` |
| `PERIOD_KEY` | string | Period key. |  | `trim(PERIOD_KEY)` |
| `TRANSACTION_TYPE` | string | Transaction type (not the status). | transaction type, type | `trim(TRANSACTION_TYPE)` |
| `TRANSACTION_STATUS` | string | Transaction status. 'Not Set' is a placeholder, not a real status. | transaction status | `trim(TRANSACTION_STATUS)` |
| `AMOUNT` | decimal | Signed transaction amount. | amount, transaction amount | `TRY_CAST(AMOUNT AS DECIMAL(38,2))` |
| `AMOUNT_ABS` | decimal | Absolute transaction amount (gross). | absolute amount, gross amount | `TRY_CAST(AMOUNT_ABS AS DECIMAL(38,2))` |
| `AGE_DAYS` | integer | Age of the item in days (MAX for "oldest"). | age, age in days, days old, oldest | `TRY_CAST(AGE_DAYS AS INT)` |
| `AGE_GROUP` | string | Ageing bucket, e.g. '0-30 Days'. | age group, aging bucket, ageing bucket | `trim(AGE_GROUP)` |
| `ITEM_CREATED_DATE` | timestamp | When the item was created. | created date | `TRY_CAST(ITEM_CREATED_DATE AS TIMESTAMP)` |
| `ITEM_ADDED_BY_NAME` | string | Person who added the item. PII. | added by | `trim(ITEM_ADDED_BY_NAME)` |
| `CURRENCY` | string | Transaction currency code (identifier, not a number). | currency | `trim(CURRENCY)` |
| `TRANSACTION_KEY` | string |  |  | `TRANSACTION_KEY` |
| `REFERENCE_JOURNAL_NUMBER` | string |  |  | `REFERENCE_JOURNAL_NUMBER` |
| `FISCAL_YEAR_PERIOD_KEY` | string |  |  | `FISCAL_YEAR_PERIOD_KEY` |
| `ITEM_ADDED_BY_USERNAME` | string |  |  | `ITEM_ADDED_BY_USERNAME` |
| `ACCOUNT_STATUS` | string |  |  | `ACCOUNT_STATUS` |
| `ACCOUNT_IS_FINALIZED` | string |  |  | `ACCOUNT_IS_FINALIZED` |
| `ACCOUNT_IS_CARRIED_FORWARD` | string |  |  | `ACCOUNT_IS_CARRIED_FORWARD` |
| `ACCOUNT_BALANCE` | string |  |  | `ACCOUNT_BALANCE` |
| `ACCOUNT_UNIDENTIFIED_BALANCE` | string |  |  | `ACCOUNT_UNIDENTIFIED_BALANCE` |
| `ACCOUNT_BALANCE_ENGAGEMENT` | string |  |  | `ACCOUNT_BALANCE_ENGAGEMENT` |
| `ACCOUNT_UNIDENTIFIED_BALANCE_ENGAGEMENT` | string |  |  | `ACCOUNT_UNIDENTIFIED_BALANCE_ENGAGEMENT` |
| `BOOOKING_DATE` | string |  |  | `BOOOKING_DATE` |
| `TEXT` | string |  |  | `TEXT` |
| `CURRENCY_RATE` | string |  |  | `CURRENCY_RATE` |
| `TRANSACTION_AMOUNT` | string |  |  | `TRANSACTION_AMOUNT` |
| `CURRENCY_NAME` | string |  |  | `CURRENCY_NAME` |
| `COUNT_OF_ATTACHMENTS` | string |  |  | `COUNT_OF_ATTACHMENTS` |
| `ACCOUNT_PERIOD_TRANSACTION_KEY` | string |  |  | `ACCOUNT_PERIOD_TRANSACTION_KEY` |
| `ENGAGEMENT_GUID` | string |  |  | `ENGAGEMENT_GUID` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**TRANSACTION_TYPE**
- `Ledger transaction`: posted in the ledger
- `Subledger transaction`: from a subledger

**TRANSACTION_STATUS**
- `Required adjustment`: needs an adjusting entry
- `Not Set`: no status recorded
- `Balance detail`
- `Timing`
- `Unresolved`

**ACCOUNT_STATUS**
- `Not prepared`
- `Approved`
- `Prepared`

**ACCOUNT_IS_FINALIZED**
- `False`
- `True`

**ACCOUNT_IS_CARRIED_FORWARD**
- `False`

**ACCOUNT_UNIDENTIFIED_BALANCE**
- `0`
- `-2755.69`
- `1434.19`
- `6.9`
- `-6.92`
- `-805.7`
- `250.87`
- `104.71`
- `-2633.23`
- `-56.32`
- `91.01`
- `-4.27`
- `-990.29`
- `283619`
- `382543`
- `0.08`
- `-110908`
- `1624.58`
- `-199272`
- `-3.75`
- `-12773`
- `620.2`
- `-143271`
- `992715`
- `-132355`
- `-83500`

**ACCOUNT_UNIDENTIFIED_BALANCE_ENGAGEMENT**
- `0`
- `-3650.74`
- `1900.01`
- `7.81`
- `-7.83`
- `-1067.39`
- `332.35`
- `138.72`
- `-74.61`
- `-3488.5`
- `120.57`
- `-4.83`
- `-1311.94`
- `0.09`
- `283619`
- `382543`
- `-110908`
- `2152.24`
- `-199272`
- `-4.24`
- `-12773`
- `821.64`
- `-143271`
- `992715`
- `-132355`
- `-83500`

**BOOOKING_DATE**
- `2026-09-01 00:00:00.0000000 +00:00`
- `2026-08-31 00:00:00.0000000 +00:00`
- `2025-02-28 00:00:00.0000000 +00:00`
- `2026-10-31 00:00:00.0000000 +00:00`
- `2026-09-04 00:00:00.0000000 +00:00`
- `2026-09-15 00:00:00.0000000 +00:00`
- `2026-09-10 00:00:00.0000000 +00:00`
- `2026-09-21 00:00:00.0000000 +00:00`
- `2026-09-17 00:00:00.0000000 +00:00`
- `2026-09-07 00:00:00.0000000 +00:00`
- `2026-09-18 00:00:00.0000000 +00:00`
- `2026-09-16 00:00:00.0000000 +00:00`
- `2026-09-08 00:00:00.0000000 +00:00`
- `2026-09-14 00:00:00.0000000 +00:00`
- `2026-09-09 00:00:00.0000000 +00:00`
- `2025-02-10 00:00:00.0000000 +00:00`
- `2025-02-18 00:00:00.0000000 +00:00`
- `2025-02-20 00:00:00.0000000 +00:00`
- `2025-02-11 00:00:00.0000000 +00:00`
- `2026-09-20 00:00:00.0000000 +00:00`

**TEXT**
- `None`
- `Bonds-1`
- `Bonds-2`
- `Bonds-3`

**CURRENCY**
- `44`
- `111`
- `50`
- `30`
- `71`
- `24`
- `73`
- `120`

**CURRENCY_NAME**
- `US Dollar`
- `British Pound`
- `Euro`
- `Canadian Dollar`
- `Swedish Krona`
- `Australian Dollar`
- `Norwegian Krone`
- `South African Rand`

**COUNT_OF_ATTACHMENTS**
- `0`

**AGE_DAYS**
- `30`
- `29`
- `0`
- `26`
- `15`
- `9`
- `20`
- `13`
- `23`
- `14`
- `22`
- `12`
- `16`
- `10`
- `21`
- `18`
- `8`
- `60`
- `17`

**AGE_GROUP**
- `0-30 Days`
- `31-60 Days`

**ENGAGEMENT_GUID**
- `949e65cb-7216-4cb5-9840-4bc138a1921b`

**SOURCE_FILE_NAME**
- `transactionfacts__20261116_174201.csv`
- `transactionfacts__20261116_154202.csv`
- `transactionfacts__20261116_134202.csv`
- `transactionfacts__20261116_191049.csv`
- `transactionfacts__20261116_194202.csv`
- `transactionfacts__20261116_144205.csv`
- `transactionfacts__20261116_164202.csv`
- `transactionfacts__20261116_192918.csv`
- `transactionfacts__20261116_124207.csv`
- `transactionfacts__20261116_114202.csv`
- `transactionfacts__20261116_104201.csv`

**MDP_CREATED_DATE**
- `2026-11-16 19:45:18.855787+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 19:45:18.855787+00:00`

## Joins (approved, use the full key)

| Join | To table | Cardinality |
|---|---|---|
| `transaction_fact_to_account` | `adra_account_dimensions` | many-to-one |
| `transaction_fact_to_period` | `adra_period_dimensions` | many-to-one |
| `transaction_fact_to_legal_entity` | `adra_legal_entity_dimensions` | many-to-one |

## Named metrics

| Metric | Meaning | SQL | Additivity |
|---|---|---|---|
| `transaction_count` | Number of reconciling items. | `COUNT(*)` | additive |
| `total_amount_abs` | Gross amount of items. | `SUM(TRY_CAST(AMOUNT_ABS AS DECIMAL(38,2)))` | additive |
| `oldest_item_age_days` | Age in days of the oldest item. | `MAX(TRY_CAST(AGE_DAYS AS INT))` | non additive |
