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
| R1 | Chen, Liu, Shan & Zhong, *PNAS* 120(51), 2023 | arXiv:2305.12763 | Source of the CCEI 0.997–0.999 baseline ceiling | S1, C4 | unverified | Kill-check E3 |
| R2 | Rationality under specialization / persona conditioning | arXiv:2501.18190 | Sole cited evidence that CCEI headroom exists under persona prompting | S2, C4 | unverified | Kill-check E2. Load-bearing input to the S4 gate |
| R3 | Yamin et al. | arXiv:2605.08556 | Revealed-preference model of LLM medical decisions; prompt-steering fails | S3 | unverified | — |
| R4 | Andrews | arXiv:2608.05015 | `1 − CCEI` as a training-time penalty; theory only, no experiments | S4, C2, C3 | unverified | Kill-check E1. Largest scoop risk |
| R5 | Aguiar & Kashaev, GARP-EFM | arXiv:2603.23993 | Cited as prior art to engage; role not specified in the plan | — | unverified | Plan lists it under "prior art you must cite" without saying what it does |
| R6 | Zhang, Swamy, Wu et al., "Back to Blackwell" | arXiv:2602.19041 | The opposite stance: accept cycles rather than project them | S5, C1 | unverified | Kill-check E6 |
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
| **R17** | Bronars, S. G. (1987), "The power of nonparametric tests of preference maximization" | *Econometrica* 55(3):693–698 | **NOT in the plan.** Test-power benchmark | C4, S9 | unverified | See `audit/BRONARS_NOTE.md` |
| **R18** | Beatty, T. K. M. & Crawford, I. A. (2011), "How demanding is the revealed preference approach to demand?" | *AER* 101(6):2782–2795 | **NOT in the plan.** Power-vs-pass tradeoff | C4, S9 | unverified | See `audit/BRONARS_NOTE.md` |
| **R19** | Crawford, I. & Tian, L. (2026), "The Empirical Content of Revealed Preference in High Dimensions" | arXiv:2605.29361 | **NOT in the plan.** Power falls as the number of goods rises | C4, S9 | unverified | Directly bears on the brief's design |

---

## Ledger discipline

1. A row moves to `verified` only after the document itself has been read, and only when the
   kill-check or note that read it is committed to this repository.
2. Abstract-only reads do **not** qualify a row as `verified` for any citation whose role in the
   plan is a claim about the paper's *contents* (R1, R2, R4, R6 in particular — the plan makes
   claims about what these papers do and do not contain, which an abstract cannot settle).
3. Classical references (R8–R12) that are not open-access may end the session `unverified`. That
   is an acceptable outcome and must be reported as such; it is not a defect to paper over.
