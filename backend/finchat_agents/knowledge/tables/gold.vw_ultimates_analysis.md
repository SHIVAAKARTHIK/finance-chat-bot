---
name: vw_ultimates_analysis
schema: gold
layer: gold
domain: subledger
type: view
status: active
purpose: Ultimates analysis (Incurred Loss/LAE, IBNR Loss/LAE, Ultimates) on LTD balances from silver.fact_fynapse_slr_journals;
  posting month derived from TRANSACTION_DATE
grain: one row per company; loss dimensions and posting period
primary_key:
- Company
- LOB
- CAT_Code
- Business_Indicator
- Accident_Year
- Posting_Year
- Posting_Month
entity_column: Legal_Entity
period_columns:
- Posting_Year
- Posting_Month
pii_columns: []
synonyms: []
built_from:
- fact_fynapse_slr_journals
known_issues: []
proposed_fields: []
reviewed: false
---

# vw_ultimates_analysis

Ultimates analysis (Incurred Loss/LAE, IBNR Loss/LAE, Ultimates) on LTD balances from silver.fact_fynapse_slr_journals; posting month derived from TRANSACTION_DATE

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `Company` | string |  |  | `Company` |
| `LOB` | string |  |  | `LOB` |
| `CAT_Code` | string |  |  | `CAT_Code` |
| `Business_Indicator` | string |  |  | `Business_Indicator` |
| `Accident_Year` | int |  |  | `Accident_Year` |
| `Posting_Year` | int |  |  | `Posting_Year` |
| `Posting_Month` | int |  |  | `Posting_Month` |
| `Legal_Entity` | string |  |  | `Legal_Entity` |
| `ASLOB` | string |  |  | `ASLOB` |
| `Treaty_Business_Type` | string |  |  | `Treaty_Business_Type` |
| `Incurred_Loss` | decimal |  |  | `Incurred_Loss` |
| `Incurred_LAE` | decimal |  |  | `Incurred_LAE` |
| `IBNR_Loss` | decimal |  |  | `IBNR_Loss` |
| `IBNR_LAE` | decimal |  |  | `IBNR_LAE` |
| `Ultimates` | decimal |  |  | `Ultimates` |

## Values

**LOB**
- `Broker`
- `Direct_Customer`
- `Corporate`

**CAT_Code**
- `CAT-014`
- `CAT-015`
- `CAT-002`
- `CAT-004`
- `NON CAT`
- `CAT-009`
- `CAT-011`
- `CAT-005`
- `CAT-007`
- `CAT-001`
- `CAT-008`
- `CAT-006`
- `CAT-003`
- `CAT-010`
- `CAT-013`
- `CAT-012`

**Business_Indicator**
- `New Business`
- `Claims Activity`
- `Customer Retention`

**Accident_Year**
- `2025`

**Posting_Year**
- `2025`

**Posting_Month**
- `2`

**ASLOB**
- `Property & Casualty`
- `Health Insurance`
- `Life Insurance`

**Treaty_Business_Type**
- `None`

**IBNR_Loss**
- `0`
- `699`
- `887`
- `2906`
- `1209`

**IBNR_LAE**
- `0`
- `1801`
- `612`
- `361`
- `1977`

## Empty columns

Empty in every row: `Treaty_Business_Type`. Do not filter or group on them.
