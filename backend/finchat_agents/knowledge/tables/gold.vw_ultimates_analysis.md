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
row_count: 113
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
- `Broker`: 54 rows
- `Direct_Customer`: 52 rows
- `Corporate`: 7 rows

**CAT_Code**
- `CAT-014`: 12 rows
- `CAT-015`: 11 rows
- `CAT-002`: 11 rows
- `CAT-004`: 10 rows
- `NON CAT`: 10 rows
- `CAT-009`: 9 rows
- `CAT-011`: 8 rows
- `CAT-005`: 7 rows
- `CAT-007`: 7 rows
- `CAT-001`: 7 rows
- `CAT-008`: 5 rows
- `CAT-006`: 5 rows
- `CAT-003`: 4 rows
- `CAT-010`: 4 rows
- `CAT-013`: 2 rows
- `CAT-012`: 1 rows

**Business_Indicator**
- `New Business`: 53 rows
- `Claims Activity`: 47 rows
- `Customer Retention`: 13 rows

**Accident_Year**
- `2025`: 113 rows

**Posting_Year**
- `2025`: 113 rows

**Posting_Month**
- `2`: 113 rows

**ASLOB**
- `Property & Casualty`: 61 rows
- `Health Insurance`: 28 rows
- `Life Insurance`: 24 rows

**Treaty_Business_Type**
- `None`: 113 rows

**IBNR_Loss**
- `0`: 109 rows
- `699`: 1 rows
- `887`: 1 rows
- `2906`: 1 rows
- `1209`: 1 rows

**IBNR_LAE**
- `0`: 109 rows
- `1801`: 1 rows
- `612`: 1 rows
- `361`: 1 rows
- `1977`: 1 rows

## Profile

Rows in the latest export: 113.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `Company` | STRING | 6 | 0 |  |  |
| `LOB` | STRING | 3 | 0 | Broker | Direct_Customer |
| `CAT_Code` | STRING | 16 | 0 | CAT-001 | NON CAT |
| `Business_Indicator` | STRING | 3 | 0 | Claims Activity | New Business |
| `Accident_Year` | INT | 1 | 0 | 2025 | 2025 |
| `Posting_Year` | INT | 1 | 0 | 2025 | 2025 |
| `Posting_Month` | INT | 1 | 0 | 2 | 2 |
| `Legal_Entity` | STRING | 1 | 0 |  |  |
| `ASLOB` | STRING | 3 | 0 | Health Insurance | Property & Casualty |
| `Treaty_Business_Type` | STRING | 0 | 113 |  |  |
| `Incurred_Loss` | DECIMAL | 57 | 0 | -5987 | 2514 |
| `Incurred_LAE` | DECIMAL | 55 | 0 | -6327 | 199122 |
| `IBNR_Loss` | DECIMAL | 5 | 0 | 0 | 2906 |
| `IBNR_LAE` | DECIMAL | 5 | 0 | 0 | 1977 |
| `Ultimates` | DECIMAL | 110 | 0 | -8813 | 199122 |

## Sample rows

| LOB | CAT_Code | Business_Indicator | Accident_Year | Posting_Year | Posting_Month | ASLOB | Treaty_Business_Type | Incurred_Loss | Incurred_LAE | IBNR_Loss | IBNR_LAE | Ultimates |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Broker | CAT-001 | Claims Activity | 2025 | 2025 | 2 | Property & Casualty | NULL | 1839 | 0 | 0 | 0 | 1839 |
| Broker | CAT-002 | Claims Activity | 2025 | 2025 | 2 | Health Insurance | NULL | -1965 | -4258 | 0 | 0 | -6223 |
| Broker | CAT-002 | New Business | 2025 | 2025 | 2 | Property & Casualty | NULL | 0 | 2891 | 0 | 0 | 2891 |
| Broker | CAT-003 | New Business | 2025 | 2025 | 2 | Property & Casualty | NULL | 0 | 1224 | 0 | 0 | 1224 |
| Broker | CAT-004 | Claims Activity | 2025 | 2025 | 2 | Property & Casualty | NULL | -3619 | 0 | 0 | 0 | -3619 |
