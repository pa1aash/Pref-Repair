# Precondition check — does published data already answer GATE ONE?

`docs/GO_NOGO_ASSESSMENT.md` gave a **QUALIFIED YES**, conditional on a pilot securing two numbers.
`docs/FRAMING.md` §6 states them as preconditions 1 and 2. This document asks whether either is already
answered in the literature, so that the pilot does only the work that is genuinely outstanding.

Two papers can plausibly bear on this, and both were read in full for this check:

- **arXiv:2505.21371**, "When Experimental Economics Meets Large Language Models: Tactics with Evidence"
  — the only source anywhere in this corpus that repeats a fixed budget-set task 100 times per model.
  Extraction: `audit/EXTRACT_2505_21371.md`.
- **Cook, Kazinnik, Modig & Palmer, "What Do LLMs Want?"** — KC Fed RWP 25-19 / FEDS 2026-006, the
  economics-front paper found only after correcting a broken search instrument.
  Extraction: `audit/EXTRACT_KCFED.md`.

---

## Precondition 1 — stable per-model CCEI across re-runs

> *"CCEI test–retest on the target models, fixed budget sets, fresh contexts, K≥5 re-runs, with ICC and
> WSCV reported. If per-model CCEI is as unstable as Nitsch's humans, the dose axis does not exist and
> the paper does not get written."* — `docs/FRAMING.md` §6

### Verdict: **GENUINELY OPEN. Not answered, and — importantly — not answered by the one paper that could have answered it.**

arXiv:2505.21371 runs **100 independent simulations per model per domain per condition**. That is far
more repetition than the K≥5 the precondition asks for. The data to compute test–retest reliability
therefore *exists* inside that study. **It is never reported.**

What the paper reports is the **mean CCEI per condition**, and then two-sample t-tests comparing means
**across formats**. It reports no standard deviation, no variance, no ICC, no coefficient of variation,
and no confidence interval for the CCEI distribution **within** a fixed model-and-format cell. The single
within-format dispersion statistic anywhere in the paper — normalised SD of 0.054 / 0.030 / 0.218 / 0.110
across the four models, against 0.231 for humans — belongs to Case Study 2 and describes **raw game
choices, not CCEI**.

**This is the distinction G0.5 warned about, and it must not be repeated here.**
`audit/ITEM2_occupants_B.md` established that the human-subjects reliability literature conflates two
different questions:

| | Manipulation | Question answered |
|---|---|---|
| **Test–retest reliability** | same model, **same** format, repeated | does the score come back the same? |
| **Format sensitivity** | same model, **different** format | does the score change when you change the ask? |

arXiv:2505.21371 measures the **second** and not the first. A prior summary of it in this repository
described it as "the first per-model reliability study on language models"; on a full read that
characterisation is **too generous** and is corrected here. It is a per-model **format-sensitivity**
study with the reliability computation left undone.

**Consequence for the pilot, and it is a favourable one.** The outstanding work is small and precisely
defined: repeat a fixed budget-set task on a fixed model in a fixed format, and report the dispersion.
That is one afternoon of local compute and it fills a genuine reporting gap rather than duplicating a
published number.

---

## Precondition 2 — framing-induced headroom on a current frontier model

> *"Framing/format headroom on a current frontier model — not persona."* — `docs/FRAMING.md` §6

### Verdict: **PARTIALLY ANSWERED, and the answer is more equivocal than either the optimistic or the pessimistic reading of it.**

Three corrections to how this repository has been describing arXiv:2505.21371.

**(a) "Flagship" is not the paper's word, and its split is by parameter count, not by proprietary status.**
The paper's own operative division, from its conclusion, is between *"two open-source models with small
parameter sizes, Llama and Qwen"* and *"GPT and DeepSeek."* DeepSeek-V3 is itself classified as
open-source in the paper's own background table. So the contrast is **7–8B versus very large**, and
`audit/HR_PARTIAL_S1/FRAMING_CONTRADICTIONS.md` C-2's use of "flagship" imported a distinction the source
does not draw.

**(b) The format effects in the small models are large and real.**

| Model | Domain | Multi-turn → single-turn | Δ |
|---|---|---|---|
| Qwen2.5-7B | risk | 0.980 → 0.739 | **−0.241** |
| Qwen2.5-7B | social | 0.994 → 0.889 | −0.105 |
| Llama-3.1-8B | risk | 0.953 → 0.841 | −0.112 |
| Llama-3.1-8B | social | 0.968 → 0.756 | **−0.212** |

All four at p < 0.01. There is abundant headroom at the 7–8B scale.

**(c) "Essentially unmoved" is a magnitude judgment, not a failed significance test — and this cuts both
ways.** GPT-4o and DeepSeek-V3 shift by only **0.001–0.006**, but **three of those four cells are still
statistically significant at p < 0.01**, including one where the reported means both round to 1.000. So
the large models are not *statistically* unmoved; they are *practically* unmoved. With 100 runs per cell,
significance is cheap and effect size is what matters. An effect of 0.003 leaves nothing for a projection
operator to work on, whatever its p-value.

### What this means, stated as a real possibility rather than managed

**The dose axis may exist mainly at smaller model scales.** That is the honest reading of (b) and (c)
together, and it is reinforced from the economics side: the KC Fed paper finds that **larger models are
rationalizable far more often**, that the smallest model it tested *"is not rationalizable at all"*, and
that its largest model *"produces a policy with an appropriate reservation wage nearly all the time."*
Both papers point the same way — **incoherence is concentrated in smaller models.**

**This is a legitimate and citable finding, not a failure.** If enforced-coherence repair has measurable
headroom only below some scale, that is a substantive result about where the intervention is useful, and
it is directly relevant to practitioners deploying small open-weight models in agentic settings — which
is a large and growing population. It should be tested directly rather than assumed in either direction.

It also **improves** the feasibility of a zero-cost pilot: the models where the effect plausibly lives
are exactly the ones that run on local hardware.

### One caution against over-reading the scale story

The KC Fed paper's rationalizability metric is **not GARP**. It is a bespoke three-part test defined only
for a McCall job-search environment — fit a switching-regime model, require BIC selection, require
p₀ < p₁, require trembling-hand error below 50% — and its results are reported **only as figures plotted
against model size, with no printed percentages**. It is suggestive corroboration of the scale gradient,
not a measurement of CCEI. Its persona result also cuts against a naive scale story: persona
susceptibility measured by fixed-effects R² is 0.025–0.056 for most models but **0.648 for its largest**,
so conditioning effects do not simply vanish with scale.

---

## Summary

| Precondition | Status | What is outstanding |
|---|---|---|
| **1 — stable per-model CCEI across re-runs** | **OPEN** | Everything. The one study with enough repetition never computed the dispersion. Pilot must measure it. |
| **2 — framing headroom on a *frontier* model** | **PARTIALLY ANSWERED, and probably negatively for very large models** | Headroom at 7–8B is established (Δ up to −0.241, p<0.01). At very large scale the effect is 0.001–0.006 — statistically detectable, practically negligible. |

**Net effect on pilot scope: less work, not more, and a sharper question.** Precondition 2 no longer
needs establishing at 7–8B — it is published. What the pilot must do is (i) compute the test–retest
dispersion nobody has computed, and (ii) check whether the published format effect reproduces at the
*even smaller* scales that run locally, which would extend the scale gradient downward and sharpen the
"where does the dose axis live" question.
