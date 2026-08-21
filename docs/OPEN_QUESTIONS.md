# Open questions

Everything this session could not settle. Ordered by how much is riding on the answer.
Each entry names who can answer it and what it would cost to find out.

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

### Q7. What do the three unread occupants actually do?

R20 (`arXiv:2406.00231`, LLM-RankFusion), R21 (`arXiv:2509.21117`, TrustJudge) and R22
(`arXiv:2604.17502`, the completeness-violation agents) are the works that refuted C3 and damaged
C2, and **none has been read in full** — all three are known from kill-check E5's summaries. Before
the paper concedes anything to them, someone should confirm the concession is warranted. It is
also possible they are further from the proposal than the summaries suggest, which would partially
restore C3.
**Cost to answer:** half a day.

### Q8. Is "minimal perturbation index" already an owned term?

E1 flags that Echenique, Imai & Saito (2023, *JEEA*) may already own this phrase. If so, the
brief's headline vocabulary collides with an existing index and compounds the "you reinvented
CCEI" attack the brief already anticipates.
**Cost to answer:** one paper fetch. Currently `unverified` (R15).

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
