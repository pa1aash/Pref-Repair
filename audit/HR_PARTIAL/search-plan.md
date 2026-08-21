# Search plan — revealed-preference-repair-llm-4f6896

Three lenses per atomic item. `time_periods` is empty in the decomposition, so **Lens D does not
apply** — there is no fiscal/reporting period in this query and no filing to target.

Retrieval constraint inherited from the calling session: **headless only**. RePEc/IDEAS/EconPapers
are known to be JS-rendered and are therefore unavailable; that is a standing gap, not a zero.

| Atomic item | Search query | Type | Lens | Target |
|---|---|---|---|---|
| Sub-Q1–4 (correct/project/repair/enforce) | `"GARP" AND "projection"` | arXiv-ft | breadth | factual |
| Sub-Q1–4 | `"enforce" AND "GARP"` | arXiv-ft | breadth | factual |
| Sub-Q1–4 | `"repair" AND "revealed preference"` | arXiv-ft | breadth | factual |
| Sub-Q1–4 | `rationality repair language model` | OpenAlex | breadth | factual |
| Sub-Q1–4 | `enforcing consistency LLM outputs axioms` | OpenAlex | breadth | factual |
| Sub-Q1–4 | `"rationality layer" LLM` | web | breadth | factual |
| Sub-Q2/Q8 (projection, minimal perturbation) | `"minimal perturbation" AND "revealed preference"` | arXiv-ft | depth | canonical |
| Sub-Q2/Q8 | `minimum distance projection rationalizable demand` | OpenAlex | depth | canonical |
| Sub-Q2/Q8 | `Echenique Imai Saito minimal perturbation index` | OpenAlex | depth | canonical |
| Sub-Q5 (inference vs training time) | `"inference-time" AND "revealed preference"` | arXiv-ft | breadth | factual |
| Sub-Q5 | `test-time intervention preference consistency LLM` | arXiv-ft | breadth | recent |
| Sub-Q6 (measurement contrast class) | `"CCEI" AND "language model"` | arXiv-ft | breadth | factual |
| Sub-Q6 | `economic rationality large language models measurement` | OpenAlex | breadth | recent |
| Sub-Q6 | `GARP violations LLM agents benchmark` | arXiv-ft | breadth | recent |
| Sub-Q7 (axiom systems) | `probabilistic coherence LLM Dutch book` | arXiv-ft | breadth | factual |
| Sub-Q7 | `transitivity violations language model preferences` | arXiv-ft | breadth | factual |
| Sub-Q7 | `WARP SARP language model` | arXiv-ft | breadth | factual |
| Entity: Afriat | `Afriat theorem efficiency index` | OpenAlex | depth | canonical |
| Entity: Afriat | `Afriat 1973 system of inequalities demand analysis` | Crossref | depth | canonical |
| Entity: Varian | `Varian goodness of fit optimizing models 1990` | OpenAlex | depth | canonical |
| Entity: Houtman-Maks | `Houtman Maks maximal consistent subsets revealed preference` | OpenAlex | depth | canonical |
| Entity: Houtman-Maks | `Houtman-Maks index computation algorithm` | arXiv-ft | depth | canonical |
| Entity: money-pump | `Echenique Lee Shum money pump revealed preference violations` | OpenAlex | depth | canonical |
| Entity: coherence theorems | `"coherence" AND "goal-directed"` | arXiv-ft | depth | canonical |
| Entity: coherence theorems | `coherence arguments do not imply goal-directed behavior` | web | adversarial | contrarian |
| Entity: coherence theorems | `Thornley coherence theorems agents shutdown` | web | adversarial | contrarian |
| Entity: Bradley-Terry | `"Bradley-Terry" AND "intransitive"` | arXiv-ft | breadth | factual |
| Entity: Bradley-Terry | `Bradley-Terry assumption violated RLHF preference data` | arXiv-ft | adversarial | contrarian |
| Entity: Bradley-Terry | `reward model transitivity violations` | arXiv-ft | breadth | factual |
| Entity: Nash learning from HF | `"Nash learning from human feedback"` | arXiv-ft | depth | canonical |
| Entity: Nash learning from HF | `"von Neumann winner" preference` | arXiv-ft | depth | canonical |
| Entity: Nash learning from HF | `preference game self-play alignment intransitive` | arXiv-ft | breadth | recent |
| Sub-Q9/Q10 (downstream quality) | `consistency and accuracy language model agents relationship` | arXiv-ft | breadth | factual |
| Sub-Q9/Q10 | `does coherence improve performance LLM agent` | web | breadth | factual |
| Sub-Q9/Q10 | `enforcing consistency degrades performance language model` | arXiv-ft | adversarial | contrarian |
| Sub-Q9/Q10 | `self-consistency downstream task accuracy tradeoff` | arXiv-ft | adversarial | contrarian |
| Sub-Q11 (direction) | `rationality alignment target criticism` | web | adversarial | contrarian |
| Sub-Q12 (econ→AI) | `revealed preference applied to artificial agents` | OpenAlex | breadth | factual |
| Sub-Q12 | `inverse reinforcement learning revealed preference microeconomics` | arXiv-ft | depth | canonical |
| Sub-Q13 (ML/alignment stance) | `accept intransitivity rather than resolve preference learning` | arXiv-ft | adversarial | contrarian |
| Sub-Q14 (literatures missing each other) | `social choice aggregation LLM preferences` | arXiv-ft | breadth | factual |
| Sub-Q14 | `Kemeny ranking LLM pairwise comparisons` | arXiv-ft | breadth | factual |
| Entity: AI agents (non-LLM) | `revealed preference reinforcement learning agent rationality` | arXiv-ft | breadth | factual |
| Cross-cutting | `limitations of CCEI critique` | web | adversarial | contrarian |
| Cross-cutting | `power of revealed preference tests Bronars` | OpenAlex | depth | canonical |

**Adversarial searches: 9** (minimum 5 required). Lens B (depth/canonical) is heavily weighted
because the economics half of this query has a 90-year canonical literature that web search will
not surface.
