# Pilot results

Run 2026-08-26 against `docs/PILOT_PROTOCOL.md`. **Zero cost** — all inference on locally-hosted
open-weight models via ollama on an M1 MacBook Air. No commercial endpoint was contacted and no free
tier was used.

100 sessions attempted: 2 models × 2 framings × 25 seeds, 25 budget-set rounds each.

---

## 0. Instrument validation, done before any model was queried

| Check | Result | Reference |
|---|---|---|
| CCEI on a Cobb–Douglas rationalisable sequence | **1.0000** | expect exactly 1 |
| CCEI on an analytically derived strict 2-cycle | **0.9000** | derived closed-form as 0.90 |
| Lemma-1 tie case detected | GARP=False, CCEI=0.9999990, `exact_ties=1` | `docs/METHOD_NOTE_Q6.md` |
| **Bronars power of the budget sets** | **1.0000** | E4 reports ≈0.999 at K=2, n=25 |
| Mean random-agent CCEI | **0.7406** | E4 replication ≈0.72 |
| Budget-line pairs intersecting | **60.0%** | E3 reports 58.1% |
| Exact budget ties under continuous prices | **0** | trap disarmed |

The instrument reproduces the published design's properties and can fail: a uniform-random agent scores
0.7406 and violates GARP 100% of the time.

## 1. Headline table

Predictive success is Selten's `m = pass rate − (1 − power)`; with power = 1.0000 it equals the pass rate.

| Model | Framing | n kept | mean CCEI | SD | WSCV | min | max | GARP pass | m |
|---|---|---|---|---|---|---|---|---|---|
| llama3.2:3b | baseline | 25 | **0.9919** | 0.0195 | **2.0%** | 0.9358 | 1.0000 | 0.76 | 0.760 |
| llama3.2:3b | reciprocal | 23 | 0.9491 | 0.0528 | 5.6% | 0.8511 | 1.0000 | **0.17** | 0.174 |
| qwen2.5:1.5b | baseline | 22 | 0.9262 | **0.1367** | **14.8%** | **0.4315** | 1.0000 | 0.27 | 0.273 |
| qwen2.5:1.5b | reciprocal | 12 | 0.9431 | 0.0836 | 8.9% | 0.7186 | 1.0000 | 0.42 | 0.417 |

## 2. Precondition 1 — stable per-model CCEI across re-runs

**Verdict: SPLITS BY SCALE. Holds decisively for the 3B model, fails decisively for the 1.5B model.**

Comparison band, from Nitsch et al. (*PNAS* 2022) on humans: WSCV ≈ 15% for CCEI; ICC 0.071–0.685 with
none reaching the conventional "good" threshold of 0.75.

| Model | WSCV | 95% CI (bootstrap, 4000 resamples) | Against the human band |
|---|---|---|---|
| **llama3.2:3b** | **2.0%** | [0.4%, 2.7%] | **~7× more stable than humans.** CI excludes 15% entirely. |
| **qwen2.5:1.5b** | **14.8%** | [3.0%, 23.5%] | **Statistically indistinguishable from humans.** CI straddles 15%. |

**ICC(1,1), model-as-subject, baseline framing, 2 models: 0.1654** — inside Nitsch's human band. That
means run-to-run noise is large relative to the gap between these two models: a single session's CCEI
cannot reliably tell them apart. **This estimator is underpowered at two subjects and is reported with
that caveat rather than leaned on.** The per-model WSCVs above are the load-bearing statistic.

Two further facts about the 1.5B model's instability: its CCEI range across *identical* re-runs is
**0.4315 to 1.0000**, and **2 of 22 sessions fall below the random-agent benchmark of 0.7406** — i.e. on
those runs it was less consistent than uniform-random choice.

## 3. Precondition 2 — framing-induced headroom

**Verdict: HOLDS for the 3B model on the violation-count metric, and is CONFOUNDED for the 1.5B model.**

| Model | baseline → reciprocal (CCEI) | Δ | p | GARP pass rate |
|---|---|---|---|---|
| llama3.2:3b | 0.9919 → 0.9491 | **−0.0428** | **0.0010** | **0.76 → 0.17** |
| qwen2.5:1.5b | 0.9262 → 0.9431 | +0.0169 | 0.66 | 0.27 → 0.42 |

**The 3B result is the clean one, and the CCEI understates it.** Mean CCEI falls only 0.043, but the
**GARP pass rate collapses from 0.76 to 0.17 — a 59-percentage-point drop**. This is exactly the
near-1 compression E3 warned about: CCEI is a poor guide to how much violation is present, because the
index is squeezed near the top of its range. Reporting CCEI alone would have made a large behavioural
change look negligible. **Any future work here must report violation counts alongside the index.**

**The 1.5B result cannot be read as a null, because of a selection effect large enough to invalidate
it.** Under reciprocal framing the model failed the output-format contract in **52% of sessions**
(13 of 25 discarded; median valid rounds fell from 24 to 16). The 12 surviving sessions are precisely
those where the model coped with the harder framing — a selected, non-random subsample. The +0.0169
"improvement" is almost certainly survivorship, not an effect.

**That discard rate is itself the most interesting result in the pilot.** At 1.5B, the reciprocal
framing's effect did not show up as measurable incoherence — it showed up as **task breakdown**. The
manipulation had a large effect on the model; the effect simply was not of the kind CCEI can score. A
revealed-preference instrument silently drops exactly the observations where the agent was most
disrupted, which biases the measured effect toward zero.

## 4. Does the flip-to-NO condition fire?

The stop rule fixed in advance: *fires if the ICC-equivalent falls inside or below the human band
(≤ 0.685) for **both** models.*

**It fires for one model and not the other. Stated plainly: PARTIAL FIRE, split on scale.**

- **qwen2.5:1.5b — FIRES.** WSCV 14.8%, CI straddling the human 15%, range 0.43–1.00 across identical
  re-runs, two sessions below the random benchmark. At this scale the dose variable is noise and a
  projection operator would be repairing sampling variation.
- **llama3.2:3b — DOES NOT FIRE.** WSCV 2.0% with a CI excluding 15% by a wide margin. At this scale
  CCEI is a stable per-model quantity and a graded dose axis is supportable.
- **The cross-model ICC of 0.1654 is inside the band**, but it is an underpowered two-subject estimate
  dominated by the 1.5B model's variance, and it is not treated as the verdict.

## 5. The finding this pilot actually produced

**Headroom and measurement reliability are inversely related across the scale range tested, and they
meet at the same place.**

- At **1.5B** there is dispersion to work with — but the measure is as noisy as human data, so the
  dispersion cannot be attributed to the agent rather than to the run.
- At **3B** the measure is stable — but at baseline there is almost nothing to repair: mean CCEI 0.9919
  and **not one session below the random benchmark**.

The projection intervention needs both at once: enough incoherence to be worth repairing, and a
measurement stable enough to attribute the repair to. Neither model tested supplies both. Whether some
intermediate scale does is an empirical question this pilot cannot answer with two models under 3B.

This is consistent with, and extends downward, the published gradient in `docs/PRECONDITION_CHECK.md`:
7–8B models show large format effects, very large models show effects of 0.001–0.006. The pilot adds
that below 3B the *instrument itself* degrades.

## 6. Deviations from protocol

1. **ICC estimator changed before any data was analysed.** The protocol said "ICC-equivalent across
   same-format re-runs". Splitting one homogeneous cell into pseudo-groups returns ≈0 by construction
   and measures nothing, so the estimator was changed to model-as-subject — the correct analogue of the
   human literature, where subjects are people. Changed before results were seen; noted as a deviation.
2. **Bootstrap CIs on WSCV added.** Not in the protocol. Added because the verdict turns on comparing
   WSCV to a single human reference value, and a point estimate cannot support that comparison.
3. **Discard rates and GARP pass rates reported per condition.** The protocol required discard reporting;
   pass rates were added when the 3B CCEI/violation-count divergence emerged. Flagged as an addition.
4. **Roster reduced from the session brief's 2–3 families at 7–8B to two models at 1.5B and 3B**, on
   measured hardware limits: 8 GB RAM with ~1 GB free, no GPU acceleration, and a measured 296-second
   model-swap penalty. Recorded in `docs/PILOT_PROTOCOL.md` §0.

## 7. What was NOT done

No projection operator was implemented; no repair was applied; no downstream payoff was measured. This
pilot answers only whether the dose axis exists. On the evidence above it does at 3B and does not at
1.5B, and neither scale offers headroom and reliability simultaneously.
