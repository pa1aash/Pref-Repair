# OpenReview submission form — exact field text

Sourced verbatim from `tex/paper.tex` as of the 2026-08-29 clean rebuild (`tex/paper.pdf`,
343508 bytes, 18 pages, main text 9 pages). Do not retype from memory when filling the form —
copy-paste from this file.

---

## Title

```
What Does Repairing Choice Inconsistency Actually Buy? A Budget-Set Diagnosis
```

Copied from `tex/paper.tex:18` (`\title{}`), with the LaTeX line break (`\\`) rendered as a
single space, since the OpenReview title field is plain text with no line breaks.

## Keywords

```
revealed preference, GARP, LLM agents, choice consistency, dose-response, exogenous payoff, budget sets, AI rationality
```

Eight terms, pulled from actual paper vocabulary (abstract and \S1 Introduction), not invented:
"GARP-rationalizability" / "GARP", "revealed preference" (paper's own framing, \S1), "LLM agent"
(abstract, \S1), "coherence" / consistency (abstract), "dose--response relationship" (abstract,
\S1), "exogenous payoff" (abstract, \S1, and the CFP's own "economic contexts" bullets), "budget
sets" (abstract, \S1, and the paper's title), "AI rationality" (matches the CFP bullet "Formal
abstractions of AI rationality and bias in economic contexts," which `docs/VENUE.md`'s fit audit
identifies as this paper's direct-fit bullet).

## TL;DR

```
Repairing an LLM agent's GARP violations produces a real, monotone dose-response effect on an exogenous payoff (Spearman rho=0.756, p<0.0001 at 1.5B).
```

21 words. States the headline finding with its actual number, taken from the abstract's reported
statistic at the 1.5B scale (the scale with measured coherence headroom, per the abstract).

## Abstract

Exact text of `\begin{abstract}...\end{abstract}` in `tex/paper.tex`, with LaTeX markup rendered
to plain text (`\emph{X}` to italics-intent-only *X*, `$...$` math rendered inline, `---` em-dashes
kept as em-dashes, `\\ ` line breaks removed since this is one continuous paragraph on the form).
Wording is unchanged from the source — nothing paraphrased or re-summarized.

```
Repairing an AI agent's incoherent preferences is not a new idea: inference-time layers that restore transitivity, isotonic projections onto preference-defined cones, and training-time rationality penalties have all been proposed, and several report downstream gains. What no existing result establishes is how much coherence is worth, because every published comparison either varies the coherence assumption by swapping in a strictly richer model class — confounding coherence with capacity — or scores the outcome with another preference judgment, or treats repair as binary. We take the economics route instead. Given an LLM agent's own choices over budget sets, we compute the minimal perturbation restoring GARP-rationalizability as a single mixed-integer program, which yields a graded, cardinal dose (an Afriat-style efficiency index) where prior work has mostly used binary cycle-counting or toggled interventions, and we apply it post hoc to a frozen agent, so capacity, training and policy are identical across doses by construction. Scoring the repaired sequences against a fixed, pre-registered exogenous payoff that no preference judgment enters, we trace the dose–response relationship from the raw sequence toward full rationalizability at two model scales (a 1.5B-parameter model with measured coherence headroom, and a 3B-parameter model with almost none, run as an identification control rather than a second point on one scale curve). The relationship is real, strongly monotone, and precisely estimated at both scales (Spearman rho=0.756, p<0.0001, n=60 at 1.5B; rho=0.614, p=0.0011, n=25 at 3B) and survives a targeted robustness check against the mechanical confound that larger violations simply have more room to improve. We also report two findings the design was not built to predict. First, the reciprocal-price framing manipulation that motivated the study does not reliably move coherence at 1.5B once a discard-selection bias in the output-format contract is corrected by a capped retry protocol — the pilot's positive finding was survivorship, not an effect, and we show the correction rather than assume it. Second, an independently published format mechanism (single-turn vs. multi-turn elicitation) produces the largest, cleanest confirmatory effect in the study, with zero discard confound on either arm. Throughout, we report Bronars power beside every efficiency index and report the discard rate as a first-class per-condition outcome rather than a silently-dropped nuisance.
```

## Track

**Long paper (up to 9 pages of main text).** Confirmed correct: the 2026-08-29 clean rebuild has
main text ending at page 9 (References start page 10, Appendix page 11, Checklist pages 12–18),
exactly at — not over — the long-paper limit. This is a form radio button, selected explicitly,
not inferred from the PDF (per `docs/SUBMISSION_CHECKLIST.md` item 3).

---

## License

**CC BY 4.0** — select this option.

Not a guess: queried live from the actual OpenReview submission invitation schema
(`https://api2.openreview.net/invitations?id=NeurIPS.cc/2026/Workshop/EconML/-/Submission`,
`edit.note.license` field) on 2026-08-29. The field's `enum` currently contains exactly one
option — `"CC BY 4.0"` — so there is no real choice to make; this is the only value the form will
accept.

## Supplementary material

**Leave empty.** `tex/checklist.tex`'s "Open access to data and code" item answers `\answerNo{}`
(confirmed unchanged on 2026-08-29 re-check): code and raw per-trace logs are not released with
this submission, and the protocol is fully specified in-text instead. An empty Supplementary
Material field is consistent with that answer, not a gap — do not attach anything on the theory
that the field being optional means it should be filled.

---

## Fields only the operator can complete — listed, not filled in here

These are yes/no confirmations of fact or personal consent. This document states what they are;
it does not recommend or pre-select an answer, because only the operator can authorize them.

- **`author_attendance`** — confirms at least one author will attend in-person in Atlanta if
  accepted. Single-option radio; operator must personally confirm this commitment.
- **`email_sharing`** — authorizes sharing all author emails with Program Chairs. No alternative
  option exists; operator must personally consent.
- **`data_release`** — authorizes release of the submission and author names to the public if
  accepted. No alternative option exists; operator must personally consent, understanding this is
  what ends anonymity, and only upon acceptance.

## Hard blocker: Serve As Reviewer

**`serve_as_reviewer` cannot be completed by this pass.** It requires an OpenReview *profile ID*
for the nominated author — a profile is created by that person logging into OpenReview and filling
out their account, which does not exist until the operator (or the relevant author) does it. This
is a precondition for the field, not a text field that can be pre-drafted here.

This is the one hard blocker to completing the form at all: no profile ID exists yet in this
project's files, and none can be fabricated. See `docs/SUBMISSION_CHECKLIST.md` step 2 for the
full decision procedure — whether any author meets the "published in a NeurIPS/ICML/ICLR/AAAI/EC/
WWW main track as lead or senior author" bar, and if not, the required fallback: nominate the
best-qualified author anyway **and** email `neurips-2026-econml-workshop@googlegroups.com` before
the deadline stating that no author meets the bar.
