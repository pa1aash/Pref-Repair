# Go / No-Go — is the narrow surviving cell sufficient for a NeurIPS EconML workshop paper?

Written 2026-08-21, session G0.5, after G0's six kill-checks and G0.5's items 1–4.
The deadline is **Aug 29 2026 AoE — eight days out**. The venue is locked by standing instruction.

This document does not decide. It states the strongest case each way at full strength, then gives
a recommendation and names exactly what the recommendation is conditional on.

---

## What is actually left, restated precisely

G0 defined the surviving cell as a conjunction. G0.5 tested each conjunct against papers read in
full. Current status:

| Conjunct | Occupied? | By what, and how close |
|---|---|---|
| **1. The object is the agent's own choice sequence** | **OPEN** | R20 repairs an LLM's pairwise *judgments about third-party passages*; R27 cleans a *teacher's training-corpus labels*; R24/R25 vary the functional form of a *learned third-party preference proxy*. None touches an agent's own budget-set demand data. |
| **2. Minimal perturbation, formally** | **CLOSED as vocabulary, OPEN as object** | R27 (Aug 2026) owns "isotonic projection onto a preference-defined monotone cone" with a proof. But it takes the ordering as **input** and cannot handle cycles at all. The GARP-consistent set is a non-convex union over orderings; R27's cone is convex. Different mathematical object, same words. |
| **3. Scored against an exogenous payoff** | **PARTIALLY OCCUPIED** | R20 scores against TREC human relevance labels — a genuine exogenous metric, on the wrong object. R41 (KC Fed) scores against **payoff-maximizing behaviour**, on the right kind of object, without any GARP machinery. So "nobody scores repair against something outside the preference data" is **false as stated**. |
| **4. Dose–response rather than on/off** | **OCCUPIED on an adjacent axis** | R25 App. C.4 Table 5 is a **published nine-level dose–response curve** with an interior optimum, in a peer-reviewed ICML paper. The dose is a training-time schedule weight on a component of a learned preference proxy, not a quantity of incoherence removed — but the *sentence* "we are first to vary the degree rather than toggling on/off" is dead. |

**The conjunction is untouched.** No paper holds two of these jointly. But three of the four
individually are now spoken for, and the fourth is spoken for in vocabulary.

---

## The strongest case for YES

**1. The conjunction is genuinely unoccupied, and it is unoccupied for a structural reason, not by
accident.** Every existing repair operates on a *preference proxy* — a judge's rankings, an
annotator pool, a reward head. The reason is that those are the objects ML has data for. Applying
the operator to an agent's **own realised choices**, post hoc, on a fixed black box, is the one
configuration in which capacity, training and the policy are **identical across doses by
construction**. R24 and R25 cannot do that experiment: their cycle-tolerant arm is a strict
superset model class, so their comparisons confound coherence with capacity — G0.5 verified this
from their own appendices, and the confound is worth more than their headline margins. A clean
identification of the coherence effect is therefore not available anywhere in the literature, and
this design is the way to get it. That is a real contribution and it is defensible in one sentence.

**2. The method question is solved, and better than expected.** Q3 went in as the project's largest
technical unknown and came out with a clean formulation: Demuynck & Rehbeck's multiplier-free
ordinal characterisation makes the constraints linear jointly in perturbed quantities, ordinal
levels and binary indicators — **a single MILP, no Afriat multipliers, no bilinear terms, no outer
search over orderings**. HiGHS solves it on the machine already measured. The known hazard
(the GARP-consistent set is not closed, so the minimum can be unattained) has a stated fix: a fixed
strict-preference margin γ, reported and shown insensitive across decades. This is a method section
that can be written in a day and defended.

**3. The venue fit is good and the empirical-evidence card is strong.** Two CFP bullets are direct
hits. The "empirical evaluation of theoretical models" emphasis describes the relationship to
Andrews (R4) exactly — 25 pages of theory, zero experiments, six months in circulation in this
community. References, appendices and the checklist sit **outside** the 9-page limit, so the MILP
formalism and the power analysis do not compete with the argument for space.

**4. The negative-result literature has a hole in exactly the right place.** Four published repair
results — Nitsch's choice-revision (worse), Yamin's isotonic calibration (worse), TrustJudge and
CONSISTRE (better) — are all **binary**. They are four points on a curve nobody has drawn. "Where
does repair stop helping and start hurting, as a function of how much you repair?" is a sharper
question than the plan's original one, and it is asked by nobody.

**5. The instrument work is done and is itself defensible.** Bronars power at the design point is
0.999 with a documented recipe; the false-CCEI-1.0 trap is characterised with a verified minimal
test case; the reporting rule (power and predictive success beside every CCEI) is written down.
Most workshop submissions in this space do not have this.

---

## The strongest case for NO

**1. Three of the four conjuncts fell in a single day of checking, and the checking is not
finished.** G0 believed the cell had four clean walls. G0.5 read six papers and found: minimality
owned in vocabulary since August 2026 (R27), the exogenous-payoff claim false as stated (R20, R41),
and a published dose–response curve (R25). The trend line is bad. RePEc alone — searched for the
first time this session, after being wrongly written off — produced a Fed working paper (R41) with
**two of the three legs**, invisible to every arXiv sweep. The residual gaps in that search are
explicitly top-k truncation on broad queries and **metadata-not-full-text indexing**, which is the
exact blind spot that hid Chadwick et al. from the original sweep. There is no reason to believe
the seventh occupant does not exist; there is only an absence of a route that would find it.

**2. The adverse empirical prior is now substantial, and it is against C1's mechanism
specifically.** Nitsch et al. (*PNAS*, 1,600+ subjects) let people revise their own inconsistent
budget-set choices — **the human analogue of this exact intervention** — and CCEI went *down*.
Yamin's isotonic calibration made its target worse in 14 of 16 cells. Zhu/Griffiths improved
coherence and lost held-out accuracy. Three axiom systems, one direction. C1 is no longer a
neutral hypothesis; it is a hypothesis with published evidence against it.

**3. The measurement instrument may not support the claim.** Nitsch reports that **not one of ~40
ICC estimates reaches 0.75**, and — the part that actually bites — *intermethod* reliability (same
session, different presentation format: 0.071–0.408) is **worse** than five-month test–retest
(0.511/0.526). Format dominates time. Format is also precisely the lever Q2 identifies as the
source of CCEI headroom. **Headroom and construct invalidity are the same variable.** If CCEI moves
0.3 when you reword the prices, a paper that reports a projection effect of similar magnitude has
to explain why its effect is signal and the reframing effect is noise. There is no clean answer to
that in eight days.

**4. The risk asymmetry — the plan's stated reason for choosing this project — is gone twice over.**
It was "either direction is publishable". A negative is now the fourth negative in a literature with
three: a replication, not a result. A positive matches TrustJudge and CONSISTRE. And G0.5 removed
the third option too: E5 had claimed "enforcement degrades" was the established ICML consensus,
which would at least have made a positive surprising — G0.5 found that claim rests on
length-uncorrected numbers in the most length-inflated cell of the paper, and that the properly
controlled replication finds a **wash**. There is no longer a result this project can get that
surprises a reader who knows the area.

**5. Eight days, and the pilot is genuinely gating.** No model call has been made. C4's headroom
evidence cannot carry the gate (E2: one retired 2024 model, no CIs, a headline value below its own
design's arithmetic floor). The real headroom evidence is E3's framing manipulation — which is also
finding (3) above, i.e. the thing that undermines the measure. The honest schedule is: pilot,
*then* decide, and the pilot has not run.

**6. The paper must now concede in its first two pages that the operator is not new, the words are
not new, and the dose–response shape is not new.** What remains is "same idea, applied to a
different object, measured better". That is a legitimate workshop contribution. It is also a thin
one to build a first submission around, against a reviewer pool that — per E1 — has had Andrews
circulating for six months.

---

## Recommendation

**QUALIFIED YES — proceed to a reframe and a pilot, with a hard stop.**

The narrow cell is real, the method is solved, and the venue fits. That is enough to justify the
next step. It is *not* enough to justify writing a paper on the current evidence, and the
difference matters.

Concretely: **do not write the paper yet. Run the pilot, restated, and let it decide.** The pilot
is one afternoon and a few dollars, it is the thing the original plan already designated a hard
gate, and every finding in G0.5 says the gate is currently unsecured rather than passed.

The pilot must be restated in three ways, all of which follow from findings above and none of which
costs extra:

1. **Vary framing and response format, not persona.** E3's manipulation is trivial, holds budget
   sets fixed, and has published effect sizes on the exact instrument. R41 independently corroborates
   that reframing moves LLM economic behaviour and personas move it less.
2. **Measure test–retest reliability of CCEI on the models under study, on fixed budget sets with
   fresh contexts, before interpreting anything.** This is now a precondition, not a robustness
   check. If the models' own CCEI is as unreliable as humans', the dose axis does not exist and the
   project stops there — cleanly, cheaply, and before any writing.
3. **Report Bronars power and predictive success beside every CCEI**, and use continuous-density
   prices with budget exhaustion so the Lemma-1 tie trap cannot fire. Both are free and both are
   already specified in this repository.

### What the recommendation is conditional on, and who resolves it

| Condition | Resolved by | When |
|---|---|---|
| CCEI test–retest on the actual models is high enough that a dose axis exists | the pilot | before any writing |
| Framing/format conditioning produces CCEI headroom on a 2026 frontier model | the pilot | same run |
| The PI accepts a contribution framed as *object + measure + rigour*, not as priority | **the PI — nobody else can** | now |
| No seventh occupant is found in the residual gaps (full-text working papers, SSRN, EconStor) | further search, or accepted as residual risk | before submission |

### The one thing that would flip this to NO

**If the pilot shows CCEI test–retest reliability on the target models is as poor as Nitsch reports
for humans.** In that case the dose variable is noise, the projection is repairing sampling
variation, and no amount of reframing rescues it. That is a measurable, cheap, pre-writing check,
and it should be run first.

### The one thing that would flip this to an unqualified YES

**A pilot showing (a) stable per-model CCEI across re-runs, and (b) a framing-induced CCEI drop on
a current frontier model.** With those two numbers in hand the paper writes itself against a clean
identification argument that no existing paper can make, and the eight days are enough.

---

## Explicit answer to the gate

**Verdict: QUALIFIED YES.** The narrow cell is sufficient for a NeurIPS EconML workshop paper
**if and only if** it is reframed as *object + graded measure + exogenous outcome + rigour* rather
than as priority, and **if and only if** the pilot secures the two numbers above first. Proceeding
to positioning (S1) is warranted. Proceeding to a draft is not, until the pilot runs.
