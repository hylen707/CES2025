# Project charter / 프로젝트 범위

## Concrete question and contribution

The supplied CES2025 deck introduces PQC, contrasts it with quantum cryptography, explains motivations and names QuSecure/Quranium. The repository's retrospective question is: **what additional evidence is needed to move from that introduction to an auditable migration argument?** This question was formulated during the 2026-10-28 preparation, not attributed to the original contributor activity.

The contribution now available is a source-to-claim audit plus a transparent timing-sensitivity model. The audit narrows security wording, separates cryptographic functions and marks vendor assertions by evidential status. The model demonstrates how long-lived confidentiality requirements and migration duration affect a hypothetical planning trigger. It is not a cryptographic implementation, a proof of quantum resistance or a vendor benchmark.

## Completion and remaining gates

| Component | Current state | Evidence |
| --- | --- | --- |
| Primary source | Text of all 12 slides read; original export preserved | `sources/original.pptx`, `sources/slides.json` |
| Claim audit | 15 observations, 9 qualified/proposed claims | `evidence.json` |
| Technical verification | NIST standards, NSA limitations, NCCoE migration guidance consulted | Source register |
| Reproducible work | 15 deterministic synthetic scenario rows and tests | `results/`, `scripts/`, `tests/` |
| Contributor ownership | Pending; original source authorship not independently established | `project.json`, contributor review |
| Original chronology/role/hours/impact | Unknown; no values invented | Null activity fields |
| Source visual meaning | Not evaluated beyond extracted text | Scope limitation |

This project uses an editorial standard of traceable claims, explicit assumptions and reproducible calculations.

## Commit interpretation

The new commits record preparation performed now, separated by reviewable deliverables. The initial repository commit is preserved. Commit count does not establish duration, contributor effort, independence, impact or learning; nothing is backdated to CES2025.
