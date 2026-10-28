# Review method and access boundaries

## Purpose and cut-off

This is a public-source scoping review, with a research cut-off of 28 October 2026. It addresses PQC commercialization, buyer work, technical assumptions and implementation constraints. It is not an exhaustive database search or a meta-analysis of pooled market forecasts.

The corpus combines analyst/market records, research papers and technical notes, standards, guidance and deployment accounts. The starting presentation and its earlier claim audit remain separate artifacts. Their source counts are not added to the corpus as if every reference were newly independent.

## Selection

Prefer the original publisher, standard setter, author, research institution or deploying organization. Include a source when it changes a market boundary, an adoption argument, a cryptographic function, a deployment constraint or an assurance requirement. Foundational papers remain relevant when a newer engineering question depends on them.

Exclude syndicated forecast copies, unsupported rankings, unexplained aggregate estimates and inaccessible report-body claims. Public commercial summaries can remain in the corpus, but their access limitation is part of the result. Format references are tracked separately from the content-source count.

Representative searches included PQC market reports and migration analyses; Kyber/Dilithium/SPHINCS+ foundations; TLS and Cortex-M4 benchmarking; hybrid KEMs; cryptanalytic failures; quantum factoring resource estimates; and official deployment/transition records. This is a topic-driven selection log, not a claimed exhaustive search history.

## Access levels

- **full_pdf_selected_sections:** the public PDF was retrieved and the recorded passages inspected; hash, page count and reviewed pages identify the version. This is not a claim to have audited every proof or reproduced an experiment.
- **public_article / public_summary:** only the specified public text or summary was reviewed.
- **abstract_only:** paper or licensed-report metadata and abstract support a limited annotation; the complete text was not reviewed.
- **author_article_and_metadata:** related primary author discussion supports the interpretation while the original paper PDF remains unreviewed.
- **standard_abstract:** official function and publication metadata, without a full standards-conformance or errata review.

PDF retrieval evidence is recorded only after document identity is checked. Alternative copies with a different title or authorship are excluded. The original P02 PDF was not reviewed; its interpretation is limited to metadata and a related primary author discussion.

## Synthesis rules

Market estimates retain publisher, scope identifier, category, currency, units, years and methodology access. CAGR calculations use one publisher's own endpoints. They do not validate the forecast. No pooled estimate is produced, and adjacent quantum-cryptography categories cannot silently become PQC TAM.

Paper findings retain algorithm version, measurement endpoint and assumptions. Preprint records are distinguished from verified publication venues. A reported proof, attack, benchmark or deployment does not imply independent replication here. Commercial and provider interests remain visible in each source card.

The [theses](theses.json) are explicitly synthesis inferences with countercases and next evidence. The [coverage summary](summary.json) is a count of reviewed records, not a quality score or a claim of market completeness.

## Reproduction

Canonical inputs are sources.json, forecasts.json, theses.json and format-benchmarks.json. The offline dossier tool regenerates source cards, bibliography and arithmetic checks. The broader verification also checks the original artifact, legacy evidence, model results, documentation links and tests.

    python dossier.py --write
    python research.py --write
    python reproduce.py

Review changed scientific and commercial interpretations separately from generated metadata. Do not redistribute complete licensed reports or paper PDFs merely because they were consulted.
