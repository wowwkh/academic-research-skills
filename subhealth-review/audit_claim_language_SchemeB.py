#!/usr/bin/env python3
"""Final claim-language audit for direct, bridge and transfer evidence boundaries."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WORKING = ROOT / "44_Source_Audited_Narrative_Review_Manuscript_SchemeB_2026-10-08.md"
CLEAN = ROOT / "57_Journal_Facing_Submission_Copy_SchemeB_2026-10-15.md"

REQUIRED_SAFETY_LOCKS = (
    "Current evidence does not support any standalone SHS biomarker diagnostic test",
    "SHSQ-25 should not be presented as a molecular diagnosis",
    "No final primary Meta estimate is reported",
    "not pooled with direct SHS/cortisol evidence",
    "not a direct measure of mitochondrial dynamics",
    "not generalized to non-pregnant SHS",
)
ABSOLUTE_ABSENCE_PATTERNS = (
    "no such study exists",
    "no such studies exist",
    "there are no studies",
    "there are no reports",
    "has never been studied",
    "have never been studied",
    "no paper has ever reported",
)
UNSUPPORTED_CAUSAL_OR_DIAGNOSTIC_PATTERNS = (
    r"\bSLIM(?: model)? (?:demonstrates|establishes|proves)\b",
    r"\bSHSQ-25 (?:is|constitutes) (?:a )?molecular diagnosis\b",
    r"\b(?:cortisol|telomere length|glycomic profiles?|endothelial measures?|mitochondrial markers?) are? (?:a )?standalone diagnostic\b",
    r"\bmitochondrial dynamics (?:is|are) demonstrated in SHS\b",
    r"\bbridge evidence (?:demonstrates|proves) (?:a )?(?:direct|causal) SHS pathway\b",
)


def main() -> None:
    for path in (WORKING, CLEAN):
        text = path.read_text(encoding="utf-8")
        body = text.split("## References", 1)[0]
        for lock in REQUIRED_SAFETY_LOCKS:
            if lock not in body:
                raise SystemExit(f"{path.name}: required claim-safety lock is missing: {lock}")
        if not (
            "The transfer evidence remains biologically plausible rather than direct SHS evidence" in body
            or "biological plausibility, not a demonstrated SHS pathway" in body
        ):
            raise SystemExit(f"{path.name}: transfer evidence is not explicitly bounded as non-direct SHS evidence")
        lowered = body.casefold()
        for phrase in ABSOLUTE_ABSENCE_PATTERNS:
            if phrase in lowered:
                raise SystemExit(f"{path.name}: unsupported absolute-absence wording: {phrase}")
        for pattern in UNSUPPORTED_CAUSAL_OR_DIAGNOSTIC_PATTERNS:
            if re.search(pattern, body, flags=re.IGNORECASE):
                raise SystemExit(f"{path.name}: unsupported causal/diagnostic wording: {pattern}")

        bridge_section = body.split("### 3.3 Low-grade-inflammation and fatigue/quality-of-life bridge evidence", 1)[1]
        bridge_section = bridge_section.split("### 3.4 Evidence certainty and quarantined rows", 1)[0]
        for phrase in ("bridge evidence", "not a direct SHSQ-25 result", "not pooled with direct SHS/cortisol evidence"):
            if phrase not in bridge_section:
                raise SystemExit(f"{path.name}: non-SHS bridge boundary is incomplete: {phrase}")

    print(
        "Claim-language audit PASS: direct/bridge/transfer boundaries retained; "
        "standalone diagnostic, causal and absolute-absence overclaims absent"
    )


if __name__ == "__main__":
    main()
