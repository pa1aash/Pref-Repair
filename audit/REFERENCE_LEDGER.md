# Reference ledger

Rows R1-R12 are the citations appearing in `docs/F3-PLAN-ORIGINAL.md`. Rows R13+ were found
during this session's audit and are **absent from the plan** - they are listed here because the
plan's reference list is incomplete in ways that matter. Every row starts at
**unverified** and is only moved to **verified** by an actual fetch of the actual document in
this repository's audit trail. A reference that could not be resolved stays **unverified** —
it is never silently dropped, and never upgraded on the strength of a search-result snippet.

**Status vocabulary**

| Status | Meaning |
|---|---|
| `unverified` | Not yet fetched. Default state. |
| `verified` | Document fetched and read; the plan MD's characterisation of it checked against the text. |
| `verified-discrepant` | Fetched, but the plan MD mischaracterises it. Discrepancy noted in the row. |
| `unresolved` | Fetch attempted and failed (paywall, 403, dead identifier). The attempt is recorded. |

---

| # | Citation | Identifier | Role in the plan | Bears on | Status | Notes |
|---|---|---|---|---|---|---|
| R1 | Chen, Liu, Shan & Zhong, *PNAS* 120(51), 2023 | arXiv:2305.12763 | Source of the CCEI 0.997–0.999 baseline ceiling | S1, C4 | **verified** | Read in full (arXiv v3 + PMC10740389). Figure confirmed to the digit; baseline-only. `audit/killcheck_E3.md` |
| R2 | Wen, S., "Economic Rationality under Specialization" | arXiv:2501.18190 | Sole cited evidence that CCEI headroom exists under persona prompting | S2, C4 | **verified-discrepant** | Read in full, 21 pp. Direction holds; magnitude unusable (headline 0.127 is below its own design's arithmetic floor of 0.25). `audit/killcheck_E2.md` |
| R3 | Yamin et al. | arXiv:2605.08556 | Revealed-preference model of LLM medical decisions; prompt-steering fails | S3 | unverified | — |
| R4 | Andrews, I., "Revealed Rationality" | arXiv:2608.05015 | `1 − CCEI` as a training-time penalty; theory only, no experiments | S4, C2, C3 | **verified-discrepant** | Read in full, 25 pp. Theory-only and no inference-time mechanism both confirmed; but he does **not** decline the sufficiency question. `audit/killcheck_E1.md` |
| R5 | Aguiar & Kashaev, GARP-EFM | arXiv:2603.23993 | **A training-time intervention** — fine-tunes a time-series foundation model on GARP-consistent synthetic data. The plan did not record this | **C3** | unverified | Abstract read; full read deferred. The plan listed it without noting it is an intervention, not a measurement |
| R6 | Zhang, Swamy, Wu et al., "Back to Blackwell" | arXiv:2602.19041 | The opposite stance: accept cycles rather than project them | S5, C1 | **verified** | Read in full. FOIL, not refutation — necessity grounds, not normative. `audit/killcheck_E6.md` |
| R7 | Consistency-as-uncertainty-signal (ICML 2026 workshop) | arXiv:2602.11619 | Reason to demote the "consistency predicts quality" angle | S6 | unverified | Present in the plan MD but absent from the session brief's citation list; included here for completeness |
| R8 | Afriat, S. N. (1973), "On a system of inequalities in demand analysis: an extension of the classical method" | *International Economic Review* 14(2) | Origin of the efficiency index (CCEI) and the Afriat inequalities | S7, S8 | unverified | Classical; identifier reconstructed, not fetched |
| R9 | Houtman, M. & Maks, J. (1985), "Determining all maximal data subsets consistent with revealed preference" | *Kwantitatieve Methoden* 19 | Minimal-deletion goodness-of-fit index | S7 | unverified | Classical; not on arXiv |
| R10 | Varian, H. R. (1990), "Goodness-of-fit in optimizing models" | *Journal of Econometrics* 46(1–2) | Goodness-of-fit framework for revealed preference | S7 | unverified | Classical |
| R11 | Samuelson, P. A. (1938), "A note on the pure theory of consumer's behaviour" | *Economica* 5(17) | Origin of revealed preference | — | unverified | Foundational citation; decorative in the plan's argument |
| R12 | Echenique, F., Lee, S. & Shum, M., "The money pump as a measure of revealed preference violations" | *Journal of Political Economy* 119(6), 2011 | Third violation-severity index alongside CCEI and Houtman–Maks | S7, method step 2 | unverified | Year/venue reconstructed, not fetched |
| **R13** | Chadwick, A., Kahng, A. & Kipper, J. (2025), "Dutch books and money pumps: rectifying vulnerabilities in LLMs through rationality" | HAR 2025 (5th Intl. Conf. on Human and Artificial Rationality), Paris | **NOT in the plan.** Found this session. Builds an inference-time "rationality layer" repairing LLM intransitivity + probabilistic incoherence | **C3**, C1, C2 | **verified** | Fetched and read in full, 19 pp. See `audit/INSTRUMENT_CALIBRATION.md` §4.1. Refutes C3 as worded |
| **R14** | Zhu, J.-Q., Yan, H. & Griffiths, T. L., "Recovering Event Probabilities from Large Language Model Embeddings via Axiomatic Constraints" | arXiv:2505.07883 | **NOT in the plan.** Enforces probability axioms on LLM-derived quantities | C3 | unverified | Abstract only. Adjacent occupant; full read deferred |
| **R15** | Echenique, F., Imai, T. & Saito, K. (2023), minimal-perturbation / money-pump-adjacent index work | *JEEA* | **NOT in the plan.** Surfaced by kill-check E1: "minimal perturbation index" is an already-owned term | S7, naming | unverified | Flagged by E1; term collision with the brief's headline phrase |
| **R16** | Echenique, F. (2021), critique of the CCEI's interpretation | — | **NOT in the plan.** Cited approvingly by Andrews; absent from the brief | S1, C4 | unverified | Flagged by E1 |
| **R17** | Bronars, S. G. (1987), "The power of nonparametric tests of preference maximization" | *Econometrica* 55(3):693–698 | **NOT in the plan.** Test-power benchmark | C4, S9 | **unresolved** | Closed on Unpaywall (zero OA locations), S2 reports `CLOSED`, JSTOR landing page only. All method description in this repo is **secondary and labelled as such**; no numerical result is attributed to Bronars directly |
| **R18** | Beatty, T. K. M. & Crawford, I. A. (2011), "How demanding is the revealed preference approach to demand?" | *AER* 101(6):2782–2795 | **NOT in the plan.** Power-vs-pass tradeoff; source of `m = r − a` and of `area = 1 − Bronars power` | C4, S9 | **verified** | Read in full via the author-hosted Oxford copy (AER and both working-paper DOIs closed). See `audit/BRONARS_NOTE.md` |
| **R19** | Crawford, I. & Tian, L. (2026), "The Empirical Content of Revealed Preference in High Dimensions" | arXiv:2605.29361 | **NOT in the plan.** Proves power falls exponentially in the number of goods | C4, S9 | **verified** | Read in full. Theorems 1–2 and simulations. See `audit/BRONARS_NOTE.md` |
| **R20** | LLM-RankFusion | arXiv:2406.00231 | **NOT in the plan.** Inference-time repair of order and transitivity inconsistency in an LLM's own pairwise judgments; improves NDCG@10 | **C1, C3** | unverified | Surfaced by kill-check E5. Occupies the inference-time repair cell. Full read is the top priority for the next session |
| **R21** | TrustJudge | arXiv:2509.21117 | **NOT in the plan.** Cuts transitivity inconsistency 15.22% → 4.40% while maintaining accuracy | **C1, C3** | unverified | Surfaced by E5 |
| **R22** | Cullen, Garland, Roman, Thomson, Ziakas & Thornley | arXiv:2604.17502 | **NOT in the plan.** Deliberately trains agents to violate completeness; reports **+11%/+18%** task usefulness | **C2** | unverified | Surfaced by E5. Direct empirical coherence/competence dissociation |
| **R23** | Zhi-Xuan, T. et al. (2024) | *Philosophical Studies*, DOI 10.1007/s11098-024-02249-w | **NOT in the plan.** Peer-reviewed argument that coherence is not rationally required and is uninformative | **C2** | unverified | Surfaced by E5. This is the brief's "clean negative" headline, already published as a thesis |
| **R24** | "Beyond Bradley-Terry Models: A General Preference Model for LM Alignment" | arXiv:2410.02197 (ICML 2025) | **NOT in the plan.** Enforce-total-order vs accept-cycles ablation on LLMs | **C2** | unverified | Surfaced by E5 |
| **R25** | "Transitivity Meets Cyclicity" | arXiv:2605.17342 (ICML 2026) | **NOT in the plan.** Second matched ablation, same direction | **C2** | unverified | Surfaced by E5 |
| **R26** | Andreoni, Gillen & Harbaugh (2013) | — | **NOT in the plan.** Reports that **31% of uniform-random agents clear CCEI 0.99** on the Andreoni–Miller design | **C4** | unverified | Surfaced by E4. Directly attacks the S4 gate's 0.99 threshold |

---

## Ledger discipline

1. A row moves to `verified` only after the document itself has been read, and only when the
   kill-check or note that read it is committed to this repository.
2. Abstract-only reads do **not** qualify a row as `verified` for any citation whose role in the
   plan is a claim about the paper's *contents* (R1, R2, R4, R6 in particular — the plan makes
   claims about what these papers do and do not contain, which an abstract cannot settle).
3. Classical references (R8–R12) that are not open-access may end the session `unverified`. That
   is an acceptable outcome and must be reported as such; it is not a defect to paper over.
