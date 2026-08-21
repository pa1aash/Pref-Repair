# Kill-check E3 — the CCEI 0.997-0.999 figure in context (arXiv:2305.12763)

Target claims: **S1** (the figure itself) and **C4** (whether headroom exists to project away).
Brief under test: `docs/F3-PLAN-ORIGINAL.md`, sections "The gap" and "S4 preflight".

Paper: Chen Y., Liu T. X., Shan Y., Zhong S., *The Emergence of Economic Rationality of GPT*.
arXiv:2305.12763v3 (econ.GN, 6 Nov 2023) = SI-complete preprint; published as
*PNAS* **120**(51) e2316205120, doi `10.1073/pnas.2316205120`, epub 12 Dec 2023, PMID 38085780,
PMCID PMC10740389. The brief's bibliographic citation is exact.

---

## Falsifier (stated before the finding)

Written before reporting what the paper contains. The question is not "is the number real" but
"could this instrument have produced a *low* number if the model had been irrational". Any one of
the following, found in the full text, converts 0.997-0.999 from a finding about the model into an
artefact of the budget-set design:

- **F1 — non-crossing budget lines.** If the 25 budget lines per subject are nested, parallel, or
  otherwise rarely intersecting, GARP violations are near-impossible by construction and CCEI = 1
  is forced regardless of behaviour. This is the single most damaging finding available and it is
  the reason E3 exists. Threshold: if fewer than ~15% of budget-line pairs intersect, the design
  is a rubber stamp.
- **F2 — degenerate instrument scale.** Fewer than ~10 observations per subject, only one relative
  price, or a price-ratio range so narrow (say within 2:1) that the revealed-preference relation
  is almost empty.
- **F3 — no power benchmark at all.** No Bronars test, no uniform-random-choice control, no
  simulated-irrational agent, no predictive-success or bootstrap analysis. A paper that reports a
  near-ceiling score without ever asking what its instrument does to a random agent has not
  established that the score means anything.
- **F4 — power benchmark run and *failed*.** A Bronars (or equivalent) rejection rate that is not
  overwhelming — say under 90% of uniform-random simulated subjects violating GARP — would mean
  the design genuinely cannot separate rational from random.
- **F5 — cross-instrument human comparison.** If the "more rational than humans" claim rests only
  on CCEI values quoted from other papers with other budget sets, the comparison is between
  instruments, not between agents, and the brief's framing inherits that defect.
- **F6 — misreported statistic.** If 0.997-0.999 turns out to be a single number, or a
  within-subject spread, or a different model, or a different domain, or conditional on a design
  choice the brief does not intend to inherit, S1 needs rewording.

What would leave the figure standing as a genuine finding: crossing budget lines, an explicit and
passing power analysis, and a human control run on the identical instrument.

Result up front: **F1, F2, F3, F4 and F5 all fail to fire. F6 fires in a narrow but consequential
way** — the figure is real, correctly transcribed, and conditional on one design choice the brief
does not mention.

---

## The figure, confirmed or corrected

**Confirmed, exactly, in both the preprint and the published version.** The two texts are
numerically identical in every value checked.

The figure is a **range across the four domain means**, not across subjects and not a single
statistic. Each domain mean is the average of **100 independent runs** ("GPT observations"), each
run consisting of 25 decisions. Model: **GPT-3.5-Turbo** via the vendor's public API, temperature 0,
all other parameters default. **Baseline condition only.**

| Domain | mean CCEI (model) | runs with CCEI = 1, of 100 | mean CCEI (human) | mean Spearman ρ, model / human |
|---|---|---|---|---|
| Risk | **0.998** | 95 | 0.980 | −0.984 / −0.826 |
| Time | **0.997** | 89 | 0.985 | −0.966 / −0.788 |
| Social | **0.997** | 81 | 0.967 | −0.951 / −0.681 |
| Food | **0.999** | 92 | 0.963 | −0.992 / −0.673 |

Two things the brief's one-line summary drops, both material to C4:

1. **The scores are baseline-condition-only.** The *same paper*, on the *same budget sets*, reports
   these means under two presentation changes:

   | Condition | Risk | Time | Social | Food |
   |---|---|---|---|---|
   | Baseline (continuous, "1 point = X units") | 0.998 | 0.997 | 0.997 | 0.999 |
   | Price framing ("Y points = 1 unit") | **0.901** | **0.884** | **0.698** | **0.894** |
   | Discrete choice (11 points on the same line) | **0.843** | **0.908** | **0.871** | **0.780** |

   Share of runs falling below CCEI 0.9 — price framing: 34%, 48%, **88%**, 49%. Discrete choice:
   51%, 32%, 33%, 55%. Under price framing the paper explicitly declines to run its structural
   preference estimation because the choices are no longer rationalisable.

2. **Even at baseline the ceiling is not hit.** 5, 11, 19 and 8 runs out of 100 violate GARP in
   risk, time, social and food. The social-preference domain has a 19% violation rate at the
   paper's own best-case condition.

Robustness the paper reports as *not* moving the score: temperature 0 → 0.5 → 1.0 (no significant
CCEI change; invalid-response rate rises to 4.7% and 9.8%, analysed conditional on valid answers);
and eight demographic personas (female/male, young child/elderly, elementary/college education,
Asian/African American) — all statistically indistinguishable from baseline. Note that this is a
*demographic* persona manipulation, not an expertise/role persona of the kind arXiv:2501.18190
uses; E3 cannot speak to that one.

Model-generation caveat: **only GPT-3.5-Turbo was tested.** No GPT-4, no other family, no snapshot
identifier or API date is given. The brief's "GPT-3.5" attribution is correct; any extrapolation to
frontier models is the brief's, not the paper's.

---

## The budget-set design that produced it

This is the central question. Full specification, reconstructed from Appendix A of the preprint
(= the published SI Appendix), with prompt footnotes cross-checked against the prose:

| Design parameter | Value |
|---|---|
| Observations per subject per domain | **25** |
| Goods | **2** (K = 2) |
| Endowment | **100 points, fixed in every round** |
| Prices | exchange rates M (good A) and N (good B), drawn i.i.d. **uniform on [0.1, 1.0], rounded to 2 decimals**, rejected unless **max{M, N} ≥ 0.5** |
| Commodity-space prices / income | p_A = 1/M, p_B = 1/N, income normalised to 100 |
| Budget-line intercepts | 100·M and 100·N, i.e. anywhere in **[10, 100]** on each axis |
| Price-ratio range | p_A/p_B = N/M ∈ **[0.1, 10]**, so **ln(p_A/p_B) ∈ [−2.30, +2.30]** |
| Budget lines cross? | **Yes, abundantly — see below** |
| Independent subjects | **100 runs per domain per condition** (10,000 tasks in the baseline) |
| Domain variation | commodity *labels only*; the price generator is byte-identical across risk, time, social and food |
| Elicitation | all 25 rounds sent in one uninterrupted context; 3 comprehension-check questions first |
| Refusals | dropped from analysis |

**F1 is refuted.** With a fixed 100-point endowment and independently drawn exchange rates, the
A-axis and B-axis intercepts move independently over a 10:1 range, so ordering flips constantly.
Simulating the paper's exact generator (2,000 subjects × 25 lines, `/tmp/cross.py`): **58.1% of
budget-line pairs intersect** (min 37%, max 79% across subjects). This is the standard Choi–Fisman–
Gale–Kariv / Choi–Kariv–Müller–Silverman graphical budget-line instrument, cited as such, and it is
the opposite of a non-crossing design.

Prompt mechanics worth knowing, since the brief's method section reuses this shape:

- System role: "act as a human decision maker … use your best judgment to come up with solutions
  that you like most", plus an instruction to answer every round (added to suppress refusals).
- The second message role carries the task format; the user role carries three comprehension checks
  and then the 25 decision rounds.
- **Baseline price framing:** "investing every 1 point for Asset A returns M dollars".
  **Alternative price framing:** "investing every 1/M points for Asset A returns 1 dollar" — the
  reciprocal is displayed directly, to 2 decimals. Same budget sets, same 25 draws.
- **Discrete condition:** the 11 options are the points allocations 0, 10, …, 100 converted to
  dollars — i.e. eleven evenly spaced points **on the identical budget line**.
- Domains: two contingent securities at 50/50 (risk); dollars today vs a cheque cashable in one
  month (time); self vs a randomly matched other subject (social); kilograms of meat vs tomatoes
  (food).

**Leakage note for `docs/CLAIMS.md` S12.** The full prompt text, the price generator, and the code
and data (public Dropbox link in the PNAS Data Availability statement) are all published. Any model
trained after Dec 2023 has plausibly seen this exact instrument. The brief's requirement to
generate budget sets fresh is correct and this paper is a concrete reason for it.

---

## What the paper says about power and ceiling effects

The paper runs **four** power analyses, in Section 4.1 and Appendix C.2 (published SI). F3 and F4
both fail to fire.

1. **Bronars (1987) power.** Simulated subjects choose uniformly at random along each budget line,
   25 choices, budget sets generated the same way. **99.9% of simulated subjects violate GARP.**
   I replicated this independently against the paper's stated generator (`/tmp/ccei_sim.py`,
   1,000 simulated subjects): **100.0% violation rate, mean CCEI 0.718, median 0.727, 95th
   percentile 0.902.** The instrument is not a rubber stamp.
2. **Predictive success** (Selten 1991 / Beatty–Crawford 2011), model over the random benchmark:
   94.9%, 88.9%, 80.9%, 91.9% (humans: 60.8%, 79.0%, 52.1%, 43.4%).
3. **Selten score** (raw CCEI minus the simulated CCEI of the same budget set): 0.279, 0.274,
   0.275, 0.281 for the model; 0.262, 0.266, 0.247, 0.244 for humans; all significantly > 0.
4. **Bootstrap power** (Andreoni–Miller 2002; 10,000 synthetic subjects resampling choices from the
   *actual* DM pool at each budget). Here the probability of rejecting GARP is **7.9%, 26.3%,
   26.0%, 8.5%** for the model versus **95.4%, 96.6%, 99.8%, 99.8%** for humans. The paper reports
   this openly and attributes it to the model's low preference heterogeneity: when a population's
   choices are nearly identical, resampling across it cannot manufacture cycles. This is the one
   place the paper's own analysis concedes reduced detection power, and it is a statement about the
   *model's* homogeneity, not about the budget sets.

**The word "ceiling" never appears in the paper, and neither does any discussion of CCEI's
nonlinearity near 1.** That gap matters, because the CCEI scale is severely compressed at the top.
Sweeping a CES maximiser with Gaussian allocation noise through the paper's own generator
(300 subjects per row, α ~ U[0.35, 0.65], ρ ~ U[−1, 0.9]):

| Allocation noise (sd, points of 100) | GARP violation rate | mean CCEI | share CCEI < 0.95 |
|---|---|---|---|
| 0 | 0.0% | 1.0000 | 0.0% |
| 2 | 2.7% | 1.0000 | 0.0% |
| 3 | 6.0% | 0.9999 | 0.0% |
| **5** | 21.3% | **0.9984** | 0.3% |
| 8 | 54.0% | 0.9908 | 3.3% |
| **12** | 78.3% | **0.9625** | 23.3% |
| 20 | 96.3% | 0.8628 | 70.7% |

Read against the paper: the observed 0.997-0.999 is what a near-deterministic optimiser with
roughly **3-5 points of allocation noise** produces, and the human 0.963-0.985 is what roughly
**8-12 points** produces. The gap between "GPT" and "human" in CCEI units is 0.03; in behavioural
units it is a factor of two to three in choice noise. Symmetrically, the 0.003 of apparent headroom
between 0.997 and 1.000 is *not* 0.3% of the available behavioural range — it is the compressed
image of a real and non-trivial residual inconsistency.

Stated limitations the authors do own, in the Discussion: mechanism unexplored; economic
rationality is only one notion of rationality; and — directly relevant — "we use a simple
experimental environment with only two commodities", concluding that rationality "can emerge in
GPT when decision contexts are simple and framed in specific ways". They also offer a mechanism
for the framing collapse: a corpus-frequency heuristic, where "50-50 split" is a high-frequency
string in allocation contexts (hence midpoint clustering under the unfamiliar reciprocal framing)
and "all or nothing" is high-frequency under option lists (hence corner clustering under discrete
choice). The framing sensitivity is *larger for the model than for humans*, verified by OLS in the
SI regression tables; humans also degrade, but significantly less.

**F5 is refuted.** The human comparison is a purpose-run parallel experiment, not literature
values: 347 subjects, representative US sample recruited on Prolific, July 2023, randomised across
the baseline / price-framing / discrete-choice conditions with ≥110 per condition, identical task
text and identical random price generator, median 30.5 minutes, $6 participation fee plus a 1-in-30
bonus lottery on one realised decision, pre-registered as AEARCTR-0011750 with IRB approval.
Literature CCEI values (range 0.81-0.99, mean 0.918, ~19 studies) are reported *separately* as a
second, weaker comparison. The instrument is genuinely held constant between model and human.

---

## Verdict

**STANDS BUT DESIGN-DEPENDENT.**

The figure is confirmed to the digit, correctly attributed to the correct paper and the correct
model, and it is **not** a low-power artefact: the budget lines cross 58% of the time pairwise, the
price ratio spans a full decade, and both the paper's Bronars test (99.9%) and my independent
replication (100.0%) show the instrument annihilates a random agent. F1-F5 all fail. S1 as written
in `docs/CLAIMS.md` is accurate and needs only a qualifier.

The brief's *use* of the figure is where the problem is. `docs/F3-PLAN-ORIGINAL.md` deploys
0.997-0.999 as the reason to fear "no headroom", and the S4 gate is phrased as "if CCEI > 0.99 even
when role-prompted, this project is dead". Three findings cut against that framing, all from inside
the cited paper:

1. **The same paper already demonstrates the headroom it is being cited to deny.** Holding the
   budget sets fixed and changing only how prices are *worded*, mean CCEI falls to 0.698-0.901;
   changing only continuous-to-discrete, to 0.780-0.908. Between 32% and 88% of runs land below
   0.9. Chen et al. is evidence *for* C4, not against it — and it is stronger evidence than
   arXiv:2501.18190 because the manipulation is trivial and the budget sets are held constant.
2. **The baseline is not actually at ceiling.** 19% of social-preference runs violate GARP at the
   paper's best condition; 5-11% in the others.
3. **CCEI compresses near 1.** A mean of 0.997 corresponds to a genuinely noisy optimiser, not to a
   perfect one. Reasoning about headroom in raw CCEI units systematically understates what is
   there. The projection operator's input is the violation set, not the index value.

Two caveats that survive in the brief's favour. First, the model is a 2023 mid-tier one; frontier
models could plausibly be at 1.000 in the baseline condition, and nothing here settles that — the
week-1 pilot is still required. Second, the framing effects here are *presentation* manipulations
(reciprocal price wording, discretisation), not the expertise-persona manipulation the brief leans
on for C4; those are different levers and E2 owns that question.

Recommended consequence for `docs/CLAIMS.md`: S1 stands with the "baseline condition" qualifier
added. C4 should record that its headroom evidence is stronger than the brief claims, and the S4
gate should be restated to measure CCEI under **framing and format** variation as well as persona —
the framing lever is the one with published effect sizes on the exact instrument. Also worth
lifting into the method: the discrete-choice condition is nearly free to run and, in this paper,
produced the largest and most uniform CCEI degradation of any manipulation.

---

## One-line summary for docs/CLAIMS.md

```
S1/C4 confirmed exactly but BASELINE-ONLY: mean CCEI .998/.997/.997/.999 (risk/time/social/food, GPT-3.5-Turbo, T=0); same budget sets reframed give .698-.908 — headroom exists.
```

---

## Fetch record

| # | URL | Status | Bytes | Method | What was read |
|---|---|---|---|---|---|
| 1 | `https://arxiv.org/pdf/2305.12763` | 200 | 7,038,936 | curl → pymupdf `get_text()`, 105 pages → 182,469 chars | **Full text, all 105 pages.** Body pp. 1-24, references pp. 25-33, Appendix A (prompts + price generator) pp. 34-52, Appendix B (human experiment) pp. 53-71, Appendix C (estimation + power analyses) pp. 72-75, Appendix D (figures/tables) pp. 76-105. |
| 2 | `https://arxiv.org/abs/2305.12763` | 200 | 41,244 | curl | Version history: v1/v2/**v3**; v3 is the version fetched (6 Nov 2023). |
| 3 | `https://api.openalex.org/works?search=...` | 200 | — | curl + json | Confirmed published venue: PNAS 120(51) e2316205120, doi `10.1073/pnas.2316205120`. |
| 4 | NCBI eutils esearch/efetch, PubMed 38085780 | 200 | — | curl | Abstract, author affiliations, PMCID PMC10740389, epub 12 Dec 2023. |
| 5 | `https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10740389/` | 200 | 262,367 | curl + regex de-tag → 68,440 chars | **Full published main text.** Used to cross-check every CCEI value, the Bronars sentence, the method section, and the Data Availability statement against the preprint. All identical. |
| 6 | `https://www.pnas.org/doi/10.1073/pnas.2316205120` | **403** | 5,505 | curl (Cloudflare interstitial) | **GAP — publisher page unreachable.** Not guessed. Fully mitigated: the arXiv v3 appendices are the SI Appendix, and PMC (#5) supplied the published main text, so nothing depends on the blocked page. |
| 7 | `https://www.ebi.ac.uk/europepmc/webservices/rest/search?...` | TLS error 35 | 0 | curl | **GAP — not reachable.** Redundant with #5; no information lost. |

**Not fetched.** The published SI Appendix PDF (linked from PMC as "Appendix 01 (PDF), 6.1MB") and
the authors' public Dropbox code/data archive. Neither was needed: the arXiv v3 appendices contain
the same design specification, and every design parameter reported above was read directly from
Appendix A footnotes and cross-checked against the prose.

**Parser hygiene.** Ligature corruption was assumed, so no conclusion rests on a substring grep.
Every number in this file was read from the running prose in its surrounding sentence, and every
CCEI value was independently re-read in the PMC HTML rendering (source #5), which has no ligature
problem. The two sources agree on all of them. Figure-panel numbers were not trusted; the
CCEI values quoted are prose values, not extracted from figure axes.

**Own computation.** Two throwaway scripts, written from the paper's stated generator, not from any
released code: `/tmp/cross.py` (budget-line intersection frequency) and `/tmp/ccei_sim.py`
(Warshall transitive-closure GARP test, binary-search CCEI, Bronars replication, and the CES-plus-
noise sensitivity sweep). Results are labelled as mine wherever they appear above and are never
mixed with the paper's reported values.
