# Kill-check E1 — Andrews, arXiv:2608.05015

Target claim: **S4** (with consequences for **C2** and **C3**).
Brief under test: `docs/F3-PLAN-ORIGINAL.md`, sections "Secondary claim (C2)" and
"What kills this paper".

The brief asserts three things about Andrews, *Revealed Rationality: Label-Free Evaluation
and Regularization from Representation Theorems*:

1. he proposes `1 − CCEI` as a **training-time** penalty, *in theory only*;
2. he runs **no experiments**;
3. he **explicitly declines to answer** whether coherence is sufficient for good behaviour.

The paper's positioning instruction — "cite him prominently and position as the empirical
complement, not the originator" — is downstream of all three.

---

## Falsifier (stated before the finding)

Written before reporting what the paper contains. Any **one** of the following, found in the
full text, kills the brief's characterisation:

- **F1 (kills "no experiments").** Any run of the proposed procedure on an actual model:
  elicited choices, a computed CCEI/Dutch-book/SARSEU number produced by the author rather
  than quoted from someone else's paper, a figure, a results table, a simulation, a pilot, or
  a released codebase reporting numbers. Reporting *other people's* numbers in a related-work
  paragraph does **not** count.
- **F2 (kills "training-time only").** Any proposal, sketch, or explicit gesture toward an
  **output-side** mechanism: projecting, repairing, correcting, re-sampling, re-ranking,
  constrained decoding, post-processing, best-of-n filtering, or a supervisor/critic loop that
  modifies the model's choices at inference time rather than modifying its weights. A single
  paragraph saying "one could also enforce this at generation time" is enough to kill it.
- **F3 (kills "declines to answer the sufficiency question").** Any passage where he takes a
  substantive position on whether coherence implies good behaviour — in either direction —
  rather than setting the question aside as out of scope.
- **F4 (kills the framing more broadly).** Anything that pre-empts an inference-time projection
  paper: naming projection-onto-the-GARP-set as his own future work, an existence/uniqueness
  result for the projection, or a cited third-party paper that already performs output-side
  repair of revealed-preference violations.

If **F1 or F2** fires, S4 is **REFUTED** and the paper loses its positioning. If only **F3**
fires, S4 is damaged in its wording but the scoop risk is unchanged. **F4** does not bear on
S4 directly but is reported because it bears on C3.

---

## What the paper actually is

A 25-page single-author theory note, classified **econ.TH**, first circulated 21 Feb 2026,
this version 5 Aug 2026. Author affiliation: an economics department and NBER. It is written
as an argument-and-survey piece, not as an empirical paper. Structure:

| § | Content |
|---|---|
| 1 | Introduction — the "if and only if" argument for using representation theorems as label-free evaluation/regularization signals |
| 2 | Probabilistic coherence via de Finetti; the sure-loss magnitude `L(p)` as an LP-computable penalty |
| 3 | Preference rationality via Afriat; **`1 − CCEI` as the penalty**; Lemma 1 |
| 4 | Joint beliefs+preferences via Echenique–Saito SARSEU; `1 − E` as the penalty; Lemma 2 |
| 5 | Implementation Considerations (~1.5 pages) |
| 6 | Relation to Existing Approaches (RLHF/DPO, calibration, the diagnostic literature, consistency-as-objective, utility engineering) |
| 7 | Limitations and Conclusion |
| App. | Proofs of Lemmas 1 and 2 |
| Refs | ~50 entries, pp. 21–25 |

The original technical content is exactly **two lemmas**:

- **Lemma 1 (§3).** CCEI can equal 1 even when GARP fails, because a revealed-preference
  comparison can hold at exact budget equality. But if prices are drawn independently across
  observations from distributions with a Lebesgue density, income is fixed or drawn
  independently of prices, each choice depends only on its own observation, and budgets are
  exhausted, then **with probability one** CCEI = 1 if and only if GARP holds. The proof is a
  measure-zero argument: the tie event confines the price vector to a proper affine hyperplane.
- **Lemma 2 (§4).** For the SARSEU analogue `E`, the supremum is attained; `E` = 1 iff SARSEU
  holds; `E` is either 1 or one of finitely many payoff ratios and is computable by binary
  search over those candidates; and at fixed prices `E` is continuous on the strictly-positive
  region.

Everything else is exposition of known theorems (de Finetti 1937/1974; Afriat 1967/1973;
Varian 1982; Echenique–Saito 2015), a survey of the diagnostic literature, and positioning.

---

## Findings against each of the four questions

### 1. Does it run any experiments, simulations, or empirical demonstrations?

**No. F1 does not fire.** The brief is correct, and the margin is not close.

Evidence, in descending order of hardness:

- **Zero figures and zero rendered images across all 25 pages** (checked programmatically: no
  embedded raster or vector images anywhere; the only drawing objects in the file are the
  fraction/matrix rules on the two appendix pages). There are no results tables. The word
  "Figure" does not occur in the text at all.
- **No experiments section exists.** The section list above is complete. §5 is the closest
  thing, and it is 1.5 pages of *considerations*, not results.
- **§5 is written entirely in the conditional.** "The suggested procedure … consists of three
  steps: (1) generate synthetic choice problems; (2) elicit responses from the model;
  (3) compute the penalty." He then says the penalty "can then be reported directly as an
  evaluation metric, or used in the same way as other constraint-based penalties." Nothing is
  reported as having been done. §3's "Translation to the LLM context" is the same mood: *one
  could* present the model with a role and a budget constraint, *one could* vary prices and
  income, compute the CCEI, and penalize `1 − CCEI`.
- **Every number in the paper is someone else's.** The "Existing evidence" paragraphs at the
  end of §§2–4 are the only place empirical results appear, and each is attributed: Chen et al.
  (2023) for CCEI above 0.997 across four domains; Wen (2025) for role specialization degrading
  GARP compliance; Zhu & Griffiths (2024) and Paleka et al. (2025) for probability incoherence;
  Dembo et al. (2026) for portfolio-choice tests on **human** subjects. He also notes that
  revealed-preference tests of SEU rationality on LLM-generated data "appear not to exist" —
  an open slot he flags rather than fills.
- Normalised full-text search (ligatures folded, NFKC, whitespace-collapsed): `simulat*` = 0
  hits; "we run" = 0; "we test" = 0; "results show" = 0; "dataset of" = 0. "experiment" occurs
  twice, both times describing other authors' work.

### 2. Does it propose or gesture at an inference-time mechanism?

**No. F2 does not fire.** The brief is correct that the mechanism differs. Again the margin is
not close, though there are two adjacency risks worth naming.

- Normalised full-text search: **`projec*` = 0 hits. `repair` = 0. `decod*` = 0. "nearest" = 0.
  "test-time"/"test time" = 0. "restore" = 0. "feasible set" = 0.** These were confirmed after
  ligature folding and cross-checked against the raw extraction; the zeros are real, not a
  parser artefact.
- His stated uses are exactly two, repeated throughout: **report the penalty as an evaluation
  metric**, or **use it as a regularizer in training**. The abstract frames the contribution as
  "label-free evaluation and regularization." §5 restates it. §7 restates it: "The role of the
  penalties proposed here is measurement and regularization, not a standalone objective."
- The nearest-miss wording is in §6, RLHF paragraph, where he distinguishes his approach from
  RLHF/DPO because those "focus on generating reward signals for model training, rather than
  **enforcing coherence on the model outputs**." Read in isolation this could sound
  output-side. In context it is not: the contrast he is drawing is *reward-shaping vs.
  coherence-as-the-target*, and the mechanism for "enforcing" it is the penalty he has just
  spent three sections constructing, i.e. driving `1 − CCEI` to zero through training. He never
  specifies an operator acting on a fixed model's outputs.
- **Adjacency risk A (§6, "The diagnostic and correction literature").** He acknowledges that
  violations may be reduced "through **post-processing of model outputs**" — and attributes
  that to **Chadwick, Kahng & Kipper (2025)**, "Dutch books and money pumps: Rectifying
  vulnerabilities in LLMs through rationality" (HAR 2025). This is Andrews citing someone
  *else's* output-side correction work. It does not fire F2, but see question 4 — it fires F4.
- **Adjacency risk B (§2, "Existing evidence").** The single occurrence of the phrase
  "inference time" in the whole paper is his description of **Alur et al. (2025)**, a
  forecasting system that "reconciles disparate forecasts of the same event using a supervisor
  agent at inference time." Again: someone else's system, cited in passing, and for probability
  forecasts rather than budget-set choices.
- One more slot worth knowing about: in §6 he cites **Pres et al. (2026)**, a position paper
  proposing that cross-input consistency functions be optimised "through **hard constraints**,
  soft penalties, or posterior regularization," and says his penalties "are instances of that
  program." The hard-constraint branch of that trichotomy is the slot an inference-time
  projection would occupy. Andrews does not develop it.

### 3. What does it say about coherence implying good behaviour?

**F3 FIRES.** The brief's third clause is wrong. He does not decline the question — he answers
it, flatly and in the negative, in four separate places, and the answer is load-bearing for his
own framing.

Paraphrased position: coherence is **necessary but nowhere near sufficient**. A model that
satisfies every axiom of subjective expected utility thereby has *some* well-defined prior and
*some* well-defined utility function — but the representation theorem is silent on *which*, and
both could be terrible. Coherence of outputs is therefore, in his phrase, value-neutral in
important respects; it constrains the *form* of behaviour, not its *content*. From this he
draws the conclusion that his penalties **complement rather than replace** other evaluation
criteria and training signals, and are not a standalone objective.

The four sites:

- **Abstract**, final sentence: because coherence does not restrict *which* objective rationalizes
  behaviour, the penalties complement rather than replace other signals.
- **§1**, penultimate paragraph before the roadmap: he emphasises directly that coherence is not
  sufficient for good behaviour, with the "both could be terrible" gloss.
- **§1**, earlier, summarising the diagnostic literature: a model can satisfy axioms of
  rationality while pursuing misaligned objectives.
- **§6**, RLHF paragraph: coherence of model outputs is in important respects value-neutral, so
  his approach is not a substitute for evaluation criteria or reward signals.
- **§7**, Limitation 1, titled "Coherence is not enough."

**Two qualifications that matter for C2.** First, his answer is *a priori*, not empirical: it is
a corollary of the non-uniqueness of the rationalizing objective, asserted, never tested. He
runs nothing that would measure the strength of the coherence–competence relationship. Second,
and more important, **he answers a different question than the one C2 poses.** He answers "is
coherence *sufficient* for good behaviour?" (no). C2 asks the *directional intervention*
question: does *enforcing* rationalizability improve, leave unchanged, or degrade downstream
decision quality? Andrews is silent on that. Non-sufficiency does not imply orthogonality, and
it certainly does not imply degradation. The empirical gap C2 targets is genuinely open.

But the brief's sentence cannot survive as written. A reviewer who opens Andrews will find the
sufficiency answer in the abstract, in the introduction, and in the limitations, and will read
"explicitly declines to answer" as a misrepresentation of a paper the brief simultaneously
proposes to cite prominently. That is a bad look in a double-blind related-work section.
**Rewrite required:** he *asserts* coherence is not sufficient but never measures the
coherence–competence relationship, and never asks whether imposing coherence helps or hurts.

### 4. Anything else that would scoop or undercut an inference-time projection paper?

Nothing in Andrews scoops the projection mechanism. Several things in it raise costs. In
descending order of severity:

1. **Chadwick, Kahng & Kipper (2025) is a live threat to C3, surfaced by Andrews' own reference
   list.** Title: "Dutch books and money pumps: Rectifying vulnerabilities in LLMs through
   rationality" (5th International Conference on Human and Artificial Rationality, Paris).
   Andrews characterises it in §6 as reducing rationality violations through **post-processing
   of model outputs**. That is output-side repair of exploitability, in a rationality framework,
   published before the brief was written. It is Dutch-book/money-pump rather than
   GARP-over-budget-sets, so it is probably not a direct scoop of the projection operator — but
   the brief's C3 says two full-text sweeps returned *zero* papers that "correct, project,
   repair, or enforce" revealed-preference consistency, and this paper is a conference paper
   rather than an arXiv preprint, so an arXiv-only sweep would never have seen it. **Recommend
   spawning a follow-up check on Chadwick et al. specifically.** It is not covered by E1's remit
   and I did not fetch it.
2. **Lemma 1 is a methodological must-adopt for the S4/C4 gate, not just a citation.** It says
   CCEI can read exactly 1.0 while GARP actually fails, whenever a revealed-preference
   comparison lands on exact budget equality. Round-number or grid-sampled prices make such ties
   *likely*, not measure-zero. The brief's day-1 deliverable computes CCEI to decide whether the
   project lives or dies — if that script uses tidy prices, it can return CCEI ≈ 1.0, trip the
   "no headroom, project is dead" STOP condition, and be wrong. Andrews' fix is the elicitation
   design itself: draw prices independently from continuous distributions and require budget
   exhaustion, and then CCEI = 1 iff GARP almost surely. This should be adopted in the pilot and
   cited.
3. **Echenique (2021), "On the meaning of the critical cost efficiency index"
   (arXiv:2109.06354), is an undercut the brief does not currently carry.** Andrews cites it
   approvingly for "substantive concerns about common interpretations of the CCEI," and
   describes the money-pump indices (Echenique, Lee & Shum 2011; Smeulders et al. 2013) as
   resolving one of CCEI's natural shortcomings, since they are positive exactly when GARP
   fails — while noting they can move discontinuously in the chosen bundles. A reviewer who
   knows this literature will ask why a projection targets a CCEI-derived object at all. The
   brief cites the money-pump index but not Echenique (2021).
4. **A name collision on "minimal perturbation."** Echenique, Imai & Saito (2023, JEEA) already
   own the term **minimal perturbation index** for the SEU setting: the minimal common factor by
   which beliefs, prices, or state-utility weights must be adjusted to rationalize the data.
   Andrews discusses and then declines it as a penalty because it depends on choices only
   through the payoff ordering and is therefore piecewise constant. The brief's headline phrase
   "minimal-perturbation projection" will read to an econ audience as a restatement of an
   existing named index. This compounds the brief's own self-identified "you reinvented CCEI"
   attack, and argues for a different name.
5. **Andrews has already published the headroom argument the brief's C4 gate rests on.** In §3's
   "Existing evidence" he observes that the CCEI-above-0.997 result comes from two-good settings
   with relatively few budget sets, and that GARP-based regularization "may have more bite in
   richer settings." He then cites Wen (2025) — arXiv:2501.18190, the same source the brief uses
   for S2 — for role specialization substantially reducing GARP compliance. The brief's S2
   provenance is corroborated, which is good; but the inference "therefore there is headroom" is
   now attributable to Andrews, not to the brief.
6. **Adjacent training-side work already cited by Andrews.** Aguiar & Kashaev (2026)
   (arXiv:2603.23993) fine-tune a time-series foundation model on synthetic GARP-satisfying data
   and improve consumer-choice prediction — the brief already lists this. Kim et al. (2026)
   reduce belief-drift violations by fine-tuning on a self-consistency loss. Chandak et al.
   (2025) find RL on forecasting outcomes reduces arbitrage violations without targeting
   consistency. Yamin et al. (2026b) — arXiv:2605.08556, the brief's S3 source — is described
   here as estimating utility functions from choices and studying how to steer models toward
   user-specified objectives, which is a slightly different emphasis than the brief's "prompt
   steering fails" gloss and is worth re-reading directly.
7. **Timing and reviewer overlap.** The note has been circulating since 21 Feb 2026, not since
   5 Aug 2026 — the arXiv date is the second version. Six months of circulation in a small
   econ-theory community means the EconML reviewer pool likely knows it. The brief's guess that
   he "will plausibly submit to this same workshop" is unverifiable from the document, but the
   paper contains no venue statement and no code or data availability statement of any kind.
8. **An explicitly flagged future-work slot, which is *not* the brief's slot.** §7, Limitation 3:
   extending the joint belief-preference (SARSEU) test beyond monetary payoffs to richer
   consequence spaces such as bundles of goods. He does not name projection, repair, or
   inference-time enforcement as future work anywhere.

---

## Verdict

**BRIEF'S CHARACTERISATION HOLDS WITH QUALIFICATION.**

The two clauses that carry the positioning both survive, and survive cleanly:

- **No experiments.** Confirmed by section structure, by zero embedded images across 25 pages,
  by the absence of any results table, by the uniformly conditional mood of §5, and by the fact
  that every number in the document is attributed to another author. The paper's own novel
  content is two lemmas with measure-theoretic and polyhedral proofs. F1 does not fire.
- **Training-time / evaluation-time only, no inference-time mechanism.** Confirmed by zero
  occurrences of projection, repair, decoding, test-time, or nearest-point vocabulary after
  ligature normalisation, and by his own repeated framing of the penalties as measurement and
  regularization. The two inference-time-adjacent passages are both descriptions of third-party
  systems in related-work paragraphs. F2 does not fire.

So the brief's mechanism is genuinely distinct, the "empirical complement, not originator"
positioning is defensible, and **S4's load-bearing content is verified**.

The qualification is the third clause, and it is a factual error, not a nuance. **F3 fires.**
Andrews does not decline the sufficiency question. He answers it in the negative in the
abstract, twice in §1, in §6, and as the first item of §7's limitations, and that answer is
structural to his argument — it is why he insists the penalties complement rather than replace
other signals. The brief must stop saying he declines. The accurate and still-favourable
formulation is: *Andrews asserts on theoretical grounds that coherence is not sufficient for
good behaviour, but never measures the coherence–competence relationship and never asks whether
imposing coherence helps or hurts downstream performance.* That preserves C2's opening — the
directional intervention question really is untouched — without misrepresenting a paper the
brief plans to foreground.

One finding outside S4's remit but material to **C3**: Andrews' reference list contains
**Chadwick, Kahng & Kipper (2025)**, which he describes as reducing rationality violations by
post-processing model outputs. That is output-side repair in a rationality framework, at a
non-arXiv venue, and C3's "zero papers that correct, project, repair, or enforce" was
established by arXiv-only sweeps that could not have seen it. C3 is not killed by E1 — different
axiom system, different exploit measure — but it is no longer clean, and it needs its own check.

---

## One-line summary for docs/CLAIMS.md

E1: Andrews 2608.05015 is 25pp of econ.TH theory - 0 figures, 0 experiments, no inference-time mechanism (S4 holds); but he does NOT decline the sufficiency question, he answers no by assertion.

---

## Fetch record

| Field | Value |
|---|---|
| URL requested | `https://arxiv.org/pdf/2608.05015` |
| HTTP status | 200 |
| Redirect | none (effective URL identical to requested) |
| Bytes downloaded | 311,374 |
| Format | PDF 1.7 |
| MD5 | `a23ccbda8ecdb9032fb64f98bb0159fa` |
| Extraction | PyMuPDF (`fitz`), page-by-page `get_text()`, full document |
| Pages extracted | 25 of 25 |
| Characters / words | 50,981 / 8,004 |
| Embedded images | 0 across all 25 pages (verified via `page.get_images(full=True)`) |
| Vector drawings | 4 objects each on pp. 19 and 21 (fraction and matrix rules in the appendix proofs); none elsewhere |
| PDF metadata title | "Revealed Rationality: Label-Free Evaluation and Regularization from Representation Theorems" |
| Version identifier in text | `arXiv:2608.05015v1 [econ.TH] 5 Aug 2026`; footnote 1 gives first version 21 Feb 2026, this version 5 Aug 2026 |
| Fallbacks used | none needed; the primary PDF fetch succeeded on the first attempt |

**Completeness statement.** The full text was read end to end: body pp. 1–17 (§§1–7), appendix
proofs pp. 18–21, references pp. 21–25. Nothing was skimmed or inferred from the abstract.

**Ligature handling.** The trap was checked for explicitly. Before any term search the extracted
text was normalised — the ff/fi/fl/ffi/ffl and st ligatures folded to ASCII, en/em dashes and
curly quotes folded, soft hyphens stripped, then NFKC, then whitespace collapsed to single
spaces so that hyphenated line breaks and mid-phrase newlines could not hide a match. Every
zero-hit term reported above (`projec*`, `repair`, `decod*`, "nearest", "test-time",
`simulat*`, "restore", "we run", "we test", "Figure") was searched on that normalised string,
and each zero was independently corroborated by a second method: reading the relevant sections
in full, and by the structural checks (no figures, no results tables, no experiments section).
The one-hit terms were verified by printing surrounding context rather than trusting the count —
this is how the "inference time" hit was identified as a description of Alur et al. (2025) and
the "post-process" hit as a description of Chadwick et al. (2025), rather than as Andrews'
own proposals.
