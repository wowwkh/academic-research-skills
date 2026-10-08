# Manuscript source audit and safe replacement package — Scheme B — 2026-10-08

## Status

The historical manuscript files, especially `31_Final_Systematic_Meta_Complete_Viewable_SchemeB_2026-09-14.md`, are **not submission-ready** after the PDF and cohort audit. They remain preserved for traceability. This package identifies the claims that must be embargoed and supplies a source-audited replacement for the abstract and core evidence paragraph.

The current state is a verified evidence audit and locked narrative synthesis, not a completed final systematic review. The historical PRISMA counts, 110-study total, 31-row Meta input, and seven-forest-plot package must not be described as final until the search export, deduplication log, dual-screening record and full-text eligibility ledger are independently completed.

## High-risk claim audit

| Historical manuscript claim or section | Audit status | Required disposition |
|---|---|---|
| “Ready for Final Submission” and “Systematic upgrade DONE” | Invalidated by source audit | Change to audit hold; retain the historical file unchanged and use this replacement package |
| PRISMA flow 1380 → 890 → 230 → 110 and “110 studies included” | Not supported by a completed auditable screening package in the current repository | Do not report as final; regenerate only after database exports, deduplication and dual screening are available |
| Cortisol Meta: 4 studies, MD 36.5 ng/mL, I²=68%, GRADE Moderate | Replaced by three PDF-audited reports with unresolved cohort independence and non-equivalent estimands | Report study-level values narratively; keep MD 32.60 ng/mL as exploratory only, I²=99.3%, GRADE Very low |
| NLR, HRV, fatigue OR, SF-36 vitality and OXPHOS pooled results | Historical rows lack verified identities or have outcome/effect mismatches | Quarantine all historical rows through `meta_analysis_eligibility_ledger_SchemeB_2026-10-08.csv` |
| Historical joint-marker fatigue OR 1.60 and SF-36 MD −8.2 | Not supported by the verified bridge PDFs as entered | Remove from quantitative claims; retain only source-audited, outcome-specific bridge results |
| Saudi prevalence 23.7% and SHSQ-25 α=0.918 | The Saudi validation article is verified, but it is context/validation evidence, not proof of a separate cortisol/NLR cohort | Use only as validation/context, with exact source identity; do not attach the historical biomarker effects |
| Quantitative SLIM thresholds such as OXPHOS decline 10–20%, 20–40% and >50% | Hypothesis/model parameters, not source-audited SHS estimates | Label as proposed thresholds requiring prospective validation; do not place in the Results as observed effects |
| “PROSPERO CRD42026XXXXX” | Placeholder, not a registration number | State “protocol registration pending” only until an actual record exists |
| Claims of dual screening, ROBINS-I/NOS distributions and GRADE for 110 studies | Not reproducible from the present source-audited files | Remove from final Results until the corresponding screening and risk-of-bias records exist |

## Verified bibliographic anchors for the replacement evidence paragraph

### Direct SHS/cortisol records

1. **Exact title:** *Association of Suboptimal Health Status and Cardiovascular Risk Factors in Urban Chinese Workers*
   **PMID/PubMed:** [22203493](https://pubmed.ncbi.nlm.nih.gov/22203493/)
   **DOI:** [10.1007/s11524-011-9636-8](https://doi.org/10.1007/s11524-011-9636-8)

2. **Exact title:** *Association of suboptimal health status with psychosocial stress, plasma cortisol and mRNA expression of glucocorticoid receptor α/β in lymphocyte*
   **PMID/PubMed:** [25518867](https://pubmed.ncbi.nlm.nih.gov/25518867/)
   **DOI:** [10.3109/10253890.2014.999233](https://doi.org/10.3109/10253890.2014.999233)

3. **Exact title:** *Latent class analysis to evaluate performance of plasma cortisol, plasma catecholamines, and SHSQ-25 for early recognition of suboptimal health status*
   **PMID/PubMed:** [30174765](https://pubmed.ncbi.nlm.nih.gov/30174765/)
   **DOI:** [10.1007/s13167-018-0144-8](https://doi.org/10.1007/s13167-018-0144-8)

### Separately graded bridge records

4. **Exact title:** *The joint subclinical elevation of CRP and IL-6 is associated with lower health-related quality of life in comparison with no elevation or elevation of only one of the biomarkers*
   **PMID/PubMed:** [26195318](https://pubmed.ncbi.nlm.nih.gov/26195318/)
   **DOI:** [10.1007/s11136-015-1068-6](https://doi.org/10.1007/s11136-015-1068-6)

5. **Exact title:** *Low-grade inflammation is negatively associated with physical Health-Related Quality of Life in healthy individuals: Results from The Danish Blood Donor Study (DBDS)*
   **PMID/PubMed:** [30921429](https://pubmed.ncbi.nlm.nih.gov/30921429/)
   **DOI:** [10.1371/journal.pone.0214468](https://doi.org/10.1371/journal.pone.0214468)

6. **Exact title:** *Association of C-reactive protein and interleukin-6 with new-onset fatigue in the Whitehall II prospective cohort study*
   **PMID/PubMed:** [23151405](https://pubmed.ncbi.nlm.nih.gov/23151405/)
   **DOI:** [10.1017/S0033291712002437](https://doi.org/10.1017/S0033291712002437)

## Citation-free replacement abstract for the current evidence-audit phase

**Background:** Suboptimal health status is commonly measured with the Suboptimal Health Status Questionnaire-25, but reported cutoffs, biomarker matrices and analytic estimands vary. We assessed whether the currently available source-verified evidence supports a primary pooled estimate of SHS-related cortisol and its proposed low-grade-inflammation bridge.

**Methods:** We audited 11 supplied PDFs at the byte and page/table level, verified article identities, recorded SHA-256 hashes and extracted source-located quantitative estimates. A primary quantitative synthesis required a verified source, a compatible SHS definition, an outcome estimand that was not incorporated into the exposure classification, and a reasonably independent study population. Cohort overlap, cortisol sampling and assay conditions were reconciled before pooling. Certainty was assessed using GRADE principles.

**Results:** Three source-audited reports contained direct SHS-related cortisol values. The derived study-level mean differences were 42.98 ng/mL, 10.81 ng/mL and 44.00 ng/mL, respectively, but the reports used a sample-median SHS score of 44, a sample-median score of 35 and a latent-class definition. The reports also differed in serum versus plasma measurement, raw versus covariate-adjusted estimates and recruitment documentation. The 2018 latent-class report used cortisol as a manifest variable in class assignment. No report therefore met all criteria for a primary pooled direct-cortisol estimate. A transparent three-report random-effects calculation gave MD 32.60 ng/mL (95% CI 11.64–53.56; I²=99.3%) and was classified as exploratory only. Low-grade-inflammation/HRQoL and inflammation/fatigue records were retained as separate bridge evidence. Twenty-four historical Meta rows lacked a verified exact identity and were quarantined. Certainty for the direct-cortisol evidence was Very low.

**Conclusions:** The source-audited literature is compatible with an association between SHS-related symptom status and altered cortisol, but it does not currently justify a primary pooled estimate or a causal claim. Future synthesis requires cohort-level deduplication, harmonized sampling protocols and prospective validation of the proposed immune-metabolic and mitochondrial SLIM model.

## Safe replacement for the core Results paragraph

Three source-audited direct reports were retained for study-level narrative synthesis. The 2012 report compared serum cortisol between groups defined by the sample-median SHS score of 44 and reported 204.31 ± 40.06 versus 161.33 ± 27.83 ng/mL. The 2015 report collected fasting morning plasma in workers recruited from three Beijing companies during January–April 2012; its adjusted Table 4 values were 178.58 ± 18.25 versus 167.77 ± 12.25 ng/mL. The 2018 report measured fasting morning plasma in 868 employees and reported 205.80 ± 29.82 versus 161.80 ± 7.79 ng/mL for LCA-defined classes. These contrasts are not interchangeable: the first two use different sample-median definitions and raw versus adjusted estimands, while cortisol is included in the 2018 LCA class assignment. Because the three reports share a potentially overlapping Xuanwu Hospital research and recruitment infrastructure and do not establish independent cohorts, no primary pooled direct-cortisol estimate was reported. The three-report random-effects calculation is retained only as an exploratory sensitivity result.

## Safe replacement for the bridge-evidence paragraph

The verified bridge evidence was not combined with direct SHS/cortisol data. The Swedish study reports adjusted SF-36 contrasts for joint CRP and IL-6 categories rather than SHSQ-25 group means. The Danish Blood Donor Study reports stratified regression coefficients for SF-12 physical health-related quality of life rather than a fatigue odds ratio or SF-36 vitality mean difference. The Whitehall II study reports separate fully adjusted CRP and IL-6 odds ratios for new-onset fatigue rather than the historical unsupported joint-marker odds ratio. These findings can inform a mechanistic narrative about low-grade inflammation, quality of life and fatigue, but they do not constitute a common estimand for quantitative pooling with the direct cortisol reports.

## Figure and table disposition

- `FigS2_Forest_Cortisol_SourceAudited_Exploratory.png/.pdf`: retain only as an explicitly labelled exploratory appendix figure.
- Historical `FigS3`–`FigS7`: do not use in a final submission until every input row has exact identity, source table and eligibility confirmation.
- Historical PRISMA flow diagram: retain as provisional planning material; do not present as final screening flow.
- New locked evidence map: use `locked_primary_synthesis_evidence_map_SchemeB_2026-10-08.csv` as the current analysis table.
- New cohort reconciliation and row eligibility ledgers: include as audit supplements or internal reviewer files.

## Next manuscript action

Create a new narrative-only manuscript version from the historical draft rather than editing the historical provisional draft in place. The new version should replace the abstract, Results, GRADE interpretation, figures and numerical Highlights using the text above; preserve the SLIM model as a clearly labelled mechanistic proposal; and keep any unverified NLR, HRV, OXPHOS and historical fatigue numbers out of the Results.
