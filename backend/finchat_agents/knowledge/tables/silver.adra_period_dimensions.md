---
name: adra_period_dimensions
schema: silver
layer: silver
domain: recon
type: dim
status: active
purpose: 'ADRA fiscal periods per legal entity: period label (e.g. ''Feb 25''), fiscal year, start and end dates and status.
  Use it to turn the period a user names into PERIOD_KEY values.'
grain: one row per period per legal entity (PERIOD_KEY, ENGAGEMENT_KEY, LEGAL_ENTITY_KEY)
primary_key:
- PERIOD_KEY
- ENGAGEMENT_KEY
- LEGAL_ENTITY_KEY
entity_column: LEGAL_ENTITY_KEY
period_columns:
- PERIOD_NAME
- PERIOD_END
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms:
- period
- periods
- fiscal period
- month
- month end
- period status
- fiscal year
- latest period
known_issues:
- code: all_string_columns
  note: Every column is stored as STRING. Cast PERIOD_START / PERIOD_END to DATE before comparing.
reviewed: true
proposed_fields: []
row_count: 9
---

# adra_period_dimensions

ADRA fiscal periods per legal entity: period label (e.g. 'Feb 25'), fiscal year, start and end dates and status.
Use it to turn the period a user names into PERIOD_KEY values.

> Period labels are 'Mon YY' ('Feb 25' = February 2025, 'Oct 26' = October 2026). Each entity has its own periods,
> so always join with the full key (PERIOD_KEY, ENGAGEMENT_KEY, LEGAL_ENTITY_KEY).

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `PERIOD_KEY` | string | Period key (join with ENGAGEMENT_KEY and LEGAL_ENTITY_KEY). |  | `trim(PERIOD_KEY)` |
| `ENGAGEMENT_KEY` | string | Engagement key. |  | `trim(ENGAGEMENT_KEY)` |
| `LEGAL_ENTITY_KEY` | string | Legal entity key. |  | `trim(LEGAL_ENTITY_KEY)` |
| `PERIOD_NAME` | string | Period label as users say it, 'Mon YY'. | period, month, period name | `trim(PERIOD_NAME)` |
| `PERIOD` | string | Period end date followed by the label, e.g. '2025-02-28 Feb 25'. Filter on PERIOD_NAME instead. | period label with date | `trim(PERIOD)` |
| `FISCAL_YEAR_NAME` | string | Fiscal year label. | fiscal year | `trim(FISCAL_YEAR_NAME)` |
| `PERIOD_START` | date | First day of the period. | period start | `TRY_CAST(PERIOD_START AS DATE)` |
| `PERIOD_END` | date | Last day of the period (use for "latest period"). | period end, month end | `TRY_CAST(PERIOD_END AS DATE)` |
| `PERIOD_STATUS` | string | Period status. | period status, open period, closed period | `trim(PERIOD_STATUS)` |
| `FISCAL_YEAR_START` | string |  |  | `FISCAL_YEAR_START` |
| `FISCAL_YEAR_END` | string |  |  | `FISCAL_YEAR_END` |
| `PERIOD_SEQUENCE` | string |  |  | `PERIOD_SEQUENCE` |
| `PERIOD_FREQUENCY` | string |  |  | `PERIOD_FREQUENCY` |
| `PERIOD_CREATED_DATE` | string |  |  | `PERIOD_CREATED_DATE` |
| `FISCAL_YEAR_PERIOD_ID` | string |  |  | `FISCAL_YEAR_PERIOD_ID` |
| `FISCAL_YEAR_PERIOD_GUID` | string |  |  | `FISCAL_YEAR_PERIOD_GUID` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**PERIOD_STATUS**
- `Opened`: period open (the only value in the November 2026 export)

**FISCAL_YEAR_NAME**
- `FY26`: 8 rows
- `FY25`: 1 rows

**FISCAL_YEAR_START**
- `2026-01-01 00:00:00.0000000 +00:00`: 8 rows
- `2025-01-01 00:00:00.0000000 +00:00`: 1 rows

**FISCAL_YEAR_END**
- `2026-12-31 00:00:00.0000000 +00:00`: 8 rows
- `2025-12-31 00:00:00.0000000 +00:00`: 1 rows

**PERIOD**
- `2026-09-30 Sep 26`: 6 rows
- `2026-10-31 Oct 26`: 2 rows
- `2025-02-28 Feb 25`: 1 rows

**PERIOD_SEQUENCE**
- `9`: 6 rows
- `10`: 2 rows
- `2`: 1 rows

**PERIOD_START**
- `2026-09-01 00:00:00.0000000 +00:00`: 6 rows
- `2026-10-01 00:00:00.0000000 +00:00`: 2 rows
- `2025-02-01 00:00:00.0000000 +00:00`: 1 rows

**PERIOD_END**
- `2026-09-30 00:00:00.0000000 +00:00`: 6 rows
- `2026-10-31 00:00:00.0000000 +00:00`: 2 rows
- `2025-02-28 00:00:00.0000000 +00:00`: 1 rows

**PERIOD_FREQUENCY**
- `Quarter end`: 6 rows
- `Month end`: 3 rows

**PERIOD_CREATED_DATE**
- `2026-11-16 09:38:29.0000000 +00:00`: 2 rows
- `2026-10-23 10:47:28.0000000 +00:00`: 1 rows
- `2026-11-16 09:38:22.0000000 +00:00`: 1 rows
- `2026-10-29 05:52:29.0000000 +00:00`: 1 rows
- `2026-11-16 09:38:28.0000000 +00:00`: 1 rows
- `2026-11-16 09:38:27.0000000 +00:00`: 1 rows
- `2026-10-18 09:40:48.0000000 +00:00`: 1 rows
- `2026-11-16 09:38:21.0000000 +00:00`: 1 rows

**FISCAL_YEAR_PERIOD_ID**
- `29004`: 6 rows
- `29005`: 2 rows
- `16025`: 1 rows

**FISCAL_YEAR_PERIOD_GUID**
- `7d5727bb-5abb-437e-b237-8885e00774b3`: 6 rows
- `ca744d3a-6ee3-4f5e-b4b4-da3977098f35`: 2 rows
- `5a62ef15-04e3-4522-9f37-4c13bb28d65c`: 1 rows

**SOURCE_FILE_NAME**
- `perioddimensions__20261116_194202.csv`: 9 rows

**MDP_CREATED_DATE**
- `2026-11-16 19:45:18.855721+00:00`: 9 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 19:45:18.855721+00:00`: 9 rows

## Joins (approved, use the full key)

| Join | To table | Cardinality |
|---|---|---|
| `account_fact_to_period` | `adra_account_facts` | many-to-one (from the fact) |
| `transaction_fact_to_period` | `adra_transaction_facts` | many-to-one (from the fact) |

## Notes

- "Latest period" for an entity = the period with the greatest PERIOD_END that has fact rows for that entity.
- If the requested period has no fact rows, say so and name the periods that do have data; do not fall back silently.
- Comparing with a previous period needs fact rows for both periods; if one is missing, say the comparison cannot be made.

## Profile

Rows in the latest export: 9.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `PERIOD_KEY` | STRING | 9 | 0 |  |  |
| `ENGAGEMENT_KEY` | STRING | 1 | 0 |  |  |
| `LEGAL_ENTITY_KEY` | STRING | 9 | 0 |  |  |
| `FISCAL_YEAR_NAME` | STRING | 2 | 0 | FY25 | FY26 |
| `FISCAL_YEAR_START` | STRING | 2 | 0 | 2025-01-01 00:00:00.0000000 +00:00 | 2026-01-01 00:00:00.0000000 +00:00 |
| `FISCAL_YEAR_END` | STRING | 2 | 0 | 2025-12-31 00:00:00.0000000 +00:00 | 2026-12-31 00:00:00.0000000 +00:00 |
| `PERIOD` | STRING | 3 | 0 | 2025-02-28 Feb 25 | 2026-10-31 Oct 26 |
| `PERIOD_NAME` | STRING | 3 | 0 |  |  |
| `PERIOD_SEQUENCE` | STRING | 3 | 0 | 10 | 9 |
| `PERIOD_START` | STRING | 3 | 0 | 2025-02-01 00:00:00.0000000 +00:00 | 2026-10-01 00:00:00.0000000 +00:00 |
| `PERIOD_END` | STRING | 3 | 0 | 2025-02-28 00:00:00.0000000 +00:00 | 2026-10-31 00:00:00.0000000 +00:00 |
| `PERIOD_FREQUENCY` | STRING | 2 | 0 | Month end | Quarter end |
| `PERIOD_STATUS` | STRING | 1 | 0 | Opened | Opened |
| `PERIOD_CREATED_DATE` | STRING | 8 | 0 | 2026-10-18 09:40:48.0000000 +00:00 | 2026-11-16 09:38:29.0000000 +00:00 |
| `FISCAL_YEAR_PERIOD_ID` | STRING | 3 | 0 | 16025 | 29005 |
| `FISCAL_YEAR_PERIOD_GUID` | STRING | 3 | 0 | 5a62ef15-04e3-4522-9f37-4c13bb28d65c | ca744d3a-6ee3-4f5e-b4b4-da3977098f35 |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | perioddimensions__20261116_194202.csv | perioddimensions__20261116_194202.csv |
| `HASH_KEY` | STRING | 9 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 19:45:18.856000 | 2026-11-16 19:45:18.856000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 19:45:18.856000 | 2026-11-16 19:45:18.856000 |

## Sample rows

| FISCAL_YEAR_NAME | FISCAL_YEAR_START | FISCAL_YEAR_END | PERIOD | PERIOD_NAME | PERIOD_SEQUENCE | PERIOD_START | PERIOD_END | PERIOD_FREQUENCY | PERIOD_STATUS | PERIOD_CREATED_DATE | FISCAL_YEAR_PERIOD_ID | FISCAL_YEAR_PERIOD_GUID | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FY26 | 2026-01-01 00:00:00.0000000 +00:00 | 2026-12-31 00:00:00.0000000 +00:00 | 2026-10-31 Oct 26 | (altered in export) | 10 | 2026-10-01 00:00:00.0000000 +00:00 | 2026-10-31 00:00:00.0000000 +00:00 | Month end | Opened | 2026-10-18 09:40:48.0000000 +00:00 | 29005 | ca744d3a-6ee3-4f5e-b4b4-da3977098f35 | perioddimensions__20261116_194202.csv | <masked> | 2026-11-16 19:45:18.856000 | <masked> | 2026-11-16 19:45:18.856000 |
| FY25 | 2025-01-01 00:00:00.0000000 +00:00 | 2025-12-31 00:00:00.0000000 +00:00 | 2025-02-28 Feb 25 | (altered in export) | 2 | 2025-02-01 00:00:00.0000000 +00:00 | 2025-02-28 00:00:00.0000000 +00:00 | Month end | Opened | 2026-10-23 10:47:28.0000000 +00:00 | 16025 | 5a62ef15-04e3-4522-9f37-4c13bb28d65c | perioddimensions__20261116_194202.csv | <masked> | 2026-11-16 19:45:18.856000 | <masked> | 2026-11-16 19:45:18.856000 |
| FY26 | 2026-01-01 00:00:00.0000000 +00:00 | 2026-12-31 00:00:00.0000000 +00:00 | 2026-10-31 Oct 26 | (altered in export) | 10 | 2026-10-01 00:00:00.0000000 +00:00 | 2026-10-31 00:00:00.0000000 +00:00 | Month end | Opened | 2026-10-29 05:52:29.0000000 +00:00 | 29005 | ca744d3a-6ee3-4f5e-b4b4-da3977098f35 | perioddimensions__20261116_194202.csv | <masked> | 2026-11-16 19:45:18.856000 | <masked> | 2026-11-16 19:45:18.856000 |
| FY26 | 2026-01-01 00:00:00.0000000 +00:00 | 2026-12-31 00:00:00.0000000 +00:00 | 2026-09-30 Sep 26 | (altered in export) | 9 | 2026-09-01 00:00:00.0000000 +00:00 | 2026-09-30 00:00:00.0000000 +00:00 | Quarter end | Opened | 2026-11-16 09:38:21.0000000 +00:00 | 29004 | 7d5727bb-5abb-437e-b237-8885e00774b3 | perioddimensions__20261116_194202.csv | <masked> | 2026-11-16 19:45:18.856000 | <masked> | 2026-11-16 19:45:18.856000 |
| FY26 | 2026-01-01 00:00:00.0000000 +00:00 | 2026-12-31 00:00:00.0000000 +00:00 | 2026-09-30 Sep 26 | (altered in export) | 9 | 2026-09-01 00:00:00.0000000 +00:00 | 2026-09-30 00:00:00.0000000 +00:00 | Quarter end | Opened | 2026-11-16 09:38:22.0000000 +00:00 | 29004 | 7d5727bb-5abb-437e-b237-8885e00774b3 | perioddimensions__20261116_194202.csv | <masked> | 2026-11-16 19:45:18.856000 | <masked> | 2026-11-16 19:45:18.856000 |
