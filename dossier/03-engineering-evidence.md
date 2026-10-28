# Engineering evidence: connect the layers

## 1 · Threat model before a date

Shor's algorithm establishes a mathematical reason that certain public-key problems change under quantum computation. Resource estimates ask a different question: what a fault-tolerant construction might require under specified physical assumptions. Gidney–Ekerå and the later Gidney estimate illustrate how engineering choices change the space/time trade-off. Neither is a calendar forecast or a demonstration that a present machine has broken deployed RSA-2048. [P01, P03, P04](04-paper-atlas.md)

The planning exercise in this repository belongs to a third layer. Mosca's timing discussion connects confidentiality lifetime, migration duration and the hypothetical threat horizon. The existing slack calculation implements that family of reasoning with a conservative equality trigger. It is neither a probability model nor a new empirical discovery. Its conceptual lineage is now explicit. [P02](04-paper-atlas.md)

## 2 · Construction papers and current standards

Kyber, Dilithium and SPHINCS+ investigate different constructions and functions. Their papers help explain design choices and assumptions. Current implementation requirements must come from the relevant standards and versions, rather than treating an earlier submission as byte-for-byte equivalent to its standardized descendant. [P05–P07](04-paper-atlas.md), [S01–S03](05-deployment-record.md)

Frodo investigates a different point in the lattice design space. Its purpose in this review is to expose an assumption/engineering trade-off, not to declare that one algebraic structure is universally preferable. Historical operation times also cannot serve as present platform measurements. [P14](04-paper-atlas.md)

This distinction matters commercially: naming a standardized algorithm identifies a function, not the completeness of a product's key handling, integration or operational assurance.

## 3 · A hybrid needs a construction

Combining classical and post-quantum components requires a specified adversary model, combiner, authentication design and encoding. The hybrid-KEM paper supplies formal distinctions; the published RFC supplies a construction with a stated scope. The RFC is **Informational**, and it excludes authentication from its intended coverage. Publication as an RFC is not itself an Internet Standards Track designation or a product validation. [P08](04-paper-atlas.md), [D10](05-deployment-record.md)

KEMTLS illustrates why cryptographic functions cannot simply be exchanged by label. It changes the handshake design to authenticate with KEMs. That is a protocol-research result, not evidence that an arbitrary KEM can replace a signature in unmodified TLS software. [P15](04-paper-atlas.md)

## 4 · Performance is a system observation

The TLS benchmarking paper uses controlled network conditions to separate effects that primitive microbenchmarks cannot isolate. Median handshake behavior, tail latency and whole-page retrieval time answer different questions. Results depend on message fragmentation, packet loss, network latency, scheme version and configuration. A number from one of those endpoints cannot silently stand in for another. [P09](04-paper-atlas.md)

The older pqm4 record and the later additional-signature study show a different boundary: what can be built and fit on constrained hardware. Memory, portability and exclusion reasons are part of the result. Different devices, candidate generations, optimizations and measurement scopes prevent a naive historical speed ranking. [P10–P11](04-paper-atlas.md)

Several historically benchmarked candidates have since changed status. A paper can remain useful as an experimental method while its candidate table becomes unsuitable as a deployment shortlist.

## 5 · An implementation attack and a design break differ

The KyberSlash record concerns secret-dependent implementation timing in affected software. The SIDH record concerns a targeted construction and auxiliary information. They are strong reasons to preserve version and threat-model specificity, not evidence that every post-quantum scheme shares one failure. The review of these two items is explicitly limited to primary abstracts and the identified supporting descriptions. [P12–P13](04-paper-atlas.md)

The newer corecrypto account adds another assurance category: implementation correctness against specifications. Correctness, hardening and complete protocol security must still be distinguished. This review records the vendor's stated proof scope and has not independently audited the proofs. [D11](05-deployment-record.md)

## 6 · What a new experiment would need

A credible local experiment would name:

1. The question and cryptographic function, including authentication assumptions.
2. Exact implementation, compiler, provider and protocol versions.
3. The workload, hardware and network conditions, with units and endpoints.
4. Functional and negative controls, including failure paths.
5. Repeated runs, distribution summaries and exclusion reasons.
6. Raw artifacts sufficient to reproduce the stated observation.

The present repository supplies a source review and deterministic planning arithmetic. It has not run the cryptographic experiments surveyed here. A later experiment should report its own conditions and outcomes instead of borrowing a paper's performance numbers.
