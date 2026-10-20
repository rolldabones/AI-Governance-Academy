**FICTIONAL CLIENT. Tamarack Instruments is an invented company; every name, figure, date and statement in this file is invented for testing the templates and describes no real organization or person.**

# Fictional Client File: Tamarack Instruments

Prepared 18 October 2026 (KST) | Test material for templates 01 to 08

## Purpose

This file is the fixed input for the pack's Mode A test runs. Part 1 is raw Client material of the kind template 01 takes. Part 2 is a Client Profile Block prepared by hand from Part 1 under template 01's rules, so that the runs of templates 02 to 08 do not depend on a run of template 01; the generated template 01 output of 18 October 2026 ([`mode-a-01-client-intake.md`](transcripts-2026-10-18-T5/mode-a-01-client-intake.md)) agrees in substance with Part 2 on every field and adds detail Part 2 omits: names in AUDIENCE_ROLES, the Q2 2027 date and the residency and works council items under STATED_CONSTRAINTS, the ISO/IEC 42001 start under STATED_OBJECTIVES, "No incidents or regulator contact mentioned" under RISK_EVENTS and four more confidence notes. No field contradicts Part 2. The seven generated outputs of that run are filed in [`transcripts-2026-10-18-T5/`](transcripts-2026-10-18-T5/) as `mode-a-<template>.md`, each labeled with model, date and verdict; the three that failed are marked as failing.

## Part 1. Raw Client material

<!-- fixture:raw:start -->
```text
Discovery call notes, 6 October 2026 (fictional). Attendees: Dana Whitfield,
General Counsel, Tamarack Instruments (fictional); Ravi Okafor, CISO; Ingrid
Solberg, Head of Quality.

- Tamarack designs and manufactures laboratory measurement instruments. HQ in
  the Netherlands; plants in the Netherlands and Germany; sales office in the
  United States. About 1,100 staff; Dana said revenue is "in the US$200 to
  300 million range".
- AI today: a customer service chatbot on the support portal is live
  (deployed). An AI visual inspection system on the German production line is
  in pilot. They plan to use AI for sales forecasting next year.
- Dana: "We are piloting, not scaling. I want governance in place before
  visual inspection goes into production in Q2 2027."
- Ravi: they run an ISO/IEC 27001 ISMS; Ingrid runs the quality management
  system under ISO 9001. They would like to start ISO/IEC 42001 work next
  year.
- Dana named the EU AI Act and the GDPR as the rules they are watching.
- Internal audit reported in June 2026 that there is no inventory of AI
  systems.
- Constraints: budget approved up to US$80,000 this fiscal year; customer
  data must stay in the EU; the German works council must be consulted before
  anything touches production staff.
- Who would attend: Dana, Ravi, Ingrid, the Head of Data (Tomas Reyes), the
  German plant manager and two internal auditors.
- Dana is the budget holder for this. Decision expected by 15 December 2026.
```
<!-- fixture:raw:end -->

## Part 2. Client Profile Block, prepared by hand from Part 1

<!-- fixture:profile:start -->
```
CLIENT PROFILE BLOCK v1.0
CLIENT_NAME: Tamarack Instruments (fictional)
INDUSTRY: Laboratory measurement instruments, design and manufacture
HEADQUARTERS_JURISDICTION: Netherlands
OPERATING_JURISDICTIONS: Netherlands, Germany, United States
COMPANY_SIZE: About 1,100 staff; revenue "in the US$200 to 300 million range"
AI_USE_CASES: Deployed: customer service chatbot on the support portal. Piloting: AI visual inspection on the German production line. Planned: AI sales forecasting next year.
AI_MATURITY: Piloting
REGULATORY_DRIVERS: EU AI Act; GDPR
CERTIFICATION_TARGETS: ISO/IEC 42001 (work to start next year)
AUDIENCE_ROLES: General Counsel; CISO; Head of Quality; Head of Data; German plant manager; two internal auditors
SPONSOR: Dana Whitfield, General Counsel
STATED_OBJECTIVES: "I want governance in place before visual inspection goes into production in Q2 2027."
STATED_CONSTRAINTS: Budget approved up to US$80,000 this fiscal year; customer data must stay in the EU; German works council consulted before anything touches production staff
INCUMBENT_FRAMEWORKS: ISO/IEC 27001 ISMS; ISO 9001 quality management system
RISK_EVENTS: Internal audit finding, June 2026: no inventory of AI systems
DECISION_TIMELINE: Decision expected by 15 December 2026
SOURCE_MATERIAL: Discovery call notes of 6 October 2026
CONFIDENCE_NOTES: Revenue band as spoken, not from filings; ISO/IEC 42001 start date not fixed
```
<!-- fixture:profile:end -->

## What the runs check

Each template's Mode A output is checked against that template's numbered Acceptance Checklist, item by item, with items scoped to other modes recorded as not applicable. Template 01 has no output modes; its run converts Part 1 and is checked against its own checklist. The cases, known defects and run record are in [`../tests.md`](../tests.md).

---

**Final Liability rests with the Human.**
