# Reproduction and validation

Python 3.11+ and its standard library are sufficient. Commands run from the repository root. They make no network requests and perform no cryptographic operations.

```bash
python scripts/ingest_pptx.py sources/original.pptx /tmp/ec5-slides.json
python scripts/migration_model.py --output /tmp/ec5-scenarios.json
python -m unittest discover -s tests -v
python scripts/validate_project.py --json
python scripts/validate_project.py --submission --json
```

Compare regenerated JSON values with `sources/slides.json` and `results/migration_scenarios.json`; generated output includes its input hash. Reproduction is deterministic and does not insert timestamps into those outputs. The original PPTX hash is also checked by the semantic validator. If input data or the model changes, regenerate results, inspect the difference and deliberately update generated-source hashes in the evidence register. Do not edit a result merely to obtain a passing check.

## Two different gates

| Mode | Checks | Current expectation |
| --- | --- | --- |
| Draft | Required metadata/types/enums, IDs, source status, file hashes, exact source links, reasoning and limits | Pass |
| Submission | Draft checks plus artifact review, verified contributor ownership with located contributor-record evidence, role and dates, nonempty reviewed evidence | Fail until contributor-owned review is completed |

`schemas/*.schema.json` documents the JSON Schema 2020-12 type contract for compatible external validators. The standard-library script is a **project semantic/type validator, not a complete JSON Schema engine**. It additionally checks relationships and hashes. Neither tool can verify factual truth, contributor understanding, completeness of bibliography or authorship.

A passing technical check does not verify an individual contribution. The stricter contribution check remains pending until located evidence supports the required fields.

For any non-null personal field, `personal_field_evidence` must link located observations from a read `student_record` source. Setting `student_verification` to `verified` additionally requires `verification_evidence_ids` from that source category. A technical standard or generated result cannot attest a contributor’s contribution. These records must be truthful and privacy reviewed; automated source-type checks cannot authenticate a person.

## Integrated research workspace

The [company brief](../research/COMPANY_BRIEF.md), [technology decisions](../research/assessments.json), and [method adoption record](../research/BENCHMARKS.md) extend the source audit. Release notices remain separate from fixture results. The complete offline entry point is `python reproduce.py` from the repository root; `python research.py --write` refreshes the reviewed research snapshot and README summary.

## Sector review verification

The integrated command also validates the literature corpus, access declarations, publication metadata, forecast arithmetic and generated catalogs. After changing canonical review inputs, run:

```bash
python dossier.py --write
python research.py --write
python reproduce.py
```

Inspect the scientific and commercial interpretation alongside the generated changes. The tests check data boundaries and consistency; they do not reproduce the cited cryptographic experiments or authenticate market forecasts.
