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
- `3`
- `7`
- `1`
- `8`
- `10`
- `5`
- `4`
- `11`
- `6`
- `9`
- `2`
- `12`

**PERIOD_SEQUENCE**
- `1`
- `8`
- `3`
- `6`
- `10`
- `2`
- `7`
- `5`
- `4`
- `9`
- `11`
- `12`

**PERIOD_FREQUENCY**
- `MonthEnd`
- `QuarterEnd`
- `HalfYearEnd`
- `YearEnd`

**ACTIVE**
- `False`
- `True`

**PERIOD_CREATED_DATE**
- `2026-10-17 15:46:28.0000000 +00:00`
- `2026-10-17 15:57:20.0000000 +00:00`

**FISCAL_YEAR_GUID**
- `04914d11-8062-433e-a568-85c68a847d1c`
- `a059d44a-98b5-4947-9800-9cbd48e6b487`
- `0bf5ef25-dca3-4220-9a54-274179383464`
- `6a31e17f-9ffb-41bd-a706-688c2c32fe93`
- `6f1c1f2f-7a2d-4d4a-8cae-a8bcdb38efe8`
- `a87d92b2-7a23-4b7a-8a0d-ef354ba345ab`

**FISCAL_YEAR_NAME**
- `FY21`
- `FY26`
- `FY22`
- `FY24`
- `FY23`
- `FY25`

**FISCAL_YEAR_START**
- `2022-01-01 00:00:00.0000000 +00:00`
- `2026-01-01 00:00:00.0000000 +00:00`
- `2024-01-01 00:00:00.0000000 +00:00`
- `2023-01-01 00:00:00.0000000 +00:00`
- `2021-01-01 00:00:00.0000000 +00:00`
- `2025-01-01 00:00:00.0000000 +00:00`

**FISCAL_YEAR_END**
- `2024-12-31 00:00:00.0000000 +00:00`
- `2026-12-31 00:00:00.0000000 +00:00`
- `2022-12-31 00:00:00.0000000 +00:00`
- `2021-12-31 00:00:00.0000000 +00:00`
- `2023-12-31 00:00:00.0000000 +00:00`
- `2025-12-31 00:00:00.0000000 +00:00`

**ENGAGEMENT_ID**
- `581`

**SOURCE_FILE_NAME**
- `perioddimension__20261116_174302.csv`

**MDP_CREATED_DATE**
- `2026-11-16 17:52:11.402764+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 17:52:11.402764+00:00`
