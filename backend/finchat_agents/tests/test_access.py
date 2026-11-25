from __future__ import annotations

import pytest

from finchat_agents.access import AccessConfig, AccessConfigError
from finchat_agents.config import get_settings

CFG = {
    "domains": {"recon": "ADRA", "subledger": "Fynapse", "fa": "FA", "ar": "AR"},
    "roles": {
        "finance_all": {"domains": ["*"], "pii_allowed": False},
        "fa_reader": {"domains": ["fa"]},
        "ar_reader": {"domains": ["ar"]},
        "pii_viewer": {"domains": ["recon"], "pii_allowed": True},
    },
    "group_roles": {"CFO": "finance_all", "Fixed asset analyst": "fa_reader", "AR analyst": "ar_reader"},
    "users": {"obj-1": "pii_viewer", "obj-2": ["fa_reader", "ar_reader"]},
    "default_role": None,
    "service_role": "finance_all",
}


def test_user_id_wins_over_groups():
    cfg = AccessConfig(CFG)
    role = cfg.resolve_role("obj-1", ["CFO"])
    assert role.name == "pii_viewer" and role.pii_allowed and role.domains == ["recon"]


def test_groups_union_and_unknown_user():
    cfg = AccessConfig(CFG)
    role = cfg.resolve_role("someone", ["Fixed asset analyst", "AR analyst", "Unknown group"])
    assert role.domains == ["fa", "ar"] and not role.pii_allowed
    assert role.allows_domain("fa") and not role.allows_domain("recon")
    assert cfg.resolve_role("someone", []) is None
    assert cfg.resolve_role(None, ["Nope"]) is None
    assert not cfg.user_access("someone").has_access


def test_star_domain_and_service_role():
    cfg = AccessConfig(CFG)
    assert cfg.resolve_role("x", ["CFO"]).allows_domain("subledger")
    assert cfg.resolve_role("x", ["CFO"]).allows_domain(None) is False  # tables without a domain stay closed
    assert cfg.service_access().role.domains == ["*"]
    assert cfg.resolve_role("obj-2").domains == ["fa", "ar"]


def test_invalid_config_is_rejected():
    bad = {**CFG, "group_roles": {"X": "missing_role"}, "roles": {**CFG["roles"], "odd": {"domains": ["nowhere"]}}}
    with pytest.raises(AccessConfigError) as ei:
        AccessConfig(bad)
    assert "unknown role 'missing_role'" in str(ei.value) and "unknown domain 'nowhere'" in str(ei.value)


def test_default_role_applies_when_set():
    cfg = AccessConfig({**CFG, "default_role": "ar_reader"})
    assert cfg.resolve_role("anyone").domains == ["ar"]


def test_shipped_access_file_loads():
    s = get_settings()
    cfg = AccessConfig.load(s.resolve_path(s.rbac_file))
    assert cfg.default_role is None  # unknown user = no access
    assert cfg.resolve_role("x", ["CFO"]).domains == ["*"]
    assert cfg.resolve_role("x", ["AR analyst"]).domains == ["ar"]
    assert not any(r.pii_allowed for r in cfg.roles.values())
