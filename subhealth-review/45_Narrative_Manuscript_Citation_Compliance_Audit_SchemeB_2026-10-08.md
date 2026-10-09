# Narrative manuscript citation-compliance audit — Scheme B — 2026-10-08

## Scope

This audit applies to `44_Source_Audited_Narrative_Review_Manuscript_SchemeB_2026-10-08.md`, not to the historical provisional manuscript. It checks the active bibliographic acceptance rule: every literature item presented for checking must have an exact article title, PMID/PubMed link and DOI link.

## Automated result

The audit script `audit_narrative_manuscript_citations_SchemeB.py` passed on 2026-10-08:

- verified reference anchors checked: **13**;
- exact titles present: **13/13**;
- PMID and PubMed URLs present: **13/13**;
- DOI strings and DOI URLs present: **13/13**;
- provisional placeholder `CRD42026XXXXX` in the narrative manuscript: **absent**;
- historical “Ready for Final Submission” status in the narrative manuscript: **absent**;
- historical “110 studies included” claim in the narrative manuscript: **absent**;
- primary pooled direct-cortisol rows in the locked evidence map: **0**.

The machine-readable anchor table is `verified_reference_anchors_narrative_manuscript_SchemeB_2026-10-08.csv`.

## Verified anchor inventory

The 13 anchors are divided into one measurement-context source, three direct cortisol records, two low-grade-inflammation/HRQoL bridge records, one inflammation/fatigue bridge record and six mechanistic transfer sources. Each row in the CSV contains the exact title, PMID, PubMed URL, DOI and DOI URL.

### Measurement context

- *Development and evaluation of a questionnaire for measuring suboptimal health status in urban Chinese* — PMID [19749497](https://pubmed.ncbi.nlm.nih.gov/19749497/); DOI [10.2188/jea.je20080086](https://doi.org/10.2188/jea.je20080086).

### Direct cortisol

- *Association of Suboptimal Health Status and Cardiovascular Risk Factors in Urban Chinese Workers* — PMID [22203493](https://pubmed.ncbi.nlm.nih.gov/22203493/); DOI [10.1007/s11524-011-9636-8](https://doi.org/10.1007/s11524-011-9636-8).
- *Association of suboptimal health status with psychosocial stress, plasma cortisol and mRNA expression of glucocorticoid receptor α/β in lymphocyte* — PMID [25518867](https://pubmed.ncbi.nlm.nih.gov/25518867/); DOI [10.3109/10253890.2014.999233](https://doi.org/10.3109/10253890.2014.999233).
- *Latent class analysis to evaluate performance of plasma cortisol, plasma catecholamines, and SHSQ-25 for early recognition of suboptimal health status* — PMID [30174765](https://pubmed.ncbi.nlm.nih.gov/30174765/); DOI [10.1007/s13167-018-0144-8](https://doi.org/10.1007/s13167-018-0144-8).

### Bridge evidence

- *The joint subclinical elevation of CRP and IL-6 is associated with lower health-related quality of life in comparison with no elevation or elevation of only one of the biomarkers* — PMID [26195318](https://pubmed.ncbi.nlm.nih.gov/26195318/); DOI [10.1007/s11136-015-1068-6](https://doi.org/10.1007/s11136-015-1068-6).
- *Low-grade inflammation is negatively associated with physical Health-Related Quality of Life in healthy individuals: Results from The Danish Blood Donor Study (DBDS)* — PMID [30921429](https://pubmed.ncbi.nlm.nih.gov/30921429/); DOI [10.1371/journal.pone.0214468](https://doi.org/10.1371/journal.pone.0214468).
- *Association of C-reactive protein and interleukin-6 with new-onset fatigue in the Whitehall II prospective cohort study* — PMID [23151405](https://pubmed.ncbi.nlm.nih.gov/23151405/); DOI [10.1017/S0033291712002437](https://doi.org/10.1017/S0033291712002437).

### Mechanistic transfer anchors

- *Immunometabolism governs dendritic cell and macrophage function* — PMID [26694970](https://pubmed.ncbi.nlm.nih.gov/26694970/); DOI [10.1084/jem.20151570](https://doi.org/10.1084/jem.20151570).
- *The Balance of MFN2 and OPA1 in Mitochondrial Dynamics, Cellular Homeostasis, and Disease* — PMID [40149969](https://pubmed.ncbi.nlm.nih.gov/40149969/); DOI [10.3390/biom15030433](https://doi.org/10.3390/biom15030433).
- *The Phosphorylation Status of Drp1-Ser637 by PKA in Mitochondrial Fission Modulates Mitophagy via PINK1/Parkin to Exert Multipolar Spindles Assembly during Mitosis* — PMID [33805672](https://pubmed.ncbi.nlm.nih.gov/33805672/); DOI [10.3390/biom11030424](https://doi.org/10.3390/biom11030424).
- *Mitochondrial DNA Leakage and cGas/STING Pathway in Microglia: Crosstalk Between Neuroinflammation and Neurodegeneration* — PMID [38685462](https://pubmed.ncbi.nlm.nih.gov/38685462/); DOI [10.1016/j.neuroscience.2024.04.009](https://doi.org/10.1016/j.neuroscience.2024.04.009).
- *Mitochondrial Damage Causes Inflammation via cGAS-STING Signaling in Acute Kidney Injury* — PMID [31665638](https://pubmed.ncbi.nlm.nih.gov/31665638/); DOI [10.1016/j.celrep.2019.09.050](https://doi.org/10.1016/j.celrep.2019.09.050).
- *Oxidized mitochondrial DNA activates the NLRP3 inflammasome during apoptosis* — PMID [22342844](https://pubmed.ncbi.nlm.nih.gov/22342844/); DOI [10.1016/j.immuni.2012.01.009](https://doi.org/10.1016/j.immuni.2012.01.009).

## Content-level checks

- The direct cortisol numbers in the manuscript are labelled derived when they are not author-reported CIs.
- The exploratory pooled MD and I² are labelled exploratory and are not presented as the primary result.
- The 2018 LCA result is labelled diagnostic/bridge because cortisol is part of class assignment.
- The Swedish, Danish and Whitehall sources are labelled bridge evidence and are not mixed with direct SHS/cortisol data.
- Mitochondrial dynamics, immune-metabolic reprogramming and SLIM thresholds are explicitly marked as hypotheses or research priorities because they are not measured in the current SHSQ-25 source-audited records.
- The narrative manuscript does not claim a completed four-database search, dual screening, PROSPERO registration or a final 110-study evidence base.

## Remaining citation work before submission

This audit passes for the current source-audited manuscript, but it is not a substitute for the final systematic-review citation audit. Before submission, every additional mechanistic, multi-omic, intervention or validation reference added to the manuscript must be entered with the same exact-title/PMID/DOI rule. The historical 110-reference bibliography remains provisional until each item is re-verified.
