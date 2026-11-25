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
row_count: 5096
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
- `FY`: 5096 rows

**YEAR_NAME**
- `2021`: 392 rows
- `2016`: 392 rows
- `2018`: 392 rows
- `2023`: 392 rows
- `2026`: 392 rows
- `2022`: 392 rows
- `2020`: 392 rows
- `2017`: 392 rows
- `2019`: 392 rows
- `2025`: 392 rows
- `2014`: 392 rows
- `2015`: 392 rows
- `2024`: 392 rows

**PERIOD_NAME**
- `Period 1`: 364 rows
- `Period 6`: 364 rows
- `Period 10`: 364 rows
- `Period 8`: 364 rows
- `Period 11`: 364 rows
- `Period 13`: 364 rows
- `Period 12`: 364 rows
- `Period 9`: 364 rows
- `Period 2`: 364 rows
- `Period 5`: 364 rows
- `Period 4`: 364 rows
- `Period 3`: 364 rows
- `Period 0`: 364 rows
- `Period 7`: 364 rows

**EXPENSE_USER_GROUP_INFO**
- `None`: 5096 rows

**VENDOR_ACCESS_LEVEL**
- `All`: 5096 rows

**BANK_ACCESS_LEVEL**
- `All`: 5096 rows

**CUSTOMER_ACCESS_LEVEL**
- `All`: 5096 rows

**PROJECT_USER_GROUP_INFO**
- `None`: 5096 rows

**LEDGER_USER_GROUP_INFO**
- `None`: 5096 rows

**PAYROLL_USER_GROUP_INFO**
- `None`: 5096 rows

**RETAIL_USER_GROUP_INFO**
- `None`: 5096 rows

**RETAIL_ACCESS_LEVEL**
- `All`: 5096 rows

**PURCHASE_USER_GROUP_INFO**
- `None`: 5096 rows

**PERIOD_STATUS**
- `Open`: 4368 rows
- `OnHold`: 364 rows
- `Closed`: 364 rows

**FIXED_ASSETS_USER_GROUP_INFO**
- `None`: 5096 rows

**PRODUCTION_USER_GROUP_INFO**
- `None`: 5096 rows

**FIXED_ASSETS_ACCESS_LEVEL**
- `All`: 5096 rows

**INVENTORY_USER_GROUP_INFO**
- `None`: 5096 rows

**PURCHASE_ACCESS_LEVEL**
- `All`: 5096 rows

**EXPENSE_ACCESS_LEVEL**
- `All`: 5096 rows

**INVENTORY_ACCESS_LEVEL**
- `All`: 5096 rows

**PAYROLL_ACCESS_LEVEL**
- `All`: 5096 rows

**TAX_USER_GROUP_INFO**
- `None`: 5096 rows

**VENDOR_USER_GROUP_INFO**
- `None`: 5096 rows

**BANK_USER_GROUP_INFO**
- `None`: 5096 rows

**SALES_ACCESS_LEVEL**
- `All`: 5096 rows

**FIXED_ASSETS_RU_ACCESS_LEVEL**
- `All`: 5096 rows

**LEDGER_ACCESS_LEVEL**
- `All`: 5096 rows

**CUSTOMER_USER_GROUP_INFO**
- `None`: 5096 rows

**TAX_ACCESS_LEVEL**
- `All`: 5096 rows

**SALES_USER_GROUP_INFO**
- `None`: 5096 rows

**PROJECT_ACCESS_LEVEL**
- `All`: 5096 rows

**PRODUCTION_ACCESS_LEVEL**
- `All`: 5096 rows

**FIXED_ASSETS_RU_USER_GROUP_INFO**
- `None`: 5096 rows

**ITM_ACCESS_LEVEL**
- `All`: 5096 rows

**ITM_USER_GROUP_INFO**
- `None`: 5096 rows

**SOURCE_FILE_NAME**
- `ledgerfiscalperiodsv2__20261116_105417.csv`: 5096 rows

**MDP_CREATED_DATE**
- `2026-11-16 11:43:20.744205+00:00`: 5096 rows

**MDP_MODIFIED_DATE**
- `2026-11-16 11:43:20.744205+00:00`: 5096 rows

## Profile

Rows in the latest export: 5096.

| Column | Type | Distinct (approx) | Nulls | Min | Max |
|---|---|---|---|---|---|
| `LEDGER_NAME` | STRING | 29 | 0 |  |  |
| `CALENDAR` | STRING | 1 | 0 | FY | FY |
| `YEAR_NAME` | STRING | 13 | 0 | 2014 | 2026 |
| `PERIOD_NAME` | STRING | 14 | 0 | Period 0 | Period 9 |
| `LEGAL_ENTITY_ID` | STRING | 29 | 0 |  |  |
| `EXPENSE_USER_GROUP_INFO` | STRING | 0 | 5096 |  |  |
| `VENDOR_ACCESS_LEVEL` | STRING | 1 | 0 | All | All |
| `BANK_ACCESS_LEVEL` | STRING | 1 | 0 | All | All |
| `CUSTOMER_ACCESS_LEVEL` | STRING | 1 | 0 | All | All |
| `PROJECT_USER_GROUP_INFO` | STRING | 0 | 5096 |  |  |
| `LEDGER_USER_GROUP_INFO` | STRING | 0 | 5096 |  |  |
| `PAYROLL_USER_GROUP_INFO` | STRING | 0 | 5096 |  |  |
| `RETAIL_USER_GROUP_INFO` | STRING | 0 | 5096 |  |  |
| `RETAIL_ACCESS_LEVEL` | STRING | 1 | 0 | All | All |
| `PURCHASE_USER_GROUP_INFO` | STRING | 0 | 5096 |  |  |
| `PERIOD_STATUS` | STRING | 3 | 0 | Closed | Open |
| `FIXED_ASSETS_USER_GROUP_INFO` | STRING | 0 | 5096 |  |  |
| `PRODUCTION_USER_GROUP_INFO` | STRING | 0 | 5096 |  |  |
| `FIXED_ASSETS_ACCESS_LEVEL` | STRING | 1 | 0 | All | All |
| `INVENTORY_USER_GROUP_INFO` | STRING | 0 | 5096 |  |  |
| `PURCHASE_ACCESS_LEVEL` | STRING | 1 | 0 | All | All |
| `EXPENSE_ACCESS_LEVEL` | STRING | 1 | 0 | All | All |
| `INVENTORY_ACCESS_LEVEL` | STRING | 1 | 0 | All | All |
| `PAYROLL_ACCESS_LEVEL` | STRING | 1 | 0 | All | All |
| `TAX_USER_GROUP_INFO` | STRING | 0 | 5096 |  |  |
| `VENDOR_USER_GROUP_INFO` | STRING | 0 | 5096 |  |  |
| `BANK_USER_GROUP_INFO` | STRING | 0 | 5096 |  |  |
| `SALES_ACCESS_LEVEL` | STRING | 1 | 0 | All | All |
| `FIXED_ASSETS_RU_ACCESS_LEVEL` | STRING | 1 | 0 | All | All |
| `LEDGER_ACCESS_LEVEL` | STRING | 1 | 0 | All | All |
| `CUSTOMER_USER_GROUP_INFO` | STRING | 0 | 5096 |  |  |
| `TAX_ACCESS_LEVEL` | STRING | 1 | 0 | All | All |
| `SALES_USER_GROUP_INFO` | STRING | 0 | 5096 |  |  |
| `PROJECT_ACCESS_LEVEL` | STRING | 1 | 0 | All | All |
| `PRODUCTION_ACCESS_LEVEL` | STRING | 1 | 0 | All | All |
| `FIXED_ASSETS_RU_USER_GROUP_INFO` | STRING | 0 | 5096 |  |  |
| `ITM_ACCESS_LEVEL` | STRING | 1 | 0 | All | All |
| `ITM_USER_GROUP_INFO` | STRING | 0 | 5096 |  |  |
| `SOURCE_FILE_NAME` | STRING | 1 | 0 | ledgerfiscalperiodsv2__20261116_10541... | ledgerfiscalperiodsv2__20261116_10541... |
| `HASH_KEY` | STRING | 4914 | 0 |  |  |
| `MDP_CREATED_BY` | STRING | 1 | 0 |  |  |
| `MDP_CREATED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:43:20.744000 | 2026-11-16 11:43:20.744000 |
| `MDP_MODIFIED_BY` | STRING | 1 | 0 |  |  |
| `MDP_MODIFIED_DATE` | TIMESTAMP | 1 | 0 | 2026-11-16 11:43:20.744000 | 2026-11-16 11:43:20.744000 |

## Sample rows

| CALENDAR | YEAR_NAME | PERIOD_NAME | EXPENSE_USER_GROUP_INFO | VENDOR_ACCESS_LEVEL | BANK_ACCESS_LEVEL | CUSTOMER_ACCESS_LEVEL | PROJECT_USER_GROUP_INFO | LEDGER_USER_GROUP_INFO | PAYROLL_USER_GROUP_INFO | RETAIL_USER_GROUP_INFO | RETAIL_ACCESS_LEVEL | PURCHASE_USER_GROUP_INFO | PERIOD_STATUS | FIXED_ASSETS_USER_GROUP_INFO | PRODUCTION_USER_GROUP_INFO | FIXED_ASSETS_ACCESS_LEVEL | INVENTORY_USER_GROUP_INFO | PURCHASE_ACCESS_LEVEL | EXPENSE_ACCESS_LEVEL | INVENTORY_ACCESS_LEVEL | PAYROLL_ACCESS_LEVEL | TAX_USER_GROUP_INFO | VENDOR_USER_GROUP_INFO | BANK_USER_GROUP_INFO | SALES_ACCESS_LEVEL | FIXED_ASSETS_RU_ACCESS_LEVEL | LEDGER_ACCESS_LEVEL | CUSTOMER_USER_GROUP_INFO | TAX_ACCESS_LEVEL | SALES_USER_GROUP_INFO | PROJECT_ACCESS_LEVEL | PRODUCTION_ACCESS_LEVEL | FIXED_ASSETS_RU_USER_GROUP_INFO | ITM_ACCESS_LEVEL | ITM_USER_GROUP_INFO | SOURCE_FILE_NAME | MDP_CREATED_BY | MDP_CREATED_DATE | MDP_MODIFIED_BY | MDP_MODIFIED_DATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FY | 2020 | Period 11 | NULL | All | All | All | NULL | NULL | NULL | NULL | All | NULL | Open | NULL | NULL | All | NULL | All | All | All | All | NULL | NULL | NULL | All | All | All | NULL | All | NULL | All | All | NULL | All | NULL | ledgerfiscalperiodsv2__20261116_10541... | <masked> | 2026-11-16 11:43:20.744000 | <masked> | 2026-11-16 11:43:20.744000 |
| FY | 2020 | Period 12 | NULL | All | All | All | NULL | NULL | NULL | NULL | All | NULL | Open | NULL | NULL | All | NULL | All | All | All | All | NULL | NULL | NULL | All | All | All | NULL | All | NULL | All | All | NULL | All | NULL | ledgerfiscalperiodsv2__20261116_10541... | <masked> | 2026-11-16 11:43:20.744000 | <masked> | 2026-11-16 11:43:20.744000 |
| FY | 2021 | Period 1 | NULL | All | All | All | NULL | NULL | NULL | NULL | All | NULL | Open | NULL | NULL | All | NULL | All | All | All | All | NULL | NULL | NULL | All | All | All | NULL | All | NULL | All | All | NULL | All | NULL | ledgerfiscalperiodsv2__20261116_10541... | <masked> | 2026-11-16 11:43:20.744000 | <masked> | 2026-11-16 11:43:20.744000 |
| FY | 2021 | Period 2 | NULL | All | All | All | NULL | NULL | NULL | NULL | All | NULL | Open | NULL | NULL | All | NULL | All | All | All | All | NULL | NULL | NULL | All | All | All | NULL | All | NULL | All | All | NULL | All | NULL | ledgerfiscalperiodsv2__20261116_10541... | <masked> | 2026-11-16 11:43:20.744000 | <masked> | 2026-11-16 11:43:20.744000 |
| FY | 2021 | Period 3 | NULL | All | All | All | NULL | NULL | NULL | NULL | All | NULL | Open | NULL | NULL | All | NULL | All | All | All | All | NULL | NULL | NULL | All | All | All | NULL | All | NULL | All | All | NULL | All | NULL | ledgerfiscalperiodsv2__20261116_10541... | <masked> | 2026-11-16 11:43:20.744000 | <masked> | 2026-11-16 11:43:20.744000 |
