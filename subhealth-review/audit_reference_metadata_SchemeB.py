#!/usr/bin/env python3
"""Validate the journal-formatted metadata layer against the 19 verified anchors."""

from __future__ import annotations

import csv
from pathlib import Path

from audit_narrative_manuscript_citations_SchemeB import ANCHORS

ROOT = Path(__file__).resolve().parent
METADATA = ROOT / "53_Verified_Reference_Metadata_Register_SchemeB_2026-10-15.csv"
EXPECTED_FIELDS = (
    "id",
    "exact_title",
    "pmid",
    "pubmed_url",
    "doi",
    "doi_url",
    "vancouver_author_string",
    "journal_abbreviation",
    "year",
    "volume",
    "issue_or_article",
    "pages_or_locator",
    "metadata_source_url",
    "metadata_status",
)


def main() -> None:
    with METADATA.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != EXPECTED_FIELDS:
            raise SystemExit("Reference metadata CSV fields do not match the locked schema")
        rows = list(reader)

    if len(rows) != len(ANCHORS):
        raise SystemExit(f"Expected {len(ANCHORS)} metadata rows, found {len(rows)}")

    expected_by_id = {
        f"A{index:02d}": (title, pmid, pubmed_url, doi, doi_url)
        for index, (title, pmid, pubmed_url, doi, doi_url, _role) in enumerate(ANCHORS, 1)
    }
    seen_ids: set[str] = set()
    seen_pmids: set[str] = set()
    seen_dois: set[str] = set()
    for row in rows:
        row_id = row["id"]
        if row_id in seen_ids:
            raise SystemExit(f"Duplicate metadata ID: {row_id}")
        seen_ids.add(row_id)
        if row_id not in expected_by_id:
            raise SystemExit(f"Unexpected metadata ID: {row_id}")

        expected_title, expected_pmid, expected_pubmed, expected_doi, expected_doi_url = expected_by_id[row_id]
        for field, expected in (
            ("exact_title", expected_title),
            ("pmid", expected_pmid),
            ("pubmed_url", expected_pubmed),
            ("doi", expected_doi),
            ("doi_url", expected_doi_url),
        ):
            if row[field] != expected:
                raise SystemExit(f"{row_id} {field} does not match the verified anchor")
        if row["pmid"] in seen_pmids:
            raise SystemExit(f"Duplicate PMID in metadata register: {row['pmid']}")
        if row["doi"].casefold() in seen_dois:
            raise SystemExit(f"Duplicate DOI in metadata register: {row['doi']}")
        seen_pmids.add(row["pmid"])
        seen_dois.add(row["doi"].casefold())

        required_metadata_fields = (
            "vancouver_author_string",
            "journal_abbreviation",
            "year",
            "volume",
            "pages_or_locator",
            "metadata_source_url",
            "metadata_status",
        )
        for field in required_metadata_fields:
            if not row[field].strip():
                raise SystemExit(f"{row_id} has an empty journal metadata field: {field}")
        if not row["metadata_status"].startswith("identity closed"):
            raise SystemExit(f"{row_id} metadata status is not explicitly tied to identity closure")
        if row["vancouver_author_string"].count("et al.") > 1:
            raise SystemExit(f"{row_id} has malformed repeated et al. in author string")

    if seen_ids != set(expected_by_id):
        raise SystemExit("Metadata register is missing one or more verified anchor IDs")

    print(
        f"Reference metadata audit PASS: {len(rows)} rows match verified title/PMID/DOI tuples; "
        "journal fields are populated; final Vancouver citation freeze remains pending"
    )


if __name__ == "__main__":
    main()
