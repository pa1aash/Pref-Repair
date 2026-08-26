<!--
================================================================================
LENGTH DECISION, RESOLVED 2026-08-26 (by the session that also built the LaTeX draft).
This file is the source of record: every paper, number and positioning argument the
drafting agent verified, uncompressed. It was not pasted into tex/paper.tex as-is
(~3 typeset pages, and only ~1 page of main-text budget remained after Parts
One/Three/the rest of Part Four). A compressed version (~1.3 typeset pages) was
written directly into tex/paper.tex's Related Work section, built from this file
using the ranked trim list below plus additional compression beyond it, because the
list's own reductions did not close the gap. Preserved verbatim in the compressed
version, per the do-not-cut set: all four HRC/DSPPO differences, the full
convex-vs-non-convex-union argument for POISE, and all three parts of the Nitsch
answer including the concession. Cut beyond the ranked list: LLM-RankFusion's prose
paragraph (kept in the comparison table only, now in Appendix B of the paper), most
supporting statistics for GPM (18/24 cells, length inflation detail — kept as one
summary sentence), and secondary connective prose throughout. See
tex/paper.tex \S2 for the shipped text; see docs/RELATED_WORK_COMPRESSED.md for the
intermediate compression pass. Nothing in the required-coverage list (six occupants,
both failed-repair papers, Andrews, R41, arXiv:2505.21371, arXiv:2406.01168, the
three most-dangerous comparisons) was dropped — every one is still named and
characterized in the shipped version, at lower prose-per-paper density.
================================================================================

OPERATOR NOTE — coverage audit for docs/RELATED_WORK.md (not for the paper prose)
Written 2026-08-26. Delete this comment block before pasting into the LaTeX draft.

SOURCE PROVENANCE, per required paper.

SOLID (read-in-full source material available in-repo; every claim and number in
the prose below traces to one of these, and none was invented):
  * POISE / TrustRoboReward, arXiv:2608.08491 — audit/ITEM2_occupants_A.md §B
    (read cover-to-cover, tables re-rendered at 170dpi and column-checked).
  * HRC/DSPPO, arXiv:2605.17342 (ICML 2026) — audit/ITEM2_occupants_C.md §B.
  * GPM, arXiv:2410.02197 (ICML 2025) — audit/ITEM2_occupants_C.md §A.
  * Nitsch et al., PNAS 2022 — audit/ITEM2_occupants_B.md §A.
  * Yamin et al., arXiv:2602.06286 — audit/ITEM2_occupants_B.md §B.
  * Andrews, arXiv:2608.05015 — audit/killcheck_E1.md (full 25pp text).
  * Cook, Kazinnik, Modig & Palmer, FEDS 2026-006 — audit/EXTRACT_KCFED.md.
  * Wang et al., arXiv:2505.21371 — audit/EXTRACT_2505_21371.md.
  * LLM-RankFusion, arXiv:2406.00231 — audit/ITEM2_occupants_A.md §A.

  * CHADWICK, KAHNG & KIPPER (2025) — BETTER SOURCED THAN THE BRIEF ASSUMED.
    The drafting brief anticipated this HAR 2025 paper would be known only from
    Andrews' reference list. It is not: the vault holds a full manual pymupdf
    extraction of the 19-page PDF from the author's own site
    (research/notes/dutch-books-and-money-pumps-rectifying-vulnerabilities-in-llms
    -through-rationali.md, source https://ansonkahng.com/docs/papers/llmrationality.pdf),
    and audit/REFERENCE_LEDGER.md row R13 records it `verified` / "read in full".
    Everything asserted below — the QP minimal-distortion projection onto the
    coherent simplex, Iterative Max Di-Cut as a polynomial-time Kemeny
    approximation, the ABSENCE of any downstream task-quality evaluation, and the
    fact that the transitivity experiments run on SYNTHETIC election data rather
    than LLM-derived data — comes from that full text. The fallback wording the
    brief authorised ("known only by citation in Andrews (2026)") is deliberately
    NOT used, because it would understate what we actually know. No web fetch was
    needed and none was performed.

  * arXiv:2406.01168 — ALSO FOUND, in the vault, as a full-text note
    (research/notes/240601168-ai-as-decision-maker-ethics-and-risk-preferences-of-
    llms.md). Ouyang, Yun & Zheng, "AI as Decision-Maker: Ethics and Risk
    Preferences of LLMs" (econ.GN, v3 10 Jun 2025). The C-4 non-monotonicity is the
    capital-expenditure result in its Section IV: single-dimension Honest alignment
    lifts the predictive coefficient on realised capex intensity to 0.5346 (p<0.01)
    against a base-model 0.0607, while full composite HHH alignment degrades it to
    0.2969 (n.s.). Characterised honestly as a training-time ALIGNMENT intervention,
    not a consistency-axiom repair: the paper contains no GARP/WARP/SARP and no
    minimum-distance objective.

THINNER (characterised from vault full-text notes, not from an independent
adversarial re-read of the PDF; claims made are correspondingly conservative):
  * TrustJudge, arXiv:2509.21117 — research/notes/trustjudge-inconsistencies-of-
    llm-as-a-judge-and-how-to-alleviate-them.md. The 15.22%->4.40% and accuracy
    figures come from that note. Cross-referenced against POISE's own Table 3
    TrustJudge-placement ablation (audit/ITEM2_occupants_A.md §B).
  * CONSISTRE, arXiv:2607.24312 — research/notes/consistre-a-unified-consistency-
    aware-framework-for-document-level-relation-extr.md. VERIFIED BY READING, not
    assumed: it is document-level relation extraction, the axioms are transitivity/
    symmetry/functional-uniqueness over knowledge-graph triples, there is no budget
    set and no GARP. A genuinely different consistency notion, as the brief guessed.
  * Buchanan & Foster, arXiv:2607.26288 — research/notes/the-innate-economic-
    preferencesof-language-models.md. VERIFIED BY READING: the brief's guess that
    it is "likely NOT a repair/intervention paper" is HALF WRONG. Part 1 is
    measurement (six revealed-preference diagnostics over 12 models); Part 2 is a
    real training-time intervention (fine-tuning with reflexivity/IIA/invariance
    loss terms, IIA 0.920 -> 0.9484 at one risk target, 0.800 at another). It
    reports no downstream task evaluation, which is the gap it leaves open. The
    prose reflects what the paper contains, not the brief's guess.

NOTHING UNFOUND. Every paper on the required-coverage list has a real in-repo
source. No characterisation below is a guess or an extrapolation.

BANNED-SENTENCE CHECK (FRAMING.md §8), run against the final prose:
  1. "Nobody repairs / corrects / projects ..."                   ABSENT
  2. "We are the first to vary the degree of coherence ..."       ABSENT
  3. "The coherence-competence question is open / untested."      ABSENT
     (The subsection heading "the open sign" is a different string, specified by
     the drafting brief; the banned literal does not occur.)
  4. "Andrews declines to answer whether coherence is sufficient" ABSENT
     Replaced throughout by the E1-corrected characterisation.
  5. "Enforcing a total order is known to degrade downstream ..." ABSENT
  6. "minimal perturbation index" as OUR coinage                  ABSENT
     The phrase occurs once, explicitly attributed to Echenique, Imai & Saito, which
     FRAMING.md §8 permits; our own object is named the non-linear Least Squares
     index. Verified by grep.

LENGTH — FLAGGED OVERAGE, REPORTED NOT SILENTLY FIXED.
The drafting brief asked for 1 to 1.5 typeset pages. This section is ~2,190 words
of prose plus a ~170-word table, i.e. roughly 3 typeset NeurIPS pages. Four
compression passes were run; the residual length is not padding but mandated
coverage. The brief required (a) all six G0 "occupant" systems named and
characterised, (b) both failed-repair papers with FRAMING.md 6.3's three-part
positioning, (c) Andrews, R41, arXiv:2505.21371 and arXiv:2406.01168, and (d) the
three most dangerous comparisons each given their own flagged paragraph with
FRAMING.md's required positioning — 6.2 alone specifies four load-bearing
differences that must all appear. Twenty papers at ~60 words each is ~1,200 words
before any positioning argument is made. Cutting to 1.5 pages therefore means
dropping mandated content, which is a scope decision for the operator, not one to
make silently inside a drafting step.

RANKED TRIM LIST, if the LaTeX step must hit 1.5 pages. Cut from the top; each item
is scoped so it can be removed without breaking a sentence that follows.
  1. (~110 w) Reliability subsection, "Two debts remain" — Echenique 2021 + Back to Blackwell. Both are
     FRAMING.md 6.4 "also required, LOWER RISK". Cheapest real cut. If cut, move the
     Least-Squares-index naming sentence into the Method section, where it belongs
     anyway, so the R15/R27 name-collision defence is not lost.
  2. (~100 w) Economics-side subsection, final sentences — Wen 2025 and Chen et al. 2023 corroboration plus
     the Bronars sentence. Not on the required-coverage list; Bronars can be cited
     once in Method instead.
  3. (~95 w) open-sign subsection, Ouyang/arXiv:2406.01168. REQUIRED coverage, so prefer shortening to
     one sentence ("a training-time alignment intervention already reports a
     non-monotonic relationship between an enforced property and realised capital
     expenditure") over deleting.
  4. (~85 w) repair subsection, LLM-RankFusion. NOT one of the six required occupants; it can be
     dropped from the prose and kept only as a table row.
  5. (~55 w) repair subsection, the two POISE dissociations. Cut LAST — FRAMING.md 6.1 says
     explicitly that this "should be used", and it is the paper's best evidence that
     the coherence/competence sign is unsettled inside a pro-projection paper.
  DO NOT CUT: any of the four HRC/DSPPO differences (6.2 requires all four); the
  convex-vs-non-convex-union argument (6.1's whole defence); any of the three parts
  of the Nitsch answer, especially the third — FRAMING.md 6.3 requires the
  concession be stated plainly, and deleting it would be the one edit here that
  changes the paper's honesty rather than its length.

BIBKEYS: see docs/RELATED_WORK_BIBKEYS.md.
================================================================================
-->


\section{Related Work}

\subsection{Inference-time and training-time repair of LLM preference consistency}

Repairing an AI system's incoherent preferences is not new, and we concede what is occupied
before claiming what is not. At least six published systems restore some consistency property
of an LLM's choices or judgments, three at inference time, one by a formally minimal projection
with a proof attached. None applies such an operator to an agent's \emph{own} choice sequence
over budget sets, indexes it by a graded coherence measure, and scores the result against a
payoff into which no preference judgment enters. That conjunction is our claim.

The sharpest vocabulary collision is POISE \citep{wang2026poise}. It reads pairwise labels as a
partial order, takes a linear extension, and returns $\arg\min_{s'}\sum_i(s'_i-s_{r_i})^2$
subject to $s'_1\le\cdots\le s'_m$ by pool-adjacent-violators; its appendix identifies this as
the metric projection onto a closed convex chain-monotone cone and proves that the edit lands
weakly closer to a posited ground truth. That is a genuine minimum-distance projection onto a
preference-defined set, and we concede the priority unqualified. \textbf{The difference is in
what can be guaranteed, not in what is computed.} Projection onto a closed convex set is
non-expansive in $L_2$, and that property is what licenses the closer-to-truth theorem. The
GARP-consistent set is not convex --- it is a union of polyhedra, one per admissible ordering
--- so projection onto it is not non-expansive and no analogue transfers. The rest is scope:
POISE projects a \emph{teacher's} score labels over a training corpus offline, so nothing an
agent chose for itself is touched; cycles are excluded by precondition and repaired by hand,
though cycles are what a GARP repair exists to remove; $m\le3$; and validation is a
68-comparison three-annotator preference vote on generated video. Two dissociations sit
unremarked in its own tables: the projection alone lowers overall quality by $0.50$ while
raising consistency by $2.27$, and its best-overall configuration is \emph{less} self-consistent
than the one it beats.

Three further systems repair at inference time. \citet{chadwick2025dutchbooks} add a rationality
layer to a frozen model, pushing incoherent probability judgments to the nearest coherent point
by a quadratic program against the model's own stated probabilities and breaking intransitive
preferences by Iterative Max Di-Cut, a polynomial-time Kemeny approximation; this is nearest to
ours in spirit, an arXiv-only search misses it, and its evaluation stops at mechanical
restoration --- the transitivity experiments use synthetic election data, and task quality is
never compared before and after. TrustJudge \citep{wang2025trustjudge} cuts a judge's pairwise
transitivity violations from $15.22\%$ to $4.40\%$ while agreement with gold labels rises, but
repairs evaluations of third-party responses and has no degree parameter. CONSISTRE
\citep{sun2026consistre} enforces transitivity, symmetry and functional uniqueness over
document-level relation-extraction triples, finding that generic self-reflection lowers F1
where axiom-targeted repair raises it; the axioms are constraint satisfaction over a
knowledge-graph output space, with no budget sets and no Afriat machinery. LLM-RankFusion
\citep{zeng2024rankfusion} repairs transitivity in relevance judgments against independent TREC
labels --- the strongest exogenous metric here --- but explicitly rejects the minimum-distance
rule, Kemeny aggregation, as NP-hard. Two training-time systems alter the agent, so neither
can hold capacity fixed across doses: \citet{buchanan2026innate} show an LLM's generation rule
is isomorphic to a random-utility discrete-choice model, find IIA the weakest of six
revealed-preference axioms across twelve models, and fine-tune with invariance losses that move
held-out IIA compliance from $0.920$ to $0.948$ at one risk target and to $0.800$ at another,
with no downstream evaluation; \citet{aguiar2026garpefm} fine-tune on GARP-consistent synthetic
data.

\begin{table}[t]
\centering\small
\caption{Where prior repair systems sit. \emph{Own choices}: the repaired object is a choice the
agent made for itself from a budget set, not a judgment about third-party items.
\emph{Exogenous payoff}: an outcome into which no preference judgment enters.}
\begin{tabular}{lcccc}
\toprule
& Own & Exogenous & Graded & Min.-distance \\
& choices & payoff & dose & projection \\
\midrule
POISE \citep{wang2026poise}                       & no  & no  & no  & \textbf{yes} \\
Rationality layer \citep{chadwick2025dutchbooks}  & no  & no  & no  & \textbf{yes} \\
TrustJudge \citep{wang2025trustjudge}             & no  & no  & no  & no \\
CONSISTRE \citep{sun2026consistre}                & no  & partial & no & no \\
LLM-RankFusion \citep{zeng2024rankfusion}         & no  & \textbf{yes} & no & no (declined) \\
Innate preferences \citep{buchanan2026innate}     & \textbf{yes} & no & no & no \\
HRC/DSPPO \citep{huang2026hrc}                    & no  & no  & \textbf{yes} & no \\
Control vectors \citep{cook2026whatllmswant}      & \textbf{yes} & no & \textbf{yes} & no \\
\midrule
This paper                                        & \textbf{yes} & \textbf{yes} & \textbf{yes} & \textbf{yes} \\
\bottomrule
\end{tabular}
\end{table}

\subsection{Coherence versus downstream competence: the open sign}

A parallel line varies the transitivity of the \emph{preference model} rather than of an
agent's choices. GPM \citep{zhang2025gpm} replaces the scalar Bradley--Terry reward head with a
skew-symmetric preference embedding able to represent cycles; HRC/DSPPO \citep{huang2026hrc}
decomposes the preference function into transitive and cyclic components and schedules their
relative weight through self-play. We cite both as friendly precedent on a neighbouring
question, not as rivals.

\textbf{HRC/DSPPO already publishes a dose--response curve, and we say so before claiming
anything about grading.} Its Appendix~C.4 traces nine settings of a schedule parameter
$\lambda\in\{-2,\dots,2\}$ against length-controlled AlpacaEval win rate: an inverted U,
interior optimum at $\lambda=+1.0$, monotone decline into the cyclic-first regime, span $4.63$
points at flat response length. Four differences separate that curve from ours.
\emph{Object}: $\lambda$ is a training-time schedule weight on a component of a learned
third-party preference proxy, where our operator acts post hoc on the agent's own realised
choices, so capacity, training and policy are identical across doses by construction --- the
comparison a training-time schedule cannot make. \emph{Units}: $\lambda$ carries no reading as
how much incoherence was removed, where a dose indexed by projection distance and the Afriat
efficiency index does, and is comparable across agents and model families. \emph{Outcome}:
every downstream number in both ICML papers is an LLM-judge win rate or preference-agreement
score, and no exogenous metric appears in either. \emph{Endpoints}: both components are present
at every $\lambda$ and all schedules converge, so the curve reaches neither extreme, where ours
runs from the raw sequence to full rationalizability.

These papers also fix the prior we work against. The cycle-tolerant arm in both is a strict
superset model class --- each states Bradley--Terry is the dimension-one special case --- and
GPM's additionally receives a context-conditioning gate worth more, by its own ablation, than
the entire headline margin, so coherence is confounded with capacity by construction. On GPM's
own length-controlled metric that arm loses in 18 of 24 head-to-head cells and all eight
final-iteration cells, its gains confined to raw win rates at up to $65\%$ greater length, and
HRC's unified-codebase retraining --- the best-controlled replication available --- finds the
arms indistinguishable downstream (9/8/1 over 18 cells). We therefore frame our contribution as
identification rather than replication: existing comparisons either confound coherence with
capacity, or score the outcome with another preference judgment, or both.

Our closest theoretical neighbour is \citet{andrews2026revealed}, who argues that
representation theorems furnish label-free evaluation and regularization signals and proposes
$1-\mathrm{CCEI}$ as a metric or training-time penalty. The note runs no experiments, contains
no inference-time operator, and attributes every number in it to another author. It states
plainly --- in the abstract, twice in the introduction, and as the first of its limitations ---
that coherence is \emph{not} sufficient for good behaviour, since a representation theorem
constrains the form of behaviour rather than its content. That position is argued a priori and
never measured: the note nowhere estimates the strength of the coherence--competence
relationship, and nowhere asks whether \emph{imposing} coherence helps or hurts. Ours is the
empirical counterpart to a theoretical proposal that has been circulating unrun. One study already reports a
non-monotonic relationship between an enforced behavioural property and a realised external
quantity: \citet{ouyang2025aidecisionmaker} fine-tune on alignment data and predict firms'
actual capital-expenditure intensity from earnings calls, where moderate single-dimension
alignment lifts the predictive coefficient to $0.5346$ ($p<0.01$) against a base-model $0.0607$
while full composite alignment degrades it to $0.2969$ and insignificance. The enforced property
is alignment compliance, not a revealed-preference axiom, and no minimum-distance objective
appears --- but that shape is what our dose--response is built to detect, and it is why we
pre-commit to no sign.

\subsection{Reliability of revealed-preference instruments, and a record of repair that failed}

\textbf{The sharpest objection to this design is psychometric, and it is in \emph{PNAS}.}
Across eight datasets and over 1{,}600 participants, \citet{nitsch2022reliability} report that
not one of roughly forty ICC estimates for CCEI or Houtman--Maks reaches $0.75$; that
presentation format alone drops within-session agreement to $0.071$, worse than agreement
across a five-month gap; and that an individual's own CCEI predicts their next about twice as
badly as guessing the population mean. The same paper contains the human analogue of our
intervention, and it moved the wrong way: 97 participants given the chance to revise their own
budget-set choices saw mean CCEI and Houtman--Maks both fall, and test--retest reliability drop
from $0.522$ to $0.443$.

Our answer has three parts of decreasing strength, the third a concession. First and strongest,
\emph{that revision arm is not a repair operator}: participants saw a \emph{random} subset of
ten of forty choices rather than the violating ones, were never told which were inconsistent,
and were given no consistency objective, so nothing guaranteed --- or attempted --- that the
revised set had fewer violations. It is an invitation to reconsider, not a projection; our
operator attains rationalizability by construction and verifies it by an
independent combinatorial GARP check. The same distinction disposes of the second published
negative: \citet{yamin2026elicited} apply isotonic calibration to elicited LLM beliefs and find
their target statistic worse in 14 of 16 cells, by up to a factor of $4.4$, and eliminated in
none --- but isotonic regression projects onto the monotone \emph{calibration} cone while the
metric scores conditional independence, so it repairs a different set than the one it is graded
on. Second, at medium strength, the reliability finding is a between-subject variance problem
rather than measurement error: Nitsch et al. diagnose it so themselves, reporting a
within-subject coefficient of variation near $15\%$ for CCEI at twenty or more trials, and
prescribe increasing individual differences ``using a manipulation (i.e., a between-groups
design)'' --- which is this paper's design. ICC is a property of the population, not the
instrument, and their participants cluster near ceiling where our conditions do not; we measure
this on the models rather than asserting it. Third, the concession, stated plainly: \emph{there
is no answer to the third-negative-in-a-row problem.} Adding \citet{zhu2025axiomatic}, who
enforce the additive probability axiom on a frozen model's embeddings and report slightly worse
held-out MSE despite strictly better coherence, three independent results across three axiom
systems point one way. The prior is not neutral, and a null here would be a fourth confirmation
rather than a discovery. We therefore carry a distance-matched null-operator control ---
identical displacement, no consistency gain --- which neither published negative had, and
without which any payoff change is confounded with having moved the bundles at all.

Two debts remain. \citet{echenique2021ccei} raises substantive concerns about how the CCEI is
ordinarily interpreted, so we report violation counts alongside the index and name the quantity
we minimise not as a coinage of ours but as the non-linear Least Squares index of
\citet{varian1985}, catalogued by \citet{chen2024goodness} and distinct from the minimal
perturbation index of \citet{echenique2023minimal}. \citet{zhang2026blackwell} press the
opposite normative case, that intransitivity of multi-objective preference should be accepted
rather than removed, since projecting onto a single acyclic order is scalarisation; if their
diagnosis of the source is right our operator is their losing baseline, so we treat it as
empirical and report a Condorcet-existence check beside every efficiency index.

\subsection{Economics-side interventions on LLM choice behaviour}

The closest neighbour on the economics side is invisible to any arXiv sweep.
\citet{cook2026whatllmswant} elicit economic choices from ten open-weight models in dictator and
McCall search environments, test whether the resulting policies are rationalizable by a
reservation-wage model, and steer behaviour toward payoff-maximising choices via personas,
prompt masking, and learned control vectors added into each layer's forward pass at inference
with a continuously swept coefficient. Two of this paper's three legs --- intervention on an
agent's own economic choices, and a continuously graded intervention strength --- are therefore
already occupied by a central-bank working paper. Absent there are Afriat machinery of any kind
(the rationalizability test is a bespoke three-part switching-regime criterion, not GARP), a
minimum-perturbation objective, a coherence-indexed dose, and a frontier traced against a
payoff: the outcome is the model's own self-reported allocation, judged by whether it moved in
the theory-predicted direction. Their finding that reframing and control vectors shift models
reliably while persona prompting has limited impact independently corroborates our choice of
manipulation.

That choice is anchored more directly in \citet{wang2025tactics}, who cross four models against
eight elicitation tactics on twenty-five-round budget-set tasks and find that \emph{format},
not persona or temperature, moves the Afriat index: persona has no significant effect on any
model and temperature none across a full sweep, while collapsing a multi-turn elicitation into
a single turn drops CCEI by up to $0.241$ for Qwen2.5-7B and $0.212$ for Llama-3.1-8B, the two
larger models being essentially unmoved. We adopted that mechanism as an experimental arm on
this evidence, and \textbf{it yields the cleanest result we obtain}: splitting each round into
a separate sequential call at the 1.5B scale collapses the GARP pass rate from $0.40$ to $0.10$
($p=0.0073$) with zero discarded sessions on either side, a larger and better-identified effect
than our own price-reframing manipulation produced at the same scale. We therefore cite that
work not only as design justification but as a literature finding our data confirm, in a
different model family and on a violation-count metric rather than the index alone --- which
sharpens a caution running through this paper, that across every manipulation we ran the GARP
pass rate carried the framing and format signal while CCEI, compressed near one, did not. \citet{wen2025specialization} corroborates that elicitation conditions rather than capacity
govern measured rationality, reporting role specialization substantially reducing GARP
compliance; and \citet{chen2023emergence}'s near-ceiling CCEI values above $0.997$ come from
two-good settings with few budget sets --- the regime in which, as \citet{andrews2026revealed}
observes, a GARP-based signal has least bite. We therefore report Bronars power
\citep{bronars1987power} and a random-agent benchmark beside every efficiency index.
