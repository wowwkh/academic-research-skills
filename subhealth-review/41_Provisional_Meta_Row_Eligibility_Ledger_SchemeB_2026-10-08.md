# Provisional Meta-row eligibility ledger — Scheme B — 2026-10-08

## Purpose and rule

The historical `meta_analysis_extraction_SchemeB.csv` contains 31 provisional rows. This ledger evaluates every row without deleting the historical file. A row is not eligible for a claimable primary synthesis unless its exact article identity, PMID/PubMed link, DOI link, source outcome and source table are verified.

No PMID or DOI has been guessed for an unverified row. Empty bibliographic fields in `meta_analysis_eligibility_ledger_SchemeB_2026-10-08.csv` mean that the historical label remains unverified and has been quarantined from primary analysis.

## Result

| Legacy-row status | Number of rows | Action |
|---|---:|---|
| No exact title + PMID/PubMed + DOI verified | 24 | Quarantine; do not use in Meta or assign a guessed identifier |
| Verified article identity, but historical outcome/effect does not match | 4 | Quarantine historical effect; retain only the separately source-audited outcome if eligible |
| Verified context article, but historical cortisol/NLR cohort is not verified | 2 | Quarantine historical effect; context article is not a substitute |
| Verified direct-cortisol identity, but historical label/effect is wrong and primary pooling is blocked | 1 | Quarantine legacy row; use the PDF-audited Yan 2018 record only as separate diagnostic evidence |
| **Historical rows eligible for the final primary pooled Meta at this stage** | **0** | **No primary pooled estimate** |

The 24 unverified rows comprise: cortisol 2, NLR 5, SDNN 4, RMSSD 3, joint fatigue OR 4, SF-36 vitality 3, and OXPHOS 3. Their historical numerical values remain traceability artifacts only.

## Verified identity corrections

### Historical `Hou 2019 PMC6107457` cortisol row

**Exact title:** *Latent class analysis to evaluate performance of plasma cortisol, plasma catecholamines, and SHSQ-25 for early recognition of suboptimal health status*
**PMID/PubMed:** [30174765](https://pubmed.ncbi.nlm.nih.gov/30174765/)
**DOI:** [10.1007/s13167-018-0144-8](https://doi.org/10.1007/s13167-018-0144-8)

This is the verified 2018 Yan report, not a verified “Hou 2019” article. The supplied PDF reports 868 complete participants, LCA groups n=298/570, and cortisol values 205.80 ± 29.82 versus 161.80 ± 7.79 ng/mL. The historical n=100/100 row and CI are not source-supported. Because cortisol is one of the manifest variables used in the LCA class assignment, the verified record is retained as diagnostic/bridge evidence and is not placed in a primary etiologic cortisol pool.

### Historical `Swedish 2015` fatigue and vitality rows

**Exact title:** *The joint subclinical elevation of CRP and IL-6 is associated with lower health-related quality of life in comparison with no elevation or elevation of only one of the biomarkers*
**PMID/PubMed:** [26195318](https://pubmed.ncbi.nlm.nih.gov/26195318/)
**DOI:** [10.1007/s11136-015-1068-6](https://doi.org/10.1007/s11136-015-1068-6)

The verified source reports adjusted SF-36 contrasts, including vitality, relative to the high/high biomarker group. It does not report the historical joint-marker fatigue OR 1.85 or the historical raw SF-36 mean/SD row. The source-audited vitality bridge estimates are retained separately; the legacy rows are quarantined.

### Historical `Danish DBDS 2019` fatigue and vitality rows

**Exact title:** *Low-grade inflammation is negatively associated with physical Health-Related Quality of Life in healthy individuals: Results from The Danish Blood Donor Study (DBDS)*
**PMID/PubMed:** [30921429](https://pubmed.ncbi.nlm.nih.gov/30921429/)
**DOI:** [10.1371/journal.pone.0214468](https://doi.org/10.1371/journal.pone.0214468)

The verified source reports stratified SF-12 physical-health regression coefficients. It does not report the historical joint-marker fatigue OR 1.52 or SF-36 vitality means/SDs. The legacy fatigue and SF-36 rows are quarantined; the source-audited SF-12 bridge records remain separate. The article's correction is recorded in the PDF audit as PMID [31136577](https://pubmed.ncbi.nlm.nih.gov/31136577/) and DOI [10.1371/journal.pone.0216339](https://doi.org/10.1371/journal.pone.0216339).

### Historical `Alzain 2024b` cortisol and NLR rows

**Exact title:** *Assessing suboptimal health status in the Saudi population: Translation and validation of the SHSQ-25 questionnaire*
**PMID/PubMed:** [38305242](https://pubmed.ncbi.nlm.nih.gov/38305242/)
**DOI:** [10.7189/jogh.14.04030](https://doi.org/10.7189/jogh.14.04030)

This verified context record is a questionnaire translation/validation paper. It does not verify the historical cortisol or NLR effect rows labelled “Alzain 2024b.” The context paper cannot substitute for an exact biomarker article, so both historical rows remain quarantined.

## Row-level actions

The complete row-level decisions, including the legacy outcome, historical effect label, verification status, exact metadata where available, reason and required action, are in:

- `meta_analysis_eligibility_ledger_SchemeB_2026-10-08.csv`

The historical 31-row file is intentionally preserved. It must not be used as the final quantitative input without applying this ledger and the cohort/estimand decision in `40_Cohort_Reconciliation_Yan_Direct_Cortisol_SchemeB_2026-10-08.md`.

## Primary analysis consequence

The current evidence state has no defensible primary pooled direct-cortisol estimate and no verified basis for the historical NLR, HRV, OXPHOS or fatigue Meta rows. The next quantitative input should contain only source-audited rows that satisfy the final eligibility rule. If no independent direct-cortisol cohorts can be established, the direct cortisol synthesis should remain narrative, with the existing pooled calculation labelled exploratory in an appendix rather than reported as the primary result.
