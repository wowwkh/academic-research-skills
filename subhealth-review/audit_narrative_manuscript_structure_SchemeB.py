#!/usr/bin/env python3
"""Check that the evidence-safe manuscript retains its required structure and locks."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANUSCRIPT = ROOT / "44_Source_Audited_Narrative_Review_Manuscript_SchemeB_2026-10-08.md"

REQUIRED_HEADINGS = (
    "## Abstract",
    "## 1. Introduction",
    "## 2. Methods: source-audited evidence adjudication",
    "## 3. Results",
    "## 4. Discussion",
    "## 5. Conclusion",
    "## 6. Reporting and availability statements",
)
REQUIRED_LOCKS = (
    "Sixteen supplied PDFs were audited",
    "No final primary Meta estimate is reported",
    "The 19 verified anchors are article-level records",
    "not an absolute absence claim",
    "primary pooled direct-cortisol estimate",
    "Funding, conflict-of-interest, author-contribution and correspondence statements are not inferred",
)
REQUIRED_EVIDENCE_FILES = (
    "42_Primary_Synthesis_Lock_and_Narrative_Evidence_Map_SchemeB_2026-10-08.md",
    "48_Verified_SHS_Original_Evidence_and_PDF_Audit_Addendum_SchemeB_2026-10-15.md",
    "49_Original_Source_Request_and_Next_Audit_Gate_SchemeB_2026-10-15.md",
    "50_Verified_Reference_Register_SchemeB_2026-10-15.md",
    "51_Claim_to_Source_Traceability_Matrix_SchemeB_2026-10-15.md",
)
FORBIDDEN_IDENTIFIERS = (
    "31814473",
    "10.1080/10715762.2019.1685668",
    "CRD42026XXXXX",
    "110 studies included",
    "Ready for Final Submission",
)


def main() -> None:
    text = MANUSCRIPT.read_text(encoding="utf-8")
    for phrase in REQUIRED_HEADINGS + REQUIRED_LOCKS + REQUIRED_EVIDENCE_FILES:
        if phrase not in text:
            raise SystemExit(f"Required manuscript structure/lock missing: {phrase}")
    for phrase in FORBIDDEN_IDENTIFIERS:
        if phrase in text:
            raise SystemExit(f"Forbidden provisional or quarantined phrase present: {phrase}")
    print(
        "Manuscript structure audit PASS: required sections, evidence locks and "
        "reporting gates present; provisional/quarantined phrases absent"
    )


if __name__ == "__main__":
    main()
