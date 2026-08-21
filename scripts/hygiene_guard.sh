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
# BASELINE: scripts/hygiene_baseline.txt lists SHA-256 hashes of history lines that have been
# reviewed and accepted as public. Those suppress HISTORY hits only. Content, path and identity
# hits are never suppressible — a leak in a tracked file always fails. See docs/DECISIONS.md D13.
#
# Exit 0 = clean (or clean modulo the documented baseline). Exit 1 = at least one live leak.

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
# History hits are checked against the documented baseline. A hit whose hash is listed there is
# reported as ACCEPTED and does not fail the run; anything else is a live leak.
BASELINE_FILE="scripts/hygiene_baseline.txt"
ACCEPTED=0
if git rev-parse HEAD >/dev/null 2>&1; then
  hist=$(git log --all -p --format='commit %H%nauthor %an <%ae>%ncommitter %cn <%ce>%n%B' \
         | grep -n -i -E "$RE" || true)
  if [ -n "$hist" ]; then
    while IFS= read -r line; do
      content=${line#*:}                      # strip grep's line number
      content=${content#[+-]}                 # strip the diff marker
      h=$(printf '%s' "$content" | shasum -a 256 | cut -c1-32)
      if [ -f "$BASELINE_FILE" ] && grep -q "^$h  " "$BASELINE_FILE" 2>/dev/null; then
        ACCEPTED=$((ACCEPTED + 1))
      else
        report "history" "$line"
      fi
    done <<<"$hist"
  fi
fi

# --- 2 + 3. file contents: tracked, plus untracked-and-not-ignored -------------------
{ git ls-files -z; git ls-files -z --others --exclude-standard; } \
  | while IFS= read -r -d '' f; do
      [ -f "$f" ] || continue
      [ "$f" = "scripts/hygiene_guard.sh" ] && continue
      [ "$f" = "scripts/hygiene_baseline.txt" ] && continue
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

# --- 6. stale-baseline check --------------------------------------------------------
# A baseline entry that no longer matches anything is dead weight and should be deleted.
if [ -f "$BASELINE_FILE" ]; then
  n_entries=$(grep -c '^[0-9a-f]\{32\}  ' "$BASELINE_FILE" 2>/dev/null || echo 0)
  if [ "$ACCEPTED" -eq 0 ] && [ "$n_entries" -gt 0 ]; then
    echo "hygiene_guard: NOTE — $n_entries baseline entries, none matched. They may be stale; consider pruning $BASELINE_FILE."
  fi
fi

if [ "$FOUND" -ne 0 ]; then
  echo
  echo "hygiene_guard: FAILED — see matches above."
  [ "$ACCEPTED" -gt 0 ] && echo "hygiene_guard: ($ACCEPTED further history match(es) suppressed by the documented baseline.)"
  exit 1
fi
if [ "$ACCEPTED" -gt 0 ]; then
  echo "hygiene_guard: clean — $ACCEPTED history match(es) accepted per $BASELINE_FILE; no live leaks."
else
  echo "hygiene_guard: clean (history, tracked + untracked-unignored files, paths, identity)."
fi
exit 0
