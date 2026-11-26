---
name: fact_trail_balance_extractions
schema: silver
layer: silver
domain: gl
type: table
status: active
purpose: Trial balance extract per company and GL account with opening; debit; credit and closing.
grain: one row per COMPANY + GL_ACCOUNT per extract load (one account balance in one extract)
primary_key: []
entity_column: COMPANY
period_columns: []
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues:
- code: duplicates
  note: 104 exact duplicate rows in the latest export (5.6%). Check duplicates at the grain before counting or summing; warn
    the user.
proposed_fields: []
reviewed: false
---

# fact_trail_balance_extractions

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `COMPANY` | string |  |  | `COMPANY` |
| `CLOSING_BALANCE` | string |  |  | `CLOSING_BALANCE` |
| `GL_ACCOUNT` | string |  |  | `GL_ACCOUNT` |
| `COST_CENTER` | string |  |  | `COST_CENTER` |
| `LOCATION` | string |  |  | `LOCATION` |
| `DEBIT` | string |  |  | `DEBIT` |
| `OPENING_BALANCE` | string |  |  | `OPENING_BALANCE` |
| `CREDIT` | string |  |  | `CREDIT` |
| `TYPE` | string |  |  | `TYPE` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**COST_CENTER**
- `None`

**LOCATION**
- `None`

**TYPE**
- `Asset`
- `Expense`
- `Liability`
- `None`
- `Revenue`
- `ProfitAndLoss`
- `Equity`

**SOURCE_FILE_NAME**
- `trailbalanceextractions__20261028_171803.csv`
- `trailbalanceextractions__20261022_184801.csv`
- `trailbalanceextractions__20261112_083009.csv`
- `trailbalanceextractions__20261106_083011.csv`
- `trailbalanceextractions__20261110_083018.csv`
- `trailbalanceextractions__20261107_083013.csv`
- `trailbalanceextractions__20261105_083003.csv`
- `trailbalanceextractions__20261111_083004.csv`
- `trailbalanceextractions__20261113_083001.csv`
- `trailbalanceextractions__20261103_124509.csv`
- `trailbalanceextractions__20261104_113725.csv`
- `trailbalanceextractions__20261108_083003.csv`
- `trailbalanceextractions__20261109_083011.csv`
- `Trail_Balance_Extract.csv`
- `trailbalanceextractions__20261026_174802.csv`
- `trailbalanceextractions__20261025_174801.csv`
- `trailbalanceextractions__20261027_153310.csv`
- `trailbalanceextractions__20261024_174802.csv`
- `trailbalanceextractions__20261029_053613.csv`
- `trailbalanceextractions__20261023_174802.csv`

**MDP_CREATED_DATE**
- `2026-10-22 19:23:45.647000+00:00`
- `2026-11-12 08:34:42.631335+00:00`
- `2026-10-28 19:26:09.899388+00:00`
- `2026-11-09 08:42:57.911778+00:00`
- `2026-11-07 08:41:29.753552+00:00`
- `2026-11-11 08:41:42.881030+00:00`
- `2026-11-06 08:44:07.276451+00:00`
- `2026-11-05 08:43:46.765970+00:00`
- `2026-11-04 11:40:23.854714+00:00`
- `2026-11-03 12:50:33.081873+00:00`
- `2026-11-13 08:41:25.335897+00:00`
- `2026-11-10 08:41:32.431204+00:00`
- `2026-11-08 08:40:40.475912+00:00`
- `2026-11-16 06:51:42.122347+00:00`
- `2026-10-28 19:26:09.899000+00:00`
- `2026-10-25 19:23:45.647000+00:00`
- `2026-10-24 19:23:45.647000+00:00`
- `2026-10-27 19:23:45.647000+00:00`
- `2026-10-26 19:23:45.647000+00:00`
- `2026-10-29 05:43:08.958221+00:00`
- `2026-10-23 19:23:45.647000+00:00`

**MDP_MODIFIED_DATE**
- `2026-10-22 19:23:45.647000+00:00`
- `2026-11-12 08:34:42.631335+00:00`
- `2026-10-28 19:26:09.899388+00:00`
- `2026-11-09 08:42:57.911778+00:00`
- `2026-11-07 08:41:29.753552+00:00`
- `2026-11-11 08:41:42.881030+00:00`
- `2026-11-06 08:44:07.276451+00:00`
- `2026-11-05 08:43:46.765970+00:00`
- `2026-11-04 11:40:23.854714+00:00`
- `2026-11-03 12:50:33.081873+00:00`
- `2026-11-13 08:41:25.335897+00:00`
- `2026-11-10 08:41:32.431204+00:00`
- `2026-11-08 08:40:40.475912+00:00`
- `2026-11-16 06:51:42.122347+00:00`
- `2026-10-28 19:26:09.899000+00:00`
- `2026-10-25 19:23:45.647000+00:00`
- `2026-10-24 19:23:45.647000+00:00`
- `2026-10-27 19:23:45.647000+00:00`
- `2026-10-26 19:23:45.647000+00:00`
- `2026-10-29 05:43:08.958221+00:00`
- `2026-10-23 19:23:45.647000+00:00`

## Empty columns

Empty in every row: `COST_CENTER`, `LOCATION`. Do not filter or group on them.
