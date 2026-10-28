# Limitations and a falsifiable next study

## Remaining uncertainty

The supplied export's text is traceable, but source authorship, original activity dates and contributor contribution are not authenticated. Its references are not a complete claim-level bibliography. Vendor materials are first party and current web pages can change. Text extraction does not establish visual meaning. The planning model uses synthetic values and excludes whole categories of security questions.

## Next study: controlled compatibility rather than a security boast

**Status: proposal only.** The contributor should first explain and modify the present audit independently. If a technical extension is chosen, use only an owned local test environment and a maintained implementation; record exact versions and consult current official protocol/library documentation at that time.

| Design element | Precommitted procedure |
| --- | --- |
| Question | Does the selected implementation/configuration interoperate and fail predictably under the specified local setup? |
| Scope | One explicit cryptographic service and protocol; no general “PQC security” conclusion |
| Baseline | Documented classical configuration serving the same function |
| Change | Supported standardized PQC/hybrid configuration, only if the chosen library/protocol actually supports it |
| Repetitions | Define repeat count, warm-up and failure handling before collecting results; keep every trial |
| Measurements | Compatibility outcomes and error classes; performance only with an explicit timing protocol/environment |
| Controls | Same hardware/software/network fixture; no secrets or personal data in output |
| Negative controls | Unsupported configuration, incompatible peer and malformed input handled inside the local fixture |
| Acceptance | Reproducible setup and recorded failure behavior, not a claim to have proved quantum resistance |
| Stop rule | Stop if production systems, third-party targets, private keys or personal data become involved |

**What could overturn the current vendor conclusion?** A versioned independent report or reproducible comparable evaluation may support a narrower claim. **What could overturn a planning result?** Better inventory data, shorter confidentiality requirements or different migration duration/horizon assumptions. Record changed assumptions and retain the earlier run for comparison.

The study is not counted as completed contributor work until the contributor performs, documents and explains it. Leaving it as an explicit proposal is an honest endpoint for this version.
