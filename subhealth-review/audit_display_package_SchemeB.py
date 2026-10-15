#!/usr/bin/env python3
"""Audit the conservative display-package disposition for the active manuscript."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANUSCRIPT = ROOT / "44_Source_Audited_Narrative_Review_Manuscript_SchemeB_2026-10-08.md"
DISPLAY_AUDIT = ROOT / "55_MolPsychiatry_Display_Package_Audit_SchemeB_2026-10-15.md"

REQUIRED_TABLE_CAPTIONS = (
    "**Table 1. Source-audited direct SHS–cortisol reports and pooling disposition.**",
    "**Table 2. Evidence strata and permissible inference boundaries.**",
    "**Table 3. Prospective validation matrix for direct SHSQ-25 human evidence.**",
)
FORBIDDEN_ACTIVE_DISPLAY_REFERENCES = (
    "FigS2_Forest_Cortisol_SourceAudited_Exploratory",
    "FigS3_Forest_NLR",
    "FigS4a_Forest_HRV_SDNN",
    "FigS4b_Forest_HRV_RMSSD",
    "FigS5_Forest_Fatigue_OR",
    "FigS6_Forest_SF36_Vitality",
    "FigS7_Forest_OXPHOS",
    "PRISMA_Flow_SchemeB",
)
REQUIRED_DISPLAY_LOCKS = (
    "RETAIN in main text",
    "EXCLUDE from submission package",
    "three tables and no final figure",
    "does not report a primary pooled estimate",
    "not a current extraction table",
)


def main() -> None:
    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    audit = DISPLAY_AUDIT.read_text(encoding="utf-8")

    for caption in REQUIRED_TABLE_CAPTIONS:
        if caption not in manuscript:
            raise SystemExit(f"Required main-text table caption is missing: {caption}")
    for phrase in REQUIRED_DISPLAY_LOCKS:
        if phrase not in audit:
            raise SystemExit(f"Display-package safeguard is missing: {phrase}")
    for filename in FORBIDDEN_ACTIVE_DISPLAY_REFERENCES:
        if filename in manuscript:
            raise SystemExit(f"Excluded legacy display is referenced by active manuscript: {filename}")

    retained_tables = sum(caption in manuscript for caption in REQUIRED_TABLE_CAPTIONS)
    if retained_tables != 3:
        raise SystemExit(f"Expected exactly three retained main-text table captions, found {retained_tables}")
    if "No final primary Meta estimate is reported" not in manuscript:
        raise SystemExit("Primary synthesis lock is missing from manuscript")

    print(
        "Display-package audit PASS: three safeguarded main-text tables retained; "
        "legacy exploratory displays absent; no final figure or pooled estimate promoted"
    )


if __name__ == "__main__":
    main()
