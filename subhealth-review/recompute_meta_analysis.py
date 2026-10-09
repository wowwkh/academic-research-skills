#!/usr/bin/env python3
"""Recompute provisional meta-analytic summaries from the extraction CSV.

This script is deliberately separate from generate_forest_plots.py.  The latter
contains the historical draft figures; this script reads the current extraction
file and computes study effects, DerSimonian-Laird random-effects summaries,
95% CIs, Q, tau-squared, and I-squared from the values that are actually in the
CSV.

It is a validation tool, not a substitute for source-PDF verification.  The
current CSV contains provisional values and does not yet include page/table
locators for most studies.  No input file is modified.
"""

from __future__ import annotations

import csv
import math
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "meta_analysis_extraction_SchemeB.csv"
SUMMARY_OUT = ROOT / "meta_analysis_recomputed_provisional.csv"
AUDIT_OUT = ROOT / "meta_analysis_input_audit_provisional.csv"

OR_RE = re.compile(
    r"OR\s*([0-9]+(?:\.[0-9]+)?)\s*\[\s*"
    r"([0-9]+(?:\.[0-9]+)?)\s*,\s*"
    r"([0-9]+(?:\.[0-9]+)?)\s*\]",
    re.IGNORECASE,
)
NUMBER_RE = re.compile(r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)")


def number(value: str) -> float | None:
    value = (value or "").strip()
    return float(value) if value else None


def metric_for(row: dict[str, str]) -> str:
    if row["Outcome"].startswith("OXPHOS") or row["Effect"].strip().upper().startswith("SMD"):
        return "SMD"
    if row["Effect"].strip().upper().startswith("OR"):
        return "logOR"
    return "MD"


def study_effect(row: dict[str, str]) -> tuple[float, float, str, str]:
    """Return effect, within-study variance, metric, and input note."""
    metric = metric_for(row)
    n1, n0 = number(row["SHS_n"]), number(row["Healthy_n"])
    if not n1 or not n0:
        raise ValueError("missing group sample size")

    if metric == "logOR":
        match = OR_RE.search(row["Effect"])
        if not match:
            raise ValueError("OR does not contain parseable 95% CI")
        odds, lower, upper = map(float, match.groups())
        if min(odds, lower, upper) <= 0 or lower >= upper:
            raise ValueError("invalid OR or CI")
        log_effect = math.log(odds)
        se = (math.log(upper) - math.log(lower)) / (2 * 1.96)
        return log_effect, se * se, metric, "OR and 95% CI parsed; pooled on log scale"

    m1, m0 = number(row["SHS_mean"]), number(row["Healthy_mean"])
    s1, s0 = number(row["SHS_sd"]), number(row["Healthy_sd"])
    if None in (m1, m0, s1, s0):
        raise ValueError("missing mean/SD")
    if min(s1, s0) <= 0:
        raise ValueError("SD must be positive")

    if metric == "MD":
        effect = m1 - m0
        variance = (s1 * s1 / n1) + (s0 * s0 / n0)
        return effect, variance, metric, "means/SDs parsed"

    # Hedges g for OXPHOS.  This is a small-sample corrected standardized mean
    # difference; the correction is based on the two independent groups.
    df = n1 + n0 - 2
    pooled_sd = math.sqrt(((n1 - 1) * s1 * s1 + (n0 - 1) * s0 * s0) / df)
    d = (m1 - m0) / pooled_sd
    correction = 1 - 3 / (4 * df - 1)
    effect = correction * d
    variance = (n1 + n0) / (n1 * n0) + effect * effect / (2 * df)
    return effect, variance, metric, "Hedges g from means/SDs"


def reported_effect(row: dict[str, str]) -> float | None:
    match = NUMBER_RE.search(row["Effect"])
    if not match:
        return None
    value = float(match.group(0))
    return math.log(value) if metric_for(row) == "logOR" else value


def random_effects(values: list[tuple[float, float]]) -> dict[str, float]:
    if len(values) < 2:
        raise ValueError("at least two studies are needed")
    effects = [effect for effect, _ in values]
    variances = [variance for _, variance in values]
    fixed_weights = [1 / variance for variance in variances]
    fixed = sum(w * e for w, e in zip(fixed_weights, effects)) / sum(fixed_weights)
    q = sum(w * (e - fixed) ** 2 for w, e in zip(fixed_weights, effects))
    df = len(values) - 1
    correction = sum(fixed_weights) - sum(w * w for w in fixed_weights) / sum(fixed_weights)
    tau2 = max(0.0, (q - df) / correction) if correction else 0.0
    random_weights = [1 / (variance + tau2) for variance in variances]
    pooled = sum(w * e for w, e in zip(random_weights, effects)) / sum(random_weights)
    se = math.sqrt(1 / sum(random_weights))
    lower = pooled - 1.96 * se
    upper = pooled + 1.96 * se
    i2 = max(0.0, (q - df) / q * 100) if q > 0 else 0.0
    return {
        "pooled": pooled,
        "lower": lower,
        "upper": upper,
        "Q": q,
        "df": df,
        "tau2": tau2,
        "I2_percent": i2,
    }


def display_effect(value: float, metric: str) -> float:
    return math.exp(value) if metric == "logOR" else value


def main() -> None:
    with INPUT.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    grouped: dict[str, list[tuple[dict[str, str], float, float, str]]] = defaultdict(list)
    audit_rows: list[dict[str, str]] = []
    for row in rows:
        metric = metric_for(row)
        try:
            effect, variance, metric, note = study_effect(row)
            error = ""
            grouped[row["Outcome"]].append((row, effect, variance, metric))
            computed = display_effect(effect, metric)
            reported = reported_effect(row)
            discrepancy = "" if reported is None else f"{computed - display_effect(reported, metric):.6f}"
        except (ValueError, ZeroDivisionError) as exc:
            effect = variance = computed = reported = None
            note = "not computable"
            error = str(exc)
            discrepancy = ""

        audit_rows.append(
            {
                "Outcome": row["Outcome"],
                "Study": row["Study"],
                "Metric": metric,
                "Numeric_inputs_complete": str(not bool(error)),
                "Source_locator_in_study_field": str("PMC" in row["Study"]),
                "Reported_effect": row["Effect"],
                "Computed_study_effect": "" if computed is None else f"{computed:.6f}",
                "Computed_minus_first_reported_number": discrepancy,
                "Audit_status": "needs PDF/page/table verification" if "PMC" not in row["Study"] else "locator named; verify PDF/table",
                "Note": note if not error else f"{note}: {error}",
            }
        )

    summary_rows: list[dict[str, str]] = []
    for outcome, entries in grouped.items():
        metric = entries[0][3]
        result = random_effects([(effect, variance) for _, effect, variance, _ in entries])
        summary_rows.append(
            {
                "Outcome": outcome,
                "k": str(len(entries)),
                "Metric": metric,
                "Pooled_effect": f"{display_effect(result['pooled'], metric):.6f}",
                "Lower_95CI": f"{display_effect(result['lower'], metric):.6f}",
                "Upper_95CI": f"{display_effect(result['upper'], metric):.6f}",
                "I2_percent": f"{result['I2_percent']:.3f}",
                "tau2_analysis_scale": f"{result['tau2']:.8f}",
                "Q": f"{result['Q']:.6f}",
                "df": str(result["df"]),
                "Status": "provisional; do not cite as final",
            }
        )

    with AUDIT_OUT.open("w", newline="", encoding="utf-8") as handle:
        fields = list(audit_rows[0])
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(audit_rows)

    with SUMMARY_OUT.open("w", newline="", encoding="utf-8") as handle:
        fields = list(summary_rows[0])
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(summary_rows)

    print(f"Read {len(rows)} rows from {INPUT.name}")
    print(f"Wrote {AUDIT_OUT.name} and {SUMMARY_OUT.name}")
    for row in summary_rows:
        print(
            f"{row['Outcome']}: {row['Metric']} k={row['k']} "
            f"{row['Pooled_effect']} [{row['Lower_95CI']}, {row['Upper_95CI']}], "
            f"I2={row['I2_percent']}%"
        )


if __name__ == "__main__":
    main()
