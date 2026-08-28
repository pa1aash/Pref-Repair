# Null-operator control — method, written before the control is run

Written 2026-08-29, in response to a reviewer argument (referred to in the operator's brief as "the
Fable review") that was never previously tested in this project: `docs/PAYOFF_AUDIT.md` §4 controls
for **severity of violation** (raw pre-repair payoff) and shows dose predicts Δpayoff beyond that
confound. It does **not** control for the specific mechanical shape of the exogenous payoff function
itself. This document designs that missing control before any number from it is looked at, per this
project's own standing practice (`docs/MAIN_EXPERIMENT_PROTOCOL.md`, `docs/PILOT_PROTOCOL.md`: write
the method, then the results; deviations are reported, not silently absorbed).

**No results from this control existed anywhere in the repository, git history, or memory before this
document was written** — confirmed by exhaustive search. This is genuinely new work, not a delayed
write-up of prior work.

---

## 1. The argument this control tests

`docs/MAIN_EXPERIMENT_PROTOCOL.md` §5 defines the exogenous payoff as an efficiency ratio against the
closed-form Cobb-Douglas optimum `x*_t` at each budget line, `alpha=0.5` fixed in advance. The
reviewer's concern: this specific payoff function has a mechanical property that could, on its own,
generate the reported dose-response relationship (`docs/MAIN_EXPERIMENT_RESULTS.md` §4, Spearman
`rho = 0.729`, `p < 0.0001`) **without GARP-restoration doing anything special**. Specifically —
payoff is concave in the expenditure share on one good, maximized at an even 50/50 split. By Jensen's
inequality, *any* operator that moves an erratic (extreme-share) bundle toward the interior of its
budget line raises the payoff score on average, regardless of whether that movement has anything to do
with restoring GARP-consistency. If the minimal-perturbation GARP projection happens to move erratic
traces toward the center as a side effect of satisfying the ordering constraints, the reported
dose-response correlation could be substantially — or entirely — a property of *displacement
magnitude toward the center*, not of *GARP-restoration specifically*.

This is a sharper version of the confound `PAYOFF_AUDIT.md` §4 already partially addresses (severity
of violation predicting room-to-improve) but is a distinct mechanism: that audit controlled for the
*level* of pre-repair payoff, not for what a *non-GARP-aware* operator of the *same displacement
budget* would have bought on its own.

---

## 2. The concavity derivation, checked against the actual code (not assumed from the protocol's prose)

`src/payoff.py` computes, for a bundle `x_t` at budget `(p_t, I_t)`:

```
payoff(x_t) = U_exo(x_t) / U_exo(x*_t),   U_exo(z) = z_A^0.5 * z_B^0.5
x*_{t,A} = 0.5 I_t / p_{t,A},   x*_{t,B} = 0.5 I_t / p_{t,B}
```

Let `s_t = p_{t,A} x_{t,A} / I_t` be the expenditure share on good A (so `x_{t,A} = s_t I_t / p_{t,A}`,
`x_{t,B} = (1-s_t) I_t / p_{t,B}` under budget exhaustion, which every bundle in this project satisfies
by construction — both `budget_sets.py`'s prompts and `projection.py`'s equality constraint (5) enforce
`p_t . x_t = I_t` exactly). Substituting:

```
U_exo(x_t) = (s_t I_t / p_{t,A})^0.5 (( 1-s_t) I_t / p_{t,B})^0.5
           = sqrt(s_t (1-s_t)) * I_t / sqrt(p_{t,A} p_{t,B})

U_exo(x*_t) = (0.5 I_t/p_{t,A})^0.5 (0.5 I_t/p_{t,B})^0.5 = 0.5 * I_t / sqrt(p_{t,A} p_{t,B})
```

Dividing, the price and income terms cancel completely:

```
payoff(x_t) = sqrt(s_t (1 - s_t)) / 0.5 = 2 * sqrt(s_t (1 - s_t))
```

**This holds exactly, verified algebraically against `src/payoff.py`'s literal code, not assumed from
`MAIN_EXPERIMENT_PROTOCOL.md`'s prose description.** Confirmed properties:

- `payoff` depends on `x_t` **only through the expenditure share `s_t`** — not on the price level, not
  on income, not on which good is "A" (the function is symmetric, `payoff(s) = payoff(1-s)`). Two
  bundles with the same share on different budget lines score identically.
- `payoff(s)` is strictly concave on `[0,1]`: `d/ds[2 sqrt(s(1-s))] = (1-2s)/sqrt(s(1-s))`, positive for
  `s<0.5`, negative for `s>0.5`, zero at `s=0.5` — a single interior maximum, `payoff(0.5)=1`, and
  `payoff -> 0` as `s -> {0,1}`.
- **Consequence for the mechanism in question:** because `payoff` is monotonically increasing as `s`
  moves toward `0.5` from either side (never non-monotonic, never overshooting relevant here since no
  legitimate operator would push `s` past `0.5`), *any* movement of `s_t` toward `0.5` raises that
  observation's payoff, by construction, independent of whether the movement satisfies any GARP
  ordering constraint. This is exactly the mechanism the reviewer describes, confirmed to hold exactly
  — not approximately, not "under some conditions" — in this project's actual implementation.

This is a real, exact property of the code, not a design flaw introduced by loose prose. It means the
dose-response result **cannot** be interpreted at face value without a control for it, which is what
the rest of this document builds.

---

## 3. The null operator: matched-displacement, center-directed, GARP-blind

**Design.** For every trace with a computed real projection dose `D_real` (the 85 GARP-violating,
successfully-projected traces in `results/main_ccei.json`), construct a second, hypothetical repaired
sequence `x̃_null` that:

1. **Knows nothing about GARP.** It never calls `garp_holds`, never touches the ordering constraints
   (1)-(4) in `src/projection.py`, and is not required to (and in general will not) restore
   GARP-consistency.
2. **Is matched in total displacement to the real projection**, so that any difference in payoff
   outcome cannot be attributed to "the null moved the data less." Uses exactly the same L1 budget
   `D_real` that the real MILP spent on that trace.
3. **Moves in the single direction the concavity argument says is privileged** — toward the interior of
   each period's budget line, i.e., toward `x*_t` (share `0.5`) — because that is the specific
   mechanism under test, not an arbitrary or random direction. (A random-direction null would not test
   this argument: by the same concavity, a *symmetric* random perturbation on average *lowers* expected
   payoff, so it would not be a meaningful adversarial control. The reviewer's claim is specifically
   about center-directed operators, so the null must be the sharpest instance of that class.)
4. **Stays on the budget line automatically.** `x_t` and `x*_t` both satisfy `p_t . x = I_t`; any convex
   combination of the two does too, so budget exhaustion needs no separate enforcement.

**Construction, one shrinkage parameter per trace:**

```
x*_t = cd_optimal_bundle(p_t, I_t)                       # src/payoff.py, unchanged, alpha=0.5
D_center = sum_t |x*_t - x_t|_1                          # total L1 distance to full re-centering
lambda   = clip(D_real / D_center, 0, 1)                 # matches the real projection's L1 budget
x̃_null_t = x_t + lambda * (x*_t - x_t)      for every t   # uniform shrink toward center, all periods
```

A single shared `lambda` across all `T=25` periods of a trace is used — not a per-period optimized
allocation — because the point of the control is to ask "what would *any* naive, GARP-blind,
center-pulling operator buy at this exact total displacement," not to let the null cherry-pick which
periods to spend its budget on for maximum payoff gain. A per-period-optimized allocator would bias the
null upward and understate how much of the real effect the crude version already explains; the uniform
version is the more conservative (harder-to-beat) choice for the real projection to still look good
against, so the comparison below is not tilted in favor of C1.

**Edge case, stated in advance:** if `D_real > D_center` (the real projection moved the trace further
than a full re-centering to `x*_t` would require), `lambda` is clipped to `1` and the null's actual
matched displacement is `D_center < D_real` — the null cannot spend more budget than full centering
uses, since moving past `x*_t` would decrease payoff by the same concavity argument and no honest
"pull toward center" operator would do that. This is logged per trace, not hidden, and the mismatch is
reported explicitly as a limit of the matching, not treated as if `D_real` was matched exactly.

**Payoff scoring.** `delta_payoff_null_t = mean_payoff(x̃_null, p, I) - mean_payoff(x, p, I)`, using
`src/payoff.py`'s unmodified `mean_payoff`, the same function that produced the real `delta_payoff` in
`results/main_ccei.json` — no separate scoring logic, so no room for the comparison itself to be
biased by an inconsistent yardstick.

---

## 4. Statistical comparisons, specified before running

All computed on the same 85-trace sample `PAYOFF_AUDIT.md` and `MAIN_EXPERIMENT_RESULTS.md` §4 use, so
every number here is directly comparable to the existing headline figures.

1. **Paired comparison, `delta_payoff_real` vs `delta_payoff_null`.** Wilcoxon signed-rank (primary,
   distribution-free) and paired t-test (reported alongside, not instead). Tests whether the real
   GARP-restoring projection buys systematically more payoff than the size-matched, GARP-blind
   center-pull at the same trace.
2. **Correlation, dose vs `delta_payoff_null`.** If the mechanical story is right, this should already
   be strongly positive and highly significant by construction (the null's `lambda`, and hence its
   payoff gain, is a deterministic function of `dose` and `D_center`) — reported as a sanity check on
   the null's own internal consistency, not as new evidence either way.
3. **Correlation, `delta_payoff_real` vs `delta_payoff_null`.** Do traces where the null predicts a
   large gain also show a large real gain?
4. **The headline test: partial correlation, dose vs `delta_payoff_real`, controlling for
   `delta_payoff_null`.** Same method `PAYOFF_AUDIT.md` §4 used to control for raw payoff, applied here
   to control for the null's mechanically-predicted gain instead. If this partial correlation collapses
   toward zero, the raw `rho=0.729` / `r=0.821` figures are substantially explained by the concavity
   mechanism, not by GARP-restoration. If it survives close to its unconditional size, GARP-restoration
   is doing something the concavity mechanism alone does not predict.
5. **OLS**, `delta_payoff_real ~ dose + delta_payoff_null`, coefficients and t-stats on both terms,
   mirroring `PAYOFF_AUDIT.md` §4's `delta_payoff ~ dose + raw_payoff` regression exactly in form.

**Decision rule, stated before results are seen** (per the operator's brief, three-way):

- **Outcome 1 (C1 survives as stated):** the paired test shows `delta_payoff_real` systematically and
  significantly exceeds `delta_payoff_null`, and the partial correlation (dose | null) remains strong
  and significant.
- **Outcome 2 (C1 needs an honest partial accounting):** the null correlation with dose/Δpayoff is
  real and non-trivial, but the real projection still shows a detectable excess effect above the null
  in the paired test and/or the partial correlation.
- **Outcome 3 (C1 as stated is not supported):** no significant paired difference between
  `delta_payoff_real` and `delta_payoff_null`, and/or the partial correlation controlling for the null
  is not significant.

This document is written and committed before `results/null_operator.json` is generated. The
implementation (`src/null_operator.py`) is a direct, literal translation of §3-4 above — any deviation
between what is coded and what is written here is reported as a deviation in
`docs/NULL_OPERATOR_RESULTS.md`, not silently reconciled.
