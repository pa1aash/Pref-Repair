\section{Related Work}

\subsection{Repairing LLM preference and judgment consistency}

Repairing an AI system's incoherent preferences is not new; we concede what is occupied before
claiming what is not. At least six published systems restore some consistency property of an
LLM's choices or judgments, three at inference time. None applies such an operator to an agent's
\emph{own} choice sequence over budget sets, indexes it by a graded coherence measure, and scores
the result against a payoff into which no preference judgment enters --- that conjunction is our
claim (Table~\ref{tab:related}, Appendix~\ref{app:related-table}).

The sharpest vocabulary collision is POISE \citep{wang2026poise}: it reads pairwise labels as a
fixed partial order and returns the pool-adjacent-violators projection onto the closed convex
chain-monotone cone $\{s': s'_1\le\cdots\le s'_m\}$, with a proved Pythagorean guarantee that the
edit lands weakly closer to a posited ground truth. We concede the minimum-distance priority
unqualified. \textbf{The difference is in what can be guaranteed, not in what is computed.}
Projection onto a closed convex set is non-expansive in $L_2$, which is what licenses that
guarantee; the GARP-consistent set is a union of polyhedra, one per admissible ordering, hence
not convex, so no analogue transfers. POISE also projects a \emph{teacher's} offline training
labels rather than an agent's own choices, excludes cycles by precondition, and validates on a
68-comparison human preference vote --- and its own ablation shows the projection alone
\emph{lowering} overall quality by $0.50$ while raising consistency by $2.27$.

Three further inference-time repairs, each on a different object.
\citet{chadwick2025dutchbooks} project incoherent probability judgments onto the nearest coherent
point by quadratic program and break intransitive preferences via a polynomial-time Kemeny
approximation, nearest to ours in spirit but tested only on synthetic election data with no
downstream task-quality comparison. TrustJudge \citep{wang2025trustjudge} cuts a judge's pairwise
transitivity violations from $15.22\%$ to $4.40\%$, but repairs judgments of third-party
responses with no degree parameter. CONSISTRE \citep{sun2026consistre} enforces
transitivity/symmetry/functional-uniqueness over relation-extraction triples --- a knowledge-graph
constraint-satisfaction notion of consistency, with no budget sets and no Afriat machinery. Two
training-time systems alter the agent itself, so neither can hold capacity fixed across doses:
\citet{buchanan2026innate} fine-tune with IIA-invariance losses (moving compliance from $0.920$ to
$0.948$) with no downstream evaluation; \citet{aguiar2026garpefm} fine-tune on GARP-consistent
synthetic data.

\subsection{Coherence versus downstream competence: the open sign}

A parallel line varies the transitivity of the \emph{preference model} rather than an agent's
choices. GPM \citep{zhang2025gpm} replaces the scalar Bradley--Terry reward head with a
skew-symmetric embedding able to represent cycles; HRC/DSPPO \citep{huang2026hrc} decomposes the
preference function into transitive and cyclic components and schedules their weight through
self-play. We cite both as friendly precedent, not rivals: in both, the cycle-tolerant arm is a
strict superset model class (each states Bradley--Terry is its dimension-one special case), so
coherence is confounded with capacity by construction, and on GPM's own length-controlled metric
that arm \emph{loses} in 18 of 24 head-to-head cells.

\textbf{HRC/DSPPO already publishes a dose--response curve, and we say so before claiming
anything about grading.} Its Appendix C.4 traces nine settings of a schedule weight
$\lambda\in\{-2,\dots,2\}$ against win rate: an inverted U, interior optimum at $\lambda=+1.0$,
span $4.63$ points. Four differences separate it from ours. \emph{Object}: $\lambda$ weights a
component of a learned third-party preference proxy during training; ours acts post hoc on the
agent's own realized choices, so capacity and training are identical across doses by
construction. \emph{Units}: $\lambda$ has no reading as incoherence removed, where our
projection-distance dose does. \emph{Outcome}: every downstream number in both ICML papers is an
LLM-judge score; ours is exogenous. \emph{Endpoints}: their schedules never reach either extreme;
ours runs from the raw sequence to full rationalizability.

Our closest theoretical neighbour is \citet{andrews2026revealed}, who argues representation
theorems furnish label-free evaluation/regularization signals and proposes $1-\mathrm{CCEI}$ as a
penalty, running no experiments and proposing no inference-time operator. He states plainly ---
in the abstract, twice in \S1, and as his first limitation --- that coherence is \emph{not}
sufficient for good behaviour; that position is argued a priori and never measured, and he never
asks whether \emph{imposing} coherence helps or hurts. Ours is the empirical counterpart to a
theoretical proposal that has circulated unrun. One study already reports the qualitative shape
we look for: \citet{ouyang2025aidecisionmaker} find alignment fine-tuning's relationship to
realized capital-expenditure prediction is non-monotonic --- moderate single-dimension alignment
\emph{raises} the predictive coefficient while full composite alignment degrades it --- for a
different enforced property and no minimum-distance objective, but the shape our design is built
to detect.

\subsection{Reliability of the instrument, and a record of repair that failed}

\textbf{The sharpest objection is psychometric, and it is in \emph{PNAS}.} Across eight datasets
and $>1{,}600$ participants, \citet{nitsch2022reliability} find not one of $\sim$40 ICC estimates
for CCEI or Houtman--Maks reaches $0.75$, and that 97 participants given the chance to revise
their own inconsistent budget-set choices saw mean CCEI \emph{fall}, with test--retest reliability
dropping from $0.522$ to $0.443$. Our answer has three parts, the third a concession. First,
\emph{that revision arm is not a repair operator}: participants saw a random subset of choices,
not the violating ones, with no consistency objective and no guarantee the revised set had fewer
violations --- our operator attains rationalizability by construction and verifies it
independently. The same distinction disposes of \citet{yamin2026elicited}'s isotonic-calibration
repair, worse in 14 of 16 cells: it projects onto the monotone \emph{calibration} cone while the
metric it is graded on scores conditional independence, a different set than the one repaired.
Second, the reliability finding is diagnosed by its own authors as a between-subject-variance
problem, not measurement error (within-subject CV $\approx15\%$), with their own prescribed
remedy --- ``a manipulation (i.e., a between-groups design)'' --- being this paper's design.
Third, the concession, stated plainly: \emph{there is no answer to the third-negative-in-a-row
problem.} Adding \citet{zhu2025axiomatic}'s frozen-embedding probability-axiom enforcement
(coherence improved, held-out MSE slightly worse), three independent results across three axiom
systems point one way, and a null result here would be a fourth confirmation rather than a
discovery. We therefore carry a distance-matched null-operator control --- identical
displacement, no consistency gain --- which neither published negative had.

\subsection{Economics-side interventions on LLM choice behaviour}

The closest neighbour on the economics side is invisible to any arXiv sweep.
\citet{cook2026whatllmswant} elicit economic choices from ten open-weight models and steer them
toward payoff-maximising behaviour via personas, prompt masking, and learned control vectors with
a continuously swept coefficient --- occupying two of our three legs (intervention on an agent's
own economic choices, continuously graded strength) without Afriat machinery, a
minimum-perturbation objective, or a payoff-traced frontier; their finding that reframing and
control vectors move models while persona prompting does not corroborates our own choice of
manipulation. That choice is anchored more directly in \citet{wang2025tactics}, who find that
\emph{format}, not persona or temperature, moves the Afriat index across four models: collapsing
multi-turn elicitation to single-turn drops CCEI by up to $0.241$. We adopted this mechanism as an
experimental arm on that evidence, and \textbf{it yields the cleanest result we obtain}:
splitting rounds into separate calls at 1.5B collapses the GARP pass rate from $0.40$ to $0.10$
($p=0.0073$) with zero discards --- confirming, in a different model family, the literature's own
strongest lever outperforms our purpose-built framing manipulation.
