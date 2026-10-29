# Research brief

## English abstract

Introductory presentations can identify an important security problem while leaving their strongest claims unsupported. This retrospective study audits a 12-slide CES2025 presentation about post-quantum cryptography, quantum cryptography and two vendors. It maps source statements to a typed evidence ledger and checks selected explanations against primary standards and government technical guidance. The audit distinguishes key establishment from signatures, qualifies blanket security language and separates vendor statements from independently established assurance. A reproducible extension evaluates five synthetic cryptographic assets under three hypothetical quantum-computer horizons. The arithmetic illustrates how confidentiality lifetime and migration duration change a planning trigger, while deliberately excluding signature systems, unknown algorithms and a PQC pilot from a safety verdict. The resulting contribution is an inspectable argument and sensitivity exercise rather than a deployment claim or quantum-resistance proof. Source authorship, attendance and personal contribution remain unverified; the audit and software were prepared in October 2026.

## Question, method and falsification

| Element | Operational definition |
| --- | --- |
| Main question | What evidence turns source-level PQC claims into a defensible migration argument? |
| Unit of audit | An independently checkable slide statement, not an entire vendor or slide |
| Source method | Preserve export, verify order, assign source/observation/claim IDs |
| Technical method | Compare selected wording to primary function/assurance descriptions |
| Extension | Deterministic synthetic inventory and horizon sensitivity |
| Disconfirming evidence | A documented implementation/audit may support a vendor claim; different lifetime/duration assumptions may change the planning trigger |
| Exclusions | No forecast of a cryptanalytically relevant quantum computer; no production risk rating or cryptographic performance measurement |

The technical analysis is retrospective. The contributor must independently explain, test and correct it before claiming any part as their own work.

## Integrated research workspace

The [company brief](../research/COMPANY_BRIEF.md), [technology decisions](../research/assessments.json), and [method adoption record](../research/BENCHMARKS.md) extend the source audit. Release notices remain separate from fixture results. The complete offline entry point is `python reproduce.py` from the repository root; `python research.py --write` refreshes the reviewed research snapshot and README summary.

## Sector context

The [commercial thesis](../dossier/01-commercial-thesis.md) and [engineering review](../dossier/03-engineering-evidence.md) place this supporting study in a broader public-source corpus. Market expansion does not independently verify the named companies' revenue, deployments or implementation assurance.
