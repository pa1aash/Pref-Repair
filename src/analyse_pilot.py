"""Analysis for the pilot. Computes only what docs/PILOT_PROTOCOL.md specifies."""
from __future__ import annotations
import json, sys
import numpy as np
sys.path.insert(0, "src")
from ccei import ccei, garp_holds, exact_tie_count, bronars, predictive_success
from budget_sets import make


def icc_model_as_subject(cells_by_model):
    """ICC(1,1) with MODEL as the subject and repeated sessions as the measurements.

    This is the correct analogue of the human-subjects reliability literature: there, subjects
    are people and the question is whether an individual's score is stable enough to tell people
    apart. Here subjects are models and the question is whether a model's score is stable enough
    to tell models apart against run-to-run noise — which is exactly what a graded dose axis
    requires. Splitting a single homogeneous cell into pseudo-groups would return ~0 by
    construction and would not measure reliability at all.

    Underpowered with few models; the count is reported alongside so the reader can discount it.
    """
    groups = [np.asarray(g) for g in cells_by_model if len(g) > 1]
    if len(groups) < 2:
        return float("nan"), len(groups)
    ns = [len(g) for g in groups]
    k = float(np.mean(ns))
    allv = np.concatenate(groups)
    grand = allv.mean()
    msb = sum(len(g) * (g.mean() - grand) ** 2 for g in groups) / (len(groups) - 1)
    msw = sum(((g - g.mean()) ** 2).sum() for g in groups) / (len(allv) - len(groups))
    denom = msb + (k - 1) * msw
    if denom == 0:
        return float("nan"), len(groups)
    return (msb - msw) / denom, len(groups)


def main():
    recs = json.load(open("results/pilot_raw.json"))
    MN, p_all, inc = make()
    rows = []
    for r in recs:
        if "p" not in r:
            continue
        p = np.array(r["p"]); x = np.array(r["x"])
        if len(p) < 20:                      # protocol: <20 valid rounds -> discard
            continue
        rows.append({"model": r["model"], "condition": r["condition"], "seed": r["seed"],
                     "n_valid": r["n_valid"], "ccei": ccei(p, x),
                     "garp": garp_holds(p, x), "ties": exact_tie_count(p, x),
                     "wall": r.get("wall_s")})
    json.dump(rows, open("results/pilot_ccei.json", "w"), indent=1)

    pw, mrc = bronars(p_all, inc, n=2000, seed=1)
    print(f"Bronars power {pw:.4f} | mean random-agent CCEI {mrc:.4f}\n")

    hdr = f"{'model':<30} {'cond':<11} {'n':>3} {'mean':>7} {'sd':>7} {'wscv':>7} {'min':>7} {'max':>7} {'pass':>6} {'m':>7}"
    print(hdr); print("-" * len(hdr))
    cells = {}
    for model in sorted({r["model"] for r in rows}):
        for cond in ["baseline", "reciprocal"]:
            sel = [r for r in rows if r["model"] == model and r["condition"] == cond]
            if not sel: continue
            c = np.array([r["ccei"] for r in sel])
            cells[(model, cond)] = c
            passr = float(np.mean([r["garp"] for r in sel]))
            wscv = c.std(ddof=1) / c.mean() if c.mean() else float("nan")
            print(f"{model:<30} {cond:<11} {len(c):>3} {c.mean():>7.4f} {c.std(ddof=1):>7.4f} "
                  f"{wscv:>7.4f} {c.min():>7.4f} {c.max():>7.4f} {passr:>6.2f} "
                  f"{predictive_success(passr, pw):>7.4f}")

    print("\n=== PRECONDITION 1 — test-retest reliability (same model, SAME format) ===")
    print("Nitsch human comparison band: ICC 0.071-0.685 (none reaching 0.75); WSCV ~15% for CCEI\n")
    out = {}
    per_model = []
    for model in sorted({r["model"] for r in rows}):
        c = cells.get((model, "baseline"))
        if c is None or len(c) < 3:
            continue
        per_model.append(c)
        wscv = c.std(ddof=1) / c.mean()
        print(f"{model}")
        print(f"   n={len(c)}  mean={c.mean():.4f}  sd={c.std(ddof=1):.4f}  "
              f"WSCV={wscv:.4f}  range=[{c.min():.4f}, {c.max():.4f}]")
        out[model] = {"n": len(c), "mean": float(c.mean()), "sd": float(c.std(ddof=1)),
                      "wscv": float(wscv), "min": float(c.min()), "max": float(c.max())}
    icc, ng = icc_model_as_subject(per_model)
    print(f"\n   ICC(1,1), model-as-subject, {ng} models, baseline format: {icc:.4f}")
    print("   (between-model variance share; can run-to-run noise be separated from model identity?)")
    out["_icc_model_as_subject"] = float(icc) if icc == icc else None
    out["_n_models"] = ng

    print("\n=== PRECONDITION 2 — format sensitivity (same model, DIFFERENT format) ===")
    for model in sorted({r["model"] for r in rows}):
        b = cells.get((model, "baseline")); rc = cells.get((model, "reciprocal"))
        if b is None or rc is None: continue
        try:
            from scipy import stats
            t, pv = stats.ttest_ind(b, rc, equal_var=False)
            pvs = f"p={pv:.2ele}".replace("ele", "e") if pv < 1e-3 else f"p={pv:.4f}"
        except Exception:
            pvs = "p=n/a"
        print(f"{model}")
        print(f"   baseline   mean={b.mean():.4f} sd={b.std(ddof=1):.4f} n={len(b)}")
        print(f"   reciprocal mean={rc.mean():.4f} sd={rc.std(ddof=1):.4f} n={len(rc)}")
        print(f"   delta = {rc.mean()-b.mean():+.4f}   {pvs}")
    json.dump(out, open("results/pilot_reliability.json", "w"), indent=1, default=float)


if __name__ == "__main__":
    main()
