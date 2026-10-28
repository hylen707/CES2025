# Reproducible extension: migration timing sensitivity

## Design

This experiment was newly prepared on **2026-10-28**. All assets and input values are synthetic, chosen to expose model boundaries. They are not derived from the student's school, an employer, a bank, a vendor or any live infrastructure.

The [NCCoE migration project](https://www.nccoe.nist.gov/applied-cryptography/migration-to-pqc) motivates separating discovery/planning from interoperability. The following arithmetic is this repository's own educational planning rule, not a NIST scoring method.

For an explicitly modeled vulnerable confidentiality use:

`slack_years = hypothetical_quantum_horizon − confidentiality_lifetime − migration_duration`

A **planning trigger** occurs when unrounded slack is less than or equal to zero. All inputs are in years relative to the hypothetical planning start. This is a conservative planning margin, not an estimate of breach probability, a forecast of quantum arrival, or a direct model of any captured ciphertext. It cannot answer whether a system is secure. Positive slack is not permission to delay migration.

## Inputs and boundary cases

| Asset | Synthetic use | Lifetime | Migration | Why included |
| --- | --- | ---: | ---: | --- |
| A-001 | RSA-2048 archive key transport | 15 | 3 | Long-lived confidentiality |
| A-002 | ECDH-P256 web session key agreement | 0.1 | 2 | Short-lived confidentiality |
| A-003 | ECDSA-P256 updater signatures | 0 | 4 | Signatures must not be evaluated as decryption timing |
| A-004 | Unknown service/algorithm | 10 | 3 | Missing data must stay unknown |
| A-005 | ML-KEM-768 pilot | 10 | 2 | A PQC name must not automatically become a safe verdict |

## Results

The deterministic run writes **15 rows** to [JSON](../results/migration_scenarios.json) and [CSV](../results/migration_scenarios.csv).

| Asset | Horizon 5 years | Horizon 10 years | Horizon 20 years |
| --- | --- | --- | --- |
| A-001 | Trigger; −13 years | Trigger; −8 years | Positive slack; +2 years |
| A-002 | Positive slack; +2.9 | Positive slack; +7.9 | Positive slack; +17.9 |
| A-003 | Signature review | Signature review | Signature review |
| A-004 | Inventory gap | Inventory gap | Inventory gap |
| A-005 | Algorithm review | Algorithm review | Algorithm review |

**Interpretation:** retention and migration assumptions can make a long-lived archive a planning trigger even when an imminent quantum-computer date is not asserted. The three excluded assets demonstrate that an inventory tool should preserve uncertainty and function-specific analysis rather than return a misleading low-risk label.

**Sensitivity:** decreasing A-001's assumed lifetime from 15 to 5 years would change its 10-year slack from −8 to +2. Increasing migration duration by one year lowers slack by one year. These are properties of the defined equation, not empirical discoveries about actual organizations.

## What was not measured

No quantum hardware, crypto implementation, throughput, memory, latency, interoperability, key compromise, attack resistance, vendor product or migration cost was measured. The method does not score symmetric cryptography, signature forgery, certificate trust, key lifecycle or implementation assurance. A manually supplied inventory is not automated cryptographic discovery.

The tests check boundary equality, tiny positive slack, monotonicity, invalid input and deliberate exclusion cases. They establish software behavior for this rule; they do not validate the rule as an enterprise risk method.
