# Phase 2 application log — docs/PROSE_AUDIT.md -> tex/paper.tex

Method note: entries were applied region-by-region through the file (abstract -> appendix), applying
the union of all 16 categories to each passage in one edit, because the audit cross-references
itself heavily (a single sentence commonly carries entries from 5+ categories and the audit's own
replacement text folds later categories' sub-fixes in). Every entry is logged below under its own
category. Line references are the audit's (pre-edit) numbering.

File went 755 -> 730 lines. All 24 `\label`s resolve; all 19 distinct `\ref` targets exist.

---

## Category 1 — rhetorical negation

APPLIED (abstract/intro): 1a#1 `is not new`->`is an established line of work`; #2 deleted `None
controls for displacement magnitude:`; #3 replaced with positive form; #4 folded; #5 deleted
`we decline a third as payoff-shopping` from abstract; #6 deleted `instead`/`standing`; #7 kept
contrast, moved forward (`with no repair step`); #8 `What none of them establishes`->`None of them
establishes`; #12 deleted `, not a restatement of coherence`; #13 -> `The design does not identify
the effect of coherence restoration.`; #14 kept negation, deleted `as originally proposed`/`mere`/
`does on its own`, added `(0.0091 vs. 0.0220)`; #15 deleted; #16 deleted; #17 `The conjunction is
new:`; #18 promoted to two sentences; #19 replaced; #20 deleted `--- not a novel method ---`;
#21 `verified independently on every output, not by solver status`; #22 replaced triple negation;
#23 `reported per cell`.
SKIPPED (marked Keep): 1a#9, #10, #11.

APPLIED (related work): 1b#24 -> `Of nine published repair systems, none satisfies all four`;
#25 parenthetical cut (definition now only in caption); #26 caption definition; #29 `the
minimum-distance priority is theirs`; #30 second half cut; #31 `have a binary edit and no Afriat
machinery`; #34 `on a priori grounds and reports no measurement of it`; #35 replaced the four-
negation cascade; #36 reordered so the positive claim closes the section.
SKIPPED (Keep): 1b#27, #28, #33.
FLAGGED: 1b#32 (see FLAGGED list).

APPLIED (method/design): 1c#37, #38 deleted; #39 kept, trimmed `naive`; #40 `$L_\infty$ is
recorded alongside.`; #41 `paired with the exogenous payoff of \S...`; #42 deleted; #43 `it is not
supplied to the solver`; #44 -> `\textbf{Guarantees.}`; #46 active voice; #47 `The payoff is fixed
independently of the agent's revealed choices.`; #48 clause deleted; #49 own sentence; #50 `which
depends only on prices and income`; #51 `This has the structure of a money-metric utility index`;
#52 recast (also fixes the dangler); #53 `All four are ruled out`; #54 merged; #55 `displacement
alone`; #56 trimmed; #57 `raises that bundle's payoff whether or not it restores GARP-consistency`;
#59 `The two are reported separately.`; #60 `it uses the per-trace $\alpha_s$, which a repair
algorithm does not observe`; #61 `The 3B model is a low-headroom control, so this condition was run
at 1.5B only.`; #62 `Independent seeding supports between-condition replication.`; #63 deleted;
#64 deleted; #65 replaced with the numbers; #66 promoted to its own sentence.
SKIPPED (Keep): 1c#45.
PARTIAL: 1c#58 — negation + `in general` hedge removed (`is not guaranteed to restore
consistency`); the audit's requested count of traces restored is not in the paper. See FLAGGED.

APPLIED (results): 1d#69 deleted `the oracle null is not plotted`; #70 `bears on the severity ...
It leaves open whether ...`; #71 shortened; #72 `and uses no GARP information`; #73 deleted; #74
deleted the self-contradictory clause; #75 lead -> `\textbf{Two payoff designs.}`; #76 -> `We treat
the "escape a bad start" reading as a hypothesis for the discussion; we do not test it.`; #78
deleted `mere`; #79 kept, dropped `real`; #80 kept, dropped `proper`; #81 -> `Neither experiment
detects a CCEI shift`; #82 deleted the sign-difference disclaimer.
SKIPPED (Keep): 1d#67, #68, #77, #83.

APPLIED (limitations/conclusion): 1e#84, #85, #86, #87, #88, #89, #90, #91, #92, #93 — all applied
as written.

APPLIED (appendix): 1f#94 `(1) Payoff inputs.`; #95 `computed from $(p_t,I_t)$ by a routine that
reads no projection output`; #97 fact-first restructure; #98 deleted; #99 `No population-level link
... is detectable`; #100 rephrased; #101 `The dose--response relationship survives it:`; #103
compressed and moved after the adopted formulation; #104 deleted `that carry no multipliers`; #105
positive statement; #107 deleted; #109 `does not transfer`; #112 `we claim no distance-minimization
guarantee`.
SKIPPED (Keep): 1f#96, #102, #106, #108, #110, #111 (#111's attachment fixed per §4 #76).

APPLIED (1g cascades): all 11 cascades dissolved by the above.
APPLIED (1h mirrored pairs): 1–9 all resolved (kept the surviving instance the audit names).
APPLIED (1i): all 8 `mere`/`merely` deleted. `command grep` confirms 0 remaining.

## Category 2 — self-announcing significance

APPLIED: #2 `significantly,` -> p-value; #3 deleted `This is the paper's central finding:`; #4
deleted; #5 replaced with the reason; #6 `four criteria`; #7 POISE lead rewritten; #8 dropped `Our
closest theoretical neighbour`; #9 deleted `and it is in \emph{PNAS}`; #10 deleted the arXiv-sweep
sentence; #11 crash framing de-elevated; #12 deleted `and its correction as a stated contribution`;
#13 `This is a claim about instrument validity.`; #14 deleted `first-class` + the announcement;
#15 unbolded the both-scales claim; #17 deleted `but the paired comparison is unambiguous:`; #18
`Experiment 2 reproduces Experiment 1:`; #19 see §7 #23; #20 deleted `is the finding`; #21 lead ->
`\textbf{Trace extremity and the null's advantage.}`; #22 unbolded the C1 verdict; #23 deleted
`This is an open design tradeoff:`; #24 deleted `central`; #25 deleted `are reported in their own
right`. All six superlative self-locating phrases removed.
SKIPPED (marked "No change"): #1.
FLAGGED: #16 (see FLAGGED list).

## Category 3 — roadmap / forward-pointer sentences

APPLIED: #1, #2, #3, #4, #6, #7, #9, #10, #11, #12, #13, #14, #15, #16, #17, #18, #19, #20, #21,
#22, #23, #24, #25, #26 — all deleted or folded as the audit specifies. The three
`Appendix~\ref{app:method-detail}` pointers reduced to one; both appendix opener template sentences
deleted.
SKIPPED (Keep): #5 (`\textbf{Contributions.}`).
NOTE: #12 deleted the only citation of `fig:pipeline`, so the figure was re-cited inside a claim
(`the \emph{dose} ... (Figure~\ref{fig:pipeline}, step 5)`) rather than left uncited.
APPLIED (3a): 1–5 de-duplicated (contributions list trimmed, related-work framing collapsed,
discard paragraph's restated sentence deleted, L461–467 cut to two sentences, both appendix openers
deleted).

## Category 4 — trailing appositive qualifications

APPLIED: 4a #1–#15 (all; #9 and #10 danglers fixed). 4b #16–#26 (all; #24's count error corrected
to `two of the four criteria`, #25's dangling modifier split). 4c #27–#47 (all; #34, #40, #45, #47
danglers fixed). 4d #49–#59 (all; #54's dangling `read as` removed). 4e #60–#68 (all; #63's
misattached `once corrected` recast). 4f #69–#77 (all; #75 and #76 danglers fixed).
PARTIAL: #48 — the zero-imputation convention was moved into §sec:method-projection as the audit
directs; Table 2's caption now points there.
PARTIAL: #51, #53 — promoted out of the appositive, but the audit's requested quantities (across-
draw SD of r; the two real-repair correlations) are not in the paper. See FLAGGED.
SKIPPED (Keep): #43.

## Category 5 — softening adverbs / undefined qualifiers

APPLIED (5a): #1 (title `Actually` cut), #2–#5, #7–#19, #21–#25, #27–#39, #41–#44, #46–#66,
#68–#77, #79–#81, #83–#101, #104, #105, #106. Where the audit said "use the number", the number
already in the paper was used (0.40->0.10; CCEI 0.99; 0.1429 vs 0.4706; 0.0118 / 0.143; $\ge0.999$;
80.4%; within 0.01).
SKIPPED (Keep): #26, #31 (`exactly` kept), #40, #45, #67, #78, #82, #92, #103.
FLAGGED: #20 (`acceptable levels`), #32 (count), #76-adjacent `attenuation`, #59/#103 (`stable`).
APPLIED (5b): #2, #3, #4, #5, #6, #7, #8 (`borderline significance` -> `does not reach
significance`), #9, #10, #11 — all resolved.
FLAGGED: 5b#1 (the `large apparent effect` contradiction).
APPLIED (5c): resolved `fixed center`/`fixed interior point`, `information-fair`, `headroom model`,
`first-class`, `an operator that knows nothing about GARP`, `formal`, `default`, `well-controlled`,
`derived quantity`, `sanity ceiling`, `adequately powered`, `known pathology`, `clean/cleanly`,
`audited adversarially`, `stated retry protocol`, superlatives.
FLAGGED: 5c `stable` (γ sweep), `attenuation` (60%), `acceptable levels`.

## Category 6 — "What" clefts and expletives

APPLIED: #2, #3, #4, #5, #6, #7 (second occurrence, now `\subsection{Scope of the guarantee}`),
#8, #9, #10, #11, #12, #13, #14, #15, #17, #18, #19, #20, #21, #22, #23, #24, #25, #26.
SKIPPED: #1 (title interrogative — audit marks stylistic; only `Actually` cut). #16 (Keep).

## Category 7 — headings and bold leads

APPLIED (7a): #3 -> `Minimal-quantity-error MILP projection`; #5 -> `Null-operator controls`;
#6 -> `Discard selection and the retry protocol`; #7 -> `Dose--response and the null-operator
control`; #8 -> `Reciprocal framing and discard selection`; #9 -> `Multi-turn elicitation format`
+ added the missing `\label{sec:results-multiturn}`; #10 -> promoted to `\section{Broader Impacts}`;
#11 -> `MILP formulation and implementation`; #12 -> mis-scoped `\label{sec:method-guarantee}`
replaced by `\subsection{Scope of the guarantee}\label{app:guarantee}`, and the Related-Work
cross-reference retargeted.
SKIPPED: #1 (title replacement — framing decision, see FLAGGED), #2 (all correct), #4 (stylistic).
APPLIED (7b): #14 (period added), #15, #16 (all four Related Work paragraphs now carry noun-phrase
leads), #17, #18 (bold->emph for term definitions), #20 (periods), #21, #23, #24, #25, #26, #27
(split into two leads), #28, #29, #30, #31, #32, #33, #35, #36 (three commitments split into three
noun-phrase-led paragraphs), #38.
SKIPPED (Keep): #13, #19, #22, #34, #37.
Terminal-period convention now uniform: every `\textbf{}` run-in lead carries a period.

## Category 8 — captions

APPLIED 8a: all four cuts; caption now 3 sentences. The body/caption mismatch (highest-severity
entry) fixed: the misdescribing sentence at L435 deleted and the figure re-cited inside the
Experiment 1 claim (`81\%; Fig.~\ref{fig:doseresponse}A`).
APPLIED 8b: sentence 6 moved into the body, sentence 7 deleted, verification-process record moved to
Appendix A; caption now 3 sentences.
APPLIED 8c: #1 (body duplicate deleted), #2 (convention moved to Method), #3 (finding moved into
§sec:discard body, footnote shrunk). Caption 3 sentences.
SKIPPED 8c: the `n` column `3 of 6` change — data cell, excluded by the operator.
APPLIED 8d: caption corrected to the zero-imputation convention and now names its payoff.
APPLIED 8e: #1, #2, #3, #4 all applied; caption 2 sentences.
APPLIED 8f: #1, #2, #3, #4 all applied; caption 2 sentences.
APPLIED 8g: #1, #2, #3 applied (caption now defines all four columns in 3 sentences).
SKIPPED 8g: #4 (`partial`, `no (declined)` are data cells — excluded), #5, #6 (stylistic).

HARD CAP CHECK (final): fig:doseresponse 3 | fig:pipeline 2 | fig:mechanism 3 |
tab:discardbreakdown 3 | tab:multiturn 2. All within the 2–3 cap.

## Category 9 — run-on / over-nested sentences

APPLIED 9a: all five worst sentences split as the audit shows (#1 93-word appendix paragraph -> 4
sentences; #2 conclusion final sentence -> 3 short sentences across a new paragraph; #3 intro
central-finding sentence -> 3; #4 Related Work garden path -> 3; #5 discard paragraph -> 3).
APPLIED 9b: every listed sentence rebuilt or split, including the two verbless "sentences" in the
Contributions list, the models fragment, the payoff-audit run-on, the mood shift at the null
operator, and the three Appendix B stacks.
APPLIED 9c: all comma splices fixed, including the true splice at L406–407 and the appendix's
lab-notebook fragment at L688–690.

## Category 10 — aphoristic endings

APPLIED (converted/deleted): #2, #3, #4, #5, #7, #8, #9, #10, #11, #12, #13, #14, #15, #17, #18,
#19, #20, #21, #22, #23, #24, #25 (converted by adding the caption's numbers), #27, #28, #29, #30,
#32, #34 (deleted — the paper now ends on its own finding), #35, #36 (made positive).
KEPT (audit says earns its place): #1 (`We build that control.` — its antecedent was also repaired
per §16b), #6 (verb corrected to `none satisfies all four`), #16 (stated positively), #26 (kept,
`real` and the internal locator dropped), #31 (kept, §1 #87 trim applied).
SKIPPED (lowest priority, stylistic): #33.

## Category 11 — process-record / internal-code leakage

APPLIED 11a: the nine surface forms for the pilot reduced to `the pilot` / `the pilot's`
throughout (verified by grep — `a pilot study`, `a pilot run`, `a pilot's`, `the same pilot`,
`anywhere piloted` all gone).
PARTIAL 11a: the audit also asks for one sentence describing/sizing the pilot at first use. Not
added — see FLAGGED.
APPLIED 11b: #1–#8, #9 (restated as a fact about the payoff), #10–#38, #39, #41–#64. Notable:
`$L_2$ would require an MIQP solver we do not have configured` -> `an MIQP formulation`;
`multi-model-residency crash under sustained rotation` and `model-major` replaced by a plain
description; `output-format contract` -> `output format`; `attempt-record`/`replicate slot` retired;
`sanity ceiling` -> `an upper bound on the reported distance`; HiGHS now named in the appendix;
`a plausible leakage channel on first read` deleted.
SKIPPED: #40 (`replicate 12` — audit marks stylistic; kept for reproducibility).
APPLIED 11c: `C1/C2/C3` now introduced once, in the Introduction, at the point C1 is stated; `(C1)`
removed from the subsection heading; `Appendix~\ref{app:payoff-audit}(1)` -> `..., check~1`;
`sec:method-nullop` heading now matches its label; `sec:method-guarantee` replaced by a real
`\subsection` + `app:guarantee` label.

## Category 12 — terminology and notation drift

APPLIED 12a: #1 (repair operator: `the projection` in Method, `the real repair` only in the paired
contrast; `restoring rationality`, `GARP-restoration`, `repair size` retired); #2 (`the null
operator` / `the primary null` / `the oracle null`; `information-fair` deleted from prose);
#3 (`null-effect control` / `headroom/null-control` -> `low-headroom control`, so `null` now names
only the operator and statistical nulls); #4 (`dose` in prose, `dose-matched` as the single name for
the matching constraint — `distance-matched` and `size-matched` retired); #5 (slot -> attempt ->
trace defined once in §sec:design and used consistently; `attempt-record`, `replicate slot` and our
own `arm` deleted); #6 (`GARP-consistency` technical, `coherence` informal; appendix's bare
`coherence` changed); #7/#8 (`payoff design` / `Experiment 1 (original payoff)` bound once);
#9 (three canonical attempt-group names); #10 (`the capped retry protocol`); #11 (`the pilot`);
#12 (`the Afriat index` -> `CCEI`, `CCEI/Houtman--Maks` -> `CCEI and Houtman--Maks`); #13 (`Bronars
power of the budget set`, never bare `power`); #14 (`legs` -> `the four criteria`, count corrected);
#15 (`minimum-distance projection`, `formal` dropped); #16 (`the Warshall-closure GARP check` named
in the Method body, not first in a caption); #17 (the four Cobb--Douglas objects renamed apart);
#18 (`feasibility incumbent` retired so the solver keeps `incumbent`); #19 (full tag once, 1.5B/3B
in prose, short tag in tables); #20 (`multi-turn`/`single-turn` throughout, including both table
labels); #21 (`reciprocal framing` after one definition); #22 (`discard-selection`; `survivorship`
removed from the heading); #23 (`dose--response relationship`); #24 (`condition`, not `arm`);
#25 (the unnamed pattern now stated as `GARP pass rate separates the conditions and CCEI does not`);
#26/#27 (`the prior operator` named; extremity terms aligned).
PARTIAL 12a: #28 `MIP`/`MILP` — left as-is; the MIP-gap sentence is operator-excluded.
APPLIED 12b: `$M,N$` prices renamed to `$p_A,p_B$` (frees `$M$`); the big-`$M$` constant renamed
from `$\alpha$` to `$M$` (removes the `$\alpha$`/`$\alpha_s$` collision).
FLAGGED 12b: the `$p$` / `$t$` / `$K$` / `$s$` collisions — see FLAGGED.
APPLIED 12c/12d/12e: `CCEI` still unexpanded (FLAGGED); `payoff-shopping`, `trace extremity`,
`legs`, `Afriat index`, `attempt-record`, `budget-set design`, `near-1 compression`,
`survivorship`, `sanity ceiling`, `derived quantity`, `output-format contract`, `model-major`,
`multi-model-residency`, `continuous-density prices`, `headline statistic`, and the bare definite
nouns at L36/77/160/172/185/226/289/291/303/321/546/570/608/634/684/746 all named or removed.
APPLIED 12f: `by more than 2x` -> `by more than $2\times$`; `at a scale with almost none` -> the
CCEI 0.99 number; `$r\approx0.37$` -> `$r=0.37$`; `$N\approx111$--$161$` -> `$N=111$--$161$`;
`$\approx2.5\times$` -> `$2.5\times$`; `$\{10^{-2},\ldots,10^{-6}\}$` -> the explicit five-element
set; `$10^{-4}\cdot\min_t I_t$` -> `$10^{-4}\cdot I = 10^{-2}$`.

## Category 13 — numbers and internal consistency (wording/description fixes only)

APPLIED: #2 (`two of our three legs` -> `two of the four criteria`); #3 (attribution added:
`which their own evaluation reports as worse in 14 of 16 cells`); #4 (`excluded from the main
CCEI/GARP analysis but scored separately for the audit in Table 2`); #5 (`has the lowest mean CCEI
of the three (0.8821), though its GARP pass rate is measured on only 3 slots`); #6 (`the same
payoff function used everywhere else` -> `the payoff of \S...`); #7 (the false appositive replaced
by the audit's reordering: `because our baseline is already single-turn, this condition tests the
reverse`); #8/#22 (extremal expressions replaced by the constants: `any $M > 100$`, `$\gamma =
10^{-2}$`, sweep direction stated); #9 (`feasibility incumbent` dropped); #10 (both halves:
`Every cell was run to its full 30 slots`, and Table 3's caption corrected to the zero-imputation
convention + named payoff); #11 (vacuous restrictive clause dropped); #12 (`Reciprocal framing
produced no detectable drop at 1.5B` replaces the unsound comparative); #13 (`drops CCEI by
$0.241$` at both sites); #14 (`that none of the three had`, and the three named); #16 (the framing
manipulation moved out of the count; count is now three prior + ours as a fourth); #17 (final
sentence rebuilt; three-item clause deleted); #18 (`acting on the confounded estimate this paper's
control was built to separate`); #19 (`within-scale` added at both sites); #21 (`No population-
level link ... is detectable`); #24 (`does not reach significance ($p=0.0508$)`); #25 (Experiment
2's ratio $3.0\times$ now stated alongside Experiment 1's).
APPLIED 13b: #36 (`20 of 20` at both sites); #38 (`$2\times$`, no literal `x`); #39 (recast so the
Results does not open on a numeral); #40 (`8 were residual discards` recast).
SKIPPED 13b (would change printed numbers — outside the operator's wording-only remit): #26–#35,
#37, #41, #42, #43.
APPLIED 13c: comparatives given their second term where the paper has one (`at 7B`, `0.40 to
0.10`, `0.9651 against 0.9315`, `0.0118 / 0.143`, `to within 0.01`, `2.5× the pilot's estimate`).
Two remain without one — see FLAGGED (#16 in §2, §4 #53).
APPLIED 13d: all 22 subject/verb mismatches fixed (`none satisfies all four`, `mean CCEI fell
among participants`, `report the same negative outcome`, `correlated with the payoff optimum`,
`All four are ruled out`, `bears on`, `the selection effect`, `a difference`, `the reciprocal-
framing effect does not survive`, `would be acting on`, `On these five traces the sign ... matched`,
`does not account for` / `survives it`, `any $M>100$ is valid`, etc.).
FLAGGED 13a: #1, #20, #23 (see FLAGGED).

## Category 14 — structural and framing

APPLIED 14a: #1 (contributions list trimmed to what is not already stated above it; the verbatim
duplicate clause `absent from every published axiom-enforcement result we are aware of` now appears
once; conclusion's retrospective opener deleted and the verdict promoted); #2 (the two undefined
`large GARP-pass-rate collapse` merged into one, with the number); #3 (exogeneity now asserted once
in the Method plus once in the audit); #4 (five novelty disclaimers reduced to one, in Related
Work).
APPLIED 14b: #5 (the bolded cross-scale claim requalified: `The relationship holds at each scale
separately ... We do not compare its magnitude across scale.`).
APPLIED 14c: #7 (the zero-valid-rounds finding moved from the caption footnote into the body of
§sec:discard); #8 (the seven mechanistic measurements moved into the body); #9 (the verification
result given its own sentence); #10 (`GARP pass rate separates the conditions and CCEI does not` —
the `understates it` overreach removed); #11 (GPM's exclusion from the table now stated: `outside
the table because it varies the transitivity of the preference model rather than an agent's
choices`).
SKIPPED 14c: #6 (moving §sec:discard's results paragraph + Table 2 into §Results — a section-level
move beyond the wording/ordering remit).
APPLIED 14d: #12 (Broader Impacts promoted to `\section{Broader Impacts}`; the recommendation
sentence added to the Conclusion); #13 (paper now ends on its own finding); #14 (Related Work now
closes on the positive claim); #15 (Conclusion split into three paragraphs); #16 (the two
limitations split into two bolded leads).
APPLIED 14e: #17 (the Introduction's build-then-retract removed); #18 (non-convexity stated first,
concession follows); #19 (our condition stated first, citation as context); #20 (Appendix B
reordered adopted-first); #21 (forward references: pipeline caption's 50- and 94-line forward refs
removed; the 3-line `\S\ref{sec:method-nullop}` pointer deleted; the 579-line mis-scoped
`sec:method-guarantee` fixed; Figure 1's citation moved into the Experiment 1 paragraph; `$K=2$`
now given where the variable count is stated).
SKIPPED 14e: the repeated `\S\ref{sec:results-c1}` pointers in Limitations were reduced but one
per paragraph retained (as the audit allows).
APPLIED 14f: #22, #23 (the load-bearing audit number now inline), #24 (POISE's actual content
stated), #25, #26, #27 (the heading no longer advertises the reversal), #28 (`Three method
commitments, each carrying an explicit risk` -> three noun-phrase leads, no over-promise).
APPLIED 14g: #29 (Appendix A now has a verdict sentence); #30 (`any consistency instrument` ->
the bounded form); #31 (mapping fixed: the Conclusion's three confounds now read against the
paper's own vocabulary and the count error at L194 is gone); #32 (`\citep{wang2025tactics}` added
at all three uncited sites); #33 (L188 qualified with a cross-reference to Limitations; `rare in
this literature` replaced by naming the comparable paper); #34/#35 (the heading no longer bills a
contribution, so the Method/Design framings agree).
SKIPPED 14h: #36 (empty `ack` — correct for anonymized submission), #37 (float placement `[h]`->
`[t]` — layout, and the previous commit was a page-budget pass), #38 (figure widths — stylistic).

## Category 15 — spelling and convention

APPLIED: #1, #2 (`neighbour` — both sentences deleted/rewritten); #3 (`payoff-maximizing behavior`);
#5 (all seven `-ly`-adverb hyphens removed: `locally hosted`, `independently drawn` ×2,
`independently verified`, `mechanically predicted`, `globally identical`, `weakly closer`);
#6 (`multi-turn` everywhere, including both table labels); #7 (`vs.\ ` everywhere; the three
`versus` converted); #8/#9 (`post hoc` roman at all three sites); #10 (terminal periods on all bold
run-in leads); #12 (citation removed from the heading); #13 (list pattern made consistent);
#14 (`\citeauthor{nitsch2022reliability}`); #15 (`and` before the last list item); #16 (`and`
before `penalizing`); #17 (`\dots`); #18 (`check~1`); #19 (`i.i.d., rejected unless`); #20
(`app:guarantee`); #22 (`Benjamini--Hochberg` spelled out at first use, abbreviated after);
#24 (`p_t \cdot \tilde{x}_t` — manual thin-space hacks removed).
SKIPPED: #4, #11, #21 (see 12a #28), #23, #25, #26 (resolved by the §14 #12 promotion), #27–#30
(verified clean, no change needed).

## Category 16 — anything else

APPLIED 16a: all 19 reread-cost sentences rebuilt or removed.
APPLIED 16b: all 21 unclear antecedents named (including `We build that control.` — L34 rewritten to
`No published result includes a displacement-matched control`, which gives it a noun antecedent;
the four `ours` disambiguated; `the solver used` -> HiGHS).
APPLIED 16c: #1 (`independently` 20 -> 13, all load-bearing), #2 (the deletable `own`s removed;
`own choices` preserved as the defined term), #3, #4, #5, #6, #7, #8, #9, #10, #11, #12.
APPLIED 16d: all nine rhetorical `\emph{}` uses dropped; the 12 legitimate ones kept (verified by
grep — every surviving `\emph{}` is either a term introduction or a genuine contrast).
APPLIED 16e: all metaphor fixes (`sharpest vocabulary collision`, `circulated unrun`, `disposes
of`, `point the same adverse way`, `three legs`, `mirrors ... the structure of`, `secretly aimed`,
`iterating the yardstick`, `built to catch`, `sanity ceiling`, `more room to improve`, `explain
away`, `paper over`).
SKIPPED 16e: `centering` / `escape a bad start` (audit: both survive scrutiny).
APPLIED 16f: all grammar/mechanics entries, including the parallelism break at L181, `where` ->
split, the mood shift, the two sentence fragments, the triple genitive, `share-fitted` glossed, the
stranded infinitive, the multiplication that did not multiply (`2 × up to 3 × 30 = 180`) recast as
`llama3.2:3b in 2 conditions, qwen2.5:1.5b in 3, 30 replicates each`, the non-like-for-like discard
comparison, and the `we` / `this paper` exception at L598.

---

# FLAGGED FOR OPERATOR — needs the author, not a prose edit

1. **§13a #1 / §5b #1 — the `large apparent effect` contradiction (Intro, now ~L92–95).**
   Applying the audit's fix would change what the sentence claims. `produced, in the pilot, a large
   apparent effect that disappears once discard-selection is corrected` sits next to `both
   statistically indistinguishable from zero`. The only pilot CCEI number in the paper is
   `+0.0169 ($p=0.66$)`; the only large pilot number is the 52% discard rate. The author must say
   which quantity `large apparent effect` refers to. **Left exactly as written.**

2. **§13a #23 — `$r=-0.41$` printed for two different correlations (Appendix A, part 4).**
   Operator-excluded. **Left exactly as written.**

3. **§13b #41 — the MIP-gap claim's provenance (`$\le 8.1\times10^{-5}$`, Method + Appendix B).**
   Operator-excluded. The phrase is byte-identical to before at both sites; only the surrounding
   comma splice was changed to a semicolon in the appendix.

4. **§1b #32 — `and one not an LLM agent at all \citep{aguiar2026garpefm}`.** The audit's positive
   replacement (`one operating on human survey choices`) is marked "author to confirm". I applied
   only §4 #17's split, which keeps the audit's own negative wording (`is not an LLM agent and is
   evaluated on forecasting`). The positive description still needs the author.

5. **§1c #58 / §5 #32 — `The null ... does not, in general, restore consistency`.** The audit wants
   the count (`It restores consistency in <N> of the 85 traces.`). That number is not in the paper.
   Applied the hedge/negation fix only: `is not guaranteed to restore consistency`.

6. **§2 #16 — `This holds at both model scales.`** The audit wants the two per-model numbers
   substituted. They are not reported anywhere. Sentence retained with the idiom fixed
   (`at both models` -> `at both model scales`).

7. **§4 #53 / §13c — `predicts the real repair's own gain less strongly in both`.** The audit wants
   the two missing correlations. Not in the paper. Comparative promoted but still unquantified.

8. **§4 #51 / §1 #74 — the across-draw SD of `r`.** Deleted the self-contradictory clause as the
   audit directs, but could not substitute the SD the audit asks for; it is not reported.

9. **§13b #37 — `significant in 14--15 of 20`.** A count reported as a range. The audit asks which
   test gives 14 and which 15, or the threshold. Not recoverable from the text. **Left as written.**

10. **§5 #20 — `never reaches acceptable levels across eight datasets`
    (\citet{nitsch2022reliability}).** The audit wants the reliability figure from the source. Not
    available here. **Left as written.**

11. **§5c / §11 #62 — `The reported distance is stable across $\gamma \in \{...\}$`.** The audit
    calls `stable` the most load-bearing unquantified word in the paper and asks for the tolerance
    or maximum relative change. Not available. **Left as written** (the set notation was made
    explicit and the sweep direction stated).

12. **§5c — `$\ge0.80$ down to $\sim$60\% attenuation`.** Ambiguous between "attenuated to 60% of
    the pilot magnitude" and "attenuated by 60%". Rewording either way would fix the meaning of a
    power claim. **Left as written.**

13. **§12d — `CCEI` is never expanded anywhere in the manuscript.** Expanding it requires knowing
    the author's preferred expansion (Critical Cost Efficiency Index is the standard, but the paper
    never commits). One-line fix for the author.

14. **§12d — `WSCV` used unexpanded, once (Limitations).** Same issue; expanding it would be a guess.

15. **§12b — the `$p$` (price vs p-value), `$t$` (observation index vs t-statistic vs
    t-distribution), `$K$` (goods vs draws) and `$s$` (share vs $\alpha_s$ subscript) collisions.**
    Fixing `$K=20$ -> $R=20$` and `$\alpha_s -> \alpha_i$` would desynchronize the text from the
    pre-rendered figure PDFs (`fig1_dose_response.pdf`, `fig_mechanism_illustration.pdf`), which
    label the same symbols. Needs a figure regeneration alongside the text change. I did fix the two
    collisions that are text-only: prices `$M,N$ -> $p_A,p_B$` and big-`$M$` `$\alpha$ -> $M$`.

16. **§11a — one sentence describing/sizing the pilot at first use.** The paper reports 25 sessions
    for one cell only; asserting "25 sessions per cell" would generalize beyond what is stated, and
    there is no appendix to point at. The nine-way surface-form drift IS fixed (everything now reads
    `the pilot`), but the description the audit asks for needs the author.

17. **§13d L284 — `Any operator that moves a bundle toward that fixed point raises that bundle's
    payoff`.** The audit notes the universal claim is not strictly true (a bundle already at
    $s=0.5$; moving past the optimum). Bounding it would change the claim. Applied only the wording
    fix (`raises that bundle's payoff whether or not it restores GARP-consistency`).

18. **§7 #1 — the title.** The audit proposes replacing it with
    `A GARP-Blind Null Operator Outperforms Minimal GARP Repair on an Exogenous Payoff`. That is a
    framing decision, not a wording fix. I applied only §5 #1 / §6 #1: cut `Actually`. Title is now
    `What Does Repairing Choice Inconsistency Buy? \\ A Budget-Set Diagnosis`.

19. **§13b #28–#35, #42 / §13a #20 — precision and significant-figure changes** (4-s.f. proportions
    from n=7, CCEI at three precisions, dose at two precisions, p-value formats, `6 (3)` in Table
    2's n column, the degenerate llama residual-discard row footnote). All would change printed
    numbers or table cells. Out of the operator's wording-only remit. **Not applied.**

20. **§14c #6 — moving §sec:discard's results paragraph and Table 2 into §Results.** A section-level
    move, beyond the wording/ordering remit. **Not applied.**
