# 1. Rhetorical negation

The dominant defect of the manuscript. Hard counts over all 754 lines: **`rather than` 21 times**; **`mere`/`merely` 8 times** (L35, L85, L116, L275, L463, L533, L632, L658); **`genuine`/`genuinely` 6 times** (L164, L166, L263, L509, L703, L731). Adding bare `not X`, `no X`, `never X` constructions the total flagged is **106 instances**, of which I recommend keeping 14. Every one of the paper's five headline claims — the abstract thesis (L34–36), the central finding (L84–85), the novelty claim (L90–91), contribution (3) (L113–117), and the C1 verdict (L533–535) — is delivered in negated form. A reader never receives a plain affirmative statement of what this paper found.

## 1a. Abstract and Introduction (lines 31–123)

| # | Line | Exact text | Disposition |
|---|---|---|---|
| 1 | 32 | `Repairing an AI agent's incoherent preferences is not new:` | Replace: `Repairing an AI agent's incoherent preferences is an established line of work:` The novelty claim arrives one sentence later and does not need this setup. |
| 2 | 34 | `None controls for displacement\nmagnitude: no result establishes whether...` | Delete `None controls for displacement magnitude:` — a compressed restatement of the sentence that follows it. |
| 3 | 34–36 | `no result establishes whether restoring coherence itself, not mere displacement toward\nan interior point, is what any reported gain comes from` | Replace: `no result establishes whether the reported gains come from restoring coherence or from displacement toward an interior point.` |
| 4 | 39 | `not\nmere displacement toward an interior point` | Same clause as #3; fold in. |
| 5 | 43 | `we decline a\nthird as payoff-shopping` | Delete from the abstract (see §11). If kept: `We designed two payoffs and stopped.` |
| 6 | 46 | `The\npaper's standing contributions are instead a capacity-deconfounded identification strategy` | Delete `instead` and `standing`: `The paper's contributions are a capacity-deconfounded identification strategy...` |
| 7 | 59–60 | `applies it to GPT-family models directly, without a\nrepair step, to ask whether they satisfy classical rationality axioms at all` | **Keep the contrast, move it forward:** `applies it to GPT-family models with no repair step, asking whether they satisfy classical rationality axioms at all`. |
| 8 | 64–65 | `What none of them establishes is a \emph{dose}` | Replace: `None of them establishes a \emph{dose}` (also §6). |
| 9 | 65–66 | `isolated from the\ncapacity and training confounds that come from comparing a richer model class to a poorer one` | **Keep.** Genuine technical contrast; the confound is named specifically. |
| 10 | 71 | `a projection applied \emph{post hoc} to a frozen agent, so nothing\nabout its weights, training, or decoding changes across doses` | **Keep.** The negation is the identification argument. |
| 11 | 75 | `--- never of the agent's own choices ---` | **Keep.** The `never` is the exogeneity claim. |
| 12 | 76 | `so the outcome measure is exogenous to the preference data by construction, not\na restatement of coherence` | Delete `, not a restatement of coherence`. `exogenous to the preference data by construction` already says it. |
| 13 | 79 | `That relationship turns out not to isolate what it was built to isolate.` | Replace: `The design does not identify the effect of coherence restoration.` (Better: reorder so no retraction is needed — §14.) |
| 14 | 84–85 | `restoring rationality, as originally proposed, does not buy more\nexogenous payoff than mere displacement toward the interior of the budget line does on its own` | **Keep the negation** — a null result is legitimately negative. Delete `as originally proposed` (§11), `mere` (§5), `does on its own` (§5), and add the number: `restoring rationality buys no more exogenous payoff than displacement toward the interior of the budget line (0.0091 vs.\ 0.0220).` |
| 15 | 86–87 | `We\nreport this as a negative result reached twice by construction, not as a null we happened to\nobserve once.` | Delete. `under two independently designed payoffs` at L83 already carries `twice`. |
| 16 | 89 | `We do not claim any of the individual pieces are new; \S\ref{sec:related} concedes exactly what\nis not.` | Delete. §Related does this work; announcing it is §3 material. |
| 17 | 90–91 | `What has not been done is the conjunction: an agent's own realized choices, ...` | Replace: `The conjunction is new: an agent's own realized choices, a graded coherence-indexed dose, and an outcome that is not itself a preference judgment.` (also §6). |
| 18 | 94–95 | `as an identification control on the method itself, not as a second\npoint on a shared dose curve across scale` | Promote to its own sentence: `The 3B run is an identification control on the method. The two scales are not two points on a shared dose curve.` |
| 19 | 101–102 | `We report the discard rate itself, not the CCEI point estimate, as the more reliable\nsignal` | Replace: `The discard rate is the more reliable signal that the manipulation disrupted the agent; the CCEI point estimate is not.` |
| 20 | 108–109 | `An application --- not a novel method --- of\n\citet{demuynck2023computing}'s minimal-quantity-error MILP projection` | Delete `--- not a novel method ---`. `An application ... of \citet{demuynck2023computing}'s` already concedes it. |
| 21 | 110 | `independently verified on every output rather than trusted from solver status alone` | **Keep the contrast**, promote from appositive: `verified independently on every output, not by solver status`. |
| 22 | 115–117 | `is not evidence that\nGARP-restoration specifically, rather than mere displacement toward the interior, is what buys\nthe exogenous payoff gain` | Triple-nested negation plus cleft. Replace: `does not show that GARP-restoration buys the exogenous payoff gain: displacement toward the interior buys as much.` |
| 23 | 118–119 | `reported per cell rather than pooled away` | Replace with `reported per cell`. Nobody expected pooling. |

## 1b. Related Work (lines 124–201)

| # | Line | Exact text | Disposition |
|---|---|---|---|
| 24 | 127 | `Repairing an AI system's incoherent preferences is not new;` | Replace: `Nine published systems repair an AI system's incoherent preferences.` L89 already concedes this; the table is the concession. |
| 25 | 128–129 | `an agent's own choices\n(not a judgment about third-party items)` | Replace: `an agent's own choices from its own budget set`. The rule-out repeats at L135 and L163. |
| 26 | 129 | `an exogenous payoff (no preference judgment enters it)` | Replace: `an exogenous payoff (fixed before data collection, scored without any preference judgment)`. |
| 27 | 130 | `a graded rather than binary dose` | **Keep.** The contrast is the criterion. |
| 28 | 159–160 | `lands weakly closer` | **Keep.** `weakly` is a mathematical weak inequality, not a hedge. |
| 29 | 160 | `We concede the minimum-distance priority unqualified:` | Replace: `The minimum-distance priority is theirs:` |
| 30 | 162–163 | `POISE also\nprojects a \emph{teacher's} offline labels, not an agent's own choices.` | Replace: `POISE projects a \emph{teacher's} offline labels.` The second half restates criterion 1 for the third time. |
| 31 | 164 | `Three further\ninference-time repairs lack a genuine degree parameter or Afriat machinery` | Replace: `Three further inference-time repairs have a binary edit and no Afriat machinery:` |
| 32 | 168 | `and one not an LLM agent at all \citep{aguiar2026garpefm}` | Replace: `and one operating on human survey choices \citep{aguiar2026garpefm}` (author to confirm the correct positive description). |
| 33 | 171–172 | `varies the transitivity of the \emph{preference model} rather than an agent's\nchoices` | **Keep.** Both terms load-bearing. |
| 34 | 176–178 | `proposes $1-\mathrm{CCEI}$ as a training penalty argued a priori,\nnever measured` | Replace: `proposes $1-\mathrm{CCEI}$ as a training penalty on a priori grounds and reports no measurement of it.` |
| 35 | 183–184 | `That revision arm is not a repair operator (a\nrandom subset, no consistency objective, no guarantee of fewer violations)` | **Worst negation cascade in Related Work.** Replace: `Their revision arm re-presented a random subset of trials with no consistency objective, so it could not guarantee fewer violations; ours attains rationalizability by construction.` |
| 36 | 199–200 | `--- not a replication, since which format is more\ndegrading reverses between their 7B model and ours.` | Replace: `Which format is more degrading therefore reverses between their 7B model and ours; this is a contrast, not a replication.` (See §14 — the section's last words are a disclaimer.) |

## 1c. Method and Experimental design (lines 202–402)

**31 instances; keep 2.** The Method reads as a defence brief rather than a description of what was done.

| # | Line | Exact text | Disposition |
|---|---|---|---|
| 37 | 209 | `This section applies, rather than proposes, a projection method.` | **Delete.** L210–212 and L212 already say this twice more. |
| 38 | 212 | `nothing about the formulation itself is new to this paper.` | **Delete.** Third statement of the same disclaimer in four lines. |
| 39 | 218–220 | `The naive Afriat-multiplier formulation is bilinear ...; we instead use the multiplier-free ordinal characterization` | **Keep.** Stated reason (bilinearity), stated consequence (linear constraints). Trim `naive` (§5). |
| 40 | 229–230 | `$L_\infty$ is recorded alongside but not separately analyzed` | Replace: `$L_\infty$ is recorded alongside.` |
| 41 | 235–236 | `applied here to an LLM's own choices and paired with an exogenous behavioral payoff rather than left as a standalone index` | Replace: `applied here to an LLM's own choices and paired with the exogenous payoff of \S\ref{sec:method-payoff}.` |
| 42 | 238 | `recorded only as an upper-bound diagnostic` | **Delete.** Redundant with `sanity ceiling` seven words earlier. |
| 43 | 239 | `confirms it never reaches the solver.` | Replace: `confirms it is not passed to the solver.` (See §13 — `feasibility incumbent` and `never reaches the solver` contradict each other.) |
| 44 | 241 | `\textbf{What can be guaranteed, and what cannot}` | Replace: `\textbf{Guarantees.}` (also §6, §7). |
| 45 | 243–244 | `because the GARP-consistent set is a union of polyhedra rather than a single convex set` | **Keep.** Load-bearing geometric fact. |
| 46 | 244 | `no distance-minimization guarantee analogous to a convex-cone projection is claimed.` | Replace: `we claim no distance-minimization guarantee analogous to a convex-cone projection.` |
| 47 | 249 | `The payoff must not be derived from the agent's own revealed choices` | Replace: `The payoff is fixed independently of the agent's revealed choices.` |
| 48 | 251–252 | `rewarding the agent for resembling its own revealed preferences rather than measuring anything external to them` | Replace: `rewarding the agent for resembling its own revealed preferences.` |
| 49 | 253 | `and never re-estimated from any agent's choices` | Promote to its own sentence: `It was never re-estimated from any agent's choices.` |
| 50 | 256–257 | `--- a function of prices and income alone, never of the agent's observed or projected bundle.` | Replace: `--- a function of prices and income alone.` `alone` already excludes the bundle. |
| 51 | 261 | `This mirrors --- not the specifics, but the structure of --- a money-metric utility index` | **The purest instance in the paper**: a not-X-but-Y inserted as an interrupting dash pair inside the verb phrase. Replace: `This has the structure of a money-metric utility index`. |
| 52 | 266 | `but without a placebo of matched size cannot separate an alignment-specific effect from a generic fine-tuning effect` | Replace: `separating an alignment-specific effect from a generic fine-tuning effect requires a placebo of matched size.` (Also fixes the dangling subject — §4.) |
| 53 | 272–273 | `None survived the audit` | Replace: `All four are ruled out`. |
| 54 | 274 | `is not an artifact of any of the four.` | **Delete the clause** — restates `None survived the audit` in the same sentence. |
| 55 | 275–276 | `could reward mere displacement without any GARP-specific effect` | Replace: `could reward displacement alone`. |
| 56 | 276–277 | `required a new control rather than an audit of the existing design` | Replace: `required a new control`. |
| 57 | 284 | `raises its payoff regardless of GARP` | Replace: `raises that bundle's payoff whether or not it restores GARP-consistency.` *Stylistic preference; competing convention holds `regardless of` is compact and standard. Flagged because it is one of 31.* |
| 58 | 288 | `The null never calls the GARP check and does not, in general, restore consistency` | Replace: `The null does not call the GARP check. It restores consistency in <N> of the 85 traces.` Two defects: negation, and `in general` hedging a countable fact (§5). |
| 59 | 295 | `We report two null constructions under this payoff, never pooled` | Replace: `We report two null constructions under this payoff separately.` |
| 60 | 297 | `since it uses information no real repair algorithm has` | Replace: `since it uses the per-trace $\alpha_s$, which a repair algorithm does not observe.` |
| 61 | 336–337 | `Not added at 3B, whose role is a null-effect control rather than a second scale point.` | Replace: `The 3B model serves as a null-effect control, so this arm was run at 1.5B only.` |
| 62 | 343–344 | `--- unlike a pilot's single shared set, needed because the main experiment targets independent between-condition replication.` | Replace: `Independent seeding supports between-condition replication.` |
| 63 | 350–351 | `reported rather than papered over` | **Delete.** Pure editorializing; the sentence already reports it. |
| 64 | 360 | `true regardless of whether projection helps, hurts, or does nothing downstream.` | **Delete.** Obvious from the fact that the claim is measured on discards. |
| 65 | 368 | `retry-rescued sessions are not a close stand-in for first-attempt sessions` | Replace: `retry-rescued sessions differ from first-attempt sessions: CCEI 0.9651 vs.\ 0.9315, GARP pass 0.1429 vs.\ 0.4706.` |
| 66 | 371 | `though not conclusive given the small residual sample` | Promote: `The residual sample ($n=6$, 3 measurable) is too small to be conclusive.` |

## 1d. Results (lines 403–594)

| # | Line | Exact text | Disposition |
|---|---|---|---|
| 67 | 440 | `The confound is real (...) but does not explain the relationship away` | **Keep.** Both halves carry numbers ($r=-0.41$; $r=0.784$). |
| 68 | 443–444 | `not distinguishable from zero ($p=0.18$)` | **Keep.** Technical statement of a null with its number. |
| 69 | 457 | `the oracle null is not plotted` | Delete from the caption. A caption states what is plotted. |
| 70 | 461–462 | `is a confound on the \emph{severity} of the raw violation, not on the specific \emph{geometry} of the payoff function` | Replace: `bears on the \emph{severity} of the raw violation. It leaves open whether the \emph{geometry} of the payoff function explains the gain.` (Also §16: a confound is not "on" a geometry.) |
| 71 | 463–464 | `whether restoring GARP-consistency \emph{specifically}, rather than merely displacing choices toward some interior point, is what buys the payoff gain above` | Replace: `whether the GARP-restoration or the displacement does the work` (the full form survives at L533–534). |
| 72 | 466 | `that does nothing but shrink every bundle toward the exogenous payoff's own fixed optimum` | Replace: `that shrinks every bundle toward the exogenous payoff's fixed optimum and uses no GARP information`. |
| 73 | 488 | `reported for completeness rather than as the primary comparison` | **Delete.** `primary` at L483 already establishes the ranking. |
| 74 | 491–492 | `--- a real but more modest signal, not distinguishable from the draw-to-draw noise the 20 draws themselves already show` | Delete and replace with the number: `The across-draw spread of $r$ is of the same size as this attenuation (SD = ...).` Also self-contradictory — §5, §13. |
| 75 | 494 | `\textbf{No third payoff was attempted, and this is a stated scope decision, not a resource constraint.}` | Replace lead with `\textbf{Two payoff designs, not three.}` — better, `\textbf{Two payoff designs.}` and let the paragraph give the reason. |
| 76 | 511–512 | `read as partial, not conclusive, support for an ``escape a bad start'' mechanism rather than pure centering, offered as a discussion-level hypothesis rather than a load-bearing result with its own significance test` | Three rule-outs in one clause. Replace the whole trailing clause: `We treat this as a hypothesis for the discussion; we do not test it.` |
| 77 | 533–535 | `is not supported under either payoff design` | **Keep.** This is the result; a negative result must be stated negatively. |
| 78 | 534 | `beyond mere displacement toward the interior of the budget line` | Delete `mere`. |
| 79 | 535–536 | `is real; it is not evidence for the specific mechanism C1 claims` | **Keep.** Both halves load-bearing. Drop `real` (§5). |
| 80 | 549 | `does \emph{not} survive proper correction for discard-selection` | **Keep the negation.** Drop `proper` (§5). |
| 81 | 555–556 | `This is no detectable CCEI shift, not a confirmation of the pilot's own naive estimate` | A negative predicate ruled out against another negative — the hardest sentence in the subsection to parse. Replace: `Both the pilot and the main experiment return null CCEI results.` |
| 82 | 557–558 | `and reading their sign difference as a reversal overstates what either number supports` | Move to Limitations, or delete. Rules out a misreading no reader has made. |
| 83 | 568 | `survives Benjamini--Hochberg correction ($p_{\mathrm{BH}}=0.0094$) but not Holm ($p_{\mathrm{Holm}}=0.058$)` | **Keep.** Genuine technical contrast, both numbered. |

## 1e. Limitations, Broader impacts, Conclusion (lines 595–667)

| # | Line | Exact text | Disposition |
|---|---|---|---|
| 84 | 598–599 | `CCEI is noisy at 1.5B, and the paper leads with GARP pass rate because of it, not by preference.` | Replace: `CCEI is noisy at 1.5B, so the paper leads with GARP pass rate.` |
| 85 | 603 | `that scale-up was deferred, not executed.` | Replace: `that scale-up was not run.` |
| 86 | 614 | `\textbf{Two fixed exogenous payoffs, not three.}` | Replace: `\textbf{Two exogenous payoffs.}` |
| 87 | 617–618 | `A third payoff, run only because the second also came back negative, would be payoff-shopping, not a robustness check` | **Keep the contrast, restate it:** `A third payoff, selected after seeing that the second was also negative, would be payoff-shopping.` `not a robustness check` is entailed. |
| 88 | 620 | `\textbf{An adverse prior the paper now joins rather than argues against.}` | Replace: `\textbf{Consistent with three prior negative results.}` |
| 89 | 625–628 | `We do not read this as evidence the coherence--competence relationship is negative in general --- C2 remains open, not settled --- only that this paper's own attempt to find a positive relationship, net of displacement, did not succeed.` | **Keep the scope limit, drop the negation frame.** Two sentences: `Net of displacement, this paper's attempt to find a positive coherence--competence relationship did not succeed. That leaves C2 open; it is not evidence that the relationship is negative.` |
| 90 | 626 | `C2 remains open, not settled` | Replace: `C2 remains open.` `not settled` is the definition of open. |
| 91 | 638–640 | `not a recommendation to deploy it universally, nor a claim that no coherence-repair method could ever help.` | Delete both clauses. They rule out two readings no honest reader would reach. |
| 92 | 660 | `a discard-selection artifact rather than a real coherence shift (C3)` | Replace: `a discard-selection artifact (C3)`. |
| 93 | 664 | `are exactly what this literature should surface by default rather than paper over.` | Delete the clause (see §10, §14). |

## 1f. Appendix A and B (lines 672–750)

| # | Line | Exact text | Disposition |
|---|---|---|---|
| 94 | 678 | `\textbf{(1) No shared derived quantity beyond the exogenous $(p, I)$.}` | Replace: `\textbf{(1) The payoff depends only on $(p_t, I_t)$.}` |
| 95 | 679–680 | `The payoff implementation has no dependency on the projection implementation` | Replace: `The payoff is computed from $(p_t, I_t)$ by a routine that reads no projection output.` |
| 96 | 680–681 | `is a function of $(p_t, I_t)$ alone and never references $x_t$ or $\tilde{x}_t$` | **Keep.** The `never references` clause names the two checkable objects. |
| 97 | 682–683 | `but this quantity is never passed to the underlying MILP solver as an actual incumbent` | State the fact first: `The share-fitted Cobb--Douglas demand is used only to log an upper bound on the reported distance; it is never passed to the solver, which exposes no incumbent interface.` |
| 98 | 684–685 | `, never to steer the solution.` | **Delete.** Fully entailed by `used only to log`. Fourth negation of one fact in a seven-line paragraph. |
| 99 | 690–691 | `GARP-consistency status alone does not predict payoff, ruling out a population-level mechanical link` | Replace: `No population-level link between GARP-consistency and payoff is detectable ($t=-0.07$, $p=0.94$).` (Also §13 — a null does not "rule out".) |
| 100 | 698 | `a geometric quantity the projection objective never references` | Duplicate of #96, thirteen lines later. Rephrase: `the cosine of the projection step against $(x^*-x)$, which appears nowhere in the projection objective`. |
| 101 | 703–704 | `It does not explain the dose--response relationship away` | Replace: `The dose--response relationship survives the confound: the partial correlation ... is $r=0.784$.` |
| 102 | 707–708 | `while raw payoff's own coefficient is not ($t=-1.36$, $p=0.18$)` | **Keep.** Genuine two-coefficient contrast. Delete `own` (§5). |
| 103 | 717–718 | `fixing a candidate preference ordering does not remove the bilinearity, since a price-weighted multiplier term remains a product of two unknowns` | Compress and move after the adopted formulation: `Afriat-multiplier parameterizations are bilinear once $\tilde{x}$ is a decision variable, and remain so under any fixed ordering.` |
| 104 | 719, 721 | `multiplier-free ordinal characterization` ... `ordinal utility levels $u_t\in[0,1]$ that carry no multipliers` | Delete `that carry no multipliers`; `multiplier-free` already carries it, 30 words earlier in the same sentence. |
| 105 | 722–723 | `with no outer search over preference orderings and no alternating scheme` | Promote to a positive statement: `The formulation is solved as a single MILP, with no outer search over preference orderings.` |
| 106 | 730 | `the GARP-consistent set is not closed` | **Keep.** The non-closedness is the reason for $\gamma$. |
| 107 | 733–734 | `never trusted from solver optimality status alone` | **Delete.** Entailed by `verified independently via the same combinatorial Warshall-closure GARP check`; also dangles (§4). |
| 108 | 743–744 | `a union of polyhedra rather than a single convex set` | **Keep.** |
| 109 | 745 | `has no analogue here` | Replace: `does not transfer` (also §16 — three `analogue` cognates in one 93-word sentence). |
| 110 | 746–747 | `the prior operator's cone is fixed by an ordering supplied as input, whereas a GARP repair must decide which revealed-preference comparisons to give up` | **Keep.** This is the actual difference between the two settings. |
| 111 | 748 | `absorbed into the binary comparison indicators above rather than eliminated` | **Keep the contrast, fix the attachment** (§4 — the participle dangles). |
| 112 | 748–749 | `which is why no distance-minimization guarantee analogous to the convex case is claimed` | The appendix's final words are an agentless negation. Replace: `We therefore claim no distance-minimization guarantee.` |

## 1g. Rule-out cascades (three or more consecutive rule-outs before the claim)

1. **L34–36 (abstract, severity: highest).** `None`, `no result`, `not mere` across two sentences, followed by the three-word claim `We build that control.` The reader reaches the contribution at word 60 of the abstract.
2. **L89–92.** `We do not claim any of the individual pieces are new` → `\S\ref{sec:related} concedes exactly what is not` → `What has not been done is the conjunction`. Three negations before the positive novelty claim.
3. **L163–169 (Related Work).** Three consecutive rule-out sentences dispatch six systems: `lack a genuine degree parameter or Afriat machinery` (164), `declines a minimum-distance method` (167), `report no downstream comparison` (169). The reader never learns what any of the six does do.
4. **L183–184 (Related Work).** Four negations — `not a repair operator`, `a random subset`, `no consistency objective`, `no guarantee of fewer violations` — before the positive claim at L184.
5. **L249–257 (Method, severity: high).** Five constructions rule out circularity before the payoff is stated: `must not be derived` (249), `would be circular` (250), `rather than measuring anything external` (251–252), `never re-estimated` (253), `never of the agent's observed or projected bundle` (256–257). The formula arrives at L254 after three lines of defence.
6. **L269–277 (Method, severity: high).** Nine lines in which no positive claim about the design appears: four failure modes, `None survived`, `is not an artifact of any of the four`, then a fifth failure mode.
7. **L494–500 (Results).** Four consecutive sentences, every one a rule-out: no third payoff / not a resource constraint / a third would be payoff-shopping / that is the degree-of-freedom problem the payoff was introduced to rule out. No positive claim arrives.
8. **L506–512 (Results).** Five contrastive moves before any claim is committed to.
9. **L637–640 (Broader impacts).** Claim, inserted concession, then two consecutive rule-outs.
10. **L679–685 (Appendix A part 1).** Four negations of a single fact.
11. **L715–718 (Appendix B, Formulation).** Two full sentences reject the Afriat-multiplier formulation before `We instead use` reaches the adopted method; the paragraph then closes on two further rule-outs (722–723). Negative at both ends, positive only in the middle.

## 1h. Mirrored pairs (same distinction stated in both directions)

1. **L79–83 vs. L113–117.** The null-operator finding stated positively (`outperforms the real GARP-restoring repair`) and then negatively (`is not evidence that GARP-restoration specifically ... is what buys`). Use the positive form in both.
2. **L135 vs. L128–129 vs. L163.** The "own choices, not third-party judgments" distinction stated three times in 35 lines, once mirrored. Keep the caption version (§8), cut L129's parenthetical and L163's negated half.
3. **L235–236 vs. L249–252.** Independence of payoff from choices stated from opposite ends, 15 lines apart. Keep the second.
4. **L236–239 vs. L250.** The share-fitted incumbent ruled out twice. Keep L250, cut the L238 disclaimer.
5. **L283–284 vs. L291.** `identical across every trace` (284) and `a single fixed target identical across every trace` (291) — same property, 8 lines apart, second time behind a bare definite noun (`the exploitable property`).
6. **L463–464 vs. L533–534.** Near-verbatim restatement of the C1 proposition, 70 lines apart. Keep L533–534.
7. **L506–508 vs. L511–512.** `does not cleanly separate ``centering'' from a more general ... account` then, three lines later, `support for an ``escape a bad start'' mechanism rather than pure centering`. The identical distinction stated in both directions inside one paragraph.
8. **L626 vs. L656–657.** The identical four-word formula `open, not settled` / `remains open, not settled` about C2, forty lines apart. Use `C2 remains open` at 626 and a different construction at 656–657.
9. **L680–681 vs. L698.** `never references $x_t$ or $\tilde{x}_t$` and `the projection objective never references`. Same claim, parts (1) and (3) of the same audit.

## 1i. `mere` / `merely` as a dismissive intensifier — 8 instances, doc-wide

L35, L85, L116, L275, L463, L533, L632, L658. Delete at all eight. The comparison is quantitative (0.0220 vs. 0.0091, $2.4\times$); `mere` editorializes a number that already makes the point, and it makes the null operator sound trivial in a paper whose central finding is that the null operator wins. L658 is the worst: `or mere displacement magnitude` ranks as trivial the very confound the paper's own control was built to isolate.

---

# 2. Sentences that announce their own significance

No literal `it is worth noting` / `crucially` / `notably` / `importantly` / `interestingly` anywhere in the 754 lines — I searched, and so did four of the six section agents independently. The manuscript instead runs three functional substitutes: **superlative self-positioning** (Related Work), **bolded verdicts** (Results), and **status labels applied to its own claims** (throughout).

| # | Line | Exact text | Fix |
|---|---|---|---|
| 1 | 57 | `The same budget-allocation instrument is the standard paradigm for\ntesting GARP experimentally on human subjects` | *Stylistic preference, not error.* An authority claim, but three citations follow, which earns it. Competing convention: `is widely used for`. **No change.** |
| 2 | 82 | `outperforms the real GARP-restoring repair on the exogenous payoff, significantly, at\nboth model scales` | `significantly,` set off by commas mid-sentence is an announcement, not a statistic. Replace with the number: `... at both model scales ($p=3.98\times10^{-10}$)`. |
| 3 | 83–84 | `This is the\npaper's central finding:` | Delete the announcement, keep the claim. Position (top of paragraph 3, with a p-value) already marks it as central. |
| 4 | 97 | `Two further results were not predicted by the design.` | Announcement of surprise. Delete and state the results (also §3, §11). |
| 5 | 101–102 | `as the more reliable\nsignal` | `more reliable` is asserted, not shown. Replace with the reason: `The discard rate is measured without conditioning on completion; the CCEI point estimate is not.` |
| 6 | 128 | `the four criteria that jointly define our claim` | Replace: `four criteria`. The colon that follows already shows they are the claim. |
| 7 | 158 | `\textbf{POISE} \citep{wang2026poise} is the sharpest vocabulary collision:` | `sharpest` has no metric behind it. Replace: `\textbf{POISE} \citep{wang2026poise} projects with pool-adjacent-violators onto a closed convex chain-monotone cone, and proves the edit lands weakly closer to a posited ground truth.` |
| 8 | 176 | `Our closest theoretical neighbour,` | Drop the ranking; the paragraph shows the closeness. Open at `\citet{andrews2026revealed} proposes ...` |
| 9 | 180 | `and it is in \emph{PNAS}` | **Delete.** Appeal to venue; the citation already carries it, and italicising the journal name makes the appeal explicit. |
| 10 | 192 | `The closest neighbour on the economics side is invisible to any arXiv sweep.` | **Delete the sentence.** Fourth superlative, and the second half is search-process leakage (§11). Open the paragraph at `\citet{cook2026whatllmswant} steer economic choices...` |
| 11 | 323–324 | `the two-model, model-major design is both a wall-clock optimization and, after that failure, a correctness requirement` | The `both X and Y` frame is an elevation device that turns a crash-imposed constraint into a design virtue. Replace: `The crash required that models not be co-resident, which the model-major design already satisfied.` |
| 12 | 354 | `and its correction as a stated contribution` (subsection heading) | **Delete from the heading.** Announcing that something is a contribution is not the same as it being one. |
| 13 | 359–360 | `This is a claim about instrument validity in its own right, true regardless of whether projection helps, hurts, or does nothing downstream.` | Replace: `This is a claim about instrument validity.` |
| 14 | 374–375 | `as a first-class per-condition outcome for every cell` | Replace: `for every cell.` `first-class` is the author telling the reader how seriously to take the number (also §11 — programming vocabulary). |
| 15 | 436–437 | `\textbf{Both scales show a significant, positive relationship, and it is stronger at the headroom model}` | **Unbold.** The two $\rho$ values that follow are the evidence; bolding tells the reader what to think of them before they see them. |
| 16 | 472 | `This holds independently at both models.` | Replace with the two per-model numbers. As written it asserts robustness with no quantity. |
| 17 | 475 | `but the paired comparison is unambiguous:` | Delete the clause; $p=3.98\times10^{-10}$ has already established the strength. |
| 18 | 482 | `The qualitative result is unchanged:` | Replace: `Experiment 2 reproduces Experiment 1:` — names what is unchanged instead of grading it. |
| 19 | 494 | `\textbf{No third payoff was attempted, and this is a stated scope decision, not a resource constraint.}` | A bolded pre-emptive defence. See §1 #75, §7. |
| 20 | 497 | `converging on the same negative paired-comparison result is the finding` | Delete `is the finding` (§10). |
| 21 | 502 | `\textbf{A partial mechanistic note.}` | Replace: `\textbf{Trace extremity and the null's advantage.}` `Partial` grades the content before the reader can. |
| 22 | 533–535 | The entire three-line bolded C1 verdict | **Unbold.** A verdict this important should be the shortest sentence in the paragraph, not the longest one in bold. |
| 23 | 603 | `This is an open design tradeoff:` | Delete the label; start at `The pass-rate metric is powered throughout...`. |
| 24 | 630 | `This paper's central result argues against imposing GARP-restoration` | Delete `central`. Nominating your own result as central inside broader impacts invites a reviewer to disagree about which result is central. |
| 25 | 662–663 | `are reported in their own right` | **Delete.** Every finding in a paper is reported in its own right; the phrase is defensive filler around findings the author suspects look like scope creep. |

**Superlative tic, counted:** `sharpest` at L158 and L180; `closest` at L176, L192, L241, L742. **Six superlative self-locating phrases**, four of them in paragraph- or lead-opening position. Related Work's table already establishes relative position without adjectives; keep none of the four in that section.

---

# 3. Sentences that announce what a section will do

**The single strongest finding in this category is doc-wide, not sectional: `Appendix~\ref{app:method-detail}` is pointed at three times in 34 lines (L222–224, L231–232, L241–242), and both appendices then open with the same template sentence (L676, L712–713) pointing back.** A reader is told three times that the details are elsewhere, arrives, and is told twice more that this is the detail of something summarized elsewhere.

| # | Line | Exact text | Fix |
|---|---|---|---|
| 1 | 68 | `We study this question in a setting where it can be answered cleanly.` | **Delete.** The next four sentences describe the setting; the announcement adds only `cleanly`, an undefined adverb (§5). |
| 2 | 76–77 | `Tracing dose\nagainst $\Delta$payoff gives the relationship this paper reports.` | **Delete.** It says the paper will report what the paper reports. |
| 3 | 89 | `\S\ref{sec:related} concedes exactly what\nis not.` | **Delete.** A pointer to a section 40 lines away, announcing that it will concede something. |
| 4 | 97 | `Two further results were not predicted by the design.` | **Delete.** Roadmap for the two sentences beneath it, and process leakage (§11). |
| 5 | 108 | `\textbf{Contributions.}` | **Keep.** Conventional bold run-in that names its content. |
| 6 | 127–128 | `Table~\ref{tab:related} positions nine\npublished systems against the four criteria that jointly define our claim` | Delete the announcement, state the criteria and the verdict: `Four criteria jointly define the claim: an agent's own choices, an exogenous payoff, a graded dose, and a minimum-distance projection. Of nine published repair systems, none has all four (Table~\ref{tab:related}).` |
| 7 | 209 | `This section applies, rather than proposes, a projection method.` | **Delete.** Roadmap plus negation. |
| 8 | 222–224 | `The full formulation, and the three method commitments governing budget exhaustion, the strict-preference margin, and per-output verification, are given in Appendix~\ref{app:method-detail}` | **Keep only this one** of the three appendix pointers, shortened: `The full formulation and the three method commitments are in Appendix~\ref{app:method-detail}.` |
| 9 | 231–232 | `the exact objective and constraint definitions are in Appendix~\ref{app:method-detail}` | **Delete.** Duplicate pointer, nine lines after #8. |
| 10 | 241–242 | `is addressed in Appendix~\ref{app:method-detail}` | **Delete the pointer**; the sentence already states the substantive answer after the colon. |
| 11 | 277 | `and is addressed separately in \S\ref{sec:method-nullop}.` | **Delete.** The target subsection begins two lines later. |
| 12 | 297–298 | `Figure~\ref{fig:pipeline} summarizes the full pipeline.` | **Delete.** Classic figure-announcement; the figure is on the same page and the caption says what it shows. |
| 13 | 366–368 | `Table~\ref{tab:discardbreakdown} breaks every reciprocal-framing session down by attempt outcome --- kept on the first attempt, rescued by a later retry, or still discarded after three attempts --- for both models.` | **Delete the entire sentence.** A verbatim restatement of the Table 2 caption (L380–382), same three-item list, same order, same words. Start the paragraph at `At 1.5B, retry-rescued sessions...`. |
| 14 | 374–375 | `We report first-attempt and residual post-retry discard rates as a first-class per-condition outcome for every cell.` | **Delete or move to Results.** Announces a reporting policy; the numbers are in Table 2. |
| 15 | 435 | `Figure~\ref{fig:doseresponse} shows the relationship split by model on shared axes.` | **Delete the announcement and cite the figure inside the claim.** Separately, this sentence *misdescribes the figure* — see §8 #1 and §14 #1. This is the highest-severity single entry in this category. |
| 16 | 445 | `Full detail in Appendix~\ref{app:payoff-audit}.` | Fold into the preceding sentence: `...once dose is included (Appendix~\ref{app:payoff-audit}).` *Stylistic preference; the competing convention allows standalone pointer sentences.* |
| 17 | 457 | `Statistics are in \S\ref{sec:results-c1}.` (caption) | **Delete.** Circular — the figure is cited only from inside `sec:results-c1`. |
| 18 | 464–467 | `\S\ref{sec:method-nullop} builds the control that closes this gap: ...` | Do not narrate the method section from inside Results. Replace: `The null operator (\S\ref{sec:method-nullop}) spends the identical $L_1$ budget as the real repair and shrinks every bundle toward the exogenous payoff's fixed optimum, using no GARP information.` |
| 19 | 479–482 | `\S\ref{sec:method-nullop} removes this by drawing an independent Cobb--Douglas weight ...` | Same defect, second occurrence, with the method section again as grammatical subject. Replace: `Experiment 2 draws an independent Cobb--Douglas weight $\alpha_s\sim\mathrm{Uniform}(0.05,0.95)$ per trace, over $K=20$ draws (\S\ref{sec:method-nullop}).` |
| 20 | 529 | `Single-trace illustration; the 85-trace comparison is in \S\ref{sec:results-c1}.` (caption) | **Delete.** Circular, plus a disclaimer the body already gave at L513–514. |
| 21 | 559–560 | `Table~\ref{tab:discardbreakdown} gives the finer-grained per-attempt breakdown these top-line numbers average over.` | Replace: `Table~\ref{tab:discardbreakdown} breaks the discards down by attempt.` |
| 22 | 637–638 | `This is a measurement design for asking whether repair helps in a given setting --- and, here, a documented instance where it does not ---` | Replace: `The design measures whether repair helps in a given setting. Here it does not.` |
| 23 | 648–649 | `This paper set out to measure whether restoring GARP-consistency in an LLM agent's own realized choices buys more exogenous payoff than the mechanical fact of displacement alone.` | Retrospective roadmap. Replace with the answer as the opening: `Restoring GARP-consistency in an LLM agent's own realized choices does not buy more exogenous payoff than displacement alone.` |
| 24 | 676 | `Full detail of the four-part adversarial audit summarized in \S\ref{sec:method-payoff}.` | **Delete the sentence.** `four-part` is visible from the four bold numerals; the § pointer is redundant with the main text's forward pointer; `adversarial` is process narration (§11). |
| 25 | 712–713 | `Full detail of the projection's exact formulation and implementation commitments, summarized in \S\ref{sec:method-projection}.` | **Delete.** Identical construction to #24 down to `Full detail of the` — the repetition makes it boilerplate. |
| 26 | 725 | `\textbf{Three method commitments, each carrying an explicit risk.}` | Announces a count and a shape, and the promise is honoured for only one of the three commitments (§14). Replace: `\textbf{Implementation commitments.}` |

## 3a. Paragraphs whose content is restated beneath them

1. **L108–122, the Contributions list, restates paragraphs 3–5 (L79–106) in the same order and near-identical words.** The clause `absent from every published axiom-enforcement result we are aware of` is **verbatim identical** at L79–80 and L113–114. Contribution (4) (L117–119) restates L97–103; contribution (5) (L119–122) restates L103–106, including `in the \emph{opposite} direction from an independently published ... finding` with `\emph{opposite}` italicized in both places. **Unique material that must survive:** `independently verified on every output` (L110); `fixed before any data collection` and the leakage / mechanical-confound checks (L111–112); the naming of `(Qwen2.5)` (L122). Everything else in L108–122 already exists above it.
2. **L127–130, the Related Work framing paragraph, is re-argued system by system at L158–200 and re-defined a second time in the caption at L134–136.** Unique content to keep: the four criterion names, `None occupies all four`, and the count `nine`.
3. **L366–375 (discard paragraph).** Sentence 1 (366–368) is fully restated by the caption at 380–382. Sentence 4 (372–374) restates its own first clause: `the first-attempt and retry-rescued groups sit much closer together, and the selection concern shows up more sharply at 1.5B than at 3B` — the second clause is the first read backwards.
4. **L461–467 (Results).** Its entire content is re-delivered by L469–477 (the result) and L533–536 (the verdict). Unique content: the severity-vs-geometry distinction only. Cut to two sentences.
5. **L676 and L712–713 are single-sentence paragraphs whose entire content is restated by the material beneath.** No sentence in either is unique. Both should go.

---

# 4. Trailing appositive qualifications

**77 instances doc-wide.** Several sentences carry two or three stacked. The pattern is heaviest in the Method (22) and the Introduction (15). Eight are outright **dangling or misattached modifiers** and are marked as such — those are grammar errors, not taste.

## 4a. Abstract and Introduction

| # | Line | Trailing text | Disposition |
|---|---|---|---|
| 1 | 43 | `; we decline a third as payoff-shopping` | **Delete from the abstract.** Move to Results or Limitations (§11). |
| 2 | 46–47 | `for the coherence--competence question, which remains open, and a discard-selection instrument-validity finding` | **Own sentence.** `The coherence--competence question remains open.` As written, the paper's most important epistemic hedge sits inside a relative clause in the abstract's last line. |
| 3 | 71–72 | `--- a projection applied \emph{post hoc} to a frozen agent, so nothing about its weights, training, or decoding changes across doses` | **Own sentence.** `The projection is applied post hoc to a frozen agent: nothing about its weights, training, or decoding changes across doses.` This is the identification argument and should not be an aside. |
| 4 | 76 | `, not a restatement of coherence` | **Delete** (§1 #12). |
| 5 | 82–83 | `, significantly, at both model scales, under two independently designed payoffs (\S\ref{sec:results-c1})` | **Three stacked qualifications on one verb.** Split: `...outperforms the real GARP-restoring repair on the exogenous payoff. The result holds at both model scales and under two independently designed payoffs (\S\ref{sec:results-c1}).` |
| 6 | 84 | `, as originally proposed,` | **Delete** — unspecifiable process reference (§11). |
| 7 | 86–87 | `, not as a null we happened to observe once` | **Delete** (§1 #15). |
| 8 | 94–95 | `, not as a second point on a shared dose curve across scale` | **Own sentence** (§1 #18). |
| 9 | 103 | `, quantifying how much a naive discard rule can distort a measured effect` | **DANGLING PARTICIPLE.** As written, the thing `quantifying` is `the discard rate itself` or `the more reliable signal`; the intended subject is the comparison between the naive and corrected estimates. Fix: `The gap between the naive and corrected estimates quantifies how much a naive discard rule can distort a measured effect.` |
| 10 | 105–106 | `, moving in the \emph{opposite} direction from an independently published finding in the same domain and model family at a larger scale, with no discard confound on either arm` | **Two stacked qualifications; split.** `...produces a large GARP-pass-rate collapse, with no discard confound on either arm. The collapse runs opposite to an independently published finding in the same domain and model family at a larger scale \citep{wang2025tactics}.` (Citation currently absent — §16.) |
| 11 | 110 | `, independently verified on every output rather than trusted from solver status alone` | **Own clause** (§1 #21). |
| 12 | 111–112 | `, audited adversarially for leakage and for the mechanical confound that larger violations simply have more room to improve` | **Keep as an appositive but drop the process verb:** `, checked for leakage and for the mechanical confound that larger violations have more room to improve`. |
| 13 | 113–114 | `--- absent from every published axiom-enforcement result we are aware of ---` | **Delete here.** Verbatim duplicate of L79–80. |
| 14 | 118–119 | `, corrected for by a stated retry protocol and reported per cell rather than pooled away` | Trim to `, corrected by a capped retry protocol and reported per cell`. |
| 15 | 120–122 | `, in the \emph{opposite} direction from an independently published single-turn-vs-multi-turn finding in the same budget-allocation domain and the same model family (Qwen2.5) at a larger scale` | **Own sentence**, and cite the finding. Currently a 30-word appositive hanging off a contribution bullet. |

## 4b. Related Work

| # | Line | Trailing text | Disposition |
|---|---|---|---|
| 16 | 164 | `lack a genuine degree parameter or Afriat machinery, on different objects:` | **Delete `, on different objects`.** The reader cannot tell which three objects, and the table already says. If they matter, name them: `on pairwise judgments, on judge scores, and on retrieval rankings respectively` (author to fill in). |
| 17 | 167–169 | `Two training-time systems, one altering the agent itself \citep{buchanan2026innate} and one not an LLM agent at all \citep{aguiar2026garpefm}, report no downstream comparison and a forecasting evaluation respectively.` | Two appositives suspend the subject across three lines before the verb arrives. Split: `\citet{buchanan2026innate} alters the agent itself at training time and reports no downstream comparison. \citet{aguiar2026garpefm} is not an LLM agent and is evaluated on forecasting.` |
| 18 | 172–173 | `both make the cycle-tolerant arm a strict superset model class, confounding coherence with capacity by construction` | The participial tail is the paragraph's real claim, demoted to an appositive. Promote: `... a strict superset model class. Coherence is therefore confounded with capacity by construction.` |
| 19 | 175–176 | `scored by an LLM judge, where ours acts post hoc and is exogenous` | Trailing contrast plus `where` used as a contrastive conjunction. Promote: `Ours acts post hoc on a payoff that is exogenous by construction.` |
| 20 | 177 | `as a training penalty argued a priori, never measured` | Trailing confession about someone else's paper. Promote: `... as a training penalty. The proposal is argued a priori and never measured.` |
| 21 | 178 | `ours is the empirical counterpart to a proposal that has circulated unrun.` | Trailing self-credit clause attached by semicolon. Convert or delete (§10, §16). |
| 22 | 185–186 | `the same distinction that disposes of \citet{yamin2026elicited}'s isotonic repair (worse in 14 of 16 cells)` | Trailing tail that smuggles in a new system *and* a new number. Promote: `The same distinction applies to \citet{yamin2026elicited}'s isotonic repair.` See §13 #3 for the number's status. |
| 23 | 189–190 | `which is why we carry a null-operator control neither published negative had.` | Trailing design-justification hung off a semicolon-joined independent clause, and it duplicates L113. Promote or delete: `We therefore carry a null-operator control, which none of the three had.` |
| 24 | 194 | `--- occupying two of our three legs without Afriat machinery;` | Trailing scorecard tacked onto a description, and it contains a **count error** (§13 #2). Promote and correct: `They meet two of the four criteria; they use no Afriat machinery.` |
| 25 | 196 | `corroborates our manipulation choice, anchored in \citet{wang2025tactics}, who find ...` | **DANGLING MODIFIER.** `anchored in \citet{wang2025tactics}` attaches to `our manipulation choice`, but the intended anchor is the finding, and the relative `who find` then jumps back over two nouns. Split: `... corroborates our manipulation choice. \citet{wang2025tactics} find that \emph{format} moves the Afriat index in the same domain and model family (Qwen2.5) at 7B.` |
| 26 | 199–200 | `--- not a replication, since which format is more degrading reverses ...` | See §1 #36. |

## 4c. Method and Experimental design

| # | Line | Trailing text | Disposition |
|---|---|---|---|
| 27 | 205–206 | `, applied and independently verified` (heading suffix) | **Delete** — §7 #3. |
| 28 | 210–212 | `, adopted here on an LLM agent's own choice sequence and verified independently on every output` | **Delete as duplicative** — independent verification gets its own sentence at L224–226. |
| 29 | 229 | `, with uniform weights, keeping the program a pure MILP` | Promote: `Weights are uniform, which keeps the program a pure MILP.` |
| 30 | 234–236 | `--- the same style of graded, minimum-cost severity measure as \citet{dean2016measuring}, applied here to an LLM's own choices and paired with an exogenous behavioral payoff rather than left as a standalone index.` | **Stacked double appositive** — an em-dash clause containing a comma-appositive containing a `rather than`. Promote and cut: `The dose is the same style of graded, minimum-cost severity measure as \citet{dean2016measuring}.` |
| 31 | 238 | `, recorded only as an upper-bound diagnostic` | **Delete** (duplicate of `sanity ceiling` seven words earlier). |
| 32 | 251–252 | `, rewarding the agent for resembling its own revealed preferences rather than measuring anything external to them` | **Delete** — restates `circular`. |
| 33 | 256–257 | `--- a function of prices and income alone, never of the agent's observed or projected bundle.` | Promote and shorten: `$x^*_t$ depends only on prices and income.` |
| 34 | 266–267 | `but without a placebo of matched size cannot separate an alignment-specific effect from a generic fine-tuning effect` | **DANGLING MODIFIER.** `without a placebo of matched size` has no local subject; the reader must carry `\citet{ouyang2024aidecisionmaker}` across two conjuncts and 25 words. Fix: `Separating an alignment-specific effect from a generic fine-tuning effect requires a placebo of matched size, which that design lacks.` |
| 35 | 267 | `--- the same separation our design is built to make.` | Promote: `Our design makes that separation.` As a trailing clause it dangles off a sentence whose subject is Ouyang et al. |
| 36 | 288 | `and does not, in general, restore consistency` | Promote with a number (§1 #58). |
| 37 | 295 | `, never pooled` | Promote: `The two are reported separately.` |
| 38 | 296–297 | `, reported only as an upper bound since it uses information no real repair algorithm has` | Promote: `The oracle null is an upper bound: it uses the per-trace $\alpha_s$.` |
| 39 | 319–320 | `(the headroom model, per a pilot with measurable within-condition coherence variation)` | Promote. A pilot justification for model choice is a design decision, not a parenthetical. |
| 40 | 336 | `, the direction our own baseline already uses.` | **MISATTACHED APPOSITIVE — and false as attached.** It attaches to `the opposite direction`, i.e. multi-turn, but the baseline is single-turn (L328). See §13 #7. |
| 41 | 336–337 | `, whose role is a null-effect control rather than a second scale point.` | Promote: `The 3B model is a null-effect control.` |
| 42 | 343–344 | `--- unlike a pilot's single shared set, needed because the main experiment targets independent between-condition replication.` | Promote and shorten: `Independent seeding supports between-condition replication.` |
| 43 | 346–347 | `, common under grid-sampled or rounded prices` | **Keep** — it names when the pathology bites. *Stylistic preference: the competing convention makes it a subordinate clause, `which is common under...`.* |
| 44 | 350–351 | `, reported rather than papered over` | **Delete** (editorializing). |
| 45 | 358–359 | `--- standard practice, and one this paper measures the consequences of directly.` | **DANGLING.** `one` attaches to `the pilot's own naive handling`, so the sentence says this paper measures the consequences of the pilot's handling, not of the general practice. Split: `Silent discarding is standard practice. This paper measures its consequences.` |
| 46 | 359–360 | `, true regardless of whether projection helps, hurts, or does nothing downstream.` | **Delete.** |
| 47 | 370–372 | `--- consistent with, though not conclusive given the small residual sample, some of the same selection concern the pilot's naive handling raised persisting at a smaller scale even after correction.` | **The worst trailing clause in the manuscript:** 33 words, an interrupting concession inside the appositive, and a dangling participle (`persisting`) 20 words from its subject (`concern`). Replace with two sentences: `The residual sample is too small ($n=6$, 3 measurable) to be conclusive. The pattern is consistent with the pilot's selection concern surviving the retry correction at reduced magnitude.` |
| 48 | 384–385 | `, with $0$ for any already-GARP-consistent trace` (caption) | **Move to the Method, near L232** — a computational convention affecting every dose number in the paper, stated only in a caption, in a subordinate clause. See §8 and §13 #10, where this convention turns out to govern Table 3 as well. |

## 4d. Results

| # | Line | Trailing text | Disposition |
|---|---|---|---|
| 49 | 462–464 | `--- it says nothing about whether restoring GARP-consistency \emph{specifically}, rather than merely displacing choices toward some interior point, is what buys the payoff gain above.` | Promote: `It does not say whether GARP-restoration or displacement buys the gain.` |
| 50 | 488 | `, reported for completeness rather than as the primary comparison` | **Delete** (redundant with `primary` at L483). |
| 51 | 491–492 | `--- a real but more modest signal, not distinguishable from the draw-to-draw noise the 20 draws themselves already show.` | Promote and quantify: give the across-draw SD of $r$. |
| 52 | 499–500 | `, exactly the researcher-degree-of-freedom problem an exogenous payoff was introduced to rule out.` | **Move to Limitations.** Methodological defence, not a result. |
| 53 | 505–506 | `, more strongly than it predicts the real repair's own gain in either.` | Promote and quantify: `It predicts the real repair's own gain less strongly ($r=$..., $r=$...).` A comparative with no second term (§13). |
| 54 | 510–512 | `--- read as partial, not conclusive, support for an ``escape a bad start'' mechanism rather than pure centering, offered as a discussion-level hypothesis rather than a load-bearing result with its own significance test.` | **DANGLING MODIFIER** — `read as` has no grammatical subject; it attaches to `the same extremity-advantage (mean $r=0.624$)`, which is not what is being read. Delete and replace with one sentence (§1 #76). |
| 55 | 520–522 | `, hand-audited in Appendix~\ref{app:payoff-audit}); every plotted quantity is recomputed by re-solving the projection MILP.` | **Move to the appendix.** A verification-process statement inside a figure caption. |
| 56 | 529 | `Single-trace illustration;` | **Delete** (caption). |
| 57 | 545–547 | `--- the same near-1 compression the pilot flagged, and a further case of GARP pass rate being the sensitive instrument for framing/format disruption while CCEI understates it.` | Promote: `CCEI compresses near 1, as the pilot found; GARP pass rate detects the disruption and CCEI does not.` The trailing form buries the section's most reusable observation. (See §14 for the `understates it` overreach.) |
| 58 | 552–553 | `--- smaller than the pilot's unretried 52\%, but the pattern is unchanged: reciprocal framing produces far more discards than any other condition, including the \emph{other} 1.5B manipulation (multiturn, 0\%).` | Promote; split at the em-dash. The pilot comparison and the cross-condition claim are two facts, and the comparison is not like-for-like (§16). |
| 59 | 566–568 | `--- a larger drop than reciprocal framing produced at 1.5B, with \emph{zero discards on either arm}.` | Promote; two facts glued on. The comparative is also unsound — reciprocal framing at 1.5B produced no detectable drop (§13 #12). |

## 4e. Limitations, Broader impacts, Conclusion

| # | Line | Trailing text | Disposition |
|---|---|---|---|
| 60 | 622–623 | `is a fourth, in the narrower sense that it failed to induce the coherence variation it was designed to.` | Confession tacked to a count. Promote: `Our reciprocal-framing manipulation at 1.5B (\S\ref{sec:results-framing}) is a fourth. It failed to induce the coherence variation it was designed to induce.` (Also fixes the stranded `designed to` — §16.) See §13 #16 for the count problem. |
| 61 | 626 | `--- C2 remains open, not settled ---` | Em-dash interruption between the negation and its `only that` completion; the reader loses the thread across nineteen words. Promote (§1 #89). |
| 62 | 627 | `this paper's own attempt to find a positive relationship, net of displacement, did not succeed` | `net of displacement` is load-bearing but buried mid-clause. Move forward: `net of displacement, this paper's attempt to find a positive relationship did not succeed.` |
| 63 | 636 | `similarly turned out, once corrected, to have no measurable effect` | **DANGLING/MISATTACHED.** `once corrected` grammatically attaches to `The reciprocal-framing manipulation`, but what was corrected was the discard selection in the *analysis*. Fix: `Correcting the discard selection removes the reciprocal-framing manipulation's apparent effect on coherence entirely (\S\ref{sec:results-framing}).` |
| 64 | 638 | `--- and, here, a documented instance where it does not ---` | Parenthetical concession inside a sentence that is already conceding. Promote: `Here it does not.` |
| 65 | 652–653 | `on that same payoff, significantly, at both model scales, under two independently designed payoffs.` | Three trailing qualifications in a row after the verb. Relocate: `at both model scales and under two independently designed payoffs, a distance-matched, GARP-blind null operator significantly outperforms the real repair on that same payoff.` |
| 66 | 653 | `, as originally proposed,` | Process record inserted as an appositive (§11). Delete: `C1 is not supported.` |
| 67 | 655 | `offers a candidate explanation without fully resolving it` | Trailing hedge with an unrecoverable antecedent (`it` = the explanation? the advantage? the mechanism?). Replace: `offers a candidate explanation for the null's advantage but does not establish it.` |
| 68 | 657 | `this is the first attempt we know of to measure it` | Trailing epistemic hedge on a priority claim. See §14 #9 for the verification of this claim against Related Work. |

## 4f. Appendix

| # | Line | Trailing text | Disposition |
|---|---|---|---|
| 69 | 682 | `--- a plausible leakage channel on first read ---` | **Delete.** A confessional aside about the authors' own reading process (§11). |
| 70 | 684–685 | `, never to steer the solution` | **Delete** (§1 #98). |
| 71 | 690–691 | `, ruling out a population-level mechanical link between coherence and payoff score` | Promote and weaken to what the test supports (§1 #99, §13 #21). |
| 72 | 697–699 | `--- the sign of the outcome tracks a geometric quantity the projection objective never references, evidence against the mechanism being a disguised optimization toward the payoff target.` | One sentence carrying a measurement, an interpretation of the measurement, and an interpretation of the interpretation. Split off the last: `This is evidence against the projection acting as a disguised optimization toward the payoff target.` |
| 73 | 703 | `--- a genuine ceiling-effect confound` | Promote: `This is a ceiling-effect confound.` Delete `genuine` (§5 #97). |
| 74 | 705–706 | `, attenuated only slightly from the unconditional $r=0.821$` | Promote: `The unconditional correlation is $r=0.821$.` Let the two numbers show the attenuation. |
| 75 | 733–734 | `, never trusted from solver optimality status alone` | **DANGLING.** As written the participial qualification attaches to `the same combinatorial Warshall-closure GARP check`, so it reads as though the *check* is not trusted from optimality status; the intended subject is the returned $\tilde{x}$. **Delete.** |
| 76 | 748 | `, absorbed into the binary comparison indicators above rather than eliminated,` | **DANGLING MODIFIER.** The participle attaches to `which revealed-preference comparisons to give up`, but the thing absorbed into the indicators is the *decision*. Fix as its own sentence: `That decision is absorbed into the binary comparison indicators $U_{t,v}$ rather than eliminated.` |
| 77 | 748–749 | `, which is why no distance-minimization guarantee analogous to the convex case is claimed` | Promote to its own sentence. A 93-word sentence should not end by explaining itself. |

---

# 5. Softening adverbs and undefined qualifiers on binary claims

**106 flagged doc-wide; keep 8.** The hedge profile is unusual: the standard hedge vocabulary (`arguably`, `somewhat`, `perhaps`, `seemingly`, `essentially`, `virtually`, `largely`, `relatively`, `effectively`) is almost entirely absent — searched across all 754 lines. What the paper has instead is **intensifiers and undefined argumentative adjectives**: `genuine`/`genuinely` 6 times (L164, L166, L263, L509, L703, L731); `real` as an adjective on the paper's own results 5 times (L440, L475, L491, L535, L651); and roughly twenty adjectives (`large`, `clean`, `adequately`, `substantially`, `much`, `far`, `almost none`, `first-class`) standing in for numbers the paper already has in its own tables.

## 5a. Delete, or replace with the number

| # | Line | Exact text | Fix |
|---|---|---|---|
| 1 | 18 | `\emph{Actually}` (title) | Delete. *Stylistic preference; the competing convention holds a slightly combative title helps a workshop paper get read. I would still cut it.* |
| 2 | 54 | `will frequently violate` | Replace with the measured rate, or `violates`. `frequently` hedges the paper's own headline quantity. |
| 3 | 59 | `applies it to GPT-family models directly` | Delete `directly` — `without a repair step` in the same sentence says it. |
| 4 | 60 | `whether they satisfy classical rationality axioms at all` | Delete `at all`. |
| 5 | 61 | `repairs exactly this kind of inconsistency` | Delete `exactly`. |
| 6 | 68 | `where it can be answered cleanly` | Sentence deleted per §3 #1. If retained, `cleanly` must be defined. |
| 7 | 82 | `significantly,` | Replace with the p-value (§2 #2). |
| 8 | 85 | `does on its own` | Delete. |
| 9 | 92 | `run together so that the identification is clean` | `clean` is undefined and repeats `cleanly` at L68. Replace: `run together so that dose is not confounded with model capacity or training.` |
| 10 | 94 | `at a scale with almost none` | Replace with the number the paper already has: `at 3B, where the pilot found mean baseline CCEI 0.99`. |
| 11 | 98 | `a large apparent effect` | `large` is undefined and contradicts the next clause. See §5b #1 and §13 #1. |
| 12 | 104 | `a large GARP-pass-rate collapse` | Give the number: 0.40 → 0.10. |
| 13 | 112 | `larger violations simply have more room to improve` | Delete `simply`. |
| 14 | 116 | `GARP-restoration specifically` | Delete `specifically`. |
| 15 | 120 | `a large GARP-pass-rate collapse` | Second instance of the same undefined `large` in 16 lines; give the number or delete the sentence as a duplicate (§14 #2). |
| 16 | 160 | `We concede the minimum-distance priority unqualified` | Delete `unqualified`. A concession is binary; the intensifier announces the author's magnanimity. |
| 17 | 164 | `lack a genuine degree parameter` | Delete `genuine`, or define: `lack a continuous degree parameter`. |
| 18 | 166 | `has a genuinely exogenous payoff` | Delete `genuinely`. The table cell at L147 already says `yes`. Note the pairing with #17 two lines earlier. |
| 19 | 168 | `not an LLM agent at all` | Delete `at all`. |
| 20 | 182 | `never reaches acceptable levels across eight datasets` | `acceptable` is an undefined threshold carrying the whole argumentative load. Replace with the figure: `never exceeds a test--retest reliability of [X] across eight datasets`. As written a reviewer cannot check the claim. |
| 21 | 189 | `all point the same adverse way` | Replace: `all report that enforcing axioms failed to improve the outcome measured.` |
| 22 | 197 | `at a larger scale` | Undefined comparative; the paper knows the number (L200 says `their 7B model`). Replace: `at 7B`. |
| 23 | 198 | `drops CCEI by up to $0.241$` | `up to` hedges a maximum that is already a maximum. Replace: `drops CCEI by $0.241$ at its largest cell`. |
| 24 | 218 | `The naive Afriat-multiplier formulation` | `The Afriat-multiplier formulation`. *Stylistic preference: `naive` is a term of art in optimization for the direct encoding; the competing convention keeps it.* |
| 25 | 226 | `the same combinatorial check used throughout` | Name it: `the Warshall-closure GARP check`. `throughout` is unlocatable (§12). |
| 26 | 233 | `comparable across sessions without further normalization` | **Keep** — `further` does real work; there is prior normalization by construction. |
| 27 | 263 | `A genuinely exogenous, real-world payoff of this kind is rare in this literature` | Delete `genuinely`; quantify `rare`, or name the one or two papers that have one. |
| 28 | 269 | `We audited this design adversarially` | Delete `adversarially` — undefined, and the author scoring their own rigour (§11). |
| 29 | 272 | `larger-dose traces simply start worse` | Replace: `larger-dose traces start with lower payoff`. |
| 30 | 275–276 | `could reward mere displacement` | Replace: `could reward displacement alone`. |
| 31 | 287 | `exactly matches the real projection's own dose` | **Keep `exactly`** — the defining constraint of the control. Delete `own`. |
| 32 | 288 | `does not, in general, restore consistency` | Replace with the count (§1 #58). A categorical verb hedged by a frequency qualifier in one clause leaves the reader unable to tell whether it *ever* restores consistency. |
| 33 | 289 | `the same payoff function used everywhere else` | Replace: `the payoff of \S\ref{sec:method-payoff}` — unlocatable, and falsified two lines later by the second payoff (§13 #6). |
| 34 | 292 | `a second, independently designed payoff` | `a second payoff`. `independently designed` is an unverifiable process claim (§11), and it is contradicted at L495–496 (§5b #10). |
| 35 | 297 | `information no real repair algorithm has` | `real` is doing argumentative work with no definition. |
| 36 | 318 | `run entirely on local compute at zero API cost` | `run on local compute`. `entirely` is redundant with `locally-hosted` in the same clause. |
| 37 | 319–320 | `per a pilot with measurable within-condition coherence variation` | `measurable` is an adverbial dodge — everything is measurable; the question is magnitude. Give the range. |
| 38 | 320–321 | `finding almost no headroom --- mean baseline CCEI 0.99` | Delete `almost no headroom`; the number follows immediately. |
| 39 | 322 | `a reproducible multi-model-residency crash` | Give the count, or delete `reproducible`. |
| 40 | 325 | `$\approx$2.1 hours wall-clock` | **Keep.** *Stylistic preference: wall-clock times are conventionally approximate.* |
| 41 | 330 | `the strongest manipulation identified in the pilot` | **Keep** — a superlative over a defined set. |
| 42 | 341 | `draws its own fresh $T=25$, $K=2$ budget set` | `its own` and `fresh` say the same thing, and `independent replicates` in the same clause says it a third time. Replace: `draws a fresh $T=25$, $K=2$ budget set`. |
| 43 | 345 | `also avoid a known pathology` | `known` is doing citation's job. Replace: `a pathology documented by \citet{andrews2026revealed}`. |
| 44 | 350 | `but is explicitly underpowered` | Delete `explicitly` — it modifies the author's disclosure, not the design. |
| 45 | 358 | `silently discarded` | **Keep** — `silently` is load-bearing and is the whole point of the subsection. |
| 46 | 358 | `the pilot's own naive handling` | `the pilot's handling`. `own` and `naive` are both editorial. |
| 47 | 369 | `a substantially lower GARP pass rate` | Replace with the numbers already in Table 2: `a GARP pass rate of 0.1429 against 0.4706`. |
| 48 | 370 | `scores lowest on the handful that can be measured` | Replace: `scores lowest on the 3 measurable slots` — and see §13 #5, where the claim is contradicted by the table it describes. |
| 49 | 372 | `sit much closer together` | Replace with the differences: `differ by 0.0118 in CCEI and 0.143 in GARP pass rate`. |
| 50 | 374 | `as a first-class per-condition outcome` | Delete `first-class`. |
| 51 | 432 | `Across all 85 GARP-violating traces` | Delete `all`. |
| 52 | 438 | `might simply start from worse raw payoff` | Delete `simply`. |
| 53 | 443 | `finds dose highly significant ($t=11.4$, $p<10^{-16}$)` | Delete `highly` — $t=11.4$ is the claim. |
| 54 | 463–464 | `merely displacing choices toward some interior point` | Delete `merely` and `some`. |
| 55 | 469 | `outperforms the real repair by roughly $2.4\times$` | Delete `roughly`. 0.0220/0.0091 = 2.42; the ratio is computed, not estimated. |
| 56 | 475 | `dose retains real information beyond what the null predicts` | Delete `real`. |
| 57 | 486 | `An oracle null ... does better still` | Replace with the number: `... wins 80.4\% of traces`. |
| 58 | 490 | `to a mean $r\approx0.37$` | Give the value: `$r=0.37$` (§13 #23). |
| 59 | 503 | `a stable measure of the raw bundles` | Delete `stable`, or define what stability means here. |
| 60 | 504 | `predicts the null's advantage strongly` | Delete `strongly`; $r=0.679$ is there. |
| 61 | 506 | `does not cleanly separate` | Delete `cleanly`. |
| 62 | 507 | `regardless of exactly where` | Delete `exactly`. |
| 63 | 509 | `a genuinely different, per-trace-varying point` | Delete `genuinely` — `per-trace-varying` already does the work. |
| 64 | 510 | `shows essentially the same extremity-advantage (mean $r=0.624$)` | Replace: `shows the same extremity-advantage to within 0.01 (mean $r=0.624$ vs.\ 0.631)`. |
| 65 | 513 | `illustrates the same idea concretely` | Delete `concretely`. |
| 66 | 515 | `are precisely the extreme-share rounds` | Delete `precisely`. |
| 67 | 527 | `leaving the other 16 at a near-corner $s=0.99$` | **Keep `near-corner`** — descriptive of $s=0.99$, not a hedge. |
| 68 | 535 | `The raw dose--response relationship ... is real` | Replace: `... holds`. |
| 69 | 544 | `CCEI moves much less` | Delete `much`, or give the effect sizes side by side. |
| 70 | 550 | `does not survive proper correction for discard-selection` | Delete `proper` — an argument, not a description. |
| 71 | 552 | `produces far more discards than any other condition` | Give the other conditions' rates. |
| 72 | 556 | `the pilot's own naive estimate` | Replace: `the pilot's uncorrected estimate`. A judgment on the paper's own earlier work with no definition attached. |
| 73 | 566 | `while CCEI barely moves (0.9522 vs.\ 0.9540, $p=0.91$)` | Replace: `while CCEI does not move` — the numbers are already in the parenthesis. |
| 74 | 601–602 | `minimum detectable effect $\approx2.5\times$ the pilot's` | An MDE is a computed quantity; `$\approx$` hedges an exact calculation. |
| 75 | 602 | `$N\approx111$--$161$` | Doubly hedged: an approximation sign on a range. `$N=111$--$161$`. |
| 76 | 603–604 | `the pass-rate metric is adequately powered throughout` | `adequately` is doing the argumentative work of a power calculation. Give the number (L348 has it: $\ge0.999$) or delete the adverb. |
| 77 | 616 | `the first's single, globally-identical optimum turned out exploitable` | `turned out` narrates discovery. Replace: `the first payoff's single, globally identical optimum is exploitable by a GARP-blind operator`. |
| 78 | 626 | `is negative in general` | **Keep.** `in general` is the scope quantifier the sentence is about. |
| 79 | 632 | `merely displaces choices toward an interior point` | Delete `merely`. |
| 80 | 634 | `exactly the confound this paper's control was built to catch` | Delete `exactly` (and see §13 #18 for the verb). |
| 81 | 635 | `similarly turned out` | Delete `similarly` (the parallel is visible) and `turned out`. |
| 82 | 636 | `to have no measurable effect on the coherence` | **Keep `measurable`** — the honest scope of a null. |
| 83 | 636–637 | `the coherence it was thought to disrupt` | `thought` by whom? Replace: `the coherence it was designed to disrupt`. |
| 84 | 640 | `silently drops disruption-caused failures` | `silently` does real work but is unanchored. Replace: `drops disruption-caused failures without recording them`. |
| 85 | 641–642 | `risks underestimating exactly the manipulations that matter most` | Delete `exactly`; `that matter most` is undefined. Replace: `underestimates the manipulations with the largest disruption effect`. |
| 86 | 651 | `a real, monotone raw dose--response relationship` | Delete `real` — contrasted against nothing at that point in the sentence. |
| 87 | 652 | `significantly,` | Interjected between commas mid-predicate in the Conclusion, in a paper whose first limitation is about being underpowered. Attach the number or drop the word. |
| 88 | 655 | `without fully resolving it` | Delete `fully`. |
| 89 | 658 | `or mere displacement magnitude` | Delete `mere` (§1i). |
| 90 | 664 | `are exactly what this literature should surface` | Delete `exactly` and the clause (§10). |
| 91 | 682 | `a plausible leakage channel` | Delete the whole clause (§4 #69). |
| 92 | 684 | `used only to log` | **Keep `only`** — exclusion work, not hedging. |
| 93 | 690 | `GARP-consistency status alone does not predict` | Delete `alone` — nothing else is in the model. |
| 94 | 693 | `spanning the full dose range` | Delete `full`; five points cannot span a full range, and the numbers follow immediately. |
| 95 | 694 | `were inspected directly` | Delete `directly` — `inspected` already means this. |
| 96 | 701–702 | `Larger-dose traces do start ...` / `worse-starting traces do have more room` | Delete both emphatic `do`. |
| 97 | 703 | `a genuine ceiling-effect confound` | Delete `genuine` — a confound is or is not one. |
| 98 | 705–706 | `attenuated only slightly` | Delete `only slightly`; 0.784 against 0.821 is the evidence. |
| 99 | 706–707 | `the dose coefficient is highly significant` | Delete `highly`. Significance is a threshold verdict. |
| 100 | 707 | `raw payoff's own coefficient` | Delete `own`. |
| 101 | 712 | `the projection's exact formulation` | Delete `exact` (sentence deleted anyway per §3 #25). |
| 102 | 715 | `The naive formulation parameterizes` | Replace: `A formulation parameterized with Afriat multipliers` — `naive` editorializes about work the paper did not do. |
| 103 | 730–731 | `can read a distance of exactly zero` | **Keep `exactly`** — the claim is precisely that the number is 0 and not 0-plus-epsilon. |
| 104 | 731 | `genuinely violating data` | Delete `genuinely` — data violate GARP or they do not. |
| 105 | 733 | `used everywhere else` | Name the place (§11, §12). |
| 106 | 734 | `were independently re-verified` | Delete `independently` here — the same sentence says `verified independently` nine words earlier. |

## 5b. Internally contradictory or self-cancelling pairs

1. **L98–100 — the highest-severity contradiction in the manuscript.** `produced, in a pilot run, a large apparent effect that disappears once discard-selection is corrected` immediately followed by `the pilot's naive estimate and the corrected main-experiment estimate are both statistically indistinguishable from zero`. `large` and `indistinguishable from zero` describe the same pilot estimate. **VERIFIED AGAINST THE FULL DOCUMENT:** the only pilot CCEI number the paper ever reports is `+0.0169 ($p=0.66$)` at L556. No `large apparent effect` on CCEI exists anywhere in the 754 lines. The two clauses cannot both be true as written. See §13 #1.
2. **L83 vs. L94–95.** `at both model scales` generalizes across scale; `not as a second point on a shared dose curve across scale` forbids it. See §14 #4.
3. **L164 vs. L166.** `a genuine degree parameter` / `a genuinely exogenous payoff` two lines apart — self-cancelling by proximity. Cut both.
4. **L198–199.** `Our opposite manipulation finds the opposite direction` — `opposite ... opposite` in six words. Rewrite: `Reversing their manipulation reverses the sign: GARP pass rate falls from 0.40 to 0.10.`
5. **L288.** `does not, in general, restore consistency` — a categorical verb hedged by a frequency qualifier in the same clause.
6. **L491–492.** `a real but more modest signal, not distinguishable from the draw-to-draw noise` — if it is not distinguishable from noise, it cannot be asserted as real. Pick one.
7. **L510–511.** `shows essentially the same extremity-advantage` immediately downgraded to `partial, not conclusive`. One of the two is wrong.
8. **L544–545.** `reaching only borderline significance (0.9900 vs.\ 0.9713, $t$-test $p=0.0508$)` — "borderline significance" at a stated $\alpha$ is a contradiction in terms. Replace: `does not reach significance ($p=0.0508$)`. **The single most reviewer-visible hedge in the Results.**
9. **L469 vs. L476–477.** `by roughly $2.4\times$` and `more than twice the payoff` — the same ratio hedged in two directions within one paragraph. Keep `2.4$\times$` once.
10. **L495 vs. L496.** `Two independently designed, independently motivated payoffs --- one the paper's original, one built specifically to remove the first one's known exploitable structure`. The second payoff's stated motivation *is* the first payoff. `independently motivated` is contradicted by the apposition that follows it, in the same sentence.
11. **L660–661.** `collapsed GARP pass rate in the opposite direction from a published finding` — `collapsed` is a magnitude verb, `in the opposite direction` is a sign statement. One of the two is wrong. If the sign is the finding: `moved GARP pass rate in the direction opposite to that reported by \citet{wang2025tactics}`.

## 5c. Adjectives and adverbs doing argumentative work with no definition behind them

Each asks the reader to accept a standard the paper never states. Ranked by how load-bearing the undefined word is.

| Line | Phrase | The question the text never answers |
|---|---|---|
| 731 | `We verified the reported distance is **stable** across $\gamma \in \{10^{-2},\ldots,10^{-6}\}$` | **The most load-bearing unquantified word in the paper.** Stable by what criterion — a tolerance, a maximum relative change? The whole $\gamma$ commitment rests on it. |
| 39 vs. 81 | `a fixed **center**` vs. `a fixed **interior point**` | Are these the same object? A reader cannot tell (§12). |
| 43, 498, 618 | `payoff-shopping` | Coined at L43, used three times, never defined. |
| 44 | `Trace extremity` | Used in the abstract as if defined; defined only at L502–503, then used bare again in the Conclusion at L655. |
| 46 | `capacity-deconfounded identification strategy` | Never unpacked; the nearest gloss (L65–66) uses a different noun. |
| 46–47, 626, 656 | `the coherence--competence question` | The Introduction never uses the word `competence`. |
| 68, 92 | `cleanly` / `clean` | What makes the setting clean, and the identification clean? |
| 80–81 | `an operator that knows nothing about GARP` | Anthropomorphic for a formal object. Replace: `an operator whose output does not depend on the GARP violation structure`. This matters because the paper's whole argument is that the control is formally blind. |
| 111 | `audited adversarially` | Adversarial how, by whom, against what? |
| 118 | `a stated retry protocol` | Stated where? The same object is `a capped retry protocol` at L99 (§12). |
| 130 | `a **formal** minimum-distance projection` | What makes a projection formal? Either the word is empty or it means "with a proved optimality property" — say that. |
| 158, 180 | `the **sharpest** vocabulary collision` / `The **sharpest** objection` | Sharpest on what axis, against which competing objections? |
| 176, 192 | `Our **closest** theoretical neighbour` / `The **closest** neighbour on the economics side` | Two "closest" objects, no distance defined; the second implicitly concedes the first was not closest. |
| 182 | `acceptable levels` | Whose acceptability criterion? |
| 189 | `the same **adverse** way` | Adverse to what? |
| 319–320 | `measurable within-condition coherence variation` | Everything is measurable; the question is magnitude. |
| 345 | `a **known** pathology` | Known to whom — the citation does this job. |
| 349 | `$\ge0.80$ down to $\sim$60\% **attenuation**` | Attenuation of what, relative to what baseline? Undefined, and it is carrying a power claim. |
| 374 | `first-class` | Programming vocabulary as an emphasis marker (§11). |
| 437 | `stronger at the **headroom model**` | `headroom model` is used at L319 and L437 and never defined; `headroom` recurs bare at L609 and L611. Replace with `at 1.5B`. |
| 483 | `the primary, **information-fair** null` | What makes a null information-fair? Defined nowhere. |
| 495 | `independently **motivated**` | Contradicted by the next clause (§5b #10). |
| 503 | `a **stable** measure` | Stable across what? |
| 630–631 | `as a **default** decision-quality intervention` | `default` is the operative word in the paper's only policy claim and is undefined. Replace: `as a routine intervention applied without a matched control`. |
| 663 | `a **well-controlled** negative` | The paper self-grading. Replace: `a negative result with a distance-matched null control`. |
| 678 | `shared **derived quantity**` | Appears once, in a bold lead, carrying the whole claim of part (1). Undefined. |
| 684 | `an upper-bound **sanity ceiling**` | Not a term of art; reads as an internal name (§11). Replace: `an upper bound on the reported distance`. |
| 742 | `the **closest** published structural analogue` | Closest by what measure, among what searched set? |

---

# 6. Sentences beginning with "What"; clefts and expletives

**Four literal `What` constructions, and one of them appears twice, 500 lines apart.**

| # | Line | Exact text | Replacement |
|---|---|---|---|
| 1 | 18 | `What Does Repairing Choice Inconsistency Actually Buy?` (title) | *Stylistic preference, not error.* An interrogative title is a normal workshop convention. Flagged here only so the `Actually` (§5 #1) is not lost. |
| 2 | 64–65 | `What none of them establishes is a \emph{dose}: how much better, as a function of how much repair was needed` | `None of them establishes a \emph{dose}: how much better, as a function of how much repair was needed` |
| 3 | 90 | `What has not been done is the conjunction:` | `The conjunction is new:` |
| 4 | 241 | `\textbf{What can be guaranteed, and what cannot}, relative to the closest published structural analogue \citep{wang2026poise}, is addressed in Appendix~\ref{app:method-detail}:` | A cleft *used as a bold run-in heading*, with 12 words of interrupting material between subject and verb. Replace: `\textbf{Guarantees.} Because the GARP-consistent set is a union of polyhedra rather than a single convex set, we claim no distance-minimization guarantee analogous to a convex-cone projection \citep{wang2026poise}.` |
| 5 | 656 | `What survives is the paper's identification argument (C2):` | `The paper's identification argument (C2) survives:` |
| 6 | 663–664 | `are exactly what this literature should surface by default rather than paper over` | Free-relative `what` clause closing the paper. Delete (§10). |
| 7 | 742 | `\textbf{What can be guaranteed, and what cannot.}` | **Second occurrence of the identical construction.** A double-`What` cleft *and* a paired rhetorical device inside a single heading. Replace: `\textbf{Scope of the guarantee.}` |

**Expletive and pseudo-cleft constructions doing the same emphasis-by-postponement work:**

| # | Line | Exact text | Replacement |
|---|---|---|---|
| 8 | 35–36 | `is what any reported gain comes from` | `...whether the reported gains come from restoring coherence or from displacement toward an interior point.` |
| 9 | 79 | `That relationship turns out not to isolate what it was built to isolate.` | Not a cleft, but the same evasive shape: the real content is deferred to the next sentence. `The design does not identify the effect of coherence restoration.` |
| 10 | 83–84 | `This is the paper's central finding:` | Expletive `This is`. Delete entirely (§2 #3). |
| 11 | 116–117 | `is what buys the exogenous payoff gain` | `...does not show that GARP-restoration buys the exogenous payoff gain.` |
| 12 | 180 | `The sharpest objection is psychometric, and it is in \emph{PNAS}.` | Expletive `it is` plus predicate-nominative framing. Replace the whole lead with `\textbf{Psychometric reliability.}` and let \citet{nitsch2022reliability} open the sentence. |
| 13 | 185–186 | `the same distinction that disposes of \citet{yamin2026elicited}'s isotonic repair` | Pseudo-cleft on a bare definite noun — *which* distinction? The reader must reconstruct it from L184. Replace: `Repair by construction rather than by re-presentation also separates ours from \citet{yamin2026elicited}'s isotonic repair.` |
| 14 | 189–190 | `which is why we carry a null-operator control` | Explanatory cleft tail. `We therefore carry a null-operator control.` |
| 15 | 192 | `The closest neighbour on the economics side is invisible to any arXiv sweep.` | Topicalised expletive-shaped opener whose subject is a ranking, not a paper. Delete (§2 #10, §11). |
| 16 | 214–216 | `GARP holds if there is no sequence of choices such that...` | **Keep.** The standard mathematical statement of an acyclicity condition; rephrasing would be worse. |
| 17 | 236–237 | `A Cobb--Douglas demand share-fitted to each trace's own observed data is computed as a feasibility incumbent and sanity ceiling` | Not a cleft but the same defect it causes: a 12-word subject before the verb. Replace: `We compute a share-fitted Cobb--Douglas demand as a sanity ceiling on the reported distance.` |
| 18 | 222–226 | `The full formulation, and the three method commitments governing budget exhaustion, the strict-preference margin, and per-output verification, are given in...` | 21 words of subject before `are given`. Splitting per §3 #8 fixes it. |
| 19 | 463–464 | `is what buys the payoff gain above` | `buys the payoff gain` (and drop `above` — §11). |
| 20 | 495–497 | `Two independently designed ... payoffs --- ... --- converging on the same negative paired-comparison result is the finding.` | Subject–verb distance of 30 words, and the predicate is a self-assessment. Replace: `Two payoff designs return the same negative paired comparison.` |
| 21 | 555 | `This is no detectable CCEI shift, not a confirmation of...` | `Neither experiment detects a CCEI shift.` |
| 22 | 570 | `this is a further case of the same pattern` | `GARP pass rate again detects the disruption and CCEI does not.` |
| 23 | 603 | `This is an open design tradeoff:` | Expletive `This is` plus a label. Delete (§2 #23). |
| 24 | 637 | `This is a measurement design for asking whether repair helps` | `The design measures whether repair helps in a given setting.` |
| 25 | 680 | `The one near-miss is that the projection's feasibility incumbent is a Cobb--Douglas demand share-fitted to the agent's own observed data` | Cleft of the "the thing that matters is" family, and the `one near-miss` framing is process narration (§11). State the fact directly. |
| 26 | 703–704 | `It does not explain the dose--response relationship away` | Expletive-ish `It` with a contested antecedent (§16). |

No `It is X that…` or `There is X which…` constructions appear anywhere in the manuscript. Checked all 754 lines.

---

# 7. Headers and bold paragraph leads

`\textbf{}` is doing **five incompatible jobs** across the manuscript: section-equivalent run-in heads (`\textbf{Compute.}`, `\textbf{Formulation.}`, `\textbf{Objective.}`); condition names (`\textbf{Baseline}`, `\textbf{Reciprocal}`, `\textbf{Multiturn}`); term definitions (`\textbf{null operator}`, `\textbf{primary}`, `\textbf{oracle}`); mid-paragraph emphasis on whole clauses (`\textbf{Budget exhaustion is imposed as an equality}`, `\textbf{Both scales show a significant, positive relationship...}`); and full argumentative sentences used as headings (`\textbf{The sharpest objection is psychometric, and it is in \emph{PNAS}.}`, `\textbf{No third payoff was attempted...}`, `\textbf{CCEI is noisy at 1.5B...}`). A reader who learns that bold means one thing is wrong within twenty lines.

**Recommendation:** reserve `\textbf{}` for run-in heads that are noun phrases with a terminal period; use `\emph{}` for first-use term definitions (matching `\emph{dose}` at L232, which already does this); unbold everything else.

## 7a. Sectioning commands

| # | Line | Current | Verdict / replacement |
|---|---|---|---|
| 1 | 18 | `\title{What Does Repairing Choice Inconsistency Actually Buy? \\ A Budget-Set Diagnosis}` | Question-plus-subtitle joined by a hard `\\`. The subtitle names the method; the main clause editorializes. A reader scanning a proceedings index learns that something is being questioned but not what was found. Replacement: `A GARP-Blind Null Operator Outperforms Minimal GARP Repair on an Exogenous Payoff`. If the interrogative form is kept (a defensible workshop convention), at minimum drop `Actually`. The manual `\\` inside `\title{}` will also break differently in the PDF metadata; prefer letting the title wrap. |
| 2 | 50, 124, 202, 313, 316, 339, 403, 595, 645, 674 | `Introduction`, `Related Work`, `Method`, `Experimental design`, `Models and conditions`, `Budget sets and power`, `Results`, `Limitations`, `Conclusion`, `Payoff exogeneity audit` | **All correct.** They name their content, are scannable, carry no suffixes, and form no paired devices. No change. |
| 3 | 205–206 | `The projection: Demuynck \& Rehbeck's (2023) minimal-quantity-error MILP, applied and independently verified` | Essay title: a colon, a possessive attribution, a redundant year (the `\citet` at L210 supplies it), and a defensive `, applied and independently verified` suffix of exactly the `, revisited` / `, in full` shape the category names. Also two citation formats for the same source five lines apart (§15). Replace: `Minimal-quantity-error MILP projection`. |
| 4 | 246 | `The exogenous payoff` | *Stylistic preference* — definite article in a heading. Flagged only for consistency with L316 and L339, which have no article. |
| 5 | 279 | `Two robustness controls against a payoff-geometry confound` | States a count and an argument (that the confound exists and that these defeat it) rather than naming content. The `\label` at L280 is `sec:method-nullop`, which names the content correctly — the heading is the thing that drifted, so cross-references at L277, L306, L455, L465, L480 and L615 all land on a heading with no matching words. Replace: `Null-operator controls`. |
| 6 | 354 | `The discard-selection problem, and its correction as a stated contribution` | Three faults: an essay-title comma-and construction; `as a stated contribution` argues for the section's own value in the contents page; and it names two things where the section actually delivers three (a problem, a protocol, and a result — Table 2). Replace: `Discard selection and the retry protocol`. |
| 7 | 429 | `\subsection{The dose--response relationship, and the control that overturns it (C1)}` | Essay title; states two results at once; narrates the project's own revision (`overturns it`); and ships an unexplained internal code `(C1)` in a heading. Replace: `\subsection{Dose--response and the null-operator control}`. |
| 8 | 538–539 | `\subsection{The reciprocal-framing manipulation: survivorship, and a correction that helps but does not fully resolve it}` | **Worst heading in the manuscript.** Three topics joined by a comma and `and`; the colon-plus-clause form reads as an argument; `helps but does not fully resolve it` editorializes, and `it` has no antecedent that survives scanning. Replace: `\subsection{Reciprocal framing and discard selection}`. |
| 9 | 562–563 | `\subsection{The multiturn/format effect: a large effect in the opposite direction from the literature}` | States the result in the heading; `effect ... effect` repeats inside one heading; slash construction `multiturn/format`. **Also missing its `\label`** while both sibling subsections have one (`sec:results-c1`, `sec:results-framing`) — nothing in the paper can cross-reference it. Replace: `\subsection{Multiturn elicitation format}` plus `\label{sec:results-multiturn}`. |
| 10 | 630 | `\paragraph{Broader impacts.}` | Markup inconsistency: four `\textbf{}` run-in leads in §Limitations followed by one `\paragraph{}` in the same section. Promote to `\section{Broader Impacts}` (§14 #12), which removes the inconsistency without touching the four `\textbf{}` leads. |
| 11 | 710 | `\section{Full MILP formulation and method-implementation detail}` | Two topics joined by `and`; `Full ... detail` is a `, in full` suffix in disguise; `method-implementation` is a compound appearing nowhere else in the manuscript. A reader scanning the contents page cannot tell this section also contains the guarantee discussion (L742–749). Replace: `\section{MILP formulation and implementation}`. |
| 12 | 741 | `\label{sec:method-guarantee}` with **no sectioning command** | **Live cross-reference defect, not merely a style issue.** A `sec:`-prefixed label floating above a bold run-in inside Appendix B; it resolves to the enclosing `\section` counter, so `\S\ref{sec:method-guarantee}` at L162 sends the reader to the top of Appendix B rather than to this paragraph. The prefix is also inconsistent with `app:payoff-audit` (L675) and `app:method-detail` (L711). Fix: `\subsection{Scope of the guarantee}\label{app:guarantee}`, and update the reference at L162. |

**Paired rhetorical heading device.** L429 (`...and the control that overturns it`) and L538–539 (`...a correction that helps but does not fully resolve it`) are built to the same "X, and the thing that undoes X" template — two of the three Results subsections. It reads as a device rather than as two independent choices.

## 7b. Bold run-in leads

| # | Line | Text | Verdict |
|---|---|---|---|
| 13 | 108 | `\textbf{Contributions.}` | **Keep.** Conventional run-in lead that names its content. The correct model for the rest. |
| 14 | 158 | `\textbf{POISE}` | **Keep.** Names the content. Add a terminal period for consistency with #13. |
| 15 | 180 | `\textbf{The sharpest objection is psychometric, and it is in \emph{PNAS}.}` | A full editorialising sentence in bold: it argues (`sharpest`), appeals to venue (`\emph{PNAS}`), and cannot be used to find anything by a reader scanning the section. It also creates a false parallel with `\textbf{POISE}` — a reader who has learned that bold means "system name" hits a sentence instead. Replace: `\textbf{Psychometric reliability.}` |
| 16 | 158 / 171 / 180 / 192 | **Half-applied leads in Related Work** | Two of the five body paragraphs get a bold lead and three do not. Either give all five noun-phrase leads (`\textbf{POISE.}` / `\textbf{Preference-model variants.}` / `\textbf{Psychometric reliability.}` / `\textbf{Economic-choice steering.}`) or drop both. Half-applied run-in leads read as unfinished formatting. |
| 17 | 241 | `\textbf{What can be guaranteed, and what cannot}` | Paired rhetorical device inside a single lead; reads as clever and defeats scanning. Replace: `\textbf{Guarantees.}` |
| 18 | 285, 295, 296 | `\textbf{null operator}`, `\textbf{primary}`, `\textbf{oracle}` | Bold used for term definition — a third use of the device within 60 lines. Use `\emph{}`, matching `\emph{dose}` at L232 and `\emph{non-monotonic}` at L265. Note that `\textbf{primary}` bolds only the adjective, so the defined term is visually `primary` while the text later calls it `primary null` (§12). |
| 19 | 324 | `\textbf{Compute.}` | **Keep.** The correct model for the others. |
| 20 | 328, 329, 331 | `\textbf{Baseline}` / `\textbf{Reciprocal}` / `\textbf{Multiturn}` | Condition *names*, not run-in heads, using the same typographic device at a different rhetorical level, and lacking the terminal period `\textbf{Compute.}` has. Pick one convention — recommend periods on all, and reserving unperiodded bold for nothing. |
| 21 | 436–437 | `\textbf{Both scales show a significant, positive relationship, and it is stronger at the headroom model}` | **Unbold.** A whole claim in bold mid-paragraph, and the only bold in Results that is not a run-in lead at all. The two $\rho$ values that follow are the evidence; bolding tells the reader what to think of them before they see them. |
| 22 | 469, 479 | `\textbf{Experiment 1 (original payoff).}` / `\textbf{Experiment 2 (corrected payoff).}` | **Keep.** They name their content. |
| 23 | 494 | `\textbf{No third payoff was attempted, and this is a stated scope decision, not a resource constraint.}` | A bolded pre-emptive defence against an accusation no reviewer has made. Replace: `\textbf{Two payoff designs.}` |
| 24 | 502 | `\textbf{A partial mechanistic note.}` | `Partial` grades the content before the reader can. Replace: `\textbf{Trace extremity and the null's advantage.}` |
| 25 | 533–535 | Three-line bolded C1 verdict with a nested em-dash aside | **Unbold and split** (§9). A verdict this important should be the shortest sentence in the paragraph, not the longest one in bold. |
| 26 | 598–599 | `\textbf{CCEI is noisy at 1.5B, and the paper leads with GARP pass rate because of it, not by preference.}` | Twenty words; two clauses joined by `and`; contains a rhetorical negation and a defence of an editorial choice. Unusable for scanning. Replace: `\textbf{CCEI is underpowered at 1.5B.}` |
| 27 | 606 | `\textbf{Single run per condition, one scale point per model.}` | Two topics comma-joined; states two limitations at once. *Stylistic preference — two short noun phrases in one bold lead is common in NeurIPS limitations.* Recommend splitting anyway, because the paragraph beneath already contains two unrelated limitations (§14 #13). |
| 28 | 614 | `\textbf{Two fixed exogenous payoffs, not three.}` | Rhetorical negation in a heading; pre-empts an objection before naming the topic. Replace: `\textbf{Two exogenous payoffs.}` |
| 29 | 620 | `\textbf{An adverse prior the paper now joins rather than argues against.}` | Essay title. Reads as clever, names no content, and a reader scanning for "how does this relate to prior negative results" will not match on it. **Worst of the four Limitations leads.** Replace: `\textbf{Consistent with three prior negative results.}` |
| 30 | 678 | `\textbf{(1) No shared derived quantity beyond the exogenous $(p, I)$.}` | Numbered plus a negative assertion, so a scanner learns nothing about what part (1) contains. Replace: `\textbf{(1) Payoff inputs.}` |
| 31 | 686–687 | `\textbf{(2) The payoff's optimum is independent of revealed preference, checked empirically as well as by construction.}` | **Longest lead in the appendix (17 words), and it states two results at once** (independence, and that it was checked two ways). Replace: `\textbf{(2) Independence of the payoff optimum from revealed preference.}` |
| 32 | 693 | `\textbf{(3) Hand-derived mechanism check.}` | `Hand-derived` narrates the labour, not the check. Replace: `\textbf{(3) Trace-level mechanism check.}` |
| 33 | 701 | `\textbf{(4) The severity-confound check.}` | A definite article the other three leads lack. Replace: `\textbf{(4) Severity confound.}` |
| 34 | 715 | `\textbf{Formulation.}` | **Keep.** |
| 35 | 725 | `\textbf{Three method commitments, each carrying an explicit risk.}` | Announces a count and editorializes, and the promise is honoured for only one of the three commitments (§14 #17). Replace: `\textbf{Implementation commitments.}` |
| 36 | 725–726, 728, 732 | `\textbf{Budget exhaustion is imposed as an equality}` / `\textbf{A fixed strict-preference margin $\gamma > 0$}` / `\textbf{Every returned $\tilde{x}$ is verified independently}` | **Mid-paragraph bolded full clauses** — a different device from the paragraph-leading bolds, colliding with them visually within the same paragraph. Break the three commitments into three paragraphs with noun-phrase leads: `\textbf{Budget exhaustion.}` / `\textbf{Strict-preference margin.}` / `\textbf{Independent verification.}` |
| 37 | 737 | `\textbf{Objective.}` | **Keep.** |
| 38 | 742 | `\textbf{What can be guaranteed, and what cannot.}` | **Worst bold lead in the appendix**: simultaneously a `What`-cleft (§6 #7), a paired-device flourish that defeats scanning, and attached to a mis-scoped `sec:` label (#12). Replace: `\textbf{Scope of the guarantee.}` and promote to `\subsection`. |

**Terminal-period convention, counted.** Periods on: `\textbf{Contributions.}` (108), `\textbf{Compute.}` (324), `\textbf{Formulation.}` (715), `\textbf{Objective.}` (737), all four appendix numerals (678, 686, 693, 701), `\textbf{Experiment 1 ...}` / `\textbf{Experiment 2 ...}` (469, 479), `\textbf{A partial mechanistic note.}` (502), and the four Limitations leads (598, 606, 614, 620). No period on: `\textbf{POISE}` (158), `\textbf{What can be guaranteed, and what cannot}` (241), `\textbf{null operator}` (285), `\textbf{primary}` / `\textbf{oracle}` (295, 296), `\textbf{Baseline}` / `\textbf{Reciprocal}` / `\textbf{Multiturn}` (328, 329, 331), the three Method-commitment clauses (725, 728, 732), and the bolded verdicts at 436–437 and 533–535. **Fifteen with, thirteen without.** Pick one.

---

# 8. Figure and table captions

Seven captioned floats exist in the manuscript. Every one is counted below against the **hard cap of 3 sentences** the operator will apply in Phase 2. Counts are made against the *current* text of `tex/paper.tex` as it stands after the earlier (7K) tightening round, not against any earlier wording.

| Float | Lines | **Sentence count** | Word count | **Verdict against the 3-sentence cap** |
|---|---|---|---|---|
| Table 1 `tab:related` | 134–136 | **3** | ~47 | Within cap |
| Figure `fig:pipeline` | 303–309 | **3** | ~85 | Within cap |
| Table 2 `tab:discardbreakdown` | 380–386 | **3** | ~100 | Within cap, at the limit |
| Table 3 `tab:headline` | 411–412 | **2** | ~35 | Within cap |
| Figure 1 `fig:doseresponse` | 450–457 | **6** | ~105 | **OVER CAP — cut 3 sentences** |
| Figure `fig:mechanism` | 520–529 | **7** | ~150 | **OVER CAP — cut 4 sentences. Worst offender in the manuscript.** |
| Table 4 `tab:multiturn` | 579–583 | **2** | ~75 | Within cap |

## 8a. Figure 1, `fig:doseresponse` (L450–457) — 6 sentences, OVER CAP

**Current sentences, counted:**
1. `Real repair's $\Delta$payoff (x-axis) against the size-matched null operator's $\Delta$payoff (y-axis), one point per GARP-violating trace ($n=85$; circle/blue: qwen2.5:1.5b, triangle/orange: llama3.2:3b).`
2. `Dashed line is $y=x$; points above it have higher null $\Delta$payoff than real.`
3. `Symmetric-log axes keep one far-larger-dose trace from compressing the rest.`
4. `\textbf{(A)} Experiment 1 (original payoff, \S\ref{sec:method-payoff}).`
5. `\textbf{(B)} Experiment 2 (corrected payoff, \S\ref{sec:method-nullop}), each trace's primary-null $\Delta$payoff averaged over $K=20$ draws of the random target ($\pm1$ SD error bars); the oracle null is not plotted.`
6. `Statistics are in \S\ref{sec:results-c1}.`

**Cuts, in order:**
- **Delete sentence 6** — `Statistics are in \S\ref{sec:results-c1}.` Circular: the figure is cited only from inside `sec:results-c1`.
- **Delete sentence 3** — `Symmetric-log axes keep one far-larger-dose trace from compressing the rest.` The justification of a plotting decision belongs in the method or nowhere. If the axis type must be stated, fold `Symmetric-log axes.` into sentence 1 as a trailing clause rather than a sentence.
- **Delete `; the oracle null is not plotted`** from sentence 5 (§1 #69) — a caption states what is plotted, not what is absent.
- **Merge sentences 4 and 5** into one.

**Proposed caption at exactly 3 sentences:**
> `Real repair's $\Delta$payoff (x-axis) against the size-matched null operator's $\Delta$payoff (y-axis) on symmetric-log axes, one point per GARP-violating trace ($n=85$; circle/blue: qwen2.5:1.5b, triangle/orange: llama3.2:3b). Dashed line is $y=x$; points above it have higher null $\Delta$payoff than real. \textbf{(A)} Experiment 1, original payoff; \textbf{(B)} Experiment 2, corrected payoff, with each trace's primary-null $\Delta$payoff averaged over $K=20$ draws of the random target ($\pm1$ SD error bars).`

**The body/caption content mismatch — CROSS-SECTION FLAG, CONFIRMED AS REAL.** This is the highest-severity caption defect in the manuscript and it is not a length problem.

- **Body, L435:** `Figure~\ref{fig:doseresponse} shows the relationship split by model on shared axes.`
- **Caption, L450–455:** `Real repair's $\Delta$payoff (x-axis) against the size-matched null operator's $\Delta$payoff (y-axis)` ... `\textbf{(A)} Experiment 1 (original payoff ...). \textbf{(B)} Experiment 2 (corrected payoff ...)`

The body sentence sits inside the paragraph reporting the **dose–response** statistics (Spearman $\rho=0.729$, Pearson $r=0.821$, L432–435) and describes a dose-vs-$\Delta$payoff plot with a per-model split "on shared axes." The caption describes a **real-vs-null scatter** whose two panels are Experiment 1 and Experiment 2, with the per-model split carried by marker shape and colour, not by panels or shared axes. **The body sentence mischaracterises what the figure now shows on both axes and on the panel structure.** It reads as leftover text from Figure 1's redesign. A reviewer who looks at the figure while reading L435 stops reading. **Fix:** delete L435 entirely and cite the figure from inside the Experiment 1 paragraph, after L471, where the real-vs-null comparison is actually being made: `...with the null winning 69 of 85 traces (81\%; Fig.~\ref{fig:doseresponse}A).`

**The second half of that flag is OVERTURNED.** The Results agent additionally suspected that the null operator is used in Figure 1's caption before it is defined. It is not: the null operator is constructed and named at **L285–289 in Method §3.3**, 165 lines before the caption, with the dose-matching property stated at L286–287 and the two variants (`primary`, `oracle`) at L295–296. The `size-matched` and `primary-null` wording in the caption is drift from that definition (§12), not a use-before-definition. **Drop the use-before-definition concern.** What survives from it is a real but lesser ordering problem: within Results, the figure is *cited* at L435, two paragraphs before the null operator is *re-introduced* at L465, so a reader following the citation at L435 meets an axis label whose object the Results section has not yet mentioned. Fixing the citation placement, as above, fixes this too.

## 8b. Figure `fig:mechanism` (L520–529) — 7 sentences, OVER CAP, and it carries results found nowhere else

**Current sentences, counted:**
1. `The largest-dose trace (qwen2.5:1.5b, reciprocal, replicate 12; $L_1=111.64$, $T=21$ rounds, hand-audited in Appendix~\ref{app:payoff-audit}); every plotted quantity is recomputed by re-solving the projection MILP.`
2. `With $K=2$, payoff is a function of expenditure share $s$.`
3. `\textbf{(A)} The original payoff, $2\sqrt{s(1-s)}$ (peak at $s=0.5$).`
4. `\textbf{(B)} The corrected payoff's per-trace-target form (peak at this trace's own draw $\alpha_s=0.704$).`
5. `\textbf{(C)} Per-round expenditure share $s$ across all 21 rounds for the raw trace, the real repair, and the null operator.`
6. `The repair changes 5 of 21 rounds (42\% of its $L_1$ budget on round 3 alone: $s$ $0.11\!\to\!0.65$, payoff $0.626\!\to\!0.953$), leaving the other 16 at a near-corner $s=0.99$; the null spreads the same total displacement over all 21 rounds.`
7. `Single-trace illustration; the 85-trace comparison is in \S\ref{sec:results-c1}.`

**Dangerous case — seven measurements appear only in this caption:**

| Quantity | Line | Where it belongs |
|---|---|---|
| `$L_1=111.64$` | 520 | Body, §sec:results-c1 — it is the largest dose in the study, referred to obliquely at L453 (`one far-larger-dose trace`) with no value |
| `$T=21$ rounds` | 521 | Body, with the trace identification |
| `$\alpha_s=0.704$` | 525 | Body |
| `The repair changes 5 of 21 rounds` | 526 | **Body.** This is the mechanistic finding the paragraph at L513–515 gestures at without a single number |
| `42\% of its $L_1$ budget on round 3 alone: $s$ $0.11\to0.65$, payoff $0.626\to0.953$` | 526–527 | **Body**, same sentence |
| `leaving the other 16 at a near-corner $s=0.99$` | 527–528 | **Body** |
| `the null spreads the same total displacement over all 21 rounds` | 528–529 | **Body** |

The body sentence at L513–515 (`the rounds that generate the null's advantage there are precisely the extreme-share rounds the real repair leaves untouched`) asserts, with no number at all, exactly what the caption proves with seven. **Move sentence 6 into the body** and the caption drops to within cap on its own.

**Cuts:**
- **Move sentence 6 to the body**, at L515.
- **Delete sentence 7** — defensive and circular; the body already says `on a single trace` at L513–514.
- **Delete `; every plotted quantity is recomputed by re-solving the projection MILP`** from sentence 1 and **`hand-audited in Appendix~\ref{app:payoff-audit}`** — verification-process records inside a caption (§11). Move to Appendix A, which already carries the hand-audit.
- **Merge sentences 3, 4 and 5** into one panel-key sentence.

**Proposed caption at exactly 3 sentences:**
> `The largest-dose trace (qwen2.5:1.5b, reciprocal, replicate 12; $L_1=111.64$, $T=21$ rounds). With $K=2$, payoff is a function of expenditure share $s$. \textbf{(A)} The original payoff $2\sqrt{s(1-s)}$, peak at $s=0.5$; \textbf{(B)} the corrected payoff at this trace's draw $\alpha_s=0.704$; \textbf{(C)} per-round $s$ for the raw trace, the real repair, and the null operator.`

## 8c. Table 2, `tab:discardbreakdown` (L380–386) — 3 sentences, within cap

Within the hard cap, so no cut is required by Phase 2. Three content defects remain.

1. **Sentence 1 is a word-level duplicate of the body at L366–368** — the same three-item list (`kept on the first attempt, rescued by a later retry, or still discarded after three attempts`), in the same order, in the same words. One of the two must go. Keep the caption (a table caption must be self-contained) and delete the body sentence (§3 #13).
2. **A specification that belongs in the Method.** `mean dose ($L_1$) is averaged over the full group, with $0$ for any already-GARP-consistent trace` (L384–385). This zero-imputation convention affects every dose number in the paper — including Table 3's dose *and* $\Delta$payoff columns, per §13 #10 — and it appears only here, in a caption, in a subordinate clause. Move to §sec:method-projection near L232.
3. **A substantive experimental finding disclosed only in a footnote.** `$^*$qwen residual discard: 3 of the 6 slots returned zero valid rounds on every attempt (no $p$/$x$ data at all)` (L385–386). Three of 30 qwen reciprocal slots (10%) produced no parseable output at all across three attempts. This is the strongest single piece of evidence for the paper's own instrument-validity claim (L359–360), and it is buried where a skimming reviewer will not credit it. Move into the body of §sec:discard around L364 (`Three of the 30 qwen reciprocal slots returned zero valid rounds on all three attempts, yielding no price or quantity data.`), and shrink the footnote to `$^*$Computed over the 3 of 6 slots with any valid rounds.`

## 8d. Table 3, `tab:headline` (L411–412) — 2 sentences, within cap, **and the second sentence is wrong**

Current: `Headline results per (model, condition) cell. GARP pass and CCEI are computed on kept traces only; dose and $\Delta$payoff are computed on the subset of kept traces that violate GARP.`

**CROSS-SECTION FLAG RESOLVED — the caption misstates the convention, and the numbers are consistent once corrected.** Full derivation in §13 #10. In brief: the table's `mean $\Delta$payoff` column, weighted by the per-cell violator counts implied by the GARP pass rates (8, 17, 18, 27, 15 — summing to the 85 of L432), gives an overall mean of **0.0062**, which matches nothing in the text. Weighted by `$n$ kept` instead (30, 28, 30, 30, 24) it gives **0.7738/85 = 0.00910**, which matches L434 and L471 exactly. The column is therefore averaged over **all kept traces with $0$ imputed for GARP-consistent ones** — the very convention Table 2's caption states for its own dose column at L384–385 — not over the violating subset. The dose column behaves the same way.

**Fix (prose only, no number changes):** replace the second sentence with `GARP pass and CCEI are computed on kept traces only; dose and $\Delta$payoff are averaged over all kept traces, with $0$ for any already-GARP-consistent trace, and are under the original payoff (\S\ref{sec:method-payoff}).` This also closes the separate ambiguity that the caption never says *which* of the two payoffs the $\Delta$payoff column uses, in a section that reports two with different values for the same quantity.

## 8e. Table 4, `tab:multiturn` (L579–583) — 2 sentences, within cap

Within the cap. Three defects remain, all in sentence 2:
1. **Most of it is a third statement of the same fact.** The column headers already read `95\% CI (Wilson)` and `mean CCEI [95\% CI ($t$)]`. Cut to `Wilson 95\% CIs for GARP pass, $t$-based 95\% CIs for CCEI.` and move the construction to the Method.
2. **`computed from the reported mean, SD, and $n$` is a process leak** (§11): it tells the reader the intervals were reconstructed from summary statistics rather than computed from the data. Either that is a limitation and belongs in §Limitations, or it is irrelevant and should go.
3. **`zero discards in either arm` (L580) duplicates `with \emph{zero discards on either arm}` at L567.** Cut from the caption; the body says it with emphasis.
4. Typography: `($df=29$) (two-sample $t$-test, $p=0.91$)` — two adjacent parentheticals. Merge.

## 8f. Figure `fig:pipeline` (L303–309) — 3 sentences, within cap

Within the cap; no Phase-2 cut required. Four content defects.
1. **A forward reference the caption forces on the reader.** `parse under the capped retry protocol of \S\ref{sec:discard}, residual discards excluded (3)` at L305 points to a section that begins at L355 — 50 lines later. The caption should say `parse (3)`; the protocol is fully specified at L361–364.
2. **The algorithm is named only here.** `combinatorial Warshall-closure GARP check (4)` — `Warshall-closure` appears in the main text at no other point; the body calls the same object `the same combinatorial check used throughout` (L226) and `the GARP check` (L288). The caption is where the algorithm gets its name. Move `Warshall-closure` into the Method text at L226 and write `GARP check (4)` here.
3. **A definition restated.** `whose $L_1$ displacement is the dose` — `dose` is defined at L232–233. Cut to `MILP projection (5)`.
4. **Sentence 3 is unparseable.** `Counts are the main experiment's (\S\ref{sec:results}).` A possessive with an elided noun — the main experiment's *what*? Even on rereading it is ambiguous between "the counts shown are from the main experiment" and "counts are reported in the results section". Delete, or `Counts are from the $N=30$ main experiment.`

## 8g. Table 1, `tab:related` (L134–136) — 3 sentences, within cap

Within the cap. Four content defects.
1. **Sentence 1, `Where prior repair systems sit.`** — a title, not a statement of what is tabulated, and it repeats `Table~\ref{tab:related} positions nine published systems` at L127–128. Delete and replace with a sentence stating what the cells mean, which nothing currently does.
2. **Sentences 2 and 3 repeat the body in substance.** `Own choices` is defined at L128–129 and again at L135; `Exogenous payoff` at L129 and again at L136. Keep the definitions in the caption (a table needs self-contained column definitions) and cut the parentheticals at L129 from the body — which also fixes §1 #25, #26 and §3 #6.
3. **The caption defines two of four columns.** `Graded dose` and `Min.-distance projection` (L141) are defined nowhere in the section. Add one clause each. Doing so would push the caption over three sentences, so use a semicolon-joined single sentence: `\emph{Graded dose}: the intervention has a continuous magnitude, not an on/off setting; \emph{Min.-distance projection}: the edit is the solution to an explicit minimum-distance program.`
4. **A third verdict value is used and defined nowhere.** `partial` (L146, CONSISTRE, Exogenous payoff) in a yes/no table. Define it in the caption or resolve it to yes/no with a footnote. Relatedly, `no (declined)` (L147) is an editorial annotation inside a data cell; change to `no` — the nuance already lives at L166–167.
5. *Stylistic preference, flagged not fixed:* every affirmative cell is `\textbf{yes}` and every negative is plain `no`, so the `This paper` row (L153) is the only fully bold row and reads as visually asserted rather than tabulated. The competing convention is checkmarks/dashes with no emphasis. A hostile reviewer will notice that the paper's own row is the only one the eye lands on.
6. *Stylistic preference:* the nine rows follow no visible ordering principle — not alphabetical, not chronological, not by yes-count. Sorting descending by number of `yes` cells would make `None occupies all four` self-evident as a gradient rather than asserted.

---

# 9. Run-on and over-nested sentences

## 9a. The five worst sentences in the manuscript, ranked

**1. L742–749 (Appendix B, the guarantee paragraph) — ~93 words, one sentence, and it is an entire paragraph.**
> `Against the closest published structural analogue, a proved-optimal projection onto a convex monotone cone \citep{wang2026poise}: because the GARP-consistent set is a union of polyhedra rather than a single convex set, the non-expansiveness that licenses a weakly-closer-to-ground-truth guarantee there has no analogue here --- the prior operator's cone is fixed by an ordering supplied as input, whereas a GARP repair must decide which revealed-preference comparisons to give up, absorbed into the binary comparison indicators above rather than eliminated, which is why no distance-minimization guarantee analogous to the convex case is claimed.`

An appositive-laden opener, a colon, a subordinate `because` clause, the main clause, an em-dash elaboration, a `whereas` clause, a dangling participial insertion (§4 #76), and a trailing `which is why` clause that explains the sentence's own purpose. It also contains three cognates of `analogue` (§16) and three referents (`the closest published structural analogue`, `there`, `here`) plus `the prior operator` all pointing at one of two systems.

**Split into four:**
> `The closest published analogue is a proved-optimal projection onto a convex monotone cone \citep{wang2026poise}. There, non-expansiveness licenses a weakly-closer-to-ground-truth guarantee, because the cone is fixed by an ordering supplied as input. The GARP-consistent set is a union of polyhedra rather than a single convex set, and a GARP repair must itself decide which revealed-preference comparisons to give up. That decision is absorbed into the binary comparison indicators $U_{t,v}$ rather than eliminated, so we claim no distance-minimization guarantee.`

**2. L659–664 (the Conclusion's final sentence, and the paper's last words) — ~86 words.**
> `Two further, unpredicted findings --- a framing manipulation's apparent effect was a discard-selection artifact rather than a real coherence shift (C3), and an elicitation-format manipulation collapsed GARP pass rate in the opposite direction from a published finding in the same domain and model family at a larger scale --- are reported in their own right: a well-controlled negative, an open identification question, and an instrument-validity finding are exactly what this literature should surface by default rather than paper over.`

The subject (`Two further, unpredicted findings`) is separated from its verb (`are reported`) by a 53-word em-dash parenthetical containing two independent clauses, one of which carries four stacked prepositional phrases. Then a colon introduces a three-item list. Then the sentence closes on an aphorism containing a pun. **Every category in this audit fires on this one sentence** — §1, §2, §4, §5, §6, §9, §10, §13, §14, §16. See §13 #17 for the honest reading of the two-versus-three question.

**Split into three:**
> `A framing manipulation's apparent effect was a discard-selection artifact (C3). An elicitation-format manipulation moved GARP pass rate in the direction opposite to that reported by \citet{wang2025tactics}, in the same domain and model family at a larger scale.` Then either stop, or give the meta-point its own sentence with the scope corrected: `A negative result with a matched null control, an open identification question, and an instrument-validity finding are all publishable.`

**3. L79–83 (Introduction, the paper's central-finding sentence).**
> `A control absent from every published axiom-enforcement result we are aware of --- an operator that knows nothing about GARP but spends the identical displacement budget shrinking every bundle toward a fixed interior point --- outperforms the real GARP-restoring repair on the exogenous payoff, significantly, at both model scales, under two independently designed payoffs (\S\ref{sec:results-c1}).`

Forty-two words separate the subject (`A control`) from its verb (`outperforms`), and the intervening material is a 27-word em-dash apposition containing its own `but` contrast. After the verb, three more comma-set qualifications follow. **This is the worst-constructed sentence in the body of the argument, where a reviewer reads for the finding.**

**Split:**
> `An operator that spends the identical displacement budget shrinking every bundle toward a fixed interior point, with no access to the GARP violation structure, outperforms the real GARP-restoring repair on the exogenous payoff (\S\ref{sec:results-c1}). The result holds at both model scales and under two independently designed payoffs. No published axiom-enforcement result we are aware of includes this control.`

**4. L193–198 (Related Work) — ~72 words, five joins, and a garden path.**
> `\citet{cook2026whatllmswant} steer economic choices toward payoff-maximising behaviour via personas and control vectors --- occupying two of our three legs without Afriat machinery; their finding that reframing moves models while persona prompting does not corroborates our manipulation choice, anchored in \citet{wang2025tactics}, who find \emph{format} moves the Afriat index in the same domain and model family (Qwen2.5) at a larger scale: collapsing multi-turn to single-turn drops CCEI by up to $0.241$.`

Joins: em-dash appositive → semicolon → embedded `that`-clause with an internal `while` contrast → comma appositive → `who`-relative → parenthetical → colon. **Garden path:** `persona prompting does not corroborates` reads as an error for several words before the reader recovers that `does not` closes the embedded clause and `corroborates` is the main verb of `their finding`. It also contains the four-criteria miscount (§13 #2) and a dangling modifier (§4 #25).

**Split into three:**
> `\citet{cook2026whatllmswant} steer economic choices toward payoff-maximizing behavior with personas and control vectors. They meet two of the four criteria and use no Afriat machinery. They find that reframing moves models while persona prompting does not, which corroborates our manipulation choice; \citet{wang2025tactics} find the same in the same domain and model family (Qwen2.5) at 7B, where collapsing multi-turn to single-turn drops CCEI by $0.241$.`

**5. L368–372 (Experimental design) — 62 words, and it is contradicted by its own table.**
> `At 1.5B, retry-rescued sessions are not a close stand-in for first-attempt sessions: higher mean CCEI but a substantially lower GARP pass rate, and the residual-discard group scores lowest on the handful that can be measured --- consistent with, though not conclusive given the small residual sample, some of the same selection concern the pilot's naive handling raised persisting at a smaller scale even after correction.`

One colon, one `but`, one `and`, an em-dash appositive containing an interrupting concession clause, a stacked noun phrase with a reduced relative inside it, and a dangling participle (`persisting`) 20 words from its subject. It also contains a rhetorical negation (§1 #65), two softeners (§5 #47, #48), a vague quantifier (`the handful`), and a claim contradicted by Table 2 (§13 #5).

**Split:**
> `At 1.5B, retry-rescued sessions differ from first-attempt sessions: mean CCEI 0.9651 against 0.9315, but GARP pass rate 0.1429 against 0.4706. The residual-discard group has the lowest mean CCEI of the three. The residual sample is too small ($n=6$, 3 measurable) to be conclusive, but the pattern is consistent with the pilot's selection concern surviving the retry correction at reduced magnitude.`

**Runners-up, in line order:** L509–512 (Results, ~60 words, dangling `read as`, two `rather than` constructions, a hedge on a hedge); L680–685 (Appendix A, ~75 words, a parenthetical inside a clause inside a dash-clause); L438–445 (Results, ~75 words, four parentheticals, two separate statistical tests in one coordinated clause); L341–344 (Experimental design, 52 words, a three-item comma list inside a parenthetical inside the main clause, then a trailing em-dash appositive with its own subordinate clause).

## 9b. Full inventory of sentences with four or more comma-joined clauses or nested parentheticals

| Line | Opening words | Defect |
|---|---|---|
| 34–36 | `None controls for displacement magnitude: no result establishes...` | Colon-joined pair, each half negated, with an embedded `not X` inside the second. |
| 57–61 | `The same budget-allocation instrument is the standard paradigm...` | 54 words; two independent clauses joined by `and`, four citations, plus `without a repair step` and `to ask whether` subordinations. |
| 61–64 | `A separate, growing literature repairs exactly this kind of inconsistency...` | 51 words; an em-dash list of three gerund phrases closed by a dash followed by `and`, which is not a standard pairing. |
| 73–76 | `We score both the raw and the repaired sequence against a fixed, equal-weight Cobb--Douglas payoff...` | 57 words; **a parenthetical inside a clause inside a sentence-level qualification** — a relative clause containing a dash-apposition, then a `so`-clause, then a trailing `not` appositive. |
| 79–83 | `A control absent from every published axiom-enforcement result...` | See §9a #3. |
| 92–95 | `We run this at a model scale where a pilot study found measurable coherence headroom...` | 49 words, two parentheticals, plus a trailing `not as` rule-out. |
| 97–101 | `The reciprocal-price framing manipulation intended to induce coherence variation at 1.5B produced, in a pilot run, a large apparent effect that disappears...` | 53 words. Subject buried under two modifiers; verb `produced` split from its object by `in a pilot run`; then a relative clause, then a colon with a two-part compound subject. Contains the §13 #1 contradiction. |
| 103–106 | `Separately, splitting single-turn elicitation into separate sequential calls at 1.5B produces...` | 49 words with two trailing appositives (§4 #10). |
| 113–117 | `A distance-matched, GARP-blind null-operator control --- absent from every published axiom-enforcement result we are aware of --- run against two independently designed exogenous payoffs, showing that...` | **A 55-word noun phrase presented as a sentence — it has no finite main verb.** Five stacked modifiers on `control`, then a `showing that` clause containing a negation containing a `rather than` containing a cleft. |
| 119–122 | `(5) A single-turn-vs-multi-turn elicitation-format manipulation that produces...` | 48 words, no finite main verb, one 30-word trailing appositive. |
| 127–130 | `Repairing an AI system's incoherent preferences is not new; Table~\ref{tab:related} positions nine published systems...` | Semicolon + colon + four list items each with its own parenthetical. |
| 160–162 | `We concede the minimum-distance priority unqualified: projection onto a closed convex set is non-expansive...` | Colon + semicolon + `hence` + `so` + parenthetical cross-reference. |
| 167–169 | `Two training-time systems, one altering the agent itself...` | Two appositives plus `respectively` binding across 25 words. |
| 171–174 | `A parallel line varies the transitivity...` | Colon + participial + em-dash + `and on`. |
| 181–183 | `\citet{nitsch2022reliability} find CCEI/Houtman--Maks reliability never reaches acceptable levels...` | Four joins plus a **parallelism break**: `find X ... and that Y` — the first conjunct is missing its `that`. |
| 186–190 | `Nitsch et al.\ diagnose their finding as a between-subject-variance problem whose prescribed remedy...` | ~55 words: subject + `whose`-relative + em-dash appositive inside that relative + semicolon-joined independent clause + parenthetical + `which is why` tail. |
| 193–198 | `\citet{cook2026whatllmswant} steer economic choices...` | See §9a #4. |
| 210–212 | `\citet{demuynck2023computing}'s multiplier-free ordinal...` | Three clauses plus a semicolon-joined independent clause on a different topic. |
| 222–226 | `The full formulation, and the three method commitments governing...` | 21-word subject, embedded three-item list, semicolon joining an unrelated verification result, then a parenthetical with a number. **Four topics in one sentence.** |
| 228–232 | `The objective is $L_1$: minimal total absolute displacement...` | **A parenthetical containing two semicolon-separated independent clauses plus a third pointer clause**, hanging off a sentence that already has a colon and two trailing modifiers. The parenthetical alone is 34 words and holds three unrelated facts. |
| 232–236 | `The \emph{dose} for a trace is its $L_1$ projection distance...` | Definition + formula + justification clause + em-dash appositive + second appositive + a `rather than`. Six units. |
| 236–239 | `A Cobb--Douglas demand share-fitted to...` | 12-word subject, two-part predicate, trailing appositive, semicolon-joined appendix claim. |
| 249–252 | `The payoff must not be derived from the agent's own revealed choices --- a utility function fit to the agent's choices (such as the projection's own feasibility incumbent above) would be circular...` | **Parenthetical inside a clause inside an em-dash appositive** — the exact nesting pattern this category names — then a conditional, then a participial appositive with a `rather than`. |
| 252–261 | `We instead fix, before any model was queried and never re-estimated from any agent's choices, an equal-weight Cobb--Douglas valuation...` | The object of `fix` arrives 14 words after the verb; the sentence then runs on through the formula to a 40-word payoff-score clause with a `so that` and a three-item list. |
| 264–267 | `\citet{ouyang2024aidecisionmaker} score LLM-generated forecasts...` | Two conjuncts + `but` + a subject-less modifier + em-dash appositive (§4 #34). |
| 269–274 | `We audited this design adversarially, before treating any dose--response result as reportable, for four failure modes: ...` | Interrupting clause splits `audited ... for`; then a four-item list; then a semicolon joining two more independent clauses. |
| 282–284 | `The payoff of \S... reduces to $\mathrm{payoff}(s)=2\sqrt{s(1-s)}$, $s$ the expenditure share on good A: concave, single interior maximum at $s=0.5$, identical across every trace.` | **Comma splice presented as a list of properties** — three predicates after the colon with no verb — plus an appositive definition mid-clause. Fix: `...where $s$ is the expenditure share on good A. It is concave with a single interior maximum at $s=0.5$, identical across traces.` |
| 285–288 | `We construct a \textbf{null operator}: for each GARP-violating trace, shrink every observed bundle...` | **Mood shift mid-sentence** (declarative → imperative after the colon), four comma units, a `chosen so` clause. |
| 291–297 | `Because the exploitable property is a single fixed target..., we build a second, independently designed payoff that removes it: ...` | 46 words, causal opener + colon + appositive + two trailing participial clauses; the following sentence adds another 45 words with two parentheticals and a trailing `since` clause. |
| 318–321 | `Two locally-hosted open-weight models, run entirely on local compute at zero API cost: ...` | **Sentence fragment with no main verb**, 45 words, carrying two parentheticals, one of which contains an em-dash appositive. |
| 324–326 | `All inference ran locally via 4-bit-quantized weights, no GPU or commercial API calls; ...` | Four independent facts joined by two commas and a semicolon, one of which (`no GPU or commercial API calls`) is a verbless fragment. |
| 331–336 | `\textbf{Multiturn} (1.5B only): baseline framing, but each of the 25 rounds is a separate sequential call...` | 55 words: colon + `but` + participial clause + semicolon + past participle + two interrupting appositives inside the that-clause. |
| 341–344 | `Each of $N=30$ independent replicates per (model, condition) cell draws its own fresh $T=25$, $K=2$ budget set...` | 52 words; a three-item comma list inside a parenthetical inside the main clause, then a trailing em-dash appositive with its own subordinate clause. Also overloads $N$ (§12) and uses `independent`/`independently` three times. |
| 348–351 | `$N=30$ gives power $\ge0.999$ against the pilot's full framing-effect magnitude...` | 46 words, four numbers, an ellipsis (`gives power` elided in the second conjunct), a parenthetical, and an editorial trailing clause. |
| 357–359 | `A pilot run found that under reciprocal framing at 1.5B, 52\% of sessions (13 of 25) failed...` | 43 words plus a dangling appositive (§4 #45). |
| 361–364 | `The main experiment implements a capped retry protocol: ...` | 44 words, colon + semicolon + trailing `but` clause. Also the clause contradicted by Table 2 (§13 #4). |
| 368–372 | `At 1.5B, retry-rescued sessions are not a close stand-in...` | See §9a #5. |
| 432–435 | `Across all 85 GARP-violating traces...` | Four independent results comma-spliced into one sentence (Spearman, Pearson, mean $\Delta$payoff, win/loss split), each with its own parenthetical. |
| 438–445 | `The confound is real...` | ~75 words, four parentheticals, a colon and a coordinated clause carrying two separate statistical tests. Split at the colon into three sentences. |
| 461–464 | `The confound just tested is a confound...` | Em-dash aside containing a `rather than` aside containing an emphasis italic. Three levels. |
| 464–467 | `\S\ref{sec:method-nullop} builds the control...` | Colon, then a noun phrase with an interposed participial clause separating `null operator` from its relative clause `that does nothing but shrink`. The relative pronoun is 12 words from its antecedent. |
| 470–472 | `mean $\Delta$payoff$_{\mathrm{null}}=0.0220$ versus...` | Comma-spliced result list: two means, a Wilcoxon $p$, a win count. |
| 473–477 | `The partial correlation of dose...` | Parenthetical, em-dash aside, `but`, colon, subordinate clause. Five segments. |
| 483–488 | `the primary, information-fair null still outperforms...` and `An oracle null privileged to know...` | Parentheticals containing four comma-joined statistics each, the second with a trailing appositive. |
| 489–492 | `The partial correlation of dose with...` | Two prepositional qualifiers before the verb, then a range, then an em-dash appositive with an embedded relative clause. |
| 495–500 | `Two independently designed...` / `Redesigning the payoff a third time...` | ~30-word subject–verb distance across an em-dash aside; then a colon, a gerund clause, and a trailing appositive with its own relative clause. |
| 502–508 | `Trace extremity (...) predicts...` | 23-word parenthetical between subject and verb; then a parenthetical with two labelled sub-results; then a trailing comparative. Followed by a **13-word quoted clause used as a prenominal adjective** before `account` (§16). |
| 509–512 | `Experiment 2's oracle null, which targets...` | See §9a runners-up. |
| 520–522, 526–529 | `fig:mechanism` caption | A parenthetical with four semicolon/comma-joined items, then a semicolon-joined independent clause; and a **parenthetical inside a parenthetical inside a clause** (`(42\% of its $L_1$ budget on round 3 alone: ...)`). |
| 542–547 | `At 3B, reciprocal framing replicates...` | ~65 words, a semicolon plus an em-dash plus two nested parentheticals of corrected $p$-values, ending in a two-clause trailing appositive. |
| 549–553 | `First-attempt discard under reciprocal framing was 43.3\%...` | Parenthetical, participle, em-dash, `but`, colon, parenthetical. |
| 555–558 | `This is no detectable CCEI shift...` | Colon, two parentheticals, `and`, a gerund subject clause. |
| 565–568 | `Splitting the 25 rounds...` | A `while` clause with a three-item parenthetical including a table reference, then an em-dash, then two more facts. |
| 570–573 | `Against the literature this arm was designed against...` | Colon-fragment, three appositives, a semicolon, then `here, at 1.5B, the reverse holds`. |
| 579–583 | `tab:multiturn` caption | See §8e. |
| 606–609 | `Every (model, condition) cell is one run of the stated protocol, with no repeated full-pipeline runs...` | Four comma-joined units, the last (`only the within-run…`) a verbless fragment appended by comma — a comma splice. |
| 609–612 | `The headroom/null-control design isolates the identification strategy from a scale confound but...` | Contrastive `but`, colon, clause, then a parenthetical containing a cross-reference and an internal term. Four levels. Also a **garden path** at `a pilot found headroom and measurement reliability do not coexist` (§16). |
| 625–628 | `We do not read this as evidence...` | A negation split across a 40-word span by an em-dash insertion. |
| 637–640 | `This is a measurement design for asking whether repair helps...` | Claim + em-dash concession + two rule-outs in one sentence. |
| 648–653 | `This paper set out to measure whether... Applying \citet{demuynck2023computing}'s minimal-quantity-error GARP repair post hoc...` | Participial opener, main clause, em-dash contrast, then three comma-set trailing qualifiers. |
| 659–664 | `Two further, unpredicted findings...` | See §9a #2. |
| 680–685 | `The one near-miss is that the projection's feasibility incumbent...` | ~75 words: an em-dash parenthetical *inside* a clause, a further parenthetical inside the following clause, a `but`-pivot, a semicolon, and a trailing negation. |
| 701–708 | `Larger-dose traces do start from worse raw payoff...` | Second sentence runs ~70 words across a partial correlation with a nested `attenuated only slightly` aside, `and in a joint OLS regression`, and a `while` contrast, with three parentheticals. |
| 715–718 | `The naive formulation parameterizes the projection with Afriat multipliers...` | Rejected-then-adopted ordering with two rule-out sentences before the adopted method appears (§14). |
| 719–723 | `We instead use the multiplier-free ordinal characterization...` | ~57 words: a three-item list followed by a two-item negation cascade. |
| 725–732 | `\textbf{A fixed strict-preference margin $\gamma > 0$}, set to $10^{-4}\cdot\min_t I_t$, converts an unattained infimum into an attained minimum: ...` | Four comma-joined units plus a colon plus a `so` clause; the justification trails the fix instead of preceding it. |
| 742–749 | `Against the closest published structural analogue...` | See §9a #1. |

## 9c. Comma splices and comma-spliced lists of results

| Line | Text | Fix |
|---|---|---|
| 41–42 | `(mean payoff gain 0.0220 vs.\ 0.0091, Wilcoxon $p=3.98\times10^{-10}$, winning 81\% of traces)` | Three independent findings comma-joined. Tolerable inside abstract parentheses; flagged for consistency with L43–44, which uses the same shape with different labels for the same three quantities (§12). |
| 199 | `(GARP pass rate $0.40\to0.10$, $p=0.0073$, zero discards)` | Three independent facts comma-joined inside a parenthetical, in Related Work, in a different unit from L566. Replace with a section cross-reference. |
| 282–284 | `concave, single interior maximum at $s=0.5$, identical across every trace` | Three properties as a comma list with no verb. |
| 324–325 | `All inference ran locally via 4-bit-quantized weights, no GPU or commercial API calls;` | A verbless fragment comma-joined to an independent clause. |
| 368–370 | `higher mean CCEI but a substantially lower GARP pass rate, and the residual-discard group scores lowest` | Two independent findings comma-joined into the colon expansion of a third. |
| 372–374 | `At 3B, the first-attempt and retry-rescued groups sit much closer together, and the selection concern shows up more sharply at 1.5B than at 3B.` | Two findings joined by `and`, where the second restates the first backwards. Delete the second clause. |
| 406–407 | `142 slots kept a usable trace, 8 were residual discards after three attempts` | **A true comma splice** — two independent clauses, comma, no conjunction. Fix: `; 8 were residual discards`. |
| 432–435, 470–472, 484–485, 487–488, 543–545 | Result lists of three or four statistics in one sentence or parenthetical | Split; see §9b. |
| 606–609 | `..., only the within-run replicate variance in the reported confidence intervals and $p$-values.` | Verbless fragment appended by comma. |
| 642–643 | `synthetic tasks, open-weight models, no new dataset, no human subjects` | Four items, no conjunction, verbless. *Stylistic preference — telegraphic register is defensible in a declaration.* The competing convention is a full sentence, which would match the rest of the paper's register. |
| 688–690 | `Comparing raw (pre-repair) payoff between the 57 traces that were already GARP-consistent and the 85 that were not: mean 0.7872 vs.\ 0.7899, Welch $t=-0.07$, $p=0.94$.` | A verbless fragment whose colon introduces three comma-joined statistics — the only fragment in the appendix, and it reads as a lab-notebook line. Fix: `Raw (pre-repair) payoff does not differ between the 57 already-GARP-consistent traces and the 85 violating traces (0.787 vs.\ 0.790; Welch $t=-0.07$, $p=0.94$).` |
| 696–699 | `Similarities were low (0.16--0.31) ..., and \emph{negative} ($-0.35$) ... --- the sign of the outcome tracks ...` | Two results plus an interpretation plus a meta-interpretation in one sentence (§4 #72). |
| 734–735 | `all 85 GARP-violating traces' projections were independently re-verified GARP-consistent, MIP gap $\le 8.1\times10^{-5}$ on every solve.` | Two independent findings joined by a bare comma. Split. |

---

# 10. Aphoristic paragraph endings

**Twenty-eight in 754 lines** — roughly one per paragraph across the whole manuscript. Individually each is defensible; cumulatively they establish a clipped-verdict voice that reads as overclaiming in a paper whose central result is a null. Four earn their place.

| # | Line | Closing text | Verdict |
|---|---|---|---|
| 1 | 36 | `We build that control.` | **EARNS ITS PLACE.** Four words after 60 words of negated setup; it lands, and it is literally what the paper does. Keep. (But see §16 #8 — its antecedent does not grammatically exist.) |
| 2 | 76–77 | `Tracing dose against $\Delta$payoff gives the relationship this paper reports.` | Delete (§3 #2). |
| 3 | 79 | `That relationship turns out not to isolate what it was built to isolate.` | Convert to an ordinary declarative stating the finding (§1 #13, §6 #9). |
| 4 | 86–87 | `We report this as a negative result reached twice by construction, not as a null we happened to observe once.` | Delete (§1 #15, §11). |
| 5 | 97 | `Two further results were not predicted by the design.` | Delete (§2 #4, §3 #4, §11). |
| 6 | 130 | `None occupies all four.` | **EARNS ITS PLACE.** The section's thesis, checkable against the table, short because the claim is short. Keep — but fix the verb: systems do not *occupy* criteria. `No system satisfies all four.` (§13 #26.) |
| 7 | 169 | `report no downstream comparison and a forecasting evaluation respectively.` | Not gnomic so much as clipped; the `respectively` closer is a compression device. Convert (§4 #17). |
| 8 | 178 | `ours is the empirical counterpart to a proposal that has circulated unrun.` | Convert: `We report the measurement that proposal calls for.` `circulated unrun` is a coinage aiming for quotability (§16). |
| 9 | 190 | `which is why we carry a null-operator control neither published negative had.` | Convert: `We therefore carry a null-operator control, which none of the three had.` And check against L113, which already makes this claim — one of the two should go. Note the count error (§13 #14). |
| 10 | 192 | `The closest neighbour on the economics side is invisible to any arXiv sweep.` | An aphorism used as a paragraph *opener*, which is rarer and more conspicuous. Delete (§2 #10, §11). |
| 11 | 200 | `not a replication, since which format is more degrading reverses between their 7B model and ours.` | Convert (§1 #36). Ending the whole section on a disclaimer is separately a structural problem (§14 #7). |
| 12 | 212 | `nothing about the formulation itself is new to this paper.` | Delete (§1 #38). |
| 13 | 239 | `Appendix~\ref{app:payoff-audit}(1) confirms it never reaches the solver.` | Convert: `The incumbent is not passed to the solver (Appendix~\ref{app:payoff-audit}).` |
| 14 | 244 | `no distance-minimization guarantee analogous to a convex-cone projection is claimed.` | Convert to active (§1 #46). |
| 15 | 267 | `--- the same separation our design is built to make.` | Convert: `Our design makes that separation.` |
| 16 | 274 | `the raw dose--response statistic we report in \S\ref{sec:results-c1} is not an artifact of any of the four.` | **EARNS ITS PLACE.** The paragraph's actual conclusion, falsifiable, and it names where the reader can check it. Keep, stated positively: `...is therefore not attributable to any of the four.` |
| 17 | 323–324 | `the two-model, model-major design is both a wall-clock optimization and, after that failure, a correctness requirement.` | Convert (§2 #11). |
| 18 | 336–337 | `Not added at 3B, whose role is a null-effect control rather than a second scale point.` | Convert (§1 #61). |
| 19 | 350–351 | `reported rather than papered over.` | **Delete.** The most self-congratulatory closer in the Method. |
| 20 | 359–360 | `true regardless of whether projection helps, hurts, or does nothing downstream.` | Delete (§2 #13). |
| 21 | 375 | `as a first-class per-condition outcome for every cell.` | Same cadence, same function. Delete `first-class` and the announcement (§2 #14). |
| 22 | 476–477 | `at the identical displacement budget, an operator with no knowledge of GARP buys more than twice the payoff the real repair does.` | Convert. Delete the ratio restatement (already given as $2.4\times$ at L469) and end the paragraph on the statistics. |
| 23 | 497 | `converging on the same negative paired-comparison result is the finding.` | Convert: `Two payoff designs return the same negative paired comparison.` |
| 24 | 499–500 | `exactly the researcher-degree-of-freedom problem an exogenous payoff was introduced to rule out.` | Convert, or move to Limitations. |
| 25 | 513–515 | `the rounds that generate the null's advantage there are precisely the extreme-share rounds the real repair leaves untouched.` | Convert **by adding the numbers currently trapped in the caption** (§8b): with `5 of 21 rounds` and `42\% of its budget on round 3` in the sentence, it stops being an aphorism and becomes a result. |
| 26 | 535–536 | `The raw dose--response relationship reported at the top of this section is real; it is not evidence for the specific mechanism C1 claims.` | **EARNS ITS PLACE.** The section's verdict, short, both halves load-bearing. Keep, dropping `real` (§5 #68) and the internal locator `reported at the top of this section` (§11). |
| 27 | 545–547 | `a further case of GARP pass rate being the sensitive instrument for framing/format disruption while CCEI understates it.` | Convert to a plain declarative (§4 #57), and bound the claim (§14 #10). |
| 28 | 557–558 | `reading their sign difference as a reversal overstates what either number supports.` | Convert, or move to Limitations. |
| 29 | 573–574 | `We do not have an explanation for the reversal; we report the disagreement as a finding in its own right.` | Convert: `We have no explanation for the reversal.` The second clause is self-congratulation and echoes `is the finding` at L497 — the same device twice in one section. |
| 30 | 603–604 | `This is an open design tradeoff: the pass-rate metric is adequately powered throughout, and every CCEI result carries its own confidence interval.` | Convert to an ordinary sentence by deleting the label (§2 #23). |
| 31 | 617–618 | `A third payoff, run only because the second also came back negative, would be payoff-shopping, not a robustness check (\S\ref{sec:results-c1}).` | **EARNS ITS PLACE.** It closes a limitation by naming the methodological principle that motivated it, and the principle is not stated elsewhere. Keep the sentence; apply only the §1 #87 trim. |
| 32 | 625–628 | `only that this paper's own attempt to find a positive relationship, net of displacement, did not succeed.` | Convert (§1 #89). The content stays; the cadence goes. |
| 33 | 642–643 | `We see no elevated misuse risk specific to this work: synthetic tasks, open-weight models, no new dataset, no human subjects.` | Declaration boilerplate; the fragment-list cadence is the aphoristic element. *Lowest priority in the audit.* |
| 34 | 662–664 | `a well-controlled negative, an open identification question, and an instrument-validity finding are exactly what this literature should surface by default rather than paper over.` | **Delete.** It is the last sentence of the paper; it makes a claim about the field rather than about the work; `paper over` is a pun the surrounding prose does not support (§16); and it is the tail of the manuscript's second-worst sentence (§9a #2). The paper should end on its own finding, not on an instruction to the field. |
| 35 | 685 | `never to steer the solution.` | Convert / delete; already deletable on redundancy grounds (§1 #98, §4 #70). |
| 36 | 722–723 | `with no outer search over preference orderings and no alternating scheme.` | **EARNS ITS PLACE on content** — a reader who knows the alternating-scheme literature learns something real from the last five words. Make it positive so it stops sounding like a flourish: `The formulation is solved as a single MILP, with no outer search over preference orderings.` |

---

# 11. Process-record and internal-code leakage

**Sixty-one instances.** After rhetorical negation this is the category most likely to cost the paper credibility, because several entries narrate revisions and beliefs the reader has no way to evaluate.

## 11a. The unnamed pilot — the largest single instance, and it spans four sections

`a pilot` / `the pilot` / `a pilot run` / `a pilot study` / `the pilot's` / `anywhere piloted` appears **19 times** across the manuscript: L92, L98, L99, L319, L321, L330, L343, L348 (×2), L350, L357, L358, L371, L542, L546, L551, L556, L601, L602, L611. It is never described, sized, cited, or located.

The reader is asked to accept, on the authority of a study they cannot see: the framing of the entire Introduction's second unpredicted result (L98–100); model selection (L319–321); the choice of manipulation (L330); the seeding design (L343); the power calculation (L348–350, L601–602); the entire motivation for §sec:discard (L357); the interpretation of the 3B replication (L542); and the limitation on model coverage (L611). Two *numbers* are reported from it — `52\% of sessions (13 of 25)` at L357 and `+0.0169 ($p=0.66$)` at L556 — plus `mean baseline CCEI 0.99` at L321 and `minimum detectable $\approx0.11$` at L350.

**Fix:** one sentence, once, at first use (L92 or L319): `A pilot run of 25 sessions per cell, reported in Appendix X, informed the following design choices.` Then every later reference can say `the pilot` and mean something. Reduce the surface forms to one (`the pilot`) — currently `a pilot study` (92), `a pilot run` (98, 357), `a pilot` (319, 343, 611), `the same pilot` (321), `the pilot` (330, 348, 350), `a pilot's` (343), `anywhere piloted` (611) is a nine-way drift for one referent (§12).

## 11b. Belief-revision and decision-process narration

| # | Line | Exact text | Should become |
|---|---|---|---|
| 1 | 39 | `Under the paper's original exogenous payoff` | `Under the first payoff`. `original` implies a superseded version and invites the question of what replaced it. |
| 2 | 43 | `we decline a third as payoff-shopping` | **Delete from the abstract.** Abstracts should not defend against unmade accusations. If wanted, it belongs in Limitations, where it already appears at L617–618. |
| 3 | 46 | `The paper's standing contributions` | `The paper's contributions`. `standing` narrates that some contributions fell over. |
| 4 | 84 | `as originally proposed` | **Delete.** Proposed by whom, where, when? |
| 5 | 86–87 | `We report this as a negative result reached twice by construction, not as a null we happened to observe once.` | **Delete.** Confessional framing about how the result was arrived at. |
| 6 | 89 | `\S\ref{sec:related} concedes exactly what is not` | **Delete.** `concedes` narrates a rhetorical posture. |
| 7 | 97 | `Two further results were not predicted by the design.` | **Delete.** Whether a result was predicted is not a property a reader can check. |
| 8 | 100 | `the pilot's naive estimate and the corrected main-experiment estimate` | Naming experiments by their revision status is project vocabulary. Use `the uncorrected pilot estimate` and `the retry-corrected estimate`, defined once. |
| 9 | 111 | `fixed before any data collection` | Pre-registration assertion phrased as narrative. Either point to the artifact that proves it or state it as a fact about the payoff: `a payoff defined by prices and income alone, with no free parameters fit to the data`. |
| 10 | 111 | `audited adversarially for leakage` | `checked for leakage` — and say what the check was. |
| 11 | 118 | `corrected for by a stated retry protocol` | `corrected by a capped retry protocol`. `stated` is a pointer to nowhere. |
| 12 | 160 | `We concede the minimum-distance priority unqualified` | Reviewer-response register — a sentence written to an imagined referee. Replace with the fact: `The minimum-distance priority is theirs.` Note that L89 already *promises* this concession, so the section performs a promise rather than stating a position. |
| 13 | 189–190 | `which is why we carry a null-operator control neither published negative had` | Narrated design motivation, and it duplicates L113. |
| 14 | 192 | `The closest neighbour on the economics side is invisible to any arXiv sweep.` | **Delete.** Describes the authors' literature-search procedure, not a property of the cited work. The reader cannot verify it (invisible to *whose* sweep, with what query?). If the point is the venue, say `\citet{cook2026whatllmswant}, in the economics literature, steer...` |
| 15 | 199 | `zero discards` | Pipeline vocabulary used bare in Related Work, ~164 lines before `discards` is defined at L363. Gloss it or drop it from the parenthetical. |
| 16 | 209 | `This section applies, rather than proposes, a projection method.` | **Delete.** A statement about the paper's own construction. |
| 17 | 212 | `nothing about the formulation itself is new to this paper` | **Delete.** Same. |
| 18 | 230–231 | `$L_2$ would require an MIQP solver we do not have configured` | `$L_2$ would require an MIQP formulation.` **The clearest confessional aside about process in the manuscript** — the reader cannot verify, use, or care about what the authors have configured. |
| 19 | 252–253 | `We instead fix, before any model was queried and never re-estimated from any agent's choices, an equal-weight Cobb--Douglas valuation` | Pre-registration smuggled in as an interrupting clause. State it as a fact in its own sentence: `$U_{\mathrm{exo}}$ was fixed before data collection and never re-estimated.` |
| 20 | 269–270 | `We audited this design adversarially, before treating any dose--response result as reportable, for four failure modes` | `We checked four failure modes of this design.` `before treating any ... as reportable` narrates the authors' own decision procedure. |
| 21 | 272–273 | `None survived the audit` | Project vocabulary. `All four are ruled out.` |
| 22 | 274–276 | `A fifth failure mode ... required a new control rather than an audit of the existing design` | Narration of *why the authors' approach changed* — belief-revision leakage. Replace: `A fifth concern --- that the payoff's concavity could reward displacement alone --- motivates the control in \S\ref{sec:method-nullop}.` |
| 23 | 292 | `a second, independently designed payoff` | `a second payoff`. `independently designed` describes the authors' process, not the payoff. |
| 24 | 318 | `at zero API cost` | **Delete.** Project budget, not method. L325 says `no ... commercial API calls` again — the same fact twice in seven lines. |
| 25 | 321–323 | `A third model family was excluded after a reproducible multi-model-residency crash under sustained rotation` | An unspecifiable reference (`a third model family`) plus three pieces of internal implementation vocabulary (`multi-model-residency`, `sustained rotation`, and `model-major` at L324) appearing without definition. Replace: `Models were run one at a time; concurrent residency of a third model caused reproducible crashes.` Or move to a reproducibility appendix. |
| 26 | 324 | `the two-model, model-major design` | `model-major` is an undefined loan from row-major/column-major ordering. Define once: `the design in which all runs for one model complete before the next model is loaded`. |
| 27 | 358 | `the required output-format contract` | `the required output format`. `contract` is code vocabulary, and the contract itself is never stated — a reader cannot evaluate a 52% failure rate against an unstated requirement. |
| 28 | 358 | `the pilot's own naive handling` | `the pilot's handling`. |
| 29 | 363 | `retried up to three total attempts with a fresh seed offset` | `retried up to three times with a new random seed`. *Stylistic preference: `seed offset` is an implementation detail that would sit comfortably in a reproducibility statement.* |
| 30 | 374 | `as a first-class per-condition outcome` | **Delete `first-class`** — programming vocabulary used as an emphasis marker. |
| 31 | 303 | `one replicate slot end to end` (caption) | `slot` is used here before it is defined; the body first uses it at L363. Either define at L303 or use `replicate`. |
| 32 | 406–407 | `187 attempt-records were collected across 150 replicate slots`, `8 were residual discards after three attempts` | Internal data-collection vocabulary (`attempt-record`, `replicate slot`, `residual discard`) used in the Results section's opening sentence. `attempt-record` appears nowhere else in the manuscript. Restate: `We ran 150 sessions and made 187 attempts; 142 sessions produced a usable trace and 8 failed after three attempts.` |
| 33 | 461 | `The confound just tested` | Narrates the paper's own sequence. `The raw-payoff confound`. |
| 34 | 464 | `the payoff gain above` | Internal locator. `the payoff gain`. |
| 35 | 488 | `reported for completeness rather than as the primary comparison` | Process aside. Delete. |
| 36 | 494 | `No third payoff was attempted, and this is a stated scope decision, not a resource constraint.` | Pre-registration-flavoured assertion phrased as narrative and unverifiable by the reader. Reduce to the design fact; move the defence to Limitations, where it already exists at L614–618. |
| 37 | 497–500 | `Redesigning the payoff a third time only because the second attempt also came back negative would be payoff-shopping` | Narrated counterfactual about the authors' own decision process. Move to Limitations. |
| 38 | 512 | `offered as a discussion-level hypothesis rather than a load-bearing result with its own significance test` | A confessional aside about the paper's own internal evidentiary tiers. Delete; say `We do not test this.` |
| 39 | 520–522 | `hand-audited in Appendix~\ref{app:payoff-audit}); every plotted quantity is recomputed by re-solving the projection MILP` | Verification-process record in a caption. Move to the appendix. |
| 40 | 520 | `replicate 12` | Run ID in prose. *Stylistic preference — defensible for reproducibility; the competing convention keeps run IDs in the appendix and identifies the trace by its properties (`the largest-dose trace`), which the caption already does.* |
| 41 | 533 | `C1 as originally proposed` | Narrated belief revision. `The hypothesis that ...`. |
| 42 | 535 | `reported at the top of this section` | Internal navigation. Delete; the reader is four paragraphs from it. |
| 43 | 549 | `the manipulation this study was designed around` | Process record about the study's own planning. `Reciprocal framing`. |
| 44 | 556 | `the pilot's own naive estimate` | Judgment on the paper's own earlier run. `the pilot's uncorrected estimate`. |
| 45 | 568–569 | `we report both` | Process aside; the two $p$-values are already both printed. Delete. |
| 46 | 570–571 | `Against the literature this arm was designed against \citep{wang2025tactics}` | Process record plus repetition (`Against ... against`). `\citet{wang2025tactics} report the opposite:` |
| 47 | 603 | `that scale-up was deferred, not executed` | `deferred` is project-management vocabulary. `We did not run that design.` |
| 48 | 611 | `a pilot found headroom and measurement reliability do not coexist anywhere piloted` | An unspecifiable reference plus a root repeated two words later. Replace: `In our model-selection sweep (\S\ref{sec:design}), headroom and measurement reliability did not coexist in any model tested.` |
| 49 | 611–612 | `a third model family was excluded after the multi-model-residency failure of \S\ref{sec:design}` | `multi-model-residency failure` is an internal incident name; a reader cannot decode "residency". Same term as L322 — remove from both places. |
| 50 | 617–618 | `run only because the second also came back negative` | `came back negative` is lab-log register. `selected after seeing the second result`. |
| 51 | 620 | `An adverse prior the paper now joins rather than argues against` | Narrated belief revision as a heading — it tells the reader the paper changed its stance mid-project. |
| 52 | 635–636 | `The reciprocal-framing manipulation this study was designed around similarly turned out, once corrected, to have no measurable effect` | Two leaks in one clause: `this study was designed around` (project history) and `once corrected` (belief revision). |
| 53 | 636–637 | `the coherence it was thought to disrupt` | Unattributed belief. `the coherence it was designed to disrupt`. |
| 54 | 648 | `This paper set out to measure` | Project narrative as the Conclusion's opening. |
| 55 | 653 | `as originally proposed` | Second occurrence of #4, in the Conclusion. |
| 56 | 676 | `the four-part adversarial audit` | Names a project artifact rather than content; `adversarial` asserts a property of the authors' process. (Sentence deleted anyway — §3 #24.) |
| 57 | 680 | `The one near-miss is that ...` | Narrates the audit's own process — we looked, we nearly found something. State the fact directly. |
| 58 | 682 | `--- a plausible leakage channel on first read ---` | **The clearest process leak in the appendix.** Narrated belief revision about the authors' own reading experience; the reader cannot use "on first read" and it invites the question of what else looked fine on first read. **Delete.** |
| 59 | 683 | `(the solver used has no such interface)` | Unspecifiable reference — the solver is never named in the appendix (it is `HiGHS`, named 460 lines earlier at L222). Name it here. |
| 60 | 684 | `an upper-bound sanity ceiling` | `sanity ceiling` reads as an internal name for a logged diagnostic; `log` is code vocabulary. Replace: `an upper bound on the reported distance`. |
| 61 | 725 | `Three method commitments, each carrying an explicit risk.` | Pre-registration-flavoured framing (`commitments`, `explicit risk`) presented as narrative, and it over-promises (§14 #17). |
| 62 | 731 | `We verified the reported distance is stable across ...` | A process assertion with no criterion (§5c). The reader is asked to accept a verification they cannot evaluate. |
| 63 | 733 | `used everywhere else` | Unspecifiable reference to the rest of the pipeline. Replace with a `\S`/`\ref` to where the Warshall-closure check is defined. |
| 64 | 678–679 | `The payoff implementation has no dependency on the projection implementation` | `implementation` twice in one clause is codebase vocabulary standing in for the objects themselves. `The payoff depends on no quantity produced by the projection.` |

## 11c. Internal tracking labels visible to the reader

**The claim-numbering scheme `C1`/`C2`/`C3` is never introduced anywhere in the manuscript.** Verified across all 754 lines. The labels appear in this order:

| Label | First appearance | All appearances |
|---|---|---|
| `C3` | **L102**, `(our claim C3)`, in the Introduction, with no scheme ever having been introduced | L102, L660 |
| `C1` | **L429**, inside a subsection heading, `(C1)` | L429 (heading), L533, L536, L653 |
| `C2` | **L626**, in the Limitations | L626, L656 |

So a reader meets `C3` first, in a parenthesis, 327 lines before `C1` appears, and 524 lines before `C2` appears. `C1` reaches most readers only through the cross-reference label `\S\ref{sec:results-c1}` (L83, L117, L274, L457, L529, L618, L624, L633), which renders as a section number and hides the code — except that the code is then printed bare in the heading at L429. **Fix:** either introduce all three claims by number at one place in the Introduction, or drop the labels entirely and refer to the claims by their content. As it stands the Conclusion's bare `C1` (L653) and `C3` (L660) are unreadable to anyone who skipped the Results.

Two further label defects:
- **L238, `Appendix~\ref{app:payoff-audit}(1)`** — a hand-written sub-item index `(1)` appended to a `\ref`. If the appendix numbers its checks, use a real label; if not, `(1)` is a private index the reader cannot resolve. Replace: `Appendix~\ref{app:payoff-audit}, check~1`.
- **L280, `\label{sec:method-nullop}`** does not match its heading (§7 #5); **L741, `\label{sec:method-guarantee}`** is attached to no sectioning command and resolves to the wrong target (§7 #12).

---

# 12. Terminology and notation drift

This category is re-derived from the whole manuscript rather than merged from section-local inventories, because every entry below is invisible from inside any one section. Line references are exhaustive within each row.

## 12a. Master table — concepts called by more than one name

Ordered by severity: number of surface forms, times how load-bearing the concept is.

| Rank | Concept | Every name used, with lines | Recommendation |
|---|---|---|---|
| 1 | **The repair operator** (the paper's primary object) | `the minimal MILP perturbation restoring GARP-consistency` (38); `the real repair` (40, 43, 452, 465, 469, 473, 484, 489, 505, 515, 526, 633, 652); `the minimal quantity perturbation` (69–70); `a projection` (71, 205, 271); `the real GARP-restoring repair` (82); `restoring rationality` (84); `\citet{demuynck2023computing}'s minimal-quantity-error MILP projection` (109); `GARP-restoration` (116, 630); `a repair operator` (184); `minimal-quantity-error MILP` (206, 306); `multiplier-free ordinal characterization` (210–211 and again 219–220); `minimal-quantity-error GARP repair` (211, 650); `the minimal perturbation $\tilde{x}_t$` (217); `the real projection` (287); `a real repair algorithm` (297); `the real repaired sequence` (307); `the repair` (526); `coherence-repair` (633, 639); `repair` (639, 649); `repair size` (651); `a GARP repair` (747); `an unregularized projection` (730) | **Fifteen distinct surface forms for one operator, and the worst drift in the manuscript.** Fix: `the minimal-quantity-error MILP projection` at first definition (L109 and L206 only); `the projection` in Method prose; `the real repair` reserved *strictly* for the paired contrast with the null operator, and defined at that contrast (L285). Retire `restoring rationality`, `GARP-restoration`, `coherence-repair`, `repair size`, and the bare `repair`. Note that `real` is doing three different jobs at L287 (the projection), L297 (a class of algorithms) and L307 (the output sequence). |
| 2 | **The GARP-blind control operator** | `a GARP-blind null operator` (38, 465); `the null` (40, 44, 288, 291, 473, 475, 483, 489, 505); `A control absent from every published axiom-enforcement result` (79); `an operator that knows nothing about GARP` (80–81); `a distance-matched, GARP-blind null-operator control` (113–114); `a null-operator control` (190); `\textbf{null operator}` (285); `the GARP-blind null` (307, caption only); `a \textbf{primary}, information-fair null` (295); `an \textbf{oracle} null` (296); `size-matched null operator` (451); `primary-null` (456); `the primary, information-fair null` (483); `Experiment 2 primary null` (504); `a matched GARP-blind operator` (624); `a GARP-blind operator` (617, 632); `a distance-matched, GARP-blind null operator` (652); `the null's advantage` (655); `the null-operator result` (623) | **Nineteen surface forms.** Fix: `the null operator` for the construct, `the primary null` and `the oracle null` for the two instances. The matching property has three names (`distance-matched`, `size-matched`, `spending the identical displacement budget`) and the blindness property has three (`GARP-blind`, `information-fair`, `knows nothing about GARP`) — state each once, in the Method, and never again. Delete `information-fair` from running prose entirely (it is never defined — §12d). |
| 3 | **`null` — a term collision on the paper's most load-bearing word** | `null operator` and its 19 variants above **vs.** `the null-effect control` describing the **3B model** (320, 337) **vs.** `the headroom/null-control design` (609) **vs.** statistical nulls: `two statistically indistinguishable nulls` (558), `a well-controlled negative` (663) | **Serious, and cross-sectional.** Three unrelated concepts share the word: the GARP-blind operator, the 3B model's design role, and a statistical null hypothesis. L609's `null-control` is ambiguous between the first two. Rename the 3B model's role to `the low-headroom control` or `the no-effect-expected model` and never write `null-control`. |
| 4 | **The perturbation magnitude** | `displacement magnitude` (34–35, 658); `the identical displacement budget` (38–39, 81, 476); `\emph{dose}` (65, 232) and `dose` (72–73, 77, 91, 115, 273, 306, 384, 390, 412, 418, 432, 438, 441, 473, 489, 610, 651, 693, 701, 704); `a graded, cardinal dose` (72–73); `a graded coherence-indexed dose` (91); `distance-matched` (113, 652); `minimal total absolute displacement` (228); `$L_1$ projection distance` (232); `the reported distance` (238, 684, 731); `$L_1$ displacement` (286, 306, 308, 465); `total $L_1$ displacement` (286); `displacement` (276, 627, 632); `mean dose ($L_1$)` (384, 390, 418); `size-matched` (451); `the same total displacement` (528); `repair size` (651) | **Nine names for one quantity plus three for the matching constraint.** Fix: `dose` in prose after one definition; `$L_1$ displacement` only where the metric matters; `dose-matched` as the single name for the constraint. The caption at L528 should read `the same dose`. |
| 5 | **The unit of analysis — six words, two or three actual objects, and nothing defines the levels** | `traces` (41, 44, 221, 224, 232, 237, 285, 293, 385, 407, 432, 434, 451, 472, 485, 688, 693, 696, 734); `realized choice sequence` (70–71); `sequence` (74, 211); `session` (233, 357, 366, 368, 380, 554); `slot` (303, 363, 385, 386, 406, 407); `replicate` (303, 341, 351, 408); `replicate slot` (303, 406); `attempt-record` (406); `draw` (293, 352, 456, 482, 490); `cell` (341, 375, 408, 411, 418, 606); `observation` (214, 727); `arm` (304, 336, 568, 580) | **The single most confusing drift for a reader trying to check the counts.** A `slot` appears to be a design position, a `session` an execution attempt, a `trace` the resulting data, and an `attempt-record` one attempt — but nothing says so, and `replicate` is used for both a slot and a trace. `attempt-record` (L406) appears exactly once in the manuscript. **Fix: one sentence near L341 defining the three levels (slot → attempt → trace), then use exactly those words.** Delete `attempt-record`, `replicate slot`, and `arm`. Note L385–386 says `slots` where Table 2's own column header is `$n$` and the surrounding body says `sessions`. |
| 6 | **The failure being repaired** | `incoherent preferences` (32, 127); `choice inconsistency` (title, 18); `coherence` (34, 46, 91, 93, 98, 173, 622, 626, 636, 656, 691); `GARP-consistency` (38, 218, 271, 463, 533, 624, 648); `GARP-consistent` (71, 225, 385, 689, 730, 735); `classical rationality axioms` (60); `rationality` (84); `inconsistency` (61); `GARP pass rate` (198, 369, 385, 543, 554, 565, 579, 598, 661); `rationalizability` (185); `GARP-violating` (224, 285, 293, 432, 451, 734); `genuinely violating data` (731) | `coherence`, `rationality` and `consistency` are used interchangeably for one property — `restoring coherence` (35) vs. `restoring rationality` (84) vs. `restoring GARP-consistency` (624, 648) are the same act under three names. **Fix:** `GARP-consistency` as the technical term, `coherence` as its informal gloss defined once as equivalent, `rationality` reserved for the axiom literature. **Note L691 specifically:** `between coherence and payoff score` inside Appendix A is the only use of `coherence` in the appendix, unglossed, inside a claim sentence — change to `between GARP-consistency and payoff`. |
| 7 | **The exogenous payoff, and the role/version confusion** | Role: `exogenous payoff` (39–40, 82, 111, 114–115, 129, 141, 166, 176, 246, 263, 467, 500, 534, 614); `an exogenous behavioral payoff` (236); `the outcome measure` (76); `the payoff function` (462); `the same payoff function used everywhere else` (289). Version: `the paper's original exogenous payoff` (39); `an equal-weight Cobb--Douglas valuation` (253); `the original payoff` (469, 479, 502, 523); `the original fixed payoff` (502–503); `the corrected payoff` (479, 524); `a second, independently designed payoff` (292); `both payoff designs` (309); `this payoff` (275, 295). Score: `The payoff score` (257); `the efficiency ratio` (257); `$\Delta$payoff` (77 and throughout); `mean payoff gain` (40); `the exogenous payoff gain` (117); `payoff gain` (651) | **The role and the version are never held apart.** `exogenous payoff` is used both as the name of the design property and as if it named a specific version. **Fix:** `the exogenous payoff` for the property; `payoff A (fixed target)` and `payoff B (per-trace target)` — or `Experiment 1 payoff` / `Experiment 2 payoff` — for the versions; `$\Delta$payoff` for the change, replacing `mean payoff gain` (40), `exogenous payoff gain` (117), and `payoff gain` (651). |
| 8 | **The two experiments** | `Experiment 1` / `Experiment 2` (454, 455, 469, 479, 490, 504, 505, 508, 509) **vs.** `original payoff` / `corrected payoff` (454, 455, 469, 479, 502, 523, 524) **vs.** `the paper's original` (495–496) **vs.** `under two independently designed payoffs` (83, 114–115, 614, 631, 653) **vs.** `two payoff designs` (309) | Two vocabularies for one split. Bind them once — `Experiment 1 (original payoff)` at first use — then use `Experiment 1` alone. |
| 9 | **The attempt-outcome groups — three groups, ten names** | `kept on the first attempt` (367, 381) / `first-attempt success` (392, 396, table) / `first-attempt ... groups` (372) / `first-attempt ... discard rates` (374) / `First-attempt discard` (550); `rescued by a later retry` (367, 381) / `retry-rescued` (368, 393, 397); `still discarded after three attempts` (367, 382) / `a residual discard` (363) / `residual discard` (394, 398) / `residual post-retry discard rates` (374) / `the residual-discard group` (369) / `residual discards` (407) / `a residual 20.0\%` (551) | Fix the table's row labels as canonical (`first-attempt success`, `retry-rescued`, `residual discard`) and use exactly those three in prose and caption. |
| 10 | **The retry mechanism** | `a capped retry protocol` (99, 305, 361); `a stated retry protocol` (118); `the retry protocol` (551) | **`the capped retry protocol`**, defined once. `stated` (118) is a pointer to nowhere. |
| 11 | **The pilot** | Nine surface forms across 19 uses — see §11a. | **`the pilot`**, one name, one description, one location. |
| 12 | **The Afriat/CCEI index** | `CCEI` (101, 177, 181, 183, 198, 321, 334, 346, 350, 363, 369, 382, 385, 390, 411, 418, 544, 547, 554, 566, 579, 581, 587, 598, 601, 602, 604); `the Afriat index` (196); `CCEI/Houtman--Maks` (181); `$1-\mathrm{CCEI}$` (177) | **`the Afriat index` at L196 and `CCEI` at L198 are the same quantity, describing the same finding, in adjacent sentences of one paragraph** — this reads as two results. Use `CCEI` throughout. `CCEI/Houtman--Maks` is a legitimate compound of two distinct indices but should be `CCEI and Houtman--Maks` rather than slashed. **`CCEI` is never expanded anywhere in the manuscript** (§12d). |
| 13 | **`power` — a term collision in adjacent sentences** | Statistical power of the design: `power $\ge0.999$`, `$\ge0.80$`, `underpowered` (348–350), `adequately powered` (603–604), `A CCEI-power-matched design` (602) **vs.** `Every replicate's Bronars power ... all 150 draws held power $\ge0.998$` (351–352) | **Serious, and the two meanings sit in consecutive sentences.** Three numbers of the form $\ge0.99x$ appear in three consecutive lines meaning two different things. Rename the second: `Bronars power of the budget set`, and never write bare `power` for it. |
| 14 | **The four evaluation criteria** | `the four criteria` (128); the four table column heads (140–141); `our three legs` (194); `all four` (130) | `legs` appears **only at L194** in the manuscript and carries a count error (§13 #2). Use `the four criteria` in both places. |
| 15 | **The minimum-distance property** | `a formal minimum-distance projection` (130); `Min.-distance projection` (141, column head); `the minimum-distance priority` (160); `a minimum-distance method` (167); `distance-minimization guarantee` (244, 748) | Four surface forms in Related Work alone. Use `minimum-distance projection` throughout; drop `formal` (130); `priority` (160) is a bare definite noun for "who did it first" and should be rephrased. |
| 16 | **The GARP test itself** | `the same combinatorial check used throughout` (225–226); `the GARP check` (288); `combinatorial Warshall-closure GARP check` (306, **caption only**, and 733) | **The algorithm is named in a figure caption (L306) before it is named in the body**, and the body's own reference at L226 is a bare definite noun with no antecedent. Use `the Warshall-closure GARP check`, named at L226, everywhere. |
| 17 | **Cobb–Douglas objects — four different things under one name** | `A Cobb--Douglas demand share-fitted to each trace's own observed data` (236–237, the feasibility incumbent); `an equal-weight Cobb--Douglas valuation` (253, the exogenous payoff); `the closed-form Cobb--Douglas demand` (255, the optimum); `a per-trace Cobb--Douglas weight $\alpha_s$` (292–293, the randomized payoff); `a Cobb--Douglas demand` (681) | Two of these — the share-fitted incumbent and the exogenous valuation — **must be kept strictly apart for the circularity argument at L249–252 to work**, and they are 17 lines apart under nearly the same name. Name them: **fitted incumbent**, **exogenous valuation**, **exogenous optimum**, **randomized valuation**. |
| 18 | **The warm-start object vs. the solver's own term** | `feasibility incumbent` (237, 250, 681) **vs.** `an actual incumbent` (683, the solver's incumbent solution) | **`incumbent` is used in two senses inside one sentence at L681–683.** Rename the paper's own construct to `feasibility reference` or `Cobb--Douglas reference bundle` so the solver's `incumbent` can keep the word. |
| 19 | **Model names — three conventions** | Ollama tags `\texttt{qwen2.5:1.5b-instruct}` / `\texttt{llama3.2:3b-instruct}` (319–320); short tags `qwen2.5:1.5b` / `llama3.2:3b` (392–398, 420–424, 451–452, 520, 579); scale labels `1.5B` / `3B` (83, 93–94, 328, 337, 349, 357, 368, 372, 432, 437, 542, 549, 573, 598, 622); `the headroom model` (319, 437); `the null-effect control` (320); official form `Qwen2.5-7B` (572); `Qwen2.5` (197, 122) | Four conventions, one of which (`the headroom model`) is never defined. Give the full tag once, use `1.5B`/`3B` in prose, use the short tag in tables, and make the comparison model consistent with whichever form is chosen. |
| 20 | **Elicitation format** | `multiturn` (331, 423, 553, 562, 566, 579, 590); `multi-turn` (197, 334, 336, 573); `single-turn` (330, 334, 335, 336, 572); `single turn` (329); `single-turn-vs-multi-turn` (119, 121); `25 sequential calls` (579); `separate sequential calls` (104, 331–332); `the multiturn/format effect` (562); `elicitation-format manipulation` (119, 660–661) | See §15 — `Multiturn`/`multiturn` vs. `multi-turn` is also a spelling inconsistency. Pick `multi-turn` and `single-turn` throughout, including the table labels at L423 and L590. |
| 21 | **The framing manipulation** | `reciprocal-price framing manipulation` (98); `\textbf{Reciprocal}` (329); `an inverted-price framing manipulation` (330); `the price-framing mechanism` (334); `reciprocal framing` (357, 366, 543, 550, 552); `reciprocal-framing session` (366, 380); `the reciprocal-framing manipulation` (538, 621, 635); `a framing manipulation` (660); `the pilot's full framing-effect magnitude` (348) | Define `reciprocal (inverted-price) framing` once at L329 and use `reciprocal framing` thereafter. **L660 drops the `reciprocal-` qualifier in the Conclusion**, where a reader may take it as a different manipulation. |
| 22 | **The discard problem** | `discard-selection` (99, 550, 660); `the discard rate` (101); `a naive discard rule` (103); `no discard confound` (106); `discard-selection bias` (118); `a discard-selection instrument-validity finding` (46–47); `survivorship` (538); `zero discards` (199, 567, 580); `The discard-selection finding` (640); `a discard-selection artifact` (660) | Fine as a family, but `discard-selection bias` should be the standard name at all sites, and `survivorship` (538) appears once, in a heading, as a fourth name. **L640's `finding` and L660's `artifact` deliberately denote different things** — the finding is that the instrument discards; the artifact is the apparent effect it produced — but nothing tells the reader they differ. Name them separately. |
| 23 | **The dose relation** | `dose--response` (115, 175, 273, 429, 610, 634, 651, 704); `raw dose--response relationship` (116, 535); `the raw dose--response statistic` (273); `a real, monotone raw dose--response relationship` (651); `raw dose--response correlation` (634); `the relationship this paper reports` (77); `That relationship` (79) | `relationship` and `correlation` name the same object at L634 and L651. Pick `dose--response relationship`. L77–79 introduces the object with no name at all and then refers back to it with a bare demonstrative. |
| 24 | **The condition/arm vocabulary** | `Three conditions` (328); `condition` (341, 375, 411, 418, 552, 580, 606); `Our arm` (336); `arm` (304 caption, 568, 580); `prompt/format arm` (304); `the cycle-tolerant arm` (172, a third party's) | Use `condition` in prose; the caption's `prompt/format arm` should read `prompt/format condition`. |
| 25 | **The unnamed pattern** | `the sensitive instrument for framing/format disruption` (546); `the same pattern` (570); `a further case of the same pattern` (570) | A bare definite noun used twice with no name ever given. Name it once (e.g. `the GARP--CCEI divergence`) and use the name at L570. |
| 26 | **The extremity claim** | `Trace extremity` (44, 502); `extremity-advantage` (510); `extreme-share rounds` (515); `trace extremity` (655) | Defined only at L502–503, used in the abstract at L44 and in the Conclusion at L655 as if established. Hyphenation is also inconsistent (`extremity-advantage` vs. `the null's advantage`). |
| 27 | **The prior operator** | `the prior operator's cone` (746) | A bare definite noun introduced with no name — it means the \citet{wang2026poise} operator. Write `their operator` or name it. |
| 28 | **MILP vs. MIP** | `MILP` (38, 69, 109, 206, 221, 222, 306, 326, 522, 683, 710) vs. `MIP gap` (226, 735) vs. `MIQP` (231) | Two initialisms for one problem class, 25 lines apart in the appendix. Either write `MILP gap` throughout or note at first use that the solver reports it as the MIP gap. As printed, `MIP gap` reads as a typo for `MILP`. |

## 12b. Overloaded symbols — the full cross-document collision

**The appendix agent flagged `$p$` and `$t$` as locally overloaded. Verified against the whole manuscript: the collision is document-wide and far larger than the appendix-local case.**

| Symbol | Meaning 1 | Meaning 2 | Meaning 3 | Verdict |
|---|---|---|---|---|
| **$p$** | **Price vector.** `$(p_t, x_t)_{t=1}^T$` (214); `budget line $(p_t, I_t)$` (254); `$p_{t,A}$`, `$p_{t,B}$` (255–256); `no $p$/$x$ data at all` (385); `the exogenous $(p, I)$` (678); `$p_t\!\cdot\!\tilde{x}_t = I_t$` (727) | **$p$-value.** L41, 43, 199, 433, 434, 437, 438, 440, 442, 443, 444, 471, 474, 485, 487, 490, 543, 544, 554, 555, 556, 566, 568, 569, 581, 582, 583, 690, 702, 705, 707, 708 — **over 40 occurrences** | `$p_{\mathrm{BH}}$`, `$p_{\mathrm{Holm}}$` (543–544, 568–569) | **CONFIRMED as a document-wide collision, not an appendix-local one.** The two meanings first collide at **L41 vs. L214** — the abstract's `Wilcoxon $p=3.98\times10^{-10}$` precedes the Method's `$(p_t, x_t)$` by 173 lines, so a reader meets $p$ as a p-value first and as a price second. They then collide *inside the same table caption* at L385 (`no $p$/$x$ data at all`) and its neighbours, and again inside Appendix A twelve lines apart (price at L678, p-value at L690). `$p<0.0001$` in a paper whose $p_t$ is a price vector is genuinely ambiguous on a skim. **Fix, document-wide:** keep $p_t$ for prices and set the statistic upright and named — `$P = 0.94$`, or spell it (`$p$-value $0.94$`) at least at first use in each section. |
| **$t$** | **Observation index.** `$T$ observations $(p_t, x_t)_{t=1}^T$` (214); `$x_{t_1}$ ... $x_{t_n}$` (215–216); `$\tilde{x}_t$` (217); `$\sum_t\sum_k$` (233, 737); `$(p_t, I_t)$` (254); `$x^*_t$` (255, 286); `$u_t$`, `$U_{t,v}$` (721–722); `$\max_t I_t$`, `$\min_t I_t$` (728–729); `$w_{t,k}$, $d_{t,k}$` (737–738) | **$t$-statistic.** `one-sample $t=5.41$` (434); `$t=11.4$` (443); `$t$-test` (545, 583); `Welch $t=-0.07$` (689); `$t=11.43$` (707); `$t=-1.36$` (708) | **$t$-distribution.** `via the $t$-distribution ($df=29$)` (582); `[95\% CI ($t$)]` (587) | **CONFIRMED as a document-wide collision.** Three unrelated roles. The worst site is **Table 4's caption (L582–583)**, where `the $t$-distribution ($df=29$) (two-sample $t$-test, $p=0.91$)` puts the distribution, the test and a p-value in one clause of a paper whose $t$ indexes observations. **Fix:** as for $p$ — name the statistic (`Welch's $t$-statistic $-0.07$`) rather than relying on the bare symbol. |
| **$N$** | **Replicates per cell.** `$N=30$` (325, 341, 348, 600); `the full $N=30$ design` (325) | **A price.** `$M,N\sim U[0.1,1.0]$ i.i.d.` (342) | **A required sample size.** `$N\approx111$--$161$` (602) | **Both meanings appear in the same sentence at L341–342.** Rename the prices to $p_A, p_B$ — which the paper *already* uses as $p_{t,A}$, $p_{t,B}$ at L255–256, so the price symbols are inconsistent with themselves. Keep $N$ for replicates. |
| **$K$** | **Number of goods.** `$K$ goods` (214); `$K=2$` (342, 522) | **Number of replicate draws.** `$K=20$ replicate draws` (293); `$K=20$ draws of the random target` (456); `across $K=20$ independent draws` (482) | — | **The manuscript asserts both `$K=2$` and `$K=20$`**, 49 lines apart at L293/L342 and again at L482/L522 — the second pair 40 lines apart with one of them inside a figure caption. Rename the draw count to $R$ or $B$. |
| **$s$** | **Expenditure share on good A.** `$s$ the expenditure share on good A` (282); `$s=0.5$` (284, 480, 523); `$s$ $0.11\to0.65$`, `$s=0.99$` (526–528); `per-round expenditure share $s$` (525) | **A subscript on the per-trace weight.** `$\alpha_s$` (293, 295, 296, 481, 525); `$x^*_{\alpha_s}$` (296) | — | The subscript $s$ in $\alpha_s$ presumably indexes traces, but $s$ was defined as a share eleven lines earlier and both appear in the same subsection *and* in the same figure caption (L525: `expenditure share $s$` and `$\alpha_s=0.704$` in adjacent sentences). Rename to $\alpha_i$ or $\alpha^{(r)}$. |
| **$\alpha$** | **Big-$M$ constant.** `the big-$M$ constant ... computable a priori as $\alpha > \max_t I_t$` (727–728) | **The per-trace Cobb–Douglas weight.** `$\alpha_s\sim\mathrm{Uniform}(0.05,0.95)$` (293, 481, 525, 296) | **Conventionally, a significance level** — in an appendix dense with p-values | Two unrelated roles for the same Greek letter, 434 lines apart, plus a third by convention. The big-$M$ constant should simply be $M$ (which is currently a price — see $N$ above); resolving the price symbols frees it. |
| **$M$** | **A price.** `$M,N\sim U[0.1,1.0]$` (342) | Referenced but not symbolized as `the big-$M$ constant` (727) | — | $M$ is used once as a price, never defined as one, and conventionally denotes a bound — which is exactly what L727 calls for and then denotes $\alpha$ instead. |
| **$U$** | **The exogenous valuation.** `$U_{\mathrm{exo}}(x) = x_A^{0.5} x_B^{0.5}$` (253–254, 257–258) | **Binary comparison indicators.** `$U_{t,v}\in\{0,1\}$ for $t\neq v$` (721–722) | Related but distinct: `ordinal utility levels $u_t\in[0,1]$` (721) | Capital $U$ carries a utility function and a binary indicator matrix; lowercase $u_t$ carries a third object. Distinguish typographically. |
| **$I$** | **Income.** `$I_t$` (254, 255–256, 727, 728, 729) | — | — | Not overloaded, but **internally inconsistent**: `income is fixed throughout` (233–234) and `income fixed at 100 throughout` (727) against a time-subscripted `$I_t$` and the extremal expressions `$\max_t I_t$` / `$\min_t I_t$` (728–729). See §13 #8 and #22. |
| **$r$** | Pearson and partial correlation (440, 441, 442, 474, 490, 504, 505, 510, 702, 703, 705, 706) | — | — | Consistent. No change. |
| **$T$** | Number of observations per trace (214, 221, 341, 521) | — | — | Consistent as a symbol, but stated in three notations as prose: `$T=25$` (221, 341), `all 25 rounds` (328), `each of the 25 rounds` (331), `$\ge20/25$-valid-rounds` (363). |
| **$\lambda$** | Shrink factor, `$\lambda\in[0,1]$` (286) | — | — | Introduced, used once, never reported. Is its distribution across traces a quantity the reader should see? |

## 12c. Same quantity under different symbols or labels across text, figures, tables and appendix

| Quantity | Text form | Table form | Figure/caption form | Appendix form | Fix |
|---|---|---|---|---|---|
| GARP pass rate after the format manipulation | `$0.40\to0.10$` (199); `from 40\% to 10\%` (565) | `0.40` / `0.10` (422–423); `12/30 (40.0\%)` / `3/30 (10.0\%)` (589–590) | — | — | **Four formats for one quantity.** Pick count/$n$ with the percentage in parentheses. |
| GARP pass rate, 3B reciprocal | `collapses from 0.73 (22/30) to 0.39 (11/28)` (543) | `0.73` / `0.39` (420–421) | — | — | Consistent in value; the text adds the counts, the table does not. |
| \citet{wang2025tactics}'s CCEI effect | `drops CCEI by up to $0.241$` (198) | — | — | — | **vs. `moves CCEI by up to $-0.241$` (334).** Same source, same effect, **opposite sign**. See §13 #13. |
| The largest-dose trace | `one far-larger-dose trace` (453, caption) | — | `$L_1=111.64$` (520, caption) | `111.64` (693) | The same trace described qualitatively in one caption and exactly in the next, and exactly again in the appendix. |
| Mean $\Delta$payoff, Experiment 1 | `$+0.0091$` (434); `0.0091` (41, 471) | column `mean $\Delta$payoff`, per cell (420–424) | — | — | The table column is unsubscripted and its payoff version unstated (§8d, §13 #10). |
| $\Delta$payoff, real vs. null | `$\Delta$payoff$_{\mathrm{null}}$` / `$\Delta$payoff$_{\mathrm{real}}$` (470–471, 473, 484, 489) | bare `mean $\Delta$payoff` (418) | `Real repair's $\Delta$payoff` / `the size-matched null operator's $\Delta$payoff` (450–451) | `$\Delta$payoff` (703, 705) | Four notations. Subscript consistently or name in words consistently. |
| Win rate | `winning 81\% of traces` (41); `70 of 85 traces (82\%)` (434); `winning 69 of 85 traces (81\%)` (472); `win rate 70.8\%` (43, 485); `win rate 80.4\%` (487) | — | — | — | Same quantity, two presentations, two precisions. Use `count of 85 (percentage)` throughout. |
| MIP gap | `MIP gap $\le 8.1\times10^{-5}$` (226) | — | — | `MIP gap $\le 8.1\times10^{-5}$` (735) | Consistent value, stated twice in near-identical sentences 509 lines apart (§14 #16). |
| Dose | `dose` (prose) | `mean dose ($L_1$)` (390, 418) | `$L_1$ displacement` (306, 308); `$L_1=111.64$`, `42\% of its $L_1$ budget` (520, 527) | `dose range (0.17 to 111.64)` (693), with **no unit given anywhere** | Three labels; and the appendix uses `dose` with a numeric range and no unit. |
| CCEI | 2 dp `0.99` (321); 4 dp `0.9522` etc. (554, 566) | 4 dp (392–398, 420–424); 4 dp with CI (589–590) | — | — | Three precisions for one metric (§13 #24). |

## 12d. Terms used once, or used as if defined and never defined

| Term | Where | Problem |
|---|---|---|
| `CCEI` | first at L101, 27 uses | **Never expanded anywhere in the manuscript.** Not "Critical Cost Efficiency Index", not anything. First use is a bare acronym in the Introduction. |
| `payoff-shopping` | 43, 498, 618 | Coined in the abstract, used three times, defined nowhere. |
| `trace extremity` | 44, 502, 655 | Used in the abstract 458 lines before its only definition. |
| `the coherence--competence question` | 46–47, 626, 656 | The word `competence` appears nowhere else in the manuscript. |
| `capacity-deconfounded` | 46 | Compound never unpacked. |
| `the headroom model` | 319, 437 | Never defined; `headroom` recurs bare at L609, L611. |
| `information-fair` | 295, 483 | Never defined. |
| `distance-matched` | 113, 652 | The mechanism is described elsewhere under a different name (§12a #2). |
| `legs` | 194 | Only occurrence in the manuscript; also a count error. |
| `the Afriat index` | 196 | Only occurrence; same object as `CCEI` two lines later. |
| `Afriat machinery` | 164, 194 | Informal collective noun for an unnamed set of objects, used twice as a criterion, defined never — and it is *not* the same thing as `the Afriat index`. |
| `chain-monotone cone` | 159 | Used without gloss. |
| `pool-adjacent-violators` | 158 | Used without gloss. |
| `length-controlled metric` | 174 | Used without gloss. |
| `rationalizability` | 185 | Used once; the Method never defines it. |
| `capacity` | 173, 657 | Used as a term of art on first use, undefined. |
| `attenuation` | 349 | Undefined, and it is carrying a power claim. |
| `continuous-density prices` | 342 | Used once; means "drawn from a continuous distribution", which the next clause already says. |
| `model-major` | 324 | Undefined loan from row-major/column-major. |
| `multi-model-residency` / `sustained rotation` | 322, 612 | Internal incident vocabulary; `residency` and `rotation` are undecodable. |
| `output-format contract` | 358 | The contract itself is never stated. |
| `the $\ge20/25$-valid-rounds threshold` | 363 | What makes a round valid is never stated. |
| `attempt-record` | 406 | Only occurrence. |
| `slot` | 303, 363, 385, 386, 406, 407 | Used at L303 (a caption) before its first body use at L363, and never defined against `session` or `trace`. |
| `budget-set design` | 542 | Only occurrence. |
| `near-1 compression` | 545 | Only occurrence. |
| `survivorship` | 538 | Only occurrence, in a heading. |
| `WSCV` | 599 | Used unexpanded, once. |
| `the headline statistic` | 608 | Bare definite noun — which statistic? CCEI, GARP pass rate, and payoff gain have all been referenced. |
| `derived quantity` | 678 | Appears once, in a bold lead, carrying the whole claim of part (1). |
| `sanity ceiling` | 684 | Only occurrence; not a term of art. |
| `non-expansiveness` | 745 | Used once, unglossed, in the appendix's longest sentence. |
| `weakly-closer-to-ground-truth guarantee` | 745 | Same clause, same problem. |
| `alternating scheme` | 723 | Used once, unglossed. |
| `ordinal utility levels` | 721 | Glossed by its symbol but never tied explicitly to `ordinal characterization` (719). |
| `$\lambda$` | 286 | Introduced, used once, never reported. |
| `C1`, `C2`, `C3` | see §11c | The scheme is never introduced. |

## 12e. Bare definite nouns introduced without a name and then reused

| Line | Text | Problem |
|---|---|---|
| 36 | `We build that control.` | `that control` refers to the control implied by `None controls for displacement magnitude` (34), which is a **verb**, not a noun. Grammatically the antecedent does not exist. |
| 77 → 79 | `the relationship this paper reports` → `That relationship` | An antecedent that itself was never named. Give it a name at L77 (`the dose--$\Delta$payoff relationship`). |
| 160 | `the minimum-distance priority` | First and only use; "priority" in the precedence sense is established nowhere. |
| 172 | `the cycle-tolerant arm` | Definite article on first mention; the reader has no arm in mind yet. `their cycle-tolerant arm`. |
| 185 | `the same distinction` | Refers back to an unnamed distinction from L184. |
| 226 | `the same combinatorial check used throughout` | Definite article, first mention, no antecedent. |
| 289 | `the same payoff function used everywhere else` | Definite reference the reader must guess, and it is falsified two lines later (§13 #6). |
| 291 | `the exploitable property` | Never named. It refers back to `a single fixed target identical across every trace`. |
| 303 | `one replicate slot` | `slot` used before definition. |
| 321 | `A third model family` | Indefinite but unspecifiable; the reader can never learn which. |
| 546, 570 | `the sensitive instrument ...` → `the same pattern` | A pattern named nowhere, referred to twice. |
| 608 | `the headline statistic itself` | Which statistic? |
| 634–635 | `the confound this paper's control was built to catch` | Which confound — the severity confound of L438, or the geometry confound of L461? |
| 684 | `the reported distance` | First use of `distance` in the appendix, with a definite article presuming a definition the reader must fetch from the main text 450 lines earlier. |
| 746 | `the prior operator's cone` | `the prior operator` has not been named. |

## 12f. Quantities stated approximately in one place and exactly in another

| Quantity | Approximate form | Exact form | Fix |
|---|---|---|---|
| Null/real ratio, Experiment 1 | `by more than 2x` (40); `by roughly $2.4\times$` (469); `more than twice` (476–477) | 0.0220/0.0091 = 2.42 | Three approximations, no exact statement. And Experiment 2's ratio (0.02167/0.00723 = 3.0×) is never given at all (§13 #25). |
| Coherence headroom at 3B | `a scale with almost none` (94) | `mean baseline CCEI 0.99` (321) | State the number at L94. |
| Attenuated partial correlation | `a mean $r\approx0.37$` (490) | Every other correlation in the manuscript is exact (§13 #23) | Report 0.37 exactly, with its across-draw SD. |
| Minimum detectable CCEI effect | `minimum detectable $\approx0.11$` (350); `$\approx2.5\times$ the pilot's` (601–602) | — | An MDE is a computed quantity; the `$\approx$` hedges an exact calculation. And the two statements are of the same thing in different units, 250 lines apart. |
| Required sample size | `$N\approx111$--$161$` (602) | — | An approximation sign on a range. |
| Largest dose | `one far-larger-dose trace` (453) | `$L_1=111.64$` (520); `111.64` (693) | Give the number where the reader first meets the trace. |
| Wall-clock | `$\approx$2.1 hours` (325) | `under 5 seconds` per solve (326); `$\le8.1\times10^{-5}$` (226) | Three precision conventions in one section. *The wall-clock approximation is defensible.* |
| Attenuation target | `$\sim$60\% attenuation` (349) | `52\%` (357) | 1 s.f. approximate and 2 s.f. exact in the same subsection. |
| Discard rate | `the pilot's unretried 52\%` (552) | `52\% of sessions (13 of 25)` (357) | Consistent; noted for completeness. |
| $\gamma$ | `$10^{-4}\cdot\min_t I_t$` (729) | Under fixed income 100 this is exactly $10^{-2}$ | The formula hides a constant (§13 #22). |
| Cosine similarity range | `Similarities were low (0.16--0.31)` (696) | The range is given, so `low` is acceptable | *No change.* |

---

# 13. Numbers and internal consistency

Ordered by severity. Entries marked **OUT OF PROSE-FIX SCOPE** must be skipped in Phase 2: they require the author to check the underlying data, and papering over them with a wording change would hide a possible error.

## 13a. Contradictions and count errors

**1. L98–100 — the manuscript's worst factual self-contradiction. CONFIRMED against the full document.**
> `The reciprocal-price framing manipulation intended to induce coherence variation at 1.5B produced, in a pilot run, a large apparent effect that disappears once discard-selection is corrected with a capped retry protocol: the pilot's naive estimate and the corrected main-experiment estimate are both statistically indistinguishable from zero.`

If the pilot's naive estimate is indistinguishable from zero, there was no `large apparent effect` to disappear. The two clauses cannot both be true. **Full-document check:** the only pilot CCEI estimate the manuscript ever reports is `+0.0169 ($p=0.66$)` at L556; the only "large" pilot number is the 52% discard rate at L357, which is a discard rate, not a coherence effect. So either the sentence means the *discard rate* was large — in which case it is conflating two quantities without saying so — or `large apparent effect` is simply wrong. **This is a prose fix only if the author confirms which quantity is meant**; the likely intended sentence is: `The reciprocal-price framing manipulation was intended to induce coherence variation at 1.5B. In the pilot it produced a 52\% discard rate but no detectable CCEI shift; the pilot's uncorrected estimate ($+0.0169$, $p=0.66$) and the retry-corrected estimate ($-0.0109$, $p=0.73$) are both indistinguishable from zero.` A reviewer who notices the contradiction will distrust the whole framing paragraph.

**2. L194 vs. L128 and the table — a count error in the sentence that scores the nearest competitor. CROSS-SECTION FLAG, CONFIRMED.**
> L194: `occupying two of our three legs without Afriat machinery`

L128 defines **four** criteria; the table has **four** columns (L140–141: Own choices, Exogenous payoff, Graded dose, Min.-distance projection); L130 says `None occupies all four`; the Control-vectors row at L151 reads `yes / no / yes / no` — two of **four**. `three legs` is wrong on both the count and the noun, and `legs` appears nowhere else in the manuscript. **Straightforward, high-confidence prose fix, no science or number change:** `they meet two of the four criteria and use no Afriat machinery`. A reviewer who checks the table against this sentence finds the paper miscounting its own defining criteria, and will then re-check everything else in the section. **Fixable in Phase 2.**

**3. L186, `(worse in 14 of 16 cells)` — CROSS-SECTION FLAG, PARTIALLY OVERTURNED.**
Full-document search: the string `14 of 16` appears **only at L186**; `14/16` appears nowhere. The Related Work agent read this as one of *the paper's own* comparative results, orphaned in a parenthetical. **That framing is overturned.** In context — `the same distinction that disposes of \citet{yamin2026elicited}'s isotonic repair (worse in 14 of 16 cells)` — the number is attributed to a cited third party, exactly parallel to `on GPM's own length-controlled metric that arm \emph{loses} in 18 of 24 cells` at L174 (which likewise appears only once, and which the same agent allowed as legitimate).

**What survives, and it is a real defect:** L174 says `GPM's **own** ... metric`, making the attribution explicit; **L186 says nothing of the kind**, so a reader cannot tell whether `14 of 16` is Yamin et al.'s reported result or this paper's own re-analysis of their data. Compounding it, the comparison target is never stated — worse than *what*, on *what measure*, in cells of *what*? **Fix (prose only):** `the same distinction separates ours from \citet{yamin2026elicited}'s isotonic repair, which their own evaluation reports as worse on [measure] in 14 of 16 cells.` If it is in fact this paper's computation, it needs a home in Results with its construction stated.

**4. L363–364 vs. Table 2 (L394, L398) — the method contradicts its own table.**
> L363–364: `a slot still failing after three attempts is a residual discard, **excluded from CCEI/GARP** but retained for audit.`
> L394: `llama3.2:3b  & residual discard      & 2  & 1.0000 & 1.0000 & 0.000`
> L398: `qwen2.5:1.5b & residual discard      & 6  & 0.8821$^*$ & 0.6667$^*$ & 24.196$^*$`

The Method states residual discards are excluded from CCEI and GARP; the table thirty lines later reports CCEI and GARP pass rates for them, and the prose at L369–370 draws a conclusion from those numbers. A reviewer will read this as either a protocol violation or a broken sentence. **Prose fix:** `a slot still failing after three attempts is a residual discard, excluded from the main CCEI/GARP analysis but scored separately for the audit in Table~\ref{tab:discardbreakdown}.`

**5. L370 vs. Table 2 (L396–398) — a claim contradicted by the table it describes.**
> `the residual-discard group scores lowest on the handful that can be measured`

True for CCEI (0.8821 < 0.9315 < 0.9651). **False for GARP pass rate:** the qwen residual-discard group's 0.6667 is the *highest* of the three qwen rows (0.4706, 0.1429, 0.6667). The unqualified `scores lowest` is wrong. **Prose fix:** `the residual-discard group has the lowest mean CCEI of the three (0.8821), though its GARP pass rate is measured on only 3 slots.`

**6. L289 vs. L291–293 — a claim falsified two lines later.**
> `it is scored by the same payoff function **used everywhere else**` — followed two lines later by `we build a **second**, independently designed payoff`.

The section defines two payoffs; the `everywhere else` claim is false the moment the second exists. **Prose fix:** `it is scored by the payoff of \S\ref{sec:method-payoff}`.

**7. L336 vs. L328 — an appositive that is false as attached.**
> `Our arm tests the opposite direction (single-turn split into multi-turn), the direction our own baseline already uses.`

The baseline (L328) is `single turn, all 25 rounds in one prompt and response`. The arm tests multi-turn. The appositive says the tested direction is the one the baseline already uses, which is false. **Prose fix:** `\citet{wang2025tactics} collapse multi-turn to single-turn; because our baseline is already single-turn, this arm tests the reverse.`

**8. L233–234 vs. L254–256 vs. L727 — fixed income written with a time subscript.**
> L233–234: `comparable across sessions without further normalization because **income is fixed throughout**`
> L254: `At budget line $(p_t, I_t)$`; L255–256: `$x^*_{t,A}=0.5 I_t/p_{t,A}$`; L727: `(income fixed at 100 throughout)`; L728–729: `$\alpha > \max_t I_t$`, `$10^{-4}\cdot\min_t I_t$`

If income is fixed, it is $I$, not $I_t$, and both extremal expressions are vacuous ($\max_t I_t = \min_t I_t = 100$), which also means $\gamma = 10^{-2}$ exactly. Either the subscript is wrong, or the dose-comparability argument at L233–234 is. **Prose fix, if income is genuinely constant:** write $I$ throughout, say so once, and replace the extrema with the constants — `$\alpha > 100$` and `$\gamma = 10^{-2}$`.

**9. L236–238 vs. L239 — a feasibility incumbent that never reaches the solver.**
> `A Cobb--Douglas demand share-fitted to each trace's own observed data is computed as a **feasibility incumbent** and sanity ceiling ... Appendix~\ref{app:payoff-audit}(1) confirms it **never reaches the solver**.`

A feasibility incumbent is by definition a starting solution supplied *to* the solver. The sentence contradicts itself in 25 words. **Prose fix:** drop `feasibility incumbent` — `We compute a share-fitted Cobb--Douglas demand as a sanity ceiling on the reported distance; it is not supplied to the solver.` L250 and L681/L683 then need the same term change (§12a #18).

**10. L408 and L434 vs. Table 3 — CROSS-SECTION FLAG, BOTH HALVES RESOLVED, BOTH FIXABLE IN PHASE 2.**

*Half one — `Every cell reached its full 30 replicates` (L408) vs. `$n$ kept` of 28 and 24.* **NOT a contradiction.** L406–407 establishes 150 slots and 8 residual discards; the table's kept counts are 30, 28, 30, 30, 24 = 142, and 142 + 8 = 150. The two cells short of 30 are exactly the two with residual discards (llama reciprocal 2, qwen reciprocal 6): 28 + 2 = 30 and 24 + 6 = 30. Every cell *was* run to 30 slots; `n kept` is the post-discard subset. Both statements are true. **What is wrong is the word `replicates`**, which §12a #5 shows is used for both slots and kept traces. **Prose fix:** `Every cell was run to its full 30 slots; 142 of 150 yielded a usable trace.`

*Half two — the per-cell `mean $\Delta$payoff` column against the three overall means.* **NOT a numeric inconsistency; the caption is wrong.** Derivation: the table's GARP pass rates imply violator counts of 8, 17, 18, 27, 15, summing to 85 and splitting 60/25 between 1.5B and 3B exactly as L432 states. Weighting the per-cell $\Delta$payoff means (0.0018, 0.0016, 0.0090, 0.0083, 0.0065) by *those violator counts* gives **0.00618**, which matches nothing. Weighting them by **`$n$ kept`** (30, 28, 30, 30, 24) gives $30(0.0018) + 28(0.0016) + 30(0.0090) + 30(0.0083) + 24(0.0065) = 0.7738$, and $0.7738 / 85 = \mathbf{0.00910}$ — matching L434's `$+0.0091$` and L471's `0.0091` exactly.

The column is therefore averaged over **all kept traces with $0$ imputed for GARP-consistent ones** — precisely the convention Table 2's caption states for its own dose column at L384–385 — and then the overall figure is a total spread over the 85 violators. The dose column behaves identically. **The caption at L412 (`dose and $\Delta$payoff are computed on the subset of kept traces that violate GARP`) misdescribes what the column contains.** **Prose fix, no numbers touched:** see §8d. Note that L484's `0.00723` for the corrected payoff is a different quantity (Experiment 2) and is not comparable to this column, which is a further reason the caption must name its payoff.

**11. L432 — a restrictive clause that excludes nothing.**
> `Across all 85 GARP-violating traces with a computed, independently-verified projection (60 at 1.5B, 25 at 3B)`

8 + 17 + 18 + 27 + 15 = 85 is *every* violating trace, so `with a computed, independently-verified projection` removed nothing. Either drop the restrictive clause or state that it excluded zero traces.

**12. L566–568 vs. L554–555 — an unsound comparative.**
> `a larger drop than reciprocal framing produced at 1.5B`

At 1.5B, reciprocal framing produced `0.40 vs.\ 0.38, $p=0.85$`, which L554–555 explicitly calls indistinguishable. The comparative measures the multiturn drop against a null effect, which flatters it without saying so. **Prose fix:** `Reciprocal framing produced no detectable drop at 1.5B; the multiturn format drops the pass rate by 30 points.`

**13. L198 vs. L334 — the same cited number with opposite signs.**
> L198: `drops CCEI by up to $0.241$`
> L334: `moves CCEI by up to $-0.241$`

Same source (\citet{wang2025tactics}), same effect, opposite sign, 136 lines apart. Both phrasings are individually defensible; they must not co-exist. **Prose fix:** pick one — `drops CCEI by $0.241$` at both sites.

**14. L188–190 — `three` becomes `neither` mid-sentence.**
> `three independently published axiom-enforcement results (adding \citet{zhu2025axiomatic}'s) all point the same adverse way, which is why we carry a null-operator control neither published negative had.`

`neither` takes two; the antecedent is three. `three ... results` also shifts to `published negative[s]`, a third name for the same set within one sentence. **Prose fix:** `... which is why we carry a null-operator control that none of the three had.`

**15. L46–47 vs. L108–122 — the abstract and the Introduction enumerate different contributions.**
The abstract states the paper's contributions are two: `a capacity-deconfounded identification strategy for the coherence--competence question` and `a discard-selection instrument-validity finding`. The Contributions list enumerates five, including the null-operator control (3) and the elicitation-format result (5), neither of which appears in the abstract's list. **Prose fix:** either enumerate the same set, or make explicit that the abstract lists only the surviving positive contributions — `standing` does not communicate that (§11 #3).

**16. L620–624 — a count built on a member it disqualifies in the same clause.**
> `Three independently published repair attempts moved the wrong way ... our reciprocal-framing manipulation ... is a fourth, **in the narrower sense that it failed to induce the coherence variation it was designed to**. The null-operator result ... is a fifth.`

The fourth member is admitted into the count and disqualified from it in the same clause: a manipulation that failed to induce variation is not a repair attempt that moved the wrong way. A skeptical reviewer will read this as inflating a prior. **Prose fix:** `Three independently published repair attempts moved the wrong way (\S\ref{sec:related}). Our null-operator result (\S\ref{sec:results-c1}) is a fourth: under two payoffs, restoring GARP-consistency does not outperform a matched GARP-blind operator.` Move the framing manipulation to its own sentence, outside the count.

**17. L659–664 — the Conclusion's final sentence. CROSS-SECTION FLAG, HONEST READING: NOT A STRICT CONTRADICTION, BUT GENUINELY MISPARSED ON FIRST READ.**
> `Two further, unpredicted findings --- a framing manipulation's apparent effect was a discard-selection artifact rather than a real coherence shift (C3), and an elicitation-format manipulation collapsed GARP pass rate in the opposite direction from a published finding in the same domain and model family at a larger scale --- are reported in their own right: a well-controlled negative, an open identification question, and an instrument-validity finding are exactly what this literature should surface by default rather than paper over.`

Read carefully, the sentence is structured as `[two new findings, A and B] are reported in their own right: [a three-item summary of everything the paper offers]`. Mapping the three items: `a well-controlled negative` = the C1 null-operator result (from earlier in the same paragraph, L651–654); `an open identification question` = C2 (L656–659); `an instrument-validity finding` = C3, which *is* one of the two. So **the list is a whole-paper summary, not an enumeration of the two, and there is no strict internal count contradiction.**

**But the sentence does not read that way, and the reason is structural, not arithmetic.** The colon after `are reported in their own right` conventionally introduces an expansion of the clause it follows, and the clause it follows is `Two further, unpredicted findings`. The reader is therefore primed to count three items against an announced two. The mis-parse is aggravated by the list's own composition: exactly one of the three items (`an instrument-validity finding`) is drawn from the announced pair, and the other two are drawn from elsewhere in the paragraph — so the reader who tries to check the mapping finds a partial match, which is worse than none. Add the 53-word parenthetical separating subject from verb (§9a #2) and this is a sentence a reviewer will have to read twice, at the exact point where the paper is asking to be believed.

**Do not frame this as an error in Phase 2.** Frame it as what it is: a colon doing the wrong job on the paper's last sentence. **Prose fix:** break the sentence (§9a #2) so the two findings each get a sentence, and either delete the three-item clause (recommended, §10 #34) or give it its own sentence with an explicit whole-paper scope: `Across the paper, a negative result with a matched null control, an open identification question, and an instrument-validity finding are all worth reporting.`

**18. L634 — a subject/verb mismatch in the paper's only policy claim.**
> `would be adopting exactly the confound this paper's control was built to catch`

A practitioner does not adopt a confound; they act on a confounded estimate. **Prose fix:** `would be acting on exactly the confounded estimate this paper's control was built to separate.` (`catch` is also a trap metaphor the paper's measurement vocabulary does not support — §16.)

**19. L610 vs. L634 and L651 — a within-scale/across-scale distinction never made explicit.**
Limitations says the design `does not trace a dose--response relationship \emph{across} scale`; Broader impacts (L634) and the Conclusion (L651) both invoke a `dose--response` relationship as a found thing. The distinction is real but unstated at either site. **Prose fix:** at L651 write `a monotone raw within-scale dose--response relationship`; at L634 write `on the strength of a raw within-scale dose--response correlation alone`.

**20. L385–386 vs. the `$n$` column at L398 — a table row weighted wrongly by construction.**
The qwen residual-discard row reports `$n$ = 6` while, per its own footnote, every statistic in it is computed over 3. A reader scanning the table without the footnote will weight the row by 6. **Prose fix:** print `6 (3)` or `3 of 6` in the `$n$` column.

**21. L690–691 — a null result stated as a positive exclusion.**
> `GARP-consistency status alone does not predict payoff, ruling out a population-level mechanical link`

$p=0.94$ with $n=142$ fails to *detect* a link; it does not rule one out — and the paper's own first limitation is about being underpowered. **Prose fix:** `No population-level link between GARP-consistency and payoff is detectable ($t=-0.07$, $p=0.94$).`

**22. L727 vs. L728–729 vs. L731–732 — the $\gamma$ constants.**
`income fixed at 100 throughout` makes `$\max_t I_t$` and `$\min_t I_t$` vacuous and pins `$\gamma = 10^{-4}\cdot\min_t I_t$` at exactly $10^{-2}$ — which is also the top of the stability sweep `$\gamma \in \{10^{-2},\ldots,10^{-6}\}$`. So the sweep only descends from the operating point and never tests a larger margin. That may be intentional, but it is not stated. Separately, `$\{10^{-2},\ldots,10^{-6}\}$` uses set-with-ellipsis notation for a descending sequence, which is ambiguous about whether all five decades were run. **Prose fix:** `$\gamma \in \{10^{-2}, 10^{-3}, 10^{-4}, 10^{-5}, 10^{-6}\}$`, and say that the sweep runs downward from the operating point.

**23. L702–703 — `$r=-0.41$` printed for two different correlations. CROSS-SECTION FLAG: OUT OF PROSE-FIX SCOPE — NEEDS AUTHOR VERIFICATION OF THE UNDERLYING NUMBERS.**
> `Larger-dose traces do start from worse raw payoff (Pearson $r=-0.41$, $p<0.0001$), and worse-starting traces do have more room to improve ($r=-0.41$ between raw payoff and $\Delta$payoff)`

These are two genuinely different correlations — corr(dose, raw payoff) and corr(raw payoff, $\Delta$payoff) — printed at identical two-decimal values, with a $p$-value supplied for the first and withheld for the second. **Full-document check:** the first value is corroborated at L440 (`dose vs.\ raw payoff, Pearson $r=-0.41$, $p<0.0001$`); the second appears **only at L703** and is corroborated nowhere. They may genuinely coincide to two decimals, or the second may be a copy-paste of the first.

**I cannot resolve this without the underlying data, and either resolution changes a reported number.** Do **not** apply a wording fix in Phase 2. Flag it to the author with two questions: (i) are the two correlations in fact equal to two decimals? (ii) if so, report both to three decimals so they visibly differ or visibly agree, and give the second one its $p$-value.

**24. L544–545 — "borderline significance."**
> `reaching only borderline significance (0.9900 vs.\ 0.9713, $t$-test $p=0.0508$)`

At a stated $\alpha$ this is a contradiction in terms, and it is the single most reviewer-visible hedge in the Results. **Prose fix:** `does not reach significance ($p=0.0508$)`.

**25. L484 vs. L469 — an unstated ratio.**
Experiment 1's ratio is stated (`roughly $2.4\times$`, L469). Experiment 2's — 0.02167/0.00723 = 3.0× — is never given, though it is the *larger* of the two. Stating only the smaller one is an asymmetry a reviewer will notice. Report both or neither.

## 13b. Precision and significant figures

| # | Issue | Instances | Fix |
|---|---|---|---|
| 26 | **$p$-value formats — five conventions across the manuscript** | Decimal: `$p=0.94$` (690), `$p=0.18$` (444, 708), `$p=0.85$` (554), `$p=0.73$` (555), `$p=0.66$` (556), `$p=0.91$` (566, 583), `$p=0.0011$` (438), `$p=0.0073$` (199, 566, 582), `$p=0.0089$` (543), `$p=0.0508$` (544). Bounded at two different cutoffs: `$p<0.0001$` (433, 434, 437, 440, 702) and `$p<0.00001$` (434). Bounded in scientific notation: `$p<10^{-16}$` (443, 707). Exact scientific at 1 s.f.: `$p=7\times10^{-19}$` (442, 705). Exact scientific at 3 s.f.: `$p=3.98\times10^{-10}$` (41, 471), `$p=1.13\times10^{-8}$` (474), `$p=1.24\times10^{-5}$` (43, 485), `$p=1.35\times10^{-9}$` (487) | **Adopt one rule:** exact to 3 s.f. above $10^{-4}$; `$p<10^{-4}$` below. Note that `$p<0.0001$` and `$p<0.00001$` appear in the *same sentence* at L433–434, and `$p=7\times10^{-19}$` (exact) sits three lines from `$p<10^{-16}$` (bounded) at L442–443 — a reader will ask why the smaller exponent is the bounded one. |
| 27 | **Three-significant-figure $p$-values at $10^{-10}$** | 41, 471, 474, 485, 487 | Three significant figures on a rank-test $p$-value at this magnitude claims resolution no finite-sample test supports. Report as `$p<10^{-4}$`. |
| 28 | **Four-significant-figure proportions from denominators of 2 to 7** | Table 2: `0.4286` ($n=21$), `0.2857` ($n=7$), `1.0000` ($n=2$), `0.4706` ($n=17$), `0.1429` ($n=7$), `0.6667` (effective $n=3$) | Four s.f. on a proportion with 7 observations claims a precision of 0.0001 where the resolution is 0.143. Report as fractions: `9/21`, `2/7`, `2/2`, `8/17`, `1/7`, `2/3` — self-documenting about sample size, which is the whole point of that table. |
| 29 | **CCEI at three different precisions** | 2 dp `0.99` (321); 3 dp none; 4 dp throughout Tables 2 and 3 and the Results prose | Pick 3 dp for CCEI throughout: `0.990`, `0.974`, `0.962`, `1.000`, `0.932`, `0.965`, `0.882`. |
| 30 | **Dose at 3 dp from $n=2$** | `5.086`, `9.839`, `0.000`, `13.847`, `7.600`, `24.196` (Table 2); `5.01`, `6.27`, `16.68`, `14.54`, `12.02` (Table 3) | **Two precisions for the same quantity in two tables.** Pick 2 dp or 3 s.f. and apply to both. |
| 31 | **$\Delta$payoff at two precisions** | 4 dp `0.0220`, `0.0091` (470–471), and the Table 3 column; 5 dp `0.02167`, `0.00723`, `0.02224` (484, 487) | One convention. 4 dp throughout. |
| 32 | **Correlations mixed exact and approximate** | `$r=0.574$`, `$r=0.784$`, `$r=0.679$`, `$r=0.631$`, `$r=0.624$`, `$r=0.821$` vs. `$r\approx0.37$` (490); and 2 dp `$r=-0.41$` (440, 702, 703) against 3 dp elsewhere | Report 0.37 exactly with its SD; pick one decimal count. Note that 3 dp on a correlation from 85 traces already overstates the resolution. |
| 33 | **Payoff means at 4 s.f. on an undetectable difference** | `mean 0.7872 vs.\ 0.7899` (689), difference 0.0027, $t=-0.07$ | Four s.f. suggest a precision the test explicitly says is unresolvable. `0.787 vs.\ 0.790`. |
| 34 | **Percentage precision — zero, one, and one-forced decimal** | `82\%` (434), `18\%` (435), `81\%` (41, 472), `70.8\%` (43, 485), `80.4\%` (487), `43.3\%` (550), `20.0\%` (551), `52\%` (357, 552), `40\%`/`10\%` (565), `42\%` (526), `40.0\%`/`10.0\%` (589–590), `52\%` (357) | Pick one. Note `a residual 20.0\% (6/30)` (551) is exactly 20% — false precision on an exact fraction. |
| 35 | **Power figures at three precisions in five lines** | `$\ge0.999$` (348), `$\ge0.80$` (349), `$\ge0.998$` (352) | Use 3 dp uniformly. (And two of the three mean different things — §12a #13.) |
| 36 | **Significance-count formats** | `significant in 20 of 20 draws` (485) vs. `significant in 20/20 draws` (487–488) | One form, three lines apart. |
| 37 | **A count reported as a range** | `significant in 14--15 of 20` (490–491) | A count of significant draws is an integer. If two tests give 14 and 15, say which gives which; if it varies by threshold, name the threshold. |
| 38 | **`by more than 2x` written with a literal `x`** | L40 | The abstract uses `$\times$` in `$3.98\times10^{-10}$` one line later. Two multiplication conventions three lines apart. Use `$2.4\times$`. |
| 39 | **Sentence-initial numeral** | `187 attempt-records were collected` (406) — the Results section's first word | Recast: `We collected 187 attempt-records across 150 replicate slots`. |
| 40 | **Numerals vs. words for small numbers** | Words: `three attempts` (407), `Two ... payoffs` (495), `a third time` (498), `nine` (127), `Three` (163), `Two` (167), `eight` (182), `three` (188), `two` (194). Numerals: `8 were residual discards` (407), `15 (18\%)` (435), `5 of 21 rounds` (526), `the other 16` (527), `3 of the 6 slots` (385) | Related Work is internally consistent (words below ten, numerals at ten and above); Results is not. At minimum recast `8 were residual discards` (407), which also puts a bare numeral immediately after a semicolon. |
| 41 | **`MIP gap $\le 8.1\times10^{-5}$` — a bound whose status is unstated** | 226, 735 | If this is the maximum observed gap, say `the largest MIP gap over the 85 solves was $8.1\times10^{-5}$`. If it is at or near the solver's configured `MIPGap` tolerance, it is a clipped bound reported as an achieved property — say `every solve terminated within the configured gap tolerance of ...`. As written the reader cannot tell which. **This one touches the underlying run configuration; if the author cannot confirm which it is, leave it and flag it — OUT OF PROSE-FIX SCOPE.** |
| 42 | **A degenerate table row presented as three measurements** | L394: `llama3.2:3b & residual discard & 2 & 1.0000 & 1.0000 & 0.000` | All three statistics are at trivial values *because* both traces were GARP-consistent: CCEI at its ceiling, pass rate 2/2, dose exactly 0 by the caption's own zero-imputation rule. These are not three independent measurements but one fact reported three times — and CCEI 1.0000 here is exactly the `CCEI can read exactly 1.0 on GARP-violating data` pathology the paper warns about at L345–346. As printed, a reader can read this row as evidence that discarded sessions are *better* behaved. **Prose fix:** a footnote — `$^\dagger$Both llama residual-discard traces were GARP-consistent, so CCEI, pass rate and dose are at their trivial values.` |
| 43 | **`up to` with a negative number** | `moves CCEI by up to $-0.241$` (334) | Ambiguous between "up to in magnitude" and "up to in value". `moves CCEI by as much as $0.241$ downward`. |

## 13c. Comparatives with no second term

| Line | Text | Missing |
|---|---|---|
| 40 | `outperforms the real repair by more than 2x` | On which quantity — the mean gain, the win rate, or the effect size? |
| 64 | `the repaired outputs are downstream-better than the raw ones` | `downstream-better` is a coined comparative with no stated metric. |
| 65 | `how much better, as a function of how much repair was needed` | Better at what? The sentence borrows the missing dimension from `downstream-better`. |
| 101–102 | `the more reliable signal` | More reliable by what reliability quantity? None is given. |
| 158, 180 | `the sharpest vocabulary collision`, `The sharpest objection` | Sharpest of what set, on what axis? No comparison class is named. |
| 176, 192 | `Our closest theoretical neighbour`, `The closest neighbour on the economics side` | Closest by what metric? |
| 186 | `worse in 14 of 16 cells` | Worse than what, on what measure? See #3. |
| 197 | `at a larger scale` | Larger than what? Ours is never sized in that section. |
| 335 | `at a larger scale` | The cited model's size is never given at that site. |
| 368 | `not a close stand-in for` | `close` has no metric. |
| 370 | `scores lowest on the handful that can be measured` | Lowest of what set — three groups in one model, or across both? Across both it is not lowest on GARP pass (#5). |
| 372 | `sit much closer together` | Closer than what? The comparison target is implied across a sentence boundary. |
| 505–506 | `more strongly than it predicts the real repair's own gain in either` | More strongly than *what values*? Two correlations are missing. |
| 544 | `CCEI moves much less` | Less than what, quantified? |
| 552 | `far more discards than any other condition` | The other conditions' rates are not given here. |
| 566–568 | `a larger drop than reciprocal framing produced at 1.5B` | See #12 — the comparison is against a null. |
| 601–602 | `minimum detectable effect $\approx2.5\times$ the pilot's` | 2.5× the pilot's *what*? The referent is nine words earlier and the possessive strands it. |
| 745 | `has no analogue here` | No analogue to *what property*, in what respect? The sentence has already named `non-expansiveness` — make it explicit. |

## 13d. Subjects that do not match their verbs semantically

| Line | Text | Fix |
|---|---|---|
| 79 | `That relationship turns out not to isolate what it was built to isolate.` | A relationship does not isolate; a design does. |
| 98–99 | `a large apparent effect that disappears once discard-selection is corrected` | An effect does not disappear; an estimate shrinks. |
| 104 | `splitting single-turn elicitation into separate sequential calls ... produces a large GARP-pass-rate collapse` | You do not split single-turn elicitation into sequential calls — you replace single-turn with multi-turn. |
| 130 | `None occupies all four.` | Systems do not *occupy* criteria. `No system satisfies all four.` (This is the section's thesis sentence — worth getting the verb right.) |
| 183 | `participants given the chance to revise their own choices saw mean CCEI \emph{fall}` | Participants do not "see" a group mean. `mean CCEI \emph{fell} among participants given a chance to revise their choices`. |
| 189 | `three ... results ... all point the same adverse way` | Results do not point; they report. |
| 192 | `The closest neighbour ... is invisible to any arXiv sweep` | A paper is not invisible; a search failed to return it. |
| 194 | `occupying two of our three legs` | Same verb, same problem as L130. |
| 198 | `Our opposite manipulation finds the opposite direction` | A manipulation does not find. |
| 271 | `a projection direction secretly aimed at the payoff optimum` | `secretly` implies intent by the algorithm. `a projection direction correlated with the payoff optimum`. |
| 272–273 | `None survived the audit` | Failure modes do not survive; hypotheses are ruled out. |
| 284 | `Any operator that moves a bundle toward that fixed point raises its payoff` | `its` is ambiguous between the operator's and the bundle's payoff. Also **the universal claim is not quite true**: a bundle already at $s=0.5$ cannot be moved toward it, and moving *past* the optimum lowers payoff. |
| 366 | `Table~\ref{tab:discardbreakdown} breaks every reciprocal-framing session down` | Split particle across a 20-word object. (Sentence deleted anyway — §3 #13.) |
| 371–372 | `some of the same selection concern ... persisting at a smaller scale` | A *concern* is raised, not persisted; the *selection effect* persists. |
| 373 | `the selection concern shows up more sharply` | A concern does not show up; a difference does. |
| 461–462 | `is a confound on the \emph{severity}` | A confound is not "on" a property. `bears on`. |
| 549 | `the manipulation this study was designed around does \emph{not} survive proper correction` | A manipulation does not survive; a *finding* does. |
| 634 | `would be adopting exactly the confound` | See #18. |
| 663–664 | `a well-controlled negative ... are exactly what this literature should surface` | Findings are surfaced; they are not "what a literature should surface". |
| 698 | `the sign of the outcome tracks a geometric quantity` | On five traces, `tracks` is a generalization the sample cannot carry. `On these five traces the sign of the cosine similarity matched the sign of the payoff change.` |
| 703–704 | `It does not explain the dose--response relationship away` | A confound does not explain a relationship away; it *would account for* the relationship. |
| 728 | `computable a priori as $\alpha > \max_t I_t$` | A constant is not computable *as* an inequality. `so any $\alpha > \max_t I_t$ is valid, and the big-$M$ constant needs no tuning.` |

## 13e. Verified as arithmetically correct

Checked and found sound, so Phase 2 should not disturb them: 142 + 8 = 150; 8 + 17 + 18 + 27 + 15 = 85; 60 + 25 = 85; 57 + 85 = 142; 21 − 5 = 16; 22/30 = 0.73; 11/28 = 0.39; 12/30 = 0.40; 3/30 = 0.10; 13/30 = 43.3%; 6/30 = 20.0%; 13/25 = 52%; 30 − 2 = 28; 30 − 6 = 24; $T(T-1) = 600$ binaries at $T=25$; 0.0220/0.0091 = 2.42; and the Table 3 → L434 reconciliation derived in #10.

---

# 14. Structural and framing problems

Re-derived from the whole manuscript. Three of the six section agents each saw a fragment of finding #1 from their own vantage; it is reconciled here into one entry with all of its locations.

## 14a. Redundancy across sections

**1. The paper's three headline findings are each stated three or four times, in the same order, in near-identical words — and one clause is duplicated verbatim.**

| Finding | Abstract | Introduction body | Contributions list | Results | Conclusion |
|---|---|---|---|---|---|
| Null operator beats real repair | L36–44 | L79–87 | L113–117 (contribution 3) | L469–477, L533–536 | L651–654 |
| Framing effect was a discard artifact | L46–47 | L97–103 | L117–119 (contribution 4) | L549–560 | L659–660 |
| Elicitation-format reversal | — | L103–106 | L119–122 (contribution 5) | L565–574 | L660–663 |
| The identification claim (C2) | L45–47 | L89–95 | — | — | L656–659 |

**The verbatim duplicate:** `absent from every published axiom-enforcement result we are aware of` appears **word for word at L79–80 and again at L113–114**, 34 lines apart. `in the \emph{opposite} direction from an independently published ... finding` appears at L105–106 and L120–122 with `\emph{opposite}` italicized in both.

**Fix, stated as three separate edits:**
- *Abstract → Introduction:* the abstract's own summary (L36–47) and the Introduction's paragraphs 3–5 (L79–106) may legitimately overlap; abstracts repeat. Leave.
- *Introduction body → Contributions list (L108–122):* this is the expensive duplication, because both are on the same page. Cut the Contributions list to only the items **not** stated in the running text above it — the verification procedure (L110), the pre-specification and leakage/mechanical-confound checks (L111–112), the per-cell reporting (L119), and the Qwen2.5 identification (L122) — reducing the rest to one clause each plus a section pointer. This buys back roughly ten lines of page budget.
- *Conclusion (L648–664):* delete the retrospective opener (L648–649, §3 #23) and open on the verdict. The three sentences unique to the Conclusion and worth protecting are L654–655 (the trace-extremity mechanism, hedged as partial), L656–659 (the C2 identification claim with its three named confounds), and L661–662 (the elicitation-format reversal). Those should survive whatever de-duplication is applied.

**2. `a large GARP-pass-rate collapse` appears twice in sixteen lines, both times undefined** (L104, L120) — the same finding, in the Introduction body and again in contribution (5), with the second adding only the model family. Merge.

**3. The exogenous payoff's independence from agent choices is asserted five times in 25 lines of Method** (L235–236, L236–239, L249–252, L252–253, L256–257), then a sixth time as failure mode one of the audit (L270) — and it has already been asserted twice in the Introduction (L75, L76) and once in the abstract's framing. **Nine assertions of one property.** State it once at L253 and let the audit at L270 be the only other mention.

**4. `We concede` / `is not new` — the same concession is made three times.** L89 (`We do not claim any of the individual pieces are new`), L127 (`Repairing an AI system's incoherent preferences is not new`), L160 (`We concede the minimum-distance priority unqualified`), plus L209 and L212 in the Method (`applies, rather than proposes`; `nothing about the formulation itself is new`). **Five novelty disclaimers across four sections.** Keep one, in Related Work.

## 14b. Cross-scale claims that contradict each other

**5. The manuscript licenses and forbids the same cross-scale comparison, in three places.**

- **L83 (Introduction):** the null-operator finding holds `at both model scales`.
- **L94–95 (Introduction):** the 3B run is `an identification control on the method itself, **not as a second point on a shared dose curve across scale**`.
- **L436–437 (Results):** `\textbf{Both scales show a significant, positive relationship, and it is stronger at the headroom model}: $\rho=0.756$ ... at 1.5B versus $\rho=0.614$ ... at 3B.`
- **L610 (Limitations):** the design `does not trace a dose--response relationship \emph{across} scale`.
- **L653 (Conclusion):** `at both model scales`.

L436–437 **is** a cross-scale comparison of the dose–response relationship — it compares two $\rho$ values across scale and asserts which is stronger — which is exactly what L94–95 and L610 disclaim. The other three sites (L83, L653) are within-scale replications of a paired comparison and are fine. **This is the tension a reviewer will find first, because L436–437 is bolded.** Fix: state once, explicitly, which cross-scale claims are licensed — the null-operator comparison is replicated *within* each scale; the dose–response magnitude is *not* compared across scale — and then either unbold and requalify L436–437 (`the relationship holds at each scale separately; we do not compare its magnitude across scale`) or drop the disclaimers.

## 14c. Results outside the Results section, and results buried in captions

**6. An entire results subsection sits inside §Experimental design (L354–401).** `\subsection{The discard-selection problem, and its correction as a stated contribution}` contains a pilot **result** (L357–359: 52%, 13 of 25), the protocol (L361–364, the only part that belongs in a design section), a **results paragraph** drawing four comparative conclusions (L366–375), and **Table 2**, a results table with six rows of measured outcomes. A reviewer looking for the paper's findings looks in `\section{Results}`, which begins at L403. **Fix:** keep L354–364 in Experimental design, retitled; move L366–375 and Table 2 into Results as a subsection. This also converts the figure caption's forward reference at L305 into a backward one, which is strictly better.

**7. The paper's strongest instrument-validity number exists only in a table-caption footnote.** L385–386: `3 of the 6 slots returned zero valid rounds on every attempt (no $p$/$x$ data at all)`. Three of 30 qwen reciprocal slots (10%) produced no parseable output at all across three attempts. This is the best available evidence for the paper's own claim at L359–360, and it is where a skimming reviewer will not credit it. Move to the body of §sec:discard (§8c #3).

**8. Seven mechanistic measurements exist only in `fig:mechanism`'s caption** (L520–529), while the body sentence they support (L513–515) contains no number at all. Full list and fix in §8b.

**9. Three further measured outcomes are stranded outside Results:** `all 150 draws held power $\ge0.998$` (L351–352); `the full $N=30$ design completed in $\approx$2.1 hours wall-clock, every MILP projection solving in under 5 seconds` (L325–326); and — most costly — `every one of the 85 GARP-violating traces' projections was independently re-verified GARP-consistent ... (MIP gap $\le 8.1\times10^{-5}$ on every solve)` (L224–226), which is one of the paper's strongest verification results and is delivered as a subordinate clause after a semicolon, in a sentence whose main subject is an appendix pointer. **It deserves its own sentence at minimum.**

**10. One of the paper's own comparative claims is over-generalized in Results and never bounded.** L546–547: `a further case of GARP pass rate being the sensitive instrument for framing/format disruption while CCEI understates it` asserts a general property of two instruments on the evidence of two conditions in two models, and `understates it` in particular claims a direction of bias that was never tested. **This is the one genuine overreach inside Results.** Soften to what was measured: `in both conditions, GARP pass rate separated the arms and CCEI did not.`

**11. GPM is argued in prose at the level of a table row but is absent from the table.** `GPM \citep{zhang2025gpm}` (L172) gets a claim (`strict superset model class`), a critique (`confounding coherence with capacity`), and a number (`loses in 18 of 24 cells`) — and `zhang2025gpm` appears nowhere else in the manuscript. L127–128 says the table positions `nine published systems`; a reader who counts the systems actually discussed in Related Work counts more. **Fix:** add a GPM row, or say explicitly at L171 why the parallel line is out of scope for the four criteria (`A parallel line, outside the table because it varies the model rather than the choices, ...`). As written, the hand-picked nine make `None occupies all four` look chosen rather than found.

## 14d. The paper's ending, and the recommendation

**12. The paper's only actionable recommendation is buried inside §Limitations, and the Conclusion makes none.** L630–635 — `This paper's central result argues against imposing GARP-restoration on deployed AI economic agents as a default decision-quality intervention` and the practitioner warning that follows — is the paper's practical payload, and it sits in a `\paragraph{Broader impacts.}` at the tail of §Limitations, after four paragraphs of self-criticism, where a reviewer skimming for "so what should I do" will not look. **Fix:** promote to `\section{Broader Impacts}` between Limitations and Conclusion, and add one sentence of recommendation to the Conclusion after L654: `A practitioner evaluating coherence repair should include a distance-matched null operator before reading a dose--response correlation as evidence of benefit.` **This is the single most actionable sentence the paper could add and it is currently absent from every section** — the Introduction diagnoses that published axiom-enforcement results lack a displacement-matched control (L79–80) and never says what a reader should do about it; Related Work diagnoses the gap (`None occupies all four`) and never says what follows; Results establishes that C1 fails and never says what to do instead.

**13. The paper's last words are an instruction to the field, delivered inside its worst sentence.** L662–664: `a well-controlled negative, an open identification question, and an instrument-validity finding are exactly what this literature should surface by default rather than paper over.` It makes a claim about the field rather than about the work, it closes on a pun (§16), and it is the tail of an 86-word sentence (§9a #2). See §13 #17 for the two-versus-three reading. **The paper should end on its own finding.**

**14. Related Work's last words are a disclaimer.** L199–200: `--- not a replication, since which format is more degrading reverses between their 7B model and ours.` The final impression of the section that establishes the paper's position is a concession about a reversal it cannot explain. Reorder within the paragraph so the positive claim closes.

**15. The Conclusion is a single seventeen-line paragraph** (L645–664) containing five distinct moves: question, result, verdict, mechanism, side findings. Break after L654 (`...is not supported.`) and again after L659 (`...displacement magnitude.`), producing three paragraphs: result and verdict; mechanism and identification claim; side findings.

**16. Two unrelated limitations share one paragraph** under a lead about single runs (L606–612). The single-run limitation (L606–609) is about repetition; the headroom/scale limitation (L609–612) is about design coverage. Split into two bolded leads.

## 14e. Ordering that forces forward references and repair sentences

**17. The Introduction builds a design, believes it, then retracts it — and both the setup and the retraction exist only because of the ordering.** L68–77 presents the design as though it works (`We study this question in a setting where it can be answered cleanly`, `Tracing dose against $\Delta$payoff gives the relationship this paper reports`); L79 then retracts it (`That relationship turns out not to isolate what it was built to isolate`). **Reordering that deletes both sentences:** present the null-operator comparison as *part of the design* at the end of paragraph 2 — `We compare the repair against a GARP-blind operator matched on displacement budget` — so paragraph 3 reports the result directly and no retraction is needed. This also removes the implication that the authors built a design, believed it, and found out otherwise, which is §11 material.

**18. Related Work concedes and then immediately repairs the concession, with a forward pointer inside the concession sentence.** L160–162: `We concede the minimum-distance priority unqualified: projection onto a closed convex set is non-expansive in $L_2$; the GARP-consistent set is a union of polyhedra, hence not convex, so no analogue transfers (\S\ref{sec:method-guarantee}).` The reader processes concession → counter-argument → cross-reference in one breath. **Reorder:** state the non-convexity first, then the concession follows without needing repair. *(Note the cross-reference target is broken — §7 #12.)*

**19. Method L336 exists only to talk the reader back from the citation at L334–335.** `Our arm tests the opposite direction (single-turn split into multi-turn), the direction our own baseline already uses.` The cited finding points the other way, so a repair sentence is needed — and the repair sentence is itself false as attached (§13 #7). **Reorder to state our arm first, then the citation as context**, and the repair sentence disappears.

**20. Appendix B's Formulation paragraph is ordered rejected-then-adopted** (L715–723), forcing the reader to hold a formulation they will not use across two sentences of bilinearity argument before reaching the one they will. Reorder: adopted characterization first, then one sentence on why Afriat multipliers were not used. This also removes the negation cascade at §1g #11.

**21. Forward references that cross section boundaries and land far away.**

| Reference | Line | Target line | Distance | Fix |
|---|---|---|---|---|
| `\S\ref{sec:discard}` inside `fig:pipeline`'s caption | 305 | 355 | 50 lines forward | Move Figure 1 to the end of §Experimental design (after L375), where everything it references already exists. |
| `\S\ref{sec:results}` inside `fig:pipeline`'s caption | 309 | 403 | 94 lines forward | Delete the sentence (§8f #4). |
| `\S\ref{sec:method-nullop}` | 277 | 280 | 3 lines forward | Delete — the target is the next subsection. |
| `\S\ref{sec:method-guarantee}` | 162 | 741 | 579 lines forward, **and the label is mis-scoped** | Fix the label (§7 #12). |
| `Figure~\ref{fig:doseresponse}` cited at L435, two paragraphs before Results re-introduces the null operator at L465 | 435 | 465 | 30 lines forward | Move the citation into the Experiment 1 paragraph (§8a). |
| `\S\ref{sec:results-c1}` cited three times in twenty lines of Limitations | 618, 624, 633 | 430 | backward | Keep the reference at first use per paragraph and drop the repeats at 624 and 633; the paragraphs are close enough that the pointer is remembered. Same for `\S\ref{sec:results-framing}` at 622 and 637. |
| `$K=2$` used at 342 after `$K$ goods` at 214 and `$K=20$` at 293 | — | — | — | Fix the number of goods at L214 (`$K=2$ goods`), which also makes the $K$ collision at L293 visible immediately (§12b). |
| `CCEI` used at L101 and thereafter, expanded nowhere | 101 | — | — | Expand at first use (§12d). |

## 14f. Framing that advertises something unusual and then declines to explain it

**22. L241–244.** `\textbf{What can be guaranteed, and what cannot}` promises a guarantee analysis at the volume of a paragraph, then hands the reader an appendix pointer and a single because-clause. Either the guarantee discussion is important enough for a paragraph in the Method, or it is a one-sentence caveat that does not need a bold lead.

**23. L269–277.** The four-failure-mode audit is announced with the full weight of a paragraph and then entirely deferred: `None survived the audit (Appendix~\ref{app:payoff-audit} gives every check and number)`. A skeptical reviewer is told there are numbers and shown none. **Fix:** put the single most load-bearing number inline — the dose/baseline-payoff correlation for failure mode four — and defer the rest.

**24. L158.** `the sharpest vocabulary collision` advertises a collision of vocabularies and never says which words collide. If the point is that POISE uses "projection" and "minimum distance" for a different object, say that: `POISE uses the same vocabulary --- projection, minimum distance --- for a different object.` That is a genuinely useful sentence, currently compressed into an adjective.

**25. L192.** `invisible to any arXiv sweep` advertises that the authors found something others would miss, then explains nothing about why or how. Delete (§11 #14).

**26. L612.** `the multi-model-residency failure of \S\ref{sec:design}` names an unusual-sounding event and hands the explanation to a cross-reference — which, at L321–323, does not explain it either. Either explain it in half a clause or drop the name.

**27. L570–573 advertises the literature reversal twice and explains it zero times.** The subsection heading (L562–563) states it (`a large effect in the opposite direction from the literature`); the body states it (L572–573); and the next sentence declines to explain it (`We do not have an explanation for the reversal`). Either give the candidate explanations (scale? task? elicitation detail?) in one sentence, or drop the advertisement from the heading and report the disagreement plainly.

**28. L725 promises three risks and delivers one.** `\textbf{Three method commitments, each carrying an explicit risk.}` Only the $\gamma$ commitment (L728–732) states its risk (`can read a distance of exactly zero on genuinely violating data`). The budget-equality commitment (L725–728) states a *benefit* (a computable big-$M$) and no risk; the verification commitment (L732–735) states a procedure and no risk. Either supply the two missing risks or drop the framing.

**29. Appendix A has no verdict.** Four audit parts run L678–708 and the section ends on `($t=-1.36$, $p=0.18$)`. Nothing states what the four-part audit concluded. A reader who reads only the appendix does not get the answer to the question the section title poses. **This is the one place in the manuscript where content should be added, not cut:** `No part of the audit found a channel by which the projection could influence payoff other than through $(p_t, I_t)$.`

## 14g. Contribution and priority claims, verified against what the manuscript supports

**30. `The discard-selection finding generalizes further` (L640) — CROSS-SECTION FLAG: UNSUPPORTED AT THE STATED SCOPE.**
> `The discard-selection finding (\S\ref{sec:discard}) generalizes further: any consistency instrument that silently drops disruption-caused failures risks underestimating exactly the manipulations that matter most.`

Checked against §sec:discard (L354–375) and every other statement of the claim. The evidence base is **one instrument, one manipulation, two models, $n=6$ residual discards at 1.5B and $n=2$ at 3B**, and §sec:discard itself frames the claim narrowly (`This is a claim about instrument validity in its own right`, L359–360). Every other statement of it in the manuscript is narrower still: the abstract calls it `a discard-selection instrument-validity finding` (L46–47), and contribution (4) calls it `An instrument-validity finding (discard-selection bias under a disruptive manipulation)` (L117–118). **L640 is the only place in the manuscript that claims generality, and it is inside the section whose job is to bound the paper's claims.** The *mechanism* is plausible and worth stating; the quantifier `any` is not supported. **Prose fix:** `The discard-selection finding (\S\ref{sec:discard}) is not specific to our instrument: a consistency instrument that drops disruption-caused failures without recording them will underestimate the disrupting manipulation.`

**31. `the first attempt we know of` (L656–659) — CROSS-SECTION FLAG: SUPPORTED, BUT STATED AGAINST A DIFFERENT SET OF DIMENSIONS THAN RELATED WORK USES.**
> `this is the first attempt we know of to measure it without confounding coherence with capacity, a preference-judgment outcome, or mere displacement magnitude.`

Checked against Related Work. The claim **is** supported there, twice: `None occupies all four` (L130) over the nine-row table, and `absent from every published axiom-enforcement result we are aware of` (L79–80, L113–114). The capacity confound is argued explicitly at L171–174 (GPM and HRC/DSPPO `both make the cycle-tolerant arm a strict superset model class, confounding coherence with capacity by construction`). The hedge `we know of` matches Related Work's own `we are aware of`. **So the priority claim is not overreach.**

**What is wrong is the mapping.** The Conclusion names **three** confounds (capacity, preference-judgment outcome, displacement magnitude); Related Work's table has **four** criteria (own choices, exogenous payoff, graded dose, minimum-distance projection). Only one maps cleanly (`preference-judgment outcome` ≈ exogenous payoff). `Capacity` is not a table column at all — it is the L171–174 argument about a literature the table excludes. `Displacement magnitude` is not a table column either — it is the null-operator control, claimed at L113–114 and absent from the table. **A reviewer who tries to check L657 against the table cannot.** **Prose fix:** either state the three confounds in Related Work's own vocabulary, or add a sentence in Related Work naming the three confounds explicitly so the Conclusion has something to point at. Note this is the same three-versus-four mismatch that produces the count error at L194 (§13 #2).

**32. The uncited contradiction of a published finding (L661–663) — CROSS-SECTION FLAG: THE CLAIM IS SUPPORTED, BUT IT IS UNCITED AT THREE OF ITS SIX OCCURRENCE SITES.**
The finding contradicted is \citet{wang2025tactics}. Full-document check of every site where the paper claims to move opposite to it:

| Line | Site | Cited? |
|---|---|---|
| 105–106 | Introduction body | **No** |
| 120–122 | Contribution (5) | **No** |
| 196–200 | Related Work | **Yes** (`\citet{wang2025tactics}`, L196) |
| 334–335 | Method, Multiturn condition | **Yes** (`\citep{wang2025tactics}`, L335) |
| 570–573 | Results | **Yes** (`\citep{wang2025tactics}`, L571) |
| 661–663 | Conclusion | **No** |

So the claim is fully supported and cited three times — but at the three sites where a reader most likely encounters it first (the Introduction, twice) and last (the Conclusion), it is asserted with no citation at all. Claiming to contradict a published result without naming it will draw a reviewer objection immediately. **Prose fix, five minutes:** add `\citep{wang2025tactics}` at L106, L122 and L663. (And note the sign inconsistency between two of the cited sites — §13 #13.)

**33. Three further claims that exceed their evidence.**
- **L188–189:** `whose prescribed remedy --- a between-groups design --- is this paper's design` claims the paper implements the remedy prescribed by a *PNAS* critique, in one clause, with no pointer to where the design is described and no acknowledgment of the power gap at L602 (`A CCEI-power-matched design would need $N\approx111$--$161$`). Not formally contradictory — between-groups ≠ adequately powered — but a reviewer reading L188 will hold the paper to L602. Add the qualifier or the cross-reference.
- **L263:** `A genuinely exogenous, real-world payoff of this kind is rare in this literature` — a priority claim with no count and one citation. Quantify or soften.
- **L690–691 and L698:** `ruling out a population-level mechanical link` on $p=0.94$, and `the sign of the outcome tracks a geometric quantity` on $n=5$. A skeptical reviewer who checks parts (2) and (3) of the payoff audit against their own numbers will discount the whole four-part audit (§13 #21, §13d).

**34. L354 bills a contribution the section does not establish.** `its correction as a stated contribution` — the section shows that retry-rescued and first-attempt sessions differ, on $n=7$ per group, in one model, one condition, and honestly says the correction is incomplete (L370–372). That supports "the correction is incomplete"; it does not obviously support billing the correction as a contribution in a heading. Reconcile with contribution (4) at L117–119.

**35. The Method disclaims novelty and the Design section then claims a contribution.** L209 (`applies, rather than proposes`) and L212 (`nothing about the formulation itself is new`) against L354 (`its correction as a stated contribution`). The two framings need to agree on what is being claimed.

## 14h. Minor structural notes

**36. `\begin{ack}\end{ack}` is empty (L666–667).** Correct for an anonymized submission; flagged only so it is not shipped empty in a camera-ready.

**37. Float placement is inconsistent:** `[h]` at L132, L377, L576; `[t]` at L300, L410, L447, L517. Use `[t]` or `[tb]` throughout — `[h]` will produce different placement behaviour. *NeurIPS style prefers `[t]`.*

**38. Figure widths differ:** `0.76\linewidth` (L449) against `0.98\linewidth` (L302, L519). Layout, not prose. *Stylistic preference.*

---

# 15. Spelling and convention consistency

**Document-wide convention, established by grep across all 754 lines: American English with `-ize`.** Evidence: `behavior` (236), `color` (15), `characterization` (210, 220, 719), `generalizes` (640), `normalization` (233), `optimization` (244, 323, 699, 748), `analyzed` (230), `centering` (507, 511), `payoff-maximising` being the sole exception. Every British form in the manuscript falls inside Related Work.

| # | Line | Issue | Fix |
|---|---|---|---|
| 1 | 176 | `Our closest theoretical neighbour` | `neighbor` — or delete the phrase per §2 #8. `neighbour` occurs only at L176 and L192. |
| 2 | 192 | `The closest neighbour on the economics side` | Same — or delete the sentence per §11 #14. |
| 3 | 193 | `payoff-maximising behaviour` | `payoff-maximizing behavior`. `maximis` occurs only here; `behaviour` only here against `behavior` at L236. |
| 4 | 162, 242, 743, 745 | `analogue` | **Not an inconsistency** — `analogue` as a noun is standard in American mathematical usage and is used consistently four times. **No change.** But see §16 #6: three cognates appear in one 93-word sentence at L742–748. |
| 5 | 318, 345, 432, 474, 542, 615, 745 | **`-ly` adverb + participle hyphenated** — `locally-hosted` (318), `independently-drawn` (345, 542), `independently-verified` (432), `mechanically-predicted` (474), `globally-identical` (615), `weakly-closer` (745) | **Never hyphenate an `-ly` adverb.** All seven. The manuscript already gets this right elsewhere: `drawn independently` (293), `seeded independently` (343), `verified independently` (212, 732), `independently re-verified` (225, 734), `independently designed` (292, 614, 631, 653), `independently published` (106, 121, 188, 621). Seven hyphenated outliers against thirteen correct forms. |
| 6 | 331, 423, 562, 566, 579, 590 | **`multiturn` vs. `multi-turn`** — `Multiturn` (331), `multiturn` (423, 553, 562, 566, 579, 590) against `multi-turn` (197, 334, 336, 573) | Pick **`multi-turn`** and change all seven, including the table condition labels at L423 and L590. `single-turn` (330, 334, 335, 336, 572) is already consistent; `single turn` at L329 is predicative and correct as is. |
| 7 | 41, 43, 440, 545, 554, 555, 566, 579, 689 vs. 437, 470, 484 | **`vs.\ ` vs. spelled-out `versus`** | `vs.\ ` is used nine times and `versus` three times (L437, L470, L484), all in the Results, for the same comparative role. Pick one. **Note:** the `vs.\ ` sites all correctly carry the `\ ` spacing macro — an earlier section-local audit reported L554, L555 and L566 as missing it; **verified against the file, they are not missing it.** No change needed there. |
| 8 | 71 vs. 176, 650 | **`post hoc` italicized once, roman twice** — `\emph{post hoc}` (71); `post hoc` (176, 650) | Pick one. The modern convention for naturalized Latin is roman, which would mean unitalicizing L71. |
| 9 | 728 | `computable a priori` — roman | Consistent with the roman `post hoc` at L176/L650; inconsistent with the italic at L71. Resolving #8 resolves this. |
| 10 | 108, 158, 241, 285, 295, 296, 324, 328, 329, 331, 436, 469, 479, 494, 502, 533, 598, 606, 614, 620, 678, 686, 693, 701, 715, 725, 728, 732, 737, 742 | **Terminal periods on bold run-ins: 15 with, 13 without** | See §7b for the full split. Pick one. |
| 11 | 132, 377, 576 vs. 300, 410, 447, 517 | **Float placement `[h]` vs. `[t]`** | Use `[t]` throughout. |
| 12 | 205–206 vs. 210 | **Two citation formats for one source five lines apart** — `Demuynck \& Rehbeck's (2023)` hand-written in a heading, `\citet{demuynck2023computing}` in the body | Use `\citeauthor`/`\citeyear`, or drop the citation from the heading (§7 #3). |
| 13 | 158, 165 | **`\citep` after a name vs. `\citet` as subject, inside one list** — `POISE \citep{wang2026poise}` and `TrustJudge \citep{wang2025trustjudge}` alongside `\citet{chadwick2025dutchbooks}` as the grammatical subject | Pick one pattern per list. |
| 14 | 186 | `Nitsch et al.\` — hard-coded author name where L181 produced it with `\citet{nitsch2022reliability}` | Use `\citeauthor{nitsch2022reliability}` or `They`. |
| 15 | 165–166 | **Three-item list with no conjunction** — `\citet{chadwick2025dutchbooks}, TrustJudge \citep{wang2025trustjudge}, CONSISTRE \citep{sun2026consistre}` | Add `and` before the last item. Serial-comma practice is otherwise consistent throughout the manuscript (verified at L72, L91–92, L222–223, L260–261, L270–272, L360, L367, L381–382, L385, L525–526, L583, L658, L663, L720–722) — **preserve it.** |
| 16 | 62–63 | The em-dash list `restoring transitivity..., projecting..., penalizing incoherence during training` has no conjunction before the final item, and is closed by a dash followed by `and` — not a standard pairing | Add `and` before `penalizing`, or convert to a colon-list. |
| 17 | 215 | `is revealed preferred to $x_{t_2}$, **...**, $x_{t_n}$` — three literal periods as a mathematical ellipsis | Use `\dots`. |
| 18 | 238 | `Appendix~\ref{app:payoff-audit}(1)` — a hand-written sub-item index appended to a `\ref` | `Appendix~\ref{app:payoff-audit}, check~1`. |
| 19 | 342 | `i.i.d.\ rejected` — the `\ ` correctly prevents sentence spacing, but the phrasing reads as "i.i.d.-rejected" | Add a comma: `i.i.d., rejected unless`. |
| 20 | 675, 711 vs. 741 | **Appendix label prefixes** — `app:payoff-audit`, `app:method-detail`, but `sec:method-guarantee` | Make the third `app:` (§7 #12). |
| 21 | 226, 735 vs. 683, 710 | **`MIP` vs. `MILP`** | Pick one (§12a #28). |
| 22 | 543 vs. 568 | **`BH` used before `Benjamini--Hochberg` is spelled out** — `BH $p_{\mathrm{BH}}=0.011$` (543); `Benjamini--Hochberg correction` (568) | Spell out at L543, abbreviate at L568. |
| 23 | 233 | `$\sum_t\sum_k \|x_{t,k}-\tilde{x}_{t,k}\|$` uses `\|…\|` for absolute value | Consider `\lvert…\rvert`. *Stylistic preference.* |
| 24 | 727 | `$p_t\!\cdot\!\tilde{x}_t = I_t$` uses `\!` negative thin spaces around the dot | Manual spacing hacks on an inline equation; `p_t \cdot \tilde{x}_t = I_t` or `p_t^\top \tilde{x}_t = I_t` is cleaner. |
| 25 | 737–739 | The objective is set inline rather than displayed | For an appendix whose stated job is the "full formulation", this is the one thing a reader will come here to copy. *Stylistic preference — page budget is the competing consideration* — but a numbered `align` would serve better. |
| 26 | 630 | `\paragraph{Broader impacts.}` sentence-case with a terminal period, against `\section{Limitations}` / `\section{Conclusion}` title-case without | If promoted to a section (§14 #12), use `\section{Broader Impacts}`. |
| 27 | — | **En-dashes** | Verified correct and consistent throughout: `Cobb--Douglas`, `dose--response`, `coherence--competence`, `test--retest`, `Houtman--Maks`, `Benjamini--Hochberg`, ranges `0.16--0.31`, `$111$--$161$`. **No change.** |
| 28 | — | **Em-dashes** | Verified: spaced ` --- ` throughout, unspaced `x---y` zero times. **No change.** |
| 29 | — | **Number-word convention** | Related Work is internally consistent (integers under ten spelled, ten and above as numerals). Results is not (§13 #40). |
| 30 | — | **Capitalization of defined terms** | Verified consistent: `GARP` always capitalized; `Generalized Axiom of Revealed Preference` title-cased at first use (L54) and never repeated in full; `Welch`, `Pearson`, `Afriat`, `Warshall` capitalized; `big-$M$` lowercase. **No change.** |

---

# 16. Anything else

## 16a. Sentences a reader must reread to recover the meaning

Ranked by how much rereading they cost.

1. **L742–749** — three referents (`the closest published structural analogue`, `there`, `here`) plus `the prior operator` all pointing at one of two systems, in one 93-word sentence. Two rereads.
2. **L659–664** — the Conclusion's final sentence; see §9a #2 and §13 #17.
3. **L195–196** — `their finding that reframing moves models while persona prompting does not corroborates our manipulation choice` — a garden path at `does not corroborates`.
4. **L611** — `a pilot found headroom and measurement reliability do not coexist anywhere piloted` — parses on first read as `a pilot found [headroom and measurement reliability]`, a noun-phrase object, before the reader hits `do not coexist` and must reparse. Compounded by the missing `that`, and by the same root twice in eight words (`pilot` / `piloted`).
5. **L336** — `Our arm tests the opposite direction (single-turn split into multi-turn), the direction our own baseline already uses.` Three referents that cannot all be the same thing (§13 #7).
6. **L34–36** — `None controls for displacement magnitude: no result establishes whether restoring coherence itself, not mere displacement toward an interior point, is what any reported gain comes from.` The embedded `, not mere displacement toward an interior point,` sits between the subject of the `whether`-clause and its predicate, so on first pass `not mere displacement` reads as attaching to `establishes`.
7. **L506–508** — `a more general ``moving an extreme trace toward the interior helps, regardless of exactly where'' account` — a **13-word quoted clause used as a prenominal adjective**; the reader cannot parse until reaching `account`, fifteen words in. Recast: `a more general account on which moving an extreme trace toward the interior helps regardless of destination`.
8. **L680–685** — the `--- a plausible leakage channel on first read ---` interruption arrives before the reader knows what the channel would be, so the dash-clause must be held in memory across the `but`.
9. **L625–628** — the `do not read this as ... only that` construction split by a nineteen-word em-dash insertion.
10. **L606–609** — the `only the within-run…` fragment appended by comma with no verb.
11. **L167–169** — `respectively` binding across 25 words and two citations; the reader must count back.
12. **L163–165** — `Three further inference-time repairs lack a genuine degree parameter or Afriat machinery, on different objects: X, Y, Z.` It cannot be determined whether `on different objects` modifies the repairs, the parameters, or the machinery.
13. **L186–188** — `whose` antecedent is `problem`, but `problem`'s remedy being `this paper's design` requires holding three nouns at once.
14. **L717–718** — `regardless of ordering` at the end of a subordinate clause of a subordinate clause; the reader must reconstruct that it answers the preceding clause's `fixing a candidate preference ordering`.
15. **L728–730** — `converts an unattained infimum into an attained minimum: the GARP-consistent set is not closed, so ...` The colon promises an explanation of the conversion and delivers the motivation for it. Reversing the halves fixes it.
16. **L555–556** — `This is no detectable CCEI shift, not a confirmation of the pilot's own naive estimate` — a negative predicate ruled out against another negative.
17. **L309** — `Counts are the main experiment's (\S\ref{sec:results}).` A possessive with an elided noun; unrecoverable even on rereading (§8f #4).
18. **L495–497** — a 30-word subject–verb distance across an em-dash aside.
19. **L502–504** — a 23-word parenthetical between subject and verb.

## 16b. Unclear antecedents

| Line | Text | Problem |
|---|---|---|
| 36 | `We build that control.` | `that control` refers to a **verb** (`None controls`), not a noun. Grammatically the antecedent does not exist. Rewrite L34 to introduce the noun (`No published result includes a displacement-matched control.`) and `We build that control` then has a referent. |
| 79 | `That relationship` | Refers to `the relationship this paper reports` (L77), itself unnamed. |
| 176, 178, 185, 200 | **`ours`, four times, three different referents** | L176 `where ours acts post hoc` (our operator); L178 `ours is the empirical counterpart` (our study); L185 `ours attains rationalizability` (our operator); L200 `their 7B model and ours` (our models). Replace each with the noun. |
| 185 | `the same distinction` | Must be reconstructed from the previous sentence's parenthetical. |
| 189 | `three independently published axiom-enforcement results` | The reader must reverse-engineer the set as {nitsch, yamin, zhu}. Name all three. |
| 190 | `neither published negative` | A fourth name for the same set, and the wrong number (§13 #14). |
| 284 | `raises its payoff` | Ambiguous between the operator's and the bundle's payoff. |
| 437 | `and it is stronger at the headroom model` | `it` = the relationship, but the nearest noun is `positive relationship` inside a coordinated clause — loose, and the sentence is bolded. |
| 464 | `this gap` | Refers to the severity/geometry distinction two clauses back, across an em-dash aside. |
| 515 | `the rounds that generate the null's advantage **there**` | `there` = in that trace; a deictic doing work a noun should do. |
| 539 | `does not fully resolve it` (in a heading) | `it` has no antecedent at all in a heading. |
| 570 | `the same pattern` | No pattern has been named (§12a #25). |
| 608 | `the headline statistic itself` | Which statistic? CCEI, GARP pass rate, and payoff gain have all been referenced. |
| 634–635 | `the confound this paper's control was built to catch` | Which confound — the severity confound of L438, or the geometry confound of L461? |
| 655 | `without fully resolving it` | `it` could be the explanation, the advantage, or the mechanism. |
| 683 | `the solver used` | Never named in the appendix (it is HiGHS, named 460 lines earlier). |
| 684 | `the reported distance` | First use of `distance` in the appendix, with a definite article. |
| 698 | `the sign of the outcome` | Which outcome? `outcome` appears nowhere else in the appendix. |
| 703 | `It does not explain ...` | `It` follows a sentence whose last noun phrase is `a genuine ceiling-effect confound` but whose grammatical subjects were two correlations. |
| 746 | `the prior operator's cone` | `the prior operator` has not been named. |

## 16c. Word-level tics, counted

1. **`independently` — 20 instances** (L42, 83, 106, 110, 114, 121, 188, 212, 225, 292, 293, 341, 343, 345, 482, 542, 614, 621, 631, 653, 732, 734). Load-bearing at L110, L212, L225, L293, L343, L732 (verification and randomization); filler or unverifiable at the rest. The repetition reads as a defensive verbal habit — the paper insisting on its own independence. Keep half.
2. **`own` — 51 lines.** `own choices` is a defined term and must not be touched; but `the projection's own feasibility incumbent` (250), `the real projection's own dose` (287), `the pilot's own naive handling` (358), `the pilot's own naive estimate` (556), `raw payoff's own marginal contribution` (443), `raw payoff's own coefficient` (707), `GPM's own length-controlled metric` (174), `HRC/DSPPO's own inverted-U dose--response curve` (174–175), `each trace's own observed data` (237, 681), `this trace's own draw` (525), `the pilot's own magnitude` (601), `this paper's own attempt` (627), `the agent's own revealed choices` (249) are all deletable or replaceable. **Note the `X's own` device used twice in two consecutive lines at L174–175** — the same "turn their own evidence against them" move; once is effective, twice reads as prosecutorial.
3. **`identical` — 3 instances** (L38–39, L81, L93). The first two are the same phrase; the third borrows its force. Use `the same` at L93.
4. **`growing literature` twice in three lines** (L59, L61). Delete `growing` from the second.
5. **`Separately, splitting ... into separate sequential calls`** (L103–104) — `Separately` and `separate` in one clause.
6. **`analogue` / `analogous` — three cognates in one 93-word sentence** (L742 `structural analogue`, L745 `no analogue here`, L748 `analogous to the convex case`). Keep one.
7. **`collapse` as the default verb for any decrease** — L104, L120, L543, L565, plus `overturns` at L429. `drops` would do at two of them.
8. **`Against the literature this arm was designed against`** (L570–571) — `Against ... against` in one clause.
9. **`Our opposite manipulation finds the opposite direction`** (L198) — `opposite ... opposite` in six words.
10. **`a pilot found ... anywhere piloted`** (L611) — same root twice in eight words.
11. **`The payoff implementation has no dependency on the projection implementation`** (L678–679) — `implementation` twice in one clause.
12. **`clean` / `cleanly`, both undefined, twice** (L68, L92).

## 16d. Emphasis markup used as rhetorical stress

**22 `\emph{}` uses** across the manuscript (L65, 71, 105, 120, 134, 136, 163, 171, 174, 180, 183, 196, 232, 265, 461, 462, 463, 549, 553, 572, 610, 697). They are doing three different jobs and the reader cannot tell them apart:

| Job | Instances | Verdict |
|---|---|---|
| **Term introduction** | `\emph{dose}` (65, 232); `\emph{Own choices}` / `\emph{Exogenous payoff}` (134, 136, caption column names) | **Keep.** This is the correct use, and §7 recommends extending it to the terms currently in bold. |
| **Genuine contrastive stress** | `\emph{teacher's}` (163); `\emph{preference model}` (171); `\emph{format}` (196); `\emph{non-monotonic}` (265); `\emph{severity}` / `\emph{geometry}` (461–462); `\emph{across}` (610) | **Keep.** In each case the contrast is the content. |
| **Rhetorical stress on a word the sentence already stresses by position** | `\emph{opposite}` (105, 120); `\emph{loses}` (174); `\emph{PNAS}` (180); `\emph{fall}` (183); `\emph{specifically}` (463); `\emph{not}` (549); `\emph{other}` (553); `\emph{more}` (572); `\emph{negative}` (697); `\emph{post hoc}` (71 — a Latin-italics question, see §15 #8) | **Drop the italics on all nine.** `18 of 24`, `$-0.35$`, `0.40 to 0.10` and the surrounding numbers already do the work. `\emph{PNAS}` should go with its clause (§2 #9). |

Nine rhetorical against twelve legitimate. As it stands the rhetorical ones devalue the contrastive ones.

## 16e. Metaphors that do not survive scrutiny

| Line | Text | Problem | Fix |
|---|---|---|---|
| 65, 72–73 | `\emph{dose}` | **Asserted before it is earned.** L65 introduces `dose` in italics as a term of art; L72–73 defines it seven lines later, in a different paragraph. Move the definition to first use, or use the plain phrasing at L65 that the sentence already supplies. | — |
| 158 | `the sharpest vocabulary collision` | Vocabularies do not collide, and the sentence never says which words are in the collision. | Say which words collide (§14 #24). |
| 178 | `a proposal that has circulated unrun` | `unrun` is a coinage; `circulated` implies a preprint circuit the reader cannot check. | `a proposal that has been argued but not measured`. |
| 185 | `the same distinction that disposes of` | Courtroom register applied to a published paper, and it overclaims — a distinction does not dispose of a method. | `the same distinction separates ours from`. |
| 189 | `point the same adverse way` | Mixed metaphor: results point, but "the same adverse way" is a direction with no compass. | `report the same negative outcome`. |
| 194 | `two of our three legs` | A stool metaphor that contradicts the four criteria and appears once, with no setup. | `two of the four criteria` (§13 #2). |
| 261–263 | `This mirrors --- not the specifics, but the structure of --- a money-metric utility index` | "Mirrors the structure of" does analogical work the sentence then hedges away with an interrupting negation. | Either the payoff *is* a money-metric-style index (say so) or the resemblance is not load-bearing (delete). |
| 271 | `a projection direction secretly aimed at the payoff optimum` | `secretly` implies intent by the algorithm. | `correlated with the payoff optimum`. |
| 499 | `iterating the yardstick` | `yardstick` and `payoff-shopping` are two metaphors for the same object, four words apart. | Keep one. |
| 634–635 | `the confound this paper's control was built to catch` | Controls do not catch confounds; they neutralize or expose them. `Catch` imports a trap metaphor the paper's measurement vocabulary does not support. | See §13 #18. |
| 684 | `an upper-bound sanity ceiling` | A ceiling that is a sanity check that is an upper bound — three metaphors stacked, and `sanity ceiling` is not a term of art. | `an upper bound on the reported distance`. |
| 703 | `more room to improve` | The ceiling-effect metaphor restated one clause after `ceiling-effect confound` names it. | `worse-starting traces improve more`. |
| 704 | `explain the dose--response relationship away` | Colloquial phrasal verb in a paragraph of regression statistics. | `does not account for`. |
| 664 | `paper over` | **A pun in the closing sentence of a paper.** Whether or not it is intentional, it reads as intentional. | Deleted per §10 #34. |
| 507, 511 | `centering` / `escape a bad start` | **Both survive scrutiny** — they describe the geometry accurately. **No change.** | — |

## 16f. Grammar and mechanics

| Line | Text | Fix |
|---|---|---|
| 181–182 | `find CCEI/Houtman--Maks ... reliability never reaches acceptable levels ..., and that participants ...` | **Parallelism break:** `find X ... and that Y`. Insert `that` in the first conjunct. |
| 175–176 | `scored by an LLM judge, where ours acts post hoc` | `where` used as a contrastive conjunction. Use `whereas`, or split. |
| 285–287 | `We construct a \textbf{null operator}: for each GARP-violating trace, shrink every observed bundle...` | **Mood shift mid-sentence** — declarative subject `We construct`, then a subjectless imperative `shrink` after the colon. Fix: `We construct a null operator that shrinks every observed bundle in a GARP-violating trace toward the exogenous optimum $x^*_t$...` |
| 318–321 | `Two locally-hosted open-weight models, run entirely on local compute at zero API cost: ...` | **Sentence fragment with no main verb**, 45 words. Telegraphic style is defensible in a design section — L328 (`Three conditions at 1.5B, two at 3B.`) uses it well — but not at this length with two nested parentheticals. Fix: `We use two locally hosted open-weight models: \texttt{qwen2.5:1.5b-instruct} and \texttt{llama3.2:3b-instruct}.` Then the two roles in their own sentences. |
| 224–225 | `every one of the 85 GARP-violating traces' projections was independently re-verified` | **Triple genitive** — `one of the traces' projections` stacks two possessives. Fix: `all 85 projections were independently re-verified GARP-consistent`. |
| 236–237 | `A Cobb--Douglas demand share-fitted to each trace's own observed data` | `share-fitted` is coined here and never explained. Fitted how, to what loss, on which shares? Fix: `a Cobb--Douglas demand whose expenditure shares are fitted to each trace's observed data`. |
| 616 | `the first's single, globally-identical optimum` | Awkward possessive-of-an-ordinal; the reader must reconstruct `the first payoff's`. |
| 622–623 | `it failed to induce the coherence variation it was designed to.` | **Stranded infinitive** — the verb is elided after `designed to`. British-style verb ellipsis, jarring in a paper that is otherwise American. Fix: `it was designed to induce`. |
| 650 | `\citet{demuynck2023computing}'s minimal-quantity-error GARP repair post hoc to a frozen agent` | A possessive on a `\citet` inside a participial phrase, followed by a four-word compound modifier and two prepositional phrases. Fix: `Applying the minimal-quantity-error GARP repair of \citet{demuynck2023computing} post hoc to a frozen agent, ...` |
| 89 | `\S\ref{sec:related} concedes exactly what is not.` | **Elliptical construction with a missing noun** — `what is not [new]`. The elision is one word too far and stops the reader. (Deleted per §3 #3, but noted in case it is kept.) |
| 406 | `(2 models $\times$ up to 3 conditions $\times$ 30 replicates)` | **The multiplication does not multiply:** $2\times3\times30 = 180$, not 150. The reader must reverse-engineer that one model ran 2 conditions and the other 3. Fix: `(llama3.2:3b in 2 conditions, qwen2.5:1.5b in 3, 30 replicates each)`. |
| 472 | `This holds independently at both models.` | `at` a model is idiomatically odd; the manuscript also uses `at 1.5B`, `at 3B`, `at the headroom model`. *Stylistic preference*, but pick one preposition and use it at all six sites (L432, 437, 438, 472, 542, 549). |
| 551–553 | `falling to a residual 20.0\% (6/30) after the retry protocol --- smaller than the pilot's unretried 52\%` | **The comparison is not like-for-like** — a post-retry rate against a pre-retry rate — and the sentence does not flag it. Fix: add the first-attempt figure: `43.3\% on first attempt, against the pilot's unretried 52\%`. |
| 559–560 | `the finer-grained per-attempt breakdown these top-line numbers average over` | Stranded preposition on a heavy relative clause; the reader parses `average over` as a verb phrase looking for an object. |
| 631 | `deployed AI economic agents` | Appears once, in the paper's only policy claim, with no definition. A reviewer will ask which deployments. Name one, or drop `deployed`. |
| 637–638 | `in a given setting` | Vacuous — every measurement design measures something in a given setting. Delete, or name the setting the design generalizes to. |
| 221 | `At $T=25$ this is 600 binaries and 125 continuous variables per trace` | $T(T-1)=600$ checks out, but `125` requires knowing $K$, which is not stated until L342 — and by then $K$ has been reused for something else (L293). State `$K=2$ goods` at L214. |
| 429–430 vs. 596–597 | `we` vs. `this paper` as the acting agent | The manuscript alternates: `we` at L36, 68, 73, 92, 252, 269, 285, 292, 295, 614, 625, 642, 651, 657, 731; `this paper` at L39, 46, 598, 620, 627, 630, 634, 648, 656. *Stylistic preference, not error* — the natural split is `we` for actions taken and `this paper` for the artifact's claims, which is roughly what happens already. The exception is **L598, `the paper leads with GARP pass rate`**, which describes an authorial choice and should be `we lead with` — or, better, is deleted per §1 #84. |

## 16g. Checked and found nothing

Verified across all 754 lines and clean: no run IDs beyond `replicate 12` (L520); no file paths, URLs, or source-code identifiers in prose; no TODO/FIXME leakage; no commented-out text; no mixed date formats (no dates); no footnotes other than the table-2 asterisk; no `It is X that` / `There is X which` clefts beyond those listed in §6; no British spellings beyond the three in §15 and the standard `analogue`; no serial-comma inconsistency; no en-dash or em-dash inconsistency; no capitalization drift on defined terms; every figure and table carries a `\label` (**one subsection does not** — L562, §7 #9); and the arithmetic listed in §13e all checks out.

---

# Triage: the five changes that most improve how a skeptical reviewer reads this paper

Drawn from the whole manuscript, not from any one section. Each entry names what a reviewer sees, and roughly how long the fix takes.

**1. Fix the Figure 1 body/caption mismatch at L435. — 10 minutes, plus 5 to move the citation.**
`Figure~\ref{fig:doseresponse} shows the relationship split by model on shared axes` (L435) describes a dose-vs-$\Delta$payoff plot with a per-model panel split. The caption (L450–455) describes a real-vs-null scatter whose panels are Experiment 1 and Experiment 2. **These are different figures.** It is the paper's first figure, it is cited from the paragraph carrying the headline dose–response statistics, and a reviewer who looks at the figure while reading that sentence stops reading and starts checking everything else. Delete L435 and cite the figure from inside the Experiment 1 paragraph after L471. *(The companion suspicion that the null operator is used before it is defined is overturned — it is defined at L285–289, 165 lines earlier.)*

**2. Resolve the `large apparent effect` self-contradiction at L98–100. — 10 minutes, but the author must decide which quantity is meant.**
`a large apparent effect that disappears once discard-selection is corrected` is immediately followed by `the pilot's naive estimate and the corrected main-experiment estimate are both statistically indistinguishable from zero`. If the pilot estimate was indistinguishable from zero, there was no large effect to disappear. The only pilot numbers anywhere in the manuscript are a 52% discard rate (L357) and `+0.0169 ($p=0.66$)` (L556), so nothing in the paper supports `large apparent effect` as written. This sits in the paragraph that introduces one of the paper's three headline findings; a reviewer who spots it discounts the framing result entirely.

**3. Fix the `two of our three legs` miscount at L194, and the same three-versus-four mismatch in the Conclusion at L657. — 5 minutes for L194, 15 for the pair.**
The paper defines **four** criteria at L128, gives them four table columns, and asserts `None occupies all four` at L130 — then at L194 scores its nearest competitor against `our three legs`. `legs` appears nowhere else in the manuscript. Purely a wording fix (`they meet two of the four criteria`), no science or number changes. The same mismatch resurfaces in the Conclusion, where the priority claim at L657 is stated against **three** confounds that do not map onto Related Work's **four** criteria — so a reviewer trying to check the paper's own priority claim against its own table cannot. A reviewer who catches either one re-checks the whole positioning argument.

**4. Correct Table 3's caption, and reconcile it with `Every cell reached its full 30 replicates`. — 15 minutes, no numbers touched.**
The caption at L412 says `dose and $\Delta$payoff are computed on the subset of kept traces that violate GARP`. Weighting the per-cell means that way gives an overall $\Delta$payoff of 0.0062, matching nothing in the text. Weighting by `$n$ kept` gives exactly 0.00910, matching L434 and L471 — so the column is averaged over **all** kept traces with 0 imputed for GARP-consistent ones, the same convention Table 2's caption already states at L384–385. The caption is wrong, and it also never says which of the two payoffs the column uses. Alongside it, `Every cell reached its full 30 replicates` (L408) is true of slots and false of kept traces, and reads as contradicting the `28` and `24` two lines below; `Every cell was run to its full 30 slots; 142 of 150 yielded a usable trace` fixes it. **The numbers are sound; only the descriptions are wrong** — which is exactly why a reviewer who tries the arithmetic and gets 0.0062 will assume the opposite.

**5. Rebuild the Conclusion's final sentence, and add the recommendation that is currently absent from the whole paper. — 30 minutes.**
The paper's last sentence (L659–664) is 86 words, separates its subject from its verb by a 53-word parenthetical, and closes on a pun (`paper over`). Its `two findings ... : three items` structure is *not* a strict count contradiction — the three-item list is a whole-paper summary and only one of its items comes from the announced pair — but the colon primes the reader to count three against two, and the partial overlap makes the mis-parse worse than a clean mismatch would. Break it into two sentences, one per finding, and delete the closing clause. Then use the space to add the sentence the paper never makes anywhere: `A practitioner evaluating coherence repair should include a distance-matched null operator before reading a dose--response correlation as evidence of benefit.` The paper's only actionable recommendation currently sits inside `\paragraph{Broader impacts.}` at the tail of §Limitations, after four paragraphs of self-criticism; the Conclusion, the Introduction and Related Work each diagnose the gap and none says what to do about it.

**Also fixable in the same pass, at 5 minutes each:** add `\citep{wang2025tactics}` at L106, L122 and L663, the three sites where the paper claims to contradict a published finding without naming it (it is correctly cited at L196, L335 and L571); and add the missing `\label{sec:results-multiturn}` at L562 and fix the mis-scoped `\label{sec:method-guarantee}` at L741, which currently sends `\S\ref` at L162 to the top of Appendix B.

**Explicitly out of prose-fix scope — do not paper over these in Phase 2:**
- **L702–703, `$r=-0.41$` printed for two different correlations.** corr(dose, raw payoff) is corroborated at L440; corr(raw payoff, $\Delta$payoff) appears only at L703, at the identical two-decimal value, with no $p$-value. They may genuinely coincide or one may be a copy-paste. **Needs author verification of the underlying numbers.**
- **L226 / L735, `MIP gap $\le 8.1\times10^{-5}$`.** Whether this is the largest observed gap or the solver's configured tolerance changes what the sentence claims. **Needs author verification of the run configuration.**
