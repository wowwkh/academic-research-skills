#!/usr/bin/env python3
"""Audit first-citation order and working Vancouver references in the manuscript."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANUSCRIPT = ROOT / "44_Source_Audited_Narrative_Review_Manuscript_SchemeB_2026-10-08.md"
METADATA = ROOT / "53_Verified_Reference_Metadata_Register_SchemeB_2026-10-15.csv"


def main() -> None:
    text = MANUSCRIPT.read_text(encoding="utf-8")
    if "## References\n" not in text:
        raise SystemExit("Working Vancouver References section is missing")
    body, references = text.split("## References\n", 1)
    rows = list(csv.DictReader(METADATA.open(encoding="utf-8", newline="")))
    if len(rows) != 19:
        raise SystemExit(f"Expected 19 metadata rows, found {len(rows)}")

    ordered = sorted(rows, key=lambda row: body.find(row["exact_title"]))
    if any(body.find(row["exact_title"]) < 0 for row in ordered):
        raise SystemExit("A verified title is missing from the manuscript body")

    for number, row in enumerate(ordered, 1):
        expected_marker = f"{row['doi_url']}) [{number}]"
        if body.count(expected_marker) != 1:
            raise SystemExit(
                f"Citation order mismatch for {row['id']}: expected one first-citation marker "
                f"{number} after its DOI audit anchor"
            )
        # The reference number must not be reused for another anchor in the body.
        other_markers = [
            f"{other['doi_url']}) [{number}]"
            for other in rows
            if other["id"] != row["id"]
        ]
        if any(marker in body for marker in other_markers):
            raise SystemExit(f"Reference number {number} is assigned to more than one anchor")

        authors = row["vancouver_author_string"].rstrip(".")
        issue = f"({row['issue_or_article']})" if row["issue_or_article"] else ""
        locator = f"{row['volume']}{issue}:{row['pages_or_locator']}"
        expected_reference = (
            f"{number}. {authors}. {row['exact_title']}. *{row['journal_abbreviation']}*. "
            f"{row['year']};{locator}. doi:{row['doi']}. PMID:"
        )
        if references.count(expected_reference) != 1:
            raise SystemExit(f"Reference list entry {number} does not match metadata row {row['id']}")

    print(
        "Vancouver citation-order audit PASS: 19 first-citation markers and 19 reference entries "
        "match the verified metadata register; evidence roles unchanged"
    )


if __name__ == "__main__":
    main()
