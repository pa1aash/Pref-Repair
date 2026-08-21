# Synthesis plan

## Core thesis

Repair of AI-agent choice coherence is common, not absent — at least a dozen implemented systems
enforce a coherence axiom on model outputs, across both timings and six axiom families — but **not one
of them estimates the effect of that repair in an identified way**: every reported sign either comes from
an operator projecting onto the set its own metric defines, or from a comparison in which the
cycle-tolerant arm is a strictly richer model class, or from an outcome that is itself a preference
judgment. The field therefore has many data points and no clean estimate, and the one configuration that
would produce one — minimally perturbing an agent's *own* choice sequence onto the rationalizable set and
scoring it against an exogenous payoff — is exactly the configuration nobody has built.

## The strongest argumentative beats

1. **The census is the answer to half one, and the taxonomy is the finding, not the count.** (Draft A.)
   The interesting fact is not how many systems intervene but *what they intervene on*: every one acts on
   a preference proxy — a judge's rankings, an annotator pool, a reward head, a training corpus — and none
   on an agent's own realised choice sequence over budget sets.
2. **Target alignment predicts the sign.** (Draft C, and this is the report's own contribution.) Every
   repair that helped projects onto the set its metric defines; both that failed do not. This is
   falsifiable and predictive, which no existing paper states.
3. **The apparent ML consensus that enforcement degrades quality is an artefact.** (Draft B's own source
   list, read correctly.) The cycle-tolerant arm is a strict superset model class in both peer-reviewed
   ablations; on length-controlled win rate the sign reverses in 18 of 24 cells; the better-controlled
   replication finds a wash. The sign is unidentified, not known.
4. **Three published failures across three axiom systems establish a real adverse prior.** (Draft B.)
   This must not be softened by beat 2 — target alignment explains the failures, it does not erase them.
5. **The reliability objection is scale-dependent.** Human indices are unreliable at the individual level;
   flagship-model efficiency scores are format-stable while small-model scores are not. Both halves stated.
6. **The two literatures do not cite each other, and the cost is rediscovery.** Economics has had the
   repair machinery since the 1980s; the ML systems reinvent convex special cases of it without the
   vocabulary. This is the answer to the query's "two related but distinct fronts" clause.
7. **The projection problem is well-posed but its complexity is open.** The GARP-consistent set is not
   closed, so the natural objective can read exactly zero on violating data; a fixed strict-preference
   margin fixes that. Minimum-cost deletion is NP-hard, deletion is polynomial at two goods, and the
   continuous quantity-perturbation objective is genuinely unclassified.

## Section structure

The nine `required_section_headings` from `research/prompt-decomposition.json`, verbatim and in order,
then `## Sources`.

## Per-section commitments

### 1. What Counts as an Intervention, and What Counts as Mere Measurement
- Evidence: Draft A §1 (the cleanest statement of the distinction), Draft B §1.
- Beat: establish the inclusion criteria the census will use, *before* counting, so the count is auditable.
- Engage: nothing yet — this is definitional groundwork.

### 2. The Economics Front: Afriat, Varian, Houtman-Maks and What They Offer as Repair
- Evidence: Draft A §2 (strongest), Draft C. The classical machinery — efficiency indices, deletion
  indices, money-pump, least-squares/minimum-cost repair.
- Beat: economics has had *constructive* repair operators for decades; they are goodness-of-fit measures
  whose constructive duals nobody in ML has picked up.
- Engage: Tension "Tractability of minimum-cost repair" — hardness is dimension-dependent, not uniform.

### 3. The Economics Front Applied to AI Agents: Who Has Intervened
- Evidence: Draft A §3, plus the central-bank working paper and the GARP fine-tuning work.
- Beat: only one system targets GARP and it does so *generatively* — rejection sampling before training,
  not projection of observed choices.

### 4. The ML/Alignment Front: Coherence Theorems, Bradley-Terry Violations, and Nash Learning
- Evidence: Draft B §4 and Draft C §4. Keep this front *separate* from §2 — an explicit query requirement.
- Beat: the coherence-implies-competence question is philosophically settled in the negative and
  empirically untested in identified form. Those are different failures.

### 5. The ML/Alignment Front Applied to Agent Choice: Enforce or Accept?
- Evidence: Draft B §5, Draft C §5.
- Beat: the enforce/accept literature rejects total orders on *existence* grounds, not on harm grounds.
- Engage: Tension "Cycles as defect versus cycles as structure" — commit to: cycle source is an empirical
  question, and scalarisation demonstrably creates cycles.

### 6. Census of Interventions Found, Inference-Time and Training-Time
- Evidence: Draft A §6 (its strongest section), cross-checked against Draft C.
- **Must be a table.** Columns: system / front / timing / axiom system / minimal? / downstream metric /
  is that metric exogenous? / sign.
- Beat: the empty column is "acts on the agent's own choice sequence" and the near-empty one is
  "exogenous outcome".

### 7. Does Enforced Coherence Change Downstream Decision Quality? The Empirical Record
- Evidence: all three drafts; this is the contested section.
- Beat: beats 2, 3 and 4 together. State the positives, state the three failures, then resolve with target
  alignment — and concede that the adverse prior survives the resolution.
- Engage: Tensions "Repair helps versus repair backfires" and "Whether the ML evidence is identified".

### 8. Where the Two Literatures Miss Each Other
- Evidence: Draft C, Draft A §2 vs §4.
- Beat: convex special cases being rediscovered without the economics vocabulary; and the indexing failure
  that hides economics working papers from ML sweeps and vice versa.

### 9. Verdict: What Is Occupied and What Remains Open
- Beat: the core thesis, stated at full strength, with the unoccupied conjunction named precisely and the
  residual search risk (full-text venues unsearchable headlessly) stated as a limitation, not hidden.

## Where drafts disagreed

Four conflicts, all adjudicated in `research/temp/synthesis-conflicts.md`. Summary of commitments:
- **Census count** — commit to a taxonomy with explicit inclusion criteria, not to any of the three bare
  numbers. The load-bearing clause is that only one system targets GARP and it does so generatively.
- **Sign of the effect** — commit to Draft C's target-alignment reconciliation, and say plainly that it is
  the report's own claim rather than a citation. Do NOT average A and B.
- **Reliability transfer** — commit to scale-dependence; state both halves; note the flagship result is a
  single unreplicated study.
- **Citation defects** — inherit neither. Emit `[N]` plus one deduplicated `## Sources`; no `{{...}}`.

## Input notes for the synthesizer

All three drafts are complete: nine sections each, 10,900–11,400 words apiece. Draft A is the census
specialist — mine it hardest for §§1–3 and §6. Draft B is the adversarial case — mine it for §7's failure
evidence and for the corrected figures on the two ICML ablations. Draft C is the reconciler — its
target-alignment argument is the single most valuable idea in the three and should carry §7's resolution.

**Draft A has no `## Sources` section** (it emits `[N]` markers without a list). Build the Sources list
fresh from the notes actually cited in the synthesised text; do not attempt to merge the three drafts'
numbering schemes, which are mutually inconsistent.

## Length target

- response_format: `argumentative` (5,000–10,000 words)
- Pass 1 target: ~9,000 words
- Pass 2 final target: **~7,500 words**. Pass 2 must CUT. The three inputs total ~26,000 words, so the
  dominant failure mode here is stapling rather than synthesising.
