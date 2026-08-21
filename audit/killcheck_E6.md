# Kill-check E6 — "Back to Blackwell": foil or refutation of C1?

Target claim: **S5** ("the opposite stance — accept cycles rather than project them"), with
consequences for **C1**.
Brief under test: `docs/F3-PLAN-ORIGINAL.md`, section "Prior art you must cite".

Paper under test: Zhang, Zhang, Grimes, Yu, Swamy & Wu, *Back to Blackwell: Closing the Loop on
Intransitivity in Multi-Objective Preference Fine-Tuning*, arXiv:2602.19041v2 (5 May 2026),
cs.LG, preprint, 24 pages. Six authors, all one institution. Read in full.

---

## Falsifier (stated before the finding)

Written before reporting what the paper contains. The brief's characterisation survives — the
paper is a **FOIL** — unless one of the following is found in the text. Any one of F1–F3 makes
it a **REFUTATION**; F4 alone makes it a **PARTIAL REFUTATION**.

- **F1 (normative argument against enforcement).** A passage arguing that forcing intransitive
  preferences into a consistent order is *wrong* — that it destroys information, discards
  signal, distorts the underlying preference, or misrepresents the evaluator/agent. Not
  "intransitivity breaks my algorithm"; specifically "resolving intransitivity is the error."
  Citing someone *else* who says this, in a related-work sentence, does not count.
- **F2 (the cycles are load-bearing).** A claim, argued or measured, that the cyclic structure
  itself carries decision-relevant information that a consistent restriction cannot express —
  e.g. that the cycle encodes a real multi-criterion trade-off, and that any acyclic summary is
  therefore a strictly impoverished representation of the preference.
- **F3 (a head-to-head loss for repair).** An empirical comparison in which a method that
  *repairs, projects, or enforces acyclicity* on a choice or preference sequence is run and
  loses to one that accepts the cycles. The enforcement must actually be an
  acyclicity/consistency operator, not merely an aggregation step.
- **F4 (a real cost of enforcement, differently mechanised).** An empirical comparison in which
  a method that collapses multi-criterion feedback into a single total order loses to one that
  refuses to — even if the losing method enforces consistency only incidentally, via
  scalarisation rather than via cycle repair. This names a cost C1 must answer even though it
  does not refute C1's mechanism.

Also recorded, per the brief: whether the paper touches GARP, Afriat, revealed preference, or
CCEI at all (bears on whether it is even in C1's literature).

**Result: F1 not found. F2 not found. F3 not found. F4 FOUND.**

---

## What the paper actually does

**Setting.** Preference fine-tuning (PFT) of language models from *multi-objective LLM-as-a-judge
feedback* — confirmed, with one distinction the brief does not record and that turns out to be
the whole ballgame: **the intransitivity the paper studies lives in the judge, not in the agent.**
It is a property of the feedback signal used to train a policy, measured over the judge's
pairwise rankings of sampled candidate responses. It is not a property of the trained model's own
choice behaviour, and the paper never measures the policy's own consistency.

Specifics:

| | |
|---|---|
| Training data | WILDCHECKLISTS (Viswanathan et al. 2025), built on WILDCHAT user conversations; per-prompt generated rubrics, each checklist item treated as one objective |
| Policies fine-tuned | Qwen2.5-Instruct at **3B and 7B** — one family, two sizes |
| Training judge | Qwen3-14B, pairwise, 5-point Likert per checklist item, order-averaged for position bias, 5–10 samples averaged |
| Benchmark judge | a small closed-weight frontier model (named in §6.3) for AlpacaEval 2.0 and Arena-Hard |
| Benchmarks | AlpacaEval 2.0, Arena-Hard (in-domain); IFEval, MMLU, ARC, HellaSwag, TruthfulQA (regression tests) |
| Intransitivity measurement | 100 held-out prompts, N ∈ {2..8} sampled responses from the 7B base model |
| Compute | 16×H100 for generation and scoring, 8×H100 for training; ~50 h/model/epoch for scoring alone; 2 epochs |
| Seeds | **one** (555134). No confidence intervals or error bars anywhere in the paper |

**The intransitivity measurement (Figure 2, p.9).** Two judges compared: **P_JC** (joint check —
the full checklist handed over at once, one aggregate score) and **P_SC** (single check — each
checklist item scored independently). Values recovered from the figure's plotted markers:

| N | Cycles present, P_JC | Cycles present, P_SC | No Condorcet Winner, P_JC | No Condorcet Winner, P_SC |
|---|---|---|---|---|
| 3 | ~21% | ~16% | ~2% | ~0.4% |
| 4 | ~41% | ~31% | ~5% | ~1% |
| 5 | ~61% | ~52% | ~4% | ~2.4% |
| 6 | ~80% | ~68% | ~7% | ~4.8% |
| 7 | ~86% | ~80% | ~8% | ~5% |
| 8 | ~93% | ~85% | ~9% | ~5% |

Two things in that table matter for C1, and the paper says both explicitly in prose:

1. **Scalarising creates cycles.** The joint-check judge — the one that collapses the rubric into
   a single score — is *more* intransitive than the per-item judge at every N. Decomposing into
   objectives "reduces but does not eliminate" intransitivity. This is the paper endorsing, with
   its own data, the Tversky (1969) claim that scalarisation of multiple criteria is a root cause
   of intransitivity.
2. **The cycles are mostly shallow.** Cycles appear in 85–93% of prompts at N = 8, but a Condorcet
   Winner still exists in 91–95% of them. The paper states the reason: "cycles may only occur
   across relatively weak responses." A best option almost always exists; the cycling happens
   below it.

**MaxEntBW.** The Maximum Entropy Blackwell Winner is a solution concept, not a repair operator.
Chain of construction: the von Neumann Winner (a Nash equilibrium of the symmetric zero-sum
preference game — well defined under single-objective intransitivity, computable by self-play);
then Bhatia et al. (2020)'s Blackwell Winner, which extends this to vector payoffs via ℓ∞
distance to a target set; then MaxEntBW, which adds KL regularisation of the adversary policy to
a reference policy. Formally: maximise over π the quantity `min_w min_{π'} E[⟨w, P(π ≻ π'|x)⟩ +
β·KL(π'‖π_ref)]`. In words — a policy that compares favourably against everything in its *local*
neighbourhood, under *whichever* objective it is judged by. The problem it solves is stated
plainly: for vector payoffs the Minimax Theorem fails (Blackwell 1956), order of play matters, and
so the self-play machinery that works in the single-objective case does not extend. MaxEntBW is
well defined anyway.

**PROSPER** (PReference Optimization with a Single Player over Entire Rubrics) is the algorithm
that computes MaxEntBWs at scale. Three reductions: (1) the KL term gives the adversary a Gibbs
closed form, eliminating adversarial training; (2) the objective is concave in the objective-weight
vector w, so the optimum sits at a simplex vertex — the weighting collapses to a prompt-wise
`argmin` over objectives, i.e. **train against whichever rubric item the current policy is
weakest on**; (3) the remaining problem is concave in π, so online mirror descent applies, and
mirror descent is implemented as square-loss regression in the style of REBEL. Theorem 4.2 gives
`V(π*) − V(π̂) ≤ O(√(1/T) + √(C·ε))` under an in-distribution regression-accuracy assumption.

**No GARP, no Afriat, no CCEI, no revealed preference.** Zero occurrences of *GARP*, *Afriat*,
*CCEI*, *revealed preference*, *rationalizab-*, *acyclic*, *Samuelson*, *Houtman*, *Varian
(the economist)*, or *money pump* — confirmed by three independent methods (raw text extraction,
Unicode-NFKD-normalised extraction to defeat ligatures, and a second extractor in layout mode).
The paper's ancestry is social choice and game theory — Condorcet, maximal lotteries, Kreweras,
Fishburn, Blackwell, dueling bandits — plus Tversky (1969) from psychology. It has no contact
with the revealed-preference/Afriat apparatus C1 is built on. The two papers do not share a
literature, a formalism, or an object of study.

---

## Its argument for accepting intransitivity

**Classification: technical necessity, unambiguously. Not a normative argument against
enforcement.** The paper's position is (i) from the brief's dichotomy, and it is stated in almost
those words.

The load-bearing sentences, paraphrased:

- Abstract: whatever the source of the intransitivity, the downstream implication is the same —
  *there is no well-defined optimal policy*, which breaks a core assumption of the standard PFT
  pipeline.
- Introduction: under intransitive preferences there is, by construction, no total ordering over
  options, since every option loses to some other. The reward-model pipeline tries to learn such
  an ordering and is therefore "fundamentally unequipped."
- §3.1: under intransitive preferences there is often no Condorcet Winner, so "we need to consider
  alternative solution concepts."
- §2: prior multi-objective PFT work "implicitly assumes that along each objective, preferences
  are transitive and there is a well-defined optimal policy," which is why it does not apply here.

Every one of these is a statement that **the target of optimisation does not exist**, not that
constructing one is harmful. The paper's move is: the optimum is undefined, so define a different
optimum (a robustness notion) that survives cycles. It nowhere claims that a repaired, acyclic
version of the preference would be *worse* than the raw one, nor that repairing would lose
information. The words *destroy*, *defect*, *artifact*, *noise*, *discard*, and *genuine* do not
appear in the paper in any relevant sense; *distort* appears once, in a related-work sentence
attributing that concern to **other** authors (Conitzer et al., Gölz et al.) and about a different
problem — aggregating across a *population of human raters*, not repairing one evaluator's cycles.

**On defect vs. genuine feature (brief question 5).** The paper gives an explicit two-source
account and it splits the difference:

- Source (i): inconsistent rankings along a *single* objective. Framed as noise/unreliability —
  the paper opens with the "blurry JPEG of the web" metaphor to characterise judge inconsistency.
  This is intransitivity as **defect**.
- Source (ii): scalarising multiple objectives into a single metric. Cited to Tversky (1969) as
  one of the most common root causes of intransitivity in psychology. This is intransitivity as
  **artifact of aggregation** — i.e. not the evaluator's failure but the measurement's.

The acknowledgements confirm this framing is deliberate ("the two root causes of intransitive
preferences that eventually inspired this project"). What the paper conspicuously does **not**
say is that source (ii) intransitivity is a *genuine feature to be preserved*. It treats (ii) as
a problem to be reduced — its own remedy is to stop scalarising at the judge, which its Figure 2
shows lowers the cycle rate. It then handles the residue with a robust solution concept because
that residue cannot be optimised against, not because it deserves protection.

So: the paper is a mechanism-of-necessity paper. F1 and F2 do not fire.

---

## Empirical comparison against consistency-enforcing baselines

**No method in this paper repairs, projects, or enforces acyclicity.** F3 does not fire — the C1
intervention is not implemented, not run, and not beaten. What the paper *does* run is a
**scalarisation** baseline, which enforces a total order as a side effect of collapsing objectives
into one number. That is F4.

**The baseline.** RLCF (RL from Checklist Feedback, Viswanathan et al. 2025): the judge scores
each checklist item; a separate 72B model then generates weights that combine per-item scores into
**one scalar reward per response**. A scalar reward induces a total order. The authors say
explicitly that this scalarisation "can lead to intransitivity." They re-implement RLCF inside
their own optimiser (REBEL) for fairness and additionally evaluate the original authors' released
checkpoint.

**Two ablations also bear on this.** PROSPER-JC asks the judge for a single aggregate score
(m(x) = 1) — scalarisation at the judge, keeping the game-theoretic optimiser. PROSPER-VB fixes
the competitor to π_ref (β → ∞), dropping the adversarial comparator.

**7B results (Table 1) — Arena-Hard / AlpacaEval, higher is better:**

| Model | Arena-Hard vanilla | Arena-Hard style-ctrl | AlpacaEval vanilla | AlpacaEval len-ctrl |
|---|---|---|---|---|
| Qwen2.5-7B-Instruct (base) | 42.4 | 44.2 | 37.1 | 25.32 |
| + RLCF (re-implemented) | 42.5 | 43.9 | 41.4 | **17.24** |
| + PROSPER-JC | 44.2 | 42.0 | 55.3 | **38.21** |
| + PROSPER-VB | 47.6 | 45.5 | 51.2 | 33.64 |
| + **PROSPER** | **49.2** | **46.1** | **55.4** | 37.61 |
| + RLCF (released ckpt, App. A) | 42.2 | 44.6 | 42.3 | 28.08 |

**Head-to-head judge win rates (Figure 3, 500 held-out prompts).** PROSPER beats RLCF **0.68**,
beats the base model **0.73**, beats PROSPER-VB 0.57, beats PROSPER-JC **0.53**. RLCF beats base
only 0.57.

**3B results (Table 3).** base 20.6 / 19.6 / 24.1 / 12.79; RLCF 22.8 / 22.9 / 26.2 / 11.62;
PROSPER-JC 22.9 / 23.4 / 24.7 / 7.4; PROSPER-VB 25.1 / 23.6 / 34.8 / 19.99; **PROSPER 26.0 / 24.6
/ 35.8 / 20.94**. Same column order.

**Regression tests (Table 2, 7B, average over IFEval/MMLU/ARC/HellaSwag/TruthfulQA).** base 72.55;
RLCF 71.30; PROSPER-JC 71.69; PROSPER-VB **72.32**; PROSPER 71.70. At 3B (Table 4): base 65.58;
RLCF 64.54; JC 63.45; VB 64.64; PROSPER 64.74.

**What this does and does not establish.**

The headline is real and it is F4: the pipeline that collapses multi-criterion feedback into one
scalar order is beaten head-to-head 0.68 by the pipeline that refuses to, and loses by 6.7 points
on Arena-Hard and 14.0 on vanilla AlpacaEval at 7B. That is a genuine, measured cost of forcing a
single ordering, and C1 has to say something about it.

But four caveats materially limit how far it travels, and an honest related-work paragraph should
carry them:

1. **The 17.24 is not load-bearing.** The re-implemented RLCF's length-controlled AlpacaEval score
   of 17.24 — 8 points *below* the untuned base — is the paper's most dramatic number and it is
   **not reproduced by the original authors' released checkpoint**, which scores 28.08, *above*
   base, on the same metric. The "scalarisation actively degrades the model" reading is an
   artifact of one re-implementation on one metric. The defensible claim is the weaker one:
   scalarisation underperforms, not that it harms.
2. **The scalarisation ablation is nearly competitive at 7B.** PROSPER-JC — single aggregate judge
   score, i.e. scalarised objectives — *beats* full PROSPER on length-controlled AlpacaEval
   (38.21 vs 37.61) and ties it on vanilla AlpacaEval (55.3 vs 55.4). Head-to-head, PROSPER beats
   JC only 0.53, which is a coin flip. The multi-objective machinery earns its keep decisively on
   Arena-Hard and at 3B, and barely at all on AlpacaEval at 7B.
3. **Nothing here is an acyclicity constraint.** RLCF loses because a 72B model guessed a fixed
   weighting of rubric items badly, and because PROSPER dynamically re-targets the policy's
   weakest criterion. The causal story is adaptive reweighting, not "cycles were preserved." No
   experiment in the paper isolates the effect of cycle preservation.
4. **One seed, no CIs, one model family, one dataset, one judge family.** Table 2 also shows every
   post-training method including PROSPER slightly *below* base on the regression average, with
   the simplest ablation (VB) coming out best on IFEval (73.75 vs base 71.16 vs PROSPER 69.50).

---

## Verdict

**FOIL — cite as contrast — with one PARTIAL-REFUTATION edge C1 must explicitly answer.**

The brief's "opposite stance" label is right in spirit and imprecise in a way that would have got
C1 into trouble if left unexamined. Five reasons this is a foil, not a refutation:

1. **Different object.** Their cycles are in the *evaluator*; C1's are in the *agent's own
   choices*. Repairing a judge's rankings and repairing an agent's demand data are interventions
   on different things.
2. **Different mechanism and timing.** They change the training objective; C1 is a post-hoc,
   inference-time operator. They never build a repair operator, so they never test one.
3. **The argument is necessity, not normativity.** "There is no well-defined optimal policy" says
   the standard pipeline's *target* does not exist. It does not say constructing one is wrong.
   F1 and F2 both fail.
4. **No shared literature.** Zero contact with GARP, Afriat, CCEI, or revealed preference,
   verified three ways.
5. **Their data partly supports C1's diagnosis.** Their P_JC-vs-P_SC comparison shows scalarising
   *creates* cycles, and their Condorcet-Winner panel shows that even at 85–93% cycle prevalence
   a best option still exists >90% of the time — cycles are common but shallow, concentrated among
   weak options. That is exactly the regime in which minimal-perturbation repair is cheap and
   loses little.

The partial-refutation edge is F4 and it is not cosmetic. A reviewer who has read this paper will
compress it to "forcing multi-criterion preferences into one consistent order costs you
performance — 0.68 head-to-head," and will ask why C1's projection is not that same losing move
wearing an economist's hat. The sharpest form of the objection is structural rather than
empirical: **if intransitivity is genuinely multi-objective in origin, then projecting onto a
single acyclic order is a choice of weighting over objectives — which is scalarisation, which is
the baseline that loses.** C1 cannot answer that by pointing at a different mechanism; it has to
argue that the choice data it repairs is single-objective (or that the residual cycles are the
noise-type, source (i), not the aggregation-type, source (ii)), and it should measure which.

**What C1 must say in related work.** State that Back to Blackwell rejects total orders on
*existence* grounds — under cyclic judge feedback there is no optimal policy to learn — and never
argues that repairing cycles destroys information, so its stance is orthogonal to, not opposed to,
inference-time projection of an agent's own choices. Then concede the one real cost it measures:
collapsing multi-criterion feedback into a single order underperforms a method that keeps the
objectives separate, and note that this bites C1 only insofar as the agent's cycles are
aggregation artifacts rather than inconsistency, which is an empirical question C1 should answer
in its own data (a per-condition split of cycle sources, or a Condorcet-Winner-existence check
alongside CCEI). Close by using their own numbers in C1's favour — cycles are frequent but a best
option survives in over 90% of cases, which is the precise condition under which minimal
perturbation is cheap.

---

## One-line summary for docs/CLAIMS.md

`E6: S5 holds as FOIL — cycles accepted because no optimal policy exists, not because repair harms; no GARP/Afriat/CCEI. Its 0.68 win over scalarising RLCF is the one cost C1 must answer.`

---

## Fetch record

| Item | Detail |
|---|---|
| URL | `https://arxiv.org/pdf/2602.19041` |
| HTTP status | 200, redirects followed, final URL identical |
| Bytes | 875,693 |
| Fallbacks used | none — primary fetch succeeded on first attempt |
| Version retrieved | arXiv:2602.19041**v2** [cs.LG], dated 5 May 2026 (the brief cites the 2602 identifier; v2 is the current revision) |
| Local copy | scratchpad only; not committed to the repo |
| Primary extraction | pymupdf (`fitz`), page-by-page `get_text()` — 24 pages, 82,954 characters |
| Pages read | **all 24** (main text 1–11, references 11–15, Appendix A supplementary results 16, Appendix B proofs 16–20, Appendix C implementation + judge prompt templates 21–24) |
| Table verification | Tables 1–4 re-extracted in pymupdf `blocks` mode to confirm column order against the caption and the surrounding prose; the bolding described in each caption matches the extracted maxima, and §6.3 prose ("close second place for length-controlled AlpacaEval") independently confirms the AlpacaEval column assignment |
| Figure 2 verification | numbers are not in the text layer; recovered two ways — (a) vector marker coordinates pulled from the page drawing paths and mapped through the axis tick positions, (b) the figure region rendered at 300 dpi and read directly. Both agree |
| Figure 3 verification | win-rate matrix read from the text layer (row-major, diagonal omitted) and cross-checked against §6.2 prose ("roughly 2/3" vs RLCF → 0.68; "roughly 3/4" vs base → 0.73) |
| Absence checks | *GARP, Afriat, CCEI, revealed preference, rationalizab-, acyclic, Samuelson, Houtman, money pump* — zero hits under all three of: raw pymupdf text, NFKD-normalised text (ligature-safe), and an independent extractor in `-layout` mode. The four *varian* hits are substring matches inside "variance"/"variant"/"variational", not the economist |
| Tooling note | fetched with `curl` per instruction; the vault fetch tool was deliberately not used (concurrent sibling agents, shared SQLite) |
