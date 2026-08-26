# Submission checklist — EconML @ NeurIPS 2026

Everything below was verified live against the CFP page (`https://econml26-workshop.github.io/`)
and the OpenReview submission invitation (`NeurIPS.cc/2026/Workshop/EconML/-/Submission`, fetched
directly via its API) on 2026-08-26. This supersedes any prior note where the two disagree.

**Single hard deadline for everything below unless a step says otherwise:**
**August 29, 2026, Anywhere on Earth** = OpenReview `duedate` **2026-08-30 11:59 UTC**, system hard
close (`expdate`) **2026-08-30 12:29 UTC** (30-minute grace window after the stated deadline, not a
separate submission window — do not plan around it). Author notification: **September 29, 2026**.
Camera-ready and Graduating Bits dates are both listed on the CFP as **"to be announced"** — no
action possible yet; re-check the CFP page after acceptance.

---

## Already satisfied — no action needed

- [x] **Anonymization.** `\usepackage[dblblindworkshop]{neurips_2026}`, author block reads
  "Anonymous Author(s)". PDF `/Info` dict has empty Author/Title/Subject/Keywords; Producer/Creator
  are generic pdfTeX/LaTeX strings; the only non-standard key is `/PTEX.Fullbanner` (a stock
  TeX-Live version string every pdfTeX PDF carries, not identifying). `CreationDate`/`ModDate` carry
  a `+05'30'` (IST) timezone offset — a very weak, non-identifying geographic signal; not worth
  fixing but noted in case the operator wants to strip it (`TZ=UTC pdflatex ...`).
- [x] **hygiene_guard.sh** — clean (`scripts/hygiene_guard.sh` exit 0, no live leaks beyond the
  accepted baseline).
- [x] **Page limit.** Content ends at page 9 of `tex/paper.pdf`; References start page 10; checklist
  starts page 12. CFP: "References, appendices and checklist are not included in the page limit."
  This paper is a **Long paper (up to 9 pages of main text)** by content — see the track field below,
  which must still be selected explicitly on the form.
- [x] **`\workshoptitle{}`.** Set to `Economics for Machine Learning` in `tex/paper.tex:4`, alongside
  `\title{}` — both are required by the template.
- [x] **PDF file size.** `tex/paper.pdf` is 336 KB. OpenReview's `pdf` field caps uploads at **50 MB**
  — no risk.
- [x] **Code/data release.** `tex/checklist.tex`'s "Open access to data and code" item answers
  `\answerNo{}`: code and raw per-trace logs are not released with this submission; the protocol is
  fully specified in-text instead. **No anonymized GitHub/OSF/Zenodo release is required or planned.**
  Do not create one on the strength of this checklist as currently written.

---

## Remaining manual steps, in order

### 1. OpenReview profile for every author
**Requires:** an OpenReview account + completed profile for each author, created *before*
submitting. The submission form's `authors` field description states this explicitly: "All authors
must have an OpenReview profile prior to submitting a paper." This is an account-creation step the
operator must do; it is separate from the paper's double-blind anonymity (OpenReview profiles are
real-identity by design — reviewers just aren't shown who they belong to for this submission).
**Deadline:** must exist before the single Aug 29 2026 AoE deadline above; no separate deadline.

### 2. Decide the reviewer nomination, and act on it now if no author qualifies
Verbatim CFP text (unchanged since the last check — confirmed live, same wording, same
"(Updated 2026-08-12)" stamps as before): *"qualified authors may be asked to serve as reviewers...
we consider authors who have published relevant work in the main tracks of conferences such as
NeurIPS, ICML, ICLR, AAAI, EC, or WWW, either as lead authors or senior authors, to be qualified
reviewers. If none of the authors meets these criteria, please nominate the author who is best
qualified to serve as a reviewer and inform the workshop organizers before the submission deadline."*

- **Requires:** a decision (does any author qualify by that bar?), then either (a) that author's
  OpenReview profile ID entered in the form's required `serve_as_reviewer` field at submission time,
  or (b) if no author qualifies, nominate the best-qualified author in that same field **and**
  separately **email `neurips-2026-econml-workshop@googlegroups.com`** stating that no author meets
  the bar and naming who is nominated instead.
- **Deadline:** this fallback email is **not** a separate deadline from the paper's — the CFP says
  "before the submission deadline," i.e. by Aug 29 2026 AoE, same as everything else. Confirmed: this
  field has no independent `duedate` in the OpenReview invitation record itself.
- **Field is required** (`serve_as_reviewer`, order 52, not optional) — the form will not submit
  without at least one entry.

### 3. Fill the OpenReview submission form
All fields below are required unless marked optional. Have ready at submission time:
- `title` — paper title (already fixed: "What Does Repairing Choice Inconsistency Actually Buy? A
  Budget-Set Diagnosis").
- `authors` — searched/added via OpenReview profile (see step 1).
- `keywords` — comma-separated list (not yet drafted; pick from the paper's own vocabulary, e.g.
  GARP, revealed preference, LLM agents, coherence, AI alignment).
- `TLDR` — optional, one sentence.
- `abstract` — paste the paper's abstract text.
- `track` — **radio button, must select "Long paper (up to 9 pages of main text)"** explicitly; it
  is not inferred from the PDF.
- `pdf` — upload `tex/paper.pdf` (confirm it's the final recompiled build — current SHA and commit:
  see `git log -1 -- tex/paper.pdf`).
- `supplementary_material` — optional, 100 MB cap if used. Not required and not planned, per the
  checklist's `\answerNo{}` on code/data release; skip unless that decision changes.

### 4. Two mandatory consent checkboxes
- `email_sharing` — "We authorize the sharing of all author emails with Program Chairs." No
  alternative option; required to submit.
- `data_release` — "We authorize the release of our submission and author names to the public in the
  event of acceptance." No alternative option; required to submit. (This is the point at which
  anonymity ends, and only *if accepted* — not a pre-submission anonymity concern.)

### 5. Attendance confirmation
`author_attendance` — required radio, single option: confirm at least one author will attend in
Atlanta if accepted. No alternative wording exists on the form.

### 6. Submit at the portal
**URL, re-confirmed live from the CFP page's own HTML** (not from memory of the original brief):
`https://openreview.net/group?id=NeurIPS.cc/2026/Workshop/EconML`
Submit by **Aug 29 2026 AoE / Aug 30 2026 11:59 UTC**, hard system close 12:29 UTC.

---

## Not required, and do not do without separately confirming intent

- **No anonymous public code repository.** The checklist commits to not releasing code with this
  submission. Do not create a GitHub/OSF/Zenodo anonymized mirror on the assumption it's needed.
- **Awareness item, not a to-do:** this repository's `origin` remote (`pa1aash/Pref-Repair` on
  GitHub) now holds the full, non-anonymized commit history — every commit's author *and* committer
  fields are `Palaash Gang <palaashgang@gmail.com>` (`git log --format='%an <%ae> | %cn <%ce>'`).
  That repo is not referenced anywhere in the submission and does not by itself compromise
  double-blind review, but it (and the near-identical GitHub username) should not be linked, named,
  or made discoverable in connection with this submission until after the double-blind period ends.
  If code is ever released post-review, that release must come from a fresh export with reauthored
  commit metadata — not a pointer to this repo's history.
- **Camera-ready formatting instructions and Graduating Bits application** — both listed on the CFP
  as "to be announced." Nothing to do until the workshop publishes them.
