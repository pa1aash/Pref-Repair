# Item 3 — RePEc/IDEAS, diagnosed and searched

*Resolves `docs/OPEN_QUESTIONS.md` Q12 and corrects two rows of
`audit/INSTRUMENT_CALIBRATION.md` Part 3. Headless HTTP only; no browser was opened.
77 queries run across the two RePEc front-ends.*

---

## What the prior session concluded, and whether it was right

The prior session recorded:

> | EconPapers (RePEc) | **GAP** | Returns HTTP 200 with ~16.5 KB of JS-driven shell, or HTTP 503 under repeat load. Results render client-side. Not retrievable headlessly […] |
> | IDEAS (RePEc) | **GAP** | Same failure mode — HTTP 200, ~16.5 KB, results injected client-side. |

**This was wrong, and the error was one of inspection, not of capability.**

EconPapers serves **static server-rendered HTML**. There is no client-side rendering of results
anywhere in the stack. The ~16.5 KB body the prior session measured was real, and it was not a
"shell" — it was the **fully-rendered Advanced Search form**, with a visible instruction in it:

> `<h1 class='colored'>Advanced Search</h1>`
> `<p><b>Please run the search by clicking on Search.</b></p>`

The page even echoes the parsed query back in an HTML comment (`ft Afriat`), proving the server
read the parameter and *chose* not to search. Two things were missing from the request, neither of
them JavaScript:

1. a **`Referer` header** from a `econpapers.repec.org` page, and
2. for anything beyond a bare `ft=`, the form's hidden **`adv=true`** field.

Supply both and the same endpoint returns `<h1>Search Results</h1>` and
`<b>222 documents matched the search for Afriat.</b>` — a plain `<ol>` of `<li>` items linking
`/paper/…` and `/article/…`, with authors, series, year, keywords and JEL codes inline.

The "JS-rendered" verdict was reached, per the accusation, by stripping tags and grepping for the
word *"result"*. That method was guaranteed to fail: **a successful EconPapers search never uses the
word "result"** in its results banner (it says "documents matched"), and **a genuine zero never uses
it either** (it says "No matching documents when searching for …"). The detector could not have
returned true on any input. The 503s were real but incidental — an IIS rate limiter that clears in
seconds, not a wall.

IDEAS was also misdiagnosed, for a different reason: the endpoint the session tried
(`/cgi-bin/htsearch`, GET) is a **retired stub**. IDEAS moved search to `/cgi-bin/htsearch2` over
**POST**. The stub returns a real page containing a real, empty search form — again server-rendered,
again not a shell. POST to the current endpoint and IDEAS answers
`Found 212 results for Afriat, showing 1-10`.

**Net effect on the audit.** RePEc — named in Q12 as *"the most likely place for a fourth occupant
to be hiding"* and the single most consequential recorded gap — was reachable headlessly the whole
time. It has now been searched. The cost estimate in Q12 ("one interactive browser session, or a
RePEc bulk-data download") was also wrong in both branches: no browser is needed, and the
bulk-data route is dead (see Diagnosis).

---

## Diagnosis

Every row below is an actual request made this session. "Bytes" is `size_download` from curl.

| Endpoint | Method | HTTP | Bytes | What the body actually contained | Verdict |
|---|---|---|---|---|---|
| `econpapers.repec.org/scripts/search.pf?ft=Afriat` | GET, no `Referer` | 200 | 16,550 | Complete Advanced Search **form**; `<h1>Advanced Search</h1>`; "Please run the search by clicking on Search."; HTML comment echoing `Referer:` (empty), `Count: 1`, `ft Afriat`. No `<script>` that writes results. | **wrong-parameters / missing Referer** — not JS |
| same URL | GET, `Referer: https://econpapers.repec.org/` | 200 | 19,525 | `<h1>Search Results</h1>`; `<b>222 documents matched the search for Afriat.</b>`; `Documents 1 to 20, page 1 of 12`; `<ol start='1'>` of 20 `<li>` items with `/paper/` and `/article/` hrefs, authors, series, year, keywords, JEL. Comment reveals a **Solr** backend: `Raw query: q=%28Afriat%29&rows=20&sort=score+desc&wt=json`. | **WORKS** |
| same URL | GET, `Referer: https://example.com/` | 200 | 16,570 | The form again. | **referer guard** (off-site rejected) |
| same URL | GET, `Referer: …/scripts/search.pf` | 200 | 16,596 | The form again — referring page *is* the search page, so it is treated as arriving at the form, not submitting it. | **needs `adv=true`** |
| `…/search.pf?ft=Afriat&adv=true&sort=rank&lgc=AND&nit=epdate&inpage=100` | GET, `Referer: …/scripts/search.pf` | 200 | 59,352 | `222 documents matched`; `Documents 1 to 100`. | **WORKS** (advanced mode, all fields live) |
| `…&adv=true&wp=on&inpage=100` | GET, `Referer: …/scripts/search.pf` | 200 | 65,482 | `117 documents matched` — working papers only. | **WORKS** (type filter live) |
| `…/search.pf?ft=<nonsense>&adv=true…` | GET, correct Referer | 200 | ~16,700 | `Advanced Search` + **`No matching documents when searching for "zzqqxx nonexistent phrase"`** — query echoed verbatim. | **WORKS — explicit zero** |
| same, immediately repeated (<5 s apart) | GET | **503** | 27 | Literal body: `The service is unavailable.` (IIS). Clears within ~10–30 s. | **transient rate limit**, not a wall |
| `ideas.repec.org/cgi-bin/htsearch?q=Afriat` | GET | 200 | 16,573 | Server-rendered IDEAS search page with an **empty** form whose `action="/cgi-bin/htsearch2"` and `method="POST"`. Banner: "IDEAS is struggling with massive bot traffic, please be patient." | **retired endpoint** — not JS |
| `ideas.repec.org/cgi-bin/htsearch2` | **POST** `q=Afriat` (+ `form=extended`, `wm=wrd`, `dt=range`, `wf`, `s`, `ul`, `db`, `de`) | 200 | 37,524 | `Found 212 results for Afriat, showing 1-10`; `<ol class="list-group">` of `<li class="list-group-item …">` items, each `AUTHORS (YEAR): <a>TITLE</a><hr>ABSTRACT<br><i>RePEc:handle</i>`. | **WORKS** |
| `ideas.repec.org/n/nep-ain/` | GET | 200 | 28,329 | Plain static archive index for NEP-AIN (Artificial Intelligence), listing every weekly issue with paper counts. | **WORKS** |
| `ideas.repec.org/getdata.html` | GET | 200 | 23,050 | The official bulk-access documentation (Guilford Protocol, ReDIF, remi, `RePEc:all`). Also states: *"We want to discourage you strongly to scrape the data from the websites."* | **WORKS** (docs only) |
| `oai.repec.org/?verb=Identify` | GET | 200 | 3,703 | **Not an OAI-PMH response.** Generic hosting placeholder page titled `Siche.openlib.org`. | **DEAD** |
| `rsync.repec.org/` | GET | 200 | 3,703 | Same placeholder page. | **DEAD** |
| `ftp://ftp.repec.org/opt/ReDIF/RePEc/` | FTP LIST | — | 0 | Connection timed out after 25 s (curl exit 28). | **DEAD** |
| `ftp://all.repec.org/RePEc/all/` | FTP LIST | — | 0 | Connection timed out after 25 s. | **DEAD** |

**The bulk-data branch of Q12's cost estimate is not available.** All four documented bulk routes —
OAI-PMH, rsync, and both FTP archives — are dead or misconfigured. The search front-ends are, as of
this session, the *only* working RePEc access route, which makes the prior misdiagnosis more
consequential than it looked: it was not one of two options, it was the only one.

---

## The working route, if any

Both front-ends work. Recipe, for reproduction:

**EconPapers (preferred — richer filters, larger pages, explicit hit counts)**

```
GET https://econpapers.repec.org/scripts/search.pf?<params>
Referer: https://econpapers.repec.org/scripts/search.pf     # required
User-Agent: <any normal browser UA>
```

Required param: `adv=true`. Useful params, all read from the live form:

| Param | Meaning |
|---|---|
| `ft` | free-text search (goes into Solr `q` wrapped in parentheses; supports quoted phrases and `AND`/`OR`) |
| `kw` | keywords + title only |
| `aus` | author (quote the surname — unquoted multi-word input is a loose OR and returns garbage) |
| `jel` | JEL code |
| `nep` | restrict to items ever listed in a NEP report (`nepain`, `nepupt`, `nepcbe`, `nepexp`, `nepdcm`, `nepmic`, …) |
| `wp` / `art` / `bkchp` / `soft` | type filters (`on`) |
| `inpage` | results per page, up to 1000 |
| `pg` | page number |
| `sort` | `rank` / `date` / `name`; `lgc` = `AND`/`OR` across textboxes |

A bare `ft=` with a `Referer` of any *other* econpapers page (e.g. the site root) also works — that
is the sidebar quick-search path — but it accepts no other parameters.

**IDEAS (useful cross-check — searches abstracts and returns abstract text)**

```
POST https://ideas.repec.org/cgi-bin/htsearch2
Referer: https://ideas.repec.org/search.html
q=<query>&form=extended&wm=wrd&dt=range&wf=4BFF&s=R&ul=&db=&de=&np=<0-based page>
```
`wf`: `4BFF` whole record / `F000` abstract / `0F00` keywords / `00F0` title / `000F` author.
`ul`: `%/p/%` papers, `%/a/%` articles. 10 results per page, fixed.

**Rate limiting.** EconPapers throttles to HTTP 503 under bursts. All requests this session were
paced ~12 s apart with exponential backoff on 503, per RePEc's request that its servers not be
hammered. IDEAS tolerated ~8 s spacing. Any systematic sweep should keep this pacing.

**Reading a zero correctly.** EconPapers returns `No matching documents when searching for <query
echoed verbatim>`; IDEAS returns `Found 0 results`. Both are explicit, both echo the query, and both
are distinguishable from the form-returned and 503 failure modes. Every zero reported below was
confirmed against a deliberate nonsense-query control (`EP-23`) that produced byte-identical
structure — so these are *the endpoint saying none*, not the endpoint saying nothing.

---

## Searches actually run, and hits

**EconPapers** (`n` = server-reported match count; zeros verified against the control)

| # | Query (free text unless noted) | Hits | Notable titles |
|---|---|---|---|
| EP-01 | `GARP` | 201 | canonical RP corpus; incl. Shiozawa NP-hardness note |
| EP-02 | `"Houtman-Maks" OR "Houtman Maks"` | 16 | Heufer & Hjertstrand; Demetry & Hjertstrand (Stata `hmindex`); Demuynck & Rehbeck |
| EP-03 | `CCEI OR "critical cost efficiency index"` | 19 | Echenique, *On the meaning of the CCEI*; Dziewulski; Polisson & Quah |
| EP-04 | `"revealed preference" AND (LLM…)` | **9** | Seror, *The Moral Mind(s) of Large Language Models*; Kashaev, Plávala & Aguiar, *Entangled vs. Separable Choice* |
| EP-05 | `GARP AND (LLM…)` | **0** | — (verified zero) |
| EP-06 | `"revealed preference" AND "artificial intelligence"` | 21 | Coupé (Canterbury WP 24/13); Serenko (2010) |
| EP-07 | `rationality AND "artificial intelligence" AND repair` | 1 | irrelevant (image-repair theory) |
| EP-08 | `("minimum cost"…) AND "revealed preference"` | 14 | Dean & Martin (*REStat* 2016); **Shiozawa, NP-hardness of the minimum cost index**; Demuynck & Rehbeck |
| EP-09 | `"revealed preference" AND (repair OR rectify OR correcting)` | 63 | all human-consumer-data; no AI |
| EP-10 | `"revealed preference" AND (projection OR project)` | 181 | no AI |
| EP-11 | `GARP AND (projection OR projecting)` | 5 | all false positives (species-distribution "GARP" algorithm) |
| EP-12 | `(rationalizable OR rationalize…) AND "language model"` | 18 | **Cook, Kazinnik, Modig & Palmer, *What Do LLMs Want?*** (both versions) |
| EP-13 | `"money pump" AND (LLM / AI)` | **0** | — (verified zero) |
| EP-14 | `"LLM agent" OR "AI agent"…` | 617 | broad; triaged by title |
| EP-15 | `(LLM…) AND preference AND (consistency OR coherence OR transitivity OR rationality)` | 40 | Lu et al.; Bini et al.; Biancotti et al. |
| EP-16 | `Afriat AND (ML / AI / "language model" / neural)` | 2 | 1 false positive; 1 = Andrews (below) |
| EP-17 | `GARP AND ("machine learning" OR AI)` | 1 | false positive (flood-hazard "GARP") |
| EP-18 | `"revealed preference" AND "machine learning"` | 30 | Basu & Echenique; Bolletta et al. |
| EP-19 | `"GARP-consistent" OR enforce/impose/restore AND GARP` | 8 | **Aguiar & Kashaev, GARP-EFM** (already ledger R5); Geanakoplos; Heufer |
| EP-20 | `perturbation AND ("revealed preference" OR GARP)` | 14 | all human data |
| EP-21 | `("inference-time" OR "post-hoc" OR decoding) AND (RP / GARP / "utility maximization")` | 5 | all false positives |
| EP-22 | `(nearest / closest / "minimum distance") AND (rationalizable / GARP)` | 78 | no AI intersection |
| EP-23 | **nonsense control** | **0** | zero-page format captured |
| EP-24/25 | re-runs of EP-05 / EP-13 | **0 / 0** | zeros confirmed twice |
| EP-26 | `(steering / "control vector" / activation) AND (rationality / preferences) AND LLM` | 8 | **Cook et al.**; Raman et al. (*STEER*, ledger-known) |
| EP-27 | `(dose OR dose-response) AND LLM` | 3 | none relevant — **no dose–response study of LLM rationality exists on RePEc** |
| EP-28 | `(nearest / closest / minimal / projection) AND (rationalizable / "GARP-consistent") AND AI` | 7 | none relevant |
| EP-29 | `("choice consistency" / "internal consistency") AND AI` | 54 | psychometrics, not RP |
| EP-30 | `(Varian/swaps/Afriat index / CCEI / Houtman-Maks) AND AI` | **0** | — (verified zero) |
| EP-31 | `(repair/correct/rectify/debias/enforce) AND (choices/preferences) AND AI AND rational` | 30 | Echenique et al. (response time); Ludwig, Mullainathan & Rambachan |
| EP-32 | `(payoff/welfare/performance) AND (coherence/consistency/rationality) AND AI AND (trade-off/cost)` | 31 | none relevant |

**EconPapers author sweeps** (surname `aus=` ∧ AI vocabulary, `lgc=AND`)

| Author | Hits | Anything on AI? |
|---|---|---|
| Aguiar | 24 | yes — GARP-EFM; *Entangled vs. Separable Choice* |
| Kashaev | 2 | yes — same two |
| Echenique | 5 | yes — *Response Time Enhances Alignment with Heterogeneous Preferences* (2026) |
| Crawford | 29 | no (name collisions only) |
| Quah | 3 | no (*Estimating Very Large Demand Systems* is ML-adjacent, not AI-choice) |
| Demuynck / Cherchye | 1 / 1 | no (*Identifying Marriage Markets*) |
| Daniel Martin | 15 | no (name collisions) |
| Hjertstrand, Smeulders, Polisson, Heufer, Halevy, Mark Dean | **0 each** | **no** — six verified zeros |

**EconPapers NEP-report sweeps** (items ever listed in the named report)

| Report | Query | Hits |
|---|---|---|
| NEP-AIN (Artificial Intelligence) | RP / GARP / Afriat / rationality / utility-max / transitivity | **54** |
| NEP-MIC (Microeconomics) | AI ∧ (RP / GARP / Afriat) | **2** — Suleymanov; Kashaev–Plávala–Aguiar |
| NEP-UPT (Utility Models & Prospect Theory) | AI vocabulary | 127 |
| NEP-CBE (Cognitive & Behavioural) | AI vocabulary | 111 |
| NEP-DCM (Discrete Choice Models) | AI vocabulary | 152 |
| NEP-EXP (Experimental) | AI vocabulary | 500 |

**IDEAS** (independent index and ranker; searches abstract text)

| # | Query | Hits | Notable |
|---|---|---|---|
| ID-01 | `"revealed preference" "large language model"` | 5 | Seror; Chen et al. |
| ID-02 | `GARP "language model"` | **0** | — |
| ID-03 | `"revealed preference" "artificial intelligence"` | 12 | Coupé; Bonanno |
| ID-04 | `rationality "artificial intelligence" repair` | **0** | — |
| ID-05 | `CCEI` | 14 | Echenique; Dziewulski; Polisson & Quah |
| ID-06 | `"Houtman-Maks"` | 12 | Hjertstrand; Demuynck & Rehbeck; De Rock–Smeulders–Cherchye–Spieksma |
| ID-07 | `"revealed preference" violations minimum cost` | 2 | Dean & Martin |
| ID-08 | `LLM preferences consistency` | 46 | **Cook et al.**; Kim, Kovach, Lee & Shin; Liu, Tang, Yang & Tam |
| ID-09 | `rationalizable "language model"` | 2 | **Cook et al.** (both versions) |
| ID-10 | `"money pump" LLM` | **0** | — |
| ID-11 | `"revealed preference" "machine learning"` | 17 | Basu & Echenique |
| ID-12 | `Afriat "artificial intelligence"` | 1 | false positive |
| ID-13 | `"Entangled vs. Separable Choice"` | 2 | Kashaev, Plávala & Aguiar |
| ID-14 | `LLM steering rationality preferences` | **0** | — |
| ID-15 | `repair rationality choices language model` | 1 | false positive |
| ID-16 | `projection rationalizable set choices` | **0** | — |
| ID-17 | `correcting inconsistent choices artificial intelligence` | 1 | false positive |
| ID-18 | **`Afriat LLM`** | **1** | **Andrews, *Revealed Rationality*** |
| ID-19 | `GARP "AI agent"` | **0** | — |
| ID-20 | `CCEI "language model"` | **0** | — |

Five further IDEAS lookups (X1–X5) were title-verification fetches for the new items below.

---

## Anything that repairs revealed-preference consistency on AI agents

### The direct answer

**No.** Across 77 queries on both RePEc front-ends, **nothing was found that takes an AI agent's
observed choice sequence and projects it onto the rationalizable (GARP-consistent) set** — not at
inference time, not by minimal perturbation, not scored against an exogenous payoff, and not
along a dose–response curve. Queries EP-05, EP-13, EP-30, ID-02, ID-16, ID-19 and ID-20 — the ones
that name the projection idea most directly — are **verified zeros**, confirmed against a
nonsense-query control that reproduces the zero-page byte structure exactly.

### Calibration: the route reproduces the audit's known anchor

The single hit on IDEAS query `Afriat LLM` is **Andrews, *Revealed Rationality: Label-Free
Evaluation and Regularization from Representation Theorems*, arXiv:2608.05015**, already ledger
row **R4**. RePEc independently surfaces the audit's central occupant from a two-word query. That
is the strongest available evidence that the route is now working and that its zeros mean
something.

### Six items RePEc surfaced that are absent from `audit/REFERENCE_LEDGER.md`

Ranked by how close they come to the occupied cell. **None does minimal-perturbation projection.**

**1. Cook, Kazinnik, Modig & Palmer, *What Do LLMs Want?* — the most consequential find.**
Federal Reserve Bank of Kansas City Research Working Paper **RWP 25-19** (2025),
DOI 10.18651/RWP2025-19, `RePEc:fip:fedkrw:102166`; reissued as Federal Reserve Board
**Finance and Economics Discussion Series 2026-006**, DOI 10.17016/FEDS.2026.006,
`RePEc:fip:fedgfe:102439`. **Not on arXiv.** This is exactly the object Q12 predicted would be
hiding on RePEc: a central-bank working paper, in economics vocabulary, invisible to any arXiv
sweep of any quality. From the abstract:

> "We study LLM preferences **as revealed by their choices** in simple allocation games and a
> job-search setting. […] we find these preferences are **malleable: reframing** (e.g., masking
> social context) **and learned control vectors shift choices toward payoff-maximizing behavior,
> while personas move them less effectively.** […] Extending a McCall job search environment, we
> also recover effective discounting from accept/reject policies, but observe that **model
> responses may not always be rationalizable**, and in some cases suggest inconsistent
> preferences."

Why it matters, on three separate fronts:

- **It is an intervention, not just a measurement.** It steers an agent's economic choices with
  **learned control vectors** — a representation-level intervention with a natural continuous
  strength parameter — and evaluates the result against **payoff-maximizing behavior**, an
  exogenous benchmark not derived from the preference data. That is two of the three legs of the
  cell `docs/OPEN_QUESTIONS.md` Q1 calls unoccupied.
- **It does not close the cell.** Steering a representation is not projecting a fixed choice
  sequence onto the rationalizable set; there is no Afriat/GARP machinery, no CCEI, no
  minimum-perturbation objective, and no dose–response curve — the reported result is
  directional ("shift toward", "less effectively"), not a traced frontier.
- **It bears directly on Q2.** Independently of this audit, it finds that **reframing moves LLM
  economic behaviour and personas move it less effectively.** Q2 proposes restating the S4 gate
  around framing rather than persona on exactly that reasoning. This is third-party corroboration
  from a Fed working paper, and it should be cited in the Q2 resolution.

**2. Bini, Cong, Huang & Jin, *Behavioral Economics of AI: LLM Biases and Corrections*.**
**NBER Working Paper 34745** (2026), `RePEc:nbr:nberwo:34745`; also arXiv:2602.09362.
"Do generative AI models […] exhibit systematic behavioral biases in economic and financial
decisions? If so, **how can these biases be mitigated?**" — the most comprehensive bias battery to
date plus mitigation. The corrections are prompt-level, not projection. Note that
`audit/INSTRUMENT_CALIBRATION.md` records NBER as "USABLE, COUNT MEANINGLESS"; the NBER endpoint
was queried but its top-k never surfaced this. RePEc did.

**3. Lu, Dhanda, Chen & Hansen, *Aligning Large Language Model Agents with Rational and Moral
Preferences: A Supervised Fine-Tuning Approach*.** arXiv:2507.20796 (2025).
"We document that off-the-shelf LLM agents exhibit **systematic deviations from payoff-sensitive
behavior** in canonical economic games […] We introduce a **supervised fine-tuning approach that
aligns agent behavior with explicit economic preferences.**" A **training-time** intervention on
economic rationality — the same family as ledger row R5 (GARP-EFM), and a second occupant of the
training-time cell. It appears in the repository only as a bibliography line inside
`research/notes/the-innate-economic-preferencesof-language-models.md`; it was never triaged.

**4. Suleymanov, *A Revealed Preference Framework for AI Alignment*.** arXiv:2603.27868 (2026).
Luce-mixture identification of whether a delegated AI implements the principal's preferences or
its own. Identification, not repair.

**5. Kops & Tsakas, *Choice via AI*.** arXiv:2602.04526 (2026). An acyclicity condition under
which an AI's menu recommendations are rationalizable by a monotonic interpretation plus a strict
preference relation. Axiomatic characterisation, not repair.

**6. Gao, Jiang & Yan, *Debiasing LLMs by Fine-tuning*.** arXiv:2604.02921 (2026). LoRA-based SFT
against rational benchmark forecasts; explicitly notes prompt-based approaches are limited. Again
training-time, and again about extrapolation bias rather than GARP.

Also newly surfaced and not in the ledger: **Echenique, Fallah, Huang & Jordan, *Response Time
Enhances Alignment with Heterogeneous Preferences*** (arXiv:2605.06987, 2026) — a known RP author
working on LLM alignment, though via response-time identification, not repair; and
**Liu, Tang, Yang & Tam, *Evaluating and Aligning Human Economic Risk Preferences in LLMs***
(arXiv:2503.06646, 2025) — "we propose an **alignment method** designed to enhance LLM adherence
to persona-specific risk preferences […] improves the **economic rationality** of LLMs."

### One find that bears on Q3, not on occupancy

**Shiozawa, *Note on the goodness-of-fit measure for GARP; NP-hardness of minimum cost index*.**
Osaka University Discussion Paper 15-18, `RePEc:osk:wpaper:1518`; journal version in *Economics
Bulletin* 35(4), 2015. Abstract in full:

> "The purpose of this paper is to show that the problem of computing minimum cost index (MCI),
> which is proposed by Dean and Martin (2010, 2015) as a goodness-of-fit measure of GARP, is
> **NP-hard**. We show the result by using a reduction from maximum acyclic subgraph problem
> (MASP) which is a traditional decision problem known to be NP-complete."

This is directly load-bearing for `docs/OPEN_QUESTIONS.md` Q3 (*"Are the Afriat inequalities
actually linear under the intended parameterisation?"*). The minimum-cost-of-violations objective
— the most natural formalisation of "minimum-cost repair" — is **NP-hard**, and the hardness comes
from precisely the combinatorial structure Q3 identifies: the search over orderings/acyclic
subgraphs, not the inner LP. Demuynck & Rehbeck (*Economic Theory* 76(4), 2023, "Computing revealed
preference goodness-of-fit measures with integer programming") is the corresponding
state-of-the-art solver and is also absent from the ledger. Both should be read before the solver
is written.

### What this does to the occupancy picture

The interventions that exist in the economics working-paper literature fall into four families,
and RePEc now confirms all four are occupied:

| Family | Occupants found | On arXiv? |
|---|---|---|
| Penalty / regularizer from a representation theorem | Andrews (R4) | yes |
| Training-time fine-tuning toward rational behaviour | Aguiar & Kashaev (R5); Lu et al.; Gao et al. | yes |
| Prompt / reframing correction | Bini et al.; Cook et al. | partly |
| Representation-level steering | Cook et al. (control vectors); Yamin et al. (R3) | partly |

**The fifth family — inference-time minimal-perturbation projection of an observed choice sequence
onto the rationalizable set, scored against an exogenous payoff, traced as a dose–response curve —
remains empty on RePEc.** Query EP-27 confirms the sharpest part of this: **no paper on RePEc
traces a dose–response curve for LLM rationality at all.** Q1's characterisation of the remaining
cell survives contact with the economics working-paper literature.

---

## Residual gap

What was searched is now searched. What remains open, stated as gaps rather than zeros:

1. **Coverage is top-k, not exhaustive, on the broad queries.** Seven queries returned more hits
   than the 100-item retrieval page (EP-01 201, EP-10 181, EP-14 617, NEP-UPT 127, NEP-CBE 111,
   NEP-DCM 152, NEP-EXP 500). Only the top 100 by Solr relevance were retrieved and triaged for
   each. A paper with weak term-frequency on the query terms but a strong on-topic abstract could
   sit below the cut. The
   narrow, decisive queries (EP-04, EP-05, EP-16, EP-19, EP-26, EP-28, EP-30) all returned fewer
   than 10 hits and were triaged exhaustively, so this gap does not touch the central finding.

2. **Titles and keywords, not full text.** EconPapers' `ft` searches RePEc **metadata** — title,
   abstract, keywords, JEL — not the PDF body. A working paper whose abstract never says
   "revealed preference", "GARP", "Afriat", "rationalizable" or "CCEI" but whose §4 does the
   projection would be invisible here, exactly as Chadwick et al. was invisible to the brief's
   arXiv sweeps (`audit/INSTRUMENT_CALIBRATION.md` §4.1). This is the same structural blind spot,
   not a new one, and RePEc cannot close it.

3. **RePEc indexes what publishers deposit.** Series that do not participate in RePEc are absent
   by construction. SSRN in particular is only partially represented, and EconStor, while
   participating, was not separately swept. Neither was searched directly this session — recorded
   as an untouched gap, not a zero.

4. **Bulk access is dead, so no offline verification is possible.** OAI-PMH, rsync and both FTP
   archives return placeholder pages or time out. There is therefore no way to confirm the
   completeness of the Solr index against the underlying ReDIF corpus, and no way to run an
   exhaustive regex sweep over all RePEc metadata. If a systematic, reproducible sweep is ever
   required, the route would have to be negotiated with RePEc directly (`getdata.html` asks that
   scrapers contact them), not scripted.

5. **Rate limiting bounds throughput.** EconPapers 503s under bursts; sustainable throughput is
   roughly 5 queries/minute with backoff. This session's 77 queries took approximately 40 minutes
   of wall clock. Any substantially larger sweep needs a time budget, not a new method.

**`audit/INSTRUMENT_CALIBRATION.md` Part 3 should be amended**: the two RePEc rows move from
**GAP** to **USABLE**, with the operative note being the `Referer` + `adv=true` requirement on
EconPapers and the `htsearch2`/POST migration on IDEAS, and with the rate limiter recorded as a
throughput constraint rather than a wall. The claim that *"the RePEc family is the most
consequential gap […] that gap is not closed by anything else in this session"* is no longer true
of this session's successor: the gap is closed, and closing it cost one afternoon of paced HTTP.
