# CES2025 · Evaluating post-quantum security claims

**From a technology overview to a traceable migration argument.**

The phrase “quantum-resistant” leaves important engineering questions open: which cryptographic function changes, which assumptions support the claim, and what evidence would justify a migration decision? This project investigates those questions through a 12-slide CES2025 presentation, primary standards, vendor case studies, and a reproducible planning model.

Its central contribution is a chain that a reader can inspect and challenge: a located source statement, a bounded interpretation, a counterargument, and a testable next question. The research connects technical precision to planning decisions while keeping uncertainty visible.

**한국어:** CES2025 발표의 PQC·QKD 설명과 기업 사례를 표준 및 출처와 대조하고, 암호 기능·안전성의 전제·전환 판단을 구분했다. 원문 검토에서 출발해 주장별 논증, 합성 자산 시나리오, 재현 검증으로 이어지는 탐구 과정과 결과를 담았다.

## What the investigation established

| Question | Finding | Supporting work |
| --- | --- | --- |
| What does a standardized PQC algorithm provide? | Key establishment and digital signatures serve different functions. Naming an algorithm leaves implementation and protocol assurance to be evaluated. | [Technical corrections](docs/04-technical-corrections.md) |
| Can the two vendors be ranked from the reviewed material? | QuSecure and Quranium have different source coverage and positioning. The reviewed evidence lacks a shared, independently measured endpoint for a performance ranking. | [Vendor evidence](docs/05-vendor-evidence.md) |
| How do planning assumptions change the result? | Confidentiality lifetime and migration duration change the timing margin. Unknown algorithms, signatures, and a PQC pilot require separate review. | [Method and results](docs/07-method-and-results.md) |

The audit records **9 sources, 15 observations, and 9 claims**. Each claim links to precise evidence and states its reasoning, counterargument, limitation, and status. The [argument map](docs/06-argument-map.md) provides a readable overview; [evidence.json](evidence.json) preserves the machine-readable relationships.

## How the project developed

1. **Preserve the starting material.** Retain the [original presentation](sources/original.pptx), verify slide order, extract [slide text](sources/slides.json), and record hashes in the [source register](docs/02-source-intake.md).
2. **Narrow the question.** Separate conceptual explanation, cryptographic function, vendor assurance, and migration planning in the [research brief](docs/03-research-brief.md).
3. **Audit consequential claims.** Compare selected wording with NIST standards and government technical guidance. Identify where a statement needs qualification or additional evidence.
4. **Make assumptions executable.** Model five synthetic assets under three hypothetical horizons and retain all 15 scenario results.
5. **Check the evidence chain.** Validate source integrity, slide locators, observation links, and generated outputs; test boundary cases and invalid inputs.

## A result that changes with the assumptions

The model defines a planning margin in years:

`slack = hypothetical_quantum_horizon − confidentiality_lifetime − migration_duration`

For a synthetic RSA archive with a 15-year confidentiality requirement and a 3-year migration duration, the margin is **−8 years** under a 10-year horizon and **+2 years** under a 20-year horizon. Reducing the assumed confidentiality requirement to 5 years also changes the 10-year margin to **+2 years**.

These reversals make the dependency explicit. The horizons are hypothetical scenarios, and positive slack does not establish security or justify delaying migration. The model keeps signatures, unknown algorithms, and a named PQC pilot outside its confidentiality-timing verdict. Inspect the [input inventory](data/synthetic_inventory.json), [model](scripts/migration_model.py), and generated [JSON](results/migration_scenarios.json) or [CSV](results/migration_scenarios.csv).

## Reproduce and inspect

Python 3.11+ and the standard library are sufficient. From the repository root:

```bash
python scripts/ingest_pptx.py sources/original.pptx /tmp/ces2025-slides.json
python scripts/migration_model.py --output /tmp/ces2025-scenarios.json
python scripts/validate_project.py
python -m unittest discover -s tests -v
```

The **28 tests** cover exact source extraction and result reproduction, evidence-link failures, equality and near-zero timing boundaries, invalid inputs, and deliberately excluded cases. See [reproduction details](docs/09-reproducibility.md) and [provenance](ATTRIBUTION.md).

## Limits and the next question

This work evaluates source claims and a synthetic planning rule. It measures no deployed system, cryptographic performance, attack resistance, or vendor product. Source traceability cannot establish a claim's scientific truth, and missing public evidence does not establish that a product is insecure.

The next technical question is whether a specified implementation interoperates and fails predictably in a controlled local fixture. The [proposed study](docs/08-limitations-and-next-study.md) defines the service, baseline, configuration, controls, and acceptance criteria. It remains proposed work, separate from the completed audit and scenario analysis.

Related investigation: [World-IT-Show](https://github.com/hylen707/World-IT-Show), which examines the evidence needed to move from material properties to device-level claims.
