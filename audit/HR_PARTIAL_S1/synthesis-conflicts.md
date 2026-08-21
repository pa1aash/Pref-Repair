# Synthesis conflicts — resolved before spawning the synthesizer

## Conflict 1: how many intervening systems are there?

- **Draft A says:** "at least a dozen published or preprinted systems", and later, counting economics-front
  operators not yet pointed at an AI agent, "seventeen distinct constructions" across "six axiom systems".
- **Draft B says:** "at least six published or preprinted systems", plus "a seventh, purely theoretical".
- **Draft C says:** "at least ten published or preprinted systems ... four at inference time and six at
  training time", and elsewhere "ten implemented systems and two formal proposals".

**Source check.** The disagreement is not factual — all three are reading the same corpus. It is a
*counting-rule* disagreement. The three rules in play are: (i) systems that intervene on an **AI agent's**
outputs, implemented and run; (ii) plus purely theoretical proposals; (iii) plus economics-front repair
operators that exist but have never been applied to an AI agent.

**Verdict: none of the three bare numbers may be used. The report states the taxonomy with explicit
inclusion criteria instead.** The defensible statement, checked against `audit/REFERENCE_LEDGER.md` and the
three occupant deep-reads:

- **Implemented and run on an AI system's outputs, inference-time:** the HAR 2025 rationality layer
  (QP projection onto the coherent simplex + iterative max-di-cut approximating a Kemeny ranking);
  TrustJudge (likelihood-aware aggregation); LLM-RankFusion (order + transitive repair); the ICML 2025
  non-transitivity paper (round-robin + Bradley-Terry aggregation); the axiomatic-constraint latent model
  (trained offline, applied at inference); representation-engineering steering of risk preferences; and the
  central-bank control-vector intervention. CONSISTRE spans both timings.
- **Implemented and run, training-time:** POISE (isotonic projection onto a chain-monotone cone);
  GARP-EFM (fine-tuning on rejection-sampled GARP-consistent synthetic panels); the innate-preferences
  fine-tune (reflexivity / IIA / cycle-additivity loss terms); supervised fine-tuning to explicit economic
  preferences; the self-consistency-loss belief-drift fix.
- **Proposed but never run:** the `1 − CCEI` training penalty; the majority-vote/Copeland reward
  modification.

**Rule for the report:** say "at least a dozen implemented systems plus two unrun proposals", give the
inference/training split, and — critically — note that **only one of them targets GARP, and it does so
generatively (rejection sampling before training) rather than by projecting an observed choice sequence.**
The precise number matters far less than that last clause, which is the actual finding.

## Conflict 2: is the published sign of the coherence-quality effect positive or negative?

- **Draft A says:** where repair has been applied to the set its own metric defines, it improved or
  preserved quality — five systems report gains.
- **Draft B says:** three independent attempts across three axiom systems moved the graded outcome the
  wrong way, establishing an adverse prior.

**Source check.** Both are correct about their own evidence, and the two sets are disjoint. The gains are
reported by operators projecting onto the set their metric defines (transitivity repair scored on
transitivity; isotonic projection scored on reversal conflicts). The failures are: a choice-revision arm
that showed participants a *random* subset of choices with no consistency objective and no guarantee of
improvement; an isotonic calibration projecting onto the *calibration* cone while being scored on
*conditional independence*; and an axiom-constrained latent model whose coherence improved while held-out
squared error rose.

**Verdict: commit to Draft C's reconciliation — target alignment between the operator and the metric it is
graded on is the discriminating variable.** This is not splitting the difference; it is a substantive,
falsifiable claim that predicts the sign, and neither A's nor B's position states it. The report argues
this explicitly and names it as the report's own contribution rather than as a citation.

## Conflict 3: does the reliability critique transfer from humans to models?

- **Draft B's** ammunition is human: no ICC among ~40 estimates reaches 0.75, and intermethod reliability
  under presentation change (0.071–0.408) is worse than five-month test–retest.
- **Draft C's** boundary condition 4 says format changes move the index a long way in *small* models
  (0.980→0.739; 0.953→0.841, both p<0.01) but leave flagship models essentially unmoved, and that persona
  and temperature move none of them.

**Verdict: both, and the split is the finding.** The report must not present the human ICC result as
though it settles the model case, and must not present the flagship-model stability as though it retires
the reliability worry. The committed reading: **the reliability objection is scale-dependent**, it is
live for small models, and the flagship-model evidence is a single study that has not been replicated.

## Conflict 4: draft-level citation defects (mechanical, not factual)

Draft A carries inline `[N]` markers but **no `## Sources` section**. Drafts B and C are clean (inline
markers plus a correctly numbered Sources list each; Draft C resolved its intermediate placeholders before
finishing). The three numbering schemes are mutually inconsistent and cannot be merged.

**Verdict:** the synthesizer writes fresh and must emit `[N]` markers with a single deduplicated
`## Sources` section built from the cited notes' frontmatter. It must not inherit either defect, and must
not carry any `{{...}}` marker into the final report.
