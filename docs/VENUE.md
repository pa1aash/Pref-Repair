# Venue — NeurIPS 2026 EconML workshop

## Source

| What | Value |
|---|---|
| Primary CFP page | `https://econml26-workshop.github.io/` |
| Submission portal | `https://openreview.net/group?id=NeurIPS.cc/2026/Workshop/EconML` |
| OpenReview API (deadline ground truth) | `https://api2.openreview.net/invitations?id=NeurIPS.cc/2026/Workshop/EconML/-/Submission` |
| Official workshop-acceptance announcement | `https://blog.neurips.cc/2026/08/10/announcing-the-neurips-2026-workshops/` |
| Style file archive | `https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip` |
| Checklist guidelines | `https://neurips.cc/public/guides/PaperChecklist` |
| Main Track Handbook (review process + LLM-use policy, incorporated by reference) | `https://neurips.cc/Conferences/2026/MainTrackHandbook` |

Fetched **2026-08-21**.

**Confidence this is the 2026 edition: very high.** Four independent confirmations, not one:
1. The page self-identifies as "EconML: Economics for Machine Learning / NeurIPS'26 Workshop / Atlanta, December 12 or 13, 2026".
2. The NeurIPS official blog post "Announcing the NeurIPS 2026 Workshops" (2026-08-10) lists "EconML: Economics for Machine Learning" under the **Atlanta** workshop set, and states workshop days "Sat Dec 12 and Sun Dec 13, 2026 – Paris and Atlanta" (Sydney runs Dec 11–12).
3. The OpenReview group id is literally `NeurIPS.cc/2026/Workshop/EconML`, and its live `Submission` invitation carries `cdate` 2026-08-17 13:00 UTC and `duedate` 2026-08-30 11:59 UTC — i.e. it is open right now.
4. The CFP text carries two "(Updated 2026-08-12)" edit stamps, so the page is actively maintained this month.

There is no prior-year "EconML @ NeurIPS" workshop page in play here; nothing on this page was substituted from an earlier edition.

## Dates

| Milestone | Value (verbatim from CFP) |
|---|---|
| Abstract deadline | **None.** No abstract-only deadline is listed on the CFP, and OpenReview exposes exactly one submission invitation (`/-/Submission`) with a single due date. Abstract text is a field of the single submission form. |
| Paper Submission | "August 29, 2026 (Anywhere on Earth)" |
| Author Notification | "September 29, 2026 (Anywhere on Earth)" |
| Graduating Bits Submission | "Date to be announced" |
| Camera Ready | "Date to be announced" |
| Workshop Date | "December 12 or 13, 2026" |
| Location | "Atlanta, December 12 or 13, 2026" |

**Deadline in absolute time, from the OpenReview invitation record (authoritative):**
- `cdate` (submissions open) = `1786971600000` = **2026-08-17 13:00 UTC**
- `duedate` = `1788091140000` = **2026-08-30 11:59 UTC**
- `expdate` = `1788092940000` = **2026-08-30 12:29 UTC** (a 30-minute hard-close grace window after the due date)

2026-08-30 11:59 UTC is exactly 2026-08-29 23:59 AoE, so the site text and the portal agree. As of 2026-08-21 the deadline is **8 days out**.

The exact workshop day (Dec 12 vs Dec 13) is **not yet fixed** by the organizers.

## Format and page limits

Verbatim from the "Submission Guidelines / Length" bullet:

> "Submissions will be classified into two tracks based on paper length. For long papers, the main text of a submitted paper is limited to nine (9) content pages, including all figures and tables. For short papers, the main text of a submitted paper is limited to four (4) content pages, including all figures and tables. References, appendices and checklist are not included in the page limit, but the main text must be self-contained. Reviewers are not required to read beyond the main text."

Precise reading of what counts:

| Element | Counts toward the limit? |
|---|---|
| Main text | Yes |
| Figures | **Yes** — "including all figures and tables" |
| Tables | **Yes** |
| References | **No** — "References, appendices and checklist are not included in the page limit" |
| Appendices | **No** |
| NeurIPS paper checklist | **No** |

Two riders that constrain how far the appendix can be leaned on: the main text "must be self-contained", and "Reviewers are not required to read beyond the main text."

Verbatim from the "Style" bullet:

> "Submissions must use the NeurIPS 2026 style file, include the NeurIPS paper checklist, and be submitted as a PDF. Review process will follow the NeurIPS 2026 Main Track Handbook guidelines."

Long vs short is **declared on the submission form**, not inferred. The OpenReview `track` field is a required radio with exactly two options:
- `"Short paper (up to 4 pages of main text)"`
- `"Long paper (up to 9 pages of main text)"`

Other portal-side limits: PDF upload max 50 MB; optional `supplementary_material` as a single zip/pdf/tgz/gz, max 100 MB, and "Ensure all material is anonymized."

## Template and double-blind invocation

**VERIFIED.** The style archive was downloaded, unpacked, read, and compiled in both modes.

- Archive: `Formatting_Instructions_For_NeurIPS_2026.zip`, downloaded from `https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip` (linked directly from the workshop CFP).
- Contents: `neurips_2026.sty`, `neurips_2026.tex`, `checklist.tex`.
- **Package name: `neurips_2026`.** Version banner, quoted from the file:

```
\ProvidesPackage{neurips_2026}[2026-01-29 NeurIPS 2026 submission/camera-ready style file]
```

- **Option name for this workshop: `dblblindworkshop`** (not `main`, not `preprint`, not plain no-option).

**Exact lines the CFP mandates:**

```latex
\usepackage[dblblindworkshop]{neurips_2026}
\workshoptitle{Economics for Machine Learning}
```

Verbatim CFP wording:

> "Anonymization: Submissions must be properly anonymized for double-blind review. Use `\usepackage[dblblindworkshop]{neurips_2026}` and `\workshoptitle{Economics for Machine Learning}` when importing the NeurIPS 2026 style files."

**Camera-ready line** (per the template's own instructions, `neurips_2026.tex` line 40 — camera-ready date is still TBA):

```latex
\usepackage[dblblindworkshop, final]{neurips_2026}
\workshoptitle{Economics for Machine Learning}
```

### Proof from the .sty source

Anonymity defaults to **on**, and `dblblindworkshop` is the one workshop option that does *not* turn it off:

```latex
% For anonymous or non-anonymous
\newif\if@anonymous\@anonymoustrue

% For workshop papers
\newcommand{\@workshoptitle}{}
\newcommand{\workshoptitle}[1]{\renewcommand{\@workshoptitle}{#1}}

\newif\if@workshop\@workshopfalse
\DeclareOption{sglblindworkshop}{
  \@workshoptrue
  \@anonymousfalse
  \newcommand{\@trackname}{\@neuripsordinal\ Conference on Neural Information Processing Systems (NeurIPS \@neuripsyear). Workshop: \@workshoptitle.}
}
\DeclareOption{dblblindworkshop}{
  \@workshoptrue
  \newcommand{\@trackname}{\@neuripsordinal\ Conference on Neural Information Processing Systems (NeurIPS \@neuripsyear). Workshop: \@workshoptitle.}
}
\DeclareOption{nonanonymous}{
  \@anonymousfalse
}
```

Note the asymmetry, which is the trap: `sglblindworkshop` contains `\@anonymousfalse`; `dblblindworkshop` **omits it**, so `\if@anonymous` stays true and the author block is replaced. Passing `nonanonymous` alongside it would silently de-anonymize the submission.

The `final` option is what flips to camera-ready and de-anonymizes:

```latex
% declare final option, which creates camera-ready copy
\newif\if@neuripsfinal\@neuripsfinalfalse
\DeclareOption{final}{
  \@neuripsfinaltrue
  \@anonymousfalse
}
```

The author block honours the flag:

```latex
    \if@anonymous
      \begin{tabular}[t]{c}\bf\rule{\z@}{24\p@}
        Anonymous Author(s) \\
        Affiliation \\
        Address \\
        \texttt{email} \\
      \end{tabular}%
    \else
```

And submission mode (no `final`, no `preprint`) additionally forces line numbers and a "do not distribute" footer:

```latex
    \newcommand{\@noticestring}{%
      Submitted to \@neuripsordinal\/ Conference on Neural Information Processing Systems (NeurIPS \@neuripsyear). Do not distribute.%
    }
    % hide the acknowledgements
    \NewEnviron{hide}{}
    \let\ack\hide
    \let\endack\endhide
    % line numbers for submission
    \RequirePackage{lineno}
    \linenumbers
```

### Compile check (run, not assumed)

Compiled `neurips_2026.tex` twice with `pdflatex`:

- `\usepackage[dblblindworkshop]{neurips_2026}` + `\workshoptitle{Economics for Machine Learning}` → exit 0. Page 1 renders **"Anonymous Author(s) / Affiliation / Address / email"**, line numbers are on, and the footer reads *"Submitted to 40th Conference on Neural Information Processing Systems (NeurIPS 2026). Do not distribute."*
- `\usepackage[dblblindworkshop,final]{neurips_2026}` + `\workshoptitle{...}` → exit 0. Page 1 renders the real author block, line numbers are off, and the footer reads *"40th Conference on Neural Information Processing Systems (NeurIPS 2026). Workshop: Economics for Machine Learning."*

So `\workshoptitle` has **no visible effect on the submission PDF** — its string only surfaces in the `final` footer. It is still mandated by the CFP, and the template states "both `\title{}` and `\workshoptitle{}` are required" for the workshop template, so set it regardless.

Cosmetic quirk, harmless: `neurips_2026.sty` line 107 defines `\newcommand{\@neuripslocation}{Sydney}`, which is never referenced anywhere in the file and does not print. It does not contradict the Atlanta venue.

## CFP topic bullets (verbatim)

The CFP is split into two themes plus a cross-cutting emphasis list.

**Theme 1: Economics in Training, Alignment, and Evaluation**
> "Using economic ideas to improve learning and alignment, explain the limitations of existing algorithms and paradigms, and align incentives in local economic interactions around AI systems."
>
> "Topics include, but are not limited to:"

- Preference aggregation for alignment and its limitations
- Pricing of data, training, and inference
- Social choice and auction mechanisms for steering alignment
- Strategic behavior in model evaluation, and the design of incentive-aware evaluation
- Strategic classification
- Mechanisms for eliciting high-quality data and feedback
- Discrete choice and behavioral modeling in learning pipelines
- AI decision making and bias in economic contexts
- Algorithmic collective action
- Formal abstractions of AI rationality and bias in economic contexts
- New formal models of incentive misalignment and information gaps around AI systems

**Theme 2: Ecosystems with Many Interacting Models**
> "New failure modes and economic levers that emerge when many models operate in the same environment."
>
> "Topics include, but are not limited to:"

- Competition between AI service providers
- AI supply chains and their dynamics
- Algorithmic collusion among learning systems
- Algorithmic monoculture and model multiplicity
- Market concentration among AI service providers
- Multi-agent learning dynamics in economic environments
- Pricing and evaluation of many interacting agents
- Feedback loops and performative prediction effects
- Ecosystem-level incentive design
- New formal models of emerging economic phenomena around AI systems

**Emphasis Across Both Themes**
> "We especially encourage contributions along the following directions:"

- "**Emerging domains:** Submissions that are looking to motivate an emerging topic, problem or direction. Clearly articulated motivation and a rigorous formal model that can spur interesting discussion and motivate further inquiry."
- "**Unique economic properties:** Solutions made possible by, or risks arising from, the unique properties of machine learning models and AI systems."
- "**Insights across scales:** Work spanning multiple scales, e.g. connecting micro-scale phenomena to ecosystem-level analysis, or exploring systems at "intermediate" scales."
- "**Empirical evidence:** Empirical evidence of economic phenomena, and empirical evaluation of theoretical models."

**Scope framing** (from About):
> "The workshop is organized around two complementary ways that economics and machine learning can inform one another:"
> - "Economic Tools for Machine Learning: How can economic ideas improve learning and alignment, reveal the limitations of existing algorithms and paradigms, and align incentives in local interactions around AI systems?"
> - "Machine Learning Ecosystems with Interacting Models: What economic phenomena emerge when many models interact in shared environments, and how can interventions improve ecosystem-level outcomes?"

## Review obligations

Yes — submitting carries a reviewing obligation, and it is enforced at the form level.

Verbatim:
> "Reciprocal review: To ensure adequate reviewing coverage, qualified authors may be asked to serve as reviewers for the workshop. The submission form includes a reciprocal reviewing clause. In general, we consider authors who have published relevant work in the main tracks of conferences such as NeurIPS, ICML, ICLR, AAAI, EC, or WWW, either as lead authors or senior authors, to be qualified reviewers. If none of the authors meets these criteria, please nominate the author who is best qualified to serve as a reviewer and inform the workshop organizers before the submission deadline."

The OpenReview submission form carries a required `serve_as_reviewer` field:
> "Enter the profile IDs of the authors of this submission who will serve as reviewers. **At least one qualified author must be nominated.** Please see the Call for Papers submission instructions for details on reviewer eligibility requirements."

Practical consequences:
- **At least one author must be nominated as a reviewer at submission time** — this is not optional and blocks the form otherwise.
- The nominee is selected from the paper's own author list (the field enumerates author usernames).
- If **no** author meets the eligibility bar, the CFP requires nominating the best-qualified author **and emailing the organizers before the deadline** — i.e. this is an action item that must happen on or before 2026-08-29 AoE, not after.
- **The number of papers a nominated reviewer will be assigned is not stated** anywhere on the CFP or the form. See Gaps.

Related, and easy to trip over:
> "Organizers conflicts of interest: In alignment with the NeurIPS workshop organization guidelines, current students, postdocs, or hosts of organizers should not submit papers to the workshop. In addition, an organizer will not be involved in assessing a submission from someone within the same organization. (Updated 2026-08-12)"

Listed organizers: Safwan Hossain (Harvard), Meena Jagadeesan (UPenn), Eric Mazumdar (Caltech), Ariel Procaccia (Harvard), Eden Saig (Caltech), Kunhe Yang (UC Berkeley).

Review process is inherited: "Review process will follow the NeurIPS 2026 Main Track Handbook guidelines."

## Checklist requirements

**Yes, there is a checklist, and it is mandatory.**

- CFP: "Submissions must use the NeurIPS 2026 style file, **include the NeurIPS paper checklist**, and be submitted as a PDF."
- It ships as `checklist.tex` inside the style archive.
- **It does not count toward the page limit.** CFP: "References, appendices and checklist are not included in the page limit". `checklist.tex`: "The checklist does NOT count towards the page limit."
- **Omitting it is a desk reject.** `checklist.tex`, verbatim: "Do not remove the checklist: **The papers not including the checklist will be desk rejected.**" The NeurIPS checklist guidelines page repeats this word for word.
- Ordering inside the single PDF, from the checklist guidelines: "in a single PDF file include, in this order, (1) the submitted paper; (2) optional technical appendices that support the paper with additional proofs, derivations, or results; (3) the NeurIPS paper checklist."
- Every question needs an answer of `\answerYes{}` / `\answerNo{}` / `\answerNA{}` plus "a short (1--2 sentence) justification right after your answer (even for \answerNA)".
- The instruction block must be stripped but the structure kept: "Delete this instruction block, but keep the section heading ``NeurIPS Paper Checklist''", "Keep the checklist subsection headings, questions/answers and guidelines below", "Do not modify the questions and only use the provided macros for your answers".
- Answers are reviewer-visible and are graded: "The checklist answers are an integral part of your paper submission." "The reviewers of your paper will be asked to use the checklist as one of the factors in their evaluation." A `\answerNo{}` with a proper justification is explicitly not grounds for rejection.

## Dual submission and prior-workshop rules

Verbatim:
> "Submission to multiple venues: We will also accept papers that are under review at the time of submission, or that have been recently accepted, provided they do not breach any dual-submission policies of those venues. We discourage dual submissions within NeurIPS 2026 itself - to multiple NeurIPS workshops, or concurrently to this workshop and the NeurIPS 2026 main track. Extended abstracts of papers under review at other conferences/journals can be submitted if this is ok for the conference/journal in question (if in doubt, please check with them first). (Updated 2026-08-12)"

Breakdown:
- Work **under review elsewhere**: allowed, subject to the other venue's own policy.
- Work **recently accepted** elsewhere: allowed, same caveat.
- **Extended abstracts** of papers under review elsewhere: allowed, "if this is ok for the conference/journal in question".
- **Within NeurIPS 2026**: "discouraged" — both multi-workshop submission and workshop-plus-main-track. Discouraged, not prohibited.
- **Prior-workshop presentation:** the CFP contains **no explicit rule** about work already presented at a previous workshop. The only text touching prior status is "recently accepted", which is about acceptance at a reviewed venue, not about prior workshop presentation. See Gaps — do not read this as permission.

Also incorporated by reference:
> "LLM use: We follow the NeurIPS 2026 Main Track Handbook policy on LLM use."

## Archival status and attendance

- **Non-archival.** Verbatim: "Non-archival: Accepted contributions will not appear in formal proceedings."
- **In-person attendance is required.** Verbatim: "In-person attendance: All accepted papers are required to have at least one author present the paper in-person in Atlanta."
- This is enforced at submission: the OpenReview form has a required `author_attendance` radio whose only selectable value is "We confirm that at least one author will attend the conference in Atlanta to present the work if the submission is accepted."
- **Presentation format:** "Posters and spotlight presentations: Accepted papers will be presented as posters, and may also be invited to give a spotlight presentation."
- **Author names become public:** the form's `data_release` field confirms "accepted submissions, along with their author names, will be released to the public after the conference is over."
- Separate, non-paper track exists: "Graduating Bits", a 5-minute lightning-talk session; "Participation does not require a submission to the workshop"; "Presentations will be given in-person in Atlanta." Application form "Coming soon!".

## Discrepancies against the planning brief's transcription

Brief under audit: `docs/F3-PLAN-ORIGINAL.md`, header table row "Deadline / format" and "Target venue".

| What the brief says | What the live CFP says | Material? |
|---|---|---|
| Deadline "**Aug 29 2026 AoE**" | "August 29, 2026 (Anywhere on Earth)"; OpenReview `duedate` 2026-08-30 11:59 UTC (= Aug 29 23:59 AoE), hard close 12:29 UTC | **No — accurate.** Confirmed against the portal, not just the page. |
| "long 9pp / short 4pp *content* pages" | "nine (9) content pages" long, "four (4) content pages" short | **No — accurate**, including the word "content". |
| "(figures+tables count)" | "including all figures and tables" | **No — accurate**, as far as it goes. |
| *(silent on references / appendices / checklist)* | "References, appendices and checklist are not included in the page limit, but the main text must be self-contained. Reviewers are not required to read beyond the main text." | **Yes — MISSING, and it cuts in the paper's favour.** An unbounded appendix is available for the LP/MILP formalism, the CCEI/Afriat background, and per-seed distributions, which changes what has to be squeezed into 9 pages. The two riders (self-contained main text; reviewers need not read past it) bound how much can be deferred. |
| "double-blind" | "Submissions must be properly anonymized for double-blind review." | **No — accurate.** |
| "non-archival" | "Accepted contributions will not appear in formal proceedings." | **No — accurate.** |
| "in-person attendance required" | "at least one author present the paper in-person in Atlanta"; enforced by a required form field | **No — accurate.** |
| "NeurIPS 2026 **EconML** (Atlanta)" | "EconML: Economics for Machine Learning", "Atlanta, December 12 or 13, 2026" | **No — accurate.** |
| Named CFP bullet: "**formal abstractions of AI rationality and bias**" | Actual bullet: "Formal abstractions of AI rationality and bias **in economic contexts**" | **Yes — STALE/TRUNCATED quote.** The bullet exists and is real, but the brief drops the qualifier "in economic contexts". The full bullet is narrower than the truncation implies, and the framing must land the work in an *economic* setting (budget sets, prices, income — which this project does have) rather than generic LLM rationality. Also note a sibling bullet the brief never mentions: "AI decision making and bias in economic contexts". |
| *(silent on notification and workshop dates)* | Notification "September 29, 2026 (Anywhere on Earth)"; workshop "December 12 or 13, 2026" | **Yes — MISSING.** Downstream scheduling (camera-ready, travel, the in-person commitment) has no dates in the brief. |
| *(silent on reviewing obligation)* | "Reciprocal review" — at least one qualified author **must** be nominated on the form; if no author qualifies, organizers must be emailed **before the deadline** | **Yes — MISSING and time-critical.** This is a pre-deadline action item, 8 days out. |
| *(silent on the checklist)* | NeurIPS paper checklist is **required**; "papers not including the checklist will be desk rejected"; does not count toward pages; must be last in the PDF | **Yes — MISSING and desk-reject-grade.** |
| *(silent on how to invoke double-blind)* | `\usepackage[dblblindworkshop]{neurips_2026}` plus `\workshoptitle{Economics for Machine Learning}` | **Yes — MISSING.** Not the default no-option `\usepackage{neurips_2026}`, and the sibling option `sglblindworkshop` silently de-anonymizes. |
| *(silent on dual submission)* | Under-review and recently-accepted work is accepted; dual submission *within* NeurIPS 2026 is discouraged | **Yes — MISSING**, and permissive in the project's favour. |
| *(silent on organizer COI)* | Students, postdocs, or hosts of the six named organizers should not submit | **Yes — MISSING.** Cheap to check against the author list. |
| Backup venue: "Any NeurIPS 2026 agent-evaluation workshop" | Not verified in this pass — out of scope | Not assessed here. |

Net: **the brief's header table is factually correct on every item it states.** Its failures are omissions, not errors, plus one truncated quotation. The two omissions that could cost the submission outright are the mandatory checklist (desk reject) and the mandatory reviewer nomination (blocks the form). The omission that most changes the writing plan is that references, appendices and checklist sit outside the 9-page count.

## Gaps

Unverified or unavailable as of 2026-08-21. **None of these are filled with a guess or with a prior-year value.**

- **Camera-ready deadline — UNKNOWN.** CFP literally reads "Date to be announced".
- **Graduating Bits deadline — UNKNOWN.** "Date to be announced"; the application form reads "Coming soon!".
- **Exact workshop day — UNRESOLVED BY THE ORGANIZERS.** "December 12 or 13, 2026". The NeurIPS blog confirms the Atlanta workshop block is Dec 12–13 but does not pin this workshop to one day.
- **Reviewer workload — NOT STATED.** The CFP mandates nominating at least one reviewer but never says how many papers that reviewer will be assigned, nor the review window (which must fall between 2026-08-29 and the 2026-09-29 notification). Not stated on the CFP, not stated in the OpenReview form fields, and no reviewer invitation exists in the portal yet.
- **Prior-workshop-presentation policy — NOT ADDRESSED.** The CFP covers under-review, recently-accepted, and extended-abstract cases, and discourages intra-NeurIPS-2026 duplication. It says nothing about work already presented at a *previous* workshop. Treat as unanswered; email `neurips-2026-econml-workshop@googlegroups.com` if it becomes relevant.
- **Acceptance rate / expected volume — NOT PUBLISHED.** No first-edition statistics exist.
- **Whether spotlight selection has separate criteria — NOT STATED.** Only "may also be invited to give a spotlight presentation."
- **Schedule — NOT PUBLISHED.** "Schedule details to be announced."
- **Whether the organizers will treat the 12:29 UTC `expdate` as a real grace period — UNKNOWN.** It is present in the invitation record; it is not documented as a policy anywhere. Do not plan against it.
- **LLM-use policy specifics — NOT READ IN THIS PASS.** The CFP delegates to the NeurIPS 2026 Main Track Handbook; the handbook text itself was not retrieved here.

## Fit audit

Written after Phases C–E. The venue is **locked by standing instruction**, so this audit informs
*how to reframe*, not *whether to switch*.

### Scoring F3 as currently scoped against each CFP bullet

Scale: **direct** (the bullet names this work) / **adjacent** (a reframe lands it) / **no**.

**Theme 1 — Economics in Training, Alignment, and Evaluation**

| Bullet | Fit | Why |
|---|---|---|
| Formal abstractions of AI rationality and bias **in economic contexts** | **direct** | GARP/Afriat over budget sets with prices and income is exactly a formal abstraction of rationality in an economic context. The qualifier the brief truncated is satisfied, not violated — this project has real budget constraints, which most "LLM rationality" work does not. |
| AI decision making and bias in economic contexts | **direct** | The downstream-payoff half of the work is literally this. The brief never targeted this bullet; it is at least as good a landing spot as the one it did target. |
| Preference aggregation for alignment **and its limitations** | **adjacent, and newly important** | The closest published neighbour (HAR 2025) solves repair *as an aggregation problem* using social-choice machinery. A reframe that positions repair-vs-aggregation as the same problem in two vocabularies lands here squarely — and "and its limitations" is where the coherence-costs-quality evidence goes. |
| Social choice and auction mechanisms for steering alignment | **adjacent** | Only if the projection is presented alongside voting-rule repair as an alternative operator. Viable but not the strongest framing. |
| Discrete choice and behavioral modeling in learning pipelines | **adjacent** | Fits the elicitation half; weak on its own. |
| Mechanisms for eliciting high-quality data and feedback | **no** | Not what this does. |
| Strategic behavior in model evaluation / strategic classification / pricing / algorithmic collective action | **no** | No contact. |

**Theme 2 — Ecosystems with Many Interacting Models:** **no fit on any bullet.** Single-agent
work. Do not attempt to stretch it; a strained Theme-2 framing would read as padding.

**Emphasis directions**

| Emphasis | Fit | Why |
|---|---|---|
| **Empirical evidence** — "empirical evaluation of theoretical models" | **direct, and this is the strongest card** | Andrews (arXiv:2608.05015) is 25 pages of theory with zero experiments, and it is six months old and circulating in this exact community. "Empirical evaluation of theoretical models" describes the relationship between this paper and that one precisely. |
| **Unique economic properties** | **adjacent** | The argument would be that budget-set revealed preference gives a *graded, cardinal* consistency measure (CCEI) that the ML front's binary cycle-counting does not. That is a real economic property and a real contribution. |
| **Insights across scales** | **adjacent** | Only under the reframe below, connecting a per-choice repair operator to task-level outcomes. |
| **Emerging domains** — "motivate an emerging topic… spur further inquiry" | **damaged** | This was the brief's implicit pitch, and Phase E removed its basis. The topic is not emerging and not unclaimed: it has an ICML'25 paper, an ICML'26 paper, a *Philosophical Studies* article, and at least three deployed repair systems. Pitching it as emerging invites a reviewer who knows that literature to reject on prior art. |

### Verdict

**The venue fit is good. The current framing is strained, and needs a specific named reframe.**

Two things are true at once and the brief conflates them. The *venue* is close to ideal — two topic
bullets are direct hits, the empirical-evidence emphasis describes the Andrews relationship exactly,
and the unbounded appendix absorbs the LP/MILP formalism that would otherwise eat the page budget.
But the *framing* — "everyone measures, nobody repairs; we repair first" — is the one thing Phase C
and Phase E jointly falsified. Submitting on that framing to a workshop whose organizers work on
preference aggregation and social choice is submitting into the teeth of the reviewers most likely
to know the counter-evidence.

### The named reframe

**From** "Repairing, Not Just Measuring, LLM Preference Inconsistency" — a priority claim.

**To** *"What Does Repairing Choice Inconsistency Actually Buy? A Budget-Set Diagnosis"* — a
**dose–response and diagnosis** claim. Four moves make it work:

1. **Concede the operator immediately and completely.** Repair exists — as a voting rule (HAR 2025),
   as rank fusion (arXiv:2406.00231), as judge calibration (arXiv:2509.21117), as a training penalty
   (arXiv:2608.05015), as fine-tuning on rationalizable data (arXiv:2603.23993). Say so in the
   introduction, before a reviewer does. This is the brief's own S7 advice, applied harder than the
   brief anticipated it would need to be.
2. **Claim the measurement instrument, not the operator.** What the ML front does not have is a
   *graded* consistency measure over a real budget constraint. Cycle-counting is binary; CCEI is
   cardinal and has a 90-year interpretation. That is the economics contribution, and it is what
   makes a **dose–response curve** possible where the ML papers only have on/off ablations.
3. **Move to an exogenous payoff.** Every occupied result scores repair on a *preference-derived*
   metric — win rates, NDCG, judge agreement. The genuinely unoccupied cell is repair scored against
   a payoff that does not come from the preference data at all. That is the paper.
4. **Report Bronars power beside every CCEI, and switch the S4 lever from persona to framing.**
   Both are Phase E findings (`audit/BRONARS_NOTE.md`, `audit/killcheck_E3.md`), both are cheap,
   and the second is the difference between a gate built on one shaky citation and a gate built on
   the PNAS paper's own within-paper manipulation.

Under that reframe the target bullet becomes **"Preference aggregation for alignment and its
limitations"** with **"Formal abstractions of AI rationality and bias in economic contexts"** as the
secondary, and the emphasis card played is **Empirical evidence**, not Emerging domains.

### Time-critical actions, independent of the reframe

The deadline is **8 days out** and three of these are blocking, not cosmetic:

1. **Nominate a reviewer on the OpenReview form.** Required field. If no author has published in a
   NeurIPS/ICML/ICLR/AAAI/EC/WWW main track, the organizers must be emailed **before** the deadline.
2. **Include the NeurIPS checklist.** Its absence is an explicit desk reject. Ships as
   `checklist.tex` in the style zip; goes last; does not count toward pages.
3. **Use `\usepackage[dblblindworkshop]{neurips_2026}` with `\workshoptitle{Economics for Machine Learning}`.**
   The sibling option `sglblindworkshop` de-anonymizes silently, with no error.
4. Check the author list against the organizer COI rule (Hossain, Jagadeesan, Mazumdar, Procaccia,
   Saig, Yang).
5. Decide long (9 pp) vs short (4 pp) — it is a radio button on the form, not inferred from the PDF.
