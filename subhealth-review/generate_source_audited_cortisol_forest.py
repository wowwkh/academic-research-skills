#!/usr/bin/env python3
"""Generate an explicitly exploratory forest plot from PDF-audited cortisol rows."""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "meta_analysis_source_audited_results_SchemeB_2026-10-08.csv"
PNG = ROOT / "FigS2_Forest_Cortisol_SourceAudited_Exploratory.png"
PDF = ROOT / "FigS2_Forest_Cortisol_SourceAudited_Exploratory.pdf"


def main() -> None:
    with INPUT.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    studies = [row for row in rows if row["result_type"] == "study_effect"]
    pooled = next(row for row in rows if row["result_type"] == "exploratory_random_effects_pool")

    labels = [
        "Yan 2015\nSHS ≥35 vs <35",
        "Yan 2012\nmedian SHS 44",
        "Yan 2018\nLCA; cortisol included",
    ]
    y = list(range(len(studies), 0, -1))
    effects = [float(row["effect"]) for row in studies]
    lows = [float(row["lower_95ci"]) for row in studies]
    highs = [float(row["upper_95ci"]) for row in studies]
    pooled_effect = float(pooled["effect"])
    pooled_low = float(pooled["lower_95ci"])
    pooled_high = float(pooled["upper_95ci"])

    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    for yi, effect, low, high, label, row in zip(y, effects, lows, highs, labels, studies):
        ax.plot([low, high], [yi, yi], color="#2f5597", linewidth=1.6, zorder=2)
        ax.scatter([effect], [yi], color="#2f5597", s=55, marker="s", zorder=3)
        ax.text(0.01, yi, label, transform=ax.get_yaxis_transform(), ha="left", va="center", fontsize=9)
        ax.text(0.99, yi, f"{effect:.2f} [{low:.2f}, {high:.2f}]", transform=ax.get_yaxis_transform(), ha="right", va="center", fontsize=9)

    py = 0
    ax.plot([pooled_low, pooled_high], [py, py], color="#b22222", linewidth=2.4, zorder=2)
    ax.scatter([pooled_effect], [py], color="#b22222", s=100, marker="D", zorder=3)
    ax.text(0.01, py, "Exploratory random effects\n(not primary)", transform=ax.get_yaxis_transform(), ha="left", va="center", fontsize=9, fontweight="bold")
    ax.text(0.99, py, f"{pooled_effect:.2f} [{pooled_low:.2f}, {pooled_high:.2f}]", transform=ax.get_yaxis_transform(), ha="right", va="center", fontsize=9, fontweight="bold")

    ax.axvline(0, color="black", linewidth=0.9)
    ax.set_yticks([0, *y])
    ax.set_yticklabels(["", "", "", ""])
    ax.set_ylim(-0.8, len(studies) + 0.8)
    ax.set_xlabel("Mean difference in cortisol (ng/mL; reported SHS/LCA group minus reference)")
    ax.set_title("Source-audited direct SHS/cortisol evidence\nExploratory only: mixed estimands, possible cohort overlap, and LCA incorporation", fontsize=11, pad=12)
    ax.text(0.5, -0.16, "Study-level CIs are derived from PDF-reported means/SDs. Yan 2018 uses cortisol in LCA class assignment. Pool: Q=297.33, I²=99.3%; do not cite as a final pooled estimate.", transform=ax.transAxes, ha="center", va="top", fontsize=8, color="#555555")
    ax.grid(axis="x", linestyle=":", linewidth=0.7, alpha=0.65)
    fig.tight_layout(rect=(0, 0.08, 1, 1))
    fig.savefig(PNG, dpi=300)
    fig.savefig(PDF)
    plt.close(fig)
    print(PNG)
    print(PDF)


if __name__ == "__main__":
    main()
