Copilot prompt: draft the remaining Fill_in details (run once with schema = silver, once with schema = gold).
Run after scripts/export_table_catalog.py has produced output/table_catalog.xlsx, output/fill_in.csv and
output/catalog_summary.md. This uses few credits: Copilot only reads text files and writes one CSV.

---

Read output/catalog_summary.md and output/fill_in.csv. Also read, for business context only:
finchat_v3_starter/reference/legacy/ (glossary, domains, calendar, v2_config/tables.yaml if present) and finchat_v3_starter/reference/semantic_pages/.
Do NOT run any SQL, scripts or terminal commands. Do NOT change any other file.

For every row in fill_in.csv where schema = silver (next time: gold), write output/fill_in_draft_silver.csv
(next time: output/fill_in_draft_gold.csv) with the same columns plus two extra columns "confidence" (high / medium / low) and "notes".
Fill only empty cells; keep every existing value, including cells starting with "proposed:".
- domain: one of ar, ap, gl, fa, cash, recon (ADRA), subledger (Fynapse); leave empty if unsure
- purpose: one short business sentence (what the table is for)
- grain: if empty, describe one row in business words; if "proposed:", add the business meaning after it
- primary_key: if empty and the summary says "no unique combination", suggest the likely business key and say why in notes
- entity_column / period_columns: column names from the summary
- pii_columns: person-related columns (names, emails, user ids)
- built_from: for gold tables, the silver tables it most likely comes from (only if the names or columns make it clear)
- known_issues: keep existing; add obvious ones (all-null columns, constant columns, "broken: <error>" for tables
  whose summary shows no rows because the query failed)
Use low confidence and a note when guessing. Output only the CSV file.

---

After Copilot: review medium and low confidence rows (domain and grain first), fix them, save as
data/table_catalog/fill_in_reviewed_silver.csv and fill_in_reviewed_gold.csv, and copy
table_catalog.xlsx and catalog_summary.md into data/table_catalog/. Then run prompts/08_full_catalog.md in Claude Code.
