# Bibkeys used in `docs/RELATED_WORK.md`

Written 2026-08-26 alongside `docs/RELATED_WORK.md`. Every `\citep{}` / `\citet{}` key that
appears in that file is listed here with the citation information the repository actually holds,
so a later step can build the `.bib` without re-deriving anything.

**Conventions and cautions for whoever builds the `.bib`:**

- Where a field is genuinely unknown from repo sources it is marked `UNKNOWN — verify`. Do not
  invent it. Four entries need a lookup before submission and are flagged in §3.
- Several papers are preprints whose author lists were **elided in the audit documents under the
  repository's model/author hygiene policy**. Where the audit records only a partial author list,
  that is noted; the arXiv ID is always exact and is sufficient to recover the full list.
- Venue strings are given as the repo records them. Two entries are *not* on arXiv
  (`chadwick2025dutchbooks`, `cook2026whatllmswant`) and will not be found by an arXiv-only
  lookup tool.

---

## 1. Papers cited in the related-work prose

| Bibkey | Authors | Year | Title | Venue / ID |
|---|---|---|---|---|
| `wang2026poise` | Wang, Zhan et al. (Peking University + 8 collaborating institutions; full list on arXiv, partially elided in `audit/ITEM2_occupants_A.md` per repo hygiene) | 2026 | TrustRoboReward: Preference-Ordered Isotonic Score Editing for Multi-Paradigm Reward Modeling *(exact subtitle — verify against arXiv listing)* | arXiv:2608.08491v1, 9 Aug 2026, cs.AI. 23 pp. Submission-format preprint (unstripped NeurIPS 2026 funding boilerplate); **no journal reference in arXiv metadata** — cite as preprint |
| `chadwick2025dutchbooks` | Alina Chadwick, Anson Kahng, Jens Kipper (University of Rochester) | 2025 | Dutch books and money pumps: rectifying vulnerabilities in LLMs through rationality | Proc. 5th International Conference on Human and Artificial Rationality (HAR 2025), Paris. **NOT on arXiv.** PDF: `https://ansonkahng.com/docs/papers/llmrationality.pdf` |
| `wang2025trustjudge` | Yidong Wang, Song, Zhu, Zhang, Yu, Chen, Song, Wang, Wang, Wu, Dai, Zhang, Ye, Zhang (Peking University et al.) — **first-name initials for the lead author are UNVERIFIED; take the full author string from arXiv** | 2025 | TrustJudge: Inconsistencies of LLM-as-a-Judge and How to Alleviate Them | arXiv:2509.21117v2, Sep 2025 |
| `sun2026consistre` | Mingxuan Sun (single author) | 2026 | CONSISTRE: A Unified Consistency-Aware Framework for Document-Level Relation Extraction with Large Language Models | arXiv:2607.24312v1, 27 Jul 2026, cs.CL. 13 pp. Comment on listing: "Submitted to IEEE/ACM Transactions on Audio, Speech, and Language Processing" — **cite as preprint, not as TASLP** |
| `buchanan2026innate` | Joy Buchanan, Joshua Foster | 2026 | The Innate Economic Preferences of Language Models | arXiv:2607.26288v1, 28 Jul 2026, econ.EM |
| `zeng2024rankfusion` | Zeng, Tendolkar, Baartmans, Wu, Chen & Wang (Oregon State / Penn State) — first names UNKNOWN, take from arXiv | 2024 | LLM-RankFusion *(full title — verify subtitle against arXiv)* | arXiv:2406.00231v2, 26 Nov 2024, cs.IR / cs.AI / cs.CL. 18 pp. Footer "Preprint. Under review."; **unrefereed preprint — no venue in arXiv metadata on either version** |
| `aguiar2026garpefm` | Aguiar & Kashaev — first names UNKNOWN, take from arXiv | 2026 | GARP-EFM: Improving Foundation Models with Revealed Preference Structure *(title reconstructed from the vault note slug `260323993-garp-efm-improving-foundation-models-with-revealed-preference-structur`; **verify exact title**)* | arXiv:2603.23993 |
| `zhang2025gpm` | Zhang, Zhang, Wu, Xu & Gu — first names UNKNOWN, take from arXiv/PMLR | 2025 | Beyond Bradley-Terry Models: A General Preference Model for Language Model Alignment | ICML 2025, PMLR 267. arXiv:2410.02197v3, 11 Jun 2025. 27 pp. **Peer-reviewed — cite the PMLR entry, not the preprint** |
| `huang2026hrc` | Huang, Li, Zhao & Li — first names UNKNOWN, take from arXiv/PMLR | 2026 | Transitivity Meets Cyclicity: Explicit Preference Decomposition for Dynamic LLM Alignment | ICML 2026, PMLR 306. arXiv:2605.17342. 26 pp. **Peer-reviewed — cite the PMLR entry** |
| `andrews2026revealed` | Andrews *(single author; economics department + NBER affiliation. First name UNKNOWN from repo sources — `audit/killcheck_E1.md` records the surname only.)* | 2026 | Revealed Rationality: Label-Free Evaluation and Regularization from Representation Theorems | arXiv:2608.05015v1, 5 Aug 2026, econ.TH. 25 pp. **Note:** v1 on arXiv is dated 5 Aug 2026 but footnote 1 gives the first circulated version as **21 Feb 2026** |
| `ouyang2025aidecisionmaker` | Shumiao Ouyang, Hayong Yun, Xingjian Zheng | 2025 | AI as Decision-Maker: Ethics and Risk Preferences of LLMs | arXiv:2406.01168v3, econ.GN (v1 3 Jun 2024, **v3 10 Jun 2025 — cite v3**). Also circulated as SSRN 4851711 under the title "How Ethical Should AI Be? How AI Alignment Shapes the Risk Preferences of LLMs" |
| `nitsch2022reliability` | Felix J. Nitsch, Lisa M. Lüpken, Nils Lüschow, Tobias Kalenscher | 2022 | On the reliability of individual economic rationality measurements | *PNAS* 119(31):e2202070119. DOI `10.1073/pnas.2202070119`; PMID 35881803; PMCID PMC9351500. Green OA (CC BY-NC-ND); data mirror `osf.io/kd4hw` |
| `yamin2026elicited` | Kaiser Yamin *(given name UNVERIFIED)*, J. Tang, S. Cortes-Gomez, A. Sharma, Eric Horvitz, Bryan Wilder | 2026 | When Agents Say One Thing and Do Another: Validating Elicited Beliefs from LLMs | arXiv:2602.06286v2, 08 May 2026, cs.AI. CC BY 4.0 |
| `zhu2025axiomatic` | Jian-Qiao Zhu, Haijiang Yan, Thomas L. Griffiths | 2025 | Recovering Event Probabilities from Large Language Model Embeddings via Axiomatic Constraints | arXiv:2505.07883 |
| `cook2026whatllmswant` | Cook, Kazinnik, Modig & Palmer — first names UNKNOWN, take from the working-paper cover page | 2026 | What Do LLMs Want? | **NOT on arXiv.** Federal Reserve Board FEDS Working Paper 2026-006; also circulated as Kansas City Fed RWP 25-19. Found via RePEc |
| `wang2025tactics` | Wang, Yao, Zhang, Gai, Liu, Zhong (Tsinghua) — first names UNKNOWN, take from arXiv | 2025 | When Experimental Economics Meets Large Language Models: Tactics with Evidence | arXiv:2505.21371v1 |
| `wen2025specialization` | Wen *(2025; author list UNKNOWN from repo sources — Andrews cites it as "Wen (2025)")* | 2025 | Economic Rationality under Specialization: Evidence of Decision Bias in AI Agents *(title reconstructed from the vault note slug `250118190-economic-rationality-under-specialization-evidence-of-decision-bias-in`; **verify exact title**)* | arXiv:2501.18190 |
| `chen2023emergence` | Chen et al. *(2023; full author list UNKNOWN from repo sources)* | 2023 | The Emergence of Economic Rationality of GPT | arXiv:2305.12763. **Also published in *PNAS* — verify and prefer the journal entry** |
| `zhang2026blackwell` | Zhang, Swamy, Wu et al. — first names UNKNOWN, take from arXiv | 2026 | Back to Blackwell: Closing the Loop on Intransitivity in Multi-Objective Preference *(title reconstructed from the vault note slug; **verify exact title and subtitle**)* | arXiv:2602.19041 |
| `echenique2021ccei` | Federico Echenique | 2021 | On the meaning of the critical cost efficiency index | arXiv:2109.06354 |
| `echenique2023minimal` | Federico Echenique, Taisuke Imai, Kota Saito | 2023 | *(Paper introducing the **minimal perturbation index** for the SEU setting. Exact title UNKNOWN from repo sources — `audit/killcheck_E1.md` §4 records authors, year, journal and the index name only. **Must be looked up.**)* | *Journal of the European Economic Association* (JEEA) |
| `varian1985` | Hal R. Varian | 1985 | *(The paper to which `chen2024goodness` traces the non-linear **Least Squares index**. Exact title UNKNOWN from repo sources; the standard candidate is "Non-parametric analysis of optimizing behavior with measurement error", J. Econometrics 30(1–2). **Verify before use.**)* | 1985 |
| `chen2024goodness` | Chen, Lanier & Quah — first names UNKNOWN, take from arXiv | 2024 | Goodness-of-fit measures for revealed preference *(survey; verify exact title)* | arXiv:2405.08464 |
| `bronars1987power` | Stephen G. Bronars | 1987 | The power of nonparametric tests of preference maximization | *Econometrica* 55(3):693–698 |

---

## 2. Keys referenced in the operator comment but NOT cited in the prose

None. Every bibkey appearing anywhere in `docs/RELATED_WORK.md` is in the table above; the
operator comment names files and arXiv IDs but issues no `\cite` commands.

The following papers are discussed in the repo's audit trail and may be wanted by other sections
of the paper, but are **deliberately not cited in Related Work** and so have no key here:
Demuynck & Rehbeck 2023 (`Economic Theory` 76(4) — the MILP formulation, belongs to Method),
Shiozawa 2015 (NP-hardness of the minimum cost index), Boodaghians & Vetta 2015 (Houtman–Maks
complexity), Gorski et al. 2007 (biconvex optimisation), Andreoni, Gillen & Harbaugh 2013 (31%
of random agents clear CCEI 0.99), Xu et al. arXiv:2502.14074 (non-transitivity in
LLM-as-a-judge), and Lu et al. arXiv:2507.20796. Add keys for these in the sections that use
them.

---

## 3. Fields that MUST be looked up before the `.bib` is final

Four entries cannot be completed from repository sources and are the only real blockers:

1. **`echenique2023minimal`** — the *title* is not recorded anywhere in the repo, only the
   authors, year, journal and the fact that it owns the term "minimal perturbation index". This
   one matters: the prose uses it to defuse a naming collision, so a wrong title is a visible
   error to exactly the reviewer who would raise the collision.
2. **`varian1985`** — recorded only as the origin of the non-linear Least Squares index, traced
   there by `chen2024goodness`. The likely target is the 1985 measurement-error paper, but the
   repo does not say so; confirm from `chen2024goodness`'s own reference list rather than
   guessing.
3. **`andrews2026revealed`** — surname and affiliation only. The given name must come from the
   arXiv listing.
4. **`wen2025specialization`**, **`chen2023emergence`**, **`zhang2026blackwell`**,
   **`aguiar2026garpefm`** — titles reconstructed from vault note slugs, which are lowercased
   and truncated. Each arXiv ID is exact; pull the canonical title and author list from the
   listing page.

Additionally, confirm published-venue entries rather than preprints for `zhang2025gpm`
(PMLR 267), `huang2026hrc` (PMLR 306), `nitsch2022reliability` (PNAS, already exact) and
`chen2023emergence` (PNAS, if the journal version is the right one to cite).
