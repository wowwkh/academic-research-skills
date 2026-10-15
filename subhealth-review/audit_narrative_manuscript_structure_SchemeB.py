#!/usr/bin/env python3
"""Check that the evidence-safe manuscript retains its required structure and locks."""

from __future__ import annotations

import re
from pathlib import Path

from evidence_scope_policy_SchemeB import forbidden_identifiers

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
    "The abstract is unstructured and within the journal’s 150–250-word review range",
)
REQUIRED_EVIDENCE_FILES = (
    "42_Primary_Synthesis_Lock_and_Narrative_Evidence_Map_SchemeB_2026-10-08.md",
    "48_Verified_SHS_Original_Evidence_and_PDF_Audit_Addendum_SchemeB_2026-10-15.md",
    "49_Original_Source_Request_and_Next_Audit_Gate_SchemeB_2026-10-15.md",
    "50_Verified_Reference_Register_SchemeB_2026-10-15.md",
    "51_Claim_to_Source_Traceability_Matrix_SchemeB_2026-10-15.md",
    "52_MolPsychiatry_Review_Format_Gate_SchemeB_2026-10-15.md",
    "53_Verified_Reference_Metadata_Register_SchemeB_2026-10-15.md",
    "53_Verified_Reference_Metadata_Register_SchemeB_2026-10-15.csv",
    "54_Vancouver_Citation_Order_Map_SchemeB_2026-10-15.md",
    "55_MolPsychiatry_Display_Package_Audit_SchemeB_2026-10-15.md",
    "56_Submission_Metadata_and_Declaration_Placeholders_SchemeB_2026-10-15.md",
)
FORBIDDEN_IDENTIFIERS = (
    *forbidden_identifiers(),
    "CRD42026XXXXX",
    "110 studies included",
    "Ready for Final Submission",
)
ABSTRACT_FORBIDDEN_HEADINGS = (
    "### Background",
    "### Methods",
    "### Results",
    "### Conclusions",
)
ABSTRACT_MIN_WORDS = 150
ABSTRACT_MAX_WORDS = 250


def main() -> None:
    text = MANUSCRIPT.read_text(encoding="utf-8")
    for phrase in REQUIRED_HEADINGS + REQUIRED_LOCKS + REQUIRED_EVIDENCE_FILES:
        if phrase not in text:
            raise SystemExit(f"Required manuscript structure/lock missing: {phrase}")
    for phrase in FORBIDDEN_IDENTIFIERS:
        if phrase in text:
            raise SystemExit(f"Forbidden provisional or quarantined phrase present: {phrase}")

    try:
        abstract = text.split("## Abstract", 1)[1].split("## 1. Introduction", 1)[0]
    except IndexError as exc:
        raise SystemExit("Unable to isolate the manuscript abstract") from exc
    for heading in ABSTRACT_FORBIDDEN_HEADINGS:
        if heading in abstract:
            raise SystemExit(f"Structured abstract heading remains in Review Article abstract: {heading}")
    abstract_words = re.findall(r"\b[\w’'-]+\b", abstract)
    if not ABSTRACT_MIN_WORDS <= len(abstract_words) <= ABSTRACT_MAX_WORDS:
        raise SystemExit(
            "Review Article abstract is outside the 150–250-word range: "
            f"{len(abstract_words)} words"
        )

    print(
        "Manuscript structure audit PASS: required sections, evidence locks, "
        "Mol Psychiatry abstract gate and reporting gates present; "
        "provisional/quarantined phrases absent"
    )


if __name__ == "__main__":
    main()
