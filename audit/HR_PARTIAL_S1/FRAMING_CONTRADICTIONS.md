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

**Status: NOT patched into FRAMING.md.** This is a substantive correction to the locked positioning and
belongs to the principal investigator, not to this session. As written, §5.1 is attackable as a
distinction without a difference; recast on the guarantee, it is not.

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
