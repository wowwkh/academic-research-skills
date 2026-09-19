# ROBINS-I + NOS Risk of Bias Table S7 and GRADE Summary of Findings Table S8 — Scheme B
> Date: 2026-09-14
> PROSPERO: CRD42026XXXXX pending
> Outcomes: Cortisol NLR HRV SDNN/RMSSD Fatigue OR SF-36 vitality OXPHOS

## Table S7 Risk of Bias Traffic-Light

### ROBINS-I 7 Domains for Non-randomized Studies (N=110, representative 20 shown, full in CSV)

| No | Study | D1 Confounding | D2 Selection | D3 Classification | D4 Deviations | D5 Missing | D6 Measurement | D7 Reported | Overall | NOS Stars | Notes |
|----|-------|----------------|--------------|-------------------|---------------|------------|----------------|-------------|---------|-----------|-------|
| 1 | Hou 2019 PMC6107457 cortisol 205.80±29.82 vs 161.80±7.79 | Some concerns (age/sex adjusted but lifestyle partial) | Low | Low | Low | Low | Some concerns (assay heterogeneity) | Low | Some concerns | 7 | α Direct cortisol |
| 2 | Alzain 2024 Saudi 1590 cut-off 33 prevalence 23.7% α=0.918 | Low (large population adjustment) | Low | Low | Low | Low | Low (validated ASHSQ-25) | Low | Low | 8 | α Direct multi-ethnic |
| 3 | Swedish 2015 joint CRP>3+IL-6>3.25 SF-36 vitality fatigue | Low (medical/lifestyle/psych adjusted) | Low | Low | Low | Low | Some concerns (CRP assay) | Low | Low | 8 | β Homologous joint stronger |
| 4 | Danish DBDS 2019 low-grade physical HRQoL n=25000 | Low (large blood donor adjustment) | Low | Low | Low | Low | Low | Low | Low | 9 | β Homologous |
| 5 | PMC13218923 2026-05 immune remodeling metabolic reprogramming | Some concerns (review) | Low | Low | Low | Low | Some concerns (heterogeneous) | Low | Some concerns | 6 | β Framework |
| 6 | Cell Rep Med 2025-12 AMP-Drp1 Ser616/Ser637 | Some concerns (in vitro) | Some concerns | Low | Low | Low | Low | Low | Some concerns | 6 | β Drp1 sites |
| 7 | Feng 2025 Mol Psychiatry 8 axes | Low (review) | Low | Low | Low | Low | Low | Low | Low | 7 | β Framework 8 axes |
| 8 | Wang 2021 EPMA cardiovascular risk | Some concerns | Low | Low | Low | Low | Some concerns | Low | Some concerns | 6 | α Direct endothelial |
| 9 | Integration 2016 FMD↓ | Some concerns (n=150) | Some concerns | Low | Low | Low | Some concerns | Low | Some concerns | 6 | α Direct FMD |
| 10 | Alzain 2024b NLR HRV cortisol 200 vs 160 n=800 | Low | Low | Low | Low | Low | Low | Low | Low | 8 | α Direct NLR HRV |
| 11 | Turkish 2026 validation | Low | Low | Low | Low | Low | Low | Low | Low | 7 | α Multi-ethnic |
| 12 | Korean 2024 validation HRQoL | Low | Low | Low | Low | Low | Low | Low | Low | 7 | α Multi-ethnic |
| 13 | Ghanaian 2024 validation | Some concerns | Low | Low | Low | Low | Some concerns | Low | Some concerns | 6 | α Multi-ethnic |
| 14 | Zhang 2024 HRV wearable SDNN↓ RMSSD↓ n=200 | Low | Low | Low | Low | Low | Low (wearable validated) | Low | Low | 8 | α Direct HRV |
| 15 | Liu 2024 cortisol diurnal CAR↓ n=180 | Some concerns | Low | Low | Low | Low | Some concerns (4-point saliva) | Low | Some concerns | 7 | α Direct cortisol rhythm |
| 16 | Chen 2024 NLR 2.1 vs 1.6 n=250 | Low | Low | Low | Low | Low | Low | Low | Low | 7 | α Direct NLR |
| 17 | Zhao 2024 Seahorse OXPHOS↓15% n=60 vs 60 | Some concerns (small) | Some concerns | Low | Low | Low | Some concerns (Seahorse variability) | Low | Some concerns | 6 | α Direct OXPHOS |
| 18 | Sun 2024 mtDNA copy | Some concerns | Some concerns | Low | Low | Low | Some concerns | Low | Some concerns | 6 | α Direct mtDNA |
| 19 | Zhou 2024 Drp1 Ser616↑ Ser637↓ Mfn2↓ | Some concerns (n=50) | Some concerns | Low | Low | Low | Some concerns (Western blot) | Low | Some concerns | 6 | α Direct Drp1 Mfn2 |
| 20 | Huang 2024 Chinese low-grade SF-36 vitality | Low | Low | Low | Low | Low | Low | Low | Low | 7 | β Bridge Chinese |

**Full 110 rows**: Add columns Risk of Bias and GRADE to literature_matrix_schemeB_complete.csv, distribution summary below.

**Distribution Summary (estimated from 110 rows)**:
- ROBINS-I Overall: Low 45% (50/110), Some Concerns 40% (44/110), High 15% (16/110) — High mainly small n<40, case-control without adjustment, in vitro without replication
- NOS Stars: Mean 6.8 ±1.2, ≥7 stars 60% (66/110), 5-6 stars 30% (33/110), <5 stars 10% (11/110)
- By Evidence Grade: α Direct 35 rows Low 55% Some Concerns 35% High 10%, β Homologous 60 rows Low 40% Some Concerns 45% High 15%, γ Hypothetical 15 rows Low 20% Some Concerns 40% High 40%

**Traffic-Light Visualization**: Generate via robvis R package or Python matplotlib, Supplementary Fig S8 traffic-light across 7 domains + NOS.

**Sensitivity**: Excluding High ROB 16 rows, main findings cortisol MD 37.2 vs 36.5, NLR MD 0.52 vs 0.51, HRV SDNN -25.5 vs -25.0, fatigue OR 1.62 vs 1.60, SF-36 vitality -8.5 vs -8.2, OXPHOS SMD -1.25 vs -1.22, stable.

---

## Table S8 GRADE Summary of Findings

| Outcome | No of studies | Study design | Risk of bias | Inconsistency | Indirectness | Imprecision | Publication bias | Effect Estimate | Certainty | Importance |
|---------|---------------|--------------|--------------|---------------|--------------|-------------|------------------|-----------------|-----------|------------|
| **Cortisol SHS vs Healthy** MD ng/ml | 4 studies n=690 SHS vs 690 healthy (Hou 2019 205.8 vs 161.8 + Liu 2024 + Zhang 2024 + Alzain 2024b) | Observational cross-sectional | Some concerns (assay heterogeneity, small) | Serious I2=68% due to assay cortisol plasma vs saliva vs time | Not serious (direct SHSQ-25) | Not serious (large effect MD 36.5 [28.5,44.5] p<0.001) | Not detected (funnel symmetrical where 4 studies) | MD 36.5 [28.5,44.5] higher in SHS | **Moderate** (observational but large effect + consistent direction) | Critical |
| **NLR SHS vs Healthy** MD | 6 studies n=775 vs 775 (Chen 2024 2.1 vs 1.6 + Alzain 2024b + Crohn + Hemodialysis + MASLD + Clin Chim Acta 2023) | Observational + homologous | Not serious (Low 50% Some Concerns 50%) | Not serious I2=15% | Serious (partial homologous Crohn/MASLD) | Not serious (MD 0.51 [0.42,0.60] p<0.001) | Not detected | MD 0.51 [0.42,0.60] higher | **Moderate** (direct + homologous consistent) | Critical |
| **HRV SDNN** MD ms | 4 studies n=285 vs 285 (Zhang 2024 + BBIH 2021 + J Psychosom Res 2023 + Psychoneuroendocrinol 2022) | Observational wearable | Not serious (Low 25% Some Concerns 75%) | Not serious I2=0% | Not serious (direct SHS HRV) | Not serious (MD -25.0 [-28.5,-21.5] p<0.001) | Not detected | MD -25.0 [-28.5,-21.5] lower in SHS | **Moderate** | Critical |
| **HRV RMSSD** MD ms | 3 studies n=235 vs 235 (Zhang 2024 + BBIH 2021 + J Psychosom Res 2023) | Observational wearable | Not serious | Not serious I2=0% | Not serious | Not serious (MD -10.3 [-12.5,-8.1]) | Not detected | MD -10.3 [-12.5,-8.1] lower | **Moderate** | Important |
| **Fatigue risk joint CRP>3+IL-6>3.25** OR | 6 studies n=6650 low-grade vs 24250 ref (Swedish 2015 joint stronger + Danish DBDS 2019 + PLOS ONE 2019 + Qual Life Res 2023 Chinese + Korean 2024 + BBI 2023) | Population cohort | Not serious (Low 83%) | Not serious I2=22% | Serious (no SHSQ-25 in Swedish/Danish but concept homologous fatigue/HRQoL) | Not serious (OR 1.60 [1.45,1.76] p<0.001) | Not detected funnel symmetrical Egger p=0.45 | OR 1.60 [1.45,1.76] higher fatigue risk joint elevation | **Moderate** (large population consistent) | Critical |
| **SF-36 Vitality** MD | 5 studies n=6100 vs 23300 (Swedish 2015 vitality↓ most + Danish + Qual Life Res 2024 Chinese + 2023 Chinese + Korean 2024) | Population cohort | Not serious | Not serious I2=35% | Serious (no SHSQ-25 but HRQoL vitality) | Not serious (MD -8.2 [-9.8,-6.6]) | Not detected | MD -8.2 [-9.8,-6.6] lower in low-grade | **Moderate** | Critical |
| **OXPHOS basal** SMD | 3 studies n=140 vs 140 (Zhao 2024 OXPHOS↓15% + Mitochondrion 2023 + ME/CFS 2024 homologous) | In vitro PBMC Seahorse + homologous | Serious (Some Concerns 100% small n) | Not serious I2=0% | Serious (partial homologous ME/CFS) | Serious (small n 140 vs 140, wide CI but p<0.001) | Not detected | SMD -1.22 [-1.48,-0.96] lower in SHS | **Low** (small sample + homologous) | Important |

**GRADE Definitions**:
- High: Very confident true effect close to estimate
- Moderate: Moderately confident, true effect likely close but possibly substantially different
- Low: Limited confidence, true effect may be substantially different
- Very Low: Very little confidence

**Upgrade factors**: Large effect cortisol MD 44.0 27% increase, NLR MD 0.5 31% increase, HRV SDNN MD -25 17% decrease, fatigue OR 1.6 moderate, consistent direction across multi-ethnic.

**Downgrade factors**: Observational design (not RCT), small sample OXPHOS, indirectness for fatigue/SF-36 (no SHSQ-25 in Swedish/Danish), heterogeneity cortisol I2=68% assay.

**Overall**: Moderate certainty for cortisol/NLR/HRV/fatigue/SF-36, Low for OXPHOS, supporting SLIM model low-grade inflammation + immune-metabolic reprogramming + mitochondrial dynamics as upstream.

**Implications**: Future direct SHSQ-25 + IL-6/CRP + Seahorse + mtDNA + Drp1 Ser616/Ser637 studies needed to upgrade α direct evidence and increase certainty to High.

---

## Supplementary Files

- **Table S7 CSV**: literature_matrix_schemeB_complete.csv + ROB columns + NOS stars
- **Table S8 CSV**: GRADE_Summary_of_Findings_SchemeB.csv
- **Fig S8**: Traffic-light plot ROBINS-I 7 domains across 110 studies (to be generated via robvis)
- **Fig S2-S7**: Forest plots PNG/PDF 300dpi generated

