#!/usr/bin/env bash
#
# hygiene_guard.sh — pre-publication leak check for the Pref-Repair repository.
#
# Scans everything that could become public if this repo were pushed:
#   1. the full commit history, including diffs and commit metadata (git log --all -p)
#   2. every tracked file's contents
#   3. every untracked-but-not-ignored file (i.e. anything one `git add .` from being public)
#   4. tracked path names and author/committer identity fields
#
# Ignored files (.venv/, research/, .hyperresearch/, .remember/, ?LAUDE.md) are deliberately
# out of scope: they are excluded from git by .gitignore and therefore cannot be published.
#
# Patterns are written with bracket escapes (e.g. cl[a]ude) so that this script never
# matches itself. The escapes are regex no-ops; the patterns match the real strings.
#
# Exit 0 = clean. Exit 1 = at least one leak found (all matches are printed).

set -uo pipefail

cd "$(git rev-parse --show-toplevel)" || { echo "not inside a git repository" >&2; exit 2; }

PATTERNS=(
  'cl[a]ude'
  'anthrop[i]c'
  'co-authored[-]by'
  'generated[ ]with'
  '0009-0006-7448-948[8]'
  'palaash[.]gang@indusschoolpune[.]com'
  '/Users/pal[a]ash'
)
RE=$(IFS='|'; echo "${PATTERNS[*]}")

FOUND=0
report() { FOUND=1; echo "LEAK [$1] $2"; }

# --- 1. commit history: messages, diffs, and metadata --------------------------------
if git rev-parse HEAD >/dev/null 2>&1; then
  hist=$(git log --all -p --format='commit %H%nauthor %an <%ae>%ncommitter %cn <%ce>%n%B' \
         | grep -n -i -E "$RE" || true)
  [ -n "$hist" ] && while IFS= read -r line; do report "history" "$line"; done <<<"$hist"
fi

# --- 2 + 3. file contents: tracked, plus untracked-and-not-ignored -------------------
{ git ls-files -z; git ls-files -z --others --exclude-standard; } \
  | while IFS= read -r -d '' f; do
      [ -f "$f" ] || continue
      [ "$f" = "scripts/hygiene_guard.sh" ] && continue
      grep -n -i -E -a "$RE" -- "$f" 2>/dev/null \
        | sed "s|^|$f:|" || true
    done > /tmp/hygiene_content_hits.$$ 2>/dev/null
if [ -s /tmp/hygiene_content_hits.$$ ]; then
  while IFS= read -r line; do report "content" "$line"; done < /tmp/hygiene_content_hits.$$
fi
rm -f /tmp/hygiene_content_hits.$$

# --- 4. path names ------------------------------------------------------------------
paths=$({ git ls-files; git ls-files --others --exclude-standard; } | grep -i -E "$RE" || true)
[ -n "$paths" ] && while IFS= read -r line; do report "path" "$line"; done <<<"$paths"

# --- 5. configured identity for this repo -------------------------------------------
ident="$(git config --local user.name || true) <$(git config --local user.email || true)>"
echo "$ident" | grep -i -E "$RE" >/dev/null && report "identity" "$ident"

if [ "$FOUND" -ne 0 ]; then
  echo
  echo "hygiene_guard: FAILED — see matches above."
  exit 1
fi
echo "hygiene_guard: clean (history, tracked + untracked-unignored files, paths, identity)."
exit 0
