# CES2025 · From quantum-security claims to migration evidence

**What turns a quantum-resistant claim into a defensible engineering decision?**

This project develops a 12-slide technology presentation into a company and technology study. It audits PQC and QKD explanations, distinguishes standards from vendor assurance, and makes a narrow migration-planning rule executable under explicit assumptions.

Its contribution is the connected argument: source statement, supported interpretation, competing explanation, reproducible result and next evidence gate. The research preserves unknown and non-comparable outcomes instead of converting a technology label into a security verdict.

발표 자료의 개념과 기업 주장을 표준·출처와 대조하고, 암호 기능·구현 안전성·전환 판단을 분리했다. 기업 사례 검토와 합성 자산 시나리오를 하나의 추적 가능한 연구 구조로 연결했다.

[Company brief](research/COMPANY_BRIEF.md) · [Research brief](docs/03-research-brief.md) · [Research workspace](research/README.md)

<!-- research-snapshot:start -->
| Core sources | Located observations | Claims | Company cases | Technology questions | Method references | Test cases |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 9 | 15 | 9 | 2 | 3 | 5 | 46 |
<!-- research-snapshot:end -->

## Findings and their consequence

| Finding | Consequence for the company and technology argument |
| --- | --- |
| Key establishment, signatures and QKD dependencies serve different functions | Compare a named function and its assumptions; a standardized algorithm alone does not establish system assurance. |
| The reviewed QuSecure and Quranium cases lack a shared, independently measured endpoint | Retain attributed offerings and evidence gaps. No vendor performance ranking or verified deployment verdict follows. |
| A synthetic 15-year archive with a 3-year migration duration has **−8 years** of slack under a 10-year horizon and **+2 years** under a 20-year horizon | Planning depends on explicit lifetime, duration and hypothetical horizon inputs. Positive slack does not establish security or justify delay. |
| Signatures, unknown algorithms and a named PQC pilot fall outside the confidentiality-timing verdict | Preserve function-specific review and inventory gaps instead of treating exclusion as safety. |

The exercise contains **five synthetic assets and fifteen scenario rows**. It measures no cryptographic implementation, live system or vendor product.

## The research system

| Layer | What it contributes |
| --- | --- |
| [Company cases](research/entities.json) | Attributed offerings and commercial/assurance questions without invented financial metrics |
| [Technology decisions](research/assessments.json) | Evidence stage, bounded action and a falsifiable next gate |
| [Technical corrections](docs/04-technical-corrections.md) · [vendor memo](docs/05-vendor-evidence.md) | Source-specific qualifications and non-comparability |
| [Argument ledger](evidence.json) | Located observations, reasoning, counterarguments and limits |
| [Scenario model](scripts/migration_model.py) | Explicit timing rule; [inputs](data/synthetic_inventory.json), [JSON](results/migration_scenarios.json) and [CSV](results/migration_scenarios.csv) |
| [Method benchmark](research/BENCHMARKS.md) · [release watch](research/releases.json) | Exact upstream references and dated, untested implementation context |

The workflow separates inventory/planning from interoperability testing. Source preservation, technical correction, company analysis and scenario sensitivity are completed within the stated scope. A version-specific local fixture remains [proposed work](docs/08-limitations-and-next-study.md). The [research status](research/STATUS.md) and README summary derive from the same records.

## Reproduce

Python 3.11+ and the standard library are sufficient:

```bash
python reproduce.py
```

The command regenerates slide extraction and scenario outputs in temporary files, checks source and artifact hashes, validates research relationships and documentation, then runs all tests. It requires no credentials, network access or cryptographic installation.

## Open evidence gates

A stronger implementation claim needs a named function, complete version tuple, authentication assumptions, an isolated fixture and reproducible success/negative-control logs. A release notice does not supply those results. Commercial metrics and independently verified deployments remain unestablished in this dataset.

[Source provenance](docs/02-source-intake.md) · [Method and results](docs/07-method-and-results.md) · [Reproduction details](docs/09-reproducibility.md) · [Provenance record](ATTRIBUTION.md) · [Contributing](CONTRIBUTING.md)

[Research change record](CHANGELOG.md)
