# Catalog review

Generated 2026-11-21 from the catalog export by `knowledge/generator.py` + `knowledge/review.py`.
Approve by editing the table pages (set the field, add it to `reviewed`, remove it from `proposed_fields`) or by
moving joins from `joins_proposed.yaml` to `joins.yaml` with `status: approved`. Rerun the generator afterwards.

## Summary

- Tables in the export: 143; pages: 143; searchable now: 91
- Without a domain (excluded from search): 29
- Broken (excluded from search and run_sql): 12
- Superseded copies (excluded from search and run_sql): 11
- Low confidence or repaired draft rows: 24
- Tables with proposed keys / grains: 62
- Duplicate warnings: 11 (of which 3 reviewed pages where the export shows 0 duplicates)
- Personal-data columns (masked, never listed): 234 in 80 tables
- Tables with values altered by Excel: 12
- Proposed joins: 171; lineage links: 158

## 1. Missing domains (excluded from search until set)

| Table | Purpose (draft) | Confidence | Notes |
|---|---|---|---|
| `gold.anomaly_audit` | Flags anomalies in insurance and expense transactions for data-quality review. | medium | No matching silver table is clear from the listed inputs; source files are Concur; Novidea and RPM. RATE_CATEGORY and OPERATOR_UNIQUE_ID are all null; CLASS_COD |
| `gold.finance_chat_eval_results` | Stores finance-chat evaluation case outcomes; correctness checks and latency measurements. | medium | No unique key was detected; suggested key combines run; case and execution time. Table is empty. |
| `gold.manage_bus_report_lists` | Catalog of management; control and financial reports with owners and links. | high | Static report catalog rather than transactional data. |
| `gold.pipeline_logs` | Records pipeline executions; source files; outcomes and failure reasons. | medium | Process_ID is repeated (841 distinct in 870 rows); Reason is null in 866 rows; HASH_KEY has 907 distinct values. |
| `gold.portal_users_log` | Audits Digital Finance Portal sign-in events from Entra ID. | high | Comment identifies this as sample data; signin_id has 46 distinct values across 50 rows. |
| `gold.vw_access_review` | Shows managers; reportees and assigned application access for certification. | medium | No unique key was detected; APPROVED_BY and APPROVED_TIMESTAMP are all null. |
| `gold.vw_audit_extraction_toolkit` | Lists audit extracts; source systems; formats and links. | high | Static reference data. |
| `gold.vw_audit_soc_report` | Summarizes the SOC 1 report; coverage period; opinion and exceptions. | high |  |
| `gold.vw_audit_soc_report_deepplinks` | Provides links to the SOC 1 report and bridge letter. | high | Static reference data. |
| `gold.vw_kpi_pipeline_success` | Summarizes successful pipeline runs as a success rate by source system. | medium | LEGAL_ENTITY contains source-system values (D365; Fynapse; Concur; Novidea) rather than legal entities. |
| `gold.vw_kpi_system_and_data_status` | Summarizes pipeline completion and data-quality anomaly counts. | medium | LEGAL_ENTITY is null for all rows; summary has no system field. |
| `gold.vw_review_controls` | Lists review controls; owners and links to control evidence. | high |  |
| `gold.vw_review_controls_access_by_area` | Shows access permissions by role and product area. | high |  |
| `gold.vw_review_controls_user_access_report` | Summarizes each user's role and areas they can access or change. | high |  |
| `gold.vw_user_access_screen` | Shows managers and their reportees with application and legal-entity access. | medium | No unique key was detected; proposed key follows manager/reportee and access dimensions. |
| `silver.access_screen_dim_application` | Lists the applications (D365; Fynapse; Power BI; UI) covered by the user access review. | high | Domain left empty: access governance not finance. |
| `silver.access_screen_dim_employee` | People (managers and reportees) in the access review with department; history kept by effective dates. | high | Domain left empty: access governance. effective_to all-null just means no row is closed yet. |
| `silver.access_screen_dim_legal_entity` | Master list of legal entities used in the access review. | high | Only 3 placeholder entities (Entity 234/345/456). |
| `silver.access_screen_dim_role` | Access types (roles) available per application in the access review. | high |  |
| `silver.access_screen_fact_certification` | Monthly certification by a manager that their reportees' access was reviewed. | high |  |
| `silver.access_screen_fact_certification_line` | Links each manager certification to the access rows it covered. | high |  |
| `silver.access_screen_fact_employee_access` | Shows which access type each employee holds on which legal entity. | high |  |
| `silver.access_screen_rel_manager_reportee` | Maps each manager to their reportees for access certification. | high |  |
| `silver.audit_extraction_toolkit` | List of audit data extracts with source system; format and download link. | high | Domain left empty: audit tooling. Static reference data loaded from CSV. |
| `silver.audit_soc_report` | Summary of the SOC 1 report (period covered; opinion; exceptions). | high | Domain left empty: audit artifacts. Static reference data from CSV. |
| `silver.audit_soc_report_deepplinks` | Links to download the SOC 1 report and request the bridge letter. | high | Domain left empty. Static reference data from CSV. |
| `silver.review_controls` | List of review controls (reference; requirement; owner; report link). | high | Domain left empty: controls. Static reference data from CSV. |
| `silver.review_controls_access_by_area` | Shows which role (CFO; Controller; AR/AP Clerk) can do what in each product area. | high | Domain left empty. Static reference data from CSV. |
| `silver.review_controls_user_access_report` | Summary of each user's role and number of areas they can access or change. | high | Domain left empty. Static sample data from CSV. |

## 2. Broken objects (for the data team)

| Table | Error |
|---|---|
| `gold.vw_commission_analysis_slr_mga` | the profiling query failed in the catalog export (no row count); the error text is not in the workbook |
| `gold.vw_expense_analysis_slr` | the profiling query failed in the catalog export (no row count); the error text is not in the workbook |
| `gold.vw_managed_coll_due_soon_accounts` | the profiling query failed in the catalog export (no row count); the error text is not in the workbook |
| `gold.vw_managed_coll_due_soon_accounts_filter` | the profiling query failed in the catalog export (no row count); the error text is not in the workbook |
| `gold.vw_managed_coll_early_payment_discounts` | the profiling query failed in the catalog export (no row count); the error text is not in the workbook |
| `gold.vw_managed_coll_early_payment_discounts_filter` | the profiling query failed in the catalog export (no row count); the error text is not in the workbook |
| `gold.vw_managed_coll_kpi` | the profiling query failed in the catalog export (no row count); the error text is not in the workbook |
| `gold.vw_managed_coll_kpi_filter` | the profiling query failed in the catalog export (no row count); the error text is not in the workbook |
| `gold.vw_managed_coll_overdue` | the profiling query failed in the catalog export (no row count); the error text is not in the workbook |
| `gold.vw_managed_coll_overdue_filter` | the profiling query failed in the catalog export (no row count); the error text is not in the workbook |
| `silver.dim_vendors` | the profiling query failed in the catalog export (no row count); the error text is not in the workbook |
| `silver.fact_cust_transactions` | the profiling query failed in the catalog export (no row count); the error text is not in the workbook |

## 2b. Superseded copies (decision: use the source of truth)

| Table | Use instead |
|---|---|
| `gold.manage_close_adra_reconciliation` | `silver.adra_account_facts` |
| `gold.manage_close_adra_reconciliation_kpi` | `silver.adra_account_facts` |
| `gold.manage_close_adra_reconciliation_status_kpi` | `silver.adra_account_facts` |
| `gold.manage_close_adra_unreconciled_accounts` | `silver.adra_account_facts`, `silver.adra_account_dimensions` |
| `gold.manage_close_adra_unreconciled_accounts_kpi` | `silver.adra_account_facts` |
| `gold.vw_manage_close_task` | `silver.adra_tasks_task_facts` |
| `gold.vw_manage_close_task_kpi` | `silver.adra_tasks_task_facts` |
| `silver.manage_close_recon_account_dims` | `silver.adra_account_dimensions` |
| `silver.manage_close_recon_account_facts` | `silver.adra_account_facts` |
| `silver.manage_close_task_facts` | `silver.adra_tasks_task_facts` |
| `silver.manage_close_task_settings` | `silver.adra_tasks_task_settings_dimension` |

## 3. Low-confidence and repaired rows

Repaired = the draft row was misaligned (values in the wrong columns) and was rebuilt from what each cell contains:
check entity, period and PII columns in particular.

| Table | Confidence | Repaired | Domain | Notes |
|---|---|---|---|---|
| `gold.depreciation_workbench` | high | yes | fa |  |
| `gold.fa_disposal_trends` | high | yes | fa | Only seven monthly rows; YEAR is 2026 for all. |
| `gold.mc_actual_cash_balance_by_bank_ac_new` | low |  | cash | Table is empty (0 rows); no source linkage beyond the table name could be confirmed. |
| `gold.mc_kpi_new` | low | yes | cash |  |
| `gold.vw_audit_soc_report` | high | yes | - |  |
| `gold.vw_balance_sheet_logistics_layout` | high | yes | gl | Static presentation layout; join by BS_LINE. |
| `gold.vw_income_statement_layout` | high | yes | gl | Static presentation layout; join by IS_LINE. |
| `gold.vw_income_statement_logistics_layout` | high | yes | gl | Static presentation layout; join by IS_LINE. |
| `gold.vw_ledger_journal_trans_bi_entities` | low | yes | gl |  |
| `gold.vw_legal_entities` | high | yes | gl |  |
| `gold.vw_manage_close_journal_entry_kpi` | medium | yes | gl |  |
| `gold.vw_manage_close_task_kpi` | medium | yes | recon |  |
| `gold.vw_managed_coll_kpi` | medium | yes | ar |  |
| `silver.adra_tasks_task_settings_dimension` | low |  | recon | Grain guessed: TASK_SETTING_KEY has 231 distinct in 228 rows and contains odd values (text in key column); ENGAGEMENT_KEY contains 'Periodic' so columns look shifted in some rows. |
| `silver.dim_customers_v3` | low |  | ar | Only 3 rows and values look misaligned (dataAreaId contains USA" / DALLAS; CustomerAccount contains ' TX 75207') so address text with commas has shifted columns. Wide table; PII (customer name/contact |
| `silver.dim_vendors` | low |  | ap | No row counts so table appears empty. Vendor names are business names not people. |
| `silver.fact_cust_table_bi_entities` | low |  | ar | Key should probably be DATA_AREA_ID + ACCOUNT_NUM; only 1 row so cannot tell. |
| `silver.fact_cust_trans_opens` | low |  | ar | Key should probably be SYS_REC_ID; only 1 row so cannot tell. |
| `silver.fact_cust_transactions` | low |  | ar | Column names use CamelCase and odata_etag so looks OData loaded. |
| `silver.fact_ledger_journal_table_bi_entities` | low |  | gl | Data looks corrupted: DATA_AREA_ID contains long posting-error messages and numeric columns hold text so columns are shifted (likely CSV quoting problem). |
| `silver.fact_vendor_invoice_headers` | low |  | ap | Only 5 rows. |
| `silver.fact_vendor_invoice_journal_lines` | low |  | ap | Data looks shifted: DATA_AREA_ID holds city names; LINE_NUMBER holds 'NJ 07058' / 'USA' (address text split by commas). |
| `silver.fact_vendor_invoice_lines` | low |  | ap | Only 5 rows. |
| `silver.fact_vendor_payment_journal_lines` | low |  | ap | Data looks shifted: DATA_AREA_ID holds city names and JOURNAL_BATCH_NUMBER holds state/zip text (address split by commas). |

## 4. Proposed keys and grains

| Table | Proposed | Grain | Primary key |
|---|---|---|---|
| `gold.anomaly_audit` | grain, primary_key | one row per HASH_KEY (one flagged or evaluated source transaction) | HASH_KEY |
| `gold.capitalization_workbench` | grain, primary_key | one row per ASSET_ID (one asset awaiting capitalization) | ASSET_ID |
| `gold.depreciation_workbench` | grain, primary_key | one row per JOURNAL_ID + ASSET_ID (one asset in a depreciation journal) | JOURNAL_ID, ASSET_ID |
| `gold.disposal_workbench` | grain, primary_key | one row per ASSET_ID (one asset disposal) | ASSET_ID |
| `gold.fa_asset_register` | grain, primary_key | one row per ASSET_ID (one fixed asset) | ASSET_ID |
| `gold.fa_capitalized_value_trend` | grain, primary_key | one row per FIXED_ASSET_NUMBER (one asset acquisition) | FIXED_ASSET_NUMBER |
| `gold.fa_disposal_trends` | grain, primary_key | one row per MONTH (one monthly disposal count) | MONTH |
| `gold.managed_coll_overdue` | grain, primary_key | one row per INVOICE_NUMBER (one overdue invoice) | INVOICE_NUMBER |
| `gold.pipeline_logs` | grain, primary_key | one row per Process_ID (one pipeline execution) | Process_ID |
| `gold.portal_users_log` | grain, primary_key | one row per signin_id (one sign-in event) | signin_id |
| `gold.vw_audit_extraction_toolkit` | grain, primary_key | one row per HASH_KEY (one audit extract option) | HASH_KEY |
| `gold.vw_audit_soc_report` | entity_column, grain | one row per HASH_KEY (one SOC report) | Period_covered, Issued |
| `gold.vw_audit_soc_report_deepplinks` | grain, primary_key | one row per HASH_KEY (one document link) | HASH_KEY |
| `gold.vw_fact_fynapse_slr_journals` | grain, primary_key | one row per JOURNAL_LINE_ID (one Fynapse journal line) | JOURNAL_LINE_ID |
| `gold.vw_fact_kpmg_general_journals_entries` | grain, primary_key | one row per GENERAL_JOURNAL_ACCOUNT_ENTRY_REC_ID (one GL posting line) | GENERAL_JOURNAL_ACCOUNT_ENTRY_REC_ID |
| `gold.vw_income_statement` | grain, primary_key | one row per ENTRY_REC_ID (one GL journal line) | ENTRY_REC_ID |
| `gold.vw_investment_analytics` | grain, primary_key | one row per ENTRY_REC_ID (one GL journal line) | ENTRY_REC_ID |
| `gold.vw_manage_close_task` | grain, primary_key | one row per TASK_KEY (one close task) | TASK_KEY |
| `gold.vw_review_controls` | grain, primary_key | one row per HASH_KEY (one control) | HASH_KEY |
| `gold.vw_review_controls_access_by_area` | grain, primary_key | one row per HASH_KEY (one product-area permission record) | HASH_KEY |
| `gold.vw_review_controls_user_access_report` | grain, primary_key | one row per HASH_KEY (one user access summary) | HASH_KEY |
| `silver.access_screen_dim_application` | grain | one row per application_id (one application in scope) | application_id |
| `silver.access_screen_dim_employee` | grain | one row per employee_email + effective_from (one person version) | employee_email, effective_from |
| `silver.access_screen_dim_legal_entity` | grain | one row per legal_entity_id (one legal entity) | legal_entity_id |
| `silver.access_screen_dim_role` | grain | one row per role_id (one role of one application) | role_id |
| `silver.access_screen_fact_certification` | grain | one row per certification_id (one manager certification for a month) | certification_id |
| `silver.access_screen_fact_certification_line` | grain | one row per certification_line_id (one access row covered by one certification) | certification_line_id |
| `silver.access_screen_fact_employee_access` | grain | one row per access_id (one employee-role-entity access grant) | access_id |
| `silver.access_screen_rel_manager_reportee` | grain | one row per relationship_id (one manager-reportee link) | relationship_id |
| `silver.adra_tasks_company_dimension` | grain, primary_key | one row per COMPANY_KEY (one company) | COMPANY_KEY |
| `silver.adra_tasks_task_facts` | grain, primary_key | one row per TASK_KEY (one close task) | TASK_KEY |
| `silver.adra_tasks_task_list_dimension` | grain, primary_key | one row per TASK_LIST_KEY (one task list) | TASK_LIST_KEY |
| `silver.adra_tasks_task_period_dimension` | grain, primary_key | one row per PERIOD_KEY (one period) | PERIOD_KEY |
| `silver.audit_extraction_toolkit` | grain, primary_key | one row per HASH_KEY (one extract option) | HASH_KEY |
| `silver.audit_soc_report` | grain, primary_key | one row per HASH_KEY (one SOC report) | HASH_KEY |
| `silver.audit_soc_report_deepplinks` | grain, primary_key | one row per HASH_KEY (one link) | HASH_KEY |
| `silver.dim_bank_account_table_bi_entities` | grain, primary_key | one row per DATA_AREA_ID + ACCOUNT_ID (one bank account of one company) | DATA_AREA_ID, ACCOUNT_ID |
| `silver.dim_companies` | grain, primary_key | one row per HASH_KEY (one company) | HASH_KEY |
| `silver.dim_customers_v3` | grain, primary_key | one row per HASH_KEY (one customer) | HASH_KEY |
| `silver.dim_ledger_bi_entities` | grain, primary_key | one row per source_key (one ledger) | source_key |
| `silver.dim_ledger_fiscal_periods_v2` | grain, primary_key | one row per HASH_KEY (one fiscal period of one ledger) | HASH_KEY |
| `silver.dim_legal_entities` | grain, primary_key | one row per legal_entity_id (one legal entity) | legal_entity_id |
| `silver.dim_main_accounts` | grain, primary_key | one row per MAIN_ACCOUNT_REC_ID (one main account in a chart) | MAIN_ACCOUNT_REC_ID |
| `silver.fact_asset_journal` | grain, primary_key | one row per HASH_KEY (one fixed asset journal line) | HASH_KEY |
| `silver.fact_cust_table_bi_entities` | grain, primary_key | one row per DATA_AREA_ID (one customer; table has only 1 row) | DATA_AREA_ID |
| `silver.fact_cust_trans_opens` | grain, primary_key | one row per DATA_AREA_ID (one open customer transaction; table has only 1 row) | DATA_AREA_ID |
| `silver.fact_customer_payment_journal_headers` | grain, primary_key | one row per HASH_KEY (one customer payment journal batch) | HASH_KEY |
| `silver.fact_exchange_rates` | grain, primary_key | one row per HASH_KEY (one rate for a currency pair and date range) | HASH_KEY |
| `silver.fact_kpmg_general_journal_account_entries` | grain, primary_key | one row per GENERAL_JOURNAL_ACCOUNT_ENTRY_REC_ID (one GL posting line) | GENERAL_JOURNAL_ACCOUNT_ENTRY_REC_ID |
| `silver.fact_kpmg_vend_payment_bi_vend_trans_open` | grain, primary_key | one row per REF_REC_ID (one open vendor invoice) | REF_REC_ID |
| `silver.fact_ledger_journal_headers` | grain, primary_key | one row per HASH_KEY (one journal batch) | HASH_KEY |
| `silver.fact_ledger_journal_trans_bi_entities` | grain, primary_key | one row per SOURCE_KEY (one ledger journal line) | SOURCE_KEY |
| `silver.fact_vend_invoice_jour_bi_entities` | grain, primary_key | one row per SOURCE_KEY (one vendor invoice journal entry) | SOURCE_KEY |
| `silver.fact_vendor_invoice_journal_headers` | grain, primary_key | one row per HASH_KEY (one vendor invoice journal batch) | HASH_KEY |
| `silver.fact_vendor_payment_journal_headers` | grain, primary_key | one row per HASH_KEY (one vendor payment journal batch) | HASH_KEY |
| `silver.manage_close_recon_account_dims` | grain, primary_key | one row per Account_Key (one reconciliation account) | Account_Key |
| `silver.manage_close_recon_account_facts` | grain, primary_key | one row per Account_Key (one account reconciliation) | Account_Key |
| `silver.manage_close_task_facts` | grain, primary_key | one row per HASH_KEY (one close task) | HASH_KEY |
| `silver.manage_close_task_settings` | grain, primary_key | one row per HASH_KEY (one task definition) | HASH_KEY |
| `silver.review_controls` | grain, primary_key | one row per HASH_KEY (one control) | HASH_KEY |
| `silver.review_controls_access_by_area` | grain, primary_key | one row per HASH_KEY (one product area) | HASH_KEY |
| `silver.review_controls_user_access_report` | grain, primary_key | one row per HASH_KEY (one user) | HASH_KEY |

## 5. Draft values not used

| Table | Problem |
|---|---|
| `silver.manage_close_task_facts` | pii_columns: 'and likely other preparer/approver name columns' is not a column of the table |

## 6. Personal-data columns

Masked in results and never listed. Columns are flagged from the drafts and by name (names, usernames, emails,
contact people, created/modified-by). Remove one from `pii_columns` only if it holds no personal data.

| Table | Personal-data columns |
|---|---|
| `gold.anomaly_audit` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `gold.manage_bus_report_lists` | OWNER |
| `gold.manage_close_adra_reconciliation` | PREPARER, REVIEWER |
| `gold.managed_coll_due_soon_accounts` | email |
| `gold.managed_coll_early_payment_discounts` | email |
| `gold.managed_coll_overdue` | EMAIL |
| `gold.pipeline_logs` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `gold.portal_users_log` | user_principal_name, user_display_name |
| `gold.vw_access_review` | MANAGER_EMAIL, MANAGER, REPORTEE, REPORTEE_EMAIL, APPROVED_BY |
| `gold.vw_audit_extraction_toolkit` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `gold.vw_audit_soc_report` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `gold.vw_audit_soc_report_deepplinks` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `gold.vw_fact_kpmg_general_journals_entries` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `gold.vw_managed_coll_due_soon_accounts` | email |
| `gold.vw_managed_coll_due_soon_accounts_filter` | email |
| `gold.vw_managed_coll_early_payment_discounts` | email |
| `gold.vw_managed_coll_early_payment_discounts_filter` | email |
| `gold.vw_managed_coll_overdue` | EMAIL |
| `gold.vw_managed_coll_overdue_filter` | EMAIL |
| `gold.vw_review_controls` | Owner, MDP_CREATED_BY, MDP_MODIFIED_BY |
| `gold.vw_review_controls_access_by_area` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `gold.vw_review_controls_user_access_report` | User, MDP_CREATED_BY, MDP_MODIFIED_BY |
| `gold.vw_user_access_screen` | MANAGER_NAME, EMAIL_ID, REPORTEE_NAME, REPORTEE_EMAIL_ID |
| `silver.access_screen_dim_employee` | employee_email, employee_name |
| `silver.access_screen_fact_certification` | manager_email, certified_by_login |
| `silver.access_screen_fact_employee_access` | employee_email |
| `silver.access_screen_rel_manager_reportee` | manager_email, reportee_email |
| `silver.adra_account_dimensions` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.adra_account_facts` | PREPARER_NAME, APPROVER_NAME, PREPARED_BY_NAME, APPROVED_BY_NAME, PREPARER_USERNAME, APPROVER_USERNAME, REVIEWER_USERNAME, REVIEWER_NAME, ASSIGNED_TO_USERNAME, ASSIGNED_TO_NAME, PREPARED_BY_USERNAME, APPROVED_BY_USERNAME, REVIEWED_BY_NAME, REVIEWED_BY_USERNAME, MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.adra_engagement_dimensions` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.adra_legal_entity_dimensions` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.adra_period_dimensions` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.adra_tasks_company_dimension` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.adra_tasks_task_facts` | TASK_PREPARER, TASK_PREPARER_NAME, TASK_APPROVER, TASK_APPROVER_NAME, TASK_PREPARED_BY_NAME, TASK_PREPARED_BY_USERNAME, TASK_LAST_APPROVED_BY_NAME, TASK_LAST_APPROVED_BY_USERNAME, TASK_ADDED_BY_NAME, TASK_ADDED_BY_USERNAME, MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.adra_tasks_task_list_dimension` | TASK_LIST_CREATED_BY_USER_NAME, TASK_LIST_CREATED_BY_NAME, MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.adra_tasks_task_period_dimension` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.adra_tasks_task_settings_dimension` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.adra_transaction_facts` | ITEM_ADDED_BY_NAME, ITEM_ADDED_BY_USERNAME, MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.audit_extraction_toolkit` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.audit_soc_report` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.audit_soc_report_deepplinks` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.dim_bank_account_table_bi_entities` | PAGER, PHONE, EMAIL, CONTACT_PERSON, MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.dim_companies` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.dim_customers_v3` | PrimaryContactEmailIsIM, PrimaryContactEmail, PrimaryContactEmailDescription, ReceiptEmail, PrimaryContactEmailPurpose, PrimaryContactEmailRecordId, MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.dim_fixed_asset_books` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.dim_fixed_assets` | CONTACT_NAME, RESPONSIBLE_NAME, MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.dim_ledger_fiscal_periods_v2` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.dim_legal_entities` | primary_contact_email_description, primary_contact_email_purpose, primary_contact_email, primary_contact_email_is_im, mdp_created_by, mdp_modified_by |
| `silver.dim_main_accounts` | USER_NAME, MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.dim_vendors` | PRIMARY_EMAIL_ADDRESS, MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_asset_journal` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_asset_master_transactions` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_cash_discounts` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_cust_table_bi_entities` | CONTACT_PERSON_ID, MAIN_CONTACT_WORKER, SYS_MODIFIED_BY, MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_cust_trans_opens` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_customer_payment_journal_headers` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_exchange_rates` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_kpmg_general_journal_account_entries` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_kpmg_vend_payment_bi_vend_trans_open` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_ledger_journal_headers` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_ledger_journal_lines` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_ledger_journal_table_bi_entities` | REJECTED_BY, SYS_CREATED_BY, APPROVER, SYS_MODIFIED_BY, MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_ledger_journal_trans_bi_entities` | APPROVER, R_CASH_DOC_REPRES_PERSON_ID, MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_purchase_order_headers` | EMAIL, CONTACT_PERSON_ID, MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_purchase_order_lines` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_trail_balance_extractions` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_vend_invoice_jour_bi_entities` | SYS_CREATED_BY, VENDOR_REQUESTED_WORKER_EMAIL, MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_vendor_invoice_headers` | VENDOR_REQUESTED_WORKER_EMAIL, MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_vendor_invoice_journal_headers` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_vendor_invoice_journal_lines` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_vendor_invoice_lines` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_vendor_payment_journal_headers` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.fact_vendor_payment_journal_lines` | CONTACT_PERSON, MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.manage_close_recon_account_dims` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.manage_close_recon_account_facts` | PreparerUsername, PreparerName, ApproverUsername, ApproverName, ReviewerUsername, ReviewerName, AssignedToUsername, AssignedToName, PreparedByUsername, ApprovedByUsername, ReviewedByUsername, MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.manage_close_task_facts` | TaskPreparer, TaskPreparedByUsername, TaskLastApprovedByUsername, TaskAddedByUsername, MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.manage_close_task_settings` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.review_controls` | Owner, MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.review_controls_access_by_area` | MDP_CREATED_BY, MDP_MODIFIED_BY |
| `silver.review_controls_user_access_report` | User, MDP_CREATED_BY, MDP_MODIFIED_BY |

## 7. Duplicate tables

| Table | Exact duplicate rows (export) | Rows | Note |
|---|---|---|---|
| `gold.mc_investment_portfolio` | 81 | 92 |  |
| `gold.mc_liquidity` | 41 | 45 |  |
| `gold.vw_ledger_journal_trans_bi_entities` | 5 | 9 |  |
| `silver.adra_tasks_task_settings_dimension` | 2 | 228 |  |
| `silver.dim_fixed_asset_books` | 0 | 300 | reviewed page says duplicates but the export shows none: still true? |
| `silver.dim_fixed_assets` | 0 | 301 | reviewed page says duplicates but the export shows none: still true? |
| `silver.fact_asset_master_transactions` | 0 | 2003 | reviewed page says duplicates but the export shows none: still true? |
| `silver.fact_ledger_journal_table_bi_entities` | 92 | 459 |  |
| `silver.fact_trail_balance_extractions` | 104 | 1847 |  |
| `silver.fact_vendor_invoice_journal_lines` | 158 | 285 |  |
| `silver.fact_vendor_payment_journal_lines` | 50 | 146 |  |

## 8. Values altered by Excel (not written to pages)

The workbook went through Excel, which turned text such as 'Feb 25' into dates. These columns had such values;
they were left out of Values, Profile and Sample rows. Re-export without opening the file in Excel (or import the
CSV as text) to get them back. Agents always check live values with get_column_values.

- `gold.fa_monthly_depreciation_trend`: TRANSACTION_YEAR_MONTH
- `gold.manage_close_adra_reconciliation`: PERIOD_NAME
- `gold.manage_close_adra_unreconciled_accounts`: PERIOD_NAME
- `gold.vw_commissions_analysis`: PERIOD_LABEL
- `gold.vw_expense_analysis`: POSTING_YEAR_MONTH
- `gold.vw_expense_analysis_gl`: YEAR_MONTH
- `gold.vw_income_statement`: FISCAL_YEAR_MONTH
- `gold.vw_investment_analytics`: POSTING_YEAR_MONTH
- `gold.vw_manage_close_task`: PERIOD_NAME
- `gold.vw_slr_gl_reconciliation`: posting_period
- `silver.adra_period_dimensions`: PERIOD_NAME
- `silver.adra_tasks_task_period_dimension`: PERIOD_NAME

## 9. Columns on pages that are not in the export


## 10. Proposed joins (joins_proposed.yaml)

| Id | From | To | Keys | Cardinality | Source |
|---|---|---|---|---|---|
| access_screen_dim_role__access_screen_dim_application__application_id | `silver.access_screen_dim_role` | `silver.access_screen_dim_application` | application_id=application_id | many_to_one | declared foreign key |
| access_screen_fact_certification_line__access_screen_fact_certification__certification_id | `silver.access_screen_fact_certification_line` | `silver.access_screen_fact_certification` | certification_id=certification_id | many_to_one | declared foreign key |
| access_screen_fact_certification_line__access_screen_fact_employee_access__access_id | `silver.access_screen_fact_certification_line` | `silver.access_screen_fact_employee_access` | access_id=access_id | many_to_one | declared foreign key |
| access_screen_fact_employee_access__access_screen_dim_employee__employee_email_effective_from | `silver.access_screen_fact_employee_access` | `silver.access_screen_dim_employee` | employee_email=employee_email, effective_from=effective_from | many_to_one | key-name match: holds the full key of silver.access_screen_dim_employee |
| access_screen_fact_employee_access__access_screen_dim_legal_entity__legal_entity_id | `silver.access_screen_fact_employee_access` | `silver.access_screen_dim_legal_entity` | legal_entity_id=legal_entity_id | many_to_one | declared foreign key |
| access_screen_fact_employee_access__access_screen_dim_role__role_id | `silver.access_screen_fact_employee_access` | `silver.access_screen_dim_role` | role_id=role_id | many_to_one | declared foreign key |
| access_screen_fact_employee_access__dim_legal_entities__legal_entity_id | `silver.access_screen_fact_employee_access` | `silver.dim_legal_entities` | legal_entity_id=legal_entity_id | many_to_one | key-name match: holds the full key of silver.dim_legal_entities |
| adra_account_dimensions__adra_engagement_dimensions__engagement_key | `silver.adra_account_dimensions` | `silver.adra_engagement_dimensions` | ENGAGEMENT_KEY=Engagement_Key | many_to_one | key-name match: holds the full key of silver.adra_engagement_dimensions |
| adra_account_dimensions__adra_legal_entity_dimensions__legal_entity_key_engagement_key | `silver.adra_account_dimensions` | `silver.adra_legal_entity_dimensions` | LEGAL_ENTITY_KEY=LEGAL_ENTITY_KEY, ENGAGEMENT_KEY=ENGAGEMENT_KEY | many_to_one | key-name match: holds the full key of silver.adra_legal_entity_dimensions |
| adra_account_facts__adra_engagement_dimensions__engagement_key | `silver.adra_account_facts` | `silver.adra_engagement_dimensions` | ENGAGEMENT_KEY=Engagement_Key | many_to_one | key-name match: holds the full key of silver.adra_engagement_dimensions |
| adra_account_facts__adra_tasks_task_period_dimension__period_key | `silver.adra_account_facts` | `silver.adra_tasks_task_period_dimension` | PERIOD_KEY=PERIOD_KEY | many_to_one | key-name match: holds the full key of silver.adra_tasks_task_period_dimension |
| adra_period_dimensions__adra_engagement_dimensions__engagement_key | `silver.adra_period_dimensions` | `silver.adra_engagement_dimensions` | ENGAGEMENT_KEY=Engagement_Key | many_to_one | key-name match: holds the full key of silver.adra_engagement_dimensions |
| adra_period_dimensions__adra_legal_entity_dimensions__legal_entity_key_engagement_key | `silver.adra_period_dimensions` | `silver.adra_legal_entity_dimensions` | LEGAL_ENTITY_KEY=LEGAL_ENTITY_KEY, ENGAGEMENT_KEY=ENGAGEMENT_KEY | many_to_one | key-name match: holds the full key of silver.adra_legal_entity_dimensions |
| adra_period_dimensions__adra_tasks_task_period_dimension__period_key | `silver.adra_period_dimensions` | `silver.adra_tasks_task_period_dimension` | PERIOD_KEY=PERIOD_KEY | many_to_one | key-name match: holds the full key of silver.adra_tasks_task_period_dimension |
| adra_tasks_company_dimension__adra_engagement_dimensions__engagement_key | `silver.adra_tasks_company_dimension` | `silver.adra_engagement_dimensions` | ENGAGEMENT_KEY=Engagement_Key | many_to_one | key-name match: holds the full key of silver.adra_engagement_dimensions |
| adra_tasks_task_facts__adra_engagement_dimensions__engagement_key | `silver.adra_tasks_task_facts` | `silver.adra_engagement_dimensions` | ENGAGEMENT_KEY=Engagement_Key | many_to_one | key-name match: holds the full key of silver.adra_engagement_dimensions |
| adra_tasks_task_facts__adra_tasks_company_dimension__company_key | `silver.adra_tasks_task_facts` | `silver.adra_tasks_company_dimension` | COMPANY_KEY=COMPANY_KEY | many_to_one | key-name match: holds the full key of silver.adra_tasks_company_dimension |
| adra_tasks_task_facts__adra_tasks_task_list_dimension__task_list_key | `silver.adra_tasks_task_facts` | `silver.adra_tasks_task_list_dimension` | TASK_LIST_KEY=TASK_LIST_KEY | many_to_one | key-name match: holds the full key of silver.adra_tasks_task_list_dimension |
| adra_tasks_task_list_dimension__adra_engagement_dimensions__engagement_key | `silver.adra_tasks_task_list_dimension` | `silver.adra_engagement_dimensions` | ENGAGEMENT_KEY=Engagement_Key | many_to_one | key-name match: holds the full key of silver.adra_engagement_dimensions |
| adra_tasks_task_list_dimension__adra_tasks_task_period_dimension__period_key | `silver.adra_tasks_task_list_dimension` | `silver.adra_tasks_task_period_dimension` | PERIOD_KEY=PERIOD_KEY | many_to_one | key-name match: holds the full key of silver.adra_tasks_task_period_dimension |
| adra_tasks_task_period_dimension__adra_engagement_dimensions__engagement_key | `silver.adra_tasks_task_period_dimension` | `silver.adra_engagement_dimensions` | ENGAGEMENT_KEY=Engagement_Key | many_to_one | key-name match: holds the full key of silver.adra_engagement_dimensions |
| adra_tasks_task_settings_dimension__adra_engagement_dimensions__engagement_key | `silver.adra_tasks_task_settings_dimension` | `silver.adra_engagement_dimensions` | ENGAGEMENT_KEY=Engagement_Key | many_to_one | key-name match: holds the full key of silver.adra_engagement_dimensions |
| adra_transaction_facts__adra_engagement_dimensions__engagement_key | `silver.adra_transaction_facts` | `silver.adra_engagement_dimensions` | ENGAGEMENT_KEY=Engagement_Key | many_to_one | key-name match: holds the full key of silver.adra_engagement_dimensions |
| adra_transaction_facts__adra_tasks_task_period_dimension__period_key | `silver.adra_transaction_facts` | `silver.adra_tasks_task_period_dimension` | PERIOD_KEY=PERIOD_KEY | many_to_one | key-name match: holds the full key of silver.adra_tasks_task_period_dimension |
| audit_soc_report__manage_bus_report_lists__report | `silver.audit_soc_report` | `gold.manage_bus_report_lists` | Report=REPORT | many_to_one | key-name match: holds the full key of gold.manage_bus_report_lists |
| audit_soc_report__vw_audit_soc_report__period_covered_issued | `silver.audit_soc_report` | `gold.vw_audit_soc_report` | Period_covered=Period_covered, Issued=Issued | many_to_one | key-name match: holds the full key of gold.vw_audit_soc_report |
| capitalization_workbench__depreciation_workbench__journal_id_asset_id | `gold.capitalization_workbench` | `gold.depreciation_workbench` | JOURNAL_ID=JOURNAL_ID, ASSET_ID=ASSET_ID | many_to_one | key-name match: holds the full key of gold.depreciation_workbench |
| capitalization_workbench__vw_kpi_pipeline_success__legal_entity | `gold.capitalization_workbench` | `gold.vw_kpi_pipeline_success` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_kpi_pipeline_success |
| capitalization_workbench__vw_legal_entities__legal_entity | `gold.capitalization_workbench` | `gold.vw_legal_entities` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_legal_entities |
| depreciation_workbench__capitalization_workbench__asset_id | `gold.depreciation_workbench` | `gold.capitalization_workbench` | ASSET_ID=ASSET_ID | many_to_one | key-name match: holds the full key of gold.capitalization_workbench |
| depreciation_workbench__disposal_workbench__asset_id | `gold.depreciation_workbench` | `gold.disposal_workbench` | ASSET_ID=ASSET_ID | many_to_one | key-name match: holds the full key of gold.disposal_workbench |
| depreciation_workbench__fa_asset_register__asset_id | `gold.depreciation_workbench` | `gold.fa_asset_register` | ASSET_ID=ASSET_ID | many_to_one | key-name match: holds the full key of gold.fa_asset_register |
| depreciation_workbench__vw_kpi_pipeline_success__legal_entity | `gold.depreciation_workbench` | `gold.vw_kpi_pipeline_success` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_kpi_pipeline_success |
| depreciation_workbench__vw_legal_entities__legal_entity | `gold.depreciation_workbench` | `gold.vw_legal_entities` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_legal_entities |
| dim_bank_account_table_bi_entities__dim_ledger_bi_entities__source_key | `silver.dim_bank_account_table_bi_entities` | `silver.dim_ledger_bi_entities` | SOURCE_KEY=source_key | many_to_one | key-name match: holds the full key of silver.dim_ledger_bi_entities |
| dim_bank_account_table_bi_entities__fact_cust_table_bi_entities__data_area_id | `silver.dim_bank_account_table_bi_entities` | `silver.fact_cust_table_bi_entities` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_table_bi_entities |
| dim_bank_account_table_bi_entities__fact_cust_trans_opens__data_area_id | `silver.dim_bank_account_table_bi_entities` | `silver.fact_cust_trans_opens` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_trans_opens |
| dim_bank_account_table_bi_entities__fact_ledger_journal_trans_bi_entities__source_key | `silver.dim_bank_account_table_bi_entities` | `silver.fact_ledger_journal_trans_bi_entities` | SOURCE_KEY=SOURCE_KEY | many_to_one | key-name match: holds the full key of silver.fact_ledger_journal_trans_bi_entities |
| dim_bank_account_table_bi_entities__fact_vend_invoice_jour_bi_entities__source_key | `silver.dim_bank_account_table_bi_entities` | `silver.fact_vend_invoice_jour_bi_entities` | SOURCE_KEY=SOURCE_KEY | many_to_one | key-name match: holds the full key of silver.fact_vend_invoice_jour_bi_entities |
| dim_fixed_asset_books__fa_capitalized_value_trend__fixed_asset_number | `silver.dim_fixed_asset_books` | `gold.fa_capitalized_value_trend` | FIXED_ASSET_NUMBER=FIXED_ASSET_NUMBER | many_to_one | key-name match: holds the full key of gold.fa_capitalized_value_trend |
| dim_fixed_asset_books__fact_cust_table_bi_entities__data_area_id | `silver.dim_fixed_asset_books` | `silver.fact_cust_table_bi_entities` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_table_bi_entities |
| dim_fixed_asset_books__fact_cust_trans_opens__data_area_id | `silver.dim_fixed_asset_books` | `silver.fact_cust_trans_opens` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_trans_opens |
| dim_fixed_assets__fa_capitalized_value_trend__fixed_asset_number | `silver.dim_fixed_assets` | `gold.fa_capitalized_value_trend` | FIXED_ASSET_NUMBER=FIXED_ASSET_NUMBER | many_to_one | key-name match: holds the full key of gold.fa_capitalized_value_trend |
| dim_fixed_assets__fact_cust_table_bi_entities__data_area_id | `silver.dim_fixed_assets` | `silver.fact_cust_table_bi_entities` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_table_bi_entities |
| dim_fixed_assets__fact_cust_trans_opens__data_area_id | `silver.dim_fixed_assets` | `silver.fact_cust_trans_opens` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_trans_opens |
| dim_ledger_fiscal_periods_v2__access_screen_dim_legal_entity__legal_entity_id | `silver.dim_ledger_fiscal_periods_v2` | `silver.access_screen_dim_legal_entity` | LEGAL_ENTITY_ID=legal_entity_id | many_to_one | key-name match: holds the full key of silver.access_screen_dim_legal_entity |
| dim_ledger_fiscal_periods_v2__dim_legal_entities__legal_entity_id | `silver.dim_ledger_fiscal_periods_v2` | `silver.dim_legal_entities` | LEGAL_ENTITY_ID=legal_entity_id | many_to_one | key-name match: holds the full key of silver.dim_legal_entities |
| dim_legal_entities__access_screen_dim_legal_entity__legal_entity_id | `silver.dim_legal_entities` | `silver.access_screen_dim_legal_entity` | legal_entity_id=legal_entity_id | one_to_one | key-name match: same primary key |
| disposal_workbench__capitalization_workbench__asset_id | `gold.disposal_workbench` | `gold.capitalization_workbench` | ASSET_ID=ASSET_ID | one_to_one | key-name match: same primary key |
| disposal_workbench__depreciation_workbench__journal_id_asset_id | `gold.disposal_workbench` | `gold.depreciation_workbench` | JOURNAL_ID=JOURNAL_ID, ASSET_ID=ASSET_ID | many_to_one | key-name match: holds the full key of gold.depreciation_workbench |
| disposal_workbench__vw_kpi_pipeline_success__legal_entity | `gold.disposal_workbench` | `gold.vw_kpi_pipeline_success` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_kpi_pipeline_success |
| disposal_workbench__vw_legal_entities__legal_entity | `gold.disposal_workbench` | `gold.vw_legal_entities` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_legal_entities |
| fa_asset_register__capitalization_workbench__asset_id | `gold.fa_asset_register` | `gold.capitalization_workbench` | ASSET_ID=ASSET_ID | one_to_one | key-name match: same primary key |
| fa_asset_register__disposal_workbench__asset_id | `gold.fa_asset_register` | `gold.disposal_workbench` | ASSET_ID=ASSET_ID | one_to_one | key-name match: same primary key |
| fa_asset_register__vw_kpi_pipeline_success__legal_entity | `gold.fa_asset_register` | `gold.vw_kpi_pipeline_success` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_kpi_pipeline_success |
| fa_asset_register__vw_legal_entities__legal_entity | `gold.fa_asset_register` | `gold.vw_legal_entities` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_legal_entities |
| fa_capitalized_value_trend__vw_kpi_pipeline_success__legal_entity | `gold.fa_capitalized_value_trend` | `gold.vw_kpi_pipeline_success` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_kpi_pipeline_success |
| fa_capitalized_value_trend__vw_legal_entities__legal_entity | `gold.fa_capitalized_value_trend` | `gold.vw_legal_entities` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_legal_entities |
| fa_disposal_trends__vw_kpi_pipeline_success__legal_entity | `gold.fa_disposal_trends` | `gold.vw_kpi_pipeline_success` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_kpi_pipeline_success |
| fa_disposal_trends__vw_legal_entities__legal_entity | `gold.fa_disposal_trends` | `gold.vw_legal_entities` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_legal_entities |
| fa_kpi__managed_coll_kpi__section_kpi_legal_entity | `gold.fa_kpi` | `gold.managed_coll_kpi` | SECTION=Section, KPI=KPI, LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.managed_coll_kpi |
| fa_kpi__mc_kpi__section_kpi_legal_entity | `gold.fa_kpi` | `gold.mc_kpi` | SECTION=SECTION, KPI=KPI, LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.mc_kpi |
| fa_kpi__vw_kpi_pipeline_success__legal_entity | `gold.fa_kpi` | `gold.vw_kpi_pipeline_success` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_kpi_pipeline_success |
| fa_kpi__vw_kpi_system_and_data_status__kpi | `gold.fa_kpi` | `gold.vw_kpi_system_and_data_status` | KPI=KPI | many_to_one | key-name match: holds the full key of gold.vw_kpi_system_and_data_status |
| fa_kpi__vw_legal_entities__legal_entity | `gold.fa_kpi` | `gold.vw_legal_entities` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_legal_entities |
| fa_kpi__vw_manage_close_journal_entry_kpi__kpi_legal_entity | `gold.fa_kpi` | `gold.vw_manage_close_journal_entry_kpi` | KPI=KPI, LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_manage_close_journal_entry_kpi |
| fa_monthly_depreciation_trend__vw_kpi_pipeline_success__legal_entity | `gold.fa_monthly_depreciation_trend` | `gold.vw_kpi_pipeline_success` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_kpi_pipeline_success |
| fa_monthly_depreciation_trend__vw_legal_entities__legal_entity | `gold.fa_monthly_depreciation_trend` | `gold.vw_legal_entities` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_legal_entities |
| fact_ap_invoices__vw_kpi_pipeline_success__legal_entity | `gold.fact_ap_invoices` | `gold.vw_kpi_pipeline_success` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_kpi_pipeline_success |
| fact_ap_invoices__vw_legal_entities__legal_entity | `gold.fact_ap_invoices` | `gold.vw_legal_entities` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_legal_entities |
| fact_asset_journal__fact_cust_table_bi_entities__data_area_id | `silver.fact_asset_journal` | `silver.fact_cust_table_bi_entities` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_table_bi_entities |
| fact_asset_journal__fact_cust_trans_opens__data_area_id | `silver.fact_asset_journal` | `silver.fact_cust_trans_opens` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_trans_opens |
| fact_asset_master_transactions__capitalization_workbench__asset_id | `silver.fact_asset_master_transactions` | `gold.capitalization_workbench` | ASSET_ID=ASSET_ID | many_to_one | key-name match: holds the full key of gold.capitalization_workbench |
| fact_asset_master_transactions__disposal_workbench__asset_id | `silver.fact_asset_master_transactions` | `gold.disposal_workbench` | ASSET_ID=ASSET_ID | many_to_one | key-name match: holds the full key of gold.disposal_workbench |
| fact_asset_master_transactions__fa_asset_register__asset_id | `silver.fact_asset_master_transactions` | `gold.fa_asset_register` | ASSET_ID=ASSET_ID | many_to_one | key-name match: holds the full key of gold.fa_asset_register |
| fact_cash_discounts__fact_cust_table_bi_entities__data_area_id | `silver.fact_cash_discounts` | `silver.fact_cust_table_bi_entities` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_table_bi_entities |
| fact_cash_discounts__fact_cust_trans_opens__data_area_id | `silver.fact_cash_discounts` | `silver.fact_cust_trans_opens` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_trans_opens |
| fact_cust_table_bi_entities__dim_ledger_bi_entities__source_key | `silver.fact_cust_table_bi_entities` | `silver.dim_ledger_bi_entities` | SOURCE_KEY=source_key | many_to_one | key-name match: holds the full key of silver.dim_ledger_bi_entities |
| fact_cust_table_bi_entities__fact_ledger_journal_trans_bi_entities__source_key | `silver.fact_cust_table_bi_entities` | `silver.fact_ledger_journal_trans_bi_entities` | SOURCE_KEY=SOURCE_KEY | many_to_one | key-name match: holds the full key of silver.fact_ledger_journal_trans_bi_entities |
| fact_cust_table_bi_entities__fact_vend_invoice_jour_bi_entities__source_key | `silver.fact_cust_table_bi_entities` | `silver.fact_vend_invoice_jour_bi_entities` | SOURCE_KEY=SOURCE_KEY | many_to_one | key-name match: holds the full key of silver.fact_vend_invoice_jour_bi_entities |
| fact_cust_trans_opens__fact_cust_table_bi_entities__data_area_id | `silver.fact_cust_trans_opens` | `silver.fact_cust_table_bi_entities` | DATA_AREA_ID=DATA_AREA_ID | one_to_one | key-name match: same primary key |
| fact_cust_trans_opens__fact_kpmg_vend_payment_bi_vend_trans_open__ref_rec_id | `silver.fact_cust_trans_opens` | `silver.fact_kpmg_vend_payment_bi_vend_trans_open` | REF_REC_ID=REF_REC_ID | many_to_one | key-name match: holds the full key of silver.fact_kpmg_vend_payment_bi_vend_trans_open |
| fact_fynapse_slr_journals__managed_coll_due_soon_accounts__invoice_number | `silver.fact_fynapse_slr_journals` | `gold.managed_coll_due_soon_accounts` | INVOICE_NUMBER=invoice_number | many_to_one | key-name match: holds the full key of gold.managed_coll_due_soon_accounts |
| fact_fynapse_slr_journals__managed_coll_early_payment_discounts__invoice_number | `silver.fact_fynapse_slr_journals` | `gold.managed_coll_early_payment_discounts` | INVOICE_NUMBER=invoice_number | many_to_one | key-name match: holds the full key of gold.managed_coll_early_payment_discounts |
| fact_fynapse_slr_journals__managed_coll_overdue__invoice_number | `silver.fact_fynapse_slr_journals` | `gold.managed_coll_overdue` | INVOICE_NUMBER=INVOICE_NUMBER | many_to_one | key-name match: holds the full key of gold.managed_coll_overdue |
| fact_fynapse_slr_journals__vw_fact_fynapse_slr_journals__journal_line_id | `silver.fact_fynapse_slr_journals` | `gold.vw_fact_fynapse_slr_journals` | JOURNAL_LINE_ID=JOURNAL_LINE_ID | one_to_one | key-name match: same primary key |
| fact_kpmg_general_journal_account_entries__fact_cust_table_bi_entities__data_area_id | `silver.fact_kpmg_general_journal_account_entries` | `silver.fact_cust_table_bi_entities` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_table_bi_entities |
| fact_kpmg_general_journal_account_entries__fact_cust_trans_opens__data_area_id | `silver.fact_kpmg_general_journal_account_entries` | `silver.fact_cust_trans_opens` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_trans_opens |
| fact_kpmg_general_journal_account_entries__vw_fact_kpmg_general_journals_entries__general_journal_account_entry_rec_id | `silver.fact_kpmg_general_journal_account_entries` | `gold.vw_fact_kpmg_general_journals_entries` | GENERAL_JOURNAL_ACCOUNT_ENTRY_REC_ID=GENERAL_JOURNAL_ACCOUNT_ENTRY_REC_ID | one_to_one | key-name match: same primary key |
| fact_kpmg_vend_payment_bi_vend_trans_open__fact_cust_table_bi_entities__data_area_id | `silver.fact_kpmg_vend_payment_bi_vend_trans_open` | `silver.fact_cust_table_bi_entities` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_table_bi_entities |
| fact_kpmg_vend_payment_bi_vend_trans_open__fact_cust_trans_opens__data_area_id | `silver.fact_kpmg_vend_payment_bi_vend_trans_open` | `silver.fact_cust_trans_opens` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_trans_opens |
| fact_ledger_journal_headers__fact_cust_table_bi_entities__data_area_id | `silver.fact_ledger_journal_headers` | `silver.fact_cust_table_bi_entities` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_table_bi_entities |
| fact_ledger_journal_headers__fact_cust_trans_opens__data_area_id | `silver.fact_ledger_journal_headers` | `silver.fact_cust_trans_opens` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_trans_opens |
| fact_ledger_journal_lines__fact_cust_table_bi_entities__data_area_id | `silver.fact_ledger_journal_lines` | `silver.fact_cust_table_bi_entities` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_table_bi_entities |
| fact_ledger_journal_lines__fact_cust_trans_opens__data_area_id | `silver.fact_ledger_journal_lines` | `silver.fact_cust_trans_opens` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_trans_opens |
| fact_ledger_journal_table_bi_entities__dim_ledger_bi_entities__source_key | `silver.fact_ledger_journal_table_bi_entities` | `silver.dim_ledger_bi_entities` | SOURCE_KEY=source_key | many_to_one | key-name match: holds the full key of silver.dim_ledger_bi_entities |
| fact_ledger_journal_table_bi_entities__fact_cust_table_bi_entities__data_area_id | `silver.fact_ledger_journal_table_bi_entities` | `silver.fact_cust_table_bi_entities` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_table_bi_entities |
| fact_ledger_journal_table_bi_entities__fact_cust_trans_opens__data_area_id | `silver.fact_ledger_journal_table_bi_entities` | `silver.fact_cust_trans_opens` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_trans_opens |
| fact_ledger_journal_table_bi_entities__fact_ledger_journal_trans_bi_entities__source_key | `silver.fact_ledger_journal_table_bi_entities` | `silver.fact_ledger_journal_trans_bi_entities` | SOURCE_KEY=SOURCE_KEY | many_to_one | key-name match: holds the full key of silver.fact_ledger_journal_trans_bi_entities |
| fact_ledger_journal_table_bi_entities__fact_vend_invoice_jour_bi_entities__source_key | `silver.fact_ledger_journal_table_bi_entities` | `silver.fact_vend_invoice_jour_bi_entities` | SOURCE_KEY=SOURCE_KEY | many_to_one | key-name match: holds the full key of silver.fact_vend_invoice_jour_bi_entities |
| fact_ledger_journal_trans_bi_entities__dim_ledger_bi_entities__source_key | `silver.fact_ledger_journal_trans_bi_entities` | `silver.dim_ledger_bi_entities` | SOURCE_KEY=source_key | one_to_one | key-name match: same primary key |
| fact_ledger_journal_trans_bi_entities__fact_cust_table_bi_entities__data_area_id | `silver.fact_ledger_journal_trans_bi_entities` | `silver.fact_cust_table_bi_entities` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_table_bi_entities |
| fact_ledger_journal_trans_bi_entities__fact_cust_trans_opens__data_area_id | `silver.fact_ledger_journal_trans_bi_entities` | `silver.fact_cust_trans_opens` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_trans_opens |
| fact_purchase_order_headers__fact_cust_table_bi_entities__data_area_id | `silver.fact_purchase_order_headers` | `silver.fact_cust_table_bi_entities` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_table_bi_entities |
| fact_purchase_order_headers__fact_cust_trans_opens__data_area_id | `silver.fact_purchase_order_headers` | `silver.fact_cust_trans_opens` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_trans_opens |
| fact_purchase_order_lines__dim_fixed_assets__data_area_id_fixed_asset_number | `silver.fact_purchase_order_lines` | `silver.dim_fixed_assets` | DATA_AREA_ID=DATA_AREA_ID, FIXED_ASSET_NUMBER=FIXED_ASSET_NUMBER | many_to_one | key-name match: holds the full key of silver.dim_fixed_assets |
| fact_purchase_order_lines__fa_capitalized_value_trend__fixed_asset_number | `silver.fact_purchase_order_lines` | `gold.fa_capitalized_value_trend` | FIXED_ASSET_NUMBER=FIXED_ASSET_NUMBER | many_to_one | key-name match: holds the full key of gold.fa_capitalized_value_trend |
| fact_purchase_order_lines__fact_cust_table_bi_entities__data_area_id | `silver.fact_purchase_order_lines` | `silver.fact_cust_table_bi_entities` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_table_bi_entities |
| fact_purchase_order_lines__fact_cust_trans_opens__data_area_id | `silver.fact_purchase_order_lines` | `silver.fact_cust_trans_opens` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_trans_opens |
| fact_trail_balance_extractions__vw_kpi_pipeline_success__legal_entity | `gold.fact_trail_balance_extractions` | `gold.vw_kpi_pipeline_success` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_kpi_pipeline_success |
| fact_trail_balance_extractions__vw_legal_entities__legal_entity | `gold.fact_trail_balance_extractions` | `gold.vw_legal_entities` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_legal_entities |
| fact_vend_invoice_jour_bi_entities__dim_ledger_bi_entities__source_key | `silver.fact_vend_invoice_jour_bi_entities` | `silver.dim_ledger_bi_entities` | SOURCE_KEY=source_key | one_to_one | key-name match: same primary key |
| fact_vend_invoice_jour_bi_entities__fact_ledger_journal_trans_bi_entities__source_key | `silver.fact_vend_invoice_jour_bi_entities` | `silver.fact_ledger_journal_trans_bi_entities` | SOURCE_KEY=SOURCE_KEY | one_to_one | key-name match: same primary key |
| fact_vendor_invoice_headers__managed_coll_due_soon_accounts__invoice_number | `silver.fact_vendor_invoice_headers` | `gold.managed_coll_due_soon_accounts` | INVOICE_NUMBER=invoice_number | many_to_one | key-name match: holds the full key of gold.managed_coll_due_soon_accounts |
| fact_vendor_invoice_headers__managed_coll_early_payment_discounts__invoice_number | `silver.fact_vendor_invoice_headers` | `gold.managed_coll_early_payment_discounts` | INVOICE_NUMBER=invoice_number | many_to_one | key-name match: holds the full key of gold.managed_coll_early_payment_discounts |
| fact_vendor_invoice_headers__managed_coll_overdue__invoice_number | `silver.fact_vendor_invoice_headers` | `gold.managed_coll_overdue` | INVOICE_NUMBER=INVOICE_NUMBER | many_to_one | key-name match: holds the full key of gold.managed_coll_overdue |
| fact_vendor_invoice_journal_lines__capitalization_workbench__asset_id | `silver.fact_vendor_invoice_journal_lines` | `gold.capitalization_workbench` | ASSET_ID=ASSET_ID | many_to_one | key-name match: holds the full key of gold.capitalization_workbench |
| fact_vendor_invoice_journal_lines__disposal_workbench__asset_id | `silver.fact_vendor_invoice_journal_lines` | `gold.disposal_workbench` | ASSET_ID=ASSET_ID | many_to_one | key-name match: holds the full key of gold.disposal_workbench |
| fact_vendor_invoice_journal_lines__fa_asset_register__asset_id | `silver.fact_vendor_invoice_journal_lines` | `gold.fa_asset_register` | ASSET_ID=ASSET_ID | many_to_one | key-name match: holds the full key of gold.fa_asset_register |
| fact_vendor_invoice_journal_lines__fact_trail_balance_extractions__company_description | `silver.fact_vendor_invoice_journal_lines` | `gold.fact_trail_balance_extractions` | COMPANY=COMPANY, DESCRIPTION=DESCRIPTION | many_to_one | key-name match: holds the full key of gold.fact_trail_balance_extractions |
| manage_bus_kpi__fa_kpi__section_kpi | `gold.manage_bus_kpi` | `gold.fa_kpi` | SECTION=SECTION, KPI=KPI | many_to_one | key-name match: holds the full key of gold.fa_kpi |
| manage_bus_kpi__managed_coll_kpi__section_kpi_legal_entity | `gold.manage_bus_kpi` | `gold.managed_coll_kpi` | SECTION=Section, KPI=KPI, LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.managed_coll_kpi |
| manage_bus_kpi__mc_kpi__section_kpi_legal_entity | `gold.manage_bus_kpi` | `gold.mc_kpi` | SECTION=SECTION, KPI=KPI, LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.mc_kpi |
| manage_bus_kpi__mc_kpi_new__section_kpi | `gold.manage_bus_kpi` | `gold.mc_kpi_new` | SECTION=SECTION, KPI=KPI | many_to_one | key-name match: holds the full key of gold.mc_kpi_new |
| manage_bus_kpi__vw_kpi_pipeline_success__legal_entity | `gold.manage_bus_kpi` | `gold.vw_kpi_pipeline_success` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_kpi_pipeline_success |
| manage_bus_kpi__vw_kpi_system_and_data_status__kpi | `gold.manage_bus_kpi` | `gold.vw_kpi_system_and_data_status` | KPI=KPI | many_to_one | key-name match: holds the full key of gold.vw_kpi_system_and_data_status |
| manage_bus_kpi__vw_legal_entities__legal_entity | `gold.manage_bus_kpi` | `gold.vw_legal_entities` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_legal_entities |
| manage_bus_kpi__vw_manage_close_journal_entry_kpi__kpi_legal_entity | `gold.manage_bus_kpi` | `gold.vw_manage_close_journal_entry_kpi` | KPI=KPI, LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_manage_close_journal_entry_kpi |
| manage_bus_report_lists__vw_kpi_pipeline_success__legal_entity | `gold.manage_bus_report_lists` | `gold.vw_kpi_pipeline_success` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_kpi_pipeline_success |
| manage_bus_report_lists__vw_legal_entities__legal_entity | `gold.manage_bus_report_lists` | `gold.vw_legal_entities` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_legal_entities |
| manage_close_journal_entries__vw_kpi_pipeline_success__legal_entity | `gold.manage_close_journal_entries` | `gold.vw_kpi_pipeline_success` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_kpi_pipeline_success |
| manage_close_journal_entries__vw_legal_entities__legal_entity | `gold.manage_close_journal_entries` | `gold.vw_legal_entities` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_legal_entities |
| managed_coll_due_soon_accounts__vw_kpi_pipeline_success__legal_entity | `gold.managed_coll_due_soon_accounts` | `gold.vw_kpi_pipeline_success` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_kpi_pipeline_success |
| managed_coll_due_soon_accounts__vw_legal_entities__legal_entity | `gold.managed_coll_due_soon_accounts` | `gold.vw_legal_entities` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_legal_entities |
| managed_coll_early_payment_discounts__managed_coll_due_soon_accounts__invoice_number | `gold.managed_coll_early_payment_discounts` | `gold.managed_coll_due_soon_accounts` | invoice_number=invoice_number | one_to_one | key-name match: same primary key |
| managed_coll_early_payment_discounts__vw_kpi_pipeline_success__legal_entity | `gold.managed_coll_early_payment_discounts` | `gold.vw_kpi_pipeline_success` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_kpi_pipeline_success |
| managed_coll_early_payment_discounts__vw_legal_entities__legal_entity | `gold.managed_coll_early_payment_discounts` | `gold.vw_legal_entities` | LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_legal_entities |
| managed_coll_kpi__fa_kpi__section_kpi | `gold.managed_coll_kpi` | `gold.fa_kpi` | Section=SECTION, KPI=KPI | many_to_one | key-name match: holds the full key of gold.fa_kpi |
| managed_coll_kpi__mc_kpi_new__section_kpi | `gold.managed_coll_kpi` | `gold.mc_kpi_new` | Section=SECTION, KPI=KPI | many_to_one | key-name match: holds the full key of gold.mc_kpi_new |
| managed_coll_kpi__vw_kpi_system_and_data_status__kpi | `gold.managed_coll_kpi` | `gold.vw_kpi_system_and_data_status` | KPI=KPI | many_to_one | key-name match: holds the full key of gold.vw_kpi_system_and_data_status |
| managed_coll_kpi__vw_manage_close_journal_entry_kpi__kpi_legal_entity | `gold.managed_coll_kpi` | `gold.vw_manage_close_journal_entry_kpi` | KPI=KPI, LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_manage_close_journal_entry_kpi |
| managed_coll_overdue__managed_coll_due_soon_accounts__invoice_number | `gold.managed_coll_overdue` | `gold.managed_coll_due_soon_accounts` | INVOICE_NUMBER=invoice_number | one_to_one | key-name match: same primary key |
| managed_coll_overdue__managed_coll_early_payment_discounts__invoice_number | `gold.managed_coll_overdue` | `gold.managed_coll_early_payment_discounts` | INVOICE_NUMBER=invoice_number | one_to_one | key-name match: same primary key |
| mc_kpi__fa_kpi__section_kpi | `gold.mc_kpi` | `gold.fa_kpi` | SECTION=SECTION, KPI=KPI | many_to_one | key-name match: holds the full key of gold.fa_kpi |
| mc_kpi__managed_coll_kpi__section_kpi_legal_entity | `gold.mc_kpi` | `gold.managed_coll_kpi` | SECTION=Section, KPI=KPI, LEGAL_ENTITY=LEGAL_ENTITY | one_to_one | key-name match: same primary key |
| mc_kpi__mc_kpi_new__section_kpi | `gold.mc_kpi` | `gold.mc_kpi_new` | SECTION=SECTION, KPI=KPI | many_to_one | key-name match: holds the full key of gold.mc_kpi_new |
| mc_kpi__vw_kpi_system_and_data_status__kpi | `gold.mc_kpi` | `gold.vw_kpi_system_and_data_status` | KPI=KPI | many_to_one | key-name match: holds the full key of gold.vw_kpi_system_and_data_status |
| mc_kpi__vw_manage_close_journal_entry_kpi__kpi_legal_entity | `gold.mc_kpi` | `gold.vw_manage_close_journal_entry_kpi` | KPI=KPI, LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_manage_close_journal_entry_kpi |
| mc_kpi_new__fa_kpi__section_kpi | `gold.mc_kpi_new` | `gold.fa_kpi` | SECTION=SECTION, KPI=KPI | one_to_one | key-name match: same primary key |
| mc_kpi_new__managed_coll_kpi__section_kpi_legal_entity | `gold.mc_kpi_new` | `gold.managed_coll_kpi` | SECTION=Section, KPI=KPI, LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.managed_coll_kpi |
| mc_kpi_new__mc_kpi__section_kpi_legal_entity | `gold.mc_kpi_new` | `gold.mc_kpi` | SECTION=SECTION, KPI=KPI, LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.mc_kpi |
| mc_kpi_new__vw_kpi_system_and_data_status__kpi | `gold.mc_kpi_new` | `gold.vw_kpi_system_and_data_status` | KPI=KPI | many_to_one | key-name match: holds the full key of gold.vw_kpi_system_and_data_status |
| mc_kpi_new__vw_manage_close_journal_entry_kpi__kpi_legal_entity | `gold.mc_kpi_new` | `gold.vw_manage_close_journal_entry_kpi` | KPI=KPI, LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_manage_close_journal_entry_kpi |
| mc_liquidity__mc_investment_portfolio__company_main_account_id | `gold.mc_liquidity` | `gold.mc_investment_portfolio` | COMPANY=COMPANY, MAIN_ACCOUNT_ID=MAIN_ACCOUNT_ID | one_to_one | key-name match: same primary key |
| vw_audit_soc_report__manage_bus_report_lists__report | `gold.vw_audit_soc_report` | `gold.manage_bus_report_lists` | Report=REPORT | many_to_one | key-name match: holds the full key of gold.manage_bus_report_lists |
| vw_commissions_analysis__adra_tasks_task_period_dimension__period_key | `gold.vw_commissions_analysis` | `silver.adra_tasks_task_period_dimension` | PERIOD_KEY=PERIOD_KEY | many_to_one | key-name match: holds the full key of silver.adra_tasks_task_period_dimension |
| vw_fact_fynapse_slr_journals__managed_coll_due_soon_accounts__invoice_number | `gold.vw_fact_fynapse_slr_journals` | `gold.managed_coll_due_soon_accounts` | INVOICE_NUMBER=invoice_number | many_to_one | key-name match: holds the full key of gold.managed_coll_due_soon_accounts |
| vw_fact_fynapse_slr_journals__managed_coll_early_payment_discounts__invoice_number | `gold.vw_fact_fynapse_slr_journals` | `gold.managed_coll_early_payment_discounts` | INVOICE_NUMBER=invoice_number | many_to_one | key-name match: holds the full key of gold.managed_coll_early_payment_discounts |
| vw_fact_fynapse_slr_journals__managed_coll_overdue__invoice_number | `gold.vw_fact_fynapse_slr_journals` | `gold.managed_coll_overdue` | INVOICE_NUMBER=INVOICE_NUMBER | many_to_one | key-name match: holds the full key of gold.managed_coll_overdue |
| vw_fact_kpmg_general_journals_entries__fact_cust_table_bi_entities__data_area_id | `gold.vw_fact_kpmg_general_journals_entries` | `silver.fact_cust_table_bi_entities` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_table_bi_entities |
| vw_fact_kpmg_general_journals_entries__fact_cust_trans_opens__data_area_id | `gold.vw_fact_kpmg_general_journals_entries` | `silver.fact_cust_trans_opens` | DATA_AREA_ID=DATA_AREA_ID | many_to_one | key-name match: holds the full key of silver.fact_cust_trans_opens |
| vw_income_statement__vw_expense_analysis__entry_rec_id | `gold.vw_income_statement` | `gold.vw_expense_analysis` | ENTRY_REC_ID=ENTRY_REC_ID | one_to_one | key-name match: same primary key |
| vw_income_statement_logistics__vw_expense_analysis__entry_rec_id | `gold.vw_income_statement_logistics` | `gold.vw_expense_analysis` | ENTRY_REC_ID=ENTRY_REC_ID | one_to_one | key-name match: same primary key |
| vw_income_statement_logistics__vw_income_statement__entry_rec_id | `gold.vw_income_statement_logistics` | `gold.vw_income_statement` | ENTRY_REC_ID=ENTRY_REC_ID | one_to_one | key-name match: same primary key |
| vw_investment_analytics__vw_expense_analysis__entry_rec_id | `gold.vw_investment_analytics` | `gold.vw_expense_analysis` | ENTRY_REC_ID=ENTRY_REC_ID | one_to_one | key-name match: same primary key |
| vw_investment_analytics__vw_income_statement__entry_rec_id | `gold.vw_investment_analytics` | `gold.vw_income_statement` | ENTRY_REC_ID=ENTRY_REC_ID | one_to_one | key-name match: same primary key |
| vw_investment_analytics__vw_income_statement_logistics__entry_rec_id | `gold.vw_investment_analytics` | `gold.vw_income_statement_logistics` | ENTRY_REC_ID=ENTRY_REC_ID | one_to_one | key-name match: same primary key |
| vw_kpi_pipeline_success__vw_kpi_system_and_data_status__kpi | `gold.vw_kpi_pipeline_success` | `gold.vw_kpi_system_and_data_status` | KPI=KPI | many_to_one | key-name match: holds the full key of gold.vw_kpi_system_and_data_status |
| vw_kpi_pipeline_success__vw_manage_close_journal_entry_kpi__kpi_legal_entity | `gold.vw_kpi_pipeline_success` | `gold.vw_manage_close_journal_entry_kpi` | KPI=KPI, LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_manage_close_journal_entry_kpi |
| vw_kpi_system_and_data_status__vw_manage_close_journal_entry_kpi__kpi_legal_entity | `gold.vw_kpi_system_and_data_status` | `gold.vw_manage_close_journal_entry_kpi` | KPI=KPI, LEGAL_ENTITY=LEGAL_ENTITY | many_to_one | key-name match: holds the full key of gold.vw_manage_close_journal_entry_kpi |
| vw_manage_close_journal_entry_kpi__vw_kpi_system_and_data_status__kpi | `gold.vw_manage_close_journal_entry_kpi` | `gold.vw_kpi_system_and_data_status` | KPI=KPI | many_to_one | key-name match: holds the full key of gold.vw_kpi_system_and_data_status |

## 11. Lineage (built_from)

| Table | Built from | Source page exists |
|---|---|---|
| `gold.capitalization_workbench` | `silver.dim_fixed_assets` | yes |
| `gold.capitalization_workbench` | `silver.dim_fixed_asset_books` | yes |
| `gold.capitalization_workbench` | `silver.fact_asset_journal` | yes |
| `gold.capitalization_workbench` | `silver.fact_asset_master_transactions` | yes |
| `gold.depreciation_workbench` | `silver.dim_fixed_assets` | yes |
| `gold.depreciation_workbench` | `silver.dim_fixed_asset_books` | yes |
| `gold.depreciation_workbench` | `silver.fact_asset_journal` | yes |
| `gold.depreciation_workbench` | `silver.fact_asset_master_transactions` | yes |
| `gold.disposal_workbench` | `silver.dim_fixed_assets` | yes |
| `gold.disposal_workbench` | `silver.dim_fixed_asset_books` | yes |
| `gold.disposal_workbench` | `silver.fact_asset_journal` | yes |
| `gold.disposal_workbench` | `silver.fact_asset_master_transactions` | yes |
| `gold.fa_asset_register` | `silver.dim_fixed_assets` | yes |
| `gold.fa_asset_register` | `silver.dim_fixed_asset_books` | yes |
| `gold.fa_asset_register` | `silver.fact_asset_master_transactions` | yes |
| `gold.fa_capitalized_value_trend` | `silver.dim_fixed_asset_books` | yes |
| `gold.fa_capitalized_value_trend` | `silver.fact_asset_master_transactions` | yes |
| `gold.fa_disposal_trends` | `silver.fact_asset_journal` | yes |
| `gold.fa_disposal_trends` | `silver.fact_asset_master_transactions` | yes |
| `gold.fa_monthly_depreciation_trend` | `silver.fact_asset_journal` | yes |
| `gold.fa_monthly_depreciation_trend` | `silver.fact_asset_master_transactions` | yes |
| `gold.fact_ap_invoices` | `silver.fact_vendor_invoice_headers` | yes |
| `gold.fact_ap_invoices` | `silver.fact_vendor_invoice_lines` | yes |
| `gold.fact_ap_invoices` | `silver.fact_vendor_invoice_journal_headers` | yes |
| `gold.fact_ap_invoices` | `silver.fact_vendor_invoice_journal_lines` | yes |
| `gold.fact_ap_invoices` | `silver.fact_kpmg_vend_payment_bi_vend_trans_open` | yes |
| `gold.fact_journal_entry_subledger_summary_balance` | `silver.fact_fynapse_slr_journals` | yes |
| `gold.fact_trail_balance_extractions` | `gold.fact_trail_balance_extractions` | yes |
| `gold.manage_close_adra_reconciliation` | `silver.adra_account_dimensions` | yes |
| `gold.manage_close_adra_reconciliation` | `silver.adra_account_facts` | yes |
| `gold.manage_close_adra_reconciliation` | `silver.adra_transaction_facts` | yes |
| `gold.manage_close_adra_reconciliation_kpi` | `silver.adra_account_facts` | yes |
| `gold.manage_close_adra_reconciliation_status_kpi` | `silver.adra_account_facts` | yes |
| `gold.manage_close_adra_reconciliation_status_kpi` | `silver.adra_transaction_facts` | yes |
| `gold.manage_close_adra_unreconciled_accounts` | `silver.adra_account_dimensions` | yes |
| `gold.manage_close_adra_unreconciled_accounts` | `silver.adra_account_facts` | yes |
| `gold.manage_close_adra_unreconciled_accounts` | `silver.adra_transaction_facts` | yes |
| `gold.manage_close_adra_unreconciled_accounts_kpi` | `silver.adra_account_facts` | yes |
| `gold.manage_close_adra_unreconciled_accounts_kpi` | `silver.adra_transaction_facts` | yes |
| `gold.manage_close_journal_entries` | `silver.fact_ledger_journal_headers` | yes |
| `gold.manage_close_journal_entries` | `silver.fact_ledger_journal_lines` | yes |
| `gold.manage_close_journal_entries` | `silver.fact_ledger_journal_trans_bi_entities` | yes |
| `gold.managed_coll_due_soon_accounts` | `silver.fact_cust_trans_opens` | yes |
| `gold.managed_coll_due_soon_accounts` | `silver.fact_cust_transactions` | yes |
| `gold.managed_coll_due_soon_accounts` | `silver.fact_cust_table_bi_entities` | yes |
| `gold.managed_coll_early_payment_discounts` | `silver.fact_cust_transactions` | yes |
| `gold.managed_coll_early_payment_discounts` | `silver.fact_cust_trans_opens` | yes |
| `gold.managed_coll_early_payment_discounts` | `silver.fact_cust_table_bi_entities` | yes |
| `gold.managed_coll_early_payment_discounts` | `silver.fact_cash_discounts` | yes |
| `gold.managed_coll_kpi` | `silver.fact_cust_trans_opens` | yes |
| `gold.managed_coll_kpi` | `silver.fact_cust_transactions` | yes |
| `gold.managed_coll_kpi` | `silver.fact_cash_discounts` | yes |
| `gold.managed_coll_overdue` | `silver.fact_cust_trans_opens` | yes |
| `gold.managed_coll_overdue` | `silver.fact_cust_transactions` | yes |
| `gold.managed_coll_overdue` | `silver.fact_cust_table_bi_entities` | yes |
| `gold.mc_actual_cash_balance_by_bank_ac` | `silver.dim_bank_account_table_bi_entities` | yes |
| `gold.mc_actual_cash_balance_by_bank_ac` | `silver.fact_ledger_journal_lines` | yes |
| `gold.mc_actual_cash_balance_by_bank_ac_new` | `silver.dim_bank_account_table_bi_entities` | yes |
| `gold.mc_investment_portfolio` | `silver.fact_kpmg_general_journal_account_entries` | yes |
| `gold.mc_investment_portfolio` | `silver.dim_main_accounts` | yes |
| `gold.mc_kpi` | `silver.fact_ledger_journal_lines` | yes |
| `gold.mc_kpi` | `silver.fact_kpmg_general_journal_account_entries` | yes |
| `gold.mc_kpi` | `silver.dim_bank_account_table_bi_entities` | yes |
| `gold.mc_kpi` | `silver.dim_main_accounts` | yes |
| `gold.mc_kpi_new` | `silver.fact_ledger_journal_lines` | yes |
| `gold.mc_kpi_new` | `silver.fact_kpmg_general_journal_account_entries` | yes |
| `gold.mc_kpi_new` | `silver.dim_bank_account_table_bi_entities` | yes |
| `gold.mc_kpi_new` | `silver.dim_main_accounts` | yes |
| `gold.mc_liquidity` | `silver.fact_kpmg_general_journal_account_entries` | yes |
| `gold.mc_liquidity` | `silver.dim_main_accounts` | yes |
| `gold.vw_access_review` | `silver.access_screen_dim_employee` | yes |
| `gold.vw_access_review` | `silver.access_screen_fact_employee_access` | yes |
| `gold.vw_access_review` | `silver.access_screen_rel_manager_reportee` | yes |
| `gold.vw_access_review` | `silver.access_screen_dim_role` | yes |
| `gold.vw_access_review` | `silver.access_screen_dim_application` | yes |
| `gold.vw_access_review` | `silver.access_screen_dim_legal_entity` | yes |
| `gold.vw_audit_extraction_toolkit` | `silver.audit_extraction_toolkit` | yes |
| `gold.vw_audit_soc_report` | `silver.audit_soc_report` | yes |
| `gold.vw_audit_soc_report_deepplinks` | `silver.audit_soc_report_deepplinks` | yes |
| `gold.vw_balance_sheet` | `silver.fact_kpmg_general_journal_account_entries` | yes |
| `gold.vw_balance_sheet` | `silver.dim_main_accounts` | yes |
| `gold.vw_balance_sheet` | `silver.dim_ledger_bi_entities` | yes |
| `gold.vw_balance_sheet_logistics` | `silver.fact_kpmg_general_journal_account_entries` | yes |
| `gold.vw_balance_sheet_logistics` | `gold.dim_coa_logistics` | yes |
| `gold.vw_cash_reconciliation` | `silver.fact_fynapse_slr_journals` | yes |
| `gold.vw_cash_reconciliation` | `silver.fact_kpmg_general_journal_account_entries` | yes |
| `gold.vw_cash_reconciliation` | `silver.fact_ledger_journal_lines` | yes |
| `gold.vw_cash_reconciliation` | `silver.dim_main_accounts` | yes |
| `gold.vw_commission_analysis_slr_mga` | `silver.fact_fynapse_slr_journals` | yes |
| `gold.vw_commissions_analysis` | `gold.fact_journal_entry_subledger_summary_balance` | yes |
| `gold.vw_commissions_analysis` | `gold.dim_coa` | yes |
| `gold.vw_expense_analysis` | `silver.fact_kpmg_general_journal_account_entries` | yes |
| `gold.vw_expense_analysis` | `silver.dim_main_accounts` | yes |
| `gold.vw_expense_analysis_gl` | `silver.fact_kpmg_general_journal_account_entries` | yes |
| `gold.vw_expense_analysis_gl` | `silver.dim_companies` | yes |
| `gold.vw_expense_analysis_gl` | `silver.dim_main_accounts` | yes |
| `gold.vw_expense_analysis_slr` | `silver.fact_fynapse_slr_journals` | yes |
| `gold.vw_fact_fynapse_slr_journals` | `silver.fact_fynapse_slr_journals` | yes |
| `gold.vw_fact_kpmg_general_journals_entries` | `silver.fact_kpmg_general_journal_account_entries` | yes |
| `gold.vw_income_statement` | `silver.fact_kpmg_general_journal_account_entries` | yes |
| `gold.vw_income_statement` | `silver.dim_main_accounts` | yes |
| `gold.vw_income_statement_logistics` | `silver.fact_kpmg_general_journal_account_entries` | yes |
| `gold.vw_income_statement_logistics` | `gold.dim_coa_logistics` | yes |
| `gold.vw_investment_analytics` | `silver.fact_kpmg_general_journal_account_entries` | yes |
| `gold.vw_investment_analytics` | `silver.dim_main_accounts` | yes |
| `gold.vw_investment_analytics` | `gold.dim_coa` | yes |
| `gold.vw_kpi_pipeline_success` | `gold.pipeline_logs` | yes |
| `gold.vw_kpi_system_and_data_status` | `gold.pipeline_logs` | yes |
| `gold.vw_kpi_system_and_data_status` | `gold.anomaly_audit` | yes |
| `gold.vw_ledger_journal_trans_bi_entities` | `silver.fact_ledger_journal_trans_bi_entities` | yes |
| `gold.vw_legal_entities` | `silver.dim_legal_entities` | yes |
| `gold.vw_manage_close_journal_entry_kpi` | `silver.fact_ledger_journal_headers` | yes |
| `gold.vw_manage_close_journal_entry_kpi` | `silver.fact_ledger_journal_lines` | yes |
| `gold.vw_manage_close_task` | `silver.manage_close_task_facts` | yes |
| `gold.vw_manage_close_task` | `silver.manage_close_task_settings` | yes |
| `gold.vw_manage_close_task_kpi` | `silver.manage_close_task_facts` | yes |
| `gold.vw_manage_close_task_kpi` | `silver.manage_close_task_settings` | yes |
| `gold.vw_managed_coll_due_soon_accounts` | `silver.fact_cust_trans_opens` | yes |
| `gold.vw_managed_coll_due_soon_accounts` | `silver.fact_cust_transactions` | yes |
| `gold.vw_managed_coll_due_soon_accounts` | `silver.fact_cust_table_bi_entities` | yes |
| `gold.vw_managed_coll_due_soon_accounts_filter` | `silver.fact_cust_trans_opens` | yes |
| `gold.vw_managed_coll_due_soon_accounts_filter` | `silver.fact_cust_transactions` | yes |
| `gold.vw_managed_coll_due_soon_accounts_filter` | `silver.fact_cust_table_bi_entities` | yes |
| `gold.vw_managed_coll_early_payment_discounts` | `silver.fact_cust_transactions` | yes |
| `gold.vw_managed_coll_early_payment_discounts` | `silver.fact_cust_trans_opens` | yes |
| `gold.vw_managed_coll_early_payment_discounts` | `silver.fact_cash_discounts` | yes |
| `gold.vw_managed_coll_early_payment_discounts_filter` | `silver.fact_cust_transactions` | yes |
| `gold.vw_managed_coll_early_payment_discounts_filter` | `silver.fact_cust_trans_opens` | yes |
| `gold.vw_managed_coll_early_payment_discounts_filter` | `silver.fact_cash_discounts` | yes |
| `gold.vw_managed_coll_kpi` | `silver.fact_cust_trans_opens` | yes |
| `gold.vw_managed_coll_kpi` | `silver.fact_cust_transactions` | yes |
| `gold.vw_managed_coll_kpi` | `silver.fact_cash_discounts` | yes |
| `gold.vw_managed_coll_kpi_filter` | `silver.fact_cust_trans_opens` | yes |
| `gold.vw_managed_coll_kpi_filter` | `silver.fact_cust_transactions` | yes |
| `gold.vw_managed_coll_kpi_filter` | `silver.fact_cash_discounts` | yes |
| `gold.vw_managed_coll_overdue` | `silver.fact_cust_trans_opens` | yes |
| `gold.vw_managed_coll_overdue` | `silver.fact_cust_transactions` | yes |
| `gold.vw_managed_coll_overdue` | `silver.fact_cust_table_bi_entities` | yes |
| `gold.vw_managed_coll_overdue_filter` | `silver.fact_cust_trans_opens` | yes |
| `gold.vw_managed_coll_overdue_filter` | `silver.fact_cust_transactions` | yes |
| `gold.vw_managed_coll_overdue_filter` | `silver.fact_cust_table_bi_entities` | yes |
| `gold.vw_premium_analysis` | `silver.fact_fynapse_slr_journals` | yes |
| `gold.vw_review_controls` | `silver.review_controls` | yes |
| `gold.vw_review_controls_access_by_area` | `silver.review_controls_access_by_area` | yes |
| `gold.vw_review_controls_user_access_report` | `silver.review_controls_user_access_report` | yes |
| `gold.vw_slr_gl_reconciliation` | `silver.fact_fynapse_slr_journals` | yes |
| `gold.vw_slr_gl_reconciliation` | `silver.fact_kpmg_general_journal_account_entries` | yes |
| `gold.vw_ultimates_analysis` | `silver.fact_fynapse_slr_journals` | yes |
| `gold.vw_user_access_screen` | `silver.access_screen_dim_employee` | yes |
| `gold.vw_user_access_screen` | `silver.access_screen_fact_employee_access` | yes |
| `gold.vw_user_access_screen` | `silver.access_screen_rel_manager_reportee` | yes |
| `gold.vw_user_access_screen` | `silver.access_screen_dim_role` | yes |
| `gold.vw_user_access_screen` | `silver.access_screen_dim_application` | yes |
| `gold.vw_user_access_screen` | `silver.access_screen_dim_legal_entity` | yes |
| `silver.manage_close_recon_account_dims` | `adra_account_dimensions (likely)` | no |
| `silver.manage_close_recon_account_facts` | `adra_account_facts (likely)` | no |
| `silver.manage_close_task_facts` | `adra_tasks_task_facts (likely)` | no |
| `silver.manage_close_task_settings` | `adra_tasks_task_settings_dimension (likely)` | no |
