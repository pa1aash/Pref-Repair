# hyperresearch run record — revealed-preference-repair-llm-4f6896

## Where the run stopped

**Step 2 of 16 (width sweep), partially complete.** The run did not fail its way to a stop; it was
stopped deliberately — see `docs/DECISIONS.md` D8. Two things happened in the same window and they
should not be confused:

1. **The STOP CONDITION fired** (D7). Phases C and E had already answered the question this run
   existed to answer, so steps 3–16 would have re-derived a settled conclusion.
2. **Three of ten fetchers died independently**, for machine reasons, not research reasons. The
   host went to sleep mid-response, killing batches 2 and 8, and batch 6 stalled behind a
   watchdog timeout.

Had the STOP CONDITION not fired, the correct response to (2) would have been to re-dispatch the
three dead batches. It did fire, so the corpus was kept as-is.

## Steps completed

| Step | Status | Artefact |
|---|---|---|
| Bootstrap | complete | `query.md`, `scaffold.md`, vault tag minted, step skills installed |
| 1 — decompose | **complete** | `prompt-decomposition.json` (14 sub-questions, 14 entities, 9 required headings), `coverage-matrix.md` (zero gap rows) |
| 2 — width sweep | **partial** | `search-plan.md` (44 planned searches, 3 lenses, 9 adversarial), `scored-urls.md`, `SOURCE_INDEX.md` — 72 sources fetched |
| 3–16 | **not run** | Stopped by decision, not by failure |

Tier was classified **`full`** by step 1, so all 16 steps were in scope. Steps 3–16 were skipped
deliberately; this is a recorded deviation from the pipeline's tier gate, not a silent drop.

## Coverage assessment for the partial sweep

72 sources against 14 sub-questions. Coverage by atomic item, judged from the source index:

| Atomic item | Status |
|---|---|
| Interventions: inference-time | **adequate** — the three known occupants plus neighbours |
| Interventions: training-time | **adequate** — Andrews, GARP-EFM, the RLHF-side penalties |
| GARP / WARP / SARP as axiom systems | **adequate** |
| Afriat efficiency methods | **adequate** |
| Varian goodness-of-fit | **thin** — batch 8 died before resolving Varian (1990); OA access failed on every route |
| Houtman–Maks | **thin** — batch 6 stalled before resolving it |
| Money-pump index (Echenique/Lee/Shum) | **thin** |
| Coherence theorems and their critiques | **adequate** — though the strongest single source (Zhi-Xuan et al., *Philosophical Studies* 2024) came from kill-check E5, not from this sweep |
| Bradley-Terry violations in RLHF | **well-covered** |
| Nash learning from human feedback | **well-covered** |
| Downstream decision quality after enforcement | **adequate**, mostly via E5 rather than via this sweep |
| Minimal-perturbation restoration | **thin** |

**Genuine gaps left open:** the three classical economics references (Varian 1990, Houtman & Maks
1985, Echenique–Lee–Shum) were not obtained in full text by this sweep. Two of them are behind
paywalls with no open-access copy. They remain `unverified` in `audit/REFERENCE_LEDGER.md` and
must not be cited as though they had been read.

## What the corpus is good for

It is the prior-art reading list the paper now needs, given that the novelty framing has to be
rebuilt (`docs/VENUE.md`, fit audit). The highest-value unread items are R20 (`arXiv:2406.00231`,
LLM-RankFusion) and R22 (`arXiv:2604.17502`, the completeness-violation agent paper) — both
surfaced by kill-check E5 and neither yet read in full.
