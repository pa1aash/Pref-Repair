"""Pipeline schematic (tex/paper.tex, fig:pipeline, placed at the end of sec.method-nullop).

A from-scratch boxes-and-arrows diagram of the full measurement pipeline described in
sec.method and sec.design: budget-set draw -> prompt/format arm -> parse + capped retry ->
GARP check -> MILP projection -> matched-null construction -> payoff scoring under both
payoff designs. No data is read; every label and count is transcribed from tex/paper.tex
(sec.method-projection, sec.method-payoff, sec.method-nullop, sec.design, sec.discard,
sec.results) so the figure and the prose use the same words and the same numbers.

Palette is scripts/make_figures.py's, with meaning held fixed across the paper's figures:
BLUE = the primary / real-repair path, ORANGE = the null-control path (orange is already
the paper's "null control" colour), GREY = superseded / dropped material. Colour is never
the only carrier: the real path is a solid border, the null path a dashed border, and the
two exit branches (residual discard, already-GARP-consistent) are dotted grey arrows with
italic labels, so the diagram survives greyscale printing.

Sizing: authored at 5.30 in wide and included at 0.98\\linewidth, so the rendered scale
factor is ~1.02 and no glyph in the final PDF falls below its authored 8 pt.
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

BLUE = "#2a78d6"     # slot 1 -- primary / real repaired sequence
ORANGE = "#eb6834"   # slot 2 -- null-operator control path
AQUA = "#1baf7a"     # slot 3 -- reserved (unused here, as in make_figures.py)
GREY = "#9b9a94"     # dropped / not-projected branches
TEXT = "#1a1a1a"
MUTED = "#52514e"
EDGE = "#4f4e4a"     # neutral pipeline-stage border
BLUE_FILL = "#eaf2fc"
ORANGE_FILL = "#fdefe9"

plt.rcParams.update({
    "font.size": 9,
    "text.color": TEXT,
    "font.family": "DejaVu Sans",
})

TITLE_PT = 8.5       # stage titles
BODY_PT = 8.0        # stage body text and edge labels (paper floor: >= 8 pt)
LINESPACING = 1.20
LINE_H = 0.132       # inches consumed per body line at BODY_PT x LINESPACING
PAD_TITLE = 0.072    # box top -> title baseline anchor
PAD_BODY = 0.218     # box top -> body block anchor
BOX_BASE = 0.275     # fixed box overhead (title line + padding)

W = 5.30             # figure width, inches


def box_h(nlines: int) -> float:
    return BOX_BASE + LINE_H * nlines


def stage(ax, x, y_top, w, h, title, lines, ec=EDGE, fc="white", ls="-", lw=1.1):
    """One pipeline stage: rounded box, bold numbered title, body lines beneath."""
    ax.add_patch(FancyBboxPatch(
        (x, y_top - h), w, h,
        boxstyle="round,pad=0,rounding_size=0.05",
        linewidth=lw, edgecolor=ec, facecolor=fc, linestyle=ls, zorder=3))
    cx = x + w / 2.0
    ax.text(cx, y_top - PAD_TITLE, title, ha="center", va="top",
            fontsize=TITLE_PT, fontweight="bold", color=TEXT, zorder=4)
    ax.text(cx, y_top - PAD_BODY, "\n".join(lines), ha="center", va="top",
            fontsize=BODY_PT, color=TEXT, linespacing=LINESPACING, zorder=4)


def flow(ax, pts, color=EDGE, ls="-", lw=1.15):
    """Polyline connector; the final segment carries the arrowhead."""
    if len(pts) > 2:
        ax.plot([p[0] for p in pts[:-1]], [p[1] for p in pts[:-1]],
                color=color, lw=lw, ls=ls, solid_capstyle="round", zorder=2)
    ax.annotate("", xy=pts[-1], xytext=pts[-2],
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                linestyle=ls, shrinkA=0, shrinkB=0,
                                mutation_scale=10), zorder=2)


DOTTED = (0, (1.6, 1.8))
DASHED = (0, (4.2, 2.0))


def build():
    # ---- row heights ------------------------------------------------------
    h_r1, h_r2, h_r3, h_r4 = box_h(3), box_h(2), box_h(3), box_h(3)
    band_a, band_b, band_c = 0.30, 0.46, 0.14
    margin = 0.03
    H = margin + h_r1 + band_a + h_r2 + band_b + h_r3 + band_c + h_r4 + margin

    y_r1_top = H - margin
    y_r1_bot = y_r1_top - h_r1
    y_r2_top = y_r1_bot - band_a
    y_r2_bot = y_r2_top - h_r2
    y_r3_top = y_r2_bot - band_b
    y_r3_bot = y_r3_top - h_r3
    y_r4_top = y_r3_bot - band_c
    y_r4_bot = y_r4_top - h_r4

    fig = plt.figure(figsize=(W, H))
    fig.patch.set_facecolor("white")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")

    # ---- row 1: three equal columns, left to right ------------------------
    bw, gap, x0 = 1.65, 0.155, 0.02
    c1x, c2x, c3x = x0, x0 + bw + gap, x0 + 2 * (bw + gap)

    stage(ax, c1x, y_r1_top, bw, h_r1, "1. Budget-set draw",
          ["T = 25 rounds, K = 2 goods",
           "continuous-density prices",
           "fresh seed per replicate"])
    stage(ax, c2x, y_r1_top, bw, h_r1, "2. Prompt / format arm",
          ["baseline, reciprocal,",
           "multiturn; 3 arms at 1.5B,",
           "2 arms at 3B"])
    stage(ax, c3x, y_r1_top, bw, h_r1, "3. Parse + capped retry",
          ["$\\geq$20/25 valid rounds:",
           "keep. Else retry, capped",
           "at 3 attempts per slot"])

    y_r1_mid = y_r1_top - h_r1 / 2.0
    flow(ax, [(c1x + bw, y_r1_mid), (c2x, y_r1_mid)])
    flow(ax, [(c2x + bw, y_r1_mid), (c3x, y_r1_mid)])

    # residual-discard exit, hanging left of the wrap connector
    y_e1 = y_r1_bot - 0.16
    flow(ax, [(3.85, y_r1_bot), (3.85, y_e1), (3.62, y_e1)], color=GREY, ls=DOTTED, lw=1.0)
    ax.text(3.56, y_e1, "residual discard: 8 of 150 slots", ha="right", va="center",
            fontsize=BODY_PT, style="italic", color=MUTED)

    # wrap: row 1 -> row 2, straight down the right-hand column
    c3_mid = c3x + bw / 2.0
    flow(ax, [(c3_mid, y_r1_bot), (c3_mid, y_r2_top)])

    # ---- row 2: two boxes, flowing right to left --------------------------
    r2r_x, r2r_w = 3.03, 2.25
    r2l_x, r2l_w = 0.02, 2.85

    stage(ax, r2r_x, y_r2_top, r2r_w, h_r2, "4. GARP check",
          ["combinatorial Warshall-closure",
           "check; 85 of 142 traces violate"])
    stage(ax, r2l_x, y_r2_top, r2l_w, h_r2, "5. MILP projection",
          ["Demuynck & Rehbeck (2023) minimal-quantity-",
           "error repair, re-verified by the same check"])

    y_r2_mid = y_r2_top - h_r2 / 2.0
    flow(ax, [(r2r_x, y_r2_mid), (r2l_x + r2l_w, y_r2_mid)])

    # already-GARP-consistent exit
    y_e2 = y_r2_bot - 0.20
    flow(ax, [(4.72, y_r2_bot), (4.72, y_e2), (4.49, y_e2)], color=GREY, ls=DOTTED, lw=1.0)
    ax.text(4.43, y_e2, "GARP-consistent (57 of 142): no projection", ha="right",
            va="center", fontsize=BODY_PT, style="italic", color=MUTED)

    # ---- row 3: the two matched paths -------------------------------------
    r3l_x, r3l_w = 0.02, 2.30
    r3r_x, r3r_w = 2.46, 2.82
    r3l_mid = r3l_x + r3l_w / 2.0
    r3r_mid = r3r_x + r3r_w / 2.0

    stage(ax, r3l_x, y_r3_top, r3l_w, h_r3, "6a. Real repaired sequence",
          ["$\\tilde{x}$: GARP-consistent by",
           "construction, independently",
           "verified; dose = its $L_1$ distance"],
          ec=BLUE, fc=BLUE_FILL, lw=1.4)
    stage(ax, r3r_x, y_r3_top, r3r_w, h_r3, "6b. Matched-null construction",
          ["GARP-blind: shrink every bundle toward the",
           "fixed center, at an identical $L_1$ displacement",
           "primary (information-fair) null; oracle null"],
          ec=ORANGE, fc=ORANGE_FILL, ls=DASHED, lw=1.4)

    # fork out of the projection: real path (blue) and null path (orange)
    r2l_mid = r2l_x + r2l_w / 2.0
    y_fork = y_r3_top + 0.11
    ax.plot([r2l_mid, r2l_mid], [y_r2_bot, y_fork], color=EDGE, lw=1.15, zorder=2)
    flow(ax, [(r2l_mid, y_fork), (r3l_mid, y_fork), (r3l_mid, y_r3_top)], color=BLUE, lw=1.3)
    flow(ax, [(r2l_mid, y_fork), (r3r_mid, y_fork), (r3r_mid, y_r3_top)],
         color=ORANGE, ls=DASHED, lw=1.3)

    # ---- row 4: shared scoring step ---------------------------------------
    stage(ax, 0.02, y_r4_top, 5.26, h_r4, "7. Payoff scoring, under both payoff designs",
          ["original: fixed equal-weight Cobb–Douglas, one optimum at $s = 0.5$ for every trace",
           "corrected: per-trace $\\alpha_s \\sim \\mathrm{Uniform}(0.05, 0.95)$, read only at scoring time",
           "$\\Delta$payoff, real repair vs. each null — paired, at matched displacement"])

    flow(ax, [(r3l_mid, y_r3_bot), (r3l_mid, y_r4_top)], color=BLUE, lw=1.3)
    flow(ax, [(r3r_mid, y_r3_bot), (r3r_mid, y_r4_top)], color=ORANGE, ls=DASHED, lw=1.3)

    assert y_r4_bot >= 0.0
    return fig, H


def main():
    fig, H = build()
    fig.savefig("figures/fig_pipeline_schematic.pdf", bbox_inches="tight", pad_inches=0.02)
    fig.savefig("figures/fig_pipeline_schematic.png", dpi=200, bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    print(f"wrote figures/fig_pipeline_schematic.pdf and .png "
          f"(authored {W:.2f} x {H:.2f} in; smallest text {BODY_PT} pt)")


if __name__ == "__main__":
    main()
