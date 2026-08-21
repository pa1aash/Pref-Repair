# Pipeline substitution map — how steps 3–7's artefacts were supplied without running steps 3–7

Companion to `STEP_DEPENDENCY_ANALYSIS.md`, which established that steps 8, 10 and 11 hard-require
three files that the skipped steps would have produced. This file records exactly what was written
into each, from what, and at what cost. It exists so that a reader of the final report can tell
which parts of the pipeline saw agent-derived evidence and which saw hand-authored substitution.

## The mapping

| Required artefact | Normally produced by | Substituted from | Fidelity |
|---|---|---|---|
| `research/loci.json` | step 4 (2 loci-analysts over the width corpus) | The six G0 kill-checks and G0.5 items 1–5, recast as six scored loci with the schema's fields | **High.** Each locus corresponds to a question that was actually investigated to full-text depth, with a falsifier committed before the finding. Scores are the orchestrator's judgement, as they would have been the analysts'. |
| `research/comparisons.md` | step 6 (reconciling depth-investigator committed positions) | Five cross-locus tensions drawn from where the audit's own findings collide | **High on content, low on independence.** These are real collisions between full-text reads — e.g. E3's framing effect *is* the reliability critique's construct-validity problem — but they were identified by the same process that produced the findings, not by a separate reconciliation pass. |
| `research/temp/source-tensions.json` | step 7 (expert-disagreement extraction from full source bodies) | Six documented disagreements between named papers, each with proponents given as real vault note ids | **High.** Every side of every tension is a paper read in full by G0 or G0.5, and the evidence strings are the actual reported numbers. |
| `research/temp/coverage-gaps.md` | step 2.5 | G0's `RUN_RECORD.md`, updated with items 2 and 3 | High. |
| `research/temp/contradiction-graph.json`, `consensus-claims.json` | step 3 | **Not supplied.** | The step-9 skill marks both as conditional (`if step 3 ran`), so they are genuinely optional. Their role is filled by `source-tensions.json`. |

`research/scaffold.md` was appended with an S1 section naming `docs/FRAMING.md` as authoritative,
restating the frozen C1 and C2, and pointing at the banned-sentence list, so that every downstream
subagent reads the freeze rather than re-deriving positioning.

## What this costs, stated rather than hidden

The pipeline's steps 3–7 exist partly to produce artefacts and partly to produce them
*independently* — two loci-analysts who have not seen each other's output, depth investigators who
commit to positions before reconciliation. Substituting removes that independence. **Any bias in
the audit now propagates into the draft instead of being independently re-found**, and the
comparisons in particular were authored by the same process that generated the findings they
reconcile.

Two mitigations, both real but neither complete:

1. **The audit's evidentiary standard is higher than the substituted step's would have been.** Each
   kill-check states a falsifier *before* reporting the finding, records fetch provenance including
   byte counts and extraction method, and distinguishes access gaps from zeros. G0.5's items read
   six occupant papers cover to cover and overturned two of G0's own conclusions in the process —
   which is evidence the process does self-correct.
2. **The step-12 critics are briefed to attack the audit's conclusions specifically**, not to
   critique the draft generically. They are pointed at the two things most likely to sink the
   paper: the six-occupant landscape and the Q3 method risk. That is the closest available
   substitute for the independence that was given up.

## What was NOT substituted

The width corpus is real: 102 source notes, 78 kept, fetched by ten parallel fetchers in G0, with
63 per-source claims files under `research/temp/`. Step 9's evidence digest is therefore built from
genuine fetched material, not from the audit. Steps 8 and 10–16 run normally against it.
