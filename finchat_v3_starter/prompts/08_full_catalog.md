Task 08: load all 122 tables from the catalog export. Read CLAUDE.md and docs/SPEC.md section 5 first.
Run after tasks 01-03 are done.

Inputs in data/table_catalog/ (produced by scripts/export_table_catalog.py, then completed with
prompts/catalog_fill_copilot.md and reviewed by Karthik):
- table_catalog.xlsx: sheets Tables (row count, primary_key_hint, exact_duplicate_rows), Keys (declared, proposed
  composite keys), Columns (type, comment, approx_distinct, min, max, null_count), Values (full value lists for
  columns with <= 50 values), Samples (5 rows per table), Fill_in, Errors (objects that failed)
- fill_in_reviewed_silver.csv and fill_in_reviewed_gold.csv: reviewed Fill_in values (these win over the Fill_in sheet),
  with confidence and notes columns
- catalog_summary.md: one block per table (for reading; the Excel and CSVs are the source)
These files contain real sample values. Do not commit them to git; add data/table_catalog/*.xlsx, *.csv and
catalog_summary.md to .gitignore if not already there.

1. Run knowledge/generator.py: create pages for new tables, update profiles (types, values, min/max, null counts,
   row counts, samples as examples) on existing ones, and never overwrite reviewed fields.
2. Front matter from the reviewed CSVs: domain, purpose, grain, primary_key, entity_column, period_columns,
   pii_columns, built_from, known_issues. Values starting with "proposed:" are kept as proposals (flag them in REVIEW.md).
   Rows with confidence = low are flagged in REVIEW.md.
3. Tables without a domain: list them and exclude them from search until a domain is set.
4. Broken objects: tables or views listed in the Errors sheet with UNRESOLVED_COLUMN (or any error on the profiling
   query) cannot be queried in Databricks. Create their pages with `status: broken` and the error text, exclude them
   from search_tables and run_sql, and list them in REVIEW.md for the data team. Re-enable automatically when a later
   export profiles them without error.
5. Duplicates: tables with exact_duplicate_rows > 0 get a known_issues note; run_sql adds a duplicate warning when they are queried.
6. Joins: propose joins.yaml entries from declared foreign keys (Keys sheet), matching key column names across tables,
   and built_from lineage. Mark them `status: proposed`; only `approved` joins are used by get_join_path.
7. Rebuild INDEX.md and the search index.

Acceptance: every table has a valid page; broken and domain-less tables are excluded from search; search finds the right
table for 20 sample questions across gold domains; knowledge/REVIEW.md lists missing domains, proposed keys and grains,
low-confidence rows, proposed joins, broken objects and duplicate tables, grouped so Karthik can approve them quickly.
