# CLAIMS — every assertion in the F3 planning brief, extracted and classified

Source: `docs/F3-PLAN-ORIGINAL.md` (sha256 `50b33f7b4d0586c9d686995500d45baaa5f767afec982f2cecc13b74f3b34eef`, immutable).
Extracted 2026-08-21, session G0. Nothing here is verified yet; verification is Phases C–F.

**Classification key**

| Class | Meaning |
|---|---|
| **load-bearing** | If false, the paper as scoped cannot be written. Prefix `C`. |
| **supporting** | If false, the paper survives but a specific section must be rewritten or a number replaced. Prefix `S`. |
| **decorative** | Framing, strategy, or colour. If false, delete a sentence. Prefix `D`. |

The **Kill-check** column is filled in during Phase E. `—` means no kill-check bears on it this session.

---

## Load-bearing claims

### C1 — The projection intervention works and its downstream effect is measurable

> "An inference-time projection layer that maps an agent's choice sequence to the nearest
> GARP-consistent set — the constructive counterpart of the CCEI index — restores
> rationalizability at bounded utility cost, and its effect on an **independent**
> decision-quality metric is measurable and non-trivial."
> (plan MD, "Primary claim (C1)")

C1 is a conjunction of three separable sub-claims, and they die differently:

- **C1a (feasibility):** a minimal-perturbation projection onto the GARP-consistent set exists
  and is computable at the stated scale.
- **C1b (bounded cost):** the perturbation ‖x̃ − x‖ required is small enough that the projected
  bundle sequence is still a plausible agent output rather than a different agent.
- **C1c (measurable downstream effect):** the projection's effect on an independent quality
  metric is non-trivial — i.e. distinguishable from zero and from the random-perturbation control.

**Kills it:** For C1a — a proof or demonstration that the minimal-perturbation problem is
intractable or ill-posed at n = 25–60 (it is not: see `docs/COMPUTE_NOTE.md`). For C1b — pilot
data showing the projection has to move bundles so far that the projected agent is
unrecognisable. For C1c — a pilot in which projected and raw agents are statistically
indistinguishable on the quality metric *and* the random-perturbation control is also
indistinguishable, leaving no signal of any kind. Note that C1c failing in the *direction* of
"projection hurts" does **not** kill the paper — see C2.

**Kill-check:** E6 (does "Back to Blackwell" argue the intervention is wrong in principle?)

### C2 — The coherence-vs-competence question is open and this project can answer it

> "does forcing rationalizability improve, leave unchanged, or **degrade** downstream decision
> quality? A clean negative — 'coherence is orthogonal to competence, so rationality metrics
> are not alignment targets' — is a *publishable and more interesting* workshop result than a
> win." (plan MD, "Secondary claim (C2)")

This is the claim that converts C1 from a methods note into a paper, and it carries the plan's
risk asymmetry: it asserts that *both* directions of result are publishable, so the project
cannot fail by getting the "wrong" answer.

**Kills it:** Someone has already answered it. Specifically: published work that empirically
tests whether enforced choice-coherence improves or degrades downstream task performance in
LLM agents, in either direction. Adjacent-literature answers count — if the ML/alignment
coherence literature has already established the dissociation, the econ framing is a
restatement, not a finding.

**Kill-check:** E5 (occupancy check against the ML/alignment coherence literature), E1 (does
Andrews already run this experiment?)

### C3 — Nobody has built the intervention (the novelty claim)

> "Two exhaustive arXiv full-text sweeps (`"revealed preference" AND "language model"`, 18 hits
> 2021–2026; `GARP OR Afriat`, 33 hits all-time) returned **zero papers that correct, project,
> repair, or enforce** revealed-preference consistency on an LLM's choices. The field measures;
> it does not intervene." (plan MD, "The gap")

The entire "NARROW but unclaimed" prior-art verdict rests on this. It is also the claim most
likely to be an artefact of the instrument rather than of the literature: a full-text search
that silently returns zero because it was mis-parsed looks identical to a genuinely empty field.

**Kills it:** Any published or preprinted paper that corrects / projects / repairs / enforces
revealed-preference consistency on the choices of an LLM or AI agent. Also killed *as stated*
(though not as a research direction) if the sweep that produced the zero is shown to be
uncalibrated — a zero from a broken instrument is not evidence of absence.

**Kill-check:** Phase C (instrument calibration + re-run), Phase D (independent sweep), E1, E5

### C4 — There is CCEI headroom to project away

> "**MDE — THE GATE:** measure CCEI on frontier models under persona/framing conditioning in
> week 1. … **If CCEI > 0.99 even when role-prompted, this project is dead — stop and do not
> write code.**" (plan MD, "S4 preflight")

The plan itself designates this a hard gate. If frontier models are near-perfectly GARP-consistent
under every condition, the projection is the identity map and there is nothing to study.

**Kills it:** A week-1 pilot measuring CCEI > 0.99 under persona and framing conditioning across
the model set. Kills it *in advance* if the literature already reports that the persona effect
on CCEI is negligible.

**Kill-check:** E2 (the actual effect size in arXiv:2501.18190), E3 (is the PNAS 0.997–0.999
figure a ceiling artefact?), E4 (is a high CCEI even informative at this n?)

### C5 — The venue is reachable as scoped

> "Target venue: NeurIPS 2026 **EconML** (Atlanta) — lands on the named CFP bullet 'formal
> abstractions of AI rationality and bias'. Deadline / format: **Aug 29 2026 AoE**, long 9pp /
> short 4pp *content* pages (figures+tables count), double-blind, non-archival, in-person
> attendance required." (plan MD, header table)

Load-bearing because the venue is locked by standing instruction and the deadline is eight days
from this session. If the CFP bullet does not exist, the page limit is different, or the deadline
has moved, the scope of the work changes immediately.

**Kills it:** The live CFP contradicting any of: the bullet's existence, the deadline, the page
limit, or the double-blind requirement.

**Kill-check:** Phase F (venue lock against the live CFP)

---

## Supporting claims

### S1 — Chen, Liu, Shan & Zhong (PNAS 2023) put GPT-3.5 at CCEI 0.997–0.999
> "Chen, Liu, Shan & Zhong (*PNAS* 2023) put GPT-3.5 at CCEI 0.997–0.999 on budget-allocation
> tasks — more rational than humans."

**Class:** supporting. It establishes the baseline ceiling that motivates the search for headroom.
**Kills it:** The paper reporting a different figure, a different model, or the figure being
conditional on a design choice the plan does not inherit.
**Kill-check:** E3

### S2 — Persona/role prompting substantially degrades GARP compliance
> "persona/role prompting ('act as a biotech expert') **substantially degrades** GARP compliance
> (arXiv:2501.18190)"

**Class:** supporting *in wording*, load-bearing *in substance* — it is the sole cited evidence
that C4's headroom exists. Classified supporting only because C4 already carries the load.
**Kills it:** The paper's actual effect size being small, or measured on something other than
CCEI/GARP, or not on frontier models.
**Kill-check:** E2

### S3 — Prompt-steering of LLM medical decisions fails under a revealed-preference model
> "revealed-preference models fitted to LLM medical decisions find prompt-steering **fails**
> (arXiv:2605.08556)"

**Class:** supporting. Corroborates that stated instructions do not reliably control revealed choice
— which is the argument for an output-side intervention over a prompt-side one.
**Kills it:** The paper actually finding prompt-steering succeeds, or not using a revealed-preference model.
**Kill-check:** —

### S4 — Andrews proposes `1 − CCEI` as a training penalty, theory only, no experiments
> "Andrews (arXiv:2608.05015, 5 Aug 2026) proposes `1 − CCEI` as a training penalty *in theory*
> and explicitly declines to answer whether coherence is sufficient for good behaviour."

**Class:** supporting, and it is the plan's single largest scoop risk. The paper's positioning
("empirical complement, not originator") is built on Andrews running nothing.
**Kills it:** Andrews containing experiments, or proposing an inference-time mechanism.
**Kill-check:** E1

### S5 — "Back to Blackwell" takes the opposite stance: accept cycles rather than project them
> "Zhang, Swamy, Wu et al., 'Back to Blackwell' arXiv:2602.19041 (the opposite stance — *accept*
> cycles rather than project them; engage with it directly)."

**Class:** supporting. Determines whether the related-work section needs a foil or a defence.
**Kills it:** The paper arguing that enforcing acyclicity is actively harmful *and* supporting it
with evidence — which would make it a refutation of C1 rather than a contrast.
**Kill-check:** E6

### S6 — The consistency-predicts-quality angle is already taken
> "arXiv:2602.11619 (ICML 2026 workshop) already reports consistency-as-uncertainty-signal
> (82–87% accuracy on consistent vs 41–65% on inconsistent tasks)."

**Class:** supporting. Drives the instruction to demote one framing.
**Kills it:** The numbers or the venue being wrong, or the consistency measure being close enough
to GARP that the angle is fully occupied rather than merely adjacent.
**Kill-check:** E5 (partially — occupancy of the coherence↔quality link)

### S7 — Projection is the constructive dual of CCEI and Houtman–Maks, known since Afriat/Varian
> "CCEI *is defined as* the minimal budget perturbation restoring GARP; Houtman–Maks *is defined
> as* the minimal deletion set. Projection is their constructive dual, known to economists since
> Afriat (1973) / Varian (1990). **The novelty cannot be the projection operator.**"

**Class:** supporting, and unusually: this is a claim the plan makes *against itself*, pre-empting
the sharpest reviewer attack. It is almost certainly true and should be stated in the paper.
**Kills it:** Nothing — but if it turned out projection is *not* a known dual, that would be a
finding in the project's favour.
**Kill-check:** —

### S8 — Given a fixed preference ordering, feasibility is a linear program
> "Given a fixed preference ordering, feasibility is a system of **Afriat inequalities** — a
> linear program. Wrap in a MILP or a search over orderings."

**Class:** supporting (method correctness).
**Kills it:** The Afriat inequalities not being linear in the decision variables under the plan's
parameterisation — a real risk if the utility levels and marginal utilities are both free, which
makes the system bilinear.  **This is an open question, not a settled one — see `docs/OPEN_QUESTIONS.md` Q3.**
**Kill-check:** —

### S9 — n ≤ 60; the ordering search blows up beyond that
> "**Keep n ≤ 60**; the ordering search blows up beyond that."

**Class:** supporting (scope constraint). Consistent with a factorial ordering search.
**Kills it:** Nothing this session; it is a self-imposed bound.
**Kill-check:** E4 (n interacts with test power — a small n bound has an evidentiary cost)

### S10 — Compute is CPU-trivial; LP/MILP over 25–50 observations runs in milliseconds
**Class:** supporting. Confirmed independently this session.
**Kills it:** Nothing — verified. See `docs/COMPUTE_NOTE.md`.
**Kill-check:** —

### S11 — Cost is ~$20–150 in API calls; effort is 2–3 weeks
**Class:** supporting (feasibility). Untested; depends on model choice and the ≥5-seeds requirement.
**Kills it:** The seed requirement forcing a model choice whose cost is an order of magnitude higher.
**Kill-check:** —

### S12 — Budget sets must be generated fresh to avoid memorisation leakage
**Class:** supporting (validity control). Standard and correct.
**Kill-check:** —

### S13 — The experimental protocol as specified (≥3 models / ≥2 families, 3 baselines, ≥5 seeds, paired bootstrap)
**Class:** supporting (design adequacy). The three named baselines — raw agent, equal-magnitude
random perturbation, and prompt-based "be consistent" — are the right three.
**Kills it:** Nothing structural. The ≥5-seeds requirement does interact with API determinism —
see `docs/COMPUTE_NOTE.md`.
**Kill-check:** —

---

## Decorative claims

| ID | Claim | Why decorative |
|---|---|---|
| **D1** | "the safest bet in the batch" | Comparative judgement against a batch not described here. Nothing depends on it. |
| **D2** | Venue is in Atlanta | Logistics. Matters for travel, not for the paper. |
| **D3** | "Backup venue: any NeurIPS 2026 agent-evaluation workshop; ICLR behavioural-ML venues" | Venue is locked by standing instruction; the backup list is inert. |
| **D4** | "He will plausibly submit to this same workshop." | Speculation about a third party's behaviour. Unknowable, and changes nothing about what to write. |
| **D5** | GPT-3.5 is "more rational than humans" | Rhetorical framing of S1. The comparison to humans is not used anywhere in the method. |
| **D6** | "Data: generated, not collected" | Restates the method. |
| **D7** | "Day-1 starting point: write `ccei.py`" | Work instruction, not an assertion about the world. |
| **D8** | "This is the sharpest attack and it is fair" | Editorial assessment of S7. |
| **D9** | "2–3 weeks, gated on a week-1 pilot" | Overlaps S11; the gating structure is real, the duration is a guess. |

---

## Kill-check summary

All six kill-checks completed. One line each, against the claims they bear on.

| Check | Bears on | One-line finding |
|---|---|---|
| **E1** | S4, C2, C3 | Andrews arXiv:2608.05015 is 25 pp of pure theory — 0 figures, 0 experiments, no inference-time mechanism, so **S4's load-bearing content is verified**. But he does *not* "decline" the sufficiency question: he answers it *no*, by assertion, in five places. |
| **E2** | S2, C4 | arXiv:2501.18190 reports CCEI 0.916 basic → 0.127 biotech / 0.298 economist. Huge on its face, but one retired 2024 single-family model, zero CIs or replications, and 0.127 sits **below its own budget grid's arithmetic floor of 0.25**. Sign survives; magnitude is unusable. **HEADROOM MARGINAL.** |
| **E3** | S1, C4 | The PNAS figure is confirmed to the digit (0.998 / 0.997 / 0.997 / 0.999, GPT-3.5-Turbo, T=0) and is **not** a low-power artefact — budget lines cross 58% of the time, Bronars power 99.9%. Crucially it is **baseline-only**: reframing the *same* budget sets drops CCEI to 0.698–0.908. |
| **E4** | C4, S9 | At K=2 goods and n=25–50 the design has Bronars power ≈0.999 (random agent scores CCEI ≈0.72), so the test genuinely can fail. But power **collapses exponentially in the number of goods** and n cannot buy it back. Every CCEI must ship with its power. |
| **E5** | **C2**, S6 | **C2 PARTIALLY OCCUPIED, and the occupied part is the larger part.** ICML'25 and ICML'26 papers already run the enforce-a-total-order vs accept-cycles ablation on LLMs and find enforcement *degrades* downstream quality; a 2026 paper deliberately breaks a coherence axiom and finds **+11%/+18%** task usefulness. The headline sentence is already a peer-reviewed thesis (*Philosophical Studies* 2024). |
| **E6** | C1, S5 | "Back to Blackwell" is a **FOIL**, not a refutation — it accepts cycles because no optimal policy *exists*, not because repair *harms*, and has zero contact with GARP/Afriat/CCEI. One edge: its scalarising baseline loses head-to-head 0.68, which C1 must answer. |

### Revised claim status after Phase C and Phase E

| Claim | Status entering the session | Status now |
|---|---|---|
| **C1** — projection works, downstream effect measurable | load-bearing, untested | **Survives in weakened form.** The operator is not novel (see C3), and two published repair interventions have now *failed*: a choice-revision repair did not improve consistency (Nitsch et al., *PNAS* 2022), and isotonic calibration worsened the thing it was meant to repair (arXiv:2602.06286). C1b (bounded cost) and C1c (measurable effect) are both live risks, not formalities. |
| **C2** — coherence-vs-competence is open | load-bearing, "what makes it a full paper" | **PARTIALLY REFUTED.** Both directions have precedent. The plan's risk asymmetry — "either result is publishable and surprising" — is substantially gone. The sharpest single datapoint: arXiv:2505.07883 enforces probabilistic coherence on LLM-derived quantities and finds coherence improves while **held-out accuracy slightly worsens** — the plan's hoped-for "clean negative", already published in a neighbouring axiom system. |
| **C3** — nobody corrects/projects/repairs/enforces | load-bearing novelty claim | **REFUTED AS WORDED.** At least three published systems repair LLM choice/judgment consistency at inference time. See `audit/INSTRUMENT_CALIBRATION.md` §4 and `audit/killcheck_E5.md`. |
| **C4** — CCEI headroom exists | hard gate | **Holds, but the lever is wrong.** Headroom is real and well evidenced — but by *framing and format* variation (E3), not by the persona conditioning the brief's gate is built on (E2). The gate should be restated. |
| **C5** — venue reachable as scoped | load-bearing | **Holds.** Deadline, page limits, blind mode and the topic bullet all confirmed against the live CFP. Two unrecorded desk-reject risks found — see `docs/VENUE.md`. |
| **S1** | supporting | Confirmed exactly; add "baseline condition only". |
| **S2** | supporting (carrying C4) | Downgraded — cannot carry the gate. |
| **S4** | supporting | Verified on the two clauses that matter; one factual correction needed. |
| **S5** | supporting | Confirmed as foil. |
| **S7** — "the novelty cannot be the projection operator" | supporting, self-critical | **Vindicated, and more forcefully than the brief anticipated.** The brief guessed the operator was un-novel because economists have known it since Afriat. It is un-novel for a second, worse reason: it has already been *built for LLMs*. |
| **S8** — Afriat feasibility is an LP | supporting | Open — see `docs/OPEN_QUESTIONS.md` Q3. |
| **S9** — n ≤ 60 | supporting | Holds at K=2; needs a K bound added. |
| **S10** — CPU-trivial | supporting | Confirmed by measurement. See `docs/COMPUTE_NOTE.md`. |

