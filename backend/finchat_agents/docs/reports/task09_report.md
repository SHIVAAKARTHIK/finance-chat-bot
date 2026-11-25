# Task 09 report: scheduled summary agent (21 Nov 2026)

## Existing code
Dhivya's fact collection / card generation is not in this workspace (`reference/legacy/summary/` does not exist, and
the reference zips contain no card code). Per the updated prompt I did not search other branches; everything below is
built new, with no KPI-registry or entity-scope code.

## What was built
- **Config** `config/summary_metrics.yaml` (used only by the summary agent, never by chat): period sets (SQL listing the
  periods with data) and 6 metrics, each a SQL template over knowledge-layer tables with a business name and thresholds:
  - recon (ADRA, per entity because each entity has its own periods): reconciliations not finalized; total absolute
    unreconciled difference; reconciliations by approval status.
  - subledger (Fynapse, per fiscal period): journal lines by source system; net reporting amount.
  - fa: fixed-asset transactions by type per posting month (run_sql's duplicate-load warning is carried onto the card).
- **Collect facts** (`summary/facts.py`): every SQL runs through run_sql's guardrails with the access file's
  `service_role`; current and previous period per scope; placeholders filled with safely quoted literals; a broken
  metric is recorded as an error and the run continues (status `partial`).
- **Rank / select** (code): key change when |change_pct| >= 10% and |change_abs| >= the metric's `min_abs`; flagged
  when |change_pct| >= 25%; top 5 per domain, key changes first (largest change), status cards fill the rest. A value
  new from zero is shown but not flagged.
- **Cards** (`summary/cards.py`, prompt `summary_cards.md`): gpt-oss writes title + text from the facts only; each card
  is number-checked against its own fact, and a card that fails gets a plain wording built from the fact in code.
- **Investigator** (flagged cards only): the v3 SQL agent with a hard 2-query budget (its own counters, service role,
  same guardrails) and the task "explain this change". `explained`, `no_cause_found` (card says "No cause found in 2
  queries.") or `failed` (explanation not supported by its query results). Its SQL is stored for audit only.
- **Storage** (`storage/summary_store.py`): checks both tables exist first and stops with a clear message if not
  (never creates them); one `finance_chat_summary_runs` row (running -> succeeded / partial / failed with counts and
  tokens); cards via MERGE; superseding per the rules below. Trace events go to
  `finance_chat_message_events` with message_id = conversation_id = run_id.
- **API** `GET /v3/cards`: active cards for the caller's role domains (SQL `domain IN (...)` plus a second check in
  code); `*` roles see all; no role -> empty list; investigator SQL is never returned.
- **Scheduler** `python -m finchat_agents.summary.run [--domain X] [--dry-run] [--trigger schedule]` for cron
  (default daily 07:00 IST, to be confirmed). `--dry-run` prints the cards and writes nothing.

## Tests
`..\.venv\Scripts\python -m pytest -q`: 303 passed, 30 skipped (live) after the superseding change. `test_summary.py`: every metric and period SQL
passes the guardrails against the real knowledge pages; literal quoting; facts, ranking and flagging (per-entity
periods, single-period entity -> status card, below-threshold changes dropped, zero previous); card number check
with plain fallback; investigator stopped at 2 queries (the third is refused); no-cause path; dry run produces recon
and subledger cards with explanations or "no cause found" and writes nothing; real run writes running + final run rows,
one card MERGE + whole-domain supersede per completed domain and trace events by run id, and never a CREATE; missing tables -> clear message and
no writes; GET /v3/cards role filtering.

Live (company laptop, `docs/LIVE_RUN.md`): `summary.run --dry-run`, then a real run once the tables exist.

## Superseding rules (decided by Karthik, 21 Nov 2026)
- Each domain is processed on its own (facts, ranking, cards, investigator, save).
- A domain that finishes **without errors** MERGEs its new cards and then marks **all** its older active cards
  `superseded` (any metric, including metrics that no longer pass the thresholds, so stale big-change cards disappear).
  The MERGE and the UPDATE go in one batch; the UPDATE runs only if the MERGE succeeded. A domain whose period query
  returns no periods (no data at all) is an error ("no periods with data"), not a quiet empty domain, so its older cards stay.
- A domain that **fails or is only partly processed** (any metric error, an exception, or a failed save) writes no new
  cards and supersedes nothing: its previous active cards stay.
- Run status: `succeeded` when every domain completed; `partial` when at least one completed and at least one failed;
  `failed` when no domain completed (nothing is superseded).
- `finance_chat_summary_runs.error_message` holds one short line per failed domain:
  `recon: <first error, max 160 chars> (+2 more); subledger: ...` (full errors are in the CLI output and trace events).
- `--domain X` reads, writes and supersedes only domain X. An unknown domain is incomplete (nothing superseded).
- `--dry-run` changes nothing.
- Cards are never deleted; superseded rows stay as history (only `status` is updated).

## Assumptions
- Recon metrics are per entity (ADRA entities have different periods; an all-entity total would compare different
  entity sets). Card metric names include the entity.
- Cards of an incomplete domain are not saved at all (not even as inactive), so the UI never mixes a partial set with
  the previous one; the CLI output lists them under "Not saved".
- The investigator gets up to 6 model steps and 3 minutes per flagged card.
- Fixed-asset months come from POSTING_DATE; the fa period query is not verified against live data.

## Open questions
1. (Resolved: superseding rules above.)
2. Thresholds (10% / 25% / min_abs per metric) and the 6 starting metrics: OK, or should Finance pick others?
3. Schedule: daily 07:00 IST?

## Superseding tests (added)
whole-domain UPDATE without a metric filter; all domains complete (including a domain with no cards); partly
processed domain keeps its cards and the run is `partial` with the error recorded; failed card save supersedes
nothing; all domains failed -> `failed`, no card MERGE or supersede, one short error line per domain; `--domain subledger` touches only subledger (recon not even
read); unknown domain supersedes nothing; dry run with failures writes nothing; never DELETE / TRUNCATE / DROP.
