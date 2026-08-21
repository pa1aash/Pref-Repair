# F3 — Repairing, Not Just Measuring, LLM Preference Inconsistency

**One sentence:** Everyone measures whether LLM agents violate revealed-preference axioms; nobody
*fixes* it — propose minimal-perturbation projection onto the GARP-consistent set as an inference-time
layer, and answer the question the measurement literature leaves open: does enforced coherence make an
agent a **better** decision-maker, or merely a more consistent one?

| | |
|---|---|
| **Target venue** | NeurIPS 2026 **EconML** (Atlanta) — lands on the named CFP bullet "formal abstractions of AI rationality and bias" |
| **Deadline / format** | **Aug 29 2026 AoE**, long 9pp / short 4pp *content* pages (figures+tables count), double-blind, non-archival, in-person attendance required |
| **Backup venue** | Any NeurIPS 2026 agent-evaluation workshop; ICLR behavioural-ML venues |
| **Prior-art verdict** | **NARROW** — measuring is saturated; repairing is unclaimed. Two caveats below are serious. |
| **Compute** | CPU-trivial. LP/MILP over ~25–50 observations runs in milliseconds. |
| **Data** | **Generated, not collected** — budget sets are synthetic. Needs LLM API calls (~$20–150). |
| **Est. effort** | 2–3 weeks, **gated on a week-1 pilot** |

---

## The gap

Economic rationality of LLMs is a well-populated measurement literature. Chen, Liu, Shan & Zhong
(*PNAS* 2023) put GPT-3.5 at CCEI 0.997–0.999 on budget-allocation tasks — more rational than humans.
Later work shows the cracks: persona/role prompting ("act as a biotech expert") **substantially
degrades** GARP compliance (arXiv:2501.18190), and revealed-preference models fitted to LLM medical
decisions find prompt-steering **fails** (arXiv:2605.08556).

Two exhaustive arXiv full-text sweeps (`"revealed preference" AND "language model"`, 18 hits 2021–2026;
`GARP OR Afriat`, 33 hits all-time) returned **zero papers that correct, project, repair, or enforce**
revealed-preference consistency on an LLM's choices. The field measures; it does not intervene.

## Primary claim (C1)

An inference-time projection layer that maps an agent's choice sequence to the nearest GARP-consistent
set — the constructive counterpart of the CCEI index — restores rationalizability at bounded utility
cost, and its effect on an **independent** decision-quality metric is measurable and non-trivial.
Direction is deliberately not pre-committed: see C2.

## Secondary claim (C2) — what makes it a full paper

**The coherence-vs-competence dissociation.** Andrews (arXiv:2608.05015, 5 Aug 2026) proposes
`1 − CCEI` as a training penalty *in theory* and explicitly declines to answer whether coherence is
sufficient for good behaviour. Answer it empirically: does forcing rationalizability improve, leave
unchanged, or **degrade** downstream decision quality? A clean negative — "coherence is orthogonal to
competence, so rationality metrics are not alignment targets" — is a *publishable and more interesting*
workshop result than a win. That asymmetry is what makes this the safest bet in the batch.

## Method

1. **Elicit choices.** Generate synthetic budget sets (prices p_t, income m_t); ask the agent to choose
   a bundle x_t. 25–50 observations per condition. Conditions: baseline, persona-conditioned,
   framing-varied, multi-step agentic.
2. **Measure.** Compute CCEI (Afriat efficiency index) via binary search over e ∈ (0,1] with a
   transitive-closure/cycle check on the revealed-preference relation; also Houtman–Maks and the
   money-pump index.
3. **Project.** Find the minimal-perturbation bundle sequence {x̃_t} that satisfies GARP. Given a fixed
   preference ordering, feasibility is a system of **Afriat inequalities** — a linear program. Wrap in a
   MILP or a search over orderings. **Keep n ≤ 60**; the ordering search blows up beyond that.
4. **Evaluate downstream.** Apply the projection as an inference-time layer on a decision task with an
   *independent* quality metric (portfolio/resource-allocation payoff, or task success), and compare
   projected vs raw agent.

## Experimental protocol

- **Models:** ≥3 frontier models across ≥2 families, so the finding is not one model's quirk.
- **Baselines (must include the trivial one):** (i) **raw agent, no projection** — the degenerate
  baseline; (ii) random perturbation of equal magnitude (controls for "any perturbation helps");
  (iii) prompt-based "be consistent" instruction (the cheap alternative a reviewer will demand).
- **Metric/estimand:** CCEI before/after; downstream payoff before/after; utility cost of projection
  measured as ||x̃ − x||.
- **Statistics:** ≥5 seeds per condition; paired bootstrap CIs on the before/after difference; report
  per-seed distributions.

## S4 preflight — run BEFORE any compute (this is a HARD GATE)

1. **Degenerate floor:** if CCEI ≈ 1.0 there is nothing to project and the projection is the identity.
2. **MDE — THE GATE:** **measure CCEI on frontier models under persona/framing conditioning in week 1.**
   Chen et al. found 0.997+ at baseline; arXiv:2501.18190 is the evidence that headroom exists under
   specialization. **If CCEI > 0.99 even when role-prompted, this project is dead — stop and do not
   write code.**
3. **Leakage:** budget sets must be generated fresh, not drawn from any published instrument the models
   may have memorised.
4. **STOP condition:** no headroom → stop. Do not proceed to the projection implementation on hope.

## What kills this paper

**"You reinvented CCEI."** This is the sharpest attack and it is fair. CCEI *is defined as* the minimal
budget perturbation restoring GARP; Houtman–Maks *is defined as* the minimal deletion set. Projection is
their constructive dual, known to economists since Afriat (1973) / Varian (1990). **The novelty cannot
be the projection operator.** It must be the *intervention* and what it reveals about decision quality.
State this in the paper before a reviewer does.

**Andrews scooped the framing 12 days before the deadline.** arXiv:2608.05015 already claims "use Afriat
representation theorems to regularize AI," including `1 − CCEI` as a penalty — theory only, no
experiments. Your mechanism differs (inference-time projection vs training-time gradient penalty) and he
runs nothing. **Cite him prominently and position as the empirical complement, not the originator.** He
will plausibly submit to this same workshop.

**Demote the "consistency predicts quality" angle** — arXiv:2602.11619 (ICML 2026 workshop) already
reports consistency-as-uncertainty-signal (82–87% accuracy on consistent vs 41–65% on inconsistent
tasks). Different consistency measure, so a GARP version is defensible, but it is no longer fresh.

## Prior art you must cite

Afriat (1973) efficiency index; Houtman & Maks (1985); Varian (1990) goodness-of-fit; Samuelson (1938)
revealed preference; Echenique, Lee & Shum money-pump index; **Chen, Liu, Shan & Zhong, *PNAS* 120(51)
2023** (arXiv:2305.12763); arXiv:2501.18190 (rationality under specialization); Yamin et al.
arXiv:2605.08556; **Andrews, arXiv:2608.05015**; Aguiar & Kashaev, GARP-EFM arXiv:2603.23993;
Zhang, Swamy, Wu et al., "Back to Blackwell" arXiv:2602.19041 (the opposite stance — *accept* cycles
rather than project them; engage with it directly).

## Day-1 starting point

Write `ccei.py`: generate budget sets, query one model under baseline vs persona conditioning, compute
CCEI. That is the entire S4 gate and it costs a few dollars and an afternoon. **Do not write the
projection LP until that number shows headroom.**
