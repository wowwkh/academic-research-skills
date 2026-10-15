# Active SHS review — navigation

**Status:** 2026-10-15  
**Active project:** a source-audited narrative review of SHSQ-25-defined suboptimal health status (SHS).  
**Active branch:** `arena/01a09fcc-academic-research-skills`

This directory contains the current `34`–`57` audit and submission milestones, the strict submission-readiness audit, clearly named title-page/cover-letter templates, and the supporting audit data, scripts, and exploratory display files. The earlier `01`–`33` planning and provisional drafts were retired during workspace cleanup and must not be treated as the active manuscript.

## Read these first

1. **44 — source-audited working manuscript**  
   `44_Source_Audited_Narrative_Review_Manuscript_SchemeB_2026-10-08.md`
2. **57 — independent journal-facing clean copy**  
   `57_Journal_Facing_Submission_Copy_SchemeB_2026-10-15.md`
3. **50–56 — locked gates for identity, traceability, journal format, displays, and declarations**
4. **Final submission-readiness audit**
   `FINAL_SUBMISSION_READINESS_AUDIT_SchemeB_2026-10-15.md`
5. **Title-page and cover-letter templates**
   `TITLE_PAGE_TEMPLATE_SchemeB_2026-10-15.md` and `COVER_LETTER_TEMPLATE_SchemeB_2026-10-15.md`
6. **48–49 — latest SHS original-evidence audit and next-audit gate**

The 44 manuscript is the audit source. The 57 copy is a separate journal-facing derivative; do not merge its clean presentation back into 44 or treat it as a replacement for source-audit notes.

## Milestone map

- **34–43:** metadata audit, source requests, PDF/online extraction, reconciliation, eligibility, and primary-synthesis lock.
- **44–49:** source-audited narrative manuscript, citation audit, mechanistic-transfer boundary, SHS context addendum, and original-source audit.
- **50–56:** verified reference register, claim-to-source traceability, Molecular Psychiatry format gate, Vancouver order, display-package audit, and submission placeholders.
- **57:** independent journal-facing submission copy.

## Locked scope and acceptance criteria

- Direct SHS–cortisol primary pooled estimate: **0**; no direct estimate is to be invented from bridge or mechanistic-transfer evidence.
- References: **19 Vancouver-numbered references** in the current journal-facing copy.
- Tables: **3**. Final figures: **0**; exploratory/internal figure files are not final display claims.
- Any unconfirmed author, declaration, submission, or editorial field remains `*`.
- Evidence from other diseases, experimental systems, or mechanistic models is labelled as bridge/transfer evidence and cannot be presented as direct SHS evidence.
- The repository must not add causal, diagnostic, or absolute-absence claims that the source audit does not support.

## Audit commands

Run from the repository root, for example:

```bash
python subhealth-review/audit_journal_facing_copy_SchemeB.py
python subhealth-review/audit_claim_language_SchemeB.py
python subhealth-review/audit_vancouver_citation_order_SchemeB.py
python subhealth-review/audit_display_package_SchemeB.py
python subhealth-review/audit_submission_placeholders_SchemeB.py
```

The scripts and CSV files are retained as reproducible audit support, not as permission to promote provisional rows into final evidence.

## Retired project and branch clarity

`asti-review/` is retired, removed from the active branch, and must not receive new work. The repository `main` branch remains the default baseline. Arena fixes this session’s active branch name to `arena/01a09fcc-academic-research-skills`; use `ACTIVE_WORKSPACE_INDEX.md` at the repository root for the single-workspace policy and project map.
