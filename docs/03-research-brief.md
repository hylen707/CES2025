# Research brief / 탐구 개요

## English abstract

Introductory presentations can identify an important security problem while leaving their strongest claims unsupported. This retrospective study audits a 12-slide CES2025 presentation about post-quantum cryptography, quantum cryptography and two vendors. It maps source statements to a typed evidence ledger and checks selected explanations against primary standards and government technical guidance. The audit distinguishes key establishment from signatures, qualifies blanket security language and separates vendor statements from independently established assurance. A reproducible extension evaluates five synthetic cryptographic assets under three hypothetical quantum-computer horizons. The arithmetic illustrates how confidentiality lifetime and migration duration change a planning trigger, while deliberately excluding signature systems, unknown algorithms and a PQC pilot from a safety verdict. The resulting contribution is an inspectable argument and sensitivity exercise rather than a deployment claim or quantum-resistance proof. Source authorship, attendance and personal contribution remain unverified; the audit and software were prepared in October 2026.

## 한국어 설명

원발표가 제시한 “양자 시대의 보안”이라는 문제를, 검증 가능한 질문으로 좁혔다. 핵심은 PQC를 소개하는 것에서 그치지 않고 **어떤 암호 기능을 바꾸는지, 어떤 근거로 안전성을 말하는지, 언제 무엇을 먼저 검토해야 하는지**를 구분하는 것이다. 기업의 설명·정부 표준·학생의 활동 증거는 서로 대체할 수 없다.

분석 결과 원자료의 개념적 구분은 출발점으로 사용할 수 있지만, 무조건적인 안전성 표현과 기업별 성능·배포 보증은 추가 근거가 필요하다. 새로 만든 합성 실험은 실제 제품의 보안을 측정하지 않는다. 장기 보관 데이터와 짧은 세션의 계획상 차이를 드러내고, 잘 모르는 항목을 안전하다고 처리하지 않는 것이 목적이다.

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
