# Changelog

All notable changes to the AI Governance Academy Client Content Prompt Pack are documented here. Format follows Keep a Changelog conventions. Versioning is semantic.

## [1.13.2] – 2026-10-20

Patch, from the repository audit of 20 October 2026 (KST). Corrections only: no prompt section of any template changes, and the T5 digests for templates 01, 02, 05, 06 and 07 still match their prompt sections. Findings that need the author's judgment, a prompt change or a new run are not in this release.

- **`law-firm-ai-deployment-spec.md`.** The phase table's lead sentence read "The sixteen sections"; the spec has seventeen, 0 to 16, and now says so. Phases added to the Contents; one serial comma removed; "Day 90" capitalized in Section 14. The amendment line records the four changes.
- **`the-turtle-and-the-phoenix.md`.** Annex row "The walked-again rule" conformed to DOCTRINE.md section 1: the three Slow AI tests are conjunctive and "governed" is one of them, not a definition of the other two. Section 1 lists the closing exercise among the kit's contents. The handle map marks "keep more than one road to every place you must reach" as the practice cut's line. The title italicized in the Afterword.
- **`the-map-and-the-pair.md`.** "This piece stays with the fourth cell" now reads "that last cell": the two sibling pieces the same sentence links define the fourth cell as the unknown knowns, and the sentence means the unknown unknowns. The paraphrase of the computational-drafting instrument restores its "frequently". The Durability paragraph says the source note points to the record of what changed, as it has since v1.13.0. One serial comma removed.
- **`the-compression-and-the-harness.md`.** The re-verification line said "one sentence of section 2"; the sentence restated at v1.11.3 is in Section 6. OWASP spelled out on first use. One serial comma removed.
- **`sounds-good.md`.** NIST spelled out on first use. One serial comma removed.
- **`slow-ai-for-the-chief-legal-officer.md`.** The spec's title italicized, as in the same sentence's other title and in the README.
- **`tests.md`.** "How a case is run" states the extraction rule exactly: the lines strictly between the marker lines, less the blank line after `## PROMPT BEGINS`. The rule reproduces the seven T5 digests in `summary.json`. The known-defect lines read "None is fixed at v1.13.2" and "Not fixed at v1.13.2".
- **Examples.** The labels of the three failing outputs (templates 04, 05 and 06) showed the link text `../tests.md` for the target `../../tests.md`; the text now matches the target. Model output is untouched.
- **README.** LLM and RFP spelled out on first use. The grc-workbook neighbor line reads "every program template", since template 01 carries no framework constant.
- **Publications table.** Unchanged: each word count still rounds to its stated hundred.
- Every template masthead, the README masthead, How to Cite and the six publication citations, the `tests.md` masthead and `CITATION.cff` to v1.13.2 in lockstep. LICENSE.md is unchanged.

## [1.13.1] – 2026-10-19

Patch, from the weekly maintenance sweep of 19 October 2026 (KST) and Michael Paik's review of the T5 runs, completed 19 October 2026 (KST), on which he concurs with the scoring as recorded. No template content changes.

- **Logged run T5 reviewed.** `tests.md` Acceptance records the reviewer. Not accepted, as before: T04, T05 and T06 open.
- Every template masthead, the README masthead and How to Cite, the `tests.md` masthead and `CITATION.cff` to v1.13.1 in lockstep.

## [1.13.0] – 2026-10-18

Front door in two halves and template 08, session T7 of the whole-account review of 15 October 2026 (KST); review doc section 9 (change 4) and reviewer report 09 (items A3, A12, B1, B2, B3, B4, B5, B7, C7; B1 to B5 and B7 deferred here from T5).

- **README in two halves (items B1, B4).** Title `AI Governance Academy`; one paragraph stating the halves. Half 1, Client Content Prompt Pack: Purpose (now "seven" program options), the Known limitation paragraph unchanged, Contents with the row for template 08, a new Offerings ladder section carrying the ladder shared verbatim with the profile README (eight rows, 2 hours to 12 months, with the GRCnext™ line) and the sentence that the Slow AI Kitchen Workshop and The AI Generalist are not program options of the pack, then Workflow, Variable Conventions, Fixed Elements and Style Rules unchanged. Half 2, Publications: the 443-word paragraph replaced by a table (File, Title, Date, Kind, Words, Occasion; words by `wc -w` at this version, rounded to the nearest hundred) and a citation line per publication under "How to cite a publication". The slow-ai-kitchen neighbor line now says the Consultant Workbook engagement, One Workflow, Thirty Days, is template 08 of this pack and carries no published price. How to Cite, the Attribution line and `CITATION.cff` carry the title `AI Governance Academy: Client Content Prompt Pack and Publications`. Versioning states that publication releases move the minor version (item B2) and reads templates 01 to 08.
- **Template 08, `08-one-workflow-thirty-days.md` (new; doc section 9 change 4).** One Workflow, Thirty Days, in the form of template 03: Program Constants (30 days; price and headcount by proposal, no figure stated; the Consultant Workbook as delivery instrument with its records W01 to W24A, the thirty-day calendar and the Day 30 decision W23; the five periods of the Workbook's "Thirty-day delivery cadence" as the spine; frameworks, board-layer, acceptance-layer and principles as in 03); Output Modes A proposal, B engagement plan mapped to W01 to W24A, C sponsor report skeleton following the Workbook's "Sponsor report", D pre-work packet (W01 charter inputs, W02 selection with the benefit scale), E Day 30 recommendation and decision following W23 and W24; Acceptance Checklist of eight items, adding "every W-record cited exists in the Workbook". Every record the template cites was checked against the Workbook's headings. The spec for this session named "four weeks" as the spine; the Workbook's cadence has five periods and the template follows the Workbook.
- **Acceptance-layer reference (item A3).** Templates 03, 04 and 08 carry the Program Constants line "Acceptance-layer reference: The Definition of Done (https://github.com/rolldabones/definition-of-done)", so the README's framework constant is now stated by a template. The README sentence is unchanged.
- **Fable slot (item B5).** Template 03 Mode B: one line after Block 4 naming the fable and the facilitation kit's twenty-minute closing exercise as the slot. Template 04 Mode B: one sentence naming the Day 1 fable slot. These are changes to prompt sections; `tests.md` records that the T5 digests for 03 and 04 are of the v1.12.0 text and that template 08 has no logged run yet.
- **`law-firm-ai-deployment-spec.md` (item B3).** A Phases section after the Contents: Days 1 to 30, sections 0 to 5; Days 31 to 60, sections 6 to 12; Days 61 to 90, sections 13 to 16. Amendment line under the Version note: "Amended 18 October 2026 (KST): phase table added; no other text changed."
- **`the-map-and-the-pair.md` (item B7).** The 458-word "Second edition" paragraph in Source basis and attribution is now a two-sentence edition note pointing to this changelog's entries [1.11.0] and [1.11.1]. The masthead and every other line are unchanged. The paragraph is kept here so that no words are lost. Edition history moved from the-map-and-the-pair.md, 18 October 2026, verbatim:

> **Second edition.** The first edition was published earlier on 15 October 2026 (KST) as release v1.10.0 of this repository and was reviewed the same day. This edition answers the review. The three questions now stand before the vocabulary and the four positions answer only the first of them, so that novelty, provenance and assurance are recorded separately; the higher-ground and valley paragraphs and the undrawn mountain are reworded to match, and Section 6 no longer makes the undrawn mountain depend on who set the question. Section 4 states what the kernel and the Comparator each establish and quotes the Comparator's own condition, makes a different author the floor and a different kind of check the standard, distinguishes the kernel's run from the work of formalization and splits the fix into an evidence fix and an adjudication fix. Section 5 redefines the asterisk as a claim in the paper that the check did not reach, separates the ineffective content of the π theorem, which is not an asterisk, from the Flint Hills consequence, which is, and no longer equates a short challenge file with a short audit. Section 7 replaces the standard of reconstruction from the record, which would have made every proof a road, with a dated literature search of stated scope, states immediacy as the mark of a road, points to Section 2 rather than restating it and adds that the test is a floor under the word and not a definition. Section 9 adds a hypothetical and narrows the closing paragraph to what the evidence supports. Section 10 extends the porousness objection to the Comparator's condition, notes that the three questions are entangled in this release and records that the hypothetical is invented. The one-page table gains a row for the three questions and the two kinds of fix and rewords seven rows; questions 3 and 6 for discussion are reworded; GRCnext™ is bolded on its first appearance; the Durability paragraph records the edition. Four corrections of wording: a counterexample has a narrow verification target rather than the easiest verification; the verifier would have caught the sign error rather than prevented it; Swanson's road put a treatment to trial, and the trial is now cited by title and year; the formalized share is stated as 300 of 719 and called formalized throughout. Two proposals of the review were not taken up: the links into the account stay where the argument uses them rather than moving to the closing table, and the repeated contrast of roads and mountains is reduced rather than removed. The first edition remains readable at tag v1.10.0. Patch v1.11.1, the same day: the Swanson entry below records the author's confirmation of the two pages the session could not read; no other text changes.

- **Template headers.** Templates 01 to 08 read `Version 1.13.0 | 2026-10-18`, the pack version (ruling 8). No constant, Output Contract or Acceptance Checklist of templates 01, 02, 05, 06 or 07 changed.
- **`tests.md`.** Masthead at v1.13.0 for templates 01 to 08; one line that template 08 has no logged run yet and that the T5 digests for 03 and 04 are of their v1.12.0 prompt sections. No new run.
- **Findings by class (report 09, T7 items).** Confirmed and edited: A3, B1, B2, B3, B4 (ladder; headcount stated as by proposal, since no headcount constant exists and none is invented), B5, B7. Already fixed: none of the T7 items. Not reproducible: none. Outside the review: the Purpose paragraph's "six" program options became "seven" with template 08. Unknown: A12 (the `lnkd.in` short links in the-compression-and-the-harness.md and the-map-and-the-pair.md; the canonical URLs cannot be resolved from a session and the links stand). C7 ("DOCTRINE.md section 7.5" at the [1.11.0] entry below) is shipped changelog text and is not edited (ruling 7).
- Version line, How to Cite and `CITATION.cff` move to 1.13.0 in lockstep. LICENSE.md is unchanged.

## [1.12.0] – 2026-10-18

Pack made testable, session T5 of the whole-account review of 15 October 2026 (KST); review doc section 5 and reviewer report 09 (items B6, A10 and the third aggressive idea).

- **Fictional Client file (new, `examples/fictional-client.md`).** Labeled fictional on its first line. Part 1 is raw discovery material for template 01; Part 2 is a Client Profile Block prepared by hand from Part 1, so that templates 02 to 07 can be run without a prior run of 01. Report 09 item B6 had found no sample Client Profile Block and no sample Mode A anywhere in the pack.
- **`tests.md` (new).** Seven cases, one per template: template 01 on the raw material, templates 02 to 07 in Mode A on the Profile Block, each passing only when its own Acceptance Checklist is met item by item. Three known defects (the self-check against a checklist the prompt section does not carry; the Profile Block supplied in a turn rather than in the placeholder; the open v1.0.0 limitation). A fourth known defect found by the run (K4, below). The run record.
- **Logged run T5, 18 October 2026 (KST).** `claude-opus-5-5`, scored by `claude-sonnet-5-5`, API system prompt = the text between `## PROMPT BEGINS` and `## PROMPT ENDS`, no tools, max_tokens 16000: T01, T02, T03 and T07 PASS; T04, T05 and T06 FAIL (4 of 7). Each failing case met every Acceptance Checklist item but stated facts about the Client that the input does not contain (04: existing ISMS and QMS registers and ISO 9001 change control; 05 and 06: that the chatbot processes customer personal data under GDPR). Session review: concur, model behavior, on all three; no dissent, no case defect. Not accepted: open cases T04, T05 and T06; reviewer pending (Michael Paik). The seven outputs are filed in `examples/transcripts-2026-10-18-T5/`, each labeled with model, date and verdict, the three failing ones marked as failing and not to be copied; transcripts and `summary.json` are in `evidence/transcripts-2026-10-18-T5/`, copied byte for byte with a closing line appended. The template 01 output agrees in substance with the hand-prepared Profile Block on every field.
- **K4 (new known defect).** Templates 05 and 06 tell the model to attach every artifact to the Client's incumbent frameworks and to name the attachment point (05 Method 1; 06 Method 3; 03 Method 2 is similar), while the Profile Block carries only framework names; the instruction invites assertions about incumbent artifacts the input does not state. It contributed to the T05 and T06 failures. Not changed here: a change to a prompt section is a new block and needs a new run.
- **Verification line for the v1.0.0 Known Limitation (report 09 item A10).** Dated 18 October 2026 (KST), carried in the README under Purpose: the spines were checked against each template's Output Modes, Acceptance Checklist and the Contents table's durations and prices, and template 06's evidence collection starts by Week 8; they were not checked against any delivered program, because the repository holds no delivery record. The limitation stays open, and the README now says so beside "Status: final". The v1.0.0 entry below is unchanged (ruling 7).
- **README.** The Workflow section points to the fictional Client file and `tests.md`.
- **Template headers.** Templates 01 to 07 read `Version 1.12.0 | 2026-10-18`, the pack version (ruling 8). No template's prompt text, Output Contract, Acceptance Checklist or constant changed.
- **Findings by class (report 09, T5 items).** Confirmed and edited: B6, A10. Already fixed: A4 (headers lockstepped at v1.11.3). Deferred, with reasons: B1 to B5 and B7 (README in two halves, publications table, offerings ladder, fable slot, law-firm phase table) are session T7's front-door work; the v1.0.0 limitation itself needs Michael's comparison with delivered programs.
- Version line, How to Cite and `CITATION.cff` move to 1.12.0 in lockstep. LICENSE.md is unchanged.

## [1.11.3] – 2026-10-17

Doctrine short forms and the mechanical train, session T3 of the whole-account review of 15 October 2026 (KST); reviewer report 09 and review doc sections 1 and 8.

- **Template headers lockstepped (ruling 8 of 15 October 2026).** The header lines of templates 01 to 07 now read `Version 1.11.3 | 2026-10-17`, the pack version; they had read 1.0.0, 1.1.0 and 1.6.1. The README's Versioning section states the lockstep; no per-file version exception exists in this repository. Template titles and the README title lose their en dash ("Prompt Template 01: Shared Client Intake"; "AI Governance Academy: Client Content Prompt Pack"), because GitHub drops an en dash from a heading slug; How to Cite and `CITATION.cff` carry the new title.
- **Amendment note, template 06, 17 October 2026 (KST).** The twelve-week spine now starts evidence collection in W8 ("W8 vendor and supplier governance and the start of evidence collection") and W11 reads "incident response, change management and evidence review". The spine had placed evidence collection at W11, which contradicted the Week 12 definition (evidence collection running for at least four weeks) and Acceptance Checklist item 6 (no later than Week 8). Program names, durations, prices, output modes, the Client Profile Block schema and every Output Contract are unchanged.
- **House style in templates 01 to 07.** Fourteen serial commas removed (01, 02, 03, 04, 05, 06, 07); one list in 02 Mode D and one in 07 Mode E reworded so the list reads without it. The README's US$10,000/month reads US$10,000 per month, as template 07 does.
- **Doctrine compressions conformed to DOCTRINE.md v1.2.0 section 8.** `law-firm-ai-deployment-spec.md`: the Informed Intent and Slow AI paragraphs of the governing principles now carry the sentence forms (Informed Intent had omitted purpose; Slow AI had read "move deliberately" and five tests). `slow-ai-for-the-chief-legal-officer.md`: "visible, explainable and auditable" reads "governed, explained and audited". `the-compression-and-the-harness.md`: the sentence that had Slow AI slowing the horse "to the pace" now states the precondition. `the-turtle-and-the-phoenix.md`, handle map: the Informed Intent artifact names purpose, authority, boundaries and exit (it had read "purpose, scope, limits"), and the Slow AI row states the precondition instead of "velocity as a governed judgment"; the story's own line "who chooses the pace" is unchanged. The README's description of the law-firm spec names the three tests. The three dated source notes gain a line recording the re-verification against DOCTRINE.md v1.2.0; the original preparation records are unchanged.
- **Pointers and names.** `law-firm-ai-deployment-spec.md` and `slow-ai-for-the-chief-legal-officer.md` link the Primer's rendered index (`primer/README.md`) instead of the 1.7 MB single file, and name it as ECOSYSTEM.md does, the Enterprise AI Architecture Primer, on first mention and "the Primer" after (they had used "Practice Primer" and "Architecture Primer"). The law-firm spec's Kitchen reference reads "Step 8, Taste Before Service (Gate 6: Verification and Validation)"; it had called Taste Before Service Gate 6. The fable kit's section 5 now states the placements the programs wire (Executive Workshop closing block; Practitioner Academy Day 1); it had said the opening of the Executive Briefing and the Executive Workshop.
- **House style in the publications.** "catalogue" reads "catalog" in the author's prose of `the-map-and-the-pair.md` (twelve instances); the quotation from the openai/math README keeps its spelling. Two serial commas removed or reworded in the fable kit's handle map and one in the CLO primer; three instances of *Human* used as a common noun in the CLO primer lowercased under the DOCTRINE.md section 6 capitalization rule.
- **Neighbor pointer returned.** The README's Part of the ecosystem list names the-ai-generalist, which names this repository (ECOSYSTEM.md protocol item 9); the pointers from AI-Impact-Assessment-Tool and origami-method are not returned, for the five-neighbor cap, and ECOSYSTEM.md records why.
- **Closing line.** Added, last, to README.md, this changelog and templates 01 to 07; moved to the last line of the six publications, after the disclaimer, and in the fable after section 11.
- Version line, How to Cite and `CITATION.cff` move to 1.11.3 in lockstep. LICENSE.md is unchanged.

## [1.11.2] – 2026-10-15

Byline correction, on the author's instruction of 15 October 2026 (KST).

- **Masthead byline, six publications** (`law-firm-ai-deployment-spec.md`, `slow-ai-for-the-chief-legal-officer.md`, `sounds-good.md`, `the-compression-and-the-harness.md`, `the-map-and-the-pair.md`, `the-turtle-and-the-phoenix.md`), line 5: "Son-U Michael Paik · former General Counsel, BABL AI Inc. · CEO, GRC Solutions Korea" now reads "Son-U Michael Paik · CEO, GRC Solutions Korea". The account no longer carries the BABL AI role in byline or credit positions, so the ruling of 6 September 2026 that "BABL AI Inc." was a permitted expansion of the byline form is moot. Biography prose that names the former role is unchanged.
- **Recorded out of sequence.** The six edits were committed and pushed as `f80ac64` ahead of this entry and without a version move. This release carries that commit and brings the changelog, version line, How to Cite and `CITATION.cff` into lockstep at 1.11.2. Program templates 01 through 07, the body of every publication, LICENSE.md, program names, durations, prices, output modes, the Client Profile Block schema and every Output Contract are unchanged.

## [1.11.1] – 2026-10-15

Source note confirmation.

- **`the-map-and-the-pair.md`**: the Swanson entry in Source basis and attribution now records that the author clicked through to the PubMed listing of DiGiacomo, Kremer and Shah (PMID 2536517) and to Swanson's 1990 article at PMC on 15 October 2026 (KST), both of which had refused automated access from the session that prepared the second edition, and confirmed the journal, the year, that the trial's abstract reports a benefit and that the 1990 abstract describes the trial as supporting the hypothesis. The two hedges that rested on the pages being unread (journal and year from general knowledge; benefit resting on the sibling publication's reading and secondary accounts) are removed as discharged. One sentence in the Second edition paragraph records the patch. Sections 1 to 10, the table, the questions and every link are unchanged.
- Version line, How to Cite and `CITATION.cff` move to 1.11.1 in lockstep. Program templates 01 through 07, the five other client-facing publications, LICENSE.md, program names, durations, prices, output modes, the Client Profile Block schema and every Output Contract are unchanged.

## [1.11.0] – 2026-10-15

Second edition of *The Map and the Pair*, revised on the day of publication after a review of the first edition.

### Changed
- the-map-and-the-pair.md: three questions now stand before the vocabulary (what was already on the map, who set the question, what checked the answer and where the check stopped) and the four positions of Section 3 answer only the first, so that novelty, provenance and assurance are recorded separately; the undrawn mountain is defined by blank space alone and the one-line test is the conjunction of the three answers. Section 4 states what the Lean kernel and the Comparator each establish and what they leave to a human reader, quotes the Comparator README's own condition that definition-hole solutions "must always be checked with an additional (potentially human) verifier", distinguishes the kernel's minutes from the work of formalization and splits the fix into an evidence fix, available now, and an adjudication fix, which arrives later; the independence of the verifier is stated as the floor and a different kind of check as the standard. Section 5 separates the ineffective content of the π theorem, which is not an asterisk, from the paper's Flint Hills consequence, which the scope note places outside the selected statement and which is; the asterisk is redefined as a claim in the paper that the check did not reach, and a short challenge file is no longer equated with a short audit. Section 7 replaces the standard of reconstruction from the record, which would have made every proof a road, with a dated literature search of stated scope, with Thomas Bloom's list as the working example, and adds that the test is a floor under the word superintelligence and not a definition. Section 9 adds a hypothetical contract review that runs the four practices in one file and narrows the closing paragraph to what the evidence supports: the releases do not settle the question of superintelligence in either direction. Section 10 extends the porousness objection to the Comparator's condition, notes that the three questions are entangled in this release and records that the hypothetical is invented. The one-page table gains a row for the three questions and the two kinds of fix and rewords seven existing rows; questions 3 and 6 for discussion are reworded to match; Section 7's statement of the objection now points to Section 2 rather than restating it; GRCnext™ is bolded on its first appearance; the Durability paragraph records the edition.
- Four corrections of wording in the same file: a counterexample has a narrow verification target rather than the easiest verification, the Eilenberg–Ganea construction being the counter-case; the verifier would have caught the sign error rather than prevented it, which corrects the author's own posted line; Swanson's road put a treatment to trial rather than saved a life, with the 1989 trial now cited by title from its PubMed listing and the 1990 abstract recorded as not re-read because the PubMed and PMC pages refused automated access on 15 October 2026 (KST); and the formalized share is stated as 300 of 719 top-line results, in the history file's own words, and called formalized rather than checked throughout.
- Source note updated: prepared against ECOSYSTEM.md v1.7.26 and the sibling publications as at v1.10.0; the Comparator README and the openai/math README, history file and scope notes for families 017 and 088 re-read at main on 15 October 2026 (KST) for the sentences quoted; a Second edition paragraph records the changes above and the two proposals of the review that were not taken up (moving the links into the account to the closing table, and removing rather than reducing the repeated contrast of roads and mountains). No link into the account is added or changed; the first edition remains readable at tag v1.10.0.
- README Contents note entry for the piece updated to name the three questions and the second edition. Version line, How to Cite and `CITATION.cff` move to 1.11.0 in lockstep. Program templates 01 through 07, sounds-good.md, the-turtle-and-the-phoenix.md, law-firm-ai-deployment-spec.md, slow-ai-for-the-chief-legal-officer.md, the-compression-and-the-harness.md, LICENSE.md, program names, durations, prices, output modes, the Client Profile Block schema and every Output Contract are unchanged.

## [1.10.0] – 2026-10-15

### Added
- the-map-and-the-pair.md, the client-facing publication *The Map and the Pair*: a discussion piece in ten sections with a one-page vocabulary table and ten questions for a governance room. Sections 1 to 3 state the question (whether a model has reached something unknown to everyone), define the map as the record and place every checked result in one of four positions: a road, higher ground on a known hill, a valley or an undrawn mountain. Sections 4 and 5 read discovery as the work of a pair, proposer and verifier, set out what a proof assistant checks and what it leaves to a human reader, name the asterisk as the boundary of a partial check and introduce three navigation terms, dead reckoning, the fix and distance to fix. Section 6 treats problem provenance as evidence and lists six disclosures a laboratory should make. Section 7 states the author's objection that no result is unrelated to the record and draws the consequence that the first clause of the test is a direction while the second and third are operable. Section 8 places Base Camp at the confirmation moment of the Final Liability lifecycle. Section 9 carries the argument to professional work, where the verifier is a court. Section 10 states the objections to the piece's own argument.
- The piece adds no doctrine, step, gate, tier or form. The doctrines are used as stated in DOCTRINE.md v1.1.1: Final Liability with the allocation lifecycle, and *the Human* capitalized only as the defined term, at Base Camp. The vocabulary and the one-line test are the author's, first posted on LinkedIn on 14 October 2026 and credited with the post's link. A closing table maps each section to the instrument in the account that already carries it.
- The occasion was OpenAI's openai/math repository (initial commit 6 October 2026, UTC), read directly at the initial commit and at main: the README, history.md, the scope notes for families 017, 088 and 249, the formalization catalogue and the Comparator challenge files, with commit timestamps read from the GitHub API. The manuscripts themselves were not read and the piece takes no position on the mathematics. The Erdős problems episode of October 2025 and OpenAI's ten results of 1 August 2026 are read through dated press reports and one arXiv preprint, each named in the source note with what was read and what was not.
- Prepared against DOCTRINE.md v1.1.1, ECOSYSTEM.md v1.7.25, Slow AI Kitchen v2.11.1 at commit `05253ac`, computational-drafting v1.4.0 at commit `9b3c12a` and The Definition of Done v1.2.2 at commit `4bdc2cd`. On 15 October 2026 (KST) every link into the account was resolved, anchor included, against clones of the linked repositories. The publication is not a program template and no Output Contract applies to it.

### Changed
- README Contents note now records six client-facing publications rather than five. Version line, How to Cite and `CITATION.cff` move to 1.10.0 in lockstep. Program templates 01 through 07, sounds-good.md, the-turtle-and-the-phoenix.md, law-firm-ai-deployment-spec.md, slow-ai-for-the-chief-legal-officer.md, the-compression-and-the-harness.md, LICENSE.md, program names, durations, prices, output modes, the Client Profile Block schema and every Output Contract are unchanged.

## [1.9.0] – 2026-10-12

### Added
- the-compression-and-the-harness.md, the client-facing publication *The Compression and the Harness*: a discussion piece in nine sections with ten questions for a governance room. Sections 1 to 3 read a language model as a lossy, frequency-weighted compression of the record, index the four cells of known and unknown by knower (the reader, the record and the model) and argue that discovery beyond the record belongs to a model paired with a check that someone wrote, with a paragraph on deterministic tools in everyday harnesses. Sections 4 to 6 read the software around a model as a harness, which transmits power before it restrains, and set out five places where the horse-and-carriage picture breaks. Section 7 applies the eight elements of computational drafting to the everyday act of instructing a model. Section 8 states the objections to the piece's own argument. Section 9 places the destination and the confirmation with the driver.
- The piece adds no doctrine, step, gate, tier or form. The doctrines are used as stated in DOCTRINE.md v1.1.1: Informed Intent with its four elements, Slow AI with its three tests and Final Liability with the allocation lifecycle. *The Human* is capitalized only as the defined term, read with The Definition of Done as the person who defines and confirms. A closing table maps each section to the instrument in the account that already carries it.
- The occasion was Stephen Wolfram's interview with Jon Hernandez, "The future with AI will be very different from what we're being sold", credited with its link in a note recording that the piece paraphrases and does not quote, that the paraphrases were checked against the auto-generated captions on 12 October 2026 (KST) and that neither has any involvement in or endorses the piece.
- Two legal references carry status tags under DOCTRINE.md section 7.5. Articles 14(4)(b) and 26(2) of Regulation (EU) 2024/1689 are cited as in force and not yet applicable, with the application date read in Regulation (EU) 2026/1744 on the Official Journal page. *Collier v. Zambito*, 1 N.Y.3d 444 (2004), and *Flanders v. Goodfellow*, 44 N.Y.3d 57 (2025), are cited from the New York Court of Appeals official reporter pages as an analogy only and not as authority on AI.
- Prepared against Slow AI Kitchen v2.11.1 at commit `05253ac` and computational-drafting v1.4.0 at commit `9b3c12a`. On 12 October 2026 (KST) every link into the account was resolved, anchor included, against clones of the linked repositories. The document's source note records, source by source, what was read directly and what was not. The publication is not a program template and no Output Contract applies to it.

### Changed
- README Contents note now records five client-facing publications rather than four. Version line, How to Cite and `CITATION.cff` move to 1.9.0 in lockstep. Program templates 01 through 07, sounds-good.md, the-turtle-and-the-phoenix.md, law-firm-ai-deployment-spec.md, slow-ai-for-the-chief-legal-officer.md, LICENSE.md, program names, durations, prices, output modes, the Client Profile Block schema and every Output Contract are unchanged.

## [1.8.0] – 2026-10-06

### Added
- slow-ai-for-the-chief-legal-officer.md, the client-facing publication *Slow AI for the Chief Legal Officer*: a practical primer for the Chief Legal Officer or General Counsel who has to make AI accountable without owning it, in fifteen sections. It is set in the author's own frame. Section 1 states the partner-guardian tension, after Ben W. Heineman Jr., and resolves it for AI: the Chief Legal Officer architects accountability and does not own AI or run the approval desk. Section 2 lays out the risk landscape as four cells, after Donald Rumsfeld's remark of 12 February 2002 and the fourth cell he did not name, with the author's answer to each for the in-house lawyer and for AI: Systems for the known knowns, Communications for the unknown knowns, training for the lawyers and education for the internal Clients, with tests, for the known unknowns, and slack with the Pareto rule for the unknown unknowns. The remaining sections are grouped under those four cells and close on a 90-day plan with dated outputs and the Slow AI test. Both influences are acknowledged and neither is doctrine; this is their first appearance in the account.
- The framework throughout is the author's own: the three doctrines, the Slow AI Kitchen as the method and GRCnext™ for the exit. The Kitchen is unchanged by the primer, and a closing table maps the primer's sections to the Kitchen's steps and gates. Proportionate friction is stated as the Kitchen's three tiers, in the README's own terms, with the Step 10 prohibited list beside them. Sections 1 to 13 each end on one record to ask to see and point to the instrument that already holds it: the Consultant Workbook's records, the service ticket and receipt of Take-Out, Delivery & Vending Machines, the Step 10 registry and the Step 11 role assignment matrix. Section 10 treats an approval as attaching to a configuration, sets out what model, agent and architecture changes each do to an authorization, restates the nine re-tiering triggers of the Enterprise AI Architecture Primer and places the contract against the running configuration and the regulatory role on the Chief Legal Officer's own desk. The primer names no model, vendor or agent framework and introduces no new form.
- The doctrines are used as stated in DOCTRINE.md v1.1.1: Informed Intent carries its four elements and the authorizer's five conditions; Final Liability carries the three attributes, the allocation lifecycle and the drafting rule of section 3.2, applied to vendor contracts; *the Human* is capitalized only as the defined term.
- The occasion was the I by IMD article "AI and the Chief Legal Officer: Redefining legal leadership" by Esteban Mezzano, Konstantinos Trantopoulos and Michael R. Wade (5 October 2026), credited with its canonical link in a note recording that it is a starting point only, that the primer does not follow its structure or adopt its priorities, data or regulatory summary and that its authors and IMD have no involvement and do not endorse it. The article was read in full in a browser on 6 October 2026 (KST) and none of its text is reproduced.
- Prepared against Slow AI Kitchen v2.9.2 at commit `c2f8ccd`. On 6 October 2026 (KST) every link into that repository was resolved, anchor included, against that commit, and every link to another repository in this account returned HTTP 200. Heineman's two books and his own summary of the second were checked the same day. The briefing is cited by date and not linked, because the Department of Defense archive refuses automated access and the link could not be confirmed as live. The publication is not a program template and no Output Contract applies to it.

### Changed
- README Contents note now records four client-facing publications rather than three. Version line, How to Cite and `CITATION.cff` move to 1.8.0 in lockstep. Program templates 01 through 07, sounds-good.md, the-turtle-and-the-phoenix.md, law-firm-ai-deployment-spec.md, LICENSE.md, program names, durations, prices, output modes, the Client Profile Block schema and every Output Contract are unchanged.

## [1.7.4] – 2026-09-30

Link correction.

- **`law-firm-ai-deployment-spec.md`**: the guided implementation of the twelve steps is repointed from `slow-ai-kitchen.msagent.ai` to https://kitchen.grcskorea.com/, where the Slow AI Kitchen application now runs.
- Version line, How to Cite and `CITATION.cff` move to 1.7.4 in lockstep. Program templates, publications' substance, LICENSE.md and every Output Contract are unchanged.

## [1.7.3] – 2026-09-13

Two corrections of substance: changelog history restored and program template version lines corrected.

- **Changelog history restored.** ~~The entries for v1.0.0, v1.1.0 and v1.2.0, and the closing text of the v1.3.0 entry, are absent from this file.~~ **STRUCK 13 September 2026.** They were deleted when v1.7.0 shipped on 22 August 2026: the file shrank from 11,507 bytes at v1.6.1 to 9,549 at v1.7.0, in a release that added an entry, and terminated mid-word at "pla" inside the v1.3.0 Added section. All four are restored byte for byte from the v1.6.1 tag archive, which is what shipped under that tag, and no replacement text was composed. Restored: the v1.0.0 creation record of all seven templates together with its Known Limitations section; the v1.1.0 entry recording that program templates 02 through 07 each gained a Board-layer reference line in Program Constants; the v1.2.0 entry adding The Definition of Done as a fixed framework constant; and the remainder of the v1.3.0 entry. Entries v1.3.1 through v1.6.1 were compared byte for byte against the same archive and are unchanged, so v1.7.0 touched only the tail.
- **Program template version lines corrected.** Line 3 of each template carries the pack version, in the form the README carries it and the form the deleted `00-README.md` carried at v1.0.0. Six templates still read `Version 1.0.0 | 2026-07-04` after their substance had changed. ~~02, 03, 04, 05, 06 and 07 at `Version 1.0.0 | 2026-07-04`~~ **STRUCK 13 September 2026.** `02-executive-briefing.md`, `05-implementation-accelerator.md`, `06-guided-ai-grc-build.md` and `07-fractional-advisor.md` now read `Version 1.1.0 | 2026-07-08`, the release in which each gained its Board-layer reference line. `03-executive-workshop.md` and `04-practitioner-academy.md` now read `Version 1.6.1 | 2026-08-13`, the release in which each gained its teaching fable line. Each line records the release in which that file's substance last changed rather than the release carrying this correction. `01-client-intake.md` is unchanged and remains correct at `Version 1.0.0 | 2026-07-04`: its bytes have not moved since creation.
- Version line, How to Cite and `CITATION.cff` move to 1.7.3 in lockstep. Program template body text, the three client-facing publications, LICENSE.md, program names, durations, prices, output modes, the Client Profile Block schema and every Output Contract are unchanged.

## [1.7.2] – 2026-09-06

Cross-link only. The slow-ai-kitchen nearest-neighbor line now names the Consultant Workbook published in that repository at v2.8.0, the delivery instrument for a 30-day initial engagement on one priority workflow, and records that the engagement is not a program option of this pack and carries no price constant here. Version line, How to Cite and `CITATION.cff` move to 1.7.2 in lockstep. Program templates 01 through 07, the three client-facing publications, LICENSE.md, program names, durations, prices, output modes, the Client Profile Block schema and every Output Contract are unchanged.

## [1.7.1] – 2026-09-06

Citation infrastructure, doctrine citation line and lockstep maintenance. Session C of the September 2026 improvement pack, one patch release per repository across all 21 public repositories.

- **`CITATION.cff` added** in the house form settled at D-C1: no `type` field, `version` and `date-released` in lockstep with the README, `license` as the SPDX identifier for this repository's licence, `abstract` taken from this repository's ECOSYSTEM.md role line rather than newly written.
- **How to Cite block** aligned to this release and pointing at `CITATION.cff`.
- All other files in this repository are unchanged byte for byte.

## [1.7.0] – 2026-08-22

### Added
- law-firm-ai-deployment-spec.md, the client-facing publication *Law Firm AI Deployment Spec v2*: a 90-day specification for building a governed, useful and auditable AI capability in a law firm, from the economic incentive to participate through a bounded production workflow to a Day 90 Definition of Done. The Slow AI Kitchen is the method beneath it, with the build mapped to the Feast and every deployed workflow to Steps 1 through 9, and the Practice Primer is the architecture reference for the architect or Chief AI Officer. Version lineage is stated in the document: Version 1 is Seth Fenster's (Founder & CEO, Litvue) LinkedIn post of August 2026, credited with its canonical link; Version 2 is an independent answer to the same brief, built on the frameworks maintained across this account. Every external link in the publication was verified live on 22 August 2026 (KST) before commit. It is not a program template and no Output Contract applies to it.

### Changed
- README Contents note now records three client-facing publications rather than two. Version and date line updated in lockstep. Program templates 01 through 07, sounds-good.md, the-turtle-and-the-phoenix.md, LICENSE.md, program names, durations, prices, output modes, the Client Profile Block schema and every Output Contract are unchanged.

## [1.6.1] – 2026-08-13

Academy pass: fable wiring and status field decided.

- **Fable wired into the programs.** `03-executive-workshop.md` Program Constants gain a line placing *The Turtle and the Phoenix* in the closing block as the retention device for the three principles. `04-practitioner-academy.md` gains the corresponding line placing it on Day 1, seating the doctrine before the instruments arrive on Day 2.
- **Reciprocal line in the kit.** `the-turtle-and-the-phoenix.md` now states where it is used in the programs and directs facilitators of either program to the Practitioner Cut rather than only the Practice Cut. The Handle Map is named as the bridge from story to workbook modules.
- **Status field decided: draft to final.** The pack carries six complete program specifications with fixed pricing, durations and constants marked do not alter, plus a facilitation kit. The draft label understated it and was inconsistent with the rest of the account.


License metadata sweep. An `SPDX-License-Identifier: CC-BY-NC-SA-4.0` line and the canonical Creative Commons legal code are now carried inside the existing license file. The filename is unchanged and the human-readable summary is retained above the legal code.

- The primary audience is automated intake and provenance tooling, which reads the SPDX tag rather than prose. Automated license detection previously reported nothing across all twenty-one repositories in this account.
- No change to the licence in force. The identifier records what was already true.

## [1.6.0] – 2026-07-30

### Added
- Section 8, The Closing Exercise, in the-turtle-and-the-phoenix.md. Twenty minutes, three required artifacts (one name written, one door listed, one errand scoped) and an acceptance test read aloud before the room leaves. The kit previously promised in its facilitation notes that every telling would end in at least one instrument and gave the facilitator no mechanism to make that happen; the exercise is that mechanism, and it applies the same acceptance rule the story argues for.
- Fourth column on the handle map, naming the artifact each row produces, so a row can be assigned rather than only discussed. One row of thirteen is marked Principle, meaning it changes how people think rather than what they file.
- One paragraph in the practitioner cut, in the scene of the reckless and the fearful, where the turtle's own caution once cost a neighbor her stores. The practice cut, the miniature and the published essay are unchanged, so the canon text stands as published.

### Changed
- Sections renumbered from the insertion of section 8: Facilitation Notes to 9, Afterword to 10, Annex to 11, with the Contents list and both internal cross-references updated. Facilitation note 3 now points at the exercise instead of stating an outcome the kit could not enforce. Version and date line in README updated in lockstep. The story arc, the miniature, the module timings, the discussion prompts, the annex, the afterword, program templates 01 through 07, sounds-good.md, LICENSE.md, program names, durations, prices, output modes, the Client Profile Block schema and every Output Contract are unchanged.

## [1.5.1] – 2026-07-30

### Added
- Link from the-turtle-and-the-phoenix.md and from the README Contents note to the published essay at https://redcaps.substack.com/p/the-turtle-and-the-phoenix, the general-audience telling of the story this kit is built on. The canonical Substack URL is used rather than a share link, so no tracking parameters enter the repository.

### Changed
- Version and date line in README updated in lockstep. No change to the story text in either telling, the miniature, the module timings, the handle map, the discussion prompts, the facilitation notes, the afterword, the annex, program templates 01 through 07, sounds-good.md, LICENSE.md, program names, durations, prices, output modes, the Client Profile Block schema or any Output Contract.

## [1.5.0] – 2026-07-30

### Added
- Ten workshop paragraphs in the practitioner cut of the-turtle-and-the-phoenix.md, nested inside the scene of those who listened, after the customs paragraph and before the failure scenes. The shelf and the choosing, the packing order, the noon page, the sparrows, the one bore of horn, the rehearsal meadow, the gate and the manifest, the flight book, the gray mornings and the walked-again rule. The story arc, the failure scenes, the kings and the classroom are unchanged.

### Changed
- Section 1 framing, the section 3 register note, facilitation note 2 and the annex preamble updated for the added material. The practitioner cut now reads at about twenty minutes aloud rather than thirteen, and the closing annex now names build disciplines for customs the reader has already met. Version and date line in README updated in lockstep. The practice cut in section 2, the miniature, the module timings, the thirteen-row handle map, the eight discussion prompts, the afterword, program templates 01 through 07, sounds-good.md, LICENSE.md, program names, durations, prices, output modes, the Client Profile Block schema and every Output Contract are unchanged.

## [1.4.1] – 2026-07-30

### Fixed
- Commit-date placeholders resolved. The publication byline, the README version line, the README Contents note entry for the publication and the v1.4.0 changelog heading each carried an unfilled placeholder token when v1.4.0 was tagged. All four now read 30 July 2026, in the date format each location uses. The v1.4.0 tag archive retains the placeholder version as the record of what shipped under that tag.

### Changed
- Version and date line in README updated in lockstep. No change to the publication text, the handle map, the discussion prompts, the annex, program templates 01 through 07, sounds-good.md, LICENSE.md, program names, durations, prices, output modes, the Client Profile Block schema or any Output Contract.

## [1.4.0] – 2026-07-30

### Added
- the-turtle-and-the-phoenix.md, the client-facing publication *The Turtle and the Phoenix*: a teaching fable on human capability in the age of AI, with the facilitation kit for using it in governance rooms. The kit carries two tellings, the practice cut for telling aloud and the practitioner cut for circulation, plus the one-minute miniature, module timings, a thirteen-row handle map, eight discussion prompts, facilitation notes and the afterword. It is not a program template and no Output Contract applies to it.
- Closing annex in the same publication for readers who design and build the arrangements, mapping seventeen story elements to build disciplines with six prompts for a build review. Vocabulary is limited to publicly documented concepts and the author's own doctrines.

### Changed
- README Contents note now records two client-facing publications rather than one. Version and date line updated in lockstep. Program templates 01 through 07, sounds-good.md, LICENSE.md, program names, durations, prices, output modes, the Client Profile Block schema and every Output Contract are unchanged.

## [1.3.1] – 2026-07-30

### Added
- LICENSE.md, formalizing the CC BY-NC-SA 4.0 terms already stated in the README License section. The terms are mirrored, not changed: attribution to Son-U Michael Paik, non-commercial use, ShareAlike on derivatives and prior written permission for commercial use. Filename follows the account majority convention (LICENSE.md, fourteen repositories, against LICENSE in five).

### Changed
- Version and date line in README updated in lockstep. Program templates 01 through 07, sounds-good.md, program names, durations, prices, output modes, the Client Profile Block schema and every Output Contract are unchanged.

## [1.3.0] – 2026-07-15

### Added
- Part of the ecosystem section in the README linking the canonical ECOSYSTEM.md in the profile repository plus the four framework constants as nearest neighbors (grc-workbook, slow-ai-kitchen, ai-governance-for-boards, definition-of-done), placed before License.
- README Contents note documenting sounds-good.md, the client-facing publication *Sounds Good* (9 July 2026). Retroactive record: the file entered the repository around its publication date without a changelog entry, a lockstep breach corrected as of this release; no Output Contract applies to it.

### Changed
- Version and date line in README updated. Program templates 01 through 07 are unchanged. No change to program names, durations, prices, output modes, the Client Profile Block schema or any Output Contract.

## [1.2.0] – 2026-07-10

### Added
- The Definition of Done Is the Work of the Human (https://github.com/rolldabones/definition-of-done) added as a fixed framework constant. The README Fixed Elements now name it as the acceptance-layer doctrine alongside the GRC Workbook, Slow AI Kitchen and AI Governance for Boards. Generated Client documents that cite frameworks may cite it where the engagement covers task-level acceptance discipline, in particular the Practitioner Academy and the Executive Workshop.

### Changed
- Version and date line in README updated. Program templates 02 through 07 are unchanged. No change to program names, durations, prices, output modes, the Client Profile Block schema or any Output Contract.

## [1.1.0] – 2026-07-08

### Added
- AI Governance for Boards (https://github.com/rolldabones/ai-governance-for-boards) added as a fixed framework constant. The README Fixed Elements now name it as the board-layer handbook alongside the GRC Workbook and Slow AI Kitchen, and every program template (02 through 07) carries a Board-layer reference line in its Program Constants. Generated Client documents that cite frameworks may now cite the handbook where the audience includes directors.

### Changed
- Version and date line in README updated. No change to program names, durations, prices, output modes, the Client Profile Block schema or any Output Contract.

## [1.0.0] – 2026-07-04

### Added
- 00-README.md: pack overview, workflow, variable conventions, fixed elements, inherited style rules, license (CC BY-NC-SA 4.0), versioning policy.
- 01-client-intake.md: shared intake template producing the Client Profile Block v1.0 (18 fields, halt condition at greater than 50 percent Unknown).
- 02-executive-briefing.md: 4 output modes (Proposal, Agenda, Talking Points, Follow-Up).
- 03-executive-workshop.md: 5 output modes including Decision Log Template and Pre-Work Packet; four-block day structure.
- 04-practitioner-academy.md: 5 output modes including Curriculum and Exercise Pack and Participant Workbook; eight-session two-day spine.
- 05-implementation-accelerator.md: 4 output modes including Artifact Starter Set and Executive Readout Template; five-day AIMS build spine.
- 06-guided-ai-grc-build.md: 5 output modes including Twelve-Week Syllabus with gate questions and Evidence Tracker; immutable minimum viable AIMS definition (six elements).
- 07-fractional-advisor.md: 5 output modes including Annual Advisory Plan and Renewal and Handover; explicit out-of-scope list.

### Known Limitations
- Program spines (workshop blocks, session counts, weekly sequence) are structural inferences pending verification against actual delivery design.
- Renewal and exit terms in template 07 are placeholders for external counsel.

---

**Final Liability rests with the Human.**
