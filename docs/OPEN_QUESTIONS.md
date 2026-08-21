# Open questions

Ordered by how much is riding on the answer. Each entry names who can answer it and what it would
cost to find out.

**Status as of session G0.5 (2026-08-21):** Q3, Q6, Q7, Q8, Q9, Q12 are **CLOSED**. Q1 is
**RE-SCOPED** — it is no longer "is the cell worth a paper" but "does the pilot secure the two
numbers", see `docs/GO_NOGO_ASSESSMENT.md`. Q2, Q4, Q5, Q10, Q11 remain open. Closed entries are
kept in place with their resolution appended rather than deleted, so the reasoning stays auditable.

---

## Blocking — these decide whether and in what form the paper exists

### Q1. Given that the repair operator is occupied, is the remaining cell worth a paper?

Phase E established that inference-time repair of LLM choice consistency is published at least
three times over, and that the coherence-vs-competence question has been tested in both
directions (`audit/killcheck_E5.md`, `audit/INSTRUMENT_CALIBRATION.md` §4). What is left
unoccupied is narrow and specific:

> Projecting an **agent's own choice sequence** onto the rationalizable set, scoring it against an
> **exogenous payoff that is not derived from the preference data**, and tracing a **dose–response
> curve** rather than a single on/off comparison.

Nobody has done that. It is a real contribution. It is also a considerably smaller claim than
"nobody repairs", and it arrives eight days before the deadline.

**Who answers it:** the principal investigator. This is a judgement about ambition and risk
appetite, not a fact an audit can establish.
**Cost to answer:** nil — but it gates everything downstream.

> **RE-SCOPED, G0.5.** The cell survives — no paper holds two of its four conjuncts jointly — but
> three of the four are now individually spoken for: minimality as vocabulary (R27, Aug 2026), the
> exogenous-payoff claim false as stated (R20, R41), and a published nine-level dose–response curve
> (R25 App. C.4). Full reasoning and both cases at full strength in `docs/GO_NOGO_ASSESSMENT.md`.
> **Verdict: QUALIFIED YES.** The question is no longer "is this worth a paper" but "does the pilot
> secure (a) stable per-model CCEI across re-runs and (b) framing-induced headroom on a current
> frontier model". Those two numbers decide it, they cost an afternoon, and they must come before
> any drafting. The residual judgement genuinely left to the PI: whether a contribution framed as
> *object + graded measure + exogenous outcome + rigour* — explicitly not as priority — is worth
> submitting.

### Q2. Does the S4 gate survive being restated around framing rather than persona?

The brief's gate is: measure CCEI under **persona** conditioning; if CCEI > 0.99, stop. Phase E
found that lever is the wrong one.

- The persona evidence (`arXiv:2501.18190`) cannot carry the gate: one retired 2024 single-family
  model, no CIs or replications, and a headline CCEI of 0.127 that sits below its own design's
  arithmetic floor of 0.25 (`audit/killcheck_E2.md`).
- The **framing** evidence is far stronger and comes from the very paper cited to fear no
  headroom: holding budget sets fixed and changing only how prices are *worded*, CCEI falls to
  0.698–0.908, with 32–88% of runs under 0.9 (`audit/killcheck_E3.md`).

**Who answers it:** the week-1 pilot, once restated to vary framing and response format alongside
persona.
**Cost to answer:** an afternoon and a few dollars of API calls — unchanged from the brief's own
estimate. Only the manipulation changes.

### Q3. Are the Afriat inequalities actually linear under the intended parameterisation?

Claim S8 asserts that "given a fixed preference ordering, feasibility is a system of Afriat
inequalities — a linear program". That is true **only** when the ordering is fixed and the Afriat
multipliers enter as their own free variables. With utility levels and multipliers both free and
no fixed ordering, the system is **bilinear**, not linear, and the outer search over orderings is
what restores linearity — at combinatorial cost.

The measured timings in `docs/COMPUTE_NOTE.md` used the fixed-ordering formulation, so they
confirm the LP is cheap **conditional on** the ordering. They say nothing about the cost of the
search over orderings, which is the actual scaling risk and the reason the brief caps n at 60.

**Who answers it:** whoever writes the solver, before writing it.
**Cost to answer:** a few hours of formulation work. Getting this wrong means discovering
mid-implementation that the "LP" is a MINLP.

> **CLOSED, G0.5.** See `docs/METHOD_NOTE_Q3.md`. Three findings:
> 1. **The alternating scheme does not work as described.** Fixing the ordering does *not*
>    linearise the projection — `λ_j·p_j·x̃_i` stays a product of two unknowns whatever the ordering
>    is. Read charitably as alternating convex search, the ceiling is stationarity only (Gorski et
>    al. 2007): a partial optimum need not be a local optimum, and with a discrete ordering block
>    cycling is possible without an anti-cycling rule.
> 2. **A clean solved form exists and the bilinearity is avoidable entirely.** Demuynck & Rehbeck
>    (2023) drop the Afriat multipliers for a multiplier-free ordinal characterisation whose
>    constraints are linear jointly in utility numbers, prices **and quantities**. The projection is
>    a **single MILP** — no multipliers, no bilinear terms, no outer ordering search.
> 3. **The real hazard is well-posedness, not complexity.** The GARP-consistent set is **not closed**
>    (Chen–Lanier–Quah Prop. 1), so the index can read exactly 0 on violating data and the minimum
>    may be unattained. Fix: a fixed strict-preference margin γ, reported, with the distance shown
>    insensitive across decades, plus an independent Warshall post-check on every returned x̃.
>
> Complexity: CCEI polynomial; Houtman–Maks **polynomial at K=2, NP-complete at K≥3** (Boodaghians
> & Vetta); the Dean–Martin minimum cost index **NP-hard** (Shiozawa 2015, via maximum acyclic
> subgraph — found on RePEc in Item 3). The **minimum-*perturbation* problem's complexity is open**
> and is stated as open rather than asserted. **S8 must be rewritten** — it is understated for
> measurement and wrong for construction. **S9's bound survives but its stated reason does not**,
> and it needs a K attached.

---

## Material — these change the work but not whether it happens

### Q4. What is K?

The brief specifies n = 25–50 observations and never specifies the **number of goods**. Kill-check
E4 shows K is the binding constraint on test power, not n: power falls exponentially in K and n
cannot buy it back. At K=2 the design has power ≈0.999; the brief's own proposed
"portfolio/resource-allocation" and "multi-step agentic" conditions would sit at K=8 (power ≈0.84)
or K=12 (power ≈0.44) at n=25 (`audit/BRONARS_NOTE.md`).
**Cost to answer:** a Monte Carlo that runs before any API call and costs nothing.

### Q5. Is the S4 gate's 0.99 threshold meaningful at all?

E4 surfaced that **31% of uniform-random agents clear CCEI 0.99** on the Andreoni–Miller design
(Andreoni, Gillen & Harbaugh 2013). If that carries over, "CCEI > 0.99 → project is dead" may be a
threshold a random agent passes a third of the time — in which case the gate is not measuring what
it is supposed to measure. The right diagnostic is the **simulated CCEI distribution** under the
actual design, not a fixed cutoff.
**Cost to answer:** same Monte Carlo as Q4.

### Q6. Does Andrews' Lemma 1 break the day-1 `ccei.py`?

E1 reports a lemma showing CCEI can read exactly 1.0 while GARP still fails, whenever a comparison
lands on exact budget equality — which round-number prices make *likely* rather than
measure-zero. The brief's day-1 script could therefore trip the STOP condition on a false
1.0. Andrews' fix is continuous-density price draws plus budget exhaustion.
**Cost to answer:** read the lemma; adopt the fix. An hour.

> **CLOSED, G0.5.** See `docs/METHOD_NOTE_Q6.md`. **The false CCEI 1.0 was reproduced numerically**,
> on the first constructed case. Minimal failing dataset: `p₁=(1,1), x₁=(5,5)`; `p₂=(2,1), x₂=(8,2)`
> — `p₁·x₂ = 10 = w₁` exactly. GARP is violated, e-GARP holds for every `e < 1`, and the brief's
> stated "binary search over e ∈ (0,1]" returns **0.999999999998**: the gate fires and the project
> is killed by a bug. The mechanism is sharper than the prior summary: the CCEI supremum is **never
> attained** when GARP fails, so the feasible set is the half-open `[0, CCEI)` and bisection only
> ever tests strictly interior midpoints — the one point where the violation lives is the one point
> it never tests.
>
> Prevalence: **100%** of T=25 integer-price designs contain at least one exact tie; **18.9%** of
> T=8 uniform-random agents on integer prices report an exact CCEI of 1.0 while violating GARP;
> **0.0%** across 63,200 continuous-price replications carrying 12,102 real GARP failures.
> **The inherited design (arXiv:2305.12763) violates Lemma 1's hypothesis in every condition** — its
> own footnotes specify two-decimal prices, a 91-point discrete grid. Any replication of it is
> unprotected. Andrews' fix is a *design* fix; an implementation guard is still required, and four
> concrete test fixtures with expected outputs are specified in the note.

### Q7. What do the three unread occupants actually do?

R20 (`arXiv:2406.00231`, LLM-RankFusion), R21 (`arXiv:2509.21117`, TrustJudge) and R22
(`arXiv:2604.17502`, the completeness-violation agents) are the works that refuted C3 and damaged
C2, and **none has been read in full** — all three are known from kill-check E5's summaries. Before
the paper concedes anything to them, someone should confirm the concession is warranted. It is
also possible they are further from the proposal than the summaries suggest, which would partially
restore C3.
**Cost to answer:** half a day.

> **CLOSED, G0.5.** Six occupants read in full across `audit/ITEM2_occupants_{A,B,C}.md`. The cell
> **survives but is narrowed**, and two prior characterisations were wrong:
> - **R20 (LLM-RankFusion)** repairs pairwise *judgments about third-party passages*, not choices.
>   Its transitivity component adds **+0.01 NDCG** for one model and **−1.12** for another; the
>   +6.13 headline is a positional-debiasing effect. It also **explicitly rejects Kemeny** (the
>   minimum-distance rule) as NP-hard — a citable published statement that minimal perturbation was
>   available and not taken.
> - **R27 (POISE)** genuinely **closes minimality as vocabulary** — a real L2 projection onto a
>   convex chain-monotone cone, with a Pythagorean theorem. But it takes the ordering as *input* and
>   cannot handle cycles; its "robot" payoff is a 3-annotator vote on 68 *generated videos*.
> - **R24/R25 (the ICML ablations) are NOT isolated treatments.** The cycle-tolerant arm is a strict
>   superset model class — both papers state BT is their dimension-1 special case — plus a scale gate
>   worth more than the headline margin. On *length-controlled* win rate the cycle-tolerant arm
>   **loses 18 of 24 cells**. The properly controlled replication (R25) finds a **wash**.
>   **`audit/killcheck_E5.md` Verdict point 1 must be withdrawn.**
> - **R31 (Nitsch, *PNAS*) and R38 (Yamin)** are the two published negatives, and both are stronger
>   than recorded: a choice-revision repair — the human analogue of this project's intervention —
>   made CCEI *worse*, and no ICC among ~40 estimates reaches 0.75.

### Q8. Is "minimal perturbation index" already an owned term?

E1 flags that Echenique, Imai & Saito (2023, *JEEA*) may already own this phrase. If so, the
brief's headline vocabulary collides with an existing index and compounds the "you reinvented
CCEI" attack the brief already anticipates.
**Cost to answer:** one paper fetch. Currently `unverified` (R15).

> **CLOSED, G0.5** (resolved en route by Item 1). Echenique, Imai & Saito perturb **beliefs,
> utilities and prices — never bundles**, and the phrase "minimal perturbation" appears **zero
> times** in the arXiv version. **The phrase is free; the idea is not.** The recommended name is
> the one the literature already uses for exactly this object: the **non-linear Least Squares
> index** (Chen, Lanier & Quah; traced to Varian 1985). Note a *second*, live collision that did
> not exist when Q8 was written: R27 (Aug 2026) owns "isotonic projection onto a preference-defined
> monotone cone".

---

## Housekeeping — cheap, but genuinely unresolved

### Q9. Should the leaked strings be purged from git history?

Two strings I introduced during this session — a machine-absolute home path in `docs/DECISIONS.md`
and a vendor filename in the hygiene guard's own header comment — were committed and pushed before
being fixed. The **working tree is clean**; only history retains them. `scripts/hygiene_guard.sh`
therefore exits non-zero on its history scan.

Purging them requires rewriting history and force-pushing a repository that is already public.
Two attempts to do so were **blocked by the permission layer**, correctly — this is a destructive,
outward-facing operation and is the user's call. See the end-of-session report.
**Cost to answer:** one decision, then about five minutes.

> **CLOSED, G0.5.** Resolved by a documented hash-based baseline rather than a history rewrite; no
> force-push was performed or needed. Full reasoning — including why a force-push does *not*
> reliably purge a public forge, which cuts against the rewrite — in `docs/DECISIONS.md` D13. The
> guard now exits 0, reports the count of accepted matches on every run, and was positive-control
> tested to confirm it still fails on new content leaks and on un-baselined history hits.

### Q10. Should the repository be public?

It is (unauthenticated HTTP 200). `docs/F3-PLAN-ORIGINAL.md` — including the prior-art verdict, the
venue strategy, and the assessment of a named third party's work as a scoop risk — is world-readable,
under a double-blind submission eight days out. Nothing in it breaks anonymity by itself, but a
public repository named for the method, containing the plan, is a deanonymisation vector worth a
moment's thought.
**Cost to answer:** one decision.

### Q11. Three classical references remain unread.

Varian (1990), Houtman & Maks (1985), and Echenique–Lee–Shum are `unverified` in
`audit/REFERENCE_LEDGER.md`. Two are paywalled with no OA copy found. Bronars (1987) is
`unresolved` outright — every access route closed, so every statement about Bronars in this
repository is sourced to **secondary** literature and labelled as such. None of these may be cited
as though read.
**Cost to answer:** library access, or accept the secondary sourcing and say so in the paper.

### Q12. RePEc was never searched.

EconPapers and IDEAS are JS-rendered and returned either an empty shell or HTTP 503 to every
headless request; this session was headless by instruction. RePEc is the main index for exactly
the economics working-paper literature where a revealed-preference repair method would most
plausibly appear outside arXiv. **This gap is not closed by anything else in this session**, and
it is the most likely place for a fourth occupant to be hiding.
**Cost to answer:** one interactive browser session, or a RePEc bulk-data download.

> **CLOSED, G0.5 — and the premise of this question was wrong.** See `audit/ITEM3_repec.md`.
> RePEc is **fully searchable headlessly**; nothing is JS-rendered. EconPapers needs a `Referer`
> header and the hidden `adv=true` field; IDEAS moved search to `/cgi-bin/htsearch2` over POST. The
> original GAP verdict came from stripping tags and grepping for the word *"result"* — a method that
> could never have succeeded, because a successful search says *"documents matched"* and a genuine
> zero says *"No matching documents"*. (The bulk-data half of this entry's cost estimate is also
> wrong: OAI-PMH, rsync and both FTP archives are dead, so the front-ends are the *only* route.)
>
> **77 queries run.** No new occupant of the target cell — nothing projects an AI agent's choice
> sequence onto the rationalizable set — with seven decisive queries verified as zeros against a
> nonsense-query control. But **six ledger-absent items surfaced**, the most consequential being
> **R41, Cook, Kazinnik, Modig & Palmer, "What Do LLMs Want?" (KC Fed RWP 25-19 / FEDS 2026-006,
> not on arXiv)** — which steers LLM economic choices with **learned control vectors** toward
> **payoff-maximizing behaviour**, i.e. two of the narrow cell's three legs, and independently
> corroborates Q2's framing-over-persona claim. Also **Shiozawa (2015)**, proving the minimum cost
> index NP-hard, which bears on Q3.
>
> **Residual gaps, stated as gaps:** top-k truncation on seven broad queries; RePEc indexes
> **metadata, not full text**, so a paper doing the projection in §4 without saying so in its
> abstract stays invisible — the same structural blind spot that hid Chadwick et al.; and
> SSRN/EconStor were not separately swept.
