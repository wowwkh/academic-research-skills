#!/usr/bin/env python3
"""Audit the separate clean journal-facing copy without touching the working audit draft."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CLEAN_COPY = ROOT / "57_Journal_Facing_Submission_Copy_SchemeB_2026-10-15.md"

REQUIRED_TABLE_CAPTIONS = (
    "**Table 1. Source-audited direct SHS–cortisol reports and pooling disposition.**",
    "**Table 2. Evidence strata and permissible inference boundaries.**",
    "**Table 3. Prospective validation matrix for direct SHSQ-25 human evidence.**",
)
FORBIDDEN_AUDIT_ONLY_PATTERNS = (
    "PMID",
    "Evidence files",
    "subhealth-review/",
    "audit_narrative_",
    "audit_reference_",
    "audit_vancouver_",
    "audit_display_",
    "audit_submission_",
    "48_Verified_SHS_Original_Evidence",
    "49_Original_Source_Request",
    "50_Verified_Reference_Register",
    "51_Claim_to_Source_Traceability",
    "52_MolPsychiatry_Review_Format_Gate",
    "53_Verified_Reference_Metadata",
    "54_Vancouver_Citation_Order_Map",
    "55_MolPsychiatry_Display_Package_Audit",
    "56_Submission_Metadata_and_Declaration_Placeholders",
    "FigS2_Forest",
    "PRISMA_Flow_SchemeB",
)
REQUIRED_CLEAN_LOCKS = (
    "No final primary Meta estimate is reported",
    "Current evidence does not support any standalone SHS biomarker diagnostic test",
    "SHSQ-25 should not be presented as a molecular diagnosis",
    "not pooled with direct SHS/cortisol evidence",
    "not a direct measure of mitochondrial dynamics",
    "not generalized to non-pregnant SHS",
)


def main() -> None:
    text = CLEAN_COPY.read_text(encoding="utf-8")
    for pattern in FORBIDDEN_AUDIT_ONLY_PATTERNS:
        if pattern in text:
            raise SystemExit(f"Audit-only material remains in clean journal-facing copy: {pattern}")
    for lock in REQUIRED_CLEAN_LOCKS:
        if lock not in text:
            raise SystemExit(f"Evidence-safety wording is missing from clean copy: {lock}")
    for caption in REQUIRED_TABLE_CAPTIONS:
        if text.count(caption) != 1:
            raise SystemExit(f"Expected exactly one clean-copy table caption: {caption}")

    if text.count("## References\n") != 1:
        raise SystemExit("Clean copy must contain exactly one References section")
    if text.count("## 6. Declarations and availability statements") != 1:
        raise SystemExit("Clean copy declaration section is missing or duplicated")
    if text.count("`*`") < 10:
        raise SystemExit("Clean copy no longer retains the requested star placeholders")
    for decision in ("- Supplementary-information decision: `*`", "- Final figure decision: `*`", "- Final table decision: `*`"):
        if decision not in text:
            raise SystemExit(f"Clean copy decision placeholder is missing: {decision}")

    references = text.split("## References\n", 1)[1]
    for number in range(1, 20):
        if not re.search(rf"^{number}\. .*doi:", references, flags=re.MULTILINE):
            raise SystemExit(f"Clean Vancouver reference {number} is missing")
    if "20. " in references:
        raise SystemExit("Clean copy contains an unexpected twentieth Vancouver reference")
    if re.search(r"doi:[^\n]+\.\.", references):
        raise SystemExit("Clean copy contains duplicated terminal punctuation after a DOI")

    print(
        "Clean journal-facing copy audit PASS: PMID/internal navigation removed; "
        "19 DOI-based Vancouver references, three tables and star placeholders retained"
    )


if __name__ == "__main__":
    main()
