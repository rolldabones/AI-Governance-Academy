# AI Governance Academy: Client Content Prompt Pack

Version 1.12.0 | 2026-10-18 | Status: final | Model-agnostic

## Purpose

This pack contains prompt templates for generating Client-specific sales and delivery content for each of the six AI Governance Academy program options. Every template is model-agnostic: plain-text instruction blocks, no vendor-specific features, no tool calls assumed. Paste into any capable LLM.

**Known limitation, open.** The program spines (workshop blocks, session counts, weekly sequence) are structural inferences pending verification against actual delivery design, as recorded in the first release. Verification of 18 October 2026 (KST): checked that each spine agrees with its template's Output Modes, Acceptance Checklist and the durations and prices in the Contents table, and that template 06's evidence collection starts by Week 8; not checked against any delivered program, because the repository holds no delivery record. The limitation stays open until that check is made.

## Contents

| File | Program | Duration | Price |
|---|---|---|---|
| 01-client-intake.md | Shared Client Intake (run first) | n/a | n/a |
| 02-executive-briefing.md | Executive Briefing | 2 hours | US$3,000 |
| 03-executive-workshop.md | Executive Workshop | 1 day | US$7,500 |
| 04-practitioner-academy.md | Practitioner Academy | 2 days | US$12,500 |
| 05-implementation-accelerator.md | Implementation Accelerator | 5 days | US$25,000 |
| 06-guided-ai-grc-build.md | Guided AI GRC Build | 12 weeks | US$60,000 |
| 07-fractional-advisor.md | Fractional AI Governance Advisor | 12 months | US$10,000 per month |

The repository also carries six client-facing publications alongside the templates: [sounds-good.md](sounds-good.md), *Sounds Good* (9 July 2026), on why AI outputs should be characterized as "sounds good" rather than "right" and what this requires of professional users, and [the-turtle-and-the-phoenix.md](the-turtle-and-the-phoenix.md), *The Turtle and the Phoenix* (30 July 2026), a teaching fable on human capability in the age of AI with the facilitation kit for using it in governance rooms, whose story is also published as an essay at https://redcaps.substack.com/p/the-turtle-and-the-phoenix, and [law-firm-ai-deployment-spec.md](law-firm-ai-deployment-spec.md), *Law Firm AI Deployment Spec v2* (22 August 2026), a 90-day specification for building a useful AI capability in a law firm that can be governed, explained and audited, written as an independent answer to the brief posed in Seth Fenster's LinkedIn post, which the document credits as its Version 1, and [slow-ai-for-the-chief-legal-officer.md](slow-ai-for-the-chief-legal-officer.md), *Slow AI for the Chief Legal Officer* (6 October 2026), a practical primer for legal leadership built on the partner-guardian tension and a four-cell map of known and unknown risk, with the Slow AI Kitchen as the method beneath it and a section on how an authorization survives a change of model, agent design or architecture; an I by IMD article was the occasion and is credited in the document as a starting point only, and [the-compression-and-the-harness.md](the-compression-and-the-harness.md), *The Compression and the Harness* (12 October 2026), a discussion piece that reads a language model as a lossy compression of the record and the software around it as a harness, argues that stating the destination and confirming the arrival stay with the Human, applies the eight elements of computational drafting to the everyday act of instructing a model and ends on ten questions for a governance room; Stephen Wolfram's interview with Jon Hernandez was the occasion and is credited in the document as a starting point only, and [the-map-and-the-pair.md](the-map-and-the-pair.md), *The Map and the Pair* (15 October 2026, second edition the same day), a discussion piece that offers a working vocabulary and three questions for reading claims that a model has discovered something: what was already on the map, who set the question and what checked the answer; the map as the record, four positions on it (a road, higher ground on a known hill, a valley and an undrawn mountain), the pair of proposer and verifier with the fix in two kinds, the asterisk as a claim the check did not reach, problem provenance as evidence and Base Camp, where Final Liability attaches at confirmation; OpenAI's openai/math release of October 2026 was the occasion, read from its own scope notes, challenge files and history, and the piece takes no position on the mathematics. None is a program template and no Output Contract applies to any of them.

## Workflow

1. Run 01-client-intake.md against raw Client information (notes, emails, RFP text, discovery call transcript). Output is a fenced **Client Profile Block**.
2. Open the template for the program option under discussion.
3. Paste the Client Profile Block into the Required Inputs section.
4. Select exactly one OUTPUT MODE per run.
5. Run. Verify against the numbered Acceptance Checklist at the bottom of each template before sending anything to the Client.

A labeled-fictional Client file for trying the workflow is in [examples/fictional-client.md](examples/fictional-client.md); the test cases built on it are in [tests.md](tests.md).

## Variable Conventions

- All variables use double braces: `{{CLIENT_NAME}}`.
- Unfilled required variables must halt generation with: `PARTIAL INPUT – Awaiting [variable list]`.
- Facts about the Client that are not present in the Client Profile Block must be rendered as `Unknown` and never invented.

## Fixed Elements (all templates)

- Program names, durations and prices are constants. No template may alter them.
- Framework names and URLs are constants: GRC Workbook (https://github.com/rolldabones/grc-workbook), Slow AI Kitchen (https://github.com/rolldabones/slow-ai-kitchen), the board-layer handbook AI Governance for Boards (https://github.com/rolldabones/ai-governance-for-boards) and the acceptance-layer doctrine The Definition of Done (https://github.com/rolldabones/definition-of-done).
- The three principles are always rendered exactly: Slow AI, Informed Intent, Final Liability rests with the Human.
- The closing line "Human-made, for Easy Work, Simply Done." appears once at the end of Client-facing documents.

## Style Rules Inherited by Every Template

- Professional prose. No em dashes. No Oxford commas. No emojis. No hashtags.
- Capitalize Client throughout.
- Currency as US$ with comma separators.
- No superlatives without evidence. No invented statistics, testimonials or case studies.

## Part of the ecosystem

This pack is one component of a larger body of AI governance, risk management and compliance work. The canonical map of all repositories is [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md) in the profile repository.

Nearest neighbors:
- [grc-workbook](https://github.com/rolldabones/grc-workbook): framework constant in every template; the build instrument the Guided AI GRC Build program delivers
- [slow-ai-kitchen](https://github.com/rolldabones/slow-ai-kitchen): framework constant; the method the Practitioner Academy teaches. Its Consultant Workbook is the delivery instrument for a 30-day initial engagement on one priority workflow; that engagement is not a program option of this pack and carries no price constant here
- [ai-governance-for-boards](https://github.com/rolldabones/ai-governance-for-boards): framework constant; the board-layer handbook cited where the audience includes directors
- [definition-of-done](https://github.com/rolldabones/definition-of-done): framework constant; the acceptance-layer doctrine cited where the engagement covers task-level acceptance discipline
- [the-ai-generalist](https://github.com/rolldabones/the-ai-generalist): the one-day corporate workshop on the same doctrines and the AI GRC minimum control set; it is not a program option of this pack and carries no price constant here

## How to Cite

> Paik, Son-U Michael. *AI Governance Academy: Client Content Prompt Pack*, v1.12.0. GRC Solutions Korea, 2026. https://github.com/rolldabones/AI-Governance-Academy

A machine-readable citation is in [CITATION.cff](CITATION.cff).

## License

This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0). To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/4.0/

You are free to share and adapt this material for non-commercial purposes, provided you give appropriate credit to Son-U Michael Paik, indicate if changes were made and distribute any derivatives under the same license. Commercial use requires prior written permission.

Attribution: AI Governance Academy Client Content Prompt Pack, Son-U Michael Paik, https://github.com/rolldabones

## Versioning

Semantic versioning applies. Templates 01 to 07 carry the pack version in their header lines, in lockstep (ruling 8 of 15 October 2026); there is no per-file version exception in this repository. Breaking changes to the Client Profile Block schema or any Output Contract increment the major version. New output modes or templates increment the minor version. Corrections increment the patch version. See CHANGELOG.md.

---

**Final Liability rests with the Human.**
