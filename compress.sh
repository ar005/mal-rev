#!/usr/bin/env bash
# compress.sh — archive the repo into a timestamped tarball in this folder.
# Reads .gitignore and converts each pattern to a tar --exclude flag.
# Usage: ./compress.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
ARCHIVE="$REPO_ROOT/re_${TIMESTAMP}.tar.gz"
GITIGNORE="$REPO_ROOT/.gitignore"

echo "Compressing: $REPO_ROOT"
echo "Output:      $ARCHIVE"
echo ""

# Build exclude flags from .gitignore (skip blank lines and comments)
EXCLUDES=()
EXCLUDES+=("--exclude=.git")
EXCLUDES+=("--exclude=./re_*.tar.gz")   # skip any previous archives in this folder

if [[ -f "$GITIGNORE" ]]; then
    while IFS= read -r line; do
        # skip blank lines and comments
        [[ -z "$line" || "$line" == \#* ]] && continue
        # strip leading and trailing slashes (tar doesn't use gitignore slash semantics)
        line="${line#/}"
        line="${line%/}"
        EXCLUDES+=("--exclude=./$line")
    done < "$GITIGNORE"
fi

echo "Exclude rules: ${#EXCLUDES[@]}"
echo ""

tar \
    --create \
    --gzip \
    --file="$ARCHIVE" \
    "${EXCLUDES[@]}" \
    --transform "s|^\.|re|" \
    -C "$REPO_ROOT" \
    .

SIZE="$(du -sh "$ARCHIVE" | cut -f1)"
echo ""
echo "Done — $ARCHIVE  ($SIZE)"
