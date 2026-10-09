# Cohort reconciliation and estimand eligibility — Yan direct cortisol reports — Scheme B — 2026-10-08

## Decision summary

A source-based reconciliation was completed for the three PDF-audited reports that contain SHS-related cortisol values. The supplied PDFs do **not** establish participant-level independence, shared or non-shared employers, recruitment dates for the 2012 and 2018 reports, or any participant-ID linkage. Therefore, this report does not claim that the samples overlap; it documents a **non-negligible and unresolved overlap risk** that is sufficient to block a primary pooled estimate.

The 2018 report has an additional estimand problem: plasma cortisol is one of the manifest variables used in the latent-class model that defines the final SHS and health-status classes. Its 205.80 versus 161.80 ng/mL contrast is therefore a diagnostic-class contrast with incorporation of cortisol into the class definition, not an independent etiologic estimate of cortisol by an SHSQ-25-defined exposure. It should not be pooled with the 2012 or 2015 group comparisons as if all three estimated the same association.

**Current primary-synthesis decision:** no direct-cortisol pooled estimate is eligible. Retain the three source-verified records as a structured narrative synthesis; retain the existing three-report forest plot and DerSimonian–Laird calculation as explicitly exploratory sensitivity material only.

## Bibliographic anchors

### Yan 2012

**Exact title:** *Association of Suboptimal Health Status and Cardiovascular Risk Factors in Urban Chinese Workers*
**PMID/PubMed:** [22203493](https://pubmed.ncbi.nlm.nih.gov/22203493/)
**DOI:** [10.1007/s11524-011-9636-8](https://doi.org/10.1007/s11524-011-9636-8)

### Yan 2015

**Exact title:** *Association of suboptimal health status with psychosocial stress, plasma cortisol and mRNA expression of glucocorticoid receptor α/β in lymphocyte*
**PMID/PubMed:** [25518867](https://pubmed.ncbi.nlm.nih.gov/25518867/)
**DOI:** [10.3109/10253890.2014.999233](https://doi.org/10.3109/10253890.2014.999233)

### Yan 2018

**Exact title:** *Latent class analysis to evaluate performance of plasma cortisol, plasma catecholamines, and SHSQ-25 for early recognition of suboptimal health status*
**PMID/PubMed:** [30174765](https://pubmed.ncbi.nlm.nih.gov/30174765/)
**DOI:** [10.1007/s13167-018-0144-8](https://doi.org/10.1007/s13167-018-0144-8)

## Study-level reconciliation

| Field | Yan 2012 | Yan 2015 | Yan 2018 |
|---|---|---|---|
| Recruitment period | Not reported in the supplied article/PDF | January–April 2012 | Not reported; ethics code 2015SY27 is not a recruitment date |
| Setting | Urban Beijing workers; a random third of 64 companies whose workers used the physical-examination center for at least two consecutive years; 21 companies selected | Urban Beijing workers from three randomly selected companies using annual physical examinations at Xuanwu Hospital | Employees from companies in Xuanwu district attending routine health examinations |
| Health-center source | Physical Examination Center, Beijing Xuanwu Hospital, Capital Medical University | Physical examination center, Xuanwu Hospital, Capital Medical University | Health Management Center, Xuanwu Hospital, Capital Medical University |
| Named employers | None; the 21 companies are not named | Justice Bureau, Insurance Company, and University | None |
| Sample flow | 4,881 workers from 21 companies; 1,476 excluded; 3,405 investigated; 3,019 had complete questionnaire/laboratory data for the reported analysis | 386 recruited; four cortisol outliers excluded; 382 analyzed; high/low groups n=193/189 | 868 complete participants; final LCA classes n=298 SHS and n=570 health status |
| Eligible age range | 20–60 years | 30–50 years | 18–60 years |
| SHS classification used for the cortisol contrast | SHSQ-25 sample median score 44: score ≥44 versus <44 | SHSQ-25 sample median score 35: score ≥35 versus <35 | Initial SHSQ-25 criterion ≥35, but final classes were estimated by LCA using SHSQ-25, cortisol, and adrenaline; the final contrast is not a cortisol-independent SHS comparison |
| Cortisol matrix | Serum cortisol in the abstract, methods and Table 2 | Plasma cortisol | Plasma cortisol |
| Fasting and sampling time | Overnight fasting; clock time not reported | Overnight fast; 7:30–8:30 a.m.; calm state; waking time recorded | 10-hour overnight fast; 7:30–8:30 a.m. after 0.5–1 hour acclimatization; seated venous draw |
| Assay information | Gamma radioimmunoassay counter GC-911, Endocrinology Institute; intra-assay and inter-assay CV reported as <5.5% and <7.5% | Radioimmunoassay in the hospital Endocrinology Department; Sino-uk, Shanghai; adjusted for waking-to-sampling interval; reference range 50–280 ng/mL | Commercial radioimmunoassay, Beijing Sino-uk Institute; XH-6020 gamma counter; intra-assay CV <6% and inter-assay CV <10%; reference range 50–280 ng/mL |
| Effect type | Raw high-versus-low group means in Table 2; continuous-score multilevel models are separate analyses | Covariate-adjusted group means in Table 4, adjusted for sex, age, company and waking-to-sampling interval | LCA-defined diagnostic-class group means; cortisol contributes to the class assignment |
| PDF source locators | PDF p. 1 abstract; pp. 2–4 Methods; pp. 5–6 Tables 1–2 | PDF pp. 3–5 Methods/Results; PDF p. 6 Table 4 | PDF pp. 2–4 Methods/Results; PDF p. 4 Table 2 and Results |
| Cohort independence status | Unresolved; high concern because the 21 employers are unnamed and the health-center frame overlaps with the other reports | Unresolved; high concern because the three employers are named but cannot be matched to the 2012 frame, and the data were collected in 2012 at the same hospital | Unresolved; high concern because the employers and recruitment dates are not reported and the same hospital/research group is involved |
| Primary-pool eligibility | Withhold pending overlap and matrix harmonization | Withhold pending overlap and adjusted-estimand handling | Exclude from an etiologic SHS–cortisol pool; retain as diagnostic/bridge evidence |

The structured versions of these fields are in `cohort_reconciliation_Yan_direct_cortisol_SchemeB_2026-10-08.csv`, and the pairwise comparison is in `cohort_overlap_pairwise_Yan_direct_cortisol_SchemeB_2026-10-08.csv`.

## Pairwise overlap assessment

### Yan 2012 versus Yan 2015

The overlap concern is the strongest for this pair. Both reports recruited urban Beijing workers through the Xuanwu Hospital/Capital Medical University examination system, and the 2015 study explicitly collected data from January to April 2012. The 2012 report selected 21 companies from a 64-company examination frame but did not name them; the 2015 report named three companies—Justice Bureau, Insurance Company and University. The PDFs do not say whether those three employers were among the 21 companies in the 2012 analytic frame, and no participant IDs or deduplication statement is supplied.

The two reports also differ in cortisol matrix and estimand: the 2012 report describes serum cortisol and a raw group comparison, whereas the 2015 report describes plasma cortisol and covariate-adjusted group means. Even if the samples were independent, they would require an estimand and matrix-compatibility justification before pooling.

**Decision:** do not pool as independent primary studies.

### Yan 2012 versus Yan 2018

Both reports use the Xuanwu Hospital/Capital Medical University health-examination infrastructure and share senior research-team members. The 2018 report describes employees from companies in Xuanwu district but does not name employers or report the recruitment period. The PDFs do not establish whether the 2018 employees were recruited after the 2012 frame, from different companies, or from an overlapping examination population.

The 2018 contrast also has diagnostic incorporation: cortisol is a manifest indicator in the LCA used to assign the final classes. This prevents treating the 2018 contrast as a conventional independent cortisol outcome after SHSQ-25 exposure classification.

**Decision:** do not pool as independent primary studies; keep the 2018 report separate as diagnostic evidence.

### Yan 2015 versus Yan 2018

Both reports are based at Xuanwu Hospital/Capital Medical University and share Yan, Dong and Wang authorship. The 2015 report names three Beijing employers, whereas the 2018 report only states that employees came from companies in Xuanwu district. No recruitment period or employer list in the 2018 PDF permits a participant-level comparison.

The two sampling protocols are similar in broad timing—morning fasting venous blood and radioimmunoassay—but are not identical: 2015 used 7:30–8:30 a.m. plasma sampling and recorded waking time; 2018 used a 10-hour fast, 0.5–1 hour acclimatization, and a specified gamma counter. Similarity does not prove independence or assay equivalence.

**Decision:** do not pool as independent primary studies; keep the 2018 report separate because of diagnostic incorporation.

## Eligibility decision for the direct cortisol synthesis

The prespecified primary synthesis requires a reasonably compatible exposure definition, outcome estimand, measurement protocol, and independent study population. Against those requirements:

- **Yan 2012:** potentially etiologic, but independence from Yan 2015/2018 and matrix/time comparability remain unresolved.
- **Yan 2015:** potentially etiologic, but it uses adjusted group means from the same 2012 recruitment period and an unresolved employer frame.
- **Yan 2018:** not an etiologic SHS-exposure/cortisol-outcome estimate because cortisol participates in the LCA class definition.

Accordingly, the primary direct-cortisol result is **narrative synthesis only at this stage**. The existing exploratory pool of MD 32.60 ng/mL (95% CI 11.64–53.56; I² 99.3%) remains reproducible sensitivity material, but it must not appear as the review's primary pooled result.

## What would resolve the gate

A final quantitative synthesis would require at least one of the following:

1. Author-level confirmation that the 2012, 2015 and 2018 samples are independent, including recruitment years, employer lists and the examination-center sampling frame;
2. participant-level deduplication or a cohort identifier that allows one report per underlying cohort;
3. a protocol-approved rule that selects one non-duplicative report per cohort and excludes the LCA-incorporated cortisol contrast from the etiologic pool; or
4. a decision to present all three only as structured narrative evidence, with no pooled direct-cortisol estimate.

Until one of these is available, the appropriate GRADE judgment remains **Very low** for the exploratory direct-cortisol evidence, and the historical provisional Meta rows and manuscript numbers must not be replaced silently.

## Audit limits

This is a source-based reconciliation of the supplied PDFs and verified article identities. It is not a participant-level record linkage, an author response, or visual inspection of every rendered PDF page. “High concern” denotes a justified risk of non-independence or estimand incompatibility; it is not proof that any individual participant was counted twice.
