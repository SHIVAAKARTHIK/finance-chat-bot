"""Scheduled summary agent. Cron on the VM calls (default schedule daily 07:00 IST, to be confirmed):

    cd backend
    .venv\\Scripts\\python -m finchat_agents.summary.run [--domain recon --domain subledger] [--dry-run] [--trigger schedule]

--dry-run prints the cards and writes nothing. A real run needs finance_chat_summary_runs / finance_chat_summary_cards
(Karthik creates them); if they are missing it stops with a clear message.
"""
from __future__ import annotations

import argparse
import asyncio
import sys

from ..config import get_settings


async def main_async(args: argparse.Namespace) -> int:
    from ..access.rbac import AccessConfig
    from ..agents.specialists import build_sql_agent
    from ..guardrails import load_from_settings
    from ..knowledge.loader import Knowledge
    from ..llm.factory import response_model, sql_model
    from ..storage.aiops import build_store
    from ..storage.summary_store import SummaryStore, SummaryTablesMissing
    from ..tools import DataDeps, TTLCache, build_data_tools, build_mcp_client
    from .cards import CardWriter
    from .facts import load_config
    from .pipeline import cards_markdown, run_summary

    s = get_settings()
    cfg = load_config(s.resolve_path(s.summary_metrics_file))
    kb = Knowledge.load()
    deps = DataDeps(kb=kb, mcp=build_mcp_client(s), settings=s, cache=TTLCache(s.column_values_cache_seconds),
                    guardrails=load_from_settings(s))
    access = AccessConfig.load(s.resolve_path(s.rbac_file)).service_access()
    if not access.has_access:
        print("The access file has no service_role; the summary agent cannot read data.", file=sys.stderr)
        return 2
    base = None if args.dry_run else build_store(s)
    store = SummaryStore.from_store(base) if base else None
    sql_agent = build_sql_agent(sql_model(s), build_data_tools(deps), kb)
    try:
        result = await run_summary(cfg=cfg, deps=deps, sql_agent=sql_agent, card_writer=CardWriter(response_model(s)),
                                   access=access, store=store, domains=args.domain or None, dry_run=args.dry_run,
                                   trigger=args.trigger)
    except SummaryTablesMissing as exc:
        print(str(exc), file=sys.stderr)
        return 3
    print(cards_markdown(result))
    return 0 if result.status != "failed" else 1


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--domain", action="append", help="limit to these domains (repeatable)")
    ap.add_argument("--dry-run", action="store_true", help="print cards, write nothing")
    ap.add_argument("--trigger", choices=["schedule", "manual"], default="manual")
    raise SystemExit(asyncio.run(main_async(ap.parse_args())))


if __name__ == "__main__":
    main()
