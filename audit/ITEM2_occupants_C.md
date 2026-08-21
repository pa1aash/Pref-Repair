# ITEM 2 / Q7 — the two ICML occupants of C2, read in full

Run 2026-08-21. Both papers read cover-to-cover from the publisher PDFs, **appendices included**,
with every headline number re-derived from the table regions and cross-checked against the prose.
Scope: arXiv:2410.02197 (GPM, ICML 2025) and arXiv:2605.17342 (HRC/DSPPO, ICML 2026) — rows 1 and 2
of the "Direct hits on C2" table in `audit/killcheck_E5.md`, and the two works on which the E5
verdict "**C2 PARTIALLY OCCUPIED — and the occupied part is the larger part**" principally rests.

Prior state: E5 read GPM at abstract/intro/results-table depth and HRC at abstract depth. This
pass reads both in full.

**Headline for the operator, stated before the evidence so it is not fitted to it:**

1. **The treatment is NOT isolated in either paper.** In both, the cycle-tolerant arm is a strictly
   larger model class with strictly more head parameters *and* an extra context-conditioning module
   that the transitive arm never receives. Coherence is confounded with capacity by construction —
   both papers say so themselves, in the form "BT is a special case of GPM".
2. **The direction E5 recorded is wrong on the metric that controls for the known artifact.** On
   GPM's own primary length-controlled metric the cycle-tolerant arm **loses to Bradley-Terry in
   18 of 24 head-to-head cells and in all 8 final-iteration cells.** The "+8.31" E5 quoted is a raw,
   length-uncorrected win rate in the single cell where the treated arm emitted 65% more tokens.
3. **A dose–response curve on transitivity weighting IS already published** — HRC Table 5, nine
   levels of λ against downstream generation quality, with an interior optimum. This is the most
   consequential finding in this document and the operator needs it now.

---

## A. arXiv:2410.02197 — "Beyond Bradley-Terry Models: A General Preference Model for Language Model Alignment" (GPM)

Zhang, Zhang, Wu, Xu & Gu. Peer-reviewed, ICML 2025 (PMLR 267). v3, 11 Jun 2025. 27 pp.

### A.1 What the paper actually does

GPM replaces the scalar reward head of a Bradley-Terry (BT) reward model with a **preference
embedding**: each response `y` is mapped to a vector `v_{y|x} ∈ R^{2k}`, and the pairwise
preference score is a skew-symmetric bilinear form

> `s(y_i ≻ y_j | x) = v_{y_i}ᵀ D(x) R≻ D(x) v_{y_j}`

with `R≻` block-diagonal of `k` copies of `[[0,−1],[1,0]]` and `D(x)` a context-dependent diagonal
scaling produced by an **eigenvalue scale gate** `G_λ(x)`. Embeddings are L2-normalised. The paper
proves (Thm 4.4, 4.5) that this form is fully expressive for any real skew-symmetric preference
matrix, hence can represent arbitrary cycles. It then proposes **GPO**, an SPPO-style iterative
self-play optimiser that maximises the *log-odds* score `s` rather than the win probability `P`.

Preference models are trained on an ~80k-pair public pairwise-preference collection, on two
instruct backbones (2B-class and 8B-class). Downstream alignment post-trains a single fixed
**8B-class instruct policy** for 3 self-play iterations.

### A.2 Is the treatment isolated? — **No. Verdict: CONFOUNDED.**

E5 asserted "optimizer, base model and preference-model size held fixed so that scalar-transitivity
is the isolated treatment". Two thirds of that is right and the load-bearing third is wrong.

**What genuinely is held fixed** (E5 correct here):
- Policy base model: the same 8B-class instruct model in every downstream cell.
- Optimiser: reported *within* column, BT+SPPO vs GPM+SPPO and BT+GPO vs GPM+GPO. Optimiser is
  not confounded with preference-model type.
- Preference training data, learning rate (2e-6), epochs (2), batch size (32), max length (2048),
  schedule, hardware. Tables 8–9.
- Preference-model **backbone** size: 2B-class vs 2B-class, 8B-class vs 8B-class.

**What is NOT held fixed — the three deltas that break the ablation:**

1. **Head capacity.** BT is a scalar head, `d = 1`. GPM is an embedding head of dimension
   `2k ∈ {2,4,6,8}`. The paper states outright: *"BT RM is a special case of GPM when the embedding
   dimension d = 1"* (Table 2 caption, and §4 "Relation to Bradley-Terry Model"). So GPM **nests**
   BT. The comparison is nested-model-vs-restriction: the richer class cannot do worse in-sample,
   and any generalisation gain it shows is jointly attributable to (a) representing cycles and
   (b) simply having more parameters and more directions to fit context-dependent taste,
   multi-aspect trade-offs, and label noise. Nothing in the design separates (a) from (b).
2. **An extra context-conditioning module.** GPM adds the eigenvalue scale gate `G_λ(x)`, a
   prompt-conditioned network that reweights preference subspaces. BT gets no analogue. By the
   paper's **own** Appendix E.1 Table 4, the gate alone is worth **+1.24** RewardBench average
   points on the 2B-class backbone at dim 6 (82.29 with gate vs 81.05 without, both with L2) and
   **+1.31** on the 8B-class backbone at dim 8 (91.90 vs 90.59). That is **larger than the entire
   headline GPM-over-BT margin at 8B (+1.34)**. The gate has nothing to do with transitivity — it
   is context-conditioning, available in principle to a scalar reward model too.
3. **L2 normalisation of the head output**, present in the reported GPM configuration and absent
   in BT. Table 4 shows this is worth up to ±1.5 points on its own and interacts with the gate.

**Consequence.** At the 8B scale, the whole reported GPM-over-BT improvement is arithmetically
within the reach of the scale gate. The "enforcement degrades quality" reading is **not
established** by this design. What is established is "a richer, context-gated preference head fits
this preference data better than a scalar one" — which is a statement about model capacity, not
about the coherence assumption.

### A.3 What object is being enforced or relaxed? — a modelling assumption, not a repair

Strictly: **the functional form of a learned third-party preference proxy.** The transitivity in
question is a *consequence* of choosing a scalar head, not a constraint applied to anything. There
is no operation anywhere in the paper that takes a sequence of choices some agent actually made and
projects it onto a consistent set. The preference data are human/AI annotations from a public
preference collection; the "agent" whose coherence varies is a reward model, not a chooser. The
words GARP, Afriat, CCEI, revealed preference, budget set and rationalizability **do not occur in
the paper** (verified by full-text grep).

So on the audit's own strictness test — *a scalar reward head is a modelling assumption, not a
repair applied to a choice sequence* — GPM is on the modelling-assumption side of the line.

### A.4 Are the downstream metrics exogenous? — **No. Every reported metric is a preference judgment.**

| Metric | What it is | Exogenous? |
|---|---|---|
| CyclicPreference accuracy | agreement with labels the authors constructed | No — it *is* the fitting target's task |
| RewardBench (Chat / Chat-Hard / Safety / Reasoning) | preference-pair agreement accuracy | No — preference agreement |
| AlpacaEval 2.0 LC.WR / WR | pairwise win rate judged by a proprietary frontier judge (Table 3) and a cheaper judge from the same family (Table 5) | No — LLM judge |
| MT-Bench (Table 6) | absolute 1–10 grade from a proprietary judge | No — LLM judge |

**Zero exogenous metrics.** §6.3 prose claims *"We evaluated the models on AlpacaEval 2.0, MT-Bench,
GSM8K, MMLU, etc."* — **no GSM8K or MMLU result appears anywhere in the paper**, main text or
appendix (verified: the string occurs exactly once, in that sentence). The only two genuinely
capability-flavoured, verifier-scorable benchmarks the paper names are promised and never reported.

No seeds, no standard deviations, no confidence intervals, no repeated runs anywhere in the paper.

### A.5 Dose–response? — **Yes, one, on the wrong outcome; none on downstream quality.**

**The knob that exists (Table 2).** Embedding dimension `d ∈ {1, 2, 4, 6, 8}`, where **`d = 1` is
exactly BT**. This is a genuine rank-of-latent-representation dose axis whose zero-dose endpoint is
the fully transitive model. Outcome traced: RewardBench average.

| Backbone | d=1 (BT) | d=2 | d=4 | d=6 | d=8 |
|---|---|---|---|---|---|
| 2B-class instruct | 74.85 | 80.33 | 80.43 | **82.29** | 81.00 |
| 8B-class instruct | 90.56 | 91.37 | 91.60 | 91.86 | **91.90** |

Shape: a large jump at `d=1 → 2` then a flat, wobbly plateau with a **non-monotone interior
optimum at d=6** on the 2B backbone (82.29, falling to 81.00 at d=8). The 8B curve is monotone but
the total range over `d=2…8` is 0.53 points — i.e. essentially flat once you have left `d=1`.
Read strictly, the curve says *"scalar vs not-scalar matters; how much not-scalar barely matters"*,
which is more consistent with a capacity step than with a graded coherence effect.

**The knob that does not exist.** No dimension sweep is run downstream. Tables 3, 5, 6 and 7 never
state which embedding dimension the downstream GPM used. There is therefore **no dose–response
between degree of transitivity relaxation and generation quality** in this paper.

### A.6 Exact headline numbers, exact baseline names

Baselines: `BT RM` (Bradley-Terry reward model, embed dim 1, same data/hparams); optimisers `SPPO`
(Wu et al. self-play) and `GPO` (this paper's); `LN-GPO` (length-normalised GPO variant, App. E.2);
policy base `base` = the unaligned 8B-class instruct model.

**Cyclic preference (Table 1)** — 4 datasets, 216–363 instances each, induced from UltraFeedback:

| Dataset | Random | BT RM | GPM |
|---|---|---|---|
| Cyclic No. 1 (Honest≻Truthful≻Helpful≻Honesty) | 50.0 | 62.4 | 100.0 (+37.6) |
| Cyclic No. 2 (IF≻Truthful≻Helpful≻IF) | 50.0 | 61.6 | 100.0 (+38.4) |
| Cyclic No. 3 (IF≻Honesty≻Helpful≻IF) | 50.0 | 50.0 | 100.0 (+50.0) |
| Cyclic No. 4 (IF≻Honesty≻Truthful≻IF) | 50.0 | 62.9 | 100.0 (+37.1) |

Two caveats the E5 summary did not carry. First, the cycles are **manufactured by switching the
evaluation criterion edge-by-edge** — App. E: "`A ≻ B` based on Honesty, `B ≻ C` based on
Helpfulness, `C ≻ A` based on Honesty". A single-criterion rater is perfectly transitive; the cycle
is an artifact of mixing criteria across edges while withholding the criterion from the model.
Second, on a 3-cycle a scalar model's arithmetic ceiling is **2/3 ≈ 66.7%**, not 50%. BT scoring
62.4/61.6/62.9 is therefore scoring **near its own ceiling**, not "like a random guess". Calling
62.4% "random" mis-states the baseline by comparing it to the wrong floor. This is exactly the
BRONARS_NOTE / killcheck_E2 arithmetic-floor failure mode, recurring in a peer-reviewed paper.

**Downstream, AlpacaEval 2.0 — the number that inverts the E5 verdict.**

Table 3 (proprietary frontier judge) and Table 5 (cheaper judge, same family), 8B-class policy,
GPM − BT deltas on the two win-rate metrics, all 24 head-to-head cells:

| Pref-model size / optimiser | Iter | Δ LC.WR (T3) | Δ LC.WR (T5) | Δ raw WR (T3) | Δ raw WR (T5) | GPM len vs BT len (T3) |
|---|---|---|---|---|---|---|
| 2B / SPPO | 1 | **−1.08** | **−0.75** | +0.89 | +3.06 | 2066 vs 1939 |
| 2B / SPPO | 2 | **−1.46** | **−3.14** | +3.99 | +5.12 | 2301 vs 2032 |
| 2B / SPPO | 3 | **−3.95** | **−6.04** | +3.49 | +3.77 | 2498 vs 2136 |
| 2B / GPO | 1 | +1.26 | +2.51 | +4.87 | +7.18 | 2102 vs 1929 |
| 2B / GPO | 2 | **−2.13** | **−5.08** | +3.06 | +2.90 | 2343 vs 2049 |
| 2B / GPO | 3 | **−4.47** | **−7.23** | +4.05 | +3.10 | 2582 vs 2151 |
| 8B / SPPO | 1 | +1.28 | +1.60 | +3.02 | +4.47 | 1861 vs 1740 |
| 8B / SPPO | 2 | **−1.82** | +1.79 | +1.43 | +5.71 | 2029 vs 1868 |
| 8B / SPPO | 3 | **−3.10** | **−2.07** | +0.72 | +5.04 | 2385 vs 1948 |
| 8B / GPO | 1 | **−0.32** | +3.35 | +2.82 | +6.38 | 1850 vs 1702 |
| 8B / GPO | 2 | **−0.98** | **−0.89** | +2.69 | +4.07 | 2115 vs 1933 |
| 8B / GPO | 3 | **−1.39** | **−0.12** | +2.98 | **+8.31** | **3249 vs 1969** |

Tally: **raw WR — GPM wins 24 of 24. Length-controlled WR — GPM wins 6 of 24, and loses all 8
final-iteration cells.** GPM's responses are longer than BT's in **24 of 24** cells, and the LC.WR
deficit *grows monotonically with self-play iteration in every one of the four blocks*.

The "+8.31" that E5 quoted as the headline is the bottom-right cell: raw win rate, cheaper judge,
where the GPM arm emitted **3249 tokens against BT's 1969 — 65% longer**. In that same cell the
length-controlled win rate is **62.51 for GPM vs 62.63 for BT, i.e. −0.12 against GPM**. The
"+1.34" E5 paired with it is not a downstream number at all — it is the RewardBench *average*
improvement at 8B (Table 2).

**The authors concede the mechanism explicitly** (App. E.2, "Discussion on Length Control"):
*"GPM-aligned models often produce longer responses than BT-aligned models. The standard AlpacaEval
Win Rate (WR) doesn't penalize length, whereas the Length-Controlled Win Rate (LC. WR) is designed
to mitigate length bias, potentially penalizing models that win primarily by being more verbose.
… While beneficial for overall quality perceived by the preference model, this can negatively
impact the LC. WR metric."*

Their remedy, LN-GPO (Table 7), closes the gap to nothing: LC.WR **45.55 (GPM) vs 45.51 (BT)**, a
+0.04 difference, while raw WR is 48.31 vs 43.38 at lengths 2112 vs 1951. Once length is controlled
*and* normalised in the objective, the entire downstream effect of relaxing scalar transitivity is
**four hundredths of a point**, single run, no CI.

**MT-Bench (Table 6)**, base 8.03: BT wins 8 of 12 cells. Best BT 8.30 (8B/SPPO/it2), best GPM 8.38
(2B/SPPO/it2). The 8B/GPO/it3 GPM cell **collapses to 7.54 — 0.49 below the unaligned base** and
0.72 below its BT counterpart.

### A.7 What the authors themselves claim about causality

Deliberately weak. Abstract: *"These findings indicate that our method **may** enhance the alignment
of foundation models with nuanced human values."* §6.3: *"our approach **may** improve reward-based
language model alignment methods."* Conclusion: *"led to performance improvements in downstream
tasks."* They claim GPM *is more expressive* and *fits preference data better*; the causal sentence
"enforcing transitivity costs downstream quality" is **never asserted by the authors**. Nor could
it be — their own length-control discussion tells against it.

---

## B. arXiv:2605.17342 — "Transitivity Meets Cyclicity: Explicit Preference Decomposition for Dynamic LLM Alignment" (HRC / DSPPO)

Huang, Li, Zhao & Li. Peer-reviewed, ICML 2026 (PMLR 306). 26 pp.

### B.1 What the paper actually does — and why its thesis is the *opposite* of what E5 recorded

HRC invokes the Balduzzi et al. (2019) decomposition: any skew-symmetric preference function
decomposes **uniquely** into a transitive potential component `ϕ_T(v,w) = f(v) − f(w)` and a cyclic
component `ϕ_C` with `∫ϕ_C(v,w)dw = 0` (Thm 4.5). Thm 4.6 identifies `ϕ_T` with BT and `ϕ_C` with
GPM. HRC then simply **adds them back together**:

> `s_HRC(y_i,y_j|x) = (r(y_i) − r(y_j))  +  v_iᵀ W v_j`
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`—— transitive ——`&nbsp;&nbsp;&nbsp;&nbsp;`—— cyclic ——`

**This paper's central complaint about GPM is that GPM is not transitive enough.** Theorem 4.7:
a pure skew-symmetric GPM of dimension `2d` can represent a cycle plus a dominant candidate that
beats everything in it *only if `d > 1`*, and **for any fixed finite `2d` there exists a cycle for
which no embedding can preserve both the cycle and the dominant candidate** ("Lack of
Arbitrariness"). Their gloss: *"attempting to model global hierarchies (transitivity) implicitly
through high-dimensional rotation is structurally brittle — complex local cycles can essentially
'crowd out' the geometric capacity required to represent a dominant solution."* HRC's fix is to
hand the model an explicit transitive scalar shortcut back.

That is a peer-reviewed ICML 2026 argument that **removing the transitive component costs
quality**, and it is the paper's entire reason for existing. E5's row 2 ("Enforcing the total order
degrades") reads the paper backwards.

### B.2 Is the treatment isolated? — **No, and worse than GPM's. Verdict: CONFOUNDED, with a strict capacity ladder.**

The three arms form a nested chain: **BT ⊂ GPM ⊂ HRC**. §4.3 states it: *"HRC is theoretically
equivalent to a constrained GPM of dimension `2d + 1`"*, with embedding `v_HRC = [r(y|x), c, v′_y]ᵀ`.
Head dimensions in the downstream comparison (App. C.2) are **BT = 1, GPM = 4, HRC = 4+1**. So each
step up the ladder strictly adds parameters. The paper is candid about what it is doing: *"HRC
(dim=4+1) effectively augments the GPM (dim=4) baseline with an explicit transitive shortcut."*

The confound structure:
- **BT vs GPM**: 1 parameter vs 4, plus GPM gets the context-aware gate `D(x)` and unit-norm
  constraint that BT does not (App. C.3 makes this explicit in the unified objective). Same three
  deltas as in GPM's own paper.
- **GPM vs HRC**: +1 scalar head, plus reward clipping. HRC's own Table 2 shows the non-transitivity
  architecture around it is worth as much as the effect: removing context gating costs **1.14**
  points (2B, dim 2+1) — versus the paper's whole headline HRC gain of **+1.23**.

**What genuinely is held fixed** — and here HRC is materially better than GPM. App. C.2: *"we
independently trained all preference models (BT, GPM, and HRC) from scratch to ensure a rigorous and
consistent evaluation pipeline … all comparisons … are based on models trained on the exact same
data distribution, eliminating potential discrepancies arising from different pre-trained
checkpoints."* A **single unified pairwise-classification objective** (Eq. 54) with `τ = 0.1` covers
all three, differing only in the definition of `s_θ`. Identical hyperparameters (Table 3), identical
SPPO protocol (Table 4, `T=3`, `K=5`, `β=0.001`, temperature 1.0), identical policy base.

This makes HRC's BT-vs-GPM cells the **best-controlled replication of GPM's claim in the
literature** — and they do not replicate it. See B.5.

### B.3 What object is being enforced or relaxed?

Same answer as GPM, one step further from the project. The transitive component is a **head in a
learned preference proxy**, and λ (below) modulates the **weight of that head in the signal shown to
the optimiser over training time**. Nothing is projected. No agent's own choice sequence is touched.
GARP / Afriat / CCEI / revealed preference / rationalizability: **zero occurrences** (verified).

### B.4 Are the downstream metrics exogenous? — **No, and this paper is explicit that they are not.**

RewardBench 2 (Best-of-4, six domains incl. Ties) and RewardBench are preference-agreement.
AlpacaEval 2.0 LC.WR, MT-Bench avg, and Arena-Hard-v0.1 WR are all judged by proprietary frontier
LLMs — three different ones, named per benchmark in §6.3. Zero exogenous metrics. No seeds, no
standard deviations, no confidence intervals anywhere (verified by grep: the strings do not occur).

To their credit, §C.7 does the judge-validation work GPM did not: a 500-pair confusion matrix
against human annotation gives **Cohen's κ ≈ 0.7655** (TP 247, FP 32, FN 26, TN 195), and a
three-judge cross-evaluation (Table 11) preserves the ranking `HRC+DSPPO > GPM+SPPO > BT+SPPO`
(41.90/41.14/40.56, then 36.14/35.77/35.25, then 46.11/44.89/43.05). Two integrity notes: the human
panel is **one annotator** ("a human annotator", singular), and §6.3 advertises *"inter-annotator
agreement measurements"* which §C.7 then does not deliver — C.7 says "three complementary analyses"
and lists two.

### B.5 The number that matters most: BT vs GPM under a controlled replication

This is the single cleanest test in either paper of "enforce the total order vs accept cycles",
because a third party trained both arms from scratch in one codebase with one objective and one set
of hyperparameters. All 18 downstream head-to-head cells (Tables 7, 8, 9), Δ = GPM − BT:

| Benchmark | PM = 2B-class | | | PM = 8B-class | | |
|---|---|---|---|---|---|---|
| | it1 | it2 | it3 | it1 | it2 | it3 |
| AlpacaEval 2.0 **LC.WR** | −1.44 | +1.64 | +0.17 | +0.09 | +0.93 | +0.58 |
| Arena-Hard-v0.1 WR | −1.4 | +1.9 | +1.2 | −3.6 | **−6.5** | −2.5 |
| MT-Bench avg | +0.21 | 0.00 | −0.38 | −0.35 | +0.20 | −0.44 |

**BT wins 9, GPM wins 8, one tie.** At the final iteration on the 8B-class preference model, BT wins
2 of 3. On preference modelling the same pattern holds: RewardBench 2 (Table 1) gives BT **70.10**
vs GPM(2) **70.08** vs GPM(4) **69.69** on the 8B-class backbone — *BT beats both cycle-tolerant
arms* — and the authors write it plainly: *"simple scalar models perform surprisingly well, with BT
(70.10%) slightly edging out GPM (70.08%)."* On the 2B-class backbone GPM(dim 2) at **55.32** is
*below* BT at **55.93**; only GPM(dim 4) at 56.40 clears it.

**GPM's headline does not survive independent retraining.** RewardBench v1 average, 2B-class
backbone, same preference dataset, same benchmark:

| | BT | best GPM | margin |
|---|---|---|---|
| GPM's own Table 2 | 74.85 | 82.29 | **+7.44** |
| HRC's Table 6 (independent retrain) | **79.76** | 80.99 | **+1.23** |

The independently-trained BT baseline scores **4.91 points higher** than the BT baseline GPM
reported, and roughly five sixths of GPM's headline advantage evaporates. At 8B: GPM's own +1.34
(90.56 → 91.90) becomes +0.68 (90.46 → 91.14). This is a baseline-strength problem, and it is the
strongest single piece of evidence that GPM's margin was capacity-and-tuning, not coherence.

### B.6 Dose–response? — **YES. This is the finding the operator needs.**

DSPPO defines a **time-varying preference score** (Eq. 12):

> `s_t = (1 + λ/√t) · s_T  +  (1 − λ/√t) · s_C`

`λ > 0` starts training transitive-heavy and lets the cyclic component in gradually; `λ < 0` does
the reverse; `λ = 0` is the static equal-weight HRC signal. Both coefficients → 1 as `t` grows, so
λ tunes the **early-training tilt toward the transitive component**, not a static mixture. At
`|λ| > 1` and small `t` one coefficient goes negative — i.e. the schedule actively *inverts* one
component; the authors flag this as semantically ill-posed.

**Appendix C.4, Table 5 — nine λ levels traced against downstream generation quality**
(AlpacaEval 2.0, iteration 3, 8B-class preference model, 8B-class policy, base LC.WR 33.13):

| λ | regime | LC.WR | raw WR | avg len |
|---|---|---|---|---|
| −2.0 | inverse (cyclic-first, extreme) | **37.27** | 41.41 | 2170 |
| −1.0 | inverse | 38.66 | 43.09 | 2192 |
| −0.5 | inverse | 40.21 | 44.22 | 2179 |
| 0.0 | static, equal weights | 40.62 | 46.30 | 2245 |
| +0.25 | transitive-first, mild | 41.09 | 44.84 | 2183 |
| +0.50 | transitive-first | 40.85 | 42.98 | 2139 |
| +0.75 | transitive-first | 41.54 | 43.73 | 2139 |
| **+1.0** | transitive-first (proposed) | **41.90** | 44.79 | 2171 |
| +2.0 | transitive-first, extreme | 40.15 | 44.30 | 2186 |

**Shape: a clean inverted U with an interior optimum at λ = +1.0.** The negative branch is
monotone-decreasing in the cyclic-first direction (40.21 → 38.66 → 37.27); the positive branch rises
to +1.0 then falls at +2.0. Total span **4.63 LC.WR points** — several times larger than any BT-vs-
GPM effect in either paper. Response length is flat across the sweep (2139–2245), so this is not a
verbosity artifact.

Authors' reading: *"λ > 0 generally leads to better performance … λ < 0 consistently underperforms.
This validates our hypothesis that starting from stable, transitive preference signals and gradually
incorporating cyclic components is beneficial for training, while the reverse trajectory struggles
to establish a solid foundation."* They also tried `λ/∛t` and sinusoidal schedules; *"these variants
did not exhibit stable or consistent improvements."*

**Direction, stated bluntly: more weight on the transitive component makes downstream quality
better, up to an interior optimum. Less transitive weight makes it monotonically worse.**

Two limits on how far this curve reaches. (i) The dose is a *schedule tilt*, not a static amount of
coherence: at every λ both components are present, and as `t → ∞` all schedules converge to the same
signal. The endpoints "pure BT" and "pure GPM" are **not on the curve** — they are the separate,
coarse arm comparison of B.5. (ii) One benchmark, one iteration index, one preference-model size,
one run per point, no CI.

A **second, unswept knob exists**: Eq. (7) carries static mixing weights `C1, C2` on the transitive
and cyclic terms. They are never assigned values, never varied, and the unified objective in App. C.3
silently sets both to 1. A static coherence-weight dose–response is therefore *available* in HRC's
formalism and **not run**.

Third knob, weakly swept: latent dimension `2d ∈ {2,4}` for GPM and `2d+1 ∈ {2+1, 4+1}` for HRC
(Tables 1, 6). Non-monotone — HRC(2+1) beats HRC(4+1) on RewardBench 2 at both scales (57.63 vs
57.12; 70.95 vs 70.67), while HRC(4+1) beats HRC(2+1) on RewardBench v1 at 8B (91.99 vs 91.84).

### B.7 Exact headline numbers, exact baseline names

Baselines: `BT+SPPO` (dim 1), `GPM+SPPO` (dim 4), `HRC+SPPO` (dim 4+1), `HRC+DSPPO` (λ = 1, the
full method). Preference-model backbones 2B-class and 8B-class instruct; policy an 8B-class instruct
model; scalability check on a 9B-class instruct backbone, 4-bit quantised.

- **RewardBench 2 average, 2B-class**: BT 55.93 / GPM(2) 55.32 / GPM(4) 56.40 / **HRC(2+1) 57.63**
  / HRC(4+1) 57.12. The abstract's "**+1.23%**" is **HRC over the best GPM arm** (57.63 − 56.40),
  *not* over BT (that margin is +1.70). E5 recorded +1.23 as an enforce-vs-relax number; it is a
  GPM-vs-HRC number, i.e. a *pro-transitivity* number.
- **RewardBench 2 average, 8B-class**: BT 70.10 / GPM(2) 70.08 / GPM(4) 69.69 / **HRC(2+1) 70.95**
  (+0.85 over best baseline = BT) / HRC(4+1) 70.67.
- **Ties domain** (the subset E5 highlighted): 2B-class BT 37.25 / GPM(2) 38.24 / GPM(4) 37.25 /
  HRC 39.22. 8B-class BT 73.53 / GPM(2) 71.57 / GPM(4) 73.53 / HRC 74.51. Note GPM(2) at 8B is
  *below* BT on Ties. The Ties gain belongs to HRC, i.e. to *adding the transitive head back*.
- **AlpacaEval 2.0 LC.WR, iteration 3**: 2B-class PM — base 33.13, BT+SPPO 40.08, GPM+SPPO 40.25,
  HRC+SPPO 43.00, **HRC+DSPPO 44.75** (+1.75 over static HRC). 8B-class PM — BT+SPPO 40.56,
  GPM+SPPO 41.14, HRC+SPPO 40.62, **HRC+DSPPO 41.90**.
- **Arena-Hard-v0.1 WR, iteration 3**: 2B-class PM — base 29.9, BT+SPPO 40.9, GPM+SPPO 42.1,
  HRC+SPPO 43.6, **HRC+DSPPO 46.8** (+3.2 over best baseline). 8B-class PM — BT+SPPO 43.7,
  GPM+SPPO 41.2, HRC+SPPO 44.6, HRC+DSPPO 44.7; peak 45.5 at iteration 2.
- **MT-Bench, iteration 3**: 2B-class PM — base 8.07, BT 8.08, **GPM 7.70**, HRC+SPPO 8.11,
  HRC+DSPPO 8.24. 8B-class PM — BT 7.99, **GPM 7.55**, HRC+SPPO 8.21, HRC+DSPPO 7.86. The
  cycle-tolerant GPM arm ends **below the unaligned base at both scales**.
- **Scalability, 9B-class 4-bit policy (Table 12)**: base 38.38, BT+SPPO(it3) 48.79,
  **HRC+DSPPO(it3) 52.20** (+3.41 over BT). No GPM arm was run here.

HRC also reports a length audit in its own favour: *"unlike GPM baselines which exhibit signs of
'reward hacking' by inflating response length (e.g., jumping to 2168 tokens), our method maintains
concise outputs (2111 tokens)"* — an independent confirmation of the length pathology documented
in A.6.

**Synthetic dominant+cycle experiment (§6.1, App. C.1)**: two-stage learning, ~50% → ~75% (find the
dominant candidate) → 100% (learn the cycle). HRC(2+1, 4+1) clears stage 1 faster and ends higher
than GPM(4); **GPM(dim 2) fails to capture the cyclic structure at all**. No numbers beyond the
50/75/100 stage markers are reported; there is no figure with axes in the released text.

**Falsified assumption, reported honestly**: Thm 4.6 requires `E[v] = 0`. Measured, it is not:
*"HRC (dim=2+1) trained on [the preference collection] with [the 2B-class backbone], we obtain
E[v] ≈ (0.13, −0.51). This suggests that the GPM component may indeed capture some transitive
signal."* So the claimed orthogonality of the transitive and cyclic components **does not hold
empirically in their own trained model** — which means even HRC's decomposition does not cleanly
isolate a "cyclicity dose".

### B.8 What the authors themselves claim about causality

They claim (a) HRC models mixed transitive–cyclic structure better than either BT or GPM, (b) DSPPO's
transitive-first schedule converges better than static, (c) the framework "consistently outperforms
existing baselines". They **never** claim that enforcing transitivity costs quality. Their claim is
the reverse in spirit: *"larger models with stronger intrinsic capabilities may require a more
conservative balance between the cyclic and transitive components to maintain stability in
multi-turn reasoning"* — i.e. **more transitivity is a stabiliser**, and at scale you want more of it.

---

## What these two genuinely close, and what they do not

### (i) Established with an isolated treatment

**Almost nothing about coherence.** Neither paper contains an isolated treatment of the coherence
assumption. In both, the cycle-tolerant arm is a strict superset model class with more head
parameters plus a context-conditioning gate the transitive arm never gets. What is isolated, and
genuinely established, is narrower:

1. **A skew-symmetric bilinear preference head can fit deliberately-constructed cyclic preference
   data that a scalar head cannot** (GPM Table 1, 100% vs ~62%). This is a representation-theoretic
   fact with an empirical demonstration. It is not in dispute and the project should concede it
   immediately. It is also close to a tautology — the datasets were built to be unfittable by a
   scalar head, and BT's 62.4% is near its own 66.7% ceiling, not near random.
2. **Re-adding an explicit transitive scalar component to a cycle-tolerant preference model improves
   downstream generation quality**. Taking the clean same-optimiser contrast HRC+SPPO vs GPM+SPPO at
   2B-class / iteration 3: LC.WR **43.00 vs 40.25 (+2.75)**, Arena-Hard **43.6 vs 42.1 (+1.5)**,
   MT-Bench **8.11 vs 7.70 (+0.41)**; plus HRC over GPM on RewardBench 2 at both scales. (Adding
   DSPPO on top widens these to +4.50 / +4.7 / +0.54, but that also changes the optimiser.) This
   contrast *is* well-controlled — same objective,
   same data, same hyperparameters, only the extra scalar head differs — and its direction is
   **pro-transitivity**.
3. **Under a controlled, unified-codebase replication, BT and GPM are indistinguishable downstream**
   (B.5: 9–8–1 across 18 cells).

### (ii) Merely suggested by a confounded comparison

Everything E5 recorded as the occupied part of C2:

- "Forcing a total order onto preference structure costs downstream quality" is **not** shown. On
  the length-controlled metric GPM's own tables show the opposite in 18 of 24 cells and in 8 of 8
  final-iteration cells; the +8.31 headline is a raw win rate at 65% length inflation; the authors'
  own length-normalised fix reduces the effect to +0.04; and an independent retrain shrinks the
  preference-modelling margin from +7.44 to +1.23.
- "Two successive ICML cycles with a consistent sign" is **not** the case. Cycle two is a paper whose
  entire thesis is that the cycle-tolerant model is *insufficiently* transitive, whose controlled
  BT-vs-GPM replication is a coin flip, and whose own dose–response favours the transitive side.
- "Downstream metrics independent of the fitting objective" is true only in the trivial sense that
  the judge is a different model from the reward model. **Every** downstream metric in both papers
  is a preference judgment — LLM-judged pairwise win rates or LLM-graded scores. Neither paper
  reports a single verifier-scorable or task-payoff metric. GPM promises GSM8K and MMLU and reports
  neither.

### (iii) Net effect on C2 and on the E5 verdict

E5's verdict — "**C2 PARTIALLY OCCUPIED — and the occupied part is the larger part**" — was reached
on row 1 and row 2 of its own table, read at abstract/results-table depth. Read in full, **rows 1
and 2 do not carry the weight E5 put on them**, and the sign E5 recorded for both is not supported
by the papers' own primary metrics.

This does **not** un-occupy C2. Rows 3–6 of the E5 table (arXiv:2604.17502 completeness-breaking,
arXiv:2606.22974 utility–behavior gap, arXiv:2406.00231 LLM-RankFusion, arXiv:2509.21117 TrustJudge)
are untouched by this pass and remain the live threats — and row 5 in particular is still the plan's
own intervention shape reporting the *improvement* direction. What changes is:

- The claim "the sign question is answered, on LLMs, with matched-ablation experiments" **must be
  withdrawn**. It is answered on LLMs with *nested-model* experiments, on LLM-judged metrics, with
  no seeds, and the two studies disagree once length is controlled.
- The space for a *properly controlled* coherence-vs-competence experiment is **larger than E5
  concluded**, provided the treatment is genuinely isolated — which, for a projection operator
  applied post hoc to a fixed agent's choices, it can be in a way it structurally cannot be for a
  learned preference head. **That is now the project's strongest single differentiator and it should
  be stated in the abstract.**
- Simultaneously, the *dose–response* differentiator is weakened. See below.

---

## Is a dose–response curve already published?

**Yes — one strong one and one weak one, both on adjacent axes, neither on the project's axis.**

**Strong: HRC/DSPPO Table 5 (arXiv:2605.17342, App. C.4).** Nine levels of λ ∈ {−2, −1, −0.5, 0,
0.25, 0.5, 0.75, 1, 2}, where λ sets the early-training weight on the transitive component relative
to the cyclic one, traced against AlpacaEval 2.0 length-controlled win rate at iteration 3. Inverted
U, interior optimum at λ = +1.0 (41.90), monotone decline into the cyclic-first regime
(40.21 → 38.66 → 37.27), decline again at the extreme transitive tilt (+2.0 → 40.15). Span 4.63
points. Length flat across the sweep, so not a verbosity artifact. **This is a published
dose–response between degree of transitivity emphasis and downstream generation quality, in a
peer-reviewed ICML paper, and it favours transitivity.**

**Weak: GPM Table 2 (arXiv:2410.02197).** Five levels of embedding dimension d ∈ {1, 2, 4, 6, 8}
with **d = 1 exactly equal to the fully transitive BT model**, traced against RewardBench average.
Non-monotone with an interior optimum at d = 6 on the 2B-class backbone. Outcome is
preference-agreement accuracy, not task quality.

**What this damages, and what it does not.**

Damaged:
- Any framing of the contribution as "**first** to vary the *degree* of coherence enforcement rather
  than toggling it on/off". That sentence is no longer available; HRC ran a nine-level sweep and
  GPM ran a five-level one.
- Any framing that predicts an interior optimum as a *novel* qualitative finding. HRC already
  reports an inverted U with an interior optimum, and explains it with a curriculum-learning story.
- Any assumption that the published prior favours the cycle-tolerant extreme. It does not: the
  published curve's optimum sits on the transitive-heavy side, and its worst point is the most
  cyclic-first setting.

Not damaged — and these are the load-bearing differences, which should be the paper's positioning:
1. **The dose is applied to a different object.** λ weights a *component of a learned third-party
   preference proxy* inside a training-time schedule. A GARP projection applies a dose to the
   *agent's own observed choice sequence*, post hoc, at inference time, with the agent and its
   training untouched. HRC's λ cannot be run on a fixed black-box agent; a projection operator can.
2. **The dose is not a coherence measure.** λ has no interpretation as "how much of the observed
   incoherence was removed". CCEI-indexed or perturbation-indexed dose does, and is comparable
   across agents, tasks and model families. λ is not.
3. **The outcome is not exogenous.** Every point on HRC's curve is an LLM-judged win rate, on a
   benchmark with a documented length pathology that the sibling paper demonstrates. An exogenous
   payoff — a verifier-checkable score, a market/portfolio return, a task-completion rate not
   derived from any preference judgment — is reported **nowhere in either paper**. This is the
   single cleanest unoccupied axis and it should carry the contribution.
4. **The endpoints are absent.** HRC's curve never reaches "fully coherent" or "fully incoherent";
   both components are present at every λ and all schedules converge. A projection dose runs from
   the raw choice sequence to full GARP-consistency, endpoints included.
5. **No variance.** Single run per λ, no seeds, no CI, one benchmark, one iteration index. A
   properly powered curve with seeds and CIs is a real methodological contribution over this table
   — but it is an incremental one, and should be sold as rigour rather than as novelty.

**Operator action:** the dose–response contribution survives, but **only if the paper is explicit
that the novelty is the object (an agent's own choices), the dose metric (a coherence index), and
the outcome (an exogenous payoff) — not the mere fact of varying a degree.** A draft that claims
"we are the first to trace a dose–response rather than an on/off comparison" will be desk-rejected
by any reviewer who knows HRC. Rewrite that sentence before anything else.

---

## Required related-work positioning

Three sentences, usable close to verbatim. They concede exactly what is established, and no more.

> **On the object of the intervention.** A parallel line in preference-based alignment varies the
> transitivity of the *preference model* rather than of an agent's choices: GPM (ICML 2025) replaces
> the scalar Bradley-Terry reward head with a skew-symmetric preference embedding, and HRC/DSPPO
> (ICML 2026) decomposes the preference function into orthogonal transitive and cyclic components
> and schedules their relative weight during self-play. Because the cycle-tolerant arm in both cases
> is a strict superset of the transitive one — both papers state that Bradley-Terry is the
> dimension-1 special case of their model — those comparisons confound the coherence assumption with
> representational capacity, and additionally endow the cycle-tolerant arm with a context-conditioning
> gate the scalar arm never receives; our treatment is applied post hoc to a fixed agent's realised
> choice sequence, so capacity, training and the policy itself are identical across doses by
> construction.

> **On the reported sign.** We do not assume that relaxing coherence helps: on GPM's own
> length-controlled win rate the cycle-tolerant arm loses to Bradley-Terry in 18 of 24 head-to-head
> cells and in every final-iteration cell, with the reported gains confined to raw win rates at
> response lengths up to 65% longer — a mechanism the authors themselves identify — and an
> independent unified-codebase retrain by HRC shrinks the preference-modelling advantage from +7.44
> to +1.23 while finding the two arms statistically indistinguishable downstream (BT 9, GPM 8, one
> tie over 18 cells). We therefore treat the sign of the coherence–competence relationship as open,
> which is precisely what a controlled dose–response is for.

> **On the dose axis.** HRC/DSPPO reports the closest existing analogue to a dose–response curve —
> nine settings of a schedule parameter weighting the transitive against the cyclic component,
> traced against a length-controlled win rate, with an interior optimum on the transitive-heavy side
> — but the dose there is a training-time weight on a component of a learned preference proxy, it
> carries no interpretation as a quantity of incoherence removed, and every outcome in both papers
> is an LLM-judge win rate or a preference-agreement score. Our contribution is a dose indexed by a
> revealed-preference consistency measure over an agent's own choices, scored against a payoff that
> is not derived from any preference judgment, which is the comparison neither paper is able to make.

Two tactical notes for the write-up:

- **Cite both as friendly precedent, not as rivals.** They are evidence that the question is live at
  ICML, that reviewers will recognise it, and — through HRC's Theorem 4.7 and its transitive-first
  schedule — that the pro-coherence direction is already respectable in the venue. Framing them as
  wrong invites a reviewer who is one of their authors. Framing them as *answering a different
  question about a different object* is both true and safe.
- **Do not repeat E5's summary of them anywhere.** The "+8.31 win-rate points" and "+1.23% on
  RewardBench 2" figures as characterised in `audit/killcheck_E5.md` are, respectively, a
  length-uncorrected number from the most length-inflated cell in the paper, and an HRC-over-GPM
  margin rather than an enforce-vs-relax margin. Either would be caught.

---

## Ledger updates

Exact replacement strings for `audit/REFERENCE_LEDGER.md`. **Not applied here** — a sibling process
owns that file. Columns follow the existing schema: ID | Title | arXiv/venue | Relevance note |
Claim | Status | Provenance.

**R24** — arXiv:2410.02197

- Relevance note (col 4) →
  `**NOT in the plan.** Nested-model comparison, NOT an isolated coherence ablation: cycle-tolerant arm is a strict superset of BT (BT = embed dim 1) plus a context gate BT never gets. On the length-controlled metric the cycle-tolerant arm LOSES in 18/24 cells and 8/8 final-iteration cells; the +8.31 is raw WR at 65% length inflation (3249 vs 1969 tok), same cell LC.WR is -0.12. Authors concede the length mechanism (App. E.2); their length-normalised fix leaves +0.04. Dose-response on embed dim d in {1,2,4,6,8} exists but on RewardBench agreement, not task quality. Zero exogenous metrics; GSM8K/MMLU promised in 6.3, never reported. No seeds/CIs.`
- Status (col 6) → `read-in-full`
- Provenance (col 7) → `Surfaced by E5; read in full ITEM2/Q7 2026-08-21 — E5's sign for this row is NOT supported by the paper's primary metric`

**R25** — arXiv:2605.17342

- Relevance note (col 4) →
  `**NOT in the plan.** Reverses E5's reading: the paper's thesis is that the cycle-tolerant model is INSUFFICIENTLY transitive (Thm 4.7), and its fix is to re-add an explicit scalar transitive head. Best-controlled BT-vs-GPM replication in the literature (unified objective, identical hparams, all arms retrained from scratch) finds a wash: BT 9 / GPM 8 / 1 tie over 18 downstream cells; BT beats both GPM arms on RewardBench 2 at 8B (70.10 vs 70.08 / 69.69). Shrinks GPM's RewardBench margin from +7.44 to +1.23. The abstract's +1.23% is HRC-over-GPM, not enforce-vs-relax. **CARRIES A PUBLISHED DOSE-RESPONSE CURVE**: App. C.4 Table 5, nine levels of schedule weight lambda in {-2,-1,-0.5,0,0.25,0.5,0.75,1,2} vs AlpacaEval 2.0 LC.WR, inverted U, interior optimum at lambda=+1.0 (41.90), monotone decline into the cyclic-first regime (40.21/38.66/37.27), span 4.63 pts, length flat. Direction favours transitivity. Dose is a training-time weight on a preference-proxy component, not a coherence index on an agent's choices; outcome is an LLM-judge win rate. Also: HRC's own orthogonality assumption E[v]=0 measured false (E[v] ~ (0.13,-0.51)). No seeds/CIs; judge validated at Cohen's kappa 0.7655 against ONE annotator.`
- Status (col 6) → `read-in-full`
- Provenance (col 7) → `Surfaced by E5; read in full ITEM2/Q7 2026-08-21 — E5 recorded this row's direction backwards; DOSE-RESPONSE ALREADY PUBLISHED, see ITEM2_occupants_C.md`

**Consequential edits owed elsewhere** (flagged, not made here):

- `audit/killcheck_E5.md` "Direct hits on C2" rows 1 and 2 — direction column and the "matched
  ablation" characterisation both need correction; the Verdict's point 1 ("with the optimizer, base
  model and preference-model size held fixed so that scalar-transitivity is the isolated treatment")
  is false as to preference-model capacity and must be withdrawn or qualified.
- `docs/CLAIMS.md` C2 — the sign of the published prior is not what the claim currently assumes.
- Any draft sentence asserting priority for "dose–response rather than on/off" — must be rewritten
  around object, dose metric and outcome exogeneity. This is now the highest-priority text change
  in the repository.
