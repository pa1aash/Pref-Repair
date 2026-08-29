"""Scratch script for stats-robustness pass §2C: per-cell Bronars power breakdown (Task 1),
uninformative-power assessment (Task 2), and conditional Beatty-Crawford-style bounded-perturbation
alternative power (Task 3, only if triggered). Pure computation, no interpretation.

Run: ./.venv/bin/python3 results/scratch_bronars_2c.py
"""
from __future__ import annotations
import json, sys
from collections import defaultdict
import numpy as np

sys.path.insert(0, "src")
from ccei import bronars, garp_holds, ccei as ccei_fn

CCEI_PATH = "results/main_ccei.json"
RAW_PATH = "results/main_raw.json"

CELL_ORDER = [
    ("llama3.2:3b-instruct-q4_K_M", "baseline"),
    ("llama3.2:3b-instruct-q4_K_M", "reciprocal"),
    ("qwen2.5:1.5b-instruct-q4_K_M", "baseline"),
    ("qwen2.5:1.5b-instruct-q4_K_M", "multiturn"),
    ("qwen2.5:1.5b-instruct-q4_K_M", "reciprocal"),
]

DOC_TABLE = {
    ("llama3.2:3b-instruct-q4_K_M", "baseline"):    dict(mean=0.9997, min=0.9990),
    ("llama3.2:3b-instruct-q4_K_M", "reciprocal"):  dict(mean=0.9998, min=0.9990),
    ("qwen2.5:1.5b-instruct-q4_K_M", "baseline"):   dict(mean=0.9995, min=0.9980),
    ("qwen2.5:1.5b-instruct-q4_K_M", "multiturn"):  dict(mean=0.9997, min=0.9980),
    ("qwen2.5:1.5b-instruct-q4_K_M", "reciprocal"): dict(mean=0.9995, min=0.9980),
}


def load_ccei():
    return json.load(open(CCEI_PATH))


def load_raw_kept(ccei_rows):
    """Match each kept ccei row (model, condition, replicate, n_attempts_used) to its p/x in
    main_raw.json, since main_ccei.json does not persist p/x."""
    raw = json.load(open(RAW_PATH))
    by_key = {}
    for r in raw:
        key = (r["model"], r["condition"], r["replicate"], r.get("attempt", 1))
        by_key[key] = r

    out = []
    for row in ccei_rows:
        key = (row["model"], row["condition"], row["replicate"], row["n_attempts_used"])
        raw_row = by_key.get(key)
        if raw_row is None:
            raise KeyError(f"no raw match for {key}")
        out.append((row, raw_row))
    return out


# ---------------------------------------------------------------------------
# TASK 1: per-cell Bronars power breakdown from the already-computed per-trace field
# ---------------------------------------------------------------------------

def task1(ccei_rows):
    cells = defaultdict(list)
    for row in ccei_rows:
        cells[(row["model"], row["condition"])].append(row)

    table = {}
    for key in CELL_ORDER:
        rows = cells.get(key, [])
        powers = [r["bronars_power"] for r in rows]
        mean_rand_ccei = [r["mean_random_ccei"] for r in rows]
        table[key] = {
            "n": len(rows),
            "mean_power": float(np.mean(powers)) if powers else None,
            "min_power": float(np.min(powers)) if powers else None,
            "max_power": float(np.max(powers)) if powers else None,
            "mean_random_ccei": float(np.mean(mean_rand_ccei)) if mean_rand_ccei else None,
            "per_trace_power": [
                {"replicate": r["replicate"], "bronars_power": r["bronars_power"],
                 "mean_random_ccei": r["mean_random_ccei"]}
                for r in sorted(rows, key=lambda r: r["replicate"])
            ],
        }
    return table


def crosscheck(table):
    flags = []
    for key in CELL_ORDER:
        doc = DOC_TABLE[key]
        comp = table[key]
        mean_diff = abs(round(comp["mean_power"], 4) - doc["mean"])
        min_diff = abs(round(comp["min_power"], 4) - doc["min"])
        ok = mean_diff <= 1e-4 and min_diff <= 1e-4
        flags.append({
            "cell": key, "doc_mean": doc["mean"], "computed_mean": round(comp["mean_power"], 4),
            "doc_min": doc["min"], "computed_min": round(comp["min_power"], 4),
            "match": ok,
        })
    return flags


# ---------------------------------------------------------------------------
# TASK 2: uninformative-power assessment (mechanical threshold check on Task 1's numbers)
# ---------------------------------------------------------------------------

def task2(table):
    means = [table[k]["mean_power"] for k in CELL_ORDER]
    mins = [table[k]["min_power"] for k in CELL_ORDER]
    condition_met = all(m > 0.99 for m in means) and all(m > 0.98 for m in mins)
    return {
        "means": {str(k): v for k, v in zip(CELL_ORDER, means)},
        "mins": {str(k): v for k, v in zip(CELL_ORDER, mins)},
        "threshold_mean_gt": 0.99,
        "threshold_min_gt": 0.98,
        "condition_met": condition_met,
    }


# ---------------------------------------------------------------------------
# TASK 3 (conditional): Bronars-style power against a bounded-perturbation near-rational
# alternative, "in the spirit of" Beatty & Crawford's demanding-alternative framing.
#
# EXACT SIMULATION DESIGN (stated precisely, since this is NOT a verified reproduction of
# Beatty & Crawford 2011's own construction -- see report):
#
# For each simulated agent s = 1..n on a given trace's T budget lines (prices p_t, income m_t,
# K=2 goods):
#   1. Draw one Cobb-Douglas share alpha_s ~ Uniform(0.2, 0.8) ONCE per agent (shared across all
#      T budget lines for that agent) -- alpha_s is the agent's fixed "latent preference", making
#      the noiseless agent perfectly GARP-consistent (Cobb-Douglas utility is rationalizable by
#      construction, so a bounded perturbation is the only source of possible violations).
#   2. At each budget line t, the exact Cobb-Douglas-optimal bundle is
#         x*_t = (alpha_s * m_t / p_t1,  (1-alpha_s) * m_t / p_t2)
#      i.e. constant expenditure shares (alpha_s, 1-alpha_s).
#   3. Perturb: draw an L1-bounded noise vector on the SAME budget line (so the perturbed bundle
#      still lies on -- not off -- the budget hyperplane, matching how Bronars' own construction
#      also always exhausts the budget). Concretely: draw a noise fraction f_t ~ Uniform(0, eta)
#      per budget line (eta = the perturbation scale, see below), draw a random direction on the
#      1-D budget line (K=2 => the line is 1-dimensional, so "direction" is just a sign), and move
#      the expenditure share by +-f_t from alpha_s, clipped to [0.01, 0.99] to stay in the interior
#      of the simplex:
#         share_t = clip(alpha_s + sign_t * f_t, 0.01, 0.99),   sign_t ~ Uniform{-1,+1}
#         x_t = (share_t * m_t / p_t1, (1-share_t) * m_t / p_t2)
#   4. eta (perturbation scale) is swept over {0.05, 0.10, 0.20} expenditure-share units so the
#      reader can see how power degrades as the alternative gets "closer to rational" (smaller eta)
#      -- eta=0 would be the exactly-rational agent (by construction always GARP-consistent, power
#      = 0 trivially, so it's reported only as a sanity check).
#   5. Test GARP on {p_t, x_t} for each simulated agent; power = fraction of n=2000 simulated
#      agents that VIOLATE GARP. (Same statistic definition as Bronars power, different data-
#      generating process for the alternative agent.)
#
# This is a bounded, mixture-style near-rational alternative (rational base behavior + bounded
# noise), NOT the uniform-random-on-the-simplex alternative that ordinary Bronars power uses. It
# is deliberately harder to violate GARP under, so power against it is a more demanding test of
# whether these budget designs carry real information beyond "not literally uniform-random
# choice".
# ---------------------------------------------------------------------------

def near_rational_agent_bundles(p, incomes, rng, eta):
    """One simulated near-rational agent's bundles across all T budget lines.
    p: (T,2) prices, incomes: (T,) expenditures. Returns x: (T,2)."""
    T = p.shape[0]
    alpha = rng.uniform(0.2, 0.8)  # one alpha per agent, shared across all T budget lines
    f = rng.uniform(0.0, eta, size=T)          # per-line noise magnitude
    sign = rng.choice([-1.0, 1.0], size=T)     # per-line noise direction
    share = np.clip(alpha + sign * f, 0.01, 0.99)
    x = np.empty((T, 2))
    x[:, 0] = share * incomes / p[:, 0]
    x[:, 1] = (1.0 - share) * incomes / p[:, 1]
    return x


def beatty_crawford_style_power(p, incomes, n=2000, seed=0, eta=0.10):
    rng = np.random.default_rng(seed)
    viol = 0
    cs = np.empty(n)
    for r in range(n):
        xr = near_rational_agent_bundles(p, incomes, rng, eta)
        ok = garp_holds(p, xr, 1.0)
        viol += (not ok)
        cs[r] = 1.0 if ok else ccei_fn(p, xr)
    return viol / n, float(cs.mean())


def task3(matched, n=2000, etas=(0.05, 0.10, 0.20)):
    cells = defaultdict(list)
    for ccei_row, raw_row in matched:
        cells[(ccei_row["model"], ccei_row["condition"])].append((ccei_row, raw_row))

    table = {}
    for key in CELL_ORDER:
        rows = cells.get(key, [])
        by_eta = {}
        for eta in etas:
            powers = []
            for ccei_row, raw_row in rows:
                p = np.array(raw_row["p"], dtype=float)
                x = np.array(raw_row["x"], dtype=float)
                incomes = np.einsum("ij,ij->i", p, x)
                seed = ccei_row["replicate"]  # match the per-trace seeding convention used for bronars_power
                pw, mean_alt_ccei = beatty_crawford_style_power(p, incomes, n=n, seed=seed, eta=eta)
                powers.append(pw)
            by_eta[eta] = {
                "n_traces": len(rows),
                "mean_power": float(np.mean(powers)) if powers else None,
                "min_power": float(np.min(powers)) if powers else None,
                "max_power": float(np.max(powers)) if powers else None,
            }
        table[key] = by_eta
    return table


def main():
    ccei_rows = load_ccei()
    t1 = task1(ccei_rows)
    xchecks = crosscheck(t1)
    t2 = task2(t1)

    out = {
        "task1_per_cell": {f"{k[0]}|{k[1]}": v for k, v in t1.items()},
        "task1_crosscheck_vs_doc": [
            {**f, "cell": f"{f['cell'][0]}|{f['cell'][1]}"} for f in xchecks
        ],
        "task2_assessment": t2,
    }

    if t2["condition_met"]:
        print("Task 2 condition MET -> running conditional Task 3 (bounded-perturbation alternative power)...", file=sys.stderr)
        matched = load_raw_kept(ccei_rows)
        # n=1000 matches the per-trace bronars_power convention already used in main_ccei.json
        # (src/analyse_main.py calls bronars(..., n=1000, seed=r)); kept identical here for
        # like-for-like comparability against Task 1's numbers.
        t3 = task3(matched, n=1000, etas=(0.05, 0.10, 0.20))
        out["task3_beatty_crawford_style"] = {
            f"{k[0]}|{k[1]}": {str(eta): v for eta, v in by_eta.items()}
            for k, by_eta in t3.items()
        }
        out["task3_triggered"] = True
    else:
        out["task3_triggered"] = False

    json.dump(out, open("results/stats_2c_bronars.json", "w"), indent=2)
    print("wrote results/stats_2c_bronars.json", file=sys.stderr)

    # human-readable summary to stdout
    print("\n=== TASK 1: per-cell Bronars power (uniform-random alternative) ===")
    for key in CELL_ORDER:
        c = t1[key]
        print(f"{key[0]:32s} {key[1]:12s} n={c['n']:3d} mean={c['mean_power']:.4f} min={c['min_power']:.4f} max={c['max_power']:.4f} mean_rand_ccei={c['mean_random_ccei']:.4f}")

    print("\n=== crosscheck vs docs/MAIN_EXPERIMENT_RESULTS.md §0 ===")
    for f in xchecks:
        print(f"{f['cell']}: doc_mean={f['doc_mean']} computed_mean={f['computed_mean']} doc_min={f['doc_min']} computed_min={f['computed_min']} match={f['match']}")

    print("\n=== TASK 2 ===")
    print(json.dumps(t2, indent=2))

    if out["task3_triggered"]:
        print("\n=== TASK 3: bounded-perturbation ('Beatty-Crawford-style') alternative power ===")
        for key in CELL_ORDER:
            for eta in (0.05, 0.10, 0.20):
                c = out["task3_beatty_crawford_style"][f"{key[0]}|{key[1]}"][str(eta)]
                print(f"{key[0]:32s} {key[1]:12s} eta={eta:.2f} n={c['n_traces']:3d} mean={c['mean_power']:.4f} min={c['min_power']:.4f} max={c['max_power']:.4f}")


if __name__ == "__main__":
    main()
