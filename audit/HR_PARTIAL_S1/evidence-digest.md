# Evidence digest

Load-bearing claims with verbatim support, extracted from 68 per-source claims files (308 claims,
268 passing the confidence/evidence filter). Ranked by presence of numbers and confidence, capped
and grouped by atomic item. **This is an evidence index, not a narrative.**

Steps 3's consensus-claims and contradiction-graph artefacts were not produced (see
`audit/HR_PARTIAL_S1/PIPELINE_SUBSTITUTION_MAP.md`); their role is filled by
`research/temp/source-tensions.json`, which the drafters read separately.

### Atomic item: Interventions that REPAIR at inference time

- The paper's only intervention on agent outputs is selective prediction (abstaining unless k=3 repeated runs agree), which raises accuracy to 87-88% at 54-62% coverage, a 6-14 percentage-point gain over single-run baselines -- this is an abstention/filtering mechanism, not a repair that makes the agent's choices more internally consistent. (empirical)
  - numbers: 87-88% accuracy, 54-62% coverage, 6-14pp gain, k=3
  > Exploiting this signal, selective prediction (answering only when k=3 runs agree) achieves 87-88% accuracy at 54-62% coverage, a 6-14pp gain over single-run baselines, and matches a split-conformal baseline without a held-out calibration set.
  [260211619-when-agents-disagree-with-themselves-behavioral-consistency-as-an-unce]

- GRPO alignment on top of SFT actively repairs structural (transitivity) inconsistencies rather than merely suppressing predictions to inflate a consistency score, evidenced by a 26.5% reduction in raw transitivity-violation counts while the number of transitivity-relevant extracted triples stays nearly constant. (empirical)
  - numbers: 1327->976 transitivity violations (-26.5%), 1667 vs 1588 transitivity-relevant triples
  > GRPO substantially reduces transitivity violations specifically: for Qwen3-8B, GRPO reduces transitivity violations from 1327 to 976 — a 26.5% reduction — while the number of transitivity-relevant triples extracted remains nearly constant (1667 vs. 1588). This pattern indicates that GRPO is actively repairing structural inconsistencies rather than suppressing predictions to artificially raise Cons.
  [consistre-a-unified-consistency-aware-framework-for-document-level-relation-extr]

- In an expanded GPT-4o World-Cup-prediction experiment with ~27 countries and pairwise disjunctive probability queries, the LLM's raw stated atomic probabilities summed to 2.121 (grossly incoherent), while the quadratic-program-repaired probabilities summed to exactly 1 by construction, demonstrating the correction mechanically restores coherence. (empirical)
  - numbers: 2.121, 1.0
  > By design, the probabilities outputted by the quadratic program sum to 1, whereas the raw probabilities sum to 2.121 in this case, indicating that our approach solves this issue of incoherence over the sample space S.
  [dutch-books-and-money-pumps-rectifying-vulnerabilities-in-llms-through-rationali]

- Simple post-hoc normalization of raw judged probabilities to sum to 1 achieves near-zero incoherence (0.0021-0.0023) at only a small accuracy cost relative to raw judged probabilities, providing a cheap non-learned coherence-only baseline against which the more complex VAE method should be judged. (empirical)
  - numbers: 0.0023 train incoherence, 0.0021 test incoherence, r 0.7862/0.7091, MSE 0.0654/0.1007
  > P_judged (normalized) Train: 0.0023 incoherence, r=0.7862, MSE=0.0654; Test: 0.0021 incoherence, r=0.7091, MSE=0.1007
  [recovering-event-probabilities-from-large-language-model-embeddings-via-axiomati]

- Zhu, Yan & Griffiths construct LLM 'steering vectors' by aligning a behaviorally-elicited (MCMC-based) representation of risk preference with the model's internal neural (residual-stream) activations via Lasso regression, then apply the resulting vector to the residual stream at inference time to modulate risk-related behavior without any retraining or fine-tuning. (empirical)
  - numbers: 3,000 binary gamble choices, layers 39-41
  > These modifications to internal neural activations, a form of representation engineering, offer an effective and targeted means of influencing model behavior without retraining or fine-tuning the model.
  [steering-risk-preferences-in-large-language-models-by-aligning-behavioral-and-ne]

- In ablation, likelihood-aware aggregation alone reduces pairwise transitivity inconsistency to as low as 1.94% for Llama-3.1-70B and 2.83% for GPT-4o, down from a baseline of 20.26% observed for Llama-3.1-8B; a perplexity(PPL)-based tie-breaking variant achieves a 16.47-point absolute improvement for Llama-3.1-8B. (empirical)
  - numbers: 1.94%, 2.83%, 20.26%, 16.47%
  > The likelihood-aware aggregation strategy achieves the best results overall, reducing inconsistency to as low as 1.94% for Llama-3.1-70B and 2.83% for GPT-4o. The PPL-based comparison shows substantial gains over baseline (16.47% absolute improvement for Llama-3.1-8B).
  [trustjudge-inconsistencies-of-llm-as-a-judge-and-how-to-alleviate-them]

- Across 8 MT-Bench task categories and 3 judge models (24 category-judge cells), the non-transitivity ratio collapses on average from 18.74% under a two-pass baseline to 4.40% with likelihood-aware aggregation and 5.64% with the PPL-based method, with some cells reaching 0.00% and hard cases like Qwen-Math dropping from 32.85% to 4.46%. (empirical)
  - numbers: 18.74%, 4.40%, 5.64%, 0.00%, 32.85%, 4.46%
  > non-transitivity ratio collapses from 18.74% under the two-pass baseline to 4.40% with likelihood-aware aggregation method and 5.64% with the PPL-based method... with extremes such as Llama-STEM reaching 0.00%, and large cuts in difficult regimes like Qwen-Math (32.85% -> 4.46%).
  [trustjudge-inconsistencies-of-llm-as-a-judge-and-how-to-alleviate-them]

- Extended to a multi-dimensional evaluation setting (factuality, coherence, helpfulness), TrustJudge reduces per-dimension Conflict Ratio by 5.13-11.03 percentage points and non-transitivity ratios (NTR_k=3, NTR_k=4) by 11.23-24.99 percentage points on average, across Gemma-2-27B-it, Qwen2.5-32B-Instruct, and Llama-3.1-70B-Instruct judges. (empirical)
  - numbers: 5.13%, 11.03%, 11.23%, 24.99%
  > we observe drops on every model and on both of the metrics: CR decreases by roughly 5.13%-11.03%, while NTR3 and NTR4 fall more sharply, on average by 11.23%-24.99%.
  [trustjudge-inconsistencies-of-llm-as-a-judge-and-how-to-alleviate-them]

- TrustJudge's coherence-repair mechanism is model-agnostic, demonstrating consistent inconsistency reductions across multiple model families (Llama-3, GPT, Qwen, Gemma) and scales (3B to 70B parameters) without requiring judge retraining. (empirical)
  - numbers: 3B, 70B
  > Extensive experimental results across multiple model families (Llama-3, GPT, Qwen, Gemma) and scales (3B to 70B parameters) demonstrate TrustJudge's effectiveness.
  [trustjudge-inconsistencies-of-llm-as-a-judge-and-how-to-alleviate-them]

- POISE provably reduces training-corpus score-pair reversal conflicts from 20.15% to exactly 0%, whereas the prior inference-time probabilistic-aggregation baseline TrustJudge still retains 20.46% reversal conflicts on the same corpus. (empirical)
  - numbers: 20.15%, 0%, 20.46%
  > POISE provably reduces training-corpus score-pair reversal conflicts from 20.15% to exactly 0%, whereas TrustJudge still retains 20.46% reversal conflicts on the same training corpus.
  [trustroboreward-preference-ordered-isotonic-score-editing-for-multi-paradigm-rob]

- Cycle/transitivity conflicts within the pairwise preference labels themselves are not resolved algorithmically by POISE; they are corrected upstream by human expert re-annotation, and affect fewer than 1% of comparison groups. (empirical)
  - numbers: <1%
  > pairwise cycle/transitivity conflicts affect fewer than 1% of groups and are already repaired in pairwise-order preprocessing... come from pairwise-order repair (cycle/transitivity conflicts corrected by expert re-annotation.
  [trustroboreward-preference-ordered-isotonic-score-editing-for-multi-paradigm-rob]

- Combining the POISE-trained reward model with inference-time TrustJudge aggregation lifts overall reward-benchmark score to 78.57%, surpassing the proprietary GPT-5-mini teacher model. (empirical)
  - numbers: 78.57%
  > Combining our model with TrustJudge at inference time further lifts the overall score to 78.57%, surpassing the proprietary teacher.
  [trustroboreward-preference-ordered-isotonic-score-editing-for-multi-paradigm-rob]

- Isotonic-regression calibration, applied as a post-hoc inference-time correction to LLMs' raw elicited belief probabilities, fails to restore conditional-independence (belief-sufficiency) and often increases the measured violation magnitude, e.g. CMI for Heart/GPT-Min rises from 0.1454 (raw) to 0.3088 (isotonic-calibrated), and for Heart/GPT-High from 0.0753 to 0.3295. (empirical)
  - numbers: CMI 0.1454->0.3088 (Heart-GPT-Min), CMI 0.0753->0.3295 (Heart-GPT-High)
  > Across all datasets and models, the qualitative conclusions remain unchanged: conditional mutual information remains substantially greater than zero, indicating persistent violations of the conditional-independence null hypothesis... In many cases, isotonic calibration increases the estimated CMI magnitude... Consequently, monotonic post-hoc calibration methods such as isotonic regression are insufficient to restore 
  [when-agents-say-one-thing-and-do-another-validating-elicited-beliefs-from-llms]

- Echenique, Saito and Imai characterize, for any positive number e, exactly which choice-under-risk datasets have a rationalization within e (in beliefs, utility, or perceived prices) of expected utility theory, proposing e itself as a continuous measure of distance from EU rationality -- a measurement index, not an active repair/correction of the underlying choices. (theoretical)
  - numbers: e in (0, infinity)
  > For any positive number e, we give a characterization of the datasets with a rationalization that is within e (in beliefs, utility, or perceived prices) of expected utility theory. The number e can then be used as a measure of how far the data is to expected utility theory.
  [210206331-approximate-expected-utility-rationalization]

- A large-scale empirical evaluation of 14 different LLMs using the STEER framework characterizes current state-of-the-art economic rationality and shows model size affects models' ability to exhibit rational behavior. (empirical)
  - numbers: 14 LLMs evaluated
  > we describe the results of a large-scale empirical experiment with 14 different LLMs, characterizing the both current state of the art and the impact of different model sizes on models' ability to exhibit rational behavior.
  [240209552-steer-assessing-the-economic-rationality-of-large-language-models]

- The GARP-consistent synthetic training data is generated by Dirichlet-based rejection sampling that discards any candidate bundle violating GARP as checked by a depth-first search over the revealed-preference graph, licensed by Afriat's theorem (GARP-consistency iff rationalizable by a locally non-satiated utility function). (theoretical)
  - numbers: Dirichlet(1,1,1) budget shares, budget m=100, T=50 periods per agent
  > For each period the sampler draws a candidate bundle and accepts it only if adding it to the sequence does not create a GARP violation.
  [260323993-garp-efm-improving-foundation-models-with-revealed-preference-structur]


### Atomic item: Interventions that ENFORCE at training time

- RewardBench is a benchmark dataset of prompt-chosen-rejected trios spanning chat, reasoning, and safety, designed to evaluate reward models trained via direct MLE classification or implicit DPO-style reward modeling. (empirical)
  - numbers: 44 pages, 19 figures, 12 tables
  > we present RewardBench, a benchmark dataset and code-base for evaluation. The RewardBench dataset is a collection of prompt-chosen-rejected trios spanning chat, reasoning, and safety, to benchmark how reward models perform on challenging, structured and out-of-distribution queries.
  [240313787-rewardbench-evaluating-reward-models-for-language-modeling]

- GARP-EFM fine-tunes Amazon Chronos-2 (a transformer-based time-series foundation model) via LoRA on synthetic data generated by rejection sampling to be GARP-consistent, constituting a training-time intervention that enforces revealed-preference consistency in the model's learned representations rather than merely measuring it. (empirical)
  - numbers: 50,000 synthetic agents, LoRA rank 16, 5,000 training steps, learning rate 1e-5
  > We fine-tune Amazon Chronos-2, a transformer-based probabilistic time-series model, on synthetic data generated from utility-maximizing agents... The fine-tuned model serves as a rationality-constrained forecasting prior.
  [260323993-garp-efm-improving-foundation-models-with-revealed-preference-structur]

- Fine-tuning Chronos-2 on GARP-consistent synthetic data reduces out-of-sample bundle-prediction L2 error by 17-18% at forecast horizons H=5, 10, 15, and by 31% at H=1, relative to zero-shot Chronos-2, on a real N=154 consumer portfolio-choice panel. (empirical)
  - numbers: 17-18% error reduction (H=5,10,15), 31% error reduction (H=1), Bundle L2 20.53->14.09 at H=1, Bundle L2 16.83->13.92 at H=10
  > We show that fine-tuning on GARP-consistent synthetic data reduces bundle prediction error by 17-18% relative to zero-shot Chronos-2 at forecast horizons of H=5, 10, and 15 and by 31% at H=1.
  [260323993-garp-efm-improving-foundation-models-with-revealed-preference-structur]

- HRC consistently improves over both Bradley-Terry (BT) and GPM baselines on RewardBench 2, e.g. +1.23% on Gemma-2B-it, with particular strength in the Ties domain (complex non-strict preferences). (empirical)
  - numbers: +1.23%
  > Experiments on RewardBench 2 demonstrate that HRC consistently improves over both BT and GPM baselines (e.g., +1.23% on Gemma-2B-it). In particular, its superior performance in the Ties domain empirically validates the model's robustness in handling complex, non-strict preferences.
  [260517342-transitivity-meets-cyclicity-explicit-preference-decomposition-for-dyn]

- PROSPER does not cause significant regression on general capability/knowledge benchmarks relative to the base model, despite optimizing a more permissive (non-scalarized, intransitivity-tolerant) objective. (empirical)
  - numbers: Table 2 average: base 72.55, +RLCF 71.30, +PROSPER-JC 71.69, +PROSPER-VB 72.32, +PROSPER 71.70
  > PROSPER does not lead to significant model commonsense reasoning and general knowledge QA capability degradation at the 7B parameter scale.
  [back-to-blackwell-closing-the-loop-on-intransitivity-in-multi-objective-preferen]

- CONSISTRE's training-time track (Track B) distills teacher reasoning traces into small open models via SFT then aligns with GRPO using a composite reward that jointly optimizes extraction accuracy and relational consistency, producing large gains in both task performance and format validity. (empirical)
  - numbers: F1 0.031->0.330 (Qwen2.5-7B), F1 0.030->0.492 (Qwen3-8B), parse success 84.0%->99.5%
  > For Qwen2.5-7B, F1 increases from 0.031 for the base model to 0.330 after the full pipeline — a more than tenfold improvement — while the parse success rate rises from 84.0% to 99.5%. For Qwen3-8B, F1 increases from 0.030 to 0.492 under the identical pipeline, with the parse success rate reaching 99.5%.
  [consistre-a-unified-consistency-aware-framework-for-document-level-relation-extr]

- Nash-MD models with mixing parameter beta in {0.125, 0.25, 0.375} outperform all other tested models, including the Bradley-Terry RLHF baseline, on the held-out PaLM-2 evaluation preference model; Nash-MD beta=0.125 is the single top-performing model on both the training and evaluation preference models. (empirical)
  - numbers: beta=0.125, beta=0.25, beta=0.375, 10000 steps, tau=0.008
  > Nash-MD models with beta=0.125, beta=0.25, and beta=0.375 outperform all other models, including RLHF. Among them, Nash-MD with beta=0.125 (highlighted in bold as 'MD1') emerges as the top-performing model, surpassing all others in both the training preference model and the evaluation model.
  [nash-learning-from-human-feedback]

- The VAE-based coherence constraint is constructed at training time (trained once on a training set of LLM embeddings) and then applied with frozen weights at inference time to novel held-out prompts (480 test dice events, ~28% the size of the training set), without any fine-tuning of the underlying LLM. (empirical)
  - numbers: 480 test events, ~28%
  > Models that use LLM embeddings to predict event probabilities are trained exclusively on the training set, with model weights held fixed during evaluation on the test set.
  [recovering-event-probabilities-from-large-language-model-embeddings-via-axiomati]

- NashMD and EGPO baselines were excluded from the LLM-scale experiments because they were computationally prohibitive, estimated at roughly 10^3 GPU-hours per configuration, illustrating a practical cost barrier to deploying some coherence/equilibrium-based training-time interventions at LLM scale. (empirical)
  - numbers: ~10^3 GPU-hours per configuration
  > We also considered NashMD and EGPO, but did not include them in our experiments because their current implementations were prohibitively slow in our setting (we estimate on the order of 10^3 GPU-hours per configuration).
  [250519731-proximal-point-nash-learning-from-human-feedback]

- The paper proves the first last-iterate linear convergence guarantee for Optimistic Multiplicative Weights Update (OMWU) to a Nash equilibrium in NLHF, without regularization-induced bias and without requiring NE uniqueness, improving on Wei et al. (2020). (theoretical)
  - numbers: 28 pages
  > we provide the first convergence guarantee for Optimistic Multiplicative Weights Update (OMWU) in NLHF, showing that it achieves last-iterate linear convergence after a burn-in phase whenever an NE with full support exists...without requiring the assumption of NE uniqueness.
  [251224818-unregularized-linear-convergence-in-zero-sum-game-from-preference-feed]

- The proposed explicitly exploratory iterative NLHF algorithm achieves an O(sqrt(T)) regret bound without exponential dependence on the KL-regularization parameter, improvable to O(log(T)) with a minimax oracle. (theoretical)
  - numbers: O(sqrt(T)), O(log(T))
  > achieves an $O(\sqrt{T})$ regret bound without an exponential dependence on the KL-regularization parameter... the regret can be improved to $O(\log(T))$ with access to a minimax oracle.
  [260601382-efficient-exploration-for-iterative-nash-preference-optimization]

- Andrews proposes computing a continuous penalty equal to 1 minus the Critical Cost Efficiency Index (CCEI) from an LLM's own budget-set choices, via Afriat's theorem, and inserting this penalty directly into the model's training loss as a label-free regularizer. (theoretical)
  - numbers: CCEI penalty = 1-CCEI, 20 pages, arXiv:2608.05015v1
  > To use this approach in model training, one could present the model with a role and a budget constraint (prices and income), and ask it to allocate across goods. One could then vary prices and income, compute the CCEI of the resulting choices, and penalize 1-CCEI.
  [260805015-revealed-rationality-full-text]

- All three proposed penalties (Dutch-book magnitude, 1-CCEI, 1-e*_SEU) are continuous, piecewise-linear or polynomial-time computable via linear programming or binary search, and equal zero if and only if the corresponding representation theorem's axiom holds -- distinguishing this from binary pass/fail axiom tests. (theoretical)
  - numbers: CCEI computable via binary search over e in [0,1], polynomial time in atoms/events for Dutch book LP
  > The penalty is continuous, piecewise linear, bounded in [0, 1], and equals zero if and only if the data are rationalizable.
  [260805015-revealed-rationality-full-text]

- Andrews (arXiv:2608.05015) is, per a Semantic Scholar citation-graph check, the ONLY paper citing Chadwick, Kahng & Kipper (HAR 2025) as of the freeze date, and it explicitly characterizes their approach as post-hoc post-processing of model outputs, distinct in kind from its own proposed training-time regularization -- Andrews does not extend Chadwick et al.'s quadratic-program simplex/Kemeny-ranking projection mechanism itself, nor does it perform any ordering search or projection onto a GARP-consistent set; its GARP/Afriat instantiation only computes CCEI (a scalar measurement, via binary search + combinatorial GARP checks) and proposes using 1-CCEI as a training penalty. (theoretical)
  - numbers: citationCount: 1, CCEI computed via binary search, each step a GARP check
  > Many authors...have documented LLM rationality violations. As discussed above, some of these papers also discuss how such violations may be reduced, for instance through additional training steps...or through post-processing of model outputs as in Chadwick et al., 2025.
  [260805015-revealed-rationality-full-text]

- POISE (Preference-Ordered Isotonic Score Editing) is a training-time algorithmic intervention that corrects a VLM reward-model's pointwise scalar scores by projecting them onto the monotone cone defined by its own pairwise preference judgments, using the Pool-Adjacent-Violators Algorithm for isotonic regression. (theoretical)
  - numbers: 0%
  > it treats pairwise labels as a target partial order and projects raw pointwise scores onto the monotone cone of that order via the Pool-Adjacent-Violators Algorithm, provably reducing training-corpus score-pair reversal conflicts to exactly 0%.
  [trustroboreward-preference-ordered-isotonic-score-editing-for-multi-paradigm-rob]


### Atomic item: Measurement only — the contrast class

- A cross-benchmark validation on SWE-bench (50 tasks, 1,000 runs) preserves the consistency-accuracy hierarchy found on HotpotQA while revealing an approximately 8x spread in mean trajectory length across models, and bootstrap analysis shows single-run evaluations misrank models 29.3% of the time. (empirical)
  - numbers: 50 tasks, 1000 runs, 8x spread, 29.3% misranking
  > A cross-benchmark validation on SWE-bench (50 tasks, 1,000 runs) preserves the consistency hierarchy while revealing an ~8x spread in mean trajectory length across models, and bootstrap analysis shows single-run evaluations misrank models 29.3% of the time.
  [260211619-when-agents-disagree-with-themselves-behavioral-consistency-as-an-unce]

- Yamin et al. (2026) recover the cost/utility function that best rationalizes an LLM's decisions by fitting a discrete choice model to the LLM's elicited probability beliefs and observed choice, applied across four medical diagnosis domains and multiple frontier/open-source models. (empirical)
  - numbers: 4 medical diagnosis domains
  > we elicit the model's probability distribution over unknowns along with the choice it would make for the decision task and then fit a discrete choice model to recover the cost function that best rationalizes the model's decisions.
  [260508556-can-revealed-preferences-clarify-llm-alignment-and-steering]

- LLM-as-a-judge scores carry systematic errors including position bias, self-preference, and intransitivity that can strongly miscalibrate Bradley-Terry-derived Elo rankings, and propagating calibrated win probabilities instead of hard labels into the Bradley-Terry procedure brings LLM-derived Elo ratings within 17.9 Elo MAE of human-derived ratings on 55 held-out LMArena models. (empirical)
  - numbers: 17.9 Elo MAE, 55 held-out models
  > judge scores carry systematic errors - such as position bias, self-preference, or intransitivity - that can strongly miscalibrate the resulting rankings... bringing LLM-derived ratings within 17.9 Elo MAE of human-derived ones when averaged over 55 held-out models on LMArena.
  [260613221-from-uncertain-judgments-to-calibrated-rankings-conformal-elo-estimati]

- The 304 EcoAgent-Bench tasks are real-derived, adapted from GAIA, HotpotQA, and MuSiQue, spanning five task families and testing four decision types: avoiding unnecessary escalation, escalating when local evidence is insufficient, selecting a model tier, and stopping on unsupported premises. (empirical)
  - numbers: 304 tasks, 5 families, 4 decisions
  > Its 304 real-derived tasks span five families adapted from GAIA, HotpotQA, and MuSiQue, and test four decisions: avoiding unnecessary escalation, escalating when local evidence is insufficient, selecting a model tier, and stopping on unsupported premises.
  [260805519-ecoagent-bench-evaluating-economic-decision-making-in-budget-constrain]

- On downstream instruction-following and general-chat benchmarks, PROSPER (accepts intransitivity) outperforms both the scalarizing RLCF baseline and the PROSPER-JC ablation (which scalarizes the checklist into one aggregate judge score), with concrete Arena-Hard and AlpacaEval 2.0 numbers. (empirical)
  - numbers: Arena-Hard vanilla/style-controlled, AlpacaEval vanilla/length-controlled:, Qwen2.5-7B-Instruct base: 42.4 / 44.2 / 37.1 / 25.32, +RLCF: 42.5 / 43.9 / 41.4 / 17.24, +PROSPER-JC (scalarized ablation): 44.2 / 42.0 / 55.3 / 38.21, +PROSPER-VB (fixed-competitor ablation): 47.6 / 45.5 / 51.2 / 33.64, +PROSPER (full method): 49.2 / 46.1 / 55.4 / 37.61
  > PROSPER outperforms RLCF and the PROSPER-JC and PROSPER-VB ablations on Arena-Hard and Vanilla AlpacaEval and is a close second place for length-controlled AlpacaEval.
  [back-to-blackwell-closing-the-loop-on-intransitivity-in-multi-objective-preferen]

- Prompting a model with a target cost function produces LOWER behavioral consistency (Implied Loss-Function Consistency, ILFC) than the model's own unprompted baseline preferences or than supplying accurate probabilistic beliefs, for every model tested -- e.g. GPT5-High baseline ILFC 74.6%, true-probability ILFC 99.2%, elicited-probability ILFC 100.0%, but cost-function-prompted ILFC only 77.3%. (empirical)
  - numbers: 74.6%, 99.2%, 100.0%, 77.3%
  > GPT5-High 58.0% 57.9% 74.6% 99.2% 100.0% 77.3% ... Cost-function prompting produces moderately high consistency across models.
  [can-revealed-preferences-clarify-llm-alignment-and-steering]

- Self-reported cost ratios (asking the model to state its own cost weights) are the least consistent predictor of realized decisions across all four models, worse than baseline revealed preferences, indicating LLMs cannot faithfully verbalize their own operative decision objective. (empirical)
  - numbers: 24.2%, 28.0%, 58.0%, 57.9%, 54.8%, 60.4%, 41.2%, 32.4%
  > The revealed-preference estimates are substantially more consistent with behavior than self-reported costs: global and case-specific self-reports generally match realized decisions poorly, reinforcing that verbalized cost ratios are unreliable descriptions of the operative policy.
  [can-revealed-preferences-clarify-llm-alignment-and-steering]

- CONSISTRE's inference-time track (Track A) enforces transitivity, symmetry, and functional-uniqueness constraints on LLM-predicted relation triples via constraint-aware prompting, constraint-based verification, and iterative self-reflection, without any fine-tuning. (empirical)
  - numbers: F1=0.5433 (Gemini-2.5 Pro, 5-shot+CoT+Self-Reflection), F1=0.530 (GPT-5.2)
  > The first track operates at inference time for black-box LLMs, combining constraint-aware prompting, constraint-based verification, and iterative self-reflection to progressively refine predictions without requiring any task-specific fine-tuning.
  [consistre-a-unified-consistency-aware-framework-for-document-level-relation-extr]

- In a scanner-panel dataset of 494 households' food expenditures, 396 households (about 80%) violate GARP at least once, but the mean MPI is only about 6% of expenditure, and formal statistical testing cannot reject the null hypothesis of rational behavior under measurement error. (empirical)
  - numbers: 396, 494, 6%, $12.80, $213
  > 396 out of the 494 households in our data set violate GARP at some point. However, most of these violations are not severe: our MPI is centered around 6% of a household's food expenditures, or about $12.80 when evaluated at the average monthly food expenditure of $213.
  [money-pump-measure-revealed-preference-violations-echenique-lee-shum]

- Poor reliability of rationality indices is driven by a genuine lack of interindividual differences in rationality (most people are similarly consistent) rather than high measurement error, since within-subject coefficient of variation is low (median 15% for CCEI, 5% for HMI) for measurements with at least 20 trials. (statistical)
  - numbers: median WSCV 15% (CCEI), median WSCV 5% (HMI), trial threshold >=20
  > an analysis of the variance components in the data tentatively suggested that within-subject variance, as a proxy for measurement error, was sufficiently low for measurements with at least 20 trials... this tentatively suggests that the low reliability... was indeed driven by a lack of interindividual differences in rationality.
  [on-the-reliability-of-individual-economic-rationality-measurements-pmc]

- Fine-tuning Llama 3.1 8B Instruct with an explicit multi-term loss (structural utility-matching term plus auxiliary reflexivity, IIA/dispersion, mass, and smoothness invariance terms) is a training-time intervention that installs a principal-specified target risk preference into the model's weights and measurably improves the model's IIA and reflexivity diagnostic scores on held-out menus. (empirical)
  - numbers: baseline IIA 0.920 -> beta=0.0001 fine-tuned IIA 0.9484, beta=0.0045 fine-tuned IIA 0.8000, beta=0.0001 model: Complete 0.9961, Reflexive 0.9941, Continuity 0.9333, Monotonicity 1.0000, Transitive 1.0000, IIA 0.9484, beta=0.0045 model: Complete 0.9914, Reflexive 0.9870, Continuity 1.0000, Monotonicity 1.0000, Transitive 0.9583, IIA 0.8000, recovered beta_hat=0.000087 (SE 0.000003) vs target beta*=0.0001, recovered beta_hat=0.004560 vs target beta*=0.0045
  > Relative to the baseline Llama 3.1 (8B Instruct), both induced-preference models substantially improve completeness and reflexivity, with completeness above 0.99 and reflexivity above 0.98. Monotonicity remains perfect in both cases. The near risk-neutral target achieves perfect transitivity and raises IIA to 0.9484.
  [the-innate-economic-preferencesof-language-models]

- Revealed preference theory (GARP, Afriat's theorem) is applied to nearly 40 leading LLMs to test whether they exhibit approximately stable moral preferences, using a probabilistic rationality test -- this is a pure measurement/scoring application, with no correction or repair mechanism. (empirical)
  - numbers: 39 models, 5 dimensions, 161 rounds
  > we applied tools from revealed preference theory to nearly 40 leading LLMs, presenting each with many structured moral dilemmas spanning five foundational dimensions of ethical reasoning. Using a probabilistic rationality test, we found that at least one model from each major provider exhibited behavior consistent with approximately stable moral preferences.
  [the-moral-minds-of-large-language-models]

- Estimated single-peaked utility functions for the 7 models passing the 5% rationality test show ideal responses clustering near-neutral (2.5 on a 0-5 Likert scale), ranging from 2.2 to 3.06, with gpt-4-0125-preview the most utilitarian outlier. (empirical)
  - numbers: 2.5, 2.2, 3.06
  > most models express preferences close to neutral (2.5 on a 0-5 Likert scale), with estimated ideal responses ranging from 2.2 to 3.06.
  [the-moral-minds-of-large-language-models]

- A non-parametric permutation approach applied to 500 synthetic datasets finds pairwise model similarity (co-classification into the same GARP-consistent type) ranging from 24% to 48%, average ~30%, sd 14%, with Llama models as systematic outliers. (empirical)
  - numbers: 24%, 48%, 30%, 14%, 500 synthetic datasets
  > the similarity range from 24% to 48%, with an average of 30% and a standard deviation of 14%. The highest similarity is observed between Gemini-1.5-flash-exp-0827, Qwen1.5-110B-Chat, and open-mixtral-8x22b... The lowest similarity is found between GPT-4-0125-preview and Llama3.2-1b.
  [the-moral-minds-of-large-language-models]

- With Llama-3.1-70B-Instruct as judge, TrustJudge reduces Score-Comparison Inconsistency from 23.32% to 14.89% and Pairwise Transitivity Inconsistency from 15.22% to 4.40%, while simultaneously increasing exact-match evaluation accuracy against gold labels by 1.19-6.85% across model sizes. (empirical)
  - numbers: 23.32%, 14.89%, 8.43%, 15.22%, 4.40%, 10.82%, 1.19%, 6.85%
  > TrustJudge reduces Score-Comparison inconsistency by 8.43% (from 23.32% to 14.89%) and Pairwise Transitivity inconsistency by 10.82% (from 15.22% to 4.40%), while maintaining higher evaluation accuracy... exact match rates increasing by 1.19-6.85% across different model sizes.
  [trustjudge-inconsistencies-of-llm-as-a-judge-and-how-to-alleviate-them]

- A Qwen3-VL-4B reward model trained with POISE achieves an overall reward-benchmark score of 77.96%, nearly matching proprietary teacher GPT-5-mini (78.09%, a 0.13-point gap) and outperforming the strongest open RoboReward-4B baseline by 10.13 points, while raising test-time score-pair consistency to 71.90% versus 57.26% (RoboReward-4B) and 68.09% (GPT-5-mini). (empirical)
  - numbers: 77.96%, 78.09%, 0.13%, 10.13%, 71.90%, 57.26%, 68.09%
  > our model achieves an overall reward score of 77.96%, nearly matching the proprietary GPT-5-mini teacher (78.09%, a gap of only 0.13%) while outperforming the strongest open-source RoboReward-4B baseline by 10.13%.
  [trustroboreward-preference-ordered-isotonic-score-editing-for-multi-paradigm-rob]


### Atomic item: Which axiom system is targeted

- The round-robin + Bradley-Terry correction increases Spearman correlation with Chatbot Arena human-preference rankings from 95.0% to 96.4%, and Kendall correlation from 82.1% to 86.3%, relative to standard AlpacaEval. (empirical)
  - numbers: 95.0%, 96.4%, 82.1%, 86.3%
  > our method increases both the Spearman correlation and the Kendall correlation with Chatbot Arena (95.0% -> 96.4% and 82.1% -> 86.3% respectively).
  [1introduction]

- Running the same LLM agent on identical inputs yields 2.3-4.2 distinct action sequences per 10 runs, establishing run-to-run behavioral variance as a training-free, black-box uncertainty signal for agentic systems -- distinct from menu-dependent revealed-preference axioms like GARP/WARP. (empirical)
  - numbers: 2.3-4.2 distinct paths per 10 runs
  > Running the same LLM agent on identical inputs yields 2.3-4.2 distinct action sequences per 10 runs; this behavioral variance constitutes a training-free, black-box uncertainty signal that instantiates selective classification and distribution-free calibration for agentic systems.
  [260211619-when-agents-disagree-with-themselves-behavioral-consistency-as-an-unce]

- Individual consumer rationality level (CCEI, Afriat efficiency index) correlates positively but weakly (r=0.456) with the bundle-fitness gain from the GARP-consistency training intervention; exact GARP-passers have mean bundle fitness 0.723 vs. 0.688 for non-passers, but CCEI is not reliable enough to use as a screening rule for when to apply the intervention. (statistical)
  - numbers: correlation r=0.456, mean fitness 0.723 (GARP passers) vs 0.688 (non-passers)
  > The correlation between CCEI and bundle fitness is 0.456. Exact GARP passers (20/154) have mean bundle fitness 0.723 versus 0.688 for the remaining consumers... the correlation is not high enough to make CCEI a reliable screening rule.
  [260323993-garp-efm-improving-foundation-models-with-revealed-preference-structur]

- An annotation study of 94 AI value-alignment research papers found that the majority do not explicitly define 'human values,' instead relying on preference elicitation (often binary choices) as an implicit stand-in for values. (empirical)
  - numbers: 94 papers
  > The majority do not define values, relying heavily on preferences as a stand in that runs the risk of reducing complex culturally situated concepts down to binary choices.
  [260810327-toward-a-theory-of-value-in-ai-alignment]

- On a text-summarization fine-tuning task evaluated with a PaLM-2-Large preference model, the Bradley-Terry-based RLHF baseline achieves a 99% win rate against the SFT starting policy, the highest win rate against SFT of any model tested. (empirical)
  - numbers: 99%
  > the RLHF baseline that we have built is a very strong baseline. It beats SFT with a win rate of 99% marking the highest win rate observed against SFT among all models when using the PaLM 2 preference model.
  [nash-learning-from-human-feedback]

- Independence of irrelevant alternatives (IIA) is the weakest revealed-preference axiom across 12 tested LLMs, ranging from 0.122 (Gemma 4 31B) to 0.920 (Llama 3.1 8B Instruct), while monotonicity and continuity are near-ceiling for nearly all models. (empirical)
  - numbers: IIA range 0.122-0.920, Llama 3.1 8B baseline: Complete 0.902, Reflexive 0.836, Continuity 1.000, Monotonicity 1.000, Transitive 0.994, IIA 0.920, Qwen 3 14B: 1.000/0.001/1.000/1.000/0.983/0.322, Gemma 4 31B: 1.000/0.000/1.000/1.000/0.968/0.122
  > independence of irrelevant alternatives is the weakest axiom across the entire subject pool... The index ranges from 0.122 for Gemma 4 to 0.920 for Llama 3.1 (8B Instruct), indicating that adding a strictly dominated third option systematically shifts the log-odds between the original pair.
  [the-innate-economic-preferencesof-language-models]

- Transitivity is high but not perfect across the 12 tested LLMs (ranging 0.957 to 1.000), indicating preference cycles among directional triads are rare but present even in frontier models. (empirical)
  - numbers: transitivity range 0.957-1.000
  > Transitivity is high throughout, ranging from 0.957 for Qwen 3 (8B) to 1.000 for Llama 3.1 (70B) and the OpenAI frontier models, implying that preference cycles are rare but not entirely absent among directional triads.
  [the-innate-economic-preferencesof-language-models]

- Among 39 LLMs tested, 2 pass the GARP-based rationality test at the 1% significance level, 5 additional at 5%, and 2 more at 10%; every major provider had at least one model passing at the 5% level. (empirical)
  - numbers: 39 models, 2 pass at 1%, 5 pass at 5%, 2 pass at 10%
  > Among the 39 models evaluated, two passed the test at the 1% significance level... while five additional models passed at the 5% level, and two more at the 10% level... Notably, each provider featured in our study had at least one model passing the rationality test at the 5% level.
  [the-moral-minds-of-large-language-models]

- Position bias is a contributing mechanism to non-transitivity: ambiguous instructions show significantly higher non-transitivity rates than consistent instructions, and with GPT-3.5-Turbo as judge over 96% of instructions are classified as ambiguous, indicating much stronger position bias than GPT-4-Turbo. (empirical)
  - numbers: 96%
  > We find that ambiguous instruction exhibits significantly higher non-transitivity rates compared to consistent instructions, suggesting position bias is indeed a contributing factor. Furthermore, when using GPT-3.5-Turbo as the judge, the proportion of ambiguous instructions exceeds 96%.
  [1introduction]

- The paper's non-transitivity measurement (soft non-transitivity degree, SNTD) is validated as non-random by repeating an ablation experiment 50 times over triplets extracted from the win-rate matrix and averaging the resulting degree of non-transitivity. (empirical)
  - numbers: 50 repetitions
  > To further verify that the observation of non-transitivity in the ablated setting is not merely due to randomness, we repeat this ablation experiment 50 times. We quantify the degree of soft non-transitivity in the win rate matrix.
  [1introduction]

- Afriat's Theorem (1967) establishes that a dataset can be thought of as generated by a consumer maximizing a continuous, increasing utility function if and only if it is free of revealed-preference cycles containing a strict relation -- this cycle-freeness property is GARP. (theoretical)
  - numbers: 1967
  > Afriat's Theorem (1967) states that a dataset can be thought of as being generated by a consumer maximizing a continuous and increasing utility function if and only if it is free of revealed preference cycles containing a strict relation. The latter property is often known by its acronym, GARP.
  [240508459-revealed-preference-and-revealed-preference-cycles-a-survey]

- A simple upper-bound algorithm compatible with off-the-shelf binary classifiers, proposed as an order-consistent alternative to Bradley-Terry reward modeling, is empirically evaluated across more than 12,000 experimental setups spanning 6 base LLMs, 2 datasets, and varying annotation quantity/quality/pairing designs. (empirical)
  - numbers: 12,000+ experimental setups, 6 base LLMs, 2 datasets
  > we propose a simple and straightforward upper-bound algorithm, compatible with off-the-shelf binary classifiers, as an alternative order-consistent reward modeling objective. To offer practical insights, we empirically evaluate the performance of these different reward modeling approaches across more than 12,000 experimental setups, using 6 base LLMs, 2 datasets, and diverse annotation designs.
  [241104991-rethinking-bradley-terry-models-in-preference-based-reward-modeling-fo]

- Under the Luce model (a general probabilistic preference model generalizing Bradley-Terry), Condorcet cycles exist with probability converging to one exponentially fast as the population of preferences grows, proving the impossibility of fully aligning diverse human preferences with a single scalar reward via RLHF. (theoretical)
  - numbers: probability -> 1 exponentially fast
  > we prove that Condorcet cycles exist with probability converging to one exponentially fast under a general probabilistic preference model called the Luce model, thereby demonstrating the impossibility of fully aligning human preferences using reward-based approaches such as reinforcement learning from human feedback.
  [250310990-statistical-impossibility-and-possibility-of-aligning-llms-with-human]

- The paper's synthetic ground-truth preference game (context-dependent low-rank bilinear preference P(y>y'|x)=sigma(A_yy' - A_y'y) for rank r>=2) is constructed to explicitly NOT admit a standard Bradley-Terry model, i.e. the training/evaluation setup is deliberately intransitive-by-construction. (theoretical)
  - numbers: r>=2
  > This type of dueling bandit instance is a generalization of a low-rank linear bandit problem. Notice that for any r >= 2 this problem does not admit a standard Bradley-Terry model.
  [250519731-proximal-point-nash-learning-from-human-feedback]

- A random-feasible-budget benchmark (Bronars 1987-style, drawing bundles uniformly from the budget simplex while ignoring all contextual/historical information) performs far worse than both zero-shot and GARP-tuned Chronos-2, with MASE values above 1 and Bundle L2 near 30, confirming both models exploit real information beyond budget-feasibility alone. (empirical)
  - numbers: Bundle L2 ~29.75-31.48 for random benchmark across horizons
  > We also include a random feasible-budget benchmark in the spirit of Bronars (1987)... MASE values above one confirm that it outperformed by the naïve random-walk baseline.
  [260323993-garp-efm-improving-foundation-models-with-revealed-preference-structur]

- An agent with cyclic/intransitive preferences (e.g., onions > pineapple > mushrooms > onions) can be induced to pay money to cycle back to its starting position (a 'money pump'), demonstrating a qualitatively self-defeating, dominated strategy that motivates the transitivity/coherence requirement. (theoretical)
  - numbers: $0.01 penny cost example
  > I end up with exactly the same slice of mushroom pizza I started with... and one penny poorer... By virtue of my incoherent preferences which cannot be given a consistent ordering, I have shot myself in the foot, done something self-defeating.
  [coherent-decisions-imply-consistent-utilities-ai-alignment-forum]


### Atomic item: Minimal-perturbation and the projection problem

- On real experimental consumer-choice datasets of 22-79 observations per subject, all of HMI, AVI and MCI compute in under 2 seconds on a standard desktop despite worst-case NP-hardness, because the MILP relaxations are tractable at empirically realistic problem sizes. (empirical)
  - numbers: 22-79 observations per subject, <1-2 seconds runtime
  > most of the goodness-of-fit measures can be computed in less than a second while no index takes more than 2 seconds
  [computing-revealed-preference-goodness-of-fit-measures-with-integer-programming]

- Demuynck & Rehbeck give a mixed-integer linear program (MILP) for the Houtman-Maks Index, Average Varian Index, and Dean-Martin Minimum Cost Index by replacing Afriat's cardinal utility/multiplier pair (U,λ) with ordinal levels u_t ∈ [0,1], which removes the bilinear λ·x product and keeps every constraint linear in utility numbers, prices, and quantities. (theoretical)
  - numbers: u_t in [0,1], binaries U_{t,v}
  > the inequalities (IP-1)-(IP-4) are linear in utility numbers, prices, and quantities.
  [computing-revealed-preference-goodness-of-fit-measures-with-integer-programming]

- The Houtman-Maks Index and the Average Varian Index are both NP-hard to compute, per Smeulders, Spieksma, Cherchye & De Rock (2014); the Dean-Martin Minimum Cost Index is likewise NP-hard. (theoretical)
  - numbers: NP-hard: HMI, AVI, MCI, P: Afriat efficiency index (CCEI)
  > Computing the HMI is an NP-hard problem [Smeulders, Spieksma, Cherchye, and De Rock, 2014], which means that there exists no polynomial time algorithm to compute this index (unless P = NP).
  [computing-revealed-preference-goodness-of-fit-measures-with-integer-programming]

- The paper's Average Price Error (APE, L1-norm price perturbation onto GARP) is fully worked out with an explicit MILP (Corollary 6, inequalities IP-15 through IP-19), but the parallel quantity-perturbation objective (Average Quantity Error, AQE) is only sketched in two sentences, with no inequalities, no MILP, no computation, and no complexity classification, and is absent from the paper's conclusion. (theoretical)
  - numbers: APE: fully worked, Corollary 6, IP-15 to IP-19, AQE: 2 sentences, 0 inequalities
  > Instead of measurement error on prices, we can conduct a similar setting for measurement error on quantities. For this, one needs to introduce variables q̃_t and define GARP consistency conditional on these bundles. The Average Quantity Error (AQE) would then consist of minimizing the mean of the errors ||q_t − q̃_t|| conditional on (p_t, q̃_t) satisfying GARP.
  [computing-revealed-preference-goodness-of-fit-measures-with-integer-programming]

- Shiozawa proposes an alternative goodness-of-fit index (SCCI, based on strongly-connected-component decomposition of the revealed-preference graph) that is provably computable in O(n^2) polynomial time, reinforcing that GARP-violation DETECTION/measurement is easy while COST-MINIMIZING relation-deletion REPAIR (MCI-style) is hard. (theoretical)
  - numbers: O(n^2)
  > This index has a natural interpretation: the ratio of the weight of GARP violation part of the data over the entire weight of revealed preference relation... it has a polynomial-time algorithm... Theorem 1. The SCCI has an O(n^2) algorithm.
  [note-on-the-goodness-of-fit-measure-for-garp-np-hardness-of-minimum-cost-index]


### Atomic item: Downstream decision quality and task performance after enforcement

- In a separate 20-model comparison using GPT-4-Turbo as judge, round-robin+BT ranking achieves a 4% increase in Spearman correlation and a 5.2% increase in Kendall correlation with Chatbot Arena versus AlpacaEval; with length-controlled debiasing applied to both methods, round-robin ranking still improves by 1.4% Spearman and 4.2% Kendall over length-controlled AlpacaEval. (empirical)
  - numbers: 4%, 5.2%, 1.4%, 4.2%, 20 models
  > our method achieves higher correlations, with a 4% increase in Spearman correlation and a 5.2% increase in Kendall correlation... our length-controlled round-robin ranking further improves correlations, with a 1.4% increase in Spearman correlation and a 4.2% increase in Kendall correlation compared to length-controlled AlpacaEval.
  [1introduction]

- In real LLM post-training on Gemma-3-4B, the practical Nash Prox algorithm (training-time intervention using LoRA rank 16) achieves statistically significant pairwise win rates over SFT (0.9433), Online IPO (0.5627), and Online DPO (0.5344) as judged by a separate Gemma3-27B-IT judge model, directly demonstrating a measured downstream task-performance effect of the coherence-related training intervention. (empirical)
  - numbers: win rate vs SFT: 0.9433 +/- 0.010, win rate vs Online IPO: 0.5627 +/- 0.017, win rate vs Online DPO: 0.5344 +/- 0.017
  > We observe that Nash Prox outperforms all the baselines... this regularization can be valuable.
  [250519731-proximal-point-nash-learning-from-human-feedback]

- RLCF is the only alignment method tested to improve performance on every one of five widely-studied benchmarks in the original paper, including a 4-point boost in hard satisfaction rate on FollowBench, a 6-point increase on InFoBench, and a 3-point rise in win rate on Arena-Hard for Qwen2.5-7B-Instruct. (empirical)
  - numbers: +4 points FollowBench hard satisfaction rate, +6 points InFoBench, +3 points Arena-Hard win rate
  > RLCF is the only method to improve performance on every benchmark, including a 4-point boost in hard satisfaction rate on FollowBench, a 6-point increase on InFoBench, and a 3-point rise in win rate on Arena-Hard.
  [250718624-checklists-are-better-than-reward-models-for-aligning-language-models]

- Reinforcement-learning training of Qwen3 thinking models on a forecasting task (OpenForesight dataset, with retrieval and an improved RL reward function) improves accuracy, calibration, AND consistency of predictions jointly, with calibration gains generalizing across benchmarks -- consistency improves as a byproduct of accuracy-oriented RL training, not as a directly targeted objective. (empirical)
  - numbers: 8B parameters
  > Our specialized model, OpenForecaster 8B, matches much larger proprietary models, with our training improving the accuracy, calibration, and consistency of predictions. We find calibration improvements from forecasting training generalize across popular benchmarks.
  [251225070-scaling-open-ended-reasoning-to-predict-the-future]

- Across 8,000 runs of four models on 200 HotpotQA questions, behaviorally consistent tasks (at most 2 unique action paths) achieve 82-87% accuracy while inconsistent tasks (4+ unique paths) achieve only 41-65% accuracy, a gap that survives controls for task difficulty -- a purely correlational finding, not the result of an enforced-coherence intervention. (empirical)
  - numbers: 82-87%, 41-65%, 8000 runs, 200 questions, 4 models
  > Across 8,000 runs of four models on 200 HotpotQA questions, consistent tasks (at most 2 unique paths) achieve 82-87% accuracy while inconsistent tasks (4 or more paths) achieve 41-65%, a gap that survives controls for task difficulty.
  [260211619-when-agents-disagree-with-themselves-behavioral-consistency-as-an-unce]

- The GARP-tuned model improves downstream bundle-fitness prediction accuracy even for real consumers who violate GARP themselves (only 20/154, ~13%, of real consumers satisfy GARP), though the improvement is not universal: it worsens prediction for 33/154 (~21%) of consumers. (empirical)
  - numbers: 121/154 consumers improved, 33/154 consumers worsened, 20/154 (13%) real consumers satisfy GARP exactly
  > The GARP model improves on zero-shot for 121 of 154 consumers... For 33 of the 154 (≈21%) consumers, the GARP model has lower bundle fitness than zero-shot.
  [260323993-garp-efm-improving-foundation-models-with-revealed-preference-structur]

- HRC+DSPPO with Gemma-2B-it as the base preference model achieves a peak length-controlled win-rate of 44.75% on AlpacaEval 2.0 and 46.8% on Arena-Hard-v0.1, significantly outperforming SPPO baselines trained with BT or GPM. (empirical)
  - numbers: 44.75%, 46.8%
  > Notably, when using Gemma-2B-it as the base preference model, HRC+DSPPO achieves a peak length-controlled win-rate of 44.75% on AlpacaEval 2.0 and 46.8% on Arena-Hard-v0.1, significantly outperforming SPPO baselines trained with BT or GPM.
  [260517342-transitivity-meets-cyclicity-explicit-preference-decomposition-for-dyn]

- S-SPPO achieves 52.19% win rate and 47.46% length-controlled win rate on AlpacaEval 2.0 with Llama-3-8B, without additional human-annotated preference data, avoiding the performance degradation seen in prior SPPO variants. (empirical)
  - numbers: 52.19% win rate, 47.46% length-controlled win rate
  > achieving 52.19% win rate and 47.46% length-controlled win rate on AlpacaEval 2.0 with Llama-3-8B, without using additional human-annotated preferences during training.
  [260601561-s-sppo-semantic-calibrated-self-play-preference-optimization]

- Tool-API LLM agents attain only 3.9-24.0% micro strict success and at most 7.3% economic-consistency, often stopping before warranted escalation or overspending on cheap tasks. (empirical)
  - numbers: 3.9%, 24.0%, 7.3%
  > Tool-API agents attain only 3.9-24.0% micro strict success (at most 7.3% economic consistency), often either stopping before warranted escalation or overspending on cheap tasks.
  [260805519-ecoagent-bench-evaluating-economic-decision-making-in-budget-constrain]

- PROSPER (accepting multi-objective intransitivity via MaxEntBW) outperforms RLCF, a baseline that scalarizes per-item LLM-judge checklist scores into a single reward using LLM-generated weights, in pairwise LLM-judge win rate roughly two-thirds of the time, and beats the base policy roughly three-quarters of the time. (empirical)
  - numbers: win rate vs base ~75%, win rate vs RLCF ~67%
  > PROSPER produces policies that generate responses preferred to the base policy responses roughly 3/4 of the time and the RLCF policy responses roughly 2/3 of the time.
  [back-to-blackwell-closing-the-loop-on-intransitivity-in-multi-objective-preferen]

- A high-powered poker-probability-judgment experiment finds a genuine positive coherence-accuracy correlation across individuals and expertise groups (novices, amateurs, experts), contrary to several prior null-result studies with medical doctors and professional economists. (empirical)
  - numbers: 25 of 30 unconfounded correlations significantly positive, 0.14 novices, 0.18 amateurs, 0.24 experts (95% CI 0.14-0.33)
  > We carry out a higher-power experiment involving poker probability judgments (and a formally analogous urn task), with groups of poker novices, occasional poker players, and poker experts, finding a positive relationship between coherence and accuracy both between groups and across individuals.
  [clarifying-the-relationship-between-coherence-and-accuracy-in-probability-judgme]

- Generic (non-constraint-aware) self-reflection baselines reduce F1 relative to a 5-shot base, whereas CONSISTRE's constraint-targeted consistency enforcement improves F1, showing that the direction of the coherence-to-performance relationship depends on whether the enforcement mechanism targets the violated axioms specifically. (empirical)
  - numbers: -0.06 to -0.08 macro F1 (generic reflection baselines), +0.117 macro F1 (CONSISTRE Track A)
  > all three generic reflection methods reduce F1 relative to the 5-shot Base, with macro F1 dropping by 0.06–0.08 ... The combined effect is a +0.117 macro F1 improvement over 5-shot Base on the same backbone, where none of the baselines achieves a positive gain, indicating that Track A's gains stem from the consistency formulation itself.
  [consistre-a-unified-consistency-aware-framework-for-document-level-relation-extr]

- Ablating the transitivity constraint from CONSISTRE's inference-time enforcement causes the largest F1 drop of any single constraint (-0.113, about -22%), identifying transitivity as the dominant contributor to the downstream-performance gain from consistency enforcement. (empirical)
  - numbers: -0.113 F1 (transitivity ablation), -22%
  > Transitivity is the dominant F1 contributor: disabling it drops F1 by 0.113
  [consistre-a-unified-consistency-aware-framework-for-document-level-relation-extr]

- A training-data ablation shows that more thorough gold-truth alignment of SFT data raises F1 but slightly lowers internal consistency at the SFT stage; subsequent GRPO resolves this apparent coherence/accuracy tradeoff by raising both F1 and consistency simultaneously, with the resulting consistency (0.727) exceeding even the raw teacher-trace baseline (0.707). (empirical)
  - numbers: F1 0.436->0.473 (gold-truth alignment), consistency 0.643->0.727 (post-GRPO), teacher baseline consistency 0.707, F1 0.473->0.492
  > after RL alignment on top of the full GT-aligned SFT checkpoint, consistency rises from 0.643 to 0.727 — exceeding even the raw teacher trace baseline (0.707) — while F1 simultaneously improves from 0.473 to 0.492. This validates the core two-stage design of Track B: SFT and GRPO are complementary.
  [consistre-a-unified-consistency-aware-framework-for-document-level-relation-extr]

- The best training-time (Track B) model, Qwen3-8B, reaches approximately 93% of the best inference-time (Track A) F1 score (GPT-5.2) and lags its consistency score by only 0.040, despite having roughly two orders of magnitude fewer parameters, indicating consistency-aware distillation plus RL can transfer both coherence and accuracy into much smaller local models. (empirical)
  - numbers: F1 0.492 (Qwen3-8B) vs 0.530 (GPT-5.2), 93%, Cons 0.719 vs 0.759, 0.040 gap
  > The best Qwen3-8B configuration achieves F1 = 0.492, which corresponds to approximately 93% of GPT-5.2's best Track A result. Equally striking is the consistency comparison: Qwen3-8B achieves Cons = 0.719, only 0.040 below Gemini-2.5 Pro's 0.759
  [consistre-a-unified-consistency-aware-framework-for-document-level-relation-extr]

- The paper does not evaluate whether its coherence/transitivity repair changes any downstream decision-quality or task-performance metric; the transitivity evaluation is confined to distance-to-Kemeny-ranking accuracy on synthetic (non-LLM) election distributions, and the probabilistic-coherence evaluation is confined to verifying the QP output sums to 1. (empirical)
  - numbers: n=10, n=25, n=50
  > To complement our theoretical results from the previous section, we aim to test how the various voting rules we study as well as their x-IMDC-u counterparts perform on synthetic data.
  [dutch-books-and-money-pumps-rectifying-vulnerabilities-in-llms-through-rationali]


### Atomic item: Reliability, power, and whether the measure can bear inference

- Divergence in agent action sequences concentrates at step 2 of the trajectory (50.5% of Llama tasks), and consistency-based metrics detect failures with AUROC 0.62-0.78. (empirical)
  - numbers: 50.5%, AUROC 0.62-0.78
  > Divergence concentrates at step 2 (50.5% of Llama tasks), and consistency metrics detect failures with AUROC 0.62-0.78.
  [260211619-when-agents-disagree-with-themselves-behavioral-consistency-as-an-unce]

- Across 8 independent datasets (>1,600 participants total) spanning social, food, risk, and ambiguity choice domains, both the CCEI (Afriat critical cost efficiency index) and the Houtman-Maks index (HMI) -- the two most prominent GARP-based rationality measures -- show moderate-to-poor test-retest and intermethod reliability by standard psychometric criteria (ICC). (empirical)
  - numbers: 8 datasets, >1,600 participants, ICC thresholds: <0.5 poor, 0.5-0.75 moderate, 0.75-0.9 good, >0.9 excellent
  > Drawing from multiple original and published datasets (in total over 1,600 participants), we unequivocally show that contemporary measurements of rationality have moderate to poor reliability according to common standards.
  [on-the-reliability-of-individual-economic-rationality-measurements-pmc]

- Specific ICC values: Study 1 intermethod reliability for CCEI = 0.071 and 0.356 (two measurements); HMI = 0.094 and 0.309. Study 2 (preregistered replication, N=148, 40 trials) intermethod ICC for CCEI = 0.408 and 0.372; HMI = 0.321 and 0.275 -- both still below the 0.5 poor-reliability threshold in most cases. (statistical)
  - numbers: CCEI ICC 0.071, 0.356 (Study 1), HMI ICC 0.094, 0.309 (Study 1), CCEI ICC 0.408, 0.372 (Study 2), HMI ICC 0.321, 0.275 (Study 2)
  > The intermethod reliability (between task versions) for the CCEI was ICC (2, 1) = 0.071... for the first measurement and ICC (2, 1) = 0.356... for the second measurement... the intermethod reliability of the CCEI was poor for both measurements.
  [on-the-reliability-of-individual-economic-rationality-measurements-pmc]

- Switching from multi-turn to single-turn dialogue administration (holding the model fixed) collapses CCEI for two open-source models but not two closed/larger models: Llama's CCEI drops from 0.953 to 0.841 (risk) and 0.968 to 0.756 (social); Qwen's drops from 0.980 to 0.739 (risk) and 0.994 to 0.889 (social), all p<0.01, while GPT and DeepSeek are essentially unaffected. (empirical)
  - numbers: 0.953, 0.841, 0.968, 0.756, 0.980, 0.739, 0.994, 0.889
  > when using the single-turn dialogue, the CCEI of Llama decreases from 0.953 to 0.841 in the risk preference and from 0.968 to 0.756 in the social preference; that of Qwen decreases from 0.980 to 0.739 in the risk preference and from 0.994 to 0.889 in the social preference (all p<0.01).
  [when-experimental-economics-meets-large-language-models-tactics-with-evidence]

- Switching from open-ended to multiple-choice answer format (same model, same budget-set task) drops CCEI significantly for Llama (0.953->0.853 risk, p<0.01; 0.968->0.936 social, p=0.033) and Qwen (0.980->0.902 risk; 0.994->0.916 social, both p<0.01), but not for GPT or DeepSeek. (empirical)
  - numbers: 0.853, 0.953, 0.936, 0.968, 0.902, 0.980, 0.916, 0.994
  > under the multiple-choice answer type, the average CCEI scores in both domains decrease significantly for Llama (risk: 0.853 vs. 0.953, p<0.01, social: 0.936 vs. 0.968, p=0.033) and Qwen (risk: 0.902 vs. 0.980, social: 0.916 vs. 0.994, both p<0.01).
  [when-experimental-economics-meets-large-language-models-tactics-with-evidence]

- In a small-scale empirical test on [vendor-assistant] (N=198) and GPT-4o (N=100), both models show agreement-following coexisting with low repair-quality on contested-value prompts, i.e. they frequently change stated positions without principled justification. (empirical)
  - numbers: N=198, N=100
  > a small-scale empirical illustration on two frontier RLHF-trained models ([vendor-assistant], N=198; GPT-4o, N=100) showing that, for both, agreement-following coexists with low repair-quality on contested-value prompts.
  [260514912-from-sycophantic-consensus-to-pluralistic-repair-why-ai-alignment-must]

- A Bayesian sampler model (limited mental samples, moderated toward 0.5 for small sample sizes) explains both the observed positive coherence-accuracy correlation in this study's data and the null results of prior studies, via a power analysis showing a prior null-result experiment (Wright et al. 1994 snooker forecasting) had only a 21% chance of detecting a significant correlation despite an underlying positive simulated correlation. (theoretical)
  - numbers: 21%
  > the chance of the experiment producing a significant correlation was only 21%.
  [clarifying-the-relationship-between-coherence-and-accuracy-in-probability-judgme]

- Naive linear pooling of an LLM's token-level probabilities across multiple mutually exclusive events does not reliably improve coherence and can make it worse than the LLM's originally stated (already coherent) probabilities, motivating the more involved normalization/QP-based repair. (empirical)
  - numbers: P(A)=0.10 vs pooled 0.1131, P(B)=0.05 vs pooled 0.0579, P(A∪B)=0.15 vs pooled 0.1489
  > In our experiments, we found that not only did taking expected probabilities of events not improve coherence, but there were cases where the expected probabilities over tokens were even less coherent than the originally outputted probabilities.
  [dutch-books-and-money-pumps-rectifying-vulnerabilities-in-llms-through-rationali]

- All four LLMs' baseline CCEI distributions are significantly higher than a simulated-random-choice CCEI distribution (p<0.01), confirming the budget-set task design has adequate power to detect GARP violations (a Bronars-style power check) before any reliability comparison is made. (statistical)
  - numbers: 100 simulated agents, p<0.01
  > The simulated CCEI is significantly lower than all four LLMs in both preference domains (all p<0.01).
  [when-experimental-economics-meets-large-language-models-tactics-with-evidence]


### Atomic item: Economics front — Afriat / Varian / Houtman-Maks machinery

- Cook, Kazinnik, Modig & Palmer test LLM choice rationalizability under the McCall job-search model using a formal three-criterion procedure (BIC-selected switching regime, correct step direction, trembling-hand error under 50%) and find that larger models are rationalizable far more often than smaller ones, with the smallest model (Mistral v0.3 7B) essentially not rationalizable at all. (empirical)
  - numbers: estimated beta clusters between 0.2 and 0.8, within-model beta SD of 0.2-0.3, trembling-hand error threshold 50%
  > To summarize, large models are rationalizable within the McCall framework, while the smallest model is not rationalizable at all.
  [what-do-llms-want-feds-2026-006-full-text]

- For a fixed LLM (GPT-4o, DeepSeek-V3, Llama-3.1-8B, Qwen2.5-7B), CCEI computed across 100 independently re-run simulations of the same 25-round budget-set task yields a full distribution rather than a fixed point, with mean CCEI of 1.000/0.994 (GPT), 1.000/0.999 (DeepSeek), 0.953/0.968 (Llama), 0.980/0.994 (Qwen) in risk/social domains. (empirical)
  - numbers: 1.000, 0.994, 0.953, 0.968, 0.980, 100 simulations, 25 rounds
  > The average CCEI scores of GPT, DeepSeek, Llama, and Qwen are 1.000, 1.000, 0.953, and 0.980 in the risk preference domain, and 0.994, 0.999, 0.968, and 0.994 in the social preference domain.
  [when-experimental-economics-meets-large-language-models-tactics-with-evidence]

- Applying the approximate-EU-rationalization methodology to three large-scale human experiments, many subjects are consistent with plain utility maximization but not with expected-utility maximization specifically, and the measured distance-to-EU correlates with subjects' demographic characteristics. (empirical)
  - numbers: 3 large-scale experiments
  > Many subjects in those experiments are consistent with utility maximization, but not with expected utility maximization. Our measure of distance to expected utility is correlated with subjects' demographic characteristics.
  [210206331-approximate-expected-utility-rationalization]

- Lanier, Polisson & Quah (2026) prove that the maximum money-pump profit extractable from a consumer's choice data equals both the minimum overpayment needed to rationalize the consumer's targets and the minimum wasted quasilinear utility, minimized over all candidate utility functions, via a novel connection to optimal transport theory. (theoretical)
  - numbers: arXiv:2404.04843v3
  > We show that the amount of money which can be pumped by an arbitrageur is equal to both (i) the minimum amount of money which the consumer overpays to attain his utility targets (minimum over all utility functions) and (ii) the minimum amount of wasted quasilinear utility (minimum again over all utility functions).
  [revealed-preference-with-optimal-transport-money-pumps-bounded-rationality-and-p]

- Temperature settings between 0 and 1 do not significantly affect CCEI/economic rationality for any of the four LLMs tested. (empirical)
  - numbers: temperature 0-1
  > temperature settings between 0 and 1 (Tactic 1) do not affect the rationality of any of the four LLMs.
  [when-experimental-economics-meets-large-language-models-tactics-with-evidence]


### Atomic item: ML/alignment front — coherence theorems and Nash learning

- In a downstream reward-guided embodied policy optimization test on PAIBench-G robot manipulation tasks, the POISE-trained reward model wins approximately 69% of 68 head-to-head paired comparisons against RoboReward-4B (judged by 3 human annotators via majority vote), producing more accurate grasping and more stable object placement. (empirical)
  - numbers: 69%, 68 paired comparisons, 3 annotators
  > We conduct a head-to-head comparison between our 4B reward model and RoboReward-4B over 68 paired comparisons, judged by 3 annotators with majority vote. Our method achieves approximately 69% win rate against RoboReward-4B, demonstrating that our reward model provides a better optimization signal for embodied task completion.
  [trustroboreward-preference-ordered-isotonic-score-editing-for-multi-paradigm-rob]

- Standard post-training alignment methods, including Nash learning from human feedback (NLHF), fundamentally underutilize test-time scaling because their resulting policies collapse to a single majority-preferred (often near-deterministic) response, destroying the output diversity needed for repeated sampling to help; even though NLHF is optimal for k=1, sampling k>1 times from it cannot guarantee win rates above 1/2 except by an arbitrarily small margin. (theoretical)
  - numbers: k=1, win rate > 1/2
  > We show that popular post-training methods, including Nash learning from human feedback (NLHF), can fundamentally underutilize the benefits of test-time scaling. Even though NLHF is optimal for k=1, sampling from the resulting (often deterministic) policy cannot guarantee win rates above 1/2 except for an arbitrarily small slack. This stems from a lack of output diversity: existing alignment methods can collapse to a
  [260108777-asymptotic-universal-alignment-a-new-alignment-framework-via-test-time]

- A family of symmetric multi-player alignment games is proposed whose symmetric Nash-equilibrium policies achieve the provably optimal (k, k/(k+1))-robust alignment rate, preserving output diversity where NLHF-style methods do not, with proven self-play convergence guarantees. (theoretical)
  - numbers: f(k) = k/(k+1)
  > we propose a family of symmetric multi-player alignment games and prove that any symmetric Nash equilibrium policy of the (k+1)-player alignment game achieves the optimal (k, k/(k+1))-robust alignment. Finally, we provide theoretical convergence guarantees for self-play learning dynamics in these games.
  [260108777-asymptotic-universal-alignment-a-new-alignment-framework-via-test-time]

- Best-Response against self-play (BR), despite being explicitly trained to beat self-play, scores only 94% against self-play and performs poorly against RLHF and Nash-based approaches, a pattern the authors attribute to 'preference hacking' (overfitting to the fixed SFT policy). (empirical)
  - numbers: 94%
  > Best-response against self-play (BR) does not exhibit strong performance... its evaluation yields a relatively modest score of 94% against self-play... This suggests the possibility of 'preference hacking,' where BR may be overly adapting to the preference model by overfitting to the specific SFT policy.
  [nash-learning-from-human-feedback]


### Atomic item: Framing, persona, and where the headroom is

- When LLMs are prompted to adopt an explicit target cost function, a substantial minority of steering attempts move the model's implied preferences in the wrong direction entirely: 27.1% for DeepSeek, 25.0% for GPT5-Minimal, 14.6% for Llama, 12.5% for GPT5-High. (empirical)
  - numbers: 27.1%, 25.0%, 14.6%, 12.5%
  > Table 1: Direction of utility steering by model. ... DeepSeek 27.1% Wrong ... GPT5-High 12.5% Wrong ... Llama 14.6% Wrong ... GPT5-Minimal 25.0% Wrong
  [can-revealed-preferences-clarify-llm-alignment-and-steering]

- Only 14.6% to 31.2% of prompted steering attempts land 'approximately on target' (within 80-120% of the way from baseline to the specified cost function), and GPT5-Minimal undershoots the target in 47.9% of cases. (empirical)
  - numbers: 14.6%-31.2% on target, 47.9% undershoot (GPT5-Minimal)
  > Across supplied cost functions, the implied FN/FP and Defer/FP ratios usually move in the correct direction relative to baseline, so explicit cost information can guide behavior. But the movement is highly heterogeneous: some cases move partway, some nearly reach the target, some overshoot, and a non-trivial minority move in the wrong direction.
  [can-revealed-preferences-clarify-llm-alignment-and-steering]

- A suite of frontier LLMs (GPT-4o, GPT-4-Turbo, Llama-3-8B/70B, [vendor-assistant]Opus) predict and simulate human risky-choice decisions as systematically more rational (closer to expected-value maximization) than humans actually behave, and this over-rationality assumption strengthens with model capability under chain-of-thought prompting. (empirical)
  - numbers: human r=0.48, Llama3-8B r=0.57 MSE=0.22, Llama3-70B r=0.80 MSE=0.10, [vendor-assistant]Opus r=0.76 MSE=0.12, GPT-4-Turbo r=0.93 MSE=0.03, GPT-4o r=0.94 MSE=0.02
  > these models deviate from human behavior and align more closely with a classic model of rational choice — expected value theory.
  [large-language-models-assume-people-are-more-rational-than-we-really-are]

- An inference-time 'control vector' intervention (activation-steering along a difference vector computed from contrasting-pair prompts, per Cook & Kazinnik 2025 / Zou et al. 2023) reliably shifts LLM dictator-game allocations along a self-interest-vs-fairness axis, but is markedly less effective and inconsistent across models in the more complex McCall search setting. (empirical)
  - numbers: control-vector coefficient s pushes Phi 4 patience beta up to approximately 0.85 under steering, still below human patience norms
  > Interventions such as prompt framing (e.g., masking social context) and control vectors reliably shift models toward more payoff-maximizing behavior, while persona-based prompting has more limited impact.
  [what-do-llms-want-feds-2026-006-full-text]

- Persona assignment (demographic/occupational) does not significantly affect any of the four LLMs' economic rationality (CCEI), with an overall sensitivity score of 0. (empirical)
  - numbers: lambda(S)=0, 14 conditions, p>0.1
  > The results show that the rationality of all four models is not significantly influenced by the persona (all p>0.1), leading to a sensitivity score lambda(S) of 0.
  [when-experimental-economics-meets-large-language-models-tactics-with-evidence]


### Ungrouped

- Applied to US grocery scanner data, the method reveals a joint-rationality gap of 0.62 between near-saturated pairwise compatibility and population-level co-typing; binary lottery data yield a comparable gap of 0.38.
  > Applied to US grocery scanner data, the construction reveals a joint-rationality gap of 0.62 between near-saturated pairwise compatibility and population-level co-typing; binary lottery data yield a comparable gap of 0.38.
  [250113721-measuring-hidden-consumer-heterogeneity-with-revealed-preferences]

- A threshold-crossing budget sweep changes GPT-5.4's escalation rate from 0% to only 3%, indicating near-total insensitivity to the budget signal that should rationally govern the escalation decision.
  > A threshold-crossing budget sweep changes GPT-5.4's escalation rate from 0% to only 3%.
  [260805519-ecoagent-bench-evaluating-economic-decision-making-in-budget-constrain]

- On the training set, axiomatically-recovered probabilities strictly dominate raw judged (elicited) probabilities on both coherence and accuracy: incoherence falls from 0.1297 to 0.0227, Pearson r rises from 0.8032 to 0.8264, and MSE falls from 0.0601 to 0.0587.
  > P_judged 0.1297 ([0.1218, 0.1376]) r=0.8032 (p<.01) MSE=0.0601 ... P_recovered 0.0227 ([0.0211, 0.0243]) r=0.8264 (p<.01) MSE=0.0587
  [recovering-event-probabilities-from-large-language-model-embeddings-via-axiomati]

- On the held-out test set, axiomatically-recovered probabilities are far more coherent than raw judged probabilities (incoherence 0.0383 vs 0.1366) and marginally more correlated with true probabilities (Pearson r 0.7328 vs 0.7286), but have slightly WORSE mean squared error against the true probabilities (MSE 0.1014 vs 0.0927) -- a mixed, not unambiguous, accuracy result under generalization.
  > Test P_judged 0.1366 ([0.1190, 0.1542]) r=0.7286 (p<.01) MSE=0.0927 ... P_recovered 0.0383 ([0.0314, 0.0452]) r=0.7328 (p<.01) MSE=0.1014
  [recovering-event-probabilities-from-large-language-model-embeddings-via-axiomati]

- An ablated VAE lacking the axiomatic latent-structure constraint performs worse on both coherence and accuracy than the full constrained method on both train and test sets, indicating the axiom-imposition step itself (not merely the VAE architecture) is responsible for the accuracy/coherence gains.
  > P_recovered^a [ablated] Train: 0.2948 incoherence, r=0.7610, MSE=0.0750; Test: 0.3457 incoherence, r=0.7167, MSE=0.1140
  [recovering-event-probabilities-from-large-language-model-embeddings-via-axiomati]

- A supervised linear probe trained directly on true-probability labels achieves near-perfect training performance but catastrophically fails to generalize (negative Pearson correlation and high incoherence on the test set), demonstrating that unsupervised axiom-constrained learning generalizes better than naive supervised probing despite using no ground-truth labels.
  > P_probe Train: 0.0006 incoherence, r=1.0, MSE<0.0001; Test: 0.8535 incoherence, r=-0.1328, MSE=0.4654
  [recovering-event-probabilities-from-large-language-model-embeddings-via-axiomati]

- Yamin et al. (2026a), 'When agents say one thing and do another: Validating elicited beliefs from LLMs' (arXiv:2602.06286), finds that LLMs' stated probability beliefs do not fully explain (are not decision-sufficient for) the models' own choices -- a measurement-only finding of belief-choice incoherence, cited by Andrews as motivation but not itself proposing a repair.
  > Yamin et al., 2026a elicit probability estimates from LLMs in decision tasks and test whether these beliefs satisfy properties required of a rational decision-maker, including decision-sufficiency... They find violations, suggesting that LLM [reported probabilities do not form a fully coherent basis for the decisions the models actually make].
  [260805015-revealed-rationality-full-text]

- The economic-consistency score is defined as the worse of accuracy on upgrade-oriented and save-oriented task family groups, specifically to expose one-sided policies that micro-averaged accuracy rewards.
  > Micro-averaged accuracy rewards one-sided policies: always-escalate controls achieve high micro success while failing save-oriented tasks. We therefore also report an economic-consistency score (the worse of accuracy on upgrade-oriented and save-oriented family groups) which exposes this failure.
  [260805519-ecoagent-bench-evaluating-economic-decision-making-in-budget-constrain]

> **Redaction note.** One vendor's assistant-family name has been replaced with `[vendor-assistant]` in this audit copy wherever it appeared as the *name of a model studied by a cited paper*. The redaction is mechanical, applies only to the committed copy, and preserves every number, sample size and finding. The unredacted file remains in the gitignored working vault. The hygiene guard cannot distinguish a cited paper's experimental subject from an attribution string, so the conservative action is taken here rather than weakening the guard.
