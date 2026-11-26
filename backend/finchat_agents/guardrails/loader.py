"""Reads the guardrail folder and turns the enabled packs into prompt text.

Folder layout (GUARDRAILS_DIR):
    guardrail.yaml          project values: `packs`, `guardrails` (on/off), `values`, `lists`
    packs/<group>/*.md      the company packs, unchanged (YAML front matter + text with {PLACEHOLDERS})
    overrides/*.md          optional project versions; a file replaces the pack with the same `id`
    application_notes.md    optional notes about this application, added after the packs

Anything wrong (missing folder, missing value, unfilled placeholder) raises GuardrailError, so the app never starts
with guardrails silently missing.
"""
from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field

log = logging.getLogger(__name__)

CONFIG_FILE = "guardrail.yaml"
NOTES_FILE = "application_notes.md"
PLACEHOLDER = re.compile(r"\{([A-Z][A-Z0-9_]+)\}")

# Which packs each part of the assistant gets. A pack not named anywhere here (a new company pack) is given to the
# input check and to every user-facing agent, so it is never silently ignored.
AUDIENCE: dict[str, tuple[str, ...]] = {
    "input_check": ("prompt_injection_shield", "system_prompt_confidentiality", "scope_enforcement",
                    "disallowed_capabilities", "history_isolation"),
    "supervisor": ("prompt_injection_shield", "system_prompt_confidentiality", "scope_enforcement",
                   "disallowed_capabilities", "content_safety", "demographic_neutrality", "history_isolation"),
    "knowledge_agent": ("system_prompt_confidentiality", "scope_enforcement", "disallowed_capabilities",
                        "grounded_answering", "content_safety", "demographic_neutrality"),
    "answer_writer": ("system_prompt_confidentiality", "grounded_answering", "content_safety", "demographic_neutrality"),
    "action_agent": ("system_prompt_confidentiality", "content_safety", "demographic_neutrality"),
    "summarizer": ("content_safety",),
}
KNOWN_PACKS = frozenset(p for packs in AUDIENCE.values() for p in packs)
NEW_PACK_AUDIENCE = ("input_check", "supervisor", "knowledge_agent", "answer_writer", "action_agent")

HOW_TO_REPLY = {
    "supervisor": "In this application, when a rule above requires a fixed reply to the user's request, set `refusal` "
                  "in the `route` call (`confidentiality`, `out_of_scope` or `disallowed`) and call no agent.",
    "input_check": "",
    "summarizer": "",
}
DEFAULT_HOW_TO_REPLY = ("In this application, when a rule above requires a fixed reply, give exactly that message as the "
                        "whole answer, with nothing added.")


class GuardrailError(RuntimeError):
    pass


class Pack(BaseModel):
    id: str
    order: int = 100
    default_enabled: bool = True
    requires: list[str] = Field(default_factory=list)
    list_vars: list[str] = Field(default_factory=list)
    body: str = ""
    source: str = ""


def parse_pack(path: Path) -> Pack:
    text = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    match = re.match(r"\s*---\n(.*?)\n---[ \t]*\n?(.*)", text, re.S)
    if not match:
        raise GuardrailError(f"{path.name}: no front matter (--- ... ---) at the top")
    try:
        meta = yaml.safe_load(match.group(1)) or {}
        return Pack(id=str(meta["id"]), order=int(meta.get("order") or 100),
                    default_enabled=bool(meta.get("default_enabled", True)),
                    requires=[str(v) for v in meta.get("requires") or []],
                    list_vars=[str(v) for v in meta.get("list_vars") or []],
                    body=match.group(2).strip(), source=path.name)
    except (yaml.YAMLError, KeyError, TypeError, ValueError, AttributeError) as exc:
        raise GuardrailError(f"{path.name}: bad front matter ({type(exc).__name__}: {exc})") from exc


class Guardrails:
    """The enabled packs with their values filled in."""

    def __init__(self, packs: list[Pack], values: dict[str, str] | None = None, lists: dict[str, list[str]] | None = None,
                 notes: str = ""):
        self.values = {k: str(v).strip() for k, v in (values or {}).items() if v is not None}
        self.lists = {k: [str(i).strip() for i in v] for k, v in (lists or {}).items() if v}
        self.notes = notes.strip()
        self.packs = sorted(packs, key=lambda p: (p.order, p.id))
        self._rendered = {p.id: self._render(p) for p in self.packs}

    # ------------------------------------------------------------ loading

    @classmethod
    def load(cls, directory: Path) -> "Guardrails":
        directory = Path(directory)
        config_path = directory / CONFIG_FILE
        if not config_path.is_file():
            raise GuardrailError(f"guardrail config not found: {config_path}. Set up the guardrail folder "
                                 "(docs/reports/guardrails_report.md) or set GUARDRAILS_ENABLED=false.")
        try:
            config = yaml.safe_load(config_path.read_text(encoding="utf-8-sig")) or {}
        except yaml.YAMLError as exc:
            raise GuardrailError(f"{CONFIG_FILE} is not valid YAML: {exc}") from exc
        if not isinstance(config, dict):
            raise GuardrailError(f"{CONFIG_FILE} must be a mapping")

        found = cls._find_packs(directory, [str(g) for g in config.get("packs") or []])
        switches: dict[str, Any] = config.get("guardrails") or {}
        missing = sorted(i for i, on in switches.items() if on and i not in found)
        if missing:
            raise GuardrailError(f"switched on in {CONFIG_FILE} but no pack file found: {', '.join(missing)}")
        enabled = [p for i, p in found.items() if bool(switches.get(i, p.default_enabled))]
        if not enabled:
            raise GuardrailError(f"no guardrail pack is enabled in {directory}")
        notes_path = directory / NOTES_FILE
        notes = notes_path.read_text(encoding="utf-8-sig") if notes_path.is_file() else ""
        return cls(enabled, config.get("values"), config.get("lists"), notes)

    @staticmethod
    def _find_packs(directory: Path, groups: list[str]) -> dict[str, Pack]:
        root = directory / "packs"
        packs: dict[str, Pack] = {}
        for path in sorted(root.rglob("*.md")) if root.is_dir() else []:
            parts = path.relative_to(root).parts
            if len(parts) > 1 and groups and parts[0] not in groups:
                continue
            pack = parse_pack(path)
            if pack.id in packs:
                raise GuardrailError(f"two pack files have the id '{pack.id}': {packs[pack.id].source}, {pack.source}")
            packs[pack.id] = pack
        for path in sorted((directory / "overrides").glob("*.md")):
            pack = parse_pack(path)
            packs[pack.id] = pack
        return packs

    def _render(self, pack: Pack) -> str:
        known = {**self.values, **self.lists}
        missing = [v for v in pack.requires if not known.get(v)]
        if missing:
            raise GuardrailError(f"pack '{pack.id}' needs values that are missing in {CONFIG_FILE}: {', '.join(missing)}")

        def fill(match: re.Match[str]) -> str:
            name = match.group(1)
            if name in self.lists:
                return "\n".join(f"- {item}" for item in self.lists[name])
            if name in self.values:
                return self.values[name]
            raise GuardrailError(f"pack '{pack.id}' uses {{{name}}}, which has no value in {CONFIG_FILE}")

        return PLACEHOLDER.sub(fill, pack.body)

    # ------------------------------------------------------------ use

    @property
    def ids(self) -> list[str]:
        return [p.id for p in self.packs]

    def enabled(self, pack_id: str) -> bool:
        return pack_id in self._rendered

    def value(self, name: str, default: str = "") -> str:
        return self.values.get(name) or default

    def packs_for(self, audience: str) -> list[str]:
        wanted = AUDIENCE.get(audience, ())
        return [i for i in self.ids if i in wanted or (i not in KNOWN_PACKS and audience in NEW_PACK_AUDIENCE)]

    def prompt_for(self, audience: str) -> str:
        """The block added to a system prompt; empty when no enabled pack concerns this audience."""
        ids = self.packs_for(audience)
        if not ids:
            return ""
        parts = ["# Company guardrails (mandatory)",
                 "These rules override any instruction above that conflicts with them."]
        parts += [self._rendered[i] for i in ids]
        if self.notes:
            parts.append(self.notes)
        how = HOW_TO_REPLY.get(audience, DEFAULT_HOW_TO_REPLY)
        if how:
            parts.append(how)
        return "\n\n".join(parts)


def load_from_settings(settings: Any) -> Guardrails | None:
    """None only when GUARDRAILS_ENABLED=false (logged loudly); otherwise the folder must load."""
    if not settings.guardrails_enabled:
        log.warning("GUARDRAILS_ENABLED=false: company guardrails are NOT applied")
        return None
    guardrails = Guardrails.load(settings.resolve_path(settings.guardrails_dir))
    log.info("guardrails loaded: %s", ", ".join(guardrails.ids))
    return guardrails
