# Step 8 — corpus-critic gap-fill results

Seven gaps identified, all attempted by three parallel fetchers. **No gap produced a source that
overturns the frozen positioning in `docs/FRAMING.md`.** One produced a source that materially
changes the confidence on a committed position, and it is reported below rather than absorbed.

## Gap outcomes

| Gap | Priority | Outcome | Effect on committed positions |
|---|---|---|---|
| `seventh-occupant-fulltext-venues` | critical | **NOT FOUND, with real instrument gaps** | Occupancy position *unchanged*; confidence NOT raised, because four of six venues were walled |
| `identification-closing-source-c2` | critical | **NOT FOUND** after a genuinely multi-front search | **C2 strengthened.** Adversarial search for a fixed-model + exogenous-outcome study returned nothing |
| `per-model-ccei-reliability` | critical | **FOUND — and it cuts both ways** | See "The one finding that changes something" below |
| `second-dose-response-curve-exogenous-payoff` | critical | **NOT FOUND** | Dose-axis contribution *strengthened*. 0 forward citations on both anchor papers |
| `poise-citation-forward-cycle-extension` | critical | **NOT FOUND**, verified four independent ways | **`FRAMING.md` §5.1 defence holds.** POISE has 0 citations (OpenAlex, Semantic Scholar, two full-text routes); Chadwick has exactly 1 (Andrews), which does not extend it |
| `minimum-perturbation-complexity` | high | **CONFIRMED OPEN**, and two access gaps closed | Method position *strengthened by verification* |
| `econstor-ssrn-central-bank-sweep` | high | **Mixed** — central-bank sweep worked, repositories walled | Occupancy position unchanged |

## The one finding that changes something

**arXiv:2505.21371** (Wang et al., "When Experimental Economics Meets Large Language Models") is the
first source anywhere in this corpus to measure **per-model CCEI stability on LLMs rather than
humans**. Four fixed models, 100 independent runs each of the same 25-round budget-set task, so a
genuine across-run distribution rather than a point estimate.

| Manipulation (model held fixed) | Effect on CCEI |
|---|---|
| Multi-turn → single-turn dialogue | Qwen2.5-7B **0.980 → 0.739**; Llama-3.1-8B **0.953 → 0.841** (both p < 0.01). **GPT-4o and DeepSeek-V3 essentially unaffected** |
| Open-ended → multiple-choice answer format | Qwen 0.980 → 0.902; Llama 0.953 → 0.853 |
| Persona conditioning | **No significant CCEI sensitivity** |
| Temperature 0 → 1 | **No significant CCEI sensitivity** |

Corroborated independently by the Fed paper (Cook, Kazinnik, Modig & Palmer, FEDS 2026-006), now
fetched in full: larger models are rationalizable far more often, the smallest model is "not
rationalizable at all", and a reasoning variant scores *worse* than its non-reasoning sibling.

**Two consequences, in opposite directions.**

1. **Tension 1 partially resolves in the project's favour.** The reliability worry was that CCEI's
   format sensitivity and its construct validity are the same variable. On the two flagship models,
   format sensitivity is *absent* — so their CCEI is stable across administration changes, and a
   dose axis can exist for them. The `PNAS` human finding does not transfer wholesale to models.
2. **But the same data undercuts a frozen precondition.** `docs/FRAMING.md` §6 precondition 2
   requires "framing/format headroom on a current frontier model". This source says format effects
   are concentrated in *small* models and that the frontier models tested were unmoved. If that
   holds for 2026 frontier models, the headroom lever the project switched to may not exist where
   it is needed. **This is a contradiction with the frozen framing and is reported, not patched.**

Also newly confirmed against the frozen text: **persona does not move CCEI** in this study either,
which independently corroborates kill-check E2's finding that the persona lever cannot carry the
gate — and the Fed paper's finding that reframing moves behaviour more than personas do.

## Access gaps, recorded as gaps and never as zeros

Four of the six new venues could not be searched, so their silence is not evidence:

- **ACL Anthology** — the `/search/` page is a client-side Google CSE widget; no server-rendered
  results even through a headless browser. Direct CSE API calls are bot-blocked.
- **PhilPapers** — Cloudflare interstitial, 403, via curl and headless browser alike.
- **EconStor** — Anubis proof-of-work bot wall, as predicted. The DSpace REST API is reachable but
  ignores the `query` parameter; `/rest/discover/search/objects` is 404; OAI-PMH is harvest-only.
- **SSRN** — Cloudflare 403 via both routes.
- **OpenReview** — worked, but is a title/abstract DBLP-integrated index, **not** PDF full text, and
  its non-phrase OR-token matching caps at 1000 results. Verified: `"money pump"` returns 1000 hits,
  none of which actually contain the phrase. Its zeros are weak evidence.

**So the "seventh occupant" risk is NOT retired.** The specific blind spot the corpus critic named —
full-text venues — remains almost entirely unsearched, because the full-text venues are the ones
that bot-wall headless clients. This must be stated as a residual risk in the final report.

## Two vault bugs found and fixed en route

- The Andrews full text (arXiv:2608.05015) was misfiled under a colliding note id `1introduction`
  that actually pointed at an unrelated paper. Fixed, re-synced, summarised, 7 claims extracted.
- `hyperresearch repair` had auto-created a stub note from a literal `[[$x]]` example inside a
  quoted prompt template in another note. Removed.

## Access gaps closed

- **Varian (1985)** — previously an access gap, recovered via a Wayback capture of a dead
  institutional URL and read in full.
- **Demuynck & Rehbeck (2023)** — OA working-paper PDF obtained. **§6 confirmed: the Average
  Quantity Error, the exact continuous quantity-perturbation objective this project needs, is
  sketched in two sentences with no inequalities, no MILP and no complexity classification**, in
  contrast to the fully worked Average Price Error. The gap the method note identified is real.
- **Chen, Lanier & Quah** (arXiv:2405.08464) — full text obtained. Confirms Proposition 1
  (non-closedness) is a **well-posedness** result and that the paper gives **no** complexity result
  for the LS index. The open-complexity statement in `docs/METHOD_NOTE_Q3.md` is correct as written.
- **Halevy, Persitz & Zrill** — 2013 working-paper draft obtained; the parametric alternative that
  sidesteps non-minimizability.
- **Shiozawa (2015)** — primary source for the MCI NP-hardness claim, read in full. Confirms the
  reduction but is scoped to relation *deletion*, not quantity perturbation, so it does not close
  the open question — it only corroborates the citation.
