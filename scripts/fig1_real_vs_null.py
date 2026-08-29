"""Figure 1, redesigned for item 7C: the real-vs-null-operator comparison that is now this
paper's actual headline (docs/PAPER_STORY.md; paper.tex \\S\\ref{sec:results-c1}), not the raw
dose-vs-payoff scatter the old fig1() in scripts/make_figures.py drew. Deliberately a separate,
standalone script (not an edit to make_figures.py) per the task instructions, so concurrent
agents regenerating Figures 2-3 in their own worktrees are not affected. Writes the same output
filenames (figures/fig1_dose_response.{pdf,png}) since tex/paper.tex's \\includegraphics already
points there -- this replaces the file's content, not its name.

Data: results/null_operator.json (Experiment 1, original fixed Cobb-Douglas payoff, 85 traces,
one real-vs-null pair each) and results/corrected_payoff.json (Experiment 2, per-trace random
target alpha_s ~ Uniform(0.05,0.95), K=20 independent draws, 85 traces per draw). Both files'
per-trace ordering is the sorted (model, condition, replicate) list of the 85 GARP-violating
traces (verified: null_operator.json's `traces` list is already sorted on that key, and
docs/CORRECTED_PAYOFF_RESULTS.md sec.0 defines corrected_payoff.json's per-draw arrays using that
same sorted trace_index) -- so index i in a corrected_payoff.json draw's arrays is the same
underlying trace as null_operator.json["traces"][i], which is how we recover each point's model
label for Panel B without a second identity field in corrected_payoff.json.

Statistic-annotation fix (the Fable-flagged OLS-line-vs-Spearman-rho mismatch in the old figure):
this redesign drops the dose-vs-payoff OLS trend line entirely, so the mismatch it caused
(a Pearson-linear-implying line captioned with a rank correlation) cannot recur. The only
correlation-shaped decoration here is the y=x reference line, which is not a fitted statistic --
it visualizes the null hypothesis "real and null buy the same payoff," not a trend estimate --
and the annotated numbers (Wilcoxon signed-rank p, win rate) are the exact paired-comparison
statistics reported in prose (paper.tex \\S\\ref{sec:results-c1}), not a proxy for them. Where a
correlation IS relevant to a reader trying to sanity-check the panel (does dose still predict
delta_payoff_real once you condition on the null?), that is a partial-correlation number already
reported in prose and appendix, not something this plot re-derives or re-annotates.
"""
from __future__ import annotations
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

# Copied from scripts/make_figures.py's style block (not imported, per task instructions, to
# avoid any cross-script coupling while other agents may be editing that file concurrently).
BLUE = "#2a78d6"     # slot 1 -- 1.5B / headroom model
ORANGE = "#eb6834"   # slot 2 -- 3B / null-control model
AQUA = "#1baf7a"     # slot 3 -- reserved (unused here)
GREY = "#9b9a94"     # naive / superseded data, deliberately desaturated
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

MODEL_STYLE = {
    "qwen2.5:1.5b-instruct-q4_K_M": dict(color=BLUE, marker="o", label="qwen2.5:1.5b (headroom)"),
    "llama3.2:3b-instruct-q4_K_M": dict(color=ORANGE, marker="^", label="llama3.2:3b (null control)"),
}


def savefig(fig, name):
    fig.savefig(f"figures/{name}.pdf", bbox_inches="tight")
    fig.savefig(f"figures/{name}.png", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote figures/{name}.pdf and .png")


def _scatter_by_model(ax, x, y, models):
    for m, style in MODEL_STYLE.items():
        mask = models == m
        if not mask.any():
            continue
        ax.scatter(
            x[mask], y[mask], s=18, marker=style["marker"], color=style["color"],
            alpha=0.7, linewidths=0, zorder=3, label=style["label"],
        )


SYMLOG_LINTHRESH = 0.01  # both panels have one far-outlier trace (the dose=111.64 trace hand-
# checked in Appendix~\ref{app:payoff-audit}(3)); a linear axis compresses the other 84 traces
# into a corner. symlog keeps the outlier on-plot without dropping or clipping it -- linear near
# zero (where deltas can be negative), log-like beyond linthresh.


def _diagonal_and_labels(ax, lo, hi):
    xs = np.linspace(lo, hi, 200)
    ax.plot(xs, xs, color="#8a8980", linewidth=1.1, linestyle="--", zorder=2)
    ax.set_xscale("symlog", linthresh=SYMLOG_LINTHRESH, linscale=0.6)
    ax.set_yscale("symlog", linthresh=SYMLOG_LINTHRESH, linscale=0.6)
    ax.set_xlim(lo, hi)
    ax.set_ylim(lo, hi)


# ---------------------------------------------------------------------------
# Panel A: Experiment 1 (original fixed-target payoff), results/null_operator.json.
# One point per GARP-violating trace (n=85): x = real repair's delta_payoff, y = the
# distance-matched null operator's delta_payoff. Above the y=x line: the null won.
# ---------------------------------------------------------------------------
def _panel_a(ax):
    d = json.load(open("results/null_operator.json"))
    traces = d["traces"]
    models = np.array([t["model"] for t in traces])
    real = np.array([t["delta_payoff_real"] for t in traces])
    null = np.array([t["delta_payoff_null"] for t in traces])

    p = d["summary"]["paired_wilcoxon_p"]
    n = d["summary"]["n"]
    win = int((null > real).sum())
    win_rate = win / n

    lo = min(real.min(), null.min()) - 0.01
    hi = max(real.max(), null.max()) * 1.05
    _diagonal_and_labels(ax, lo, hi)
    _scatter_by_model(ax, real, null, models)

    ax.set_xlabel(r"Real repair $\Delta$payoff")
    ax.set_ylabel(r"Null operator $\Delta$payoff")
    ax.set_title("A. Experiment 1: original payoff", fontsize=9, color=TEXT, loc="left", pad=8)
    p_str = "$p$ < 0.0001" if p < 0.0001 else f"$p$ = {p:.4f}"
    ax.text(
        0.04, 0.96,
        f"Wilcoxon {p_str}\nnull wins {win}/{n} ({win_rate:.0%})",
        transform=ax.transAxes, ha="left", va="top", fontsize=8, color=MUTED,
    )


# ---------------------------------------------------------------------------
# Panel B: Experiment 2 (corrected, per-trace random-target payoff),
# results/corrected_payoff.json. Same 85 traces, K=20 independent draws of the random
# target alpha_s per trace; each point is one trace's mean delta_payoff over the 20 draws
# (real repair on x, primary information-fair null on y), with a vertical error bar showing
# +/-1 sd of the null's delta_payoff across those 20 draws -- the draw-to-draw uncertainty
# the aggregation would otherwise hide. Wilcoxon p and win rate annotated are the paper's
# own reported across-draws means (mean of 20 per-draw Wilcoxon tests / win rates;
# docs/CORRECTED_PAYOFF_RESULTS.md sec.1), not re-derived from the per-trace means plotted
# here, since the two aggregations answer slightly different questions and the prose number
# is the one the caption and \\S\\ref{sec:results-c1} actually cite.
# ---------------------------------------------------------------------------
EXP2_PRIMARY_WILCOXON_P = 1.24e-05   # docs/CORRECTED_PAYOFF_RESULTS.md sec.1, mean across 20 draws
EXP2_PRIMARY_WIN_RATE = 0.7076       # docs/CORRECTED_PAYOFF_RESULTS.md sec.1, mean across 20 draws


def _panel_b(ax, model_lookup):
    d = json.load(open("results/corrected_payoff.json"))
    draws = d["draws"]
    n = d["n_traces"]

    real_per_trace = np.array([[dr["delta_payoff_real"][i] for dr in draws] for i in range(n)])
    null_per_trace = np.array([[dr["delta_payoff_null_fixed"][i] for dr in draws] for i in range(n)])

    real_mean = real_per_trace.mean(axis=1)
    null_mean = null_per_trace.mean(axis=1)
    null_sd = null_per_trace.std(axis=1)

    models = np.array([model_lookup[i] for i in range(n)])

    lo = min(real_mean.min(), (null_mean - null_sd).min()) - 0.01
    hi = max(real_mean.max(), (null_mean + null_sd).max()) * 1.05
    _diagonal_and_labels(ax, lo, hi)

    for m, style in MODEL_STYLE.items():
        mask = models == m
        if not mask.any():
            continue
        ax.errorbar(
            real_mean[mask], null_mean[mask], yerr=null_sd[mask],
            fmt=style["marker"], color=style["color"], ecolor=style["color"],
            alpha=0.7, markersize=4.2, linewidth=0, elinewidth=0.8, capsize=0,
            zorder=3, label=style["label"],
        )

    ax.set_xlabel(r"Real repair $\Delta$payoff (mean over $K$=20 draws)")
    ax.set_ylabel(r"Primary null $\Delta$payoff (mean over $K$=20 draws)")
    ax.set_title("B. Experiment 2: corrected payoff", fontsize=9, color=TEXT, loc="left", pad=8)
    p_str = "$p$ < 0.0001" if EXP2_PRIMARY_WILCOXON_P < 0.0001 else f"$p$ = {EXP2_PRIMARY_WILCOXON_P:.4f}"
    ax.text(
        0.04, 0.96,
        f"Wilcoxon {p_str} (mean of $K$=20 draws)\nnull wins {EXP2_PRIMARY_WIN_RATE:.1%} of trace-draws\n"
        r"error bars: $\pm 1$ sd over draws",
        transform=ax.transAxes, ha="left", va="top", fontsize=8, color=MUTED,
    )


def fig1():
    d = json.load(open("results/null_operator.json"))
    model_lookup = {i: t["model"] for i, t in enumerate(d["traces"])}

    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.85))
    _panel_a(axes[0])
    _panel_b(axes[1], model_lookup)

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(
        handles, labels, loc="lower center", ncol=2, bbox_to_anchor=(0.5, -0.08),
        frameon=False, fontsize=8,
    )
    fig.tight_layout()
    savefig(fig, "fig1_dose_response")


if __name__ == "__main__":
    fig1()
