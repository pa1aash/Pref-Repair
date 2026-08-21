# BRONARS_NOTE — the power number that must accompany every CCEI

*Standing rule for this project. Written during kill-check E4; see `audit/killcheck_E4.md` for the
evidence and the fetch record. Read this before designing any budget sets or reporting any CCEI.*

---

## The rule

> **Any CCEI number this project ever reports must be paired with the Bronars power of the budget
> sets that produced it, because a high CCEI under low test power means "the test could not have
> failed", not "the agent is rational".**

This is not a stylistic preference. It is the difference between a result and a tautology.

CCEI is a goodness-of-fit statistic on a *test*, and a test only carries information if it could have
come out the other way. The revealed-preference literature has had a name for this since 1987 —
Bronars power — and a correction for it since 2011 — Selten's measure of predictive success. The
canonical demonstration of why it matters is Beatty & Crawford's Spanish household panel: a GARP pass
rate of **0.957**, which sounds like a triumph, against a relative area of **0.912**, meaning the
test had only **8.8 % power**. Corrected predictive success: **0.045**. In their words, the model
"out-performed a random number generator - but only by 4.5%", and "for many households the relative
area of the target is equal to 1 - the theory cannot fail."

The three quantities are linked by one identity, which is the whole of the argument:

```
area  a  =  1 − Bronars power                       (Beatty & Crawford 2011, §3)

predictive success  m  =  pass rate  −  area
                       =  pass rate  +  Bronars power  −  1     (Selten 1991)
```

Bronars power costs nothing to compute. It depends only on the prices and budgets — **the agent's
choices never enter it** — so it can and must be computed *before* a single API call is spent.

---

## How to compute Bronars power for a given design

Bronars' alternative hypothesis is Becker's (1962) "irrational" consumer: choices drawn uniformly at
random from the budget hyperplane, exhausting the budget. Power is the probability that such a
consumer violates GARP on your budget sets.

**Recipe** (Bronars' Algorithm 1, the one the literature means when it says "Bronars power"; the
implementation matches `powerps` in the Stata package `rpaxioms` and `bronars` in the R package
`revpref`):

1. Take the design: `T` observations, `K` goods, prices `p_t`, expenditure `m_t = p_t · x_t`.
   Work with income-normalised prices `r_t = p_t / m_t`, so that `r_t · x_t = 1`.
2. For each observation `t`, draw budget shares uniformly on the (K−1)-simplex:
   `w_t ~ Dirichlet(1, …, 1)`. Equivalently, draw `K` independent `Exponential(1)` variates and
   normalise. Do **not** draw quantities uniformly in a box and rescale — that is a different, wrong
   distribution.
3. Convert to a bundle: `x_kt = w_kt / r_kt`.
4. Test GARP on `{r_t, x_t}`.
5. Repeat `S` times (1,000 is the `rpaxioms` default; 2,000–10,000 is cheap here).
   **Bronars power = (number of replications violating GARP) / S.**

Step 2 is the entire content of the benchmark. The map `x ↦ w` with `w_k = r_k x_k` is linear with a
constant Jacobian, so "uniform on the budget hyperplane" and "uniform on the budget-share simplex"
are the same distribution — which is why the geometric quantity (Selten's Area) and the statistical
quantity (Bronars power) are one minus each other.

### Reference implementation

```python
import numpy as np

def garp_violated(r, x):
    """r: T x K income-normalised prices (r_t . x_t = 1).  x: T x K bundles."""
    E = r @ x.T                                    # E[i,j] = r_i . x_j
    D = (E <= 1.0 + 1e-12)                         # x_i R^0 x_j  (directly revealed preferred)
    n = D.shape[0]
    C = D | np.eye(n, dtype=bool)                  # reflexive
    k = 1
    while k < n:                                   # transitive closure by repeated squaring
        C = C | (C @ C)
        k *= 2
    # GARP: x_i R x_j  =>  not x_j P^0 x_i, i.e. r_j . x_i >= 1
    return bool(np.any(C & (E.T < 1.0 - 1e-12)))

def bronars_power(prices_normalised, sims=2000, seed=0):
    """prices_normalised: a callable rng -> (T x K) array of r, i.e. THE DESIGN."""
    rng = np.random.default_rng(seed)
    K = prices_normalised(rng).shape[1]
    hits = 0
    for _ in range(sims):
        r = prices_normalised(rng)
        w = rng.dirichlet(np.ones(K), size=r.shape[0])   # uniform on the simplex
        hits += garp_violated(r, w / r)
    return hits / sims
```

### The variant you also need: power at a CCEI threshold

This project's S4 gate is a *threshold on CCEI* ("if CCEI > 0.99 … this project is dead"), not a
pass/fail on GARP. `P(reject GARP)` is the wrong statistic for a threshold rule. Compute the whole
CCEI distribution under the same random benchmark and report:

- the **mean simulated CCEI** — the "chance" level for your design;
- **`P(simulated CCEI < e)`** at whatever `e` your gate uses (0.99, 0.95, 0.90);
- the **Selten / Dean–Martin score** = measured CCEI − mean simulated CCEI.

To do it, replace the pass/fail check with a bisection on the efficiency level. `x_i R^0_e x_j` iff
`E[i,j] ≤ e`; GARP at level `e` is violated iff some `C[i,j]` holds with `E[j,i] < e`; CCEI is the
largest `e` with no violation. Bisect on `[0, 1]` to `1e-4`.

Why this matters concretely: on the Andreoni–Miller altruism design, Andreoni, Gillen & Harbaugh
(2013, Table 1) report that 69 % of uniform-random simulated subjects had CCEI below 0.99 — meaning
**31 % of pure random agents would have cleared a CCEI-0.99 bar on that design.** A gate stated
without the simulated CCEI distribution of the actual budget sets is not a gate.

### And the check that Bronars power cannot give you

Bronars power is *unconditional*: it ignores where the agent actually chose. Andreoni, Gillen &
Harbaugh's objection, in their words: "Suppose … the budgets offered did not intersect near the
points where individuals are actually choosing. Then if preferences do not conform to utility
maximization, the test would be unlikely to discover it. This is true even if Bronars' analysis shows
that randomly made choices provide a high probability of violations."

This is not hypothetical for this project. The paper this project inherits its design from
(arXiv:2305.12763) reports **99.9 % Bronars power** and, on the *same budget sets*, **bootstrap
power of 7.9 %–26.3 %** for its language-model observations. Both numbers are correct; they answer
different questions. So:

> **Bronars power is necessary, not sufficient.** Report it always. If it is high *and* the measured
> CCEI is near 1, run a conditional index too — bootstrap power, or Hjertstrand's PURP/cPURP curve —
> before claiming the agent is rational rather than merely untested.

---

## What power level is acceptable

There is **no threshold sanctioned by the literature**, and this note does not invent one. What the
literature supplies is the identity `m = pass rate − (1 − power)` and a body of applied practice.
The operational rules below are this project's own conventions, chosen so that reported CCEIs are
interpretable; they are stated as conventions, not as findings.

| Bronars power of the design | Verdict | What to do |
|---|---|---|
| **≥ 0.95** | Acceptable. Predictive success ≈ pass rate; a high CCEI is informative. | Report power and `m` alongside CCEI, and move on. |
| **0.80 – 0.95** | Marginal. Up to 20 % of the pass rate is unearned. | Report power and `m` prominently; do not report a bare pass rate or a bare CCEI anywhere. |
| **< 0.80** | Not reportable as evidence of rationality. | Redesign the budget sets before collecting data. Do not "fix" it in the write-up. |
| **< 0.50** | The test is close to unfailable. | The projection operator will also be near-degenerate (GARP already holds almost surely), so this is a second, independent route to the brief's degenerate floor. Stop. |

For calibration, published Bronars power on designs this project is adjacent to:

| design | n | K | Bronars power | source |
|---|---|---|---|---|
| Andreoni & Miller (2002), Group 1 | 8 | 2 | 78.1 % | reported in Hjertstrand, IFN WP 1309 §5.1 |
| Andreoni & Miller (2002), Group 2 | 11 | 2 | 94.7 % | same |
| Andreoni & Miller altruism design, recomputed as Bronars M1 | 8–11 | 2 | 75 % (mean simulated CCEI 0.88) | Andreoni, Gillen & Harbaugh (2013), Table 1 |
| Andreoni & Harbaugh (2009) risk design, Bronars M1 | — | 2 | 91 % (mean simulated CCEI 0.82) | same |
| Choi et al. (2014)-style random prices, as used in arXiv:2305.12763 | 25 | 2 | **99.9 %** | arXiv:2305.12763, Appendix C.2 |
| Spanish ECPF household panel (observational) | ≤ 8 | 5 | **8.8 %** (area 0.912) | Beatty & Crawford (2011) |

The last row is the warning. Observational price variation over a handful of periods across five
commodity groups produced a test that essentially could not fail.

### The dimensionality trap — the part that is easy to walk into

Power **falls exponentially in the number of goods**, and adding observations does not buy it back.
Crawford & Tian (2026, arXiv:2605.29361) prove that for fixed `T`, Selten's Area
`A_K ≥ 1 − C_T·exp(−c₁K)` (graph-theoretic) and `A_K ≥ 1 − T(T−1)·exp(−c₂K)` (Afriat LP), so
`A_K → 1` and power → 0 as `K` grows. Their simulations show it bites at moderate `K`:

- `T = 10`: Area exceeds 0.9 by `K = 9`, and 0.95 by `K = 11`.
- `T = 20`: those thresholds move only to `K = 13` and `K = 15`.
- `T = 50`: Area still reaches 0.95 by `K = 20`.
- `K = 24`, `T = 10`: Area **0.9996** — power 0.0004. Imposing additive separability into 6 groups of
  4 pulls it back to 0.005.

Their own caveat, repeated so it is not overstated: the result is asymptotic, "not a monotonicity
theorem for small steps in K".

**Two goods is not a limitation of this project's design; at n = 25–50 it is the reason the design
works.** Any move to more goods — a portfolio task, a resource-allocation task, a "multi-step
agentic" condition with a wider commodity space — changes the test, and its power must be recomputed
for that condition rather than inherited from the 2-good baseline. **CCEI is not comparable across
conditions whose budget-set geometry differs.**

### Design choices that raise power

- **Make budget lines cross, near where choices actually fall.** This is the whole mechanism.
  "If there are no intersections at all, then irrational behavior can never be detected"
  (Cherchye, Crawford, De Rock & Vermeulen 2008).
- **Do not vary income without varying relative prices.** Parallel outward shifts are the classic
  power-killer: Beatty & Crawford's opening example (`p1=[3,4]`, `p2=[4,3]`, budgets 10 and 5) has
  area exactly 1 — no choice whatsoever can violate GARP.
- **But do not maximise relative price variation either — power is not monotone in it.** Beatty &
  Crawford's own worked pair: `[3,4]`/`[4,3]` at equal budgets gives area 0.816; the *more extreme*
  `[2.5,5]`/`[5,2.5]` gives area 0.889 — less power. Extreme price ratios push the crossing region
  into a corner of the simplex, and corners hold little volume. Crawford & Tian find the same at
  `T = 25`: reducing the price-dispersion parameter σ from 1.0 to 0.5 *raises* power substantially,
  because tightly-clustered constraints "cross frequently and the relative prices are similar but not
  identical". Aim for moderate, non-degenerate relative-price variation.
- **Use an explicit crossing-forcing draw rule.** The Choi et al. (2014) rule — draw budget-line
  intercepts uniformly on `[a, b]`, then discard any budget line whose intercepts are *all* in the
  lower half `[a, b/2]` — is what the design in arXiv:2305.12763 implements as `M, N ∈ [0.1, 1]` with
  `max{M, N} ≥ 0.5`, and it is what delivers the 99.9 % figure.
- **Prefer a fixed, power-screened design to a naive adaptive one in higher dimensions.** Crawford &
  Tian simulate the Blundell–Browning–Crawford sequential-maximum-power path and find that at
  `K = 10` its Area is 0.97 against 0.77 for the benchmark, and by `K = 20` it reaches 0.9996 — the
  adaptive design is *worse* in high dimensions, because an extreme price vector can shift the next
  constraint so far in or out that constraints stop crossing.
- **Screen candidate designs by simulation, not by intuition.** Generating 20 candidate price
  sequences, computing Bronars power for each, and keeping the best is seconds of compute and is the
  only way to know.
- **Fix the design across conditions.** If baseline, persona, framing and agentic conditions use
  different budget sets, their CCEIs are not comparable. Use the *same* budget sets across
  conditions, so that power is held constant and the only thing varying is the agent.

---

## Checklist for the experiment-design session

Run this **before** writing `ccei.py`'s query loop and before spending anything on API calls.

- [ ] **Fix `K` explicitly and write it down.** The brief specifies `n = 25–50` and never states the
      number of goods. `K` is the binding constraint on power; `n` is not.
- [ ] **Compute Bronars power on the candidate budget sets** using the recipe above, `S ≥ 2000`, and
      record the random seed. No API calls until this number exists.
- [ ] **Compute the simulated CCEI distribution too** — mean, median, and `P(CCEI < e)` at the
      efficiency levels any gate or headline number will use (0.99 for the S4 gate).
- [ ] **Check the gate against the benchmark.** If the S4 gate is "CCEI > 0.99 means dead", verify
      that a uniform-random agent on these exact budget sets would *not* clear 0.99 at a
      non-negligible rate. If it would, the gate is measuring the design, not the agent.
- [ ] **Redesign if power < 0.80.** Use the design levers above — force crossings, moderate the price
      dispersion, apply the Choi-style discard rule, screen 20 candidate draws and keep the best.
      Do not proceed and caveat later.
- [ ] **Use one budget-set design across all conditions** (baseline / persona / framing / agentic) so
      power is constant and CCEI differences are attributable to the agent.
- [ ] **Recompute power separately for any downstream or higher-dimension task**, especially a
      portfolio or resource-allocation task. Never inherit the 2-good baseline's power number.
- [ ] **Pre-register the reporting format**, so no number can escape without its power:
      `CCEI = _____ (n = ___, K = ___, Bronars power = _____, predictive success m = r − (1 − power) = _____, mean simulated CCEI = _____)`.
- [ ] **If Bronars power is high and measured CCEI is near 1, add a conditional index** — bootstrap
      power or a PURP/cPURP curve — before making any claim that the agent is rational.
- [ ] **Report the area, not just the power, in the paper.** Beatty & Crawford's framing ("how
      demanding was the test?") is the one a referee who knows this literature will use.

---

## Sources

Read in full for this note: Beatty & Crawford (2011), *AER* 101(6):2782–2795, DOI
`10.1257/aer.101.6.2782` (author-hosted copy; the AER version and both cemmap/IFS working-paper DOIs
are closed on Unpaywall). Crawford & Tian (2026), arXiv:2605.29361v1. Chen, Liu, Shan & Zhong,
*PNAS* 120(51), 2023, arXiv:2305.12763, Appendix C.2. Andreoni & Harbaugh (2008) and Andreoni,
Gillen & Harbaugh (2013), power-index papers. Hjertstrand, IFN WP 1309 (= *JEBO* 188:36–45).
Demetry, Hjertstrand & Polisson, IFN WP 1342 (= *Stata Journal* 22(2), 2022). Cherchye, Crawford,
De Rock & Vermeulen (2008), "The Revealed Preference Approach to Demand".

**Bronars (1987), *Econometrica* 55(3):693–698, DOI `10.2307/1913608`, could not be obtained.** It is
closed-access with no OA copy anywhere (Unpaywall `is_oa: false`, zero OA locations; Semantic Scholar
`openAccessPdf.status: "CLOSED"`). Every description of his method in this note is taken from named
secondary sources that restate it, and no numerical result is attributed to Bronars himself. Full
fetch record in `audit/killcheck_E4.md`.
