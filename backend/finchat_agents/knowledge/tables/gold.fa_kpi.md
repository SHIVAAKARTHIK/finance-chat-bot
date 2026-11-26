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
- `Asset Lifecycle`
- `Capitalization workflow`
- `In service`

**KPI**
- `Capitalized`
- `Draft`
- `Depreciation: Exceptions`
- `Disposal pending`
- `Review`
- `In service`
- `Depreciation: Calculated`
- `Depreciation: Pending Approval`
- `Approval`
- `Retired`
- `Depreciation: Posted`

**AMOUNT**
- `2166600`
- `1848641.72`
- `2035900`
- `14217.86`
- `18900`
- `1000`
- `-314.03`
- `-303.8`
- `100`
- `-31900`
- `-298.84`
- `-228803.04`

**COUNT**
- `1`
- `9`
- `189`
- `199`
- `1763`

**POSTING_SCHEMA**
- `GAAP`
