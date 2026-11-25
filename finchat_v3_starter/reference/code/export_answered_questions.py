"""Export the ADRA and Fynapse questions Finance Chat currently answers correctly to Excel.

Reads the silver golden reports (tests/golden/reports/golden_silver_dev_*.json) and the golden
question files (tests/golden/silver/*.yaml). For every question it keeps the LATEST run result,
and writes only the questions whose latest result is correct:

  - ADRA business questions (close_recon.yaml, cr_*)          -> "Business ground truth"
  - ADRA generated questions (question_bank_adra_*.yaml, qb_a*) -> "Generated, SQL-verified"
  - Fynapse business question (dev_cross_domain_v1.yaml, dev_xdom_10)
  - Fynapse generated questions (question_bank_fynapse.yaml, qb_f*)

Privacy: answers produced for the PII-viewer role are NOT exported (they can contain person names);
the standard-role variant of the same question is used instead. Hold-out questions are never read.

Usage (from backend):
  python finance_intelligence\\scripts\\export_answered_questions.py
  python finance_intelligence\\scripts\\export_answered_questions.py --out answered_questions.xlsx --include-pending

Requires: pip install openpyxl pyyaml
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parents[1]  # finance_intelligence/
DEFAULT_REPORTS = ROOT / "tests" / "golden" / "reports"
DEFAULT_GOLDEN = ROOT / "tests" / "golden" / "silver"

BUSINESS_FILES = {"close_recon.yaml": "adra", "dev_cross_domain_v1.yaml": None}
BANK_FILES = {"question_bank_adra_part1.yaml": "adra", "question_bank_adra_part2.yaml": "adra",
              "question_bank_fynapse.yaml": "fynapse", "questions_bank_adra_part1.yaml": "adra",
              "questions_bank_adra_part2.yaml": "adra", "questions_bank_fynapse.yaml": "fynapse"}
BUSINESS_FYNAPSE_IDS = {"dev_xdom_10"}
PII_ROLES = {"pii_viewer"}
CORRECT = {"pass", "correct"}

PATTERN_LABELS = {
    "lookup_value": "Single value lookup", "lookup_status": "Status lookup", "lookup_flag": "Yes/no lookup",
    "count_by_group": "Count by category", "count_filtered": "Count with condition", "share_of_total": "Share / percentage",
    "sum_total": "Total", "top_n": "Top N", "count_by_dimension": "Count by attribute", "sum_by_dimension": "Total by attribute",
    "count_lookup": "Count for one item", "sum_lookup": "Total for one item", "max_value": "Maximum", "not_found": "Not found handling",
    "not_found_or_no_access": "Not found / no access handling", "pii_masking": "Person data (masked)",
    "compare_periods": "Period comparison", "count_and_sum_by_group": "Count and total by category",
    "count_by_group_filtered": "Count by category with filter", "count_distinct": "Distinct count",
    "top_n_by_count": "Top N by count", "sum_by_group": "Total by category",
}


@dataclass
class Question:
    id: str
    domain: str
    source: str  # Business ground truth | Generated, SQL-verified
    question: str
    expected: str = ""
    category: str = ""


@dataclass
class Result:
    id: str
    role: str
    status: str  # normalised: correct / safe_refusal / wrong_answer / error / deferred / fail
    answer: str
    latency_s: float | None
    report: str
    run_time: str
    raw: dict[str, Any] = field(default_factory=dict)


# ----------------------------------------------------------------------------- golden questions
def _numbers_text(expect: dict[str, Any]) -> str:
    if not isinstance(expect, dict):
        return ""
    if expect.get("numbers"):
        return "Expected figures: " + ", ".join(str(n) for n in expect["numbers"])
    if expect.get("values") and isinstance(expect["values"], dict):
        return ", ".join(f"{k}: {v}" for k, v in expect["values"].items())
    parts = []
    if expect.get("text_contains"):
        parts.append("Contains: " + ", ".join(map(str, expect["text_contains"])))
    if expect.get("kind") and not parts:
        k = expect["kind"]
        parts.append("Expected outcome: " + (", ".join(k) if isinstance(k, list) else str(k)))
    return "; ".join(parts)


def load_questions(golden_dir: Path) -> dict[str, Question]:
    qs: dict[str, Question] = {}
    for p in sorted(golden_dir.glob("*.yaml")):
        name = p.name
        if "holdout" in name.lower():
            continue  # never read the hold-out set
        if name not in BUSINESS_FILES and name not in BANK_FILES:
            continue
        doc = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        for q in doc.get("questions", []) or []:
            qid = q.get("id")
            if not qid:
                continue
            if name == "dev_cross_domain_v1.yaml":
                if qid not in BUSINESS_FYNAPSE_IDS:
                    continue
                domain, source = "fynapse", "Business ground truth"
            elif name in BUSINESS_FILES:
                domain, source = BUSINESS_FILES[name], "Business ground truth"
            else:
                domain, source = BANK_FILES[name], "Generated, SQL-verified"
            expect = q.get("expect") or {}
            expected = q.get("expected_text") or _numbers_text(expect)
            roles = (expect.get("as_role") if isinstance(expect, dict) else None) or q.get("as_role")
            if not expected and roles:
                std = roles.get("standard") or next(iter(roles.values()))
                expected = _numbers_text(std)
                if std.get("check") == "person_names_masked":
                    expected = "Person names masked for users without PII permission"
            category = (q.get("category") or PATTERN_LABELS.get(q.get("pattern", ""), q.get("pattern", ""))
                        or "Business question")
            qs[qid] = Question(qid, domain, source, str(q.get("question", "")).strip(), str(expected).strip(), category)
            for i, para in enumerate(q.get("paraphrases") or [], start=1):
                pid = f"{qid}~p{i}"
                qs[pid] = Question(pid, domain, source, str(para).strip(), str(expected).strip(), category)
    return qs


# ----------------------------------------------------------------------------- reports
def _status(r: dict[str, Any]) -> str:
    c = (r.get("classification") or "").lower()
    if c:
        return c
    o = (r.get("outcome") or "").lower()
    return {"pass": "correct", "fail": "fail", "deferred": "deferred"}.get(o, o or "unknown")


def _fmt_value(v: Any) -> str:
    if isinstance(v, float):
        return f"{v:,.2f}"
    if isinstance(v, int) and not isinstance(v, bool):
        return f"{v:,}"
    return str(v)


def _answer_text(r: dict[str, Any]) -> str:
    actual = r.get("actual")
    if isinstance(actual, dict):
        if actual.get("answer"):
            return str(actual["answer"]).strip()
        table = actual.get("table")
        if isinstance(table, dict) and table.get("rows"):
            return _table_text(table)
    for key in ("answer_text", "answer", "message"):
        if r.get(key):
            return str(r[key]).strip()
    aa = r.get("actual_answer")
    if isinstance(aa, dict) and aa:
        return "; ".join(f"{k.replace('_', ' ')}: {_fmt_value(v)}" for k, v in aa.items())
    return ""


def _table_text(table: dict[str, Any], max_rows: int = 12) -> str:
    cols = table.get("columns") or []
    keys = [c.get("key") if isinstance(c, dict) else c for c in cols]
    labels = {(c.get("key") if isinstance(c, dict) else c): (c.get("label") if isinstance(c, dict) else c) for c in cols}
    lines = []
    for row in (table.get("rows") or [])[:max_rows]:
        if isinstance(row, dict):
            lines.append(", ".join(f"{labels.get(k, k)}: {row.get(k)}" for k in keys if k in row))
        else:
            lines.append(", ".join(f"{labels.get(k, k)}: {v}" for k, v in zip(keys, row)))
    return "\n".join(lines)


def _report_time(path: Path, doc: dict[str, Any]) -> str:
    m = re.search(r"(\d{8})_(\d{6})", path.name)
    if m:
        return datetime.strptime(m.group(1) + m.group(2), "%Y%m%d%H%M%S").isoformat(sep=" ")
    return datetime.fromtimestamp(path.stat().st_mtime).isoformat(sep=" ", timespec="seconds")


def load_latest_results(report_dir: Path) -> dict[tuple[str, str], Result]:
    latest: dict[tuple[str, str], Result] = {}
    files = sorted(report_dir.glob("golden_silver_*.json"), key=lambda p: (_report_time(p, {}), p.name))
    for p in files:
        try:
            doc = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            print(f"skip {p.name}: {e}", file=sys.stderr)
            continue
        when = _report_time(p, doc)
        for r in doc.get("results", []) or []:
            rid = r.get("id")
            if not rid:
                continue
            role = r.get("role") or "default"
            st = _status(r)
            if st == "deferred":
                continue  # a deferred run says nothing about the answer; keep earlier real results
            lat = r.get("latency_ms") or r.get("elapsed_ms")
            latest[(rid, role)] = Result(rid, role, st, _answer_text(r),
                                         round(float(lat) / 1000, 1) if lat else None, p.name, when, r)
    return latest


# ----------------------------------------------------------------------------- excel
HEADERS = ["#", "Domain", "Source", "Category", "Question", "Finance Chat answer", "Expected answer (ground truth)",
           "Result", "Response time (s)", "Tested on", "Question id"]
WIDTHS = [5, 10, 22, 26, 55, 70, 60, 12, 12, 19, 34]
HEAD_FILL = PatternFill("solid", fgColor="1F3864")
OK_FILL = PatternFill("solid", fgColor="E2EFDA")


def _sheet(ws, rows: list[list[Any]]) -> None:
    ws.append(HEADERS)
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = HEAD_FILL
        c.alignment = Alignment(wrap_text=True, vertical="center")
    for r in rows:
        ws.append(r)
    for i, w in enumerate(WIDTHS, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
        if row[7].value == "Correct":
            row[7].fill = OK_FILL
    ws.freeze_panes = "E2"
    ws.auto_filter.ref = ws.dimensions


def pick_result(qid: str, results: dict[tuple[str, str], Result]) -> Result | None:
    """Prefer a non-PII role; never export a PII-viewer answer."""
    cands = [r for (rid, role), r in results.items() if rid == qid and role not in PII_ROLES]
    if not cands:
        return None
    return sorted(cands, key=lambda r: (r.status in CORRECT, r.run_time), reverse=True)[0]


def build(questions: dict[str, Question], results: dict[tuple[str, str], Result], include_pending: bool):
    answered: dict[str, list[list[Any]]] = {"adra": [], "fynapse": []}
    pending: list[list[Any]] = []
    stats: dict[str, dict[str, int]] = {}

    def order(q: Question):
        return (0 if q.source.startswith("Business") else 1, q.id)

    for q in sorted(questions.values(), key=order):
        r = pick_result(q.id, results)
        s = stats.setdefault(f"{q.domain}|{q.source}", {"tested": 0, "correct": 0})
        if r is None:
            continue
        s["tested"] += 1
        row = [None, "ADRA" if q.domain == "adra" else "Fynapse", q.source, q.category, q.question,
               r.answer, q.expected, "Correct" if r.status in CORRECT else r.status.replace("_", " ").title(),
               r.latency_s, r.run_time, q.id]
        if r.status in CORRECT:
            s["correct"] += 1
            answered[q.domain].append(row)
        elif include_pending:
            pending.append(row)
    for rows in list(answered.values()) + [pending]:
        for i, row in enumerate(rows, start=1):
            row[0] = i
    return answered, pending, stats


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--reports", type=Path, default=DEFAULT_REPORTS)
    ap.add_argument("--golden", type=Path, default=DEFAULT_GOLDEN)
    ap.add_argument("--out", type=Path, default=Path(f"FinanceChat_answered_questions_{datetime.now():%Y%m%d}.xlsx"))
    ap.add_argument("--include-pending", action="store_true",
                    help="add an internal sheet with questions not yet answered correctly (do not send to business)")
    args = ap.parse_args()

    questions = load_questions(args.golden)
    if not questions:
        print(f"No golden questions found in {args.golden}", file=sys.stderr)
        return 1
    results = load_latest_results(args.reports)
    if not results:
        print(f"No golden_silver reports found in {args.reports}", file=sys.stderr)
        return 1
    answered, pending, stats = build(questions, results, args.include_pending)

    wb = Workbook()
    ws = wb.active
    ws.title = "Summary"
    ws.append(["Finance Chat - questions answered correctly"])
    ws["A1"].font = Font(bold=True, size=14)
    ws.append([f"Generated {datetime.now():%Y-%m-%d %H:%M} from the latest automated test run of each question."])
    ws.append(["Answers are checked against verified ground truth (business answers, or SQL run on Databricks)."])
    ws.append(["Answers come from the semantic (silver) layer and are labelled Unverified in the app."])
    ws.append([])
    ws.append(["Domain", "Source", "Tested", "Answered correctly"])
    for c in ws[6]:
        c.font = Font(bold=True)
    for key, s in sorted(stats.items()):
        dom, src = key.split("|")
        ws.append(["ADRA" if dom == "adra" else "Fynapse", src, s["tested"], s["correct"]])
    for col, w in zip("ABCD", (12, 26, 10, 20)):
        ws.column_dimensions[col].width = w
    _sheet(wb.create_sheet("ADRA"), answered["adra"])
    _sheet(wb.create_sheet("Fynapse"), answered["fynapse"])
    if args.include_pending:
        _sheet(wb.create_sheet("INTERNAL - not yet correct"), pending)
    wb.save(args.out)

    print(f"Wrote {args.out}")
    for key, s in sorted(stats.items()):
        print(f"  {key.replace('|', ' / ')}: {s['correct']} correct of {s['tested']} tested")
    missing = [q.id for q in questions.values() if pick_result(q.id, results) is None]
    if missing:
        print(f"  not found in any report (not exported): {len(missing)} e.g. {missing[:5]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
