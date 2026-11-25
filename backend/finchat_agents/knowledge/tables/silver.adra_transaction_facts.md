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
row_count: 4622
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
- `Balance detail`: 4116 rows
- `Timing`: 66 rows
- `Unresolved`: 11 rows

**ACCOUNT_STATUS**
- `Not prepared`: 3325 rows
- `Approved`: 912 rows
- `Prepared`: 385 rows

**ACCOUNT_IS_FINALIZED**
- `False`: 3820 rows
- `True`: 802 rows

**ACCOUNT_IS_CARRIED_FORWARD**
- `False`: 4622 rows

**ACCOUNT_UNIDENTIFIED_BALANCE**
- `0`: 1330 rows
- `-2755.69`: 671 rows
- `1434.19`: 671 rows
- `6.9`: 374 rows
- `-6.92`: 363 rows
- `-805.7`: 165 rows
- `250.87`: 154 rows
- `104.71`: 132 rows
- `-2633.23`: 104 rows
- `-56.32`: 104 rows
- `91.01`: 88 rows
- `-4.27`: 88 rows
- `-990.29`: 48 rows
- `283619`: 44 rows
- `382543`: 44 rows
- `0.08`: 44 rows
- `-110908`: 33 rows
- `1624.58`: 33 rows
- `-199272`: 22 rows
- `-3.75`: 22 rows
- `-12773`: 22 rows
- `620.2`: 22 rows
- `-143271`: 11 rows
- `992715`: 11 rows
- `-132355`: 11 rows
- `-83500`: 11 rows

**ACCOUNT_UNIDENTIFIED_BALANCE_ENGAGEMENT**
- `0`: 1330 rows
- `-3650.74`: 671 rows
- `1900.01`: 671 rows
- `7.81`: 374 rows
- `-7.83`: 363 rows
- `-1067.39`: 165 rows
- `332.35`: 154 rows
- `138.72`: 132 rows
- `-74.61`: 104 rows
- `-3488.5`: 104 rows
- `120.57`: 88 rows
- `-4.83`: 88 rows
- `-1311.94`: 48 rows
- `0.09`: 44 rows
- `283619`: 44 rows
- `382543`: 44 rows
- `-110908`: 33 rows
- `2152.24`: 33 rows
- `-199272`: 22 rows
- `-4.24`: 22 rows
- `-12773`: 22 rows
- `821.64`: 22 rows
- `-143271`: 11 rows
- `992715`: 11 rows
- `-132355`: 11 rows
- `-83500`: 11 rows

**BOOOKING_DATE**
- `2026-09-01 00:00:00.0000000 +00:00`: 1573 rows
- `2026-08-31 00:00:00.0000000 +00:00`: 1562 rows
- `2025-02-28 00:00:00.0000000 +00:00`: 605 rows
- `2026-10-31 00:00:00.0000000 +00:00`: 176 rows
- `2026-09-04 00:00:00.0000000 +00:00`: 88 rows
- `2026-09-15 00:00:00.0000000 +00:00`: 80 rows
- `2026-09-10 00:00:00.0000000 +00:00`: 72 rows
- `2026-09-21 00:00:00.0000000 +00:00`: 72 rows
- `2026-09-17 00:00:00.0000000 +00:00`: 64 rows
- `2026-09-07 00:00:00.0000000 +00:00`: 56 rows
- `2026-09-18 00:00:00.0000000 +00:00`: 48 rows
- `2026-09-16 00:00:00.0000000 +00:00`: 48 rows
- `2026-09-08 00:00:00.0000000 +00:00`: 48 rows
- `2026-09-14 00:00:00.0000000 +00:00`: 32 rows
- `2026-09-09 00:00:00.0000000 +00:00`: 24 rows
- `2025-02-10 00:00:00.0000000 +00:00`: 22 rows
- `2025-02-18 00:00:00.0000000 +00:00`: 22 rows
- `2025-02-20 00:00:00.0000000 +00:00`: 11 rows
- `2025-02-11 00:00:00.0000000 +00:00`: 11 rows
- `2026-09-20 00:00:00.0000000 +00:00`: 8 rows

**TEXT**
- `None`: 4589 rows
- `Bonds-1`: 11 rows
- `Bonds-2`: 11 rows
- `Bonds-3`: 11 rows

**CURRENCY**
- `44`: 1980 rows
- `111`: 1154 rows
- `50`: 740 rows
- `30`: 462 rows
- `71`: 121 rows
- `24`: 110 rows
- `73`: 33 rows
- `120`: 22 rows

**CURRENCY_NAME**
- `US Dollar`: 1980 rows
- `British Pound`: 1154 rows
- `Euro`: 740 rows
- `Canadian Dollar`: 462 rows
- `Swedish Krona`: 121 rows
- `Australian Dollar`: 110 rows
- `Norwegian Krone`: 33 rows
- `South African Rand`: 22 rows

**COUNT_OF_ATTACHMENTS**
- `0`: 4622 rows

**AGE_DAYS**
- `30`: 1562 rows
- `29`: 1562 rows
- `0`: 781 rows
- `26`: 88 rows
- `15`: 80 rows
- `9`: 72 rows
- `20`: 72 rows
- `13`: 64 rows
- `23`: 56 rows
- `14`: 48 rows
- `22`: 48 rows
- `12`: 48 rows
- `16`: 32 rows
- `10`: 30 rows
- `21`: 24 rows
- `18`: 22 rows
- `8`: 11 rows
- `60`: 11 rows
- `17`: 11 rows

**AGE_GROUP**
- `0-30 Days`: 4611 rows
- `31-60 Days`: 11 rows

**ENGAGEMENT_GUID**
- `949e65cb-7216-4cb5-9840-4bc138a1921b`: 4622 rows

**SOURCE_FILE_NAME**
- `transactionfacts__20261116_174201.csv`: 442 rows
- `transactionfacts__20261116_154202.csv`: 442 rows
- `transactionfacts__20261116_134202.csv`: 442 rows
- `transactionfacts__20261116_191049.csv`: 442 rows
- `transactionfacts__20261116_194202.csv`: 442 rows
- `transactionfacts__20261116_144205.csv`: 442 rows
- `transactionfacts__20261116_164202.csv`: 442 rows
- `transactionfacts__20261116_192918.csv`: 442 rows
- `transactionfacts__20261116_124207.csv`: 362 rows
- `transactionfacts__20261116_114202.csv`: 362 rows
- `transactionfacts__20261116_104201.csv`: 362 rows

**MDP_CREATED_DATE**
- `2026-11-16 19:45:18.855787+00:00`: 4622 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 19:45:18.855787+00:00`: 4622 rows

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

## Profile

Rows in the latest export: 4622.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `TRANSACTION_KEY` | STRING | 442 | 0 |  |  |
| `REFERENCE_JOURNAL_NUMBER` | STRING | 392 | 154 | 01a1c962-52ff-741c-b20d-5c041c9e12d7 | Tax payment-201 |
| `ENGAGEMENT_KEY` | STRING | 1 | 0 |  |  |
| `LEGAL_ENTITY_KEY` | STRING | 9 | 0 |  |  |
| `PERIOD_KEY` | STRING | 9 | 0 |  |  |
| `FISCAL_YEAR_PERIOD_KEY` | STRING | 3 | 0 |  |  |
| `ACCOUNT_KEY` | STRING | 65 | 0 |  |  |
| `ITEM_ADDED_BY_USERNAME` | STRING | 3 | 0 |  |  |
| `ITEM_ADDED_BY_NAME` | STRING | 3 | 0 |  |  |
| `TRANSACTION_TYPE` | STRING | 2 | 0 | Ledger transaction | Subledger transaction |
| `TRANSACTION_STATUS` | STRING | 5 | 0 | Balance detail | Unresolved |
| `ACCOUNT_STATUS` | STRING | 3 | 0 | Approved | Prepared |
| `ACCOUNT_IS_FINALIZED` | STRING | 2 | 0 | False | True |
| `ACCOUNT_IS_CARRIED_FORWARD` | STRING | 1 | 0 | False | False |
| `ITEM_CREATED_DATE` | STRING | 58 | 0 | 2026-10-18 16:39:06.0000000 +00:00 | 2026-11-16 13:27:23.0000000 +00:00 |
| `ACCOUNT_BALANCE` | STRING | 66 | 0 | -13424 | 98583.59 |
| `ACCOUNT_UNIDENTIFIED_BALANCE` | STRING | 27 | 0 | -110908 | 992715 |
| `ACCOUNT_BALANCE_ENGAGEMENT` | STRING | 65 | 0 | -10381.98 | 98583.59 |
| `ACCOUNT_UNIDENTIFIED_BALANCE_ENGAGEMENT` | STRING | 27 | 0 | -1067.39 | 992715 |
| `BOOOKING_DATE` | STRING | 20 | 0 | 2025-02-10 00:00:00.0000000 +00:00 | 2026-10-31 00:00:00.0000000 +00:00 |
| `TEXT` | STRING | 3 | 4589 | Bonds-1 | Bonds-3 |
| `AMOUNT` | STRING | 449 | 0 | -0.05 | 988931 |
| `AMOUNT_ABS` | STRING | 430 | 0 | 0 | 9898040.66 |
| `CURRENCY_RATE` | STRING | 178 | 0 | 0.0176470588 | 1.25 |
| `TRANSACTION_AMOUNT` | STRING | 430 | 0 | -0.04 | 99586.04 |
| `CURRENCY` | STRING | 8 | 0 | 111 | 73 |
| `CURRENCY_NAME` | STRING | 8 | 0 | Australian Dollar | US Dollar |
| `COUNT_OF_ATTACHMENTS` | STRING | 1 | 0 | 0 | 0 |
| `AGE_DAYS` | STRING | 19 | 0 | 0 | 9 |
| `AGE_GROUP` | STRING | 2 | 0 | 0-30 Days | 31-60 Days |
| `ACCOUNT_PERIOD_TRANSACTION_KEY` | STRING | 65 | 0 |  |  |
| `ENGAGEMENT_GUID` | STRING | 1 | 0 | 949e65cb-7216-4cb5-9840-4bc138a1921b | 949e65cb-7216-4cb5-9840-4bc138a1921b |
| `SOURCE_FILE_NAME` | STRING | 11 | 0 | transactionfacts__20261116_104201.csv | transactionfacts__20261116_194202.csv |
| `HASH_KEY` | STRING | 4641 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 19:45:18.856000 | 2026-11-16 19:45:18.856000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 19:45:18.856000 | 2026-11-16 19:45:18.856000 |

## Sample rows

| REFERENCE_JOURNAL_NUMBER | ITEM_ADDED_BY_USERNAME | ITEM_ADDED_BY_NAME | TRANSACTION_TYPE | TRANSACTION_STATUS | ACCOUNT_STATUS | ACCOUNT_IS_FINALIZED | ACCOUNT_IS_CARRIED_FORWARD | ITEM_CREATED_DATE | ACCOUNT_BALANCE | ACCOUNT_UNIDENTIFIED_BALANCE | ACCOUNT_BALANCE_ENGAGEMENT | ACCOUNT_UNIDENTIFIED_BALANCE_ENGAGEMENT | BOOOKING_DATE | TEXT | AMOUNT | AMOUNT_ABS | CURRENCY_RATE | TRANSACTION_AMOUNT | CURRENCY | CURRENCY_NAME | COUNT_OF_ATTACHMENTS | AGE_DAYS | AGE_GROUP | ENGAGEMENT_GUID | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NULL | <masked> | <masked> | Ledger transaction | Balance detail | Prepared | False | False | 2026-10-18 16:39:06.0000000 +00:00 | 30890 | 0 | 30890 | 0 | 2026-09-01 00:00:00.0000000 +00:00 | NULL | 30890 | 30890 | 1 | 30890 | 44 | US Dollar | 0 | 60 | 31-60 Days | 949e65cb-7216-4cb5-9840-4bc138a1921b | transactionfacts__20261116_104201.csv | <masked> | 2026-11-16 19:45:18.856000 | <masked> | 2026-11-16 19:45:18.856000 |
| INSPECTION FEES | <masked> | <masked> | Subledger transaction | Balance detail | Approved | False | False | 2026-10-23 10:54:07.0000000 +00:00 | 51853 | 0 | 51853 | 0 | 2025-02-28 00:00:00.0000000 +00:00 | NULL | 10022 | 10022 | 1 | 10022 | 44 | US Dollar | 0 | 0 | 0-30 Days | 949e65cb-7216-4cb5-9840-4bc138a1921b | transactionfacts__20261116_104201.csv | <masked> | 2026-11-16 19:45:18.856000 | <masked> | 2026-11-16 19:45:18.856000 |
| MANAGEMENT FEES RECEIPT | <masked> | <masked> | Subledger transaction | Balance detail | Approved | False | False | 2026-10-23 10:54:07.0000000 +00:00 | 51853 | 0 | 51853 | 0 | 2025-02-28 00:00:00.0000000 +00:00 | NULL | 15664 | 15664 | 1 | 15664 | 44 | US Dollar | 0 | 0 | 0-30 Days | 949e65cb-7216-4cb5-9840-4bc138a1921b | transactionfacts__20261116_104201.csv | <masked> | 2026-11-16 19:45:18.856000 | <masked> | 2026-11-16 19:45:18.856000 |
| DIRECT_PAID_LOSS | <masked> | <masked> | Subledger transaction | Balance detail | Prepared | False | False | 2026-10-23 10:54:07.0000000 +00:00 | -26257 | 0 | -26257 | 0 | 2025-02-28 00:00:00.0000000 +00:00 | NULL | -4326 | 4326 | 1 | -4326 | 44 | US Dollar | 0 | 0 | 0-30 Days | 949e65cb-7216-4cb5-9840-4bc138a1921b | transactionfacts__20261116_104201.csv | <masked> | 2026-11-16 19:45:18.856000 | <masked> | 2026-11-16 19:45:18.856000 |
| DIRECT_PAID_LOSS_LAE | <masked> | <masked> | Subledger transaction | Balance detail | Prepared | False | False | 2026-10-23 10:54:07.0000000 +00:00 | -26257 | 0 | -26257 | 0 | 2025-02-28 00:00:00.0000000 +00:00 | NULL | -6078 | 6078 | 1 | -6078 | 44 | US Dollar | 0 | 0 | 0-30 Days | 949e65cb-7216-4cb5-9840-4bc138a1921b | transactionfacts__20261116_104201.csv | <masked> | 2026-11-16 19:45:18.856000 | <masked> | 2026-11-16 19:45:18.856000 |
