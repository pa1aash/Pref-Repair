# ITEM 2 / Q7 — the two closest occupants, read in full

Run 2026-08-21. Resolves the first half of `docs/OPEN_QUESTIONS.md` Q7 for **R20**
(`arXiv:2406.00231`, LLM-RankFusion) and **R27** (`arXiv:2608.08491`, TrustRoboReward / POISE).
Both were `unverified` in `audit/REFERENCE_LEDGER.md`; both are now read cover to cover,
appendices included.

**The narrow cell under test**, as stated in Q7:

> Projecting an **agent's own choice sequence** onto the rationalizable set, scoring the result
> against an **exogenous payoff that is not derived from the preference data**, and tracing a
> **dose–response curve** (varying the DEGREE of enforced coherence) rather than a single on/off
> comparison.

**Headline: the cell survives both papers.** Neither occupies it. But the ledger's
characterisation of R27 is wrong in *both* directions and must be corrected — R27 is closer than
recorded on minimality (it is a genuine metric projection with a proved Pythagorean guarantee)
and considerably further than recorded on the payoff axis (the "robot-manipulation test" is a
68-comparison human preference vote on generated video, not a physical success criterion).

**Provenance and method.** Both PDFs pulled with `curl` from the arXiv `/pdf/` endpoint and
text-extracted with PyMuPDF; `hyperresearch fetch` is broken on raw PDFs in this build. Every
number below was cross-checked against a 170-dpi render of the page it sits on, because the
extractor is known to scramble table column order. Pages re-rendered and read as images:
R20 p.5 (Table 3) and p.7 (Tables 4–5); R27 p.9 (Table 3, Figure 2, the PAIBench-G paragraph).
All numbers in this document survived that check.

**Naming.** Model identities are elided per repository hygiene policy and replaced by stable
size-class labels, defined once per paper. No number is changed by the substitution.

---

# A. LLM-RankFusion (`arXiv:2406.00231`)

Zeng, Tendolkar, Baartmans, Wu, Chen & Wang (Oregon State / Penn State). v2, 26 Nov 2024,
18 pp. Footer reads "Preprint. Under review." arXiv metadata carries **no journal reference and
no venue comment** on either version, so it stands as an **unrefereed preprint** as of this run.
Subjects cs.IR / cs.AI / cs.CL.

Size-class labels used below (Table 4 row order): **E1** 11B-class encoder–decoder,
**E2** 20B-class encoder–decoder, **D1** 8B-class open-weight decoder, **D2** 70B-class
open-weight decoder, **D3** 7B-class open-weight decoder, **D4** 13B-class open-weight decoder,
**D5** 8×7B open-weight mixture-of-experts, **P1** mid-tier proprietary, **P2** frontier
proprietary (2023 vintage).

## What it actually does

The system re-ranks 100 BM25-retrieved passages per query. A model is asked, for each pair,
"which of these two passages is more relevant to the query?", and a sorting algorithm
(Bubblesort or Heapsort) turns those pairwise answers into a full ranked list. The paper names
two failure modes:

1. **Order inconsistency** — the answer flips when the two passages are swapped in the prompt
   (positional bias). Measured in Table 1 as the discrepancy between the softmaxed logits of the
   two answer tokens; values run from 0.06 to −1.00, where |1| means total position-determinism.
2. **Transitive inconsistency** — non-transitive triads in the tournament graph over all 100
   passages, counted by Kułakowski's method (Table 2). Circular triads run 0.72 (D3) to 104.67
   (E1) against a stated maximum of 161,684 for 100 passages. Type-1 and Type-2 triads (those
   involving ties) dominate the totals, 4,528–13,483.

Three interventions, none of which is a projection:

- **In-context learning.** A two-turn demonstration in the prompt showing the same pair judged
  both ways round. Changes the *elicitation*, not the elicited data.
- **Calibration.** Query both permutations, read the log-probabilities of the two answer tokens,
  form `P^(ij)_ij = exp(S_A)/(exp(S_A)+exp(S_B))` per permutation (Eq. 1), then set
  `P_ij = exp(P^(ij)_ij) / (exp(P^(ij)_ij) + exp(P^(ji)_ji))` (Eq. 2) so that `P_ij + P_ji = 1`,
  and declare `d_i ≻ d_j` iff `P_ij > 0.5`. This is a fixed re-normalisation formula with no free
  parameter and no distance-to-original term.
- **Borda-count aggregation.** `B(d_i) = Σ_j (m − r_ij)` over ranked-list proposals from different
  sorters and different models (Eqs. 3–5), then sort by Borda score.

### Three findings that the prior summary missed

**(i) Transitive inconsistency is never re-measured after repair.** Table 2's caption states
outright that "This tournament graph is constructed from the comparisons *without* ICL and
calibration." No post-repair triad count appears anywhere in the paper. The only
"consistency" quantity reported after the intervention is the **average Kendall-tau distance
between the ranked lists produced from 100 different initial orderings** (Table 9) — a
run-to-run *stability* measure, not a transitivity measure. The claim that this paper "repairs
transitive inconsistency and improves NDCG" therefore has no direct evidential link in the
paper itself.

**(ii) The component that targets transitivity contributes essentially nothing to the exogenous
metric.** Aggregation across sorters (Table 7, DL19, 100 initial orderings): for D1, best single
sorter 70.57 ± 0.35 → aggregated 70.58 ± 0.45, a gain of **+0.01**. For P2, 74.75 → 75.04
(+0.29). For D5, best single 70.88 → aggregated **69.76**, i.e. *worse* than the better sorter
alone. And in Table 9 the aggregated Kendall-tau distance is worse than the better single sorter
for **all nine models** (e.g. D1: Heapsort 0.060 vs aggregated 0.084). Aggregation buys a
hedge against picking the wrong sorter; it does not buy quality. Essentially the entire headline
NDCG gain comes from ICL + calibration, which attack **positional bias** — a framing/measurement
artefact of the elicitation, not a coherence axiom in the revealed-preference sense.

**(iii) Repair sometimes hurts, and the ledger's quoted range is wrong.** Table 4 individual
components: E2 loses **−2.49** from ICL alone and −0.10 from calibration alone; D2 loses −0.81
from ICL alone. The E5 summary's "+1.30 to +2.75 NDCG@10 in the ICL+calibration ablation" is in
fact just the P2 row read across; the actual ICL+Calibration column ranges **+1.07 to +9.17**,
and individual-component cells reach **−2.49**.

## Exact numbers, with baselines

**Table 4** — NDCG@10, pairwise sorting with Bubblesort from the BM25 initial order, TREC DL 2019.
Baseline = PRP-Sort with no intervention.

| Model | Baseline | ICL only | Calibration only | ICL + Calibration |
|---|---|---|---|---|
| E1 | 67.87 | 68.64 (+0.77) | 69.73 (+1.86) | 71.05 (+3.18) |
| E2 | 72.63 | 70.14 (**−2.49**) | 72.53 (−0.10) | 73.70 (+1.07) |
| D1 | 65.38 | 66.35 (+0.97) | 69.58 (+4.20) | **71.51 (+6.13)** |
| D2 | 72.43 | 71.62 (**−0.81**) | 74.12 (+1.69) | 74.55 (+2.12) |
| D3 | 56.35 | 61.04 (+4.69) | 60.18 (+3.83) | 63.11 (+6.76) |
| D4 | 61.25 | 68.07 (+6.82) | 64.46 (+3.21) | 70.42 (+9.17) |
| D5 | 65.06 | 70.05 (+4.99) | 66.75 (+1.69) | 71.16 (+6.10) |
| P1 | 64.72 | 68.83 (+4.11) | 68.99 (+4.27) | 72.06 (+7.34) |
| P2 | 72.04 | 73.34 (+1.30) | 74.56 (+2.52) | 74.79 (+2.75) |

The ledger's "65.38 → 71.51 on DL19 for an 8B-class model" is the **D1** row and is correct.

**Table 5** — NDCG@10, D1 only, against scheme baselines:

| Scheme | DL19 | DL20 |
|---|---|---|
| Setwise | 63.25 | 60.27 |
| Listwise | 69.61 | **65.49** |
| Pairwise (PRP-Sort) | 65.38 | 60.16 |
| Pairwise + ICL + Calibration (theirs) | **71.51** | 65.10 |

Note the second column: on DL20 the repaired pairwise ranker (65.10) **does not beat the
listwise baseline** (65.49). The paper's prose does not mention this.

**Table 15** (appendix, robustness to prompt wording, D1, DL19, 10 templates):
Bubblesort 62.68 ± 3.07 → 70.84 ± 1.61; Heapsort 63.82 ± 4.63 → 70.10 ± 1.92. The variance
reduction is the more solid of the two effects.

**Data-integrity note.** Table 3 and Table 4 report the same nominal configuration (Bubblesort,
BM25 initial order, DL19) and disagree for two of nine models: D3 is 61.25 in Table 3 but 56.35
in Table 4; D4 is 50.59 in Table 3 but 61.25 in Table 4. The other seven rows match to the digit.
Confirmed by direct page render, so it is a fault in the paper, not in the extractor. D4's
Table-4 baseline is numerically identical to D3's Table-3 entry, which looks like a row shift.
Do not cite either table's D3/D4 entries without flagging this.

A second such fault: Table 8's P2 row (74.82 Bubblesort / 75.02 Heapsort) and its
"Large-Model aggregation" row (74.22 / 74.75) are the exact reverse of Table 7, where 74.22 /
74.75 are P2's *individual* post-repair figures. One of the two tables has the aggregated and
individual values transposed for the large-model group. Also confirmed by page render.

## Four-criterion table — R20

| Criterion | Verdict | Basis |
|---|---|---|
| **Agent's own choice sequence** | **NO** | What is repaired is the model's *relevance judgments about third-party passages* under a query — an evaluative judgment about an external property, for which a ground truth exists (NIST relevance labels 0–3, reproduced in the paper's own Tables 10–11). There is no budget, no bundle, no consumption, no set of alternatives the agent chooses *for itself*. In revealed-preference terms there is no analogue: GARP concerns choices from budget sets where no correct bundle exists, whereas here every comparison has a right answer. This is judgment consistency, not preference coherence. |
| **Exogenous payoff** | **YES (qualified)** | NDCG@10 against TREC Deep Learning 2019/2020 relevance labels — human assessments collected years earlier for a different purpose, wholly independent of the system under test. This is the strongest exogenous metric anywhere in the occupancy set. The qualification: it is still a human *relevance annotation*, not a task payoff or a physical success criterion. It is exogenous **to the repaired data**, not exogenous **to preference** as such. |
| **Dose–response** | **NO** | The ablation is a 2×2 factorial of binary switches — {no ICL, ICL} × {no calibration, calibration} (Table 4) — plus aggregation on/off (Table 7) and aggregation across a fixed model-size group (Table 8). No knob exists to turn. Calibration (Eqs. 1–2) has no temperature, weight, or tolerance; Borda count (Eqs. 3–5) has no strength parameter. The nearest thing to a degree is the number of rankers aggregated, and quality is never traced against it — Table 8 fixes the group at three models and reports one point. |
| **Minimal perturbation** | **NO — and explicitly declined** | No distance-to-original objective appears anywhere. The one place a minimum-perturbation rule could have entered, the authors name it and reject it: "*other rank aggregation methods exist, such as … Kemeny rank aggregation [18] … many of these are either NP-hard or not specifically designed for list aggregation. By using the simple and computationally efficient Borda count method…*" Kemeny aggregation **is** the minimum-Kendall-tau-distance consensus — the minimal-perturbation rule for orderings. They saw it and walked past it on tractability grounds. |

**Verdict on R20: leaves the narrow cell OPEN on three of four criteria.** It is a real occupant
of the neighbouring cell — inference-time consistency repair on a model's own pairwise outputs,
scored against an exogenous human-labelled metric, reporting improvement — and the project must
cite it and position against it. But it repairs *judgments about other items*, uses no
projection, minimises no distance, and has no dose–response. Its explicit refusal of Kemeny is
the single most useful sentence in the paper for this project: it is a published, citable
statement that the minimal-perturbation route was available and was not taken.

---

# B. TrustRoboReward / POISE (`arXiv:2608.08491`)

Wang, Zhan et al. (Peking University + eight collaborating institutions). v1, 9 Aug 2026, 23 pp.
Footer "Preprint"; the acknowledgments section still carries unstripped NeurIPS 2026
funding-disclosure boilerplate, so it is a submission-format preprint. No journal reference in
arXiv metadata. Subjects cs.AI.

Size-class labels: **B4** 4B-class open-weight vision-language backbone, **B8** its 8B-class
sibling, **T** the proprietary teacher used for distillation and as an upper-bound reference.

## What it actually does

The pipeline distils a teacher into a robot-video reward model under **four supervision
paradigms on a shared item pool**: Score-A (rate one trajectory's task progress 1–5), Score-B
(rate a video-QA answer 1–5), Pair-A (compare two trajectories, {win, lose, tie}), Pair-B
(compare two answers). Because all four come from the same teacher on the same items, they
contradict each other: the **cross-paradigm noise rate** is defined as

> `η_cross = Pr_(i,j)[ (v_ij = win ∧ s_i < s_j) ∨ (v_ij = lose ∧ s_i > s_j) ]`

i.e. the fraction of jointly-labelled pairs where the score-implied order contradicts the
pairwise label.

**POISE** (Preference-Ordered Isotonic Score Editing) fixes the pairwise labels, treats them as
a partial order, builds a linear extension `r = (r_1, …, r_m)` from worst to best, and solves

> `(ŝ'_1, …, ŝ'_m) = argmin_{s' ∈ R^m} Σ_i (s'_i − s_{r_i})²  s.t.  s'_1 ≤ s'_2 ≤ … ≤ s'_m`   (Eq. 1)

by the Pool-Adjacent-Violators Algorithm in `O(m)`. PAVA partitions the chain into blocks and
sets every position in block `B_k` to the pooled mean `µ_k = (1/|B_k|) Σ_{j∈B_k} s_{r_j}`
(Eq. 2). Real outputs are then quantised back to `{1,…,5}` by
`ŝ_{r_i} = max(1, min(5, ⌊ŝ'_i + ½⌋))`.

This is a genuine metric projection. Appendix B makes it explicit: `C_r = {x ∈ R^m : x_{r_1} ≤ …
≤ x_{r_m}}` is a closed convex cone, `ŝ' = argmin_{x ∈ C_r} ‖x − s‖²₂ = P_{C_r}(s)`, and Lemma 1
is the standard obtuse-angle characterisation `⟨y − P_C(y), z − P_C(y)⟩ ≤ 0`. **Theorem 1** then
falls out as the Pythagorean consequence: given "golden scores" `g` order-consistent with the
pairwise labels,

> `‖ŝ' − g‖²₂ ≤ ‖s − g‖²₂ − ‖ŝ' − s‖²₂ < ‖s − g‖²₂`

whenever `s` violates the order on at least one comparable pair. **On the minimality axis this is
the real thing**, and the ledger is right to call it the closest published structural analogue.

### Where it is not the same mathematical object as a GARP projection

This matters directly for `docs/OPEN_QUESTIONS.md` **Q3**, and it cuts in the project's favour.

1. **The order is an input, not an output.** POISE takes the ranking as given by the pairwise
   labels and projects only the *cardinal levels* onto a cone. A GARP repair must decide *which
   revealed-preference relations to give up* — the ordering is precisely what is in question.
   POISE solves the half of the problem Q3 identifies as easy (convex, conditional on a fixed
   ordering) and never touches the half Q3 identifies as the scaling risk (the combinatorial
   search over orderings). The GARP-consistent set is a **union over orderings** and is therefore
   **not convex**; `C_r` is convex only because `r` is frozen. Lemma 1 does not survive the union.
2. **It cannot handle cycles at all.** Stated as a precondition: "*The only precondition is that
   {v_ij} induces a valid partial order.*" Cycles are rare in their data only because "*RoboReward
   groups contain at most three items*", they "occur in < 1% of groups", and they "are fixed by
   **expert re-annotation**" — human hands, outside the algorithm. Repeated in Limitations:
   "Extending POISE to large-scale noisy preference graphs without manual cycle repair is an
   important direction for future work." Cycles are the entire problem a GARP repair exists to
   solve; POISE assumes them away.
3. **Dimension m ≤ 3.** Every projection in the paper is over at most three numbers.
4. **Quantisation breaks the guarantee.** Remark 1 concedes that round-half-up "is not a metric
   projection onto a convex set" and bounds the extra error by `√m / 2 ≤ 0.87` — on a 1-to-5
   scale, that is up to 22% of the full range. The proved theorem applies to `ŝ'`, the object
   that is *not* used as a training label.
5. **A ground truth is assumed.** Theorem 1 posits golden scores `g` and assumes the pairwise
   order is consistent with them. Revealed-preference repair has no `g` — there is no true
   utility level to be closer to. Their guarantee is "projection moves you toward the truth";
   the corresponding revealed-preference statement does not exist.

### The downstream test is not what the ledger says it is

The PAIBench-G experiment is, verbatim: "*The task is image-to-video prediction from an initial
robot observation and a manipulation instruction. We conduct a head-to-head comparison between
our 4B reward model and RoboReward-4B over **68 paired comparisons, judged by 3 annotators with
majority vote**. Our method achieves approximately **69% win rate** against RoboReward-4B.*"

So: a **video-generation** policy (a 2B-class video world model tuned with a diffusion RL method,
Appendix E.2) optimised against each reward model, with the comparison decided by **three human
annotators voting on which generated video they prefer**. No confidence interval, no significance
test, n = 68. The paper's own Limitations section says it outright:

> "our downstream validation is based on **video generation and human preference comparison
> rather than closed-loop policy execution on physical robots**."

There is no physical success criterion, no task payoff, no robot. The ledger's "downstream
robot-manipulation test (~69% win rate)" overstates it and should be corrected.

## Exact numbers, with baselines

**Table 1 — main comparison.** Overall = mean of micro-averaged pointwise score agreement and
micro-averaged pairwise accuracy. Cons. = 100 × (1 − mean conflict ratio).

| Row | Recipe | Overall | Cons. |
|---|---|---|---|
| T (proprietary teacher) | — | 78.09 | 68.09 |
| **B4 theirs** | SFT `S2 ∪ P1`, RL `S3` | **77.96** | **71.90** |
| B8 theirs | SFT `S2 ∪ P1`, RL `S3` | 77.46 | 73.58 |
| B8 raw-distillation SFT | `S1 ∪ P1` | 77.21 | 63.66 |
| **B4 raw-distillation SFT** | `S1 ∪ P1` | **77.09** | 64.81 |
| B8 RoboReward baseline | — | 69.82 | 56.14 |
| **B4 RoboReward baseline** | — | **67.83** | 57.26 |
| B4 no fine-tune | — | 62.06 | 62.20 |

The abstract's three headline gaps: 78.09 − 77.96 = **0.13** vs the teacher; 77.96 − 67.83 =
**10.13** vs the RoboReward baseline; consistency 71.90 vs 57.26 and 68.09.

**But 10.13 is not the effect of the projection.** RoboReward-4B is a *different training recipe*
(single-paradigm, no multi-paradigm corpus). The matched comparison for POISE is raw-distillation
SFT on the same four-paradigm corpus: **77.09 → 77.96, i.e. +0.87 Overall** — and that +0.87
requires the additional RL stage.

**Table 2 — data routing (all B4, matched 3-epoch recipes).** This is the isolation that matters:

| Recipe | SFT data | RL data | Overall | Cons. |
|---|---|---|---|---|
| Raw distillation | `S1 ∪ P1` | — | **77.09** | 64.81 |
| **Theirs w/o RL** | `S2 ∪ P1` | — | **76.59** | 67.08 |
| Fully cleaned | `S2 ∪ P2` | `S3 ∪ P3` | 77.53 | 69.79 |
| Pairwise-only cleaned | `S1 ∪ P2` | `P3` | 75.48 | 64.94 |
| Theirs | `S2 ∪ P1` | `S3` | 77.96 | 71.90 |

**Read rows 1 and 2 together.** Both are SFT-only, same corpus size class, same epochs; the only
difference is whether the pointwise scores were isotonically projected. The projection **costs
0.50 Overall** (77.09 → 76.59) while raising consistency by 2.27 (64.81 → 67.08). That is a
coherence-up / competence-down cell **in the paper's own ablation table**, and the paper does not
remark on it. The net gain only appears once the rewritten-label residual `S3` is fed back
through an RL stage — which is a different intervention, not the projection.

Cleaning the pairwise side is worse still: 75.48 vs 77.09, **−1.61**. The authors call this "a
critical asymmetry" and keep the pairwise labels uncleaned in their deployed recipe.

**Table 3 — TrustJudge placement (B4).**

| Reward model | TrustJudge | Overall | Cons. |
|---|---|---|---|
| Theirs | inference | **78.57** | 68.81 |
| Theirs | — | 77.96 | **71.90** |
| Theirs | training | 77.02 | 62.02 |

A second dissociation the paper does not flag: the configuration with the **best** Overall (78.57)
has **worse** self-consistency (68.81) than the configuration it beats (71.90). Their own
explanation is entropy-based, not coherence-based.

**Ablation of the RL stage:** 76.59 → 77.96 Overall (+1.37) but 67.08 → 71.90 consistency
(+4.82) — the authors note the effect is "approximately 3.5× greater on consistency than on
accuracy."

### Two evidentiary faults

**(a) The abstract's central theoretical claim is unsubstantiated in the body.** "POISE provably
reduces training-corpus score-pair reversal conflicts from **20.15% to 0%**, whereas TrustJudge
still retains **20.46%** reversal conflicts on the same training corpus." Those two figures appear
**only in the abstract**. A full-text scan of all 23 pages, all seven tables, and Appendices A–F
finds neither number anywhere else. `η_cross = 0` is a definitional consequence of the projection
and is proved; the *empirical* 20.15% pre-repair rate and the 20.46% comparator are asserted and
never shown.

**(b) Figure 2 contradicts its own prose.** The rendered bar chart labels read: theirs 0.53
pointwise / 0.69 pairwise; RoboReward 0.38 / 0.49; untuned backbone 0.35 / 0.46. The adjacent
paragraph says "*ρ = 0.42 pointwise, ρ = 0.55 pairwise*" and "*Compared to the RoboReward
baseline (0.38, 0.49), Ours 4B improves by +0.04 and +0.06*". The figure implies +0.15 and +0.20.
Worse, the same paragraph claims theirs is "*the only 4B-scale model exceeding the ρ = 0.50
strong-correlation threshold*", which its own quoted pointwise figure of 0.42 does not do. One
of the two is wrong; the paper does not say which. Confirmed by direct page render.

## Four-criterion table — R27

| Criterion | Verdict | Basis |
|---|---|---|
| **Agent's own choice sequence** | **NO — and further away than R20** | Three separate steps of remove. (i) What is projected is the **teacher's** pointwise score labels, not the deployed model's outputs. (ii) The projection is applied to a **training corpus offline**, before any student model exists — it is data cleaning, not inference-time repair of an agent's behaviour. (iii) The items scored are third-party objects (robot trajectory videos, video-QA answers) with an assumed ground truth `g`. The one genuine self-consistency element is that both the scores and the ordering constraints come from the same judge — but they are that judge's *evaluations of other things*, not choices it made for itself under a budget. |
| **Exogenous payoff** | **NO** | The downstream test is a **3-annotator majority-vote human preference win rate** over 68 generated videos. That is a preference judgment by construction. The benchmark metrics are agreement with a 7,030-sample human-annotated gold set; the pairwise half (`PAIR-A`/`PAIR-B`, and hence half of every Overall figure) is pure preference agreement. Only `Score-A` — task-progress rating against a completion rubric — has any claim to being a success criterion, and it is a human rating of a video, not an outcome. The paper's Limitations concede that closed-loop physical execution was never run. |
| **Dose–response** | **NO** | The correction is all-or-nothing per group: PAVA returns the exact projection and `η_cross = 0` by construction. There is no `λ`, no tolerance, no partial step, no fidelity-vs-monotonicity trade-off parameter anywhere in Eq. (1), Eq. (2), or Algorithm 1. The ablations are **discrete configuration swaps**: four `(SFT, RL)` data-routing tuples (Table 2), a drop-the-RL-stage sub-row, and a three-way TrustJudge placement (Table 3). Nothing is traced against a degree. |
| **Minimal perturbation** | **YES** | Eq. (1) is a stated `argmin` of squared Euclidean distance to the original scores subject to a monotonicity constraint; Appendix B identifies it as the metric projection `P_{C_r}(s)` onto a closed convex cone and proves the Pythagorean inequality. This is a formal minimal-perturbation projection, and it is the first one found in the occupancy sweep. Caveats that limit its reach: the cone is defined by a **fixed** linear extension, the dimension is `m ≤ 3`, cycles are excluded by precondition and repaired by hand, and the guarantee is voided by the integer quantisation that produces the actual labels (Remark 1). |

**Verdict on R27: closes the minimality criterion; leaves own-choice, exogenous payoff and
dose–response OPEN.** It is the strongest structural precedent in the corpus and creates a real
citation and vocabulary hazard — "projects raw pointwise scores onto the monotone cone",
published August 2026, with a proved projection theorem. It is *not* a competitor for the cell:
it repairs a teacher's training labels offline, presupposes an acyclic order, works in three
dimensions, and validates against a human preference vote.

---

# Does the narrow cell survive these two?

## Combined criterion matrix

| Criterion | R20 LLM-RankFusion | R27 TrustRoboReward / POISE | Cell status |
|---|---|---|---|
| Agent's **own choice sequence** | **NO** — pairwise judgments about third-party passages, with ground truth | **NO** — a teacher's training-corpus labels about third-party videos, cleaned offline | **OPEN** |
| **Exogenous payoff** | **YES (qualified)** — NDCG@10 vs independent human relevance labels | **NO** — 3-annotator preference win rate, n = 68; gold-set agreement | **OPEN** (R20 satisfies it, but on the wrong object) |
| **Dose–response** | **NO** — 2×2 binary factorial | **NO** — four discrete routing recipes | **OPEN** |
| **Minimal perturbation** | **NO** — Kemeny explicitly rejected as NP-hard | **YES** — L2 projection onto a convex monotone cone, PAVA, Pythagorean theorem | **NARROWED** |

## Verdict: **NARROWED, NOT CLOSED**

No single paper holds more than one of the four criteria, and no pair of criteria is held
jointly by either. The conjunction — own choice sequence **and** exogenous payoff **and**
dose–response **and** minimality — is untouched by both.

What genuinely narrows:

- **Minimality is no longer unclaimed vocabulary.** R27 owns "isotonic projection onto a
  preference-defined monotone cone" with a proof, from August 2026. Combined with R15's prior
  claim on "minimal perturbation index" (`docs/OPEN_QUESTIONS.md` Q8), the project's headline
  phrasing now has two live collisions. The defensible distinction is precise and must be stated
  in the paper's first two pages: **R27 projects cardinal levels onto a convex cone with the
  order held fixed; a GARP repair must search over orders, and the feasible set is a non-convex
  union.** That is the same distinction as Q3, and Q3's answer is now externally corroborated —
  the convex, order-conditional half is published; the combinatorial half is not.
- **The exogenous-metric bar is set by R20, not unoccupied.** TREC relevance labels are a real
  exogenous metric, and any claim of the form "nobody scores coherence repair against something
  outside the preference data" is false as stated. The surviving claim is narrower: nobody scores
  it against a payoff that is not itself a human judgment, on the agent's own choices.

What the two papers unexpectedly *give back* to the project:

- **R20's Kemeny refusal** is a citable, published statement that the minimum-distance
  aggregation rule was considered and abandoned for tractability.
- **R27's Table 2 rows 1–2** are a matched, same-recipe pair in which the isotonic projection
  alone **lowers** Overall quality by 0.50 while raising consistency by 2.27; and **R27's Table 3**
  shows the best-Overall configuration having *worse* consistency than the one it beats. Both are
  coherence/competence dissociations sitting unremarked inside a paper whose thesis is that
  consistency helps. Together with R38 (`arXiv:2602.06286`, isotonic calibration failing outright)
  and R31 (Nitsch et al., a repair intervention failing to improve consistency), the direction of
  the effect is materially less settled than kill-check E5's "the published sign is positive"
  concluded from abstracts.
- **R20's decomposition** shows the transitivity-targeting component contributing ~+0.01 NDCG
  while the positional-debiasing component contributes +6.13. If that generalises, the
  coherence-repair effect reported in the inference-time-repair strand may be largely a
  positional-bias effect wearing a transitivity label. This is a testable, unclaimed proposition
  and it is close to the project's own dose–response question.

**Practical consequence.** The concession the project was preparing to make to R20 and R27 is
warranted in *scope* but not in *degree*. Both must be cited prominently and positioned against;
neither justifies retiring the cell. The three sentences that must appear early in the paper are:
(1) prior repair operators act on judgments about other items, not on the agent's own choice
sequence; (2) the one formal minimal-perturbation projection in the literature fixes the ordering
and projects only cardinal levels, which is the convex, order-conditional sub-problem; (3) no
prior work varies the degree of enforcement.

---

## Ledger updates

Proposed replacement `Status` and `Notes` strings for `audit/REFERENCE_LEDGER.md`. **Not applied
here** — a sibling process owns that file.

**R20** (`arXiv:2406.00231`, LLM-RankFusion)

- Status: `read-in-full`
- Verdict line: *Read in full (18 pp, v2, unrefereed preprint). Repairs an LLM's pairwise
  relevance judgments about third-party passages — not its own choice sequence — via prompt
  demonstrations, logit re-normalisation and Borda aggregation; no projection, no distance
  objective, no dose–response; explicitly rejects Kemeny (the minimum-distance rule) as NP-hard;
  transitivity is never re-measured after repair and the transitivity-targeting component adds
  ~+0.01 NDCG@10. Occupies the neighbouring cell only. Leaves the narrow cell OPEN.*
- Correction to carry: the previously recorded "+1.30 to +2.75" ablation range is the frontier-
  proprietary row alone; the true ICL+Calibration column spans +1.07 to +9.17 and individual
  components reach −2.49. Tables 3 and 4 disagree on two baselines (see this document).

**R27** (`arXiv:2608.08491`, TrustRoboReward / POISE)

- Status: `read-in-full`
- Verdict line: *Read in full (23 pp, v1, submission-format preprint). POISE is a genuine
  minimal-perturbation L2 projection onto a closed convex monotone cone (PAVA, Pythagorean
  guarantee, Theorem 1) — this criterion is CLOSED — but it projects a **teacher's training-corpus
  score labels** offline, holds the ordering fixed as an input, presupposes acyclicity (cycles
  repaired by hand, m ≤ 3), and validates on a 68-comparison 3-annotator human preference win
  rate, not an exogenous payoff. No dose–response. Leaves the narrow cell OPEN on own-choice,
  payoff and dose–response.*
- Corrections to carry: the "downstream robot-manipulation test (~69% win rate)" is a human
  preference vote on **generated video**, not physical execution — the paper's Limitations say so.
  The abstract's "20.15% → 0%, TrustJudge 20.46%" figures appear nowhere in the body. Figure 2
  contradicts its own caption prose (0.53/0.69 plotted vs 0.42/0.55 stated).
