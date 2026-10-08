# Meta-analysis data audit — Scheme B — 2026-10-08

## Purpose

This is the first pre-submission integrity gate. It audits whether the historical forest-plot results can be reproduced from the current extraction file. It does **not** certify the scientific validity of the extracted values: most rows still require source-PDF, page/table, population, cutoff, and unit verification.

Files audited:

- `meta_analysis_extraction_SchemeB.csv` — 31 rows
- `generate_forest_plots.py` — historical draft-figure generator
- `recompute_meta_analysis.py` — reproducible validation calculation added in this step

No values in the extraction CSV were changed in this step.

## Main finding

The current figures are **not reproducible from the current CSV as written**. `generate_forest_plots.py` contains hard-coded study effects, confidence intervals, pooled estimates, and I² values; it does not read and calculate from `meta_analysis_extraction_SchemeB.csv`.

Therefore, the existing Fig S2–S7 files must be treated as **draft figures**, not final results. They must be regenerated after source-PDF verification and after the plotting code is connected to the verified extraction table.

## Recalculation from the current CSV

The new validation script uses:

- mean difference for cortisol, NLR, HRV, and SF-36 vitality;
- Hedges g for OXPHOS;
- log odds ratios with standard errors derived from the reported 95% CIs for the fatigue outcome;
- DerSimonian–Laird random-effects pooling;
- Q, tau-squared, and I² calculated from the study-level inputs.

All values below remain **provisional**, because the underlying source values have not yet been fully verified.

| Outcome | k | Metric | Historical draft result | Recomputed from current CSV | I² draft | I² recomputed |
|---|---:|---|---|---|---:|---:|
| Cortisol | 4 | MD | 36.5 [28.5, 44.5] | 35.859 [28.809, 42.909] | 68% | 87.031% |
| NLR | 6 | MD | 0.51 [0.42, 0.60] | 0.506 [0.458, 0.554] | 15% | 0.000% |
| HRV SDNN | 4 | MD | −25.0 [−28.5, −21.5] | −24.956 [−28.150, −21.761] | 0% | 0.000% |
| HRV RMSSD | 3 | MD | −10.3 [−12.5, −8.1] | −10.335 [−12.096, −8.573] | 0% | 0.000% |
| Fatigue risk | 6 | OR | 1.60 [1.45, 1.76] | 1.593 [1.465, 1.733] | 22% | 0.000% |
| SF-36 vitality | 5 | MD | −8.2 [−9.8, −6.6] | −8.288 [−9.333, −7.244] | 35% | 39.366% |
| OXPHOS basal | 3 | SMD | −1.22 [−1.48, −0.96] | −1.203 [−1.458, −0.948] | 0% | 0.000% |

The differences are not merely rounding. In particular, cortisol, NLR, fatigue, and SF-36 I² values cannot be claimed from the current CSV without a documented alternative dataset, transformation, or model.

## Input provenance audit

- 31/31 rows are numerically parseable under the current CSV schema.
- Only the Hou 2019 row names a source locator (`PMC6107457`) in the study field.
- The other rows do not contain a DOI/PMID, PDF filename, page number, table/figure number, or extraction reviewer.
- The CSV therefore cannot yet support independent verification or a defensible dual-extraction claim.
- The exact SHSQ-25 status and direct-versus-bridge status of several NLR, fatigue, SF-36, HRV, and OXPHOS rows still need to be confirmed from the original reports.

The row-level audit is saved as `meta_analysis_input_audit_provisional.csv`; the numerical recalculation is saved as `meta_analysis_recomputed_provisional.csv`.

## Required correction before final analysis

1. Obtain the source PDFs or stable DOI/PMID records for the core rows.
2. Add, for every included row, the exact page/table/figure locator, units, cutoff, group definition, adjusted/unadjusted status, and reviewer initials.
3. Replace all estimated values with PDF-extracted values; do not silently retain an estimate.
4. Label each study as direct SHSQ-25 evidence, low-grade-inflammation bridge evidence, or mechanistic/homologous evidence.
5. Decide in advance which direct and bridge studies can be pooled; run direct-only and sensitivity analyses where appropriate.
6. Replace the hard-coded forest-plot arrays with calculations driven by the verified CSV.
7. Re-run all pooled effects, confidence intervals, I², sensitivity analyses, GRADE, manuscript text, and figures.

## Current decision

**Gate 1: FAIL for final submission, PASS for continuing the verification workflow.**

The topic, manuscript architecture, and analysis package remain usable. The current numerical results must not be described as final until the source-level extraction and reproducible recalculation are complete.
