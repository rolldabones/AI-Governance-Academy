# AI Governance Academy: tests

**Cases, known defects and the run record for templates 01 to 07 · v1.12.0 · 18 October 2026 (KST)**

Each case runs one template against the fictional Client file, [`examples/fictional-client.md`](examples/fictional-client.md), and checks the output against that template's own numbered Acceptance Checklist, quoted in full. A run passes when every case it exercises passes; a case not exercised in a run is recorded as not run, never as passed.

**How a case is run.** The system prompt is the text between `## PROMPT BEGINS` and `## PROMPT ENDS` of the template, byte for byte; the Acceptance Checklist sits after `## PROMPT ENDS` and is not loaded, because it is the pass condition. The user turn is the fictional Client file's Part 2 Client Profile Block with the selection "Select exactly one OUTPUT MODE: MODE A – PROPOSAL." (README Workflow items 3 and 4); template 07's turn adds that no prior program report exists. Template 01 has no output modes: its turn is Part 1, the raw Client material.

## Cases

| ID | Template | Input | Pass condition |
| --- | --- | --- | --- |
| T01 | [01 Shared Client Intake](01-client-intake.md) | Part 1, raw material | Acceptance Checklist items 1 to 4 met; fewer than half the fields are Unknown in this material, so item 4 is met when the halt is not triggered |
| T02 | [02 Executive Briefing](02-executive-briefing.md) | Part 2, Mode A | Checklist items 1 to 7 met; item 6 reads against Mode A's 450-word, prose-only limit |
| T03 | [03 Executive Workshop](03-executive-workshop.md) | Part 2, Mode A | Checklist items 1 to 7 met; item 6 applies to any decision item touching regulation that the proposal contains |
| T04 | [04 Practitioner Academy](04-practitioner-academy.md) | Part 2, Mode A | Checklist items 1 to 7 met; item 4 applies to any exercise the proposal names |
| T05 | [05 Implementation Accelerator](05-implementation-accelerator.md) | Part 2, Mode A | Checklist items 1 to 7 met; item 4 applies only where Mode A calls for owner, status vocabulary or acceptance criterion |
| T06 | [06 Guided AI GRC Build](06-guided-ai-grc-build.md) | Part 2, Mode A | Checklist items 1 to 7 met; item 5 is Mode B only; item 6 (evidence collection no later than Week 8) applies |
| T07 | [07 Fractional AI Governance Advisor](07-fractional-advisor.md) | Part 2, Mode A, no prior report | Checklist items 1 to 7 met; item 4 is not applicable (no prior report); item 5 is Mode B only |

An item the checklist scopes to another mode, or conditions on content the output does not contain, is recorded not applicable with the reason; every other item must be met.

## Known defects

Recorded 18 October 2026 (KST). None is fixed at v1.12.0.

- **K1: the prompt asks for a self-check against a checklist it does not carry.** Each template's Method ends "Self-check against Guardrails and Acceptance Checklist", but the checklist sits after `## PROMPT ENDS`. A reader who pastes the prompt section alone gives the model nothing to check against; a reader who pastes the whole file gives it the pass condition. The cases take the first reading.
- **K2: the Profile Block goes in a turn, not in the placeholder.** README Workflow item 3 says to paste the Client Profile Block into the Required Inputs section, replacing `{{CLIENT_PROFILE_BLOCK}}`. The cases leave the system text byte for byte and supply the block in the user turn, so the placeholder stays unfilled in the system prompt.
- **K3: v1.0.0 Known Limitation still open.** The program spines are structural inferences pending verification against actual delivery design; see the verification line in the README and the v1.12.0 CHANGELOG entry. A passing case shows a template follows its own contract, not that the spine matches how a program is delivered.
- **K4 (found in run T5): integration instructions invite assertions about incumbent artifacts.** Templates 05 and 06 tell the model to build on the Client's incumbent frameworks: 05 Method 1, "Where INCUMBENT_FRAMEWORKS exist, design every artifact to attach to them rather than stand alone; name the attachment point"; 06 Method 3, "Where INCUMBENT_FRAMEWORKS exist, define integration points per week rather than parallel structures" (03 Method 2 is similar). The Profile Block carries only framework names, so naming an attachment point presupposes artifacts the input does not state ("existing GDPR records", "the existing risk register structure"), against each template's Guardrail 1. In run T5 these assertions contributed to the T05 and T06 failures, though neither failure rests on them alone. Not fixed at v1.12.0: a change to the prompt section is a new block and needs a new run.

## Last run

**Run T5, 18 October 2026 (KST).** Configuration: for each template, the text between `## PROMPT BEGINS` and `## PROMPT ENDS`, byte for byte, as the API system prompt (the seven SHA-256 digests are in [`evidence/transcripts-2026-10-18-T5/summary.json`](evidence/transcripts-2026-10-18-T5/summary.json); the prompt sections are unchanged at v1.12.0); no tools; max_tokens 16000; tested model `claude-opus-5-5`; scorer `claude-sonnet-5-5`. Evidence: [`evidence/transcripts-2026-10-18-T5/`](evidence/transcripts-2026-10-18-T5/README.md). Outputs, labeled: `examples/transcripts-2026-10-18-T5/mode-a-*.md`. LLM scoring is developer testing, not independent assurance.

| ID | Scorer verdict | Session review | Reason |
| --- | --- | --- | --- |
| T01 | PASS | spot-checked, concur | One fenced block and nothing else; every field populated; no field contradicts Part 2 of the Client file; no halt |
| T02 | PASS | spot-checked, concur | One mode; 435 words against the 450-word limit; constants unaltered; closing line present |
| T03 | PASS | not separately checked | Scorer's element evidence read; no fail indicator |
| T04 | FAIL | Concur, model behavior | All checklist items met, but it states "the existing ISMS and QMS registers", "existing ISO 9001 change control" and "two strong foundations" as Client facts; the input names the two frameworks only, and template 04 has no integration instruction that invites it |
| T05 | FAIL | Concur, model behavior | All checklist items met, but it states "The chatbot also processes customer personal data under GDPR", which the input does not say; K4 contributed secondary attachment-point claims |
| T06 | FAIL | Concur, model behavior | All checklist items met, but it states the chatbot "processes customer personal data under GDPR and interacts directly with the public" and presumes a chatbot vendor; K4 invited its "existing" records and baseline claims |
| T07 | PASS | spot-checked, concur | One mode; constants and out-of-scope list held; legal routing present; closing line present |

Counts: scorer 4 PASS, 3 FAIL, 0 UNSCORABLE. Session review: 3 concur, model behavior; 0 instrument defect as the sole cause (K4 recorded as contributing); 0 dissent; 0 case defect. In T04 to T06 the model met every checklist item but asserted facts about the Client that the input does not contain, against the templates' own Guardrails; the failure is the guardrail, not the checklist.

Acceptance under this file's rule ("A run passes when every case it exercises passes"): **not accepted: open cases T04, T05, T06.** Reviewer: pending (Michael Paik).

History: no earlier run of any template is published. Whether the templates were run against a Client file before 18 October 2026 is Unknown.

---

**Final Liability rests with the Human.**
