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
