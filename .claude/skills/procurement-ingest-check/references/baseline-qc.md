# Procurement brief baseline QC

Reviewed 6 October 2026. Verdict: **substantially correct; accepted as a known-good example with the caveats below**. The participant reports generating this brief with Claude Opus 5.5; model provenance was not independently verified.

`BRIEF.md.gz` is an exact, deterministic gzip copy of `task/BRIEF.md`, without editorial changes. Decompressed SHA-256: `493f5faa747fb78b69700f9c5b52dd0b2bf70f86b02c96971e542be3cab476a1`. Read it with `gzip -dc BRIEF.md.gz` or Python's `gzip` module. The `/procurement-ingest-check` skill uses this historical example alongside `reference-rubric.md`. Approved replacements copy the reference rubric, not this compressed example.

## Findings

The document covers all fourteen requirement and context documents in its inventory. Checked against their PDFs, plus the RFQ-02, RFQ-04 and GRANT-02 Markdown companions for workbook cells. No submitted bids or evaluation records were consulted for this review. The brief contains no bidder prices, rankings or eligibility conclusions, although CASE-01 itself includes bid information and therefore is not an isolated requirements-only source.

All seven mandatory gates and their evidence requirements match RFQ-02 T1. The 48 simultaneous positions, temperature/load/bias ranges, independent CSV/JSON export, eight-person training, SAT deadline and required service duration are correct. The S$450,000 excluding-GST ceiling, budget allocations and C1–C5 price inclusions reconcile. The four weights (35/30/20/15), weighted formula, one-decimal rounding and fixed panel scores match RFQ-05. Grant dates, the limited effect of PV-01, formal addenda and human approval roles also match. Source IDs and locators support the core claims.

## Caveats for the checker

- **Additional technical detail:** The brief cites RFQ-03 §4.1 but does not enumerate exported channel identifiers, timestamps, units, operating settings and event codes, or its documented file structure. It also omits some documentation and handover detail from RFQ-03 §5.1 and GRANT-03 §3.1 (as-installed configuration list, operating instructions, exported-field description, event-log retrieval procedure and retained training attendance). These are useful coverage improvements, not failures of the extracted headline gates.
- **Q1–Q2 are wording differences:** The workbook abbreviates the M4 export and M5 evidence descriptions; the explicit RFQ-02 T1 text and RFQ-03 §2.1 supply the fuller requirements. Do not treat these questions as evidence that event logs or implementation evidence are optional, or require participants to reproduce them as genuine contradictions.
- **Q5 is partly answered:** RFQ-01 §4.1 and §9.3 establish the formal pre-close revision route for a bidder's commitment. RFQ-06 records Institute-issued requirement addenda. The brief distinguishes these correctly in §9; only the detailed recording mechanics remain unspecified.
- **Q6–Q7 concern missing rubric detail:** RFQ-05 provides locked panel scores and weights; this brief's scope excludes evaluation records. A checker should not infer that those questions authorise inventing new scores, price bands or a scoring rubric.
- **Post-close changes:** The §9 shorthand that a post-close explanation “cannot add” a new price, warranty or capability should be read as “cannot establish a new commitment through informal correspondence”. RFQ-01 §6.2 explicitly refers to an applicable formal process; do not turn this into an absolute prohibition on every separately authorised later procurement action.
- **Date-sensitive Q9:** The draft target of 30 September 2026 has passed as of this review, but that alone does not show that a decision or purchase order was missed. There is no completion evidence in the reviewed source set. This question is review-date context, not a new requirement or a fact the checker must demand in every brief.

Use this as a semantic comparison example, not an exhaustive answer key. Equivalent wording and other well-supported unresolved questions are acceptable. Requirement documents remain authoritative; recheck the baseline if their contents change. Keep the reference-check activity out of section 5 attendee instructions.

## Reviewed source fingerprints

Paths are relative to `task/`; hashes record the exact source versions checked.

| Source | SHA-256 |
| --- | --- |
| `case/00-start-here/CASE-01-executive-case-brief.pdf` | `060e81ff57f51bed4a345876ee25774984ce6b2f102f071923ae0f5f866056ff` |
| `case/00-start-here/TECH-01-plain-language-encabulation-explainer.pdf` | `8c379e9b0408498ec457f79b2294fe0d531d796b9eee5d7ac8a194e22b122a54` |
| `case/01-project-and-grant/EMAIL-01-internal-clarification-on-project-end-service.pdf` | `7b1f68d72e2a0294e896309b3ac0fba207aa8616717f364f4d5c394e8fed50b5` |
| `case/01-project-and-grant/GRANT-01-grant-award-and-project-agreement.pdf` | `f30504d75b93e238d2850525fcdab9bcc3cb7e42747f4cb28afb3e1c175effe0` |
| `case/01-project-and-grant/GRANT-02-approved-equipment-budget-schedule.pdf` | `695702c9f44758d58b534e1998e3a684910ff60b6239df691ac51b9eedc59e6f` |
| `case/01-project-and-grant/GRANT-03-milestones-and-deliverables-annex.pdf` | `27026bca5905ed860de27b1ce38771c5812003544d2eca9841bf868f591122ed` |
| `case/01-project-and-grant/GRANT-04-approved-project-variation-pv-01.pdf` | `c90d21f40284c3d9e1cb688814beb20b86fc758cdd774df6cf8338e60819c962` |
| `case/01-project-and-grant/PLAN-01-pi-implementation-and-experiment-plan.pdf` | `112dfdb0802b28d087f5ec53223ebf275b70fc3f18e0d0a6588020a36aae198e` |
| `case/02-tender/RFQ-01-open-tender-request-rfq-arer-26-014.pdf` | `c544e2f241d5c95e065ed9f18b99176a0f16ff2253c4aa7755805b892d568750` |
| `case/02-tender/RFQ-02-mandatory-requirements-schedule.pdf` | `59f2b4c53c588a84314706b7808077dcce79614625f97157de10f7402d5f5926` |
| `case/02-tender/RFQ-03-technical-specification-for-arer-300.pdf` | `b2b08f29cc6e3281bc20a6e236c8703cb7b073ae8b9237230026bccc8c627f10` |
| `case/02-tender/RFQ-04-commercial-response-template.pdf` | `3242bda172b4ac835fc213897092b5b75550ce757b44eb78383d764a4c270723` |
| `case/02-tender/RFQ-05-evaluation-guide.pdf` | `702292367dd7e277e7f373646fc52a255172aed1eded7e664bb89d8952cc4c84` |
| `case/02-tender/RFQ-06-formal-tender-addendum-register.pdf` | `e6c2ea28000ef02d542cdee08f6228b941667de06b96b391151132c91c54e307` |
| `case/01-project-and-grant/GRANT-02-approved-equipment-budget-schedule.pdf.md` | `87a1a6feb65d8f502ea936d0fb0e347228d91497d47e154a3b79a15fb5890d2d` |
| `case/02-tender/RFQ-02-mandatory-requirements-schedule.pdf.md` | `33fcdf3b045ceef4bf45ab86546fda72a8219c7e84881cba348b010c5613a595` |
| `case/02-tender/RFQ-04-commercial-response-template.pdf.md` | `f36cda838e0c12f1c9b4066937d60b0981b54697ec4a9988555c67d8c66dc50b` |
