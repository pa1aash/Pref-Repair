# Compute scope

## The projection step needs no rented compute

The planning brief says the projection is CPU-trivial. That is confirmed, and measured rather
than assumed. On this machine (Apple silicon, Python 3.13.12, SciPy 1.18.0, HiGHS backend —
no extra install, no accelerator), a full Afriat-inequality feasibility LP with a fixed
preference ordering and a Houtman–Maks-style MILP with binary keep/drop indicators both solve
at the brief's stated scale in well under ten seconds:

| n (observations) | constraint rows | LP (fixed ordering) | MILP (binary drop set) |
|---|---|---|---|
| 25 | 600 | 0.12 s | 1.26 s |
| 40 | 1,560 | 0.05 s | 2.97 s |
| 50 | 2,450 | 0.08 s | 4.02 s |
| 60 | 3,540 | 0.78 s | 3.26 s |

Constraint count grows as `n(n−1)` and both solvers stay comfortable across the brief's whole
n ≤ 60 envelope. **No RunPod or Vultr spend is needed for the projection itself, and none
should be budgeted for it.** The real scaling risk is not the solver but the *search over
preference orderings* that wraps it — that is combinatorial in n, and it is why the brief caps
n at 60. If a future session needs larger n, the answer is a smarter formulation (a single
MILP over the binary revealed-preference relation rather than an outer loop over orderings),
not a bigger machine. One caveat on the LP above: it is linear only because the ordering is
fixed and the Afriat multipliers enter as their own variables. With both utility levels and
multipliers free and no fixed ordering, the system is bilinear, not linear — see
`docs/OPEN_QUESTIONS.md` Q3 before anyone writes the solver.

## What self-hosting would buy, and roughly what it would cost

The spend that actually matters is model inference, and the question is not raw price — the
brief's $20–150 API estimate is plausible for a few thousand short completions either way —
but whether the ≥5-seeds-per-condition requirement is *satisfiable* on a commercial API. It
largely is not, for three reasons that compound. First, temperature-0 decoding on a hosted
frontier model is not deterministic: batching, mixture-of-experts routing, and
floating-point accumulation order vary run to run, so a "seed" is best-effort and the
per-seed distribution the brief wants to report is partly provider noise of unknown
magnitude. Second, hosted model snapshots move and retire, so a CCEI number measured in
week 1 may not be reproducible by a reviewer in week 4, let alone by a reader next year —
for a paper whose entire contribution is a measured before/after difference, that is a
reproducibility hole in the headline result. Third, several plausible mechanisms in this
space need token-level logprobs (the neighbouring HAR 2025 rationality layer reads token
probabilities as majority-graph edge weights), and logprob access is restricted or absent on
several frontier endpoints. Self-hosting an open-weight model fixes all three: weights are
pinned to a hash, `seed` genuinely reproduces a sample, and logits are yours.

Rough cost, to be verified before commitment rather than trusted here — GPU list prices on
the usual rental providers run roughly $0.40–0.70/hr for a 24 GB consumer card, ~$1.50–2.50/hr
for an 80 GB A100, and ~$2.50–4.00/hr for an H100; a 70B-class model at 8-bit needs two 80 GB
cards. The elicitation workload is small (order 10³–10⁴ short completions across conditions ×
seeds × models), so wall-clock is dominated by setup and idle time, not by generation: budget
one or two working days of a two-A100 pod, i.e. roughly **$60–150**, plus the same again in
wasted idle if the pod is left up. That is the same order as the brief's API estimate, so the
choice is not a cost decision — it is a validity decision, and the cost is a rounding error
either way. **Recommendation, not a decision:** run the frontier-API models the brief requires
for external validity and breadth (≥3 models, ≥2 families — that requirement genuinely needs
commercial endpoints), and additionally self-host one open-weight model as the *reproducibility
anchor* on which the ≥5-seeds analysis, the per-seed distributions, and any logprob-dependent
mechanism are actually run. Existing RunPod access covers this; no new provider is needed. The
call on whether the anchor model is worth the extra setup day belongs to the experiment-design
session, not to G0.
