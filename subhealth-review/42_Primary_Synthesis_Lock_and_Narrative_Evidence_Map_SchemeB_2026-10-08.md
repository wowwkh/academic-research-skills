# Primary synthesis lock and narrative evidence map — Scheme B — 2026-10-08

## Locked decision

The source-audited evidence map is now locked for the current evidence state. No study is assigned to a primary pooled direct-cortisol Meta because the available reports do not jointly satisfy the minimum requirements of independent cohorts, compatible SHS definition, compatible cortisol matrix/sampling protocol, and a common estimand.

The locked rule is:

1. Source-verified records may be used in study-level narrative synthesis.
2. Direct SHS-cortisol records are not pooled unless cohort independence and estimand compatibility are established.
3. The 2018 LCA record is diagnostic/bridge evidence, not an etiologic SHS-cortisol effect, because cortisol contributes to class assignment.
4. Low-grade-inflammation/HRQoL and inflammation/fatigue records remain separate bridge evidence and cannot be pooled with direct SHS-cortisol records.
5. Historical rows without an exact title, PMID/PubMed link, DOI link and source table remain quarantined.

The machine-readable locked map is `locked_primary_synthesis_evidence_map_SchemeB_2026-10-08.csv`. It contains 11 source-audited estimand rows and zero `pooled_primary` rows.

## Verified source identities and locked roles

### Direct SHS/cortisol evidence

| Exact title | PMID/PubMed | DOI | Locked role |
|---|---|---|---|
| *Association of Suboptimal Health Status and Cardiovascular Risk Factors in Urban Chinese Workers* | [22203493](https://pubmed.ncbi.nlm.nih.gov/22203493/) | [10.1007/s11524-011-9636-8](https://doi.org/10.1007/s11524-011-9636-8) | Narrative study-level evidence; withheld from primary pool pending cohort and matrix reconciliation |
| *Association of suboptimal health status with psychosocial stress, plasma cortisol and mRNA expression of glucocorticoid receptor α/β in lymphocyte* | [25518867](https://pubmed.ncbi.nlm.nih.gov/25518867/) | [10.3109/10253890.2014.999233](https://doi.org/10.3109/10253890.2014.999233) | Narrative study-level evidence; withheld from primary pool pending cohort and adjusted-estimand reconciliation |
| *Latent class analysis to evaluate performance of plasma cortisol, plasma catecholamines, and SHSQ-25 for early recognition of suboptimal health status* | [30174765](https://pubmed.ncbi.nlm.nih.gov/30174765/) | [10.1007/s13167-018-0144-8](https://doi.org/10.1007/s13167-018-0144-8) | Diagnostic/bridge evidence; excluded from etiologic pool because cortisol is included in LCA class assignment |

### Bridge evidence kept separate

| Exact title | PMID/PubMed | DOI | Locked role |
|---|---|---|---|
| *The joint subclinical elevation of CRP and IL-6 is associated with lower health-related quality of life in comparison with no elevation or elevation of only one of the biomarkers* | [26195318](https://pubmed.ncbi.nlm.nih.gov/26195318/) | [10.1007/s11136-015-1068-6](https://doi.org/10.1007/s11136-015-1068-6) | Low-grade-inflammation/SF-36 vitality bridge; narrative only |
| *Low-grade inflammation is negatively associated with physical Health-Related Quality of Life in healthy individuals: Results from The Danish Blood Donor Study (DBDS)* | [30921429](https://pubmed.ncbi.nlm.nih.gov/30921429/) | [10.1371/journal.pone.0214468](https://doi.org/10.1371/journal.pone.0214468) | Low-grade-inflammation/SF-12 physical HRQoL bridge; narrative only |
| *Association of C-reactive protein and interleukin-6 with new-onset fatigue in the Whitehall II prospective cohort study* | [23151405](https://pubmed.ncbi.nlm.nih.gov/23151405/) | [10.1017/S0033291712002437](https://doi.org/10.1017/S0033291712002437) | Separate-marker inflammation/fatigue bridge; narrative only |

## Locked evidence-set counts

| Evidence set | Source-audited rows | Quantitative primary pool | Current synthesis |
|---|---:|---:|---|
| Direct SHS-cortisol, potentially etiologic | 2 | 0 | Narrative study-level values; cohort independence unresolved |
| Direct SHS-cortisol, LCA diagnostic | 1 | 0 | Diagnostic/bridge evidence; cortisol incorporation prevents etiologic pooling |
| Low-grade inflammation and HRQoL bridge | 6 | 0 | Separate narrative bridge; Dinh and Garvin estimands not interchangeable |
| Inflammation and new-onset fatigue bridge | 2 | 0 | Separate narrative bridge; CRP and IL-6 reported as separate markers |
| **Total source-audited estimand rows** | **11** | **0** | **No primary pooled direct-cortisol estimate** |

## What is quantitatively reportable now

The three direct source-audited records can be reported as study-level observations:

- Yan 2012 reports higher serum cortisol in the sample-median high-SHS-score group than in the low-score group; the source reports raw means and a test statistic.
- Yan 2015 reports higher adjusted plasma cortisol in the high-SHS-score group, with adjustment for sex, age, company and waking-to-sampling interval.
- Yan 2018 reports different plasma cortisol distributions between LCA classes, but cortisol is part of the class-definition model and therefore the result is diagnostic rather than an independent etiologic association.

The derived MDs and CIs are preserved in the source-audited CSV and are explicitly labelled as derived, not author-reported. The exploratory three-report random-effects calculation remains available for transparency only: MD 32.60 ng/mL (95% CI 11.64–53.56), I² 99.3%; it is not part of the locked primary synthesis.

The bridge records can support a mechanistic narrative about low-grade inflammation, physical HRQoL and fatigue, but they cannot be combined with direct SHS/cortisol data or used to restore unsupported historical joint-marker estimates.

## Manuscript-safe wording

The following wording is compatible with the locked evidence state:

> Across three source-audited reports, SHS-related cortisol differences were observed in Beijing occupational/health-examination populations. However, the reports used non-equivalent SHS definitions and cortisol estimands, shared a potentially overlapping Xuanwu Hospital research and recruitment infrastructure, and did not establish independent cohorts. In addition, the 2018 diagnostic study used cortisol as a manifest indicator in latent-class assignment. We therefore synthesized the direct evidence narratively and did not report a primary pooled cortisol estimate.

A pooled value may appear only in a clearly labelled sensitivity appendix with the existing warning that it is exploratory and not a final estimate.

## Reopening criteria

The locked decision may be reopened only if new evidence provides:

- recruitment years and employer lists for all three reports;
- author-level or participant-level confirmation of independence/deduplication;
- a protocol-approved decision about serum versus plasma and sampling time;
- a common exposure/outcome estimand, or a justified transformation; and
- a decision to exclude the LCA-incorporated cortisol contrast from an etiologic pool.

Until then, the historical 31-row Meta CSV, old forest plots and manuscript numerical claims remain traceability artifacts and must not be presented as final results.
