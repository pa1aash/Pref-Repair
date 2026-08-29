"""Corrected payoff (per-trace random Cobb-Douglas weight), per docs/CORRECTED_PAYOFF_DESIGN.md.

Implements the design exactly as frozen:
  - alpha_s ~ Uniform(0.05, 0.95), drawn i.i.d. per (model, condition, replicate) slot, from an
    RNG stream independent of the budget-set seed family and never read by projection.py or the
    null-operator construction (design doc S1, S5).
  - payoff_s(x_t) = [s^alpha_s (1-s)^(1-alpha_s)] / [alpha_s^alpha_s (1-alpha_s)^(1-alpha_s)],
    i.e. src/payoff.py's existing mean_payoff/cd_optimal_bundle called with alpha=alpha_s instead
    of the hardcoded 0.5. No changes to payoff.py itself (design doc S1, S4).
  - Two null constructions, per design doc S6, kept separate throughout:
      PRIMARY (information-fair): shrink toward the FIXED (0.5,0.5) target, matched L1
      displacement -- identical construction to src/null_operator.py's null, rescored under alpha_s.
      ORACLE (upper bound): shrink toward the TRUE per-trace x*_alpha_s, matched L1 displacement.
  - K=20 independent draws of the whole alpha_s vector (85 traces), per the operator's Part-2
    instruction, to characterise sampling variability from the random target itself.

Re-runs src/projection.py's project() on the same 85 GARP-violating traces from
results/main_ccei.json to recover x_tilde_real, which was not stored previously -- verifies the
reproduced dose_l1 matches the stored value as a correctness check.

Seed formula, stated explicitly because the design doc's suggested formula
(`20260829_500_000 + 1000*replicate_index`) is ambiguous once multiple models/conditions and
multiple draws are involved (replicate_index alone is not unique across the 85 traces, and K=20
draws need distinct streams). Resolved as:
    trace_index  = position of (model, condition, replicate) in the sorted list of all 85 traces
    seed(k, idx) = 20_260_829_500_000 + k * 1_000_000 + 1000 * trace_index
This is a necessary concretisation of the design doc's formula, not a substantive change to it --
noted here rather than silently resolved, per the operator's instruction to report rather than
improvise around anything ambiguous in the frozen design.
"""
from __future__ import annotations
import json, sys
from collections import defaultdict
import numpy as np
from scipy import stats
sys.path.insert(0, "src")
from payoff import mean_payoff, cd_optimal_bundle
from projection import project

RAW_PATH = "results/main_raw.json"
CCEI_PATH = "results/main_ccei.json"
OUT_PATH = "results/corrected_payoff.json"

ALPHA_LO, ALPHA_HI = 0.05, 0.95
K_DRAWS = 20
SEED_BASE = 20_260_829_500_000


def load_kept_traces():
    recs = json.load(open(RAW_PATH))
    by_slot = defaultdict(list)
    for r in recs:
        by_slot[(r["model"], r["condition"], r["replicate"])].append(r)
    kept = {}
    for slot, attempts in by_slot.items():
        attempts_sorted = sorted(attempts, key=lambda a: a.get("attempt", 1))
        rec = next((a for a in attempts_sorted if a.get("n_valid", 0) >= 20), None)
        if rec is None:
            continue
        p = np.array(rec["p"], dtype=float)
        x = np.array(rec["x"], dtype=float)
        incomes = np.einsum("ij,ij->i", p, x)
        kept[slot] = (p, x, incomes)
    return kept


def paired_stats(dpay_real, dpay_null, dose):
    n = len(dpay_real)
    wil_stat, wil_p = stats.wilcoxon(dpay_real, dpay_null)
    t_stat, t_p = stats.ttest_rel(dpay_real, dpay_null)
    r_dose_real, _ = stats.pearsonr(dose, dpay_real)
    r_dose_null, _ = stats.pearsonr(dose, dpay_null)
    r_real_null, _ = stats.pearsonr(dpay_real, dpay_null)
    denom = np.sqrt((1 - r_dose_null**2) * (1 - r_real_null**2))
    partial_r = (r_dose_real - r_dose_null * r_real_null) / denom if denom > 0 else float("nan")
    df = n - 3
    if abs(partial_r) < 1.0:
        t_partial = partial_r * np.sqrt(df / (1 - partial_r**2))
        p_partial = 2 * (1 - stats.t.cdf(abs(t_partial), df))
    else:
        t_partial, p_partial = float("inf"), 0.0
    n_null_gt_real = int((dpay_null > dpay_real).sum())
    return {
        "n": n,
        "mean_delta_payoff_real": float(dpay_real.mean()),
        "mean_delta_payoff_null": float(dpay_null.mean()),
        "sd_delta_payoff_real": float(dpay_real.std(ddof=1)),
        "sd_delta_payoff_null": float(dpay_null.std(ddof=1)),
        "wilcoxon_p": float(wil_p), "wilcoxon_stat": float(wil_stat),
        "paired_t": float(t_stat), "paired_t_p": float(t_p),
        "pearson_dose_vs_real": float(r_dose_real),
        "pearson_dose_vs_null": float(r_dose_null),
        "pearson_real_vs_null": float(r_real_null),
        "partial_r_dose_vs_real_given_null": float(partial_r),
        "partial_r_p": float(p_partial), "partial_r_df": int(df),
        "n_null_gt_real": n_null_gt_real, "n_real_gt_null": n - n_null_gt_real,
        "win_rate_null": n_null_gt_real / n,
    }


def main():
    kept = load_kept_traces()
    ccei_rows = json.load(open(CCEI_PATH))
    violating = sorted(
        [r for r in ccei_rows if r.get("dose_l1", 0.0) > 0.0],
        key=lambda r: (r["model"], r["condition"], r["replicate"]),
    )
    n_traces = len(violating)
    print(f"{n_traces} GARP-violating traces loaded from {CCEI_PATH}.")

    # --- Reconstruct x, p, incomes and re-run the real projection to get x_tilde_real ---
    traces = []
    dose_mismatches = []
    for idx, row in enumerate(violating):
        slot = (row["model"], row["condition"], row["replicate"])
        p, x, incomes = kept[slot]
        x_tilde, dose_l1, dose_linf, info = project(p, x, incomes, time_limit=30.0)
        if x_tilde is None:
            # Re-solve compute-budget retry only (not a design change): the original run
            # (docs/MAIN_EXPERIMENT_RESULTS.md) solved every trace within a 30s budget; a
            # re-solve hitting the time limit here reflects transient machine load, not a
            # different optimization problem. Retried once at 4x the original budget.
            print(f"  retry with time_limit=120s for {slot} (30s solve failed: {info.get('message')})")
            x_tilde, dose_l1, dose_linf, info = project(p, x, incomes, time_limit=120.0)
        if x_tilde is None:
            raise RuntimeError(f"projection failed to re-solve for {slot} even at 120s: {info}")
        if abs(dose_l1 - row["dose_l1"]) > 1e-3:
            dose_mismatches.append((slot, dose_l1, row["dose_l1"]))
        x_star_fixed = cd_optimal_bundle(p, incomes, alpha=0.5)
        d_center_fixed = float(np.abs(x_star_fixed - x).sum())
        traces.append({
            "idx": idx, "model": row["model"], "condition": row["condition"],
            "replicate": row["replicate"], "p": p, "x": x, "incomes": incomes,
            "x_tilde_real": x_tilde, "dose_real": dose_l1,
            "dose_real_stored": row["dose_l1"],
            "x_star_fixed": x_star_fixed, "d_center_fixed": d_center_fixed,
        })

    if dose_mismatches:
        print(f"WARNING: {len(dose_mismatches)} dose_l1 mismatches on re-solve (tol 1e-3):")
        for m in dose_mismatches:
            print("  ", m)
    else:
        print(f"Re-solved projection check OK: all {n_traces} traces' dose_l1 matched "
              f"results/main_ccei.json to 1e-3.")

    # PRIMARY null bundle (fixed 0.5/0.5 center, matched L1) -- does not depend on alpha_s,
    # so constructed once, outside the K-draw loop.
    for tr in traces:
        lam = min(tr["dose_real"] / tr["d_center_fixed"], 1.0) if tr["d_center_fixed"] > 0 else 0.0
        tr["lambda_fixed"] = lam
        tr["x_null_fixed"] = tr["x"] + lam * (tr["x_star_fixed"] - tr["x"])

    dose = np.array([tr["dose_real"] for tr in traces])
    models = np.array([tr["model"] for tr in traces])

    draws = []
    for k in range(K_DRAWS):
        alphas = np.empty(n_traces)
        for tr in traces:
            seed = SEED_BASE + k * 1_000_000 + 1000 * tr["idx"]
            rng = np.random.default_rng(seed)
            alphas[tr["idx"]] = rng.uniform(ALPHA_LO, ALPHA_HI)

        raw_new = np.empty(n_traces)
        real_new = np.empty(n_traces)
        null_fixed_new = np.empty(n_traces)
        null_oracle_new = np.empty(n_traces)
        lambda_oracle = np.empty(n_traces)

        for tr in traces:
            i = tr["idx"]
            a = alphas[i]
            p, x, incomes = tr["p"], tr["x"], tr["incomes"]
            raw_new[i] = mean_payoff(x, p, incomes, alpha=a)
            real_new[i] = mean_payoff(tr["x_tilde_real"], p, incomes, alpha=a)
            null_fixed_new[i] = mean_payoff(tr["x_null_fixed"], p, incomes, alpha=a)

            x_star_a = cd_optimal_bundle(p, incomes, alpha=a)
            d_center_a = float(np.abs(x_star_a - x).sum())
            lam_a = min(tr["dose_real"] / d_center_a, 1.0) if d_center_a > 0 else 0.0
            lambda_oracle[i] = lam_a
            x_null_oracle = x + lam_a * (x_star_a - x)
            null_oracle_new[i] = mean_payoff(x_null_oracle, p, incomes, alpha=a)

        dpay_real = real_new - raw_new
        dpay_null_fixed = null_fixed_new - raw_new
        dpay_null_oracle = null_oracle_new - raw_new

        draw_result = {
            "draw": k,
            "alphas": alphas.tolist(),
            "delta_payoff_real": dpay_real.tolist(),
            "delta_payoff_null_fixed": dpay_null_fixed.tolist(),
            "delta_payoff_null_oracle": dpay_null_oracle.tolist(),
            "primary": paired_stats(dpay_real, dpay_null_fixed, dose),
            "oracle": paired_stats(dpay_real, dpay_null_oracle, dose),
        }
        # per-model breakdown, primary null
        for m in sorted(set(models)):
            mask = models == m
            draw_result[f"primary_{m}"] = paired_stats(dpay_real[mask], dpay_null_fixed[mask], dose[mask])
            draw_result[f"oracle_{m}"] = paired_stats(dpay_real[mask], dpay_null_oracle[mask], dose[mask])
        draws.append(draw_result)
        print(f"draw {k}: primary mean_real={draw_result['primary']['mean_delta_payoff_real']:.5f} "
              f"mean_null={draw_result['primary']['mean_delta_payoff_null']:.5f} "
              f"wilcoxon_p={draw_result['primary']['wilcoxon_p']:.4g} "
              f"| oracle mean_null={draw_result['oracle']['mean_delta_payoff_null']:.5f} "
              f"wilcoxon_p={draw_result['oracle']['wilcoxon_p']:.4g}")

    json.dump({
        "n_traces": n_traces, "k_draws": K_DRAWS,
        "alpha_lo": ALPHA_LO, "alpha_hi": ALPHA_HI, "seed_base": SEED_BASE,
        "dose_mismatches": len(dose_mismatches),
        "draws": draws,
    }, open(OUT_PATH, "w"), indent=1, default=float)
    print(f"\nWrote {OUT_PATH}")


if __name__ == "__main__":
    main()
