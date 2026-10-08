#!/usr/bin/env python3
"""Recompute the source-audited direct SHS/cortisol sensitivity analysis.

The input is the PDF-audited extraction addendum, not the historical provisional
31-row CSV. Only the three direct cortisol rows with supplied-PDF page/table
locators are used. The pooled result is explicitly exploratory because the
reports use non-equivalent SHS definitions and may overlap in their Beijing
occupational populations.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "meta_analysis_verified_online_extraction_SchemeB_2026-10-08.csv"
OUTPUT = ROOT / "meta_analysis_source_audited_results_SchemeB_2026-10-08.csv"

DIRECT_IDS = ("YAN2015-CORT", "YAN2012-CORT", "YAN2018-CORT")


def f(row: dict[str, str], key: str) -> float:
    return float(row[key])


def study_effect(row: dict[str, str]) -> tuple[float, float, float, float]:
    n1, n0 = f(row, "group_1_n"), f(row, "group_2_n")
    m1, m0 = f(row, "group_1_mean_or_effect"), f(row, "group_2_mean_or_effect")
    s1, s0 = f(row, "group_1_sd_or_ci"), f(row, "group_2_sd_or_ci")
    effect = m1 - m0
    se = math.sqrt(s1 * s1 / n1 + s0 * s0 / n0)
    return effect, se * se, effect - 1.96 * se, effect + 1.96 * se


def dl(values: list[tuple[float, float]]) -> dict[str, float]:
    effects = [x[0] for x in values]
    variances = [x[1] for x in values]
    weights = [1 / v for v in variances]
    fixed = sum(w * e for w, e in zip(weights, effects)) / sum(weights)
    q = sum(w * (e - fixed) ** 2 for w, e in zip(weights, effects))
    df = len(values) - 1
    c = sum(weights) - sum(w * w for w in weights) / sum(weights)
    tau2 = max(0.0, (q - df) / c) if c else 0.0
    random_weights = [1 / (v + tau2) for v in variances]
    pooled = sum(w * e for w, e in zip(random_weights, effects)) / sum(random_weights)
    se = math.sqrt(1 / sum(random_weights))
    return {
        "effect": pooled,
        "lower": pooled - 1.96 * se,
        "upper": pooled + 1.96 * se,
        "Q": q,
        "df": df,
        "tau2": tau2,
        "I2": max(0.0, (q - df) / q * 100) if q else 0.0,
    }


def row_result(result_type: str, outcome: str, study: str, effect: float,
               lower: float, upper: float, **extra: object) -> dict[str, str]:
    row = {
        "result_type": result_type,
        "outcome": outcome,
        "study": study,
        "metric": "MD",
        "effect": f"{effect:.6f}",
        "lower_95ci": f"{lower:.6f}",
        "upper_95ci": f"{upper:.6f}",
        "Q": "",
        "df": "",
        "tau2": "",
        "I2_percent": "",
        "status": "exploratory_only_non_equivalent_definitions_or_overlap",
        "notes": "",
    }
    for key, value in extra.items():
        row[key] = "" if value is None else str(value)
    return row


def main() -> None:
    with INPUT.open(encoding="utf-8", newline="") as handle:
        all_rows = list(csv.DictReader(handle))
    rows = [row for row in all_rows if row["record_id"] in DIRECT_IDS]
    if {row["record_id"] for row in rows} != set(DIRECT_IDS):
        raise SystemExit("The three direct PDF-audited cortisol rows are not all present")

    studies: list[tuple[dict[str, str], float, float, float, float]] = []
    for row in rows:
        effect, variance, lower, upper = study_effect(row)
        studies.append((row, effect, variance, lower, upper))

    output: list[dict[str, str]] = []
    for row, effect, variance, lower, upper in studies:
        output.append(row_result(
            "study_effect",
            "Direct_SHS_cortisol_ng_ml",
            row["record_id"],
            effect,
            lower,
            upper,
            n_shs=row["group_1_n"],
            n_reference=row["group_2_n"],
            pdf_page_table=row["source_locator"],
            notes="MD and CI derived from PDF-reported means/SDs; CI uses independent-group normal approximation.",
        ))

    pooled = dl([(effect, variance) for _, effect, variance, _, _ in studies])
    output.append(row_result(
        "exploratory_random_effects_pool",
        "Direct_SHS_cortisol_ng_ml",
        "3 PDF-audited reports",
        pooled["effect"],
        pooled["lower"],
        pooled["upper"],
        Q=f"{pooled['Q']:.6f}",
        df=pooled["df"],
        tau2=f"{pooled['tau2']:.6f}",
        I2_percent=f"{pooled['I2']:.3f}",
        notes="Not a primary estimate: SHS definitions differ (median 35, median 44, LCA), 2015 values are covariate-adjusted, and cohort overlap is unresolved.",
    ))

    for index, dropped in enumerate(rows):
        keep = [x for i, x in enumerate(studies) if i != index]
        result = dl([(effect, variance) for _, effect, variance, _, _ in keep])
        output.append(row_result(
            "leave_one_out_exploratory_pool",
            "Direct_SHS_cortisol_ng_ml",
            f"drop_{dropped['record_id']}",
            result["effect"],
            result["lower"],
            result["upper"],
            Q=f"{result['Q']:.6f}",
            df=result["df"],
            tau2=f"{result['tau2']:.6f}",
            I2_percent=f"{result['I2']:.3f}",
            notes="Sensitivity only; does not resolve cohort overlap or definition incompatibility.",
        ))

    fields = list(output[0])
    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUTPUT}")
    for row in output:
        if row["result_type"] == "exploratory_random_effects_pool":
            print(row)


if __name__ == "__main__":
    main()
