# Kill-check E5 — is claim C2 already occupied by the ML/alignment literature?

Run 2026-08-21. Scope: the ML / AI-alignment literature only. The economics-framed
revealed-preference literature (GARP, Afriat, CCEI) is deliberately **out of scope** here —
it is covered by other kill-checks. Instruments: `scripts/arxiv_ft_search.py` (arXiv full-text,
partial index), the arXiv metadata API, OpenAlex, Crossref, and general web fetch for
non-indexed forum material. Every source below is labelled **peer-reviewed**, **preprint**, or
**blog/forum**.

C2 as stated in `docs/CLAIMS.md`: *"does forcing rationalizability improve, leave unchanged, or
degrade downstream decision quality? A clean negative — 'coherence is orthogonal to competence,
so rationality metrics are not alignment targets' — is a publishable and more interesting
workshop result than a win."*

---

## Falsifier (stated before the finding)

Written down before reading the retrieved papers, so that the verdict is not fitted to what
turned up.

**C2 is ALREADY ANSWERED (→ OCCUPIED) if the ML/alignment literature contains work that:**

1. **manipulates** the coherence of an agent's or a preference model's choices — enforcing a
   coherence axiom (transitivity / completeness / scalar-representability) where it did not
   hold, or relaxing one where it did — rather than merely *measuring* incoherence; **and**
2. measures the **causal effect of that manipulation on an independent downstream quality
   metric**, with a reported sign; **and**
3. does so on a construct close enough to *choice coherence* that a revealed-preference
   restatement contributes no new proposition — i.e. it is about preferences over options,
   not about logical self-consistency of factual assertions.

A stronger form of occupancy: the same result exists **on LLM agents**, and the headline
sentence C2 proposes to publish ("coherence is orthogonal to competence, so rationality
metrics are not alignment targets") is already the stated thesis of a citable work.

**C2 is GENUINELY OPEN if the literature only contains:**

- descriptive documentation that coherence assumptions fail (cycles exist, BT is misspecified),
  with no intervention;
- normative / philosophical argument that coherence is not *required*, with no measurement;
- cycle-tolerant *methods* that beat total-order methods on benchmarks but confound the
  coherence manipulation with a change of model class, optimizer, or parameter count, so that
  the coherence axiom is not the isolated treatment;
- correlational "consistent runs score higher" results, which establish coherence as a
  *predictor* rather than a *treatment*.

**Middle case — PARTIALLY OCCUPIED:** one direction of the manipulation is settled (e.g.
relaxing coherence is known not to cost competence) while the other is not; or the
manipulations exist but are applied to reward models / judges rather than to an agent's own
decision sequence; or the downstream metric is itself a preference judgment rather than an
exogenous payoff.

---

## What the ML/alignment literature says, by strand

### Strand 1 — Non-transitive / cyclic preferences in reward models

**They exist, they are not sampling noise, and their cost to a scalar reward is now priced.**

- **Liu, Long, Shi, Su & Xiao, "Statistical Impossibility and Possibility of Aligning LLMs with
  Human Preferences: From Condorcet Paradox to Nash Equilibrium" (arXiv:2503.10990, 2025,
  preprint, 63pp).** Proves human preferences are representable by a reward model **iff** the
  preference among generated responses is free of any Condorcet cycle, and that under a general
  Luce-type probabilistic preference model **Condorcet cycles exist with probability converging
  to one exponentially fast** in the annotator pool. This is the impossibility result underneath
  the whole strand: reward-based alignment cannot fully represent pooled human preferences.

- **Dong, Yu & Poupart, "The Representation–Rationalizability Tradeoff in Reward Learning"
  (arXiv:2606.00291, 29 May 2026, preprint, 31pp).** *Read in full.* The load-bearing result for
  C2's ML analogue. The excess cross-entropy loss of any embedding-based reward decomposes
  **exactly** into an *embedding loss* (information the representation discards) and an
  *agreement cost* (how far the pooled preferences, seen through that representation, are from
  being rationalizable by **any** scalar reward). Their Theorem 4.2 lower-bounds the agreement
  cost by a margin-weighted cycle probability; a non-zero cycle sum "prevents any scalar reward
  from rationalizing the preferences." The two terms move in **opposite** directions as the
  representation refines — a richer encoder exposes more comparisons that no total order can
  rank consistently. So *the cost of forcing rationalizability is a quantity that rises with how
  well you can see the agent's choices*, there is a data-dependent floor "that representation
  design alone cannot eliminate", and joint embedding+reward training is not guaranteed to find
  the sweet spot. Corroborated experimentally on synthetic data and three real preference
  datasets (Jester, Sushi, MT-Bench) with two sentence encoders. **Note the metric: excess
  fitting loss, not an exogenous decision payoff.**

- **Xing, "Attention Limited Reward Learning" (arXiv:2607.04590, 6 July 2026, preprint, 24pp).**
  *Read in full.* Models each label as passing through a low-capacity, rationally-inattentive
  evaluation channel. Proposition 1: a scalar BT reward can represent observed log-odds **iff**
  their circulation around every cycle vanishes; heterogeneous attention generically fails this.
  A combinatorial Hodge decomposition then prices the irreducible cyclic component. Empirically,
  on a public pairwise arena dataset (32 models, 74 pairs, 15,001 decisive votes) the **observed
  cyclic energy exceeds its sampling-noise null** (parametric bootstrap, p = 0.008; robust to
  vote thresholds of 50 and 200, p = 0.046 / 0.008). The best scalar fit loses 0.0034 bits per
  comparison (≈0.0013 noise-corrected). So the cycles in real preference data over model outputs
  are a population-level feature, not annotator noise.

- **What is done about it.** Four families: (i) general/latent preference models that drop the
  scalar head — GPM (arXiv:2410.02197, **peer-reviewed**, ICML 2025), General Preference RL
  (arXiv:2605.18721, preprint); (ii) explicit transitive/cyclic decompositions — HRC
  (arXiv:2605.17342, **peer-reviewed**, ICML 2026), covariate-assisted intransitive BT via Hodge
  theory (arXiv:2601.07158, preprint); (iii) game-theoretic reformulations (strand 3);
  (iv) **axiom-enforcing loss surgery** — Hollender & Kraiczy, "Enforcing Axioms for AI Alignment
  under Loss-Based Rules" (**peer-reviewed**, ICLR 2026, OpenReview `MpYSoTK65s`), and Xiao,
  Shi, Liu, Long & Su (arXiv:2506.12350, preprint), who show a slight modification of the reward
  objective enforces pairwise-majority or Condorcet consistency under general profiles. Family
  (iv) is the closest existing thing to "enforce coherence as an intervention" — but it is
  theory, on the aggregation rule, with no LLM downstream-quality experiment.

### Strand 2 — Bradley-Terry violations in RLHF, and what happens when BT is enforced anyway

**The failure is documented, and the consequence of enforcing BT anyway has a name: the fit
converges to a pseudo-true ranking that can be wrong.**

- **The reversal result (arXiv:2607.04590, preprint), Example 1, "A three-item projection
  reversal."** Three candidates with deliberative rewards R\*A = 2, R\*B = 1, R\*C = 0, and
  attention-scaled log-odds ℓAB = ε, ℓAC = ε, ℓBC = 5ε. **Every individual pairwise majority
  points in the deliberatively correct direction.** Yet the BT fit yields r†A = (8/3)ε,
  r†B = (10/3)ε, r†C = 0 — i.e. **B is ranked above A although A is best**, and "the reversal is
  not a knife-edge feature of the expansion." The paper states plainly that the projection which
  "discards all cyclic components of the human log odds" induces an error that "is not merely
  cardinal; it can reverse the learned ranking." Proposition 3 adds that no method consuming only
  passive labels can disentangle reward from attention from defaults. **This is the sharpest
  existing statement of "enforced coherence degrades decision quality" in ML vocabulary** — the
  projection operator is exactly the move C1 proposes, and the degradation is exactly C2's
  negative direction. It is analytic plus a real-data existence proof, not a downstream task
  experiment.

- **Sun, Shen & Ton, "Rethinking Bradley-Terry Models in Preference-Based Reward Modeling"
  (arXiv:2411.04991, preprint, 52pp).** Establishes convergence rates for BT reward models, then
  argues BT is **not necessary** from the downstream-optimization perspective, because a reward
  model only needs *order consistency* up to a monotonic transformation. Proposes an
  order-consistent upper-bound alternative and empirically compares reward-modelling objectives
  across many settings. Relevant because it separates "is the total order correct" from "is the
  BT parameterisation imposed" — a distinction the plan's projection framing currently collapses.

- **Xiao, Shi, Liu, Long & Su (arXiv:2506.12350, preprint).** RLHF violates almost all social
  choice axioms (majority consistency, pairwise majority, Condorcet), yet works; they resolve the
  paradox by showing that under mild, empirically plausible assumptions on the preference profile
  RLHF *does* satisfy pairwise-majority and Condorcet consistency. Cuts **against** a naive "the
  incoherence must be hurting us" prior.

- **LLM-side documentation that the assumption fails in the agent's own judgments** (all
  preprints unless noted): TrustJudge (arXiv:2509.21117) measures 15.22% pairwise transitivity
  inconsistency in an 8B/70B-class judge before intervention; "Diagnosing LLM Judge Reliability"
  (arXiv:2604.15302) finds aggregate violation rates of only 0.8–4.1% on SummEval but **33–67% of
  documents exhibiting at least one directed 3-cycle** — aggregate rates hide per-item
  incoherence; "LLM-Derived Preference Judgments Are Not Self-Consistent" (arXiv:2608.17644,
  Cornell/Georgia Tech) tests *cardinal* self-consistency (willingness-to-pay vs. exchange
  indifference) across flight, apartment and hotel scenarios over six models and reports "large
  persistent inconsistencies", concluding LLM preference judgments "cannot be faithfully
  summarized by a single utility function"; "Can LLMs Rank?" (arXiv:2606.30412) instruments
  Kendall's coefficient of consistency ζ (circular triads) on homelessness-service allocation and
  emergency triage.

### Strand 3 — Nash learning from human feedback / von Neumann winner / preference games

**Yes — several of these papers run exactly the "enforce a total order vs. accept cycles"
comparison, and two of them run it on LLMs with downstream generation-quality metrics.**

- **Munos et al., "Nash Learning from Human Feedback" (arXiv:2312.00886, peer-reviewed, ICML
  2024).** Motivates the whole line: preference models "can model non-transitive preferences …
  a characteristic not attainable by reward models since they inherently assign a single score to
  each policy", and Appendix C.2 gives a non-transitive-dice construction where individually
  transitive raters aggregate to an intransitive preference model. Framing, not an A/B.

- **Swamy et al., "A Minimaximalist Approach to RLHF" (SPO; arXiv:2401.04056, peer-reviewed,
  ICML 2024).** States the equivalence explicitly: "assuming an underlying reward function exists
  is equivalent to assuming that there exists a total order over agent behavior." **Figure 5(a)
  is the A/B:** across a variety of intransitive preferences over a discrete set of three options,
  SPO (Minimax Winner, cycle-accepting) "learns the MW almost exactly, while RM always converges
  to a corner." Also reports the honest converse: with *noisy but transitive* preferences the RM
  approach is sometimes **better**, "doing so can provide a strong empirical benefit in some
  stochastic situations." So the sign of the enforce-vs-accept effect is already known to be
  **regime-dependent**, and SPO says so. Domain: synthetic 3-option and MuJoCo continuous
  control, **not** LLMs.

- **Zhang, Zhang, Wu, Xu & Gu, "Beyond Bradley-Terry Models: A General Preference Model for
  Language Model Alignment" (GPM; arXiv:2410.02197, peer-reviewed, ICML 2025).** *Read in full.*
  The cleanest published instance of C2's question in ML clothing. On CyclicPreference datasets
  induced from UltraFeedback (216–363 instances, cycles across instruction-following / honesty /
  truthfulness / helpfulness), the BT reward model scores **62.4%** where random guessing is 50.0%
  and GPM is near-perfect. Then, holding the optimizer and base model fixed (same SPPO/GPO
  settings, matched 2B/8B preference-model sizes, same 8B-class instruct base), **GPM beats BT
  downstream** on AlpacaEval 2.0 and MT-Bench — improvements up to +8.31 win-rate points in one
  cell and +1.34 in another. The treatment isolated is *whether the preference signal is forced
  to be a scalar (transitive) score*; the metric is independent generation quality.

- **Huang, Li, Zhao & Li, "Transitivity Meets Cyclicity: Explicit Preference Decomposition for
  Dynamic LLM Alignment" (HRC/DSPPO; arXiv:2605.17342, peer-reviewed, ICML 2026).** Same
  experiment, one year on and with a three-way arm. Decomposes preferences into orthogonal
  transitive (scalar) and cyclic (vector) components, then compares **BT vs. GPM vs. HRC** as
  preference models feeding the same self-play optimizer. +1.23% on RewardBench 2 with a 2B-class
  preference model, and downstream **44.75% length-controlled win rate on AlpacaEval 2.0 / 46.8%
  on Arena-Hard-v0.1, "significantly outperforming SPPO baselines trained with BT or GPM."** Its
  strongest relative gains are in the *Ties* domain — i.e. exactly where a strict total order is
  most artificial.

- Related, same family: SPPO (arXiv:2405.00675), Direct Nash Optimization (arXiv:2404.03715),
  Multiplayer Nash Preference Optimization (arXiv:2509.23102), Efficient Exploration for Iterative
  Nash Preference Optimization (arXiv:2606.01382), Markov-chain preference alignment
  (arXiv:2606.22652), Stackelberg Learning from Human Feedback (arXiv:2512.16626), and the survey
  "AI Alignment From Social Choice Perspectives" (arXiv:2606.21550). The von Neumann winner itself
  traces to contextual dueling bandits (arXiv:1502.06362, peer-reviewed, COLT 2015).
  "Back to Blackwell" (arXiv:2602.19041) sits in this strand; it is handled by kill-check E6 and
  is mentioned here only as context.

**Answer to the brief's key question:** yes, the enforce-vs-accept downstream comparison exists,
it exists on LLMs, and it has been run at two successive ICML cycles with a consistent sign —
forcing the total order costs downstream quality. The caveat that keeps part of C2 alive is in
the Verdict.

### Strand 4 — "Coherence theorems do not imply competence / goal-directedness"

**This argument is well established, mostly negative and conceptual, and its headline sentence is
already published — in a peer-reviewed philosophy journal.**

- **Shah, "Coherence arguments do not entail goal-directed behavior" (Alignment Forum /
  LessWrong, 3 Dec 2018 — blog/forum).** Constructs the trivial rationalising utility
  (U(h,a) = 1 iff the policy takes a at h, else 0), concluding "all behavior can be modeled as
  maximizing expected utility, but not all behavior is goal-directed." Establishes that
  coherence is a **vacuous constraint** as a predictor of goal-directedness — not that coherence
  harms or helps performance.

- **Thornley (EJT) with Dan H, "There are no coherence theorems" (Alignment Forum, 20 Feb 2023 —
  blog/forum, CAIS Philosophy Fellowship).** Defines a coherence theorem as one stating that an
  agent not representable as an EU maximizer is liable to dominated strategies, and argues **no
  such theorem exists**. Completeness is the weak link: money-pump arguments for completeness are
  non-forcing against an agent following "if I previously turned down X, I will not choose any
  option I strictly disprefer to X." Explicitly holds that agents with incomplete preferences
  **can still act competently**.

- **The counter — Grace, "Coherence arguments imply a force for goal-directed behavior"
  (AI Impacts / LessWrong, 25 Mar 2021 — blog/forum).** Concedes that any observable behaviour
  sequence is consistent with EU maximization, but argues for *probabilistic pressure*: internal
  incoherence creates incentives for reform. Concedes coherence forces only "mark out an aspect
  of the incentive landscape" and note that coherence pressure has not made humans coherent. So
  even the strongest defender of coherence arguments does not claim coherence → competence.

- **Zhi-Xuan, Carroll, Franklin & Ashton, "Beyond Preferences in AI Alignment"
  (arXiv:2408.16984; PEER-REVIEWED, *Philosophical Studies*, 9 Nov 2024,
  DOI 10.1007/s11098-024-02249-w).** *Read the relevant sections in full.* This is the paper that
  most directly pre-empts C2's headline. Three-step argument in §3.1: (i) **"Coherence is not
  rationally required"** — completeness is not a rationality requirement, only coherent
  extendibility is, so rational agents need not be representable as EU maximizers; (ii)
  **"Coherent EU maximization is intractable"** — most utility functions cannot be tractably
  maximized in compliance with the axioms, so agents must either approximate or "insist on
  complying with the rationality axioms, but give up on even approximate optimality with respect
  to their original utility functions… it is not always resource rational to maximize expected
  utility"; (iii) **"Coherence alone is not informative"** — EUT says almost nothing about what
  goals a system will pursue. Its summary table states outright that *"EUT-style global coherence
  is not rationally required," "EUT analyses are only weakly informative about AI behavior,"* and
  *"locally coherent agents may better preserve tool-like corrigibility."* Point (ii) is a
  **published claim that enforcing coherence can cost competence** — arrived at by tractability
  argument rather than by experiment.

- **Thornley, "The shutdown problem: an AI engineering puzzle for decision theorists"
  (PEER-REVIEWED, *Philosophical Studies*, 19 Jun 2024, DOI 10.1007/s11098-024-02153-3)**, with
  the empirical follow-ups in Strand 5. Also: Benavoli, Facchini & Zaffalon, "Why AI Safety
  Requires Uncertainty, Incomplete Preferences, and Non-Archimedean Utilities" (arXiv:2512.23508,
  preprint); "Revisiting the shutdown problem" (arXiv:2606.08296, preprint).

- **Measurement side (both preprints, one peer-reviewed venue):** MacDermott et al., "Measuring
  Goal-Directedness" (arXiv:2412.04758, NeurIPS 2024) defines maximum-entropy goal-directedness
  MEG; "Towards Measuring Goal-Directedness in AI Systems" (arXiv:2410.04683). Both treat
  goal-directedness as a quantity *separate from* coherence, which presupposes the dissociation
  rather than testing it.

**What this strand establishes and does not:** it establishes, with peer review, that coherence
is neither necessary for competence nor sufficient to predict capable or dangerous agency, and
that enforcing it can be computationally costly. It does **not** provide a measured dose–response
between enforced choice coherence and task performance. That measurement gap is the part of C2
that Strand 5 now partially fills.

### Strand 5 — Empirical links between enforced consistency and task performance

Sorted by direction. **"Enforce" below always means the coherence axiom is the manipulated
variable, not the measured one.**

**(a) Enforcing coherence HELPS — and this is the direction the plan does not want.**

- **Zeng, Tendolkar, Baartmans, Wu, Chen & Wang, "LLM-RankFusion: Mitigating Intrinsic
  Inconsistency in LLM-based Ranking" (arXiv:2406.00231, preprint).** *Read in full.* The nearest
  existing thing to C1+C2 combined on an LLM's own judgments. Identifies **order inconsistency**
  and **transitive inconsistency** (non-transitive triads, counted via Kułakowski's method) in an
  LLM's pairwise comparisons, then repairs both — in-context order-agnostic demonstrations plus
  calibration for the first, multi-ranker aggregation for the second — and measures **NDCG@10 on
  TREC DL 2019/2020**, an exogenous IR relevance metric with human labels. Repair **improves**
  quality: +1.30 to +2.75 NDCG@10 in the ICL+calibration ablation, and 65.38 → 71.51 on DL19 for
  an 8B-class model against the standard pairwise baseline. They also show the unrepaired ranker
  is "highly sensitive to the initial order of candidate passages" — the instability that
  coherence repair removes.
- **TrustJudge (arXiv:2509.21117, preprint).** Training-free, inference-time. Likelihood-aware
  aggregation cuts pairwise transitivity inconsistency **from 15.22% to 4.40%** and
  score-comparison inconsistency from 23.32% to 14.89%, **"while maintaining higher evaluation
  accuracy."** Enforced coherence, no quality cost.
- **BlitzRank (arXiv:2602.05448, preprint)** takes the opposite tack in the same setting —
  handles non-transitive preferences by collapsing cycles into equivalence classes and emitting
  tiered rankings rather than a forced total order, across 14 benchmarks and 5 models.

**(b) Enforcing coherence HURTS.**

- **arXiv:2607.04590 Example 1** (projection reversal) — analytic, plus real-data evidence that
  the cyclic component being projected away is above noise.
- **arXiv:2606.00291** — the agreement cost is the priced penalty for forcing scalar
  rationalizability, with a data-dependent floor.
- **arXiv:2401.04056 Fig. 5(a)** — under intransitive preferences, the total-order (reward-model)
  approach "always converges to a corner" while the cycle-accepting method recovers the Minimax
  Winner. Continuous control, not LLMs.
- **arXiv:2410.02197 and arXiv:2605.17342** — BT underperforms cycle-tolerant preference models
  downstream on AlpacaEval 2.0 / Arena-Hard / MT-Bench / RewardBench 2, with optimizer and base
  model held fixed.

**(c) Relaxing coherence costs NOTHING — the dissociation, run on LLM agents.**

- **Cullen, Garland, Roman, Thomson, Ziakas & Thornley, "Towards Shutdownable Agents:
  Generalizing Stochastic Choice in RL Agents and LLMs" (arXiv:2604.17502, v4 9 Jul 2026,
  preprint in ICML format).** *Read in full.* This runs C2's experiment **with the sign of the
  manipulation reversed**, which is logically the same dissociation test. Agents are trained via
  DReST to **violate completeness** deliberately — to satisfy POST (Preferences Only between
  Same-Length Trajectories), lacking a preference between every pair of different-length
  trajectories — and are then scored on USEFULNESS, an independent task-competence metric
  (fraction of available discounted coins collected conditional on trajectory length). The paper
  frames the question in exactly C2's terms: *"The interesting question is how DReST and default
  agents compare with respect to USEFULNESS."* Results, 5 seeds: deep-RL DReST agents score
  **11% (PPO) and 18% (A2C) HIGHER test USEFULNESS than default agents**, with a train–test gap
  49% / 35% smaller; two 8B-class open-weight instruct models fine-tuned to POST reach
  **near-maximum USEFULNESS (1.000 and 0.944 → 1.000) alongside NEUTRALITY ≈ 0.998–1.000**
  across 40 held-out task families; and there is **no measurable "training tax"** — DReST test
  usefulness exceeds default within 10M environment steps. **Deliberately breaking a VNM axiom
  did not cost competence and improved generalisation.** Caveats to keep: USEFULNESS is
  conditional on trajectory length by construction, and the authors flag this as differing from
  the intuitive unconditional notion; the axiom broken is completeness, not transitivity/GARP;
  and the manipulation is training-time, not an inference-time projection.

**(d) Coherent preferences do not transfer into behaviour at all.**

- **Zhou & Ackerman, "When Preferences Fail to Become Incentives: A Utility–Behavior Gap in Large
  Language Models" (arXiv:2606.22974, v2 22 Jun 2026, preprint).** Reproduces the finding that
  LLMs reveal a coherent, model-specific utility structure under pairwise elicitation, then tests
  whether that structure is *motivational*. Writing tasks (essays, grant-proposal abstracts,
  incident postmortems, translations) with quality assessed by a blind independent judge panel;
  the models are first shown to be modulable by direct exhortation, establishing that the quality
  channel works. Then: **"In all tasks, across all models tested, offering LLMs outcomes that
  they report in the choice paradigm as being highly preferred does not lead them to create
  higher quality outputs than offering them dispreferred outcomes, or even no outcomes at all."**
  Conclusion: coherent elicited preferences "should not be taken as evidence that those
  preferences have incentive value for the models or affect their behavior in other contexts."
  This is a published empirical **coherence/behaviour dissociation on LLMs** — the elicited
  coherence is real and it is inert.

**(e) Correlational only (coherence as predictor, not treatment).**

- "Can LLMs Rank? A Tale of Triads and Triage" (arXiv:2606.30412, preprint): under a synthetic
  BTL model, the circular-triad consistency coefficient ζ is "a strong predictor of ranking
  accuracy", monotonically increasing against Kendall τ to ground truth; applied to homelessness
  service allocation and emergency-department triage, three leading models show "considerably
  different performance profiles". They note that prior work "all report consistency metrics and
  ranking accuracy in separate tables."
- Behavioural-consistency-as-uncertainty (arXiv:2602.11619) — already known to the plan, which
  correctly demotes it.

---

## Direct hits on C2, if any

Ranked by how much of C2 they consume. "On LLM agents?" is stated explicitly for each.

| # | Work | Type | Manipulation | Downstream metric | On LLM agents? | Direction |
|---|---|---|---|---|---|---|
| 1 | GPM, arXiv:2410.02197 | peer-reviewed (ICML 2025) | preference signal forced to a scalar (transitive) score vs. not, optimizer + base model held fixed | AlpacaEval 2.0 LC win rate, MT-Bench; RewardBench; cyclic-preference accuracy | **Yes** — 8B-class instruct base, 2B/8B preference models | Enforcing the total order **degrades** (BT 62.4% vs ~random 50.0% on cyclic sets; downstream up to +8.31 WR for the cycle-tolerant arm) |
| 2 | HRC/DSPPO, arXiv:2605.17342 | peer-reviewed (ICML 2026) | three-arm BT vs. GPM vs. explicit transitive+cyclic decomposition, same self-play optimizer | RewardBench 2, AlpacaEval 2.0, Arena-Hard-v0.1, MT-Bench | **Yes** | Enforcing the total order **degrades**; +1.23% RewardBench 2, 44.75% LC-WR / 46.8% Arena-Hard beating both BT and GPM arms |
| 3 | Shutdownable agents, arXiv:2604.17502 | preprint (ICML format) | completeness deliberately **broken** (POST) via DReST reward | USEFULNESS (task competence), 5 seeds, 40 held-out task families | **Yes** — deep RL agents *and* two 8B-class open-weight instruct models | Relaxing coherence costs **nothing**; +11% / +18% USEFULNESS in deep RL, near-maximum in LLMs, no training tax |
| 4 | Utility–behavior gap, arXiv:2606.22974 | preprint | none — tests whether *existing* coherent preferences drive behaviour | blind independent judge-panel quality on four writing tasks | **Yes** | Coherence is **inert**: high-utility incentives produce no quality gain over dispreferred or absent incentives |
| 5 | LLM-RankFusion, arXiv:2406.00231 | preprint | order + transitive inconsistency **repaired at inference time** in the model's own pairwise judgments | NDCG@10 on TREC DL 2019/2020 (human relevance labels — genuinely exogenous) | **Yes** | Enforcing coherence **improves** (+1.30 to +2.75 in ablation; 65.38 → 71.51 on DL19) |
| 6 | TrustJudge, arXiv:2509.21117 | preprint | transitivity violations resolved by likelihood-aware aggregation, training-free | evaluation accuracy vs. reference | **Yes** | Enforcing coherence **does not hurt** (15.22% → 4.40% inconsistency "while maintaining higher evaluation accuracy") |
| 7 | Attention-limited reward learning, arXiv:2607.04590 | preprint | analytic projection onto the transitive/potential subspace | correctness of the recovered ranking | Partly — real arena votes over model outputs, but the *agent* is the annotator population | Projection can **reverse** the correct ranking even when every pairwise majority is correct |
| 8 | Representation–rationalizability tradeoff, arXiv:2606.00291 | preprint | representation richness, which controls how much rationalizability must be forced | excess cross-entropy (fit), not a task payoff | No — reward models on Jester/Sushi/MT-Bench | Forcing rationalizability has a priced, irreducible cost that **grows** with representational fidelity |
| 9 | SPO, arXiv:2401.04056 | peer-reviewed (ICML 2024) | total-order reward model vs. Minimax Winner under intransitive preferences | recovery of the MW; MuJoCo returns | **No** — 3-option synthetic and continuous control | Enforcing the total order **degrades** under intransitivity; but **helps** under noisy-but-transitive preferences |

Rows 1, 2, 3, 4, 5 and 6 all satisfy the falsifier's three conditions and are on LLM agents.
Row 5 in particular is the plan's own intervention shape — inference-time coherence repair on an
LLM's revealed pairwise choices, scored against an exogenous human-labelled metric — and it
reports the **improvement** direction, i.e. the outcome the plan treats as the less interesting
one.

---

## Verdict

### **C2 PARTIALLY OCCUPIED — and the occupied part is the larger part.**

**What is taken:**

1. **The sign question, on LLMs, with matched-ablation experiments.** "Does forcing a total order
   onto preference structure cost downstream quality?" is answered **yes**, at two successive
   ICML cycles (GPM 2025, HRC 2026), with the optimizer, base model and preference-model size
   held fixed so that scalar-transitivity is the isolated treatment, and with downstream metrics
   (AlpacaEval 2.0, Arena-Hard-v0.1, MT-Bench, RewardBench 2) that are independent of the fitting
   objective. A GARP-flavoured restatement adds no new proposition to this.

2. **The converse, on LLM agents.** "Does relaxing a coherence axiom cost competence?" is
   answered **no** (arXiv:2604.17502): deliberately breaking completeness produced +11%/+18%
   task usefulness in deep RL and no loss at all in two 8B-class LLMs, with no training tax.
   That is a direct empirical coherence/competence dissociation, published as such.

3. **The inference-time repair cell — occupied, and in the direction the plan disfavours.**
   LLM-RankFusion (arXiv:2406.00231) and TrustJudge (arXiv:2509.21117) both repair an LLM's own
   intransitive pairwise judgments at inference time and both report **improved or maintained**
   task quality on exogenous metrics. So the plan's "clean negative" is not the safe default it
   is assumed to be; for the *inference-time repair* operator specifically, the published sign is
   positive.

4. **The headline sentence.** "Coherence is orthogonal to competence, so rationality metrics are
   not alignment targets" is not an available finding — it is the standing thesis of
   Zhi-Xuan et al., *Philosophical Studies* 2024 (peer-reviewed), continuous with a
   forum literature running from 2018 (Shah) through 2023 (Thornley) and already conceded by its
   principal opponent (Grace 2021). Add the utility–behavior gap paper (arXiv:2606.22974), which
   supplies the *empirical* version on LLMs: elicited coherent preferences are inert with respect
   to output quality. Publishing this sentence as a result in Aug 2026 would be a restatement.

**What is genuinely still open (the narrow half):**

- No work found applies a **minimal-perturbation projection of an agent's own consumption/choice
  sequence onto the rationalizable set** and scores the result on an **exogenous, non-preference
  payoff** (portfolio return, allocation efficiency, task success). The existing repairs act on
  pairwise *judgments* feeding a ranking, or on *annotator aggregation* feeding a reward model —
  not on the agent's own bundle choices, and not against a payoff that exists independently of
  anyone's preferences. The one paper that analyses the projection operator directly
  (arXiv:2607.04590) does it analytically, on the annotator side.
- No work found varies **degree** of enforced coherence and traces a dose–response curve on task
  quality. Everything is binary: enforced vs. not.
- The **regime-dependence** flagged by SPO — enforcement hurts under genuine intransitivity but
  can help under noisy-but-transitive preferences — has not been mapped for LLM agents. That is a
  real, unclaimed question, and it is a sharper one than C2 as currently written.

**Consequence for the plan's risk asymmetry.** The plan's stated safety net is that *both*
directions of result are publishable. That net is substantially cut. "Enforcement degrades" is
now the consensus of the preference-model literature and would read as confirmatory. "Enforcement
improves" is already reported for inference-time coherence repair on LLM judgments. Neither
outcome is a surprise to a reviewer who reads this strand, and both have peer-reviewed or
well-cited precedent. C2 can survive only if it is re-scoped to the exogenous-payoff /
dose-response / regime-dependence questions above, and if it cites GPM, HRC, the shutdownable-
agents work, and the utility–behavior gap paper prominently and positions against them.

---

## One-line summary for docs/CLAIMS.md

C2 PARTIALLY OCCUPIED: ML already tests coherence-vs-competence both ways (ICML'25/'26: BT total-order costs LLM downstream quality; POST-training costs none); only exogenous-payoff repair is open.

---

## Instrument gaps

Every item here is recorded as a **gap** — an absence of measurement, never as a zero.

1. **Semantic Scholar Graph API — HTTP 429 throughout.** Probed explicitly at the end of the
   session: `GET /graph/v1/paper/search?query=intransitive+preferences+RLHF` returned
   `HTTP 429 {"message": "Too Many Requests…"}`. **No Semantic Scholar evidence was collected at
   all.** Citation-chaining forward/backward from the key papers — the main use of that endpoint —
   did not happen. This is the single largest gap in this kill-check.

2. **arXiv full-text index is partial.** `scripts/arxiv_ft_search.py` documents that it does not
   cover all of arXiv and misses many pre-2021 papers. Every zero or low count from it is weak
   evidence of absence. Strand 4's foundational material (Shah 2018, Thornley 2023, Grace 2021)
   is not on arXiv at all and was reachable only by web fetch.

3. **Two EMPTY results were query artefacts, not literature zeros.**
   `"Bradley-Terry" AND "violat" AND "transitivity"` and
   `"coherence" AND "capability" AND "dissociat"` both returned EMPTY because the instrument does
   exact phrase matching and `violat` / `dissociat` are truncated stems, not words. **Neither is
   evidence about the literature.** Re-run with full words before anyone cites them.

4. **arXiv full-text counts of exactly 200 are ceilings, not counts.** Nine queries returned
   exactly 200 (`"Nash learning from human feedback"`, `"reward model" AND "transitivity"`,
   `"coherence" AND "competence" AND "agent"`, `"Bradley-Terry" AND "misspecification" AND
   "preference"`, and five broad-phrase probes). Those are lower bounds. The broad-phrase probes
   in particular returned topically unrelated results and were abandoned in favour of narrower
   queries — they contributed nothing and should not be read as coverage.

5. **OpenAlex free-text `search=` is unusable for this topic.**
   `search=coherence arguments goal-directed behavior AI` returned 18,468 hits dominated by
   argumentation-mining, EEG and agricultural-policy papers. Switched to
   `filter=title.search:` and `filter=title_and_abstract.search:`, which behaved. Consequence:
   the OpenAlex sweep was title/abstract-scoped, so it cannot corroborate any full-text-only
   finding.

6. **OpenAlex citation counts are unreliable here.** ICML/ICLR papers appear as arXiv-shadowed
   records ("arXiv (Cornell University)") with near-zero citation counts — GPM shows `c: 1`, SPO
   `c: 3` — which is an indexing artefact, not impact. **No impact judgement in this document
   rests on an OpenAlex citation count.**

7. **Crossref does not index PMLR or OpenReview proceedings.** Queries for the ICML papers
   returned unrelated items. Venue and peer-review status for ICML/ICLR entries were confirmed
   from the PMLR/OpenReview banner printed in the PDFs themselves (e.g. "Proceedings of the 42nd
   ICML, PMLR 267, 2025"; "Proceedings of the 43rd ICML, PMLR 306, 2026"), which is weaker
   evidence than a registry record. Crossref **did** resolve both *Philosophical Studies*
   articles cleanly (DOIs recorded above) — those two are solid.

8. **Two peer-reviewed philosophy articles were not read in the original.** *Beyond Preferences
   in AI Alignment* was read via its arXiv version (arXiv:2408.16984), which may differ from the
   *Philosophical Studies* version of record. *The shutdown problem* (Phil Studies 2024) was
   **not read at all** — only its Crossref record and its characterisation by citing preprints.
   PhilPapers and publisher-side full text were not attempted.

9. **Forum sources were read through a general web fetch with no version history.** Post dates
   for the Alignment Forum / LessWrong / AI Impacts items are as displayed on the page; these
   posts are edited in place and the retrieved text may not be the 2018/2021/2023 original.
   Comment threads, where much of the substantive disagreement lives, were not read.

10. **Not attempted at all:** PhilPapers; the NeurIPS/ICML/ICLR OpenReview review threads (which
    would show whether reviewers already raised the coherence-vs-competence framing); ACL
    Anthology; Google Scholar. `hyperresearch fetch` was deliberately not used — sibling agents
    were running concurrently and would contend on its SQLite database.

11. **Coverage skew.** The retrieved corpus is heavily 2026-weighted because the full-text index
    favours recent deposits. Pre-2021 ML work on intransitivity in game evaluation (Nash
    averaging, "Re-evaluating evaluation", open-ended learning in symmetric zero-sum games) was
    **not swept** and is a known blind spot of this kill-check.

---

## Fetch record

**Instrument runs.** 34 arXiv full-text queries via `scripts/arxiv_ft_search.py`; 4 arXiv
metadata `id_list` batches (74 identifiers resolved to titles/dates/authors); 8 OpenAlex queries
(4 free-text `search=`, discarded; 4 `title.search:` / `title_and_abstract.search:`, used);
4 Crossref `query.bibliographic` queries; 1 Semantic Scholar probe (429); 3 web fetches and
2 web searches for non-indexed forum material.

**PDFs downloaded and text-extracted** (all via `curl` + PyMuPDF; sizes are the retrieved PDFs):

| arXiv ID | Short title | Bytes | Depth read |
|---|---|---|---|
| 2606.00291 | Representation–Rationalizability Tradeoff in Reward Learning | 2,969,818 | full — intro, theory §4, related work, refs |
| 2607.04590 | Attention Limited Reward Learning | 659,364 | full — intro, Prop. 1–3, Example 1, arena case study |
| 2604.17502 | Towards Shutdownable Agents (RL agents and LLMs) | 1,140,548 | full — abstract, metrics §2.2, Tables 1–2, discussion §5 |
| 2605.17342 | Transitivity Meets Cyclicity (HRC/DSPPO) | 687,761 | abstract, intro, contributions, downstream tables |
| 2410.02197 | Beyond Bradley-Terry Models (GPM) | 1,535,748 | abstract, intro, §6.2 cyclic, §6.3 downstream, App. E |
| 2408.16984 | Beyond Preferences in AI Alignment | 789,188 | §3.1 coherence arguments in full, Table 3 |
| 2401.04056 | A Minimaximalist Approach to RLHF (SPO) | 5,535,127 | abstract, intro, Fig. 2/5 discussion, results |
| 2312.00886 | Nash Learning from Human Feedback | 657,542 | intransitivity passages, Appendix C |
| 2606.21550 | AI Alignment From Social Choice Perspectives | 584,107 | skim |
| 2607.11432 | Generalizing Preference-based RL: Rationality Model for Incomparability | 650,280 | skim |
| 2503.10990 | Statistical Impossibility/Possibility… Condorcet to Nash | 1,269,532 | abstract + contents |
| 2506.12350 | Theoretical Tensions in RLHF | 501,446 | abstract + intro |
| 2411.04991 | Rethinking Bradley-Terry Models | 10,542,888 | abstract |
| 2602.11619 | When Agents Disagree With Themselves | 771,770 | abstract |
| 2606.22974 | When Preferences Fail to Become Incentives | 2,626,288 | abstract + intro |
| 2608.17644 | LLM-Derived Preference Judgments Are Not Self-Consistent | 820,249 | abstract + intro |
| 2606.30412 | Can LLMs Rank? A Tale of Triads and Triage | 2,392,922 | abstract, §3.2, Fig. 1 discussion |
| 2406.00231 | LLM-RankFusion | 1,269,532* | abstract, §3.3, Tables 3–5 |
| 2604.15302 | Diagnosing LLM Judge Reliability | — | abstract |
| 2602.05448 | BlitzRank | — | abstract |
| 2509.21117 | TrustJudge | — | abstract + intro |

\* size recorded from the download loop; not re-verified.

**Identifiers resolved to titles but not fetched** (screened out on title/abstract): 2601.07158,
2605.18721, 2606.17634, 2602.16610, 2608.12391, 2606.02340, 2608.08491, 2608.06310, 2602.23603,
2604.19786, 2607.16660, 2602.03160, 2601.18722, 2602.12180, 2603.25681, 2602.18550, 2606.13221,
2606.26523, 2606.08267, 2502.16339, 2403.09045, 2608.05455, 2608.07584, 2606.00278, 2605.08503,
2511.12869, 2510.15021, 2406.11039, 2502.14581, 2605.23024, 2601.08777, 2512.16626, 2606.01382,
2509.23102, 2606.07629, 2606.08296, 2605.20203, 2412.04758, 2607.26288, 2606.23985, 2603.21874,
2508.13700, 2505.21371, 2608.02553, 2512.23508, 2410.04683, 2604.21098, 2407.00805, 2310.18244,
2604.17207, 2606.22652, 2606.01561, 2603.21006, 2602.19041 (E6's).

**Web sources fetched** (blog/forum, not academically indexed):

| URL | Author / date as displayed | Status |
|---|---|---|
| alignmentforum.org/posts/NxF5G6CJiof6cemTw/coherence-arguments-do-not-entail-goal-directed-behavior | Shah, 3 Dec 2018 | fetched, read |
| alignmentforum.org/posts/yCuzmCsE86BTu9PfA/there-are-no-coherence-theorems | Thornley (EJT) with Dan H, 20 Feb 2023 | fetched, read |
| aiimpacts.org/coherence-arguments-imply-a-force-for-goal-directed-behavior/ | Grace, 25 Mar 2021 | fetched, read |
| openreview.net/pdf?id=MpYSoTK65s | Hollender & Kraiczy, ICLR 2026 | located via search, **not fetched** — recorded as a gap |

**Registry records confirmed:**
`10.1007/s11098-024-02249-w` (Beyond Preferences in AI Alignment, *Philosophical Studies*,
9 Nov 2024) and `10.1007/s11098-024-02153-3` (The shutdown problem, *Philosophical Studies*,
19 Jun 2024), both via Crossref.
