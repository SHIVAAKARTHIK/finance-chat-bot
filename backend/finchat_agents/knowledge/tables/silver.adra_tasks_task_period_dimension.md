---
name: adra_tasks_task_period_dimension
schema: silver
layer: silver
domain: recon
type: table
status: active
purpose: Calendar periods used by close tasks.
grain: one row per PERIOD_KEY (one period)
primary_key:
- PERIOD_KEY
entity_column: null
period_columns:
- PERIOD_NAME
- PERIOD_START
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues: []
row_count: 71
proposed_fields:
- grain
- primary_key
reviewed: false
---

# adra_tasks_task_period_dimension

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `PERIOD_KEY` | string |  |  | `PERIOD_KEY` |
| `FISCAL_YEAR_PERIOD_GUID` | string |  |  | `FISCAL_YEAR_PERIOD_GUID` |
| `PERIOD_CODE` | string |  |  | `PERIOD_CODE` |
| `PERIOD_NAME` | string |  |  | `PERIOD_NAME` |
| `PERIOD_SEQUENCE` | string |  |  | `PERIOD_SEQUENCE` |
| `PERIOD_START` | string |  |  | `PERIOD_START` |
| `PERIOD_END` | string |  |  | `PERIOD_END` |
| `PERIOD_FREQUENCY` | string |  |  | `PERIOD_FREQUENCY` |
| `ACTIVE` | string |  |  | `ACTIVE` |
| `PERIOD_CREATED_DATE` | string |  |  | `PERIOD_CREATED_DATE` |
| `FISCAL_YEAR_KEY` | string |  |  | `FISCAL_YEAR_KEY` |
| `FISCAL_YEAR_GUID` | string |  |  | `FISCAL_YEAR_GUID` |
| `FISCAL_YEAR_NAME` | string |  |  | `FISCAL_YEAR_NAME` |
| `FISCAL_YEAR_START` | string |  |  | `FISCAL_YEAR_START` |
| `FISCAL_YEAR_END` | string |  |  | `FISCAL_YEAR_END` |
| `ENGAGEMENT_ID` | string |  |  | `ENGAGEMENT_ID` |
| `ENGAGEMENT_KEY` | string |  |  | `ENGAGEMENT_KEY` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**PERIOD_CODE**
- `3`: 6 rows
- `7`: 6 rows
- `1`: 6 rows
- `8`: 6 rows
- `10`: 6 rows
- `5`: 6 rows
- `4`: 6 rows
- `11`: 6 rows
- `6`: 6 rows
- `9`: 6 rows
- `2`: 6 rows
- `12`: 5 rows

**PERIOD_SEQUENCE**
- `1`: 6 rows
- `8`: 6 rows
- `3`: 6 rows
- `6`: 6 rows
- `10`: 6 rows
- `2`: 6 rows
- `7`: 6 rows
- `5`: 6 rows
- `4`: 6 rows
- `9`: 6 rows
- `11`: 6 rows
- `12`: 5 rows

**PERIOD_FREQUENCY**
- `MonthEnd`: 48 rows
- `QuarterEnd`: 12 rows
- `HalfYearEnd`: 6 rows
- `YearEnd`: 5 rows

**ACTIVE**
- `False`: 59 rows
- `True`: 12 rows

**PERIOD_CREATED_DATE**
- `2026-10-17 15:46:28.0000000 +00:00`: 59 rows
- `2026-10-17 15:57:20.0000000 +00:00`: 12 rows

**FISCAL_YEAR_GUID**
- `04914d11-8062-433e-a568-85c68a847d1c`: 12 rows
- `a059d44a-98b5-4947-9800-9cbd48e6b487`: 12 rows
- `0bf5ef25-dca3-4220-9a54-274179383464`: 12 rows
- `6a31e17f-9ffb-41bd-a706-688c2c32fe93`: 12 rows
- `6f1c1f2f-7a2d-4d4a-8cae-a8bcdb38efe8`: 12 rows
- `a87d92b2-7a23-4b7a-8a0d-ef354ba345ab`: 11 rows

**FISCAL_YEAR_NAME**
- `FY21`: 12 rows
- `FY26`: 12 rows
- `FY22`: 12 rows
- `FY24`: 12 rows
- `FY23`: 12 rows
- `FY25`: 11 rows

**FISCAL_YEAR_START**
- `2022-01-01 00:00:00.0000000 +00:00`: 12 rows
- `2026-01-01 00:00:00.0000000 +00:00`: 12 rows
- `2024-01-01 00:00:00.0000000 +00:00`: 12 rows
- `2023-01-01 00:00:00.0000000 +00:00`: 12 rows
- `2021-01-01 00:00:00.0000000 +00:00`: 12 rows
- `2025-01-01 00:00:00.0000000 +00:00`: 11 rows

**FISCAL_YEAR_END**
- `2024-12-31 00:00:00.0000000 +00:00`: 12 rows
- `2026-12-31 00:00:00.0000000 +00:00`: 12 rows
- `2022-12-31 00:00:00.0000000 +00:00`: 12 rows
- `2021-12-31 00:00:00.0000000 +00:00`: 12 rows
- `2023-12-31 00:00:00.0000000 +00:00`: 12 rows
- `2025-12-31 00:00:00.0000000 +00:00`: 11 rows

**ENGAGEMENT_ID**
- `581`: 71 rows

**SOURCE_FILE_NAME**
- `perioddimension__20261116_174302.csv`: 71 rows

**MDP_CREATED_DATE**
- `2026-11-16 17:52:11.402764+00:00`: 71 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 17:52:11.402764+00:00`: 71 rows

## Profile

Rows in the latest export: 71.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `PERIOD_KEY` | STRING | 72 | 0 |  |  |
| `FISCAL_YEAR_PERIOD_GUID` | STRING | 68 | 0 | 046af9ee-76c0-46fc-ac3f-3f7821e66aba | ff40b98e-cc7c-4e9a-a458-87ca1e95daca |
| `PERIOD_CODE` | STRING | 12 | 0 | 1 | 12 |
| `PERIOD_NAME` | STRING | 71 | 0 |  |  |
| `PERIOD_SEQUENCE` | STRING | 12 | 0 | 1 | 9 |
| `PERIOD_START` | STRING | 72 | 0 | 2021-01-01 00:00:00.0000000 +00:00 | 2026-12-01 00:00:00.0000000 +00:00 |
| `PERIOD_END` | STRING | 73 | 0 | 2021-01-31 00:00:00.0000000 +00:00 | 2026-12-31 00:00:00.0000000 +00:00 |
| `PERIOD_FREQUENCY` | STRING | 4 | 0 | HalfYearEnd | YearEnd |
| `ACTIVE` | STRING | 2 | 0 | False | True |
| `PERIOD_CREATED_DATE` | STRING | 2 | 0 | 2026-10-17 15:46:28.0000000 +00:00 | 2026-10-17 15:57:20.0000000 +00:00 |
| `FISCAL_YEAR_KEY` | STRING | 6 | 0 |  |  |
| `FISCAL_YEAR_GUID` | STRING | 5 | 0 | 04914d11-8062-433e-a568-85c68a847d1c | a87d92b2-7a23-4b7a-8a0d-ef354ba345ab |
| `FISCAL_YEAR_NAME` | STRING | 6 | 0 | FY21 | FY26 |
| `FISCAL_YEAR_START` | STRING | 6 | 0 | 2021-01-01 00:00:00.0000000 +00:00 | 2026-01-01 00:00:00.0000000 +00:00 |
| `FISCAL_YEAR_END` | STRING | 6 | 0 | 2021-12-31 00:00:00.0000000 +00:00 | 2026-12-31 00:00:00.0000000 +00:00 |
| `ENGAGEMENT_ID` | STRING | 1 | 0 | 581 | 581 |
| `ENGAGEMENT_KEY` | STRING | 1 | 0 |  |  |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | perioddimension__20261116_174302.csv | perioddimension__20261116_174302.csv |
| `HASH_KEY` | STRING | 70 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 17:52:11.403000 | 2026-11-16 17:52:11.403000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 17:52:11.403000 | 2026-11-16 17:52:11.403000 |

## Sample rows

| FISCAL_YEAR_PERIOD_GUID | PERIOD_CODE | PERIOD_NAME | PERIOD_SEQUENCE | PERIOD_START | PERIOD_END | PERIOD_FREQUENCY | ACTIVE | PERIOD_CREATED_DATE | FISCAL_YEAR_GUID | FISCAL_YEAR_NAME | FISCAL_YEAR_START | FISCAL_YEAR_END | ENGAGEMENT_ID | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| c91c4585-3d43-4798-8167-fb7e89183d93 | 1 | (altered in export) | 1 | 2025-01-01 00:00:00.0000000 +00:00 | 2025-01-31 00:00:00.0000000 +00:00 | MonthEnd | False | 2026-10-17 15:46:28.0000000 +00:00 | a87d92b2-7a23-4b7a-8a0d-ef354ba345ab | FY25 | 2025-01-01 00:00:00.0000000 +00:00 | 2025-12-31 00:00:00.0000000 +00:00 | 581 | perioddimension__20261116_174302.csv | <masked> | 2026-11-16 17:52:11.403000 | <masked> | 2026-11-16 17:52:11.403000 |
| 5a62ef15-04e3-4522-9f37-4c13bb28d65c | 2 | (altered in export) | 2 | 2025-02-01 00:00:00.0000000 +00:00 | 2025-02-28 00:00:00.0000000 +00:00 | MonthEnd | False | 2026-10-17 15:46:28.0000000 +00:00 | a87d92b2-7a23-4b7a-8a0d-ef354ba345ab | FY25 | 2025-01-01 00:00:00.0000000 +00:00 | 2025-12-31 00:00:00.0000000 +00:00 | 581 | perioddimension__20261116_174302.csv | <masked> | 2026-11-16 17:52:11.403000 | <masked> | 2026-11-16 17:52:11.403000 |
| f05e68f0-23e7-4743-b35f-3039c2df7d9f | 3 | (altered in export) | 3 | 2025-03-01 00:00:00.0000000 +00:00 | 2025-03-31 00:00:00.0000000 +00:00 | QuarterEnd | False | 2026-10-17 15:46:28.0000000 +00:00 | a87d92b2-7a23-4b7a-8a0d-ef354ba345ab | FY25 | 2025-01-01 00:00:00.0000000 +00:00 | 2025-12-31 00:00:00.0000000 +00:00 | 581 | perioddimension__20261116_174302.csv | <masked> | 2026-11-16 17:52:11.403000 | <masked> | 2026-11-16 17:52:11.403000 |
| aa22e522-514c-4739-832a-8c99d7363bc1 | 4 | (altered in export) | 4 | 2025-04-01 00:00:00.0000000 +00:00 | 2025-04-30 00:00:00.0000000 +00:00 | MonthEnd | False | 2026-10-17 15:46:28.0000000 +00:00 | a87d92b2-7a23-4b7a-8a0d-ef354ba345ab | FY25 | 2025-01-01 00:00:00.0000000 +00:00 | 2025-12-31 00:00:00.0000000 +00:00 | 581 | perioddimension__20261116_174302.csv | <masked> | 2026-11-16 17:52:11.403000 | <masked> | 2026-11-16 17:52:11.403000 |
| 7607e490-5970-4c37-9f3d-fe07213a7ee0 | 5 | (altered in export) | 5 | 2025-05-01 00:00:00.0000000 +00:00 | 2025-05-31 00:00:00.0000000 +00:00 | MonthEnd | False | 2026-10-17 15:46:28.0000000 +00:00 | a87d92b2-7a23-4b7a-8a0d-ef354ba345ab | FY25 | 2025-01-01 00:00:00.0000000 +00:00 | 2025-12-31 00:00:00.0000000 +00:00 | 581 | perioddimension__20261116_174302.csv | <masked> | 2026-11-16 17:52:11.403000 | <masked> | 2026-11-16 17:52:11.403000 |
