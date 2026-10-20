# AI Governance Academy: tests

**Cases, known defects and the run record for templates 01 to 08 · v1.14.5 · 20 October 2026 (Korea Standard Time, KST)**

Each case runs one template against the fictional Client file, [`examples/fictional-client.md`](examples/fictional-client.md), and checks the output against that template's own numbered Acceptance Checklist, quoted in full. A run passes when every case it exercises passes; a case not exercised in a run is recorded as not run, never as passed.

**How a case is run.** The system prompt is the text between `## PROMPT BEGINS` and `## PROMPT ENDS` of the template, byte for byte (the lines strictly between the two marker lines, less the blank line that follows `## PROMPT BEGINS`, each line ending in a newline; this rule reproduces the seven T5 digests in `summary.json`); the Acceptance Checklist sits after `## PROMPT ENDS` and is not loaded, because it is the pass condition. The user turn is the fictional Client file's Part 2 Client Profile Block with the selection "Select exactly one OUTPUT MODE: MODE A – PROPOSAL." (README Workflow items 3 and 4); template 07's turn adds that no prior program report exists. Template 01 has no output modes: its turn is Part 1, the raw Client material.

## Cases

| ID | Template | Input | Pass condition |
| --- | --- | --- | --- |
| T01 | [01 Shared Client Intake](01-client-intake.md) | Part 1, raw material | Acceptance Checklist items 1 to 4 met; fewer than half the fields are Unknown in this material, so item 4 is met when the halt is not triggered |
| T02 | [02 Executive Briefing](02-executive-briefing.md) | Part 2, Mode A | Checklist items 1 to 7 met; item 6 reads against Mode A's limit of 450 words, the sign-off and the closing line included, and prose only |
| T03 | [03 Executive Workshop](03-executive-workshop.md) | Part 2, Mode A | Checklist items 1 to 7 met; item 6 applies to any decision item touching regulation that the proposal contains |
| T04 | [04 Practitioner Academy](04-practitioner-academy.md) | Part 2, Mode A | Checklist items 1 to 7 met; item 4 applies to any exercise the proposal names |
| T05 | [05 Implementation Accelerator](05-implementation-accelerator.md) | Part 2, Mode A | Checklist items 1 to 7 met; item 4 applies only where Mode A calls for owner, status vocabulary or acceptance criterion |
| T06 | [06 Guided AI GRC Build](06-guided-ai-grc-build.md) | Part 2, Mode A | Checklist items 1 to 7 met; item 5 is Mode B only; item 6 (evidence collection no later than Week 8) applies |
| T07 | [07 Fractional AI Governance Advisor](07-fractional-advisor.md) | Part 2, Mode A, no prior report | Checklist items 1 to 7 met; item 4 is not applicable (no prior report); item 5 is Mode B only |
| T08 | [08 One Workflow, Thirty Days](08-one-workflow-thirty-days.md) | Part 2, Mode A | Checklist items 1 to 8 met; item 3 reads price and headcount as by proposal with no figure; item 6 applies to every W-record the proposal cites; item 7 applies to any decision item touching regulation that the proposal contains |

An item the checklist scopes to another mode, or conditions on content the output does not contain, is recorded not applicable with the reason; every other item must be met. Where a run draws more than one sample of a case, the case passes only when every sample passes.

**Scorer guidance (from v1.14.3).** A consequence that follows from a stated constraint applied to a stated system is not a new Client fact (the works council constraint applied to a system on the production line); neither is proposed work nor a conditional statement. Asserted current states, owners, attributions, incumbent functions and relations that the Profile Block does not state are failures. Runs before v1.14.3 were scored without this guidance; their session reviews applied it as dissents.

**Harness rule (from v1.14.4).** Every execution of a run writes to its own output folder and log; every execution is reported with its result, kept or not; a re-run needs a stated reason and Michael Paik's approval before it starts, and the reason is recorded with the run.

**Acceptance and residual defects.** A template is accepted when a logged run passes every sample of its case and the reviewer's decision recorded with that run accepts it; a case that passes every sample without that decision stays open. Where the model's residual defects keep a case from passing after the prompt section has been corrected for them, the defects are recorded here as residual, with their rates, and the control is the human check at README Workflow item 5: every output is verified against its checklist and Guardrails before it reaches the Client.

## Known defects

Recorded 18 October 2026 (KST); K5 and K6 recorded 20 October 2026 (KST). Status at v1.14.5: K1, K2 and K4 fixed, with no recurrence in run A3; K5 residual; K6 resolved for templates 03 and 08 by removing the rule and residual for template 02; K3 open. Residual defects are controlled at README Workflow item 5.

- **K1: the prompt asks for a self-check against a checklist it does not carry.** Each template's Method ended "Self-check against Guardrails and Acceptance Checklist", but the checklist sits after `## PROMPT ENDS`. A reader who pastes the prompt section alone gives the model nothing to check against; a reader who pastes the whole file gives it the pass condition. The cases take the first reading. **Fixed in text at v1.14.0:** the Method step of templates 02 to 08 reads "Self-check against the Style Rules and Guardrails below", which the prompt section carries; the checklist stays outside it as the pass condition. Run A1 attributed no failure to K1.
- **K2: the Profile Block goes in a turn, not in the placeholder.** README Workflow item 3 said to paste the Client Profile Block into the Required Inputs section, replacing `{{CLIENT_PROFILE_BLOCK}}`. The cases leave the system text byte for byte and supply the block in the user turn, so the placeholder stays unfilled in the system prompt. **Fixed in text at v1.14.0:** README Workflow item 3 names both forms and says the cases use the second.
- **K3: v1.0.0 Known Limitation still open.** The program spines are structural inferences pending verification against actual delivery design; see the verification line in the README and the v1.12.0 CHANGELOG entry. A passing case shows a template follows its own contract, not that the spine matches how a program is delivered.
- **K4 (found in run T5): integration instructions invite assertions about incumbent artifacts.** Templates 05 and 06 told the model to build on the Client's incumbent frameworks (05 Method 1, "name the attachment point"; 06 Method 3, "define integration points per week"; 03 Method 2 similar), while the Profile Block carries only framework names, so naming an attachment point presupposed artifacts the input does not state, against each template's Guardrail 1. **Fixed in text at v1.14.0** in templates 03, 04, 05, 06 and 08: framework names are not evidence of any register, process, control or record the Client holds, and an attachment point the Profile Block does not state is rendered `Unknown`. **Run A1:** no recurrence in T04, T05 and T08, and T05, which failed on it in run T5, passed; T06 stated who holds the incumbent systems (recorded under K5); T07 stated incumbent ISO 9001 processes, because templates 02 and 07 had not received the rule. **Fixed in text at v1.14.1:** templates 02 and 07 carry the rule in Guardrail 1.
- **K5 (found in run A1): the model infers relations between Profile Block facts that the block does not state.** The block lists facts field by field; the model joined them: the internal auditors in AUDIENCE_ROLES as the source of the finding in RISK_EVENTS (T04, T06, and attempt 1's T03 and T08), the ISMS and QMS owners as present (T06), the participants' time zone (T03) and the pilot's maturity and its link to product acceptance (T08). K4's rule, written for registers, processes, controls and records, does not reach these. **Fixed in text at v1.14.1:** templates 02 to 08 carry a final Guardrail: "Do not infer relations the Profile Block does not state between its facts: who raised, owns or attends what, where people are based or the state of a system. Where the deliverable needs such a relation, render it `Unknown`." **Run A2 (v1.14.1):** recurred in 11 of 24 samples; on review, most of them stated attributions that Part 1 of the fixture gives and Part 2 had dropped (case defect C1, below), and the rest (T02-s1, T03-s2, T04-s2) stand as model behavior. **Run A3 (v1.14.2):** after review under the scorer guidance, recurred in 1 of 24 samples (T06-s1: an existing governance team, owners of controls, the audit finding closed). **Residual at v1.14.3**, controlled at Workflow item 5.

- **K6 (found in run A2): "Prose only" does not hold.** Mode A of templates 02, 03 and 08 ended "Prose only."; every sample of T03 and T08 and one of T02 used bulleted or numbered lists under headings. **Fixed in text at v1.14.2:** the three Mode A lines read "Prose only: paragraphs under section headings, with no bullet lists, numbered lists or tables." **Run A3 (v1.14.2):** lists in 8 of 9 samples (all of T03 and T08, two of T02); over runs A2 and A3, T03 and T08 kept to prose in 0 of 12 samples. **At v1.14.3,** on Michael Paik's decision, the rule is removed from the two-page proposals of templates 03 and 08 and their checklist items, and kept for template 02's one-page letter, where it is **residual** (3 of 6 samples kept to prose over runs A2 and A3), controlled at Workflow item 5.
- **C1, case defect (found in run A2): Part 2 of the fixture dropped three attributions that Part 1 states.** Part 2 had named the Sponsor without "budget holder", quoted STATED_OBJECTIVES without its speaker and given SOURCE_MATERIAL without its attendees, while Part 1 states all three and template 01's outputs in runs T5 and A1 carry them. Samples that stated these attributions failed against Part 2 alone. **Fixed at v1.14.2:** Part 2 carries the three attributions. A case defect changes the input, so runs before v1.14.2 used the earlier Part 2.

**Instrument notes (runs A2 and A3).** In A3 the scorer again applied the constraint reading unevenly: it failed T04-s1, T04-s2 and T06-s3 for applying stated constraints to stated systems and passed T05-s3 and T07-s2 for the same pairing; the scorer guidance of v1.14.3 settles the reading. In run A2, the scorer applied checklist item 4 of template 04 unevenly (T04-s2 was passed as "borderline" on the same pattern that failed T04-s1 and T04-s3), counted a `Unknown` rendered under the K4 rule as a failure (T04-s2) and read two consequences of a stated constraint as unstated (T05-s3). The checklists required URLs where frameworks are cited, but no prompt section said so; at v1.14.2 the Style Rules of templates 02 to 08 add "Name each framework with its URL", and template 04's Mode A asks for each named exercise's module or pattern and artifact.

## Last run

**Run A3, 20 October 2026 (KST).** Cases T01 to T08 against the v1.14.2 prompt sections and fixture at `7fe5751`, the head of pull request rolldabones/AI-Governance-Academy#1 before it was merged, three samples per case; configuration otherwise as for run A2. Evidence: [`evidence/transcripts-2026-10-20-A3/`](evidence/transcripts-2026-10-20-A3/README.md). Outputs, labeled: `examples/transcripts-2026-10-20-A3/mode-a-*-s*.md`. LLM scoring is developer testing, not independent assurance.

| Run and case | Samples (s1, s2, s3) | Case verdict | Session review | Reason |
| --- | --- | --- | --- | --- |
| A3 T01 | FAIL, PASS, PASS | FAIL | concur | s1 records the ISMS as "run by Ravi Okafor"; Part 1 says "Ravi: they run an ISO/IEC 27001 ISMS" |
| A3 T02 | FAIL, FAIL, PASS | FAIL | concur | s1 and s2 use lists in the prose-only letter (K6) |
| A3 T03 | FAIL, FAIL, FAIL | FAIL | concur | Lists in every sample (K6; rule removed at v1.14.3) |
| A3 T04 | FAIL, FAIL, FAIL | FAIL | s1, s2 dissent, PASS; s3 concur on item 4 | s1 and s2 apply stated constraints to stated systems, not Client facts under the scorer guidance; s3 names the fable kit's closing exercise without its artifact or module |
| A3 T05 | PASS, PASS, PASS | PASS | concur | Every applicable item met in all samples |
| A3 T06 | FAIL, PASS, FAIL | FAIL | s1 concur; s3 dissent, PASS | s1 states an existing governance team, owners of controls and the audit finding closed (K5); s3 applies the works council constraint to the production-line system |
| A3 T07 | PASS, PASS, PASS | PASS | concur | Every applicable item met in all samples |
| A3 T08 | FAIL, FAIL, FAIL | FAIL | concur | Lists in every sample (K6; rule removed at v1.14.3) |

**Two executions (recorded at v1.14.4).** The A3 harness ran twice; the first execution (scorer: 13 of 24 samples PASS, 1 of 8 cases, T02) was overwritten on a suggestion of the Claude session that prepared run A3, whose reason was not recorded, and the run report described the second only. The record above and the evidence are the second execution; the first survives as a console summary in the evidence README. Neither execution is accepted.

Counts: by sample, scorer 10 PASS, 14 FAIL, 0 UNSCORABLE; after review, 13 PASS and 11 FAIL (8 of them K6). By case, 2 PASS (T05, T07), 6 FAIL. Session review of the 14 failing samples: 11 concur, 3 dissent to PASS (T04-s1, T04-s2, T06-s3).

Acceptance: **not accepted: open cases T01, T02, T03, T04, T06, T08.** Reviewer: Michael Paik, 20 October 2026 (KST), concurs with the positions as recorded.

Independent review, 20 October 2026: T05 and T07 passed every sample in this run, but the reviewer's decision above does not accept templates 05 and 07, so under the acceptance rule they also stay open; no template is accepted (README Purpose, Test status).

**Correction to run A2's record.** At v1.14.2 this file said that A2's T01 result "also describes v1.14.2", because template 01 and its input were unchanged. A3's T01-s1 failed on the same prompt section and input: a run's result does not carry over to another run, because each sample is drawn anew.

**Status after A3.** On Michael Paik's decision of 20 October 2026 (KST), no further run is scheduled for this pull request: v1.14.3 removes the prose-only rule from templates 03 and 08, records K5 and template 02's K6 as residual and adds the scorer guidance, and the templates stand **not accepted**, with the residual defects controlled at README Workflow item 5. A later run, under the scorer guidance, may accept a template; it takes the name of the session that makes it.

## Earlier runs

Result rows are labeled by run and case, so that no script reading the Cases table above can take a result row for a case row.

**Run A2, 20 October 2026 (KST).** Cases T01 to T08 against the v1.14.1 prompt sections at `11981fc`, the head of pull request rolldabones/AI-Governance-Academy#1 before it was merged, three samples per case; configuration otherwise as for run A1 (tested model `claude-opus-5-5`, scorer `claude-sonnet-5-5`, no tools, max_tokens 16000). The fixture was Part 2 as it stood at v1.14.1. Evidence: [`evidence/transcripts-2026-10-20-A2/`](evidence/transcripts-2026-10-20-A2/README.md). Outputs, labeled: `examples/transcripts-2026-10-20-A2/mode-a-*-s*.md`. LLM scoring is developer testing, not independent assurance.

| Run and case | Samples (s1, s2, s3) | Case verdict | Session review | Reason |
| --- | --- | --- | --- | --- |
| A2 T01 | PASS, PASS, PASS | PASS | concur | Every sample one fenced block, every field populated, no halt |
| A2 T02 | FAIL, FAIL, FAIL | FAIL | s1, s2 concur; s3 case defect C1 | s1 cites frameworks without URLs and states the June finding as current (K5); s2 uses a bulleted list (K6) |
| A2 T03 | FAIL, FAIL, FAIL | FAIL | concur | Lists in every sample (K6); s2 states that most of the budget remains available (K5); s3 cites frameworks without URLs |
| A2 T04 | FAIL, FAIL, FAIL | FAIL | concur; dissent on one indicator of s2 | s1 and s3: an exercise names no asset or artifact (item 4); s2 states the chatbot carries GDPR and residency into every exercise (K5); its information-security-policy point was rendered `Unknown` as required |
| A2 T05 | PASS, FAIL, FAIL | FAIL | s2 case defect C1; s3 dissent, PASS | s2 states attributions Part 1 gives; s3's two indicators follow from Part 2 |
| A2 T06 | FAIL, FAIL, PASS | FAIL | s1 case defect C1; s2 case defect C1, dissent on one indicator | Attributions Part 1 gives; "production plan" follows from the stated objective |
| A2 T07 | PASS, PASS, PASS | PASS | concur | Constants, out-of-scope list and legal routing held; no incumbent process asserted |
| A2 T08 | FAIL, FAIL, FAIL | FAIL | concur | Lists in every sample (K6); s1 and s3 also carry C1 attributions |

Counts: by sample, scorer 8 PASS, 16 FAIL, 0 UNSCORABLE; by case, 2 PASS (T01, T07), 6 FAIL. Session review of the 16 failing samples: 11 concur as model behavior (T08-s1 and T08-s3 also carry C1 attributions), 4 recorded as case defect C1 (T02-s3, T05-s2, T06-s1, T06-s2), 1 dissent to PASS (T05-s3); dissents on single indicators in T04-s2 and T06-s2. Under the rule that a case passes only when every sample passes, the dissents do not change any case verdict.

Acceptance: **not accepted: open cases T02, T03, T04, T05, T06, T08.** Reviewer: Michael Paik, 20 October 2026 (KST), concurs with the positions as recorded.

**Run A1, 20 October 2026 (KST).** Configuration as for run T5, with case T08 added: for each template, the prompt section extracted by the rule above as the API system prompt; no tools; max_tokens 16000; tested model `claude-opus-5-5`; scorer `claude-sonnet-5-5`; one sample per case. The eight SHA-256 digests in [`evidence/transcripts-2026-10-20-A1/summary.json`](evidence/transcripts-2026-10-20-A1/summary.json) are of the v1.14.0 prompt sections at `e4f3a97`, the head of pull request rolldabones/AI-Governance-Academy#1 before it was merged. Evidence: [`evidence/transcripts-2026-10-20-A1/`](evidence/transcripts-2026-10-20-A1/README.md), with a superseded first attempt kept and explained there. Outputs, labeled: `examples/transcripts-2026-10-20-A1/mode-a-*.md`. LLM scoring is developer testing, not independent assurance.

| Run and case | Scorer verdict | Session review | Reason |
| --- | --- | --- | --- |
| A1 T01 | PASS | concur | One fenced block; every field populated; no halt. INCUMBENT_FRAMEWORKS adds "internal audit function", which Part 1, the case's input, supports |
| A1 T02 | FAIL | concur, model behavior; rule ambiguous | 455 words with the sign-off and the closing line against the 450-word limit, 443 without; the template did not say which, and v1.14.1 says they count |
| A1 T03 | FAIL | concur, model behavior | States "All listed participants appear to be based in Central European Time" and schedules on that basis (K5) |
| A1 T04 | FAIL | concur, model behavior | States "The internal auditors who raised the finding take part" (K5); counts "those seven roles" against six roles. No incumbent artifact asserted |
| A1 T05 | PASS | concur | Every applicable item met; attachment points rendered `Unknown` |
| A1 T06 | FAIL | concur, model behavior | States "The two internal auditors raised the June 2026 finding" and that the ISMS and QMS owners are in the room (K5); attachment points rendered `Unknown` |
| A1 T07 | FAIL | concur; instrument contributing | States "existing ISO 9001 change control" and the disciplines the two management systems provide; template 07 lacked the K4 rule (fixed at v1.14.1) |
| A1 T08 | FAIL | concur, model behavior | States that the workflow "is mature enough to run supervised cases against a matched baseline" and that "inspection outcomes connect directly to product acceptance" (K5) |

Counts: scorer 2 PASS, 6 FAIL, 0 UNSCORABLE. Session review: 8 concur; T02 records an ambiguous rule and T07 an instrument gap as contributing; 0 dissent; 0 case defect. One sample per case: the run does not measure variance, and attempt 1 drew different outputs from the same configuration.

Acceptance under this file's rule: **not accepted: open cases T02, T03, T04, T06, T07, T08.** Reviewer: Michael Paik, 20 October 2026 (KST), concurs with the positions as recorded.

**Run T5, 18 October 2026 (KST).** The v1.12.0 prompt sections of templates 01 to 07 (seven SHA-256 digests in [`evidence/transcripts-2026-10-18-T5/summary.json`](evidence/transcripts-2026-10-18-T5/summary.json)); no tools; max_tokens 16000; tested model `claude-opus-5-5`; scorer `claude-sonnet-5-5`. Evidence: [`evidence/transcripts-2026-10-18-T5/`](evidence/transcripts-2026-10-18-T5/README.md). Outputs, labeled: `examples/transcripts-2026-10-18-T5/mode-a-*.md`. No T5 digest matches a later prompt section.

| Run and case | Scorer verdict | Session review | Reason |
| --- | --- | --- | --- |
| T5 T01 | PASS | spot-checked, concur | One fenced block and nothing else; every field populated; no field contradicts Part 2 of the Client file; no halt |
| T5 T02 | PASS | spot-checked, concur | One mode; 435 words against the 450-word limit; constants unaltered; closing line present |
| T5 T03 | PASS | not separately checked | Scorer's element evidence read; no fail indicator |
| T5 T04 | FAIL | Concur, model behavior | All checklist items met, but it states "the existing ISMS and QMS registers", "existing ISO 9001 change control" and "two strong foundations" as Client facts; the input names the two frameworks only, and template 04 has no integration instruction that invites it |
| T5 T05 | FAIL | Concur, model behavior | All checklist items met, but it states "The chatbot also processes customer personal data under GDPR", which the input does not say; K4 contributed secondary attachment-point claims |
| T5 T06 | FAIL | Concur, model behavior | All checklist items met, but it states the chatbot "processes customer personal data under GDPR and interacts directly with the public" and presumes a chatbot vendor; K4 invited its "existing" records and baseline claims |
| T5 T07 | PASS | spot-checked, concur | One mode; constants and out-of-scope list held; legal routing present; closing line present |

Counts: scorer 4 PASS, 3 FAIL, 0 UNSCORABLE. Session review: 3 concur, model behavior; 0 instrument defect as the sole cause (K4 recorded as contributing); 0 dissent; 0 case defect. Acceptance: **not accepted: open cases T04, T05, T06.** Reviewer: Michael Paik, 19 October 2026 (KST), concurs.

History: no run before T5 is published. Whether the templates were run against a Client file before 18 October 2026 is Unknown.

---

**Final Liability rests with the Human.**
