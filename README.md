# AI Governance Academy

Version 1.14.7 | 2026-10-26 | Status: final (known limitation and test status open; see Purpose) | Model-agnostic

**Acceptance status ([ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md), 26 October 2026, KST):** Not accepted. Run A4 (26 October 2026) of the published templates passed 7 of 24 samples and none of the 8 cases after review, below the 80 percent ACCEPTANCE.md (c) requires; the open defects K7, K8 and K9 and the residual K5 are listed in tests.md. The account's status table is in [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md#instrument-status).

**Caution.** The templates are unvalidated: no template is accepted under [tests.md](tests.md) and the program spines are not verified against a delivered program (known defect K3), so every output rests on the human check at Workflow item 5.

This repository has two halves. The first is the Client Content Prompt Pack: eight prompt templates that generate Client-specific sales and delivery content for the AI Governance Academy program options. The second is the Publications: six client-facing pieces, from an essay on how to characterize AI output to a working vocabulary for reading discovery claims, published here as the text of record. The halves share one version number, one license and one closing line.

## Client Content Prompt Pack

### Purpose

This pack contains prompt templates for generating Client-specific sales and delivery content for each of the seven AI Governance Academy program options. Every template is model-agnostic: plain-text instruction blocks, no vendor-specific features, no tool calls assumed. Paste into any capable large language model (LLM). In the program name Guided AI GRC Build, GRC stands for governance, risk management and compliance.

**Known limitation, open.** The program spines (workshop blocks, session counts, weekly sequence) are structural inferences pending verification against actual delivery design, as recorded in the first release. Verification of 18 October 2026 (Korea Standard Time, KST): checked that each spine agrees with its template's Output Modes, Acceptance Checklist and the durations and prices in the Contents table, and that template 06's evidence collection starts by Week 8; not checked against any delivered program, because the repository holds no delivery record. The limitation stays open until that check is made.

**Test status, open.** No template at this version is accepted under [tests.md](tests.md): in runs A2 and A3 of 20 October 2026 and A4 of 26 October 2026 (KST), three samples per case, the model still inferred relations between Client facts the Profile Block does not state (known defect K5) and used lists in template 02's prose-only letter (K6). Run A4 found three open defects in the text: template 01 lacks the relation guard (K7), template 04 has no asset category for the fable kit (K8) and no template says whose the decision date is (K9). These defects are controlled at Workflow item 5, by the human who verifies each output before it reaches the Client.

### Contents

| File | Program | Duration | Price |
|---|---|---|---|
| 01-client-intake.md | Shared Client Intake (run first) | n/a | n/a |
| 02-executive-briefing.md | Executive Briefing | 2 hours | US$3,000 |
| 03-executive-workshop.md | Executive Workshop | 1 day | US$7,500 |
| 04-practitioner-academy.md | Practitioner Academy | 2 days | US$12,500 |
| 05-implementation-accelerator.md | Implementation Accelerator | 5 days | US$25,000 |
| 06-guided-ai-grc-build.md | Guided AI GRC Build | 12 weeks | US$60,000 |
| 07-fractional-advisor.md | Fractional AI Governance Advisor | 12 months | US$10,000 per month |
| 08-one-workflow-thirty-days.md | One Workflow, Thirty Days | 30 days | by proposal |

### Offerings ladder

The ladder is shared with the profile README (github.com/rolldabones) and is written identically there. The Slow AI Kitchen Workshop and The AI Generalist appear on it but are not program options of this pack: the Workshop is a facilitation design that runs as Day 2 of the Practitioner Academy, and The AI Generalist is its own repository.

| Duration | Offering | Instrument | Price |
|---|---|---|---|
| 2 hours | Executive Briefing | [AI-Governance-Academy, template 02](02-executive-briefing.md) | US$3,000 |
| 1 day | Executive Workshop (executive leadership) | [AI-Governance-Academy, template 03](03-executive-workshop.md) | US$7,500 |
| 1 day | The AI Generalist (working professionals) | [the-ai-generalist](https://github.com/rolldabones/the-ai-generalist) | by proposal |
| 2 days | Practitioner Academy (the Slow AI Kitchen workshop is Day 2) | [AI-Governance-Academy, template 04](04-practitioner-academy.md) | US$12,500 |
| 5 days | Implementation Accelerator | [AI-Governance-Academy, template 05](05-implementation-accelerator.md) | US$25,000 |
| 30 days | One Workflow, Thirty Days (the Consultant Workbook engagement) | [slow-ai-kitchen/consultant-workbook.md](https://github.com/rolldabones/slow-ai-kitchen/blob/main/consultant-workbook.md); [AI-Governance-Academy, template 08](08-one-workflow-thirty-days.md) | by proposal |
| 12 weeks | Guided AI GRC Build | [AI-Governance-Academy, template 06](06-guided-ai-grc-build.md) | US$60,000 |
| 12 months | Fractional AI Governance Advisor | [AI-Governance-Academy, template 07](07-fractional-advisor.md) | US$10,000 per month |

GRCnext™: [GRCnext-Copilot](https://github.com/rolldabones/GRCnext-Copilot) and [RedCap-00](https://github.com/rolldabones/RedCap-00) are public and free; GRCnext™ advisory is on inquiry.

### Workflow

1. Run 01-client-intake.md against raw Client information (notes, emails, request for proposal (RFP) text, discovery call transcript). Output is a fenced **Client Profile Block**.
2. Open the template for the program option under discussion.
3. Supply the Client Profile Block: paste it into the Required Inputs section in place of `{{CLIENT_PROFILE_BLOCK}}`, or give the template's prompt section as the system prompt and the Profile Block as the user message. The test cases in [tests.md](tests.md) use the second form.
4. Select exactly one OUTPUT MODE per run.
5. Run. Before sending anything to the Client, verify the output against the numbered Acceptance Checklist at the bottom of the template and against its Guardrails, and remove or render `Unknown` any Client fact or relation the Profile Block does not state. This check is the control for the residual defects recorded in [tests.md](tests.md).

A labeled-fictional Client file for trying the workflow is in [examples/fictional-client.md](examples/fictional-client.md); the test cases built on it are in [tests.md](tests.md).

**Evidence and examples.** Most of this repository by size is the record of the test runs in [tests.md](tests.md). Each run has two folders: `evidence/transcripts-<date>-<run>/` holds the transcripts, the scores, `summary.json` and, from run A1, the harness, with a README that says what was run, when and how; `examples/transcripts-<date>-<run>/` holds the same generated outputs, labeled, as examples. The runs are T5 of 18 October 2026 and A1, A2 and A3 of 20 October 2026: [evidence/transcripts-2026-10-18-T5/](evidence/transcripts-2026-10-18-T5/), [evidence/transcripts-2026-10-20-A1/](evidence/transcripts-2026-10-20-A1/), [evidence/transcripts-2026-10-20-A2/](evidence/transcripts-2026-10-20-A2/) and [evidence/transcripts-2026-10-20-A3/](evidence/transcripts-2026-10-20-A3/). Read the evidence README of a run before its transcripts. Glosses of the three principles inside a generated output, passing or not, are model output, not doctrine; the doctrines are as stated in [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md), the account's single normative statement of the three doctrines. The example `examples/transcripts-2026-10-20-A3/mode-a-05-implementation-accelerator-s1.md`, for instance, glosses Slow AI in words the doctrine does not use.

### Variable Conventions

- All variables use double braces: `{{CLIENT_NAME}}`.
- Unfilled required variables must halt generation with: `PARTIAL INPUT – Awaiting [variable list]`.
- Facts about the Client that are not present in the Client Profile Block must be rendered as `Unknown` and never invented.

### Fixed Elements (all templates)

- Program names, durations and prices are constants. No template may alter them.
- Framework names and URLs are constants: GRC Workbook (https://github.com/rolldabones/grc-workbook), Slow AI Kitchen (https://github.com/rolldabones/slow-ai-kitchen), the board-layer handbook AI Governance for Boards (https://github.com/rolldabones/ai-governance-for-boards) and the acceptance-layer doctrine The Definition of Done (https://github.com/rolldabones/definition-of-done).
- The three principles are always rendered exactly: Slow AI, Informed Intent, Final Liability rests with the Human.
- The closing line "Human-made, for Easy Work, Simply Done." appears once at the end of Client-facing documents.

### Style Rules Carried by Every Program Template

Templates 02 to 08 state these rules in their own Style Rules, because a model sees only the prompt section. Template 01 returns a fenced block and no prose.


- Professional prose. No em dashes. No Oxford commas. No emojis. No hashtags.
- Capitalize Client throughout.
- Currency as US$ with comma separators.
- No superlatives without evidence. No invented statistics, testimonials or case studies.

## Publications

Six client-facing publications sit beside the templates, each the text of record for its piece, dated with its first publication and described by the occasion its own masthead names. None is a program template and no Output Contract applies to any of them.

| File | Title | Date | Kind | Words | Occasion |
|---|---|---|---|---|---|
| [sounds-good.md](sounds-good.md) | *Sounds Good* | 9 July 2026 | essay | 2,200 | none |
| [the-turtle-and-the-phoenix.md](the-turtle-and-the-phoenix.md) | *The Turtle and the Phoenix* | 30 July 2026 | teaching fable with facilitation kit | 7,200 | none |
| [law-firm-ai-deployment-spec.md](law-firm-ai-deployment-spec.md) | *Law Firm AI Deployment Spec v2* | 22 August 2026 | specification | 4,000 | Seth Fenster's LinkedIn post, credited as Version 1 |
| [slow-ai-for-the-chief-legal-officer.md](slow-ai-for-the-chief-legal-officer.md) | *Slow AI for the Chief Legal Officer* | 6 October 2026 | primer | 7,400 | I by IMD article by Mezzano, Trantopoulos and Wade |
| [the-compression-and-the-harness.md](the-compression-and-the-harness.md) | *The Compression and the Harness* | 12 October 2026 | discussion piece | 7,800 | Stephen Wolfram's interview with Jon Hernandez |
| [the-map-and-the-pair.md](the-map-and-the-pair.md) | *The Map and the Pair* | 15 October 2026 | discussion piece | 10,800 | OpenAI's openai/math release of October 2026 |

The date is the masthead date of first publication; *The Map and the Pair* is in its second edition, revised the same day, and the CHANGELOG entries of 15 October 2026 record the changes. The story of *The Turtle and the Phoenix* is also published as an essay at https://redcaps.substack.com/p/the-turtle-and-the-phoenix; the file here adds the facilitation kit. Words are counted with `wc -w` at v1.14.0 and rounded to the nearest hundred.

### How to cite a publication

> Paik, Son-U Michael. *Sounds Good*. In AI Governance Academy, v1.14.7. GRC Solutions Korea, 2026. https://github.com/rolldabones/AI-Governance-Academy/blob/main/sounds-good.md

> Paik, Son-U Michael. *The Turtle and the Phoenix*. In AI Governance Academy, v1.14.7. GRC Solutions Korea, 2026. https://github.com/rolldabones/AI-Governance-Academy/blob/main/the-turtle-and-the-phoenix.md

> Paik, Son-U Michael. *Law Firm AI Deployment Spec v2*. In AI Governance Academy, v1.14.7. GRC Solutions Korea, 2026. https://github.com/rolldabones/AI-Governance-Academy/blob/main/law-firm-ai-deployment-spec.md

> Paik, Son-U Michael. *Slow AI for the Chief Legal Officer*. In AI Governance Academy, v1.14.7. GRC Solutions Korea, 2026. https://github.com/rolldabones/AI-Governance-Academy/blob/main/slow-ai-for-the-chief-legal-officer.md

> Paik, Son-U Michael. *The Compression and the Harness*. In AI Governance Academy, v1.14.7. GRC Solutions Korea, 2026. https://github.com/rolldabones/AI-Governance-Academy/blob/main/the-compression-and-the-harness.md

> Paik, Son-U Michael. *The Map and the Pair*. In AI Governance Academy, v1.14.7. GRC Solutions Korea, 2026. https://github.com/rolldabones/AI-Governance-Academy/blob/main/the-map-and-the-pair.md

## Part of the ecosystem

This pack is one component of a larger body of AI governance, risk management and compliance work. The canonical map of all repositories is [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md) in the profile repository.

Nearest neighbors:
- [grc-workbook](https://github.com/rolldabones/grc-workbook): framework constant in every program template; the build instrument the Guided AI GRC Build program delivers
- [slow-ai-kitchen](https://github.com/rolldabones/slow-ai-kitchen): framework constant; the method the Practitioner Academy teaches. Its Consultant Workbook engagement, One Workflow, Thirty Days, is template 08 of this pack and carries no published price
- [ai-governance-for-boards](https://github.com/rolldabones/ai-governance-for-boards): framework constant; the board-layer handbook cited where the audience includes directors
- [definition-of-done](https://github.com/rolldabones/definition-of-done): framework constant; the acceptance-layer doctrine cited where the engagement covers task-level acceptance discipline
- [the-ai-generalist](https://github.com/rolldabones/the-ai-generalist): the one-day corporate workshop on the same doctrines and the AI GRC minimum control set; it is not a program option of this pack and carries no price constant here

## How to Cite

> Paik, Son-U Michael. *AI Governance Academy: Client Content Prompt Pack and Publications*, v1.14.7. GRC Solutions Korea, 2026. https://github.com/rolldabones/AI-Governance-Academy

A machine-readable citation is in [CITATION.cff](CITATION.cff).

## License

This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0). To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/4.0/

You are free to share and adapt this material for non-commercial purposes, provided you give appropriate credit to Son-U Michael Paik, indicate if changes were made and distribute any derivatives under the same license. Commercial use requires prior written permission.

Attribution: AI Governance Academy: Client Content Prompt Pack and Publications, Son-U Michael Paik, https://github.com/rolldabones

## Versioning

Semantic versioning applies. Templates 01 to 08 carry the pack version in their header lines, in lockstep, by Michael Paik's decision of 15 October 2026; there is no per-file version exception in this repository. Breaking changes to the Client Profile Block schema or any Output Contract increment the major version. New output modes or templates increment the minor version, and so does a new publication or a new edition of one: publication releases move the minor version. Corrections increment the patch version. See CHANGELOG.md.

---

**Final Liability rests with the Human.**
