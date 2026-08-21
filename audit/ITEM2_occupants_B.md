# ITEM 2 — the two published negative results on repair, read in full

Scope: open question Q7, the "unread occupants" strand, restricted to the two works that bear
on whether a repair operator does anything at all — `R31` (Nitsch et al., *PNAS* 2022) and
`R38` (arXiv:2602.06286). Both were `unverified` in `audit/REFERENCE_LEDGER.md` and both are
cited in `audit/INSTRUMENT_CALIBRATION.md` §4.5 and §4.7 and in `docs/CLAIMS.md` (row C1) on
the strength of a fetcher summary alone. Both have now been read end to end.

**Access.** Neither is an access gap.
- R31: DOI `10.1073/pnas.2202070119`, PMID 35881803, PMCID PMC9351500. Green OA (CC BY-NC-ND)
  via PMC; also mirrored at `osf.io/kd4hw`. Full text read; every number below was
  re-verified by an independent `curl` of the PMC page after reading, not taken from the
  vault note alone.
- R38: `arXiv:2602.06286v2` [cs.AI], 08 May 2026, CC BY 4.0, HTML renderer available. Full
  text read including all eight appendices. Table 1 and Table 4 were re-extracted from the
  live HTML and cross-checked column-by-column against the prose, because the PDF-era warning
  about scrambled table columns applies here — Table 4 is a four-numeric-column table and a
  naive extraction interleaves the raw and calibrated columns.

Model family names in the R38 section are elided per repository hygiene; the four families are
named in Table 4 of the source and the labels below map one-to-one onto its rows in order.

---

## A. Nitsch, Lüpken, Lüschow & Kalenscher (2022), "On the reliability of individual economic rationality measurements", *PNAS* 119(31):e2202070119

### What it does

A psychometric audit of the two indices this project proposes to use as its instrument. Not an
AI paper — human subjects throughout. Three original online studies plus reanalysis of five
published datasets: eight datasets, >1,600 participants total.

The task in the original studies is a modified dictator game: each trial gives the participant
a variable endowment `m_i ∈ {2,…,10}` which they split between themselves and their best
friend at variable prices `p_Self, p_Friend ∈ {1,2,3}`. That is a two-good budget-set demand
design — the same object this project intends to elicit from an agent. Prices and budgets are
described as "randomly sampled per trial".

Three presentation formats were crossed with two measurements:

| Format | Description |
|---|---|
| diagram | Cartesian budget line, all economic parameters visible (the Choi et al. paradigm) |
| slider | continuous allocation via a slider, economic parameters concealed |
| bundles | budget line discretised into five choice options |

Indices: **CCEI** (Afriat's critical cost efficiency index — the minimal hypothetical fraction
of wealth the chooser wastes) and **HMI** (Houtman–Maks — the *count* of choices in the largest
GARP-consistent subset; note it is a count, not a fraction, which matters for reading the
deltas below). Reliability is `ICC(2,1)`, interpreted on the Koo & Li (2016) bands, preregistered
for study 2: **<0.5 poor, 0.5–0.75 moderate, 0.75–0.9 good, >0.9 excellent.**

Bronars power was computed per study by bootstrapping 1,000 virtual random choosers:
**91.8%** in study 1 (20 trials), **>99.9%** in studies 2 and 3 (40 trials). The design is not
underpowered — this is a real negative, not a failure to detect.

### (1) What "test–retest" means operationally, and the exact ICCs

The paper separates **three** distinct reliability constructs and reports each separately. This
is the single most useful structural feature of the paper for our purposes.

| Construct | Same subjects? | Gap | Budget sets | Task format |
|---|---|---|---|---|
| **Intermethod** | yes | none — same measurement block, same session | same measurement | **different** (diagram vs slider vs bundles) |
| **Test–retest (short)** | yes | minutes — second block of the same online session, separated by a filler reading task (study 1) or nothing (study 2) | fresh random draws | **same** format |
| **Test–retest (long)** | yes (97 of 148 re-recruited) | **~5 months** | fresh random draws | same format (diagram) |
| **Split-half** | yes | none — trials of a single measurement split in two | within one measurement | same format |

On budget sets: the paper does **not** state that identical budget lines were reused across
test and retest, and the described sampling procedure ("budgets and prices were randomly
sampled per trial") implies fresh draws each block. Recorded here as an inference, not a quoted
fact — but an important one, because it means their test–retest ICC confounds instability of the
index with variation in the budget sets drawn. See §"Implications" below.

**CCEI**

| Estimate | ICC(2,1) | 95% CI |
|---|---|---|
| Study 1 intermethod, measurement 1 | **0.071** | [−0.108, 0.297] |
| Study 1 intermethod, measurement 2 | 0.356 | [0.176, 0.539] |
| Study 2 intermethod, measurement 1 | 0.408 | [0.293, 0.522] |
| Study 2 intermethod, measurement 2 | 0.372 | [0.263, 0.482] |
| Study 1 test–retest, diagram | 0.626 | [0.404, 0.779] |
| Study 1 test–retest, bundles | 0.439 | [0.180, 0.641] |
| Study 1 test–retest, slider | 0.277 | [−0.021, 0.531] |
| Study 2 test–retest, diagram | 0.515 | [0.372, 0.635] |
| Study 2 test–retest, bundles | 0.497 | [0.354, 0.617] |
| Study 2 test–retest, slider | 0.434 | [0.283, 0.564] |
| Study 3 test–retest, diagram (task-familiar) | 0.522 | [0.343, 0.665] |
| Study 3, **after the revision intervention** | **0.443** | [0.248, 0.603] |
| **5-month** test–retest (studies 2↔3, 80 effective trials) | 0.511 | [0.338, 0.651] |
| Published C07 split-half | 0.256 | [0.056, 0.436] |
| Published C14 split-half | 0.503 | [0.402, 0.591] |
| Published K19 split-half | **0.183** | [−0.166, 0.491] |
| Published N21 test–retest | 0.483 | [0.340, 0.619] |
| Published A14 split-half | 0.408 | [0.268, 0.532] |

**HMI**

| Estimate | ICC(2,1) | 95% CI |
|---|---|---|
| Study 1 intermethod, measurement 1 | **0.094** | [−0.089, 0.320] |
| Study 1 intermethod, measurement 2 | 0.309 | [0.129, 0.497] |
| Study 2 intermethod, measurement 1 | 0.321 | [0.204, 0.442] |
| Study 2 intermethod, measurement 2 | 0.275 | [0.164, 0.390] |
| Study 1 test–retest, diagram / bundles / slider | 0.345 / 0.550 / 0.310 | [0.054,0.583] / [0.317,0.720] / [0.014,0.556] |
| Study 2 test–retest, diagram / bundles / slider | 0.505 / 0.640 / 0.343 | [0.360,0.626] / [0.525,0.732] / [0.182,0.487] |
| Study 3 test–retest, diagram (task-familiar) | 0.613 | [0.455, 0.733] |
| Study 3, **after the revision intervention** | 0.593 | [0.431, 0.719] |
| **5-month** test–retest | 0.526 | [0.355, 0.662] |
| Published C07 / C14 / K19 / N21 | 0.442 / **0.158** / **0.685** / 0.497 | [0.263,0.592] / [0.032,0.279] / [0.451,0.831] / [0.355,0.630] |

**Correction to the prior ledger summary.** The range recorded in
`audit/REFERENCE_LEDGER.md` and `audit/INSTRUMENT_CALIBRATION.md` §4.5 as "ICC 0.07–0.55" is
wrong at the top end. The true range across every estimate in the paper is **0.071 to 0.685**
(CCEI tops out at 0.626, HMI at 0.685). The correct and stronger statement is:

> **Not one of the ~40 ICC estimates reported in the paper reaches 0.75, the threshold for
> "good" reliability.** Every single estimate is poor or moderate.

Two further findings that the summary omitted and that matter more than the range:

- **The 5-month gap is not the problem.** Long-term test–retest (CCEI 0.511, HMI 0.526) is
  essentially identical to minutes-apart test–retest. The instability is not drift over time;
  it is the index. You cannot fix it by re-measuring sooner.
- **Intermethod is worse than test–retest.** Holding the subject and the session fixed and
  changing only the *presentation* of the budget set drops CCEI agreement to 0.071–0.408.
  Presentation format moves the index more than five months does. This is the same lever
  `docs/OPEN_QUESTIONS.md` Q2 proposes to pull for headroom, and it cuts both ways — see below.

### (2) The repair intervention: what it was, on whom, before/after

Study 3, `n = 97` re-recruited from study 2's 148, ~5 months later, diagram task only,
2 × 40 trials. Following Breig & Feldman (SSRN 2021, `10.2139/ssrn.3975829`), after both
measurement blocks were complete participants were shown **a random subset of 10 of their 40
choices per block** and given the opportunity to remake or revise each one. The previous choice
was displayed as a reminder; the slider's starting point on the budget line was re-randomised
"transparently to the participants" to force an active decision.

Before/after:

| | Δ mean CCEI | Δ mean HMI |
|---|---|---|
| Measurement 1 | **−0.025** | **−0.262** |
| Measurement 2 | **−0.013** | **−0.058** |

All four deltas are **negative** — consistency went down, not up. Test–retest reliability also
fell: CCEI **0.522 → 0.443** (moderate → poor), HMI **0.613 → 0.593**.

Three honesty notes on the magnitude and the strength of this null, because the ledger's
one-liner overstates it:

1. **HMI is a count.** ΔHMI = −0.262 out of 40 trials is a quarter of one trial. It is not a
   backfire; it is a nothing.
2. **ΔCCEI = −0.025 is not nothing.** On a [0,1] index sitting near 0.9, a 2.5-point drop is
   real in size, and it is the wrong sign.
3. **No inferential test is reported.** The paper gives descriptive means only — no p-value, no
   CI, no test statistic on any of the four deltas. This is a descriptive null on n = 97, not a
   powered equivalence test. That is a genuine soft spot in the negative result and it should be
   said out loud whenever this paper is cited against us.

The authors flag this themselves in Limitations:

> "we could not replicate the finding of Breig and Feldman (31) that allowing participants to
> revise their choices leads to an increase of revealed preference consistency… **due to the
> ineffectiveness of the intervention, we cannot rule out that a more effective intervention
> could increase the reliability** of rationality measurements."

That sentence is the most quotable line in the paper for our purposes and it is in the
original's own voice.

### (3) Is an individual's CCEI a stable trait? Their answer

No — but the *diagnosis* is not the one the summary implies, and the diagnosis is what matters.

`ICC = σ²_between / (σ²_between + σ²_error)`. A low ICC can come from a large denominator
(noisy instrument) or a small numerator (everyone is the same). Nitsch et al. explicitly test
which, and conclude it is the **numerator**:

- **Within-subject coefficient of variation** (their proxy for measurement error) drops sharply
  once a measurement has ≥20 trials, and is then "relatively small": **median WSCV 15% for CCEI,
  5% for HMI**.
- The revision intervention — designed to remove mistake choices, i.e. to shrink the error
  term — did not raise reliability, which they read as further evidence that error is not the
  binding constraint.
- Therefore: "the low reliability of contemporary measurements of individual rationality… was
  indeed driven by **a lack of interindividual differences in rationality**."

The sharpest single sentence in the paper:

> "taking individual measurements of CCEI and HMI yielded **approximately two times worse
> predictive accuracy** for another measurement within the same individual than simply assuming
> the population mean."

Also relevant and absent from every prior summary: **there is a practice effect.** Participants
became measurably *more* rational at the second measurement (study 1: b = 0.023, SE = 0.017,
t(240.93) = 1.387, p = 0.167; **study 2: b = 0.037, SE = 0.02, t(658.25) = 3.183, p = 0.002**).
Re-measuring the same subject on the same instrument moves the index upward.

### (4) What it implies for using CCEI as an outcome measure

Read carefully, the paper's prescription is narrower than "don't use CCEI", and it points
*toward* this project's design rather than away from it:

> "the lack of reliability poses a challenge to the contemporary search for **sociodemographic
> or psychological correlates** of economic rationality. Pragmatically speaking, our results
> show that a simple increase of trials or using a different task interface is not sufficient to
> fix this problem (unless the sample size is increased substantially); rather, **individual
> differences must be increased**. Possible avenues to explore here are, for instance, to ask
> participants to make decisions under stress or time pressure, increasing the difficulty of the
> decisions or **using a manipulation (i.e., a between-groups design)**."

The indictment is of **correlational, individual-differences** designs — "which people are
rational, and what predicts it". The recommended remedy is **an experimental manipulation that
widens the spread**. That is exactly what `docs/OPEN_QUESTIONS.md` Q2 proposes (framing /
response-format conditioning, CCEI 0.698–0.908 with 32–88% of runs under 0.9) and exactly what
the dose–response design does. Nitsch et al. do not tell us not to run this experiment; they
tell us not to run the experiment we were not proposing.

They also nominate **generative models** — formalising the construct rather than measuring it
ad hoc — as the promising direction, which is why GARP-EFM (`R5`, arXiv:2603.23993) cites this
paper as its motivation.

### (5) Within-session vs between-session: yes, explicitly and by design

This was a specific question and the answer is unambiguously yes. Fig. 1D of the paper states
the design: "**Intermethod reliability was calculated within measurements (across task
versions). Test-retest reliability was calculated between measurements (per task version).**"
Study 3's goal 2 is a dedicated between-session (5-month) estimate, and split-half is a third,
purely within-block estimate. The three are reported in separate subsections throughout.

The finding that matters: **within-session, across-format agreement (0.071–0.408 for CCEI) is
worse than between-session, same-format agreement (0.183–0.626)**. Format dominates time.

---

## B. Yamin, Tang, Cortes-Gomez, Sharma, Horvitz & Wilder, "When Agents Say One Thing and Do Another: Validating Elicited Beliefs from LLMs" (arXiv:2602.06286v2)

### What it does

The predecessor of `R3` (arXiv:2605.08556) by an overlapping team. It is a **measurement /
validation** paper, not an intervention paper; the repair attempt is a five-paragraph appendix.

The framework elicits, in **separate context windows**, (i) a probability judgment `p(x) =
P_E(θ=1 | x)` and (ii) a decision `A`, and asks whether the two are mutually consistent with
*some* "near-rational" decision-maker who holds `p` as its true subjective belief. The
structural kinship to GARP is real and worth noting: like Afriat, it derives **necessary and
sufficient** conditions for observational equivalence to a coherent agent **without assuming
any particular utility function** (Proposition 5). Two conditions:

- **Belief sufficiency** — `p` is a sufficient statistic for the decision-relevant information
  the agent holds. Testable as `H₀ : I(A; θ | p) = 0`, i.e. conditional independence
  `A ⟂ θ | p`, estimated by a kNN (k=3) conditional-mutual-information estimator with 500-resample
  bootstrap CIs.
- **Action-guiding / monotonicity** — the probability of choosing each action shifts
  systematically with `p`.

Empirics: four clinically grounded diagnosis domains (structural heart disease and diabetes from
real datasets; two expert-built paediatric Bayesian networks, "Cry" and "Fever"), four model
families, 200 covariate–outcome pairings × 5 repetitions per dataset.

Headline: **all 16 model–domain pairs reject the belief-sufficiency null** — every 95% bootstrap
CI on CMI is strictly above zero. But the residual dependence is small for the strongest models
(Random-Forest MSE improvement from adding `A` alongside `p`: 4.89% for the strongest model,
against 15.19% for the weakest). Monotonicity fares better: choices are usually monotone in
elicited risk, with a weak-monotonicity violation in 9 of 16 cells.

### (1) What precisely was being repaired

**Not preferences, and not the gap between stated and revealed preference.** The object being
repaired is the **elicited belief `p`** — a stated probability. The defect being repaired is
**belief insufficiency**: the model's action `A` carries information about the true state `θ`
that its stated `p` does not carry. So the target is the *stated* side of a say/do gap, and the
diagnostic is a conditional-independence statistic, not a consistency index over choices.

This is a meaningful distance from our setting. There is no budget set, no bundle, no GARP, and
critically **no exogenous payoff is ever scored** — `θ` is a ground-truth label used inside the
diagnostic, never a payoff the repaired agent is evaluated against.

### (2) What isotonic calibration was applied to, and how

Appendix G. The raw elicited belief `p` was replaced by its isotonic-regression-calibrated
counterpart `p_iso`, and `I(A; θ | p_iso)` was re-estimated with the identical kNN estimator and
bootstrap. Nothing else changed. The action distribution `A` was **not** re-elicited — the same
actions are re-scored against a recalibrated conditioning variable.

Isotonic regression is a genuine minimum-adjustment projection: it is the L2 projection of `p`
onto the cone of monotone functions of `p` fitted against realised `θ`. The structural analogy to
our projection operator is therefore real. But note *which* set it projects onto: the
**monotone-calibration** cone, defined by agreement between stated probability and empirical
frequency. That is **not** the set defined by `A ⟂ θ | p`, which is what the metric scores.

### (3) The exact before/after numbers

Table 4, raw vs isotonic-calibrated CMI, all sixteen cells (values verified against the live
HTML; model families elided per repo hygiene, ordering preserved):

| Domain / model | CMI (raw `p`) | 95% CI | CMI (`p_iso`) | 95% CI | Direction |
|---|---|---|---|---|---|
| Heart / A-min | 0.1454 | [0.1119, 0.1789] | **0.3088** | [0.2711, 0.3464] | worse ×2.1 |
| Heart / A-high | 0.0753 | [0.0422, 0.1085] | **0.3295** | [0.2967, 0.3624] | **worse ×4.4** |
| Heart / B | 0.0718 | [0.0365, 0.1070] | 0.1011 | [0.0650, 0.1373] | worse ×1.4 |
| Heart / C | 0.0675 | [0.0354, 0.0997] | 0.1948 | [0.1604, 0.2291] | worse ×2.9 |
| Cry / A-min | 0.2232 | [0.1874, 0.2589] | 0.2589 | [0.2247, 0.2931] | worse ×1.2 |
| Cry / A-high | 0.1901 | [0.1390, 0.2412] | 0.2002 | [0.1499, 0.2505] | worse ×1.1 |
| Cry / B | 0.4223 | [0.3764, 0.4681] | 0.5857 | [0.5340, 0.6375] | worse ×1.4 |
| Cry / C | 0.1745 | [0.1265, 0.2225] | 0.2110 | [0.1673, 0.2547] | worse ×1.2 |
| Fever / A-min | 0.1446 | [0.1128, 0.1765] | 0.1918 | [0.1593, 0.2242] | worse ×1.3 |
| Fever / A-high | 0.0944 | [0.0564, 0.1323] | 0.1112 | [0.0718, 0.1505] | worse ×1.2 |
| Fever / B | 0.3289 | [0.2893, 0.3686] | 0.5584 | [0.5167, 0.6001] | worse ×1.7 |
| Fever / C | 0.2060 | [0.1663, 0.2456] | 0.2407 | [0.1947, 0.2867] | worse ×1.2 |
| Diab / A-min | 0.0193 | [0.0129, 0.0258] | 0.0300 | [0.0222, 0.0378] | worse ×1.6 |
| Diab / A-high | 0.0461 | [0.0182, 0.0740] | 0.0340 | [0.0013, 0.0667] | *better* (CIs overlap) |
| Diab / B | 0.2695 | [0.2357, 0.3033] | 0.4521 | [0.4044, 0.4998] | worse ×1.7 |
| Diab / C | 0.0351 | [0.0169, 0.0533] | 0.0353 | [0.0162, 0.0544] | flat |

**Tally: 14 of 16 clearly worse, 1 flat, 1 nominally better with heavily overlapping CIs. In
zero of 16 cells does the violation go away.** The largest degradations are ×4.4 and ×2.9. Note
the pattern: **the cells that were cleanest before repair degrade the most** — Heart/A-high goes
from the second-lowest raw CMI in its domain to the highest calibrated CMI in the entire table.

### (4) The authors' own explanation for why it failed

> "In many cases, isotonic calibration increases the estimated CMI magnitude, reflecting improved
> marginal calibration without eliminating residual dependence between actions and ground truth
> after conditioning on elicited beliefs. These results suggest that **miscalibration alone does
> not account for the observed belief insufficiency.** Instead, the dependence appears to arise
> from **structural mismatches between elicited beliefs and the internal decision-relevant
> representations used by the models.** Consequently, monotonic post-hoc calibration methods such
> as isotonic regression are insufficient to restore conditional independence in this setting."

That is the whole of their explanation. They do not explain the *increase* — only the failure to
decrease. The increase is attributed to "improved marginal calibration", which is not a mechanism.

**A mechanism they do not offer, recorded here as this audit's inference and not as their claim.**
Isotonic regression via pool-adjacent-violators produces a **step function**: distinct raw values
of `p` are pooled into level sets, so `p_iso = f(p)` is a strict *coarsening* of `p`. For any
deterministic `f`, the chain rule gives

    I(A;θ | f(p)) − I(A;θ | p)  =  I(A;p | f(p))  −  I(A;p | θ, f(p))

The first term on the right is the information about the action carried by the resolution of `p`
that the calibration threw away. Because `A` was generated from the same context that produced
the fine-grained `p`, that term is generally large. The difference is therefore positive whenever
the discarded resolution of `p` is action-relevant but not state-relevant — which is precisely
the expected situation. Compounding this, the kNN CMI estimator is being run on a conditioning
variable that has just been converted from near-continuous to heavily tied and atomic, and
kNN mutual-information estimators degrade badly under ties.

If that account is right, a material part of the reported "repair made it worse" is an
**artifact of the repair coarsening the conditioning variable of its own diagnostic**, not
evidence that repair operators backfire. The observed pattern — biggest inflation where raw CMI
was smallest, i.e. where `p` carried the most usable resolution — is the signature this account
predicts. It does not rescue isotonic calibration (the violation still never goes to zero,
which is their actual claim), but it substantially weakens the paper's usefulness as evidence
that *projection-type repair backfires in general*.

### (5) Specific to their setting, or general?

**Explicitly hedged to their setting.** The concluding sentence of Appendix G ends "…insufficient
to restore conditional independence **in this setting**." The Discussion does not mention the
calibration result at all; the paper's stated conclusion is the measurement finding ("elicited
probabilities can help interpret model decisions, but should be empirically validated rather than
assumed to faithfully represent model beliefs"). Nobody claims a general law about repair. The
result is a five-paragraph robustness appendix, not a thesis.

---

## The strongest objection these create

> Two independent groups have now tried to repair choice coherence and both moved the wrong way.
> Nitsch et al. (*PNAS* 2022) gave 97 people the chance to revise their own inconsistent
> budget-set choices — the human analogue of the projection this paper proposes — and mean CCEI
> and Houtman–Maks both went *down* (ΔCCEI −0.025 and −0.013) while test–retest reliability fell
> from 0.522 to 0.443; Yamin et al. (arXiv:2602.06286) applied isotonic calibration, a genuine
> minimum-adjustment projection onto a consistency-defined cone, and the violation it targeted
> got *worse* in 14 of 16 cells, by up to a factor of 4.4, and vanished in none. The same *PNAS*
> paper establishes that the instrument this proposal builds its entire dose variable on is not
> reliable enough to support individual-level inference at all — every one of ~40 ICC estimates
> falls below the "good" threshold, presentation format alone drops agreement to 0.071, and an
> individual's own CCEI predicts their next CCEI about twice as badly as simply guessing the
> population mean. The authors are therefore proposing to grade an unreliable quantity, perturb
> it with an operator class that has twice been published as failing, and read the resulting
> payoff difference as a treatment effect.

A third citation makes it a pattern rather than a coincidence, and a reviewer will find it:
Zhu, Yan & Griffiths (`R14`, arXiv:2505.07883) enforced the additive probability axiom on a
frozen model's embeddings and reported **held-out MSE slightly worse** for the recovered
probabilities than for the raw ones, despite strictly better coherence. Three papers, three
different axiom systems, one direction: **enforcing a coherence constraint destroyed information
the constrained object was carrying.** That is the direction claim C1 in `docs/CLAIMS.md`
assumes away.

## The best available answer

There is one, it is partial, and it has three components of decreasing strength.

**Strong — neither failure is a projection onto the set that is being scored.**

- *Nitsch's revision arm is not a repair operator at all.* Participants were shown a **random**
  subset of 10 of 40 choices — not the choices that caused the GARP violations — were never told
  which choices were inconsistent, were given no consistency objective, and were free to change
  nothing. There is no guarantee, and no attempt at one, that the revised set has fewer
  violations. It is an invitation to reconsider, not a projection. Its failure is evidence
  against *"self-correction restores consistency"* — a claim this project does not make and does
  not need. On the mechanical question "does the operator raise CCEI", Nitsch is silent, because
  Nitsch's operator has no such guarantee, whereas ours attains its target by construction.
- *Yamin's isotonic arm projects onto the wrong set and then mismeasures itself.* Isotonic
  regression projects onto the monotone-**calibration** cone; the metric scores conditional
  independence, which isotonic regression neither optimises nor is monotone in. And, per the
  identity in §B(4), the projection coarsens the very variable the diagnostic conditions on,
  which mechanically inflates that diagnostic. A projection whose target set *is* the set the
  metric defines does not have this failure mode. Ours does not: `CCEI → 1` is attained by
  construction and is not estimated.

That is a real, technical, defensible answer, and it should be written into the paper.

**Medium — the reliability finding is a numerator problem, and the recommended remedy is our
design.** Nitsch et al. diagnose their own low ICC as *low between-subject variance*, not high
measurement error (WSCV median 15% CCEI / 5% HMI at ≥20 trials), and prescribe: "individual
differences must be increased… using a manipulation (i.e., a between-groups design)." ICC is a
property of the population under study, not of the instrument. Their human samples cluster near
ceiling with almost no spread. Our populations do not: `arXiv:2501.18190` reports CCEI 0.916 →
0.127/0.298 across persona conditions and `audit/killcheck_E3.md` reports 0.698–0.908 across
framings with 32–88% of runs under 0.9. If between-condition variance is an order of magnitude
larger, the same instrument can have far higher ICC. **This must be measured, not asserted** —
see the next section — but the argument is sound and it is the paper's own argument.

**Weak, and the honest limit — there is no answer to the third-negative-in-a-row problem.**
Nitsch's revision null carries no p-value and no CI (descriptive means only, n = 97), and
Yamin's is a robustness appendix explicitly hedged to its setting. Individually, neither is
strong evidence. But three independent instances pointing the same way establish an **adverse
prior**, and `audit/killcheck_E5.md` already established that neither direction of our result is
a surprise to an informed reviewer. So the effect of these papers is not to refute C1 — it is to
convert the "clean negative" fallback from an interesting outcome into a fourth confirmation.
The safety net `docs/F3-PLAN-ORIGINAL.md` relies on is thinner than the plan believes, and
nothing in the literature repairs that. This bears directly on Q1 and it is the PI's call.

## Implications for measuring a projection effect at all

**Does the reliability finding mean a before/after CCEI difference could be measuring noise?**
Not in the form the question is usually asked, and worse in another form.

*Not literally.* In this design CCEI is the **treatment**, not the outcome. The projection sets
CCEI to a target by construction; the post-projection value is not an estimate and carries no
sampling error. "ΔCCEI is noise" does not apply to the projection step, and ΔCCEI should be
reported as a **manipulation check**, never as an outcome.

*But three real hazards follow, and two of them are worse than the naive version.*

1. **The dose variable is measured with error.** The dose is defined relative to `CCEI_pre`,
   which *is* an estimate. Nitsch's WSCV of ~15% for CCEI is, on an index sitting near 0.9, a
   within-subject SD of roughly ±0.13 — **wider than the entire headroom the S4 gate is arguing
   about.** Error in the dose attenuates the dose–response slope and injects
   regression-to-the-mean: runs that happened to draw a low `CCEI_pre` get a large perturbation
   *and* would have reverted upward anyway.
2. **What actually varies run to run is which bundles get moved.** If the agent's choice sequence
   is unstable across re-runs, the projection is largely repairing sampling noise, and the
   payoff difference is driven by which re-run was drawn. This is the version that bites, and it
   is invisible if only CCEI is checked.
3. **The noise floor that matters is the payoff's, not CCEI's.** Nitsch says nothing about
   payoff reliability. If the exogenous payoff has a run-to-run SD comparable to the projection
   effect, the study is unpowered regardless of how clean the CCEI story is.

**What the project must do before interpreting any intervention effect.** These are cheap,
they run before any intervention, and stating them pre-emptively converts the objection into a
methods paragraph.

- **Re-test the models, not the humans.** `K ≥ 5` independent re-runs of each agent on the
  **same** budget sets, fresh context each time, randomised trial order and randomised
  within-budget-line starting point (Nitsch randomised the slider start "transparently to the
  participants" for exactly this reason). Report `ICC(2,1)` and WSCV for CCEI *and* HMI on the
  Koo & Li bands. Because our budget sets can be held fixed across re-runs — which Nitsch's
  apparently were not — our ICC is not directly comparable to theirs and should be higher; say
  so, and say why.
- **Preregister a reliability floor and an alternative.** If per-run CCEI cannot clear "good"
  (0.75), the individual run cannot carry a continuous dose variable; switch to condition-level
  means with runs as replicates, and power on the condition, not the run.
- **Measure intermethod reliability too, and expect it to be bad.** Nitsch's worst numbers are
  not test–retest but intermethod (CCEI 0.071–0.408) — same subject, same session, different
  presentation. Our Q2 manipulation *is* a presentation manipulation. Headroom and construct
  validity are the same variable here, and the paper needs an explicit paragraph owning that
  tension rather than being caught by it.
- **Report the payoff's own run-to-run variance under no intervention, and power the
  dose–response against that number.** This is the actual noise floor and no reviewer will
  accept the result without it.
- **Guard the practice effect.** Nitsch found CCEI rises on second measurement (study 2
  b = 0.037, p = 0.002). The model analogue is in-context accumulation and order effects. Fresh
  contexts, randomised order, counterbalanced conditions.
- **Add a distance-matched null-operator control.** This is the single most valuable design
  change these two papers imply, and **neither paper had it.** Alongside the GARP projection,
  run a perturbation of *identical* magnitude (same L1/L2 displacement, same number of bundles
  moved) that relocates bundles along the budget line **without** improving consistency. Without
  it, any payoff change is confounded with "we moved the bundles at all", and both published
  negatives are wide open to exactly that confound — Nitsch's revision arm has no
  matched-magnitude control and Yamin's isotonic arm has no matched-coarsening control. Having
  one is a genuine methodological contribution and it is cheap.
- **Correct the record in the S4 gate.** A 0.99 threshold is not usable when the instrument's
  own within-subject SD may be ±0.13. Combined with `R26` (31% of uniform-random agents clear
  CCEI 0.99) and Q6 (Andrews' Lemma 1: CCEI can read exactly 1.0 while GARP fails), the gate is
  attacked from three independent directions. Replace it with the simulated CCEI distribution
  under the actual design.

## Verdict: does the narrow cell survive?

**It survives. The bar rises, materially, in three specific places.**

The surviving cell, as stated in `docs/OPEN_QUESTIONS.md` Q1 and `audit/killcheck_E5.md`, is:
minimal-perturbation projection of **an agent's own choice sequence** onto the rationalizable
set, scored against an **exogenous payoff not derived from the preference data**, traced as a
**dose–response curve**. Test the two papers against each of the three conjuncts:

| | Nitsch (R31) | Yamin (R38) |
|---|---|---|
| Own-choice projection onto the rationalizable set? | **No** — human subjects, and the manipulation is voluntary re-choice of a random 25% of trials with no consistency objective and no guarantee of improvement | **No** — the repaired object is a stated probability, not a choice sequence; the projection targets a calibration cone, not the set the metric defines |
| Exogenous payoff scored under the repaired object? | **No** — the outcomes are CCEI, HMI and ICC, all internal to the preference data | **No** — `θ` is a ground-truth label inside a conditional-independence diagnostic; no payoff is ever scored |
| Dose–response over degree of enforcement? | **No** — one arm, binary | **No** — one arm, binary |

Zero of six conjuncts are occupied. The cell is **not closed** and neither paper can be cited as
having done the experiment.

What they do change:

1. **C1 stops being an assumption and becomes a hypothesis with an adverse prior.** Three
   independent results in three axiom systems all point at "enforcing coherence destroys
   information". The paper must now argue *for* a positive effect rather than presuming one, and
   must cite all three prominently rather than being caught by them.
2. **A reliability floor becomes a precondition, not a robustness check.** Test–retest of CCEI
   *on the models under study*, with fixed budget sets and fresh contexts, has to run and be
   reported before any intervention effect is interpreted. It is cheap and it should have been
   in the plan.
3. **The "clean negative" fallback loses most of its value.** This is the real cost and it lands
   on Q1, not on the science. A fourth negative in a literature that already has three is not a
   result; it is a replication. If the paper's insurance policy is "either direction is
   publishable", that policy is now largely void.

There is, however, a compensating reframe that these papers *strengthen* rather than weaken.
Because every published repair result — positive and negative alike — is binary (enforced vs
not), the question none of them can pre-empt is **where the crossover is**: whether the
dose–response curve is monotone, and whether there is an interior optimum at partial
enforcement. Nitsch backfired slightly at full self-revision; Yamin degraded at full
calibration; TrustJudge and CONSISTRE improved at full enforcement. Those are four points on a
curve nobody has drawn, in four different systems. Drawing the curve in one system, with a
distance-matched control and an exogenous payoff, is a contribution that survives everything in
this document — and it is a sharper claim than the one the plan currently makes.

---

## Ledger updates

Proposed replacement rows for `audit/REFERENCE_LEDGER.md`. **Not applied here** — a sibling
process owns that file.

**R31** — status: `verified`

> | **R31** | Nitsch, F. J., Lüpken, L. M., Lüschow, N. & Kalenscher, T. (2022), "On the reliability of individual economic rationality measurements" | *PNAS* 119(31):e2202070119; DOI 10.1073/pnas.2202070119; PMCID PMC9351500 | **NOT in the plan.** Psychometric audit of CCEI and HMI; plus a choice-revision "repair" arm that failed | **C1, C4** | **verified** | **Read in full** (PMC, re-verified against live HTML). Prior ledger range "ICC 0.07–0.55" is **wrong at the top**: true range **0.071–0.685**, and **none of ~40 ICC estimates reaches 0.75 ("good")**. Intermethod (same session, different presentation) is *worse* than 5-month test–retest — format dominates time. Repair arm (n=97, random 10 of 40 choices revisable): **all four deltas negative** (ΔCCEI −0.025 / −0.013; ΔHMI −0.262 / −0.058 — a quarter of one trial out of 40), test–retest CCEI 0.522 → 0.443. **But no p-value, CI or test statistic is reported on any delta** — a descriptive null, not a powered equivalence test, and the authors concede "we cannot rule out that a more effective intervention could increase the reliability". Diagnosis is **low between-subject variance, not measurement error** (WSCV median 15% CCEI / 5% HMI at ≥20 trials); their own prescription is "individual differences must be increased… using a manipulation (i.e., a between-groups design)" — i.e. our design. **Verdict: does not close the cell; imposes a model-level test–retest precondition and corrects the S4 gate.** `audit/ITEM2_occupants_B.md` §A |

**R38** — status: `verified-discrepant`

> | **R38** | Yamin, K., Tang, J., Cortes-Gomez, S., Sharma, A., Horvitz, E. & Wilder, B., "When Agents Say One Thing and Do Another: Validating Elicited Beliefs from LLMs" | arXiv:2602.06286v2 [cs.AI], 08 May 2026 | **NOT in the plan.** Belief/action coherence measurement; Appendix G tests isotonic calibration as a repair | **C1, C2** | **verified-discrepant** | **Read in full** (arXiv HTML; Tables 1 and 4 re-extracted and column-checked against prose). The ledger's "isotonic calibration fails to repair belief-insufficiency and often worsens it" is **directionally right but materially overstated as evidence against projection.** Exact numbers (Table 4): **14 of 16 cells worse, 1 flat, 1 nominally better with overlapping CIs; violation eliminated in 0 of 16**; largest degradation ×4.4 (0.0753 → 0.3295). **Three qualifications the summary omitted:** (a) the repaired object is a **stated probability**, not a choice sequence — no GARP, no budget set, and **no exogenous payoff is ever scored**; (b) isotonic regression projects onto the **calibration** cone while the metric scores conditional independence — it repairs a different set than the one it is graded on; (c) PAVA **coarsens** the diagnostic's own conditioning variable, which by `I(A;θ|f(p)) − I(A;θ|p) = I(A;p|f(p)) − I(A;p|θ,f(p))` mechanically inflates CMI, and the observed pattern (largest inflation where raw CMI was smallest) matches that artifact — this mechanism is **this audit's inference, not the authors' claim**. Authors hedge explicitly to "in this setting" and omit the result from the Discussion entirely; it is a robustness appendix, not a thesis. **Verdict: does not close the cell; supplies an adverse prior on C1 and a strong argument for a distance-matched null-operator control.** `audit/ITEM2_occupants_B.md` §B |

**Also worth propagating** (not owned here): `audit/INSTRUMENT_CALIBRATION.md` §4.5 repeats the
incorrect "ICC 0.07–0.55" figure and should read **0.071–0.685, none above 0.75**; and §4.7's
"isotonic calibration fails… and often worsens it" should carry the 14/16 tally and the
wrong-set / coarsening qualification. `docs/CLAIMS.md` row C1's "isotonic calibration worsened
the thing it was meant to repair" is not quite right — it worsened the *diagnostic*, and the
thing it was meant to repair was marginal calibration, which it improved.
