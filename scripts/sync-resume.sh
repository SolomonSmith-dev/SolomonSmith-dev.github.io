#!/usr/bin/env bash
# Sync the canonical resume into the site.
#
# Copies the resume PDF from swe-job-hunt/MATERIALS over assets/resume/SolomonSmithResume.pdf
# (same filename, so every existing link keeps working) and regenerates resume.md and
# _includes/skills.html from the resume .md through scripts/resume_md.py.
#
#   scripts/sync-resume.sh                 # default source: ~/Projects/swe-job-hunt/MATERIALS
#   RESUME_SRC_DIR=/path scripts/sync-resume.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC_DIR="${RESUME_SRC_DIR:-$HOME/Projects/swe-job-hunt/MATERIALS}"
BASENAME="Solomon-Smith_AI-Backend-Engineer_resume"
SRC_MD="$SRC_DIR/$BASENAME.md"
SRC_PDF="$SRC_DIR/$BASENAME.pdf"
PDF_SITE_PATH="/assets/resume/SolomonSmithResume.pdf"
DEST_PDF="$ROOT$PDF_SITE_PATH"

for f in "$SRC_MD" "$SRC_PDF"; do
  [[ -f "$f" ]] || { echo "sync-resume: missing $f" >&2; exit 1; }
done

/bin/cp -f "$SRC_PDF" "$DEST_PDF"
python3 "$ROOT/scripts/resume_md.py" \
  --source "$SRC_MD" \
  --page "$ROOT/resume.md" \
  --skills "$ROOT/_includes/skills.html" \
  --pdf "$PDF_SITE_PATH"

if [[ "$SRC_PDF" -ot "$SRC_MD" ]]; then
  echo "sync-resume: note: $SRC_PDF is older than $SRC_MD; regenerate the PDF if the text changed" >&2
fi
echo "sync-resume: copied $(basename "$SRC_PDF") to $DEST_PDF"
