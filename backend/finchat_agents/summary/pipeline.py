"""Summary agent pipeline (Dhivya's design, plain Python):

collect facts (config SQL via run_sql, service role) -> rank / select (code) -> card text (gpt-oss, number check)
-> flagged big change? -> investigator (v3 SQL agent, max 2 queries) -> explanation on the key-change card
-> one run row + cards (MERGE) + supersede older cards. --dry-run writes nothing.

Each domain is processed on its own. A domain that finishes without errors saves its cards and supersedes ALL its
older active cards (any metric). A domain that fails or is only partly processed saves nothing new and keeps its
previous active cards. Run status: `succeeded` when every domain completed, `partial` when at least one completed and
at least one failed, `failed` when none completed (nothing is superseded then). error_message holds one short line
per failed domain. `--domain X` touches
only domain X. Cards are never deleted: superseded rows stay as history.
"""
from __future__ import annotations

import datetime as dt
import uuid
from typing import Any, Literal

from pydantic import BaseModel, Field

from ..access.rbac import UserAccess
from ..runtime.agent import Agent
from ..runtime.tools import Budget, RunContext
from ..storage.summary_store import SummaryStore
from ..storage.trace_sink import AiopsTraceSink
from ..storage.writer import BackgroundWriter
from ..tools.deps import DataDeps
from ..tracing.sinks import TraceSink
from ..tracing.tracer import Tracer
from .cards import CardWriter, investigate
from .facts import Fact, SummaryConfig, collect_facts, rank_and_select


class SummaryResult(BaseModel):
    run_id: str
    status: Literal["succeeded", "partial", "failed"] = "succeeded"
    cards: list[dict[str, Any]] = Field(default_factory=list)  # cards of completed domains (saved in a real run)
    held_cards: list[dict[str, Any]] = Field(default_factory=list)  # cards of incomplete domains (never saved)
    domains: dict[str, Literal["complete", "incomplete"]] = Field(default_factory=dict)
    facts_collected: int = 0
    errors: list[str] = Field(default_factory=list)  # every error, "<domain>: <error>" (CLI output)
    domain_errors: dict[str, list[str]] = Field(default_factory=dict)
    dry_run: bool = False


def _now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def card_row(f: Fact, title: str, text: str, run_id: str, *, explanation: str | None, explanation_status: str,
             investigator_sql: list[str], now: dt.datetime) -> dict[str, Any]:
    return {
        "card_id": str(uuid.uuid4()), "run_id": run_id, "domain": f.domain, "card_type": f.card_type, "rank": f.rank,
        "period_label": f.period_label, "comparison_label": f.comparison_label, "metric_name": f.metric_name,
        "source_tables": f.source_tables or None, "current_value": f.current_value, "previous_value": f.previous_value,
        "change_abs": f.change_abs, "change_pct": f.change_pct, "is_flagged": f.flagged, "title": title,
        "card_text": text, "explanation": explanation, "explanation_status": explanation_status,
        "investigator_sql": investigator_sql or None, "status": "active", "created_at": now,
    }


async def run_summary(
    *,
    cfg: SummaryConfig,
    deps: DataDeps,
    sql_agent: Agent,
    card_writer: CardWriter,
    access: UserAccess,
    store: SummaryStore | None,
    domains: list[str] | None = None,
    dry_run: bool = False,
    trigger: Literal["schedule", "manual"] = "manual",
    sinks: list[TraceSink] | None = None,
) -> SummaryResult:
    run_id = str(uuid.uuid4())
    result = SummaryResult(run_id=run_id, dry_run=dry_run)
    started = _now()
    if not dry_run:
        if store is None:
            raise RuntimeError("storage is not configured (DATABRICKS_SERVER_HOSTNAME, DATABRICKS_HTTP_PATH); use --dry-run")
        await store.check_tables()  # stops with a clear message if Karthik has not created the tables yet
    writer = BackgroundWriter() if not dry_run else None
    trace_sinks: list[TraceSink] = list(sinks or [])
    aiops_sink = AiopsTraceSink(store.base, writer, conversation_id=run_id) if store and writer else None
    if aiops_sink:
        trace_sinks.append(aiops_sink)
    tracer = Tracer(trace_sinks, run_id=run_id, message_id=run_id)  # events are keyed by the job run id
    ctx = RunContext(tracer=tracer, budget=Budget(max_seconds=1800), user=access)
    run_domains = list(dict.fromkeys(domains or cfg.domains))  # --domain X: only X is read, written or superseded

    def run_row(status: str, **extra: Any) -> dict[str, Any]:
        return {"run_id": run_id, "trigger_type": trigger, "status": status, "domains": run_domains,
                "cards_created": extra.get("cards", 0), "cards_flagged": extra.get("flagged", 0),
                "llm_call_count": ctx.counters.llm_calls, "input_tokens": ctx.counters.input_tokens,
                "output_tokens": ctx.counters.output_tokens, "error_message": extra.get("error"),
                "started_at": started, "completed_at": extra.get("completed")}

    async def run_domain(domain: str) -> None:
        errors: list[str] = []
        cards: list[dict[str, Any]] = []
        if not any(m.domain == domain for m in cfg.metrics):
            errors.append("no metrics configured for this domain")
        else:
            try:
                facts = await collect_facts(cfg, deps, access, [domain], errors)
                result.facts_collected += len(facts)
                selected = rank_and_select(facts, cfg)
                texts = await card_writer.write(selected, ctx)
                now = _now()
                for f in selected:
                    text = texts[f.fact_id]
                    explanation, status, sql = None, "not_flagged", []
                    if f.flagged:
                        inv = await investigate(sql_agent, f, access, tracer)
                        explanation, status, sql = inv.explanation, inv.status, inv.sql
                    cards.append(card_row(f, text.title, text.card_text, run_id, explanation=explanation,
                                          explanation_status=status, investigator_sql=sql, now=now))
            except Exception as exc:  # noqa: BLE001 - one domain failing must not stop the others
                errors.append(f"{type(exc).__name__}: {str(exc)[:300]}")
        if not errors and store and not dry_run:
            try:
                await store.save_domain(domain, cards, run_id)
            except Exception as exc:  # noqa: BLE001
                errors.append(f"saving cards failed: {type(exc).__name__}: {str(exc)[:300]}")
        if errors:
            result.domains[domain] = "incomplete"
            result.held_cards += cards
            result.errors += [f"{domain}: {e}" for e in errors]
            result.domain_errors[domain] = errors
        else:
            result.domains[domain] = "complete"
            result.cards += cards

    if store and not dry_run:
        await store.upsert_run(run_row("running"))
    try:
        for domain in run_domains:
            await run_domain(domain)
        complete = sum(1 for v in result.domains.values() if v == "complete")
        result.status = "succeeded" if complete == len(run_domains) else ("partial" if complete else "failed")
    except Exception as exc:
        result.status = "failed"
        result.errors.append(f"{type(exc).__name__}: {str(exc)[:300]}")
        result.domain_errors.setdefault("run", []).append(f"{type(exc).__name__}: {str(exc)[:300]}")
    finally:
        await tracer.emit("answer", agent="summary_agent", payload={"run_id": run_id, "status": result.status,
                                                                     "cards": len(result.cards), "domains": result.domains,
                                                                     "errors": result.errors[:5]})
        if store and not dry_run:
            flagged = sum(1 for c in result.cards if c["is_flagged"])
            await store.upsert_run(run_row(result.status, cards=len(result.cards), flagged=flagged, completed=_now(),
                                           error=error_summary(result.domain_errors)))
        if writer:
            await writer.stop(timeout=120)
    return result


ERROR_LINE_CHARS = 160


def error_summary(domain_errors: dict[str, list[str]]) -> str | None:
    """One short line per failed domain for finance_chat_summary_runs.error_message:
    `recon: <first error, cut to 160 chars> (+2 more); subledger: ...`. None when nothing failed."""
    parts = []
    for domain, errs in domain_errors.items():
        if not errs:
            continue
        first = " ".join(errs[0].split())
        if len(first) > ERROR_LINE_CHARS:
            first = first[: ERROR_LINE_CHARS - 3].rstrip() + "..."
        parts.append(f"{domain}: {first}" + (f" (+{len(errs) - 1} more)" if len(errs) > 1 else ""))
    return "; ".join(parts)[:2000] or None


def cards_markdown(result: SummaryResult) -> str:
    lines = [f"# Summary run {result.run_id} ({'dry run' if result.dry_run else result.status})",
             f"Facts collected: {result.facts_collected}; cards: {len(result.cards)}", ""]
    for c in sorted(result.cards, key=lambda c: (c["domain"], c["rank"])):
        flag = " [flagged]" if c["is_flagged"] else ""
        lines += [f"## {c['domain']} #{c['rank']} {c['title']}{flag}", "", c["card_text"], ""]
        if c["explanation"]:
            lines += [f"Explanation ({c['explanation_status']}): {c['explanation']}", ""]
    if result.domains:
        lines.insert(2, "Domains: " + ", ".join(f"{d} {v}" for d, v in result.domains.items()))
    if result.held_cards:
        lines += [f"## Not saved ({len(result.held_cards)} cards of incomplete domains; their previous cards stay active)", ""]
    if result.errors:
        lines += ["## Errors", "", *[f"- {e}" for e in result.errors], ""]
    return "\n".join(lines)
