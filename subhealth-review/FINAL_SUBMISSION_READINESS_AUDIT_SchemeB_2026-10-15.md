# Final submission-readiness audit — Scheme B — 2026-10-15

## Executive verdict

The project has reached **final scientific-content review** and has a **near-final journal-facing manuscript**, but it has **not yet reached a submission-ready package**.

The evidence and narrative gates pass for the deliberately narrow scope. The remaining blockers are mainly package completion, author confirmation and final journal-format production. They are listed below so that they are not mistaken for missing scientific evidence.

## Scope of this audit

The audit checked:

- `44_Source_Audited_Narrative_Review_Manuscript_SchemeB_2026-10-08.md` as the source-audited working manuscript;
- `57_Journal_Facing_Submission_Copy_SchemeB_2026-10-15.md` as the separate clean copy;
- files `48`–`56` as the evidence, citation, display and submission gates;
- all active audit scripts; and
- the repository package inventory.

The audit does **not** convert the targeted evidence-verification phase into a systematic review. The manuscript must continue to describe the search as targeted source verification rather than as a completed multi-database search with dual screening.

## Confirmed PASS items

| Gate | Result | Check |
|---|---|---|
| Active manuscript separation | PASS | 44 remains the source-audit manuscript; 57 remains an independent clean copy |
| Review abstract | PASS | Unstructured; 213 words, within the 150–250-word range recorded in the journal gate |
| Citation order | PASS | In-text citation markers 1–19 and reference entries 1–19 are present and ordered |
| Reference identity | PASS | 19 title/PMID/DOI tuples match the verified metadata register |
| Main-text tables | PASS | Three labelled tables are retained and safeguarded against evidence inflation |
| Final figures | PASS for current plan | No final figure is promoted; exploratory forest plots and historical PRISMA files remain excluded |
| Primary synthesis | PASS | Direct SHS–cortisol primary pooled estimate remains 0 |
| Evidence boundaries | PASS | Direct, bridge, context and mechanistic-transfer evidence remain separated |
| Claim language | PASS | No unsupported diagnostic, causal or absolute-absence claims were detected by the current audits |
| Clean-copy audit navigation | PASS | PMID links and internal audit-file navigation are removed from 57 |
| Reference punctuation | FIXED in this audit pass | The 19 duplicated terminal periods after DOI strings were corrected in 57 |

## Remaining blockers before submission

### 1. Non-personal declaration fields are still blank

The clean copy currently contains `*` under:

- Data availability;
- Code availability; and
- Ethics and consent.

These are not author-name or affiliation fields. Proposed wording is provided in the title-page template, but the authors must confirm whether it accurately describes the final data/code hosting arrangement and the journal’s preferred ethics wording.

### 2. Display and supplementary decisions are not frozen

Files 55 and 56 currently record the following decisions as pending:

- supplementary-information decision;
- final-figure decision; and
- final-table decision.

The evidence-safe current recommendation is:

- **three main-text tables retained**;
- **zero final figures**; and
- **no supplementary files**, unless the authors deliberately choose to submit a supplementary package.

The exploratory figures, historical PRISMA diagram, GRADE files and audit CSVs must not be silently uploaded as supplementary material. If no supplement is selected, the final manuscript should contain an explicit “No supplementary information accompanies this submission” statement where required by the journal.

### 3. Title-page and cover-letter documents are not yet completed

The repository previously contained the placeholder register but not a completed standalone title page or cover letter. Templates have now been added:

- `TITLE_PAGE_TEMPLATE_SchemeB_2026-10-15.md`
- `COVER_LETTER_TEMPLATE_SchemeB_2026-10-15.md`

They remain templates until the authors replace the marked fields. The following still require author confirmation: author order, affiliations/institutions, ORCID, corresponding-author details, running title, funding, competing interests, author contributions, originality/exclusive-submission wording and any suggested-reviewer information.

### 4. The manuscript is content-complete Markdown, not a final upload file

File 57 is a clean content copy. It is not yet a final Word/PDF submission artifact with journal pagination, table placement, title-page separation and final proofing. The final upload version must be produced only after the fields above are closed.

### 5. Final length needs an independent production check

The clean Markdown copy is approximately 4,000 lexical words before the reference list and declarations, whereas file 52 records the source-audited manuscript at approximately 4,600 words. The journal gate records an approximate 6,000-word Review Article target. This is not automatically a rejection condition, but the authors should consciously decide whether the shorter clean copy is sufficient before typesetting; do not pad it with unsupported claims or quarantined evidence.

## Proposed factual wording for author confirmation

The following wording is evidence-compatible but should be confirmed before insertion into the final upload file:

**Data availability:** No new participant-level data were generated or analysed. This narrative review used public bibliographic records, publicly available full text where accessible and user-supplied article PDFs. Source-located values, derived calculations and eligibility decisions are preserved in the project audit records; copyrighted article PDFs are not redistributed as a new public dataset.

**Ethics and consent:** Not applicable. No new human participants were recruited, no participant-level identifiers were accessed and no participant-level record linkage was performed for this narrative review.

**Code availability:** The citation/evidence audit and supporting analysis scripts are retained with the project records. The authors should replace this sentence with the final repository link or the journal-approved “available on reasonable request” wording, as appropriate.

## Evidence issues that are intentionally not blockers

- The current review is narrative and source-audited, not a completed systematic review; this limitation is explicitly stated.
- The 2018 latent-class cortisol report remains diagnostic/bridge evidence because cortisol contributes to class assignment.
- The direct cortisol reports are not pooled; the exploratory calculation is not presented as a primary result.
- The unresolved pregnancy title–PMID–DOI tuple `31814473` is excluded and must remain excluded unless independently reconciled.
- Mechanistic-transfer studies remain hypotheses and cannot be promoted to direct SHS evidence.
- No new literature is required merely to close the current 19-anchor identity register; any added paper would require a new identity and scope audit.

## Closure sequence

1. Author confirms the title-page and declaration fields.
2. Author chooses no supplement or supplies a deliberately rebuilt supplementary package.
3. Author confirms three tables and zero final figures for the current package.
4. Insert/approve the data, code and ethics wording.
5. Finalize the title page and cover letter.
6. Convert 57 into the target journal’s upload format, recalculate word count and proof every table, citation, DOI and declaration.
7. Re-run all audit scripts and perform a final human read-through immediately before submission.

Until steps 1–6 are complete, the correct status is **final scientific review / conditional journal-facing draft**, not “ready to submit.”
