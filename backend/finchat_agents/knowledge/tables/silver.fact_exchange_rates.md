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
- `Default`
- `Average`

**FROM_CURRENCY**
- `GBP`
- `EUR`
- `USD`
- `AUD`

**TO_CURRENCY**
- `USD`
- `SEK`
- `CAD`
- `NOK`
- `ZAR`
- `AUD`
- `NZD`
- `AED`
- `EUR`

**START_DATE**
- `2026-09-01 12:00:00.0000000 +00:00`
- `2026-08-01 12:00:00.0000000 +00:00`
- `2026-10-21 12:00:00.0000000 +00:00`

**RATE**
- `12.772`
- `1.1319`
- `11.3452`
- `1.8873`
- `1.6292`
- `54.1188999999999`
- `1.1703`
- `1.3248`
- `1.9067`
- `4.1571`
- `0.6948`
- `4.8658`
- `4.9704`
- `13.2737`
- `10.0231`
- `16.4355`
- `1.4247`
- `21.8476`
- `18.6034`
- `1.6126`
- `1.12`
- `2.2862`
- `10.9181`
- `13.0103`
- `21.7682`

**END_DATE**
- `2154-12-31 12:00:00.0000000 +00:00`
- `2026-08-31 12:00:00.0000000 +00:00`

**CONVERSION_FACTOR**
- `One`

**RATE_TYPE_DESCRIPTION**
- `Default global rate`
- `Default average rate`

**SOURCE_FILE_NAME**
- `exchangerates__20261116_105417.csv`

**MDP_CREATED_DATE**
- `2026-11-16 11:42:09.319360+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 11:42:09.319360+00:00`
