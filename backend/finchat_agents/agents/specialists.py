"""Catalog, SQL and knowledge agents. Prompts live in agents/prompts/*.md; table knowledge in knowledge/."""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

from ..access.rbac import UserAccess
from ..knowledge.loader import Knowledge
from ..llm.types import ModelHandle
from ..runtime.agent import Agent
from ..runtime.tools import RunContext, Tool, ToolContext

PROMPTS_DIR = Path(__file__).resolve().parent / "prompts"
KNOWLEDGE_EXAMPLES = 3


# every agent that reads results, table pages or earlier answers gets this rule (the input check has its own wording)
NO_DATA_RULE = ("data_rule", "input_guard")


@lru_cache(maxsize=None)
def load_prompt(name: str) -> str:
    text = (PROMPTS_DIR / f"{name}.md").read_text(encoding="utf-8").strip()
    if name in NO_DATA_RULE:
        return text
    return f"{text}\n\n{load_prompt('data_rule')}"


def with_rules(prompt: str, kb: Knowledge) -> str:
    return f"{prompt}\n\n---\n\n{kb.rules.strip()}" if kb.rules else prompt


CATALOG_SCHEMA = {
    "type": "object",
    "properties": {
        "answer": {"type": "string", "description": "The plan in two or three plain sentences."},
        "tables": {"type": "array", "items": {"type": "string"}, "description": "Fully qualified names, anchor first."},
        "columns": {"type": "array", "items": {"type": "string"}, "description": "Columns with their SQL expressions."},
        "joins": {"type": "array", "items": {"type": "string"}, "description": "Join conditions with every key column."},
        "filters": {"type": "array", "items": {"type": "string"}, "description": "Stored filter values, or 'not found'."},
        "caveats": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["answer", "tables"],
}

SQL_SCHEMA = {
    "type": "object",
    "properties": {
        "answer": {"type": "string", "description": "The result in plain words, numbers exactly as returned."},
        "status": {"type": "string", "enum": ["ok", "no_data", "failed"]},
        "result_ids": {"type": "array", "items": {"type": "string"}, "description": "run_sql result ids holding the answer."},
        "sql": {"type": "string", "description": "Final SQL, audit trail only."},
        "explanation": {"type": "string", "description": "Business-language explanation of the calculation, no SQL words."},
        "caveats": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["answer", "status", "result_ids", "explanation"],
}

CATALOG_TOOLS = ("search_tables", "describe_table", "get_join_path", "get_column_values", "get_glossary")
SQL_TOOLS = ("describe_table", "get_join_path", "get_column_values", "resolve_period", "resolve_entity", "run_sql", "calculate")


def _pick(tools: dict[str, Tool], names: tuple[str, ...]) -> list[Tool]:
    return [tools[n] for n in names if n in tools]


def build_catalog_agent(llm: ModelHandle, tools: dict[str, Tool], kb: Knowledge, **kw: Any) -> Agent:
    return Agent(
        "catalog_agent",
        with_rules(load_prompt("catalog"), kb),
        llm,
        _pick(tools, CATALOG_TOOLS),
        description="Find the tables, columns, approved joins, stored filter values and caveats for a data task. "
                    "Returns a plan for the SQL agent.",
        output_schema=CATALOG_SCHEMA,
        **kw,
    )


def format_examples(examples: list[Any]) -> str:
    blocks = []
    for e in examples:
        note = f"\nNote: {e.notes}" if e.notes else ""
        blocks.append(f"Q: {e.question}{note}\n```sql\n{e.sql.strip()}\n```")
    return "Similar verified examples (adapt the pattern; check values for this question):\n\n" + "\n\n".join(blocks)


class SqlAgent(Agent):
    def __init__(self, *args: Any, kb: Knowledge, **kw: Any):
        super().__init__(*args, **kw)
        self.kb = kb

    async def extra_context(self, task: str, ctx: RunContext) -> str | None:
        user = ctx.user
        domains = user.domains if isinstance(user, UserAccess) else None
        examples = self.kb.similar_examples(task, k=KNOWLEDGE_EXAMPLES, domains=domains)
        return format_examples(examples) if examples else None


def build_sql_agent(llm: ModelHandle, tools: dict[str, Tool], kb: Knowledge, **kw: Any) -> SqlAgent:
    return SqlAgent(
        "sql_agent",
        with_rules(load_prompt("sql"), kb),
        llm,
        _pick(tools, SQL_TOOLS),
        kb=kb,
        description="Write and run Databricks SQL for one data question, repair it on errors or empty results, and "
                    "return the answer, result_ids and a business explanation. Pass the catalog result in 'context'.",
        output_schema=SQL_SCHEMA,
        **kw,
    )


KNOWLEDGE_KEY = "knowledge_answers"  # RunContext.extras: general-knowledge texts given to the supervisor


def build_knowledge_agent(llm: ModelHandle, tools: dict[str, Tool], **kw: Any) -> Agent:
    return Agent(
        "knowledge_agent",
        load_prompt("knowledge"),
        llm,
        _pick(tools, ("get_glossary",)),
        description="Answer a general question (concepts, standards, how-to, any topic) from model knowledge. "
                    "No company data, no web.",
        max_steps=4,
        **kw,
    )


def knowledge_tool(agent: Agent) -> Tool:
    """ask_knowledge_agent that also records the text (its numbers are general knowledge, labelled as such)."""
    base = agent.as_tool()

    async def handler(args: dict[str, Any], tctx: ToolContext) -> Any:
        result = await base.handler(args, tctx)
        tctx.run.extras.setdefault(KNOWLEDGE_KEY, []).append(result.answer)
        return result

    return Tool(spec=base.spec, handler=handler)


ANALYST_SCHEMA = {
    "type": "object",
    "properties": {
        "answer": {"type": "string", "description": "The conclusion, numbers exactly as returned or calculated."},
        "steps": {"type": "array", "items": {"type": "string"}, "description": "Steps taken, in business language."},
        "result_ids": {"type": "array", "items": {"type": "string"}},
        "status": {"type": "string", "enum": ["ok", "partial", "failed"]},
        "caveats": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["answer", "steps", "status"],
}

ACTION_SCHEMA = {
    "type": "object",
    "properties": {
        "answer": {"type": "string"},
        "files": {"type": "array", "items": {"type": "string"}},
        "status": {"type": "string", "enum": ["ok", "failed"]},
    },
    "required": ["answer", "status"],
}


def build_analyst_agent(llm: ModelHandle, sql_agent_tool: Tool, tools: dict[str, Tool], **kw: Any) -> Agent:
    return Agent(
        "analyst_agent",
        with_rules(load_prompt("analyst"), kw.pop("kb")),
        llm,
        [sql_agent_tool, *_pick(tools, ("calculate", "get_glossary"))],
        description="Answer a multi-step question (comparison, trend, variance, ratio, top-N with context): splits it into "
                    "sub-questions for the SQL agent and combines the results with calculations.",
        output_schema=ANALYST_SCHEMA,
        **kw,
    )


def build_action_agent(llm: ModelHandle, action_tools: list[Tool], **kw: Any) -> Agent:
    return Agent(
        "action_agent",
        load_prompt("action"),
        llm,
        action_tools,
        description="Create files: an Excel export of query results or a saved report (Markdown + Excel). Give the "
                    "result ids to include. Nothing is emailed, shared or sent.",
        output_schema=ACTION_SCHEMA,
        max_steps=6,
        **kw,
    )
