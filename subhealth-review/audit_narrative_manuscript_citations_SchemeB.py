#!/usr/bin/env python3
"""Audit exact-title/PMID/DOI anchors in the source-audited manuscript."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANUSCRIPT = ROOT / "44_Source_Audited_Narrative_Review_Manuscript_SchemeB_2026-10-08.md"
OUTPUT = ROOT / "verified_reference_anchors_narrative_manuscript_SchemeB_2026-10-08.csv"

ANCHORS = [
    ("Development and evaluation of a questionnaire for measuring suboptimal health status in urban Chinese", "19749497", "https://pubmed.ncbi.nlm.nih.gov/19749497/", "10.2188/jea.je20080086", "https://doi.org/10.2188/jea.je20080086", "measurement_context"),
    ("Association of Suboptimal Health Status and Cardiovascular Risk Factors in Urban Chinese Workers", "22203493", "https://pubmed.ncbi.nlm.nih.gov/22203493/", "10.1007/s11524-011-9636-8", "https://doi.org/10.1007/s11524-011-9636-8", "direct_cortisol"),
    ("Association of suboptimal health status with psychosocial stress, plasma cortisol and mRNA expression of glucocorticoid receptor α/β in lymphocyte", "25518867", "https://pubmed.ncbi.nlm.nih.gov/25518867/", "10.3109/10253890.2014.999233", "https://doi.org/10.3109/10253890.2014.999233", "direct_cortisol"),
    ("Latent class analysis to evaluate performance of plasma cortisol, plasma catecholamines, and SHSQ-25 for early recognition of suboptimal health status", "30174765", "https://pubmed.ncbi.nlm.nih.gov/30174765/", "10.1007/s13167-018-0144-8", "https://doi.org/10.1007/s13167-018-0144-8", "direct_diagnostic_bridge"),
    ("The joint subclinical elevation of CRP and IL-6 is associated with lower health-related quality of life in comparison with no elevation or elevation of only one of the biomarkers", "26195318", "https://pubmed.ncbi.nlm.nih.gov/26195318/", "10.1007/s11136-015-1068-6", "https://doi.org/10.1007/s11136-015-1068-6", "bridge_hrqol"),
    ("Low-grade inflammation is negatively associated with physical Health-Related Quality of Life in healthy individuals: Results from The Danish Blood Donor Study (DBDS)", "30921429", "https://pubmed.ncbi.nlm.nih.gov/30921429/", "10.1371/journal.pone.0214468", "https://doi.org/10.1371/journal.pone.0214468", "bridge_hrqol"),
    ("Association of C-reactive protein and interleukin-6 with new-onset fatigue in the Whitehall II prospective cohort study", "23151405", "https://pubmed.ncbi.nlm.nih.gov/23151405/", "10.1017/S0033291712002437", "https://doi.org/10.1017/S0033291712002437", "bridge_fatigue"),
    ("Immunometabolism governs dendritic cell and macrophage function", "26694970", "https://pubmed.ncbi.nlm.nih.gov/26694970/", "10.1084/jem.20151570", "https://doi.org/10.1084/jem.20151570", "mechanistic_transfer"),
    ("The Balance of MFN2 and OPA1 in Mitochondrial Dynamics, Cellular Homeostasis, and Disease", "40149969", "https://pubmed.ncbi.nlm.nih.gov/40149969/", "10.3390/biom15030433", "https://doi.org/10.3390/biom15030433", "mechanistic_transfer"),
    ("The Phosphorylation Status of Drp1-Ser637 by PKA in Mitochondrial Fission Modulates Mitophagy via PINK1/Parkin to Exert Multipolar Spindles Assembly during Mitosis", "33805672", "https://pubmed.ncbi.nlm.nih.gov/33805672/", "10.3390/biom11030424", "https://doi.org/10.3390/biom11030424", "mechanistic_transfer"),
    ("Mitochondrial DNA Leakage and cGas/STING Pathway in Microglia: Crosstalk Between Neuroinflammation and Neurodegeneration", "38685462", "https://pubmed.ncbi.nlm.nih.gov/38685462/", "10.1016/j.neuroscience.2024.04.009", "https://doi.org/10.1016/j.neuroscience.2024.04.009", "mechanistic_transfer"),
    ("Mitochondrial Damage Causes Inflammation via cGAS-STING Signaling in Acute Kidney Injury", "31665638", "https://pubmed.ncbi.nlm.nih.gov/31665638/", "10.1016/j.celrep.2019.09.050", "https://doi.org/10.1016/j.celrep.2019.09.050", "mechanistic_transfer"),
    ("Oxidized mitochondrial DNA activates the NLRP3 inflammasome during apoptosis", "22342844", "https://pubmed.ncbi.nlm.nih.gov/22342844/", "10.1016/j.immuni.2012.01.009", "https://doi.org/10.1016/j.immuni.2012.01.009", "mechanistic_transfer"),
]


def main() -> None:
    text = MANUSCRIPT.read_text(encoding="utf-8")
    rows: list[dict[str, str]] = []
    for title, pmid, pubmed_url, doi, doi_url, role in ANCHORS:
        checks = {
            "exact_title_present": title in text,
            "pmid_present": pmid in text,
            "pubmed_url_present": pubmed_url in text,
            "doi_present": doi in text,
            "doi_url_present": doi_url in text,
        }
        rows.append({
            "exact_title": title,
            "pmid": pmid,
            "pubmed_url": pubmed_url,
            "doi": doi,
            "doi_url": doi_url,
            "role": role,
            "all_anchor_checks_pass": "PASS" if all(checks.values()) else "FAIL",
            **{key: "PASS" if value else "FAIL" for key, value in checks.items()},
        })
    forbidden_placeholders = ["CRD42026XXXXX", "Ready for Final Submission", "110 studies included"]
    for phrase in forbidden_placeholders:
        if phrase in text:
            raise SystemExit(f"Forbidden provisional phrase remains in narrative manuscript: {phrase}")
    if any(row["all_anchor_checks_pass"] != "PASS" for row in rows):
        raise SystemExit("At least one verified reference anchor is incomplete")

    fields = list(rows[0])
    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"Citation audit PASS: {len(rows)} verified anchors; output={OUTPUT}")


if __name__ == "__main__":
    main()
