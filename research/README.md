# Supporting evidence workbench

The main research route begins in the [CES reading room](../dossier/README.md), which connects the market thesis, literature review and deployment context. This workbench preserves the narrower source audit, company cases and synthetic model behind that review.

Inspect the [company brief](COMPANY_BRIEF.md), [attributed cases](entities.json), [technology actions](assessments.json) and [source-role protocol](protocol.json). The [research status](STATUS.md) shares the current reading-room coverage summary, while [snapshot.json](snapshot.json) retains separate original-audit counts and artifact hashes.

Method references in [BENCHMARKS.md](BENCHMARKS.md) and [benchmarks.json](benchmarks.json) support the original evidence workflow. Publication-format references are tracked separately in [the dossier](../dossier/FORMAT.md). The [release record](releases.json) remains contextual and does not assert implementation testing.

Use [research design decisions](DECISIONS.md) and [contribution review](../docs/review/CONTRIBUTION_REVIEW.md) for detailed scope. Run the integrated offline check from the root:

    python reproduce.py
