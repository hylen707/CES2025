# Argument map

The ledger stores three different things: **source observation**, **retrospective analysis**, and **proposal**. “Verified source content” means the text was found at the specified locator; it does not certify the text's truth or contributor ownership.

| Claim | Evidence path | Warrant | Strong alternative | Boundary |
| --- | --- | --- | --- | --- |
| C-001: conceptual introduction | Deck O-001/003/007 | Definitions and examples are documented; an implementation method is not | Images/notes or omitted material could add detail | Text-only conclusion |
| C-002: qualify security wording | Deck O-002 → NIST O-008 | Conditional assumptions cannot support an unconditional guarantee | Introductory simplification | No attack or implementation test |
| C-003: separate functions | NIST O-008/009/010 | Key establishment and signatures serve distinct roles | Grouping is reasonable at overview level | No protocol recommendation |
| C-004: compare complete assumptions | Deck O-003 → NSA O-011 | Authentication and engineering remain necessary | Particular QKD systems may mitigate constraints | No universal technology ranking |
| C-005: limit vendor conclusions | Deck O-005/006 → vendor O-013/014 | Different positioning and missing comparable measurements do not justify a winner | Nonpublic evidence could exist | Neither endorsement nor insecurity claim |
| C-006: repair citation gaps | Deck O-006/007 → O-014 | Current category marketing cannot establish a historical architecture claim | An original source may have been omitted | Missing support is not falsity |
| C-007: inspect planning assumptions | Deck O-004 → NCCoE O-012 → run O-015 | Discovery and planning can be studied without inventing security tests | A toy rule simplifies deployment reality | Educational heuristic only |
| C-008: scenario-sensitive result | Run O-015 → arithmetic | Hypothetical horizon changes the trigger | Different inputs can reverse the result | No predicted quantum date |
| C-009: compatibility follow-up | NCCoE O-012 | Planning arithmetic leaves interoperability untested | Scope can stop at a source audit | Proposed, not completed |

Full IDs use the `EC5` prefix in the machine-readable ledger. Each claim includes exact observation IDs, matching source locators, reasoning, counterargument, limitation and status. `scripts/validate_project.py` checks those links and rejects duplicate/dangling IDs; it cannot decide whether an argument is scientifically sound.

## Why the argument is stronger after qualification

The output is now falsifiable: a reader can identify the claim, locate its evidence, challenge the reasoning and state what would change the conclusion. A stronger claim would require stronger evidence, not more emphatic phrasing. Independent reasoning by the contributor remains a separate requirement from the retrospective audit.
