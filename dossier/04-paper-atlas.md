# Paper atlas

The review distinguishes published papers, preprint records, selected full-PDF passages and abstract-level coverage.
Historical results retain their original algorithm versions and measurement conditions.

## Foundations

### P01 · Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer

[arXiv / SIAM publication record](https://arxiv.org/abs/quant-ph/9508027) · 1997
Access: **full_pdf_selected_sections**. Locator: PDF pages 1, 2, 4.

Publication: SIAM Journal on Computing, 1997; arXiv v2, 1996 · journal_article.

**Question:** Which cryptographic problems are threatened?
**Approach:** Quantum algorithms for factoring and discrete logarithms.
**What it supports:** Polynomial asymptotic complexity changes the underlying threat model.
**Boundary:** It does not supply a hardware arrival date or deployment cost.
**Use in this review:** Separate mathematical possibility from an operational quantum attack.

Source context: Research authors; no independent reproduction or proof audit performed here.

### P02 · Cybersecurity in an era with quantum computers: will we be ready?

[IACR Cryptology ePrint Archive](https://eprint.iacr.org/2015/1075) · 2015
Access: **author_article_and_metadata**. Locator: Paper metadata; author ISACA article, Managing Quantum Risk.

Publication: Cryptology ePrint Archive 2015/1075; related author article, ISACA 2015 · preprint_record.

**Question:** When must migration precede a hypothetical threat?
**Approach:** Paper metadata and the author's public timing discussion.
**What it supports:** Confidentiality lifetime and migration duration interact with the horizon.
**Boundary:** The original PDF was inaccessible; this is a planning relation, not a forecast.
**Use in this review:** Attribute the timing model's conceptual lineage to Mosca.

Source context: Research authors; no independent reproduction or proof audit performed here.

## Resource Estimates

### P03 · How to factor 2048 bit RSA integers in 8 hours using 20 million noisy qubits

[arXiv / Quantum publication record](https://arxiv.org/abs/1905.09749) · 2021
Access: **full_pdf_selected_sections**. Locator: PDF pages 1, 2, 22.

Publication: Quantum 5, 433 (2021); arXiv v3 · journal_article.

**Question:** What resources could an RSA attack require?
**Approach:** Fault-tolerant construction under explicit superconducting-platform assumptions.
**What it supports:** An estimate includes error correction and substantial physical resources.
**Boundary:** Gate errors, cycle times and architecture are assumed, not available hardware.
**Use in this review:** Treat the headline as a conditional engineering estimate.

Source context: Research authors; no independent reproduction or proof audit performed here.

### P04 · How to factor 2048 bit RSA integers with less than a million noisy qubits

[arXiv / Google author record](https://arxiv.org/abs/2505.15917) · 2025
Access: **full_pdf_selected_sections**. Locator: PDF pages 1, 2, 21.

Publication: arXiv:2505.15917 (2025), preprint record · preprint_record.

**Question:** Can resource engineering materially change estimates?
**Approach:** Arithmetic, storage and fault-tolerance optimizations under stated assumptions.
**What it supports:** The estimate changes qubit requirements and execution-time trade-offs.
**Boundary:** It is not an experimental RSA-2048 break or a Q-Day date.
**Use in this review:** Stress-test planning against changing resource estimates.

Source context: Research authors; no independent reproduction or proof audit performed here.

## Scheme Design

### P05 · CRYSTALS – Kyber: a CCA-secure module-lattice-based KEM

[ETH Zurich author archive](https://crypto.ethz.ch/publications/BDKLL18.html) · 2018
Access: **full_pdf_selected_sections**. Locator: PDF pages 1, 3, 5.

Publication: IEEE EuroS&P 2018; author-hosted version · conference_paper.

**Question:** How is a practical lattice KEM constructed?
**Approach:** Module-LWE construction with a chosen-ciphertext-security transform.
**What it supports:** It connects assumptions, parameters and implementation trade-offs.
**Boundary:** Historical Kyber is not byte-for-byte the final ML-KEM specification.
**Use in this review:** Trace algorithm lineage while using current standards for implementation.

Source context: Research authors; no independent reproduction or proof audit performed here.

### P06 · CRYSTALS-Dilithium: A Lattice-Based Digital Signature Scheme

[CRYSTALS author archive / IACR TCHES](https://pq-crystals.org/dilithium/data/dilithium-20180114.pdf) · 2018
Access: **full_pdf_selected_sections**. Locator: PDF pages 1, 2, 7.

Publication: IACR TCHES 2018(1), 238–268 · journal_article.

**Question:** How can signature design simplify secure implementation?
**Approach:** Lattice signatures using uniform sampling and optimized arithmetic.
**What it supports:** Implementation simplicity is an explicit design objective.
**Boundary:** Design intent does not certify every compiler or device implementation.
**Use in this review:** Separate signatures, implementation assurance and current ML-DSA conformance.

Source context: Research authors; no independent reproduction or proof audit performed here.

### P07 · The SPHINCS+ Signature Framework

[IACR Cryptology ePrint Archive](https://eprint.iacr.org/2019/1086) · 2019
Access: **abstract_only**. Locator: Primary abstract and publication metadata.

Publication: ACM CCS 2019; ePrint 2019/1086 · conference_paper.

**Question:** What alternative assumptions support signatures?
**Approach:** Primary abstract describes stateless hash-based signatures and FORS.
**What it supports:** The framework offers a different assumption and performance profile.
**Boundary:** Full-PDF retrieval failed; proof details were not reviewed.
**Use in this review:** Use it for lineage and diversification, not a universal ranking.

Source context: Research authors; no independent reproduction or proof audit performed here.

### P14 · Frodo: Take off the ring! Practical, Quantum-Secure Key Exchange from LWE

[Douglas Stebila author archive](https://www.douglas.stebila.ca/research/papers/CCS-BCDMNNRS16/) · 2016
Access: **full_pdf_selected_sections**. Locator: PDF pages 1, 3, 20.

Publication: ACM CCS 2016; author full version · conference_paper.

**Question:** What does reducing algebraic structure cost?
**Approach:** LWE construction with implementation and TLS experiments.
**What it supports:** Assumption choices create communication and computation trade-offs.
**Boundary:** Its historical measurements are not current FrodoKEM or ML-KEM performance.
**Use in this review:** Assess structural assumptions together with deployment constraints.

Source context: Research authors; no independent reproduction or proof audit performed here.

## Protocols

### P08 · Hybrid Key Encapsulation Mechanisms and Authenticated Key Exchange

[Douglas Stebila author archive](https://www.douglas.stebila.ca/research/papers/PQCrypto-BBFGS19/) · 2019
Access: **full_pdf_selected_sections**. Locator: PDF pages 1, 3, 10.

Publication: PQCrypto 2019; author full version · conference_paper.

**Question:** When does combining schemes preserve intended security?
**Approach:** Formal KEM notions, combiners and authenticated exchange models.
**What it supports:** Hybrid guarantees require a specified construction and adversary model.
**Boundary:** A proof for a construction does not validate arbitrary concatenation or deployment.
**Use in this review:** Require combiner, authentication and protocol details.

Source context: Research authors; no independent reproduction or proof audit performed here.

### P15 · Post-Quantum TLS Without Handshake Signatures

[KEMTLS author project](https://kemtls.org/publication/kemtls/) · 2020
Access: **full_pdf_selected_sections**. Locator: PDF pages 1, 2, 3.

Publication: ACM CCS 2020; full version January 2022 · conference_paper.

**Question:** Can authentication be redesigned around KEMs?
**Approach:** Protocol construction, security analysis and implementation experiments.
**What it supports:** KEMTLS changes the handshake rather than swapping primitive labels.
**Boundary:** Research-protocol results do not imply stock TLS interoperability.
**Use in this review:** Distinguish protocol redesign from drop-in algorithm replacement.

Source context: Research authors; no independent reproduction or proof audit performed here.

## Benchmarks

### P09 · Benchmarking Post-Quantum Cryptography in TLS

[Douglas Stebila author archive](https://www.douglas.stebila.ca/research/papers/PQCrypto-PaqSteTam20/) · 2020
Access: **full_pdf_selected_sections**. Locator: PDF pages 1, 5, 6, 12.

Publication: PQCrypto 2020; author full version · conference_paper.

**Question:** How do network conditions change protocol costs?
**Approach:** Controlled Linux network emulation plus Internet experiments.
**What it supports:** Latency, packet loss and fragmentation change handshake behavior.
**Boundary:** Historical candidates and platforms cannot supply current product benchmarks.
**Use in this review:** Measure end-to-end conditions, not primitive cycles alone.

Source context: Research authors; no independent reproduction or proof audit performed here.

### P10 · pqm4: Testing and Benchmarking NIST PQC on ARM Cortex-M4

[IACR Cryptology ePrint Archive](https://eprint.iacr.org/2019/844) · 2019
Access: **full_pdf_selected_sections**. Locator: PDF pages 1, 2, 4.

Publication: Cryptology ePrint Archive 2019/844 · preprint_record.

**Question:** Which schemes fit a constrained microcontroller?
**Approach:** Board-specific functional, cycle, memory and code-size measurements.
**What it supports:** Resource limits exclude some implementations from the tested set.
**Boundary:** The candidate inventory is a July 2019 snapshot.
**Use in this review:** Keep hardware, implementation and measurement scope with results.

Source context: Research authors; no independent reproduction or proof audit performed here.

### P11 · pqm4: Benchmarking NIST Additional Post-Quantum Signature Schemes on Microcontrollers

[IACR Cryptology ePrint Archive](https://eprint.iacr.org/2024/112) · 2024
Access: **full_pdf_selected_sections**. Locator: PDF pages 1, 2, 3, 5.

Publication: Cryptology ePrint Archive 2024/112 · preprint_record.

**Question:** How do additional signatures behave on embedded hardware?
**Approach:** Integrates candidates and records performance and exclusion reasons.
**What it supports:** Memory, portability and implementation availability affect feasibility.
**Boundary:** A different board and candidate generation prevent naive historical comparisons.
**Use in this review:** Preserve exclusions and configuration alongside performance.

Source context: Research authors; no independent reproduction or proof audit performed here.

## Cryptanalysis

### P12 · KyberSlash: Exploiting secret-dependent division timings in Kyber implementations

[IACR Cryptology ePrint Archive](https://eprint.iacr.org/2024/1049) · 2025
Access: **abstract_only**. Locator: Primary abstract and publication metadata.

Publication: IACR TCHES 2025(2), 209–234; ePrint 2024/1049 · journal_article.

**Question:** Can implementation behavior defeat an otherwise studied design?
**Approach:** Primary abstract and author notes report timing experiments.
**What it supports:** Secret-dependent division enabled key recovery in affected implementations.
**Boundary:** The complete paper was not retrieved; this is not a break of all ML-KEM.
**Use in this review:** Inspect implementation, platform and patch scope separately.

Source context: Research authors; no independent reproduction or proof audit performed here.

### P13 · An efficient key recovery attack on SIDH

[IACR Cryptology ePrint Archive](https://eprint.iacr.org/2022/975) · 2023
Access: **abstract_only**. Locator: Primary abstract and publication metadata.

Publication: EUROCRYPT 2023; ePrint 2022/975 · conference_paper.

**Question:** Can a promising candidate fail under new analysis?
**Approach:** Primary abstract describes an attack exploiting SIDH auxiliary structure.
**What it supports:** The reported classical attack undermines the targeted construction.
**Boundary:** Abstract-only review cannot audit the proof or generalize to all isogeny schemes.
**Use in this review:** Keep cryptanalytic uncertainty and algorithm specificity visible.

Source context: Research authors; no independent reproduction or proof audit performed here.

