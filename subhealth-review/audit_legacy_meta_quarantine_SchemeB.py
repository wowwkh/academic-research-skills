#!/usr/bin/env python3
"""Validate that legacy Meta rows remain quarantined until exact source audit."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEDGER = ROOT / "meta_analysis_eligibility_ledger_SchemeB_2026-10-08.csv"

EXPECTED_ROWS = 31
EXPECTED_UNVERIFIED = 24
OUTCOMES_REQUIRING_SOURCE_AUDIT = {
    "NLR",
    "HRV_SDNN_ms",
    "HRV_RMSSD_ms",
    "Fatigue_OR_joint",
    "SF36_Vitality",
    "OXPHOS_basal",
}
FORBIDDEN_PRIMARY_STATUSES = {
    "eligible_primary_pool",
    "pooled_primary",
    "included_primary",
}


def main() -> None:
    with LEDGER.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    if len(rows) != EXPECTED_ROWS:
        raise SystemExit(f"Expected {EXPECTED_ROWS} ledger rows; found {len(rows)}")

    unverified = [
        row for row in rows
        if row["verification_status"] == "unverified_no_exact_title_pmid_doi"
    ]
    if len(unverified) != EXPECTED_UNVERIFIED:
        raise SystemExit(
            f"Expected {EXPECTED_UNVERIFIED} unverified rows; found {len(unverified)}"
        )

    for row in rows:
        status = row["eligibility_status"]
        if status in FORBIDDEN_PRIMARY_STATUSES:
            raise SystemExit(
                f"Legacy row incorrectly eligible for primary pooling: {row['legacy_row_id']}"
            )
        if row["verification_status"] == "unverified_no_exact_title_pmid_doi":
            if any(row[field].strip() for field in ("pmid", "pubmed_url", "doi", "doi_url")):
                raise SystemExit(
                    f"Unverified row contains bibliographic identifiers: {row['legacy_row_id']}"
                )
            if status != "quarantine_from_primary_meta":
                raise SystemExit(
                    f"Unverified row is not quarantined: {row['legacy_row_id']}"
                )
        if row["legacy_outcome"] in OUTCOMES_REQUIRING_SOURCE_AUDIT:
            if status in FORBIDDEN_PRIMARY_STATUSES or status == "eligible_for_primary_pool":
                raise SystemExit(
                    f"Outcome row bypassed source-audit gate: {row['legacy_row_id']}"
                )

    print(
        "Legacy Meta quarantine audit PASS: "
        f"{len(rows)} rows; {len(unverified)} unverified rows quarantined; "
        "no primary pooled legacy rows"
    )
    print("Eligibility statuses:", dict(Counter(row["eligibility_status"] for row in rows)))


if __name__ == "__main__":
    main()
