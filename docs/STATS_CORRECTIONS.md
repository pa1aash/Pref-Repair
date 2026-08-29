# Statistical corrections and robustness checks — Session 2 (Track 2)

Pure computation, run against already-collected data. No interpretation of what any result means
for the paper's claims — that is reserved for the session that actually edits `paper.tex`. Each
section below was produced by an independent sub-agent working only from the repo's existing
result files (`results/*.json`), `tex/paper.tex`, and `docs/*.md`; each sub-agent's own
reconstruction/sanity checks are reported inline. Full per-trace working data for every section is
saved under `results/` (file named per section, referenced below).

---

## 2A. Multiple-comparison correction

### 1. The full test family (N = 31)

Source (a): `tex/paper.tex` — verified via a full grep pass and manual read of every hit (lines
48–49, 221, 401–402, 405–406, 428–434, 440–441, 452–453, 474, 619–620, 632, 635–638). 16 distinct
statistical tests were found; 7 are **restated verbatim at a second location** (once in
prose/abstract, once in a results or appendix section reporting the identical statistic). Each is
counted **once**, with both locations cited.

| # | Test | Location(s) | Raw p |
|---|---|---|---|
| P1 | 1.5B dose-response Spearman (ρ=0.756, n=60) | tex:48-49, restated tex:405 | p<0.0001 → **0.0001** ¹ |
| P2 | 3B dose-response Spearman (ρ=0.614, n=25) | tex:48-49, restated tex:406 | 0.0011 |
| P3 | Multiturn GARP pass-rate collapse (0.40→0.10) | tex:221, restated tex:473-474 | 0.0073 |
| P4 | Multiturn CCEI (0.9522 vs 0.9540) | tex:474 | 0.91 |
| P5 | Pooled dose-response Spearman (ρ=0.729, n=85) | tex:401 | p<0.0001 → **0.0001** ¹ |
| P6 | Pooled dose-response Pearson (r=0.821) | tex:401 | p<0.0001 → **0.0001** ¹ |
| P7 | Pooled one-sample t (mean Δpayoff, t=5.41) | tex:402 | p<0.00001 → **0.00001** ¹ |
| P8 | Severity-confound Pearson, dose vs raw payoff (r=-0.41) | tex:429, restated tex:632 | p<0.0001 → **0.0001** ¹ |
| P9 | Severity-confound partial correlation (r=0.784) | tex:431, restated tex:635 | 7×10⁻¹⁹ |
| P10 | Severity-confound OLS dose coefficient (t=11.4/11.43) | tex:433, restated tex:637 | p<10⁻¹⁶ → **1e-16** ¹ |
| P11 | Severity-confound OLS raw-payoff coefficient | tex:434, restated tex:638 | 0.18 |
| P12 | 3B framing GARP pass (0.73→0.39) | tex:440 | 0.0089 |
| P13 | 3B framing CCEI t-test (0.9900 vs 0.9713) | tex:441 | 0.0508 |
| P14 | 1.5B reciprocal-vs-baseline GARP pass (0.40 vs 0.38) | tex:452 | 0.85 |
| P15 | 1.5B reciprocal-vs-baseline CCEI (0.9522 vs 0.9413) | tex:453 | 0.73 |
| P16 | GARP-consistent vs violating raw payoff, Welch t=-0.07 | tex:619-620 | 0.94 |
| N1 | Null-op paired Wilcoxon, pooled (n=85) | docs/NULL_OPERATOR_RESULTS.md §1 | 3.98e-10 |
| N2 | Null-op paired Wilcoxon, qwen2.5:1.5b (n=60) | docs/NULL_OPERATOR_RESULTS.md §1 table | 5.5e-08 |
| N3 | Null-op paired Wilcoxon, llama3.2:3b (n=25) | docs/NULL_OPERATOR_RESULTS.md §1 table | 0.0010 |
| N4 | Null-op paired t-test, pooled | docs/NULL_OPERATOR_RESULTS.md §1 | 0.00084 |
| N5 | Null-op paired t-test, qwen2.5:1.5b | docs/NULL_OPERATOR_RESULTS.md §1 table | 0.0040 |
| N6 | Null-op paired t-test, llama3.2:3b | docs/NULL_OPERATOR_RESULTS.md §1 table | 0.0038 |
| N7 | Null-op partial correlation (dose vs real\|null), r=0.574 | docs/NULL_OPERATOR_RESULTS.md §3 | 1.13e-08 |
| C1 | Corrected-payoff PRIMARY pooled Wilcoxon (median of 20 draws) | docs/CORRECTED_PAYOFF_RESULTS.md §1 | 6.02e-07 |
| C2 | Corrected-payoff PRIMARY llama Wilcoxon (median of 20) | docs/CORRECTED_PAYOFF_RESULTS.md §1 table | 0.00615 |
| C3 | Corrected-payoff PRIMARY qwen Wilcoxon (median of 20) | docs/CORRECTED_PAYOFF_RESULTS.md §1 table | 1.97e-05 |
| C4 | Corrected-payoff PRIMARY pooled partial-r (median of 20) | docs/CORRECTED_PAYOFF_RESULTS.md §1 | 1.18e-04 |
| C5 | Corrected-payoff ORACLE pooled Wilcoxon (median of 20) | docs/CORRECTED_PAYOFF_RESULTS.md §2 | 2.57e-10 |
| C6 | Corrected-payoff ORACLE llama Wilcoxon (median of 20) | docs/CORRECTED_PAYOFF_RESULTS.md §2 table | 3.53e-04 |
| C7 | Corrected-payoff ORACLE qwen Wilcoxon (median of 20) | docs/CORRECTED_PAYOFF_RESULTS.md §2 table | 8.90e-08 |
| C8 | Corrected-payoff ORACLE pooled partial-r (median of 20) | docs/CORRECTED_PAYOFF_RESULTS.md §2 | 6.27e-05 |

¹ Six paper.tex statements report only an inequality bound (e.g. `p<0.0001`), not an exact value.
Substituted with the stated bound itself for correction purposes — conservative (the true p is
smaller), and none of the six bounded tests sit near a rejection boundary, so this does not affect
any reject/fail-to-reject call in this family.

Not double-counted: tex:429/632, tex:431/635, tex:433/637, tex:434/638 are each the **same**
severity-confound test restated once in the main-text robustness paragraph and once in Appendix B's
payoff audit — confirmed identical statistics (r, t, p match to the reported precision).

### 2. Family-construction decision for the K=20-draws experiment

Two conventions were considered for the corrected-payoff experiment's 20 independent α-draws, each
producing its own pooled/per-model Wilcoxon p and partial-r p:

- **Chosen convention — one summary test per statistic (8 tests, C1–C8 above):** the **median
  p-value across the 20 draws** is used as "the reported test" for each of {PRIMARY pooled
  Wilcoxon, PRIMARY llama, PRIMARY qwen, PRIMARY pooled partial-r, ORACLE pooled Wilcoxon, ORACLE
  llama, ORACLE qwen, ORACLE pooled partial-r}. Justification: `docs/CORRECTED_PAYOFF_RESULTS.md`
  itself frames K=20 as a robustness/stability check on one underlying claim per statistic, and
  reports mean/median/min/max rather than 20 separate findings — the median is the most
  representative, least outlier-sensitive summary of what a paper would actually state.
- **Sensitivity check — all-20-draws convention:** treating each draw's **pooled** Wilcoxon p as a
  separate test (replacing C1 and C5 with 40 tests) gives a 69-test family. Under Holm this yields
  60/69 rejections; under BH, 63/69. **Every one of the other 29 tests' reject/fail status is
  unchanged** between the 31-test and 69-test families — expanding the draws only affects how many
  of the 20 individual per-draw p-values survive on their own (nearly all do, since every primary
  and oracle per-draw pooled p is ≤1.01e-4). This convention did not change any substantive
  conclusion for tests outside the K=20 experiment itself.

### 3. Correction results — full family (N = 31), α = 0.05

Sorted by raw p. Holm and BH implemented by hand (both step-down/step-up formulas with monotonicity
enforcement), cross-checked against `scipy.stats.false_discovery_control(method='bh')` — identical
output. Holm sanity-checked on a synthetic 5-point example against the classical step-down
definition and matched exactly.

| Raw p | Test | Holm-adj p | Holm (α=0.05) | BH-adj p | BH (α=0.05) |
|---|---|---|---|---|---|
| 7.00e-19 | P9 severity partial-r | 2.17e-17 | reject | 2.17e-17 | reject |
| 1.00e-16 | P10 severity OLS dose coef | 3.00e-15 | reject | 1.55e-15 | reject |
| 2.57e-10 | C5 corrected oracle pooled Wilcoxon | 7.45e-09 | reject | 2.66e-09 | reject |
| 3.98e-10 | N1 null-op Wilcoxon pooled | 1.11e-08 | reject | 3.09e-09 | reject |
| 1.13e-08 | N7 null-op partial-r | 3.05e-07 | reject | 7.01e-08 | reject |
| 5.50e-08 | N2 null-op Wilcoxon qwen | 1.43e-06 | reject | 2.84e-07 | reject |
| 8.90e-08 | C7 corrected oracle qwen Wilcoxon | 2.23e-06 | reject | 3.94e-07 | reject |
| 6.02e-07 | C1 corrected primary pooled Wilcoxon | 1.45e-05 | reject | 2.33e-06 | reject |
| 1.00e-05 | P7 pooled one-sample t | 2.30e-04 | reject | 3.44e-05 | reject |
| 1.97e-05 | C3 corrected primary qwen Wilcoxon | 4.33e-04 | reject | 6.11e-05 | reject |
| 6.27e-05 | C8 corrected oracle pooled partial-r | 1.32e-03 | reject | 1.77e-04 | reject |
| 1.00e-04 | P1 1.5B dose-response Spearman | 2.00e-03 | reject | 2.07e-04 | reject |
| 1.00e-04 | P5 pooled dose-response Spearman | 2.00e-03 | reject | 2.07e-04 | reject |
| 1.00e-04 | P6 pooled dose-response Pearson | 2.00e-03 | reject | 2.07e-04 | reject |
| 1.00e-04 | P8 severity Pearson dose-vs-raw-payoff | 2.00e-03 | reject | 2.07e-04 | reject |
| 1.18e-04 | C4 corrected primary pooled partial-r | 2.00e-03 | reject | 2.29e-04 | reject |
| 3.53e-04 | C6 corrected oracle llama Wilcoxon | 5.30e-03 | reject | 6.44e-04 | reject |
| 8.40e-04 | N4 null-op paired t-test pooled | 1.18e-02 | reject | 1.45e-03 | reject |
| 1.00e-03 | N3 null-op Wilcoxon llama | 1.30e-02 | reject | 1.63e-03 | reject |
| 1.10e-03 | P2 3B dose-response Spearman | 1.32e-02 | reject | 1.71e-03 | reject |
| 3.80e-03 | N6 null-op paired t-test llama | 4.18e-02 | reject | 5.61e-03 | reject |
| 4.00e-03 | N5 null-op paired t-test qwen | 4.18e-02 | reject | 5.64e-03 | reject |
| 6.15e-03 | C2 corrected primary llama Wilcoxon | 5.54e-02 | **fail** | 8.29e-03 | reject |
| 7.30e-03 | P3 multiturn GARP pass-rate collapse | 5.84e-02 | **fail** | 9.43e-03 | reject |
| 8.90e-03 | P12 3B framing GARP pass | 6.23e-02 | **fail** | 1.10e-02 | reject |
| 5.08e-02 | P13 3B framing CCEI t-test | 3.05e-01 | fail | 6.06e-02 | fail |
| 1.80e-01 | P11 severity OLS raw-payoff coef | 9.00e-01 | fail | 2.07e-01 | fail |
| 7.30e-01 | P15 1.5B reciprocal CCEI | 1.000 | fail | 8.08e-01 | fail |
| 8.50e-01 | P14 1.5B reciprocal GARP pass | 1.000 | fail | 9.09e-01 | fail |
| 9.10e-01 | P4 multiturn CCEI | 1.000 | fail | 9.40e-01 | fail |
| 9.40e-01 | P16 GARP-consistency-vs-payoff Welch t | 1.000 | fail | 9.40e-01 | fail |

**Totals:** 22/31 survive Holm; 25/31 survive BH.

**Consistency check:** every test that survives Holm also survives BH (no Holm-reject/BH-fail
cases), the expected relationship since BH is uniformly less conservative than Holm at the same α —
no implementation bug indicated.

### 4. Tests whose significance status changes across raw / Holm / BH

Comparing raw p<0.05 (25/31 tests) against each correction:

- **Raw-significant → Holm non-significant (3 tests):** C2 (corrected primary llama Wilcoxon,
  p=0.00615), P3 (**multiturn GARP pass-rate collapse, p=0.0073** — one of the paper's headline
  results), P12 (3B framing GARP pass, p=0.0089).
- **Raw-significant → BH non-significant:** none — the set of BH-rejecting tests (25) is identical
  to the set of raw-significant tests (25).
- **Holm → BH:** the same 3 tests (C2, P3, P12) differ — fail under Holm, reject under BH,
  consistent with Holm's stricter mid-distribution threshold.
- No test moves from raw-non-significant to significant under either correction — corrections only
  ever remove or preserve significance here.

### 5. Interaction of already-null results with the correction procedure

P4 (multiturn CCEI, p=0.91), P14 (framing GARP-pass survivors, p=0.85), P15 (framing CCEI
survivors, p=0.73) remain clearly non-significant under both Holm (adjusted p = 1.000) and BH
(adjusted p = 0.940, 0.909, 0.808 respectively) — no flips.

One mechanical, non-substantive artifact: under BH, P4's adjusted p (raw p=0.91, rank 30 of 31)
comes out to 0.9400 — identical to P16's adjusted value (raw p=0.94, rank 31, the family maximum) —
rather than P4's own per-rank formula value (0.9403). This is BH's required monotonicity
enforcement (adjusted p-values must be non-decreasing as raw p increases), not a bug, but worth
flagging for anyone re-deriving these by the per-rank formula alone.

**Working file:** `results/stats_2a_holm_bh.json`.

---

## 2B. Within-condition correlations

**(1) Sanity check — reproducing the pooled figures.** Filtering `results/main_ccei.json` to
`model == "qwen2.5:1.5b-instruct-q4_K_M"` and `dose_l1 > 0` yields exactly n=60 (18 baseline + 27
multiturn + 15 reciprocal violating traces, matching Table 1's kept-n minus already-GARP-consistent
traces per cell). Pooled figures on this n=60 sample: Spearman ρ=0.7557 (p=2.99e-12) — paper states
ρ=0.756, p<0.0001, match. Pearson r=0.8190 (p=1.29e-15). Secondary check, llama3.2:3b (n=25):
Spearman ρ=0.6138 (p=0.00110), matching the paper's stated ρ=0.614, p=0.0011 exactly.

**(2) Per-condition correlations**

| Model | Condition | n | Spearman ρ (p) | Pearson r (p) |
|---|---|---|---|---|
| 1.5B | baseline | 18 | 0.7853 (p=1.13e-04) | 0.7358 (p=5.01e-04) |
| 1.5B | multiturn | 27 | 0.7314 (p=1.46e-05) | 0.7258 (p=1.83e-05) |
| 1.5B | reciprocal | 15 | 0.6107 (p=1.56e-02) | 0.9732 (p=1.13e-09) |
| 1.5B | **pooled (n=60)** | 60 | 0.7557 (p=2.99e-12) | 0.8190 (p=1.29e-15) |
| 3B | baseline | 8 | 0.7143 (p=4.65e-02) | 0.9608 (p=1.46e-04) |
| 3B | reciprocal | 17 | 0.5392 (p=2.55e-02) | 0.4733 (p=5.50e-02) |
| 3B | **pooled (n=25)** | 25 | 0.6138 (p=1.10e-03) | 0.8266 (p=3.53e-07) |

All 1.5B within-condition n's (18, 27, 15) are well above a ~10-observation floor; every
within-condition ρ for both models is positive and moderate-to-large (0.54–0.79), in the same range
as the pooled figure.

**(3) Confound check — mean dose and mean Δpayoff per condition (violating-trace subsets)**

| Model | Condition | n | mean dose_l1 | mean Δpayoff |
|---|---|---|---|---|
| 1.5B | baseline | 18 | 27.8009 | 0.015064 |
| 1.5B | multiturn | 27 | 16.1536 | 0.009230 |
| 1.5B | reciprocal | 15 | 19.2393 | 0.010465 |
| 3B | baseline | 8 | 18.7991 | 0.006704 |
| 3B | reciprocal | 17 | 10.3334 | 0.002560 |

Mean dose and mean Δpayoff do co-vary across conditions in both models — the between-condition
level-shift pattern that could in principle inflate a pooled correlation relative to the
within-condition relationship.

**(4) Demeaned-pooled correlation** (removes each condition's own mean from dose and Δpayoff before
pooling, isolating the within-condition signal)

| Model | n | Raw pooled ρ | Demeaned-pooled ρ | Raw pooled r | Demeaned-pooled r |
|---|---|---|---|---|---|
| 1.5B | 60 | 0.7557 | 0.7477 | 0.8190 | 0.8153 |
| 3B | 25 | 0.6138 | 0.7077 | 0.8266 | 0.8140 |

**(5) Factual summary.** For 1.5B, the pooled correlation (ρ=0.7557) is closely tracked by every
within-condition correlation (baseline 0.7853, multiturn 0.7314, reciprocal 0.6107) — all positive,
all in the same 0.61–0.79 range, none near zero or opposite-signed. The demeaned-pooled correlation
(ρ=0.7477, r=0.8153) is nearly identical to the raw pooled correlation, changing ρ by only ~0.008
and r by ~0.004. For 3B, both within-condition ρ's are positive (0.7143, 0.5392) and the
demeaned-pooled ρ (0.7077) is actually *higher* than the raw pooled ρ (0.6138), not lower. In both
models, the numbers show the pooled correlation detecting essentially the same relationship present
within each condition individually — they do not show the signature of a between-condition
dose-level shift substantially inflating the pooled figure.

**Working file:** `results/stats_2b_within_condition.json`.

---

## 2C. Bronars power per cell

### (1) Per-cell Bronars power (uniform-random alternative), Table 1's 5 cells

n=1000 simulated Dirichlet-random agents per trace (seed = replicate index), aggregated per cell
from `results/main_ccei.json`'s existing per-trace `bronars_power` field.

| Model | Condition | n | Mean power | Min power | Max power | Mean random-agent CCEI |
|---|---|---|---|---|---|---|
| llama3.2:3b | baseline | 30 | 0.9997 | 0.9990 | 1.0000 | 0.7255 |
| llama3.2:3b | reciprocal | 28 | 0.9998 | 0.9990 | 1.0000 | 0.7218 |
| qwen2.5:1.5b | baseline | 30 | 0.9995 | 0.9980 | 1.0000 | 0.7217 |
| qwen2.5:1.5b | multiturn | 30 | 0.9997 | 0.9980 | 1.0000 | 0.7200 |
| qwen2.5:1.5b | reciprocal | 24 | 0.9995 | 0.9980 | 1.0000 | 0.7293 |

Cross-checked against `docs/MAIN_EXPERIMENT_RESULTS.md` §0: all 5 cells match to the reported 4
decimal places — no discrepancy.

### (2) Assessment: "uninformatively close to 1 everywhere"?

Yes. All 5 cell means exceed 0.99 (range 0.9995–0.9998), all mins exceed 0.98 (range
0.9980–0.9990), max power is 1.0000 in every cell. Essentially every simulated uniform-random agent
violates GARP on these budget sets, in every cell, with no meaningful cell-to-cell variation. This
triggered the conditional alternative-power calculation below.

### (3) Alternative power against a bounded-perturbation near-rational agent

**No prior implementation exists in this repo.** `audit/BRONARS_NOTE.md` and
`audit/REFERENCE_LEDGER.md` (row R18) discuss Beatty & Crawford (2011) extensively, but their
actual construction is the standard uniform-random Bronars power / Selten area applied to their own
household panel — not a bounded-perturbation near-rational alternative. **What follows is a
Bronars-style power calculation against a bounded-perturbation near-rational alternative, in the
spirit of Beatty & Crawford's demanding-alternative framing — not a reproduction of their exact
method.**

**Simulation design.** Per simulated agent: draw one Cobb-Douglas share `α ~ Uniform(0.2, 0.8)`
once (shared across all T lines — the noiseless agent is exactly rational, so any violation comes
only from the perturbation). At each budget line, perturb: `f_t ~ Uniform(0, η)`,
`sign_t ~ Uniform{−1,+1}`, `share_t = clip(α + sign_t·f_t, 0.01, 0.99)`; bundle stays exactly on the
budget line. Swept `η ∈ {0.05, 0.10, 0.20}`, n=1000 agents per (trace, η).

**Results (mean/min/max power across each cell's kept traces):**

| Model | Condition | n | η=0.05 | η=0.10 | η=0.20 |
|---|---|---|---|---|---|
| llama3.2:3b | baseline | 30 | 0.051 / 0.014 / 0.090 | 0.284 / 0.177 / 0.395 | 0.820 / 0.730 / 0.893 |
| llama3.2:3b | reciprocal | 28 | 0.047 / 0.014 / 0.078 | 0.297 / 0.130 / 0.399 | 0.850 / 0.742 / 0.925 |
| qwen2.5:1.5b | baseline | 30 | 0.046 / 0.004 / 0.118 | 0.259 / 0.095 / 0.434 | 0.794 / 0.585 / 0.932 |
| qwen2.5:1.5b | multiturn | 30 | 0.049 / 0.008 / 0.087 | 0.285 / 0.143 / 0.390 | 0.822 / 0.676 / 0.940 |
| qwen2.5:1.5b | reciprocal | 24 | 0.044 / 0.007 / 0.081 | 0.268 / 0.168 / 0.358 | 0.815 / 0.659 / 0.911 |

Unlike the uniform-random benchmark, power against this harder near-rational alternative varies
substantially by perturbation scale (~4-5% at η=0.05 to ~80-85% at η=0.20) and shows visible
cell-to-cell and trace-to-trace spread at each η — a mechanical property of the simulation design,
not an interpretive claim.

**Caveat.** The exact choice of α's spread, the noise functional form, and the η grid are one
defensible-but-not-uniquely-correct operationalization of "a more demanding null than
uniform-random." Different choices would shift these numbers.

**Working files:** `results/scratch_bronars_2c.py`, `results/stats_2c_bronars.json`.

---

## 2D. Discard breakdown (reciprocal-framing sessions) — feeds Session 4

Computed a per-slot, three-group discard breakdown for all 60 reciprocal-framing slots (30
llama3.2:3b + 30 qwen2.5:1.5b) from `results/main_raw.json`, using the same CCEI/GARP/dose
methodology as `src/analyse_main.py` (incomes = p_t·x_t; `ccei()`/`garp_holds()`; `project()` for
L1 dose, retried once at 120s on any 30s solve failure — no failures occurred).

**Data-structure finding, verified directly:** for every attempt record with `n_valid > 0`, the
`p`/`x` arrays are already truncated to exactly `n_valid` rows (no separate validity mask exists;
verified for all 92 reciprocal attempt records with p/x present). For `n_valid == 0` records, `p`/`x`
keys are entirely absent (confirmed for all 28 such records).

**Sanity check against `docs/MAIN_EXPERIMENT_RESULTS.md` §2:** exact match. llama3.2:3b: 21
first-attempt-success / 7 retry-rescued / 2 residual-discard (matches 9/30, 2/30 discard figures).
qwen2.5:1.5b: 17 / 7 / 6 (matches 13/30, 6/30). **Cross-validation:** combined group1+group2 stats
reproduce `results/main_summary.json`'s existing reciprocal cells exactly (llama n=28, CCEI 0.9713,
GARP 0.393; qwen n=24, CCEI 0.9413, GARP 0.375).

**Group-level summary (n, mean CCEI, sd CCEI, GARP pass rate, mean dose L1):**

| Model | Group | n | mean CCEI | sd CCEI | GARP pass | mean dose L1 |
|---|---|---|---|---|---|---|
| llama3.2:3b | first_attempt_success | 21 | 0.9742 | 0.0393 | 0.4286 | 5.086 |
| llama3.2:3b | retry_rescued | 7 | 0.9624 | 0.0499 | 0.2857 | 9.839 |
| llama3.2:3b | residual_discard | 2 | 1.0000 | 0.0000 | 1.0000 | 0.000 |
| qwen2.5:1.5b | first_attempt_success | 17 | 0.9315 | 0.1621 | 0.4706 | 13.847 |
| qwen2.5:1.5b | retry_rescued | 7 | 0.9651 | 0.0381 | 0.1429 | 7.600 |
| qwen2.5:1.5b | residual_discard | 6 | 0.8821* | 0.2043* | 0.6667* | 24.196* |

\* qwen residual_discard: 3 of 6 slots had `n_valid=0` in every attempt (no p/x data at all — CCEI/
GARP/dose recorded as `null`, excluded from these means, not fabricated). Stats above are over the
3 computable slots only (`n_valid` = 1, 12, 17). Full n_valid distribution for that group:
`{0: 3, 1: 1, 12: 1, 17: 1}`. llama residual_discard slots used `n_valid` = 3 and 14 (both
computable, both trivially/near-trivially GARP-consistent).

**`results/discard_breakdown.json` structure:** top-level keys `description`, `source_data`,
`methodology`, `solve_failures_after_retry` (empty), `sanity_check_vs_docs_MAIN_EXPERIMENT_RESULTS_section2`,
`group_summary_by_model`, and `slots` — a flat list of 60 records (one per model×replicate), each
with `model`, `condition`, `replicate`, `group`, `chosen_attempt`, `n_attempts_present`,
`attempt_n_valid_sequence`, `n_valid`, `ccei`, `garp_pass`, `dose_l1`, `dose_linf`,
`projection_status`, and a `note` field with explicit caveats on every sub-threshold or zero-data
row. `null` in this file means "undefined," not "zero."

No interpretive claims about what these numbers imply for the discard-bias-direction question —
reserved entirely for Session 4.

---

## 2E. Variable count and dose normalization

**Variable-count verification.** Read `src/projection.py`'s actual variable layout directly, not
the stated claim. At T=25, K=2: `n_x = T·K = 50` (continuous, x̃), `n_u = T = 25` (continuous,
ordinal-utility u), `n_U = T(T-1) = 600` (binary comparison indicators — matches the "600 binaries"
claim exactly), `n_d = T·K = 50` (continuous L1-auxiliary variables `d_{t,k}`, added via
`n_vars_full = n_vars + n_d`). Continuous total = `n_x + n_u + n_d = 50+25+50 = 125`. The
previously-stated "75 continuous" (`tex/paper.tex` line ~242; `docs/MAIN_EXPERIMENT_PROTOCOL.md`
§4) omitted the 50 `d` auxiliary variables entirely (it only counted `n_x + n_u = 75`). **125 is the
correct continuous count, not 75. Corrected statement: "$T=25$ is 600 binaries and 125 continuous
variables per trace."**

**Reconstruction check.** All 85 GARP-violating traces' `(p, x, incomes)` were reconstructed from
`results/main_raw.json` via the same first-attempt-with-n_valid≥20 rule used elsewhere, and
`project()` was re-solved (time_limit=30s; 0/85 traces required the 120s retry). All 85 recomputed
`dose_l1` values matched `results/main_ccei.json` exactly (max diff = 0.0), confirming the
reconstruction before the recovered x̃ was used for anything downstream.

**Raw vs. expenditure-normalized dose.** `dose_norm = Σ_t p_t · |x̃_t − x_t|` (price-weighted,
expenditure units, vs. the existing raw quantity-unit `dose_l1`), computed for all 85 traces and
correlated against Δpayoff alongside the existing raw dose:

| Split | n | Spearman ρ (raw) | p | Spearman ρ (norm) | p | Pearson r (raw) | p | Pearson r (norm) | p |
|---|---|---|---|---|---|---|---|---|---|
| Pooled | 85 | 0.7293 | 2.5e-15 | 0.7296 | 2.4e-15 | 0.8207 | 7.0e-22 | 0.8312 | 7.2e-23 |
| 1.5B (qwen2.5) | 60 | 0.7557 | 3.0e-12 | 0.7484 | 6.2e-12 | 0.8190 | 1.3e-15 | 0.8299 | 2.5e-16 |
| 3B (llama3.2) | 25 | 0.6138 | 0.0011 | 0.6485 | 0.00046 | 0.8266 | 3.5e-7 | 0.8249 | 3.9e-7 |

**Comparison to the paper's reported pooled figures (ρ=0.729, r=0.821).** Pooled Spearman ρ changes
from 0.7293 (raw) to 0.7296 (normalized), a difference of 0.0003. Pooled Pearson r changes from
0.8207 to 0.8312, a difference of 0.0105. Per-model: 1.5B ρ changes from 0.7557 to 0.7484 (diff
0.0073); 3B ρ changes from 0.6138 to 0.6485 (diff 0.0347); 1.5B r changes from 0.8190 to 0.8299
(diff 0.0109); 3B r changes from 0.8266 to 0.8249 (diff 0.0017). All correlations remain significant
at p<0.005 in every split, raw and normalized alike. The paper's stated pooled 0.729/0.821 match the
recomputed raw-dose values essentially exactly (the tiny gap is rounding in the paper text).

**Working file:** `results/dose_normalized.json` (full 85-row table: raw dose_l1, dose_norm,
delta_payoff, reconstruction-match flags).

---

## 2F. Extremity stratification

**(1) Alignment spot-check.** Cross-referenced all 85 `results/null_operator.json` traces against
`results/main_ccei.json` filtered to `garp == False`, sorted by (model,condition,replicate),
comparing `dose_l1`/`dose_real`, `raw_payoff`, and `delta_payoff`/`delta_payoff_real` for exact
float equality at every position (full 85/85 check, not a spot sample). **All 85 positions match
exactly**, independently corroborating that `null_operator.json` and `corrected_payoff.json` share
positional order.

**(2) Extremity cutpoints** (`extremity = 1 − raw_payoff`, n=85, using the original fixed-α=0.5
`raw_payoff`)

| Grouping | Stratum | Extremity range |
|---|---|---|
| Tercile | low | 0.0178 – 0.1209 |
| Tercile | mid | 0.1245 – 0.2016 |
| Tercile | high | 0.2041 – 1.0000 |
| Quartile | q1 (low) | 0.0178 – 0.1051 |
| Quartile | q2 | 0.1079 – 0.1498 |
| Quartile | q3 | 0.1536 – 0.2661 |
| Quartile | q4 (high) | 0.2776 – 1.0000 |

**(3) Experiment 1 (original fixed-α=0.5 payoff)**

Tercile:

| Stratum | n | mean extremity | null win-rate | mean Δ_real | mean Δ_null | gap (null−real) |
|---|---|---|---|---|---|---|
| low | 29 | 0.0861 | 0.7241 | 0.0038891 | 0.0058154 | 0.0019263 |
| mid | 28 | 0.1550 | 0.7500 | 0.0055688 | 0.0102468 | 0.0046780 |
| high | 28 | 0.3936 | 0.9643 | 0.0180635 | 0.0504267 | 0.0323632 |

Quartile:

| Stratum | n | mean extremity | null win-rate | mean Δ_real | mean Δ_null | gap (null−real) |
|---|---|---|---|---|---|---|
| q1 (low) | 22 | 0.0766 | 0.7727 | 0.0026100 | 0.0049179 | 0.0023079 |
| q2 | 21 | 0.1276 | 0.5714 | 0.0057081 | 0.0065443 | 0.0008362 |
| q3 | 21 | 0.1928 | 0.9524 | 0.0060652 | 0.0187579 | 0.0126927 |
| q4 (high) | 21 | 0.4499 | 0.9524 | 0.0223728 | 0.0584746 | 0.0361017 |

**(4) Experiment 2 — primary null** (`delta_payoff_null_fixed`), aggregated across 20 draws
(win-rate, gap: mean [min, max])

Tercile:

| Stratum | n | mean extremity | win-rate | gap |
|---|---|---|---|---|
| low | 29 | 0.0861 | 0.5810 [0.4483, 0.6897] | 0.0019096 [0.0004912, 0.0035719] |
| mid | 28 | 0.1550 | 0.6179 [0.4643, 0.7500] | 0.0037424 [0.0017544, 0.0059691] |
| high | 28 | 0.3936 | 0.9286 [0.8929, 0.9643] | 0.0381126 [0.0268283, 0.0529634] |

Quartile:

| Stratum | n | mean extremity | win-rate | gap |
|---|---|---|---|---|
| q1 (low) | 22 | 0.0766 | 0.6227 [0.4545, 0.8182] | 0.0022805 [0.0008186, 0.0036978] |
| q2 | 21 | 0.1276 | 0.4619 [0.3333, 0.5714] | 0.0004602 [−0.0011542, 0.0016905] |
| q3 | 21 | 0.1928 | 0.8405 [0.7143, 0.9524] | 0.0125123 [0.0093080, 0.0161948] |
| q4 (high) | 21 | 0.4499 | 0.9095 [0.8571, 0.9524] | 0.0430822 [0.0270825, 0.0627339] |

**(5) Experiment 2 — oracle null** (`delta_payoff_null_oracle`), aggregated across 20 draws

Tercile:

| Stratum | n | mean extremity | win-rate | gap |
|---|---|---|---|---|
| low | 29 | 0.0861 | 0.7017 [0.4828, 0.7931] | 0.0028969 [0.0011637, 0.0039826] |
| mid | 28 | 0.1550 | 0.7536 [0.6071, 0.8929] | 0.0048055 [0.0034317, 0.0061708] |
| high | 28 | 0.3936 | 0.9589 [0.9286, 0.9643] | 0.0377524 [0.0263610, 0.0530744] |

Quartile:

| Stratum | n | mean extremity | win-rate | gap |
|---|---|---|---|---|
| q1 (low) | 22 | 0.0766 | 0.7409 [0.5000, 0.8636] | 0.0030495 [0.0013362, 0.0043316] |
| q2 | 21 | 0.1276 | 0.6048 [0.5238, 0.7143] | 0.0017226 [0.0003581, 0.0027373] |
| q3 | 21 | 0.1928 | 0.9214 [0.8571, 1.0000] | 0.0135219 [0.0110913, 0.0161900] |
| q4 (high) | 21 | 0.4499 | 0.9500 [0.9048, 0.9524] | 0.0423050 [0.0253884, 0.0609917] |

Purely descriptive/tabular — no claims about which mechanism this supports; reserved for
whichever session writes up Track 3.

**Working file:** `results/extremity_stratification.json`.
