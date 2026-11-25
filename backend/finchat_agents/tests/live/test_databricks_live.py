"""Live Databricks checks through the MCP server. Run only with RUN_LIVE=1 and the service principal in backend/.env:

    $env:RUN_LIVE="1"; ..\\.venv\\Scripts\\python -m pytest tests/live/test_databricks_live.py -v -s
"""
from __future__ import annotations

import os
from decimal import Decimal

import pytest

from finchat_agents.access import Role, UserAccess
from finchat_agents.config import Settings
from finchat_agents.knowledge.loader import Knowledge
from finchat_agents.tools import DataDeps, TTLCache, build_mcp_client, warm_up
from finchat_agents.tools.catalog import column_values
from finchat_agents.tools.run_sql import execute_guarded

pytestmark = [pytest.mark.live, pytest.mark.skipif(os.getenv("RUN_LIVE") != "1", reason="live test: set RUN_LIVE=1")]

ALL = UserAccess(user_id="live-test", role=Role(name="finance_all", domains=["*"]))
KB = Knowledge.load()
EXAMPLES_WITH_NUMBERS = [e for e in KB.examples if e.expected and e.expected.get("numbers")]


@pytest.fixture
async def deps():
    s = Settings()
    client = build_mcp_client(s)
    yield DataDeps(kb=KB, mcp=client, settings=s, cache=TTLCache(60))
    await client.aclose()


async def test_warm_up(deps):
    assert (await warm_up(deps))["mcp"] == "ok"


async def test_adra_account_facts_count_is_97(deps):
    r = await execute_guarded("SELECT COUNT(*) AS n FROM lakehouse_mvpai.silver.adra_account_facts", deps, ALL)
    assert r.rows == [[97]]


async def test_fynapse_entity_values(deps):
    out = await column_values(deps, ALL, "fact_fynapse_slr_journals", "PARENT_ENTITY")
    print("\nFynapse PARENT_ENTITY values now:", out["values"])
    assert out["values"], "PARENT_ENTITY returned no values"


async def test_adra_entity_codes_used_by_examples(deps):
    out = await column_values(deps, ALL, "adra_legal_entity_dimensions", "ENTITY_CODE")
    codes = {str(v["value"]).strip() for v in out["values"]}
    print("\nADRA ENTITY_CODE values:", sorted(codes))
    assert {"100", "561"} <= codes


def _numbers(rows) -> list[float]:
    out = []
    for r in rows:
        for v in r:
            if isinstance(v, (int, float, Decimal)) and not isinstance(v, bool):
                out.append(float(v))
            else:
                try:
                    out.append(float(str(v)))
                except (TypeError, ValueError):
                    pass
    return out


@pytest.mark.parametrize("example", EXAMPLES_WITH_NUMBERS, ids=[e.id for e in EXAMPLES_WITH_NUMBERS])
async def test_example_sql_returns_expected_numbers(deps, example):
    r = await execute_guarded(example.sql, deps, ALL)
    got = _numbers(r.rows)
    missing = []
    for want in example.expected["numbers"]:
        w = float(str(want).rstrip("%").replace(",", ""))
        tol = max(abs(w) * 0.005, 0.011)
        if not any(abs(g - w) <= tol for g in got):
            missing.append(want)
    assert not missing, f"{example.id}: expected {missing} not in result {r.rows[:10]}"
