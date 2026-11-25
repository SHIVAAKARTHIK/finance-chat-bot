"""Small BM25 index (no dependencies). Embeddings can be added later behind the same interface."""
from __future__ import annotations

import math
import re
from collections import Counter

_TOKEN = re.compile(r"[a-z0-9]+")

STOPWORDS = frozenset(
    """a an and are as at be by can do does did each for from give had has have how i in into is it its me my
    of on or our show tell that the their there these this those to us was we were what when where which who whom
    why will with you your please list many much all across per any get find""".split()
)


def stem(token: str) -> str:
    if len(token) > 4 and token.endswith("ies"):
        return token[:-3] + "y"
    if len(token) > 3 and token.endswith("s") and not token.endswith(("ss", "us")):
        return token[:-1]
    return token


def tokenize(text: str) -> list[str]:
    """Lowercase words; underscores split words; stopwords and bare numbers dropped; light stemming."""
    out = []
    for tok in _TOKEN.findall(text.lower().replace("_", " ")):
        if tok in STOPWORDS or tok.isdigit():
            continue
        out.append(stem(tok))
    return out


class BM25Index:
    def __init__(self, docs: dict[str, list[str]], *, k1: float = 1.5, b: float = 0.75):
        self.k1, self.b = k1, b
        self.docs = {doc_id: Counter(tokens) for doc_id, tokens in docs.items()}
        self.lengths = {doc_id: sum(c.values()) for doc_id, c in self.docs.items()}
        n = len(self.docs) or 1
        self.avg_len = (sum(self.lengths.values()) / n) or 1.0
        df: Counter[str] = Counter()
        for counts in self.docs.values():
            df.update(counts.keys())
        self.idf = {t: math.log(1 + (n - f + 0.5) / (f + 0.5)) for t, f in df.items()}

    def score(self, query_tokens: list[str], doc_id: str) -> float:
        counts = self.docs[doc_id]
        length = self.lengths[doc_id]
        total = 0.0
        for t in set(query_tokens):
            tf = counts.get(t, 0)
            if not tf:
                continue
            denom = tf + self.k1 * (1 - self.b + self.b * length / self.avg_len)
            total += self.idf.get(t, 0.0) * tf * (self.k1 + 1) / denom
        return total

    def search(self, query: str, k: int = 5, allowed: set[str] | None = None) -> list[tuple[str, float]]:
        q = tokenize(query)
        if not q:
            return []
        scored = [
            (doc_id, self.score(q, doc_id)) for doc_id in self.docs if allowed is None or doc_id in allowed
        ]
        scored = [s for s in scored if s[1] > 0]
        scored.sort(key=lambda s: (-s[1], s[0]))
        return scored[:k]
