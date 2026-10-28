# Technical correction memo

The following are retrospective recommendations. The original deck is preserved unchanged. Source and claim IDs resolve in `evidence.json`.

| Source statement/locator | Evidence issue | Defensible replacement | Trace |
| --- | --- | --- | --- |
| Slide 4, security statement | Algorithm families and implementation conditions are unspecified | Selected PQC schemes are designed to resist known classical and quantum attacks under stated assumptions; this is not a system-wide guarantee | O-002 → O-008; C-002 |
| Slide 4, mathematical families | A list of research approaches can be mistaken for the finalized standardized set | Identify the actual algorithm and function being discussed; do not imply every listed family is equally standardized | O-001; S-002–004; C-003 |
| Slide 5, PQC/QKD distinction | Software versus physics does not compare complete security services | State the key-establishment/authentication responsibilities and the physical/protocol dependencies separately | O-003 → O-011; C-004 |
| Slide 7, RSA/ECC threat | Future capability is not an observed break of all deployed systems | Identify the vulnerable public-key function and scenario; do not assign an arrival date or extend the statement to all cryptography | O-004; S-006; C-007 |
| Slide 7, compliance motivation | No jurisdiction, organization or requirement is specified | Treat compliance as a question requiring an applicable rule and date, not proof this project/product is compliant | O-004; C-001 |
| Slide 9, government implementation | A broad deployment claim lacks an independently verified program/scope/date | Attribute to the deck; request dated agency/program evidence and distinguish pilot, test, procurement and authorization | O-005, O-013; C-005 |
| Slide 10, Layer-2 and security guarantee | Architecture and security/scalability claims lack claim-level support | Keep unverified pending a versioned architecture, algorithm/parameter details and independent evaluation | O-006, O-007, O-014; C-006 |

The abbreviated O/C suffixes above refer to full `O-EC5-...` and `C-EC5-...` IDs.

## Standards clarify function, not a product verdict

[NIST FIPS 203](https://csrc.nist.gov/pubs/fips/203/final) defines ML-KEM for establishing a shared secret; it is not itself an application data-encryption protocol. [FIPS 204](https://csrc.nist.gov/pubs/fips/204/final) defines ML-DSA signatures, and [FIPS 205](https://csrc.nist.gov/pubs/fips/205/final) defines hash-based SLH-DSA signatures. These roles must stay distinct when discussing replacement. A named standardized algorithm does not establish correct randomness, key handling, authentication, protocol integration, implementation or operation.

The [NSA QKD technical limitations](https://www.nsa.gov/Cybersecurity/Quantum-Key-Distribution-QKD-and-Quantum-Cryptography-QC/) explain why physical principles alone do not establish deployed assurance. This source has a National Security Systems context; the memo does not generalize that policy to all QKD research or applications.

**Strongest counterargument:** an introductory deck necessarily simplifies. **Response:** retain concise explanations but make assumptions explicit and link a deeper audit; correction need not turn every slide into a cryptographic specification.
