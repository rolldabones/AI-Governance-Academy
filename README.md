# AI Governance Academy – Client Content Prompt Pack

Version 1.2.0 | 2026-07-10 | Status: draft | Model-agnostic

## Purpose

This pack contains prompt templates for generating Client-specific sales and delivery content for each of the six AI Governance Academy program options. Every template is model-agnostic: plain-text instruction blocks, no vendor-specific features, no tool calls assumed. Paste into any capable LLM.

## Contents

| File | Program | Duration | Price |
|---|---|---|---|
| 01-client-intake.md | Shared Client Intake (run first) | n/a | n/a |
| 02-executive-briefing.md | Executive Briefing | 2 hours | US$3,000 |
| 03-executive-workshop.md | Executive Workshop | 1 day | US$7,500 |
| 04-practitioner-academy.md | Practitioner Academy | 2 days | US$12,500 |
| 05-implementation-accelerator.md | Implementation Accelerator | 5 days | US$25,000 |
| 06-guided-ai-grc-build.md | Guided AI GRC Build | 12 weeks | US$60,000 |
| 07-fractional-advisor.md | Fractional AI Governance Advisor | 12 months | US$10,000/month |

## Workflow

1. Run 01-client-intake.md against raw Client information (notes, emails, RFP text, discovery call transcript). Output is a fenced **Client Profile Block**.
2. Open the template for the program option under discussion.
3. Paste the Client Profile Block into the Required Inputs section.
4. Select exactly one OUTPUT MODE per run.
5. Run. Verify against the numbered Acceptance Checklist at the bottom of each template before sending anything to the Client.

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

## License

This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0). To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/4.0/

You are free to share and adapt this material for non-commercial purposes, provided you give appropriate credit to Son-U Michael Paik, indicate if changes were made and distribute any derivatives under the same license. Commercial use requires prior written permission.

Attribution: AI Governance Academy Client Content Prompt Pack, Son-U Michael Paik, https://github.com/rolldabones

## Versioning

Semantic versioning applies. Breaking changes to the Client Profile Block schema or any Output Contract increment the major version. New output modes or templates increment the minor version. Corrections increment the patch version. See CHANGELOG.md.
