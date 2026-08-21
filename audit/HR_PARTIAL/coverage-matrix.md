## Coverage Matrix — query phrase → atomic item mapping

| Query phrase (verbatim) | Mapped atomic item(s) | Scope check | Gap? |
|---|---|---|---|
| "published or preprinted work" | scope: both peer-reviewed and preprint in scope | OK — preprints explicitly included, and non-arXiv venues too (HAR 2025 precedent) | No |
| "inference-time … intervention" | Entity: inference-time interventions; Sub-Q5 | OK | No |
| "training-time intervention" | Entity: training-time interventions; Sub-Q5 | OK — both are in scope, not just inference-time | No |
| "CORRECTS" | Sub-Q1 | OK — kept as its own verb, not merged | No |
| "PROJECTS" | Sub-Q2 | OK | No |
| "REPAIRS" | Sub-Q3 | OK | No |
| "ENFORCES" | Sub-Q4 | OK | No |
| "revealed-preference consistency" | Entities GARP/WARP/SARP; Sub-Q7 | OK — treated as the family, not only GARP. Includes transitivity and probabilistic coherence as neighbouring axiom systems so near-misses are not silently excluded | No |
| "GARP/WARP/SARP compliance" | Entities: GARP, WARP, SARP | OK — all three named separately | No |
| "minimal-perturbation restoration of rationalizability" | Entity + Sub-Q8 | OK | No |
| "choices or outputs" | scope: both choice sequences and raw model outputs | OK — "outputs" is broader than "choices" and is preserved; token-probability-level interventions therefore qualify | No |
| "LLM-based or AI agent" | Entities: LLM-based agents; AI agents (non-LLM) | OK — "or AI agent" is broader than LLM and is kept as its own entity | No |
| "as opposed to merely measuring or scoring" | Sub-Q6 (contrast class) | OK — the measurement literature is in scope as the contrast that defines the gap | No |
| "the relationship between enforced choice-coherence and downstream decision-quality" | Sub-Q9 | OK | No |
| "or task performance" | Sub-Q10 | OK — kept distinct from decision quality; a task-success metric is not the same as decision quality | No |
| "empirically tested" | Sub-Q9, Sub-Q10, and the "empirical or theoretical" required_field on both intervention entities | OK — theory-only proposals must be distinguished from tested ones | No |
| "in either direction" | Sub-Q11 | OK — a degradation finding counts as an answer, not as a null | No |
| "the economics literature" | Front 1; Entities Afriat / Varian / Houtman-Maks | OK | No |
| "Afriat/Varian/Houtman-Maks efficiency and repair methods" | Entities, each with a repair-vs-measure field | OK — all three named individually; "repair" preserved as distinct from "efficiency" | No |
| "the ML/alignment literature" | Front 2 | OK | No |
| "coherence theorems" | Entity: coherence theorems, with a relation-to-competence field | OK — includes the "coherence does not imply competence" critiques | No |
| "Bradley-Terry/RLHF consistency violations" | Entity: Bradley-Terry consistency violations in RLHF | OK — both the BT model and the RLHF pipeline context | No |
| "Nash learning from human feedback" | Entity: Nash learning from human feedback | OK — with the von Neumann winner / preference-game family as its neighbourhood | No |
| "two related but distinct search fronts" | required_formats: explicit separation; headings 2–3 vs 4–5 | OK — the draft structure enforces the separation rather than merging into one narrative | No |

**Zero `Gap? = YES` rows.**

Two scope decisions worth recording, because they widen rather than narrow:

1. "**or outputs**" is read at full breadth. An intervention that operates on token probabilities
   rather than on a realised choice sequence still qualifies. Narrowing this to "choice sequences"
   would have excluded the closest known neighbour to the target intervention.
2. "**revealed-preference consistency**" is read as the axiom family, with transitivity and
   probabilistic coherence tracked as adjacent systems. A census that admitted only GARP-over-budget-sets
   would report an empty field while the neighbouring field is populated — which is precisely the
   failure mode this run exists to avoid.
