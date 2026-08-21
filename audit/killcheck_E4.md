# Kill-check E4 — test power behind any CCEI number

**Status:** added by the audit. E4 is **not** in `docs/F3-PLAN-ORIGINAL.md`; it exists because the
plan treats a high CCEI as evidence of agent rationality without anywhere asking whether the budget
sets that produced it *could* have produced a violation.

**Bears on:** C4 (there is CCEI headroom to project away), S1 (the 0.997–0.999 ceiling), S9 (n ≤ 60).

**Companion deliverable:** `audit/BRONARS_NOTE.md` — the standing rule and the computation recipe.

---

## Falsifier (stated before the finding)

E4 is an objection worth raising only if all three of the following survive contact with the
literature. Each has a stated falsifier, and I commit to reporting a falsification as such.

| # | Proposition E4 needs | What would falsify it |
|---|---|---|
| **F1** | Test power against a uniform-random benchmark is the standard, named diagnostic for "could this test have failed?", and is computable for a synthetic design before any data are collected. | No such standard exists, or it is not computable ex ante from prices alone. |
| **F2** | Power varies materially with design — enough that a plausible design could be low-powered. | Power is essentially pinned near 1 for any design a researcher would actually write down, making the diagnostic vacuous. |
| **F3** | Specifically at n = 25–50 with K = 2–3 goods, power is *not* automatically adequate, so the brief's stated design is at risk. | Power at n = 25–50, K = 2–3 is ≈ 1 under any sane price draw — in which case the brief's design is fine and E4 reduces to a *reporting* obligation, not a *design* defect. |

**Outcome, stated up front so the reader can check I did not move the goalposts: F1 and F2 survive.
F3 is FALSIFIED.** At K = 2–3 and n = 25–50 the power of the brief's design is ≈ 1. E4 therefore
does **not** kill C4 or S9. What E4 does establish is (a) a reporting obligation that the brief
currently omits, and (b) two specific design boundaries beyond which the brief's own stated
extensions would silently destroy the test. Both are recorded below.

---

## What Bronars power is and how it is computed

Bronars, S. G. (1987), "The power of nonparametric tests of preference maximization",
*Econometrica* 55(3):693–698, DOI `10.2307/1913608`.

**The original paper could not be read.** It is closed-access; Unpaywall reports
`is_oa: false`, `oa_status: "closed"`, zero OA locations; Semantic Scholar returns
`openAccessPdf.status: "CLOSED"` with the abstract elided by the publisher. Everything in this
section is therefore taken from sources that restate the method, and each is marked **[secondary]**.
No number in this section is attributed to Bronars unless a named secondary source attributes it to
him.

**The construction.** [secondary: Cherchye, Crawford, De Rock & Vermeulen (2008), "The Revealed
Preference Approach to Demand", §on power; Andreoni & Harbaugh (2008), "Power Indices for Revealed
Preference Tests", §3.1; Hjertstrand (2019/2021), IFN WP 1309, §1 and §3; Demetry, Hjertstrand &
Polisson (2020/2022), IFN WP 1342, §2.4]

Power is the probability of rejecting the null (utility maximisation) when it is false, so it
requires a stated alternative. Bronars adopts Becker's (1962) "irrational" consumer: choices are
drawn uniformly at random from the budget hyperplane, exhausting the budget. Concretely, for a
design of T observations over K goods with prices `p_t` and expenditures `m_t = p_t · x_t`:

1. For each observation `t`, draw budget shares `w_t` uniformly on the (K−1)-simplex —
   i.e. `w_t ~ Dirichlet(1, …, 1)`.
2. Convert to quantities: `q_kt = w_kt · m_t / p_kt`.
3. Test GARP on the synthetic dataset `{p_t, q_t}`.
4. Repeat many times. **Power = fraction of replications that violate GARP.**

Step 1 is the whole content of the benchmark: the map `x ↦ w` with `w_k = p_k x_k / m` is linear
with a constant Jacobian, so "uniform on the budget hyperplane" and "uniform on the budget-share
simplex" are the same distribution. This is why the geometric and the probabilistic statements of
the measure coincide (see the Selten Area below).

Two things follow immediately and matter for design:

- Power is a property of **the prices and budgets alone**. The agent's choices never enter. It can
  therefore be computed *before* a single API call, from the synthetic budget sets by themselves.
- Power is driven by **budget-hyperplane intersections**. "This probability depends on the number of
  budget set intersections associated with the different consumption bundles in the data set under
  study. If there are no intersections at all, then irrational behavior can never be detected."
  [secondary: Cherchye et al. 2008]

**Bronars' variants.** Bronars gave three algorithms. Algorithm 1 draws shares uniformly on the
simplex; Algorithm 2 constructs random shares with expected share `1/K`; Algorithm 3 centres the
randomness on the *observed* shares. "Method 1, however, has come to dominate the literature."
[secondary: Andreoni & Harbaugh 2008 §3.1; Hjertstrand IFN WP 1309 fn. 2 and fn. 4]. When the
literature says "Bronars power" unqualified, it means Algorithm 1.

**What Bronars himself applied it to.** [secondary: a 2008 ANPEC conference paper,
"On the existence of well-behaved macro utility functions", §2.2 and fn. 6] His Monte Carlo used
aggregate US consumption expenditure series, and his concern was budget sets that expand outward
over time under income growth without relative prices moving enough to make them cross. Two of his
findings are restated there: the test was more likely to commit a Type II error on annual budget
hyperplanes than on quarterly ones, and power was much higher on per-capita series than on aggregate
ones. **I did not find a citable source for the exact numerical power values in Bronars' own tables,
and I do not report any.**

**The standard objection to the benchmark.** Uniform-random choice is unconditional — it ignores
where the agent actually chose. "Suppose, for instance, the budgets offered did not intersect near
the points where individuals are actually choosing. Then if preferences do not conform to utility
maximization, the test would be unlikely to discover it. This is true even if Bronars' analysis
shows that randomly made choices provide a high probability of violations." [Andreoni, Gillen &
Harbaugh (2013), quoted verbatim in Hjertstrand IFN WP 1309 §1]. Conditional alternatives —
bootstrap power, Famulari's price-reshuffling index, Andreoni–Gillen–Harbaugh's jittering / optimal
placement / Afriat power indices, Hjertstrand's PURP and cPURP — exist precisely to fix this, and
they generally report **lower** power than Bronars on the same design. Bronars power is a *necessary*
condition for a design to be informative, not a sufficient one. See the 7.9%–26.3% figures in the
next section but one.

---

## The power-vs-pass tradeoff (Beatty & Crawford; Selten's measure)

Beatty, T. K. M. & Crawford, I. A. (2011), "How Demanding Is the Revealed Preference Approach to
Demand?", *American Economic Review* 101(6):2782–2795, DOI `10.1257/aer.101.6.2782`.

**Access:** the AER version is closed (Unpaywall `is_oa: false` for the article DOI and for both
cemmap/IFS working-paper DOIs). An author-hosted copy on the Oxford economics faculty server was
fetched and read in full (12 pp.; abstract, data, and results match the published article's
description). Quotations below are from that copy.

**The problem they name.** "A well known problem with revealed preference methods is that when data
are found to satisfy their restrictions it is hard to know whether this should be viewed as a triumph
for economic theory, or a warning that these conditions are so undemanding that almost anything
goes." Their opening figure is a two-good, two-observation environment with `p1 = [3,4]`,
`p2 = [4,3]` and budgets 10 and 5: a modest relative-price change combined with a large income
change, in which "regardless of where a nonsatiated consumer's choices fall, revealed preference
restrictions on their behaviour simply cannot be violated." They quote Varian (1982): "lack of
variation in the price data limits the power of these methods."

**The measure.** Let `r ∈ {0,1}` be the pass/fail indicator and `a ∈ [0,1]` the *relative area* —
the size of the GARP-consistent set of budget shares as a fraction of the whole outcome space.
They impose three axioms on any success measure `m(r,a)`:

- **Monotonicity:** `m(1,0) > m(0,1)`.
- **Equivalence:** `m(0,0) = m(1,1)` — "no restrictions" and "nothing ruled out" are equally
  uninformative.
- **Aggregability:** `m(λr₁+(1−λ)r₂, λa₁+(1−λ)a₂) = λm(r₁,a₁) + (1−λ)m(r₂,a₂)`.

**Selten's Theorem** (Selten 1991): `m = r − a` satisfies all three, and any `m(r,a)` satisfying them
is a positive affine transform `β + γm`, `γ > 0`. So one may as well use the difference.
`m ∈ [−1,1]`; `m ≈ 0` means "the apparent accuracy of the data simply mirrors the size of the target".

**The bridge to Bronars — this is the load-bearing sentence.** B&C §3: "Bronars' (1987) adopts
Becker's (1962) idea of uniform random choices over the outcome space as a general alternative
hypothesis to a null of optimising behaviour. **The implication is that area may be interpreted as
one minus Bronars' (1987) statistical power measure.**"

Therefore:

```
predictive success  m  =  pass rate  −  area
                       =  pass rate  −  (1 − Bronars power)
                       =  pass rate  +  Bronars power  −  1
```

This is the corrected measure. `powerps` in the Stata package `rpaxioms` implements exactly this
[Demetry, Hjertstrand & Polisson, IFN WP 1342 §2.4, §3.3], as does `bronars` in the R package
`revpref`.

**Their empirical illustration, which is the point of the paper.** Spanish Continuous Family
Expenditure Survey (ECPF), 21,866 observations on 3,134 households, 5 broad commodity groups,
households observed up to 8 consecutive quarters, national price indices.

| quantity | value |
|---|---|
| GARP pass rate `r` | **0.957** |
| relative area `a` | **0.912** |
| predictive success `m = r − a` | **0.045** |
| implied Bronars power `1 − a` | **0.088** |
| smoothed hit rate `r_d` / `m_d` | 0.97 / 0.058 |

Their gloss: "The implication is that the standard economic model of utility maximisation
out-performed a random number generator - but only by 4.5%. Given this, the unadjusted pass rate of
95.7% seems a great deal less impressive and even somewhat misleading regarding the success of the
model." And: "for many households the relative area of the target is equal to 1 - the theory cannot
fail."

**A 95.7% pass rate at 8.8% power is the exact failure mode E4 exists to prevent.**

**Two worked two-good areas from B&C, useful as sanity anchors:**

| environment (2 goods, 2 observations) | area `a` | implied power |
|---|---|---|
| `p1=[3,4]`, `p2=[4,3]`, budgets 10 and 10 | 40/49 ≈ 0.816 | 0.184 |
| `p1=[3,4]`, `p2=[4,3]`, budgets 10 and **5** | **1.000** | **0.000** |
| `p1=[2.5,5]`, `p2=[5,2.5]`, budgets 10 and 10 | 8/9 ≈ 0.889 | 0.111 |

Note the third row: *more* extreme relative-price variation gave *less* power, because it pushes the
crossing point toward a corner. Power is not monotone in price variation. See the design section.

---

## How power varies with n, number of goods, and price variation

### (a) Number of observations n — power rises with n, and fast at low K

**Direction.** B&C, from a regression of household-level outcomes on household characteristics:
"the number of times we observe a household is significantly and negatively related both to the
probability of passing GARP and the relative area. This is entirely as one would expect - more
observations make RP tests more demanding."

**Numbers, K = 2 goods, same experimental family, only n differs.** Andreoni & Miller (2002) ran a
generalised dictator game where the two payoffs are the two goods; because every subject in a group
faced the same budgets, the Bronars index is a single number per group.

| design | n (decision rounds) | K | Bronars power |
|---|---|---|---|
| Andreoni & Miller (2002) Group 1 | 8 | 2 | **78.1 %** |
| Andreoni & Miller (2002) Group 2 | 11 | 2 | **94.7 %** |

[Reported in Hjertstrand, IFN WP 1309 §5.1, attributing both figures to Andreoni & Miller (2002).]

**Numbers at n = 25, K = 2 — the brief's own design.** Chen, Liu, Shan & Zhong (*PNAS* 120(51),
2023; arXiv:2305.12763 — reference R1, the source of the brief's 0.997–0.999 ceiling) used 25 tasks
allocating 100 points between two commodities, with prices drawn as `M, N ∈ [0.1, 1]` subject to
`max{M,N} ≥ 0.5` (Appendix A fn. 9), a Choi et al. (2014)-style rule. They report:

> "We employ the choices of a hypothetical subject who chooses uniformly randomly among all
> allocations on each budget line as a point of comparison. Each of the hypothetical simulated
> subjects makes 25 choices from randomly generated budget sets in the same way that [the model]
> observations and human subjects do. **We find that 99.9% of the hypothetical simulated subjects
> reject GARP.**"

(The bracketed substitution is the audit's; the original names the vendor's model.)

They also report predictive success of 94.9 %, 88.9 %, 80.9 %, 91.9 % across their four preference
domains, against GARP pass rates of 95, 89, 81, 92 out of 100. Those pair as
`m = pass rate − 0.001` exactly, confirming `m = r − (1 − power)` with `power = 0.999` and
confirming that their prose description of the formula has its sign transposed. Their Selten scores
(mean agent CCEI minus mean simulated CCEI) average ≈ 0.28 against mean agent CCEI 0.997–0.999,
implying a **mean CCEI of ≈ 0.72 for a uniform-random agent on that design** — a figure independently
reproduced below.

**Caveat that must travel with that 99.9 %.** The same paper's *conditional* (bootstrap) power, which
resamples budget shares from the observed choice distribution rather than uniformly, is
**7.9 %, 26.3 %, 26.0 %, 8.5 %** for the model observations across the four domains (against
95.4 %–99.8 % for their human subjects). Unconditional Bronars power of 99.9 % and conditional power
of 7.9 % on the same budget sets is not a contradiction — it is the Andreoni–Gillen–Harbaugh
objection made numerical. A high Bronars number licenses "the design could have failed"; it does not
license "the design could have failed *given how this agent behaves*".

### (b) Number of goods K — power FALLS, exponentially

Crawford, I. & Tian, L. (2026), "The Empirical Content of Revealed Preference in High Dimensions",
arXiv:2605.29361v1 [econ.TH], 28 May 2026. **Fetched and read in full (8 pp. + appendices).**

They work with Selten's Area `A_K`, defined as the fraction of the product simplex `∆_{K−1}^T`
satisfying GARP, and state its probabilistic representation explicitly: `A_K = P((w_1,…,w_T) ∈ S_K)`
where the `w_t` are i.i.d. uniform on `∆_{K−1}`. **That is Bronars' benchmark exactly, so
`Bronars power = 1 − A_K`.** (The identification of area with `1 − power` is B&C's, quoted above;
Crawford & Tian do not themselves cite Bronars — the bridge runs through B&C, of which Crawford is a
co-author.)

**Theorem 1 (graph-theoretic).** Fix `T ≥ 2`. Under (A1) bounded normalised price ratios and (A2)
non-vanishing price dispersion, there is `c₁ > 0` with
`A_K ≥ 1 − C_T · exp(−c₁ K)`, where `C_T = Σ_{L=2}^{T} C(T,L)(L−1)!` counts directed cycles on `[T]`.
Hence `A_K → 1`, i.e. **power → 0**, exponentially in K.

**Theorem 2 (Afriat LP).** Same conclusion via LP feasibility:
`A_K ≥ 1 − T(T−1)·exp(−c₂ K)`.

**Mechanism.** A GARP violation is a directed cycle in the revealed-preference graph. Every cycle
must contain an "expensive" edge whose unweighted (Carli) average relative normalised price exceeds
1; for that edge to exist, the budget-share vector must be skewed toward the cheap goods. In high
dimensions almost all of the simplex's volume sits at *spread-out* allocations, so skewed regions
have exponentially small measure. Their own analogy: coin flips concentrate near half heads.

**Their honest caveat, which I repeat rather than overstate:** "the result is asymptotic rather than a
monotonicity theorem for small steps in K. It does not logically force A3 > A2 in every possible
environment."

**Their simulation numbers** (inverse normalised prices `1/r_k ~ LogN(0,σ)`, benchmark `σ = 1`
calibrated to ACNielsen Homescan scanner data, where the fitted parameters were `µ̂ = 5.69`,
`σ̂ = 1.19`):

| finding | figure |
|---|---|
| 2 goods, 2 budget constraints (their Figure 1 example) | `A_2 = 40/49 ≈ 0.82` → power 0.18 |
| add a third good to that example (their Figure 2) | `A_3 ≈ 0.95` → power ≈ 0.05 |
| T = 10 | Area > 0.9 by **K = 9**; > 0.95 by **K = 11** |
| T = 20 | those thresholds move only to **K = 13** and **K = 15** |
| T = 50 | Area reaches 0.95 by **K = 20** |
| T = 25, σ from 1.0 → 0.5 | K-threshold for Area ≥ 0.9 moves from **K = 14** to **K = 42** |
| K = 24, T = 10, unrestricted | Area = **0.9996** — power 0.0004 |
| same, imposing weak / additive separability into 3 groups of 8 | 0.73 / 0.66 |
| same, into 6 groups of 4 | 0.07 / 0.005 |

Their summary: "increasing the number of observations slows, but does not prevent, the loss of
empirical content", and "the effects of adding observations are attenuated as T increases".
**Doubling n does not buy back what adding four goods costs.**

**A tension I am flagging rather than resolving.** B&C's ECPF regression found that "the number of
commodity groups observed in the household's bundle decreases the probability of passing GARP and
also decreases the relative area" — i.e. *more* goods, *more* power, the opposite sign to Crawford &
Tian. These are not directly comparable: B&C's regressor is the number of *non-zero* expenditure
categories, which is endogenous to the household's corner solutions and confounded with how much
price variation that household's basket was exposed to; Crawford & Tian hold the price distribution
fixed and vary K by construction. The controlled statement is Crawford & Tian's. But the discrepancy
is real and is recorded here so a later session does not "discover" it and think something was
hidden.

### (c) Price variation and budget-line crossing — non-monotone; what you want is crossing, not variation

The naive rule "more price variation ⇒ more power" is **wrong**, and three sources agree on why.

- **Too little relative price variation kills power.** Varian (1982), quoted by B&C: "lack of
  variation in the price data limits the power of these methods." Parallel budget lines under pure
  income growth never cross, and "if there are no intersections at all, then irrational behavior can
  never be detected" [Cherchye et al. 2008]. B&C's Figure 1 (budgets 10 and 5, modest price change)
  has area exactly 1.
- **Too much relative price variation also kills power.** B&C's own third example: moving prices from
  `[3,4]/[4,3]` to the more extreme `[2.5,5]/[5,2.5]` at equal budgets *raises* the area from 0.816
  to 0.889. Extreme price ratios push the crossing region toward a corner of the simplex, and corners
  have little volume.
- **What actually drives power is that budget constraints cross near where choices fall.** Crawford &
  Tian, on their `σ` panel: "Lower dispersion in relative prices reduces the Area—having budget
  constraints tightly clustered so that (i) they cross frequently and (ii) the relative prices are
  similar but not identical."

### (d) This session's own Monte Carlo (labelled as such, not literature)

Because the literature reports `A_K` curves as figures rather than as tables at the exact `(K, T)`
the brief needs, I computed the grid directly, using the recipe in `audit/BRONARS_NOTE.md`. Three
price designs, uniform Dirichlet(1,…,1) budget shares, GARP by transitive closure, 1,200 replications
per cell. **These are this audit's numbers, not published ones.**

`design = "choi"`: intercepts `~ U[1,100]`, discarding any budget line whose intercepts are *all*
in the lower half — the rule Crawford & Tian attribute to Choi et al. (2014) and the analogue of
Chen et al.'s `max{M,N} ≥ 0.5`.

| Bronars power | n = 8 | n = 11 | n = 25 | n = 50 |
|---|---|---|---|---|
| **K = 2** | 0.605 | 0.807 | **0.999** | **1.000** |
| **K = 3** | 0.547 | 0.762 | **0.999** | **1.000** |
| K = 4 | 0.443 | 0.701 | 0.991 | 1.000 |
| K = 5 | 0.357 | 0.563 | 0.983 | 1.000 |
| K = 8 | 0.161 | 0.273 | 0.838 | 0.997 |
| K = 12 | 0.038 | 0.113 | 0.435 | 0.905 |

`design = "lognormal"` (Crawford & Tian's `1/r_k ~ LogN(0,1)` benchmark): K = 2 gives
0.494 / 0.680 / 0.995 / 1.000; K = 3 gives 0.411 / 0.647 / 0.989 / 1.000; K = 8 gives
0.073 / 0.147 / 0.539 / 0.959; K = 12 gives 0.018 / 0.031 / 0.191 / 0.512.

**Three external checks that this simulator is not lying:**

1. K = 2, n = 25, Choi-style prices → **0.999**, against Chen et al.'s reported **99.9 %** on the same
   design family.
2. Direction and rough magnitude at K = 2, n = 8 → 0.605 and n = 11 → 0.807, against Andreoni &
   Miller's 78.1 % and 94.7 % for their two *specific, hand-chosen* 8- and 11-budget designs. A
   purpose-built design beating a random draw is the expected sign.
3. Lognormal, n ≈ 10: area (= 1 − power) crosses 0.9 between K = 8 and K = 12, against Crawford &
   Tian's "with T = 10, the Area exceeds 0.9 by K = 9".

**Power at a CCEI threshold, not at pass/fail.** The brief's gate is a threshold on CCEI
("if CCEI > 0.99 … this project is dead"), not a pass/fail on GARP. The relevant object is therefore
the whole CCEI distribution under the random benchmark, not just `P(CCEI < 1)`. Same simulator,
500 replications, Choi-style prices:

| K | n | mean random CCEI | P(CCEI<1) | P(CCEI<0.99) | P(CCEI<0.95) | P(CCEI<0.90) |
|---|---|---|---|---|---|---|
| 2 | 8 | 0.927 | 0.606 | 0.548 | 0.398 | 0.274 |
| **2** | **25** | **0.726** | 0.998 | **0.996** | 0.984 | 0.924 |
| 2 | 50 | 0.605 | 1.000 | 1.000 | 1.000 | 0.998 |
| **3** | **25** | **0.769** | 1.000 | **0.996** | 0.984 | 0.890 |
| 3 | 50 | 0.649 | 1.000 | 1.000 | 1.000 | 1.000 |
| 5 | 8 | 0.969 | 0.352 | 0.320 | 0.216 | 0.122 |
| 5 | 25 | 0.840 | 0.978 | 0.964 | 0.908 | 0.754 |

The mean random CCEI of **0.726** at (K=2, n=25) matches the ≈ 0.72 implied by Chen et al.'s reported
Selten scores — an independent cross-check on both. The (K=5, n=8) row is the cautionary one: a
uniform-random agent there has a *median CCEI of 1.000*, so a measured "CCEI = 0.99" would be
literally worse than chance.

Independently corroborating the same threshold effect from published data: Andreoni, Gillen &
Harbaugh (2013), Table 1, report for Bronars Method 1 on the Andreoni–Miller altruism design an
average simulated CCEI of **0.88** with 59 % of simulated samples below CCEI 0.95 and **69 % below
0.99** — so on that design **31 % of uniform-random agents would clear a 0.99 CCEI bar**. On the
Andreoni–Harbaugh (2009) risk design the corresponding figures are average simulated CCEI 0.82, 80 %
below 0.95, 88 % below 0.99.

---

## What this implies for the brief's n = 25–50 design

**1. On power at the brief's stated parameters, the brief is fine, and E4's F3 is falsified.**
At K = 2 (the brief's method step 1 says "prices `p_t`, income `m_t`; ask the agent to choose a
bundle `x_t`", and R1, the design it inherits, is two-commodity) and n = 25–50, Bronars power is
0.999–1.000 under both the Choi-style and lognormal price draws, and the mean CCEI of a
uniform-random agent is 0.61–0.73. A measured CCEI of 0.997 on such a design **is** a real finding:
it sits ~0.27 above the random benchmark. **E4 does not kill C4 and does not kill S1.**

**2. But the brief never reports power, and that omission is itself the defect.** `docs/CLAIMS.md`
records C4 as turning on a threshold — "if CCEI > 0.99 even when role-prompted, this project is
dead". A threshold decision taken on an unreported-power design is not interpretable, and the fix
costs nothing: the power computation runs on the budget sets alone, before any API spend. B&C's ECPF
case (pass 0.957 at power 0.088) is the standing demonstration of what happens when you skip it.
This is why `audit/BRONARS_NOTE.md` exists.

**3. S9's `n ≤ 60` cap is not binding on power at K = 2–3 — but it removes the only lever you have
in higher dimensions.** S9 caps n at 60 because the ordering search in the projection step blows up.
At K = 2–3 that costs nothing: power is already ≈ 1 by n = 25. The cost lands the moment K rises.
Crawford & Tian: going from T = 10 to T = 20 moves the Area-0.9 threshold only from K = 9 to K = 13;
at T = 50 the Area still hits 0.95 by K = 20. So with n capped at 60 you cannot recover a design that
has too many goods. **The binding constraint on the brief is K, not n**, and the brief never mentions
K at all.

**4. Two places the brief's own text invites the failure it is protected from.**
   - Method step 4 proposes evaluating downstream on "portfolio/resource-allocation payoff". A
     portfolio task with 8 assets at n = 25 has Bronars power ≈ 0.84 (this session's Choi-design
     grid); with 12 assets, ≈ 0.44. If the downstream task's CCEI is ever reported alongside the
     elicitation CCEI, they are not on the same footing.
   - The protocol's "multi-step agentic" condition is undefined in dimensionality. If a multi-step
     condition effectively raises the number of distinct goods, its power is a different (and lower)
     number from the baseline condition's, and CCEI is not comparable across conditions. **Comparing
     CCEI across conditions with different budget-set geometry compares two different tests.**

**5. Two consequences for the projection claim (C1) specifically.**
   - The projection operator moves bundles until GARP holds. On a low-power design, GARP already
     holds almost surely, so the projection degenerates to the identity — the same degenerate floor
     the brief already flags in preflight item 1, but reached by a route the brief does not list.
     **Low test power is a second, independent path to the degenerate floor.**
   - The "utility cost of projection" metric `‖x̃ − x‖` is denominated in the same geometry that sets
     the power. Reporting it without the area/power of the design makes it uninterpretable across
     conditions for the same reason CCEI is.

**6. Report predictive success, not the pass rate.** Whatever CCEI or GARP pass rate the pilot
produces, the reportable quantity is Selten's `m = r − (1 − power)`, plus the Selten/Dean–Martin
score (measured CCEI minus mean simulated CCEI). Both are one extra line of output from the same
Monte Carlo. R1 already reports all three; a paper that does not will be asked why by any reviewer
who knows this literature.

**7. Bronars power is necessary, not sufficient.** R1's own bootstrap power of 7.9 %–26.3 % on the
identical budget sets shows that a design can be unconditionally powerful and still conditionally
uninformative about the specific agent in front of you. If the pilot reports 99.9 % Bronars power and
a near-1.0 CCEI, the honest follow-up is a conditional index (bootstrap, or Hjertstrand's PURP/cPURP
curve) before claiming the agent is rational.

---

## Verdict

**E4 does not kill C4, S1, or S9.** The brief's stated design — n = 25–50 observations over 2 goods —
has Bronars power ≈ 0.999, and a uniform-random agent on that design scores a mean CCEI of ≈ 0.72.
The high CCEI figures the brief relies on are therefore *not* artefacts of an unfailable test, and R1
in fact already reports the power of its own design (99.9 %), which the brief neglected to carry over.
The proposed falsifier F3 is falsified, and I record that as a falsification rather than reinterpreting
it.

**E4 does establish three binding obligations, none of which the brief currently carries:**

1. **A reporting rule.** No CCEI number this project reports may appear without the Bronars power of
   the budget sets that produced it, plus predictive success `m = r − (1 − power)`. Costs nothing;
   runs before any API call. See `audit/BRONARS_NOTE.md`.
2. **A dimensionality bound.** Power collapses exponentially in the number of goods and n cannot buy
   it back (Crawford & Tian, Theorems 1 and 2, and their simulations). The brief specifies n but
   never K. Any condition with more than ~5 goods at n ≤ 60 needs its power computed and stated, and
   any condition below the threshold in `audit/BRONARS_NOTE.md` should be redesigned, not reported.
3. **A threshold-specific requirement.** The brief's S4 gate is a *threshold* on CCEI, not a
   pass/fail on GARP, so the correct diagnostic is the CCEI distribution under the random benchmark,
   not `P(reject GARP)`. On some published designs 31 % of uniform-random agents clear CCEI 0.99
   (Andreoni, Gillen & Harbaugh 2013, Table 1). The gate must be stated relative to the simulated
   CCEI distribution of the actual budget sets used.

**Risk if ignored:** the paper reports a CCEI, a reviewer who knows Beatty & Crawford asks "what was
the area?", and the answer does not exist. That is a recoverable referee report at K = 2 and a fatal
one at K = 8.

---

## One-line summary for `docs/CLAIMS.md`

> E4: at K=2, n=25–50 Bronars power is ~0.999 (random-agent CCEI ~0.72), so C4/S1/S9 survive — but power falls exponentially in K and n cannot recover it; report power with every CCEI.

---

## Fetch record

Instruments used: `curl`, OpenAlex, Crossref, Unpaywall (email parameter supplied on every request),
`scripts/arxiv_ft_search.py`, PyMuPDF text extraction. `hyperresearch fetch` was deliberately not
used (concurrent sibling agents contend on its SQLite database).

### Read in full

| Source | URL / identifier | Status |
|---|---|---|
| Crawford & Tian (2026), "The Empirical Content of Revealed Preference in High Dimensions" | `https://arxiv.org/pdf/2605.29361` | **200, 8 pp. + appendices, read in full.** Confirms arXiv:2605.29361v1 [econ.TH] 28 May 2026 |
| Beatty & Crawford (2011) — author-hosted copy | `https://users.ox.ac.uk/~econ0237/papers/RevisedPowerPaper.pdf` | **200, 12 pp., read in full.** Abstract, ECPF data, and the 0.957 / 0.912 / 0.045 results all match the published article |
| Chen, Liu, Shan & Zhong (arXiv:2305.12763) — reference R1 | `https://arxiv.org/pdf/2305.12763` | **200, 105 pp.** Read: main text §on rationality score, and Appendix C.2 "GARP Test Power Analyses" |
| Andreoni & Harbaugh (2008), "Power Indices for Revealed Preference Tests" | `https://harbaugh.uoregon.edu/Papers/power.pdf` | **200, 6 pp. (extract), read.** Source for Bronars' three methods |
| Andreoni, Gillen & Harbaugh (2013), "The Power of Revealed Preference Tests: Ex-Post Evaluation of Experimental Design" | `https://econweb.ucsd.edu/~jandreon/WorkingPapers/GARPPower.pdf` | **200, 50 pp.** Read: §3, §4.1, Table 1 |
| Hjertstrand (2019/2021), "Power Against Random Expenditure Allocation for Revealed Preference Tests", IFN WP 1309 (= *JEBO* 188:36–45, DOI `10.1016/j.jebo.2021.05.001`) | `https://ifnstorprodsc01.blob.core.windows.net/wfiles/wp/wp1309.pdf` | **200, 16 pp., read.** Source for the Andreoni–Miller 78.1 % / 94.7 % figures and the Bronars-Algorithm mapping |
| Demetry, Hjertstrand & Polisson, "Testing Axioms of Revealed Preference in Stata", IFN WP 1342 (= *Stata Journal* 22(2), 2022) | `https://ifnstorprodsc01.blob.core.windows.net/wfiles/wp/wp1342.pdf` | **200, 24 pp., read.** Source for the Dirichlet(1,…,1) implementation and the `powerps` definition of predictive success |
| Cherchye, Crawford, De Rock & Vermeulen (2008), "The Revealed Preference Approach to Demand" | `https://revealedpreferences.org/assets/articles/RevPref.pdf` | **200, 34 pp.**, power section read |
| 2008 ANPEC conference paper, "On the existence of well-behaved macro utility functions" | `https://www.anpec.org.br/encontro2008/artigos/200806301053170-.pdf` | **200, 15 pp.**, §2.2 and fn. 6 read. Used **only** as a secondary account of Bronars' own application |

### Could not be read (recorded, not papered over)

| Source | Attempt | Result |
|---|---|---|
| **Bronars (1987), *Econometrica* 55(3):693–698** | Unpaywall `10.2307/1913608` | `is_oa: false`, `oa_status: "closed"`, `oa_locations: []`, `has_repository_copy: false` |
| same | Semantic Scholar `DOI:10.2307/1913608` | HTTP 200; `openAccessPdf.status: "CLOSED"`; abstract elided by publisher |
| same | JSTOR `stable/1913608`, Econometric Society landing page | HTTP 200 landing pages, no accessible full text; WebFetch on the Econometric Society page returned **403** |
| same | targeted web search for any OA scan | none found |
| **Verdict** | — | **`unresolved`.** All method description in this note is secondary and marked as such. Bronars' own numerical results are *not* reported here beyond the two directional findings a named secondary source attributes to him. |
| Beatty & Crawford — published AER version | Unpaywall `10.1257/aer.101.6.2782` | `is_oa: false`, closed. Also closed: cemmap `10.1920/wp.cem.2010.1710`, IFS `10.1920/re.ifs.2024.0744`. Author-hosted copy used instead (above) |
| Hjertstrand — EconStor mirror | `https://www.econstor.eu/bitstream/10419/210950/1/1685477690.pdf` | **Blocked** by an Anubis proof-of-work bot wall. Routed to the IFN working-paper server instead |
| IFN direct site | `https://www.ifn.se/media/xf4bpowg/wp1342.pdf` | **Cloudflare interstitial.** Routed to the IFN blob-storage URL instead |
| A Fine Theorem blog post on Beatty & Crawford | WebFetch | **403.** Not needed; the paper itself was obtained |
| CORE API | `api.core.ac.uk/v3/search/works` | **502** |

### Instrument gaps

- **Semantic Scholar anonymous search is rate-limited in this environment.**
  `GET /graph/v1/paper/search` returned **HTTP 429**. Single-paper lookups by DOI
  (`/graph/v1/paper/DOI:…`) returned **200** and were used. Recorded as an environment gap, not as a
  literature finding.
- **arXiv full-text searches run** via `scripts/arxiv_ft_search.py`, all `[OK]` (real results pages,
  counts trustworthy): `"Bronars"` → 201 hits; `"power of nonparametric tests"` → 25;
  `"predictive success" AND "revealed preference"` → 20; `"Bronars" AND "power"` → 84;
  `"Bronars power"` → 3 (2208.07659, **2305.12763**, 2102.03436);
  `"Becker" AND "GARP" AND "power"` → 21; `"Selten" AND "predictive success" AND "GARP"` → 9
  (including 2605.29361). No search returned `EMPTY` or `ERROR`.
- **Figures read as text.** Crawford & Tian's `A(K)` curves are figures; the numbers quoted from them
  are the ones stated in their prose, not values read off the plots. The `(K, n)` grid in §(d) is
  this session's own Monte Carlo, computed because the paper does not tabulate the cells the brief
  needs.

### Reference-ledger effect

`audit/REFERENCE_LEDGER.md` rows R17 (Bronars 1987), R18 (Beatty & Crawford 2011) and R19 (Crawford &
Tian 2026) point at this note. On the evidence above: **R18 and R19 are supportable as `verified`**
(both documents fetched and read in full); **R17 must stay `unresolved`** — closed-access, no OA copy,
secondary sources only. R1 (arXiv:2305.12763) was also read in substantial part for this check, which
bears on kill-check E3.
