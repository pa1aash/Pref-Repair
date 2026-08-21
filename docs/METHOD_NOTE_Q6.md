# Method note Q6 — the false-CCEI-1.0 trap

*Resolves `docs/OPEN_QUESTIONS.md` Q6. Source read in full: Andrews, "Revealed Rationality:
Label-Free Evaluation and Regularization from Representation Theorems", arXiv:2608.05015v1
[econ.TH], 5 Aug 2026 — §3 (Lemma 1, pp. 8–9) and "Appendix: Proofs" (proof of Lemma 1, p. 18).
MD5 `a23ccbda8ecdb9032fb64f98bb0159fa`, identical to the file recorded in `audit/killcheck_E1.md`.
Every number below was produced on this machine with exact rational arithmetic; scratch scripts
were kept outside the repository.*

**Verdict: yes, Lemma 1 breaks the day-1 `ccei.py` as the brief specifies it, and the failure was
reproduced numerically.** The brief (`docs/F3-PLAN-ORIGINAL.md`, "Method" step 2) specifies "CCEI
… via binary search over e ∈ (0,1] with a transitive-closure/cycle check". On a dataset built from
round-number prices, that exact procedure returns **0.999999999998** on data that **violates
GARP** — tripping the S4 STOP gate ("if CCEI > 0.99 … this project is dead") on an artefact.

---

## Lemma 1, stated exactly

Andrews' §3 sets up the standard objects. Weak inequalities throughout:

- **Direct revealed preference.** If `x_t` was chosen when `x_s` was affordable — `p_t · x_s ≤ p_t · x_t`
  — then `x_t R_D x_s`. `R` is the transitive closure of `R_D`.
- **GARP.** If `x_t R x_s` then `p_s · x_t ≥ w_s`. In his gloss: "if `x_t` is revealed preferred to
  `x_s` (directly or through a chain), then `x_t` must not have been strictly inside the budget set
  at which `x_s` was chosen."
- **e-GARP.** "the relaxation in which budget constraints are tightened by a factor `e ∈ [0,1]`:
  `x_t` is directly revealed preferred to `x_s` under e-GARP **only if** `p_t · x_s ≤ e · p_t · x_t`."
- **CCEI.** `CCEI = sup{ e ∈ [0,1] : the data satisfy e-GARP }`.

He then states the problem in one sentence: *"Unfortunately, however, when a revealed preference
comparison holds with exact budget equality, the CCEI may equal one even though GARP fails."*
And then the repair, verbatim:

> **Lemma 1.** Suppose that the price vectors `p_t` are drawn independently across observations
> from distributions with densities with respect to Lebesgue measure, that each choice `x_t`
> depends only on observation `t`'s prices `p_t` and income `w_t`, with income fixed or drawn
> independently of the prices, and that choices exhaust their budgets, `p_t · x_t = w_t > 0` for
> all `t`. Then with probability one CCEI = 1 if and only if the data satisfy GARP.

Four hypotheses, all load-bearing:

1. **prices independent across observations, each with a Lebesgue density** — this is what makes
   the tie event measure-zero;
2. **each choice depends only on its own observation** `(p_t, w_t)` — no cross-round conditioning,
   so `p_t` stays independent of `x_s` for `s ≠ t`;
3. **income fixed, or drawn independently of prices**;
4. **budget exhaustion**, `p_t · x_t = w_t > 0`, which also guarantees `x_s ≠ 0`.

**The proof mechanism** (Appendix, p. 18) is a measure-zero argument plus a strictness argument,
and it is worth separating the two halves because only the first half is protected by the design:

- *Half one — no ties, almost surely.* Fix `t ≠ s`. Under (2) and (3), `p_t` is independent of
  `(x_s, w_t)`. Conditional on `(x_s, w_t)`, the event `p_t · x_s = w_t` confines `p_t` to the
  proper affine hyperplane `{q ∈ R^K : q · x_s = w_t}`, which has conditional — hence
  unconditional — probability zero under (1). Union over the finitely many ordered pairs: with
  probability one, `p_t · x_s ≠ w_t` for every `t ≠ s`.
- *Half two — on the no-ties event, CCEI is a certificate.* If GARP fails, take a violating cycle
  with repetitions removed: distinct `t_1, …, t_m`, `m ≥ 2`, `t_{m+1} = t_1`, with
  `p_{t_i} · x_{t_{i+1}} ≤ p_{t_i} · x_{t_i} = w_{t_i}` and at least one inequality strict. Because
  every comparison in the cycle is between *distinct* observations, no-ties upgrades **all** of them
  to strict. So `ρ = max_i (p_{t_i} · x_{t_{i+1}}) / (p_{t_i} · x_{t_i}) < 1`, and for every
  `e ∈ (ρ, 1]` the same cycle is a cycle of strict direct e-revealed-preference relations and
  violates e-GARP. Hence `CCEI ≤ ρ < 1`.

The whole result therefore hinges on one number: `ρ`, the largest expenditure ratio in the binding
cycle. **`ρ < 1` is exactly what a tie destroys**, and `ρ = 1` is exactly the false 1.0.

---

## The mechanism: why a tie breaks the binary search

Write `A[t][s] = (p_t · x_s) / w_t`, so `A[t][t] = 1`. Then `x_t R_D^e x_s ⟺ A[t][s] ≤ e`.

**Step 1 — the set of feasible efficiency levels is an interval, and it is half-open.**
Lowering `e` only removes edges from `R_e` and only makes the violation test harder to satisfy, so
`{e : e-GARP holds}` is an interval containing 0. Measured on 173 randomly drawn GARP-violating
datasets (T = 5, K = 2, prices with a Lebesgue density), **the supremum was attained 0 times out of
173.** The set is always `[0, CCEI)`, never `[0, CCEI]`. That is not a pathology of the tie case;
it is the generic shape. On the textbook two-observation violation `A = [[1, 9/10], [4/5, 1]]`,
e-GARP holds for every `e < 9/10` and fails at `e = 9/10`, so `CCEI = 9/10` and the sup is not
attained.

**Step 2 — the tie moves the missing right endpoint to exactly 1.** Suppose one comparison in the
only violating cycle sits at exact budget equality, `p_t · x_s = w_t`, i.e. `A[t][s] = 1`. Then:

- at `e = 1`, the direct relation `A[t][s] ≤ 1` holds **because the inequality is weak** — the edge
  is present, the cycle closes, GARP fails;
- at any `e < 1`, `A[t][s] = 1 > e`, so that edge **vanishes**, the cycle opens, and e-GARP holds.

So `{e : e-GARP holds} = [0, 1)` and `CCEI = sup [0,1) = 1`. The index is *correctly* 1. What is
false is the inference `CCEI = 1 ⟹ GARP`.

**Step 3 — bisection cannot see the endpoint.** A bisection on `[0,1]` (or on the brief's `(0,1]`)
only ever evaluates strictly interior midpoints. Every interior point of `[0,1)` passes, so the
lower bracket marches to 1 and the routine returns `1 − 2^{-N}`. **The single point where the
violation lives is the one point the search never tests.** Verified: 60 bisection iterations against
exact-rational expenditure comparisons return `0.9999999999999999`; a 40-iteration all-float
implementation in the style of the reference checker in `audit/BRONARS_NOTE.md` returns
`0.999999999998181`. Both are `> 0.99`; both round to `1.0` at four decimals.

Adding a "test `e = 1` first" short-circuit does not help either, because it only short-circuits
when GARP *holds* — the failing branch still falls through to the same blind bisection.

**Step 4 — the inequality directions a naive implementation gets wrong.** The tie is a boundary
point, so every `≤`/`<` choice around it changes the answer:

| where | correct | naive bug | effect on the minimal case |
|---|---|---|---|
| direct relation `x_t R_D^e x_s` | `A[t][s] ≤ e + tol` (**inclusive**) | `A[t][s] < e` — "strictly affordable" | violation **never detected at all**; `garp_holds` returns `True` |
| violation test `p_s · x_t < e · w_s` | `A[s][t] < e − tol` (**exclusive**) | `A[s][t] ≤ e` | flags indifference as a violation — any pair each of whose bundles sits exactly on the other's budget line, which GARP permits |
| bisection bracket | must be paired with an independent check at `e = 1` | bracket alone | returns `≈ 1.0` on violating data |

The first row is the one to watch: writing `if p_t @ x_s < w_t` because "strictly affordable" reads
naturally in English silently deletes exactly the comparisons Lemma 1 is about. Confirmed on the
minimal case: weak direct relation → violation found; strict direct relation → no violation found.

One caveat on convention. Andrews states the relaxation only on the *direct relation* side and
leaves the conclusion side implicit; his proof uses `p_{t_i} · x_{t_{i+1}} < e · p_{t_i} · x_{t_i}`.
The implementation used here takes the standard Afriat form (violation iff `x_t R_e x_s` and
`p_s · x_t < e · w_s`). The trap survives either convention — with the conclusion side left
un-relaxed (`p_s · x_t < w_s`) the minimal case still shows `CCEI = 1` with GARP failing, because
the tie edge is absent for every `e < 1` regardless of how the conclusion is written.

---

## The guard requirement

> **A `ccei.py` implementation must guard against X, tested by constructing an input where Y,
> expected output Z.**

**X — what must not happen.** The script must never derive a GARP verdict, or a STOP-gate verdict,
from the CCEI number. Concretely, three prohibitions:

- **X1.** No code path may infer `garp_holds` from `ccei == 1.0`, from `ccei > 1 − tol`, or from the
  bisection bracket. `garp_holds` must come from an independent exact evaluation of the
  revealed-preference relation at `e = 1`.
- **X2.** The direct-preference test must use a **weak, inclusive** comparison
  (`p_t · x_s ≤ e · w_t + tol`, `tol ≥ 0`), and the violation test a **strict, exclusive** one
  (`p_s · x_t < e · w_s − tol`). Neither may be flipped, and `tol` may not be widened to paper over
  a failing tie test.
- **X3.** The script must count and report `n_exact_ties` = the number of ordered pairs `(t, s)`,
  `t ≠ s`, with `|p_t · x_s − w_t| ≤ tol · w_t`, and must refuse to emit a STOP verdict while that
  count is non-zero and `garp_holds` is `False`.

**Y — the inputs that test it.** Four fixtures, all `T = 2`, `K = 2`, all exact in binary floating
point (see the next section for the base case). Let `ε = 1e-9 · w_1`.

- **Y1 (tie exactly on the line):** the minimal case below, `p_1 · x_2 = w_1 = 10`.
- **Y2 (tie nudged inside):** `x_2 = (8, 2 − ε)`, so `p_1 · x_2 = w_1 − ε`. Genuinely affordable,
  genuine GARP violation, `CCEI` genuinely just below 1.
- **Y3 (tie nudged outside):** `x_2 = (8, 2 + ε)` with `w_2` recomputed, so `p_1 · x_2 = w_1 + ε`.
  `x_2` is genuinely unaffordable at `t = 1`, there is no revealed-preference edge, and GARP holds.
- **Y4 (canary):** run Y1 through a deliberately mutated copy of the checker whose direct relation
  uses `<` instead of `≤`.

**Z — the required outputs.**

| fixture | `ccei` | `garp_holds` | `n_exact_ties` | gate fires? |
|---|---|---|---|---|
| Y1 | `1.0` exactly (`≥ 0.9999` from a bisection) | **`False`** | `1` | **no** |
| Y2 | `0.999999999` — strictly `< 1.0`, and `≥ 0.99` | `False` | `0` | **no** |
| Y3 | `1.0` | **`True`** | `0` | permitted, subject to the Bronars checks below |
| Y4 | `≥ 0.9999` | `True` — **and the test asserts this mutant is rejected** | `1` | n/a |

All four rows were run in exact rational arithmetic with `tol = 1e-12` and came out as tabulated.
Y2 and Y3 together pin `tol`: it must be small enough that Y3 stays clean, which forbids "fixing"
Y1 by widening the tolerance. Y4 is the mutation test that proves X2 is actually enforced rather
than accidentally true.

---

## Minimal failing test case

Two observations, two goods, integer prices, integer bundles, exact budget exhaustion.

| t | prices `p_t` | bundle `x_t` | income `w_t = p_t · x_t` |
|---|---|---|---|
| 1 | `(1, 1)` | `(5, 5)` | `10` |
| 2 | `(2, 1)` | `(8, 2)` | `18` |

**Expenditure matrix** `E[t][s] = p_t · x_s`, and its income-normalised form `A[t][s] = E[t][s]/w_t`:

```
E = [[10, 10],        A = [[  1,   1 ],
     [15, 18]]             [5/6,   1 ]]
```

**The revealed-preference relation at e = 1.**
`A[1][2] = 1 ≤ 1`, so `x_1 R_D x_2` — the tie. `A[2][1] = 5/6 ≤ 1`, so `x_2 R_D x_1`, strictly.

**The cycle.** `x_1 R x_2` and `p_2 · x_1 = 15 < 18 = w_2`, so `x_2` was chosen when `x_1` was
strictly cheaper and available. GARP requires `p_2 · x_1 ≥ w_2`. **GARP is violated.**

In words: at observation 1 the two bundles cost exactly the same (10 each) and the agent took
`x_1`; at observation 2 the agent took `x_2` even though `x_1` was strictly inside that budget.
That is a genuine, non-marginal inconsistency, not a rounding artefact.

**The efficiency sweep.** e-GARP was evaluated in exact rational arithmetic:

| `e` | 0.5 | 0.8 | 5/6 | 0.9 | 0.99 | 0.999 | 0.9999999 | **1.0** |
|---|---|---|---|---|---|---|---|---|
| e-GARP violated? | no | no | no | no | no | no | no | **yes** |

`{e : e-GARP holds} = [0, 1)`. `CCEI = sup [0,1) = 1`, and the supremum is not attained.

**What each implementation returns.**

| implementation | returns | verdict against the S4 gate |
|---|---|---|
| naive bisection on `[0,1]`, 60 iterations, exact rationals | `0.9999999999999999` | **gate fires — project declared dead** |
| naive bisection on `[0,1]`, 40 iterations, float, normalised-price style of `audit/BRONARS_NOTE.md` | `0.999999999998181` | **gate fires — project declared dead** |
| bisection with a "test `e = 1` first" short-circuit | `0.9999999999999999` | **gate fires — short-circuit does not help** |
| GARP check with a **strict** direct relation (`<`) | reports `garp_holds = True` | **violation never seen at all** |
| GARP check with a **weak** direct relation (`≤`, zero or positive tolerance) | reports `garp_holds = False` | correct |
| guarded implementation (X1–X3) | `ccei = 1.0`, `garp_holds = False`, `n_exact_ties = 1` | **gate does not fire** |

**Confirmation.** This was verified numerically, not derived on paper alone. The dataset was run
through both a naive and a guarded implementation using the repository interpreter (`.venv/bin/python`),
with the revealed-preference relation evaluated in exact rational arithmetic so that no
floating-point question can be raised about the tie. The naive implementation produced the false
answer on the first attempt; no search over candidate datasets was needed. The float reference
checker from `audit/BRONARS_NOTE.md` correctly flags the GARP violation — the bug is in the CCEI
layer, not in that GARP layer.

**How likely is this in practice?** The tie event is not exotic on tidy prices. Measured over
random designs with `T = 25`, `K = 2`, prices drawn on a grid in `[1, 5]`, income exhausted, choice
on an 11-point grid:

| price grid | share of ordered pairs `(t,s)` that are exact ties | share of datasets containing at least one tie |
|---|---|---|
| integers (step 1) | 7.3 % | **100 %** |
| halves (step 0.5) | 3.4 % | 100 % |
| quarters (step 0.25) | 1.5 % | 99.5 % |
| one decimal (step 0.1) | 0.47 % | 92 % |
| two decimals (step 0.01) | 0.04 % | 20 % |
| continuous (Lebesgue density) | **0.00 %** | **0 %** |

And the trap itself — `CCEI = 1` exactly while GARP fails — over uniform-random agents on the same
designs (`S = 1500`, `T = 8`; exact arithmetic):

| price grid | P(GARP fails) | P(CCEI > 0.99) | P(GARP fails **and** CCEI > 0.99) | of which: P(CCEI = 1 **and** GARP fails) |
|---|---|---|---|---|
| integers (step 1) | 0.674 | 0.515 | **0.189** | **0.189** |
| halves (0.5) | 0.715 | 0.415 | 0.130 | 0.117 |
| quarters (0.25) | 0.737 | 0.348 | 0.085 | 0.062 |
| one decimal (0.1) | 0.730 | 0.323 | 0.053 | 0.019 |
| two decimals (0.01) | 0.724 | 0.312 | 0.036 | 0.001 |
| continuous | 0.711 | 0.341 | 0.052 | **0.000** |

Read the top row: on integer prices, **19 % of all uniform-random agents produce an exact CCEI of
1.0 while genuinely violating GARP**, and that accounts for essentially the entire false-clear rate
at `T = 8`. Read the bottom row: with prices drawn from a density the tie trap is gone. Across
**63,200 continuous-price replications** (`T` = 2, 3, 5, 8, 10 and 25, with both decile-grid and
continuous budget shares) there were **12,102 genuine GARP failures and not one exact CCEI of
1.0** — exactly what Lemma 1 predicts.

The trap weakens as `T` grows, because it needs *every* violating cycle to be tie-bound: at `T = 25`
on integer prices with uniform-random agents it falls to 1.0 %. But it comes straight back for
near-rational agents, which is the regime the S4 gate actually operates in: a `T = 25` agent
targeting a fixed budget share with ±1 grid-step noise on a quarter-point price grid shows
`P(CCEI = 1 and GARP fails) = 8.7 %`, against `0.0 %` for the same agent on continuous prices.

---

## Andrews' design fix, and why an implementation guard is still needed

Andrews' remedy is explicit and it is an **elicitation-design** remedy: *"the fact that the CCEI may
equal one even when GARP fails can be addressed by a suitable elicitation strategy."* Draw prices
independently across observations from continuous distributions, keep income fixed or independent
of prices, let each choice depend only on its own observation, and require budget exhaustion. Then
the tie event lies in a finite union of proper affine hyperplanes and has probability zero, so
`CCEI = 1 ⟺ GARP` almost surely. §5 restates this as a standing side-condition: the choice problems
"need not be sampled in any specific way (save for the conditions needed to apply Lemma 1)."

**What it buys, precisely: it makes the bad event measure-zero on data you generate yourself.**
That is real and it is confirmed above — zero tie traps in 63,200 continuous-price replications
carrying 12,102 real GARP failures. Adopt it: `docs/DECISIONS.md` should record continuous price
draws plus enforced budget exhaustion as a design constraint on the pilot.

**What it does not buy: anything at all about data the script is handed.** It is a distributional
guarantee about a sampler, not a property of the estimator. Four ways the guarantee is void while
the code is unchanged:

1. **The inherited design already violates the hypothesis.** The design this project takes its
   0.997–0.999 ceiling from (arXiv:2305.12763, reference R1) specifies its price parameters as
   `M, N ∈ [0.1, 1]` with `max{M, N} ≥ 0.5` and — in the same footnote, in *every* condition
   including the baseline — **"We keep two decimals."** That is a 91-point discrete price grid with
   no Lebesgue density. Its discrete-choice condition then adds a decile grid on the choice side:
   11 options indexed `i = 1, …, 11` at `M_i = (i − 1) × 10 × M` (the companion expression for `N_i`
   extracts as `100 − (i−1) × 10 × N`, which is almost certainly a mangled rendering of
   `(100 − (i−1) × 10) × N`; the exact form is not load-bearing here, and it should be re-read from
   the PDF before being quoted). On that exact design the tie trap is small but non-zero —
   `P(CCEI = 1 and GARP fails)` measured at 0.7 % for uniform-random agents at `T = 8` on the
   discrete-choice condition, 0.3 % for near-rational agents at `T = 25` — and the trap is not the
   binding problem there (see the next section). The point stands regardless: **the hypothesis of
   Lemma 1 fails on the design the project inherits**, so the guarantee simply does not apply to
   any replication of it.
2. **Replication.** A reviewer, a co-author, or a future session re-runs `ccei.py` on hand-written
   prices — `(2, 3)`, income 12 — because that is what people type into a test. Integer prices are
   the worst row of the table above.
3. **Prompt legibility.** Prices are shown to a model as text. There is real pressure to round them
   for readability, and rounding is exactly the operation that destroys the density.
4. **Elicited bundles are discrete anyway.** Even under continuous prices, a model asked to split
   100 points returns integers, and Lemma 1's hypothesis is on the *price* side, so this alone is
   survivable — but it is one more reason the input distribution in production is not the input
   distribution in the lemma.

So the fix is layered: **design fix removes the trap from data you generate; guard X1–X3 removes it
from data you receive.** Ship both. The guard costs one extra transitive-closure evaluation at
`e = 1` per dataset and a tie counter — measured in microseconds at `n ≤ 60`.

---

## Interaction with the Bronars threshold trap

`audit/BRONARS_NOTE.md` and kill-check E4 establish a second, unrelated way the S4 gate fires
wrongly: on the Andreoni–Miller altruism design, **31 % of uniform-random simulated agents clear
CCEI 0.99** (Andreoni, Gillen & Harbaugh 2013, Table 1). That trap is about the *threshold* being
above the chance level of a low-power design. Q6's trap is about the *index* failing to certify
GARP. They are independent, and they are separated cleanly in the measurements above:

| | tie trap (Q6) | threshold trap (E4) |
|---|---|---|
| what goes wrong | `CCEI = 1` exactly while GARP fails | `CCEI ∈ (0.99, 1)` while GARP fails |
| cause | a comparison at exact budget equality; the sup of `[0, 1)` is 1 | the design has too little power for 0.99 to mean anything |
| Andrews' design fix removes it? | **yes — measured 0 in 63,200 continuous-price replications** | **no** |
| implementation guard removes it? | yes (X1–X3) | no — needs the simulated null distribution |
| measured, `T = 25`, near-rational agent, ±1 grid step | 8.7 % on quarter-point prices, **0.0 %** continuous | 23.1 pp of the 31.8 % total false-clear on quarter-point prices, and **29.0 %** on continuous prices |

The last row is the one to internalise. For a `T = 25` near-rational agent, quarter-point prices
give a total false-clear rate `P(GARP fails and CCEI > 0.99)` of **31.8 %**, of which 8.7 pp is the
tie trap and 23.1 pp is threshold slack. Moving to continuous prices takes the tie component to
exactly zero and leaves the threshold component at **29.0 %**. **Fixing Q6 does not fix Q5, and
vice versa.**

**One Monte Carlo checks both.** The Bronars run that `audit/BRONARS_NOTE.md` already mandates
before any API call — uniform-random agents on the actual budget sets, `S ≥ 2000` — needs three
extra recorded fields per replication and then answers both questions at once:

- `garp_holds` — exact check at `e = 1`, weak direct relation. Averaging gives **Bronars power**.
- `ccei` — the bisection value. Its distribution gives the **mean simulated CCEI** and
  `P(simulated CCEI > e)` at the gate's threshold.
- `n_exact_ties` — the tie counter from X3.

Then report the joint cells, which is where both traps become visible in one table:

- `P(garp_holds = False and ccei > 0.99)` — the **total false-clear rate** of the gate under the
  random-agent null. If this is not near zero, the gate is broken, whatever the cause.
- `P(garp_holds = False and ccei ≥ 1 − δ)` for the bisection tolerance `δ` — the **tie-driven**
  component. Non-zero means the design violates Lemma 1's hypotheses and the guard is doing work.
- The difference between the two — the **power-driven** component, which only a redesign or a
  different threshold can fix.
- `mean(n_exact_ties)` — a design diagnostic that needs no agent at all. It should be **exactly
  zero** under continuous prices; any non-zero value is proof the price sampler is on a grid.

Crucially, run this Monte Carlo on the **exact prices and exact response format the pilot will
use** — the same rounding, the same grid, the same integer point totals. A Monte Carlo run on
pristine continuous prices will report zero ties and certify a script that is about to be handed
two-decimal prices.

---

## Acceptance checklist for the day-1 script

A future session can execute this directly, in order, before the first API call.

1. **Write `src/ccei.py` to return a record, not a number.** Minimum fields: `ccei` (float, the
   bisection value), `garp_holds` (bool, from an independent exact evaluation at `e = 1`),
   `n_exact_ties` (int), `n_observations`, `n_goods`, and the tolerance actually used. No caller may
   reach a STOP verdict from `ccei` alone.
2. **Use the weak/strict pair correctly.** Direct relation `p_t · x_s ≤ e · w_t + tol`; violation
   test `p_s · x_t < e · w_s − tol`; one shared `tol`, default `1e-12` on income-normalised prices,
   recorded in the output.
3. **Add the four fixtures Y1–Y4 as unit tests** with the expected outputs in the table above.
   Y1 must show `ccei ≥ 0.9999` together with `garp_holds = False`; Y4 must fail the mutant.
4. **Assert the gate contract in code:** the STOP verdict may be returned only when
   `garp_holds is True`. Raise on `ccei > 0.99 and garp_holds is False` rather than returning a
   verdict, and print the offending tie pairs `(t, s)`.
5. **Make the price sampler continuous by construction** — draw `p_t` from a continuous
   distribution independently across observations, do not round for the prompt beyond the precision
   the model is actually shown, keep income fixed or independently drawn, and enforce
   `p_t · x_t = w_t` on every elicited bundle (reject or renormalise otherwise). Record the sampler
   and the seed.
6. **Run the design audit with no agent:** draw the budget sets, compute `n_exact_ties` across all
   ordered pairs, and require it to be **0**. A non-zero count means the sampler is on a grid; fix
   the sampler, do not raise `tol`.
7. **Run the single combined Monte Carlo** on those exact budget sets and that exact response
   format, `S ≥ 2000`, seed recorded, per the recipe in `audit/BRONARS_NOTE.md` extended with the
   three fields above. Report: Bronars power, mean simulated CCEI, `P(CCEI > 0.99)`,
   `P(garp_holds = False and ccei > 0.99)`, and the tie-driven share of that last quantity.
8. **Gate on the Monte Carlo before spending anything.** Proceed only if Bronars power ≥ 0.80 (per
   `audit/BRONARS_NOTE.md`), the tie-driven false-clear share is 0, and the total false-clear rate
   under the random-agent null is small enough that "CCEI > 0.99" carries information on this
   design. If it is not, the threshold must be replaced by the simulated null distribution — that
   is Q5's business, not Q6's, and Q6's guard will not rescue it.
9. **Cite Lemma 1 wherever the CCEI method is described** — arXiv:2608.05015 §3 — and state in the
   paper that prices are drawn from continuous distributions with budgets exhausted *for this
   reason*. A referee who knows the note will look for it.
10. **Re-run steps 6–8 for every condition** whose budget-set geometry or response format differs
    (discrete-choice, alternative price framing, any higher-dimension task). Neither the tie
    diagnostic nor the power number transfers across designs.
