# Standards and deployment record

Guidance, normative functions, controlled experiments and provider self-reports have different evidentiary roles.

### D01 · Transition to Post-Quantum Cryptography Standards, NIST IR 8547

[NIST](https://csrc.nist.gov/pubs/ir/8547/final) · 2026-10-27
Access: **full_pdf_selected_sections**. Locator: PDF pp. 8,20; transition approach and timelines.

**Question:** What changed in the finalized migration roadmap?
**Approach:** Final technical transition report.
**What it supports:** Risk priorities and cryptographic functions have differentiated transition treatment.
**Boundary:** Federal-focused applicability is not a universal private-sector legal deadline.
**Use in this review:** Map obligations and dependencies to the actual organization.

Source context: Government guidance, not vendor assurance or revenue evidence.

### D02 · Timelines for migration to post-quantum cryptography

[UK NCSC](https://www.ncsc.gov.uk/guidance/pqc-migration-timelines) · 2025-03-20
Access: **public_article**. Locator: Executive summary; milestones 2028,2031,2035.

**Question:** How does a staged migration programme look?
**Approach:** UK guidance separates discovery, priorities and completion.
**What it supports:** Planning and dependency discovery precede broad transition.
**Boundary:** Indicative guidance is not a global statutory deadline.
**Use in this review:** Use staged buyer tasks with jurisdiction stated.

Source context: Government guidance; implementation remains context dependent.

### D03 · Project Leap phase 2: quantum-proofing payment systems

[BIS Innovation Hub](https://www.bis.org/publications/project-leap-phase-2-quantum-proofing-payment-systems) · 2025
Access: **public_article**. Locator: Project summary; report section 5 conclusion available in indexed extract.

**Question:** What does a payment-system experiment reveal?
**Approach:** Multi-party test replaces signatures in liquidity transfers.
**What it supports:** Compatibility changes and performance differences require coordinated preparation.
**Boundary:** An experimental system is not evidence of sector-wide rollout.
**Use in this review:** Budget for integration and negative-control testing, not algorithms alone.

Source context: Official experiment summary; underlying results not reproduced here.

### D04 · PQ.03 Guidelines for Telecom Use Cases V2.0

[GSMA](https://www.gsma.com/solutions-and-impact/technologies/security/gsma_resources/post-quantum-cryptography-guidelines-for-telecom-use-cases-pq-03-2/) · publication date not established
Access: **public_summary**. Locator: Scope; V2.0 migration description.

**Question:** Why do telecom use cases require separate migration plans?
**Approach:** Industry guidelines map architectures, standards and performance implications.
**What it supports:** Phased transformation depends on use case and stakeholders.
**Boundary:** Public scope does not establish deployment rates or measured performance.
**Use in this review:** Treat telecom as several buyer workflows.

Source context: Industry-member guidance; full report body not reviewed.

### D05 · State of the post-quantum Internet in 2025

[Cloudflare](https://blog.cloudflare.com/pq-2025/) · 2025
Access: **public_article**. Locator: Opening traffic milestone and migration discussion.

**Question:** What does a traffic adoption metric measure?
**Approach:** Provider reports its human-initiated traffic observation.
**What it supports:** The milestone concerns a defined traffic population.
**Boundary:** It is not all Internet traffic or enterprise-wide readiness.
**Use in this review:** Keep the denominator and covered cryptographic function explicit.

Source context: Provider self-report; no independent traffic audit.

### D06 · iMessage with PQ3

[Apple Security Research](https://security.apple.com/blog/imessage-pq3/) · 2024-02-21
Access: **public_article**. Locator: Initial establishment, rekeying and hybrid design sections.

**Question:** What makes migration a protocol problem?
**Approach:** Vendor engineering account of hybrid establishment and rekeying.
**What it supports:** The design addresses ongoing conversation security as well as setup.
**Boundary:** Vendor-defined levels are not a universal comparative standard.
**Use in this review:** Evaluate the threat model and recovery properties.

Source context: Vendor engineering claims, not an independent product ranking.

### D07 · A new path for Kyber on the web

[Google Chrome Team](https://security.googleblog.com/2024/09/a-new-path-for-kyber-on-web.html) · 2024-09-13
Access: **public_article**. Locator: Chrome 131 changes and compatibility discussion.

**Question:** Why does standardization require migration work?
**Approach:** Engineering notice describes Kyber-to-ML-KEM codepoint changes.
**What it supports:** The final specification is incompatible with the experimental variant.
**Boundary:** The announcement is historical, not current browser support documentation.
**Use in this review:** Pin versions and wire formats before interoperability claims.

Source context: Provider-authored implementation notice.

### D08 · OpenSSL 3.5 Final Release

[OpenSSL Library](https://openssl-library.org/post/2025-04-08-openssl-35-final-release/) · 2025-04-08
Access: **public_article**. Locator: PQC feature list.

**Question:** How does distribution change the commercial layer?
**Approach:** Official library release announcement.
**What it supports:** Native support includes ML-KEM, ML-DSA and SLH-DSA.
**Boundary:** Feature availability does not establish application configuration or assurance.
**Use in this review:** Distinguish bundled primitives from paid integration and operations.

Source context: Maintainer announcement; not a recommendation to install the initial release.

### D09 · Status Report on the Fourth Round, NIST IR 8545

[NIST](https://csrc.nist.gov/pubs/ir/8545/final) · 2025-03
Access: **public_summary**. Locator: Official abstract and selection scope.

**Question:** How does the algorithm portfolio evolve?
**Approach:** Official fourth-round evaluation report summary.
**What it supports:** HQC was selected for further standard development.
**Boundary:** A selection record is not itself a final algorithm standard.
**Use in this review:** Keep selection, draft and final-standard status distinct.

Source context: Government selection account; complete technical report not reviewed.

### D10 · RFC 9954: Hybrid Key Exchange in TLS 1.3

[RFC Editor / IETF](https://www.rfc-editor.org/rfc/rfc9954.html) · 2026-07
Access: **public_article**. Locator: Status; sections 1.3,3,6.

**Question:** What does the published hybrid construction cover?
**Approach:** Informational RFC defines a hybrid key-exchange construction.
**What it supports:** Its scope separates ephemeral exchange from authentication.
**Boundary:** Informational publication is not an Internet Standards Track status.
**Use in this review:** Name the specification and its exact scope.

Source context: Published technical specification; no product validation implied.

### D11 · A blueprint for formal verification of Apple corecrypto

[Apple Security Research](https://security.apple.com/blog/formal-verification-corecrypto/) · 2026-05-22
Access: **public_article**. Locator: Implementation criteria and verification scope.

**Question:** Which assurance property is being demonstrated?
**Approach:** Vendor describes implementation proofs against algorithm specifications.
**What it supports:** Correctness, optimization and hardening are separate engineering criteria.
**Boundary:** A correctness proof is not complete protocol or side-channel assurance.
**Use in this review:** Ask what is proved, on which implementation and assumptions.

Source context: Vendor-authored account; proofs not independently audited here.

### S01 · Module-Lattice-Based Key-Encapsulation Mechanism Standard

[NIST](https://csrc.nist.gov/pubs/fips/203/final) · 2024-08-13
Access: **standard_abstract**. Locator: FIPS 203: official abstract and final publication metadata.

**Question:** What cryptographic function is standardized?
**Approach:** Official normative publication abstract.
**What it supports:** ML-KEM establishes a shared secret.
**Boundary:** The abstract does not establish implementation certification or current errata coverage.
**Use in this review:** Use the standard's function, not a vendor-security shortcut.

Source context: Normative source; algorithm function only in this review.

### S02 · Module-Lattice-Based Digital Signature Standard

[NIST](https://csrc.nist.gov/pubs/fips/204/final) · 2024-08-13
Access: **standard_abstract**. Locator: FIPS 204: official abstract and final publication metadata.

**Question:** What cryptographic function is standardized?
**Approach:** Official normative publication abstract.
**What it supports:** ML-DSA provides digital signatures.
**Boundary:** The abstract does not establish implementation certification or current errata coverage.
**Use in this review:** Use the standard's function, not a vendor-security shortcut.

Source context: Normative source; algorithm function only in this review.

### S03 · Stateless Hash-Based Digital Signature Standard

[NIST](https://csrc.nist.gov/pubs/fips/205/final) · 2024-08-13
Access: **standard_abstract**. Locator: FIPS 205: official abstract and final publication metadata.

**Question:** What cryptographic function is standardized?
**Approach:** Official normative publication abstract.
**What it supports:** SLH-DSA provides hash-based signatures.
**Boundary:** The abstract does not establish implementation certification or current errata coverage.
**Use in this review:** Use the standard's function, not a vendor-security shortcut.

Source context: Normative source; algorithm function only in this review.

