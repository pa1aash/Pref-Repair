# Cross-locus comparisons

> **SUBSTITUTED artefact.** Not produced by step 6. Written by the S1 orchestrator from G0's six
> kill-checks and G0.5's items 1–5. Locus references point at `audit/` files rather than at
> `interim-*` vault notes, because the investigating work was done by the audit rather than by
> step 5. See `audit/HR_PARTIAL_S1/PIPELINE_SUBSTITUTION_MAP.md`.

## Tension 1: The measure that creates the headroom is the measure that destroys the instrument

- **Locus "Whether CCEI can bear individual-level inference"** ([[on-the-reliability-of-individual-economic-rationality-measurements-pmc]], `audit/ITEM2_occupants_B.md`) commits: no published ICC for CCEI reaches 0.75, and *intermethod* reliability under a presentation change (0.071–0.408) is worse than five-month test–retest (0.511/0.526).
- **Locus "Sign and identification"** (`audit/killcheck_E3.md`) commits: the strongest evidence that CCEI headroom exists at all is that holding budget sets fixed and changing only how prices are *worded* drops mean CCEI to 0.698–0.908.
- **The cross-locus dynamic:** these are the same fact, read twice. Presentation format moves CCEI a long way. Locus E3 calls that *headroom* — the thing that makes the project possible. The reliability locus calls it *low construct validity* — the thing that makes the measurement meaningless. There is no third reading available in which format sensitivity is large and the index is a stable trait. This is the single most dangerous unresolved tension in the project and it is not resolvable from the literature.
- **How the draft should engage this:** the section that motivates headroom must state the reliability finding in the same breath, and must resolve it empirically rather than rhetorically — by reporting per-model CCEI test–retest on fixed budget sets with fresh contexts *before* interpreting any dose–response. A draft that cites the framing effect as headroom without citing it as a reliability problem is one referee away from collapse.
- **Calibration:** E3 is high confidence (full text, figures independently replicated). The reliability locus is high confidence on the ICC numbers and *low* confidence on whether they transfer to models — the authors' own diagnosis is low between-subject variance, and model conditions have far more spread than their human samples. Both loci name the same thing that would change their position: a measured per-model ICC. That makes it a genuine open question and it must be flagged as one.

## Tension 2: The apparent ML consensus is an artefact, and that helps

- **Locus "Sign and identification"** (`audit/ITEM2_occupants_C.md`) commits: the two peer-reviewed ablations cited for "enforcing a total order degrades quality" compare a strict superset model class against a poorer one, and on length-controlled metrics the sign reverses — the cycle-tolerant arm loses 18 of 24 cells.
- **Locus "Does the object of intervention change the result"** commits: only a post-hoc operator on a fixed agent's own choices holds capacity and training identical across doses.
- **The cross-locus dynamic:** convergence, and it is the project's opening. The first locus establishes that no existing estimate of the coherence effect is identified; the second establishes that this design is the one that identifies it. The confound in the literature is not incidental — it is structural, because varying the coherence assumption *in a preference model* necessarily varies its expressive capacity. Only moving the intervention off the model and onto the realised choices breaks that.
- **How the draft should engage this:** this is the contribution paragraph. State the confound concretely (both papers say Bradley–Terry is their dimension-1 special case), state the length artefact, then state that a post-hoc operator has no such confound by construction. Do not frame either paper as wrong — one of their authors may review this.
- **Calibration:** high confidence, from full reads including appendices, with numbers re-derived from table regions. `audit/killcheck_E5.md` Verdict point 1 is withdrawn on this basis and the draft must not reuse its summary figures.

## Tension 3: The operator is published; the object is not

- **Locus "Occupancy of the intervention cell"** (`audit/ITEM2_occupants_A.md`, `audit/ITEM3_repec.md`) commits: minimality is closed as vocabulary — an August 2026 paper owns "isotonic projection onto a preference-defined monotone cone" with a proof — and a central-bank working paper already steers LLM economic choices toward payoff-maximising behaviour with a continuous control parameter.
- **Locus "Well-posedness and computability"** (`docs/METHOD_NOTE_Q3.md`) commits: that published projection is onto a **convex** cone with the ordering held as *input*; the GARP-consistent set is a **non-convex union over orderings**, and the guarantee that makes the convex case clean does not survive the union.
- **The cross-locus dynamic:** complication, not conflict. The occupancy locus says the words are taken and two of the three legs are taken separately. The method locus says the mathematical object is different, and names precisely where: the combinatorial half. Both are right, and the distinction is technical rather than rhetorical — which is what makes it defensible.
- **How the draft should engage this:** concede the vocabulary in the first two pages and immediately draw the technical distinction, with the convex-cone-versus-non-convex-union contrast stated explicitly. Cite the isotonic work as the closest solved analogue and as independent evidence that the order-conditional half is done. Cite the central-bank paper as the closest economics-side neighbour.
- **Calibration:** high confidence. The convexity distinction was verified against the isotonic paper's own stated precondition — that the pairwise values already induce a valid partial order — and against its handling of cycles by expert re-annotation rather than by the operator.

## Tension 4: Repair works when the operator targets the set it is graded on

- **Locus "Sign and identification"** commits: three published repairs improved or preserved quality; three worsened it.
- **Locus "Are the cycles a defect or a structure"** commits: the foil paper rejects total orders on *existence* grounds, never arguing that repair destroys information.
- **The cross-locus dynamic:** the apparent contradiction in the first locus dissolves under a distinction the second one sharpens. Every success projects onto the set its metric defines. Both failures do not — one showed participants a random subset of choices with no consistency objective and no guarantee of improvement, the other projects onto the calibration cone while being scored on conditional independence. Target alignment between operator and metric, not the direction of the intervention, is the load-bearing variable.
- **How the draft should engage this:** make this an explicit subsection, not a footnote. It is simultaneously the answer to the strongest objection and a genuine methodological contribution — it predicts *when* repair should help, which nothing in the literature currently does. Then concede the residual: three independent negatives across three axiom systems establish an adverse prior even after the distinction is drawn.
- **Calibration:** medium-high. The distinction is sound and checkable from both papers' own descriptions. What it does not do is make the prior neutral, and the draft must not claim that it does.

## Tension 5: Gradedness is taken; the dose axis is not

- **Locus "Sign and identification"** commits: a nine-level dose–response curve with an interior optimum is already published, in a peer-reviewed ICML paper, and it favours the transitive side.
- **Locus "Does the object of intervention change the result"** commits: that dose is a training-time schedule weight on a component of a learned third-party preference proxy, with no interpretation as a quantity of incoherence removed, scored by an LLM judge, and its curve never reaches either endpoint.
- **The cross-locus dynamic:** conflict on the headline, convergence underneath. The sentence "we are first to vary the degree rather than toggling on/off" is dead. What survives is that their dose is not a coherence measure, their outcome is not exogenous, and their endpoints are absent — three differences that are individually defensible and jointly decisive.
- **How the draft should engage this:** rewrite any priority claim around **object, dose metric and outcome exogeneity** before writing anything else. The banned sentence is listed literally in `docs/FRAMING.md` §7. Cite the curve as friendly precedent that the question is live at this venue's sibling conference.
- **Calibration:** high confidence — the curve is in Appendix C.4, Table 5, nine λ values, span 4.63 points, response length flat across the sweep so it is not a verbosity artefact.

---

# Step 8 corpus-critic update (post-adversarial-search)

Confidence adjustments after seven targeted gaps and three parallel fetchers. Full log in
`research/temp/corpus-critic-results.md`.

## Tension 1 — PARTIALLY RESOLVED, and it moved in the project's favour

The adversarial search found the missing evidence. **arXiv:2505.21371** measures per-model CCEI
across 100 independent runs on four fixed models. Holding the model fixed and changing only
administration format, **Qwen2.5-7B falls 0.980 → 0.739 and Llama-3.1-8B falls 0.953 → 0.841
(p < 0.01), while GPT-4o and DeepSeek-V3 are essentially unaffected.** Persona and temperature move
CCEI in none of the four.

**Effect on the committed position:** the worry was that format sensitivity and construct
invalidity are the same variable, so headroom and measurement error could not be separated. On
flagship models they *are* separable — those models' CCEI is stable across administration changes.
The human `PNAS` reliability finding does not transfer wholesale. **Confidence in "CCEI can carry a
dose axis" rises from low to medium, for flagship models specifically.**

**But the same source undercuts a different position, and the draft must carry both halves.** If
format effects live in small models and frontier models are format-stable, then the framing lever
that `docs/FRAMING.md` §6 precondition 2 relies on for headroom may not exist where it is needed.
The draft must not cite this source as reassurance about reliability without also citing it as a
threat to headroom. **This is flagged as a contradiction with the frozen framing and is reported
rather than patched** — see the session report.

## Tension 2 — STRENGTHENED

Adversarial search for a study that isolates the coherence treatment on a fixed model *and* scores
an exogenous, non-judge outcome returned **nothing**, across OpenAlex, the arXiv full-text
instrument (8+ phrasings, the most direct query returning a genuine EMPTY), four WebSearch angles,
and a re-check of all vault notes. Both anchor papers have **zero forward citations**, so nobody has
extended them into that territory either. **Confidence in the identification claim rises to high.**

## Tension 3 — STRENGTHENED, materially

The defence rests on POISE's projection being onto a *convex* cone with the ordering held fixed,
where a GARP repair needs a non-convex union over orderings. The risk was that someone had already
extended it. **POISE has zero forward citations**, confirmed four independent ways (OpenAlex
citation graph, its own `cited_by_count`, Semantic Scholar after ~6 retries against 429s, and two
full-text routes). Chadwick et al. has exactly one citation — Andrews — which explicitly
distinguishes their post-processing from its own training-time regularization and performs no
ordering search and no projection. **Confidence in the technical distinction rises to high.**

One recorded instrument gap: the arXiv full-text instrument's pagination is broken — the
`search_classic` → `search.arxiv.org` redirect drops the `start` parameter, so page 2+ silently
re-returns page 1. For one 78-hit query only the top 10 were inspected. That tail is a gap, not a
verified zero.

## Tension 5 — STRENGTHENED

No second dose–response curve found. Forward citations of both the Fed paper (two citing works,
both fetched and read: an altruism-steering paper whose dose axis is an SAE direction rather than a
coherence index, and an ultimatum-game characterisation with no dose at all) and of GARP-EFM (one
citing work, Andrews, theory-only) contain nothing closer than the already-known curve.
**Confidence that the object/dose-metric/outcome distinction is defensible rises to high.**

## Occupancy locus — confidence NOT raised, and this matters

The adversarial venue sweep found no seventh occupant, but **four of the six target venues could not
be searched at all**: ACL Anthology (client-side search widget), PhilPapers (Cloudflare 403),
EconStor (Anubis proof-of-work wall), SSRN (Cloudflare 403). The fifth, OpenReview, is
title/abstract-level rather than full text and its zeros are weak. So the absence of a seventh
occupant is **not** evidence of absence — the specific blind spot the corpus critic named, full-text
indexing, remains almost entirely unsearched precisely because full-text venues wall headless
clients. **This must appear in the final report as a live residual risk, not as a clean result.**

## Method locus — STRENGTHENED by verification, gap confirmed real

Demuynck & Rehbeck's §6 Average Quantity Error — the exact continuous quantity-perturbation
objective this project needs — is confirmed to be **sketched in two sentences, with no inequalities,
no MILP, and no complexity classification**, in contrast to their fully worked Average Price Error.
Chen, Lanier & Quah give **no** complexity result for the LS index anywhere. The open-complexity
statement in `docs/METHOD_NOTE_Q3.md` is verified correct rather than merely unrefuted, and the
worked-implementation gap the project would fill is real.
