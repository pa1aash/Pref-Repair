# Paper story — where Track 1 leaves the paper's argument

Written 2026-08-29, closing Track 1. Synthesizes two parallel sub-agent analyses run against
`docs/CORRECTED_PAYOFF_RESULTS.md` (1C-i, the verdict) and against `results/null_operator.json` +
`results/corrected_payoff.json` directly (1C-ii, the mechanism check). Documentation and judgment
only — `FRAMING.md` and `paper.tex` are untouched in this session.

---

## 1. The headline finding, stated plainly

**C1 as currently written in `FRAMING.md` — that restoring GARP-consistency specifically improves
an exogenous measure of decision quality, beyond what mere displacement toward the interior of the
budget line would buy on its own — is not supported by either of two independently-designed
exogenous payoffs.** A GARP-blind operator, spending the identical L1 displacement budget as the
real GARP-restoring repair but with no knowledge of GARP at all, outperforms the real repair under
both payoffs, significantly, at both models, and (under the second payoff) in every one of 20
independent randomized trials. This is not a hedge or a "more work needed" result — it is a
negative finding, reached twice, by two payoffs built specifically not to share the flaw that sank
the first one.

---

## 2. Experiment 1 — the original payoff and the centering-confound mechanism

The paper's original exogenous payoff, equal-weight Cobb-Douglas efficiency (`docs/
MAIN_EXPERIMENT_PROTOCOL.md` §5), reduces algebraically to `payoff(x) = 2*sqrt(s(1-s))` where `s`
is expenditure share on one good (`docs/NULL_OPERATOR_VERDICT.md` §1C) — concave, with a single
maximum at `s=0.5`, identical for every trace in the experiment. A null operator that does nothing
but shrink each trace's bundles toward that fixed point, matched to the real repair's own L1
displacement, **out-performed the real GARP-restoring repair by roughly 2.4x** (mean
`Δpayoff_null = 0.0220` vs. mean `Δpayoff_real = 0.0091`), significant at both models
independently (`docs/NULL_OPERATOR_RESULTS.md` §1). The paper's headline dose-response correlation
(`rho=0.729`, `docs/MAIN_EXPERIMENT_RESULTS.md` §4) is real, but this control shows it is
substantially explained by the payoff's own geometry, not by GARP-restoration specifically.

## 3. Experiment 2 — the corrected payoff, same qualitative result

`docs/CORRECTED_PAYOFF_DESIGN.md` designed a second payoff specifically to remove the single-fixed-
target property: the Cobb-Douglas weight becomes a per-trace, independently-drawn random variable
`alpha_s ~ Uniform(0.05,0.95)`, so there is no longer one universally-correct point to aim at.
Implemented and run in `docs/CORRECTED_PAYOFF_RESULTS.md`, with the comparison repeated across
`K=20` independent draws of the random target for robustness. Result: **the same GARP-blind,
fixed-center null operator still out-performs the real repair, by roughly 3x** (mean
`Δpayoff_null = 0.0217` vs. mean `Δpayoff_real = 0.0072`), significant (Wilcoxon `p<0.05`) in
**20 of 20 independent draws**, with a win rate for the null of 70.8% of traces on average. An
upper-bound "oracle" null (privileged, aims at the true per-trace random target) does even better
(80.4% win rate, significant in 20/20 draws) — reported for completeness, not as the primary
comparison, per the design doc's own instruction to keep the two nulls separate.

A partial correlation of dose with the real repair's `Δpayoff`, controlling for the null's own
predicted gain, remains positive (mean `r=0.369`, primary null) and is significant in 14 of 20
draws — attenuated from Experiment 1's `r=0.574`, but 1C-i's analysis found this attenuation is
**not distinguishable from the draw-to-draw noise the corrected experiment's own 20 draws already
show** (0.574 sits inside the observed range of those 20 draws, well under the max). It is not
read as a new, separate finding — the paired-comparison result (null beats real) is the same
verdict-determining fact in both experiments, and that fact is unambiguous in both.

## 4. Why no third payoff was attempted — a stated methodological choice

**No further payoff redesign is planned, and this is a deliberate scope decision, not a
resource constraint.** Two independently-designed, independently-motivated payoffs — one the
paper's original, one built from scratch specifically to remove the first one's known flaw —
converging on the same negative result *is* the finding. A third attempt, run only because the
second one also came back negative, would not be a further robustness check; it would be
payoff-shopping — iterating the yardstick until one is found under which GARP-restoration happens
to look good, which is precisely the kind of researcher-degree-of-freedom problem an exogenous
payoff was introduced to prevent in the first place. The paper should report both experiments as
the completed empirical core of this question, not as an unfinished search.

## 5. A partial mechanistic note, offered with its own caveat

1C-ii tested whether the null's advantage is really about "centering" specifically, or more
generally about "any operator that moves a badly-erratic trace away from its extreme starting
point looks good, and centering is just a cheap way to do that." Trace extremity (`1 - raw_payoff`
under the original fixed payoff, a stable measure of the raw bundles regardless of which payoff
later scores them) predicts the null's gain strongly in **both** experiments (Experiment 1:
Pearson `r=0.679`; Experiment 2 primary null: mean `r=0.631` across 20 draws) and predicts it more
strongly than it predicts the real repair's own gain in both cases.

**This pattern alone does not cleanly discriminate the two explanations**, and 1C-ii flagged this
itself rather than claim more than the data support: Experiment 2's *primary* null is mechanically
the identical fixed-center-shrink operator as Experiment 1's — only the scoring payoff changed —
so finding the same extremity-dependence in both is close to expected either way, not strong
independent evidence for the "generic escape" reading. The more informative piece is that
Experiment 2's *oracle* null — which targets a genuinely different, per-trace-varying point, not a
universal fixed one — shows essentially the same extremity-advantage pattern (mean `r=0.624`).
That a trace-varying target still tracks starting-point extremity this closely is read as
**partial support** for "moving toward the interior helps most when the start was extreme,
regardless of exactly which interior point," with fixed-point centering as one cheap
implementation of that broader mechanism rather than a distinct phenomenon of its own — offered as
a plausible explanatory note for the paper's discussion section, not as a load-bearing result on
its own, and not as strong as a fully independent test would be.

## 6. What survives, untouched by this result

- **C2 (the identification claim)** is logically independent of C1 and unaffected: it does not
  claim a sign for the coherence-competence relationship, only that this project's design is the
  first to measure that relationship without confounding it with representational capacity or a
  preference-judgment scoring function (`docs/FRAMING.md` §2). Nothing in the payoff-control work
  touches this claim's identification argument.
- **C3 (the discard-selection instrument-validity finding)** is also logically independent — it is
  about which observations survive a naive discard rule, not about what an exogenous payoff says
  about the survivors (`docs/FRAMING.md` §3). It replicated directionally at main-experiment scale
  (`docs/MAIN_EXPERIMENT_RESULTS.md` §2: 43.3% first-attempt discard under 1.5B reciprocal framing
  vs. nowhere near that elsewhere) and is untouched by anything in this session.

These two claims, not C1, are what the paper's contribution should rest on if C1 is retired or
substantially rewritten — a scope decision for the operator, not attempted in this session.

## 7. What this document is not confident about, stated rather than smoothed over

- **The partial correlation's persistence (significant in 14-15/20 draws, not 20/20) is a real,
  if modest, signal that dose carries some information about the real repair's payoff beyond what
  the null predicts.** This document does not claim that signal is zero — only that it is not
  large or consistent enough to overturn the paired-comparison verdict, which is unambiguous in
  both experiments. A reader who weighs the partial correlation more heavily than the paired test
  could reasonably read this as closer to Outcome 2 (a partial, honestly-reduced claim) than
  Outcome 3 (fully unsupported) — 1C-i's call for Outcome 3 rests on treating the paired-magnitude
  result as decisive, which this document agrees with but flags as a judgment call, not a
  mechanical consequence of the numbers alone.
- **The mechanism note in §5 is the least certain part of this document.** 1C-ii was explicit that
  its own cross-experiment comparison cannot cleanly separate "centering" from "generic escape from
  a bad start" using the primary nulls alone, because the operator didn't change between
  experiments. The oracle-null evidence is suggestive, not conclusive, and should be presented in
  the paper (if at all) as a discussion-section hypothesis, not a result with its own significance
  test standing behind it.
- **Neither sub-agent, nor this document, has verified the corrected payoff's own self-audited
  limitation** (`docs/CORRECTED_PAYOFF_DESIGN.md` §4: the fix is weaker for the most extreme-share
  traces, since no bounded random target's support reaches literal corner allocations) **against
  a stratified breakdown by dose or extremity within Experiment 2's own data.** The design doc
  called for this stratified check explicitly; it has not been run. If it were, it would plausibly
  sharpen §5's mechanism note but is not expected to change the headline verdict, since the
  paired-comparison result already holds at both models and in every draw without stratification.
