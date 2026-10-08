#!/usr/bin/env python3
"""Build the locked, source-audited evidence map for Scheme B.

The source-audited extraction CSV is retained as the quantitative source file.
This output adds the pre-specified synthesis role and prevents bridge or
non-independent direct-cortisol estimates from silently entering a primary
pooled analysis.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "meta_analysis_verified_online_extraction_SchemeB_2026-10-08.csv"
OUTPUT = ROOT / "locked_primary_synthesis_evidence_map_SchemeB_2026-10-08.csv"

DIRECT = {
    "YAN2012-CORT": {
        "analysis_set": "direct_SHS_cortisol",
        "synthesis_status": "narrative_study_level_withheld_from_primary_pool",
        "pooling_decision": "not_pooled",
        "rationale": "Potentially etiologic SHS-cortisol comparison, but cohort independence, serum-versus-plasma comparability, sampling time and sample-median SHS definition remain unresolved.",
        "next_action": "Keep the source value in narrative synthesis; reopen quantitative pooling only after cohort and measurement reconciliation.",
    },
    "YAN2015-CORT": {
        "analysis_set": "direct_SHS_cortisol",
        "synthesis_status": "narrative_study_level_withheld_from_primary_pool",
        "pooling_decision": "not_pooled",
        "rationale": "Potentially etiologic SHS-cortisol comparison, but the January-April 2012 Xuanwu Hospital frame may overlap Yan 2012 and Table 4 reports covariate-adjusted values.",
        "next_action": "Keep the adjusted study-level value in narrative synthesis; do not treat the derived CI as author-reported.",
    },
    "YAN2018-CORT": {
        "analysis_set": "direct_SHS_cortisol_diagnostic_bridge",
        "synthesis_status": "diagnostic_evidence_excluded_from_etiologic_pool",
        "pooling_decision": "not_pooled",
        "rationale": "Cortisol is a manifest variable in the LCA that assigns the final SHS and health-status classes; the contrast is not an independent SHSQ-25 exposure-cortisol outcome estimate.",
        "next_action": "Report as diagnostic/bridge evidence only; do not combine with etiologic group comparisons.",
    },
}

BRIDGE = {
    "bridge_low_grade_inflammation": {
        "analysis_set": "low_grade_inflammation_HRQoL_bridge",
        "synthesis_status": "narrative_bridge_only",
        "pooling_decision": "not_pooled_with_direct_SHS_cortisol",
        "rationale": "Low-grade-inflammation and HRQoL estimands do not use SHSQ-25-defined SHS or the direct cortisol outcome.",
        "next_action": "Retain as a separately graded mechanistic bridge; do not mix effect scales with direct SHS-cortisol data.",
    },
    "bridge_fatigue_inflammation": {
        "analysis_set": "inflammation_fatigue_bridge",
        "synthesis_status": "narrative_bridge_only",
        "pooling_decision": "not_pooled_with_direct_SHS_cortisol",
        "rationale": "Whitehall II reports separate CRP and IL-6 fatigue ORs, not SHSQ-25-defined SHS or a joint-marker effect.",
        "next_action": "Retain separate-marker results as bridge evidence; do not restore the unsupported historical joint-marker OR.",
    },
}

FIELDS = [
    "record_id",
    "article_role",
    "exact_title",
    "pmid",
    "pubmed_url",
    "doi",
    "doi_url",
    "outcome",
    "source_locator",
    "effect_measure",
    "effect_value",
    "ci_lower",
    "ci_upper",
    "effect_status",
    "analysis_set",
    "synthesis_status",
    "pooling_decision",
    "rationale",
    "next_action",
]


def main() -> None:
    with INPUT.open(encoding="utf-8", newline="") as handle:
        source_rows = list(csv.DictReader(handle))

    output: list[dict[str, str]] = []
    for source in source_rows:
        role = source["article_role"]
        if source["record_id"] in DIRECT:
            decision = DIRECT[source["record_id"]]
        elif role in BRIDGE:
            decision = BRIDGE[role]
        else:
            raise SystemExit(f"Unexpected source-audited role: {role}")
        row = {field: source.get(field, "") for field in FIELDS}
        row.update(decision)
        output.append(row)

    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUTPUT} ({len(output)} rows)")
    print("primary pooled direct-cortisol rows:", sum(row["pooling_decision"] == "pooled_primary" for row in output))
    print("narrative/bridge rows:", sum(row["pooling_decision"] != "pooled_primary" for row in output))


if __name__ == "__main__":
    main()
