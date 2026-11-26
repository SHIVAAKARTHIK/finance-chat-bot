---
name: dim_ledger_fiscal_periods_v2
schema: silver
layer: silver
domain: gl
type: table
status: active
purpose: Fiscal calendar periods per ledger with year and period name.
grain: one row per HASH_KEY (one fiscal period of one ledger)
primary_key:
- HASH_KEY
entity_column: LEDGER_NAME
period_columns:
- YEAR_NAME
- PERIOD_NAME
pii_columns:
- MDP_CREATED_BY
- MDP_MODIFIED_BY
synonyms: []
built_from: []
known_issues:
- code: empty_column
  note: EXPENSE_USER_GROUP_INFO, PROJECT_USER_GROUP_INFO, LEDGER_USER_GROUP_INFO, PAYROLL_USER_GROUP_INFO, RETAIL_USER_GROUP_INFO
    all null
proposed_fields:
- grain
- primary_key
reviewed: false
---

# dim_ledger_fiscal_periods_v2

## Columns

| Column | Type | Meaning | Also called | SQL expression |
|---|---|---|---|---|
| `LEDGER_NAME` | string |  |  | `LEDGER_NAME` |
| `CALENDAR` | string |  |  | `CALENDAR` |
| `YEAR_NAME` | string |  |  | `YEAR_NAME` |
| `PERIOD_NAME` | string |  |  | `PERIOD_NAME` |
| `LEGAL_ENTITY_ID` | string |  |  | `LEGAL_ENTITY_ID` |
| `EXPENSE_USER_GROUP_INFO` | string |  |  | `EXPENSE_USER_GROUP_INFO` |
| `VENDOR_ACCESS_LEVEL` | string |  |  | `VENDOR_ACCESS_LEVEL` |
| `BANK_ACCESS_LEVEL` | string |  |  | `BANK_ACCESS_LEVEL` |
| `CUSTOMER_ACCESS_LEVEL` | string |  |  | `CUSTOMER_ACCESS_LEVEL` |
| `PROJECT_USER_GROUP_INFO` | string |  |  | `PROJECT_USER_GROUP_INFO` |
| `LEDGER_USER_GROUP_INFO` | string |  |  | `LEDGER_USER_GROUP_INFO` |
| `PAYROLL_USER_GROUP_INFO` | string |  |  | `PAYROLL_USER_GROUP_INFO` |
| `RETAIL_USER_GROUP_INFO` | string |  |  | `RETAIL_USER_GROUP_INFO` |
| `RETAIL_ACCESS_LEVEL` | string |  |  | `RETAIL_ACCESS_LEVEL` |
| `PURCHASE_USER_GROUP_INFO` | string |  |  | `PURCHASE_USER_GROUP_INFO` |
| `PERIOD_STATUS` | string |  |  | `PERIOD_STATUS` |
| `FIXED_ASSETS_USER_GROUP_INFO` | string |  |  | `FIXED_ASSETS_USER_GROUP_INFO` |
| `PRODUCTION_USER_GROUP_INFO` | string |  |  | `PRODUCTION_USER_GROUP_INFO` |
| `FIXED_ASSETS_ACCESS_LEVEL` | string |  |  | `FIXED_ASSETS_ACCESS_LEVEL` |
| `INVENTORY_USER_GROUP_INFO` | string |  |  | `INVENTORY_USER_GROUP_INFO` |
| `PURCHASE_ACCESS_LEVEL` | string |  |  | `PURCHASE_ACCESS_LEVEL` |
| `EXPENSE_ACCESS_LEVEL` | string |  |  | `EXPENSE_ACCESS_LEVEL` |
| `INVENTORY_ACCESS_LEVEL` | string |  |  | `INVENTORY_ACCESS_LEVEL` |
| `PAYROLL_ACCESS_LEVEL` | string |  |  | `PAYROLL_ACCESS_LEVEL` |
| `TAX_USER_GROUP_INFO` | string |  |  | `TAX_USER_GROUP_INFO` |
| `VENDOR_USER_GROUP_INFO` | string |  |  | `VENDOR_USER_GROUP_INFO` |
| `BANK_USER_GROUP_INFO` | string |  |  | `BANK_USER_GROUP_INFO` |
| `SALES_ACCESS_LEVEL` | string |  |  | `SALES_ACCESS_LEVEL` |
| `FIXED_ASSETS_RU_ACCESS_LEVEL` | string |  |  | `FIXED_ASSETS_RU_ACCESS_LEVEL` |
| `LEDGER_ACCESS_LEVEL` | string |  |  | `LEDGER_ACCESS_LEVEL` |
| `CUSTOMER_USER_GROUP_INFO` | string |  |  | `CUSTOMER_USER_GROUP_INFO` |
| `TAX_ACCESS_LEVEL` | string |  |  | `TAX_ACCESS_LEVEL` |
| `SALES_USER_GROUP_INFO` | string |  |  | `SALES_USER_GROUP_INFO` |
| `PROJECT_ACCESS_LEVEL` | string |  |  | `PROJECT_ACCESS_LEVEL` |
| `PRODUCTION_ACCESS_LEVEL` | string |  |  | `PRODUCTION_ACCESS_LEVEL` |
| `FIXED_ASSETS_RU_USER_GROUP_INFO` | string |  |  | `FIXED_ASSETS_RU_USER_GROUP_INFO` |
| `ITM_ACCESS_LEVEL` | string |  |  | `ITM_ACCESS_LEVEL` |
| `ITM_USER_GROUP_INFO` | string |  |  | `ITM_USER_GROUP_INFO` |
| `SOURCE_FILE_NAME` | string |  |  | `SOURCE_FILE_NAME` |
| `HASH_KEY` | string |  |  | `HASH_KEY` |
| `MDP_CREATED_BY` | string |  |  | `MDP_CREATED_BY` |
| `MDP_CREATED_DATE` | timestamp |  |  | `MDP_CREATED_DATE` |
| `MDP_MODIFIED_BY` | string |  |  | `MDP_MODIFIED_BY` |
| `MDP_MODIFIED_DATE` | timestamp |  |  | `MDP_MODIFIED_DATE` |

## Values

**CALENDAR**
- `FY`

**YEAR_NAME**
- `2021`
- `2016`
- `2018`
- `2023`
- `2026`
- `2022`
- `2020`
- `2017`
- `2019`
- `2025`
- `2014`
- `2015`
- `2024`

**PERIOD_NAME**
- `Period 1`
- `Period 6`
- `Period 10`
- `Period 8`
- `Period 11`
- `Period 13`
- `Period 12`
- `Period 9`
- `Period 2`
- `Period 5`
- `Period 4`
- `Period 3`
- `Period 0`
- `Period 7`

**EXPENSE_USER_GROUP_INFO**
- `None`

**VENDOR_ACCESS_LEVEL**
- `All`

**BANK_ACCESS_LEVEL**
- `All`

**CUSTOMER_ACCESS_LEVEL**
- `All`

**PROJECT_USER_GROUP_INFO**
- `None`

**LEDGER_USER_GROUP_INFO**
- `None`

**PAYROLL_USER_GROUP_INFO**
- `None`

**RETAIL_USER_GROUP_INFO**
- `None`

**RETAIL_ACCESS_LEVEL**
- `All`

**PURCHASE_USER_GROUP_INFO**
- `None`

**PERIOD_STATUS**
- `Open`
- `OnHold`
- `Closed`

**FIXED_ASSETS_USER_GROUP_INFO**
- `None`

**PRODUCTION_USER_GROUP_INFO**
- `None`

**FIXED_ASSETS_ACCESS_LEVEL**
- `All`

**INVENTORY_USER_GROUP_INFO**
- `None`

**PURCHASE_ACCESS_LEVEL**
- `All`

**EXPENSE_ACCESS_LEVEL**
- `All`

**INVENTORY_ACCESS_LEVEL**
- `All`

**PAYROLL_ACCESS_LEVEL**
- `All`

**TAX_USER_GROUP_INFO**
- `None`

**VENDOR_USER_GROUP_INFO**
- `None`

**BANK_USER_GROUP_INFO**
- `None`

**SALES_ACCESS_LEVEL**
- `All`

**FIXED_ASSETS_RU_ACCESS_LEVEL**
- `All`

**LEDGER_ACCESS_LEVEL**
- `All`

**CUSTOMER_USER_GROUP_INFO**
- `None`

**TAX_ACCESS_LEVEL**
- `All`

**SALES_USER_GROUP_INFO**
- `None`

**PROJECT_ACCESS_LEVEL**
- `All`

**PRODUCTION_ACCESS_LEVEL**
- `All`

**FIXED_ASSETS_RU_USER_GROUP_INFO**
- `None`

**ITM_ACCESS_LEVEL**
- `All`

**ITM_USER_GROUP_INFO**
- `None`

**SOURCE_FILE_NAME**
- `ledgerfiscalperiodsv2__20261116_105417.csv`

**MDP_CREATED_DATE**
- `2026-11-16 11:43:20.744205+00:00`

**MDP_MODIFIED_DATE**
- `2026-11-16 11:43:20.744205+00:00`

## Empty columns

Empty in every row: `EXPENSE_USER_GROUP_INFO`, `PROJECT_USER_GROUP_INFO`, `LEDGER_USER_GROUP_INFO`, `PAYROLL_USER_GROUP_INFO`, `RETAIL_USER_GROUP_INFO`, `PURCHASE_USER_GROUP_INFO`, `FIXED_ASSETS_USER_GROUP_INFO`, `PRODUCTION_USER_GROUP_INFO`, `INVENTORY_USER_GROUP_INFO`, `TAX_USER_GROUP_INFO`, `VENDOR_USER_GROUP_INFO`, `BANK_USER_GROUP_INFO`, `CUSTOMER_USER_GROUP_INFO`, `SALES_USER_GROUP_INFO`, `FIXED_ASSETS_RU_USER_GROUP_INFO`, `ITM_USER_GROUP_INFO`. Do not filter or group on them.
