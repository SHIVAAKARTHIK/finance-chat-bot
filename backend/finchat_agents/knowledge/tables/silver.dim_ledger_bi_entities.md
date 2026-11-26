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
- `USD`
- `None`

**fiscal_calendar**
- `5637144576`
- `0`

**budget_exchange_rate_type**
- `0`

**accounting_currency**
- `USD`
- `None`

**is_budget_control_enabled**
- `No`

**chart_of_accounts**
- `5637144577`
- `5637145326`
- `5637146076`
- `0`

**description**
- `Tower Hill Prime Insurance Co.`
- `Tower Hill E&S Insurance Exchange`
- `Tower Hill Insurance Managers`
- `Tower Hill Re Holdings`
- `Tomoka Re Holdings`
- `Tower Hill Re`
- `Tower Hill Specialty Group LLC`
- `Tower Hill Claims Service`
- `Lovable 3`
- `Rock-It Cargo USA LLC`
- `THIG Agency`
- `Lovable 4`
- `Tower Hill Insurance Exchange`
- `Cars USA Shipping LLC`
- `Bluegrass Insurance Management`
- `Tower Hill Holdings`
- `Lovable 5`
- `Tower Hill Specialty LLC`
- `Tower Hill Risk Management LLC`
- `Tower Hill Insurance Holdings`
- `THIG`
- `Company accounts data`
- `Tower Hill Preferred Insurance Co.`
- `Tower Hill E&S Risk Management`
- `Lovable 2`
- `Lovable 1`

**default_exchange_rate_type**
- `0`
- `5637144579`

**reporting_currency_exchange_rate_type**
- `0`
