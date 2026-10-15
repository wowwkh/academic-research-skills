"""Shared evidence-scope policy for the active narrative manuscript.

Identifiers listed here may be documented in the audit addendum, but they must not
be promoted into the active manuscript without an explicit re-adjudication. Keeping
this list in one module prevents the citation and structure audits from drifting.
"""

from __future__ import annotations

# Candidate records that are unresolved or deliberately scope-excluded:
# - 31814473 and its DOI: unresolved title/PMID/DOI tuple;
# - 30849741: TCM/BDT intervention;
# - 34495543: book chapter/secondary source;
# - 36564831: COACS/MetS-only metabolome;
# - 38788028: exercise intervention.
QUARANTINED_OR_SCOPE_EXCLUDED_IDENTIFIERS = frozenset(
    {
        "31814473",
        "10.1080/10715762.2019.1685668",
        "30849741",
        "34495543",
        "36564831",
        "38788028",
    }
)


def forbidden_identifiers() -> tuple[str, ...]:
    """Return deterministic identifiers for audit error messages."""

    return tuple(sorted(QUARANTINED_OR_SCOPE_EXCLUDED_IDENTIFIERS))
