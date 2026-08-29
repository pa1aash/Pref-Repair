"""Result-mechanism figure for S4.1 (the C1 null-operator control).

Illustrates, on one hand-verified exemplar trace, WHY a GARP-blind, size-matched null operator
outperforms the real GARP-restoring projection on the exogenous payoff -- under BOTH payoff
designs (the original fixed-centre Cobb-Douglas payoff of docs/MAIN_EXPERIMENT_PROTOCOL.md S5,
and the corrected per-trace-random-target payoff of docs/CORRECTED_PAYOFF_DESIGN.md S1).

Exemplar trace: qwen2.5:1.5b-instruct-q4_K_M, reciprocal framing, replicate 12 -- the single
largest-dose GARP violation in the 85-trace sample (dose_L1 = 111.637), and the same trace
docs/PAYOFF_AUDIT.md S3 hand-checked and docs/NULL_OPERATOR_RESULTS.md S1 singles out.

NO NUMBER IN THIS FIGURE IS ILLUSTRATIVE OR INVENTED. Everything is recomputed here from
results/main_raw.json by re-solving src/projection.py's MILP and re-running src/payoff.py, and
is checked against the stored values in results/main_ccei.json and results/corrected_payoff.json
before anything is plotted (see the assertions in load_exemplar()). The script aborts rather
than draw a figure if any check fails.

Because K=2 and every bundle exhausts its budget, the payoff is exactly a function of the
expenditure share s on good A alone (docs/NULL_OPERATOR_METHOD.md S2):

    original  : payoff(s)        = 2 * sqrt(s (1-s))                                 peak at s = 0.5
    corrected : payoff_alpha(s)  = s^a (1-s)^(1-a) / [a^a (1-a)^(1-a)]               peak at s = a

so both payoff surfaces can be drawn as 1-D curves and every bundle marked as a point on them.

Palette follows scripts/make_figures.py, colour assigned by entity and held fixed:
grey = raw (unrepaired) choice, blue = the real GARP projection, orange = the primary
(information-fair) null operator, aqua = the oracle null (upper bound, privileged information).
"""
from __future__ import annotations
import json
import sys
from collections import defaultdict

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, "src")
from payoff import mean_payoff, cd_optimal_bundle  # noqa: E402
from projection import project  # noqa: E402

BLUE = "#2a78d6"     # the real GARP-restoring projection
ORANGE = "#eb6834"   # the primary, information-fair null operator
AQUA = "#1baf7a"     # the oracle null (privileged information; upper bound only)
GREY = "#9b9a94"     # the raw, unrepaired choice
TEXT = "#1a1a1a"
MUTED = "#52514e"
RULE = "#c9c8c2"

plt.rcParams.update({
    "font.size": 11.5,
    "axes.edgecolor": RULE,
    "axes.labelcolor": TEXT,
    "text.color": TEXT,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "font.family": "DejaVu Sans",
})

# --- the exemplar trace, and the corrected payoff's draw index -----------------------------
SLOT = ("qwen2.5:1.5b-instruct-q4_K_M", "reciprocal", 12)
DRAW_K = 0                      # which of the K=20 corrected-payoff draws Panel B uses
SEED_BASE = 20_260_829_500_000  # src/corrected_payoff.py's seed formula, reproduced exactly
ALPHA_LO, ALPHA_HI = 0.05, 0.95


def payoff_share(s, alpha):
    """Payoff as an exact function of the expenditure share on good A (see module docstring)."""
    s = np.clip(s, 1e-12, 1 - 1e-12)
    return (s ** alpha * (1 - s) ** (1 - alpha)) / (alpha ** alpha * (1 - alpha) ** (1 - alpha))


def load_exemplar():
    """Rebuild (p, x, incomes), re-solve the real projection, rebuild both nulls, and check
    every recovered quantity against what is already stored in results/."""
    recs = json.load(open("results/main_raw.json"))
    by_slot = defaultdict(list)
    for r in recs:
        by_slot[(r["model"], r["condition"], r["replicate"])].append(r)
    # same "first attempt with n_valid >= 20" rule src/analyse_main.py uses
    attempts = sorted(by_slot[SLOT], key=lambda a: a.get("attempt", 1))
    rec = next(a for a in attempts if a.get("n_valid", 0) >= 20)
    p = np.array(rec["p"], dtype=float)
    x = np.array(rec["x"], dtype=float)
    incomes = np.einsum("ij,ij->i", p, x)

    ccei = json.load(open("results/main_ccei.json"))
    violating = sorted([r for r in ccei if r.get("dose_l1", 0.0) > 0.0],
                       key=lambda r: (r["model"], r["condition"], r["replicate"]))
    idx = next(i for i, r in enumerate(violating)
               if (r["model"], r["condition"], r["replicate"]) == SLOT)
    stored = violating[idx]

    x_tilde, dose, _, info = project(p, x, incomes, time_limit=120.0)
    assert x_tilde is not None and info["verified_garp_consistent"], info
    assert abs(dose - stored["dose_l1"]) < 1e-3, (dose, stored["dose_l1"])
    assert abs(mean_payoff(x, p, incomes) - stored["raw_payoff"]) < 1e-6
    assert abs(mean_payoff(x_tilde, p, incomes) - stored["repaired_payoff"]) < 1e-6

    # corrected payoff: alpha for this trace at draw k, via src/corrected_payoff.py's seed formula
    seed = SEED_BASE + DRAW_K * 1_000_000 + 1000 * idx
    alpha = float(np.random.default_rng(seed).uniform(ALPHA_LO, ALPHA_HI))
    cp = json.load(open("results/corrected_payoff.json"))["draws"][DRAW_K]
    assert abs(alpha - cp["alphas"][idx]) < 1e-12, (alpha, cp["alphas"][idx])

    # the two nulls, exactly as src/null_operator.py / src/corrected_payoff.py build them
    x_star_fix = cd_optimal_bundle(p, incomes, alpha=0.5)
    lam_fix = min(dose / float(np.abs(x_star_fix - x).sum()), 1.0)
    x_null_fix = x + lam_fix * (x_star_fix - x)

    x_star_or = cd_optimal_bundle(p, incomes, alpha=alpha)
    lam_or = min(dose / float(np.abs(x_star_or - x).sum()), 1.0)
    x_null_or = x + lam_or * (x_star_or - x)

    # cross-check every trace-level delta against results/corrected_payoff.json
    raw_a = mean_payoff(x, p, incomes, alpha=alpha)
    for key, bundle in [("delta_payoff_real", x_tilde),
                        ("delta_payoff_null_fixed", x_null_fix),
                        ("delta_payoff_null_oracle", x_null_or)]:
        got = mean_payoff(bundle, p, incomes, alpha=alpha) - raw_a
        assert abs(got - cp[key][idx]) < 1e-9, (key, got, cp[key][idx])

    share = lambda b: p[:, 0] * b[:, 0] / incomes  # noqa: E731
    return {
        "p": p, "x": x, "incomes": incomes, "x_tilde": x_tilde,
        "dose": dose, "alpha": alpha, "idx": idx, "T": p.shape[0],
        "lam_fix": lam_fix, "lam_or": lam_or,
        "s_raw": share(x), "s_real": share(x_tilde),
        "s_nullfix": share(x_null_fix), "s_nullor": share(x_null_or),
        "disp_real": np.abs(x_tilde - x).sum(axis=1),
        "disp_null": np.abs(x_null_fix - x).sum(axis=1),
        # trace-level mean payoffs, both surfaces
        "A": {a: mean_payoff(b, p, incomes) for a, b in
              [("raw", x), ("real", x_tilde), ("nullfix", x_null_fix)]},
        "B": {a: mean_payoff(b, p, incomes, alpha=alpha) for a, b in
              [("raw", x), ("real", x_tilde), ("nullfix", x_null_fix), ("nullor", x_null_or)]},
    }


def draw_panel(ax, d, alpha, title, summary, show_oracle):
    """One payoff surface, with the two representative rounds marked on it."""
    ss = np.linspace(1e-4, 1 - 1e-4, 800)
    ax.plot(ss, payoff_share(ss, alpha), color=MUTED, linewidth=1.4, zorder=3)
    ax.axvline(alpha, color=RULE, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    ax.text(alpha, 0.22, f"peak\n$s={alpha:.3f}$", ha="center", va="center",
            fontsize=11.0, color=MUTED, zorder=6,
            bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.85))

    t_spend, t_idle = 3, 9   # the round the repair spends most on; a modal untouched round
    for t, marker, ms in [(t_spend, "o", 30), (t_idle, "s", 27)]:
        pts = [(d["s_raw"][t], GREY), (d["s_real"][t], BLUE), (d["s_nullfix"][t], ORANGE)]
        if show_oracle:
            pts.append((d["s_nullor"][t], AQUA))
        # on the idle round raw and repaired coincide exactly (the repair spends nothing
        # there), so the raw marker is drawn oversized to read as a ring around the blue one
        coincide = abs(d["s_raw"][t] - d["s_real"][t]) < 1e-9
        for s, col in pts:
            y = payoff_share(s, alpha)
            size = ms * (2.4 if (coincide and col is GREY) else 1.0)
            ax.plot([s, s], [0, y], color=col, linewidth=0.7, alpha=0.35, zorder=2)
            ax.scatter([s], [y], s=size, color=col, zorder=5,
                       edgecolors="white", linewidths=0.7, marker=marker)

    # round-3: the repair vaults almost to the peak; the null barely moves
    ax.annotate("", xy=(d["s_real"][t_spend], payoff_share(d["s_real"][t_spend], alpha)),
                xytext=(d["s_raw"][t_spend], payoff_share(d["s_raw"][t_spend], alpha)),
                arrowprops=dict(arrowstyle="-|>", color=BLUE, linewidth=1.0,
                                connectionstyle="arc3,rad=-0.22", shrinkA=4, shrinkB=4), zorder=4)
    # round-9: the repair does not move at all; the null does
    ax.annotate("", xy=(d["s_nullfix"][t_idle], payoff_share(d["s_nullfix"][t_idle], alpha)),
                xytext=(d["s_raw"][t_idle], payoff_share(d["s_raw"][t_idle], alpha)),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, linewidth=1.0,
                                connectionstyle="arc3,rad=-0.3", shrinkA=4, shrinkB=4), zorder=4)

    label_bbox = dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.82)
    ax.text(0.015, 0.02, "round 3\n(42% of budget)",
            fontsize=11.0, color=MUTED, ha="left", va="bottom", linespacing=1.2,
            zorder=6, bbox=label_bbox)
    ax.text(0.985, 0.02, "round 9\n(untouched)",
            fontsize=11.0, color=MUTED, ha="right", va="bottom", linespacing=1.2,
            zorder=6, bbox=label_bbox)
    ax.text(0.5, 0.58, summary, transform=ax.transAxes, ha="center", va="center",
            fontsize=11.0, color=TEXT, linespacing=1.3, zorder=6,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=RULE, linewidth=0.6, alpha=0.92))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.02)
    ax.set_xlabel("share on good A, $s$", fontsize=13.0)
    ax.set_title(title, fontsize=13.0, loc="left", color=TEXT, pad=6)
    ax.tick_params(axis="both", labelsize=11.0)


def main():
    d = load_exemplar()
    a = d["alpha"]
    T = d["T"]

    fig = plt.figure(figsize=(6.9, 5.4))
    gs = fig.add_gridspec(2, 2, height_ratios=[2.2, 1.3], hspace=1.05, wspace=0.30)
    axA = fig.add_subplot(gs[0, 0])
    axB = fig.add_subplot(gs[0, 1], sharey=axA)
    axC = fig.add_subplot(gs[1, :])

    draw_panel(axA, d, 0.5, "A. Original payoff",
               "trace mean $\\Delta$payoff\n"
               f"real repair {d['A']['real'] - d['A']['raw']:+.4f}\n"
               f"null operator {d['A']['nullfix'] - d['A']['raw']:+.4f}", show_oracle=False)
    draw_panel(axB, d, a, "B. Corrected payoff",
               "trace mean $\\Delta$payoff\n"
               f"real repair {d['B']['real'] - d['B']['raw']:+.4f}\n"
               f"null operator {d['B']['nullfix'] - d['B']['raw']:+.4f}\n"
               f"oracle null {d['B']['nullor'] - d['B']['raw']:+.4f}", show_oracle=True)
    axA.set_ylabel("exogenous payoff")
    plt.setp(axB.get_yticklabels(), visible=False)

    handles = [
        plt.Line2D([], [], marker="o", linestyle="", color=GREY, markersize=5.2,
                   markeredgecolor="white", label="raw"),
        plt.Line2D([], [], marker="o", linestyle="", color=BLUE, markersize=5.2,
                   markeredgecolor="white", label="GARP-repaired"),
        plt.Line2D([], [], marker="o", linestyle="", color=ORANGE, markersize=5.2,
                   markeredgecolor="white", label="null (matched, GARP-blind)"),
        plt.Line2D([], [], marker="o", linestyle="", color=AQUA, markersize=5.2,
                   markeredgecolor="white", label="oracle null (B only)"),
    ]
    fig.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.52, 0.015), ncol=4,
               frameon=False, fontsize=11.0, handletextpad=0.25, columnspacing=0.9)

    # --- Panel C: where each operator spends its identical L1 budget ---------------------
    ts = np.arange(T)
    w = 0.42
    axC.bar(ts - w / 2, d["disp_real"], width=w, color=BLUE, zorder=3,
            label="real GARP projection")
    axC.bar(ts + w / 2, d["disp_null"], width=w, color=ORANGE, zorder=3,
            label="null operator")
    axC.set_xticks(ts[::2])
    axC.set_xticklabels([str(t) for t in ts[::2]], fontsize=11.0)
    axC.set_xlim(-0.8, T - 0.2)
    axC.set_xlabel("round $t$", fontsize=13.0)
    axC.set_ylabel("$\\|\\tilde{x}_t - x_t\\|_1$", fontsize=13.0)
    n_touched = int((d["disp_real"] > 1e-6).sum())
    axC.set_title(f"C. Where each operator spends its identical $L_1$ budget of {d['dose']:.1f}",
                  fontsize=13.0, loc="left", color=TEXT, pad=10)
    axC.legend(loc="upper right", frameon=False, fontsize=11.0, handlelength=1.2,
               borderaxespad=0.2, ncol=1, columnspacing=1.2)
    axC.set_ylim(0, float(d["disp_real"].max()) * 1.28)

    fig.suptitle("Why a GARP-blind null outperforms the real repair\n"
                 "(one illustrative trace, not a statistical result --- see caption)",
                 fontsize=12.5, y=1.0, color=MUTED)

    fig.savefig("figures/fig_mechanism_illustration.pdf", bbox_inches="tight")
    fig.savefig("figures/fig_mechanism_illustration.png", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("wrote figures/fig_mechanism_illustration.pdf and .png")

    # --- everything the caption asserts, printed for the record -------------------------
    print(f"\nexemplar: {SLOT}, trace_index={d['idx']}, T={T}, dose_L1={d['dose']:.5f}")
    print(f"alpha_s (draw k={DRAW_K}) = {a:.6f}; lambda_fixed = {d['lam_fix']:.6f}, "
          f"lambda_oracle = {d['lam_or']:.6f}")
    print("panel A (alpha=0.5) trace means: "
          f"raw {d['A']['raw']:.4f}, real {d['A']['real']:.4f}, null {d['A']['nullfix']:.4f}")
    print("panel B (alpha=%.4f) trace means: raw %.4f, real %.4f, null %.4f, oracle %.4f"
          % (a, d["B"]["raw"], d["B"]["real"], d["B"]["nullfix"], d["B"]["nullor"]))
    for t in (3, 9):
        print(f"round {t}: s_raw={d['s_raw'][t]:.4f} s_real={d['s_real'][t]:.4f} "
              f"s_null={d['s_nullfix'][t]:.4f} s_oracle={d['s_nullor'][t]:.4f} | "
              f"A payoff raw/real/null = {payoff_share(d['s_raw'][t], 0.5):.4f}/"
              f"{payoff_share(d['s_real'][t], 0.5):.4f}/{payoff_share(d['s_nullfix'][t], 0.5):.4f}"
              f" | B payoff raw/real/null/oracle = {payoff_share(d['s_raw'][t], a):.4f}/"
              f"{payoff_share(d['s_real'][t], a):.4f}/{payoff_share(d['s_nullfix'][t], a):.4f}/"
              f"{payoff_share(d['s_nullor'][t], a):.4f}")
    touched = [(int(t), round(float(d["disp_real"][t]), 3),
                round(float(d["disp_real"][t]) / d["dose"] * 100, 1))
               for t in np.where(d["disp_real"] > 1e-6)[0]]
    print("rounds the repair touches (t, L1, % of budget):", touched)
    print("per-round: null beats real on %d of %d rounds under payoff A, %d of %d under payoff B"
          % ((payoff_share(d["s_nullfix"], 0.5) > payoff_share(d["s_real"], 0.5)).sum(), T,
             (payoff_share(d["s_nullfix"], a) > payoff_share(d["s_real"], a)).sum(), T))


if __name__ == "__main__":
    main()
