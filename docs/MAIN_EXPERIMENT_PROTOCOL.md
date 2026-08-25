# Main experiment protocol — written before any data collection

Written 2026-08-26, after `docs/FRAMING.md`'s second amendment (C1 rescoped to 1.5B with a 3B
null-effect control; C3 added on the discard-selection problem). This document is Part Two of that
session's mandate: design the full main experiment. **No model has been queried for this experiment
at the time of writing.** Deviations from this document, if any arise during Part Three, are recorded
as deviations in `docs/MAIN_EXPERIMENT_RESULTS.md`, not silently absorbed — same standing rule as
`docs/PILOT_PROTOCOL.md`.

Cost so far: zero. Local inference only, per standing instruction. No commercial endpoint contacted.

---

## 1. Model roster

**Confirmed: `qwen2.5:1.5b-instruct-q4_K_M` (headroom model, per amended C1) and
`llama3.2:3b-instruct-q4_K_M` (null-effect control, per amended C1).** Both already verified to load
and generate in the pilot; both re-verified healthy at the start of this session.

### The third-family feasibility check, done empirically rather than estimated

`gemma2:2b-instruct-q4_K_M` (1.7 GB on disk) was pulled and tested on this machine during this
session, matching the pilot's own verification bar ("both were verified to load and answer a
trivial prompt before this protocol was written").

**Individually, it works and works well.** First load: 8.5 s. A later reload after other models had
been resident: 0.3 s. Both far faster than the pilot's originally measured 296 s swap penalty — this
machine's actual swap cost varies by an order of magnitude depending on prior memory state, which is
itself a finding (below).

**But the 3-model roster failed under sustained testing, and the failure was observed, not
hypothesized.** Cycling between `gemma2:2b` → `llama3.2:3b` → `qwen2.5:1.5b` in quick succession to
measure fresh swap timings pushed `PhysMem` to 89 MB unused (`top -l 1`), `ollama ps` showed **two**
models resident simultaneously (`gemma2:2b` and `llama3.2:3b` both listed, contradicting the pilot's
assumed one-model-at-a-time eviction behaviour), and the `qwen2.5:1.5b` load that followed took 137 s
— then the ollama server **stopped responding entirely** and had to be restarted via
`brew services start ollama`. No data was lost (all three model blobs survived on disk), but the
server crash is real, measured evidence that this exact machine cannot be trusted to hold a
third distinct model family in rotation over a multi-hour run without intervention.

**Decision: proceed with the two-model roster.** `gemma2:2b` is not added to the main experiment.
This is consistent with the amended C1's own scope — the main experiment is not a scale-gradient
study, it is one headroom model (1.5B) plus one null-effect control (3B) — so a third family would
have bought a capacity comparison the current framing does not call for, at a demonstrated stability
cost. The `gemma2:2b` weights are left on disk (1.7 GB, well within the 33 GB currently free) in case
a future session wants to extend the roster on hardware that can hold three models resident, or via
the RunPod/Vultr option discussed at the Gate.

**Consequence for run design.** The pilot's documented invariant — "all sessions for one model
complete before the next is loaded" — is upgraded from a wall-clock optimisation to a **correctness
requirement**: the main run must never request a model, then a second, then the first again, inside
one session. Both models being requested causes ollama to hold both resident (observed directly this
session), which is exactly the condition that produced the crash. The run script enforces this by
looping conditions inside a model, never models inside a condition (matching `src/run_pilot.py`'s
existing structure, which already does this correctly).

---

## 2. Budget-set design and the power calculation

### 2.1 Independent budget sets per replicate — the design change from the pilot

The pilot used **one fixed set of 25 budget lines**, reused identically across every model, condition
and seed, because its purpose was a same-condition test–retest reliability check (`n` re-runs of the
*identical* stimulus is what test–retest reliability means). The main experiment's purpose is
different: it needs **independent replicates** to power a between-condition comparison, and reusing
one fixed budget-set draw across all replicates would silently convert "25 independent framing
comparisons" into "25 repeated measurements of one comparison" — precisely the Andrews Lemma-1 tie
trap's sibling error, not on prices, but on replication itself.

**Design:** for each replicate `r` in `1..N` (per model, per condition), draw a **fresh, independent**
`T=25`, `K=2` budget-set with `src/budget_sets.py`'s existing generator (`M, N ~ U[0.1, 1.0]` i.i.d.,
rejected unless `max(M,N) ≥ 0.5`), seeded by a distinct, recorded seed
`20260826_000 + 1000*replicate_index` (disjoint from the pilot's single seed `20260826`, so no draw
is accidentally reused). Continuous-density prices and enforced budget exhaustion are unchanged from
the pilot — both are required by `docs/METHOD_NOTE_Q6.md` and are already implemented in
`budget_sets.py`.

**Bronars power is a property of the generating process, not of any one draw**, and the pilot already
validated it at 1.0000 (E4 replication ≈0.999) for this exact generator. It does not need
re-validating per replicate. What is verified per replicate, cheaply, before that replicate's model
call: `n_exact_ties == 0` on the drawn budget set (the Q6 guard), and the drawn set's own Bronars
power computed in the same call as a spot-check, logged but not gated on unless it falls outside
[0.98, 1.00] — in which case the draw is rejected and redrawn with the next seed offset, and the
rejection is logged.

### 2.2 Power calculation — explicit, not a round number

**The paper leads with GARP pass rate, not CCEI, per `docs/PILOT_RESULTS.md` §3's own stated rule**
("CCEI is a poor guide to how much violation is present... any future work here must report
violation counts alongside the index"). The power calculation below is therefore built primarily on
the pass-rate metric, with CCEI's own power requirement computed and reported honestly as a much
harder target — which is itself part of what the Gate below asks the operator to weigh.

**The only clean, unconfounded framing-effect size the pilot produced is at 3B**, per the amended
C1/C3: `baseline 0.76 → reciprocal 0.17` GARP pass rate, `p = 0.0010`, `n = 25` and `23`. The 1.5B
pass-rate shift (`0.27 → 0.42`) is explicitly unusable for this purpose — C3 exists precisely because
it is a survivorship artefact of the 52% discard, not a measured effect. The 3B magnitude is used
below as the **planning target** for the 1.5B confirmatory run: not a claim that 1.5B will show the
same effect (that is what the experiment measures), but the only evidence-based benchmark available,
stated as such.

**Two-proportion power (Fleiss, exact, not the normal approximation), α = 0.05 two-sided:**

| Assumed reciprocal-condition pass rate (baseline fixed at 0.76) | Δ | n per group, 80% power | n per group, 90% power |
|---|---|---|---|
| 0.17 (the pilot's actual 3B finding) | 0.59 | **10** | 13 |
| 0.30 (half the pilot's magnitude, conservative) | 0.46 | 18 | — |
| 0.40 | 0.36 | 29 | — |
| 0.50 | 0.26 | 53 | — |
| 0.60 (a fifth of the pilot's magnitude) | 0.16 | 133 | — |

**Design choice: `N = 30` independent replicates per condition.** This is not the bare 80%-power
floor (`n = 10`) — a design that fragile would be worth almost nothing if the true 1.5B effect turns
out to be smaller than 3B's, which is exactly the open question. `N = 30` gives power ≥ 0.999 at the
pilot's full magnitude, retains power ≥ 0.80 down to roughly 60% attenuation of that magnitude
(interpolating the table above, between the `n=18` and `n=29` rows), and is small enough that its
wall-clock cost (§4 below) is a non-issue locally. `N = 30` is used uniformly across every condition
at both models, for a symmetric, easily-described design.

**CCEI's own power requirement, computed honestly rather than assumed away.** Using **1.5B's own
measured within-condition noise** (baseline WSCV 14.8%, SD 0.1367 — this is the number that actually
governs power at the scale the experiment runs, not 3B's much tighter 0.0195) and the 3B CCEI delta
(0.0428) as the same planning-target convention used above:

| Planning SD | Assumed Δ | n per group, 80% power |
|---|---|---|
| 1.5B baseline SD (0.1367), conservative | 0.0428 | **161** |
| 1.5B pooled baseline+reciprocal SD (0.1133) | 0.0428 | 111 |
| 3B's own tight SD (0.0391) — **wrong SD to use here, shown for contrast only** | 0.0428 | 14 |

**At `N = 30`, the design is well-powered for the leading metric (GARP pass rate) and explicitly
underpowered for a CCEI effect of 3B's magnitude** — the minimum CCEI effect `N=30` could reliably
detect at 1.5B is roughly 0.11 (Cohen's d ≈ 0.79 against the baseline SD), about 2.5× the 3B magnitude.
This is not hidden: `docs/MAIN_EXPERIMENT_RESULTS.md` reports both the pass-rate result (adequately
powered) and the CCEI result (with its own confidence interval, explicitly flagged if the interval is
uninformatively wide) rather than treating the two metrics as equally trustworthy. Reaching CCEI power
matching the pass-rate design would need `N ≈ 111–161` — the exact tradeoff the Gate (§5) puts to the
operator.

---

## 3. Conditions

**Two conditions confirmed at minimum, per the pilot and E3:** `baseline` (direct per-token-return
framing) and `reciprocal` (E3's inverted-price framing, the pilot's strongest manipulation). Unchanged
wording from `src/run_pilot.py`'s `prompt()` function.

### 3.1 A third arm: single-turn vs. multi-turn format — added, and justified

**Decision: yes, add it, at the 1.5B model only.** `docs/PRECONDITION_CHECK.md` §(b) is direct
evidence that this is a real, large, independently-published mechanism distinct from reciprocal-price
framing: arXiv:2505.21371 reports multi-turn→single-turn CCEI drops of up to **−0.241** (Qwen2.5-7B,
risk domain, p<0.01) — an order of magnitude larger than the 3B reciprocal-framing CCEI delta
(−0.043) this project's own pilot found. Both `docs/GO_NOGO_ASSESSMENT.md` and `docs/FRAMING.md` §7
(preconditions) name format, not persona, as the headroom lever the literature actually supports.
Testing only reciprocal-price framing and never the literature's own strongest lever would leave an
obvious gap a reviewer who knows arXiv:2505.21371 would ask about immediately.

**What the manipulation is, precisely.** `baseline` and `reciprocal` are both **single-turn**: one
prompt containing all 25 rounds, one response containing all 25 lines (`src/run_pilot.py`'s existing
format). The new **`multiturn`** condition holds price framing at `baseline` wording and instead asks
for the 25 rounds as **25 separate sequential API calls**, each call's prompt containing the running
conversation history (all prior rounds and the model's own prior answers) plus the next round's
prices, requesting exactly one `A=<int> B=<int>` line summing to 100. This isolates the format
mechanism from the framing mechanism — exactly the design discipline `audit/BRONARS_NOTE.md` demands
("fix the design across conditions... only the thing being tested varies").

**Not added at 3B.** The 3B arm exists only as C1's null-effect control — to show the identification
strategy reports no repairable incoherence where none exists. Adding a third condition there tests a
different question (does 3B's format sensitivity also vanish?) that is interesting but not required by
the amended C1, and adding it would cost roughly 50% more 3B wall-clock for a question the current
framing does not need answered. It is named here as a cheap follow-up if the operator wants it later.

**Per-session cost for `multiturn` is assumed, not yet measured, and must be re-measured before the
run — flagged explicitly rather than silently inherited.** 25 round-trip calls each with a short
prompt and a ~5–10 token response plausibly costs less generation time than one 700-token single-turn
response, but adds per-call scheduling overhead absent from the single-turn format. §4 uses a
conservative planning estimate (1.3× the single-turn wall-clock) pending a small pretest (5 sessions)
at the start of Part Three, whose measured timing replaces this estimate before the full `N=30` run
starts.

---

## 4. The projection: minimal-perturbation MILP, per `docs/METHOD_NOTE_Q3.md`

Applied to every trace with `garp_holds(p, x) == False` under the independent Warshall check (traces
that already satisfy GARP get dose = 0 by definition — no MILP call needed). Implements the
**recommended formulation** from `docs/METHOD_NOTE_Q3.md` verbatim — the multiplier-free ordinal
characterisation (Demuynck & Rehbeck 2023), not the withdrawn alternating-ordering scheme:

- **Variables:** `x̃_t ∈ R²_+` (perturbed bundles, `K=2`), `u_t ∈ [0,1]` (ordinal levels, not Afriat
  utilities — no multipliers), `U_{t,v} ∈ {0,1}` for `t ≠ v` (comparison indicators). At `T=25`:
  600 binaries, 75 continuous.
- **Constraints (1)–(6)** exactly as specified in `METHOD_NOTE_Q3.md` §"Recommended formulation",
  re-derived from Demuynck & Rehbeck Theorem 2 before coding rather than copied on trust, per that
  note's own residual-risk item.
- **Budget exhaustion (5) imposed as equality**, `p_t·x̃_t = I_t = 100` for every session (income is
  fixed at 100 across this whole project) — this is both the standard design choice and what makes
  the big-`M` constant (`α > max_t I_t = 100`) computable a priori.
- **γ margin:** `γ = 10⁻⁴ · min_t I_t = 0.01` expenditure units, per the note's recommendation. Before
  trusting any reported dose, the sensitivity sweep the note requires is run: `γ ∈ {10⁻², 10⁻³,
  10⁻⁴, 10⁻⁵, 10⁻⁶}`, and the projection distance is reported alongside evidence it is stable across
  that range. If it is not stable, that is reported as a finding, not smoothed over.
- **Objective: `L1` primary** (`Σ_t Σ_k w_{t,k}·d_{t,k}`, uniform weights `w=1`), solved via
  `scipy.optimize.milp` on the HiGHS backend — the exact backend already measured in
  `docs/COMPUTE_NOTE.md` (sub-5-second solves at comparable binary counts). `L∞` is computed as a
  free-to-add robustness check (a single shared `d` variable) per the note's suggestion; `L2` is
  skipped — it needs an MIQP solver this project does not have configured, and the note explicitly
  permits reporting `L1` alone with `L2` as optional.
- **The dose** for a trace is its `L1` projection distance, `Σ_t Σ_k |x_{t,k} − x̃_{t,k}|`, comparable
  across sessions without further normalisation because income is fixed at 100 throughout.
- **Verification, mandatory on every returned `x̃`:** feed `(p, x̃)` back through `src/ccei.py`'s
  `garp_holds()` — the same independent Warshall closure used everywhere else in this project — and
  assert it passes. A solver optimality report is never trusted alone, per the note's explicit
  warning about badly-scaled big-`M` models.
- **Feasibility / warm start:** fit a Cobb–Douglas demand to the observed `(p_t, x_t, I_t)` by
  least-squares share-fitting, feed the resulting rationalisable sequence as an incumbent. This also
  gives a free sanity ceiling on the true minimum, per the note.

This step is CPU-only and was already shown trivial at this scale in `docs/COMPUTE_NOTE.md`; no
change to that conclusion is expected, but solve time and MIP gap are logged per trace regardless,
because the perturbation MILP's relaxation is weaker than the deletion MILPs `COMPUTE_NOTE.md`
actually timed, per the note's own caveat.

---

## 5. The exogenous payoff — designed to be genuinely exogenous, not a rationalising fit

**The requirement, restated from the amended C1:** the payoff must not be derived from the agent's own
preference data. A utility function *fit to* the agent's revealed choices (e.g., the best-fitting
Cobb–Douglas demand used above as a MILP warm start) would be circular if used as the payoff — it
would by construction reward the agent for being close to its own revealed preferences, which is a
restatement of coherence, not an independent yardstick.

**Design: a fixed, pre-registered, symmetric objective valuation, independent of any data this project
collects.** Define `U_exo(x) = x_A^0.5 · x_B^0.5` — Cobb–Douglas with **equal weights, chosen before
any model was queried and not fit to any agent's choices in this project** (0.5/0.5 is the
zero-degrees-of-freedom choice; it is not estimated from data, so there is nothing in it that could
leak information from the agent's revealed preferences). This mirrors the structure — not the
specifics — of `docs/GO_NOGO_ASSESSMENT.md`'s approving citation of R41 (KC Fed): scoring behaviour
against payoff-maximising performance in a domain with a computable optimum, not against another
preference judgment.

**The payoff score for a bundle `x_t` at budget `(p_t, I_t)`:**

```
payoff(x_t) = U_exo(x_t) / U_exo(x*_t)
```

where `x*_t` is the **closed-form Cobb–Douglas-optimal bundle at that exact budget line**
(`x*_{t,A} = 0.5·I_t/p_{t,A}`, `x*_{t,B} = 0.5·I_t/p_{t,B}` — standard Cobb–Douglas demand, computable
in closed form, no optimisation call needed). This is a normalised **efficiency ratio in (0, 1]**:
1.0 exactly when the agent's bundle happens to be the exogenously-optimal one, and it degrades
smoothly as the chosen bundle moves away from that fixed optimum — regardless of what the agent
itself was trying to do. **Payoff is computed identically for the raw sequence and the projected
(repaired) sequence**, at the same budget sets, so the dose–response curve is
`Δpayoff = mean(payoff(x̃)) − mean(payoff(x))` plotted against the projection dose from §4.

**Why this is not circular, stated plainly for the paper's method section.** Three properties jointly
establish exogeneity: (i) the exponents are fixed by the experimenter before data collection and never
re-estimated from any agent's choices — unlike the MILP's own Cobb–Douglas warm start, which *is*
fit per-session and is used only as a numerical device, never as the payoff; (ii) the optimal bundle
`x*_t` at each budget line is a closed-form function of `(p_t, I_t)` alone — it does not depend on
`x_t` or `x̃_t` at all, so nothing about the agent's actual choice enters the yardstick; (iii) the same
fixed function scores every model, condition and repair identically, so no condition-specific fitting
can inflate or deflate any comparison. A reviewer's natural next question — "why Cobb–Douglas and not
something else" — is answered by precedent: it is the standard closed-form demand system with a known
optimum, it requires no solver (avoiding a second dependency on the MILP's own optimisation
machinery), and — the point that matters for the design's economics-literature credibility — it is
structurally the same idea as a **money-metric utility index** (Varian's own device for welfare
comparison across the very GARP/Afriat objects this paper's method section already relies on).

**Cost:** trivial. Two closed-form evaluations per bundle, no solver call. This is the cheapest
component of the entire pipeline and adds no measurable wall-clock.

---

## 6. The 52% discard problem — decided per C3, not silently dropped

**Decision: both proposed mitigations, adopted together.**

**(a) Capped retry protocol.** For each `(model, condition, replicate_index)` slot: attempt
generation on the independently-drawn budget set with seed `s`. If the response fails the
`≥20/25` valid-rounds threshold (unchanged from `docs/PILOT_PROTOCOL.md` §6), retry on the **same
budget set** with a fresh seed offset (`s+1000`, then `s+2000`) — up to **3 total attempts**. All
attempts are logged in full (raw response, validity, wall time), not just the last one. A slot that
still fails after 3 attempts is recorded as a **residual discard** and excluded from CCEI/GARP
computation for that slot — but its existence, and every failed attempt's raw output, remain in
`results/main_raw.json` for audit. Three attempts is the cap because: it converts a ~52% first-attempt
failure rate into an expected ~14% residual failure rate under the (conservative, i.i.d.) approximation
`0.52³ ≈ 0.14`, at a bounded and budgeted cost (§7), without unboundedly retrying a session that is
genuinely unable to comply.

**(b) Discard rate reported as a first-class per-condition outcome, both pre- and post-retry.**
`docs/MAIN_EXPERIMENT_RESULTS.md` reports, for every `(model, condition)` cell: the first-attempt
discard rate (directly comparable to the pilot's own unretried 52%/12%/8%/0% figures), the residual
(post-retry) discard rate, and the count of slots that never recovered across all 3 attempts. This
operationalises C3's own requirement (`docs/FRAMING.md` §3): "the discard rate itself is reported as a
per-condition outcome... so that C3's finding is measured at the scale the main experiment actually
runs, rather than asserted from the pilot alone." The comparison between reciprocal-framing and
baseline discard rates at 1.5B, post-retry, is also C3's own stated kill condition — if the two
converge, that specific claim weakens and the write-up says so.

**What is explicitly not done:** silently dropping a slot after one failure (the pilot's own baseline
handling, now understood — via C3 — to bias the measured framing effect toward zero) and no cap at all
(unbounded retries would let a handful of pathological seeds consume arbitrary compute and would
itself bias the surviving sample in a new, unreported way).

---

## 7. Wall-clock estimate — from the pilot's actual measured per-session timing, not a guess

Computed from `results/pilot_raw.json`'s recorded `wall_s` per `(model, condition)` cell, the retry
protocol's expected-attempts-under-a-3-cap formula applied to the pilot's own first-attempt discard
rates, and the pilot's documented 296 s model-swap penalty (this session's own ad hoc re-measurement
of swap timing was contaminated by the 3-model stability test in §1 and produced numbers ranging
0.3–137 s plus a server crash — not used for planning; the pilot's single clean measurement is used
instead).

**Primary design (`N = 30` per condition, as specified in §2.2 and §3.1):**

| Cell | Expected attempts/slot | Wall-clock |
|---|---|---|
| qwen 1.5B baseline | 1.13 | 1086 s |
| qwen 1.5B reciprocal | 1.79 | 1918 s |
| qwen 1.5B multiturn (assumed 1.3× baseline mean, unmeasured) | 1.13 | 1411 s |
| llama 3B baseline | 1.00 | 1251 s |
| llama 3B reciprocal | 1.09 | 1239 s |
| 2 model loads | — | 592 s |
| **Total** | | **7496 s ≈ 124.9 min ≈ 2.08 hours** |

**Alternative design, powered to match a 3B-magnitude CCEI effect at 1.5B (`N = 150` at qwen
baseline + reciprocal, per §2.2's CCEI power table; all other cells unchanged):**

| Total | **19,509 s ≈ 325.1 min ≈ 5.42 hours** |
|---|---|

Both are within reach of a single local session's wall-clock. The decision the Gate (below) actually
turns on is not raw feasibility but **stability risk**: this exact machine's ollama server crashed
once already this session under sustained multi-model load (§1), and a 5.4-hour unattended run is a
materially longer exposure window than the 2.1-hour primary design.

---

## 8. Deliberate scope limits, stated rather than silently assumed

- **Two models, per §1.** A third family is feasible individually but not demonstrated stable across
  a multi-hour run on this machine; adding one is a documented follow-up, not silently dropped.
- **`multiturn` format arm only at 1.5B**, per §3.1 — not because 3B's format sensitivity is
  uninteresting, but because the amended C1 does not require it and it would add cost without
  answering the current claim.
- **CCEI at `N=30` is explicitly underpowered relative to a 3B-magnitude effect at 1.5B**, per §2.2 —
  reported honestly rather than treated as equivalent in reliability to the pass-rate result.
- **`L2` projection is not computed** — no MIQP solver is configured; `L1` and `L∞` are, per §4.
- **The exogenous payoff is one fixed valuation (equal-weight Cobb–Douglas)**, not a family of
  payoffs — a robustness sweep over alternative fixed weightings (e.g. 0.3/0.7) is a cheap follow-up,
  named here and not run, because the current claim needs one exogenous yardstick, not a sensitivity
  family, and adding one is unlikely to change the qualitative dose–response reading.
