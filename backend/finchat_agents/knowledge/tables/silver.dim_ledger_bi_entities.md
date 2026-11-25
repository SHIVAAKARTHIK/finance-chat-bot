---
name: dim_ledger_bi_entities
schema: silver
layer: silver
domain: gl
type: table
status: active
purpose: D365 ledger setup per legal entity (currencies; chart of accounts).
grain: one row per source_key (one ledger)
primary_key:
- source_key
entity_column: name
period_columns: []
pii_columns: []
synonyms: []
built_from: []
known_issues: []
row_count: 26
proposed_fields:
- grain
- primary_key
reviewed: false
---

# dim_ledger_bi_entities

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `name` | string |  |  | `name` |
| `reporting_currency` | string |  |  | `reporting_currency` |
| `fiscal_calendar` | string |  |  | `fiscal_calendar` |
| `budget_exchange_rate_type` | string |  |  | `budget_exchange_rate_type` |
| `accounting_currency` | string |  |  | `accounting_currency` |
| `is_budget_control_enabled` | string |  |  | `is_budget_control_enabled` |
| `chart_of_accounts` | string |  |  | `chart_of_accounts` |
| `description` | string |  |  | `description` |
| `source_key` | string |  |  | `source_key` |
| `default_exchange_rate_type` | string |  |  | `default_exchange_rate_type` |
| `reporting_currency_exchange_rate_type` | string |  |  | `reporting_currency_exchange_rate_type` |
| `primary_for_legal_entity` | string |  |  | `primary_for_legal_entity` |

## Values

**reporting_currency**
- `USD`: 21 rows
- `None`: 5 rows

**fiscal_calendar**
- `5637144576`: 25 rows
- `0`: 1 rows

**budget_exchange_rate_type**
- `0`: 26 rows

**accounting_currency**
- `USD`: 25 rows
- `None`: 1 rows

**is_budget_control_enabled**
- `No`: 26 rows

**chart_of_accounts**
- `5637144577`: 18 rows
- `5637145326`: 5 rows
- `5637146076`: 2 rows
- `0`: 1 rows

**description**
- `Tower Hill Prime Insurance Co.`: 1 rows
- `Tower Hill E&S Insurance Exchange`: 1 rows
- `Tower Hill Insurance Managers`: 1 rows
- `Tower Hill Re Holdings`: 1 rows
- `Tomoka Re Holdings`: 1 rows
- `Tower Hill Re`: 1 rows
- `Tower Hill Specialty Group LLC`: 1 rows
- `Tower Hill Claims Service`: 1 rows
- `Lovable 3`: 1 rows
- `Rock-It Cargo USA LLC`: 1 rows
- `THIG Agency`: 1 rows
- `Lovable 4`: 1 rows
- `Tower Hill Insurance Exchange`: 1 rows
- `Cars USA Shipping LLC`: 1 rows
- `Bluegrass Insurance Management`: 1 rows
- `Tower Hill Holdings`: 1 rows
- `Lovable 5`: 1 rows
- `Tower Hill Specialty LLC`: 1 rows
- `Tower Hill Risk Management LLC`: 1 rows
- `Tower Hill Insurance Holdings`: 1 rows
- `THIG`: 1 rows
- `Company accounts data`: 1 rows
- `Tower Hill Preferred Insurance Co.`: 1 rows
- `Tower Hill E&S Risk Management`: 1 rows
- `Lovable 2`: 1 rows
- `Lovable 1`: 1 rows

**default_exchange_rate_type**
- `0`: 25 rows
- `5637144579`: 1 rows

**reporting_currency_exchange_rate_type**
- `0`: 26 rows

## Profile

Rows in the latest export: 26.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `name` | STRING | 27 | 0 |  |  |
| `reporting_currency` | STRING | 1 | 5 | USD | USD |
| `fiscal_calendar` | STRING | 2 | 0 | 0 | 5637144576 |
| `budget_exchange_rate_type` | STRING | 1 | 0 | 0 | 0 |
| `accounting_currency` | STRING | 1 | 1 | USD | USD |
| `is_budget_control_enabled` | STRING | 1 | 0 | No | No |
| `chart_of_accounts` | STRING | 4 | 0 | 0 | 5637146076 |
| `description` | STRING | 27 | 0 | Bluegrass Insurance Management | Tower Hill Specialty LLC |
| `source_key` | STRING | 27 | 0 |  |  |
| `default_exchange_rate_type` | STRING | 2 | 0 | 0 | 5637144579 |
| `reporting_currency_exchange_rate_type` | STRING | 1 | 0 | 0 | 0 |
| `primary_for_legal_entity` | STRING | 27 | 0 |  |  |

## Sample rows

| reporting_currency | fiscal_calendar | budget_exchange_rate_type | accounting_currency | is_budget_control_enabled | chart_of_accounts | description | default_exchange_rate_type | reporting_currency_exchange_rate_type |
|---|---|---|---|---|---|---|---|---|
| NULL | 0 | 0 | NULL | No | 0 | Company accounts data | 0 | 0 |
| USD | 5637144576 | 0 | USD | No | 5637144577 | Tower Hill Prime Insurance Co. | 0 | 0 |
| USD | 5637144576 | 0 | USD | No | 5637144577 | THIG | 5637144579 | 0 |
| USD | 5637144576 | 0 | USD | No | 5637144577 | Tower Hill Claims Service | 0 | 0 |
| USD | 5637144576 | 0 | USD | No | 5637144577 | Bluegrass Insurance Management | 0 | 0 |
