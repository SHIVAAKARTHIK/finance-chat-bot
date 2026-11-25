"""Score an answer against a question-bank expectation, in code (numbers with tolerance, required text).

Categories: correct, partial, could_not_answer, wrong, error. Target: zero wrong.
"""
from __future__ import annotations

import re
from decimal import Decimal
from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, Field

from ..agents.number_check import extract_numbers

Category = Literal["correct", "partial", "could_not_answer", "wrong", "error"]

NOT_FOUND_WORDS = re.compile(
    r"\b(no data|not found|could not find|couldn't find|cannot find|can't find|does not exist|doesn't exist|no record|"
    r"no rows|not available|no matching|isn't any|is no|are no|cannot compare|can't compare|cannot be compared|"
    r"no comparable|not possible to compare|not have access|no access|outside (your|their) access|not populated|"
    r"empty|no values|no value|blank|null)\b",
    re.I,
)
MASKED_WORDS = re.compile(r"\b(mask|masked|personal data|personal information|restricted|not permitted|privacy|hidden|withheld)\b", re.I)


class EvalCase(BaseModel):
    id: str
    question: str
    domain: str = ""
    expect: dict[str, Any] = Field(default_factory=dict)
    role: str = "standard"
    paraphrase_of: str | None = None


class Score(BaseModel):
    category: Category
    found_numbers: list[str] = Field(default_factory=list)
    missing_numbers: list[str] = Field(default_factory=list)
    missing_text: list[str] = Field(default_factory=list)
    note: str = ""


def load_cases(paths: list[Path], *, include_paraphrases: bool = True) -> list[EvalCase]:
    cases: list[EvalCase] = []
    for path in paths:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for q in data.get("questions", []):
            if "question" not in q:
                continue
            expect = q.get("expect")
            if expect is None and "as_role" in q:  # PII cases: score the standard (no PII) role
                expect = dict(q["as_role"].get("standard") or {})
            base = EvalCase(id=q["id"], question=q["question"], domain=q.get("domain", ""), expect=expect or {})
            cases.append(base)
            if include_paraphrases:
                for i, p in enumerate(q.get("paraphrases") or [], 1):
                    cases.append(base.model_copy(update={"id": f"{q['id']}~p{i}", "question": p, "paraphrase_of": q["id"]}))
    return cases


def _as_number(text: str) -> tuple[Decimal, bool] | None:
    t = str(text).strip()
    pct = t.endswith("%")
    try:
        return Decimal(t.rstrip("%").replace(",", "")), pct
    except Exception:
        return None


def _answer_numbers(answer: str, tables: list[dict[str, Any]]) -> list[Decimal]:
    nums = [n.value for n in extract_numbers(answer)]
    for t in tables:
        for row in t.get("rows", []):
            for cell in row:
                if isinstance(cell, (int, float)) and not isinstance(cell, bool):
                    nums.append(Decimal(str(cell)))
                elif cell is not None:
                    nums += [n.value for n in extract_numbers(str(cell))]
    return nums


def _present(expected: Decimal, got: list[Decimal], tol_pct: float) -> bool:
    for g in got:
        tol = max(abs(expected) * Decimal(str(tol_pct)) / 100, Decimal("0.005"))
        if abs(g - expected) <= tol or abs(abs(g) - abs(expected)) <= tol:
            return True
    return False


def _text(answer: str, tables: list[dict[str, Any]]) -> str:
    cells = " ".join(str(c) for t in tables for row in t.get("rows", []) for c in row)
    return f"{answer} {cells}".lower()


def _kinds(expect: dict[str, Any]) -> list[str]:
    k = expect.get("kind", "answer")
    return list(k) if isinstance(k, list) else [k]


def _unsupported_figures(answer: str, question: str) -> list[str]:
    """Numbers in the answer that are not in the question, ignoring years and small period/day numbers."""
    q = {n.value for n in extract_numbers(question)}
    out = []
    for n in extract_numbers(answer):
        v = abs(n.value)
        if n.value in q or (v == v.to_integral_value() and (v <= 31 or 1990 <= v <= 2100)):
            continue
        out.append(n.text)
    return out


def score(case: EvalCase, status: str, answer: str, tables: list[dict[str, Any]] | None = None) -> Score:
    tables = tables or []
    expect = case.expect
    kinds = _kinds(expect)
    if status == "failed":
        return Score(category="error", note="answer failed")
    if status == "clarification" and "clarify" in kinds:
        return Score(category="correct", note="clarification accepted")

    negative = {"not_found", "cannot_compare", "access_denied", "pii_restricted"}
    text = _text(answer, tables)
    if "answer" not in kinds or (set(kinds) & negative and not expect.get("numbers")):
        if "pii_restricted" in kinds:
            if MASKED_WORDS.search(text) or (expect.get("text_contains_any") and any(t.lower() in text for t in expect["text_contains_any"])):
                return Score(category="correct")
            if "answer" in kinds and re.search(r"\bnot (yet )?(been )?approved\b", text):
                return Score(category="correct", note="answered without names")
            return Score(category="partial", note="needs review: no masking wording found")
        figures = _unsupported_figures(answer, case.question)
        if figures:
            return Score(category="wrong", note=f"figures stated for a not-found / cannot-compare case: {figures}")
        if NOT_FOUND_WORDS.search(text) or status in ("declined", "partial"):
            return Score(category="correct")
        return Score(category="partial", note="needs review: no not-found wording")

    expected = [x for x in (_as_number(n) for n in expect.get("numbers", [])) if x is not None]
    tol = float(expect.get("tolerance_pct", 0.5))
    got = _answer_numbers(answer, tables)
    found = [str(e) for e, _ in expected if _present(e, got, tol)]
    missing = [str(e) for e, _ in expected if not _present(e, got, tol)]
    missing_text = [t for t in expect.get("text_contains", []) if str(t).lower() not in text]
    any_ok = True
    if expect.get("text_contains_any"):
        any_ok = any(str(t).lower() in text for t in expect["text_contains_any"])
        if not any_ok:
            missing_text.append("one of: " + ", ".join(map(str, expect["text_contains_any"])))
    if not missing and not missing_text:
        return Score(category="correct", found_numbers=found)
    text_checks = len(expect.get("text_contains", [])) + (1 if expect.get("text_contains_any") else 0)
    if found or (not expected and text_checks and len(missing_text) < text_checks):
        return Score(category="partial", found_numbers=found, missing_numbers=missing, missing_text=missing_text)
    gave_up = status in ("partial", "clarification", "declined") or NOT_FOUND_WORDS.search(text) is not None
    if gave_up or (expected and not got):
        return Score(category="could_not_answer", missing_numbers=missing, missing_text=missing_text)
    return Score(category="wrong", missing_numbers=missing, missing_text=missing_text,
                 note="the answer states a result, but not the expected one")
