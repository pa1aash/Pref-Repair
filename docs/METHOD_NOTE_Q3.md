# Method note Q3 — the projection problem's actual formulation

Resolves open question Q3 (`docs/OPEN_QUESTIONS.md`) and re-states claims S8 and S9
(`docs/CLAIMS.md`). This is a formulation note, not code. Everything asserted here is
sourced; every access failure is recorded in the fetch record at the end.

**Headline.** The fixed-ordering alternating scheme is **heuristic-only**. It has no
local-optimality guarantee, no bound on its gap, and — as literally described in Q3 — it does
not even do what it claims, because fixing the ordering does *not* remove the bilinearity. It
should not be used. It also is not needed: the projection problem is a **named, published
index** (the non-linear Least Squares index) and there is a **published multiplier-free
mixed-integer linear formulation** that makes it a MILP with no bilinear term anywhere. The
one genuine hazard is not bilinearity and not complexity — it is that the GARP-consistent set
**is not closed**, so the minimum may not be attained at all.

---

## The question, precisely stated

Observed data `D = (p_t, x_t)_{t≤T}`, prices `p_t ∈ R^K_++`, bundles `x_t ∈ R^K_+`, which
violates GARP. Wanted: the nearest rationalisable dataset that keeps the same budget sets.

> Find `x̃ = (x̃_t)_{t≤T}` minimising `Σ_t (x_t − x̃_t)' W_t (x_t − x̃_t)`
> subject to `x̃_t ∈ B(p_t, p_t·x_t)` for every `t` — i.e. `p_t·x̃_t ≤ p_t·x_t` —
> and `(p_t, x̃_t)_{t≤T}` satisfies GARP.

This is not a new object. Chen, Lanier & Quah (arXiv:2405.08464, read in full) define exactly
this and call it the **non-linear Least Squares (LS) loss function**:

> `LS(U; D) = inf { Σ_{t=1..T} (q_t − q̃_t)' W^t_D (q_t − q̃_t) : (q̃_t, p_t)_{t≤T} is
> rationalized by U and q̃_t ∈ B(p_t, p_t·q_t) }`, with the LS index `LS(D) = inf_U LS(U; D)`.

Because a dataset is rationalisable iff it satisfies GARP (Afriat's theorem), `inf_U` and the
GARP constraint are the same thing, and their `LS(D)` is the project's projection distance
verbatim, weighting matrix and budget restriction included. Smeulders, Crama & Spieksma's
survey traces the idea to **Varian (1985)**: "the goal is here to find a dataset which does
satisfy the conditions and is only minimally different from the observed dataset."

The audit's framing of Q3 contains one error worth correcting before anything else.

**With the data fixed, the Afriat inequalities are already a linear program — no ordering
search is required.** In `U_i ≤ U_j + λ_j·p_j·(x_i − x_j)`, the coefficient `p_j·(x_i − x_j)`
multiplying `λ_j` is a *number* when `x` is data. The system is therefore linear in `(U, λ)`
jointly, with no fixed ordering and both blocks free. This is Afriat (1967) as restated by
Diewert (1973), and the survey draws the standard conclusion from it: "Afriat (1967a) provided
a linear program, formed by the Afriat Inequalities, that characterizes rationalizability. This
allows us to conclude that garp can be tested in polynomial time."

So the bilinearity is not created by leaving the ordering free. It is created **entirely** by
promoting `x̃` to a decision variable, which turns `λ_j·p_j·x̃_i` into a product of two
unknowns. And that product is *unaffected* by fixing the ordering: knowing the sign of
`U_i − U_j` tells you nothing about `λ_j·p_j·x̃_i`. **Fixing the ordering does not linearise
the projection problem.** Section 3 turns on this.

---

## Why measurement is easy and construction is not

This distinction is the load-bearing one for the whole project, and it should be stated
explicitly in the method section.

**Measurement never touches the Afriat inequalities.** CCEI (Afriat's efficiency index) is
computed by binary search over `e ∈ [0,1]`, and each feasibility check is a purely
combinatorial GARP test on the `e`-relaxed revealed-preference relation: build the direct
relation `x_t R^e x_v ⟺ e·p_t·x_t ≥ p_t·x_v`, take its transitive closure, and check that no
pair has both `x_t R x_v` and `x_v P⁰ x_t`. Varian (1982) proposed Warshall's algorithm for the
closure, giving `O(n³)`; the survey notes matrix-multiplication closures reach `O(n^2.373)` and
that Talla Nobibon, Smeulders & Spieksma (2015) give an `O(n²)` GARP test. Nothing here is an
LP, nothing is bilinear, nothing searches orderings. Smeulders et al. (2014) close the loop by
giving an exact **polynomial-time** algorithm for Afriat's index; Dean & Martin's comparison
table lists its complexity as `P` while MCI, HMI and MPI are all `NP`.

One precision point on the binary search, from Chen, Lanier & Quah (footnote 15): "It is common
in empirical applications of Afriat's index for e* to be calculated via a binary search over the
entire interval [0,1], with e-GARP being checked at each value of e. **This approach leads to an
approximation of e* rather than its exact value.**" The exact value can be had by noting that
`e` only matters at the `O(T²)` candidate ratios `p_t·x_v / p_t·x_t`; sort those and search over
them. The day-1 script should do this. It also interacts with Q6 (Andrews' Lemma 1): binary
search on a continuum plus exact budget equality is precisely where a false 1.0 comes from.

**Construction is a different problem.** Once `x̃` is a decision variable, the object being
searched over is no longer a scalar `e` on an interval with a cheap combinatorial oracle. It is
a `K·T`-dimensional continuous variable whose value *changes the revealed-preference relation
itself* — moving `x̃_v` flips whether `p_t·x̃_t ≥ p_t·x̃_v`, so the combinatorial structure is
endogenous. There is no outer scalar to bisect. This, not bilinearity per se, is the real
difficulty, and it is why the measurement timings in `docs/COMPUTE_NOTE.md` do not transfer.

The moral for the paper: **the bilinearity of the Afriat inequalities is irrelevant to
everything the project measures, and is avoidable in the one thing it constructs.**

---

## Is the alternating scheme convergent?

**No. Heuristic-only, and weaker than the usual biconvex heuristic.** Four separate reasons,
in increasing order of severity.

**1. It is not well-defined as described.** "Fix the ordering → solve the now-linear system" is
false. As shown above, fixing the ordering leaves `λ_j·p_j·x̃_i` bilinear. To make an inner LP
you must fix the ordering *and* one of `{λ, x̃}` — a three-block alternation, not the two-block
scheme in the plan. Anyone implementing the plan as written discovers a MINLP mid-build, which
is precisely the failure Q3 was raised to prevent.

**2. Read as alternating convex search (ACS), the guarantee ceiling is a partial optimum, not a
local optimum.** Take blocks `{x̃}` and `{U, λ}`. For fixed `(U, λ)` the constraints are linear
in `x̃`; for fixed `x̃` they are linear in `(U, λ)`; the objective is convex in `x̃` and constant
in `(U, λ)`. So the problem *is* biconvex, and ACS applies. Gorski, Pfeuffer & Klamroth (2007),
*Mathematical Methods of Operations Research* 66(3), 373–407, §4.2.1, state the ceiling in their
own words before proving it:

> "we will show that under weak assumptions the set of all accumulation points generated by ACS
> form a connected, compact set C and that each of these points is a stationary point of f **but
> that no better convergence results (like local or global optimality properties) can be obtained
> in general.**"

The theorems behind that sentence:

| Result | What it gives | What it does not give |
|---|---|---|
| Thm 4.5 | `{f(z_i)}` converges monotonically if `f` is bounded below | says nothing about `{z_i}` |
| Example 4.3 | explicit biconvex `f` where `f(z_i) → 0` while `z_i → ∞` | — |
| Thm 4.7 | *if* `{z_i}` converges, the limit is a **partial optimum** | convergence is a hypothesis, not a conclusion |
| Thm 4.9 | with compactness + per-block uniqueness, accumulation points are partial optima of equal value forming a compact continuum | still only partial optima |
| Example 4.2 | a partial optimum satisfying the necessary local-optimality condition (Thm 4.4, Wendell & Hurter 1976) that **is not a local optimum** | — |

So: convergence to a point that is not a local minimum, let alone a global one, is not an edge
case — it is the guarantee. And Thm 4.4's local-optimality condition assumes **separable**
constraints `x ∈ X, y ∈ Y`. The projection problem's constraints are *jointly* constrained: the
bilinear coupling means each block's feasible section moves as the other block moves, so even
that weak necessary condition does not apply off the shelf, and ACS can stall at a point where
neither single-block move is feasible-improving purely because of the coupling.

**3. With a discrete ordering block, none of those theorems apply at all.** A set of orderings
is not a convex set and "solve for fixed `x̃`" is not a convex subproblem. What survives is only
the elementary monotone-descent argument: the objective never increases, and the ordering set is
finite, so *strict* descent forces finite termination. But strict descent is exactly what fails
under ties, and ties are the normal case here — an `L1` objective on a degenerate LP has multiple
optima routinely, and several orderings can share the same cost. **Without an explicit
anti-cycling rule (a tabu list of visited orderings, or a lexicographic tie-break), cycling among
orderings is possible and the scheme need not terminate.** Adding an anti-cycling rule restores
finite termination — to a partial optimum with no quality guarantee, which is the same place.

**4. It reports the wrong kind of number for this paper.** The projection distance *is* the
headline quantity — the dose axis of the dose–response curve. An alternating heuristic returns a
restart-dependent **upper bound** on that distance with no certificate. A branch-and-bound
solver returns an optimum with a reportable MIP gap. For a paper whose contribution is a measured
before/after difference along a measured perturbation size, that difference matters.

**Verdict:** not provably convergent in any sense the project needs. Monotone descent of the
objective value; partial optimality at best and only under hypotheses that do not hold here; no
local optimality; no bound on the gap; cycling possible absent an anti-cycling rule. Do not use
it as the primary method.

---

## What the literature already solves

Per source, what it offers, and whether it is the same problem.

### Demuynck & Rehbeck (2023), *Economic Theory*, "Computing revealed preference goodness-of-fit measures with integer programming" — **the key source; read in full**

DOI `10.1007/s00199-023-01489-x`; open working-paper version ECARES 2021-26. This is the paper
that dissolves Q3, and neither the plan nor the audit had found it.

Their move is to **drop the Afriat multipliers entirely**. Their Theorem 2: `D` satisfies GARP
iff there exist numbers `u_t ∈ [0,1]` such that for all `t, v`

```
p_t·q_t ≥ p_t·q_v   ⟹   u_t ≥ u_v          (GARP-1)
p_t·q_t >  p_t·q_v   ⟹   u_t >  u_v          (GARP-2)
```

These `u_t` are ordinal levels, not Afriat utilities — there is **no `λ`**, so there is no
`λ·x̃` product to be bilinear. They then encode the two implications with binaries `U_{t,v}`
and state the property that matters here explicitly: "the inequalities (IP-1)-(IP-4) are
**linear in utility numbers, prices, and quantities**." That is the whole resolution of Q3 in
one clause. Because the inequalities are linear in quantities, promoting `x̃` to a decision
variable keeps the program linear.

They use this to give MILPs for the Houtman–Maks index, the Average Varian index and Dean &
Martin's Minimum Cost Index, and then, in §5, for "minimal measurement error in expenditures,
prices or quantities". The quantity case — the project's problem — is named as the **Average
Quantity Error (AQE)** but only *sketched*: "one needs to introduce variables `q̃_t ∈ R^K_+`
and define GARP consistency conditional on these bundles. The Average Quantity Error (AQE) would
then consist of minimizing the mean of the errors `‖q_t − q̃_t‖` conditional on `(p_t, q̃_t)_{t≤T}`
satisfying GARP." They develop and compute the expenditure and price cases in full; the quantity
case gets two sentences, no worked inequalities, no computation, and is absent from their
conclusion. **The formulation exists in the literature; the worked, computed, budget-constrained
version does not.** That is a defensible position for the project to occupy.

Their timings: HMI, AVI and MCI on real experimental datasets of 22–79 observations per subject,
"most of the goodness-of-fit measures can be computed in less than a second while no index takes
more than 2 seconds" on a standard desktop.

### Chen, Lanier & Quah (arXiv:2405.08464, v2 Feb 2026), "Goodness-of-fit and utility estimation: what's possible and what's not" — **read in full; the most dangerous source for this project**

Names the projection problem (the non-linear LS index, above) and then attacks its
well-posedness. Two results the paper must confront:

- **Proposition 1: no goodness-of-fit index is both continuous and accurate.** The reason is
  structural: "the datasets which obey GARP do not form a closed set." One can build GARP-obeying
  `D_n → D̄` with `D̄` violating GARP. They call such boundary cases **cusp datasets**.
- **Consequence for the projection.** The Afriat, Varian, Swaps and LS indices are *continuous
  but not accurate*; Houtman–Maks is *accurate but discontinuous*. So **the LS index can report a
  distance of exactly 0 for a dataset that violates GARP**, and since the feasible set
  `{x̃ : (p, x̃) satisfies GARP}` is not closed, the infimum need not be attained by any `x̃`.
  Their Proposition 7 / §3 result is the matching statement on the estimation side: the Afriat,
  Varian, Swaps and Least Squares loss functions are accurate but **not minimizable** — `argmin`
  is empty — with Houtman–Maks the only exception.
- **The repair they supply.** Their Proposition 11 characterises the utility classes that admit
  accurate *and* minimizable loss functions generating accurate *and* continuous indices: exactly
  those whose rationalisable datasets form a **closed set**. They show the **homothetic** class
  and the **expected-utility class with concave Bernoulli functions** qualify. Restricting to
  homothetic preferences (HARP in place of GARP) makes the projection well-posed by construction.
- They also record the practical alternative: Halevy, Persitz & Zrill (2018) use the LS loss to
  estimate utility and "avoid the problems we point out here by confining utility functions to a
  parametric family."

This is the single most important source for the method section. It is also the source of the
one honest reason a reviewer could reject a naive projection: *your minimum may not exist.*

### Dean & Martin (2016), *REStat* 98(3), 524–534, "Measuring Rationality with the Minimum Cost of Revealed Preference Violations" — **working-paper version read in full**

The **Minimum Cost Index (MCI)**: "the minimum cost of breaking all revealed preference cycles
in a data set, where the cost of removing a relation is determined by the money metric."

**It is not the same problem.** MCI deletes *relations* from a fixed revealed-preference
relation; the project moves *bundles*, which changes the relation. Their decision variables are
a subset `B ⊆ R` of relations to delete; the data are untouched. Their algorithm is not an MILP:
they reduce to the **maximal acyclic set problem (MASP)**, show it equivalent to the **minimum
set covering problem**, and hand it to off-the-shelf covering solvers. They are explicit that
"the calculation of MCI is an NP-hard problem" and that brute force is hopeless — "with only
twenty observations there are over a million combinations to check, and with 40 there are more
than 1 × 10¹²". Demuynck & Rehbeck (2023) later give the MILP version (their Corollary 4, with
binaries `B_{t,v}` for the deleted relations).

Two things transfer to this project regardless. First, their complexity table: MCI `NP`, Afriat
Efficiency Index `P`, Houtman–Maks `NP`, Money Pump `NP`. Second, the **Selten score** —
measured index minus mean simulated index under uniform-random choice — which
`audit/BRONARS_NOTE.md` has already picked up and which applies verbatim to a perturbation
distance.

### Smeulders, Spieksma, Cherchye & De Rock (2014), *ACM TEAC* 2(1), Article 3 — **abstract-level only; PDF access failed on every route**

The complexity results, verified through three independent secondary sources that state them
consistently (the same authors' own 2019 survey, Dean & Martin 2016, Demuynck & Rehbeck 2023):

- **Afriat's efficiency index (CCEI) is computable in polynomial time**, for several revealed
  preference axioms. Before this, the only published algorithm was Varian's (1990)
  *approximation* algorithm.
- **Varian's (vector) efficiency index is NP-hard.**
- **The Houtman–Maks index is NP-hard.**
- **No constant-factor polynomial-time approximation exists for either, unless P = NP.** (A
  secondary source states this in the stronger `O(n^{1−δ})` form; the survey states the
  constant-factor form. The stronger form is recorded here as *unverified* because the primary
  text could not be read.)
- Hardness is obtained by reduction from independent set.

Companion: Smeulders, Cherchye, De Rock & Spieksma (2013), *JPE* 121(6), 1248–1258 — the mean
and median money-pump indices are NP-hard, while the most- and least-severe money-pump indices
are polynomial.

### Smeulders, Crama & Spieksma (2019), *EJOR*, "Revealed Preference Theory: An Algorithmic Outlook" — **read in full**

The survey that ties it together, and the only source found that discusses the projection
problem's algorithmics directly:

> "A third approach to the definition of goodness-of-fit measures was introduced by Varian (1985).
> When a dataset fails to satisfy the rationalizability conditions, the goal is here to find a
> dataset which does satisfy the conditions and is only minimally different from the observed
> dataset. **The problem of finding these minimally different rationalizable datasets can be
> formulated as a non-linear optimization problem, which, in general, is hard to solve.** To avoid
> solving large scale non-linear problems, De Peretti (2005) approaches this problem with an
> iterative procedure. Working on garp, his algorithm tackles violations one at a time, also
> perturbing only one observation at a time. [...] **While this algorithm does not guarantee an
> optimal solution**, it allows handling large datasets, especially if the number of violations is
> small."

Note carefully: "hard to solve" here is an informal remark about non-linear programming, **not a
complexity claim**. It must not be cited as one. De Peretti, C. (2005), *Macroeconomic Dynamics*
9(3), 372–397 is the named prior heuristic for this exact problem — see the recommended
formulation's fallback.

### Boodaghians & Vetta (2015), arXiv:1507.07581 / WINE 2015 — **read in full**

Sharpens the Houtman–Maks hardness with a threshold in the **number of goods**, which is
directly relevant to open question Q4:

> "for two-commodity markets the consumer rationality problem is **polynomial time solvable**;
> we prove this via a reduction to the vertex cover problem on perfect graphs. For
> three-commodity markets, however, the problem is **NP-complete**."

In general the deletion problem is equivalent in approximation to directed feedback vertex set.
Consequence: **"Houtman–Maks is NP-hard" is false at K = 2.** Any complexity claim the paper
makes must carry its `K`.

### Varian (1982, 1990) — algorithmics as reported by the survey and by Chen–Lanier–Quah

Varian (1982), *Econometrica* 50(4), 945–973: the GARP formulation, tested **combinatorially**
by transitive closure of the direct revealed-preference relation, with Warshall's algorithm
suggested for the closure. Not by solving Afriat's inequalities.

Varian (1990), *J. Econometrics* 46(1–2), 125–140: introduces the vector-valued efficiency index
`(e_1,…,e_n)` and supplies an **approximation algorithm**, not an exact one; the exact
polynomial-time algorithm for the scalar (Afriat) case had to wait for Smeulders et al. (2014),
and the vector case turned out to be NP-hard. Both remain **abstract-level only** in this repo —
paywalled, no OA copy found, consistent with `docs/OPEN_QUESTIONS.md` Q11.

Varian (1985), *J. Econometrics* 30(1), 445–458 is the origin of the minimal-perturbation
formulation per the survey. **Access failed** (see fetch record).

### Afriat (1967, 1973)

The constructive theorem and the efficiency index. The point that matters: Afriat's theorem is
in practice *checked* combinatorially, not by solving the inequality system. The survey is blunt
that both routes are polynomial and that the combinatorial route is the one people use; Demuynck
& Rehbeck concur that IP testing of GARP "is a very inefficient method to test for GARP as IP
methods are very inefficient compared to alternative available tests for GARP (either via Afriat
inequalities [Diewert, 1973] or via Warshall's algorithm [Warshall, 1962, Varian, 1982])." The
inequalities earn their keep only when you need to *build* something, which is the project's case.

### Echenique, Imai & Saito (2023), *JEEA*, "Approximate Expected Utility Rationalization" (arXiv:2102.06331) — **read in full (arXiv v1)**

**Not the same problem, and it does not own the phrase.** Their `e` measures how far the *model*
must be perturbed, not the data: "if one 'perturbs' marginal utility enough, then a dataset is
always consistent with expected utility. Our measure is simply a measure of how large of a
perturbation is needed to rationalize the data." The three equivalent readings they give are
perturbations of **beliefs, utilities, or prices** — never bundles, and never a distance in
quantity space. Structurally it is an `e`-relaxation index in the CCEI family, applied to
expected utility rather than to general GARP.

On Q8's term-collision worry: the string "minimal perturbation" occurs **zero** times in the
arXiv version; "CCEI" occurs 316 times. So the literal phrase is not theirs. But the *concept* —
a minimum-size perturbation that restores rationalisability — is thoroughly occupied, by the
Varian (1985) / Least-Squares index, by this paper's `e`, and by Demuynck & Rehbeck's AQE. The
honest conclusion for Q8 is: the phrase is free, the idea is not, and calling the quantity a
"minimal perturbation index" invites exactly the "you reinvented CCEI" attack the plan already
fears. **Recommendation: call it the LS index, or the quantity-space projection distance, and
cite Varian (1985) and Chen–Lanier–Quah for the name.** Caveat: only the arXiv version was read;
the published *JEEA* text may differ.

### The repair papers surfaced by this audit

| Work | What it does | Same problem? |
|---|---|---|
| **TrustRoboReward / POISE** (arXiv:2608.08491) | Treats pairwise labels as a **fixed partial order**, takes a linear extension, and solves chain isotonic regression `argmin Σ(s'_i − s_{r_i})² s.t. s'_1 ≤ … ≤ s'_m` by PAVA — an exact `O(m)` `L2` projection onto a monotone cone, with a proof (their Thm 1) that it weakly improves `L2` distance to ground truth | **The closest solved analogue, and the sharpest illustration of the point.** It is exactly the project's problem *conditional on the ordering being given and acyclic*. They say so themselves: cycles occur in "<1% of groups and are fixed by expert re-annotation", and their Limitations section names "extending POISE to large-scale noisy preference graphs without manual cycle repair" as future work. The moment the order must be *chosen*, PAVA's exactness evaporates. Conditional on an ordering the projection is a cheap convex problem; the whole difficulty lives in choosing the ordering. |
| **Chadwick, Kahng & Kipper (HAR 2025)** | Two halves: a voting rule (Iterative Max Di-Cut, benchmarked against Kemeny) for intransitivity, and a **quadratic program** projecting incoherent probabilities onto the coherent set, under a faithfulness constraint | The QP half is a genuine minimum-distance projection, but onto the **probability simplex with coherence constraints** — a convex set, fixed and known in advance. The GARP-consistent set is neither convex nor closed. The precedent is rhetorical, not technical. The voting-rule half is the same admission POISE makes: they solve the ordering problem with a combinatorial rule, separately. |
| **LLM-RankFusion** (arXiv:2406.00231) | ICL calibration for order inconsistency + aggregation over multiple rankers for transitive inconsistency | Aggregation, not projection. No optimisation over a distance. |
| **TrustJudge** (arXiv:2509.21117) | Distribution-sensitive scoring + likelihood-aware aggregation | Aggregation. POISE's own §2 positions itself explicitly *against* TrustJudge as "label-local" and unable to enforce a hard consistency guarantee. |
| **Innate Economic Preferences** (arXiv:2607.26288) | Training-time invariance losses (reflexivity / IIA / transitivity) | Penalty, not projection. No nearest-point problem. |
| **CONSISTRE** (arXiv:2607.24312) | Constraint-aware prompting + verification + self-reflection; and SFT+GRPO | Iterative repair loop, no optimisation formulation. |

**Nothing in the ML literature solves the joint choose-the-order-and-project problem.** Every
one of them either takes the order as given (POISE), or replaces the projection with an
aggregation rule (Chadwick et al., LLM-RankFusion, TrustJudge), or drops the minimum-distance
requirement altogether. That gap is real, and it is the economics MILP literature — not the ML
literature — that fills it.

---

## Complexity

**Established, with citations:**

| Problem | Status | Source |
|---|---|---|
| GARP test on fixed data | Polynomial: `O(n³)` by Warshall, `O(n^2.373)` by fast matrix multiplication, `O(n²)` by Talla Nobibon et al. (2015) | survey, read in full |
| Afriat feasibility on fixed data | Linear program in `(U, λ)`; polynomial | Afriat (1967), Diewert (1973), via survey |
| CCEI / Afriat efficiency index | **Polynomial** (exact) | Smeulders et al. (2014), via 3 independent secondary sources |
| Varian's vector index | **NP-hard**; no constant-factor approximation unless P = NP | Smeulders et al. (2014), via survey |
| Houtman–Maks index | **NP-hard** in general; no constant-factor approximation unless P = NP | Smeulders et al. (2014), via survey |
| Houtman–Maks, `K = 2` goods | **Polynomial** | Boodaghians & Vetta (2015), read in full |
| Houtman–Maks, `K = 3` goods | **NP-complete** | Boodaghians & Vetta (2015), read in full |
| Minimum Cost Index | **NP-hard**, by reduction from set covering | Dean & Martin (2016), read in full |
| Mean / median money-pump index | **NP-hard**; most- and least-severe variants polynomial | Smeulders et al. (2013), via survey |

**Not established: the complexity of the minimum-perturbation (LS) problem.** No source read in
this session states a complexity result for it. The closest is the survey's informal "can be
formulated as a non-linear optimization problem, which, in general, is hard to solve" — a remark
about non-linear programming practice, not a hardness theorem. **The complexity of the
minimum-perturbation-onto-GARP problem is open, or at least unestablished in the literature this
session could reach.** It must be reported that way.

**Does Houtman–Maks hardness transfer? Not without a reduction, and I have not verified one.**
Three specific reasons for caution, any one of which is fatal to a hand-waved transfer:

1. **Different objective type.** HM minimises a *cardinality* (how many rows to drop). LS
   minimises a *continuous distance*. There is no obvious cost-preserving map: deleting an
   observation is not "moving it a lot", because moving it far costs a large but finite amount,
   whereas deletion costs exactly 1 regardless of how far the deleted point was from consistency.
2. **Different feasible-set geometry.** Deletion only ever *removes* revealed-preference arcs.
   Perturbation moves bundles, which can *create* arcs that were not present in the original
   relation. A perturbation instance is not a sub-instance of a deletion instance.
3. **The `K`-threshold cuts against it.** Boodaghians & Vetta put HM in `P` at `K = 2` and make
   it `NP`-complete at `K = 3`. If the project runs at `K = 2` — which `audit/BRONARS_NOTE.md`
   recommends on power grounds — then even the deletion problem is polynomial there, so an
   appeal to "HM is NP-hard" proves nothing about the project's actual operating point.

**A well-posedness problem sits logically prior to the complexity question, and is worse.**
Because the GARP-consistent set is not closed (Chen–Lanier–Quah, Proposition 1), the infimum may
be **unattained**: there may be no nearest rationalisable dataset at all, and the LS index can
read 0 on data that violates GARP. Complexity is a question about how long it takes to find the
minimiser; this is a question about whether one exists. Asking the second question first is not
pedantry — it changes the formulation (see below).

Finally, on the practical side, "NP-hard" is not "intractable at this scale." Demuynck & Rehbeck
solve NP-hard indices on 22–79-observation datasets in under 2 seconds; `docs/COMPUTE_NOTE.md`
independently measured a Houtman–Maks-style MILP at 1.26–4.02 s for `n = 25–60`. The right claim
in the paper is "NP-hard in general, but the instances at this scale solve to optimality in
seconds," with a measured table.

---

## RECOMMENDED FORMULATION

A clean solved form exists. Use it. **A single MILP built on the multiplier-free ordinal
characterisation, with an explicit strict-preference margin and an independent combinatorial
verification of the output.** No Afriat multipliers, no bilinear terms, no outer search over
orderings, no alternating scheme.

### Variables

- `x̃_t ∈ R^K_+`, `t = 1..T` — the perturbed bundles. `K·T` continuous.
- `u_t ∈ [0,1]`, `t = 1..T` — ordinal levels. `T` continuous. **These are not Afriat utilities
  and carry no multipliers**; that is the whole point.
- `U_{t,v} ∈ {0,1}`, `t ≠ v` — indicator that `u_t ≥ u_v`. `T(T−1)` binary.

### Constraints

Following Demuynck & Rehbeck (2023), Theorem 2 and (IP-1)–(IP-4), with `q` replaced by the
decision variable `x̃`. Sign conventions below were reconstructed from their prose justifications
and should be re-derived once from the source before coding, not copied on trust.

```
(1)  u_t − u_v  ≤  −ε + 2·U_{t,v}                 for all t ≠ v,   0 < ε < 1/T
(2)  U_{t,v} − 1  ≤  u_t − u_v                    for all t ≠ v
(3)  p_t·x̃_t − p_t·x̃_v  ≤  −γ + α·U_{t,v}        for all t ≠ v
(4)  α·(U_{v,t} − 1)  ≤  p_t·x̃_v − p_t·x̃_t       for all t ≠ v
(5)  p_t·x̃_t = p_t·x_t = I_t                      for all t          [budget exhaustion]
(6)  x̃_t ≥ 0                                      for all t
```

(1)–(2) tie the binaries to the ordinal levels; (3)–(4) tie the binaries to the revealed
preference relation on the *perturbed* bundles. Every one of (1)–(6) is linear in
`(x̃, u, U)`, because prices are data and no multiplier appears anywhere.

Three implementation points that matter:

**Impose budget exhaustion (5) as an equality, not `≤`.** It is standard in this experimental
design, it is Andrews' own fix for the Lemma-1 problem behind Q6, and it has a structural
payoff here: with `p_t·x̃_t = I_t` a *constant*, the left-hand side of (3) becomes
`I_t − p_t·x̃_v`, linear in a single block of variables. That makes the big-`M` constant
computable a priori — `α > max_t I_t` suffices — and materially better conditioned than the
free-budget version.

**`γ > 0` is not optional, and it is where the non-closedness gets handled.** Demuynck &
Rehbeck's `δ` is defined as a minimum over *observed* strictly-positive expenditure gaps. Once
`x̃` is a variable the optimiser can shrink those gaps toward zero, so no data-derived `δ`
is valid. Their own workaround in the price-error case is to drop `δ` and take a supremum
instead of a maximum — which is exactly the non-attainment that Chen–Lanier–Quah prove is
unavoidable. Replace it with a **fixed modelling constant `γ`**, in expenditure units, chosen
relative to price scale (e.g. `γ = 10⁻⁴ · min_t I_t`), and be explicit in the paper that the
program computes the **`γ`-margin projection**, which is a projection onto a *closed* subset of
the GARP-consistent set. Report `γ` and show the distance is insensitive to it across two or
three decades. That converts an unattained infimum into an attained minimum, and converts a
silent failure into a reported parameter.

**Objective: use `L1` by default.**

```
min  Σ_t Σ_k  w_{t,k} · d_{t,k}     s.t.   x̃_{t,k} − x_{t,k} ≤ d_{t,k},
                                            x_{t,k} − x̃_{t,k} ≤ d_{t,k}
```

This keeps the whole thing a pure MILP, which HiGHS solves — the backend already measured in
`docs/COMPUTE_NOTE.md`. The weighted-`L2` version `Σ_t (x_t − x̃_t)' W_t (x_t − x̃_t)` is the
literature's LS index and is a convex MIQP, which needs Gurobi/CPLEX/SCIP. Report `L1` as
primary and `L2` as a robustness check if an MIQP solver is available. `L∞` (a single `d`
variable) gives a "worst-case single-bundle move" reading and is nearly free to add.

### Size and expected cost

`T(T−1)` binaries plus `K·T + T` continuous: 600 binaries at `T = 25`, 2,450 at `T = 50`, 3,540
at `T = 60` — the same binary counts as the MILPs already timed in `docs/COMPUTE_NOTE.md`, and
the same regime as Demuynck & Rehbeck's sub-2-second solves at `T = 22–79`. **But do not assume
the timings carry over.** The projection adds `K·T` continuous variables inside big-`M`
constraints, which weakens the LP relaxation relative to the deletion MILP. Re-measure before
committing to `T = 60`, and report the MIP gap alongside every distance.

### Feasibility is free, and gives a warm start

The feasible set is never empty. Any bundle sequence generated by maximising a single
well-behaved utility at the observed prices and incomes satisfies GARP exactly. So compute the
Cobb–Douglas (or CES) demand at `(p_t, I_t)` with shares fitted to the observed data, feed it as
an incumbent, and the solver starts with a valid upper bound on the projection distance. This
also gives a sanity ceiling: the true minimum can never exceed the distance to the best-fitting
parametric demand — which is exactly the Halevy–Persitz–Zrill (2018) parametric-recoverability
approach used as a bound rather than as the answer.

### If the MILP is too slow: the named honest heuristic, and its failure mode

Do not invent one. Use **De Peretti (2005)**, *Macroeconomic Dynamics* 9(3), 372–397, which is
the published heuristic for exactly this problem: tackle violations one at a time, perturbing one
observation at a time; for a cycle between `x_i` and `x_j`, compute the minimal perturbation that
removes the violation under each of the two orientations, take the cheaper, update the dataset,
re-test GARP, repeat.

**Its failure mode, stated plainly.** The survey says outright that "this algorithm does not
guarantee an optimal solution." Concretely it returns an **upper bound** on the projection
distance that can be arbitrarily loose, for three reasons: it is *greedy* (an early cheap fix
can force expensive later ones); it is *order-dependent* (the answer depends on which violation
is processed first); and it is *myopic in dimension* (it moves one observation at a time, so it
cannot find a joint move that clears several cycles at once and is cheaper than the sum of
separate fixes). It is fastest exactly where it is least needed — the survey notes it works well
"especially if the number of violations is small" — and degrades where the paper's interesting
cases live.

**How to detect that it has returned a bad answer.** Three cheap checks, all of which should be
run and reported:

1. **Bound the gap.** Solve the MILP's root LP relaxation, or run the MILP under a time limit and
   read its best bound. That gives a valid lower bound; De Peretti gives an upper bound; report
   the interval. A wide interval is a published caveat, not a hidden defect.
2. **Randomise the processing order and report the spread.** Run 50 random orders. A wide spread
   is direct, self-generated evidence that the heuristic is not finding the optimum. A tight
   spread is weak evidence it is close — not proof.
3. **Plant a known answer.** Take a GARP-consistent synthetic dataset, apply a known perturbation
   of known size, and check whether the heuristic recovers it. Do this at each `K` and `T` in the
   design. This doubles as the Bronars power machinery Q4/Q5 already require.

### Always verify the output independently

Whatever produces `x̃`, feed it back through the **plain combinatorial GARP test** — Warshall
closure on the relation induced by `(p_t, x̃_t)` — and assert it passes. This is `O(T³)`, costs
nothing, is completely independent of the MILP's big-`M` encoding, and catches every numerical
knife-edge the `γ` margin was meant to prevent. A solver that reports optimality on a badly
scaled big-`M` model can return an `x̃` that violates GARP by a hair. Never report a projection
that has not passed this check.

### Well-posedness fallback if the `γ` margin proves unsatisfying

Chen–Lanier–Quah's Proposition 11 gives a principled alternative: restrict to a class whose
rationalisable datasets form a **closed** set. The **homothetic** class qualifies (project onto
HARP rather than GARP), as does the **expected-utility class with concave Bernoulli functions**.
This buys an attained minimum and a continuous, accurate index by construction, at the price of a
stronger behavioural assumption. Worth a paragraph in the paper either way, because it is the
first thing an economics referee will ask about.

---

## What this means for claims S8 and S9

### S8 — "Given a fixed preference ordering, feasibility is a system of Afriat inequalities — a linear program. Wrap in a MILP or a search over orderings."

**Status: wrong in both halves, in opposite directions. Rewrite it.**

- *Understated for measurement.* With the data fixed, the Afriat system is an LP in `(U, λ)`
  **without** fixing any ordering (Afriat 1967; Diewert 1973). The "given a fixed preference
  ordering" qualifier is unnecessary there.
- *Wrong for construction.* Once `x̃` is a decision variable, fixing the ordering does **not**
  restore linearity — `λ_j·p_j·x̃_i` stays bilinear whatever the ordering is. The clause "wrap in
  a search over orderings" therefore does not do the job it is claimed to do, and the alternating
  scheme built on it is heuristic-only (§3).
- *The correct statement.* Under the ordinal, multiplier-free characterisation (Demuynck &
  Rehbeck 2023, Theorem 2), the constraints are linear in utility numbers, prices **and
  quantities** simultaneously. The projection is therefore a single MILP (or convex MIQP under
  `L2`), with no bilinear term and no outer ordering loop. `docs/COMPUTE_NOTE.md`'s caveat
  paragraph — "with both utility levels and multipliers free and no fixed ordering, the system is
  bilinear" — should be replaced by "the Afriat parameterisation is bilinear once quantities are
  decision variables; the ordinal parameterisation is not, and is what should be used."

Proposed replacement text for S8:

> The projection is a mixed-integer linear program. Using the multiplier-free ordinal
> characterisation of GARP, the constraints are linear jointly in the perturbed quantities, the
> ordinal utility levels and the binary comparison indicators, so no Afriat multipliers and no
> bilinear terms appear and no outer search over orderings is required. The Afriat-multiplier
> parameterisation *is* bilinear once quantities are free and should not be used for the
> projection.

**Kill condition for the rewritten S8:** the MILP failing to solve to a usable gap at the design's
`(T, K)`, or the `γ`-margin projection distance proving sensitive to `γ`.

### S9 — "Keep n ≤ 60; the ordering search blows up beyond that."

**Status: the bound is fine; the stated reason is not, and it is missing its `K`.**

- There is no explicit ordering search in the recommended formulation. What scales is the
  `T(T−1)` binary count and the branch-and-bound tree, not a factorial enumeration.
- The `n ≤ 60` figure is corroborated *empirically* by two independent sources — Demuynck &
  Rehbeck at `T = 22–79` in under 2 s, and `docs/COMPUTE_NOTE.md` at `n = 25–60` in under 5 s —
  though both measured the *deletion* MILP, not the perturbation MILP, whose relaxation is weaker.
- **The bound needs a `K`.** Boodaghians & Vetta put the deletion problem in `P` at `K = 2` and
  make it `NP`-complete at `K = 3`. `K`, not `n`, is where the complexity threshold lives, which
  agrees with kill-check E4's finding that `K` is the binding constraint on test power. A scope
  claim written only in `n` is incomplete.

Proposed replacement text for S9:

> Keep `T ≤ 60` and state `K` explicitly. The projection MILP has `T(T−1)` binaries plus `K·T`
> continuous variables; comparable MILPs at this scale solve in seconds, but the perturbation
> variant's relaxation is weaker and its timings must be measured, not inherited. Complexity is
> `K`-dependent: the related deletion problem is polynomial at `K = 2` and NP-complete at `K = 3`.

---

## Residual risk and what would resolve it

**High — the minimum may not exist.** The GARP-consistent set is not closed, so the projection
distance can be an unattained infimum, and the LS index can read 0 on GARP-violating data
(Chen–Lanier–Quah, Prop. 1). The `γ`-margin formulation resolves it by construction, but
introduces a reported free parameter. *Resolves it:* a sensitivity sweep over `γ` across two or
three decades, plus the Warshall post-check on every returned `x̃`. Half a day.

**High — the projection distance may not behave as a dose variable.** The project needs a
*monotone, interpretable* perturbation axis. `L1`, `L2` and `L∞` will not rank agents identically,
and Chen–Lanier–Quah's accuracy/continuity impossibility means every choice has a known defect.
*Resolves it:* report at least two norms and show the dose–response conclusion is invariant to
the choice. If it is not, that is a finding, not a bug.

**Medium — the perturbation MILP's timings are inherited, not measured.** All the sub-second
evidence is for *deletion* MILPs with fixed data. Adding `K·T` continuous variables inside
big-`M` constraints weakens the LP relaxation by an unknown amount. *Resolves it:* run the
formulation above at `T ∈ {25, 40, 50, 60}` × `K ∈ {2, 3, 5}`, report solve time and MIP gap.
A few hours; costs nothing.

**Medium — Smeulders et al. (2014) has not been read in primary form.** Every complexity number
in the table above that traces to it is secondary-sourced. The three secondary sources agree, and
two of them are by the same authors, but the `O(n^{1−δ})` inapproximability form appears in only
one and is recorded as unverified. *Resolves it:* library access to *ACM TEAC* 2(1) Art. 3.
Same fix as `docs/OPEN_QUESTIONS.md` Q11.

**Medium — Varian (1985) is the origin of the formulation and could not be read.** The
attribution rests on the survey's characterisation. *Resolves it:* library access to
*J. Econometrics* 30(1), 445–458.

**Low — Demuynck & Rehbeck's AQE is a two-sentence sketch.** They name it and never work it out,
so the inequality signs and constants above are reconstructed from their prose justifications
rather than copied from a stated theorem. *Resolves it:* re-derive (1)–(4) once from Theorem 2
before coding, and unit-test the encoding against the independent Warshall GARP test on random
data — if the MILP declares feasible where Warshall declares a violation, the encoding is wrong.
An hour, and it should be a permanent test in the repo.

**Low — the EIS reading is of the arXiv version only.** The published *JEEA* version may use
different terminology, which bears on Q8's naming question. *Resolves it:* one OA fetch of the
*JEEA* PDF, which Unpaywall reports as available.

**Not resolved by this session — RePEc was still not searched.** `docs/OPEN_QUESTIONS.md` Q12
stands. The economics working-paper literature is where a fourth formulation of this exact
projection would most plausibly sit. The three primary economics sources found here
(Demuynck–Rehbeck, Chen–Lanier–Quah, Boodaghians–Vetta) were reached via OpenAlex and general
web search, not via RePEc, so this gap is narrower than it was but still open.

---

## Fetch record

**Instrument note.** `hyperresearch fetch` remains broken on raw PDFs in this build
(`audit/INSTRUMENT_CALIBRATION.md` §4.6); every PDF below was retrieved with `curl` and
extracted with PyMuPDF, ligature-expanded and NFKC-normalised before grepping.

### Read in full

| Source | URL | Status |
|---|---|---|
| Demuynck & Rehbeck (2023), ECARES WP 2021-26 version | `dipot.ulb.ac.be/dspace/bitstream/2013/334880/3/2021-26-DEMUYNCK_REHBECK-computing.pdf` | OK, 27 pp. §§1–6 read; Thm 2, Cor. 1–6, IP-1…IP-19 read verbatim |
| Chen, Lanier & Quah, arXiv:2405.08464v2 | `arxiv.org/pdf/2405.08464` | OK, 42 pp. Intro + index definitions + Props 1, 7, 11 read |
| Smeulders, Crama & Spieksma (2019), EJOR — accepted MS | `orbi.uliege.be/bitstream/2268/213504/1/Survey%20Revision%202.pdf` | OK, 44 pp. §§1, 5.1, 5.2 read verbatim |
| Dean & Martin, working-paper version | `columbia.edu/~md3405/Working_Paper_11.pdf` | OK, 35 pp. §§1–2 + Table 2 read |
| Gorski, Pfeuffer & Klamroth (2007) | `www2.math.uni-wuppertal.de/~klamroth/publications/gopfkl07.pdf` | OK, 34 pp. §4 (Defs 4.1–4.3, Thms 4.1–4.9, Examples 4.1–4.3, Alg. 4.1) read verbatim |
| Boodaghians & Vetta, arXiv:1507.07581 | `arxiv.org/pdf/1507.07581` | OK, 16 pp. Abstract + §§1–2 read |
| Echenique, Imai & Saito, arXiv:2102.06331v1 | `arxiv.org/pdf/2102.06331` | OK, 86 pp. Intro + §2 perturbation definitions read; keyword census run |
| TrustRoboReward / POISE, arXiv:2608.08491 | `arxiv.org/html/2608.08491` | OK. §3.2, Thm 1, Limitations read verbatim |

### Abstract / secondary only

| Source | Route | Status |
|---|---|---|
| Smeulders, Spieksma, Cherchye & De Rock (2014), *ACM TEAC* 2(1) Art. 3 | `feb.kuleuven.be/public/u0037710//papers/TEAC2014paper.pdf` **HTTP 401**; `dl.acm.org/doi/pdf/10.1145/2560793` **403**; `dl.acm.org/doi/abs/...` **403 via WebFetch**; SSRN delivery **403**; `lirias.kuleuven.be/retrieve/253744` **410**; two guessed KU Leuven DPS paths **404**; Unpaywall `10.1145/2560793` → `is_oa: false` | **ACCESS GAP.** Results carried on three agreeing secondary sources, all read in full: the same authors' 2019 EJOR survey, Dean & Martin (2016), Demuynck & Rehbeck (2023). The `O(n^{1−δ})` inapproximability form is single-sourced and marked unverified. |
| Varian (1985), *J. Econometrics* 30(1) | `deepblue.lib.umich.edu/bitstream/2027.42/25557/1/0000099.pdf` returned a 1,959-byte HTML interstitial under both HTTP and HTTPS and both UAs — 0 extractable characters | **ACCESS GAP.** Attribution rests on the 2019 survey's characterisation. |
| Varian (1990), *J. Econometrics* 46(1–2); Varian (1982), *Econometrica* 50(4) | not fetched; paywalled, consistent with Q11 | **ACCESS GAP.** Algorithmic content sourced to the 2019 survey and to Chen–Lanier–Quah. |
| Dean & Martin (2016), published *REStat* version | Unpaywall `10.1162/rest_a_00542` → `is_oa: false` | Working-paper version read instead. Page/volume metadata from Crossref + OpenAlex. |
| De Peretti (2005), *Macroeconomic Dynamics* 9(3) | not fetched; OpenAlex title search did not surface it directly | Description sourced verbatim to the 2019 survey, which reads the algorithm and states its non-optimality. |
| Gorski et al. published version | Unpaywall `10.1007/s00186-007-0161-1` → `is_oa: false` | Author-hosted preprint read instead; theorem numbering assumed to match. |
| Chadwick, Kahng & Kipper (HAR 2025) | not re-fetched this session | Read in full in a prior session; description sourced to `audit/INSTRUMENT_CALIBRATION.md` §4.1 and `docs/DECISIONS.md`. |
| LLM-RankFusion, TrustJudge, Innate Economic Preferences, CONSISTRE | arXiv API `id_list` | Abstracts only. Sufficient for the "not the same problem" classification; none is load-bearing here. |

### Search instruments

| Instrument | Query | Result |
|---|---|---|
| arXiv full-text (`scripts/arxiv_ft_search.py`) | `"minimum cost" AND "revealed preference"` | `[OK]` 55 hits |
| " | `"Houtman-Maks" AND "NP-hard"` | `[OK]` 3 hits — 2512.23352, 2507.04396, 2303.08202; all three triaged by abstract, none about projection |
| " | `"revealed preference" AND "computational complexity"` | `[OK]` 119 hits |
| " | `"minimal perturbation" AND "revealed preference"` | `[OK]` 3 hits — 2608.05015 (Andrews, already in ledger), 2106.14486, 2411.01042 |
| " | `"GARP" AND "mixed integer" AND "perturbation"` | `[OK]` 8 hits — surfaced 2405.08464, the decisive source |
| " | `"nearest" AND "rationalizable" AND "bundle"` | `[OK]` 6 hits |
| " | `"Demuynck" AND "Rehbeck"` | `[OK]` 28 hits |
| OpenAlex | 8 title searches (Dean–Martin, Smeulders TEAC, EIS, Gorski, Demuynck–Rehbeck, Varian 1985/1990, Boodaghians–Vetta, De Peretti) | All resolved except De Peretti and Varian 1990 |
| Crossref | Dean–Martin bibliographic | Resolved: `10.1162/rest_a_00542`, 2016 |
| Unpaywall | 4 DOIs | 1 OA (`10.1093/jeea/jvad028`), 3 closed |
| Web search | 3 targeted queries | Located the Dean–Martin and Gorski author-hosted PDFs and the Demuynck–Rehbeck lead |
| Semantic Scholar | not attempted | Known 429 in this environment; recorded as a gap per instruction |
| RePEc / IDEAS / EconPapers | `ideas.repec.org` landing pages returned HTTP 200 HTML but were not mined | **GAP — Q12 still open.** |

**No zero reported in this note came from an `ERROR` status.** Every arXiv full-text query above
returned `[OK]`, so the counts are trustworthy; the index is nonetheless partial, so none of them
is treated as evidence of absence.
