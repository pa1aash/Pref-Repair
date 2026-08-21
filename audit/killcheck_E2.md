# Kill-check E2 — effect size of persona conditioning on CCEI (arXiv:2501.18190)

Target claim: **S2** ("persona/role prompting substantially degrades GARP compliance"), which is
the sole cited evidence for **C4** (the hard gate: CCEI headroom exists under conditioning).
Brief under test: `docs/F3-PLAN-ORIGINAL.md`, sections "The gap" and "S4 preflight".

Paper: ShuiDe Wen, *Economic Rationality under Specialization: Evidence of Decision Bias in AI
Agents*. Tsinghua Shenzhen International Graduate School. arXiv:2501.18190**v2** [cs.AI],
submitted 30 Jan 2025, revised 17 Mar 2025. 21 pages, single author, no listed venue.

The brief's gate needs a number. The brief supplies the word "substantially". This check
replaces the word with the number, and then asks whether the number can be believed.

---

## Falsifier (stated before the finding)

Committed before opening Table 1. For this paper to retire the C4 gate risk in advance, **two
independent conditions** must both hold — a magnitude condition and a credibility condition.
Either one failing is reported.

**Magnitude thresholds.** Let Δ = (non-persona baseline CCEI) − (persona-conditioned CCEI),
both measured in this paper.

| Finding | Reading |
|---|---|
| Persona CCEI ≥ 0.99, or Δ < 0.005 | **Gate at risk.** The brief's only cited evidence points the wrong way; projection is ~the identity map and S2 is refuted. |
| Δ ∈ [0.005, 0.03), or persona CCEI ∈ (0.97, 0.99) | **Gate unresolved.** Real but marginal; the week-1 pilot decides everything and should be powered for a small effect. |
| Persona CCEI ≤ 0.95 **and** Δ ≥ 0.03 | **Magnitude condition met.** There is something for a projection to move. |

**Credibility conditions.** All four must hold, or a large Δ does not license "confirmed":

- **K1** — the baseline is an *in-study, same-pipeline* non-persona control, not a figure quoted
  from a different paper run on different infrastructure.
- **K2** — some dispersion exists: replications, seeds, SDs, CIs, or a significance test. A point
  estimate with no spread cannot establish that an effect is measurable.
- **K3** — at least one model that is current, or a multi-model set, so the number transfers to
  the brief's "≥3 frontier models across ≥2 families" protocol.
- **K4** — the reported numbers survive internal cross-checks: table against prose against
  figure, and against the arithmetic bounds of the paper's own stated design.

**Mapping committed in advance.** Magnitude met + K1–K4 all hold → HEADROOM CONFIRMED. Magnitude
met + one or more of K1–K4 fails → HEADROOM MARGINAL. Magnitude not met → HEADROOM ABSENT. No
extractable numbers, or K4 failing so completely that even the *sign* is uninterpretable →
CANNOT DETERMINE FROM THIS PAPER.

---

## The numbers

The paper reports exactly one results table and one results figure. There is no other numeric
result anywhere in the 21 pages. Table 1 (p. 11) verbatim, verified three ways — raw text layer,
`blocks` mode with x/y coordinates, and the page rendered at 170 dpi and read directly:

| Subject | Total rounds | GARP violations | Average CCEI | Average Spearman |
|---|---|---|---|---|
| Humans *(quoted from Chen et al. 2023)* | 347 × 25 | 50 | **0.9600** | −0.7500 |
| Reference LLM row *(quoted from Chen et al. 2023)* | 100 × 25 | 3 | **0.8730** | −0.6850 |
| Basic Agent — *no persona, this study* | 100 × 25 | 99 | **0.9160** | −0.4590 |
| **Biotech Expert Agent** — *persona* | 100 × 25 | 88 | **0.1270** | −0.1750 |
| **Economist Agent** — *persona* | 100 × 25 | 100 | **0.2977** | −0.3694 |
| Basic Agent (new) — *no persona, second run* | 100 × 25 | 70 | **0.8500** | −0.7700 |

Fig. 5 (same page) re-plots these and exposes one series the text never states — a **GARP
Violation Ratio**: Humans 0.144, reference LLM 0.03, Basic 0.99, Biotech 0.88, Economist 1.0.
That confirms the violation column is *the number of sessions containing at least one violation,
out of N sessions* (50/347 = 0.144 ✓), not a count of violating pairs. The paper never defines it.

### The load-bearing delta

| Comparison | Baseline | Persona | **Δ** |
|---|---|---|---|
| Biotech vs in-study Basic Agent | 0.9160 | 0.1270 | **0.789** |
| Economist vs in-study Basic Agent | 0.9160 | 0.2977 | **0.618** |
| Biotech vs Basic Agent (new) | 0.8500 | 0.1270 | **0.723** |
| Economist vs Basic Agent (new) | 0.8500 | 0.2977 | **0.552** |
| Biotech vs quoted reference LLM | 0.8730 | 0.1270 | **0.746** |
| Economist vs quoted reference LLM | 0.8730 | 0.2977 | **0.575** |

The answer to the brief's implicit question — "0.99 → 0.97 or 0.99 → 0.75?" — is **neither**.
The paper claims something far more extreme: **0.92 → 0.13**. Δ ≈ 0.55–0.79, roughly twenty-five
times the magnitude threshold set above. "Substantially degrades" is, if anything, an
*understatement* of what this paper asserts. That is the first sign to be suspicious.

### Three findings inside the table that cut against the brief

**(a) On the GARP-violation metric the persona effect is zero or negative.** The study's own
non-persona control violates GARP in **99 of 100 sessions**. The biotech persona violates in
**88** — *fewer*. The economist persona violates in 100 — one more. The entire violation-rate gap
in the table is between this study's agents (88–100%) and the *quoted* reference row (3%), i.e.
between two different papers and two different pipelines. It is not a persona effect. Of the two
metrics the brief leans on ("GARP compliance"), the one actually named in S2 shows **no
persona effect at all**.

**(b) The paper's own baseline is already broken, so it cannot isolate a persona effect.** A
non-persona agent at CCEI 0.85–0.92 with a 70–99% session violation rate is nowhere near the
0.997–0.999 ceiling the brief cites in S1. Whatever is destroying rationality in this pipeline is
already fully operative *before* any persona is applied.

**(c) The baseline in this paper contradicts the baseline in the brief.** S1 attributes CCEI
0.997–0.999 to Chen et al. (2023). This paper attributes **0.8730** to the same Chen et al.
(2023), with no table or page citation and no reconciliation. The brief uses S1 as the ceiling
and this paper as the demonstration of degradation from that ceiling — but the two claims rest on
baselines 0.12 apart, both sourced to the same PNAS article. **At most one of S1 and S2 can be
quoting Chen et al. correctly.** E3 should resolve which.

### Other indices

**None.** Ligature-normalised full-text search (ff/fi/fl/ffi/ffl folded, dashes and quotes folded,
soft hyphens stripped, NFKC, whitespace collapsed) returns:

| Index | Occurrences |
|---|---|
| Houtman–Maks | **0** ("houtman" 0, "maks" 0) |
| Money-pump | **0** (both spellings) |
| Afriat | **1** — reference list only, never used |
| Varian | 2 — one metric definition (§3.5 cites Varian 1982 for the violation test), one reference |

The paper reports **GARP violation count, CCEI, and Spearman correlation, and nothing else**.
No Houtman–Maks, no money-pump, no Afriat inequalities, no Bronars power benchmark.

---

## Study design and its limits

**Task.** Two goods only — products A and B with prices (pA, pB) and a stated fixed budget of 100
points; the agent chooses quantities. 25 rounds per session. A second "risk preference" task
varies whether pA and pB differ slightly (low-risk) or sharply (high-risk).

**Scale.** 100 sessions × 25 rounds = 2,500 decisions per agent condition; humans 347 × 25 quoted
from Chen et al. Three agent conditions (basic / biotech expert / economist) plus one later-added
basic repeat.

**Manipulation.** Personas are injected as the **system prompt** ("system introduction") through a
hosted assistants API, with a fresh thread per round to clear context. This is genuine
persona/role conditioning and matches the mechanism S2 describes — the mechanism match is fine.
No prompts are reproduced anywhere in the paper.

**Model.** A single **2024-vintage mini-tier reasoning model** — one checkpoint, one vendor, one
family. It is two generations old, superseded and retired well before 2026. **K3 fails
outright.** The brief's own protocol demands ≥3 frontier models across ≥2 families; this paper
supplies one obsolete model, so it cannot tell you what a 2026 frontier model's CCEI does under
persona conditioning. A 2025 measurement on a small model is weak evidence about a 2026 frontier
model in *either* direction — models have generally become more coherent, which pushes the true
2026 persona effect toward zero, i.e. toward the gate.

**No statistics of any kind. K2 fails.** Zero hits across the whole document for: confidence
interval, standard error, p-value, t-test, bootstrap, ANOVA, regression, significance test, error
bar, variance, SD, seed, random seed, sample size, statistical power, ablation, pre-registration.
"Average CCEI" is reported to four decimals with no spread, no n per cell beyond the row label,
and no test. Nothing in the paper establishes that any difference between rows is distinguishable
from noise.

**No replication — except one accidental one, and it is unflattering.** "Basic Agent" and "Basic
Agent (new)" are the same condition run twice. They differ by **0.066 in CCEI** (0.9160 vs
0.8500) and **29 percentage points in violation rate** (99 vs 70). That is the paper's only
implicit noise estimate, and it is larger than the entire headroom the brief needs to detect
(the gate turns on whether CCEI falls below 0.99). The "(new)" row is also highlighted in **yellow
in the published PDF** — an uncleaned editing highlight — is absent from Fig. 5, and is never
mentioned in the body text.

**No code, no data, no prompts.** Zero hits for github, code availability, data availability,
appendix, temperature. Nothing is reproducible.

**The headline risk claim has no supporting number.** The abstract asserts "more significant
decision deviations under high-risk conditions" and the conclusion asserts "in high-risk
situations, specialized models... tend to exhibit more GARP violations". "High-risk" appears 10
times in the text. **No result is broken out by risk condition anywhere.** The risk manipulation
is described, then never analysed.

**The table is internally inconsistent. K4 fails on three counts.**

1. *Spearman column contradicts its own definition.* §3.5 defines it as rank consistency between
   agent decisions and human decisions. The **Humans** row then carries −0.7500 — humans cannot
   correlate −0.75 with humans. The column is measuring something else (plausibly a
   price–quantity demand slope), and the paper never says what.
2. *CCEI and violation counts are not commensurate.* Basic Agent: 99% of sessions violate, CCEI
   0.916. Biotech: 88% of sessions violate — fewer — CCEI 0.127. A 0.79 CCEI gap alongside a
   *smaller* violation rate is possible in principle (severity vs frequency) but is never
   explained, tested, or even noticed.
3. *§3.1 and §3.2 are the same paragraph, duplicated verbatim.* An editorial signal about the
   care taken with the rest.

### Independent arithmetic cross-check — the reported CCEI is below its own floor

Fig. 4 (p. 8) is a workflow screenshot containing **the only round-level data the paper exposes
anywhere**: 26 rounds of (pA, pB, xA, xB), read at 600 dpi. Recomputing from it:

- **pA + pB = 1.0 in every round, and xA + xB = 100 in every round.** Observed expenditure
  p·x ranges **35 to 74** (mean 51.1) and is **never the stated 100-point budget**. The choices
  exhaust a fixed *quantity*, not the stated monetary budget. Under a standard Afriat setup the
  budget sets are therefore misspecified — and which convention the analysis used (stated m=100,
  or observed expenditure) changes every number in Table 1. The paper does not say.
- **Only 8 distinct price vectors across 26 rounds.** p = (0.5, 0.5) recurs **six times**, with
  bundles (80,20), (85,15), (10,90), (90,10), (50,50), (65,35). Identical budget sets answered
  with opposite bundles manufacture GARP violations mechanically, for any agent, persona or not.
  This alone can explain a 99% violation rate in the non-persona control.
- **Computed CCEI of that sequence: 0.554.** Uniform-random choice on the same price vectors
  (400 draws): mean 0.504, median 0.498, 5th percentile 0.297, minimum 0.265.
- **Adversarial floor on that price grid: exactly 0.2500** — the value produced by always buying
  the relatively expensive good at corner bundles. Confirmed two ways: analytically (the
  (0.8, 0.2) / (0.2, 0.8) price pair binds — e·80 > 20 ⟹ e > 0.25) and by random search over
  3,000 corner-bundle sequences, minimum found 0.2500.

**Therefore the reported Biotech CCEI of 0.1270 lies below the arithmetic minimum attainable on
the only budget-set grid the paper publishes**, and the Economist's 0.2977 sits barely above that
worst-case floor — i.e. it claims an agent instructed to use cost-benefit analysis behaved at
near-maximal perversity, and does not remark on it. Reaching 0.127 at all requires a repeated
(0.9, 0.1) / (0.1, 0.9) extreme price pair with perfectly perverse corner choices; that grid
contains (0.9, 0.1) once and (0.1, 0.9) never.

*Caveat, stated plainly:* the paper never says the persona conditions used this exact grid, and
publishes no round-level data for them. So this is an **unresolved inconsistency between the
headline number and the only design the paper exposes**, not proof the number is wrong. Nothing
in the paper resolves it. The CCEI routine used here was validated first — it returns 1.0000 on a
Cobb–Douglas rationalizable sequence over the same prices, and 0.1111 on the textbook
two-observation extreme swap.

### Caveats the paper itself raises

§5.3 "Research Limitations" lists exactly three, **all about external validity**:

1. Narrow domain scope — only biotechnology and economics; healthcare, finance, legal unexplored.
2. Limited representativeness of the two chosen agent types.
3. Task simplification — no intertemporal planning, no multi-agent coordination.

It raises **no** caveat about sample size, statistical power, absence of replication, the CCEI
implementation, budget-set specification, the missing risk-condition breakdown, or the mismatch
between its 0.8730 baseline and Chen et al.'s published figure. The paper's self-assessment does
not touch any of the problems that actually bear on the gate.

---

## Verdict on headroom

### HEADROOM MARGINAL

Against the falsifier committed above: the **magnitude condition is met by a wide margin**
(Δ = 0.55–0.79 against a 0.03 threshold; persona CCEI 0.127/0.298 against a 0.95 threshold).
**K1 holds** — there is a genuine in-study non-persona control. **K2, K3 and K4 all fail**: no
dispersion of any kind, one obsolete single-family model, and three independent internal
inconsistencies including a headline value below its own design's arithmetic floor. Magnitude met
+ credibility failed → **MARGINAL**, per the mapping fixed in advance.

Not CANNOT-DETERMINE, and the distinction matters: the *direction* survives even if every
specific number is wrong. Two independently constructed persona conditions both collapse CCEI,
and they do so relative to a control run through the same pipeline. The sign is robust to the
measurement being bad; only the magnitude is unusable.

Not CONFIRMED, and that distinction matters more. **This paper cannot carry the C4 gate, and the
brief should stop treating it as though it does.** Concretely:

- The number the brief needs — what a **2026 frontier** model's CCEI does under persona
  conditioning — is not in this paper and cannot be extrapolated from it. One retired mini-tier
  2024 checkpoint is the entire evidence base.
- The metric S2 actually names ("GARP compliance") shows a **zero-to-negative** persona effect
  here. Only CCEI moves, and CCEI is the number that fails the arithmetic cross-check.
- The paper's non-persona control is already at CCEI 0.85–0.92, so even taken at face value it
  demonstrates headroom **without** persona conditioning — which means it is not evidence that
  *persona conditioning* is the lever. If the pilot needs a lever, this paper does not identify one.
- The brief's S1 ceiling (0.997–0.999) and S2 degradation evidence use baselines 0.12 apart, both
  attributed to Chen et al. (2023). That contradiction is live and belongs to E3.

Per the task's scope limit, no verdict is rendered here on the project's own gate; that is the
week-1 pilot's measurement. What this check establishes is only that **the gate is currently
unsecured** — the brief's "S4 preflight" is written as though headroom is already evidenced, and
on this citation it is not. The pilot must be treated as genuinely gating rather than
confirmatory, and powered for a *small* effect (Δ ~0.01) rather than the Δ ~0.7 this paper
advertises.

---

## One-line summary for docs/CLAIMS.md

`E2: 2501.18190 gives CCEI 0.916 basic -> 0.127 biotech / 0.298 economist, but on one retired 2024 model, with no replications or CIs, and 0.127 is below its own budget grid's arithmetic floor.`

---

## Fetch record

| Field | Value |
|---|---|
| URL requested | `https://arxiv.org/pdf/2501.18190` |
| HTTP status | 200 |
| Redirect | none (effective URL identical to requested) |
| Bytes downloaded | 1,636,878 |
| Format | PDF 1.7 |
| MD5 | `55196272b895c09a037b581df0f0ada4` |
| Secondary URL | `https://arxiv.org/abs/2501.18190` — HTTP 200, 40,824 bytes, for version + subject metadata |
| Version retrieved | **v2**, 17 Mar 2025 (listing: v1 30 Jan 2025, 748 KB; v2 17 Mar 2025, 1,599 KB — the 1,599 KB matches the bytes downloaded, confirming v2) |
| arXiv subject | Artificial Intelligence (cs.AI), primary and only |
| Extraction | PyMuPDF (`fitz`), page-by-page `get_text()`, full document |
| Pages extracted | **21 of 21** |
| Characters / words | 41,844 / 5,709 |
| Fallbacks used | none — the primary PDF fetch succeeded on the first attempt; the HTML and ar5iv mirrors were not needed |
| Local copies | scratchpad only; nothing committed to the repo |
| Tooling note | fetched with `curl` per instruction; the vault fetch tool was deliberately not used (concurrent sibling agents, shared SQLite) |

**Completeness statement.** Read end to end: §1 Introduction (pp. 1–3), §2 Theoretical Background
incl. the multi-objective model (pp. 4–7), §3 Experimental Design (pp. 7–11), §4 Results (pp.
11–13), §5 Discussion / Limitations / Future Work (pp. 13–17), §6 Conclusion (pp. 17–19),
References (pp. 19–21). Nothing was skimmed or inferred from the abstract.

**Table verification.** Table 1 was recovered three independent ways and all three agree: (a) the
raw text layer; (b) `blocks` mode with x/y coordinates, confirming the header block spans
x=330–494 and that "Average CCEI" and "Average Spearman Correlation" are two columns collapsed
into one extraction block — the specific trap flagged in the task; (c) the page rendered at
170 dpi and read directly, which also surfaced the yellow highlight on the "(new)" row. Column
assignment was independently corroborated by Fig. 5, whose GARP Violation Ratio series
(0.144 / 0.03 / 0.99 / 0.88 / 1) reproduces the violation column divided by the session count.

**Figure verification.** Embedded images are present on pp. 6, 8 (×2), 9 and 12 only. Fig. 4
(p. 8) was cropped and re-rendered at 600–700 dpi to recover the 26-round dataset in the agent
log panel; the left and right halves were rendered separately because the panel is wider than the
figure frame and the two crops overlap, giving a redundant read of rounds 4–25. Figs. 1–3 are a
causal-chain schematic and two workflow screenshots and contain no results data.

**Ligature handling.** Before any term search the extracted text was normalised — ff/fi/fl/ffi/ffl
and st ligatures folded to ASCII, en/em dashes and curly quotes folded, soft hyphens stripped,
then NFKC, then whitespace collapsed to single spaces, so hyphenated line breaks and mid-phrase
newlines could not hide a match. Every zero-hit term reported above (houtman, maks, money pump,
money-pump, confidence interval, standard error, p-value, t-test, bootstrap, anova, regression,
seed, random seed, sample size, error bar, variance, ablation, pre-registration, github, code is
available, data availability, appendix, temperature) was searched on that normalised string. The
single "afriat" hit and the two "varian" hits were verified by printing surrounding context
rather than trusting the count — "afriat" is a reference-list entry never cited in the body, and
one "varian" is §3.5's citation of Varian (1982) for the violation test.

**Numeric cross-check reproducibility.** The CCEI binary search, the 400-draw uniform-random
benchmark and the 3,000-draw adversarial corner search were run on the Fig. 4 data in the
scratchpad. The routine was validated before use against two cases with known answers
(Cobb–Douglas rationalizable → 1.0000; two-observation extreme swap → 0.1111) and returned both
exactly.
