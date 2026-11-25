Task 09: scheduled summary agent. Read CLAUDE.md and docs/SPEC.md first. Run after task 04 (agents) works.

Design (from Dhivya): scheduler -> collect facts -> rank/select (code) -> generate cards -> flagged big change? ->
investigator (max 2 queries) -> explanation attached to the key-change card.

Tables: reference/aiops/finance_chat_summary_cards.sql (finance_chat_summary_runs, finance_chat_summary_cards).
Karthik creates them in Databricks after review; if they do not exist yet, the code must fail with a clear message,
not create them itself. Writes only to these two tables.

1. Existing code: Dhivya's fact collection / card generation lives on another branch (feature/finance-kpi or hers).
   Do not search other branches yourself. If Karthik has copied it into reference/legacy/summary/, reuse its logic;
   otherwise build it as below. Never bring in KPI-registry or entity-scope code.
2. Collect facts (code, config-driven): config/summary_metrics.yaml lists metrics per domain, each with a SQL
   template over knowledge-layer tables (current period and previous period), a business name and thresholds.
   Start with 3-5 metrics for recon (ADRA: not finalized accounts, unreconciled difference, approval status counts),
   subledger (Fynapse: journal lines by source, net amount) and fa (with the duplicate warning). Run through run_sql
   with the service role (rbac service_role).
3. Rank/select (code): change_pct and change_abs vs thresholds per metric (defaults: |change_pct| >= 10% and
   |change_abs| >= the metric's min_abs); top 5 cards per domain; flagged = above the big-change threshold
   (default |change_pct| >= 25%).
4. Generate cards: the response model (gpt-oss) writes title + card_text from the selected facts only; numbers come
   from the facts (apply the number check).
5. Investigator (flagged cards only): the v3 SQL agent with a 2-query budget and the task "explain this change"
   (which accounts, sources or entities drove it); same run_sql guardrails. If no cause is found in 2 queries,
   explanation_status = no_cause_found and the card says so. Investigator SQL stored for audit only.
6. Storage: one finance_chat_summary_runs row per run; cards via MERGE; previous active cards for the same
   domain + metric become superseded. Trace events in finance_chat_message_events with the run_id.
7. API: GET /v3/cards returns active cards for the caller's role domains (filtered at read time).
8. Scheduler: CLI entry point `python -m finchat_agents.summary.run [--domain X] [--dry-run]` that cron on the VM can
   call (default schedule daily 07:00 IST, to confirm). --dry-run prints cards without writing.

Acceptance: --dry-run produces cards for recon and subledger from the latest periods; flagged cards carry an explanation
or "no cause found"; a real run writes one run row and its cards; GET /v3/cards filters by role; tests with fakes for
ranking, flagging, supersede logic and the 2-query budget.
