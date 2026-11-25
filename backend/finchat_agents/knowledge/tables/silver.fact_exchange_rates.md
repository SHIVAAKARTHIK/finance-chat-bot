---
name: fact_exchange_rates
schema: silver
layer: silver
domain: gl
type: table
status: active
purpose: Currency exchange rates by rate type and validity dates.
grain: one row per HASH_KEY (one rate for a currency pair and date range)
primary_key:
- HASH_KEY
entity_column: null
period_columns:
- START_DATE
- END_DATE
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues: []
row_count: 35
proposed_fields:
- grain
- primary_key
reviewed: false
---

# fact_exchange_rates

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `RATE_TYPE_NAME` | string |  |  | `RATE_TYPE_NAME` |
| `FROM_CURRENCY` | string |  |  | `FROM_CURRENCY` |
| `TO_CURRENCY` | string |  |  | `TO_CURRENCY` |
| `START_DATE` | string |  |  | `START_DATE` |
| `RATE` | string |  |  | `RATE` |
| `END_DATE` | string |  |  | `END_DATE` |
| `CONVERSION_FACTOR` | string |  |  | `CONVERSION_FACTOR` |
| `RATE_TYPE_DESCRIPTION` | string |  |  | `RATE_TYPE_DESCRIPTION` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**RATE_TYPE_NAME**
- `Default`: 34 rows
- `Average`: 1 rows

**FROM_CURRENCY**
- `GBP`: 18 rows
- `EUR`: 13 rows
- `USD`: 3 rows
- `AUD`: 1 rows

**TO_CURRENCY**
- `USD`: 6 rows
- `SEK`: 5 rows
- `CAD`: 4 rows
- `NOK`: 4 rows
- `ZAR`: 4 rows
- `AUD`: 4 rows
- `NZD`: 3 rows
- `AED`: 3 rows
- `EUR`: 2 rows

**START_DATE**
- `2026-09-01 12:00:00.0000000 +00:00`: 18 rows
- `2026-08-01 12:00:00.0000000 +00:00`: 16 rows
- `2026-10-21 12:00:00.0000000 +00:00`: 1 rows

**RATE**
- `12.772`: 3 rows
- `1.1319`: 2 rows
- `11.3452`: 2 rows
- `1.8873`: 2 rows
- `1.6292`: 2 rows
- `54.1188999999999`: 2 rows
- `1.1703`: 2 rows
- `1.3248`: 2 rows
- `1.9067`: 2 rows
- `4.1571`: 1 rows
- `0.6948`: 1 rows
- `4.8658`: 1 rows
- `4.9704`: 1 rows
- `13.2737`: 1 rows
- `10.0231`: 1 rows
- `16.4355`: 1 rows
- `1.4247`: 1 rows
- `21.8476`: 1 rows
- `18.6034`: 1 rows
- `1.6126`: 1 rows
- `1.12`: 1 rows
- `2.2862`: 1 rows
- `10.9181`: 1 rows
- `13.0103`: 1 rows
- `21.7682`: 1 rows

**END_DATE**
- `2154-12-31 12:00:00.0000000 +00:00`: 22 rows
- `2026-08-31 12:00:00.0000000 +00:00`: 13 rows

**CONVERSION_FACTOR**
- `One`: 35 rows

**RATE_TYPE_DESCRIPTION**
- `Default global rate`: 34 rows
- `Default average rate`: 1 rows

**SOURCE_FILE_NAME**
- `exchangerates__20261116_105417.csv`: 35 rows

**MDP_CREATED_DATE**
- `2026-11-16 11:42:09.319360+00:00`: 35 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 11:42:09.319360+00:00`: 35 rows

## Profile

Rows in the latest export: 35.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `RATE_TYPE_NAME` | STRING | 2 | 0 | Average | Default |
| `FROM_CURRENCY` | STRING | 4 | 0 | AUD | USD |
| `TO_CURRENCY` | STRING | 9 | 0 | AED | ZAR |
| `START_DATE` | STRING | 3 | 0 | 2026-08-01 12:00:00.0000000 +00:00 | 2026-10-21 12:00:00.0000000 +00:00 |
| `RATE` | STRING | 25 | 0 | 0.6948 | 54.1188999999999 |
| `END_DATE` | STRING | 2 | 0 | 2026-08-31 12:00:00.0000000 +00:00 | 2154-12-31 12:00:00.0000000 +00:00 |
| `CONVERSION_FACTOR` | STRING | 1 | 0 | One | One |
| `RATE_TYPE_DESCRIPTION` | STRING | 2 | 0 | Default average rate | Default global rate |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | exchangerates__20261116_105417.csv | exchangerates__20261116_105417.csv |
| `HASH_KEY` | STRING | 36 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:42:09.319000 | 2026-11-16 11:42:09.319000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:42:09.319000 | 2026-11-16 11:42:09.319000 |

## Sample rows

| RATE_TYPE_NAME | FROM_CURRENCY | TO_CURRENCY | START_DATE | RATE | END_DATE | CONVERSION_FACTOR | RATE_TYPE_DESCRIPTION | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Average | EUR | USD | 2026-10-21 12:00:00.0000000 +00:00 | 1.12 | 2154-12-31 12:00:00.0000000 +00:00 | One | Default average rate | exchangerates__20261116_105417.csv | <masked> | 2026-11-16 11:42:09.319000 | <masked> | 2026-11-16 11:42:09.319000 |
| Default | GBP | EUR | 2026-09-01 12:00:00.0000000 +00:00 | 1.1703 | 2154-12-31 12:00:00.0000000 +00:00 | One | Default global rate | exchangerates__20261116_105417.csv | <masked> | 2026-11-16 11:42:09.319000 | <masked> | 2026-11-16 11:42:09.319000 |
| Default | GBP | USD | 2026-09-01 12:00:00.0000000 +00:00 | 1.3248 | 2154-12-31 12:00:00.0000000 +00:00 | One | Default global rate | exchangerates__20261116_105417.csv | <masked> | 2026-11-16 11:42:09.319000 | <masked> | 2026-11-16 11:42:09.319000 |
| Default | EUR | USD | 2026-09-01 12:00:00.0000000 +00:00 | 1.1319 | 2154-12-31 12:00:00.0000000 +00:00 | One | Default global rate | exchangerates__20261116_105417.csv | <masked> | 2026-11-16 11:42:09.319000 | <masked> | 2026-11-16 11:42:09.319000 |
| Default | GBP | CAD | 2026-08-01 12:00:00.0000000 +00:00 | 1.8873 | 2026-08-31 12:00:00.0000000 +00:00 | One | Default global rate | exchangerates__20261116_105417.csv | <masked> | 2026-11-16 11:42:09.319000 | <masked> | 2026-11-16 11:42:09.319000 |
