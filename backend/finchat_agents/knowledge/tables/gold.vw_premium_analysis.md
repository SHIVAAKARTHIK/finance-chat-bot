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
- `Health Insurance`
- `Property & Casualty Insurance`
- `Auto Insurance`
- `Life Insurance`

**Cost_Center**
- `Underwriting`
- `P&C Claims`
- `Health Provider Management`
- `Accident Assessment`
- `Life Operations`
- `Health Claims Processing`

**Business_Indicator**
- `New Business`
- `Claims Activity`
- `Customer Retention`

**LOB**
- `Broker`
- `Direct_Customer`
- `Corporate`

**ASLOB**
- `Property & Casualty`
- `Health Insurance`
- `Life Insurance`

**State**
- `New Jersey`
- `Massachusetts`
- `Michigan`
- `Florida`
- `Oregon`
- `Minnesota`
- `Ohio`
- `Texas`
- `Illinois`
- `Indiana`

**CAT_Code**
- `NVS`

**Treaty_Business_Type**
- `NVS`

**Reinsurer_ID**
- `NVS`

**Accident_Year**
- `NVS`

**Tax_Year**
- `2025`

**Categories**
- `NVS`

**Subline_Type**
- `Commercial Property`
- `Group Health`
- `Commercial Auto`
- `Personal Auto`
- `Group Life`
- `Individual Health`
- `Term Life`

**Posting_Layer**
- `US_GAAP`

**Business_Event**
- `DIRECT WRITTEN PREMIUM`
- `DIRECT_UPR_CHANGE`
- `ASSUMED WRITTEN PREMIUM`
- `ASSUMED UPR CHANGE`

**Source_System**
- `DAG`

**Source_Type**
- `SLR`

**Premium_Category**
- `Direct`
- `Assumed`

**Premium_Category_Sort**
- `1`
- `2`

**Posting_Year**
- `2025`

**Posting_Quarter**
- `1`

**Posting_Month**
- `2`

**Posting_Period_Date**
- `2025-02-01 00:00:00`
