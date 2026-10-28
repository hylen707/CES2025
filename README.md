# CES2025 Research Review

## Post-quantum security: the migration market and the engineering beneath it

**Research cut-off: 28 October 2026.** A sector brief, annotated literature review and reproducible evidence desk.

The central assessment is that PQC commercialization should be examined through the work buyers must complete: discover cryptographic dependencies, plan migration, integrate compatible systems, and establish assurance. Algorithm availability is one input. The commercial value and engineering burden depend on what changes around it.

This is a synthesis to test against evidence. Native platform support can absorb some work into existing products, public market estimates have unresolved scope differences, and a successful experiment does not establish a repeatable enterprise rollout.

CES2025 자료를 출발점으로 양자내성 보안을 하나의 신기술 소개가 아니라 시장·구매 과제·논문·배포 조건이 연결되는 연구 주제로 확장했다. 시장 전망의 범위와 실제 도입 증거를 구분하고, 논문 결과가 적용되는 조건과 남는 불확실성을 분석한다.

<!-- research-snapshot:start -->
**Evidence desk** · 37 catalogued records: 15 papers/technical notes, 8 market/analyst records, and 14 standards, policy or deployment records.

Paper access: 11 selected full-PDF reviews; 4 records with explicitly limited access.
<!-- research-snapshot:end -->

### The commercial question

Published PQC forecasts point to expansion, but their reported categories and horizons do not reconcile into a defensible consensus market size. The review keeps each estimate attached to its publisher, definition and access limitations. Physical quantum cryptography and the broader quantum-technology economy remain separate categories.

The more useful commercial question is where a buyer has a funded, non-duplicated task and what evidence a supplier must provide to complete it. The [market thesis](dossier/01-commercial-thesis.md) develops that question without assigning unsupported revenue or market share to the two companies in the original presentation.

### The engineering question

The paper collection connects theoretical threats, conditional resource estimates, primitive design, hybrid protocols, network experiments, embedded constraints and implementation attacks. These bodies of evidence answer different questions. A fast historical candidate is not necessarily a sound current choice; a correctness proof and a complete deployment-security argument also have different scopes.

The [engineering review](dossier/03-engineering-evidence.md) explains those connections. The [paper atlas](dossier/04-paper-atlas.md) identifies what each reviewed record supports and where the review stops.

### Read the review

1. [Commercial thesis and buyer work](dossier/01-commercial-thesis.md) — market boundaries, value chain and commercialization questions.
2. [Analyst desk](dossier/02-analyst-desk.md) — source-by-source critique and access scope.
3. [Engineering evidence](dossier/03-engineering-evidence.md) — assumptions, protocols, performance and assurance.
4. [Paper atlas](dossier/04-paper-atlas.md) — annotated papers and technical notes.
5. [Standards and deployment record](dossier/05-deployment-record.md) — guidance, official functions, experiments and provider accounts.
6. [Synthesis and research agenda](dossier/06-synthesis-and-agenda.md) — propositions, countercases and decisive next evidence.

The [review method](dossier/METHOD.md), [source registry](dossier/sources.json), [forecast data](dossier/forecasts.json) and [bibliography](dossier/references.bib) make the reading trail inspectable. The format draws on a publication catalog and paper-linked experimental documentation; [format references](dossier/FORMAT.md) record the exact upstream versions.

### Evidence and access

Source coverage is a scoping review rather than an exhaustive systematic review. Public summaries are distinguished from selected full-PDF passages. Licensed report bodies are not represented as reviewed. Provider descriptions and controlled experiments retain their own denominators and scope.

The supplied [12-slide presentation](sources/original.pptx) remains unchanged. Later-publication material is dated as later research. The original [claim audit](evidence.json), [company cases](research/COMPANY_BRIEF.md) and [synthetic planning exercise](docs/07-method-and-results.md) remain available as supporting studies.

### Reproduce or extend

```bash
python reproduce.py
```

The offline command checks the original source, synthetic results, literature records, access boundaries, forecast arithmetic, generated review files and tests. To refresh reviewed source records, run `python dossier.py --write`, then `python research.py --write` and inspect the changed interpretation.

[Contribution guide](CONTRIBUTING.md) · [Change record](CHANGELOG.md) · [Provenance](ATTRIBUTION.md)
