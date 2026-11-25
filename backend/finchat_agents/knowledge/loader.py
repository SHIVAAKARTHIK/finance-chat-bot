"""Load and validate the knowledge layer: table pages, joins, glossary, rules, examples; build the search index.

    python -m finchat_agents.knowledge.loader            # validate and print a summary
    python -m finchat_agents.knowledge.loader --write-index   # also rewrite knowledge/INDEX.md
"""
from __future__ import annotations

import argparse
import re
from collections import deque
from functools import lru_cache
from pathlib import Path
from typing import Any

import sqlglot
import yaml
from pydantic import ValidationError
from sqlglot import exp

from ..config import PACKAGE_DIR
from .models import Column, Example, GlossaryEntry, Join, SearchHit, TableMeta, TablePage
from .page import PageFormatError, parse_columns, parse_page, parse_values
from .search import BM25Index, tokenize

KNOWLEDGE_DIR = Path(__file__).resolve().parent
DEFAULT_RBAC = PACKAGE_DIR / "config" / "rbac.v3.yaml"


class KnowledgeError(Exception):
    def __init__(self, problems: list[str]):
        super().__init__("knowledge layer is invalid:\n- " + "\n- ".join(problems))
        self.problems = problems


def sql_tables(sql: str) -> set[str]:
    """Fully qualified table names (lowercase) read by a statement; CTE names are excluded."""
    tree = sqlglot.parse_one(sql, read="databricks")
    ctes = {c.alias_or_name.lower() for c in tree.find_all(exp.CTE)}
    out = set()
    for t in tree.find_all(exp.Table):
        name = t.name.lower()
        if not t.db and name in ctes:
            continue
        out.add(".".join(p for p in (t.catalog, t.db, t.name) if p).lower())
    return out


def load_domains(rbac_file: Path | None) -> dict[str, str]:
    path = rbac_file or DEFAULT_RBAC
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return {str(k): str(v) for k, v in (data.get("domains") or {}).items()}


def _load_page(path: Path) -> TablePage:
    doc = parse_page(path.read_text(encoding="utf-8"))
    meta = TableMeta.model_validate(doc.front)
    cols_section = doc.section("Columns")
    values_section = doc.section("Values")
    values = parse_values(values_section.content) if values_section else {}
    pii = set(meta.pii_columns)
    columns = [
        Column(**c, pii=c["name"] in pii, values=[v for v, _ in values.get(c["name"], [])])
        for c in (parse_columns(cols_section.content) if cols_section else [])
    ]
    body = path.read_text(encoding="utf-8").split("\n---", 2)[-1].lstrip("-\n")
    return TablePage(meta=meta, columns=columns, body=body.strip(), path=str(path))


_GLOSS_FIELD = re.compile(r"^(Aliases|Tables|Status):\s*(.*)$", re.I)


def parse_glossary(text: str) -> list[GlossaryEntry]:
    entries = []
    for block in re.split(r"^## +", text, flags=re.M)[1:]:
        lines = block.strip().splitlines()
        term, rest = lines[0].strip(), lines[1:]
        fields: dict[str, Any] = {"term": term}
        body = []
        for line in rest:
            m = _GLOSS_FIELD.match(line.strip())
            if m and not body:
                key, value = m.group(1).lower(), m.group(2)
                fields[key] = value.strip().lower() if key == "status" else [v.strip() for v in value.split(",") if v.strip()]
            else:
                body.append(line)
        fields["text"] = "\n".join(body).strip()
        entries.append(GlossaryEntry(**fields))
    return entries


class Knowledge:
    def __init__(
        self,
        tables: dict[str, TablePage],
        joins: list[Join],
        glossary: list[GlossaryEntry],
        rules: str,
        examples: list[Example],
        domains: dict[str, str],
    ):
        self.tables = tables
        self.joins = joins
        self.glossary = glossary
        self.rules = rules
        self.examples = examples
        self.domains = domains
        self._by_name = {}
        for tid, page in tables.items():
            for key in (tid, page.meta.fqn, page.meta.name):
                self._by_name.setdefault(key.lower(), tid)
        self.index = BM25Index({tid: self._table_tokens(p) for tid, p in tables.items()})
        self.example_index = BM25Index({e.id: tokenize(e.question) for e in examples})
        self.warnings: list[str] = []

    # ------------------------------------------------------------ loading

    @classmethod
    def load(cls, root: Path | str = KNOWLEDGE_DIR, *, rbac_file: Path | None = None, strict: bool = True) -> "Knowledge":
        root = Path(root)
        problems: list[str] = []
        tables: dict[str, TablePage] = {}
        for path in sorted((root / "tables").glob("*.md")):
            try:
                page = _load_page(path)
            except (PageFormatError, ValidationError, yaml.YAMLError) as exc:
                problems.append(f"{path.name}: {exc}")
                continue
            if path.name != f"{page.id}.md":
                problems.append(f"{path.name}: file name must be '{page.id}.md'")
            tables[page.id] = page

        joins = []
        for fname in ("joins.yaml", "joins_proposed.yaml"):  # proposals are never used by get_join_path
            data = yaml.safe_load((root / fname).read_text(encoding="utf-8")) if (root / fname).exists() else {}
            for j in (data or {}).get("joins", []):
                try:
                    join = Join.model_validate(j)
                except ValidationError as exc:
                    problems.append(f"{fname} {j.get('id')}: {exc}")
                    continue
                if fname == "joins_proposed.yaml" and join.status == "approved":
                    problems.append(f"{fname} {join.id}: approve a join by moving it to joins.yaml")
                    continue
                joins.append(join)

        glossary = parse_glossary((root / "glossary.md").read_text(encoding="utf-8")) if (root / "glossary.md").exists() else []
        rules = (root / "rules.md").read_text(encoding="utf-8") if (root / "rules.md").exists() else ""
        ex_data = yaml.safe_load((root / "examples.yaml").read_text(encoding="utf-8")) if (root / "examples.yaml").exists() else {}
        examples = []
        for e in (ex_data or {}).get("examples", []):
            try:
                examples.append(Example.model_validate(e))
            except ValidationError as exc:
                problems.append(f"examples.yaml {e.get('id')}: {exc}")

        kb = cls(tables, joins, glossary, rules, examples, load_domains(rbac_file))
        errors, warnings = kb.validate()
        kb.warnings = warnings
        problems += errors
        if problems and strict:
            raise KnowledgeError(problems)
        return kb

    # ------------------------------------------------------------ validation

    def validate(self) -> tuple[list[str], list[str]]:
        errors: list[str] = []
        warnings: list[str] = []
        for tid, page in self.tables.items():
            m = page.meta
            if m.domain is None:
                warnings.append(f"{tid}: no domain (excluded from search until set)")
            elif self.domains and m.domain not in self.domains:
                errors.append(f"{tid}: domain '{m.domain}' is not in the access file ({', '.join(self.domains)})")
            for target in m.superseded_by:
                if target not in self.tables:
                    errors.append(f"{tid}: superseded_by '{target}' has no page")
            if m.status == "broken":
                continue
            if not page.columns:
                errors.append(f"{tid}: no columns table")
                continue
            if not m.purpose or not m.grain:
                (errors if m.reviewed is True else warnings).append(f"{tid}: purpose and grain are required")
            refs = {"primary_key": m.primary_key, "period_columns": m.period_columns, "pii_columns": m.pii_columns}
            if m.entity_column:
                refs["entity_column"] = [m.entity_column]
            for field, cols in refs.items():
                if field in m.proposed_fields:
                    continue
                for c in cols:
                    if not page.has_column(c):
                        errors.append(f"{tid}: {field} column '{c}' is not in the columns table")
            names = [c.name for c in page.columns]
            if len(names) != len(set(names)):
                errors.append(f"{tid}: duplicate column names")

        seen: set[str] = set()
        for j in self.joins:
            if j.id in seen:
                errors.append(f"joins.yaml: duplicate id {j.id}")
            seen.add(j.id)
            for side, tid, idx in (("from", j.from_, 0), ("to", j.to, 1)):
                page = self.tables.get(tid)
                if page is None:
                    errors.append(f"joins.yaml {j.id}: {side} table '{tid}' has no page")
                    continue
                for pair in j.keys:
                    if not page.has_column(pair[idx]):
                        errors.append(f"joins.yaml {j.id}: column '{pair[idx]}' is not in {tid}")

        for e in self.examples:
            listed = set()
            for t in e.tables:
                page = self.tables.get(t)
                if page is None:
                    errors.append(f"examples.yaml {e.id}: table '{t}' has no page")
                else:
                    listed.add(page.meta.fqn.lower())
            try:
                used = sql_tables(e.sql)
            except sqlglot.errors.ParseError as exc:
                errors.append(f"examples.yaml {e.id}: SQL does not parse: {str(exc)[:200]}")
                continue
            if used != listed:
                errors.append(f"examples.yaml {e.id}: SQL reads {sorted(used)} but tables lists {sorted(listed)}")

        for g in self.glossary:
            for t in g.tables:
                if t not in self.tables:
                    errors.append(f"glossary.md '{g.term}': table '{t}' has no page")
        return errors, warnings

    # ------------------------------------------------------------ lookup

    def resolve_table(self, name: str) -> TablePage | None:
        tid = self._by_name.get(name.strip().strip("`").lower())
        return self.tables.get(tid) if tid else None

    def searchable(self, domains: list[str] | None = None) -> set[str]:
        """Active tables with a domain, limited to `domains` (None or '*' = all)."""
        allow_all = domains is None or "*" in domains
        return {
            tid
            for tid, p in self.tables.items()
            if p.meta.status == "active" and p.meta.domain and not p.meta.superseded_by
            and (allow_all or p.meta.domain in domains)  # type: ignore[operator]
        }

    def search_tables(self, query: str, k: int = 5, domains: list[str] | None = None) -> list[SearchHit]:
        hits = self.index.search(query, k=k, allowed=self.searchable(domains))
        out = []
        for tid, score in hits:
            m = self.tables[tid].meta
            out.append(SearchHit(table=tid, fqn=m.fqn, score=round(score, 3), domain=m.domain, layer=m.layer, purpose=m.purpose))
        return out

    def join_path(self, a: str, b: str) -> list[Join] | None:
        """Shortest chain of approved joins between two tables (either direction); None if not connected."""
        pa, pb = self.resolve_table(a), self.resolve_table(b)
        if pa is None or pb is None:
            return None
        start, goal = pa.id, pb.id
        if start == goal:
            return []
        approved = [j for j in self.joins if j.status == "approved"]
        prev: dict[str, tuple[str, Join]] = {}
        queue, seen = deque([start]), {start}
        while queue:
            node = queue.popleft()
            for j in approved:
                if node not in (j.from_, j.to):
                    continue
                nxt = j.other(node)
                if nxt in seen:
                    continue
                seen.add(nxt)
                prev[nxt] = (node, j)
                if nxt == goal:
                    path, cur = [], goal
                    while cur != start:
                        cur, join = prev[cur]
                        path.append(join)
                    return list(reversed(path))
                queue.append(nxt)
        return None

    def glossary_lookup(self, text: str) -> list[GlossaryEntry]:
        """Entries whose term or alias appears in `text` (whole words, case-insensitive)."""
        low = f" {re.sub(r'[^a-z0-9&]+', ' ', text.lower())} "
        out = []
        for g in self.glossary:
            for name in g.names:
                norm = re.sub(r"[^a-z0-9&]+", " ", name.lower()).strip()
                if norm and f" {norm} " in low:
                    out.append(g)
                    break
        return out

    def similar_examples(self, question: str, k: int = 3, domains: list[str] | None = None) -> list[Example]:
        allowed = None
        if domains is not None and "*" not in domains:
            ok = self.searchable(domains)
            allowed = {e.id for e in self.examples if all(t in ok for t in e.tables)}
        by_id = {e.id: e for e in self.examples}
        return [by_id[i] for i, _ in self.example_index.search(question, k=k, allowed=allowed)]

    # ------------------------------------------------------------ index

    def _table_tokens(self, page: TablePage) -> list[str]:
        m = page.meta
        toks = tokenize(m.name) * 3
        for s in m.synonyms:
            toks += tokenize(s) * 2
        toks += tokenize(m.purpose)
        for c in page.columns:
            toks += tokenize(c.name)
            for s in c.synonyms:
                toks += tokenize(s)
        if m.domain and m.domain in self.domains:
            toks += tokenize(self.domains[m.domain])
        return toks

    def index_markdown(self) -> str:
        lines = [
            "# Table index",
            "",
            "Generated from the table pages by `python -m finchat_agents.knowledge.loader --write-index`. Do not edit by hand.",
            "",
            "| Table | Domain | Layer | Type | Status | Grain | Purpose |",
            "|---|---|---|---|---|---|---|",
        ]
        for tid in sorted(self.tables):
            m = self.tables[tid].meta
            purpose = " ".join(m.purpose.split())
            status = f"superseded by {', '.join(m.superseded_by)}" if m.superseded_by else m.status
            lines.append(
                f"| `{tid}` | {m.domain or '-'} | {m.layer} | {m.type} | {status} | {' '.join(m.grain.split())} | {purpose} |"
            )
        return "\n".join(lines) + "\n"


@lru_cache(maxsize=1)
def get_knowledge() -> Knowledge:
    return Knowledge.load()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=str(KNOWLEDGE_DIR))
    ap.add_argument("--write-index", action="store_true")
    args = ap.parse_args()
    kb = Knowledge.load(args.root)
    print(f"tables: {len(kb.tables)}, joins: {len(kb.joins)}, glossary: {len(kb.glossary)}, examples: {len(kb.examples)}")
    for w in kb.warnings:
        print(f"warning: {w}")
    if args.write_index:
        (Path(args.root) / "INDEX.md").write_text(kb.index_markdown(), encoding="utf-8")
        print("INDEX.md written")


if __name__ == "__main__":
    main()
