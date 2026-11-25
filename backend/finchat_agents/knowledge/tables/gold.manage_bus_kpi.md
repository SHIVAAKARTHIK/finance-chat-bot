---
name: manage_bus_kpi
schema: gold
layer: gold
domain: gl
type: view
status: active
purpose: Displays MTD; QTD and YTD business KPIs for each legal entity.
grain: one row per KPI and legal entity
primary_key:
- SECTION
- KPI
- LEGAL_ENTITY
- POSTING_SCHEMA
entity_column: LEGAL_ENTITY
period_columns: []
pii_columns: []
synonyms: []
built_from: []
known_issues: []
row_count: 56
proposed_fields: []
reviewed: false
---

# manage_bus_kpi

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `SECTION` | string |  |  | `SECTION` |
| `KPI` | string |  |  | `KPI` |
| `MTD_AMOUNT` | string |  |  | `MTD_AMOUNT` |
| `QTD_AMOUNT` | string |  |  | `QTD_AMOUNT` |
| `YTD_AMOUNT` | string |  |  | `YTD_AMOUNT` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `POSTING_SCHEMA` | string |  |  | `POSTING_SCHEMA` |

## Values

**SECTION**
- `Reports and Insights Overview`: 56 rows

**KPI**
- `Revenue`: 7 rows
- `Cash Position`: 7 rows
- `Net Income`: 7 rows
- `EBITDA`: 7 rows
- `Working Capital`: 7 rows
- `Operating Expense`: 7 rows
- `Gross Margin`: 7 rows
- `Operating Margin`: 7 rows

**MTD_AMOUNT**
- `N/A`: 18 rows
- `0`: 6 rows
- `-3087.54`: 2 rows
- `-1345.47`: 2 rows
- `-2609.07`: 2 rows
- `74561.49`: 2 rows
- `400029.83`: 2 rows
- `1998220.76`: 2 rows
- `450000`: 1 rows
- `18`: 1 rows
- `734765.81`: 1 rows
- `408931.82`: 1 rows
- `8901.99`: 1 rows
- `900000`: 1 rows
- `5400000`: 1 rows
- `77879.35`: 1 rows
- `7326.16`: 1 rows
- `1345.47`: 1 rows
- `434570.05`: 1 rows
- `1200000`: 1 rows
- `2609.07`: 1 rows
- `2005546.92`: 1 rows
- `3087.54`: 1 rows
- `1800000`: 1 rows
- `7000000`: 1 rows
- `3317.86`: 1 rows
- `6102680.56`: 1 rows
- `6.5`: 1 rows

**QTD_AMOUNT**
- `N/A`: 18 rows
- `0`: 6 rows
- `-3087.54`: 2 rows
- `-1345.47`: 2 rows
- `-2609.07`: 2 rows
- `74561.49`: 2 rows
- `400029.83`: 2 rows
- `1998220.76`: 2 rows
- `450000`: 1 rows
- `18`: 1 rows
- `734765.81`: 1 rows
- `408931.82`: 1 rows
- `8901.99`: 1 rows
- `900000`: 1 rows
- `5400000`: 1 rows
- `77879.35`: 1 rows
- `7326.16`: 1 rows
- `1345.47`: 1 rows
- `434570.05`: 1 rows
- `1200000`: 1 rows
- `2609.07`: 1 rows
- `2005546.92`: 1 rows
- `3087.54`: 1 rows
- `1800000`: 1 rows
- `7000000`: 1 rows
- `3317.86`: 1 rows
- `6102680.56`: 1 rows
- `6.5`: 1 rows

**YTD_AMOUNT**
- `N/A`: 18 rows
- `0`: 6 rows
- `-3087.54`: 2 rows
- `-1345.47`: 2 rows
- `-2609.07`: 2 rows
- `74561.49`: 2 rows
- `400029.83`: 2 rows
- `1998220.76`: 2 rows
- `450000`: 1 rows
- `18`: 1 rows
- `734765.81`: 1 rows
- `408931.82`: 1 rows
- `8901.99`: 1 rows
- `900000`: 1 rows
- `5400000`: 1 rows
- `77879.35`: 1 rows
- `7326.16`: 1 rows
- `1345.47`: 1 rows
- `434570.05`: 1 rows
- `1200000`: 1 rows
- `2609.07`: 1 rows
- `2005546.92`: 1 rows
- `3087.54`: 1 rows
- `1800000`: 1 rows
- `7000000`: 1 rows
- `3317.86`: 1 rows
- `6102680.56`: 1 rows
- `6.5`: 1 rows

**POSTING_SCHEMA**
- `GAAP`: 56 rows

## Profile

Rows in the latest export: 56.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `SECTION` | STRING | 1 | 0 | Reports and Insights Overview | Reports and Insights Overview |
| `KPI` | STRING | 8 | 0 | Cash Position | Working Capital |
| `MTD_AMOUNT` | STRING | 28 | 0 | -1345.47 | N/A |
| `QTD_AMOUNT` | STRING | 28 | 0 | -1345.47 | N/A |
| `YTD_AMOUNT` | STRING | 28 | 0 | -1345.47 | N/A |
| `LEGAL_ENTITY` | STRING | 7 | 0 |  |  |
| `POSTING_SCHEMA` | STRING | 1 | 0 | GAAP | GAAP |

## Sample rows

| SECTION | KPI | MTD_AMOUNT | QTD_AMOUNT | YTD_AMOUNT | POSTING_SCHEMA |
|---|---|---|---|---|---|
| Reports and Insights Overview | Revenue | 0 | 0 | 0 | GAAP |
| Reports and Insights Overview | Revenue | 408931.82 | 408931.82 | 408931.82 | GAAP |
| Reports and Insights Overview | Revenue | 2005546.92 | 2005546.92 | 2005546.92 | GAAP |
| Reports and Insights Overview | Revenue | 0 | 0 | 0 | GAAP |
| Reports and Insights Overview | Revenue | 0 | 0 | 0 | GAAP |
