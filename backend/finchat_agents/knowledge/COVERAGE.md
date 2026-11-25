# Knowledge coverage (2026-11-21)

Read-only report generated from `knowledge/tables/*.md`, `joins.yaml`, `examples.yaml` and the catalog workbook. Nothing was changed.

Notes on the inputs:
- The catalog file in the workspace is `finchat_v3_starter/data/table_catalog/tables.xlsx` (there is no `table_catalog.xlsx`); its `Tables` sheet was used. Sheets: Columns, Samples, Tables, fill_in, fill_in_draft_gold, fill_in_draft_silver, keys, values.
- Status: `ok` = active with a domain; `broken` = cannot be queried; `no domain` = active without a domain (not searchable); `superseded` = a copy whose source of truth is another table (`superseded_by`, the `adra_*` decision), excluded from search.
- Approved joins come from `joins.yaml` (status approved). `joins_proposed.yaml` holds proposals only and is not counted.
- Examples are counted per table they use (`examples.yaml`); one example can count for several tables.

## 1. Pages by schema

| schema | pages |
|---|---:|
| gold | 78 |
| silver | 65 |
| **total** | **143** |

## 2. Catalog vs pages

Catalog `Tables` sheet: 143 tables. Pages: 143.

**Catalog tables without a page (0):** none

**Pages without a catalog table (0):** none

## 3. Per page

| schema.table | domain | status | purpose | grain | PK | columns | with meaning | with synonyms | approved joins | examples (verified / unverified) |
|---|---|---|:-:|:-:|:-:|---:|---:|---:|---:|---|
| `gold.anomaly_audit` | - | no domain | y | y | y | 31 | 0 | 0 | 0 | 0 / 0 |
| `gold.capitalization_workbench` | fa | ok | y | y | y | 7 | 0 | 0 | 0 | 0 / 0 |
| `gold.depreciation_workbench` | fa | ok | y | y | y | 8 | 0 | 0 | 0 | 0 / 0 |
| `gold.dim_coa` | gl | ok | y | y | y | 11 | 0 | 0 | 0 | 0 / 0 |
| `gold.dim_coa_logistics` | gl | ok | y | y | y | 7 | 0 | 0 | 0 | 0 / 0 |
| `gold.disposal_workbench` | fa | ok | y | y | y | 11 | 0 | 0 | 0 | 0 / 0 |
| `gold.fa_asset_register` | fa | ok | y | y | y | 13 | 0 | 0 | 0 | 0 / 0 |
| `gold.fa_capitalized_value_trend` | fa | ok | y | y | y | 5 | 0 | 0 | 0 | 0 / 0 |
| `gold.fa_disposal_trends` | fa | ok | y | y | y | 5 | 0 | 0 | 0 | 0 / 0 |
| `gold.fa_kpi` | fa | ok | y | y | y | 6 | 0 | 0 | 0 | 0 / 0 |
| `gold.fa_monthly_depreciation_trend` | fa | ok | y | y | y | 4 | 0 | 0 | 0 | 0 / 0 |
| `gold.fact_ap_invoices` | ap | ok | y | y | y | 13 | 0 | 0 | 0 | 0 / 0 |
| `gold.fact_journal_entry_subledger_summary_balance` | subledger | ok | y | y | y | 28 | 0 | 0 | 0 | 0 / 0 |
| `gold.fact_trail_balance_extractions` | gl | ok | y | y | y | 4 | 0 | 0 | 0 | 0 / 0 |
| `gold.finance_chat_eval_results` | - | no domain | y | y | y | 38 | 0 | 0 | 0 | 0 / 0 |
| `gold.manage_bus_kpi` | gl | ok | y | y | y | 7 | 0 | 0 | 0 | 0 / 0 |
| `gold.manage_bus_report_lists` | - | no domain | y | y | y | 7 | 0 | 0 | 0 | 0 / 0 |
| `gold.manage_close_adra_reconciliation` | recon | superseded | y | y | y | 9 | 0 | 0 | 0 | 0 / 0 |
| `gold.manage_close_adra_reconciliation_kpi` | recon | superseded | y | y | y | 4 | 0 | 0 | 0 | 0 / 0 |
| `gold.manage_close_adra_reconciliation_status_kpi` | recon | superseded | y | y | y | 3 | 0 | 0 | 0 | 0 / 0 |
| `gold.manage_close_adra_unreconciled_accounts` | recon | superseded | y | y | y | 8 | 0 | 0 | 0 | 0 / 0 |
| `gold.manage_close_adra_unreconciled_accounts_kpi` | recon | superseded | y | y | y | 3 | 0 | 0 | 0 | 0 / 0 |
| `gold.manage_close_journal_entries` | gl | ok | y | y | y | 7 | 0 | 0 | 0 | 0 / 0 |
| `gold.managed_coll_due_soon_accounts` | ar | ok | y | y | y | 10 | 0 | 0 | 0 | 0 / 0 |
| `gold.managed_coll_early_payment_discounts` | ar | ok | y | y | y | 10 | 0 | 0 | 0 | 0 / 0 |
| `gold.managed_coll_kpi` | ar | ok | y | y | y | 5 | 0 | 0 | 0 | 0 / 0 |
| `gold.managed_coll_overdue` | ar | ok | y | y | y | 10 | 0 | 0 | 0 | 0 / 0 |
| `gold.mc_actual_cash_balance_by_bank_ac` | cash | ok | y | y | y | 5 | 0 | 0 | 0 | 0 / 0 |
| `gold.mc_actual_cash_balance_by_bank_ac_new` | cash | ok | y | y | y | 6 | 0 | 0 | 0 | 0 / 0 |
| `gold.mc_investment_portfolio` | gl | ok | y | y | y | 5 | 0 | 0 | 0 | 0 / 0 |
| `gold.mc_kpi` | cash | ok | y | y | y | 4 | 0 | 0 | 0 | 0 / 0 |
| `gold.mc_kpi_new` | cash | ok | y | y | y | 4 | 0 | 0 | 0 | 0 / 0 |
| `gold.mc_liquidity` | cash | ok | y | y | y | 5 | 0 | 0 | 0 | 0 / 0 |
| `gold.pipeline_logs` | - | no domain | y | y | y | 12 | 0 | 0 | 0 | 0 / 0 |
| `gold.portal_users_log` | - | no domain | y | y | y | 25 | 25 | 0 | 0 | 0 / 0 |
| `gold.vw_access_review` | - | no domain | y | y | y | 12 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_audit_extraction_toolkit` | - | no domain | y | y | y | 10 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_audit_soc_report` | - | no domain | y | y | y | 11 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_audit_soc_report_deepplinks` | - | no domain | y | y | y | 8 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_balance_sheet` | gl | ok | y | y | y | 29 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_balance_sheet_logistics` | gl | ok | y | y | y | 34 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_balance_sheet_logistics_layout` | gl | ok | y | y | y | 12 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_cash_reconciliation` | cash | ok | y | y | y | 23 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_commission_analysis_slr_mga` | subledger | broken | y | y | y | 34 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_commissions_analysis` | gl | ok | y | y | y | 53 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_expense_analysis` | gl | ok | y | y | y | 45 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_expense_analysis_gl` | gl | ok | y | y | y | 28 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_expense_analysis_slr` | subledger | broken | y | y | y | 27 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_fact_fynapse_slr_journals` | subledger | ok | y | y | y | 75 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_fact_kpmg_general_journals_entries` | gl | ok | y | y | y | 38 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_income_statement` | gl | ok | y | y | y | 75 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_income_statement_layout` | gl | ok | y | y | y | 12 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_income_statement_logistics` | gl | ok | y | y | y | 69 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_income_statement_logistics_layout` | gl | ok | y | y | y | 12 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_investment_analytics` | gl | ok | y | y | y | 57 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_kpi_pipeline_success` | - | no domain | y | y | y | 5 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_kpi_system_and_data_status` | - | no domain | y | y | y | 5 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_ledger_journal_trans_bi_entities` | gl | ok | y | y | y | 4 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_legal_entities` | gl | ok | y | y | y | 3 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_manage_close_journal_entry_kpi` | gl | ok | y | y | y | 5 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_manage_close_task` | recon | superseded | y | y | y | 8 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_manage_close_task_kpi` | recon | superseded | y | y | y | 4 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_managed_coll_due_soon_accounts` | ar | broken | y | y | y | 10 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_managed_coll_due_soon_accounts_filter` | ar | broken | y | y | y | 17 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_managed_coll_early_payment_discounts` | ar | broken | y | y | y | 10 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_managed_coll_early_payment_discounts_filter` | ar | broken | y | y | y | 17 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_managed_coll_kpi` | ar | broken | y | y | y | 5 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_managed_coll_kpi_filter` | ar | broken | y | y | y | 12 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_managed_coll_overdue` | ar | broken | y | y | y | 10 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_managed_coll_overdue_filter` | ar | broken | y | y | y | 17 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_premium_analysis` | subledger | ok | y | y | y | 38 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_review_controls` | - | no domain | y | y | y | 10 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_review_controls_access_by_area` | - | no domain | y | y | y | 11 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_review_controls_user_access_report` | - | no domain | y | y | y | 10 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_slr_gl_reconciliation` | subledger | ok | y | y | y | 14 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_subsidiary_ledgers` | gl | ok | y | y | y | 10 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_ultimates_analysis` | subledger | ok | y | y | y | 15 | 0 | 0 | 0 | 0 / 0 |
| `gold.vw_user_access_screen` | - | no domain | y | y | y | 9 | 0 | 0 | 0 | 0 / 0 |
| `silver.access_screen_dim_application` | - | no domain | y | y | y | 4 | 0 | 0 | 0 | 0 / 0 |
| `silver.access_screen_dim_employee` | - | no domain | y | y | y | 9 | 0 | 0 | 0 | 0 / 0 |
| `silver.access_screen_dim_legal_entity` | - | no domain | y | y | y | 4 | 0 | 0 | 0 | 0 / 0 |
| `silver.access_screen_dim_role` | - | no domain | y | y | y | 6 | 0 | 0 | 0 | 0 / 0 |
| `silver.access_screen_fact_certification` | - | no domain | y | y | y | 6 | 0 | 0 | 0 | 0 / 0 |
| `silver.access_screen_fact_certification_line` | - | no domain | y | y | y | 4 | 0 | 0 | 0 | 0 / 0 |
| `silver.access_screen_fact_employee_access` | - | no domain | y | y | y | 9 | 0 | 0 | 0 | 0 / 0 |
| `silver.access_screen_rel_manager_reportee` | - | no domain | y | y | y | 8 | 0 | 0 | 0 | 0 / 0 |
| `silver.adra_account_dimensions` | recon | ok | y | y | y | 29 | 10 | 7 | 2 | 0 / 8 |
| `silver.adra_account_facts` | recon | ok | y | y | y | 67 | 19 | 15 | 3 | 0 / 13 |
| `silver.adra_engagement_dimensions` | recon | ok | y | y | y | 12 | 3 | 2 | 1 | 0 / 0 |
| `silver.adra_legal_entity_dimensions` | recon | ok | y | y | y | 20 | 7 | 5 | 3 | 0 / 16 |
| `silver.adra_period_dimensions` | recon | ok | y | y | y | 22 | 9 | 6 | 2 | 0 / 17 |
| `silver.adra_tasks_company_dimension` | recon | ok | y | y | y | 10 | 0 | 0 | 0 | 0 / 0 |
| `silver.adra_tasks_task_facts` | recon | ok | y | y | y | 47 | 0 | 0 | 0 | 0 / 0 |
| `silver.adra_tasks_task_list_dimension` | recon | ok | y | y | y | 17 | 0 | 0 | 0 | 0 / 0 |
| `silver.adra_tasks_task_period_dimension` | recon | ok | y | y | y | 23 | 0 | 0 | 0 | 0 / 0 |
| `silver.adra_tasks_task_settings_dimension` | recon | ok | y | y | n | 20 | 0 | 0 | 0 | 0 / 0 |
| `silver.adra_transaction_facts` | recon | ok | y | y | y | 38 | 14 | 9 | 3 | 0 / 4 |
| `silver.audit_extraction_toolkit` | - | no domain | y | y | y | 10 | 0 | 0 | 0 | 0 / 0 |
| `silver.audit_soc_report` | - | no domain | y | y | y | 11 | 0 | 0 | 0 | 0 / 0 |
| `silver.audit_soc_report_deepplinks` | - | no domain | y | y | y | 8 | 0 | 0 | 0 | 0 / 0 |
| `silver.dim_bank_account_table_bi_entities` | cash | ok | y | y | y | 111 | 0 | 0 | 0 | 0 / 0 |
| `silver.dim_companies` | gl | ok | y | y | y | 11 | 0 | 0 | 0 | 0 / 0 |
| `silver.dim_customers_v3` | ar | ok | y | y | y | 316 | 0 | 0 | 0 | 0 / 0 |
| `silver.dim_fixed_asset_books` | fa | ok | y | y | y | 60 | 8 | 7 | 1 | 0 / 1 |
| `silver.dim_fixed_assets` | fa | ok | y | y | y | 69 | 7 | 7 | 2 | 0 / 0 |
| `silver.dim_ledger_bi_entities` | gl | ok | y | y | y | 12 | 0 | 0 | 0 | 0 / 0 |
| `silver.dim_ledger_fiscal_periods_v2` | gl | ok | y | y | y | 44 | 0 | 0 | 0 | 0 / 0 |
| `silver.dim_legal_entities` | gl | ok | y | y | y | 106 | 0 | 0 | 0 | 0 / 0 |
| `silver.dim_main_accounts` | gl | ok | y | y | y | 46 | 0 | 0 | 0 | 0 / 0 |
| `silver.dim_vendors` | ap | broken | y | y | n | 47 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_asset_journal` | fa | ok | y | y | y | 34 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_asset_master_transactions` | fa | ok | y | y | y | 31 | 7 | 6 | 1 | 0 / 0 |
| `silver.fact_cash_discounts` | ap | ok | y | y | n | 18 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_cust_table_bi_entities` | ar | ok | y | y | y | 200 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_cust_trans_opens` | ar | ok | y | y | y | 39 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_cust_transactions` | ar | broken | y | y | n | 85 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_customer_payment_journal_headers` | ar | ok | y | y | y | 12 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_customer_payment_journal_lines` | ar | ok | y | y | n | 69 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_exchange_rates` | gl | ok | y | y | y | 14 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_fynapse_slr_journals` | subledger | ok | y | y | y | 75 | 21 | 21 | 0 | 9 / 0 |
| `silver.fact_kpmg_general_journal_account_entries` | gl | ok | y | y | y | 38 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_kpmg_vend_payment_bi_vend_trans_open` | ap | ok | y | y | y | 17 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_ledger_journal_headers` | gl | ok | y | y | y | 17 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_ledger_journal_lines` | gl | ok | y | y | n | 128 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_ledger_journal_table_bi_entities` | gl | ok | y | y | n | 83 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_ledger_journal_trans_bi_entities` | gl | ok | y | y | y | 246 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_purchase_order_headers` | ap | ok | y | y | n | 128 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_purchase_order_lines` | ap | ok | y | y | n | 155 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_trail_balance_extractions` | gl | ok | y | y | n | 15 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_vend_invoice_jour_bi_entities` | ap | ok | y | y | y | 145 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_vendor_invoice_headers` | ap | ok | y | y | n | 135 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_vendor_invoice_journal_headers` | ap | ok | y | y | y | 17 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_vendor_invoice_journal_lines` | ap | ok | y | y | n | 87 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_vendor_invoice_lines` | ap | ok | y | y | n | 106 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_vendor_payment_journal_headers` | ap | ok | y | y | y | 16 | 0 | 0 | 0 | 0 / 0 |
| `silver.fact_vendor_payment_journal_lines` | ap | ok | y | y | n | 106 | 0 | 0 | 0 | 0 / 0 |
| `silver.manage_close_recon_account_dims` | recon | superseded | y | y | y | 28 | 0 | 0 | 0 | 0 / 0 |
| `silver.manage_close_recon_account_facts` | recon | superseded | y | y | y | 66 | 0 | 0 | 0 | 0 / 0 |
| `silver.manage_close_task_facts` | recon | superseded | y | y | y | 46 | 0 | 0 | 0 | 0 / 0 |
| `silver.manage_close_task_settings` | recon | superseded | y | y | y | 19 | 0 | 0 | 0 | 0 / 0 |
| `silver.review_controls` | - | no domain | y | y | y | 10 | 0 | 0 | 0 | 0 / 0 |
| `silver.review_controls_access_by_area` | - | no domain | y | y | y | 11 | 0 | 0 | 0 | 0 / 0 |
| `silver.review_controls_user_access_report` | - | no domain | y | y | y | 10 | 0 | 0 | 0 | 0 / 0 |

## 4. Totals

| measure | count |
|---|---:|
| pages | 143 |
| silver | 65 |
| gold | 78 |
| ok | 91 |
| broken | 12 |
| no domain | 29 |
| superseded | 11 |
| without grain | 0 |
| without primary key | 14 |
| without purpose | 0 |
| searchable (search_tables can return) | 91 |
| columns (all pages) | 4665 |
| columns with a business meaning | 130 |
| columns with synonyms | 85 |
| pages with at least one approved join | 9 |
| pages used by at least one example | 7 |
| examples | 27 |
| examples verified | 9 |
| catalog tables | 143 |
| catalog tables without page | 0 |
| pages not in catalog | 0 |

## 5. Reviewed CSVs in task 08

No. `fill_in_reviewed_silver.csv` and `fill_in_reviewed_gold.csv` were not in the workspace when task 08 ran, and they are still not there (`finchat_v3_starter/data/table_catalog/` holds only `tables.xlsx` and `README.md`). The generator supports them (`read_catalog(xlsx, reviewed_csvs=...)`, CLI `--reviewed`), and reviewed rows win over the draft sheets. Task 08 used the workbook's `fill_in_draft_silver` / `fill_in_draft_gold` sheets as the review input instead; nothing from them is marked `reviewed` on the pages. To apply the reviewed CSVs, place them in `data/table_catalog/` and re-run the generator.

## 6. Top 10 most incomplete pages in the domains ap, ar, cash, fa, gl, recon, subledger

The demo-domain list in the request was a placeholder (`<list your demo domains>`), so all configured domains were used. Score = missing purpose 3 + missing grain 3 + missing primary key 2 + up to 4 for the share of columns without a meaning + 1 without approved joins + 1 without examples (higher = less complete). Superseded and broken pages are excluded.

| # | schema.table | domain | score | missing |
|---:|---|---|---:|---|
| 1 | `silver.adra_tasks_task_settings_dimension` | recon | 8.0 | primary key; 20/20 columns without meaning; no approved joins; no examples |
| 2 | `silver.fact_cash_discounts` | ap | 8.0 | primary key; 18/18 columns without meaning; no approved joins; no examples |
| 3 | `silver.fact_customer_payment_journal_lines` | ar | 8.0 | primary key; 69/69 columns without meaning; no approved joins; no examples |
| 4 | `silver.fact_ledger_journal_lines` | gl | 8.0 | primary key; 128/128 columns without meaning; no approved joins; no examples |
| 5 | `silver.fact_ledger_journal_table_bi_entities` | gl | 8.0 | primary key; 83/83 columns without meaning; no approved joins; no examples |
| 6 | `silver.fact_purchase_order_headers` | ap | 8.0 | primary key; 128/128 columns without meaning; no approved joins; no examples |
| 7 | `silver.fact_purchase_order_lines` | ap | 8.0 | primary key; 155/155 columns without meaning; no approved joins; no examples |
| 8 | `silver.fact_trail_balance_extractions` | gl | 8.0 | primary key; 15/15 columns without meaning; no approved joins; no examples |
| 9 | `silver.fact_vendor_invoice_headers` | ap | 8.0 | primary key; 135/135 columns without meaning; no approved joins; no examples |
| 10 | `silver.fact_vendor_invoice_journal_lines` | ap | 8.0 | primary key; 87/87 columns without meaning; no approved joins; no examples |
