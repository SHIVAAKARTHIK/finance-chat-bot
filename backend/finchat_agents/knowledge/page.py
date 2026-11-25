"""Read and write table pages: YAML front matter + Markdown sections.

A section heading followed by the line `<!-- reviewed -->` is owned by a person: the generator never rewrites it.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

import yaml

REVIEWED_MARK = "<!-- reviewed -->"
_FRONT = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", re.S)
_SECTION = re.compile(r"^## +(.+?)\s*$", re.M)

COLUMN_HEADER = ["Column", "Type", "Meaning", "Also called", "SQL expression"]


@dataclass
class Section:
    heading: str
    content: str  # without the heading line and the reviewed marker, stripped
    reviewed: bool = False


@dataclass
class PageDoc:
    front: dict[str, Any]
    intro: str  # everything before the first "## " section (title and purpose)
    sections: list[Section] = field(default_factory=list)

    def section(self, heading: str) -> Section | None:
        return next((s for s in self.sections if s.heading.lower() == heading.lower()), None)

    def set_section(self, heading: str, content: str, *, after: str | None = None) -> None:
        existing = self.section(heading)
        if existing is not None:
            existing.content = content.strip()
            return
        new = Section(heading, content.strip())
        if after and (anchor := self.section(after)) is not None:
            self.sections.insert(self.sections.index(anchor) + 1, new)
        else:
            self.sections.append(new)


class PageFormatError(ValueError):
    pass


def parse_page(text: str) -> PageDoc:
    m = _FRONT.match(text.replace("\r\n", "\n"))
    if not m:
        raise PageFormatError("page must start with a YAML front matter block between '---' lines")
    front = yaml.safe_load(m.group(1)) or {}
    if not isinstance(front, dict):
        raise PageFormatError("front matter must be a mapping")
    body = m.group(2)
    matches = list(_SECTION.finditer(body))
    intro = body[: matches[0].start()] if matches else body
    sections: list[Section] = []
    for i, sm in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        content = body[sm.end():end].strip("\n")
        reviewed = False
        stripped = content.lstrip("\n")
        if stripped.startswith(REVIEWED_MARK):
            reviewed = True
            content = stripped[len(REVIEWED_MARK):]
        sections.append(Section(sm.group(1).strip(), content.strip(), reviewed))
    return PageDoc(front=front, intro=intro.strip(), sections=sections)


def render_page(doc: PageDoc) -> str:
    front = yaml.safe_dump(doc.front, sort_keys=False, allow_unicode=True, width=120).strip()
    parts = [f"---\n{front}\n---", doc.intro.strip()]
    for s in doc.sections:
        head = f"## {s.heading}"
        if s.reviewed:
            head += f"\n{REVIEWED_MARK}"
        parts.append(f"{head}\n\n{s.content.strip()}" if s.content.strip() else head)
    return "\n\n".join(p for p in parts if p) + "\n"


# ---------------------------------------------------------------- markdown tables

def _cells(line: str) -> list[str]:
    inner = line.strip()
    if inner.startswith("|"):
        inner = inner[1:]
    if inner.endswith("|"):
        inner = inner[:-1]
    return [c.strip() for c in inner.split("|")]


def _unquote(cell: str) -> str:
    cell = cell.strip()
    if len(cell) >= 2 and cell.startswith("`") and cell.endswith("`"):
        return cell[1:-1]
    return cell


def parse_markdown_table(content: str) -> list[dict[str, str]]:
    """First Markdown table in `content` as a list of {header: cell} (backticks around a whole cell removed)."""
    lines = [ln for ln in content.splitlines() if ln.strip().startswith("|")]
    if len(lines) < 2:
        return []
    header = _cells(lines[0])
    rows = []
    for ln in lines[2:]:
        cells = _cells(ln)
        cells += [""] * (len(header) - len(cells))
        rows.append({h: _unquote(c) for h, c in zip(header, cells)})
    return rows


def parse_columns(content: str) -> list[dict[str, Any]]:
    out = []
    for row in parse_markdown_table(content):
        name = row.get("Column", "").strip()
        if not name:
            continue
        synonyms = [s.strip() for s in row.get("Also called", "").split(",") if s.strip()]
        out.append(
            {
                "name": name,
                "type": row.get("Type", "").strip() or "string",
                "meaning": row.get("Meaning", "").strip(),
                "synonyms": synonyms,
                "sql": row.get("SQL expression", "").strip() or name,
            }
        )
    return out


def render_columns(columns: list[dict[str, Any]]) -> str:
    def esc(v: str) -> str:
        return str(v or "").replace("|", "\\|").replace("\n", " ")

    lines = ["| " + " | ".join(COLUMN_HEADER) + " |", "|" + "---|" * len(COLUMN_HEADER)]
    for c in columns:
        sql = c.get("sql") or c["name"]
        lines.append(
            f"| `{c['name']}` | {esc(c.get('type', 'string'))} | {esc(c.get('meaning', ''))} | "
            f"{esc(', '.join(c.get('synonyms', [])))} | `{esc(sql)}` |"
        )
    return "\n".join(lines)


_VALUE_HEAD = re.compile(r"^\*\*(.+?)\*\*\s*$")  # column names may contain spaces or punctuation
_VALUE_ITEM = re.compile(r"^-\s+`([^`]*)`(?::\s*(.*))?$")


def parse_values(content: str) -> dict[str, list[tuple[str, str]]]:
    """`**COLUMN**` followed by `- `value`: meaning` items."""
    out: dict[str, list[tuple[str, str]]] = {}
    current: str | None = None
    for line in content.splitlines():
        line = line.strip()
        if m := _VALUE_HEAD.match(line):
            current = m.group(1)
            out.setdefault(current, [])
        elif current and (m := _VALUE_ITEM.match(line)):
            out[current].append((m.group(1), (m.group(2) or "").strip()))
    return out


def render_values(values: dict[str, list[tuple[str, str]]]) -> str:
    blocks = []
    for col, items in values.items():
        lines = [f"**{col}**"] + [f"- `{v}`" + (f": {m}" if m else "") for v, m in items]
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)
