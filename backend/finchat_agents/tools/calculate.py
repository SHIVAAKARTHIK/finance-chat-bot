"""calculate: a restricted expression evaluator over returned rows. No imports, attributes, files or network.

The expression is parsed with `ast` and walked node by node; only arithmetic, comparisons, boolean logic,
literals, names, subscripts, comprehensions and a short list of functions are allowed. Earlier run_sql results are
available by result id (r1, r2, ...) as lists of row dicts; extra values come in `variables`.
"""
from __future__ import annotations

import ast
import math
import operator
import statistics
from decimal import Decimal
from typing import Any

from ..llm.types import ToolSpec
from ..runtime.tools import Tool, ToolContext, ToolError
from .run_sql import RESULTS_KEY

CALC_KEY = "calc_results"  # RunContext.extras[CALC_KEY] = [values], used by the number check
MAX_EXPRESSION_CHARS = 2000
MAX_SEQUENCE = 100_000
MAX_EXPONENT = 100
MAX_STEPS = 1_000_000


def _avg(xs):
    xs = list(xs)
    return sum(xs) / len(xs) if xs else None


def _pct(part, total):
    return None if not total else 100.0 * part / total


def _pct_change(old, new):
    return None if not old else 100.0 * (new - old) / abs(old)


FUNCTIONS = {
    "sum": sum, "min": min, "max": max, "abs": abs, "round": round, "len": len,
    "avg": _avg, "mean": _avg, "median": lambda xs: statistics.median(list(xs)),
    "pct": _pct, "pct_change": _pct_change, "sorted": sorted, "int": int, "float": float,
    "sqrt": math.sqrt, "any": any, "all": all, "list": list, "set": lambda xs: sorted(set(xs), key=str),
}

_BIN = {
    ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv, ast.Mod: operator.mod, ast.Pow: operator.pow,
}
_CMP = {
    ast.Eq: operator.eq, ast.NotEq: operator.ne, ast.Lt: operator.lt, ast.LtE: operator.le,
    ast.Gt: operator.gt, ast.GtE: operator.ge, ast.In: lambda a, b: a in b, ast.NotIn: lambda a, b: a not in b,
}


class CalcError(Exception):
    pass


def _plain(v: Any) -> Any:
    """Decimals become floats so they mix with float arithmetic."""
    if isinstance(v, Decimal):
        return float(v)
    if isinstance(v, dict):
        return {k: _plain(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [_plain(x) for x in v]
    return v


class _Evaluator:
    def __init__(self, names: dict[str, Any]):
        self.scopes = [names]
        self.steps = 0

    def lookup(self, name: str) -> Any:
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        if name in FUNCTIONS:
            return FUNCTIONS[name]
        raise CalcError(f"unknown name '{name}'")

    def ev(self, node: ast.AST) -> Any:
        self.steps += 1
        if self.steps > MAX_STEPS:
            raise CalcError("expression is too expensive")
        method = getattr(self, f"_{type(node).__name__}", None)
        if method is None:
            raise CalcError(f"'{type(node).__name__}' is not allowed")
        return method(node)

    def _Expression(self, n):
        return self.ev(n.body)

    def _Constant(self, n):
        if isinstance(n.value, (int, float, str, bool)) or n.value is None:
            return n.value
        raise CalcError("only numbers, strings, booleans and None are allowed as literals")

    def _Name(self, n):
        return self.lookup(n.id)

    def _List(self, n):
        return [self.ev(e) for e in n.elts]

    def _Tuple(self, n):
        return tuple(self.ev(e) for e in n.elts)

    def _Dict(self, n):
        return {self.ev(k): self.ev(v) for k, v in zip(n.keys, n.values)}

    def _UnaryOp(self, n):
        v = self.ev(n.operand)
        if isinstance(n.op, ast.USub):
            return -v
        if isinstance(n.op, ast.UAdd):
            return +v
        if isinstance(n.op, ast.Not):
            return not v
        raise CalcError("operator not allowed")

    def _BinOp(self, n):
        op = _BIN.get(type(n.op))
        if op is None:
            raise CalcError("operator not allowed")
        a, b = self.ev(n.left), self.ev(n.right)
        if isinstance(n.op, ast.Pow) and isinstance(b, (int, float)) and abs(b) > MAX_EXPONENT:
            raise CalcError("exponent too large")
        if isinstance(n.op, ast.Mult) and (isinstance(a, (str, list)) or isinstance(b, (str, list))):
            raise CalcError("repeating strings or lists is not allowed")
        try:
            return op(a, b)
        except ZeroDivisionError:
            return None

    def _BoolOp(self, n):
        if isinstance(n.op, ast.And):
            v = True
            for e in n.values:
                v = self.ev(e)
                if not v:
                    return v
            return v
        v = False
        for e in n.values:
            v = self.ev(e)
            if v:
                return v
        return v

    def _Compare(self, n):
        left = self.ev(n.left)
        for op, comp in zip(n.ops, n.comparators):
            right = self.ev(comp)
            if not _CMP[type(op)](left, right):
                return False
            left = right
        return True

    def _IfExp(self, n):
        return self.ev(n.body) if self.ev(n.test) else self.ev(n.orelse)

    def _Subscript(self, n):
        target = self.ev(n.value)
        if isinstance(n.slice, ast.Slice):
            s = n.slice
            return target[slice(*(self.ev(x) if x is not None else None for x in (s.lower, s.upper, s.step)))]
        key = self.ev(n.slice)
        try:
            return target[key]
        except (KeyError, IndexError, TypeError) as exc:
            raise CalcError(f"cannot index with {key!r}: {exc}") from exc

    def _Call(self, n):
        if not isinstance(n.func, ast.Name) or n.func.id not in FUNCTIONS:
            raise CalcError("only these functions are allowed: " + ", ".join(sorted(FUNCTIONS)))
        if n.keywords and not (n.func.id in ("sorted",) and all(k.arg == "reverse" for k in n.keywords)):
            raise CalcError("keyword arguments are not allowed (except sorted(..., reverse=True))")
        args = [self.ev(a) for a in n.args]
        kwargs = {k.arg: self.ev(k.value) for k in n.keywords}
        return FUNCTIONS[n.func.id](*args, **kwargs)

    def _comprehension(self, gens: list[ast.comprehension], emit) -> list:
        out: list = []

        def loop(i: int) -> None:
            if i == len(gens):
                out.append(emit())
                if len(out) > MAX_SEQUENCE:
                    raise CalcError("result is too long")
                return
            g = gens[i]
            if g.is_async:
                raise CalcError("async comprehensions are not allowed")
            for item in self.ev(g.iter):
                scope = self.scopes[-1]
                self._bind(g.target, item, scope)
                if all(self.ev(c) for c in g.ifs):
                    loop(i + 1)

        self.scopes.append({})
        try:
            loop(0)
        finally:
            self.scopes.pop()
        return out

    def _bind(self, target: ast.AST, value: Any, scope: dict) -> None:
        if isinstance(target, ast.Name):
            scope[target.id] = value
        elif isinstance(target, (ast.Tuple, ast.List)):
            values = list(value)
            if len(values) != len(target.elts):
                raise CalcError("cannot unpack")
            for t, v in zip(target.elts, values):
                self._bind(t, v, scope)
        else:
            raise CalcError("only simple loop variables are allowed")

    def _ListComp(self, n):
        return self._comprehension(n.generators, lambda: self.ev(n.elt))

    def _GeneratorExp(self, n):
        return self._comprehension(n.generators, lambda: self.ev(n.elt))

    def _SetComp(self, n):
        return sorted(set(self._comprehension(n.generators, lambda: self.ev(n.elt))), key=str)

    def _DictComp(self, n):
        pairs = self._comprehension(n.generators, lambda: (self.ev(n.key), self.ev(n.value)))
        return dict(pairs)


def evaluate(expression: str, names: dict[str, Any]) -> Any:
    if len(expression) > MAX_EXPRESSION_CHARS:
        raise CalcError(f"expression is longer than {MAX_EXPRESSION_CHARS} characters")
    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError as exc:
        raise CalcError(f"syntax error: {exc.msg}") from exc
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute):
            raise CalcError("attribute access is not allowed")
        if isinstance(node, ast.Name) and node.id.startswith("__"):
            raise CalcError("dunder names are not allowed")
    value = _Evaluator({k: _plain(v) for k, v in names.items()}).ev(tree)
    if isinstance(value, float):
        value = round(value, 10)
    return value


def make_calculate_tool() -> Tool:
    spec = ToolSpec(
        name="calculate",
        description=(
            "Evaluate a small Python-like expression over query results. Earlier run_sql results are available by "
            "result_id (r1, r2, ...) as lists of row dicts, e.g. sum(r['BALANCE'] for r in r1) or "
            "pct_change(r1[0]['n'], r2[0]['n']). Functions: " + ", ".join(sorted(FUNCTIONS)) + ". "
            "Pass extra numbers in 'variables'. Prefer doing arithmetic in SQL when one query can do it."
        ),
        input_schema={
            "type": "object",
            "properties": {
                "expression": {"type": "string"},
                "variables": {"type": "object", "description": "Optional named values (numbers, lists)."},
            },
            "required": ["expression"],
        },
    )

    async def handler(args: dict[str, Any], tctx: ToolContext) -> dict[str, Any]:
        expression = str(args.get("expression") or "").strip()
        if not expression:
            raise ToolError("Give an expression to evaluate.")
        names: dict[str, Any] = {rid: res.records() for rid, res in tctx.run.extras.get(RESULTS_KEY, {}).items()}
        variables = args.get("variables") or {}
        if not isinstance(variables, dict):
            raise ToolError("'variables' must be an object of name: value.")
        for k, v in variables.items():
            if not str(k).isidentifier() or str(k).startswith("__"):
                raise ToolError(f"invalid variable name '{k}'")
            names[str(k)] = v
        try:
            value = evaluate(expression, names)
        except CalcError as exc:
            raise ToolError(f"calculate: {exc}") from exc
        except (TypeError, ValueError, ArithmeticError) as exc:
            raise ToolError(f"calculate failed: {type(exc).__name__}: {exc}") from exc
        tctx.run.extras.setdefault(CALC_KEY, []).append(value)
        return {"expression": expression, "result": value}

    return Tool(spec=spec, handler=handler)
