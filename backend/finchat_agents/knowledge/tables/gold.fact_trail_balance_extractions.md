---
name: fact_trail_balance_extractions
schema: gold
layer: gold
domain: gl
type: view
status: active
purpose: Consolidated trial-balance amounts by company and balance description.
grain: one row per company and trial-balance description
primary_key:
- COMPANY
- DESCRIPTION
entity_column: COMPANY
period_columns: []
pii_columns: []
synonyms: []
built_from:
- fact_trail_balance_extractions
known_issues: []
proposed_fields: []
reviewed: false
---

# fact_trail_balance_extractions

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `COMPANY` | string |  |  | `COMPANY` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `DESCRIPTION` | string |  |  | `DESCRIPTION` |
| `AMOUNT` | double |  |  | `AMOUNT` |

## Values

**DESCRIPTION**
- `Consolidated Assets`
- `Consolidated Expenses`
- `Consolidated Revenue`
- `Consolidated Liabilities`
- `Consolidated Equity`

**AMOUNT**
- `2609.07`
- `-2719983.55`
- `-15653913.44`
- `-77879.35`
- `8901.99`
- `-1880270.17`
- `3026.89`
- `-2609.07`
- `17652134.2`
- `-408931.82`
- `64172478.6`
- `2794545.04`
- `-63540340.98`
- `1345.47`
- `3329957.27`
- `3317.86`
- `-103910859.8`
- `-2929927.44`
- `-1345.47`
- `-3087.54`
- `7326.16`
- `136088672.4`
- `-2005546.92`
