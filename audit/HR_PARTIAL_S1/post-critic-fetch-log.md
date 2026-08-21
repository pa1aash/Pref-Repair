# Step 13 — post-critic gap-fetch log

## Triage: how many critic findings were EVIDENCE gaps rather than CITATION gaps?

44 findings across four critics (14 critical). Every width- and depth-critic finding naming a missing
topic was checked against the vault before any fetch was considered. Result:

| Critic-named topic | Notes already in vault | Verdict |
|---|---|---|
| ELSPR training-data self-purification | 1 | citation gap — patcher can cite |
| Drift-to-coherence martingale intervention | 1 | citation gap |
| Empirical content of revealed preference in high dimensions | 1 | citation gap — load-bearing for power |
| Axioms for AI alignment from human feedback | 1 | citation gap |
| Prompt perturbation over comparison graphs | 1 | citation gap |
| Position bias in listwise ranking | 1 | citation gap |
| Self-play preference optimisation cluster | 2 | citation gap |
| Stackelberg learning from human feedback | 1 | citation gap |
| Maximal lotteries | 1 | citation gap |
| Shapley–Scarf revealed preference | 1 | citation gap |

**Ten of ten were citation gaps, not evidence gaps.** The corpus already holds the sources; the draft
simply did not cite them. That is the patcher's job and no fetch would help.

This is worth recording as a finding about the run itself: the width critic observed that "the whole
self-play/Stackelberg/Markov-chain Nash sub-cluster and the whole judge-graph-repair sub-cluster being
uncited together suggests two evidence chains were dropped wholesale rather than by per-source
judgement." That is a drafting failure, not a coverage failure, and it is correctable by patch.

## Genuine evidence gaps found: 2 (of a cap of 5)

Both are census-completeness items surfaced by the corrected economics working-paper search, and both are
absent from the vault:

| arXiv | Why it matters | Status |
|---|---|---|
| 2503.06646 | Reported to propose an alignment method improving "the economic rationality of LLMs" — if so, a training-time economics-front intervention the census omits | fetched this step |
| 2602.09362 | arXiv version of an NBER working paper on AI behavioural biases **and their mitigation** — if the mitigations are interventions rather than prompt tweaks, it belongs in the census | fetched this step |

One fetcher was spawned rather than the permitted two-to-four: the gap is two documents, and splitting
them across fetchers would have added contention on the vault's SQLite database for no benefit.

## Gaps deliberately NOT filled

- **De Peretti (2005)**, *Macroeconomic Dynamics* 9(3):372–397. The depth critic correctly notes the
  report claims the quantity-perturbation program "was never written down" and that this is false. But
  the source is already characterised in full in `docs/METHOD_NOTE_Q3.md`, which names it as the fallback
  heuristic and states its failure mode. **No fetch needed — the patcher cites the method note.** The
  report's claim is a drafting error, not an evidence gap.
- **Bronars (1987)** remains `unresolved` — closed access, every route failed across two sessions. The
  patcher must cite it as secondary-sourced, exactly as `audit/BRONARS_NOTE.md` does, and must not
  present it as read.
- Full-text venues (ACL Anthology, PhilPapers, EconStor, SSRN) remain bot-walled. Any residual
  "seventh occupant" risk stands, and the report must state it as a limitation rather than claim census
  completeness.
