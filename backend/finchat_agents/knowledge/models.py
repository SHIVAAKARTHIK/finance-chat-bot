"""Typed knowledge objects: table pages, joins, glossary entries, examples."""
from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

KnownIssueCode = Literal[
    "duplicates",  # source loaded more than once; check duplicates at the grain
    "orphans",  # fact keys without a dimension row
    "all_string_columns",  # every column stored as STRING
    "entity_values_changing",  # entity codes recently changed; check current values
    "empty_column",  # a column is not populated
    "broken",  # object cannot be queried
    "other",
]

DEFAULT_CATALOG = "lakehouse_mvpai"


class KnownIssue(BaseModel):
    model_config = ConfigDict(extra="forbid")
    code: KnownIssueCode
    note: str = ""


def _as_list(v: Any) -> Any:
    if v is None:
        return []
    if isinstance(v, str):
        return [p.strip() for p in v.split(",") if p.strip()]
    return v


class TableMeta(BaseModel):
    """Front matter of a table page."""

    model_config = ConfigDict(extra="forbid", populate_by_name=True)

    name: str
    schema_: str = Field(alias="schema")
    catalog: str = DEFAULT_CATALOG
    layer: Literal["bronze", "silver", "gold"]
    domain: str | None = None
    type: Literal["fact", "dim", "view", "table"] = "table"
    status: Literal["active", "broken"] = "active"
    purpose: str = ""
    grain: str = ""
    primary_key: list[str] = Field(default_factory=list)
    entity_column: str | None = None
    period_columns: list[str] = Field(default_factory=list)
    pii_columns: list[str] = Field(default_factory=list)
    synonyms: list[str] = Field(default_factory=list)
    built_from: list[str] = Field(default_factory=list)
    # A copy of data that has a source of truth elsewhere: excluded from search, refused by run_sql with "use X instead".
    superseded_by: list[str] = Field(default_factory=list)
    known_issues: list[KnownIssue] = Field(default_factory=list)
    row_count: int | None = None
    broken_error: str | None = None
    proposed_fields: list[str] = Field(default_factory=list)  # fields whose value is a proposal awaiting review
    reviewed: bool | list[str] = False  # True = every field reviewed; a list = those fields

    @field_validator("primary_key", "period_columns", "pii_columns", "synonyms", "built_from", "superseded_by", mode="before")
    @classmethod
    def _norm_lists(cls, v: Any) -> Any:
        return _as_list(v)

    @property
    def id(self) -> str:
        return f"{self.schema_}.{self.name}"

    @property
    def fqn(self) -> str:
        return f"{self.catalog}.{self.schema_}.{self.name}"

    def is_reviewed(self, field: str) -> bool:
        return self.reviewed is True or (isinstance(self.reviewed, list) and field in self.reviewed)

    def has_issue(self, code: str) -> bool:
        return any(i.code == code for i in self.known_issues)


class Column(BaseModel):
    name: str
    type: str = "string"
    meaning: str = ""
    synonyms: list[str] = Field(default_factory=list)
    sql: str = ""
    pii: bool = False
    values: list[str] = Field(default_factory=list)


class TablePage(BaseModel):
    meta: TableMeta
    columns: list[Column] = Field(default_factory=list)
    body: str = ""  # Markdown after the front matter, shown to agents by describe_table
    path: str = ""

    @property
    def id(self) -> str:
        return self.meta.id

    def column(self, name: str) -> Column | None:
        low = name.lower()
        return next((c for c in self.columns if c.name.lower() == low), None)

    def has_column(self, name: str) -> bool:
        return any(c.name == name for c in self.columns)


class Join(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    from_: str = Field(alias="from")
    to: str
    keys: list[tuple[str, str]]
    cardinality: Literal["many_to_one", "one_to_one", "many_to_many"]
    status: Literal["approved", "proposed", "blocked"]
    note: str = ""

    def condition(self, from_ref: str | None = None, to_ref: str | None = None) -> str:
        """SQL ON condition with the full key, e.g. `f.A = d.A AND f.B = d.B`."""
        a = from_ref or self.from_.split(".")[-1]
        b = to_ref or self.to.split(".")[-1]
        return " AND ".join(f"{a}.{x} = {b}.{y}" for x, y in self.keys)

    def other(self, table_id: str) -> str:
        return self.to if table_id == self.from_ else self.from_


class GlossaryEntry(BaseModel):
    term: str
    aliases: list[str] = Field(default_factory=list)
    tables: list[str] = Field(default_factory=list)
    status: Literal["approved", "draft"] = "approved"
    text: str = ""

    @property
    def names(self) -> list[str]:
        return [self.term, *self.aliases]


class Example(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    question: str
    sql: str
    tables: list[str]
    expected: dict[str, Any] | None = None
    verified: bool = False
    notes: str = ""


class SearchHit(BaseModel):
    table: str  # schema.table
    fqn: str
    score: float
    domain: str | None
    layer: str
    purpose: str
