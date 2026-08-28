# Null-operator control — results

Run 2026-08-29 against `docs/NULL_OPERATOR_METHOD.md`, unchanged from that document's design
(`src/null_operator.py` is a literal implementation of its §3-4; no deviation to report). Zero
cost — pure post-hoc analysis of `results/main_raw.json` and `results/main_ccei.json`, no model
queried. Output: `results/null_operator.json` (85 traces + summary statistics).

**Reconstruction check passed exactly**: for all 85 GARP-violating, successfully-projected traces,
re-deriving `(p, x, incomes)` from `results/main_raw.json` via the same "first attempt with
`n_valid >= 20`" rule `src/analyse_main.py` uses, and recomputing `raw_payoff` from scratch,
matched the value already stored in `results/main_ccei.json` to `1e-6` for every trace — the
reconstruction used for this control is provably the same data the headline dose-response result
was computed from, not a re-drawn or approximated sample.

**`lambda` (the null's shrink fraction) was never clipped at 1.0** — every real projection's dose
was smaller than the distance a full re-centering to `x*_t` would have required, so the null's
matched displacement equals the real projection's dose *exactly*, for all 85 traces, with no
edge-case degradation to report.

---

## 1. Headline paired comparison

```
n = 85
mean delta_payoff_real: 0.0091  (sd 0.0155)
mean delta_payoff_null: 0.0220  (sd 0.0438)

Wilcoxon signed-rank (real vs null):  p = 3.98e-10
Paired t-test:                        t = -3.46,  p = 0.00084

Traces where null > real:  69 / 85  (81%)
Traces where real > null:  16 / 85  (19%)
median delta_payoff_real: 0.0029
median delta_payoff_null: 0.0080
```

**The size-matched, GARP-blind, center-pull null buys more than double the average payoff gain
that the real GARP-restoring projection buys, at the identical total L1 displacement budget, and
the difference is highly significant in both directions of testing.** This is not a marginal or
borderline result — the null wins on 81% of individual traces, and the paired tests agree with
`p < 0.001` on the parametric test and `p < 1e-9` on the non-parametric one.

**Holds at both models, not driven by one arm or a handful of outliers:**

| Model | n | mean Δpayoff_real | mean Δpayoff_null | Wilcoxon p | paired t-test p |
|---|---|---|---|---|---|
| qwen2.5:1.5b (headroom) | 60 | 0.0113 | 0.0267 | 5.5e-08 | 0.0040 |
| llama3.2:3b (null control) | 25 | 0.0039 | 0.0105 | 0.0010 | 0.0038 |

The single largest-dose trace in the sample (qwen 1.5b, reciprocal, replicate 12, `dose = 111.64`,
the same trace `docs/PAYOFF_AUDIT.md` §3 hand-checked) illustrates the mechanism directly: the real
projection bought `Δpayoff = +0.0739`; a GARP-blind center-pull spending the identical `111.64`
units of displacement would have bought `+0.2026` — nearly three times as much. This is consistent
with `PAYOFF_AUDIT.md` §3's own finding that the real projection's movement has low cosine
similarity (0.16-0.31) with the direction toward the exogenous optimum — most of its displacement
budget is spent satisfying GARP ordering constraints, not moving toward the center, so a null that
spends its entire matched budget moving straight at the center outperforms it on this payoff by
construction of the mechanism under test.

---

## 2. Supporting correlations

```
Spearman, dose vs delta_payoff_null:   rho = 0.912   p = 6.8e-34
Pearson,  dose vs delta_payoff_null:   r   = 0.813   p = 3.7e-21
```

Sanity check on the null's internal consistency, not new evidence: `delta_payoff_null` is a
near-deterministic function of `dose` (up to the per-trace `d_center` denominator), so this strong
correlation was expected by construction and confirms the implementation behaves as designed.

```
Spearman, delta_payoff_real vs delta_payoff_null:   rho = 0.708   p = 3.6e-14
Pearson,  delta_payoff_real vs delta_payoff_null:   r   = 0.727   p = 3.2e-15
```

The real and null gains are substantially correlated with each other — traces where the null
predicts a large gain tend to also show a large real gain — consistent with both being driven
substantially by the same underlying quantity (displacement magnitude / dose).

---

## 3. The headline partial-correlation test

```
Pearson, dose vs delta_payoff_real (unconditional):            r = 0.821   (matches
                                                                  MAIN_EXPERIMENT_RESULTS.md §4 exactly)

Partial correlation, dose vs delta_payoff_real | delta_payoff_null:
    r = 0.574,  t = 6.35,  df = 82,  p = 1.13e-08
```

Controlling for the null's mechanically-predicted gain attenuates the correlation from `r = 0.821`
to `r = 0.574` — a real, substantial reduction (roughly a third of the unconditional relationship's
strength, in variance terms roughly halved: `0.821² = 0.674` vs `0.574² = 0.329`) — but the partial
correlation remains large and highly significant. Dose retains genuine, independent information
about `delta_payoff_real` beyond what the size-matched null already predicts.

```
OLS: delta_payoff_real = -0.00138 + 0.000499*dose + 0.0632*delta_payoff_null
     dose coefficient:        t = 6.35,  p = 1.13e-08   (survives, dominant)
     delta_payoff_null coef:  t = 1.67,  p = 0.098       (not significant, given dose in the model)
```

This mirrors `docs/PAYOFF_AUDIT.md` §4's regression exactly in form. There, `dose` survived and
`raw_payoff` did not, once both were in the model together. Here, `dose` again survives and
`delta_payoff_null` does not — but `dose` and `delta_payoff_null` are themselves highly correlated
(`rho = 0.912` above), so the OLS is not a clean test of "does the null explain the effect" on its
own; the partial-correlation figure above is the more reliable read of that question, per the
method document's own stated primary test.

---

## 4. Reading the two results together

These two findings point in different directions and both must be reported, not just the one that
is more convenient:

1. **In raw magnitude, the real GARP-restoring projection is a substantially *less* efficient way
   to buy exogenous payoff than a naive, GARP-blind, center-pull operator spending the identical
   displacement budget** (§1) — the opposite of what "GARP-restoration does something beyond
   geometry" would predict. If GARP-restoration bought payoff *via* the concavity mechanism the
   Fable review describes, it should do at least as well as an operator that spends its whole
   budget purely on that mechanism; it does markedly worse, on 81% of traces.
2. **Dose still carries real, independent predictive information about `delta_payoff_real` beyond
   what the null explains** (§3) — controlling for the null's own predicted level, dose remains a
   strong, significant predictor (partial `r = 0.574`, `p = 1.1e-08`), not a redundant proxy.

Fact 1 directly contradicts the specific claim under test (that the GARP-specific direction of
repair is what is buying the payoff gain, beyond mere displacement toward the center) — the
matched null shows a *cheaper, more effective* route to the same kind of gain exists and does not
need GARP at all. Fact 2 shows the dose-response relationship is not *purely* mechanical
either — something about how much a trace needs to move to become GARP-consistent still predicts
how much the *actual* repair helps, beyond the null's own level. Both facts are consistent with a
single underlying picture: **displacement magnitude (dose) predicts payoff gain largely through the
concavity mechanism, and the GARP-specific direction of movement is, if anything, a less efficient
way to capture that mechanism than a direct center-pull would be** — not a wholly separate,
GARP-specific source of payoff.
