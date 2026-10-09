# Attachment identity and online extraction addendum — Scheme B — 2026-10-08

## Scope and evidence state

This addendum records the 11 PDF filenames supplied by the user. Initially the PDF bytes were not mounted, so the first version used PubMed/PMC/publisher verification. The user subsequently uploaded `subhealth_pdfs_2026-10-08.zip` to the GitHub branch; all 11 PDFs were then extracted successfully. The byte-level manifest, SHA-256 values, PDF page locators, and updated findings are now recorded in `38_PDF_Byte_Extraction_Audit_SchemeB_2026-10-08.md`.

The companion CSV contains the quantitative extraction rows. These rows are an **audited extraction addendum**; they do not overwrite `meta_analysis_extraction_SchemeB.csv`, the historical provisional input. The historical CSV and its forest plots remain provisional until outcome harmonisation, cohort-overlap checking, and a reproducible re-analysis are complete.

Rules applied:

1. No PMID, DOI, title, or effect was guessed from a filename.
2. Every verified article below has an exact title, a PubMed link, and a DOI link.
3. A record that is identifiable but not eligible for the direct SHSQ-25 meta-analysis is labelled `bridge`, `context`, or `exclude-unrelated`.
4. `file.pdf` is now verified as the Dinh et al. Danish Blood Donor Study paper; its PDF hash and Table 4 locator are recorded in file 38.
5. Derived mean differences and confidence intervals are explicitly labelled as derived and are not silently substituted into the historical meta-analysis.

## Attachment-to-article identity inventory

### 1. `1-s2.0-S0022399917310899-main.pdf`

- **Identity status:** verified.
- **Exact article title:** *Impaired mental health and low-grade inflammation among fatigued bereaved individuals*.
- **PMID/PubMed:** [30097134](https://pubmed.ncbi.nlm.nih.gov/30097134/).
- **DOI:** [10.1016/j.jpsychores.2018.06.010](https://doi.org/10.1016/j.jpsychores.2018.06.010).
- **Journal/year:** *Journal of Psychosomatic Research*, 2018;112:40-46.
- **Design and relevance:** bereaved-adult cross-sectional fatigue/inflammation study; SF-36 energy/vitality and CRP/IL-6/TNF-α. It is a mechanistic bridge, not an SHSQ-25 cohort.
- **Online verification:** ScienceDirect article preview and PubMed abstract identify 78 bereaved adults and the fatigue-group definition; no table-level mean/SD suitable for the direct SHS cortisol pool was entered.

### 2. `19_333.pdf`

- **Identity status:** verified.
- **Exact article title:** *Development and evaluation of a questionnaire for measuring suboptimal health status in urban Chinese*.
- **PMID/PubMed:** [19749497](https://pubmed.ncbi.nlm.nih.gov/19749497/).
- **DOI:** [10.2188/jea.je20080086](https://doi.org/10.2188/jea.je20080086).
- **Journal/year:** *Journal of Epidemiology*, 2009;19(6):333-341.
- **Design and relevance:** questionnaire development/validation; SHSQ-25 origin, five domains, reliability and validity. It is a definition/context record, not a cortisol meta-analysis row.
- **Online verification:** PubMed abstract reports the 25-item instrument, 2,799 completed questionnaires from a 3,000-person study, and the validation results.

### 3. `Association of suboptimal health status with psychosocial stress  plasma cortisol and mRNA expression of glucocorticoid receptor     in lymphocyte.pdf`

- **Identity status:** verified.
- **Exact article title:** *Association of suboptimal health status with psychosocial stress, plasma cortisol and mRNA expression of glucocorticoid receptor α/β in lymphocyte*.
- **PMID/PubMed:** [25518867](https://pubmed.ncbi.nlm.nih.gov/25518867/).
- **DOI:** [10.3109/10253890.2014.999233](https://doi.org/10.3109/10253890.2014.999233).
- **Journal/year:** *Stress*, 2015;18(1):29-34.
- **Design and relevance:** cross-sectional study of workers in three Beijing companies; direct SHSQ-25/high-versus-low SHS cortisol and glucocorticoid-receptor evidence.
- **Online table extraction:** publisher full-text/PDF search exposes Table 4: high SHS, n=193, plasma cortisol 178.58 ± 18.25 ng/mL; low SHS, n=189, 167.77 ± 12.25 ng/mL; `p < 0.001`. The four cortisol outliers were excluded from the 386 recruited workers, leaving 382 for this analysis.

### 4. `file.pdf`

- **Identity status:** verified after byte-level extraction.
- **Exact article title:** *Low-grade inflammation is negatively associated with physical Health-Related Quality of Life in healthy individuals: Results from The Danish Blood Donor Study (DBDS)*.
- **PMID/PubMed:** [30921429](https://pubmed.ncbi.nlm.nih.gov/30921429/).
- **DOI:** [10.1371/journal.pone.0214468](https://doi.org/10.1371/journal.pone.0214468).
- **PDF locator:** abstract on PDF p. 1; multivariable regression Table 4 on PDF p. 8.
- **Action:** retain as a low-grade-inflammation/SF-12 bridge record, not as an SHSQ-25 or fatigue-OR row. The separate correction is PMID [31136577](https://pubmed.ncbi.nlm.nih.gov/31136577/), DOI [10.1371/journal.pone.0216339](https://doi.org/10.1371/journal.pone.0216339).

### 5. `ijerph16173007.pdf`

- **Identity status:** verified identity, but unrelated to the target review and excluded.
- **Exact article title:** *Migration, Work, and Health: Lessons Learned from a Clinical Case Series in a Northern Italy Public Hospital*.
- **PMID/PubMed:** [31438461](https://pubmed.ncbi.nlm.nih.gov/31438461/).
- **DOI:** [10.3390/ijerph16173007](https://doi.org/10.3390/ijerph16173007).
- **Journal/year:** *International Journal of Environmental Research and Public Health*, 2019;16(17):3007.
- **Action:** this DOI/file is not a SHS/cortisol paper and must not be used for the current cortisol row or any SHSQ-25 claim.

### 6. `jogh-12-04077.pdf`

- **Identity status:** verified.
- **Exact article title:** *Translation and cross-cultural validation of a precision health tool, the Suboptimal Health Status Questionnaire-25, in Korean*.
- **PMID/PubMed:** [36181723](https://pubmed.ncbi.nlm.nih.gov/36181723/).
- **DOI:** [10.7189/jogh.12.04077](https://doi.org/10.7189/jogh.12.04077).
- **Journal/year:** *Journal of Global Health*, 2022;12:04077.
- **Design and relevance:** Korean SHSQ-25 translation/cross-cultural validation; context/definition evidence, not a direct cortisol/NLR/HRV effect row.
- **Online verification:** PMC full text is available at [PMC9526479](https://pmc.ncbi.nlm.nih.gov/articles/PMC9526479/).

### 7. `jogh-14-04030.pdf`

- **Identity status:** verified.
- **Exact article title:** *Assessing suboptimal health status in the Saudi population: Translation and validation of the SHSQ-25 questionnaire*.
- **PMID/PubMed:** [38305242](https://pubmed.ncbi.nlm.nih.gov/38305242/).
- **DOI:** [10.7189/jogh.14.04030](https://doi.org/10.7189/jogh.14.04030).
- **Journal/year:** *Journal of Global Health*, 2024;14:04030.
- **Design and relevance:** Arabic/Saudi SHSQ-25 translation and validation; context/definition evidence, not the unverified “Alzain 2024b NLR/HRV/cortisol cohort.”
- **Online verification:** PMC full text is available at [PMC10836270](https://pmc.ncbi.nlm.nih.gov/articles/PMC10836270/).

### 8. `s11136-015-1068-6.pdf`

- **Identity status:** verified.
- **Exact article title:** *The joint subclinical elevation of CRP and IL-6 is associated with lower health-related quality of life in comparison with no elevation or elevation of only one of the biomarkers*.
- **PMID/PubMed:** [26195318](https://pubmed.ncbi.nlm.nih.gov/26195318/).
- **DOI:** [10.1007/s11136-015-1068-6](https://doi.org/10.1007/s11136-015-1068-6).
- **Journal/year:** *Quality of Life Research*, 2016;25:213-221 (published online 2015).
- **Design and relevance:** Swedish population study; low-grade inflammation/SF-36 bridge evidence, not SHSQ-25.
- **Online table extraction:** PMC Table 1 reports n=905 overall and the joint-marker complete-case groups: high CRP/low IL-6 n=66, low CRP/high IL-6 n=52, low CRP/low IL-6 n=355, high CRP/high IL-6 n=61. Table 4 reports adjusted SF-36 contrasts versus high/high; the vitality Model-b contrasts are +11.3, +9.9, and +6.1 points for high-CRP/low-IL-6, low-CRP/high-IL-6, and low/low, respectively. These are regression contrasts, not interchangeable raw group means.

### 9. `s11524-011-9636-8.pdf`

- **Identity status:** verified.
- **Exact article title:** *Association of Suboptimal Health Status and Cardiovascular Risk Factors in Urban Chinese Workers*.
- **PMID/PubMed:** [22203493](https://pubmed.ncbi.nlm.nih.gov/22203493/).
- **DOI:** [10.1007/s11524-011-9636-8](https://doi.org/10.1007/s11524-011-9636-8).
- **Journal/year:** *Journal of Urban Health*, 2012;89(2):329-338.
- **Design and relevance:** cross-sectional urban Chinese worker study; direct SHSQ-25/cortisol evidence, with SHS grouped at the sample median score of 44 rather than the canonical ≥35 threshold.
- **Online table extraction:** PMC Table 1 gives high-score n=1,547 and low-score n=1,472 among the 3,019 participants with complete questionnaire/laboratory data. Table 2 reports cortisol 204.31 ± 40.06 ng/mL versus 161.33 ± 27.83 ng/mL, respectively; `t=34.076`, `p<0.001`.

### 10. `s13167-018-0144-8.pdf`

- **Identity status:** verified.
- **Exact article title:** *Latent class analysis to evaluate performance of plasma cortisol, plasma catecholamines, and SHSQ-25 for early recognition of suboptimal health status*.
- **PMID/PubMed:** [30174765](https://pubmed.ncbi.nlm.nih.gov/30174765/).
- **DOI:** [10.1007/s13167-018-0144-8](https://doi.org/10.1007/s13167-018-0144-8).
- **Journal/year:** *EPMA Journal*, 2018;9(3):299-305.
- **Design and relevance:** cross-sectional Beijing employee study using latent class analysis; direct SHSQ-25/plasma cortisol evidence.
- **Online table extraction:** PMC Table 2 and the Results text report LCA-defined SHS n=298, cortisol 205.80 ± 29.82 ng/mL, and health-status n=570, cortisol 161.80 ± 7.79 ng/mL. The LCA-defined SHS prevalence is 34.78%; the article also reports an estimated cortisol cutoff of 180 ng/mL. The project’s earlier `Hou 2019` label and `10.3390/ijerph16173007` DOI were incorrect; this record is the verified source.

### 11. `S0033291712002437.pdf`

- **Identity status:** verified.
- **Exact article title:** *Association of C-reactive protein and interleukin-6 with new-onset fatigue in the Whitehall II prospective cohort study*.
- **PMID/PubMed:** [23151405](https://pubmed.ncbi.nlm.nih.gov/23151405/).
- **DOI:** [10.1017/S0033291712002437](https://doi.org/10.1017/S0033291712002437).
- **Journal/year:** *Psychological Medicine*, 2013;43(8):1773-1783.
- **Design and relevance:** prospective fatigue/inflammation bridge cohort; not SHSQ-25 and not a direct mitochondrial/OXPHOS study.
- **Online table extraction:** fully adjusted Table 4 reports new-onset fatigue OR 1.28 (95% CI 1.09-1.49) for CRP ≥1.0 versus <1.0 mg/L (`n=4,689`) and OR 1.24 (95% CI 1.06-1.45) for IL-6 ≥1.5 versus <1.5 pg/mL (`n=4,654`). These are separate-marker adjusted ORs, not the unverified joint-marker OR 1.60.

## Quantitative rows verified from online full text

The companion CSV contains one row per estimand and preserves the distinction between reported values and derived values. Direct SHS rows currently verified are:

| Record | Exact title | PMID / DOI | Direct SHS definition | Group data | Effect handling |
|---|---|---|---|---|---|
| Yan 2015 | *Association of suboptimal health status with psychosocial stress, plasma cortisol and mRNA expression of glucocorticoid receptor α/β in lymphocyte* | [25518867](https://pubmed.ncbi.nlm.nih.gov/25518867/) / [10.3109/10253890.2014.999233](https://doi.org/10.3109/10253890.2014.999233) | SHS score ≥35 vs <35 after median split | n=193, 178.58 ± 18.25 vs n=189, 167.77 ± 12.25 ng/mL | MD and CI are derived from the reported means/SDs; source reports `p<0.001`, not this CI |
| Yan 2012 | *Association of Suboptimal Health Status and Cardiovascular Risk Factors in Urban Chinese Workers* | [22203493](https://pubmed.ncbi.nlm.nih.gov/22203493/) / [10.1007/s11524-011-9636-8](https://doi.org/10.1007/s11524-011-9636-8) | Sample-median SHS score ≥44 vs <44 | n=1,547, 204.31 ± 40.06 vs n=1,472, 161.33 ± 27.83 ng/mL | MD and CI are derived; source reports `t=34.076`, `p<0.001` |
| Yan 2018 | *Latent class analysis to evaluate performance of plasma cortisol, plasma catecholamines, and SHSQ-25 for early recognition of suboptimal health status* | [30174765](https://pubmed.ncbi.nlm.nih.gov/30174765/) / [10.1007/s13167-018-0144-8](https://doi.org/10.1007/s13167-018-0144-8) | LCA-defined SHS vs health status; SHSQ-25 is one manifest indicator | n=298, 205.80 ± 29.82 vs n=570, 161.80 ± 7.79 ng/mL | MD and CI are derived; source reports the group means/SDs and LCA performance |

These three direct rows should **not yet be pooled as independent studies** without checking cohort overlap, cortisol sampling/assay comparability, and the non-equivalent SHS grouping rules. The 2012 and 2015 reports are from related Beijing occupational research; the LCA-defined 2018 classification is methodologically different.

## Calculation convention for derived direct rows

For the three direct cortisol rows only, the addendum’s derived values use the transparent independent-group approximation:

```text
MD = mean_high_SHS − mean_reference
SE(MD) = sqrt(SD_high_SHS² / n_high_SHS + SD_reference² / n_reference)
95% CI = MD ± 1.96 × SE(MD)
```

This is a reproducibility aid, not a replacement for author-reported adjusted estimates. The exact derived values are in the CSV, with `effect_status=derived_not_author_reported`.

## What remains blocked

- No unverified Liu 2024, Zhang 2024, Alzain 2024b NLR/HRV/cortisol, Chen 2024 NLR, SHS HRV, or SHS PBMC-Seahorse row is promoted into the analysis by this addendum.
- `meta_analysis_extraction_SchemeB.csv`, historical forest plots, `GRADE_Summary_of_Findings_SchemeB.csv`, and prose numerical claims remain provisional and must not be described as final evidence.
- The three direct cortisol rows require cohort-overlap checking, harmonisation of SHS definitions, assay timing/unit review, and a fresh reproducible pooled analysis before they can replace the historical provisional results.

## Required next input

No further upload is required for the 11 supplied PDFs. The immediate next research step is a data-reconciliation pass: decide which verified direct and bridge estimands meet the protocol, remove invalid historical rows, then regenerate Meta, forest plots, GRADE, and numerical prose. The raw ZIP is retained only in Git history for provenance and should not remain as a permanent public source artifact.
