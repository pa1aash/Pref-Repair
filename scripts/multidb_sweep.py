#!/usr/bin/env python3
"""
Multi-database literature sweep with explicit gap accounting.

Every endpoint returns one of:
    OK     -- a parsed response; `count` and `sample` are trustworthy
    EMPTY  -- a parsed response with zero records; a genuine zero
    GAP    -- 403 / bot-wall / rate-limit / timeout / unparseable

A GAP is never collapsed into a zero. That distinction is the whole point of this file:
"the endpoint said nothing" and "the endpoint said none" are different facts, and only one
of them is evidence about the literature.

Unpaywall requires an email on every request and this build has no config slot for it, so it
is inlined at the call site.
"""
from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field

UA = "pref-repair-audit/0.1 (mailto:palaashgang@gmail.com)"
EMAIL = "palaashgang@gmail.com"


@dataclass
class DBResult:
    source: str
    query: str
    status: str                       # OK | EMPTY | GAP
    count: int | None = None
    sample: list[str] = field(default_factory=list)
    detail: str = ""

    def line(self) -> str:
        if self.status == "GAP":
            return f"  [GAP]   {self.source:<16} {self.detail}"
        n = "0" if self.status == "EMPTY" else str(self.count)
        return f"  [{self.status:<5}] {self.source:<16} n={n}"


def _get(url: str, timeout: int = 45, headers: dict | None = None,
         retries: int = 3) -> tuple[int, bytes, str]:
    """GET with exponential backoff on 429/503. A rate limit that survives the backoff is
    reported as an error, not retried forever and not silently turned into an empty result."""
    last = (0, b"", "no attempt")
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read(), ""
        except urllib.error.HTTPError as e:
            last = (e.code, b"", f"HTTP {e.code} {e.reason}")
            if e.code in (429, 503) and attempt < retries:
                time.sleep(5 * (2 ** attempt))
                continue
            return last
        except Exception as e:                               # noqa: BLE001
            last = (0, b"", f"{type(e).__name__}: {e}")
            if attempt < retries:
                time.sleep(3 * (attempt + 1))
                continue
            return last
    return last


def _json_db(source, query, url, count_path, items_path, title_key, headers=None) -> DBResult:
    code, body, err = _get(url, headers=headers)
    if code != 200:
        return DBResult(source, query, "GAP", detail=err or f"HTTP {code}")
    try:
        d = json.loads(body)
    except Exception as e:                                   # noqa: BLE001
        return DBResult(source, query, "GAP", detail=f"unparseable JSON: {e}")
    cur = d
    for k in count_path:
        cur = cur.get(k, {}) if isinstance(cur, dict) else {}
    count = cur if isinstance(cur, int) else None
    items = d
    for k in items_path:
        items = items.get(k, []) if isinstance(items, dict) else []
    if not isinstance(items, list):
        items = []
    titles = []
    for it in items[:8]:
        t = it.get(title_key)
        if isinstance(t, list):
            t = t[0] if t else None
        if t:
            titles.append(" ".join(str(t).split())[:110])
    if count == 0 or (count is None and not items):
        return DBResult(source, query, "EMPTY", count=0)
    return DBResult(source, query, "OK", count=count if count is not None else len(items),
                    sample=titles)


def crossref(q):
    u = ("https://api.crossref.org/works?rows=8&select=title,DOI,issued&query.bibliographic="
         + urllib.parse.quote(q) + f"&mailto={EMAIL}")
    return _json_db("Crossref", q, u, ["message", "total-results"], ["message", "items"], "title")


def openalex(q):
    u = ("https://api.openalex.org/works?per-page=8&search=" + urllib.parse.quote(q)
         + f"&mailto={EMAIL}")
    return _json_db("OpenAlex", q, u, ["meta", "count"], ["results"], "title")


def semantic_scholar(q):
    u = ("https://api.semanticscholar.org/graph/v1/paper/search?limit=8&fields=title,year"
         "&query=" + urllib.parse.quote(q))
    return _json_db("SemanticSchol", q, u, ["total"], ["data"], "title")


def europepmc(q):
    u = ("https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&pageSize=8&query="
         + urllib.parse.quote(q))
    return _json_db("EuropePMC", q, u, ["hitCount"], ["resultList", "result"], "title")


def unpaywall_doi(doi):
    # Unpaywall is a DOI-resolution service, not a search engine: used to check OA status.
    u = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={EMAIL}"
    code, body, err = _get(u)
    if code != 200:
        return DBResult("Unpaywall", doi, "GAP", detail=err or f"HTTP {code}")
    try:
        d = json.loads(body)
    except Exception as e:                                   # noqa: BLE001
        return DBResult("Unpaywall", doi, "GAP", detail=f"unparseable: {e}")
    loc = d.get("best_oa_location") or {}
    return DBResult("Unpaywall", doi, "OK", count=1,
                    sample=[f"oa={d.get('is_oa')} title={str(d.get('title'))[:70]} "
                            f"url={loc.get('url_for_pdf') or loc.get('url')}"])


def repec_ideas(q):
    # EconPapers / IDEAS share the RePEc corpus. Both are HTML-only; a bot-wall is a GAP.
    u = "https://econpapers.repec.org/scripts/search.pf?ft=" + urllib.parse.quote(q)
    code, body, err = _get(u)
    if code != 200:
        return DBResult("EconPapers", q, "GAP", detail=err or f"HTTP {code}")
    text = body.decode("utf-8", "replace")
    import re
    m = re.search(r"(?:found|about|)\s*([\d,]+)\s*(?:papers?|items?|results?|hits?|matches)", text, re.I)
    if m:
        return DBResult("EconPapers", q, "OK", count=int(m.group(1).replace(",", "")))
    if re.search(r"(?:no|0)\s+(?:papers|items|matches|results|hits)|nothing found", text, re.I):
        return DBResult("EconPapers", q, "EMPTY", count=0)
    return DBResult("EconPapers", q, "GAP",
                    detail=f"HTML parsed but no count marker ({len(text)} bytes)")


def nber(q):
    u = "https://www.nber.org/api/v1/working_page_listing/contentType/working_paper/_/_/search?page=1&perPage=8&q=" + urllib.parse.quote(q)
    return _json_db("NBER", q, u, ["totalResults"], ["results"], "title")


ENGINES = [crossref, openalex, semantic_scholar, europepmc, repec_ideas, nber]


def sweep(query: str, pause: float = 1.5) -> list[DBResult]:
    out = []
    for fn in ENGINES:
        r = fn(query)
        out.append(r)
        print(r.line(), flush=True)
        for s in r.sample[:4]:
            print(f"          - {s}", flush=True)
        time.sleep(pause)
    return out


if __name__ == "__main__":
    import sys
    for q in sys.argv[1:]:
        print(f"\n=== {q!r}")
        sweep(q)
