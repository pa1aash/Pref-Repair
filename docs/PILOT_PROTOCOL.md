# Pilot protocol — locally-hosted, zero-cost

**Written before any pilot data was collected.** Deviations from this document are recorded as
deviations in `docs/PILOT_RESULTS.md`, not silently absorbed.

**Cost: zero.** No commercial model endpoint is called at any point. All inference runs on
locally-hosted open-weight models via ollama on this machine. No free tier is used, so no free-tier
terms needed checking.

---

## 0. Hardware envelope — measured, not assumed

| Property | Measured value |
|---|---|
| Machine | MacBook Air (M1), 8 cores, arm64 |
| RAM | **8.0 GB** (`sysctl hw.memsize` = 8589934592) |
| Free at design time | **0.9–1.4 GB** (VS Code and the agent harness hold ~7 GB) |
| Disk free | 24 GB |
| GPU acceleration | **Unavailable.** ollama's Metal/GPU discovery watchdog times out on every start; it falls back to `library=cpu` and reports `available="1.4 GiB"` |

**This is materially tighter than the roster in the session brief assumed.** Three 7–8B models
quantised to Q4_K_M would be ~14 GB on disk and ~5 GB resident each; with under 1.5 GB free and no GPU,
they would thrash. The roster below is sized to what the machine can actually do.

**Measured swap penalty — the decisive constraint.** Loading a second model after a first forced an
eviction and the reload took **296 seconds** for a 986 MB model. Consequence, binding on the run order:
**all sessions for one model complete before the next model is loaded. Models are never interleaved.**

## 1. Model roster

Selected for (i) fitting the envelope, (ii) two distinct families, (iii) sitting *below* the 7–8B scale
where `docs/PRECONDITION_CHECK.md` shows the format effect is already published — so the pilot extends
the scale gradient downward rather than duplicating a known result.

| Model | Params | Quant | Size | Verified | Gen speed |
|---|---|---|---|---|---|
| `qwen2.5:1.5b-instruct-q4_K_M` | 1.5B | Q4_K_M | 986 MB | loads, responds | ~14 tok/s |
| `llama3.2:3b-instruct-q4_K_M` | 3B | Q4_K_M | 2.0 GB | loads, responds | ~10 tok/s |

Both were verified to load and answer a trivial prompt before this protocol was written, per the brief.
A third family (Phi-3.5 / Gemma) and a 7B tier are **out of scope for this run** on the memory evidence
above; adding them is a follow-up on a machine with more free RAM, and that is recorded as a limitation
rather than quietly dropped.

## 2. Budget-set design

Reuses the instrument from `audit/killcheck_E3.md` (the PNAS design) **with one deliberate change**,
required by `docs/METHOD_NOTE_Q6.md`:

| Parameter | Value | Source |
|---|---|---|
| Rounds per session | **25** | E3 |
| Goods | **2** (K=2) | E3 — also where Bronars power is ≈0.999 and Houtman–Maks is polynomial |
| Endowment | **100 tokens, fixed, must be fully spent** | E3 (budget exhaustion) |
| Exchange rates | `M, N ~ U[0.1, 1.0]` i.i.d., **rejected unless max{M,N} ≥ 0.5** | E3 |
| **Price precision** | **full float64 — NOT rounded to 2 decimals** | **DEVIATION from E3, mandated by `docs/METHOD_NOTE_Q6.md`** |
| Budget sets | **held fixed across every model, format and re-run** | required for test–retest |

**Why the precision deviation is mandatory.** E3's instrument rounds exchange rates to two decimals. That
is a 91-point discrete grid, which violates the Lemma-1 hypothesis (`docs/METHOD_NOTE_Q6.md`): with
discrete prices, exact budget ties occur, and a naive CCEI can report exactly 1.0 while GARP is violated.
Measured prevalence: **100%** of 25-observation integer-price designs contain at least one exact tie, and
**18.9%** of uniform-random agents report a false 1.0. Continuous-density draws plus budget exhaustion
take the tie rate to **0.0%** across 63,200 replications. Using E3's rounding would import a known bug.

## 3. Conditions

Two framing conditions, **not persona** — per `audit/killcheck_E3.md`, `docs/PRECONDITION_CHECK.md`, and
the KC Fed finding that reframing moves economic behaviour more than personas do. Budget sets identical
across conditions; only the wording changes.

- **`baseline`** — direct framing: *"A pays {M} per token, B pays {N} per token."*
  (E3's "investing every 1 point for Asset A returns M dollars".)
- **`reciprocal`** — E3's reciprocal price framing, its single strongest published manipulation:
  *"it takes {1/M} tokens to buy one unit of A, {1/N} to buy one unit of B."* Same budget line, inverted
  presentation. E3 reports this dropping mean CCEI to 0.698–0.901 on identical budget sets.

## 4. Sample sizes and what each answers

| Quantity | Design | n |
|---|---|---|
| **Test–retest reliability** (precondition 1) | same model, **same** format (`baseline`), fresh context each time, **seeds 1..25** | 25 sessions per model |
| **Format sensitivity** (precondition 2) | same model, **different** format (`reciprocal`), same 25 seeds | 25 sessions per model |

**These are kept separate by construction and reported separately.** Conflating them is the exact error
`docs/PRECONDITION_CHECK.md` identifies in the prior literature.

Total: 2 models × 2 conditions × 25 sessions = **100 sessions**. At ~35 s (1.5B) and ~50 s (3B) per
session, ≈75 minutes of compute plus two model loads.

**Fresh context per session** — every session is a separate `/api/generate` call with no history.
Sessions differ only by `seed`, which is the sampling seed; `temperature = 0.7` so that repeated runs can
differ (at temperature 0 test–retest is trivially perfect and measures nothing).

## 5. Metrics

Computed for every condition. All three are required by `audit/BRONARS_NOTE.md`'s standing rule.

1. **CCEI** — Afriat efficiency index by bisection on `e ∈ (0,1]`, each feasibility check a Warshall
   transitive-closure GARP test on the `e`-relaxed relation. Implementation must be validated first on
   two cases with known answers: a Cobb–Douglas rationalisable sequence → **1.0000**, and the textbook
   two-observation extreme swap → **0.1111**.
2. **Bronars power** — for the actual budget sets, before any model output: draw budget shares
   `w_t ~ Dirichlet(1,1)`, convert to quantities, test GARP, repeat 2,000×. Power = fraction violating.
   Also report the **mean simulated CCEI** of the random agent.
3. **Predictive success** — Selten's `m = pass rate − (1 − power)`.

Reliability statistics for precondition 1, over the 25 same-format sessions per model:
**mean, SD, within-subject coefficient of variation (WSCV), and the ICC-equivalent** — here the
intraclass correlation across sessions treating session as the repeated measure. Nitsch's human
comparison band is **ICC 0.071–0.685, none reaching the conventional "good" threshold of 0.75.**

## 6. Response handling

- Required format: 25 lines, `ROUND=<n> A=<int> B=<int>`, integers summing to 100.
- A line failing to parse, or not summing to 100, makes that **round** invalid.
- A session with **fewer than 20 of 25 valid rounds is discarded** and recorded as a parse failure.
  Discards are reported per condition; a high discard rate is itself a finding about small-model
  instruction-following, not something to paper over.
- **No retries and no repair of model output.** Whatever the model emits is the datum.

## 7. Stop rule — the flip-to-NO condition, fixed in advance

From `docs/GO_NOGO_ASSESSMENT.md`: *"If the pilot shows CCEI test–retest reliability on the target models
is as poor as Nitsch reports for humans… the dose variable is noise, the projection is repairing sampling
variation, and no amount of reframing rescues it."*

Operationalised, committed before seeing any data:

- **FIRES** if the ICC-equivalent across same-format re-runs falls **inside or below Nitsch's human band
  (≤ 0.685)** for **both** models.
- **DOES NOT FIRE** if ICC > 0.75 (the conventional "good" threshold) for at least one model.
- **AMBIGUOUS** in between (0.685 < ICC ≤ 0.75) — reported as ambiguous, not rounded to a verdict.

Reported plainly either way. A fired stop rule is the primary finding and this session does **not**
proceed past reporting it.

## 8. Deliberate scope limits

- **Two models, both under 3B.** The envelope forbids more. The scale gradient this tests is *below*
  the published 7–8B result, not across it.
- **No projection operator is implemented.** This pilot measures whether the dose axis exists. Building
  the repair operator is downstream of that and out of scope.
- **No paid API call, no free tier.** Local inference only.
