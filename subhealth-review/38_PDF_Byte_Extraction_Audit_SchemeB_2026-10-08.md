# PDF byte-extraction audit — Scheme B — 2026-10-08

## Status

The user uploaded `subhealth_pdfs_2026-10-08.zip` to the GitHub branch `arena/01a09fcc-academic-research-skills`. The archive was retrieved from commit `87df78b` and passed ZIP integrity testing. All 11 PDFs extracted successfully with text available for review.

The archive SHA-256 is:

```text
6e33e901edd151757037a42ce63f91e422e24eca091b4de972336ed041697ee6
```

The shell utilities `pdfinfo` and `pdftotext` are not installed in this environment. Instead, the PDF bytes were parsed with `pypdf 6.19.0`; page count, metadata, SHA-256, extracted text length, and table locators were recorded. This is a byte-level PDF extraction, but not a claim that the unavailable command-line utilities were run.

## Archive manifest

| PDF filename | Bytes | Pages | SHA-256 | Extracted text | Status |
|---|---:|---:|---|---:|---|
| `1-s2.0-S0022399917310899-main.pdf` | 371,854 | 7 | `3a26f5ca3f34c92ed1631fc447a9b120c6a7d15c94d7f4b89d547f75c919ee61` | 45,922 chars | complete |
| `19_333.pdf` | 124,440 | 9 | `0433415fb33e82236865f543a271bc1c51089b412d815ddb0b774da1c375ec4d` | 41,281 chars | complete |
| `Association of suboptimal health status with psychosocial stress  plasma cortisol and mRNA expression of glucocorticoid receptor     in lymphocyte.pdf` | 439,515 | 7 | `fc3401389212ee909d6826e799fec739447fae120e72f62f66a5678791bb62d2` | 36,515 chars | complete |
| `S0033291712002437.pdf` | 105,409 | 12 | `291d1c3d4d661235c4aae807060c043e610bc4b130f42d84feb516b75d546092` | 52,709 chars | complete |
| `file.pdf` | 539,380 | 16 | `69ea7e3324170625ac69e57b02f11dd79c9f0dab6062eeeb5f5680674cca66a4` | 60,318 chars | complete |
| `ijerph16173007.pdf` | 786,778 | 8 | `6f512b7ac0b69483cdc066b8b27c574863fd6128bb6ad9bb62b442ca3ac5e11e` | 27,883 chars | complete |
| `jogh-12-04077.pdf` | 1,785,917 | 9 | `49979318e26fe00b7503ffcd6e274e9a01406f9f63621724d2496183f87551d8` | 36,882 chars | complete |
| `jogh-14-04030.pdf` | 705,751 | 9 | `b70af09ce0a6341c2546c98a01a5eb8f2ef3632af34638859aba082e464ce96a` | 36,855 chars | complete |
| `s11136-015-1068-6.pdf` | 459,081 | 9 | `ef5e490f6d922cabd797410eef12f01b9b5a17732d466201f746a0d35f895bff` | 41,797 chars | complete |
| `s11524-011-9636-8.pdf` | 133,849 | 10 | `4e7f2efaf074552d54a2d3bdedca2d7c0440acfe8b18f5a71ae252f9aa40c5e2` | 30,950 chars | complete |
| `s13167-018-0144-8.pdf` | 708,200 | 7 | `19645700864cf4d0bae15dd084e0238801ca97f76fdd8c4fd39cb6fe25fd0051` | 31,736 chars | complete |

## PDF-level findings

### Direct SHS/cortisol rows confirmed from the supplied PDF bytes

1. **Association of suboptimal health status with psychosocial stress, plasma cortisol and mRNA expression of glucocorticoid receptor α/β in lymphocyte**  
   PMID [25518867](https://pubmed.ncbi.nlm.nih.gov/25518867/); DOI [10.3109/10253890.2014.999233](https://doi.org/10.3109/10253890.2014.999233).  
   **PDF p. 6, Table 4:** high SHS n=193, plasma cortisol 178.58 ± 18.25 ng/mL; low SHS n=189, 167.77 ± 12.25 ng/mL; adjusted `p<0.001`. The table footnote states adjustment for sex, age, company, and waking-to-sampling interval. Four cortisol outliers were excluded from 386 recruited workers.

2. **Association of Suboptimal Health Status and Cardiovascular Risk Factors in Urban Chinese Workers**  
   PMID [22203493](https://pubmed.ncbi.nlm.nih.gov/22203493/); DOI [10.1007/s11524-011-9636-8](https://doi.org/10.1007/s11524-011-9636-8).  
   **PDF p. 6, Table 2:** high SHS-score group, 204.31 ± 40.06 ng/mL; low SHS-score group, 161.33 ± 27.83 ng/mL; `t=34.076`, `p<0.001`. The analytic sample is n=3,019; Table 1 provides high/low group sizes n=1,547/1,472. The grouping cut point is the sample median SHS score of 44.

3. **Latent class analysis to evaluate performance of plasma cortisol, plasma catecholamines, and SHSQ-25 for early recognition of suboptimal health status**  
   PMID [30174765](https://pubmed.ncbi.nlm.nih.gov/30174765/); DOI [10.1007/s13167-018-0144-8](https://doi.org/10.1007/s13167-018-0144-8).  
   **PDF p. 4, Table 2:** LCA-defined health group cortisol 161.80 ± 7.79 ng/mL and LCA-defined SHS group cortisol 205.80 ± 29.82 ng/mL. The LCA Results section gives n=570 health and n=298 SHS; prevalence 34.78%.

These source values match the three direct rows already recorded in `meta_analysis_verified_online_extraction_SchemeB_2026-10-08.csv`. The MDs and 95% CIs in that CSV remain derived calculations, not author-reported CIs.

### The previously unresolved `file.pdf` is now identified

`file.pdf` is not an unidentified article. Its PDF title page and citation identify:

- **Exact article title:** *Low-grade inflammation is negatively associated with physical Health-Related Quality of Life in healthy individuals: Results from The Danish Blood Donor Study (DBDS)*.
- **PMID/PubMed:** [30921429](https://pubmed.ncbi.nlm.nih.gov/30921429/).
- **DOI:** [10.1371/journal.pone.0214468](https://doi.org/10.1371/journal.pone.0214468).
- **PDF locators:** abstract on PDF p. 1; multivariable regression Table 4 on PDF p. 8.
- **Reported estimates:** LGI CRP 3-10 mg/L versus no LGI; women using OC RC −0.36 (95% CI −0.94 to −0.19), women not using OC RC −0.63 (−1.05 to −0.21), and men RC −0.76 (−1.10 to −0.42).
- **Separate correction record:** *Correction: Low-grade inflammation is negatively associated with physical Health-Related Quality of Life in healthy individuals: Results from The Danish Blood Donor Study (DBDS)*; PMID [31136577](https://pubmed.ncbi.nlm.nih.gov/31136577/); DOI [10.1371/journal.pone.0216339](https://doi.org/10.1371/journal.pone.0216339).

This is a low-grade-inflammation/SF-12 bridge study, not an SHSQ-25 cohort and not a fatigue OR row.

### Bridge and context records confirmed from supplied PDFs

- `s11136-015-1068-6.pdf`: **The joint subclinical elevation of CRP and IL-6 is associated with lower health-related quality of life in comparison with no elevation or elevation of only one of the biomarkers**; PMID [26195318](https://pubmed.ncbi.nlm.nih.gov/26195318/); DOI [10.1007/s11136-015-1068-6](https://doi.org/10.1007/s11136-015-1068-6). PDF p. 6, Table 4 reports SF-36 vitality Model-b contrasts of 11.3, 9.9, and 6.1 points relative to the high/high group.
- `S0033291712002437.pdf`: **Association of C-reactive protein and interleukin-6 with new-onset fatigue in the Whitehall II prospective cohort study**; PMID [23151405](https://pubmed.ncbi.nlm.nih.gov/23151405/); DOI [10.1017/S0033291712002437](https://doi.org/10.1017/S0033291712002437). PDF p. 7, Table 4 confirms fully adjusted OR 1.28 (1.09-1.49) for CRP and OR 1.24 (1.06-1.45) for IL-6.
- `1-s2.0-S0022399917310899-main.pdf`: **Impaired mental health and low-grade inflammation among fatigued bereaved individuals**; PMID [30097134](https://pubmed.ncbi.nlm.nih.gov/30097134/); DOI [10.1016/j.jpsychores.2018.06.010](https://doi.org/10.1016/j.jpsychores.2018.06.010). Confirmed as a bereavement/fatigue/inflammation bridge, not SHSQ-25.
- `19_333.pdf`: **Development and evaluation of a questionnaire for measuring suboptimal health status in urban Chinese**; PMID [19749497](https://pubmed.ncbi.nlm.nih.gov/19749497/); DOI [10.2188/jea.je20080086](https://doi.org/10.2188/jea.je20080086). Confirmed as SHSQ-25 origin/validation, not a cortisol effect row.
- `jogh-12-04077.pdf`: **Translation and cross-cultural validation of a precision health tool, the Suboptimal Health Status Questionnaire-25, in Korean**; PMID [36181723](https://pubmed.ncbi.nlm.nih.gov/36181723/); DOI [10.7189/jogh.12.04077](https://doi.org/10.7189/jogh.12.04077). Context/validation only.
- `jogh-14-04030.pdf`: **Assessing suboptimal health status in the Saudi population: Translation and validation of the SHSQ-25 questionnaire**; PMID [38305242](https://pubmed.ncbi.nlm.nih.gov/38305242/); DOI [10.7189/jogh.14.04030](https://doi.org/10.7189/jogh.14.04030). Context/validation only.

### Unrelated record confirmed

`ijerph16173007.pdf` is **Migration, Work, and Health: Lessons Learned from a Clinical Case Series in a Northern Italy Public Hospital**; PMID [31438461](https://pubmed.ncbi.nlm.nih.gov/31438461/); DOI [10.3390/ijerph16173007](https://doi.org/10.3390/ijerph16173007). It is excluded from the SHS review and must not be used for cortisol or SHSQ-25 claims.

## Analysis consequence

The uploaded PDFs have resolved the attachment-access problem and corrected the identity of `file.pdf`. They verify three direct cortisol rows and several bridge/context rows, but they do **not** validate the unverified 2024 NLR, HRV, or PBMC-Seahorse rows. The historical Meta input, forest plots, GRADE table, and prose numbers remain provisional until outcome harmonisation, cohort-overlap checking, and a documented re-analysis are completed.

The raw ZIP contained journal PDFs and is not needed as a permanent repository artifact; it should not be retained in the public source tree after extraction. The audit above preserves the archive hash and each PDF hash for reproducibility.
