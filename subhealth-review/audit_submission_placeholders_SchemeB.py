#!/usr/bin/env python3
"""Ensure author-supplied submission fields remain explicit star placeholders."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANUSCRIPT = ROOT / "44_Source_Audited_Narrative_Review_Manuscript_SchemeB_2026-10-08.md"
PLACEHOLDER_FILE = ROOT / "56_Submission_Metadata_and_Declaration_Placeholders_SchemeB_2026-10-15.md"

REQUIRED_PLACEHOLDER_LINES = (
    "- Running title: `*`",
    "- Author names and order: `*`",
    "- Affiliations matched to author superscripts: `*`",
    "- ORCID identifiers: `*`",
    "- Corresponding author: `*`",
    "- Corresponding-author email: `*`",
    "- Funding statement: `*`",
    "- Competing-interest statement: `*`",
    "- Author-contribution statement: `*`",
    "- Data-availability confirmation: `*`",
    "- Code-availability confirmation: `*`",
    "- Ethics/consent wording confirmation: `*`",
    "- Supplementary-information decision: `*`",
    "- Final figure decision: `*`",
    "- Final table decision: `*`",
)


def main() -> None:
    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    placeholders = PLACEHOLDER_FILE.read_text(encoding="utf-8")
    for line in REQUIRED_PLACEHOLDER_LINES:
        if line not in placeholders:
            raise SystemExit(f"Required author-completion placeholder is missing: {line}")
    if "56_Submission_Metadata_and_Declaration_Placeholders_SchemeB_2026-10-15.md" not in manuscript:
        raise SystemExit("Manuscript does not point to the placeholder gate")
    if "### Author-completion placeholders — not for submission" not in manuscript:
        raise SystemExit("Manuscript lacks the explicit non-submission placeholder section")
    if "replace them only with user-confirmed information" not in placeholders.casefold():
        raise SystemExit("Placeholder file lacks the user-confirmation safeguard")

    print(
        "Submission-placeholder audit PASS: author, declaration, correspondence, "
        "figure and supplementary fields remain explicit `*` placeholders"
    )


if __name__ == "__main__":
    main()
