from __future__ import annotations

from types import SimpleNamespace

import pytest

from finchat_agents.eval.scorecard import BANK_DIR, BANKS, CaseResult, run_case, summarize, to_markdown
from finchat_agents.eval.scoring import EvalCase, Score, load_cases, score


def case(expect, q="What is the balance of account 141111 for 100-Northwind in Feb 25?"):
    return EvalCase(id="c1", question=q, expect=expect)


def test_load_cases_with_paraphrases():
    paths = [BANK_DIR / f for b in ("adra", "fynapse") for f in BANKS[b]]
    cases = load_cases(paths)
    main = [c for c in cases if not c.paraphrase_of]
    assert len(main) == 41 and len(cases) > len(main)
    pii = next(c for c in cases if c.id == "qb_a22_pii_lookup")
    assert "pii_restricted" in pii.expect["kind"]
    assert len(load_cases(paths, include_paraphrases=False)) == 41


def test_numbers_correct_partial_wrong_could_not_answer():
    c = case({"kind": "answer", "numbers": ["1981646.00"], "tolerance_pct": 0.5})
    assert score(c, "answered", "The balance is 1,981,646.").category == "correct"
    assert score(c, "answered", "The balance is about 1.98 million.").category == "correct"  # within 0.5%
    assert score(c, "answered", "The balance is 2,500,000.").category == "wrong"
    assert score(c, "partial", "I could not find the balance.").category == "could_not_answer"
    assert score(c, "failed", "").category == "error"
    multi = case({"kind": "answer", "numbers": ["7", "24", "9"], "text_contains": ["Approved"]})
    assert score(multi, "answered", "Approved 7, Not prepared 24").category == "partial"
    tbl = [{"title": "t", "columns": ["s", "n"], "rows": [["Approved", 7], ["Not prepared", 24], ["Prepared", 9]]}]
    assert score(multi, "answered", "Three statuses.", tbl).category == "correct"  # tables count as answer


def test_text_expectations():
    c = case({"kind": "answer", "text_contains": ["Not prepared"]})
    assert score(c, "answered", "Account 213130 is Not prepared.").category == "correct"
    assert score(c, "answered", "Account 213130 is Approved.").category == "wrong"
    assert score(c, "answered", "I could not find account 213130.").category == "could_not_answer"
    anyc = case({"kind": "answer", "text_contains_any": ["not finalized", "No", "False"]})
    assert score(anyc, "answered", "No, it is not finalized.").category == "correct"


def test_not_found_and_cannot_compare():
    c = case({"kind": "not_found"}, q="What is the balance of account 141111 for 100-Northwind in March 2023?")
    assert score(c, "answered", "There is no data for March 2023 for 100-Northwind; data exists for Feb 25.").category == "correct"
    assert score(c, "answered", "The balance in March 2023 was 1,981,646.").category == "wrong"
    cmp_ = case({"kind": "cannot_compare"})
    assert score(cmp_, "partial", "Jan 25 has no data, so the change cannot be compared.").category == "correct"


def test_pii_cases():
    c = case({"kind": ["pii_restricted", "answer"]})
    assert score(c, "answered", "The preparer's name is masked for your role.").category == "correct"
    assert score(c, "answered", "Account 213130 has not been approved yet.").category == "correct"
    assert score(c, "answered", "It was prepared on 25 Oct.").category == "partial"


def test_clarify_accepted():
    c = case({"kind": ["answer", "clarify"], "numbers": ["0"]})
    assert score(c, "clarification", "Do you mean lines with REVERSES populated?").category == "correct"


class FakeOrch:
    def __init__(self, answer):
        self._answer = answer

    async def answer(self, question, user, extra_sinks=None):
        debug = SimpleNamespace(mode="fast", latency_ms=1234.0, llm_calls=3, sql_calls=1, sql=["SELECT 1"])
        return SimpleNamespace(status="answered", answer=self._answer, tables=[], how_calculated="h", debug=debug)


async def test_run_case_summary_and_markdown(tmp_path):
    c = case({"kind": "answer", "numbers": ["1981646.00"]})
    good = await run_case(FakeOrch("Balance 1,981,646."), None, c, tmp_path)
    bad = await run_case(FakeOrch("Balance 5."), None, c.model_copy(update={"id": "c2"}), tmp_path)
    assert good.score.category == "correct" and good.latency_s == 1.23 and good.mode == "fast"
    s = summarize([good, bad])
    assert s["categories"]["correct"] == 1 and s["categories"]["wrong"] == 1
    assert s["by_mode"]["fast"]["avg_llm_calls"] == 3
    md = to_markdown([good, bad], s, "Test")
    assert "**wrong 1**" in md and "### c2 (wrong)" in md and "SELECT 1" in md


def test_consistency():
    sc = Score(category="correct", found_numbers=["1"])
    base = dict(status="answered", mode="fast", latency_s=1, llm_calls=3, sql_calls=1, answer="a")
    r1 = CaseResult(case=case({}), score=sc, run=1, **base)
    r2 = CaseResult(case=case({}), score=Score(category="wrong"), run=2, **base)
    assert summarize([r1, r2])["consistency"] == {"c1": False}
