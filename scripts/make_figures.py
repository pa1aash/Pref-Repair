"""Paper figures for Part Three (docs/MAIN_EXPERIMENT_RESULTS.md's headline findings).

Reads results/main_ccei.json (per-trace records) and the pilot/main numbers transcribed
directly from docs/PILOT_RESULTS.md and docs/MAIN_EXPERIMENT_RESULTS.md (both cited inline
below, no numbers invented). Palette: dataviz skill's validated categorical slots 1/2/3
(blue #2a78d6, orange #eb6834, aqua #1baf7a) -- color assigned by entity and held fixed
across figures: 1.5B (headroom model) is always blue, 3B (null-control model) is always
orange, "retry-corrected / trustworthy" data is blue, "naive / survivorship-biased" data
is a desaturated grey to flag it visually as the thing being superseded.
"""
from __future__ import annotations
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

BLUE = "#2a78d6"     # slot 1 -- 1.5B / headroom model / retry-corrected data
ORANGE = "#eb6834"   # slot 2 -- 3B / null-control model
AQUA = "#1baf7a"     # slot 3 -- reserved (unused, kept for a possible third series)
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

rows = json.load(open("results/main_ccei.json"))


def savefig(fig, name):
    fig.savefig(f"figures/{name}.pdf", bbox_inches="tight")
    fig.savefig(f"figures/{name}.png", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote figures/{name}.pdf and .png")


# ---------------------------------------------------------------------------
# Figure 1: dose-response, 1.5B (headroom) vs 3B (null control), two panels,
# shared axes, identical marker/line spec so the attenuation is the only
# visual difference between panels.
# ---------------------------------------------------------------------------
def fig1():
    viol = [r for r in rows if not r["garp"] and "dose_l1" in r and r.get("projection_verified")]
    q = [r for r in viol if r["model"].startswith("qwen")]
    l = [r for r in viol if r["model"].startswith("llama")]

    all_dose = np.array([r["dose_l1"] for r in viol])
    xmax = all_dose.max() * 1.05

    fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.9), sharex=True, sharey=True)

    for ax, data, color, label, n in [
        (axes[0], q, BLUE, "qwen2.5:1.5b (headroom)", len(q)),
        (axes[1], l, ORANGE, "llama3.2:3b (null control)", len(l)),
    ]:
        dose = np.array([r["dose_l1"] for r in data])
        dpay = np.array([r["delta_payoff"] for r in data])
        rho, p = stats.spearmanr(dose, dpay)

        ax.axhline(0, color="#c9c8c2", linewidth=0.8, zorder=1)
        ax.scatter(dose, dpay, s=16, color=color, alpha=0.65, linewidths=0, zorder=3)

        # OLS trend line (display only; rho/p above are the reported statistic)
        b, a = np.polyfit(dose, dpay, 1)
        xs = np.linspace(0, xmax, 50)
        ax.plot(xs, a + b * xs, color=color, linewidth=1.6, zorder=2)

        ax.set_title(label, fontsize=9, color=TEXT, loc="left")
        ax.set_xlabel("Projection dose ($L_1$)")
        ax.set_xlim(0, xmax)
        p_str = "$p$ < 0.0001" if p < 0.0001 else f"$p$ = {p:.4f}"
        ax.text(0.97, 0.06, f"Spearman $\\rho$ = {rho:.3f}\n{p_str}\n$n$ = {n}",
                 transform=ax.transAxes, ha="right", va="bottom", fontsize=7.5, color=MUTED)

    axes[0].set_ylabel("$\\Delta$ exogenous payoff\n(repaired $-$ raw)")
    fig.suptitle("Projection dose ($L_1$) vs. change in exogenous payoff, by model\n"
                  "(each point: one GARP-violating trace, post hoc projection; shared axes both panels)",
                  fontsize=8.5, y=1.08, color=MUTED)
    fig.tight_layout()
    savefig(fig, "fig1_dose_response")


# ---------------------------------------------------------------------------
# Figure 2: the discard-selection bias, before vs after the C3 retry protocol.
# Numbers transcribed from docs/PILOT_RESULTS.md sec.3 (pilot, single-attempt,
# silent discard) and docs/MAIN_EXPERIMENT_RESULTS.md sec.2-3 (main, capped
# 3-attempt retry, residual discard reported).
# ---------------------------------------------------------------------------
def fig2():
    # CCEI: baseline -> reciprocal, at qwen 1.5b
    pilot_base, pilot_recip = 0.9262, 0.9431          # PILOT_RESULTS.md sec.3, single attempt
    pilot_delta, pilot_p = 0.0169, 0.66
    pilot_discard_recip = 0.52                         # 13/25

    main_base, main_recip = 0.9522, 0.9413             # MAIN_EXPERIMENT_RESULTS.md sec.3
    main_delta, main_p = -0.0109, 0.7276
    main_discard_first, main_discard_resid = 0.433, 0.20  # sec.2, 13/30 -> 6/30

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(4.6, 4.6), sharex=False,
                                    gridspec_kw={"height_ratios": [1.3, 1]})

    # top: CCEI delta, pilot (naive) vs main (retry-corrected)
    labels = ["Pilot\n(naive: silent discard,\nn=12 surviving)",
              "Main experiment\n(C3 retry protocol,\nn=24 surviving)"]
    deltas = [pilot_delta, main_delta]
    colors = [GREY, BLUE]
    ps = [pilot_p, main_p]
    x = np.arange(2)
    bars = ax1.bar(x, deltas, color=colors, width=0.5, zorder=3)
    ax1.axhline(0, color="#8a8980", linewidth=0.8, zorder=1)
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels, fontsize=8)
    ax1.set_ylabel("$\\Delta$ CCEI\n(reciprocal $-$ baseline)")
    ax1.set_title("1.5B reciprocal-framing CCEI comparison: pilot (single attempt) vs. main experiment (retry protocol)",
                   fontsize=8.3, loc="left", color=TEXT)
    for xi, d, p in zip(x, deltas, ps):
        va = "bottom" if d >= 0 else "top"
        offset = 0.0015 if d >= 0 else -0.0015
        ax1.text(xi, d + offset, f"{d:+.4f}\n$p$={p:.2f}", ha="center", va=va, fontsize=7.5, color=MUTED)
    ax1.set_ylim(-0.02, 0.025)

    # bottom: discard rate, pilot single-attempt vs main first-attempt vs main residual
    labels2 = ["Pilot\n(single attempt)", "Main, first\nattempt", "Main, after\n3-attempt retry"]
    rates = [pilot_discard_recip, main_discard_first, main_discard_resid]
    colors2 = [GREY, "#c9c2a0", BLUE]
    x2 = np.arange(3)
    ax2.bar(x2, rates, color=colors2, width=0.55, zorder=3)
    ax2.set_xticks(x2)
    ax2.set_xticklabels(labels2, fontsize=8)
    ax2.set_ylabel("Discard rate\n(reciprocal framing, 1.5B)")
    ax2.set_ylim(0, 0.6)
    for xi, r in zip(x2, rates):
        ax2.text(xi, r + 0.015, f"{r:.0%}", ha="center", va="bottom", fontsize=8, color=MUTED)

    fig.tight_layout()
    savefig(fig, "fig2_discard_bias")


# ---------------------------------------------------------------------------
# Figure 3: the multiturn / format effect at 1.5B -- GARP pass rate vs CCEI,
# side by side, to make the "GARP pass rate is the sensitive instrument, CCEI
# is not" point visually rather than only in prose. Numbers from
# docs/MAIN_EXPERIMENT_RESULTS.md sec.3.
# ---------------------------------------------------------------------------
def fig3():
    conds = ["baseline", "multiturn"]
    garp_pass = [0.40, 0.10]     # 12/30, 3/30
    garp_p = 0.0073
    ccei_mean = [0.9522, 0.9540]
    ccei_sd = [0.0721, 0.0509]
    ccei_p = 0.9131
    n = [30, 30]
    discard = [0.0, 0.0]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.2, 2.7))
    colors = [BLUE, "#7ea6d9"]

    x = np.arange(2)
    ax1.bar(x, garp_pass, color=colors, width=0.5, zorder=3)
    ax1.set_xticks(x); ax1.set_xticklabels(["baseline", "multiturn\n(25 seq. calls)"], fontsize=8.5)
    ax1.set_ylabel("GARP pass rate")
    ax1.set_ylim(0, 0.55)
    for xi, v in zip(x, garp_pass):
        ax1.text(xi, v + 0.015, f"{v:.0%}", ha="center", fontsize=8.5, color=MUTED)
    ax1.text(0.5, 0.97, f"$p$ = {garp_p}", transform=ax1.transAxes, ha="center", va="top",
              fontsize=8, color=MUTED)
    ax1.set_title("GARP pass rate", fontsize=8.7, loc="left")

    ax2.bar(x, ccei_mean, yerr=ccei_sd, color=colors, width=0.5, zorder=3,
            error_kw={"ecolor": MUTED, "elinewidth": 1, "capsize": 3})
    ax2.set_xticks(x); ax2.set_xticklabels(["baseline", "multiturn\n(25 seq. calls)"], fontsize=8.5)
    ax2.set_ylabel("mean CCEI")
    ax2.set_ylim(0.75, 1.05)
    ax2.text(0.5, 0.97, f"$p$ = {ccei_p:.2f}", transform=ax2.transAxes, ha="center", va="top",
              fontsize=8, color=MUTED)
    ax2.set_title("Mean CCEI", fontsize=8.7, loc="left")

    fig.suptitle("1.5B, baseline vs. multiturn format: GARP pass rate and mean CCEI\n"
                  "(zero discards in either arm; error bars are $\\pm 1$ SD)",
                  fontsize=8.3, y=1.12, color=MUTED)
    fig.tight_layout()
    savefig(fig, "fig3_multiturn_format")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
