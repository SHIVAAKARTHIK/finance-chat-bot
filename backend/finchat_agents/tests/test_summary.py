"""Task 09: summary agent with fakes: config SQL validity, ranking, flagging, card text number check, the 2-query
investigator budget, dry run, storage (run row, cards, supersede, missing tables) and GET /v3/cards role filtering."""
from __future__ import annotations

import json
import re
from decimal import Decimal

import httpx
import pytest
from fastapi import FastAPI

from finchat_agents.access import AccessConfig, Role, UserAccess
from finchat_agents.agents.specialists import build_sql_agent
from finchat_agents.api.router import create_router
from finchat_agents.config import Settings
from finchat_agents.knowledge.loader import Knowledge
from finchat_agents.llm import fake
from finchat_agents.llm.fake import FakeProvider
from finchat_agents.llm.types import LLMResult, ModelHandle, ToolCall
from finchat_agents.runtime.tools import RunContext
from finchat_agents.storage.aiops import AiopsStore
from finchat_agents.storage.summary_store import SummaryStore, SummaryTablesMissing, build_supersede
from finchat_agents.summary.cards import NO_CAUSE, CardWriter, investigate, plain_card
from finchat_agents.summary.facts import Fact, collect_facts, load_config, rank_and_select, render, sql_literal
from finchat_agents.summary.pipeline import cards_markdown, run_summary
from finchat_agents.tools import build_data_tools
from finchat_agents.tools.sql_guard import guard_sql
from finchat_agents.tracing import MemorySink, Tracer

from .fakes import DT, L, S, FakeMcpServer, data_responder, make_deps

SERVICE = UserAccess(user_id="service", role=Role(name="finance_all", domains=["*"]))
CFG = load_config(Settings(_env_file=None).resolve_path("config/summary_metrics.yaml"))
D = "DECIMAL"


@pytest.fixture(scope="module")
def kb() -> Knowledge:
    return Knowledge.load()


def summary_responder(sql: str):
    s = sql.lower()
    if "as scope" in s:
        return [("scope", S), ("label", S), ("sort_key", DT)], [
            ["Cars USA Shipping, LLC", "Oct 26", "2026-10-31"], ["Cars USA Shipping, LLC", "Sep 26", "2026-09-30"],
            ["100-Northwind", "Feb 25", "2025-02-28"]]
    if "concat('fy'" in s:
        return [("FISCAL_YEAR", L), ("PERIOD", L), ("label", S), ("sort_key", DT)], [
            [2026, 9, "FY2026 P9", "2026-09-30"], [2026, 8, "FY2026 P8", "2026-08-31"]]
    if "month_start" in s:
        return [("month_start", DT), ("label", S), ("sort_key", DT)], []
    label = next((x for x in ("oct 26", "sep 26", "feb 25") if f"'{x}'" in s), None)
    if "is_finalized" in s:
        return [("value", L)], [[{"oct 26": 17, "sep 26": 12, "feb 25": 38}[label]]]
    if "unidentified_balance_abs" in s:
        return [("value", D)], [[{"oct 26": "22831252.26", "sep 26": "22000000.00", "feb 25": "3940448.00"}[label]]]
    if "account_status" in s and "grp" in s:
        return [("grp", S), ("value", L)], [["Approved", 6], ["Not prepared", 11], ["Prepared", 6]]
    if "source_system as grp" in s:
        return [("grp", S), ("value", L)], ([["NOVIDEA", 433], ["ACCRUAL", 100]] if "period = 9" in s else [["NOVIDEA", 200], ["ACCRUAL", 100]])
    if "sum(reporting_amount)" in s:
        return [("value", D)], [["-0.06" if "period = 9" in s else "-0.02"]]
    return data_responder(sql)


# ---------------------------------------------------------------- config

def test_every_metric_and_period_sql_passes_the_guardrails(kb):
    sample = {"scope": "Cars USA Shipping, LLC", "label": "Oct 26", "FISCAL_YEAR": 2026, "PERIOD": 9, "month_start": "2026-09-01"}
    for name, ps in CFG.period_sets.items():
        guard_sql(ps["sql"], kb, SERVICE, 1000)
    for m in CFG.metrics:
        g = guard_sql(render(m.sql, sample), kb, SERVICE, 1000)
        assert {p.id for p in g.tables} <= set(m.tables) | {"silver.adra_legal_entity_dimensions", "silver.adra_period_dimensions"}
    assert set(CFG.domains) == {"recon", "subledger", "fa"} and CFG.defaults.top_n == 5


def test_literals_are_quoted_safely():
    assert sql_literal("O'Brien'; DROP TABLE x --") == "'O''Brien''; DROP TABLE x --'"
    assert sql_literal(9) == "9" and sql_literal(None) == "NULL"
    with pytest.raises(KeyError, match="placeholder"):
        render("SELECT {missing}", {"label": "x"})


# ---------------------------------------------------------------- facts, ranking, flagging

async def test_collect_rank_and_flag(kb):
    deps, server = make_deps(FakeMcpServer(summary_responder), kb=kb)
    errors: list[str] = []
    facts = await collect_facts(CFG, deps, SERVICE, ["recon", "subledger"], errors)
    assert errors == []
    by = {(f.metric_id, f.scope, f.group): f for f in facts}
    nf = by[("recon_not_finalized", "Cars USA Shipping, LLC", None)]
    assert (nf.current_value, nf.previous_value, nf.change_abs, nf.change_pct) == (17, 12, 5, Decimal("41.7"))
    assert nf.period_label == "Oct 26" and nf.comparison_label == "vs Sep 26"
    assert by[("recon_not_finalized", "100-Northwind", None)].previous_value is None  # only one period
    selected = rank_and_select(facts, CFG)
    recon = [f for f in selected if f.domain == "recon"]
    assert recon[0] is nf and nf.flagged and nf.card_type == "key_change" and nf.rank == 1
    unid = by[("recon_unidentified_abs", "Cars USA Shipping, LLC", None)]
    assert not unid.selected  # +3.8%: below the 10% threshold
    assert all(f.card_type == "status" for f in recon[1:])  # the rest are Northwind status facts filling the top 5
    assert len(recon) == 5
    src = by[("subledger_lines_by_source", None, "NOVIDEA")]
    assert src.flagged and src.change_pct == Decimal("116.5")
    assert not by[("subledger_net_amount", None, None)].selected or by[("subledger_net_amount", None, None)].card_type == "status"


async def test_a_period_set_without_rows_is_an_error_not_a_silent_empty_domain(kb):
    def responder(sql: str):
        if "concat('fy'" in sql.lower():
            return [("FISCAL_YEAR", L), ("PERIOD", L), ("label", S), ("sort_key", DT)], []  # e.g. every fiscal period is NULL
        return summary_responder(sql)

    deps, _ = make_deps(FakeMcpServer(responder), kb=kb)
    errors: list[str] = []
    facts = await collect_facts(CFG, deps, SERVICE, ["subledger"], errors)
    assert facts == [] and len(errors) == 2 and all("no periods with data" in e for e in errors)


async def test_a_null_value_makes_no_card_and_the_fynapse_period_query_skips_null_periods(kb):
    """A SUM over no rows is NULL: that must not become a "not available" card; and periods with a NULL fiscal year or
    period (which would sort first and match no rows) are not offered as the current period."""
    def responder(sql: str):
        if "sum(reporting_amount)" in sql.lower():
            return [("value", D)], [[None]]
        return summary_responder(sql)

    deps, _ = make_deps(FakeMcpServer(responder), kb=kb)
    errors: list[str] = []
    facts = await collect_facts(CFG, deps, SERVICE, ["subledger"], errors)
    assert errors == [] and not [f for f in facts if f.metric_id == "subledger_net_amount"]
    assert [f for f in facts if f.metric_id == "subledger_lines_by_source"]  # the other metric still produces facts
    assert "FISCAL_YEAR IS NOT NULL AND PERIOD IS NOT NULL" in " ".join(CFG.period_sets["fynapse_periods"]["sql"].split())


def test_new_from_zero_values_do_not_push_out_a_real_big_decline():
    """Fixed assets once showed five "new from zero" cards and dropped a -97% fall (182 -> 5) because zero-previous sorted first."""
    def fact(name, cur, prev, pct=None):
        f = Fact(metric_id="fa_transactions_by_type", domain="fa", metric_name=name, current_value=Decimal(cur), previous_value=Decimal(prev))
        f.change_abs = f.current_value - f.previous_value
        f.change_pct = Decimal(str(pct)) if pct is not None else None
        return f

    new = [fact(f"type {i}", 9, 0) for i in range(6)]
    decline = fact("Depreciation", 5, 182, -97.3)
    sel = rank_and_select([*new, decline], CFG)
    assert sel[0] is decline and decline.flagged and decline.rank == 1
    assert len([f for f in sel if f.domain == "fa"]) == 5  # top 5: the decline plus four of the new values


def test_ranking_thresholds_and_zero_previous():
    def fact(mid, cur, prev, pct=None, domain="recon"):
        f = Fact(metric_id=mid, domain=domain, metric_name=mid, current_value=Decimal(cur), previous_value=Decimal(prev))
        f.change_abs = f.current_value - f.previous_value
        f.change_pct = Decimal(str(pct)) if pct is not None else None
        return f

    facts = [fact("recon_not_finalized", 13, 12, 8.3), fact("recon_status_counts", 30, 10, 200), fact("recon_not_finalized", 5, 0),
             fact("recon_unidentified_abs", 2500, 1000, 150), fact("recon_unidentified_abs", 1010, 900, 12.2)]
    sel = rank_and_select(facts, CFG)
    assert [f.metric_id for f in sel if f.card_type == "key_change"] == ["recon_status_counts", "recon_unidentified_abs", "recon_not_finalized"]
    assert sel[0].flagged and sel[1].flagged  # 200% then 150%: real big changes first
    assert sel[2].change_pct is None and not sel[2].flagged  # new from zero: shown after them, not flagged
    assert not facts[0].selected and not facts[4].selected  # 8.3% below 10%; 110 below min_abs 1000


# ---------------------------------------------------------------- card text

async def test_card_writer_number_check_falls_back_to_plain_text():
    f1 = Fact(metric_id="m", domain="recon", metric_name="Not finalized", period_label="Oct 26", comparison_label="vs Sep 26",
              current_value=Decimal(17), previous_value=Decimal(12), change_abs=Decimal(5), change_pct=Decimal("41.7"))
    f2 = f1.model_copy(update={"fact_id": "f2"})

    def reply(record):
        return fake.tool_call("submit_result", {"cards": [
            {"fact_id": f1.fact_id, "title": "Not finalized up 41.7%", "card_text": "17 in Oct 26, up from 12 in Sep 26."},
            {"fact_id": "f2", "title": "Big jump", "card_text": "Up to 99 accounts."}]})

    writer = CardWriter(ModelHandle(FakeProvider([reply]), "gptoss"))
    out = await writer.write([f1, f2], RunContext(tracer=Tracer([MemorySink()])))
    assert out[f1.fact_id].card_text == "17 in Oct 26, up from 12 in Sep 26." and not out[f1.fact_id].fallback
    assert out["f2"].fallback and out["f2"].card_text == plain_card(f2).card_text
    assert "compared with 12 in Sep 26 (+41.7%)" in out["f2"].card_text


# ---------------------------------------------------------------- investigator budget

async def test_investigator_has_a_two_query_budget(kb):
    deps, server = make_deps(FakeMcpServer(summary_responder), kb=kb)
    q = "SELECT COUNT(*) AS n FROM lakehouse_mvpai.silver.adra_account_facts"
    p = FakeProvider([fake.tool_call("run_sql", {"sql": q}), fake.tool_call("run_sql", {"sql": q}),
                      fake.tool_call("run_sql", {"sql": q}),
                      fake.tool_call("submit_result", {"answer": "Mostly new accounts.", "status": "ok", "result_ids": ["r1"], "explanation": "e"})])
    agent = build_sql_agent(ModelHandle(p, "claude"), build_data_tools(deps), kb)
    f = Fact(metric_id="m", domain="recon", metric_name="Not finalized", current_value=Decimal(17), previous_value=Decimal(12),
             change_abs=Decimal(5), change_pct=Decimal("41.7"), period_label="Oct 26", comparison_label="vs Sep 26")
    inv = await investigate(agent, f, SERVICE, Tracer([MemorySink()]))
    assert len(server.queries) == 2 and len(inv.sql) == 2
    third = p.calls[3]["messages"][-1].content[0]
    assert third.is_error and "SQL call budget reached (2 queries" in third.content
    assert inv.status == "explained" and inv.explanation == "Mostly new accounts."
    assert "at most 2 queries" in p.calls[0]["messages"][0].text


async def test_investigator_no_cause(kb):
    deps, _ = make_deps(FakeMcpServer(summary_responder), kb=kb)
    p = FakeProvider([fake.tool_call("submit_result", {"answer": "", "status": "no_data", "result_ids": [], "explanation": ""})])
    inv = await investigate(build_sql_agent(ModelHandle(p, "c"), build_data_tools(deps), kb), Fact(metric_id="m", domain="recon",
                            metric_name="x"), SERVICE, Tracer([MemorySink()]))
    assert inv.status == "no_cause_found" and inv.explanation == NO_CAUSE


# ---------------------------------------------------------------- pipeline

def card_reply(record):
    facts = json.loads(record["messages"][0].text.split("\n", 1)[1])
    cards = [{"fact_id": f["fact_id"], "title": f["name"][:40], "card_text": f"{f['name']} in {f['period']}."} for f in facts]
    return LLMResult(tool_calls=[ToolCall(id="w1", name="submit_result", input={"cards": cards})], stop_reason="tool_use")


def investigator_script():
    return [fake.tool_call("submit_result", {"answer": "Driven by accounts moving back to not prepared.", "status": "ok",
                                             "result_ids": [], "explanation": "e"}),
            fake.tool_call("submit_result", {"answer": "", "status": "no_data", "result_ids": [], "explanation": ""})]


async def run(kb, store=None, dry_run=True, domains=("recon", "subledger"), responder=summary_responder):
    deps, server = make_deps(FakeMcpServer(responder), kb=kb)
    sql_agent = build_sql_agent(ModelHandle(FakeProvider(investigator_script()), "claude"), build_data_tools(deps), kb)
    writer = CardWriter(ModelHandle(FakeProvider([card_reply] * 3), "gptoss"))  # one card call per domain
    return await run_summary(cfg=CFG, deps=deps, sql_agent=sql_agent, card_writer=writer, access=SERVICE, store=store,
                             domains=list(domains), dry_run=dry_run), server


async def test_dry_run_produces_cards_and_explanations_without_writing(kb):
    result, server = await run(kb)
    assert result.status == "succeeded" and result.dry_run
    domains = {c["domain"] for c in result.cards}
    assert domains == {"recon", "subledger"}
    flagged = [c for c in result.cards if c["is_flagged"]]
    assert len(flagged) == 2
    assert flagged[0]["explanation_status"] == "explained" and flagged[1]["explanation"] == NO_CAUSE
    assert all(c["explanation_status"] == "not_flagged" for c in result.cards if not c["is_flagged"])
    assert not any(q.lower().startswith(("merge", "update", "insert")) for q in server.queries)
    md = cards_markdown(result)
    assert "dry run" in md and "[flagged]" in md


class SummaryExecutor:
    def __init__(self, missing: bool = False, cards: list[dict] | None = None, fail_domain: str | None = None):
        self.missing, self.cards, self.fail_domain = missing, cards or [], fail_domain
        self.statements: list[tuple[str, dict]] = []
        self.batches: list[list[tuple[str, dict]]] = []
        self.queries: list[tuple[str, dict]] = []

    async def execute(self, statements):
        if self.fail_domain and any(p.get("domain") == self.fail_domain for sql, p in statements if "summary_cards" in sql):
            raise RuntimeError("warehouse unavailable")
        self.batches.append(list(statements))
        self.statements += statements

    async def query(self, sql, params):
        self.queries.append((sql, params))
        if sql.startswith("SELECT 1 FROM") and self.missing:
            raise RuntimeError("[TABLE_OR_VIEW_NOT_FOUND] The table or view `lakehouse_mvpai`.`aiops`.`finance_chat_summary_runs` cannot be found.")
        if "finance_chat_summary_cards" in sql:
            return self.cards
        return []


async def test_real_run_writes_run_row_cards_and_supersedes(kb):
    ex = SummaryExecutor()
    result, _ = await run(kb, store=SummaryStore(ex), dry_run=False)
    runs = [s for s in ex.statements if "MERGE INTO lakehouse_mvpai.aiops.finance_chat_summary_runs " in s[0]]
    assert [s[1]["r0_status"] for s in runs] == ["running", "succeeded"]
    final = runs[-1][1]
    assert final["r0_cards_created"] == len(result.cards) and final["r0_cards_flagged"] == 2 and final["r0_run_id"] == result.run_id
    cards = [s for s in ex.statements if "MERGE INTO lakehouse_mvpai.aiops.finance_chat_summary_cards " in s[0]]
    assert len(cards) == 2 and sum(c[0].count(" UNION ALL ") + 1 for c in cards) == len(result.cards)  # one MERGE per domain
    supersede = [s for s in ex.statements if s[0].startswith("UPDATE lakehouse_mvpai.aiops.finance_chat_summary_cards")]
    assert {s[1]["domain"] for s in supersede} == {"recon", "subledger"}
    assert all(s[1]["run_id"] == result.run_id and "run_id <> CAST(:run_id AS STRING)" in s[0] for s in supersede)
    events = [s for s in ex.statements if "finance_chat_message_events" in s[0]]
    assert events and events[0][1]["r0_message_id"] == result.run_id  # trace events keyed by the run id
    assert not any("CREATE" in s[0].upper().split("(")[0] for s in ex.statements)  # never creates tables


async def test_missing_tables_stop_with_a_clear_message_and_write_nothing(kb):
    ex = SummaryExecutor(missing=True)
    with pytest.raises(SummaryTablesMissing, match="finance_chat_summary_cards.sql.*never creates tables"):
        await run(kb, store=SummaryStore(ex), dry_run=False)
    assert ex.statements == []


def test_supersede_statement_covers_the_whole_domain():
    sql, params = build_supersede("lakehouse_mvpai", "aiops", "recon", "run-2")
    assert sql == ("UPDATE lakehouse_mvpai.aiops.finance_chat_summary_cards SET status = 'superseded' WHERE status = 'active' "
                   "AND domain = CAST(:domain AS STRING) AND run_id <> CAST(:run_id AS STRING)")
    assert params == {"domain": "recon", "run_id": "run-2"} and "metric_name" not in sql
    with pytest.raises(Exception):
        build_supersede("lakehouse_mvpai", "gold", "recon", "r")


# ---------------------------------------------------------------- supersede rules: success, partial failure, one domain

def card_batches(ex: SummaryExecutor) -> dict[str, list[str]]:
    """domain -> statement kinds ("MERGE" / "UPDATE") of its card batch."""
    out: dict[str, list[str]] = {}
    for batch in ex.batches:
        if not any("finance_chat_summary_cards" in sql for sql, _ in batch):
            continue
        upd = [p for sql, p in batch if sql.startswith("UPDATE")]
        assert len(upd) == 1 and batch[-1][0].startswith("UPDATE")  # supersede runs last, after the MERGE
        out[upd[0]["domain"]] = [sql.split()[0] for sql, _ in batch]
    return out


def final_run_row(ex: SummaryExecutor) -> dict:
    runs = [s[1] for s in ex.statements if "MERGE INTO lakehouse_mvpai.aiops.finance_chat_summary_runs " in s[0]]
    return runs[-1]


def never_deletes(ex: SummaryExecutor) -> bool:
    return not any(sql.lstrip().upper().startswith(("DELETE", "TRUNCATE", "DROP")) for sql, _ in ex.statements)


def card_domains_written(ex: SummaryExecutor) -> set[str]:
    """Domains of every card row MERGEd or superseded (MERGE params are r<i>_domain)."""
    out = set()
    for sql, p in ex.statements:
        if "finance_chat_summary_cards" in sql:
            out |= {v for k, v in p.items() if k == "domain" or k.endswith("_domain")}
    return out


async def test_successful_domains_supersede_all_their_older_cards(kb):
    ex = SummaryExecutor()
    result, _ = await run(kb, store=SummaryStore(ex), dry_run=False, domains=("recon", "subledger"))
    assert result.status == "succeeded" and result.domains == {"recon": "complete", "subledger": "complete"}
    batches = card_batches(ex)
    assert batches["recon"] == ["MERGE", "UPDATE"] and batches["subledger"] == ["MERGE", "UPDATE"]
    for sql, p in ex.statements:
        if sql.startswith("UPDATE"):
            assert "metric_name" not in sql and p["run_id"] == result.run_id  # whole domain, never this run's cards
    row = final_run_row(ex)
    assert row["r0_status"] == "succeeded" and row["r0_error_message"] is None
    assert never_deletes(ex)


async def test_a_domain_whose_data_has_no_periods_keeps_its_old_cards(kb):
    """fa has no months with data in this fake: an error, not a quiet empty domain that would replace its cards with nothing."""
    ex = SummaryExecutor()
    result, _ = await run(kb, store=SummaryStore(ex), dry_run=False, domains=("recon", "fa"))
    assert result.status == "partial" and result.domains == {"recon": "complete", "fa": "incomplete"}
    assert set(card_batches(ex)) == {"recon"} and card_domains_written(ex) == {"recon"}
    assert "fa: fa_transactions_by_type: no periods with data" in final_run_row(ex)["r0_error_message"]


def failing_net_amount(sql: str):
    if "sum(reporting_amount)" in sql.lower():
        raise ValueError("[UNRESOLVED_COLUMN.WITH_SUGGESTION] A column with name `REPORTING_AMOUNT` cannot be resolved.")
    return summary_responder(sql)


async def test_partly_processed_domain_keeps_its_previous_cards(kb):
    ex = SummaryExecutor()
    result, _ = await run(kb, store=SummaryStore(ex), dry_run=False, responder=failing_net_amount)
    # subledger: lines_by_source worked, net_amount failed -> partly processed -> nothing saved or superseded
    assert result.status == "partial" and result.domains == {"recon": "complete", "subledger": "incomplete"}
    assert set(card_batches(ex)) == {"recon"} and card_domains_written(ex) == {"recon"}
    assert result.held_cards and all(c["domain"] == "subledger" for c in result.held_cards)
    assert all(c["domain"] == "recon" for c in result.cards)
    row = final_run_row(ex)
    assert row["r0_status"] == "partial" and row["r0_error_message"].startswith("subledger: subledger_net_amount")
    assert "recon" not in row["r0_error_message"]  # only failed domains are listed
    assert row["r0_cards_created"] == len(result.cards)
    assert "Not saved" in cards_markdown(result) and never_deletes(ex)


async def test_failed_card_save_does_not_supersede_and_marks_partial(kb):
    ex = SummaryExecutor(fail_domain="recon")
    result, _ = await run(kb, store=SummaryStore(ex), dry_run=False)
    assert result.domains == {"recon": "incomplete", "subledger": "complete"} and result.status == "partial"
    assert set(card_batches(ex)) == {"subledger"}  # the recon MERGE + UPDATE batch never ran
    assert "recon: saving cards failed" in final_run_row(ex)["r0_error_message"]


async def test_all_domains_failed_is_failed_supersedes_nothing_and_summarises_errors(kb):
    long_msg = "[TABLE_OR_VIEW_NOT_FOUND] " + "x" * 500

    def broken(sql: str):
        if "as scope" in sql.lower() or "concat('fy'" in sql.lower() or "month_start" in sql.lower():
            raise ValueError(long_msg)
        return summary_responder(sql)

    ex = SummaryExecutor()
    result, _ = await run(kb, store=SummaryStore(ex), dry_run=False, responder=broken, domains=("recon", "subledger", "fa"))
    assert result.status == "failed" and result.domains == {"recon": "incomplete", "subledger": "incomplete", "fa": "incomplete"}
    assert result.cards == [] and card_batches(ex) == {}
    assert not any("finance_chat_summary_cards" in sql for sql, _ in ex.statements)  # no card MERGE, no supersede
    row = final_run_row(ex)
    assert row["r0_status"] == "failed" and row["r0_cards_created"] == 0
    msg = row["r0_error_message"]
    parts = msg.split("; ")
    assert [p.split(":")[0] for p in parts] == ["recon", "subledger", "fa"]  # one short line per domain
    assert parts[0].endswith("(+2 more)")  # recon has three metrics on the same failing period set
    assert all(len(p) <= 200 for p in parts) and "xxxxx" * 40 not in msg
    assert never_deletes(ex)


def test_error_summary():
    from finchat_agents.summary.pipeline import error_summary

    assert error_summary({}) is None and error_summary({"recon": []}) is None
    assert error_summary({"recon": ["a  b\nc", "d"], "fa": ["e"]}) == "recon: a b c (+1 more); fa: e"
    assert len(error_summary({"recon": ["y" * 999]})) == len("recon: ") + 160


async def test_single_domain_run_only_touches_that_domain(kb):
    ex = SummaryExecutor()
    result, server = await run(kb, store=SummaryStore(ex), dry_run=False, domains=("subledger",))
    assert result.status == "succeeded" and result.domains == {"subledger": "complete"}
    assert set(card_batches(ex)) == {"subledger"} and card_domains_written(ex) == {"subledger"}
    assert all(c["domain"] == "subledger" for c in result.cards)
    assert not any("adra_" in q.lower() for q in server.queries)  # recon data is not even read
    assert final_run_row(ex)["r0_domains_0"] == "subledger"


async def test_unknown_domain_is_incomplete_and_supersedes_nothing(kb):
    ex = SummaryExecutor()
    result, _ = await run(kb, store=SummaryStore(ex), dry_run=False, domains=("recn",))
    assert result.status == "failed" and result.domains == {"recn": "incomplete"} and card_batches(ex) == {}
    assert "no metrics configured" in result.errors[0]


async def test_dry_run_with_failures_writes_nothing(kb):
    result, server = await run(kb, store=None, dry_run=True, responder=failing_net_amount)
    assert result.status == "partial" and result.domains["subledger"] == "incomplete"
    assert not any(q.lower().lstrip().startswith(("merge", "update", "insert", "delete")) for q in server.queries)


# ---------------------------------------------------------------- GET /v3/cards

CARD_ROWS = [{"card_id": "1", "domain": "recon", "rank": 1, "title": "Recon", "current_value": Decimal("17")},
             {"card_id": "2", "domain": "subledger", "rank": 1, "title": "Fynapse", "current_value": Decimal("433")}]
ACCESS = AccessConfig({
    "domains": {"recon": "ADRA", "subledger": "Fynapse", "fa": "FA"},
    "roles": {"finance_all": {"domains": ["*"]}, "recon_reader": {"domains": ["recon"]}},
    "users": {"cfo": "finance_all", "recon-user": "recon_reader"},
})


def cards_client(ex) -> httpx.AsyncClient:
    from types import SimpleNamespace

    service = SimpleNamespace(access=ACCESS, store=AiopsStore(ex) if ex else None)
    app = FastAPI()
    app.include_router(create_router(service), prefix="/v3")
    return httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://t")


async def test_cards_are_filtered_by_role():
    ex = SummaryExecutor(cards=CARD_ROWS)
    async with cards_client(ex) as c:
        recon = (await c.get("/v3/cards", params={"user_id": "recon-user"})).json()["cards"]
        assert [x["card_id"] for x in recon] == ["1"]  # the subledger row is dropped in code even if the query returned it
        sql, params = ex.queries[-1]
        assert "domain IN (CAST(:d0 AS STRING))" in sql and params == {"d0": "recon"} and "investigator_sql" not in sql
        everything = (await c.get("/v3/cards", params={"user_id": "cfo"})).json()["cards"]
        assert {x["domain"] for x in everything} == {"recon", "subledger"} and "domain IN" not in ex.queries[-1][0]
        assert everything[0]["current_value"] == "17"
        assert (await c.get("/v3/cards", params={"user_id": "nobody"})).json() == {"cards": []}
        assert (await c.get("/v3/cards")).status_code == 401
    async with cards_client(None) as c:
        assert (await c.get("/v3/cards", params={"user_id": "cfo"})).status_code == 503
