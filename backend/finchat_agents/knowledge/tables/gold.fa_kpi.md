---
name: fa_kpi
schema: gold
layer: gold
domain: fa
type: view
status: active
purpose: Summarizes fixed-asset lifecycle; capitalization and depreciation workflow KPIs.
grain: one row per section and KPI
primary_key:
- SECTION
- KPI
entity_column: LEGAL_ENTITY
period_columns: []
pii_columns: []
synonyms: []
built_from: []
known_issues: []
row_count: 12
proposed_fields: []
reviewed: false
---

# fa_kpi

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `SECTION` | string |  |  | `SECTION` |
| `KPI` | string |  |  | `KPI` |
| `AMOUNT` | double |  |  | `AMOUNT` |
| `COUNT` | long |  |  | `COUNT` |
| `LEGAL_ENTITY` | string |  |  | `LEGAL_ENTITY` |
| `POSTING_SCHEMA` | string |  |  | `POSTING_SCHEMA` |

## Values

**SECTION**
- `Asset Lifecycle`: 4 rows
- `Capitalization workflow`: 4 rows
- `In service`: 4 rows

**KPI**
- `Capitalized`: 2 rows
- `Draft`: 1 rows
- `Depreciation: Exceptions`: 1 rows
- `Disposal pending`: 1 rows
- `Review`: 1 rows
- `In service`: 1 rows
- `Depreciation: Calculated`: 1 rows
- `Depreciation: Pending Approval`: 1 rows
- `Approval`: 1 rows
- `Retired`: 1 rows
- `Depreciation: Posted`: 1 rows

**AMOUNT**
- `2166600`: 1 rows
- `1848641.72`: 1 rows
- `2035900`: 1 rows
- `14217.86`: 1 rows
- `18900`: 1 rows
- `1000`: 1 rows
- `-314.03`: 1 rows
- `-303.8`: 1 rows
- `100`: 1 rows
- `-31900`: 1 rows
- `-298.84`: 1 rows
- `-228803.04`: 1 rows

**COUNT**
- `1`: 6 rows
- `9`: 2 rows
- `189`: 2 rows
- `199`: 1 rows
- `1763`: 1 rows

**POSTING_SCHEMA**
- `GAAP`: 12 rows

## Profile

Rows in the latest export: 12.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `SECTION` | STRING | 3 | 0 | Asset Lifecycle | In service |
| `KPI` | STRING | 10 | 0 | Approval | Review |
| `AMOUNT` | DOUBLE | 11 | 0 | -228803.04 | 2166600 |
| `COUNT` | LONG | 5 | 0 | 1 | 1763 |
| `LEGAL_ENTITY` | STRING | 1 | 0 |  |  |
| `POSTING_SCHEMA` | STRING | 1 | 0 | GAAP | GAAP |

## Sample rows

| SECTION | KPI | AMOUNT | COUNT | POSTING_SCHEMA |
|---|---|---|---|---|
| Asset Lifecycle | Capitalized | 2035900 | 189 | GAAP |
| Asset Lifecycle | Disposal pending | 14217.86 | 9 | GAAP |
| Asset Lifecycle | In service | 1848641.72 | 189 | GAAP |
| Asset Lifecycle | Retired | -31900 | 9 | GAAP |
| Capitalization workflow | Approval | 100 | 1 | GAAP |
