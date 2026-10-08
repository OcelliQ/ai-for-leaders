# Procurement brief: reference rubric

Supplied workshop reference for RFQ-ARER-26-014, one ARER-300 research test platform. This contains worked answers and can replace an incorrect student brief with their approval. It defines requirements, not bidder compliance or an award recommendation. Original signed, approved and issued sources govern if the case changes.

## 1. Source inventory and authority

| Source | Status and role |
| --- | --- |
| GRANT-01, v1.0, 1 April 2026 | Signed agreement: research objective, project term, ceiling and change rule |
| GRANT-02, v1.0, 1 April 2026 | Approved budget: allocation, excluding-GST comparison and finance checks |
| GRANT-03, v1.0, 1 April 2026 | Signed annex: milestones and evidence |
| GRANT-04, v1.0, 15 June 2026 | Approved PV-01: changes only the pilot checkpoint |
| RFQ-01, v1.0, 6 July 2026 | Issued request: scope, submission, dates, changes and approvals |
| RFQ-02, v1.0, 6 July 2026 | Issued mandatory schedule: M1–M7 and evidence |
| RFQ-03, v1.1, 20 July 2026 | Issued technical specification incorporating ADD-01 |
| RFQ-04, v1.0, 6 July 2026 | Issued commercial template: required price inclusions, C1–C8 |
| RFQ-05, v1.0, 6 July 2026 | Issued evaluation guide: gates, weights and locked panel scores |
| RFQ-06, v1.0, 28 August 2026 | Approved register: ADD-01 and ADD-02 only; closed at tender close |
| PLAN-01, v1.1, 20 June 2026 | Draft operational plan; context, not a grant or tender amendment |
| EMAIL-01, 10–11 August 2026 | Internal service clarification; context, not a new requirement |
| TECH-01, v1.0, 6 July 2026 | Approved terminology explainer; context, not tender authority |
| CASE-01, v1.0, 3 September 2026 | Generated case orientation and roles; also includes bidder information |

Requirement sources are in `case/01-project-and-grant/` and `case/02-tender/`; CASE-01 and TECH-01 are in `case/00-start-here/`. A complete inventory identifies the requirement-setting records and distinguishes contextual records; it need not claim all contextual documents were inputs to an isolated agent.

The signed grant and approved written variation define project terms; the issued RFQ and numbered formal addenda define tender requirements. A variation changes only what it expressly identifies. Draft plans, emails, workbooks, generated summaries and supplier claims cannot silently amend them. Sources: GRANT-01 §4.1, §7.2; RFQ-01 §2.1, §8.2; RFQ-06 §3.1; CASE-01 §4.3.

## 2. Purpose and scope

Buy one fixed-price platform, including mandatory options, installation, SAT, training and required service, to develop and validate lower-carbon semiconductor packaging materials. The validated reliability dataset is due 31 December 2029; operational capability must support verification and close-out through 31 March 2030. Sources: RFQ-01 §1.1, §5.2; GRANT-01 §1.1–§3.2.

Extract requirements before assessing offers. Do not use bid prices, bidder-specific features, previous rankings or the example recommendation to define the criteria. A source-cited brief is not evidence that runtime access restrictions were enforced.

## 3. Mandatory gates: all must pass

| Gate | Required rule | Evidence |
| --- | --- | --- |
| M1 | Complete evaluated price ≤ S$450,000 excluding GST | Submitted commercial schedule |
| M2 | SAT by 31 January 2027 | Submitted implementation plan; shipment or installation is insufficient |
| M3 | At least 48 specimens simultaneously per controlled run across specified ranges | Submitted technical schedule; sequential 24-position batches are insufficient |
| M4 | Raw readings AND event logs export as CSV OR JSON without a continuing vendor-hosted service | Submitted technical schedule; a dashboard alone is insufficient |
| M5 | Price includes installation, SAT and training for eight staff | Commercial and implementation schedules; training is on site |
| M6 | Warranty, two preventive-maintenance visits yearly and two-business-day response, from SAT through 31 March 2030 | Submitted service schedule, read with commercial and implementation records |
| M7 | Mandatory commitments entered the submitted proposal or formal pre-close tender record | Submitted record and RFQ-06; conditional correspondence is not a commitment |

Sources: RFQ-02 T1 M1–M7, §2.1–§3.2; RFQ-03 §2.1; RFQ-06 T1 ADD-02. Record the value, exact source locator, status and pass/fail/unresolved finding during verification. A failed gate excludes the bid from weighted ranking; missing or conditional evidence cannot be assumed compliant. Gates are not weighted criteria. Sources: RFQ-05 §1.1, §4.1–§4.2.

## 4. Technical, acceptance and handover requirements

The delivered configuration supports synchronised temperature, mechanical load and electrical bias at every simultaneous specimen position: −40 °C to 125 °C, 0 to 500 N and 0 to 24 V. Sources: RFQ-03 §1.1–§1.2.

Exports preserve channel identifiers, timestamps, units, operating settings, raw readings and event codes in documented CSV or JSON. Files remain locally readable after the hosted account ends. Sources: RFQ-03 §3.1, §4.1.

SAT demonstrates configured simultaneous operation, required ranges, sample raw export, event logging and operator handover; reconcile sample readings with the controller display. Record configuration, serial identifiers, procedure, results, open items, owners and signatures. Representative specimens or simulator loads may be used when they demonstrate the supplied configuration. Retain training attendance and export evidence. Sources: RFQ-01 §7.1, §10.2; RFQ-03 §4.2; GRANT-03 §3.1.

Provide an as-installed configuration list, operating instructions, exported-field description and event-log retrieval procedure. Train eight staff on site using the delivered configuration, including a hands-on export exercise. Sources: RFQ-03 §2.1, §5.1.

## 5. Scoring

| Criterion | Weight | Basis |
| --- | --- | --- |
| Technical performance and useful capacity | 35% | Locked panel score, 0–100; excess capacity has diminishing benefit |
| Total evaluated lifecycle cost | 30% | Locked panel score, 0–100; complete included cost and price bands |
| Delivery, installation and training | 20% | Locked panel score, 0–100; plan credibility and lead time |
| Service above mandatory minimum | 15% | Locked panel score, 0–100; minimum compliance is not full marks |

Weights total 100%. Eligible total = 0.35 × technical + 0.30 × cost + 0.20 × delivery/training + 0.15 × service; round the sum to one decimal place. Recorded criterion scores do not change or renormalise when another bid fails. Only gate-passing bids enter the weighted ranking. Do not invent price bands, scores or a new rubric when details are absent. Sources: RFQ-05 T1, §2.2, §4.2.

## 6. Complete cost and service

The single controlling ceiling is S$450,000 excluding GST. Planning allocations are S$360,000 platform/options, S$30,000 installation/SAT/training and S$60,000 warranty/maintenance/support; these are not independent bidder gates. Sources: GRANT-01 §2.1, §6.1–§6.2; GRANT-02 T1, §2.1.

C6 evaluated price is SUM(C1:C5): base instrument, mandatory options, installation/SAT, eight-person training, and warranty/maintenance/support through 31 March 2030. Identify GST separately in C7; C8 exclusions or optional accessories must not conceal mandatory cost. Unpriced future options are not included commitments. Reconcile component sums, total and included scope; unresolved arithmetic goes to Finance and Procurement. Sources: RFQ-04 T1 C1–C8; RFQ-01 §3.1, §5.2; GRANT-02 §2.2, §4.1.

Service starts at SAT and covers warranty, two PM visits yearly and two-business-day response through 31 March 2030. Dataset delivery on 31 December 2029 does not end service; PV-01 does not move the service end. Response time is not a promised repair-completion time. Sources: RFQ-02 T1 M6; RFQ-04 T1 C5; GRANT-03 §2–§3.3; GRANT-04 §2–§3.2.

## 7. Dates and change control

| Date | Meaning |
| --- | --- |
| 1 April 2026 | Project starts |
| 6 July 2026 | RFQ issued |
| 20 July 2026 | ADD-01 clarifies temperature wording; −40 °C retained |
| 5 August 2026 | ADD-02 confirms on-site venue and eight-person class |
| 14 August 2026 | Written clarification questions due |
| 28 August 2026, 17:00 Singapore time | Tender closes; addendum register closed with only ADD-01 and ADD-02 |
| 30 September 2026 | Draft PLAN-01 decision/PO target, not a mandatory RFQ date |
| 31 January 2027 | SAT/equipment commissioning deadline |
| 31 March 2028 | Revised pilot checkpoint; originally 28 February 2028 |
| 31 December 2029 | Validated dataset due |
| 31 March 2030 | Project close-out and required service end |

Sources: GRANT-01 §1.1, §3.2; GRANT-03 T1; GRANT-04 §1–§2; RFQ-01 §2.1; RFQ-02 T1; RFQ-06 T1, §2; PLAN-01 T1.

Only numbered formal Procurement addenda change tender requirements. A bidder's material change must be a formal revision accepted into the record by close. Clarifications may explain existing commitments; conditional emails, expectations and pending approvals do not amend them. Post-close informal explanations cannot establish new price, warranty or capability commitments; a separate applicable formal process would be required. Distinguish Institute-issued addenda from bidder-specific revisions. Sources: RFQ-01 §4.1, §6.2, §8.2, §9.3; RFQ-06 §3.1–§4.2.

## 8. People, evidence and unresolved questions

Dr. Anika Rao owns research need and technical rationale; the Evaluation Panel assesses gates and recommends; Mira Tan owns procurement process, clarification status and bidder contact; Joel Lim checks complete cost and GST; the Executive Approval Committee makes the human award decision. A brief, AI memo or recommendation does not authorise contact, amendment, supplier selection or award. Sources: CASE-01 T4, §5.1–§5.3; RFQ-01 §8.1; RFQ-05 §3.1.

Every decisive requirement must retain a document ID and usable clause/table/row locator. Uncertainty needs a named resolver rather than an invented rule. Reasonable questions include business-day calendar, PM treatment of part-years, warranty scope, unavailable full addendum texts, unspecified scoring-band detail and process-approved arithmetic resolution. These are examples, not required wording or a mandatory question count. Mira Tan routes process questions, Joel Lim cost questions and Dr. Rao technical questions.

RFQ-02 workbook cells abbreviate M4/M5; the fuller T1 schedule and RFQ-03 govern their interpretation. This is not evidence that event logs or implementation evidence are optional. A passed draft target date alone does not prove a missed milestone or move SAT. Do not require the historical baseline's date-sensitive or speculative questions in new briefs.

## Acceptance rubric

| Dimension | Must-pass evidence | Material errors or omissions |
| --- | --- | --- |
| Source scope and authority | Requirement-setting inventory; signed/issued versus context distinction; no supplier-derived rules | Omitting an authority-changing source or using bids, draft plans or summaries to change requirements |
| Mandatory gates | All seven gates, complete obligations, all-pass eligibility before ranking | Missing/relaxing any gate; scoring a failed or unknown gate as eligible |
| Technical and acceptance | Simultaneous capacity, all ranges, raw readings and logs, independent export, actual SAT and eight-person on-site training | Sequential capacity, wrong ranges, dashboard-only data, shipment instead of SAT or omitted training |
| Scoring | Four named criteria, exact weights, locked scores, formula, final one-decimal rounding | Wrong weights, invented scores or renormalisation; treating gates as weighted slices |
| Budget and support | Complete ≤ S$450,000 ex GST, mandatory inclusions, service from SAT to 31 March 2030 with required cadence/response | Instrument-only cost, GST included in the gate, omitted service or earlier support end |
| Dates and changes | SAT, varied pilot, dataset and close-out dates; narrow PV-01 effect; formal tender change rule | Using the pilot or dataset date as service end, changing SAT from a draft plan, treating email as amendment |
| Traceability and uncertainty | Usable source locators for decisive claims; missing/conflicting evidence labelled and routed | Fabricated citations, untraceable decisive values, invented resolutions or presumed compliance |
| Accountability and boundaries | Panel recommendation, Finance/Procurement checks and human committee award; no bid ranking in this extraction output | AI award authority, unauthorised bidder contact or offer-specific conclusions presented as requirements |

All eight dimensions must meet for **Substantially correct**; do not average away a material error. An absent core rule is **Incomplete**; a contradictory rule is **Incorrect**; unresolvable source verification is **Unable to verify**. A report may meet through equivalent concise wording and cross-references. Extra export-field, handover-document, record-retention and administrative-date detail is an improvement when the core obligation is preserved, not an automatic fail. Exact titles, versions, headings and the number or wording of questions are not grading targets. The accepted compressed example remains substantially correct under this rule despite its documented minor omissions.
