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
row_count: 23
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
- `Consolidated Assets`: 7 rows
- `Consolidated Expenses`: 7 rows
- `Consolidated Revenue`: 4 rows
- `Consolidated Liabilities`: 4 rows
- `Consolidated Equity`: 1 rows

**AMOUNT**
- `2609.07`: 1 rows
- `-2719983.55`: 1 rows
- `-15653913.44`: 1 rows
- `-77879.35`: 1 rows
- `8901.99`: 1 rows
- `-1880270.17`: 1 rows
- `3026.89`: 1 rows
- `-2609.07`: 1 rows
- `17652134.2`: 1 rows
- `-408931.82`: 1 rows
- `64172478.6`: 1 rows
- `2794545.04`: 1 rows
- `-63540340.98`: 1 rows
- `1345.47`: 1 rows
- `3329957.27`: 1 rows
- `3317.86`: 1 rows
- `-103910859.8`: 1 rows
- `-2929927.44`: 1 rows
- `-1345.47`: 1 rows
- `-3087.54`: 1 rows
- `7326.16`: 1 rows
- `136088672.4`: 1 rows
- `-2005546.92`: 1 rows

## Profile

Rows in the latest export: 23.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `COMPANY` | STRING | 7 | 0 |  |  |
| `LEGAL_ENTITY` | STRING | 1 | 0 |  |  |
| `DESCRIPTION` | STRING | 5 | 0 | Consolidated Assets | Consolidated Revenue |
| `AMOUNT` | DOUBLE | 24 | 0 | -103910859.83 | 136088672.38 |

## Sample rows

| DESCRIPTION | AMOUNT |
|---|---|
| Consolidated Assets | 136088672.38 |
| Consolidated Equity | -1880270.16999999 |
| Consolidated Expenses | 64172478.5999999 |
| Consolidated Liabilities | -103910859.83 |
| Consolidated Revenue | -63540340.98 |
