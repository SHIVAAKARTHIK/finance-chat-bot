"""A rate limiter shaped like slowapi's: it wraps the route function with functools.wraps in ANOTHER module.

FastAPI resolves string annotations (the integration module uses `from __future__ import annotations`) with the wrapper's
`__globals__`, which here is this module, not the integration module. A pass-through lambda in a test cannot reproduce that."""
import functools


def wrapping_limit(fn):
    @functools.wraps(fn)
    async def wrapper(*args, **kwargs):
        return await fn(*args, **kwargs)

    return wrapper
