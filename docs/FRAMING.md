# FRAMING — locked positioning for the F3 paper

**Status: FROZEN as of session S1, 2026-08-21.**

**AMENDED 2026-08-22 (§5.1 only).** The freeze was lifted deliberately, once, by the principal
investigator, to resolve contradiction C-1 recorded in `audit/HR_PARTIAL_S1/FRAMING_CONTRADICTIONS.md`.
Pre-amendment sha256 `716dfc699e20a2a1aba6475e575d36b50288ca1606a15815906f57d1beb4afc4`;
post-amendment sha256 `9c73659f9878997f7d2ed5395502c64d756e53b8b900edb7f6500bc8b74ea4e3`.
Only §5.1 was touched. Every other section stands as frozen, and the report-don't-revise rule remains
in force for them.

**AMENDED 2026-08-26 (§1 rewritten; new §3 added; §§3–7 renumbered to §§4–8 accordingly).** The freeze
was lifted deliberately a second time, by the principal investigator, to reconcile C1 with what
`docs/PILOT_RESULTS.md` and `docs/GO_NOGO_ASSESSMENT.md` actually license, and to promote a pilot
finding to a standalone claim (C3). Three pilot findings motivate the changes, each cited at the point
it is used below: (i) headroom and measurement reliability do not coexist across the two piloted
scales (`PILOT_RESULTS.md` §5) — the 1.5B model has headroom but a noisy CCEI (WSCV 14.8%), the 3B
model has a stable CCEI (WSCV 2.0%) but almost no headroom (mean baseline CCEI 0.9919); (ii) the 3B
framing manipulation is clean and large on the violation-count metric (GARP pass 0.76→0.17, p=0.0010)
while the 1.5B framing "effect" is confounded by selective discard (`PILOT_RESULTS.md` §3); (iii) the
1.5B discard rate itself — 52% of reciprocal-framing sessions failed the output-format contract — is a
finding about instrument validity, not a footnote (`PILOT_RESULTS.md` §3, §6).
Pre-amendment sha256 (measured at the start of this session)
`a6a5468a1860d79d5625c5b8aee5c45f5a79c41b6104d6d68be1b5ec664824b3`;
post-amendment sha256 `4ab272f403f5e9fce61c9937c642626b60f42aad6a26dba184327c3bc08e3107`
(computed immediately before this hash string was inserted, per the same convention as the
2026-08-22 entry — the hash necessarily does not cover the bytes of its own insertion).
**Reported, not silently fixed:** the pre-amendment hash just above does not reproduce the
post-amendment hash recorded in the 2026-08-22 entry immediately above
(`9c73659f9878997f7d2ed5395502c64d756e53b8b900edb7f6500bc8b74ea4e3`). Either that earlier hash was
mis-recorded, or the file changed between 2026-08-22 and the start of this session without a logged
amendment. This is flagged for the operator's attention and is not resolved by this amendment.

Nothing in this file may be silently revised. If
the resumed research pipeline (or anything else) surfaces evidence that contradicts a claim here,
the contradiction is **reported**, not edited away. The record of what was believed at freeze time
is the point.

Inputs: `docs/F3-PLAN-ORIGINAL.md` (immutable brief), G0's six kill-checks, G0.5's items 1–5,
`docs/VENUE.md` (live CFP + fit audit), `docs/GO_NOGO_ASSESSMENT.md` (QUALIFIED YES).

---

## 0. One paragraph on what changed, and why the claims below are not the brief's claims

The brief's premise was priority: *"everyone measures whether LLM agents violate revealed-preference
axioms; nobody fixes it."* That is false. Six published systems repair LLM choice or judgment
consistency — three at inference time — and one of them (R27, August 2026) owns the phrase
"projection onto a preference-defined monotone cone" with a proof. A published nine-level
dose–response curve exists (R25, ICML 2026). A Fed working paper invisible to every arXiv sweep
(R41) already steers LLM economic choices toward payoff-maximising behaviour with a continuous
control parameter. **The paper cannot claim to be first at anything it originally intended to claim
to be first at.** What survives is a conjunction nobody holds, and a measurement argument nobody
can make with their design. The claims below are scoped to exactly that and no further.

---

## 1. C1 — restated (amended 2026-08-26)

> **C1 (amended).** For an LLM agent's *own* choice sequence over budget sets, **at the model scale
> where the pilot found headroom (1.5B-class, `qwen2.5:1.5b`)**, the minimal perturbation required to
> restore GARP-rationalizability is computable exactly, and the relationship between the **amount** of
> that perturbation and the agent's performance on an **exogenous payoff** — one not derived from any
> preference judgment — is measurable, monotone or non-monotone as the data determine, and identified
> without confounding coherence with model capacity. **The identical procedure is also run at a scale
> with no measured headroom (3B-class, `llama3.2:3b`) as a null-effect control** — not to extend the
> dose curve across scale, but to demonstrate the identification strategy works correctly where there
> is nothing to repair.

**What changed from the frozen (2026-08-21) statement, and why.** The original C1 reads as if a single
dose–response curve would be traced *across* a scale range. `docs/PILOT_RESULTS.md` found that headroom
and measurement reliability do not coexist anywhere in the two-model range piloted: at 1.5B there is
dispersion to repair, but CCEI's own test–retest WSCV is **14.8%** (95% CI [3.0%, 23.5%]) —
statistically indistinguishable from Nitsch et al.'s human band (WSCV ≈ 15%); at 3B CCEI is stable
(WSCV **2.0%**, CI [0.4%, 2.7%], ~7× tighter than the human band), but there is almost nothing to
repair — mean baseline CCEI 0.9919 and not one of 25 sessions below the random-agent benchmark of
0.7406. Running the main experiment "across a scale range" would silently blend a noisy-but-real
candidate effect with a clean-but-absent one. **The experiment is instead run at the scale where
headroom actually exists (1.5B), and the 3B result is kept as what it is — a null-effect control on
the identification strategy, not a second point on the same dose curve.**

**What is claimed:** the *conjunction* — own choices, exogenous payoff, and a dose axis indexed by
a coherence measure, run at 1.5B where the pilot licenses it — the identification argument that follows
from applying the operator post hoc to a fixed agent, and the null-control demonstration at 3B that the
same pipeline reports no repairable incoherence where none is expected.

**What is explicitly NOT claimed, and is conceded in the paper's first two pages:**

- Not that repair is new. It is not (R13, R20, R21, R27, R29, R30, R37).
- Not that projection onto a consistency-defined set is new. It is not (R27).
- Not that "minimal perturbation" is our term. The object already has a name in economics — the
  **non-linear Least Squares index** (R43, traced to Varian 1985) — and we use that name.
- Not that varying a degree rather than toggling is new. It is not (R25 App. C.4, R24 Table 2).
- Not that the sign of the effect is predicted. It is not; that is the measurement.
- **Added 2026-08-26: not that the 1.5B dose–response curve is measurable on a single replicate.**
  Within-condition CCEI at 1.5B is as noisy as Nitsch's human data. The paper states this as a limitation
  it owns rather than a problem it hides. It is why `docs/MAIN_EXPERIMENT_PROTOCOL.md` draws
  **independent** budget-set replicates per session rather than the pilot's repeated-identical-condition
  design, and why the required replicate count comes from an explicit power calculation against the
  pilot's own effect size rather than a round number.

**C1's three sub-claims, and how each now dies — scoped to the 1.5B headroom model unless noted:**

- **C1a (computability).** Dead if the MILP in §5 fails to solve to a usable gap at the design's
  (T, K), or if the γ-margin projection distance proves sensitive to γ. Both are checkable before
  any model call. Unaffected by this amendment.
- **C1b (bounded cost).** Dead if the perturbation needed is so large the projected sequence is a
  different agent. Note R6's own data cuts *for* us here: cycles are frequent but shallow — a
  Condorcet winner survives in >90% of cases — which is the regime where minimal perturbation is
  cheap. Unaffected by this amendment.
- **C1c (identified, measurable effect).** Dead if projected and raw agents are indistinguishable
  on the exogenous payoff **and** the distance-matched null-operator control is also
  indistinguishable, leaving no signal of any kind, **at 1.5B, over enough independent replicates
  that "indistinguishable" is a power statement rather than a noise statement.** A negative direction
  does not kill C1c — but see C2 for what a negative is now worth. **At 3B, C1c is expected to fail to
  reject the null; that is the control functioning correctly, not the claim failing.**

**The adverse prior, stated in the claim rather than hidden from it.** Three published attempts to
enforce a coherence constraint moved the wrong way: a choice-revision intervention on human
budget-set data lowered CCEI (R31, *PNAS*), isotonic calibration worsened its target in 14 of 16
cells (R38), and enforcing the additive probability axiom on model embeddings worsened held-out MSE
(R14). C1 is a hypothesis with evidence against it, not a formality. The paper says so.

---

## 2. C2 — restated

> **C2 (frozen).** The relationship between enforced choice-coherence and downstream competence in
> LLM agents is currently **unidentified, not merely unanswered**: every existing comparison either
> confounds the coherence assumption with representational capacity, or scores the outcome with a
> preference judgment, or both. Measuring it on a fixed agent with a graded, cardinal coherence
> index (CCEI) and an exogenous payoff supplies the identification the existing binary,
> capacity-confounded, judge-scored comparisons cannot.

**This differs from the session brief's expected wording, and the divergence is deliberate.** The
brief anticipated C2 becoming *"replicating and extending a partially-established finding."* G0.5
Item 2c read the two ICML papers in full and found the "partially-established finding" is not
established:

- The cycle-tolerant arm in **both** R24 and R25 is a **strict superset model class** — both papers
  state Bradley–Terry is the dimension-1 special case of their model — plus, in R24, a
  prompt-conditioned scale gate the scalar arm never receives, worth **more than the entire headline
  margin**. Coherence is confounded with capacity by construction.
- On R24's own **length-controlled** win rate the cycle-tolerant arm **loses to Bradley–Terry in 18
  of 24 head-to-head cells and in all 8 final-iteration cells**. The "+8.31" figure is raw and
  length-uncorrected, from the cell where the treated arm emitted 65% more tokens.
- R25 — the better-controlled replication, all arms retrained from scratch under one objective —
  finds a **wash**: 9 / 8 / 1 tie across 18 downstream cells.
- **Zero exogenous metrics** appear in either paper. Every downstream number is an LLM-judge win
  rate or a preference-agreement score.

So `audit/killcheck_E5.md`'s Verdict point 1 — "the sign question is answered, at two successive
ICML cycles" — **is withdrawn**. The sign is open. That is *better* for C2 than G0 believed, and it
is why C2 is framed as an **identification** claim rather than a replication claim.

**What C2 is worth now.** Less than the brief assumed, in one specific way that must not be papered
over: the plan's risk asymmetry ("either direction is publishable") is gone. A negative is the
fourth negative in a literature with three — a replication. A positive matches R21 and R37. The
paper's value does not come from the sign; it comes from being the first estimate of that sign that
is not confounded.

---

## 3. C3 — the discard-selection instrument-validity finding (new, 2026-08-26)

> **C3 (new).** A framing manipulation that measurably disrupts an LLM agent's task performance does
> not necessarily register as measured incoherence — it can instead register as **failure to produce a
> scoreable output at all**. At 1.5B, the reciprocal-framing manipulation broke the required
> output-format contract in **52% of sessions** (13 of 25; median valid rounds fell from 24 to 16). A
> naive revealed-preference instrument that discards unparseable sessions — standard practice, and the
> pilot's own baseline handling — silently drops exactly the observations where the framing
> manipulation had its largest behavioural effect, biasing any measured coherence effect toward zero.
> **This is a finding about instrument validity. It holds regardless of whether preference repair
> helps, hurts, or does nothing to downstream performance**, and it is reported as a claim in its own
> right rather than folded into C1's dose–response result.

**Why this is a separate claim, not a footnote to C1.** C1 is about what happens to the observations
that survive discard. C3 is about the observations that do not survive, and about what discarding them
does to any inference drawn from the ones that remain. The two are logically independent: C3 is true
even if C1 turns out to be entirely null, and C1 could in principle be answered cleanly even if C3's
selection problem did not exist — e.g. if disruption and discard were uncorrelated with the framing
treatment. The pilot shows they are not: discards under reciprocal framing at 1.5B (13/25) vastly
exceed discards under baseline framing at 1.5B (3/25) and reciprocal framing at 3B (0/25).

**The evidence.** `docs/PILOT_RESULTS.md` §3: under reciprocal framing at 1.5B, 13 of 25 sessions were
discarded for failing to produce ≥20 of 25 valid, format-conforming rounds. The 12 surviving sessions
are not a random subsample of what the model would have produced; they are precisely the sessions where
the model coped with the harder framing, which is itself informative about the manipulation's effect
and is exactly the information a silent discard throws away. The pilot's own illustration: 1.5B's naive
baseline→reciprocal CCEI delta is +0.0169 (p = 0.66, not significant) — a number the pilot explicitly
flags as "almost certainly survivorship, not an effect" (`PILOT_RESULTS.md` §3), because it is computed
only on the observations the manipulation did *not* disrupt enough to break the output contract.

**What C3 requires of the main experiment.** `docs/MAIN_EXPERIMENT_PROTOCOL.md` Part 6 specifies how
disrupted sessions are handled going forward — not silently dropped, as the pilot's own baseline
handling did. The discard rate is reported as a per-condition outcome alongside CCEI, GARP pass rate,
and the projection dose, so C3's finding is measured at the scale the main experiment actually runs
(1.5B), not merely asserted from the pilot alone.

**Kill condition.** C3 is killed by evidence that the pilot's 52% figure is an artefact of one prompt
template or one seed range rather than a property of the framing manipulation itself — e.g. if the main
experiment's larger, independently-seeded replicate set shows the reciprocal-framing discard rate is
statistically indistinguishable from the baseline discard rate. That comparison is reported explicitly
in `docs/MAIN_EXPERIMENT_RESULTS.md`, not assumed.

---

## 4. Abstract-level framing

Title: **"What Does Repairing Choice Inconsistency Actually Buy? A Budget-Set Diagnosis."**

> Repairing an AI agent's incoherent preferences is not a new idea: inference-time layers that
> restore transitivity, isotonic projections onto preference-defined cones, and training-time
> rationality penalties have all been proposed, and several report downstream gains. What no
> existing result establishes is *how much* coherence is worth, because every published comparison
> either varies the coherence assumption by swapping in a strictly richer model class — confounding
> coherence with capacity — or scores the outcome with another preference judgment, or treats repair
> as binary. We take the economics route instead. Given an LLM agent's own choices over budget sets,
> we compute the minimal perturbation restoring GARP-rationalizability as a single mixed-integer
> program, which yields a **graded, cardinal** dose (the Afriat efficiency index) where the ML
> literature has only binary cycle-counting, and we apply it *post hoc* to a frozen agent, so
> capacity, training and policy are identical across doses by construction. Scoring the repaired
> sequences against an exogenous payoff that no preference judgment enters, we trace the
> dose–response curve from the raw sequence to full rationalizability. This is the empirical
> counterpart to a theoretical proposal that has been circulating unrun: representation theorems
> have been argued to furnish label-free evaluation and regularization signals for AI systems, but
> that argument has never been tested on a model. Its author states plainly — in his abstract,
> twice in §1, and as his first limitation — that coherence is *not* sufficient for good behaviour,
> but that position is argued a priori and never measured, and he never asks whether *imposing*
> coherence helps or hurts. We supply that measurement, and report the Bronars power of every
> budget set beside every efficiency index we report.

**What that paragraph does, sentence by sentence:** concedes priority immediately (1); names the
gap as *identification*, not novelty (2); states the method and the two things that make the design
clean — cardinal dose and post-hoc application to a frozen agent (3); states the outcome measure and
that the endpoints are on the curve (4); lands the CFP's **"empirical evaluation of theoretical
models"** emphasis on the Andrews relationship explicitly (5); pre-empts the power objection (5).

**CFP targeting** (per `docs/VENUE.md`): primary bullet **"Preference aggregation for alignment and
its limitations"**; secondary **"Formal abstractions of AI rationality and bias in economic
contexts"** — the full bullet including the qualifier the brief truncated. Emphasis card played:
**Empirical evidence**, *not* Emerging domains.

---

## 5. Method, stated — Q3's resolution, not left implicit

The projection is a **single mixed-integer linear program**. It uses the multiplier-free ordinal
characterisation of GARP (R42, Demuynck & Rehbeck 2023), under which the constraints are linear
*jointly* in the perturbed quantities, the ordinal utility levels and the binary comparison
indicators. **No Afriat multipliers appear, so no bilinear term appears, and there is no outer
search over preference orderings.**

This matters because the obvious formulation does not work. Parameterised with Afriat multipliers,
the constraint `U_i ≤ U_j + λ_j·p_j·(x̃_i − x̃_j)` is bilinear once `x̃` is a decision variable, and
**fixing the preference ordering does not fix it** — `λ_j·p_j·x̃_i` remains a product of two unknowns
whatever the ordering is. The fix-ordering-then-alternate scheme the brief implies is therefore not
merely heuristic; as described it is not a well-defined step. Read charitably as alternating convex
search it reaches stationarity only, a partial optimum need not be a local optimum (R46), and with a
discrete ordering block cycling is possible without an anti-cycling rule. **Claim S8 is rewritten
accordingly** — it was understated for measurement (the Afriat system is already an LP with no
ordering fixed) and wrong for construction.

Three stated method commitments, each with its risk:

1. **Budget exhaustion imposed as an equality.** Standard for this design, it makes the big-M
   constant computable a priori, and it is simultaneously the fix for the Lemma-1 tie trap (§7).
2. **A fixed strict-preference margin γ > 0, reported, with the distance shown insensitive across
   two or three decades.** This is not a nicety. The GARP-consistent set is **not closed** (R43,
   Prop. 1), so the unregularised index can read exactly 0 on violating data and the minimum may be
   unattained. γ converts an unattained infimum into an attained minimum on a closed subset, and
   converts a silent failure into a reported parameter. **The paper computes the γ-margin
   projection and says so.**
3. **Every returned x̃ is verified by an independent combinatorial GARP check** (Warshall transitive
   closure), never trusted from solver status alone.

**Stated method risk, carried openly:** the complexity of the minimum-*perturbation* problem is
**open**. Adjacent results bracket it — Houtman–Maks is polynomial at K=2 and NP-complete at K≥3
(R45); the Dean–Martin minimum cost index is NP-hard (R44, via maximum acyclic subgraph) — but no
reduction has been verified for this objective and the paper will not assert one. Mitigation is
scope: K=2 with n ≤ 60, where E4 also puts Bronars power at ≈0.999, and where the deletion problem
is provably easy. **K, not n, is the binding constraint**, and the paper states a K bound.

Objective: **L1 by default** (a pure MILP, HiGHS-solvable, already measured in
`docs/COMPUTE_NOTE.md`), with weighted **L2** — the literature's LS index — as a robustness check
where an MIQP solver is available.

---

## 6. What kills this paper — updated for the six-occupant landscape

Andrews is no longer the central risk. He is now an *asset* (§4, sentence 5). The three dangerous
comparisons are these, in order.

### 6.1 R27 (TrustRoboReward / POISE, arXiv:2608.08491) — the vocabulary collision

**The attack.** "You claim a minimal projection onto a preference-consistent set. That was published
in August 2026, with a proof, and you did not cite it."

**Why it is dangerous.** It is precise, it is recent, it is correct on the words, and it takes about
thirty seconds for a reviewer to make.

**What the defence is NOT.** An earlier version of this section argued that POISE takes the ordering
as input while a GARP repair must *search over orderings*. **That argument is withdrawn.** It does not
survive contact with this project's own method note: the recommended formulation is a single MILP in
which the ordering is absorbed into `T(T−1)` binary comparison indicators, with no outer search and no
factorial enumeration (`docs/METHOD_NOTE_Q3.md`). The ordering search is a **solved encoding**, not an
open problem, and a reviewer who reads both documents would find them contradicting each other. Stated
that way the distinction is attackable as a distinction without a difference.

**The positioning, which must appear in the first two pages. The difference is in what can be
GUARANTEED, not in what is computed.** POISE projects cardinal scores onto a **convex** chain-monotone
cone. Projection onto a closed convex set is non-expansive in L2 — the projection of two points is
never further apart than the points themselves — and it is precisely that property which licenses
POISE's theorem that the edit lands **weakly closer to ground truth**. The GARP-consistent set is not
convex: it is a **union of polyhedra**, one per admissible preference ordering, and a union of convex
sets is not convex. **Projection onto such a union is not non-expansive, and no analogue of the
weakly-closer-to-truth theorem is available for it.** That is a structural difference in the strength
of claim the two operators can support, and it holds regardless of how efficiently either is computed.

Two supporting points, which reinforce the distinction but do not carry it:

- The continuous **quantity**-perturbation objective is unworked in the prior literature. The
  state-of-the-art integer-programming treatment of revealed-preference goodness-of-fit sketches it in
  two sentences, with no inequalities written down and no complexity classification, in contrast to the
  fully worked price-error case.
- Once bundles become decision variables rather than data, the revealed-preference relation is itself
  **endogenous** to the optimisation — the constraint set depends on the solution. POISE's cone is
  fixed by its input ordering and has no such feedback.

Cite POISE as the closest convex analogue, and as independent evidence that the **order-conditional,
convex** half of the problem is solved. The honest claim is that the non-convex half is not, and that
the guarantee does not transfer.

*Bonus, and it should be used:* POISE's own Table 2 contains a matched pair in which the isotonic
projection **alone lowers Overall quality by 0.50 while raising consistency by 2.27**, and its Table
3 shows the best-Overall configuration having *worse* consistency than the one it beats. Two
unremarked coherence/competence dissociations inside a paper whose thesis is that the projection
helps.

### 6.2 R25 (HRC/DSPPO, ICML 2026) — the published dose–response curve

**The attack.** "Appendix C.4, Table 5. Nine levels, inverted U, interior optimum. Your dose–response
is not new."

**Why it is dangerous.** It is peer-reviewed, at this venue's sibling conference, and it is a real
curve. Any sentence of the form *"we are the first to vary the degree rather than toggling on/off"*
is a desk-reject waiting to happen. **That sentence is banned from this paper.**

**The positioning.** Four differences, all load-bearing, none cosmetic: (i) their dose is a
training-time schedule weight on a component of a *learned third-party preference proxy*; ours is
applied post hoc to the *agent's own realised choices*, so capacity and training are identical
across doses **by construction** — the comparison they cannot make; (ii) λ carries no interpretation
as "how much incoherence was removed", a coherence-indexed dose does, and is comparable across
agents and model families; (iii) every outcome in both ICML papers is an LLM-judge win rate or
preference-agreement score — **no exogenous metric appears anywhere in either**; (iv) their curve
never reaches either endpoint, ours runs from the raw sequence to full rationalizability.
Cite both as **friendly precedent answering a different question about a different object** — not as
rivals. One of their authors may well be a reviewer.

### 6.3 R31 (Nitsch et al., *PNAS* 2022) — the human analogue that failed, and the reliability attack

**The attack, at full strength.** "You propose to grade an unreliable quantity, perturb it with an
operator class that has twice been published as failing, and read the payoff difference as a
treatment effect. Nitsch gave 97 people the chance to revise their own inconsistent budget-set
choices — the human analogue of your intervention — and CCEI went *down*. Not one of their ~40 ICC
estimates reaches 0.75, and presentation format alone drops agreement to 0.071."

**Why it is the most dangerous of the three.** It attacks the measure, not the novelty, and it is in
*PNAS*.

**The positioning, in three parts of decreasing strength — and the third is a concession.**

1. **Strong: Nitsch's revision arm is not a repair operator.** Participants saw a **random** subset
   of 10 of 40 choices — not the violating ones — were never told which were inconsistent, were
   given no consistency objective, and could change nothing. There is no guarantee the revised set
   has fewer violations, and none was attempted. It is an invitation to reconsider, not a
   projection. Our operator attains `CCEI → 1` **by construction**; it is not estimated. Likewise
   R38's isotonic arm projects onto the *calibration* cone while being scored on conditional
   independence — it repairs a different set than it is graded on.
2. **Medium: the reliability finding is a between-subject-variance problem, and its authors'
   prescribed remedy is our design.** They diagnose low ICC as low between-subject variance, not
   high measurement error (WSCV ~15% CCEI at ≥20 trials), and prescribe increasing individual
   differences "using a manipulation (i.e., a between-groups design)". ICC is a property of the
   population, not the instrument. Their humans cluster near ceiling; our conditions do not.
   **This must be measured on the actual models, not asserted** — which is why it is a pilot
   precondition (§7).
3. **Concession, stated plainly: there is no answer to the third-negative-in-a-row problem.** Three
   independent instances across three axiom systems point one way. That does not refute C1, but it
   converts the "clean negative" fallback from an interesting outcome into a fourth confirmation.
   The paper concedes this rather than pretending the prior is neutral.

### 6.4 Also required, lower risk

- **R41 (Cook, Kazinnik, Modig & Palmer, KC Fed / FEDS 2026-006)** — must be cited. Not on arXiv,
  economics vocabulary, and it already steers LLM economic choices with learned control vectors
  toward payoff-maximising behaviour: **two of our three legs**, without Afriat machinery, without a
  minimum-perturbation objective, without a traced frontier. Position as the closest economics-side
  neighbour and as independent corroboration that framing moves LLM economic behaviour more than
  personas do.
- **R6 ("Back to Blackwell")** — foil, not refutation (E6). But answer its one real edge: if
  intransitivity is multi-objective in origin, projecting onto a single acyclic order *is*
  scalarisation, which is their losing baseline. The answer is empirical — split our own cycles by
  source with a Condorcet-existence check alongside CCEI — and it must be in the paper.
- **R16 (Echenique 2021, on the CCEI's interpretation)** — cite it. A reviewer who knows this
  literature will ask why a projection targets a CCEI-derived object at all.

---

## 7. Preconditions before drafting (from `docs/GO_NOGO_ASSESSMENT.md`)

Frozen here because they bound what this framing is licensed to claim:

1. **CCEI test–retest on the target models**, fixed budget sets, fresh contexts, K≥5 re-runs, with
   ICC and WSCV reported. If per-model CCEI is as unstable as Nitsch's humans, **the dose axis does
   not exist** and the paper does not get written.
2. **Framing/format headroom on a current frontier model** — not persona (E2 cannot carry it; E3 and
   R41 both point at framing).
3. **Bronars power and predictive success beside every CCEI**, continuous-density prices with budget
   exhaustion so the Lemma-1 tie trap cannot fire (`docs/METHOD_NOTE_Q6.md`).
4. **A distance-matched null-operator control** — same displacement magnitude, no consistency gain.
   Neither published negative had one; both are open to the "we just moved the bundles" confound,
   and without it so are we.

---

## 8. Banned sentences

Literal strings that must not appear in the paper. Each is false or fatal.

- "Nobody repairs / corrects / projects revealed-preference consistency in LLM agents."
- "We are the first to vary the degree of coherence enforcement rather than toggling it on or off."
- "The coherence–competence question is open / untested."
- "Andrews declines to answer whether coherence is sufficient." *(He answers it, in the negative, in
  five places — E1.)*
- "Enforcing a total order is known to degrade downstream quality." *(Withdrawn — Item 2c.)*
- Any use of "minimal perturbation index" as **our** coinage. It is the LS index, and a second
  collision exists (R27).
