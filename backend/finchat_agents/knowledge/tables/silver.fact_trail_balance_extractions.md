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
row_count: 1847
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
- `None`: 1847 rows

**LOCATION**
- `None`: 1847 rows

**TYPE**
- `Asset`: 735 rows
- `Expense`: 497 rows
- `Liability`: 263 rows
- `None`: 163 rows
- `Revenue`: 130 rows
- `ProfitAndLoss`: 31 rows
- `Equity`: 28 rows

**SOURCE_FILE_NAME**
- `trailbalanceextractions__20261028_171803.csv`: 208 rows
- `trailbalanceextractions__20261022_184801.csv`: 208 rows
- `trailbalanceextractions__20261112_083009.csv`: 174 rows
- `trailbalanceextractions__20261106_083011.csv`: 87 rows
- `trailbalanceextractions__20261110_083018.csv`: 87 rows
- `trailbalanceextractions__20261107_083013.csv`: 87 rows
- `trailbalanceextractions__20261105_083003.csv`: 87 rows
- `trailbalanceextractions__20261111_083004.csv`: 87 rows
- `trailbalanceextractions__20261113_083001.csv`: 87 rows
- `trailbalanceextractions__20261103_124509.csv`: 87 rows
- `trailbalanceextractions__20261104_113725.csv`: 87 rows
- `trailbalanceextractions__20261108_083003.csv`: 87 rows
- `trailbalanceextractions__20261109_083011.csv`: 87 rows
- `Trail_Balance_Extract.csv`: 76 rows
- `trailbalanceextractions__20261026_174802.csv`: 52 rows
- `trailbalanceextractions__20261025_174801.csv`: 52 rows
- `trailbalanceextractions__20261027_153310.csv`: 52 rows
- `trailbalanceextractions__20261024_174802.csv`: 52 rows
- `trailbalanceextractions__20261029_053613.csv`: 52 rows
- `trailbalanceextractions__20261023_174802.csv`: 51 rows

**MDP_CREATED_DATE**
- `2026-10-22 19:23:45.647000+00:00`: 208 rows
- `2026-11-12 08:34:42.631335+00:00`: 174 rows
- `2026-10-28 19:26:09.899388+00:00`: 156 rows
- `2026-11-09 08:42:57.911778+00:00`: 87 rows
- `2026-11-07 08:41:29.753552+00:00`: 87 rows
- `2026-11-11 08:41:42.881030+00:00`: 87 rows
- `2026-11-06 08:44:07.276451+00:00`: 87 rows
- `2026-11-05 08:43:46.765970+00:00`: 87 rows
- `2026-11-04 11:40:23.854714+00:00`: 87 rows
- `2026-11-03 12:50:33.081873+00:00`: 87 rows
- `2026-11-13 08:41:25.335897+00:00`: 87 rows
- `2026-11-10 08:41:32.431204+00:00`: 87 rows
- `2026-11-08 08:40:40.475912+00:00`: 87 rows
- `2026-11-16 06:51:42.122347+00:00`: 76 rows
- `2026-10-28 19:26:09.899000+00:00`: 52 rows
- `2026-10-25 19:23:45.647000+00:00`: 52 rows
- `2026-10-24 19:23:45.647000+00:00`: 52 rows
- `2026-10-27 19:23:45.647000+00:00`: 52 rows
- `2026-10-26 19:23:45.647000+00:00`: 52 rows
- `2026-10-29 05:43:08.958221+00:00`: 52 rows
- `2026-10-23 19:23:45.647000+00:00`: 51 rows

**MDP_MODIFIED_DATE**
- `2026-10-22 19:23:45.647000+00:00`: 208 rows
- `2026-11-12 08:34:42.631335+00:00`: 174 rows
- `2026-10-28 19:26:09.899388+00:00`: 156 rows
- `2026-11-09 08:42:57.911778+00:00`: 87 rows
- `2026-11-07 08:41:29.753552+00:00`: 87 rows
- `2026-11-11 08:41:42.881030+00:00`: 87 rows
- `2026-11-06 08:44:07.276451+00:00`: 87 rows
- `2026-11-05 08:43:46.765970+00:00`: 87 rows
- `2026-11-04 11:40:23.854714+00:00`: 87 rows
- `2026-11-03 12:50:33.081873+00:00`: 87 rows
- `2026-11-13 08:41:25.335897+00:00`: 87 rows
- `2026-11-10 08:41:32.431204+00:00`: 87 rows
- `2026-11-08 08:40:40.475912+00:00`: 87 rows
- `2026-11-16 06:51:42.122347+00:00`: 76 rows
- `2026-10-28 19:26:09.899000+00:00`: 52 rows
- `2026-10-25 19:23:45.647000+00:00`: 52 rows
- `2026-10-24 19:23:45.647000+00:00`: 52 rows
- `2026-10-27 19:23:45.647000+00:00`: 52 rows
- `2026-10-26 19:23:45.647000+00:00`: 52 rows
- `2026-10-29 05:43:08.958221+00:00`: 52 rows
- `2026-10-23 19:23:45.647000+00:00`: 51 rows

## Profile

Rows in the latest export: 1847.
Exact duplicate rows: 104.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `COMPANY` | STRING | 7 | 0 |  |  |
| `CLOSING_BALANCE` | STRING | 388 | 87 | -110908 | 99713.1 |
| `GL_ACCOUNT` | STRING | 220 | 87 | 101413 | 999900 |
| `COST_CENTER` | STRING | 0 | 1847 |  |  |
| `LOCATION` | STRING | 0 | 1847 |  |  |
| `DEBIT` | STRING | 260 | 0 | 0 | 99713.1 |
| `OPENING_BALANCE` | STRING | 67 | 87 | -0.04 | 9944 |
| `CREDIT` | STRING | 211 | 0 | 0 | 993654.3 |
| `TYPE` | STRING | 6 | 163 | Asset | Revenue |
| `SOURCE_FILE_NAME` | STRING | 18 | 0 | Trail_Balance_Extract.csv | trailbalanceextractions__20261113_083... |
| `HASH_KEY` | STRING | 1616 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 20 | 0 | 2026-10-22 19:23:45.647000 | 2026-11-16 06:51:42.122000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 20 | 0 | 2026-10-22 19:23:45.647000 | 2026-11-16 06:51:42.122000 |

## Sample rows

| CLOSING_BALANCE | GL_ACCOUNT | COST_CENTER | LOCATION | DEBIT | OPENING_BALANCE | CREDIT | TYPE | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 26167 | 102100 | NULL | NULL | 26167 | 0 | 0 | Asset | trailbalanceextractions__20261109_083... | <masked> | 2026-11-09 08:42:57.912000 | <masked> | 2026-11-09 08:42:57.912000 |
| -15853 | 102403 | NULL | NULL | 0 | 0 | 15853 | Asset | trailbalanceextractions__20261109_083... | <masked> | 2026-11-09 08:42:57.912000 | <masked> | 2026-11-09 08:42:57.912000 |
| 45563 | 103703 | NULL | NULL | 45563 | 0 | 0 | Asset | trailbalanceextractions__20261109_083... | <masked> | 2026-11-09 08:42:57.912000 | <masked> | 2026-11-09 08:42:57.912000 |
| 160552 | 103803 | NULL | NULL | 160552 | 0 | 0 | Asset | trailbalanceextractions__20261109_083... | <masked> | 2026-11-09 08:42:57.912000 | <masked> | 2026-11-09 08:42:57.912000 |
| 143544 | 109050 | NULL | NULL | 224290 | 0 | 80746 | Asset | trailbalanceextractions__20261109_083... | <masked> | 2026-11-09 08:42:57.912000 | <masked> | 2026-11-09 08:42:57.912000 |
