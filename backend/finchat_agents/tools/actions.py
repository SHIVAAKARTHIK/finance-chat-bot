"""Actions: export_excel and save_report. Nothing is emailed, shared or sent; files land in OUTPUT_DIR/<conversation>/.

- Tables come from query results by result_id (rows built in code, never typed by the model; PII already masked).
- Report text is number-checked: every number must come from this question's results, calculations or the question.
- Idempotent: the file name is derived from the message id, the action and the title, so a retried step overwrites
  the same file instead of creating a second one.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import re
from decimal import Decimal
from pathlib import Path
from typing import Any

from ..llm.types import ToolSpec
from ..runtime.tools import RunContext, Tool, ToolContext, ToolError
from .calculate import CALC_KEY
from .run_sql import RESULTS_KEY, SqlResult

FILES_KEY = "files"  # RunContext.extras[FILES_KEY] = [{"name", "path"}]
QUESTION_KEY = "question"
CONVERSATION_KEY = "conversation_id"
MAX_ROWS_PER_TABLE = 10_000
MAX_SECTIONS = 30


def _slug(text: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_").lower()
    return (s or "export")[:60]


def _key(run: RunContext, action: str, title: str) -> str:
    base = f"{run.tracer.message_id or run.run_id}|{action}|{title.strip().lower()}"
    return hashlib.sha256(base.encode()).hexdigest()[:10]


def _folder(run: RunContext, output_dir: Path) -> Path:
    conv = str(run.extras.get(CONVERSATION_KEY) or "no_conversation")
    folder = output_dir / re.sub(r"[^A-Za-z0-9_-]", "_", conv)[:80]
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def _results(run: RunContext, ids: list[str]) -> list[tuple[str, SqlResult]]:
    store: dict[str, SqlResult] = run.extras.get(RESULTS_KEY, {})
    missing = [i for i in ids if i not in store]
    if missing:
        known = ", ".join(store) or "none yet"
        raise ToolError(f"Unknown result_id(s): {', '.join(missing)}. Results available for this question: {known}.")
    return [(i, store[i]) for i in ids]


def _cell(v: Any) -> Any:
    if isinstance(v, Decimal):
        return float(v)
    if isinstance(v, (str, int, float, bool, dt.date, dt.datetime)) or v is None:
        return v
    return str(v)


def _keep_text_as_text(wb: Any) -> None:
    """Excel formula injection: data such as `=HYPERLINK(...)` must open as text, never run as a formula. openpyxl treats
    text starting with "=" as a formula, so every text cell is marked as a string; the value itself is unchanged."""
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for cell in row:
                if isinstance(cell.value, str):
                    cell.data_type = "s"


META_SUFFIX = ".meta.json"  # owner record next to each file; the download route checks it


def download_url(conversation_folder: str, name: str) -> str:
    return f"/v3/files/{conversation_folder}/{name}"


def _register(run: RunContext, path: Path) -> dict[str, str]:
    """Remember the file for the envelope and write its owner record (who may download it)."""
    import json

    owner = getattr(run.user, "user_id", None)
    meta = {
        "user_id": owner,
        "conversation_id": run.extras.get(CONVERSATION_KEY),
        "message_id": run.tracer.message_id,
        "name": path.name,
        "created_at": dt.datetime.now(dt.timezone.utc).isoformat(),
    }
    path.with_name(path.name + META_SUFFIX).write_text(json.dumps(meta), encoding="utf-8")
    files = run.extras.setdefault(FILES_KEY, [])
    entry = {"name": path.name, "path": str(path), "url": download_url(path.parent.name, path.name)}
    if entry not in files:
        files.append(entry)
    return entry


def write_workbook(path: Path, tables: list[tuple[str, SqlResult]]) -> None:
    from openpyxl import Workbook
    from openpyxl.styles import Font

    wb = Workbook()
    wb.remove(wb.active)
    used: set[str] = set()
    for title, res in tables:
        name = re.sub(r"[\[\]:*?/\\]", " ", title).strip()[:28] or "Sheet"
        base, n = name, 2
        while name.lower() in used:
            name = f"{base[:25]} {n}"
            n += 1
        used.add(name.lower())
        ws = wb.create_sheet(name)
        ws.append(res.columns)
        for c in ws[1]:
            c.font = Font(bold=True)
        for row in res.rows[:MAX_ROWS_PER_TABLE]:
            ws.append([_cell(v) for v in row])
    if not wb.sheetnames:
        wb.create_sheet("Empty")
    _keep_text_as_text(wb)
    tmp = path.with_suffix(".tmp.xlsx")
    wb.save(tmp)
    tmp.replace(path)  # atomic: a retry never leaves a half-written file


def _md_table(res: SqlResult, limit: int = 200) -> str:
    def esc(v: Any) -> str:
        return " ".join(str("" if v is None else _cell(v)).split()).replace("|", "/")

    lines = ["| " + " | ".join(res.columns) + " |", "|" + "---|" * len(res.columns)]
    lines += ["| " + " | ".join(esc(v) for v in row) + " |" for row in res.rows[:limit]]
    if res.row_count > limit:
        lines.append(f"\n_{res.row_count - limit} more rows in the Excel file._")
    return "\n".join(lines)


def make_action_tools(output_dir: Path) -> list[Tool]:
    output_dir = Path(output_dir)

    async def export_excel(args: dict[str, Any], tctx: ToolContext) -> dict[str, Any]:
        title = str(args.get("title") or "").strip()
        specs = args.get("tables") or []
        if not title or not specs:
            raise ToolError("Give a title and at least one table: {'title': ..., 'result_id': 'r1'}.")
        tables = []
        for spec in specs:
            if not isinstance(spec, dict) or not spec.get("result_id"):
                raise ToolError("Each table needs a result_id from run_sql (tables are built from query results only).")
            (_, res), = _results(tctx.run, [str(spec["result_id"])])
            tables.append((str(spec.get("title") or spec["result_id"]), res))
        path = _folder(tctx.run, output_dir) / f"{_slug(title)}_{_key(tctx.run, 'excel', title)}.xlsx"
        write_workbook(path, tables)
        entry = _register(tctx.run, path)
        return {"file": entry["name"], "sheets": [t for t, _ in tables], "rows": [r.row_count for _, r in tables]}

    async def save_report(args: dict[str, Any], tctx: ToolContext) -> dict[str, Any]:
        title = str(args.get("title") or "").strip()
        sections = args.get("sections") or []
        if not title or not sections or not isinstance(sections, list):
            raise ToolError("Give a title and sections: [{'heading': ..., 'text': ..., 'result_ids': ['r1']}].")
        if len(sections) > MAX_SECTIONS:
            raise ToolError(f"At most {MAX_SECTIONS} sections.")
        from ..agents.number_check import allowed_numbers, unsupported_numbers  # lazy: avoids an import cycle

        run = tctx.run
        allowed = allowed_numbers(run.extras.get(RESULTS_KEY, {}).values(), run.extras.get(CALC_KEY, []),
                                  [str(run.extras.get(QUESTION_KEY) or ""), title])
        md = [f"# {title}", "", f"_Generated {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC by Finance Chat. "
              "Figures come from the queries listed in each section._", ""]
        tables: list[tuple[str, SqlResult]] = []
        bad: list[str] = []
        for i, sec in enumerate(sections, 1):
            if not isinstance(sec, dict):
                raise ToolError("Each section must be an object with heading, text and optional result_ids.")
            heading = str(sec.get("heading") or f"Section {i}").strip()
            text = str(sec.get("text") or "").strip()
            bad += unsupported_numbers(f"{heading}\n{text}", allowed)
            md += [f"## {heading}", "", text, ""]
            for rid, res in _results(run, [str(r) for r in sec.get("result_ids") or []]):
                md += [_md_table(res), ""]
                tables.append((heading, res))
        if bad:
            raise ToolError("The report text contains numbers that are not in this question's results: "
                            + ", ".join(dict.fromkeys(bad)) + ". Use only numbers from the query results, then retry.")
        folder = _folder(run, output_dir)
        stem = f"{_slug(title)}_{_key(run, 'report', title)}"
        md_path = folder / f"{stem}.md"
        md_path.write_text("\n".join(md), encoding="utf-8")
        files = [_register(run, md_path)]
        if tables:
            xlsx = folder / f"{stem}.xlsx"
            write_workbook(xlsx, tables)
            files.append(_register(run, xlsx))
        return {"files": [f["name"] for f in files], "sections": len(sections)}

    table_ref = {"type": "object", "properties": {"result_id": {"type": "string"}, "title": {"type": "string"}}, "required": ["result_id"]}
    return [
        Tool(ToolSpec(
            name="export_excel",
            description="Save query results as an Excel file (one sheet per table) for the user to download. Tables are "
                        "referenced by result_id; nothing is sent or shared.",
            input_schema={"type": "object", "properties": {"title": {"type": "string"},
                                                           "tables": {"type": "array", "items": table_ref}},
                          "required": ["title", "tables"]},
        ), export_excel, parallel_safe=False),
        Tool(ToolSpec(
            name="save_report",
            description="Save a report (Markdown, plus Excel when sections include result tables) linked to this "
                        "conversation. Section text may only contain numbers from this question's results.",
            input_schema={"type": "object", "properties": {
                "title": {"type": "string"},
                "sections": {"type": "array", "items": {"type": "object", "properties": {
                    "heading": {"type": "string"}, "text": {"type": "string"},
                    "result_ids": {"type": "array", "items": {"type": "string"}}}, "required": ["heading", "text"]}},
            }, "required": ["title", "sections"]},
        ), save_report, parallel_safe=False),
    ]
