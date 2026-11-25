---
name: vw_premium_analysis
schema: gold
layer: gold
domain: subledger
type: view
status: active
purpose: Written, Unearned (UPR change) and Earned Premium by key dimensions and posting period (MTD/QTD/YTD/LTD)
grain: one row per legal entity; posting period; business dimension and premium category
primary_key:
- Legal_Entity
- Posting_Period_Date
- Profit_Center
- Cost_Center
- Business_Indicator
- LOB
- ASLOB
- State
- Subline_Type
- Business_Event
- Premium_Category
entity_column: Legal_Entity
period_columns:
- Posting_Year
- Posting_Quarter
- Posting_Month
- Posting_Period_Date
pii_columns: []
synonyms: []
built_from:
- fact_fynapse_slr_journals
known_issues: []
row_count: 161
proposed_fields: []
reviewed: false
---

# vw_premium_analysis

Written, Unearned (UPR change) and Earned Premium by key dimensions and posting period (MTD/QTD/YTD/LTD)

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `Legal_Entity` | string |  |  | `Legal_Entity` |
| `Parent_Entity` | string |  |  | `Parent_Entity` |
| `Profit_Center` | string |  |  | `Profit_Center` |
| `Cost_Center` | string |  |  | `Cost_Center` |
| `Intercompany` | string |  |  | `Intercompany` |
| `Business_Indicator` | string |  |  | `Business_Indicator` |
| `LOB` | string |  |  | `LOB` |
| `ASLOB` | string |  |  | `ASLOB` |
| `State` | string |  |  | `State` |
| `CAT_Code` | string |  |  | `CAT_Code` |
| `Treaty_Business_Type` | string |  |  | `Treaty_Business_Type` |
| `Reinsurer_ID` | string |  |  | `Reinsurer_ID` |
| `Accident_Year` | string |  |  | `Accident_Year` |
| `Tax_Year` | string |  |  | `Tax_Year` |
| `Categories` | string |  |  | `Categories` |
| `Subline_Type` | string |  |  | `Subline_Type` |
| `Posting_Layer` | string |  |  | `Posting_Layer` |
| `Business_Event` | string |  |  | `Business_Event` |
| `Source_System` | string |  |  | `Source_System` |
| `Source_Type` | string |  |  | `Source_Type` |
| `Premium_Category` | string |  |  | `Premium_Category` |
| `Premium_Category_Sort` | int |  |  | `Premium_Category_Sort` |
| `Posting_Year` | int |  |  | `Posting_Year` |
| `Posting_Quarter` | int |  |  | `Posting_Quarter` |
| `Posting_Month` | int |  |  | `Posting_Month` |
| `Posting_Period_Date` | date |  |  | `Posting_Period_Date` |
| `Written_Premium_MTD` | decimal |  |  | `Written_Premium_MTD` |
| `Written_Premium_QTD` | decimal |  |  | `Written_Premium_QTD` |
| `Written_Premium_YTD` | decimal |  |  | `Written_Premium_YTD` |
| `Written_Premium_LTD` | decimal |  |  | `Written_Premium_LTD` |
| `Unearned_Premium_MTD` | decimal |  |  | `Unearned_Premium_MTD` |
| `Unearned_Premium_QTD` | decimal |  |  | `Unearned_Premium_QTD` |
| `Unearned_Premium_YTD` | decimal |  |  | `Unearned_Premium_YTD` |
| `Unearned_Premium_LTD` | decimal |  |  | `Unearned_Premium_LTD` |
| `Earned_Premium_MTD` | decimal |  |  | `Earned_Premium_MTD` |
| `Earned_Premium_QTD` | decimal |  |  | `Earned_Premium_QTD` |
| `Earned_Premium_YTD` | decimal |  |  | `Earned_Premium_YTD` |
| `Earned_Premium_LTD` | decimal |  |  | `Earned_Premium_LTD` |

## Values

**Profit_Center**
- `Health Insurance`: 49 rows
- `Property & Casualty Insurance`: 44 rows
- `Auto Insurance`: 39 rows
- `Life Insurance`: 29 rows

**Cost_Center**
- `Underwriting`: 56 rows
- `P&C Claims`: 29 rows
- `Health Provider Management`: 26 rows
- `Accident Assessment`: 19 rows
- `Life Operations`: 16 rows
- `Health Claims Processing`: 15 rows

**Business_Indicator**
- `New Business`: 72 rows
- `Claims Activity`: 63 rows
- `Customer Retention`: 26 rows

**LOB**
- `Broker`: 82 rows
- `Direct_Customer`: 70 rows
- `Corporate`: 9 rows

**ASLOB**
- `Property & Casualty`: 83 rows
- `Health Insurance`: 49 rows
- `Life Insurance`: 29 rows

**State**
- `New Jersey`: 20 rows
- `Massachusetts`: 19 rows
- `Michigan`: 18 rows
- `Florida`: 17 rows
- `Oregon`: 17 rows
- `Minnesota`: 16 rows
- `Ohio`: 15 rows
- `Texas`: 14 rows
- `Illinois`: 13 rows
- `Indiana`: 12 rows

**CAT_Code**
- `NVS`: 161 rows

**Treaty_Business_Type**
- `NVS`: 161 rows

**Reinsurer_ID**
- `NVS`: 161 rows

**Accident_Year**
- `NVS`: 161 rows

**Tax_Year**
- `2025`: 161 rows

**Categories**
- `NVS`: 161 rows

**Subline_Type**
- `Commercial Property`: 44 rows
- `Group Health`: 34 rows
- `Commercial Auto`: 22 rows
- `Personal Auto`: 17 rows
- `Group Life`: 15 rows
- `Individual Health`: 15 rows
- `Term Life`: 14 rows

**Posting_Layer**
- `US_GAAP`: 161 rows

**Business_Event**
- `DIRECT WRITTEN PREMIUM`: 60 rows
- `DIRECT_UPR_CHANGE`: 35 rows
- `ASSUMED WRITTEN PREMIUM`: 33 rows
- `ASSUMED UPR CHANGE`: 33 rows

**Source_System**
- `DAG`: 161 rows

**Source_Type**
- `SLR`: 161 rows

**Premium_Category**
- `Direct`: 95 rows
- `Assumed`: 66 rows

**Premium_Category_Sort**
- `1`: 95 rows
- `2`: 66 rows

**Posting_Year**
- `2025`: 161 rows

**Posting_Quarter**
- `1`: 161 rows

**Posting_Month**
- `2`: 161 rows

**Posting_Period_Date**
- `2025-02-01 00:00:00`: 161 rows

## Profile

Rows in the latest export: 161.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `Legal_Entity` | STRING | 1 | 0 |  |  |
| `Parent_Entity` | STRING | 1 | 0 |  |  |
| `Profit_Center` | STRING | 4 | 0 | Auto Insurance | Property & Casualty Insurance |
| `Cost_Center` | STRING | 6 | 0 | Accident Assessment | Underwriting |
| `Intercompany` | STRING | 1 | 0 |  |  |
| `Business_Indicator` | STRING | 3 | 0 | Claims Activity | New Business |
| `LOB` | STRING | 3 | 0 | Broker | Direct_Customer |
| `ASLOB` | STRING | 3 | 0 | Health Insurance | Property & Casualty |
| `State` | STRING | 10 | 0 | Florida | Texas |
| `CAT_Code` | STRING | 1 | 0 | NVS | NVS |
| `Treaty_Business_Type` | STRING | 1 | 0 | NVS | NVS |
| `Reinsurer_ID` | STRING | 1 | 0 | NVS | NVS |
| `Accident_Year` | STRING | 1 | 0 | NVS | NVS |
| `Tax_Year` | STRING | 1 | 0 | 2025 | 2025 |
| `Categories` | STRING | 1 | 0 | NVS | NVS |
| `Subline_Type` | STRING | 7 | 0 | Commercial Auto | Term Life |
| `Posting_Layer` | STRING | 1 | 0 | US_GAAP | US_GAAP |
| `Business_Event` | STRING | 4 | 0 | ASSUMED UPR CHANGE | DIRECT_UPR_CHANGE |
| `Source_System` | STRING | 1 | 0 | DAG | DAG |
| `Source_Type` | STRING | 1 | 0 | SLR | SLR |
| `Premium_Category` | STRING | 2 | 0 | Assumed | Direct |
| `Premium_Category_Sort` | INT | 2 | 0 | 1 | 2 |
| `Posting_Year` | INT | 1 | 0 | 2025 | 2025 |
| `Posting_Quarter` | INT | 1 | 0 | 1 | 1 |
| `Posting_Month` | INT | 1 | 0 | 2 | 2 |
| `Posting_Period_Date` | DATE | 1 | 0 | 2025-02-01 00:00:00 | 2025-02-01 00:00:00 |
| `Written_Premium_MTD` | DECIMAL | 97 | 0 | 0 | 49303 |
| `Written_Premium_QTD` | DECIMAL | 97 | 0 | 0 | 49303 |
| `Written_Premium_YTD` | DECIMAL | 97 | 0 | 0 | 49303 |
| `Written_Premium_LTD` | DECIMAL | 97 | 0 | 0 | 49303 |
| `Unearned_Premium_MTD` | DECIMAL | 67 | 0 | 0 | 8445 |
| `Unearned_Premium_QTD` | DECIMAL | 67 | 0 | 0 | 8445 |
| `Unearned_Premium_YTD` | DECIMAL | 67 | 0 | 0 | 8445 |
| `Unearned_Premium_LTD` | DECIMAL | 67 | 0 | 0 | 8445 |
| `Earned_Premium_MTD` | DECIMAL | 161 | 0 | -8445 | 49303 |
| `Earned_Premium_QTD` | DECIMAL | 161 | 0 | -8445 | 49303 |
| `Earned_Premium_YTD` | DECIMAL | 161 | 0 | -8445 | 49303 |
| `Earned_Premium_LTD` | DECIMAL | 161 | 0 | -8445 | 49303 |

## Sample rows

| Profit_Center | Cost_Center | Business_Indicator | LOB | ASLOB | State | CAT_Code | Treaty_Business_Type | Reinsurer_ID | Accident_Year | Tax_Year | Categories | Subline_Type | Posting_Layer | Business_Event | Source_System | Source_Type | Premium_Category | Premium_Category_Sort | Posting_Year | Posting_Quarter | Posting_Month | Posting_Period_Date | Written_Premium_MTD | Written_Premium_QTD | Written_Premium_YTD | Written_Premium_LTD | Unearned_Premium_MTD | Unearned_Premium_QTD | Unearned_Premium_YTD | Unearned_Premium_LTD | Earned_Premium_MTD | Earned_Premium_QTD | Earned_Premium_YTD | Earned_Premium_LTD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Auto Insurance | Underwriting | New Business | Broker | Property & Casualty | New Jersey | NVS | NVS | NVS | NVS | 2025 | NVS | Commercial Auto | US_GAAP | DIRECT WRITTEN PREMIUM | DAG | SLR | Direct | 1 | 2025 | 1 | 2 | 2025-02-01 00:00:00 | 36523 | 36523 | 36523 | 36523 | 0 | 0 | 0 | 0 | 36523 | 36523 | 36523 | 36523 |
| Property & Casualty Insurance | Underwriting | New Business | Broker | Property & Casualty | Ohio | NVS | NVS | NVS | NVS | 2025 | NVS | Commercial Property | US_GAAP | DIRECT WRITTEN PREMIUM | DAG | SLR | Direct | 1 | 2025 | 1 | 2 | 2025-02-01 00:00:00 | 5338 | 5338 | 5338 | 5338 | 0 | 0 | 0 | 0 | 5338 | 5338 | 5338 | 5338 |
| Auto Insurance | Accident Assessment | Claims Activity | Broker | Property & Casualty | Texas | NVS | NVS | NVS | NVS | 2025 | NVS | Commercial Auto | US_GAAP | DIRECT_UPR_CHANGE | DAG | SLR | Direct | 1 | 2025 | 1 | 2 | 2025-02-01 00:00:00 | 0 | 0 | 0 | 0 | 3410 | 3410 | 3410 | 3410 | -3410 | -3410 | -3410 | -3410 |
| Health Insurance | Health Provider Management | Customer Retention | Broker | Health Insurance | Ohio | NVS | NVS | NVS | NVS | 2025 | NVS | Group Health | US_GAAP | DIRECT_UPR_CHANGE | DAG | SLR | Direct | 1 | 2025 | 1 | 2 | 2025-02-01 00:00:00 | 0 | 0 | 0 | 0 | 5114 | 5114 | 5114 | 5114 | -5114 | -5114 | -5114 | -5114 |
| Health Insurance | Health Claims Processing | Claims Activity | Direct_Customer | Health Insurance | Illinois | NVS | NVS | NVS | NVS | 2025 | NVS | Individual Health | US_GAAP | DIRECT WRITTEN PREMIUM | DAG | SLR | Direct | 1 | 2025 | 1 | 2 | 2025-02-01 00:00:00 | 14970 | 14970 | 14970 | 14970 | 0 | 0 | 0 | 0 | 14970 | 14970 | 14970 | 14970 |
