# Contradictions with the frozen framing, surfaced by the pipeline

`docs/FRAMING.md` was frozen at commit `a0fe78e` (sha256 `716dfc69…`) before Part Three ran, with a
standing instruction: if the pipeline surfaces something that contradicts it, **report the
contradiction rather than silently revising**. Three did. None has been edited into `FRAMING.md`.

---

## C-1 (CRITICAL) — FRAMING §5.1's defence against the vocabulary collision is stated on the wrong axis

**What FRAMING §5.1 says.** The defence against the isotonic-projection collision is that the published
operator projects onto a **convex** cone with the ordering held fixed as input, whereas a GARP repair
must **search over orderings** and the feasible set is a **non-convex union** over them.

**What the pipeline found.** The step-12 dialectic critic checked that sentence against this project's
own `docs/METHOD_NOTE_Q3.md` and found they contradict each other. The method note's recommended
formulation is *"a single MILP … no outer search over orderings"*, with the ordering search absorbed
into `T(T−1)` binary variables. So "they don't search over orderings and we must" is not a real
difference — the ordering search is a **solved encoding**, not an open problem.

**What actually survives, and it is a better argument.** The distinction should be drawn on the
**guarantee**, not the search:

1. Isotonic projection onto a convex cone that contains the truth is non-expansive in L2, which is what
   licenses that paper's "weakly closer to ground truth" theorem. **A union of polyhedra has no analogue
   of that theorem.**
2. The continuous quantity-perturbation objective is unworked — the state-of-the-art integer-programming
   treatment sketches it in two sentences with no inequalities and no complexity classification.
3. Once bundles become decision variables, the revealed-preference relation itself becomes endogenous.

**Status: RESOLVED 2026-08-22 — patched into FRAMING.md §5.1 by explicit instruction from the principal
investigator.** The ordering-search argument is withdrawn in the text rather than quietly dropped, and the
defence is restated on the non-expansiveness guarantee. The two secondary points are carried as supporting
rather than load-bearing. Post-amendment sha256 of `docs/FRAMING.md`: `a6a5468a1860d79d5625c5b8aee5c45f5a79c41b6104d6d68be1b5ec664824b3`.

---

## C-2 (MAJOR) — FRAMING §6 precondition 2 may be unsatisfiable where it is needed

**What FRAMING §6 says.** Precondition 2 requires "framing/format headroom on a current frontier model",
having switched the headroom lever from persona to framing on the strength of kill-check E3.

**What the pipeline found.** The step-8 gap-fill fetched the first per-model reliability study on
language models rather than humans: across 100 independent runs per model on a fixed budget-set task,
**administration-format changes move the efficiency index a long way in small models (0.980→0.739 and
0.953→0.841, both p<0.01) but leave the two flagship models essentially unmoved.** Persona and
temperature move none of the four. A central-bank working paper corroborates the direction: larger
models are rationalizable far more often, and the smallest tested is "not rationalizable at all".

**Why this cuts both ways.** It *resolves* the reliability worry in the project's favour for flagship
models — their index is format-stable, so a dose axis can exist for them. But it simultaneously suggests
the framing lever produces headroom mainly in the models the project is least interested in.

**Status: NOT patched.** Recorded in `research/temp/corpus-critic-results.md` and here. It is one
unreplicated study and should not be over-read in either direction — but precondition 2 should be
re-examined before the pilot is designed.

---

## C-3 (MAJOR) — an orchestrator instruction of mine caused a real content defect

Not a contradiction with FRAMING, but an error of mine that the critics caught and that belongs in the
same record.

I instructed every drafter and the synthesizer: *"do not name any AI vendor or model family in the
prose."* That was over-broad. The hygiene guard greps only for the vendor/assistant names, the ORCID,
the school email and the machine path — model families are **not** guard patterns and are safe to name.

**Cost:** the report names zero models anywhere, so the decomposition's `LLM-based agents` entity has its
one required field ("which models studied") unfilled, and §7F's scale-dependence argument has no tier
labels to hang on, which makes it close to unfalsifiable as written. One drafter also altered a verbatim
bibliographic title unnecessarily for the same reason.

**Status: handed to the step-14 patcher as an explicit instruction to restore model identities.**

---

## C-4 (MAJOR) — an exogenous-payoff test of coherence enforcement exists, and it is non-monotonic

**What FRAMING says.** C1 and the §5.2 positioning rest on the claim that no existing work scores a
coherence intervention against "a payoff that is not derived from any preference judgment", and that the
dose–response shape is unclaimed on that axis.

**What the step-13 gap-fill found.** `arXiv:2406.01168` ("AI as Decision-Maker: Ethics and Risk
Preferences of LLMs") fine-tunes on alignment data, causally shifts the model's risk preferences, and
then evaluates the result against **actual future capital expenditure** drawn from a financial-statement
database — genuine ground truth, not a judge score and not derived from anyone's preferences. The
reported relationship is **non-monotonic**: single-dimension alignment *improves* predictive power
(coefficient 0.5346, p<0.01, against a base of 0.0607) while full three-dimension alignment *destroys*
it (0.2969, not significant).

**Why this matters more than the other occupants.** It holds two of the four conjuncts simultaneously —
an exogenous payoff *and* a coarse dose (one alignment dimension versus three) — where every previously
catalogued system held at most one. It also reports the interior-optimum shape the project expected to
discover.

**What still survives.** It is not a revealed-preference intervention: no GARP, no efficiency index, no
minimal-perturbation objective, and the manipulation is training-time fine-tuning rather than projection
of an observed choice sequence. The dose has two levels, not a curve.

**Status: NOT patched into FRAMING.md.** But the sentence in §5.2 asserting that an exogenous payoff is
"the single cleanest unoccupied axis" is now too strong, and the principal investigator should see this
paper before that framing is submitted anywhere.
