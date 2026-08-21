# Coverage gaps

> Carried forward from G0's partial width sweep (`audit/HR_PARTIAL/RUN_RECORD.md`) and updated
> after G0.5's items 2 and 3. Items with weak source coverage that the draft must not overclaim on.

| Atomic item | Coverage | Note |
|---|---|---|
| Interventions, inference-time | **well-covered** | Six occupants, four read in full during G0.5 |
| Interventions, training-time | **adequate** | Two more surfaced by the RePEc search and not yet read |
| GARP / WARP / SARP | **adequate** | — |
| Afriat efficiency methods | **adequate** | — |
| Varian goodness-of-fit | **THIN** | Varian (1990) and (1985) both unread; paywalled, no OA copy found. Do not cite as though read |
| Houtman–Maks | **THIN** | Original (1985) unread; complexity results carried from secondary sources |
| Money-pump index | **THIN** | Full text obtained but not deeply analysed |
| Bronars power | **adequate but secondary** | **Bronars (1987) itself is `unresolved`** — closed access, every route failed. Every statement about it in this repository is secondary and labelled as such. Must not be cited as though read |
| Coherence theorems and critiques | **well-covered** | Peer-reviewed and forum sources, labelled by type |
| Bradley–Terry violations in RLHF | **well-covered** | Both ICML ablations read in full incl. appendices |
| Nash learning from human feedback | **well-covered** | — |
| Downstream quality after enforcement | **adequate** | Six data points, all binary; no exogenous-payoff study on an agent's own choices |
| Minimal-perturbation formulations | **adequate** | Resolved in `docs/METHOD_NOTE_Q3.md`; Demuynck & Rehbeck and Chen–Lanier–Quah both surfaced but not read in full |
| Reliability of CCEI | **adequate** | One source, but it is large and in *PNAS* |

**Structural gaps that no amount of further searching in this repository closes:**

1. **Metadata-not-full-text indexing.** Both the arXiv legacy full-text index (partial) and RePEc
   (title/abstract/keywords only) will miss a paper that performs the projection in its §4 without
   saying so in its abstract. This is the exact blind spot that hid the HAR 2025 occupant from the
   original sweep, and it is not closed.
2. **Semantic Scholar was never reachable.** Persistent HTTP 429 across every session. No
   citation-chaining forward or backward from the key papers was ever performed.
3. **SSRN and EconStor unswept.** Adjacent working-paper repositories, not separately searched.
4. **Three classical economics references remain unread** and one (Bronars) is unresolved outright.
