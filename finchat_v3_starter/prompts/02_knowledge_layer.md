Task 02: knowledge layer for ADRA, Fynapse and fixed assets. Read CLAUDE.md and docs/SPEC.md section 5-6 first.

Inputs (in the starter pack, copy into the repo under backend/finchat_agents/reference/):
- reference/semantic_pages/adra/*.md and fynapse/*.md (already reviewed table pages, joins, metrics, rules, verified queries)
- reference/legacy/silver_query_skill.md, reference/legacy/glossary.yaml, domains.yaml, calendar.yaml (v2 knowledge; reuse facts, not structure)
- reference/question_bank/*.yaml (questions with expected answers; use their SQL / patterns as examples)

Build backend/finchat_agents/knowledge/:
1. tables/<schema>.<table>.md for the 6 ADRA tables, the Fynapse table and the fixed-asset tables, in the format of
   reference/semantic_pages, plus a front-matter block: name, schema, layer, domain (recon | subledger | fa), grain,
   primary_key, entity_column, period_columns, pii_columns, known_issues.
   - Remove every hardcoded entity scope (581, 14781, 14782, UK03..UK17, DATA_AREA_ID 100/dat). Describe the columns, not allowed values.
   - Fynapse: note the entity values recently changed to 100 (being confirmed); tell agents to check current values with get_column_values.
   - Fixed assets: note the duplicate loads and how to detect them.
2. INDEX.md (one line per table) and joins.yaml (from adra/joins.md; composite keys in full).
3. glossary.md and rules.md (merge adra/fynapse rules + legacy glossary; drop KPI content).
4. examples.yaml: question, sql, tables, expected (if known). Use the verified queries; strip entity-scope filters that
   came from RBAC, keep filters the question itself asks for.
5. knowledge/loader.py: loads pages, index, joins, glossary, examples; validates front matter; builds a simple search
   index (BM25 over name, purpose, synonyms, column names; embeddings optional later).
6. knowledge/generator.py: reads the catalog Excel (sheets Tables, Keys, Columns, Values, Samples, Fill_in, Errors from
   scripts/export_table_catalog.py) plus optional reviewed CSVs (fill_in_reviewed_*.csv, which win over Fill_in) and
   writes/updates table pages; objects in Errors get `status: broken`. It must never overwrite a field a person edited
   (keep a `reviewed: true` marker per field or section). Test it with a small fake Excel; real Excel comes later.

Acceptance
- Loader tests: every page valid, every join references known tables/columns, no hardcoded entity values in pages.
- Search test: 15 sample questions from the question banks return the right table in the top 3.
- Report: pages created, anything you could not determine (list as questions for Karthik).
