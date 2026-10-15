# Molecular Psychiatry review-format gate — Scheme B — 2026-10-15

## Source and purpose

This gate maps the active source-audited narrative manuscript to the official Molecular Psychiatry preparation page:

- [Molecular Psychiatry — Preparation of Articles](https://www.nature.com/mp/authors-and-referees/preparation-of-articles)

It is a journal-format gate, not evidence that the manuscript is ready for submission. Scientific claims remain controlled by the evidence audits, reference register and claim-to-source matrix.

## Journal-facing requirements recorded from the official page

For Review Articles, the official page specifies:

- an **unstructured abstract**;
- an abstract length of **150–250 words**;
- an article length of approximately **6,000 words**;
- no more than **6** figures/tables as the article display limit shown on the page;
- no more than **250** references as the article limit shown on the page;
- **Vancouver** references, numbered in order of first citation;
- all authors for papers with up to six authors, and the first six followed by *et al.* for papers with more than six authors;
- figure legends on a separate manuscript page after the references; and
- a supplementary-information statement before the references when supplementary files are submitted.

The journal page should be rechecked immediately before submission because journal instructions can change.

## Current manuscript status

| Gate | Current status | Evidence or next action |
|---|---|---|
| Review-article abstract structure | **PASS** | 44 contains one unstructured abstract paragraph; no Background/Methods/Results/Conclusions subheadings remain |
| Abstract word count | **PASS** | 44 abstract: approximately 213 words under the 150–250-word range |
| Main-text length | **WORKING PASS** | 44 main narrative is approximately 4,600 words excluding the evidence-file navigation block; assess final word count after numbered references, tables and legends are formatted |
| Display-item budget | **PROVISIONAL PASS** | File 55 retains three safeguarded main-text tables and excludes exploratory legacy displays; no final figure is currently included |
| Journal-facing clean copy | **PROVISIONAL PASS; user review pending** | File 57 separates the clean copy from the audit draft, removes PMID/internal navigation, retains DOI-based Vancouver references, three tables and `*` decision placeholders |
| Vancouver numbered citations | **PROVISIONAL PASS; final journal cleanup pending** | 44 now carries 19 first-citation numeric markers and a working Vancouver list; `audit_vancouver_citation_order_SchemeB.py` and file 54 confirm order/tuple preservation |
| Full reference metadata | **PROVISIONAL PASS; final freeze pending** | File 53 contains 19 journal-formatted candidate entries and a machine-readable register; `audit_reference_metadata_SchemeB.py` confirms exact title/PMID/DOI tuple preservation and populated journal fields |
| Supplementary-information statement | **PLACEHOLDER SAVED; author decision required** | File 56 records `*`; add a journal statement only if supplementary files are actually submitted |
| Author and affiliation page | **PLACEHOLDER SAVED; author confirmation required** | File 56 records `*`; do not invent author order, affiliations, ORCID, correspondence or contact information |
| Funding/COI/contributions | **PLACEHOLDER SAVED; author confirmation required** | File 56 records `*`; do not infer these statements from cited articles or source PDFs |

## Presentation rule

The source-audited title/PMID/DOI anchors are retained during the evidence phase because they make identity checking transparent. They are not the final Vancouver reference presentation. The conversion step must preserve the one-to-one mapping between every in-text citation, the 19-row verified reference register and the claim traceability matrix. Any reference that cannot be closed with exact title, PMID/PubMed URL, DOI/DOI URL and journal-formatted metadata remains pending and must not be silently formatted from a secondary citation.

## Current decision

The manuscript has passed the abstract-format gate, provisional metadata gate, provisional citation-order gate, provisional display-package gate and clean-copy audit but has **not** passed the final submission-format gate. Author/declaration and figure/supplement fields remain saved as `*` placeholders in file 56 and the clean copy. The remaining presentation work is user review, final journal cleanup and replacement of those placeholders with author-confirmed information; none may change evidence roles or add unsupported claims.
