"""Post-deploy smoke test. Run on the VM (or anywhere that can reach the backend) after `docker compose up`:

    python -m finchat_agents.deploy.smoke --base-url http://localhost:8000 --user-id <test user object id>

or, inside the container:

    docker compose exec backend python -m finchat_agents.deploy.smoke --base-url http://127.0.0.1:8000 --user-id <id>

Checks: /v3/health/live, /v3/health is green (every enabled check ok), then a few generic questions return
`answered` or `partial` with a non-empty answer. Prints statuses and timings only (no answers, no SQL). Exit code 0 when
everything passed. Use a test user id that the access file maps to a role (never a personal id in shared logs).
"""
from __future__ import annotations

import argparse
import asyncio
import sys
import time
from typing import Any

import httpx

# Generic questions: one per path (data count, catalog, knowledge, general). Not taken from any question bank.
SMOKE_QUESTIONS = [
    "How many account reconciliations are there?",
    "Which tables hold fixed asset data?",
    "What does an unidentified difference mean in a reconciliation?",
    "Hello, what can you help me with?",
]
OK_STATUSES = {"answered", "partial"}


async def run_smoke(client: httpx.AsyncClient, user_id: str, questions: list[str] | None = None,
                    groups: list[str] | None = None) -> tuple[bool, list[str]]:
    lines: list[str] = []
    ok = True

    r = await client.get("/v3/health/live")
    live = r.status_code == 200
    ok &= live
    lines.append(f"live: {'ok' if live else f'FAIL ({r.status_code})'}")

    r = await client.get("/v3/health", params={"refresh": "true"})
    body: dict[str, Any] = r.json() if r.headers.get("content-type", "").startswith("application/json") else {}
    green = r.status_code == 200 and body.get("status") == "ok"
    ok &= green
    checks = ", ".join(f"{k}={v.get('status')}" for k, v in (body.get("checks") or {}).items())
    lines.append(f"health: {body.get('status', r.status_code)} ({checks})")

    for q in questions or SMOKE_QUESTIONS:
        t0 = time.monotonic()
        try:
            r = await client.post("/v3/chat", json={"message": q, "user_id": user_id, "groups": groups or []})
            env = r.json() if r.status_code == 200 else {}
            passed = env.get("status") in OK_STATUSES and bool((env.get("answer") or "").strip())
            status = env.get("status") or f"http {r.status_code}"
        except httpx.HTTPError as exc:
            passed, status = False, type(exc).__name__
        ok &= passed
        lines.append(f"{'ok  ' if passed else 'FAIL'} {status:<13} {time.monotonic() - t0:6.1f}s  {q}")
    return ok, lines


async def main_async(args: argparse.Namespace) -> int:
    async with httpx.AsyncClient(base_url=args.base_url, timeout=args.timeout) as client:
        ok, lines = await run_smoke(client, args.user_id, groups=args.group)
    print("\n".join(lines))
    print("SMOKE PASSED" if ok else "SMOKE FAILED")
    return 0 if ok else 1


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base-url", default="http://127.0.0.1:8000")
    ap.add_argument("--user-id", required=True, help="test user's Entra object id (mapped in the access file)")
    ap.add_argument("--group", action="append", help="Entra group name (repeatable), if roles map by group")
    ap.add_argument("--timeout", type=float, default=300.0)
    raise SystemExit(asyncio.run(main_async(ap.parse_args())))


if __name__ == "__main__":
    main()
