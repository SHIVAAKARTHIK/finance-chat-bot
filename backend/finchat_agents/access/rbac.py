"""Role-based access from config/rbac.v3.yaml: role -> domains (+ PII flag). No row-level entity scopes.

Resolution: explicit user (Entra object id) first, then Entra group names. No match (and no default role) = no access.
A user in several groups gets the union of their roles' domains; PII is allowed if any matched role allows it.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field


class Role(BaseModel):
    name: str
    domains: list[str] = Field(default_factory=list)
    pii_allowed: bool = False

    def allows_domain(self, domain: str | None) -> bool:
        return domain is not None and ("*" in self.domains or domain in self.domains)


class UserAccess(BaseModel):
    """What the tools need to know about the user. Stored in RunContext.user."""

    user_id: str
    groups: list[str] = Field(default_factory=list)
    role: Role | None = None

    @property
    def has_access(self) -> bool:
        return self.role is not None and bool(self.role.domains)

    @property
    def domains(self) -> list[str]:
        return list(self.role.domains) if self.role else []

    @property
    def pii_allowed(self) -> bool:
        return bool(self.role and self.role.pii_allowed)


class AccessConfigError(ValueError):
    pass


class AccessConfig:
    def __init__(self, data: dict[str, Any]):
        self.domains: dict[str, str] = {str(k): str(v) for k, v in (data.get("domains") or {}).items()}
        self.roles: dict[str, Role] = {}
        for name, spec in (data.get("roles") or {}).items():
            spec = spec or {}
            self.roles[name] = Role(name=name, domains=list(spec.get("domains") or []), pii_allowed=bool(spec.get("pii_allowed", False)))
        self.group_roles: dict[str, str] = {str(k): str(v) for k, v in (data.get("group_roles") or {}).items()}
        self.users: dict[str, Any] = {str(k): v for k, v in (data.get("users") or {}).items()}
        self.default_role: str | None = data.get("default_role")
        self.service_role: str | None = data.get("service_role")
        problems = self.validate()
        if problems:
            raise AccessConfigError("access file is invalid:\n- " + "\n- ".join(problems))

    @classmethod
    def load(cls, path: str | Path) -> "AccessConfig":
        return cls(yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {})

    def validate(self) -> list[str]:
        problems = []
        for role in self.roles.values():
            for d in role.domains:
                if d != "*" and d not in self.domains:
                    problems.append(f"role {role.name}: unknown domain '{d}'")
        refs = [("group_roles", g, r) for g, r in self.group_roles.items()]
        for uid, r in self.users.items():
            for name in r if isinstance(r, list) else [r]:
                refs.append(("users", uid, str(name)))
        if self.default_role:
            refs.append(("default_role", "", self.default_role))
        if self.service_role:
            refs.append(("service_role", "", self.service_role))
        for where, key, role in refs:
            if role not in self.roles:
                problems.append(f"{where} {key}: unknown role '{role}'".replace("  ", " "))
        return problems

    def _combine(self, names: list[str]) -> Role | None:
        roles = [self.roles[n] for n in names if n in self.roles]
        if not roles:
            return None
        domains: list[str] = []
        for r in roles:
            domains += [d for d in r.domains if d not in domains]
        return Role(name="+".join(r.name for r in roles), domains=domains, pii_allowed=any(r.pii_allowed for r in roles))

    def resolve_role(self, user_id: str | None, groups: list[str] | None = None) -> Role | None:
        if user_id and user_id in self.users:
            r = self.users[user_id]
            return self._combine([str(x) for x in (r if isinstance(r, list) else [r])])
        names = [self.group_roles[g] for g in (groups or []) if g in self.group_roles]
        if names:
            return self._combine(list(dict.fromkeys(names)))
        return self._combine([self.default_role]) if self.default_role else None

    def user_access(self, user_id: str, groups: list[str] | None = None) -> UserAccess:
        return UserAccess(user_id=user_id, groups=list(groups or []), role=self.resolve_role(user_id, groups))

    def service_access(self) -> UserAccess:
        role = self._combine([self.service_role]) if self.service_role else None
        return UserAccess(user_id="service", role=role)
