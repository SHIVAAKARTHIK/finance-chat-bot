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
- `Reports and Insights Overview`

**KPI**
- `Revenue`
- `Cash Position`
- `Net Income`
- `EBITDA`
- `Working Capital`
- `Operating Expense`
- `Gross Margin`
- `Operating Margin`

**MTD_AMOUNT**
- `N/A`
- `0`
- `-3087.54`
- `-1345.47`
- `-2609.07`
- `74561.49`
- `400029.83`
- `1998220.76`
- `450000`
- `18`
- `734765.81`
- `408931.82`
- `8901.99`
- `900000`
- `5400000`
- `77879.35`
- `7326.16`
- `1345.47`
- `434570.05`
- `1200000`
- `2609.07`
- `2005546.92`
- `3087.54`
- `1800000`
- `7000000`
- `3317.86`
- `6102680.56`
- `6.5`

**QTD_AMOUNT**
- `N/A`
- `0`
- `-3087.54`
- `-1345.47`
- `-2609.07`
- `74561.49`
- `400029.83`
- `1998220.76`
- `450000`
- `18`
- `734765.81`
- `408931.82`
- `8901.99`
- `900000`
- `5400000`
- `77879.35`
- `7326.16`
- `1345.47`
- `434570.05`
- `1200000`
- `2609.07`
- `2005546.92`
- `3087.54`
- `1800000`
- `7000000`
- `3317.86`
- `6102680.56`
- `6.5`

**YTD_AMOUNT**
- `N/A`
- `0`
- `-3087.54`
- `-1345.47`
- `-2609.07`
- `74561.49`
- `400029.83`
- `1998220.76`
- `450000`
- `18`
- `734765.81`
- `408931.82`
- `8901.99`
- `900000`
- `5400000`
- `77879.35`
- `7326.16`
- `1345.47`
- `434570.05`
- `1200000`
- `2609.07`
- `2005546.92`
- `3087.54`
- `1800000`
- `7000000`
- `3317.86`
- `6102680.56`
- `6.5`

**POSTING_SCHEMA**
- `GAAP`
