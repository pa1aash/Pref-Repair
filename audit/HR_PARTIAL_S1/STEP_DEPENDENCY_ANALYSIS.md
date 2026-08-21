# Can steps 8–16 run without steps 3–7? — dependency analysis

Performed before resuming the pipeline, per the session brief's instruction not to assume
steps 8+ can run standalone. Method: read the `## Recover state` block of every step skill under
the local skills directory and record what each reads **as a file, by path**.

## What each step reads

| Step | Required inputs | Present after G0? |
|---|---|---|
| 8 corpus-critic | `scaffold.md`, `comparisons.md`, `loci.json`, `temp/source-tensions.json`, `prompt-decomposition.json` | scaffold ✅, decomposition ✅, **comparisons ❌, loci ❌, source-tensions ❌** |
| 9 evidence-digest | `scaffold.md`, `prompt-decomposition.json`, `temp/consensus-claims.json` *(if step 3 ran)*, `temp/contradiction-graph.json` *(if step 3 ran)* | ✅ / ✅ / optional / optional |
| 10 triple-draft | `scaffold.md`, `prompt-decomposition.json`, `temp/evidence-digest.md`, `comparisons.md`, `temp/source-tensions.json`, `temp/coverage-gaps.md` *(if exists)* | **evidence-digest ❌** (step 9 makes it), **comparisons ❌, source-tensions ❌** |
| 11 synthesize | `scaffold.md`, `prompt-decomposition.json`, `temp/draft-{a,b,c}.md`, `comparisons.md`, `temp/source-tensions.json`, `temp/evidence-digest.md`, `query-<tag>.md` | drafts come from step 10; **comparisons ❌, source-tensions ❌** |
| 12 critics | `scaffold.md`, `prompt-decomposition.json`, `notes/final_report_<tag>.md`, `query-<tag>.md` | report comes from step 11 |
| 13 gap-fetch | `scaffold.md` | ✅ |
| 14 patcher | `scaffold.md`, `notes/final_report_<tag>.md`, `temp/evidence-digest.md`, `query-<tag>.md` | from earlier steps |
| 15 polish | `notes/final_report_<tag>.md`, `query-<tag>.md` | from earlier steps |
| 16 readability | `scaffold.md`, `notes/final_report_<tag>.md` | from earlier steps |

## Verdict

**Steps 8–16 cannot run untouched.** Three artefacts from the skipped steps are hard file
dependencies, read by path with no provenance check:

- `research/loci.json` (step 4) — required by step 8
- `research/comparisons.md` (step 6) — required by steps 8, 10, 11
- `research/temp/source-tensions.json` (step 7) — required by steps 8, 10, 11

Step 3's two artefacts are explicitly conditional (`if step 3 ran`) and are therefore genuinely
optional. `temp/coverage-gaps.md` is conditional too.

**But the orchestrator reads these as files and does not verify how they were produced.** So the
choice is between *backfilling* steps 3–7 and *substituting* equivalent content from the audit
trail. The substitution is chosen, and the mapping is recorded in `PIPELINE_SUBSTITUTION_MAP.md`
alongside this file.

**Why substitution rather than backfill.** Steps 3–7 exist to discover contradictions, depth loci
and expert tensions from a fresh corpus. G0 and G0.5 already did that work, by targeted means and
to a higher standard than a re-derivation would reach: six kill-checks each with a falsifier
committed *before* the finding, forty-odd ledger rows with per-source read-depth recorded, and
full-text reads of the load-bearing papers. Re-running steps 3–7 would re-derive known findings in
a lossier format — the pipeline's own artefacts are summaries, whereas the audit files carry the
underlying evidence and the access gaps. Backfilling would also risk the re-derivation *disagreeing*
with the audit on some detail, which would then have to be adjudicated for no benefit.

The cost of substitution is that the artefacts are hand-authored rather than agent-derived, so any
bias in the audit propagates into the pipeline instead of being independently re-found. That is
accepted and stated here rather than hidden; the step-12 critics are briefed to attack the audit's
own conclusions, which is the mitigation.
