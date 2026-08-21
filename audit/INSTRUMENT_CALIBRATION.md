# Instrument calibration

The planning brief's entire novelty claim (C3) rests on one sentence: *"Two exhaustive arXiv
full-text sweeps … returned **zero papers that correct, project, repair, or enforce**
revealed-preference consistency on an LLM's choices."*

A zero from a broken instrument is indistinguishable from a zero from an empty literature.
This file calibrates the instrument **before** reporting anything it found, so that the
calibration evidence can be judged independently of the result it produced.

Session G0, 2026-08-21. Instrument source: `scripts/arxiv_ft_search.py`, `scripts/multidb_sweep.py`.

---

## Part 1 — Calibration (written before the re-run numbers)

### 1.1 The redirect trap, reproduced

arXiv's full-text index is not reachable through the REST API — the API's `all:` field
searches metadata only. Full text is behind a legacy endpoint that must be driven by POST:

```
POST https://arxiv.org/search_classic/     query=<q>&searchtype=ft&start=0
```

It answers **HTTP 302** with a `location:` header pointing at `search.arxiv.org`. Measured
directly:

| What the client does | Bytes returned | What it looks like |
|---|---|---|
| Reads the 302 body | **290** | Apache "The document has moved" stub — parses as zero hits |
| Follows the redirect | **11,953** | A real results page: `Displaying hits 1 to 10 of 201.` |

The 290-byte stub contains no hit markers, so a naive parser scores it as an empty
literature. This is the single most likely explanation for an inherited zero, and it is
reproduced here rather than assumed.

### 1.2 True-empty is distinguishable from instrument error

| Condition | HTTP | Bytes | `Full Text Search` in page | `Displaying hits` | `No Results.` |
|---|---|---|---|---|---|
| Real hits (`Afriat`) | 200 | 11,953 | yes | yes | no |
| Genuine zero (`zzqxwv nonexistent phrase kkjjhh`) | 200 | 2,840 | yes | no | **yes** |
| Redirect stub (unfollowed) | 302 | 290 | **no** | no | no |

The instrument therefore returns three statuses and never collapses them:

- `OK` — results page with a count line; the count is trustworthy *subject to §1.5*.
- `EMPTY` — results page carrying the No-Results marker; a genuine zero.
- `ERROR` — anything else. **An ERROR is an instrument gap and is never reported as a zero.**

### 1.3 Positive controls

Distinctive phrases from papers independently confirmed to exist via the arXiv REST API:

| Control query | Expected paper | Hits | Returned it? |
|---|---|---|---|
| `"rationality shift"` | 2501.18190 | 1 | **PASS** |
| `"Maximum Entropy Blackwell Winner"` | 2602.19041 | 1 | **PASS** |
| `"The Emergence of Economic Rationality of GPT"` | 2305.12763 | 132 | **PASS** |
| `"Can Revealed Preferences Clarify LLM Alignment and Steering"` | 2605.08556 | 3 | **PASS** |
| `"GARP-EFM"` | 2603.23993 | 2 | **PASS** |
| `"When Agents Disagree With Themselves"` | 2602.11619 | 12 | **PASS** |
| `"Revealed Rationality"` | 2608.05015 | 4 | **PASS** |
| `"Attention Is All You Need"` | 1706.03762 | 234 | **FAIL** — returned only citing papers |
| `"Denoising Diffusion Probabilistic Models"` | 2006.11239 | 251 | **FAIL** — returned only citing papers |

**6 of 8.** Both failures are pre-2021 landmarks, and in both cases the search returned
hundreds of papers that *cite* them without returning the paper itself. Two consequences,
both load-bearing:

1. **The index includes reference lists.** A hit on `Afriat` may be a paper that merely cites
   Afriat in its bibliography, not a paper about Afriat. Hit counts overstate topical relevance.
2. **The index is incomplete for older material.** Absence of an old paper from this index is
   not evidence the paper does not exist.

Quoted strings behave as exact-phrase queries (1 hit for a unique phrase); unquoted strings
behave loosely (`rationality shift` → 256). Boolean `AND` / `OR` are honoured.

### 1.4 The ligature trap

PDF text extraction preserves typographic ligatures — `ﬁ`, `ﬂ`, `ﬀ`, `ﬃ` — as single
codepoints. A grep for `identification` silently misses `identiﬁcation`. Every full-text
search in this session normalises ligatures and applies NFKC folding before matching
(`normalise()` in `scripts/arxiv_ft_search.py`), and any zero-hit grep over extracted PDF
text is confirmed by a second method before absence is concluded.

### 1.5 The counts are NOT census counts — the most important caveat

`quantum` returns **485** hits across the whole of arXiv. arXiv holds hundreds of thousands
of quantum papers. The legacy full-text index is a **partial index**, so:

> Every hit count in this file is a **lower bound on a partial corpus**, not a census.
> A hit is strong evidence of presence. A zero is **weak** evidence of absence.

This alone is fatal to the word "exhaustive" in the brief's sentence. No search of this
endpoint is exhaustive, whatever number it returns.

---

## Part 2 — The re-run, with the calibrated instrument

The brief's two sweeps, re-run verbatim:

| Sweep | Brief's number | **Calibrated number** | Factor |
|---|---|---|---|
| `"revealed preference" AND "language model"` | 18 | **162** | ×9.0 |
| `GARP OR Afriat` | 33 | **202** | ×6.1 |

Supporting measurements:

| Query | Hits |
|---|---|
| `"revealed preference"` | 210 |
| `GARP` | 200 |
| `Afriat` | 201 |
| `("GARP" OR "Afriat") AND "language model"` | 45 |
| `"GARP" AND "large language model"` | 16 |
| `"Afriat" AND "large language model"` | 15 |
| `"CCEI" AND "language model"` | **5** |
| `"GARP-consistent"` | 7 |
| `"minimal perturbation" AND "revealed preference"` | 3 |
| `"CCEI" AND "penalty"` | 3 |

**The brief's inherited numbers are wrong by roughly an order of magnitude in both sweeps.**
They are consistent with a run that read the 290-byte redirect stub for most queries, or with
a metadata-only search mistaken for a full-text one. Either way the sweep that produced C3 was
uncalibrated, and C3 cannot rest on it.

Note the shape of the corrected numbers: the *broad* counts are large, but the *tight*
intersection `"CCEI" AND "language model"` is **5** — 2608.05015, 2607.20937, 2501.18190,
2505.21371, 2305.12763. The literature that computes Afriat-style efficiency indices on
language models really is small. The brief's conclusion about the size of the field was
directionally defensible; its evidence for it was not.

---

## Part 3 — Instrument gaps

Recorded as gaps, never as zeros.

| Endpoint | Status | Detail |
|---|---|---|
| arXiv full-text (legacy) | **PARTIAL** | Works, calibrated, but indexes only part of the corpus and includes bibliographies. See §1.3, §1.5. |
| Crossref | **USABLE, COUNT MEANINGLESS** | `query.bibliographic` is a loose OR; reports millions of "results". Only the relevance-ranked top-k is informative. |
| OpenAlex | **USABLE AFTER BACKOFF** | Returned HTTP 429 on first contact; succeeds with exponential backoff (now implemented). |
| Semantic Scholar | **GAP** | Persistent HTTP 429 on the anonymous endpoint across every attempt, including after backoff. Matches the brief's preflight warning. **No S2 evidence was obtained this session.** |
| Unpaywall | **USABLE** | Requires `&email=` inline on every request (no config slot in this build). |
| Europe PMC | **USABLE, LOW RELEVANCE** | Works, but the corpus is biomedical; returns near-noise for this topic. |
| EconPapers (RePEc) | **GAP** | Returns HTTP 200 with ~16.5 KB of JS-driven shell, or HTTP 503 under repeat load. Results render client-side. Not retrievable headlessly, and this session is headless by instruction. |
| IDEAS (RePEc) | **GAP** | Same failure mode — HTTP 200, ~16.5 KB, results injected client-side. |
| NBER | **USABLE, COUNT MEANINGLESS** | JSON API works (`totalResults` 16,873 for a two-word query = loose OR). Top-k only. |

**The RePEc family is the most consequential gap.** It is the main index for exactly the
economics working-paper literature where a revealed-preference repair method would most
plausibly appear outside arXiv, and it could not be searched headlessly. That gap is not
closed by anything else in this session.

---

## Part 4 — What the calibrated instrument actually found

### 4.1 The intervention exists — outside the vocabulary the brief searched

**Chadwick, A., Kahng, A. & Kipper, J. (2025), "Dutch books and money pumps: rectifying
vulnerabilities in LLMs through rationality."** 5th International Conference on Human and
Artificial Rationality (HAR), Paris. 19 pp. Retrieved and read in full this session.

They build, and empirically evaluate, **a dedicated inference-time "rationality layer"** that:

- queries the LLM for all pairwise comparisons, reads token probabilities as weighted edges in
  a majority graph, and applies a voting rule (Iterative Max Di-Cut, benchmarked against
  Kemeny) to return a **transitive ranking** — i.e. it repairs intransitive preferences;
- separately takes the model's incoherent probability estimates and solves a **quadratic
  program** to return the nearest coherent distribution — i.e. a minimum-distance projection
  onto the coherent set;
- explicitly requires the output be *"sufficiently faithful to those provided by the LLM"* —
  the same bounded-perturbation criterion the brief proposes;
- composes the two into a unified layer over cardinal utilities.

This was invisible to the brief's sweeps for two reasons, both structural: it is **not on
arXiv** (so no arXiv sweep of any quality would find it), and it is written in
social-choice and philosophy vocabulary — **zero occurrences** of GARP, Afriat, CCEI,
"revealed preference", "budget", "projection", or "perturbation" in 19 pages.

**Consequence for C3:** the claim *"the field measures; it does not intervene"* is **false as
written**. Inference-time repair of an LLM's preference intransitivity, with a faithfulness
constraint, is published and has empirical results.

**What survives:** the specific instantiation the brief proposes — GARP/Afriat efficiency over
budget-set demand data, with CCEI as the measure and Houtman–Maks and money-pump as
companions — is *not* what Chadwick et al. do. They never touch prices, income, budget sets,
or demand data; transitivity of pairwise menu choices is a weaker and different condition than
GARP over a demand system.

**What is strengthened:** Chadwick et al.'s own §5 names the brief's claim C2 as *open*, in
their words: it will be crucial to measure how their approach affects the model's accuracy and
calibration, and it "has yet to be determined how useful our system is in real-world
scenarios." An independent group building the neighbouring intervention and flagging the
downstream-quality question as unanswered is direct corroboration that C2 is unoccupied.

### 4.2 A second adjacent occupant

**arXiv:2505.07883** — Zhu, Yan & Griffiths, "Recovering Event Probabilities from Large
Language Model Embeddings via Axiomatic Constraints." Recovers *coherent* event probabilities
from LLM embeddings by imposing the probability axioms. Same move (enforce an axiom system on
incoherent model output), different axiom system. Not fetched in full this session — recorded
as a lead, status `unverified`.

### 4.3 Nothing found that does the GARP/budget-set version

Across every query in Part 2 and a further battery (`"GARP" AND "projection"`,
`"enforce" AND "GARP"`, `"repair" AND "GARP"`, `"GARP-consistent"`,
`"minimal perturbation" AND "revealed preference"`, `"inference-time" AND "revealed
preference"`, `"rationalizable" AND "language model"`), every returned candidate was triaged
by abstract and none proposes minimal-perturbation projection of an agent's demand data onto
the GARP-consistent set. The nearest neighbours are:

- **arXiv:2603.23993** (Aguiar & Kashaev, GARP-EFM) — a *training-time* intervention:
  fine-tunes a time-series foundation model on GARP-consistent synthetic data. Intervention,
  not measurement, and the brief's ledger did not record what it does.
- **arXiv:2608.05015** (Andrews) — training-time penalty, theory only. See `killcheck_E1.md`.

Given §1.5, this is **weak** evidence of absence and must be reported as such.
