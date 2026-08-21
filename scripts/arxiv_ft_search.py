#!/usr/bin/env python3
"""
arXiv full-text search instrument.

The arXiv REST API's `all:` field searches metadata only (title / abstract / authors).
Full text lives behind the legacy endpoint, which must be driven by POST and which
answers with a 302 to search.arxiv.org. The 302 body is a ~290-byte Apache stub; a
client that reads it instead of following the redirect sees no hits and mistakes that
for an empty literature. This module follows the redirect and refuses to report a
count unless it can positively identify a full-text results page.

Three outcomes are distinguished, and they are NOT interchangeable:

    OK        a real results page; `count` is trustworthy
    EMPTY     a real results page that says "No Results." — a genuine zero
    ERROR     anything else (stub, bot-wall, timeout, unrecognised markup).
              An ERROR is an instrument gap. It is never reported as a zero.
"""

from __future__ import annotations

import html
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from dataclasses import dataclass, field

ENDPOINT = "https://arxiv.org/search_classic/"
UA = "pref-repair-audit/0.1 (mailto:palaashgang@gmail.com)"

# Markers that identify a genuine full-text results page rather than a stub or error.
PAGE_MARKER = "Full Text Search"
EMPTY_MARKER = "No Results."
COUNT_RE = re.compile(r"Displaying hits (\d+) to (\d+) of (\d+)")
HIT_RE = re.compile(r"https?://arxiv\.org/abs/([0-9]{4}\.[0-9]{4,5})")

# Ligatures that PDF extraction leaves in text. A naive substring search for
# "identification" will miss "identi<fi-ligature>cation". Normalise before matching.
LIGATURES = {
    "ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi",
    "ﬄ": "ffl", "ﬅ": "st", "ﬆ": "st",
}


def normalise(text: str) -> str:
    """NFKC-fold and expand ligatures so substring matching is not defeated by them."""
    for lig, plain in LIGATURES.items():
        text = text.replace(lig, plain)
    text = unicodedata.normalize("NFKC", text)
    return text


@dataclass
class Result:
    query: str
    status: str                      # OK | EMPTY | ERROR
    count: int | None = None
    ids: list[str] = field(default_factory=list)
    titles: list[str] = field(default_factory=list)
    detail: str = ""

    def __str__(self) -> str:
        if self.status == "OK":
            return f"[OK]    {self.count:>5} hits   {self.query!r}"
        if self.status == "EMPTY":
            return f"[EMPTY]     0 hits   {self.query!r}   (genuine zero)"
        return f"[ERROR]     ? hits   {self.query!r}   -- {self.detail}"


def _post(query: str, start: int, timeout: int) -> str:
    data = urllib.parse.urlencode(
        {"query": query, "searchtype": "ft", "start": str(start)}
    ).encode()
    req = urllib.request.Request(ENDPOINT, data=data, headers={"User-Agent": UA})
    # urllib follows the 302 automatically and re-issues as GET, which is what
    # search.arxiv.org expects.
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read()
        return raw.decode(resp.headers.get_content_charset() or "utf-8", "replace")


def search(query: str, start: int = 0, timeout: int = 60, retries: int = 2) -> Result:
    page = ""
    for attempt in range(retries + 1):
        try:
            page = _post(query, start, timeout)
            break
        except Exception as exc:                      # noqa: BLE001 - report, never swallow
            if attempt == retries:
                return Result(query, "ERROR", detail=f"{type(exc).__name__}: {exc}")
            time.sleep(3 * (attempt + 1))

    page = normalise(page)

    if PAGE_MARKER not in page:
        return Result(
            query, "ERROR",
            detail=f"not a full-text results page ({len(page)} bytes) -- "
                   f"redirect stub, bot-wall, or markup change",
        )

    m = COUNT_RE.search(page)
    if m:
        ids, titles = _extract_hits(page)
        return Result(query, "OK", count=int(m.group(3)), ids=ids, titles=titles)

    if EMPTY_MARKER in page:
        return Result(query, "EMPTY", count=0)

    return Result(query, "ERROR",
                  detail="results page with neither a count line nor a No-Results marker")


def _extract_hits(page: str) -> tuple[list[str], list[str]]:
    ids = list(dict.fromkeys(HIT_RE.findall(page)))
    text = html.unescape(re.sub(r"<[^>]+>", "\x01", page))
    titles = []
    for chunk in text.split("\x01"):
        chunk = chunk.strip()
        if 25 < len(chunk) < 200 and chunk.count(" ") > 3 and "arxiv.org" not in chunk:
            titles.append(chunk)
    return ids, titles[:40]


def search_all(query: str, cap: int = 200, page_size: int = 10) -> Result:
    """Page through results up to `cap` hits, collecting every arXiv id."""
    first = search(query)
    if first.status != "OK":
        return first
    ids = list(first.ids)
    total = min(first.count or 0, cap)
    for start in range(page_size, total, page_size):
        nxt = search(query, start=start)
        if nxt.status != "OK":
            first.detail += f" [pagination stopped at {start}: {nxt.detail}]"
            break
        ids.extend(i for i in nxt.ids if i not in ids)
        time.sleep(1.0)
    first.ids = ids
    return first


if __name__ == "__main__":
    for q in sys.argv[1:]:
        r = search(q)
        print(r)
        if r.ids:
            print("        first ids:", ", ".join(r.ids[:10]))
