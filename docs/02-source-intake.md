# Source provenance / 원자료 추적

## Acquired material

The user supplied [the presentation](https://docs.google.com/presentation/d/1peRhHYgJG_D8uguCsuhvRnjvRsCMFWyXUypYKYCSjGI/edit). A public PPTX export was acquired on **2026-10-28** and preserved as `sources/original.pptx` (456,383 bytes).

**SHA-256:** `54afad5df9edde276dc3ec89b77cf48078ec6d92a1c3ef79b82b3eb33994c2ca`

`scripts/ingest_pptx.py` follows `ppt/presentation.xml` through its relationship table. It does not assume that filename order equals display order. The checked export contains **12 slides**, in this case resolving to slide1.xml through slide12.xml. `sources/slides.json` preserves the run order and relationship IDs. Text run indices in evidence locators are 1-based positions in each slide's `text` array.

## Source map

| Slide | Extracted focus | Audit use |
| --- | --- | --- |
| 1–3 | Title, contents, PQC section heading | Context only |
| 4 | PQC aim, mathematical bases, security statement | Conditional-security correction |
| 5 | PQC versus quantum cryptography | Function and infrastructure comparison |
| 6–7 | Motivation, RSA/ECC, protection and compliance | Threat and planning question |
| 8–9 | Companies heading, QuSecure | Vendor evidence boundary |
| 10 | Quranium, DeQUIP, Layer-2 and collaboration claims | Citation and assurance gap |
| 11 | Closing | Context only |
| 12 | References | Claim-level citation audit |

## What this acquisition establishes

It establishes the text present in this export and its slide order. It does not authenticate author identity, contribution, presentation date, conference attendance, conversations or third-party claims. The “2025” title is source labeling, not an independently established activity date. No speaker-note text was found in the exported note parts. Images, layout and visual meaning have not been rendered or audited.

The acquisition timestamp and technical review belong to 2026. Current vendor pages may differ from 2025 material. The cited QuSecure release carries a 2024 dateline but its present page contains later site content; it is not treated as an immutable historical snapshot.

## Updating the source

Keep the original export immutable. Acquire a new version under a new filename, record its hash and date, re-extract its text, and explain changes before updating claims. If a visual or note changes the interpretation, create a new observation and cite that precise region. Do not silently replace source bytes beneath an existing hash.
