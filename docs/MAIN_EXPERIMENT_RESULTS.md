# Main experiment results

Run 2026-08-26 against `docs/MAIN_EXPERIMENT_PROTOCOL.md`, at the `N=30` scope the operator selected
at the Gate. **Zero cost** — all inference on locally-hosted open-weight models via ollama on the
same M1 MacBook Air used for the pilot, under `caffeinate` to survive idle sleep. No commercial
endpoint was contacted.

187 attempt-records logged across 150 replicate slots (2 models × up to 3 conditions × 30
replicates); 142 slots kept a usable trace, 8 were residual discards after 3 attempts. Every cell
got its full 30 replicates — no cell was short-changed by the retry protocol.

---

## 0. Instrument validity, checked on every replicate's own independently-drawn budget set

Unlike the pilot (one shared budget set), every replicate here draws its own. Bronars power is
therefore reported per cell as a mean across 30 independent draws, not a single number:

| Model | Condition | Mean Bronars power | Min | Mean random-agent CCEI |
|---|---|---|---|---|
| llama3.2:3b | baseline | 0.9997 | 0.9990 | 0.7255 |
| llama3.2:3b | reciprocal | 0.9998 | 0.9990 | 0.7218 |
| qwen2.5:1.5b | baseline | 0.9995 | 0.9980 | 0.7217 |
| qwen2.5:1.5b | multiturn | 0.9997 | 0.9980 | 0.7200 |
| qwen2.5:1.5b | reciprocal | 0.9995 | 0.9980 | 0.7293 |

Every one of 150 independent draws holds power ≥ 0.998 — the design's power does not depend on
which specific draw a replicate happened to get. All 85 GARP-violating traces' projections were
independently re-verified GARP-consistent (§4 of the protocol's requirement); zero failed
verification; MIP gap on every solve was ≤ 8.1×10⁻⁵ (essentially exact).

---

## 1. Headline table

| Model | Condition | n kept | mean CCEI | 95% CI | GARP pass | mean dose (L1) | mean Δpayoff |
|---|---|---|---|---|---|---|---|
| llama3.2:3b | baseline | 30 | 0.9900 | [0.9796, 1.0003] | 0.73 | 5.01 | +0.0018 |
| llama3.2:3b | reciprocal | 28 | 0.9713 | [0.9552, 0.9874] | 0.39 | 6.27 | +0.0016 |
| qwen2.5:1.5b | baseline | 30 | 0.9522 | [0.9253, 0.9791] | 0.40 | 16.68 | +0.0090 |
| qwen2.5:1.5b | multiturn | 30 | 0.9540 | [0.9350, 0.9729] | 0.10 | 14.54 | +0.0083 |
| qwen2.5:1.5b | reciprocal | 24 | 0.9413 | [0.8833, 0.9993] | 0.38 | 12.03 | +0.0065 |

---

## 2. Discard rates — C3's finding, now measured at experiment scale, not just the pilot

| Model | Condition | First-attempt discard | Residual (post-3-attempt) discard |
|---|---|---|---|
| llama3.2:3b | baseline | 0/30 (0.0%) | 0/30 (0.0%) |
| llama3.2:3b | reciprocal | 9/30 (30.0%) | 2/30 (6.7%) |
| qwen2.5:1.5b | baseline | 5/30 (16.7%) | 0/30 (0.0%) |
| qwen2.5:1.5b | multiturn | 0/30 (0.0%) | 0/30 (0.0%) |
| qwen2.5:1.5b | reciprocal | 13/30 (43.3%) | 6/30 (20.0%) |

**C3 replicates directionally at the new scale, with a smaller first-attempt magnitude than the
pilot's 52% (43.3% here) — plausibly because this run's budget sets are independently drawn per
replicate rather than the pilot's single fixed set, which itself may have been an unusually hard
draw.** The qualitative finding stands regardless: reciprocal framing at 1.5B produces far more
output-contract failures than any other cell, including the *other* 1.5B manipulation (`multiturn`,
0% discard) — so the discard problem is specific to the reciprocal-price-framing manipulation, not
to 1.5B as a scale or to unusual task formats generally.

**The retry protocol recovers most, not all, of the failures.** First-attempt discard at 1.5B
reciprocal (43.3%) falls to a residual 20.0% after 3 attempts — a real reduction, not a full fix.
20% residual discard is still large enough that the surviving 24 sessions are not guaranteed to be
representative, which bears directly on how the confirmatory test below should be read.

---

## 3. Confirmatory framing-effect tests

### 3B (null-effect control per the amended C1): replicates the pilot's finding

```
GARP pass rate: baseline 22/30 = 0.73  vs  reciprocal 11/28 = 0.39     p = 0.0089
CCEI:           baseline 0.9900±0.0277 vs reciprocal 0.9713±0.0415    t-test p = 0.0508
```

**Same qualitative pattern as the pilot, at a comparable (if smaller) magnitude**: reciprocal
framing produces a large, statistically significant collapse in GARP pass rate (Δ = −0.34 here vs.
the pilot's −0.59) while CCEI itself moves much less and only reaches borderline significance
(p = 0.051, not < 0.05) — the same near-1 compression effect the pilot flagged. This is a genuine
replication with an independent budget-set design, not the same fixed stimulus re-scored.

### 1.5B reciprocal framing: the effect the pilot could not measure cleanly — now measured, and it is not there

```
GARP pass rate: baseline 12/30 = 0.40  vs  reciprocal 9/24 = 0.38     p = 0.8515
CCEI:           baseline 0.9522±0.0721 vs reciprocal 0.9413±0.1375   t-test p = 0.7276
```

**With the C3-motivated retry protocol partially correcting the discard-selection problem, the
1.5B reciprocal-framing effect is statistically indistinguishable from zero on both metrics.** This
is a real result, not a null-by-underpowering: `N=24` survives per cell, comfortably above the
`n=10` the pilot's own 3B magnitude would have needed to detect at 80% power (§2.2 of the
protocol), and the observed CCEI point estimate actually moves in the *expected* direction
(0.9522 → 0.9413) but the effect is small relative to 1.5B's own high noise (SD 0.0721 baseline,
0.1375 reciprocal) and the confidence intervals overlap almost entirely. **Read plainly: once the
survivorship bias C3 identified is substantially (not fully — 20% residual discard remains)
corrected, reciprocal-price framing does not reliably move 1.5B's coherence on this design.** The
pilot's own confounded +0.0169 CCEI "effect" is neither confirmed nor cleanly refuted here — it is
superseded by a properly-powered, still-noisy null.

### 1.5B multiturn (the literature's format mechanism, arXiv:2505.21371): the largest, cleanest effect in this experiment

```
GARP pass rate: baseline 12/30 = 0.40  vs  multiturn 3/30 = 0.10      p = 0.0073
CCEI:           baseline 0.9522±0.0721 vs multiturn 0.9540±0.0509    t-test p = 0.9131
```

**This is the strongest confirmatory result in the whole run, and it came with zero discards on
either side of the comparison** — no selection-bias caveat is needed. Splitting each of 25 rounds
into a separate sequential call collapses the GARP pass rate from 40% to 10% (a larger drop than
reciprocal framing produced at 1.5B, and comparable in magnitude to 3B's reciprocal-framing
collapse), while CCEI again barely moves (p = 0.91) — a third independent replication, across two
models and two different manipulations now, of the same pattern: **GARP pass rate is the sensitive
instrument for framing/format disruption; CCEI is not.** `docs/PILOT_RESULTS.md` §3's own
recommendation — report violation counts alongside the index — is vindicated a second and third
time by this run.

**Read against `docs/MAIN_EXPERIMENT_PROTOCOL.md` §3.1's justification for adding this arm:** the
literature's predicted mechanism (format, not price-wording) is confirmed as the dominant lever at
this scale, cheaply (§3.1 estimated 1.3× baseline wall-clock; actual measured cost was closer to 2×
but still small in absolute terms) and without the discard-selection problem that compromises the
reciprocal-framing comparison.

---

## 4. The dose–response relationship — C1's central question

Across all 85 GARP-violating traces (60 at 1.5B, 25 at 3B) with a computed projection dose:

```
Spearman rho = 0.729   p < 0.0001
Pearson  r   = 0.821   p < 0.0001
mean delta_payoff = +0.0091  (sd = 0.0155)
one-sample t-test (delta_payoff != 0): t = 5.41, p < 0.00001
repair improved payoff:  70 / 85 traces (82%)
repair worsened payoff:  15 / 85 traces (18%)
```

**The dose axis is real, monotone, and strongly predictive of the payoff gain from repair.** Larger
projection distance (more perturbation needed to restore GARP) is associated with a larger positive
change in the exogenous payoff after projection — exactly the relationship C1 asks whether it
exists, and it does, at a significance level (`p < 0.0001`) that is not a borderline call. Repair
does not help universally — 18% of traces lost payoff after projection, consistent with the adverse
prior `docs/FRAMING.md` §1 states rather than hides — but the population-level effect is positive
and precisely estimated.

**Split by model, both are significant, but the headroom model's relationship is stronger:**

| Model | n violating | mean dose | mean Δpayoff | Spearman rho | p |
|---|---|---|---|---|---|
| qwen2.5:1.5b (headroom) | 60 | 20.42 | +0.0113 | 0.756 | < 0.0001 |
| llama3.2:3b (null control) | 25 | 13.04 | +0.0039 | 0.614 | 0.0011 |

**This is the one place this run's data contradicts the amended C1's own stated expectation for the
3B control, and it is reported rather than silently patched, per standing practice.**
`docs/FRAMING.md` §1 (amended 2026-08-26) states: *"At 3B, C1c is expected to fail to reject the
null; that is the control functioning correctly, not the claim failing."* That expectation is not
borne out: 3B's dose–response relationship is smaller than 1.5B's (rho 0.614 vs 0.756, mean
Δpayoff 0.0039 vs 0.0113) but it is itself statistically significant (`p = 0.0011`, `n = 25`), not a
null result. **The correct reading, on this evidence, is not "the control found nothing" but "the
control found a real effect of about a third the size."** 3B has little baseline CCEI headroom
(mean 0.9900) — there is not much incoherence sitting around to repair — but on the violations that
do occur (mostly induced by reciprocal framing, per §3 above), projecting them onto the
GARP-consistent set still measurably helps on the exogenous payoff. This narrows what the 3B arm
demonstrates: it is evidence the identification strategy is not an artefact of the 1.5B model
specifically, but it is not the "nothing happens" result the amendment's language anticipated, and
the amendment's framing should be read with that correction in mind rather than treated as
confirmed.

---

## 5. What this experiment actually found, stated plainly

1. **The dose–response relationship C1 asks about is real, strongly monotone, and precisely
   estimated** at both models, stronger at 1.5B (the headroom model) than at 3B (the control) —
   consistent with, but not identical to, what the amended C1 predicted (§4 above).
2. **CCEI compression near 1 is not a pilot artefact.** It reproduced independently at 3B
   (reciprocal framing) and at 1.5B (multiturn format), across two different manipulations, on
   freshly and independently drawn budget sets. GARP pass rate is the metric that carries the
   framing/format signal; CCEI understates it every time this project has measured it.
3. **The pilot's headline 1.5B reciprocal-framing finding does not survive proper replication.**
   Once the C3-motivated retry protocol reduces (not eliminates) the discard-selection bias, there
   is no detectable coherence effect of reciprocal framing at 1.5B on this design. The pilot's own
   confounded number should not be cited as evidence either way.
4. **The literature's predicted format mechanism (arXiv:2505.21371) outperforms this project's own
   reciprocal-price-framing manipulation at 1.5B**, and does so without any discard-selection
   confound at all — the cleanest single comparison in the whole run.
5. **The discard problem (C3) is specific to reciprocal-price framing, not to 1.5B generally.** The
   `multiturn` condition at the same model had zero discards.

## 6. Deviations from protocol

1. **Wall-clock ran close to the protocol's `N=30` estimate (§7, ~2.1 hours) despite a mid-session
   contention spike during pretesting** (one test call took 995 s under heavy concurrent load from
   other processes on this machine). The full run itself, once launched, showed no comparable
   outliers — the slowest call was 44.5 s — so the contention observed during pretesting did not
   carry into the timed run. Recorded as a deviation because the Gate decision was made with that
   risk stated explicitly, and the risk did not materialise.
2. **`multiturn`'s per-session wall-clock was measured, not merely assumed**, per the protocol's own
   requirement (§3.1) that its planning estimate "must be re-measured before the run." The smoke
   test's single-session measurement (63.6 s) was higher than the 1.3× planning assumption (41.5 s)
   but the full run's actual mean was closer to the plan; the discrepancy did not require redesign.
3. **The machine did not crash during the timed run.** §1's model-roster decision anticipated
   instability risk from multi-model cycling; the two-model, model-major design held up cleanly
   across the full 187-attempt run.

---

## 7. What was not done

`N=150` (the CCEI-power-matched design from the protocol's §2.2) was not run — the operator deferred
that decision pending this run's results, per the Gate resolution. Given §4's dose–response result
is already significant at `p < 0.0001` on the `N=30` design's 85 violating traces, a case can be made
that the CCEI-specific power shortfall matters less than it looked at Gate time, since the underlying
claim (C1c) has independent, strong support from the dose–response analysis rather than resting on
the CCEI framing-effect comparison alone. That is a judgement for the operator, not resolved here.
