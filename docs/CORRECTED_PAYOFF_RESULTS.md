# Corrected-payoff null-operator control — raw results

Run 2026-08-29 against `docs/CORRECTED_PAYOFF_DESIGN.md`, implemented exactly as frozen in that
document (`src/corrected_payoff.py`). No interpretation, no verdict, no paper edits in this
document — numbers only, same discipline as `docs/NULL_OPERATOR_RESULTS.md`.

---

## 0. Implementation notes and deviations

**Seed-formula concretisation (not a design change).** The design doc's suggested formula
(`20260829_500_000 + 1000*replicate_index`) is ambiguous once multiple models/conditions and
`K=20` independent draws are involved (`replicate_index` alone is not unique across the 85
traces). Resolved as: `trace_index` = position of `(model, condition, replicate)` in the sorted
list of all 85 violating traces; `seed(k, trace_index) = 20_260_829_500_000 + k*1_000_000 +
1000*trace_index`. Documented per the operator's instruction to report rather than silently
resolve ambiguity in the frozen design.

**Solver retry (operational, not a design change).** Re-running `src/projection.py`'s `project()`
to recover `x̃_real` (needed to re-score under the new payoff; not stored in `results/
main_ccei.json`) hit the 30s solver time limit on one trace (`qwen2.5:1.5b, baseline, replicate
11`) on the first attempt, under heavy machine contention (load average ~140-150 observed during
this session, consistent with previously-documented contention in `docs/
MAIN_EXPERIMENT_RESULTS.md` §6). Retried once at `time_limit=120s`; succeeded. On the run whose
numbers are reported below, **all 85 traces solved within the original 30s budget with no
retries needed.**

**Reconstruction check: passed.** Re-solving the projection MILP for all 85 GARP-violating traces
reproduced `dose_l1` matching `results/main_ccei.json` to `1e-3` for every trace, with zero
mismatches.

**Design parameters used, exactly as frozen:** `alpha_s ~ Uniform(0.05, 0.95)`, one independent
draw per trace per replicate-draw `k`, `K = 20` independent draws of the full 85-trace alpha
vector. Both null constructions from `docs/CORRECTED_PAYOFF_DESIGN.md` §6 computed and kept
separate: **PRIMARY** (information-fair — shrinks toward the fixed `(0.5,0.5)` target, identical
construction to `src/null_operator.py`, matched L1 displacement) and **ORACLE** (upper bound —
shrinks toward the true per-draw `x*_{alpha_s}`, matched L1 displacement).

---

## 1. PRIMARY null (information-fair), aggregated across `K=20` draws

**Pooled (n=85 traces per draw):**

| Statistic | mean | median | min | max | sd |
|---|---|---|---|---|---|
| mean Δpayoff_real | 0.007234 | 0.007253 | 0.005916 | 0.008746 | 0.000689 |
| mean Δpayoff_null | 0.021673 | 0.020452 | 0.017501 | 0.026749 | 0.003159 |
| Wilcoxon p | 1.24e-05 | 6.02e-07 | 4.74e-09 | 1.01e-04 | 2.96e-05 |
| paired t-test t | -3.244 | -3.239 | -4.732 | -1.979 | 0.852 |
| paired t-test p | 0.01069 | 0.00177 | 8.90e-06 | 0.05106 | 0.01701 |
| win rate (null > real) | 0.7076 | 0.7118 | 0.6235 | 0.7765 | 0.0415 |
| n (null > real) | 60.15 | 60.5 | 53 | 66 | 3.53 |
| n (real > null) | 24.85 | 24.5 | 19 | 32 | 3.53 |
| partial r (dose vs real \| null) | 0.3689 | 0.4092 | -0.0862 | 0.6992 | 0.2271 |
| partial r p-value | 0.0672 | 1.18e-04 | 1.39e-13 | 0.5242 | 0.1464 |
| Pearson r (dose vs real, unconditional) | 0.6555 | 0.6737 | 0.3915 | 0.8436 | 0.1306 |

**Significance counts across the 20 draws:** Wilcoxon p<0.05 in **20/20** draws (pooled).
Partial-correlation p<0.05 in **14/20** draws (pooled).

**Per-model breakdown, aggregated across `K=20` draws:**

| Model | n | mean Δpayoff_real | mean Δpayoff_null | Wilcoxon p (mean/median) | paired t p (mean/median) | win rate (null>real) | draws with Wilcoxon p<0.05 |
|---|---|---|---|---|---|---|---|
| llama3.2:3b | 25 | 0.002764 | 0.009061 | 0.03409 / 0.00615 | 0.02785 / 0.01215 | 0.678 | 16/20 |
| qwen2.5:1.5b | 60 | 0.009097 | 0.026929 | 1.58e-04 / 1.97e-05 | 0.01876 / 0.00711 | 0.720 | 20/20 |

---

## 2. ORACLE null (upper bound, uses privileged per-trace `alpha_s`), aggregated across `K=20` draws

**Pooled (n=85 traces per draw):**

| Statistic | mean | median | min | max | sd |
|---|---|---|---|---|---|
| mean Δpayoff_real | 0.007234 | 0.007253 | 0.005916 | 0.008746 | 0.000689 |
| mean Δpayoff_null | 0.022242 | 0.021104 | 0.017700 | 0.027656 | 0.003187 |
| Wilcoxon p | 1.35e-09 | 2.57e-10 | 1.62e-11 | 9.58e-09 | 2.78e-09 |
| paired t-test t | -3.458 | -3.478 | -5.121 | -2.101 | 0.930 |
| paired t-test p | 0.00762 | 0.00082 | 1.91e-06 | 0.03861 | 0.01252 |
| win rate (null > real) | 0.8035 | 0.8000 | 0.7294 | 0.8588 | 0.0308 |
| n (null > real) | 68.3 | 68 | 62 | 73 | 2.62 |
| n (real > null) | 16.7 | 17 | 12 | 23 | 2.62 |
| partial r (dose vs real \| null) | 0.3728 | 0.4226 | -0.0874 | 0.6951 | 0.2229 |
| partial r p-value | 0.0652 | 6.27e-05 | 2.20e-13 | 0.6072 | 0.1592 |
| Pearson r (dose vs real, unconditional) | 0.6555 | 0.6737 | 0.3915 | 0.8436 | 0.1306 |

(`mean Δpayoff_real` and `Pearson r (dose vs real)` are identical to §1 — the real repair does not
change between the primary and oracle comparisons, only the null does.)

**Significance counts across the 20 draws:** Wilcoxon p<0.05 in **20/20** draws (pooled).
Partial-correlation p<0.05 in **15/20** draws (pooled).

**Per-model breakdown, aggregated across `K=20` draws:**

| Model | n | mean Δpayoff_real | mean Δpayoff_null | Wilcoxon p (mean/median) | paired t p (mean/median) | win rate (null>real) | draws with Wilcoxon p<0.05 |
|---|---|---|---|---|---|---|---|
| llama3.2:3b | 25 | 0.002764 | 0.009848 | 8.08e-04 / 3.53e-04 | 0.00719 / 0.00454 | 0.782 | 20/20 |
| qwen2.5:1.5b | 60 | 0.009097 | 0.027406 | 3.79e-07 / 8.90e-08 | 0.01486 / 0.00497 | 0.8125 | 20/20 |

---

## 3. Correlations between real and null, across draws

```
Spearman(delta_payoff_real, delta_payoff_null_primary): mean 0.5739, median 0.5645, min 0.4715, max 0.6722
Spearman(delta_payoff_real, delta_payoff_null_oracle):  mean 0.5992, median 0.6031, min 0.4996, max 0.7058
Spearman(dose, delta_payoff_real):                       mean 0.5758, median 0.5895, min 0.4507, max 0.7130
```

---

## 4. Full per-draw table

`k` = draw index (seed `20_260_829_500_000 + k*1_000_000 + 1000*trace_index` per trace).

| k | primary mean_real | primary mean_null | primary Wilcoxon p | oracle mean_null | oracle Wilcoxon p |
|---|---|---|---|---|---|
| 0 | 0.00804 | 0.01956 | 9.036e-05 | 0.02091 | 3.174e-10 |
| 1 | 0.00732 | 0.02635 | 3.510e-07 | 0.02703 | 8.428e-10 |
| 2 | 0.00751 | 0.02026 | 9.970e-07 | 0.02098 | 1.539e-09 |
| 3 | 0.00705 | 0.01963 | 2.782e-07 | 0.01973 | 1.850e-10 |
| 4 | 0.00755 | 0.02108 | 8.896e-08 | 0.02190 | 1.135e-10 |
| 5 | 0.00737 | 0.01968 | 2.446e-06 | 0.02044 | 1.959e-10 |
| 6 | 0.00719 | 0.02046 | 2.149e-06 | 0.02104 | 4.704e-10 |
| 7 | 0.00761 | 0.02465 | 1.217e-06 | 0.02494 | 1.011e-10 |
| 8 | 0.00672 | 0.02556 | 1.371e-07 | 0.02597 | 5.983e-11 |
| 9 | 0.00705 | 0.02476 | 7.925e-06 | 0.02530 | 9.101e-09 |
| 10 | 0.00680 | 0.02044 | 8.527e-07 | 0.02117 | 5.260e-10 |
| 11 | 0.00825 | 0.02675 | 4.822e-06 | 0.02766 | 1.457e-09 |
| 12 | 0.00663 | 0.01866 | 4.735e-09 | 0.01899 | 4.871e-11 |
| 13 | 0.00788 | 0.02197 | 3.562e-05 | 0.02264 | 1.343e-09 |
| 14 | 0.00592 | 0.01778 | 1.686e-08 | 0.01851 | 1.617e-11 |
| 15 | 0.00875 | 0.02579 | 1.007e-04 | 0.02651 | 9.585e-09 |
| 16 | 0.00619 | 0.01750 | 4.484e-08 | 0.01770 | 3.962e-11 |
| 17 | 0.00738 | 0.01995 | 1.148e-08 | 0.01990 | 9.541e-11 |
| 18 | 0.00692 | 0.01753 | 2.938e-08 | 0.01823 | 2.774e-11 |
| 19 | 0.00657 | 0.02509 | 1.508e-07 | 0.02529 | 8.428e-10 |

Full per-trace, per-draw data (alphas, `delta_payoff_real`, `delta_payoff_null_fixed`,
`delta_payoff_null_oracle` for all 85 traces × 20 draws) is in `results/corrected_payoff.json`.
