# Decision log

Running log of choices made and why. Newest entries appended at the bottom.
Each entry: date, decision, reason, and what would reverse it.

---

## 2026-08-21 — Session G0 (repo genesis + characterisation)

**D1. Home directory `~/.git` deleted.**
The home directory was itself a git repository with this project nested inside it. Verified 0
commits, 0 refs, 0 remotes, empty index before deletion; the 571 MB of loose objects were
unreachable. Reversal: none — the objects are gone. Nothing reachable was lost.

**D2. Commit/PR attribution suppressed at user scope.**
Set `attribution: {commit: "", pr: "", commitTrailers: false, sessionUrl: false}` in the
agent harness user settings. The older `includeCoAuthoredBy` flag is deprecated in the
installed build and is set to `false` alongside it for belt-and-braces. Verified end to end
by making a commit in a throwaway repo and inspecting the raw commit object. Reversal: unset
those keys.

**D3. Remote reached over SSH port 443, not 22.**
Port 22 to github.com times out on this network. A repo-local `url.insteadOf` rewrite routes
`git@github.com:` through `ssh://git@ssh.github.com:443/`. This is repo-local by choice so no
user-global SSH config was touched. Reversal: `git config --local --unset-all
url."ssh://git@ssh.github.com:443/".insteadOf`.

**D4. Hygiene guard scope is "anything that could become public", not the literal filesystem.**
The guard scans commit history (messages, diffs, author/committer metadata), all tracked
files, and all untracked-but-not-ignored files. Ignored trees (`.venv/`, `research/`,
`.hyperresearch/`, `.remember/`) are out of scope because they cannot be published by
definition, and `research/` will routinely contain vendor names from fetched sources — a
guard that is permanently red is a guard nobody runs. The guard's own patterns are
bracket-escaped (`cl[a]ude`) so it never matches itself. Verified with a positive-control
test that planted one string per pattern class and confirmed all six were caught.

**D5. The planning brief is treated as immutable input.**
`docs/F3-PLAN-ORIGINAL.md` is chmod `a-w` and its sha256 is recorded. Everything this session
produces is *about* that file, never *in* it. Reversal: none wanted.

**D6. The repository is public.**
Confirmed by unauthenticated HTTP 200 on the GitHub URL. The planning brief — including the
prior-art verdict and venue strategy — is world-readable as of this session. Flagged rather
than decided: if that is unwanted, the repo must be flipped to private before the next push.

---

## 2026-08-21 — Session G0, Phase C/E outcome

**D7. The session's STOP CONDITION fired. The pipeline was halted at step 2.**

The calling brief set this condition: *if the calibrated instrument finds the exact intervention
— correction / projection / repair / enforcement of revealed-preference consistency on LLM agent
choices — already published, stop, and do not write any further characterisation implying
novelty.*

It is published, by at least three independent groups, and none of them was in the plan's
reference list:

| Work | Venue | What it does |
|---|---|---|
| Chadwick, Kahng & Kipper (2025) | HAR 2025, Paris (not arXiv) | An inference-time "rationality layer" that repairs an LLM's intransitive preferences via a voting rule and projects its incoherent probabilities onto the coherent set via a quadratic program, under an explicit faithfulness constraint |
| LLM-RankFusion (arXiv:2406.00231) | — | Repairs order and transitivity inconsistency in an LLM's own pairwise judgments **at inference time**, and improves NDCG@10 (65.38 → 71.51 in one setting) |
| TrustJudge (arXiv:2509.21117) | — | Cuts transitivity inconsistency from 15.22% to 4.40% while maintaining evaluation accuracy |

And the second half — whether enforced coherence changes downstream quality — has been tested
repeatedly, in both directions, at ICML 2025 and ICML 2026 and in a 2026 agent paper that
deliberately breaks a coherence axiom and gains +11%/+18% task usefulness.

**Why the condition is treated as fired even though no paper does the exact GARP-over-budget-sets
version.** The plan's novelty rests on two sentences: "the field measures; it does not intervene",
and "a clean negative on coherence-vs-competence is a publishable and more interesting result".
The first is false. The second is substantially false — both signs have precedent, so the risk
asymmetry that made this "the safest bet in the batch" is gone. Waiting for a paper that matches
on every detail before acknowledging that would be motivated reasoning: the reviewer who knows
this literature will not care that the axiom system differs.

**What was NOT concluded.** The project is not dead, and this session does not have the standing
to declare it so. A narrow cell is genuinely unoccupied — projecting an *agent's own choice
sequence* onto the rationalizable set and scoring it against an **exogenous, non-preference
payoff**, with a dose–response curve rather than a single on/off comparison. Nobody has done
that. Whether that cell is worth a workshop paper eight days before a deadline is a judgement for
the principal investigator, not for an audit session.

**Reversal:** if a careful re-read of the three systems above shows they are further from the
proposal than the summaries suggest, C3 could be partially restored. The full texts are in the
vault and in `audit/`. Nothing was discarded.

**D8. The hyperresearch run was stopped after step 2 rather than run to step 16.**
Steps 3–16 exist to settle a novelty question that Phases C and E had already settled by the time
step 2's fetchers were dispatched. Running roughly two more hours of loci analysis, depth
investigation, triple-drafting and adversarial critique to re-derive a conclusion already in hand
would have been process theatre. Wave 1 was allowed to complete because the corpus itself is the
useful artefact — it is the prior-art reading list the paper now needs. Everything under
`research/` is gitignored, so the partial output was copied to `audit/HR_PARTIAL/`.

**D9. The agent-harness directory and its generated root markdown file are excluded via
wildcard-escaped ignore rules (`.?laude/`, `?LAUDE.md`).** Git's bracket character classes did not
match under `core.ignorecase`, so `?` is used instead. A rule spelling the name out literally would
itself be the vendor string the hygiene guard exists to catch — which is exactly what the guard
caught when it was first tried. Verified with `git check-ignore`.

---

## 2026-08-21 — Session G0, end-of-session decisions (taken by the principal investigator)

**D10. Push with the hygiene guard failing on its history scan.**
Asked and answered directly. The guard's working-tree, path and identity scans are clean; only its
history scan fails, on three strings introduced during this session — a machine-absolute home path
in an early version of this file, and a vendor filename inside the guard's own header comment.
Clearing them requires rewriting published history and force-pushing, which was offered and
declined. The calling brief said not to push with the guard failing; that instruction is
**explicitly overridden** by this decision, and it is recorded here rather than quietly followed.

Consequence to carry forward: **`scripts/hygiene_guard.sh` now exits 1 by design.** A guard that
always fails is a guard people stop reading, so the next session should either perform the rewrite
or add a documented baseline of known-accepted history hits. Do not "fix" it by narrowing the scan.

**D11. The repository stays public.**
Also asked and answered. `docs/F3-PLAN-ORIGINAL.md` is world-readable, including the prior-art
verdict, the venue strategy, and the line assessing a named researcher's paper as a scoop risk,
during a double-blind review cycle that closes in eight days. The deanonymisation risk was raised
and accepted. Nothing in the repository breaks anonymity mechanically.

**D12. A copyrighted full-text source dump was caught before it reached the public remote.**
A width-sweep fetcher wrote a 59 KB PDF text extraction — the complete text of arXiv:2608.05015 —
into the repository root rather than into the gitignored vault, and a `git add -A` staged it. It
was committed locally, but the commit had not been pushed. `scripts/hygiene_guard.sh` caught it on
its content scan (the paper's acknowledgements name AI assistants, which matched a guard pattern),
the two unpushed commits were rewound with `git reset --soft`, the file was moved into
`research/notes/` where the fetcher should have put it, and the work was re-committed without it.

Two things worth carrying forward. First, **the guard earned its keep** — it caught a
copyright-and-publication problem it was not written to look for, via a pattern aimed at something
else entirely. Second, **`git add -A` is not safe in this repository** while agents are writing
files concurrently; stage explicit paths instead. This is also the strongest argument for keeping
the guard exiting 0 in normal operation (see D10): had it already been red, this would have been
lost in the noise.

---

## 2026-08-21 — Session G0.5 (closeout)

**D13. The guard's permanent-red state is resolved with a documented baseline, NOT a history
rewrite. This CLOSES D10. No force-push was performed and none is needed.**

D10 left `scripts/hygiene_guard.sh` exiting 1 on six history matches, and flagged that a
permanently-red guard is one people stop reading. Two options were on the table: a documented
baseline of accepted history hits, or a `filter-repo` rewrite purging the strings and a
force-push.

**Chosen: the baseline.** The reasoning turns on the fact that the repository is public, which
cuts the *opposite* way to intuition:

1. **A force-push does not actually purge a public repository.** Rewritten-away objects remain
   reachable on the forge by their old SHA until garbage collection, which is not guaranteed or
   scheduled on demand; forks, caches and any existing clone retain them regardless. A rewrite
   would deliver the *appearance* of removal without the substance — the worst outcome, because
   it would also retire the record of what happened.
2. **A rewrite is irreversible and outward-facing; the baseline is neither.** It breaks every
   existing clone and rewrites 17 published commit SHAs, to remove a machine home path and a
   filename.
3. **The content does not warrant it.** Three distinct strings: a home-directory path that
   discloses an OS account name already visible in the repository owner's public profile, and a
   generated filename naming a tool vendor. No credential, no token, no ORCID, no non-public
   email, no third-party copyrighted text. The one item in this session's history that *would*
   have warranted a rewrite — a 59 KB full-text dump of a copyrighted paper — was caught before
   it was pushed (D12) and is not in history at all.
4. **The principal investigator already declined the rewrite once**, in D10, on the same facts.

**Mechanism.** `scripts/hygiene_baseline.txt` lists the truncated SHA-256 of each accepted
history line with a one-line justification. Hashes rather than literal strings, deliberately: a
baseline file spelling the text out would re-introduce into the working tree precisely what the
guard exists to keep out of it — the failure mode that caught this repository twice already.

**The suppression is narrow by construction, and that was verified rather than assumed:**

- Baseline entries suppress **history** hits only. Content, path and identity hits are never
  suppressible. Confirmed: planting a file containing an ORCID and a co-author trailer still
  fails the run.
- An un-baselined history hit still fails. Confirmed by removing one entry and re-running — the
  guard failed on exactly that string and no other.
- A wrong or stale hash surfaces the hit rather than silently passing. Confirmed.
- Suppressed matches are **counted and reported on every run**, pass or fail, so the baseline can
  never quietly grow without someone seeing the number move.

**Standing rule.** Adding a baseline entry is a decision, not a chore: it asserts "this string is
public, we looked at it, and we accept it." Anything carrying a credential, a personal identifier,
or third-party copyrighted text is purged, never baselined. That rule is written into the head of
the baseline file, where the next person to hit a red guard will actually read it.
