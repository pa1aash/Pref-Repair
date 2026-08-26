"""Analysis for the main experiment, per docs/MAIN_EXPERIMENT_PROTOCOL.md.

For every (model, condition, replicate) slot: picks the first attempt with n_valid >= 20 (the
kept trace); computes CCEI, GARP pass/fail, and that replicate's OWN Bronars power (each
replicate has an independently-drawn budget set, unlike the pilot's single shared set); projects
GARP-violating traces via src/projection.py and records the L1 dose; scores both the raw and
projected sequence against the exogenous payoff in src/payoff.py. Reports first-attempt and
post-retry (residual) discard rates per condition, per C3's requirement.
"""
from __future__ import annotations
import json, sys, math
from collections import defaultdict
import numpy as np
from scipy import stats
sys.path.insert(0, "src")
from ccei import ccei as ccei_fn, garp_holds, exact_tie_count, bronars
from projection import project
from payoff import mean_payoff, payoff as payoff_fn

RAW_PATH = "results/main_raw.json"
CCEI_OUT = "results/main_ccei.json"
SUMMARY_OUT = "results/main_summary.json"


def load_slots():
    recs = json.load(open(RAW_PATH))
    by_slot = defaultdict(list)
    for r in recs:
        by_slot[(r["model"], r["condition"], r["replicate"])].append(r)
    return by_slot


def two_proportion_p(k1, n1, k2, n2):
    p1, p2 = k1 / n1, k2 / n2
    pbar = (k1 + k2) / (n1 + n2)
    se = math.sqrt(pbar * (1 - pbar) * (1 / n1 + 1 / n2))
    if se == 0:
        return float("nan")
    z = (p1 - p2) / se
    return 2 * (1 - stats.norm.cdf(abs(z)))


def wilson_ci(k, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    denom = 1 + z**2 / n
    center = (p + z**2 / (2 * n)) / denom
    half = (z * math.sqrt(p * (1 - p) / n + z**2 / (4 * n**2))) / denom
    return (max(0.0, center - half), min(1.0, center + half))


def main():
    by_slot = load_slots()
    rows = []
    discard_first = defaultdict(lambda: [0, 0])   # (model,cond) -> [n_discarded_first_attempt, n_total]
    discard_resid = defaultdict(lambda: [0, 0])   # (model,cond) -> [n_never_recovered, n_total]

    for (model, cond, r), attempts in sorted(by_slot.items()):
        attempts_sorted = sorted(attempts, key=lambda a: a.get("attempt", 1))
        first = attempts_sorted[0]
        discard_first[(model, cond)][1] += 1
        if first.get("n_valid", 0) < 20:
            discard_first[(model, cond)][0] += 1

        kept = next((a for a in attempts_sorted if a.get("n_valid", 0) >= 20), None)
        discard_resid[(model, cond)][1] += 1
        if kept is None:
            discard_resid[(model, cond)][0] += 1
            continue

        p = np.array(kept["p"]); x = np.array(kept["x"])
        incomes = np.einsum("ij,ij->i", p, x)
        c = ccei_fn(p, x)
        gh = garp_holds(p, x)
        ties = exact_tie_count(p, x)
        pw, mean_rand_ccei = bronars(p, incomes, n=1000, seed=r)

        row = {"model": model, "condition": cond, "replicate": r, "n_valid": kept["n_valid"],
               "n_attempts_used": kept.get("attempt", 1), "ccei": c, "garp": gh, "ties": ties,
               "bronars_power": pw, "mean_random_ccei": mean_rand_ccei,
               "raw_payoff": mean_payoff(x, p, incomes)}

        if not gh:
            xt, dose1, dosei, info = project(p, x, incomes, time_limit=30.0)
            if xt is not None:
                row["dose_l1"] = dose1
                row["dose_linf"] = dosei
                row["projection_verified"] = info.get("verified_garp_consistent")
                row["projection_gap"] = info.get("mip_gap")
                row["repaired_payoff"] = mean_payoff(xt, p, incomes)
                row["delta_payoff"] = row["repaired_payoff"] - row["raw_payoff"]
            else:
                row["projection_status"] = info.get("status")
        else:
            row["dose_l1"] = 0.0
            row["dose_linf"] = 0.0
            row["repaired_payoff"] = row["raw_payoff"]
            row["delta_payoff"] = 0.0

        rows.append(row)

    json.dump(rows, open(CCEI_OUT, "w"), indent=1, default=float)

    print(f"{'model':<30} {'cond':<11} {'n':>3} {'mean_ccei':>9} {'sd':>7} {'pass':>6} "
          f"{'mean_dose':>10} {'d_payoff':>9}")
    print("-" * 92)
    cells = defaultdict(list)
    for row in rows:
        cells[(row["model"], row["condition"])].append(row)

    summary = {}
    for (model, cond), rs in sorted(cells.items()):
        cceis = np.array([x["ccei"] for x in rs])
        passr = np.mean([x["garp"] for x in rs])
        doses = [x.get("dose_l1", 0.0) for x in rs]
        dpayoffs = [x.get("delta_payoff", 0.0) for x in rs]
        print(f"{model:<30} {cond:<11} {len(rs):>3} {cceis.mean():>9.4f} {cceis.std(ddof=1) if len(rs)>1 else 0:>7.4f} "
              f"{passr:>6.2f} {np.mean(doses):>10.3f} {np.mean(dpayoffs):>9.4f}")
        n_disc_f, n_tot_f = discard_first[(model, cond)]
        n_disc_r, n_tot_r = discard_resid[(model, cond)]
        summary[f"{model}|{cond}"] = {
            "n_kept": len(rs), "mean_ccei": float(cceis.mean()),
            "sd_ccei": float(cceis.std(ddof=1)) if len(rs) > 1 else None,
            "garp_pass_rate": float(passr), "mean_dose_l1": float(np.mean(doses)),
            "mean_delta_payoff": float(np.mean(dpayoffs)),
            "discard_rate_first_attempt": n_disc_f / n_tot_f if n_tot_f else None,
            "discard_rate_residual": n_disc_r / n_tot_r if n_tot_r else None,
            "n_slots_total": n_tot_r,
        }

    print("\n=== Discard rates (first-attempt vs. post-retry residual), per C3 ===")
    for (model, cond), (n_disc_f, n_tot_f) in sorted(discard_first.items()):
        n_disc_r, n_tot_r = discard_resid[(model, cond)]
        print(f"{model:<30} {cond:<11} first-attempt={n_disc_f}/{n_tot_f} "
              f"({n_disc_f/n_tot_f:.1%})   residual={n_disc_r}/{n_tot_r} ({n_disc_r/n_tot_r:.1%})")

    print("\n=== Confirmatory framing-effect tests ===")
    for model in sorted({r["model"] for r in rows}):
        b = cells.get((model, "baseline")); rc = cells.get((model, "reciprocal"))
        if not b or not rc:
            continue
        b_pass = sum(x["garp"] for x in b); rc_pass = sum(x["garp"] for x in rc)
        p_val = two_proportion_p(b_pass, len(b), rc_pass, len(rc))
        b_ccei = np.array([x["ccei"] for x in b]); rc_ccei = np.array([x["ccei"] for x in rc])
        t, tp = stats.ttest_ind(b_ccei, rc_ccei, equal_var=False)
        print(f"{model}")
        print(f"   GARP pass rate: baseline {b_pass}/{len(b)}={b_pass/len(b):.2f} vs "
              f"reciprocal {rc_pass}/{len(rc)}={rc_pass/len(rc):.2f}   p={p_val:.4g}")
        print(f"   CCEI: baseline {b_ccei.mean():.4f}±{b_ccei.std(ddof=1):.4f} vs "
              f"reciprocal {rc_ccei.mean():.4f}±{rc_ccei.std(ddof=1):.4f}   t-test p={tp:.4g}")
        summary[f"{model}|framing_test"] = {
            "garp_pass_p": float(p_val), "ccei_ttest_p": float(tp),
            "baseline_pass_rate": b_pass/len(b), "reciprocal_pass_rate": rc_pass/len(rc),
            "baseline_ccei_ci95": wilson_ci(b_pass, len(b)),
        }

    json.dump(summary, open(SUMMARY_OUT, "w"), indent=1, default=float)
    print(f"\nWrote {CCEI_OUT} and {SUMMARY_OUT}")


if __name__ == "__main__":
    main()
