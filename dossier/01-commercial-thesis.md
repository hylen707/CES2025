# Commercial thesis: follow the migration work

## Assessment

The evidence supports examining PQC as a migration and assurance problem with several potential commercial layers. It does not yet establish which layer will capture the most value, how much new spending is incremental, or which supplier will win. This assessment is an inference across the analyst, policy and deployment records, not a reported market fact. [TH01–TH02](theses.json)

### Start with the boundary

Three different markets are easy to confuse:

- **PQC products and services:** classical computing implementations, cryptographic discovery, migration management, key infrastructure and related integration.
- **Quantum cryptography:** categories such as QKD and QRNG may depend on different physical infrastructure.
- **Quantum technology:** computing, communication and sensing include businesses outside a PQC security budget.

The review therefore uses the Fortune quantum-cryptography report and McKinsey's wider technology monitor as boundary cases, rather than adding their categories to PQC projections. [M02, M07](02-analyst-desk.md)

### Published forecasts remain publisher-specific

All values below are the publishers' reported projections in **USD billions**, not verified realized revenue. Different scopes and end years prevent a consensus interpretation.

| Source | Reported 2026 base | Forecast endpoint | Quoted CAGR | Treatment |
| --- | ---: | --- | ---: | --- |
| [MarketsandMarkets / M04](02-analyst-desk.md) | 0.60 | 3.80 in 2031 | 44.5% | Separate PQC report definition |
| [Grand View Research / M05](02-analyst-desk.md) | 2.20 | 20.50 in 2033 | 37.8% | Separate PQC report definition |
| [Juniper Research / M06](02-analyst-desk.md) | 1.20 | 13.00 in 2035 | 30.0% | Separate PQC report definition |
| [Fortune / M07](02-analyst-desk.md) | 0.3455 | 2.2632 in 2034 | 26.5% | Adjacent quantum-cryptography category |

The [arithmetic output](market-checks.json) recomputes each row's implied annual growth and exposes the difference from the quoted rounded percentage. This checks arithmetic only. It neither validates the publisher's forecast nor reconciles its method. No pooled market estimate is generated.

To make a comparable market estimate, a researcher would first need consistent product coverage, geography, revenue recognition, base/target years, price basis and treatment of bundled services. Public summaries do not supply that reconciliation. An average of the headlines would introduce precision without resolving those missing definitions.

### Readiness is not procurement

Capgemini's methodology covers 1,000 organizations with annual revenue of at least $1 billion across 13 sectors and 13 countries. Its activity grouping includes plans within five years. That is evidence about a selected large-company survey population and intentions, rather than a production-deployment or revenue measure. [M03](02-analyst-desk.md)

Guidance and experiments add different demand signals. NIST's finalized transition report and the UK NCSC's staged guidance identify organizational work; their applicability must stay attached to the relevant context. BIS's payment experiment exposes compatibility and coordination burdens. GSMA describes use-case-specific transformation. None of these observations alone quantifies a supplier's billable market. [D01–D04](05-deployment-record.md)

### Where a commercial proposition could exist

The following is an analytical work map. Possible contract units are hypotheses to investigate, not observed vendor pricing.

| Buyer job | Evidence the buyer needs | Potential commercial work | Commercial question |
| --- | --- | --- | --- |
| Discover dependencies | Coverage, ownership and repeatable inventory records | Discovery tooling and assessment | What remains billable after existing platform discovery? |
| Plan and execute change | Dependency mapping, rollback, compatibility and completion records | Migration software, integration and programme services | Is the spend incremental or a replacement of existing lifecycle work? |
| Update identity and signing | Issuer, HSM, device and certificate-chain interoperability | PKI/signing integration and operational support | Who controls distribution and can bundle the change? |
| Establish assurance | Configuration-specific correctness, side-channel and protocol evidence | Review, testing and maintained assurance | Which evidence is reusable across customers and releases? |
| Maintain constrained fleets | Memory, updateability, trust-root and lifecycle evidence | OEM integration and long-lived support | Can the installed base actually be updated within its lifetime? |

Library and platform distribution can compress the standalone value of primitive availability. Integration, assurance and operational ownership may remain differentiated, but that is a proposition requiring budget and procurement evidence. OpenSSL's release milestone and the provider accounts show distribution paths; they do not establish incremental addressable revenue. [D05–D08, D11](05-deployment-record.md)

### Implication for the original company cases

QuSecure and Quranium remain differently scoped cases from the supplied presentation and reviewed vendor material. A large sector forecast cannot verify their architecture, deployments, revenue or market share. The [company brief](../research/COMPANY_BRIEF.md) retains the actual evidence gaps.

A useful next commercial record would identify the buyer, contracted function, deployment scope, renewal or project boundary, implementation outcome and whether the revenue duplicates an existing product bundle. Without that record, market expansion and company-specific value capture remain separate questions.
