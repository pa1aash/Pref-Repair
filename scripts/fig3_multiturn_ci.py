"""Figure 3 redesign (plan item 7E): 1.5B baseline vs. multiturn elicitation format.

Standalone script -- deliberately NOT importing from make_figures.py, since that module may
be edited concurrently by another agent in a different worktree. The small style block below
(palette, rcParams) is copied from make_figures.py's header to stay visually consistent with
the rest of the paper's figures.

Numbers (point estimates, SD, n, p-values) are transcribed from docs/MAIN_EXPERIMENT_RESULTS.md
sec.3 / tex/paper.tex's Figure 3 discussion and are NOT recomputed here. What this script adds
on top of the original fig3() in make_figures.py:

  1. GARP pass-rate bars get 95% Wilson score confidence intervals (binomial proportion CI --
     more appropriate than the normal approximation for n=30 and proportions near the tails).
  2. CCEI bars get 95% CIs via the t-distribution (df = n-1 = 29) applied to the reported
     mean/SD/n, replacing the old +/-1 SD error bars. This matches, to four decimal places, the
     95% CI already reported for these same two cells in docs/MAIN_EXPERIMENT_RESULTS.md's
     headline table (baseline [0.9253, 0.9791], multiturn [0.9350, 0.9729]) -- confirming the
     paper's existing CCEI-CI convention is the t-distribution, not the normal approximation.
  3. The second bar in each panel gets a hatch pattern (in addition to the existing lighter-blue
     fill) so the two conditions are distinguishable without relying on color alone.
  4. A purely descriptive caption (written in tex/paper.tex, not here) replaces the old
     "+/-1 SD" wording.
"""
from __future__ import annotations
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

# --- style block copied from scripts/make_figures.py (kept identical, not imported) --------
BLUE = "#2a78d6"     # slot 1 -- 1.5B / headroom model / retry-corrected data
LIGHT_BLUE = "#7ea6d9"
TEXT = "#1a1a1a"
MUTED = "#52514e"

plt.rcParams.update({
    "font.size": 9,
    "axes.edgecolor": "#c9c8c2",
    "axes.labelcolor": TEXT,
    "text.color": TEXT,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "font.family": "DejaVu Sans",
})


def savefig(fig, name):
    fig.savefig(f"figures/{name}.pdf", bbox_inches="tight")
    fig.savefig(f"figures/{name}.png", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote figures/{name}.pdf and .png")


def wilson_ci(x, n, z=1.96):
    """Wilson score interval for a binomial proportion. Returns (phat, lo, hi)."""
    phat = x / n
    denom = 1 + z**2 / n
    center = (phat + z**2 / (2 * n)) / denom
    margin = z * math.sqrt(phat * (1 - phat) / n + z**2 / (4 * n**2)) / denom
    return phat, center - margin, center + margin


def t_ci(mean, sd, n, conf=0.95):
    """CI for a mean from sample SD via the t-distribution (df = n-1)."""
    tcrit = stats.t.ppf(1 - (1 - conf) / 2, df=n - 1)
    margin = tcrit * sd / math.sqrt(n)
    return mean, mean - margin, mean + margin


# ---------------------------------------------------------------------------
# Figure 3: the multiturn / format effect at 1.5B -- GARP pass rate vs CCEI,
# side by side. Numbers from docs/MAIN_EXPERIMENT_RESULTS.md sec.3.
# ---------------------------------------------------------------------------
def fig3():
    conds = ["baseline", "multiturn"]
    garp_x = [12, 3]
    garp_n = [30, 30]
    garp_p = 0.0073  # Pearson chi-square, no continuity correction (verified: matches to 4 s.f.)

    ccei_mean = [0.9522, 0.9540]
    ccei_sd = [0.0721, 0.0509]
    ccei_n = [30, 30]
    ccei_p = 0.9131  # two-sample t-test, unchanged

    colors = [BLUE, LIGHT_BLUE]
    hatches = [None, "//"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.2, 2.7))
    x = np.arange(2)

    # --- Panel 1: GARP pass rate with Wilson 95% CI error bars ---
    garp_pass, garp_lo, garp_hi = [], [], []
    for xi_, n_ in zip(garp_x, garp_n):
        p, lo, hi = wilson_ci(xi_, n_)
        garp_pass.append(p); garp_lo.append(lo); garp_hi.append(hi)
    garp_pass = np.array(garp_pass)
    yerr_garp = np.array([garp_pass - np.array(garp_lo), np.array(garp_hi) - garp_pass])

    bars1 = ax1.bar(x, garp_pass, color=colors, width=0.5, zorder=3,
                     yerr=yerr_garp, error_kw={"ecolor": MUTED, "elinewidth": 1, "capsize": 3})
    for bar, h in zip(bars1, hatches):
        if h:
            bar.set_hatch(h)
            bar.set_edgecolor("white")
    ax1.set_xticks(x); ax1.set_xticklabels(["baseline", "multiturn\n(25 seq. calls)"], fontsize=8.5)
    ax1.set_ylabel("GARP pass rate")
    ax1.set_ylim(0, 0.68)
    for xi_, v, hi in zip(x, garp_pass, garp_hi):
        ax1.text(xi_, hi + 0.015, f"{v:.0%}", ha="center", fontsize=8.5, color=MUTED)
    ax1.text(0.5, 0.99, f"$p$ = {garp_p}", transform=ax1.transAxes, ha="center", va="top",
              fontsize=8, color=MUTED)
    ax1.set_title("GARP pass rate", fontsize=8.7, loc="left")

    # --- Panel 2: mean CCEI with t-distribution 95% CI error bars ---
    ccei_lo, ccei_hi = [], []
    for m, sd, n_ in zip(ccei_mean, ccei_sd, ccei_n):
        _, lo, hi = t_ci(m, sd, n_)
        ccei_lo.append(lo); ccei_hi.append(hi)
    ccei_mean_arr = np.array(ccei_mean)
    yerr_ccei = np.array([ccei_mean_arr - np.array(ccei_lo), np.array(ccei_hi) - ccei_mean_arr])

    bars2 = ax2.bar(x, ccei_mean, yerr=yerr_ccei, color=colors, width=0.5, zorder=3,
                     error_kw={"ecolor": MUTED, "elinewidth": 1, "capsize": 3})
    for bar, h in zip(bars2, hatches):
        if h:
            bar.set_hatch(h)
            bar.set_edgecolor("white")
    ax2.set_xticks(x); ax2.set_xticklabels(["baseline", "multiturn\n(25 seq. calls)"], fontsize=8.5)
    ax2.set_ylabel("mean CCEI")
    ax2.set_ylim(0.75, 1.05)
    for xi_, v, hi in zip(x, ccei_mean, ccei_hi):
        ax2.text(xi_, hi + 0.012, f"{v:.3f}", ha="center", fontsize=8.5, color=MUTED)
    ax2.text(0.5, 0.99, f"$p$ = {ccei_p:.2f}", transform=ax2.transAxes, ha="center", va="top",
              fontsize=8, color=MUTED)
    ax2.set_title("Mean CCEI", fontsize=8.7, loc="left")

    # No fig.suptitle: axis-level titles ("GARP pass rate" / "Mean CCEI") plus the LaTeX
    # caption already state what's plotted and how the error bars are computed, so a third,
    # redundant super-title (as the old figure had) is dropped rather than merely reworded --
    # same super-title-trimming direction applied to Figure 1's concurrent redesign.
    fig.tight_layout()
    savefig(fig, "fig3_multiturn_format")

    # Print CI values for the record.
    for cond, p, lo, hi in zip(conds, garp_pass, garp_lo, garp_hi):
        print(f"GARP {cond}: {p:.4f} 95% Wilson CI [{lo:.4f}, {hi:.4f}]")
    for cond, m, lo, hi in zip(conds, ccei_mean, ccei_lo, ccei_hi):
        print(f"CCEI {cond}: {m:.4f} 95% t-CI [{lo:.4f}, {hi:.4f}]")


if __name__ == "__main__":
    fig3()
