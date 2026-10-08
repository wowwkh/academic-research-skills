# Source-audited Meta reconciliation and analysis decision — Scheme B — 2026-10-08

## Purpose

This report is the first analysis decision after the 11 supplied PDFs became readable. It distinguishes source-verified study-level estimates from the historical 31-row provisional Meta input. It does **not** silently replace the historical results with a pooled estimate that violates the protocol.

## Source-audited direct cortisol records

### 1. Yan 2015

**Exact title:** *Association of suboptimal health status with psychosocial stress, plasma cortisol and mRNA expression of glucocorticoid receptor α/β in lymphocyte*
**PMID/PubMed:** [25518867](https://pubmed.ncbi.nlm.nih.gov/25518867/)
**DOI:** [10.3109/10253890.2014.999233](https://doi.org/10.3109/10253890.2014.999233)
**PDF locator:** p. 6, Table 4.

- High SHS: n=193, 178.58 ± 18.25 ng/mL.
- Low SHS: n=189, 167.77 ± 12.25 ng/mL.
- Derived MD: 10.81 ng/mL; derived 95% CI 7.70 to 13.92.
- The table reports adjusted means/SDs and `p<0.001`; the derived CI is not author-reported.

### 2. Yan 2012

**Exact title:** *Association of Suboptimal Health Status and Cardiovascular Risk Factors in Urban Chinese Workers*
**PMID/PubMed:** [22203493](https://pubmed.ncbi.nlm.nih.gov/22203493/)
**DOI:** [10.1007/s11524-011-9636-8](https://doi.org/10.1007/s11524-011-9636-8)
**PDF locator:** p. 6, Table 2; group sizes from Table 1.

- High SHS-score group: n=1,547, 204.31 ± 40.06 ng/mL.
- Low SHS-score group: n=1,472, 161.33 ± 27.83 ng/mL.
- Derived MD: 42.98 ng/mL; derived 95% CI 40.53 to 45.43.
- The grouping cut point is the sample median SHS score 44, not the canonical SHSQ-25 ≥35 threshold.
- The source reports `t=34.076`, `p<0.001`.

### 3. Yan 2018

**Exact title:** *Latent class analysis to evaluate performance of plasma cortisol, plasma catecholamines, and SHSQ-25 for early recognition of suboptimal health status*
**PMID/PubMed:** [30174765](https://pubmed.ncbi.nlm.nih.gov/30174765/)
**DOI:** [10.1007/s13167-018-0144-8](https://doi.org/10.1007/s13167-018-0144-8)
**PDF locator:** p. 4, Table 2 and Results section.

- LCA-defined SHS: n=298, 205.80 ± 29.82 ng/mL.
- LCA-defined health: n=570, 161.80 ± 7.79 ng/mL.
- Derived MD: 44.00 ng/mL; derived 95% CI 40.55 to 47.45.
- The source reports LCA SHS prevalence 34.78% and a cortisol cutoff of 180 ng/mL.

## Why a primary pooled cortisol estimate is not yet defensible

The three records are not exchangeable study arms:

1. SHS definitions differ: median score 35, median score 44, and LCA-defined status.
2. Yan 2015 reports covariate-adjusted Table 4 values; Yan 2012 reports a raw group comparison; Yan 2018 reports LCA-classified groups.
3. The Beijing occupational populations may overlap, but the source PDFs do not establish independent cohorts.
4. A pooled result would therefore risk double-counting participants and mixing incompatible estimands.

## Exploratory calculation, not a final result

For transparency only, a DerSimonian–Laird random-effects calculation was run on the three study-level MDs using the independent-group approximation for each derived variance:

- Exploratory MD: **32.60 ng/mL**
- 95% CI: **11.64 to 53.56**
- Q: **297.33**, df=2
- I²: **99.3%**
- Tau²: **340.84**

This result is labelled **exploratory only** and must not replace the historical or final Meta result. The very high heterogeneity supports the decision not to report a primary pooled direct-cortisol estimate until cohort identity and SHS definition are reconciled.

Leave-one-out sensitivity results are also recorded in `meta_analysis_source_audited_results_SchemeB_2026-10-08.csv`; they range from approximately MD 26.91 to 43.32 and remain unstable when one report is removed.

## Bridge evidence decisions

The supplied PDFs also verify bridge evidence, but these estimands are not pooled with direct SHS/cortisol data:

- Dinh et al. — *Low-grade inflammation is negatively associated with physical Health-Related Quality of Life in healthy individuals: Results from The Danish Blood Donor Study (DBDS)*; PMID [30921429](https://pubmed.ncbi.nlm.nih.gov/30921429/); DOI [10.1371/journal.pone.0214468](https://doi.org/10.1371/journal.pone.0214468). Reports stratified SF-12 PCS regression coefficients, not SHSQ-25 or fatigue.
- Garvin et al. — *The joint subclinical elevation of CRP and IL-6 is associated with lower health-related quality of life in comparison with no elevation or elevation of only one of the biomarkers*; PMID [26195318](https://pubmed.ncbi.nlm.nih.gov/26195318/); DOI [10.1007/s11136-015-1068-6](https://doi.org/10.1007/s11136-015-1068-6). Reports adjusted SF-36 contrasts, not raw SHS group means.
- Cho et al. — *Association of C-reactive protein and interleukin-6 with new-onset fatigue in the Whitehall II prospective cohort study*; PMID [23151405](https://pubmed.ncbi.nlm.nih.gov/23151405/); DOI [10.1017/S0033291712002437](https://doi.org/10.1017/S0033291712002437). Reports separate CRP and IL-6 fatigue ORs, not the historical unsupported joint-marker OR 1.60.

These are retained as narrative bridge evidence and separately graded in `GRADE_Summary_of_Findings_SchemeB_source_audited_2026-10-08.csv`.

## Files generated or updated

- `meta_analysis_verified_online_extraction_SchemeB_2026-10-08.csv` — now includes PDF page locators, SHA-256, page count, and `pypdf_complete` status.
- `meta_analysis_source_audited_results_SchemeB_2026-10-08.csv` — study-level effects, exploratory pool, and leave-one-out results.
- `GRADE_Summary_of_Findings_SchemeB_source_audited_2026-10-08.csv` — source-audited certainty decisions.
- `FigS2_Forest_Cortisol_SourceAudited_Exploratory.png/pdf` — explicitly labelled exploratory forest plot.
- `recompute_source_audited_meta_SchemeB.py` — reproducible direct-cortisol sensitivity calculation.
- `generate_source_audited_cortisol_forest.py` — forest-plot generator.
- `38_PDF_Byte_Extraction_Audit_SchemeB_2026-10-08.md` — PDF manifest and page/table audit.

The historical 31-row CSV, old forest plots, old GRADE table, and manuscript numerical claims remain in the repository for traceability but are not promoted as final evidence.

## Next analytical gate

Before changing the primary Meta results, complete a cohort-reconciliation table for the three Yan reports: recruitment years, companies, health-centre source, participant IDs or overlap evidence, cortisol sampling time, assay, and the exact SHS classification. If independent cohorts cannot be established, use one study per cohort or a narrative synthesis rather than a naïve pooled estimate.
