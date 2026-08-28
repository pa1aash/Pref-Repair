"""Null-operator control, per docs/NULL_OPERATOR_METHOD.md.

For every GARP-violating, successfully-projected trace in results/main_ccei.json, builds a
GARP-blind "null" repair that shrinks every bundle toward the exogenous Cobb-Douglas center
x*_t by a single shared lambda per trace, chosen so the null's total L1 displacement matches
the real projection's dose_l1 (clipped at lambda=1, i.e. full re-centering, if dose_l1 exceeds
the distance to full re-centering). Scores the null repair with the same payoff.mean_payoff used
for the real repair, then compares delta_payoff_real vs delta_payoff_null.

Reconstructs each trace's (p, x, incomes) from results/main_raw.json using the exact same
"first attempt with n_valid >= 20" rule src/analyse_main.py uses, and cross-checks the
reconstructed raw_payoff against the value already stored in results/main_ccei.json as a
correctness guard on the reconstruction.
"""
from __future__ import annotations
import json, sys
from collections import defaultdict
import numpy as np
from scipy import stats
sys.path.insert(0, "src")
from payoff import mean_payoff, cd_optimal_bundle

RAW_PATH = "results/main_raw.json"
CCEI_PATH = "results/main_ccei.json"
OUT_PATH = "results/null_operator.json"


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


def main():
    kept = load_kept_traces()
    ccei_rows = json.load(open(CCEI_PATH))
    violating = [r for r in ccei_rows if r.get("dose_l1", 0.0) > 0.0]

    results = []
    recon_mismatches = []
    clipped = []

    for row in violating:
        slot = (row["model"], row["condition"], row["replicate"])
        if slot not in kept:
            raise RuntimeError(f"no reconstructed trace for {slot}")
        p, x, incomes = kept[slot]

        raw_payoff_recon = mean_payoff(x, p, incomes)
        if abs(raw_payoff_recon - row["raw_payoff"]) > 1e-6:
            recon_mismatches.append((slot, raw_payoff_recon, row["raw_payoff"]))

        x_star = cd_optimal_bundle(p, incomes, alpha=0.5)
        d_center = float(np.abs(x_star - x).sum())
        dose_real = row["dose_l1"]

        if d_center <= 0.0:
            lam = 0.0
        else:
            lam = dose_real / d_center
        lam_clipped = min(lam, 1.0)
        if lam > 1.0:
            clipped.append({"slot": slot, "dose_real": dose_real, "d_center": d_center})

        x_null = x + lam_clipped * (x_star - x)
        dose_null = lam_clipped * d_center

        null_payoff = mean_payoff(x_null, p, incomes)
        delta_payoff_null = null_payoff - raw_payoff_recon

        results.append({
            "model": row["model"], "condition": row["condition"], "replicate": row["replicate"],
            "dose_real": dose_real, "d_center": d_center, "lambda": lam_clipped,
            "dose_null": dose_null,
            "raw_payoff": raw_payoff_recon,
            "delta_payoff_real": row["delta_payoff"],
            "delta_payoff_null": delta_payoff_null,
        })

    if recon_mismatches:
        print(f"WARNING: {len(recon_mismatches)} reconstruction mismatches (raw_payoff):")
        for m in recon_mismatches[:10]:
            print("  ", m)
    else:
        print(f"Reconstruction check OK: all {len(results)} traces' raw_payoff matched "
              f"results/main_ccei.json to 1e-6.")

    print(f"lambda clipped at 1.0 (dose_real > d_center) for {len(clipped)}/{len(results)} traces.")
    for c in clipped:
        print("  ", c)

    dose = np.array([r["dose_real"] for r in results])
    dpay_real = np.array([r["delta_payoff_real"] for r in results])
    dpay_null = np.array([r["delta_payoff_null"] for r in results])
    n = len(results)

    wil_stat, wil_p = stats.wilcoxon(dpay_real, dpay_null)
    t_stat, t_p = stats.ttest_rel(dpay_real, dpay_null)

    rho_dose_null, p_dose_null = stats.spearmanr(dose, dpay_null)
    r_dose_null, pr_dose_null = stats.pearsonr(dose, dpay_null)

    rho_real_null, p_real_null = stats.spearmanr(dpay_real, dpay_null)
    r_real_null, pr_real_null = stats.pearsonr(dpay_real, dpay_null)

    r_dose_real, _ = stats.pearsonr(dose, dpay_real)

    # partial correlation: dose vs delta_payoff_real | delta_payoff_null
    r_xy = r_dose_real
    r_xz = r_dose_null
    r_yz = r_real_null
    denom = np.sqrt((1 - r_xz**2) * (1 - r_yz**2))
    partial_r = (r_xy - r_xz * r_yz) / denom
    # t-stat for partial correlation, df = n - 3 (one predictor partialled out)
    df = n - 3
    t_partial = partial_r * np.sqrt(df / (1 - partial_r**2))
    p_partial = 2 * (1 - stats.t.cdf(abs(t_partial), df))

    # OLS: delta_payoff_real ~ dose + delta_payoff_null  (with intercept)
    X = np.column_stack([np.ones(n), dose, dpay_null])
    beta, _, _, _ = np.linalg.lstsq(X, dpay_real, rcond=None)
    resid = dpay_real - X @ beta
    dof = n - X.shape[1]
    sigma2 = (resid @ resid) / dof
    cov_beta = sigma2 * np.linalg.inv(X.T @ X)
    se = np.sqrt(np.diag(cov_beta))
    t_beta = beta / se
    p_beta = 2 * (1 - stats.t.cdf(np.abs(t_beta), dof))

    summary = {
        "n": n,
        "mean_delta_payoff_real": float(dpay_real.mean()),
        "sd_delta_payoff_real": float(dpay_real.std(ddof=1)),
        "mean_delta_payoff_null": float(dpay_null.mean()),
        "sd_delta_payoff_null": float(dpay_null.std(ddof=1)),
        "mean_dose_real": float(dose.mean()),
        "mean_dose_null": float(np.array([r["dose_null"] for r in results]).mean()),
        "n_clipped_lambda": len(clipped),
        "paired_wilcoxon_stat": float(wil_stat), "paired_wilcoxon_p": float(wil_p),
        "paired_ttest_t": float(t_stat), "paired_ttest_p": float(t_p),
        "spearman_dose_vs_null": float(rho_dose_null), "p_spearman_dose_vs_null": float(p_dose_null),
        "pearson_dose_vs_null": float(r_dose_null), "p_pearson_dose_vs_null": float(pr_dose_null),
        "spearman_real_vs_null": float(rho_real_null), "p_spearman_real_vs_null": float(p_real_null),
        "pearson_real_vs_null": float(r_real_null), "p_pearson_real_vs_null": float(pr_real_null),
        "pearson_dose_vs_real_unconditional": float(r_dose_real),
        "partial_r_dose_vs_real_given_null": float(partial_r),
        "partial_r_t": float(t_partial), "partial_r_df": int(df), "partial_r_p": float(p_partial),
        "ols_intercept": float(beta[0]), "ols_dose_coef": float(beta[1]),
        "ols_dose_t": float(t_beta[1]), "ols_dose_p": float(p_beta[1]),
        "ols_null_coef": float(beta[2]), "ols_null_t": float(t_beta[2]), "ols_null_p": float(p_beta[2]),
        "reconstruction_mismatches": len(recon_mismatches),
    }

    json.dump({"summary": summary, "traces": results}, open(OUT_PATH, "w"), indent=1, default=float)

    print("\n=== Null-operator control summary ===")
    for k, v in summary.items():
        print(f"  {k}: {v}")
    print(f"\nWrote {OUT_PATH}")


if __name__ == "__main__":
    main()
