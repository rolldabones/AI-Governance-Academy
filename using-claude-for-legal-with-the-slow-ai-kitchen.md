# Using Claude for Legal with The Slow AI Kitchen

**A first-time guide for enterprise legal teams**

Son-U Michael Paik · CEO, GRC Solutions Korea

1 November 2026

*GRC Solutions Korea is not affiliated with Anthropic, and Anthropic has not reviewed or endorsed this guide. Claude and Claude for Legal are Anthropic's product names, used here to refer to the product.*

> Anthropic has given lawyers a kitchen. It has not given them a chef.
>
> LinkedIn, 1 November 2026

**Starting point.** On 1 November 2026 (Korea Standard Time, KST) I published a LinkedIn post that opens with the line above, with nine comments beneath it: Anthropic's own sources, a setup guide and seven worked examples ([post](https://www.linkedin.com/feed/update/urn:li:activity:7522632632627716096/)). The post ran Claude for Legal, Anthropic's offering for in-house legal teams and law firms, through the twelve steps of the Slow AI Kitchen. This guide is the thread rewritten for a reader who is meeting Claude for Legal for the first time, and perhaps Claude for the first time. It runs from the decision to buy to the first quarterly review. Every command, label and field named here was checked against Anthropic's published source or against the product as it stood in my own Claude account that day, and Section 25 says which. The method's vocabulary is explained as it arrives, the seven examples are written out as recipes with their tests, and the guide keeps the one thing the thread could not hold: a table of what the product does at each of the method's gates, what it does not do and what the lawyer adds.

**For:** the General Counsel or deputy deciding whether and how to adopt Claude for Legal; the lawyer or legal operations lead who will set it up; the person who will own it afterward; and any colleague who wants to understand what the product is before using it. No prior knowledge of Claude is assumed. The doctrine behind the method is [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md). The method is the [Slow AI Kitchen](https://github.com/rolldabones/slow-ai-kitchen) and the recipe form is its [Cookbook](https://github.com/rolldabones/slow-ai-kitchen/blob/main/slow-ai-cookbook.md). This guide adds five recipes, two Feast records and one table. It adds no doctrine, step, gate, tier or form.

**One vendor, worked.** The method is vendor-neutral by design, and the Cookbook's recipes name capabilities, not models, because the model is interchangeable and the discipline is not. This guide breaks that habit once, on purpose. It takes one vendor's product and works it, as the demonstration that the method survives contact with a real product. Section 21 shows how to run the same table against any other product, and the Cookbook's rule stands for every recipe that is not this experiment.

**Edition and durability.** First edition, 1 November 2026 (KST). The product facts are a snapshot of that date. Anthropic's announcement of 28 October names six gallery artifacts; four days later the gallery's Anthropic section listed more than fifteen, so the product moves faster than any guide. Section 25 lists every product and legal fact relied on, with its source and the date it was read. A second edition is owed when the weekly external link check of the rolldabones account reports a cited page dead, or when a reader reports that a named command, label or page has changed. Until then the text stands as written and the register shows what has moved. If a screen you see differs from a screen described here, the screen wins; tell me.

**A declared interest.** This guide was prepared with Claude, a model made by Anthropic, and it concerns Anthropic's product. The product was read in the author's own paid Claude account; Anthropic had no part in the guide. Readers should hold the vendor's claims and mine to the same test: Section 21 names the evidence behind each row and Section 24 says where this guide is most likely to be wrong.

## Contents

Part I. Before you start

1. [How to use this guide](#1-how-to-use-this-guide)
2. [Words you will meet](#2-words-you-will-meet)
3. [If this is your first day with Claude](#3-if-this-is-your-first-day-with-claude)
4. [What Claude for Legal is, and what Anthropic says it is not](#4-what-claude-for-legal-is-and-what-anthropic-says-it-is-not)
5. [The Slow AI Kitchen on one page](#5-the-slow-ai-kitchen-on-one-page)

Part II. Plan the Menu: decisions before the first dish

6. [Choose the plan and the terms](#6-choose-the-plan-and-the-terms)
7. [Privilege and confidentiality, in plain words](#7-privilege-and-confidentiality-in-plain-words)
8. [Write the registry entry](#8-write-the-registry-entry)

Part III. Mise en Place: set up in one sitting

9. [Install the plugin](#9-install-the-plugin)
10. [Run the cold-start interview](#10-run-the-cold-start-interview)
11. [Read the practice profile, field by field](#11-read-the-practice-profile-field-by-field)
12. [Connect a research tool](#12-connect-a-research-tool)
13. [Open the artifact gallery](#13-open-the-artifact-gallery)

Part IV. Cook: five recipes

14. [The recipe card](#14-the-recipe-card)
15. [Recipe 1: NDA triage](#15-recipe-1-nda-triage)
16. [Recipe 2: a vendor MSA against the playbook](#16-recipe-2-a-vendor-msa-against-the-playbook)
17. [Recipe 3: cite check before filing](#17-recipe-3-cite-check-before-filing)
18. [Recipe 4: regulatory horizon scan](#18-recipe-4-regulatory-horizon-scan)
19. [Recipe 5: Ask legal, the front door](#19-recipe-5-ask-legal-the-front-door)

Part V. Run the Feast

20. [Staff the brigade and keep the evidence](#20-staff-the-brigade-and-keep-the-evidence)
21. [What the product does for you, and what it does not](#21-what-the-product-does-for-you-and-what-it-does-not)
22. [The rules that apply, dated](#22-the-rules-that-apply-dated)

Part VI. Next steps

23. [Next steps: the first day, week, month and quarter](#23-next-steps-the-first-day-week-month-and-quarter)
24. [Where this guide is weakest](#24-where-this-guide-is-weakest)
25. [Currency register](#25-currency-register)

- [Questions for discussion](#questions-for-discussion)
- [This guide and the account](#this-guide-and-the-account)
- [Source basis and attribution](#source-basis-and-attribution)

## 1. How to use this guide

The guide has six parts. Part I explains the words and the two things being combined: Anthropic's product and the Slow AI Kitchen method. Part II covers the decisions a legal function makes before anyone opens the product: the plan, the terms, privilege and the registry entry that records what may run. Part III is one sitting of setup. Part IV works five tasks a legal team does every week, each as a recipe you can follow. Part V covers the people, the evidence, the gap table and the rules. Part VI tells you what to do on the first day and in the first quarter, and what this guide cannot tell you.

Three reading paths. A General Counsel with twenty minutes reads Sections 4, 6, 7, 8 and 23. The person doing the setup reads Sections 9 to 13 with the product open, then Section 15. The person who will own the deployment reads everything, and Section 21 twice.

The guide is complete in a defined sense. It runs one plugin (commercial-legal) and five of the ready-made legal artifacts from the decision to buy to the first quarterly review, and it names the other eleven plugins without working them. A team that has done everything in it will have a working first workflow, a registry entry, a role matrix and an evidence trail. It will not have covered its litigation, privacy or corporate practice; the same recipe form applies there, and the gap table in Section 21 is how to check any further plugin or artifact before relying on it.

Two conventions. Where the guide describes a screen or a label, it was seen in the product on 1 November 2026 and is written as seen; where it describes a behavior that Anthropic documents but I did not run, it says so. The method's units, steps, gates and tiers, are written as the Kitchen writes them: capitalized when numbered (Step 2, Gate 1, Tier 3) and lowercase otherwise; the role names (Owner, Reviewer, Approver, Builder, Preparer) are capitalized. The product's own built-in checks are also called gates, in the vendor's word; when this guide means the method's, it says the Kitchen's gates. All of these are explained in Section 5 before they are used.

## 2. Words you will meet

| Word | What it means here |
|---|---|
| Claude | Anthropic's AI assistant, used through a web app, desktop apps for Mac and Windows, mobile apps and an add-in for Microsoft 365. |
| Model | The underlying AI system that reads your prompt and writes the answer. Claude is a family of models; the product chooses one for you unless you choose. |
| Plan | What your organization has bought. Free, Pro, Max and Ultra are individual plans; Team and Enterprise are sold to organizations. Section 6 says why Client work runs only on the organizational plans or the API. |
| API | The application programming interface, the way a company's own software talks to Claude without the apps. Used here only as one of the places sensitive matters may run. |
| Claude desktop app | The Mac or Windows application. Its Cowork tab is where plugins are installed and where longer, multi-step work runs. |
| Claude Code | Anthropic's tool for developers, run from a terminal. Lawyers will rarely use it; this guide gives the Cowork path first and the Claude Code path second. |
| Plugin | A bundle of skills, agents and settings for one practice area, installed into Claude. Claude for Legal is twelve of them. |
| Skill | A set of written instructions, in a plain-text file, that tells Claude how to do one task, such as triaging an NDA. A plugin bundles its skills. |
| Slash command | A command typed into Claude's message box beginning with a slash, such as `/commercial-legal:review`. It runs the skill of that name. |
| Agent | A set of instructions, separate from the skills, that runs without being asked, on a timetable or when data changes, such as a Monday sweep of recently signed agreements, and posts or files what it finds. |
| Cold-start interview | The plugin's first-run interview, ten to twenty minutes by the repository's count, in which it asks how your team works and writes your answers into the practice profile. |
| Practice profile | A plain-English document, saved as a file named `CLAUDE.md`, that records your playbook positions, escalation rules and house style. Every skill in the plugin reads it before working. |
| Playbook | Your team's positions on each clause: what you accept as standard, what you accept as a fallback and what you never accept. In this product it lives in the practice profile. |
| Connector | A link between Claude and another system, such as a legal research database, a document management system or Slack, built on the Model Context Protocol (MCP), an open standard. Once connected, Claude can read from that system and, where allowed, write to it. |
| Research connector | A connector to a legal research source such as CourtListener. The product's citation checks depend on one. |
| Artifact | An interactive page that Claude builds and hosts, such as a tracker or a dashboard, which you can open, fill and share. The legal gallery is a set of ready-made ones. |
| Tracked changes | Word's feature that marks every edit so a reader can accept or reject each one. The product's contract skills are written to output in this mode. |
| Zero data retention | An API arrangement under which Anthropic keeps no copy of your prompts and outputs after answering, on the endpoints and models it covers. |
| Data processing addendum | The contract term under which a provider processes your data on your instructions; the baseline for legal work. |
| Audit log | The organization's record of who did what in Claude and when; Enterprise only. It does not contain the content of chats. |
| Compliance API | The Enterprise feed from which an organization's security team pulls activity events, chat data and file content into its own monitoring tools. |
| Step, gate, tier | The Slow AI Kitchen's units. A step is one of twelve stages of the work; a gate is a checkpoint the work must pass; a tier sets how deep each gate goes for a task of given stakes. Section 5. |
| Owner, Reviewer, Approver, Builder, Preparer | The method's five task roles. The Owner answers for the outcome; the Reviewer checks it; the Approver signs off; the Builder uses the AI; the Preparer frames the task and does the first pass. Section 5. |
| Service Record | The method's one-page close-out of a piece of high-stakes work, written by the Owner within a day of release. |
| Informed Intent, Slow AI, Final Liability | The three doctrines beneath the method, explained in Section 5. |
| GRCnext™ | The author's framework for the choices an organization keeps open when a risk happens: Services, Tolerances, Pipes, Switches, Exits. It appears in the registry entry's last row. |

## 3. If this is your first day with Claude

Claude is an AI assistant made by Anthropic. You use it by writing to it in plain language and reading what it writes back; it can also read documents you give it, search connected systems and build pages and files. It runs in a web browser at claude.ai, in a desktop app for Mac and Windows, in mobile apps and, for this product, inside Microsoft Word and Outlook through the Claude for Microsoft 365 add-in.

Four things matter on the first day.

**The plan decides the terms.** Free, Pro, Max and Ultra are individual plans. Team and Enterprise are sold to organizations, and on those plans Anthropic does not train on your content by default and the organization controls retention and sharing. Nothing Client-related goes into an individual account, however convenient. Section 6 has the detail.

**The desktop app is where the legal plugins live.** Open the app, and the Cowork tab is the part built for longer, multi-step work. Customize, then Browse plugins, is where the twelve legal plugins are installed. Once a plugin is installed, its skills fire when relevant and its slash commands are available from the message box. Section 9 walks through it.

**Connectors are how Claude reaches your systems.** In the app, Settings, then Connectors, lists what Claude can be linked to. For legal work the first connector is a research tool, because the product marks every citation by where it came from and treats a citation it could not check as unverified. Section 12.

**Artifacts are the ready-made tools.** At claude.ai/artifacts, under Legal artifacts, Anthropic and its partners have published interactive tools for legal work: a citation checker, a regulatory timeline, a legal front door for colleagues' questions and more. Each opens as a sample you can look at before you make your own copy. Section 13.

If you have used no AI assistant before, one more thing. Claude writes fluent, confident text whether or not it is right. The whole of this guide is organized around that fact: the method puts a lawyer's reading, tests and sign-off around the product so that fluency is never mistaken for verification.

## 4. What Claude for Legal is, and what Anthropic says it is not

As at 1 November 2026, Claude for Legal is four things. It is twelve practice-area plugins published as open source under the Apache 2.0 license in the repository anthropics/claude-for-legal: commercial-legal, corporate-legal, employment-legal, privacy-legal, product-legal, regulatory-legal, ai-governance-legal, ip-legal, litigation-legal, legal-clinic, law-student and legal-builder-hub, with a partner-built cocounsel-legal beside them. Open source means the instruction files can be read by anyone, which is how this guide checked them. It is, by Anthropic's count, more than sixty legal connectors added since the product launched in May, to the systems legal teams already use, from document management and contract lifecycle management to legal research. It is a gallery of legal artifacts introduced on 28 October 2026 and built by Anthropic and, for a second shelf, by law firms, legal technology companies and access-to-justice organizations. And it is Claude inside Word and Outlook, where counterparty paper is reviewed against a playbook with tracked changes.

Anthropic's own words set the frame. The plugin repository says that every output from these plugins is a draft for attorney review, that the plugins are built with source attribution on every citation, conservative defaults on privilege and subjective legal calls, jurisdiction assumptions surfaced and explicit gates before anything is filed, sent or relied on, and that "These plugins do not represent Anthropic's legal positions." The attorney using the plugin, not the plugin and not Anthropic, is responsible for the legal positions taken in the work product. The artifacts announcement says the same thing in one sentence: Claude completes the first pass, and a lawyer applies their judgment to the results. That is a vendor describing a kitchen: stocked, with gates on the doors and no chef.

The Slow AI Kitchen is the discipline for cooking in it. The method's first instruction is the one the product cannot give. Human steps come in front: the task framed, done defined, the first pass made by hand, the context read. Only then is the AI used. What follows is that discipline, worked against this product as it stood on one day.

## 5. The Slow AI Kitchen on one page

The Slow AI Kitchen is a twelve-step method for using AI on work that matters. Steps 1 through 9 govern one dish, the production of a single piece of work product, with seven gates, which are checkpoints the work must pass. Steps 10 through 12, the Feast, govern the deployment of tools across a whole function, with three more gates. A gate that is skipped does not disappear; it becomes a liability.

The nine steps of one dish, with their kitchen names: Define the Dish (Step 1, frame the task and name who owns the outcome); Mise en Place (Step 2, Gate 1, write three to seven pass-or-fail tests that define done); Knife Work (Step 3, Gate 2, the manual first pass that cannot be delegated without losing cognitive grip on the task); Read the Kitchen (Step 4, Gate 3, who is affected if the output is wrong and what action follows); Apply Heat (Step 5, Gate 4, use the AI inside that frame, at the speed of human verification, not at the speed of machine generation); Name the Chef de Partie (Step 6, Gate 5, confirm the named Owner, Reviewer, Approver and escalation path); Build the Plate (Step 7, the deliverable); Taste Before Service (Step 8, Gate 6, test it against the tests, by a human, against something outside the model); Open the Pass (Step 9, Gate 7, the human release decision and the review after it). The three steps of the Feast: Plan the Menu (Step 10, Gate 8, the registry of which tools may run, for which work, at which tier, by whom); Staff the Brigade (Step 11, Gate 9, who is trained and authorized for what); Run the Event (Step 12, Gate 10, the audit log, the incident procedure and the review cycle).

Tiers set the depth of each gate and never remove one. Tier 1 is low-stakes internal work. Tier 2 is moderate: internal analyses, training materials, Client-facing drafts under review, process documentation, with a full set of tests, a documented context check, a named Reviewer and an evidence log. Tier 3 is high-stakes: decisions affecting customers, employees or regulated operations, legal, compliance or risk determinations, external representations, automation tied to action, with the full method, the first pass retained as evidence, distinct Reviewer, Approver and Owner with the escalation path named, second review with an evidence log, a sign-off record, a remediation or rollback plan on file and a Service Record. The tier is assigned before the work begins, by a named human, with the reason recorded; in organizational use the registry under Step 10 sets it, and a team does not classify its own work down.

Five task roles run through the recipes: Preparer, Builder, Reviewer, Approver and Owner. In a small team one person holds several. In every team the Owner is a human. At the Feast, three organizational roles: the AI Owner, accountable for AI-assisted outcomes in a function; AI Operators, trained and authorized to use specific tools at specific tiers; and an Executive Sponsor at the top of the escalation chain.

Three doctrines run through all twelve steps. **Informed Intent** is the playbook written before the review, so that the machine executes a standard rather than reconstructing one afterward. **Slow AI** is the precondition, not a limit on how fast anything runs: AI that cannot be governed, explained and audited is not deployed, and the three tests are conjunctive. In this product they are tested at the joints, the approvals, the connectors and the exceptions, which is where the attention goes. **Final Liability** is a named lawyer on every output, because the Owner cannot be the AI. The closing line of every document in this account states the third: Final Liability rests with the Human.

## 6. Choose the plan and the terms

In the Kitchen, Plan the Menu is Step 10, the first step of the Feast and Gate 8, the authorized tool registry. It comes before any dish here because the terms decide everything after. Do these four things before anyone opens the product.

1. **Buy the organizational plan.** Client work runs on Team, Enterprise or the API under Anthropic's commercial terms, never on a personal plan. Under those terms Anthropic does not train on customer content by default, and Enterprise administrators set an organization-wide retention period, the length of time your chats are kept. On Team and Enterprise plans artifacts stay inside your organization by default and an owner decides whether anyone may share outside it. Sign the data processing addendum. Record the retention period you chose.
2. **Decide where the most sensitive matters run.** On the API, retention is thirty days as standard, or zero on eligible endpoints and models under a zero data retention agreement. Anthropic's guidance adds that for its most capable models, where safety monitoring requires it, prompts and outputs are retained for thirty days in a governed store that is automatically deleted, so zero data retention does not reach every model, and the registry should say which. Claude is also available inside a customer's own cloud through Amazon Bedrock and Google Cloud Vertex AI, which changes where the data resides and whom the customer contracts with, and does not by itself switch off that safety monitoring. If your firm has neither an API team nor a cloud team, the practical answer is that the most sensitive matters do not go into the product at all until it does.
3. **Understand who at Anthropic can read what.** Human review at Anthropic is, in its words, a very narrow exception: retained data is processed by automated safety systems; only content flagged by those systems can be reached by a human reviewer; and every human read is logged to an entry that customers with Access Transparency can retrieve. Ask your Anthropic contact whether your plan includes Access Transparency and write the answer down.
4. **Write the registry entry before the first login.** Section 8 gives a filled example. The point is that what may run, for which work, at which tier and by whom is decided by the function, in writing, before any individual decides it for themselves.

## 7. Privilege and confidentiality, in plain words

A lawyer's first question about any new tool is whether using it puts privilege or confidentiality at risk. As at 1 November 2026 the public record gives two anchors and one vendor statement.

**The ruling that turned on a consumer account.** The decision every AI privilege memo now cites is *United States v. Heppner* in the Southern District of New York, a bench ruling of 10 February 2026 with a memorandum opinion filed on 17 February. A criminal defendant had used a consumer Claude account, on his own initiative and not at counsel's direction, to analyze his case; the court held the documents neither privileged nor work product. As the law firm alerts report it, the chatbot was not a lawyer and had not been engaged by counsel; the consumer terms permitted the provider to log, train on and disclose the exchanges, so there was no reasonable expectation of confidentiality; and the material was not prepared at the behest of counsel. Anthropic's own reading is that the ruling said nothing about lawyers using enterprise tools. The lesson for a legal team is the one Section 6 already gave: the plan decides the terms, and the terms decide the expectation of confidentiality.

**The order that reads like a registry entry.** Anthropic's privilege guidance reports four later trial-level decisions holding AI-assisted litigation preparation protected as work product, among them *Morgan v. V2X, Inc.* in the District of Colorado, the one I read at source. On 30 March 2026 the magistrate judge there amended the protective order so that no party may input confidential information into any artificial intelligence platform unless the provider is contractually prohibited from storing or using inputs to train or improve its model and from disclosing inputs to any third party except where essential to delivering the service, with any such third party bound by obligations no less protective; the provider must contractually afford the party the ability to remove or delete all confidential information on request; and a party intending to use AI it contends meets these requirements must retain written documentation of those contractual protections. The court also ordered the plaintiff to disclose, within ten days, the name of any AI platform he had used with the other side's confidential information. Expect to be asked, and keep the paperwork that answers.

**What Anthropic itself suggests.** Its guidance proposes, in effect, a registry entry in four lines: whether you are on commercial terms with a data processing addendum and the no-training commitment, which it calls the baseline expectation for legal technology; whether the sensitivity of the matter calls for zero data retention or an in-tenancy deployment; how you will keep a lawyer in the loop, verify output against primary sources and document your AI use; and your Client-consent and engagement-letter practice, which several bar opinions, including American Bar Association (ABA) Formal Opinion 512, address. The guidance describes Anthropic's products and its view of the public record as at June 2026, says it is not legal advice and says the right answer depends on jurisdiction, Clients and matters. Section 22 returns to all of this, with the bar rules.

## 8. Write the registry entry

Step 10, Gate 8, is the authorized tool registry: which tools, for which workflows, at which tier, by whom and what is prohibited. Here is one entry for this product, filled in as a legal function might fill it on 1 November 2026. Replace the names, and do not skip the last row.

| Field | Entry |
|---|---|
| Tool | Claude Enterprise; the commercial-legal and privacy-legal plugins from anthropics/claude-for-legal; the Tabular review, Playbook deviation board, Cite check, Regulatory horizon scan and Ask legal artifacts |
| Surfaces | claude.ai, the Claude desktop app, the Claude for Word sidebar |
| Terms | Commercial terms with the data processing addendum signed; retention period set in the Enterprise retention controls and recorded here; matters the General Counsel designates as highly sensitive do not run here but on the API with zero data retention on a model it covers, or in the company's own cloud |
| Tier 1 | Internal notes and summaries |
| Tier 2 | Contract first pass (Recipe 2), horizon scans (Recipe 4), front-door routing (Recipe 5) |
| Tier 3 | Anything filed, sent to a counterparty or relied on for a legal determination, and the GREEN path of NDA triage (Recipe 1) until reclassified; second review and sign-off record |
| Prohibited | Client material on personal accounts; material under a protective order until the order has been read against the Morgan conditions in Section 7; investigation material outside its designated workspace; any connector with write access to the document management system |
| Connectors | Named individually; read-only unless the AI Owner approves otherwise; a research connector connected before any citation is relied on |
| Sharing | Artifacts stay inside the organization; external sharing off unless the AI Owner allows it for a named artifact; production artifacts made in clean chats |
| Owner | AI Owner: the deputy General Counsel for commercial |
| Review | Quarterly, and on any model change or Anthropic policy change; the Usage Policy effective 12 November 2026 is one such trigger |
| Evidence | Enterprise audit logs and the Compliance API; the matter file (prompt, profile version, output, reviewer, decision); Service Records for Tier 3 |
| Exit | What leaves with us if we switch: the practice profile and playbook, which are plain text files we hold; the deviation log; the Service Records. What does not: Unknown until asked, for the artifacts' stored data and the connector configurations |

The last row is **GRCnext™**, the framework's question about choices rather than controls: what options remain when the risk happens, and whether they can be executed under stress. A registry entry that cannot name what leaves with you has not finished. Ask the vendor the question before you sign, and record the answer.

## 9. Install the plugin

Nothing in Part III produces work product. All of it decides what the work product will be measured against, which is why it comes first.

**In the Claude desktop app.** Open the Cowork tab. Click Customize in the left sidebar, then Browse plugins. Install commercial-legal, or the plugin for your desk: privacy, corporate, employment, litigation, regulatory, AI governance, intellectual property or product. After install, the plugin's skills fire automatically when relevant, its slash commands are available by typing `/` in the message box, and its agents run on the cadence set in their files or in the practice profile.

**In Claude Code**, for the one lawyer on the team who lives in a terminal: add the marketplace with `/plugin marketplace add` followed by the path to the downloaded repository folder or its GitHub address, install with `/plugin install commercial-legal@claude-for-legal` and restart. The quick start page says the plugin is not live until you restart. When asked whether to install for this project only or for all projects, choose all projects (user scope), or the plugin cannot read files outside the project folder, which for a lawyer is most files.

**In Word and Outlook.** Install Claude for Microsoft 365 from Microsoft AppSource. Once installed, the skills from any plugin you have enabled are available from the sidebar by typing `/`, and connectors are reachable from the same surface. I have not tested this path; Section 16 says what it means for the contract recipe.

## 10. Run the cold-start interview

Type `/commercial-legal:cold-start-interview` and press Enter. The plugin interviews you, conversationally, about your playbook positions, your escalation rules and the recurring problem that costs the team the most time (the repository's own phrase for it is "the thing that makes you groan when it hits your desk"). The repository's main page gives ten to twenty minutes per plugin, the plugin's own page says ten, and both warn that skipping setup "is the single most common reason a skill produces generic output."

Three things to know before you start.

**It will ask which side you sit on.** Early in setup the interview asks whether to build a sales-side playbook (you sell; usually your paper), a purchasing-side playbook (you buy; usually their paper) or both, because the answer flips nearly every position: liability caps, the direction of indemnities, termination rights, ownership of intellectual property. If you pick both, it builds sales-side first and you run `/commercial-legal:cold-start-interview --side purchasing` afterward for the other.

**Bring documents.** Have five to ten recent signed agreements ready to share; twenty give a clearer pattern. The interview reads them to learn the positions you have accepted in signed deals. That is not the same as you having read them: Section 15 says what you must read yourself before the first run.

**A two-minute quick start exists.** The interview asks "Quick or full?" at the start. Use quick for Tier 1 work only. Everything a lawyer will rely on needs the full interview, with your commercial counsel in the room, because the NDA skill will refuse to pass anything to signature until attorney-reviewed positions exist; answer full, or upgrade later with `/commercial-legal:cold-start-interview --full`.

## 11. Read the practice profile, field by field

The interview writes a practice profile: a plain-English document, saved as a file named `CLAUDE.md`, that every skill in the plugin reads before it works. The repository gives its location as `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`, a hidden folder in your home directory; it can be edited directly and survives plugin updates. I confirmed that path for Claude Code only. If you cannot find the file from the desktop app, you do not need to: `/commercial-legal:cold-start-interview --redo` re-interviews you and shows a diff before overwriting, `--redo <section>` redoes one part, and any skill will record a new position when you tell it to. Read it in full after the interview, because its structure is the Kitchen's Mise en Place written down by someone else, and every field is a question the method asks at Gates 1, 3, 5 and 6.

- **Who we are**: the company and its industry, the size of the contracts team, who the final escalation point is, roughly how many agreements a month and which contract system you use. The section carries a field the template labels "The thing that hurts": the recurring problem that costs the team the most time, recorded in the team's own words, so that the skills know what to look for first.
- **Who's using this**: a lawyer, a non-lawyer with attorney access or a non-lawyer without; and the attorney contact. The answer changes the header every output carries and the gate before signature in Section 15.
- **Available integrations**, each with a fallback if unavailable.
- **Playbook**, by side, in five clause groups. Limitation of liability is four positions, not one: the direct cap as a multiple of fees, indirect and consequential damages, the carve-outs above the cap and the cap base definition, with Acceptable fallbacks and Never accept beneath them. Indemnification and term and termination carry Standard position, Acceptable fallbacks and Never accept; data protection carries Standard position, Requirements and Acceptable fallbacks; governing law and venue carries Preferred, Acceptable, Escalate and Never. Then The one thing, the deal-breaker every review on that side checks first.
- **Escalation**: a matrix in four columns, Can approve, Without escalation, Escalates to and Via, with dollar thresholds and automatic escalations regardless of dollar value. Put names in it, not teams.
- **House style**: tone in redlines, who reads stakeholder summaries, where work product goes, where renewal alerts go.
- **Outputs**: a work-product header in a lawyer and a non-lawyer variant, and a reviewer note with five fields, Sources, Read, Flagged for your judgment, Currency and Before relying. The reviewer note sits above every deliverable and is where the plugin tells you what it could not verify and what you should do before relying on the output.
- **Decision posture on subjective legal calls**: the plugin prefers the recoverable error, flagging the line for your review rather than deciding silently.
- **NDA triage preferences**, including the closing instruction appended to every triage.
- **Seed documents reviewed**: a table of the agreements the playbook was learned from.

Three further sections are read once and rarely edited: **Review preferences**, whose `confirm_routing` setting, on by default, makes the review command ask you to confirm where it is routing an agreement before it proceeds; **Matter workspaces**, which matter only to practices with several Clients; and the **Shared guardrails** every skill follows, including the rule that a citation's tag records where it came from and never how confident the model is.

If a threshold is wrong, edit the file or tell a skill to record the new position. If your practice changes materially, run `/commercial-legal:cold-start-interview --redo`.

## 12. Connect a research tool

Connect a research tool before anything else. In the desktop app: Settings, then Connectors, then CourtListener or your research platform. The repository's guardrail is specific, and it is the reason this comes before any work. A citation that arrives through a research connector is tagged with its source. A citation from model knowledge alone is tagged `[verify]`. If no research tool is connected at all, the reviewer note above the deliverable records that sources were not verified. The repository's words: the connectors are what make the cites trustworthy; set them up before you set up anything else.

What the tags mean when you see them. `[verify]`, or the longer `[model knowledge — verify]`, marks a fact the reader should confirm against a primary source before relying on it. `[review]` marks a judgment call the attorney has to make. A source tag such as `[CourtListener]` means the citation appeared in that tool's result in this session. The plugin's own rule is that the tag describes where a citation came from, not how confident the model is, and the skill's output is never verified by the skill itself; the reader is what verifies. That is the method's Gate 6 in the vendor's words.

## 13. Open the artifact gallery

Go to claude.ai/artifacts and open Legal artifacts, with an Anthropic section and a Partners section. Select an artifact and press Try it: a view-only sample opens, loaded with sample data and marked "Sample data" and "Content is user-generated and unverified." In the sample, Make it yours gives you an editable copy to load with your own documents and connectors. Look at the sample first; it shows you the fields you will have to fill and the decisions you will be asked to make.

Four facts for the registry. Anthropic says a legal team can work on an artifact with colleagues across the business or with Clients and partners, with sharing settings that ensure privacy and support ethical walls between teams. On Team and Enterprise plans artifacts stay inside the organization by default and an owner decides whether users can share outside it. When you share an artifact made in a chat, viewers also get access to the attachments and files in that chat, so make the production copy in a clean chat. And if the gallery does not appear, an owner may need to turn on the artifact capabilities under Organization settings, Capabilities.

On plan availability: the gallery showed in my own Max account on 1 November 2026 and is therefore not Enterprise-only, although the announcement files it under Claude Enterprise and names no other plan; the help center gives Team every artifact capability Max has, with organization sharing added, and one practitioner reports testing the gallery on Max and Team; I did not see a Team account myself. Client material stays on commercial terms in any case. Name an owner for every artifact before you share it.

## 14. The recipe card

The Cookbook writes one pass through Steps 1 to 9 in eight fields, and the order is the discipline: AI does not enter until the fifth. The Dish frames the task (Step 1). Done Means states three to seven pass-or-fail checks, written before AI is touched (Step 2, Gate 1). Prep by Hand is the manual first pass (Step 3, Gate 2). Watch For reads the setting the output will land in (Step 4, Gate 3). Bring in AI is bounded use (Step 5, Gate 4). Who Signs names the Owner, the Reviewer, the Approver and the escalation path (Step 6, Gate 5). Plate and Taste builds the deliverable against Done Means and tests it (Steps 7 and 8, Gate 6). Serve is the human release decision and the review after it (Step 9, Gate 7), closed by a Service Record written by the Owner within a day.

The Cookbook's starter set stays in Tiers 1 and 2. Recipes 1 and 3 below run at Tier 3, and Recipes 2 and 5 reach it at a named point, which is why they carry the controls that the Kitchen's Tier Application Map, its table of controls per tier, adds at that tier and why every Tier 3 pass ends in a Service Record. Each recipe opens with its tier and closes with two sentences: what the product does at the gates as observed and what the Kitchen adds. Section 21 collects them.

## 15. Recipe 1: NDA triage

**Tier.** 2 for the YELLOW and RED paths, which reach a lawyer by design. 3 for the GREEN path, which can reach signature without one, until the weekly sample has run clean for a quarter and the AI Owner records the reclassification in the registry.

**The Dish.** The week's inbound nondisclosure agreements (NDAs), triaged so that only the hard ones reach a lawyer's desk. The plugin's three outcomes, in its own labels: GREEN, route to signature; YELLOW, flag for the named approver; RED, do not submit, talk to legal first. GREEN means route to signature. It does not negotiate.

**Done Means.** Five tests. No GREEN was issued before attorney-reviewed NDA positions were in the profile. Every YELLOW names its approver and every RED quotes the clause. No GREEN carries an obligation beyond confidentiality. While the GREEN path is Tier 3, every GREEN that went to signature carries a lawyer's recorded yes to the skill's question whether an attorney has reviewed it; once reclassified, the weekly sample stands in. The misses are logged.

**Prep by Hand.** Read three of this week's NDAs in full by hand and write the team's position for each check the skill runs: mutuality, the definition of confidential information and its marking and oral-disclosure rules, the carve-outs, residuals, term and survival, restrictive covenants, attorneys' fees, the backup and archival carve-out and governing law. Decide which side the company sits on for NDAs. The skill reads those positions from a section headed `NDA triage positions` under the matching side of the profile's Playbook. The template does not contain that section and the interview does not write it; the skill offers to add a position whenever it meets a term the playbook does not cover, says of itself that it "does not ship with default positions on NDA terms," and will not issue GREEN until the section exists and has been attorney-reviewed. Add the section yourself, under the side you use, before the first run. Its lines are what every GREEN will be measured against, and nobody but you can write them.

**Watch For.** The repository says NDA triage is built for self-serve by non-lawyers, so that sales and business development can run it before calling legal. The person pressing for signature today is in sales. A wrong GREEN binds the company for the term. An NDA from a jurisdiction outside the configured posture may not transfer, and the skill flags that.

**Bring in AI.** In the desktop app, type `/commercial-legal:review` in the message box and attach the NDA; in Claude Code, give the file's path after the command. The command takes one agreement at a time, as a file, a link, a contract-system record or pasted text, and by default asks you to confirm where it is routing the review before it proceeds; the loop over the week's inbox is yours. The skill determines the side and asks if that is unclear. Any obligation beyond confidentiality, a standstill, a license grant, a non-solicit, a non-compete, exclusivity, an assignment of intellectual property, a right of first refusal, a most-favored-nation term or broad arbitration, makes the NDA YELLOW automatically. It checks the clauses listed above against the playbook. GREEN returns a check table with playbook references; a clean NDA gets one line, no red flags identified, route for signature per standard process. YELLOW returns one-line actionable edits and, for each flagged item, its section, the playbook position it hits, a legal risk rating, a business friction rating and a likely resolution. RED returns the exact quoted language, why it is a problem, the ratings and a recommended response: use our paper, push back with specific language or walk. Redlines are as small as possible, a word before a phrase, a subclause before a sentence, a sentence before a clause; anything needing new drafting is routed to legal. Three gates are built in. If the output is headed outside the privilege circle, the skill flags it and offers a privileged version and a sanitized one. Before a non-lawyer's GREEN proceeds to signature, the skill asks for an explicit yes to the question whether an attorney has reviewed, and without one it generates a one-page brief for the attorney instead. Without attorney-reviewed positions in the profile it will not issue GREEN at all, and defaults to YELLOW.

**Who Signs.** The salesperson who runs the triage is the Builder. One named counsel is Owner of every YELLOW, every RED and the weekly GREEN sample, and is the attorney whose review the skill asks about. A second lawyer or the contracts manager is Reviewer of the sample. The signatory under the signature authority policy is Approver. The approvers named in the YELLOW labels come from the escalation matrix.

**Plate and Taste.** Each week, reread three GREENs in full against the positions written by hand. One miss returns the week's GREENs to YELLOW and reopens the profile, because a miss is a profile defect before it is a model defect.

**Serve.** Sign within scope. Log what the triage missed. A Service Record within a day for the GREEN path while it is Tier 3. After a quarter of clean samples the AI Owner may record the GREEN path as Tier 2 in the registry; nothing else reclassifies it.

What the product does at the gates: the refusal to issue GREEN without attorney-reviewed positions, which is Gate 1 built into the skill; the confirmation demanded before a non-lawyer's GREEN reaches signature, which is Gate 7; the automatic YELLOW for obligations beyond confidentiality, which is part of Gate 3; and quoted clauses with playbook references, which are Gate 6's evidence. What the Kitchen adds: the positions written by hand before the first run, the weekly rereading of what the machine passed, an Owner who is not the person pressing the button and the record.

## 16. Recipe 2: a vendor MSA against the playbook

**Tier.** 2 for the negotiation draft, which a lawyer reviews before it leaves. 3 at signature.

**The Dish.** A supplier's master services agreement (MSA) on the supplier's paper, reviewed from the purchasing side against the company's playbook, with redlines the lawyer can send.

**Done Means.** Four tests. Every clause in the profile's five groups carries a status against the playbook. Every deviation names its approver and the fallback offered. The reviewer note's five fields are filled, Sources and Read by the lawyer. Tracked changes, every one accepted or rejected by hand, none in bulk.

**Prep by Hand.** The playbook is the Informed Intent and it is written before the review. For limitation of liability on the purchasing side the template asks for four positions rather than one and says the amount is the least important of them. Direct cap: the supplier's liability at twenty-four months' fees paid or payable. Indirect and consequential damages: excluded both ways, with the carve-outs preserved. Carve-outs we require above the cap: confidentiality, data breach, indemnity, gross negligence. Cap base definition we accept: fees paid in the twelve months before the claim, never the current order form alone or the prior three months. Acceptable fallbacks: twelve months' fees with the carve-outs intact. Never accept: the carve-outs removed, or a cap base left undefined. Write The one thing. Then read the supplier's draft once and mark the three clauses you expect to fight.

**Watch For.** The plugin assumes you are the customer in most reviews and flips the playbook's polarity when you are the vendor, so a profile built sales-side reviews a purchase badly unless the purchasing side has been built too. The escalation matrix's dollar thresholds and automatic escalations decide who approves what. The counterparty's defined terms carry positions the clause headings hide.

**Bring in AI.** For one contract, `/commercial-legal:review` in the Word sidebar with tracked changes on. The repository says every contract-touching skill is authored to work in the Claude for Word sidebar with tracked changes as the output mode, so that a reviewer accepts or rejects each change as for a human markup. I have not tested that path; test it on a contract you have already reviewed by hand before relying on it. For a stack of contracts, the playbook deviation board artifact: each clause marked standard, fallback or deviation with the contract's wording quoted beside the playbook position, and each deviation held, waiting for a decision, until the person who approves it approves. Asking for a stakeholder summary turns the review into two paragraphs for the business; that skill has no slash command and fires on the request.

**Who Signs.** The deal lawyer is Owner. The approver of each deviation is whoever the escalation matrix names for that clause and amount.

**Plate and Taste.** Accept or reject every change. Never accept all. Check the three marked clauses first; if the review missed one, fix the profile, not the lawyer. Every plugin output carries the reviewer note, Sources, Read, Flagged for your judgment, Currency, Before relying. That is Gate 6, pre-printed by the vendor. Fill the human half.

**Serve.** The negotiation draft leaves under the lawyer's name. At signature the dish is Tier 3: second review, sign-off record, an amendment path on file for a deviation that surfaces after signature, Service Record within a day. Then the loop most teams skip. Your redlines of its redlines reveal intent. The deal-debrief agent sweeps recently signed agreements for playbook deviations each Monday and prompts the attorney to log the context while memory is fresh. The playbook-monitor agent runs after each debrief and proposes a playbook update when the same clause has been overridden five or more times in a rolling twelve months. `/commercial-legal:review-proposals` is where a human says yes or no to each proposal. The playbook changes by decision, not by drift.

What the product does at the gates: the deviation hold for a named approver, which is Gate 5 applied clause by clause; the reviewer note, which is Gate 6's log; the escalation matrix in the profile; and the monitor's proposal loop, which is Step 9's post-action review turned into an agent. What the Kitchen adds: the playbook written before the review, the human decision on every proposal and the rule that no change is accepted in bulk.

## 17. Recipe 3: cite check before filing

**Tier.** 3. The output is an external representation to a court.

**The Dish.** A thirty-page brief with forty-one authorities, filing Friday.

**Done Means.** Four tests. Every authority was pulled from the reporter or through a research connector, none from model memory. Every quotation matches the reporter page, checked by a human. Subsequent history was checked in your citator, the service that reports whether a case is still good law. Every flag carries a recorded human decision.

**Prep by Hand.** The drafting lawyer has read every case cited. Any `[verify]` tag left by a drafting skill is cleared before the check runs, because the cite check reads the brief you give it.

**Watch For.** The affected party is the court. Fabricated citations have drawn sanctions since *Mata v. Avianca* in 2023, and the orders have not grown gentler. The artifact's own description: each footnote is checked against the source files you add, and you see the ones that need a decision, like a quote that does not match or a wrong page. An authority you did not add reads as not found, and the artifact does not claim to check whether a case has been overruled. Its banner says the content is user-generated and unverified. It means it.

**Bring in AI.** From the gallery, Cite check, Try it to see the sample, then Make it yours; add the brief and the source files. The sample reads "31 citations. 7 need a reviewer." The flags come in three kinds. Can't be found: not found, by citation or by name. Substance: a quotation that differs by a word, a source read as saying something else, a citation with no significance, a pincite that points to the wrong page. Form: drop "at" before the pincite. Each flag takes one of three decisions: Fixed, Not an issue, Flag for attorney.

**Who Signs.** The signing attorney, who certifies the filing under Federal Rule of Civil Procedure 11 in a United States federal court or the local equivalent, is Owner and, in a small firm, Approver as well; where the team allows it, a partner who did not draft approves. A second lawyer is Reviewer.

**Plate and Taste.** Open every flag, and a sample of the unflagged. Can't be found means a missing file or a case that does not exist; pull it from the reporter before deciding which. Not an issue is a human override; record the reason. The artifact flags what it detects. The risk sits in what it did not.

**Serve.** File. The remediation plan is on file before filing: a wrong citation found afterward is corrected with the court under the applicable rules. The Service Record within a day: what was flagged, what was wrong, what changes in the drafting profile. The Kitchen's test of ownership applies here with no softening: the Owner can stand at a whiteboard and explain to another lawyer what was done and why, with no model in the room.

What the product does at the gates: the comparison of each footnote against its source with the mismatch shown, which is Gate 6's test on the quotation, and a decision recorded per flag, which is Gate 7's shape. What the Kitchen adds: the lawyer who read the cases before the check, the citator check the artifact does not claim, the sample of the unflagged and the record of every override.

## 18. Recipe 4: regulatory horizon scan

**Tier.** 2. The scan informs. The moment a missed effective date becomes a compliance determination, the determination is Tier 3.

**The Dish.** The upcoming laws and regulations that will affect this company, on one timeline, scored for impact and linked to their sources.

**Done Means.** Four tests. Every item links to an official source: the Official Journal, the Federal Register, a gazette or the regulator's own page. Every item carries a date and a status: proposed, adopted or in force. Every impact score has been confirmed or changed by the Owner. The regimes already tracked by hand all appear.

**Prep by Hand.** Not "our business." Write the entity, the sectors, the products and the eight jurisdictions where the company sells. List the regimes the team already tracks and their next dates. That list is how you will judge what the scan missed.

**Watch For.** Impact scores are the model's opinion until the Owner confirms them. An item with no official source is an item with no source. A timeline that looks complete is the most dangerous kind.

**Bring in AI.** From the gallery, Regulatory horizon scan, Try it, then Make it yours. Describe the business and where it operates. The artifact puts upcoming laws and regulations on one timeline, scores each for its impact on the business and links it to its source; the sample shows an impact rating and a next key date for each item. Then ask it what it excluded, and why.

**Who Signs.** Regulatory counsel owns the timeline.

**Plate and Taste.** Click every link. No official source, delete the item. Compare the timeline against the hand list and account for every regime missing from either side.

**Serve.** Publish internally with the Owner's name and the run date, monthly. The regulatory-legal plugin's scheduled agent, reg-change-monitor, which the repository's agent table calls Reg Feed Watcher, reads the feeds, filters them by the materiality threshold learned at setup and posts a digest, weekly by default. It is a Feast item: it is registered under Step 10 with a named operator under Step 11 before it runs unattended.

What the product does at the gates: a source link on every item, which is Gate 6's precondition, and a schedulable agent for the recurring sweep. What the Kitchen adds: the hand list that measures the scan, the Owner's confirmation of every score and the registry entry before any agent runs on its own.

## 19. Recipe 5: Ask legal, the front door

**Tier.** 2 for the routing. 3 for any answer that is a final recommendation to an individual about their own situation, which Section 22 explains.

**The Dish.** Colleagues ask legal questions in plain words. Questions that approved guidance covers are answered at once. Everything else goes to a lawyer with a brief, and the requester can see its status.

**Done Means.** Five tests. Every published answer carries an Approved by entry naming a lawyer and a Review by entry. Nothing leaves Drafts without both. Every answer cites the guidance item it rests on. The requester is told that an AI answered. A named lawyer samples the auto-answers weekly.

**Prep by Hand.** The Guidance tab is the Informed Intent. Load the signature authority policy, the NDA rules and the data request procedure as documents; the artifact drafts answers from them, each marked with its source document and with Legal's position quoted from it, and places them in Drafts. The sample is explicit about the gate: "Colleagues see only what you approve." Approve twenty answers a lawyer would sign before the door opens.

**Watch For.** The sample's inbox tags questions High risk, Urgent, New follow-up, Draft ready and Sensitive, and shows one titled "A question about a member of my team" tagged Sensitive, not yet sorted and with no legal team assigned, twenty-two hours late. That is the question the auto-answer must never take. An auto-answer to an employee about their own case is a final recommendation about an individual's legal rights or livelihood. Anthropic's Usage Policy, effective 12 November 2026, lists Legal and Employment among its high-risk areas and requires a qualified person to review such a recommendation before it reaches the individual, who must be told that AI was used; internal drafting that is not the final recommendation is excluded. The front door's routine answers are internal, and the policy's requirement may still bind where the answer is final. Build as if it does.

**Bring in AI.** From the gallery, Ask legal, Try it, then Make it yours. The artifact has two views, Legal and Colleague, and three tabs: Inbox, with filters for new, waiting and due or late; Guidance, with filters for published, lawyers only, drafts and to review, an audience setting per item and the Approved by and Review by fields; and Insights. The sample reports its own headline figure, the share answered without a lawyer. Read that figure weekly. Do not celebrate it.

**Who Signs.** The lawyer named in Approved by owns the answer. The lawyer who receives a routed question owns that one.

**Plate and Taste.** Weekly, read what was routed and sample what was answered. An item that keeps escalating becomes new guidance or leaves the set. An answer a lawyer would not have given retires its item the same day.

**Serve.** Open the door to one function first, sales or procurement, with the twenty approved answers and the Sensitive routing checked. Service Record for any answer that reached an individual as a final recommendation.

What the product does at the gates: approval before colleagues see an answer, which is Gate 7 built in; source attribution on each answer, which is Gate 6; routing to a lawyer with a brief; and the Sensitive tag. What the Kitchen adds: the twenty answers a lawyer signed before go-live, the weekly reading of what was routed, the retirement rule and the Tier 3 reading of a final answer to an individual, without which the front door is a chatbot wearing Legal's name.

## 20. Staff the brigade and keep the evidence

**Step 11, Gate 9: Staff the Brigade.** A role matrix, filled for a legal function. Every name in it is a person, not a team.

| Role | Who | Record |
|---|---|---|
| Executive Sponsor | The General Counsel | Named in the registry; top of the escalation chain |
| AI Owner | One deputy per function | Accountable for outcomes in that function; signs reclassifications |
| AI Operators | The lawyers who have completed the cold-start interview for their plugin and a Slow AI Kitchen workshop | Listed against tools and tiers; training completion logged; reauthorized on a cycle |
| Builders | The non-lawyers who run NDA triage and ask the front door | Authorized for Tier 1 and the triage path only |
| Reviewer and Approver | Per the escalation matrix, by clause and amount | Distinct from the Owner at Tier 3 |

Three things make the matrix real. A billing or innovation code that credits AI work, including the training, because experimentation that competes with billable-hour expectations loses; the [*Law Firm AI Deployment Spec v2*](law-firm-ai-deployment-spec.md) in this pack makes that its first instruction. The professional liability policy read for its AI exclusions, before the first production workflow. And a sponsor senior enough to protect the people and the initiative from short-term agendas.

**Step 12, Gate 10: Run the Event.** The Kitchen asks for audit logging of consequential AI-assisted decisions: what tool, what input, what output, what human reviewed it. Evidence for this product lives in three places, and the method requires all three.

- **On the platform.** Enterprise audit logs record who did what and when, exportable by organization owners for the past 180 days, and they do not contain the title or content of chats and projects, only their identifiers. Chat inputs and outputs are exportable by a Primary Owner through data export. The Compliance API, available to Enterprise organizations and Claude Platform customers, pulls activity events, chat data and file content, now including the audit log events, so that Claude activity can be monitored in the tools a security team already uses. Access Transparency logs any human read at Anthropic.
- **In the matter file.** The prompt, the profile version, the output, the reviewer and the decision, because the platform's records belong to the organization and are exported by its owners, and a matter needs a record of its own that a lawyer can produce.
- **In the Service Record.** For every Tier 3 output, within a day: which steps were skipped or abbreviated, which gates were argued, what the Owner would not sign and what this service changes in the method. Ten Service Records trigger a method review under Gate 10.

**When something goes wrong.** A wrong citation found after filing: correct it with the court under the applicable rules, pull the output, read the profile that produced it, log the change and write the Service Record that day. The debrief is the prep list for the next service.

## 21. What the product does for you, and what it does not

The table collects the closing sentences of Sections 15 to 19 and adds the Feast rows from Sections 8 and 20. Every entry in the second column was observed on 1 November 2026, in Anthropic's published source or in the author's account; Section 25 gives the source for each. The third column is what was not observed and what Anthropic's own documents say is the lawyer's to supply. Read it as the honest version of the brochure.

| Kitchen gate | What the product does here, as observed | What it does not do | What the lawyer adds |
|---|---|---|---|
| Gate 1, Definition of Done | The practice profile's positions, fallbacks and never-accept lists; refusal to issue GREEN without attorney-reviewed positions | The three to seven pass-or-fail tests for this dish | Writes the tests before the run |
| Gate 2, Manual First Pass | Nothing. The cold-start interview asks for seed documents; it does not read them for you | The reading | Reads three NDAs, the counterparty draft, every case cited |
| Gate 3, Socio-Technical Context | Automatic YELLOW for obligations beyond confidentiality; jurisdiction flags; the Sensitive tag; a destination check against the privilege circle | Who is affected if the output is wrong and what action follows | Reads the setting; decides the tier |
| Gate 4, Bounded AI Use | `[verify]` tags on citations from model knowledge; the reviewer note's record that no research tool was connected; connectors scoped per plugin | The bound itself: which connectors, which tier, which tool | Writes the registry entry |
| Gate 5, Final Liability | Deviations held for a named approver; Approved by on each front-door answer; an escalation matrix in the profile | An Owner distinct from the Builder | Names the lawyer, not the team |
| Gate 6, Verification and Validation | The reviewer note's five fields; footnotes compared against source files; every artifact answer linked to its passage; a Mark checked control on the Tabular review artifact | The checking, and the sample of what was not flagged | Fills the human half of the note; rereads the GREENs |
| Gate 7, Human Release Decision | Confirmation that an attorney has reviewed before a non-lawyer's GREEN reaches signature; "Colleagues see only what you approve"; Fixed, Not an issue, Flag for attorney | The decision and its reason | Decides, and records the override |
| Service Record | Nothing | The one-page close-out | Writes it within a day for Tier 3 |
| Gate 8, Authorized Tool Registry | Nothing within the product; Anthropic's guidance suggests four registry questions | The registry | Writes Section 8 |
| Gate 9, Competency and Authorization Record | The cold-start interview as a setup step | Training records, authorization by tier, a reauthorization cycle | Staffs the brigade |
| Gate 10, Operational Audit and Review Cycle | Audit logs for who, what and when; the Compliance API for chat data and file content on Enterprise; a playbook-monitor agent that runs after each deal debrief and proposes changes | A record the matter can produce on its own; the incident procedure; the method review | Keeps the matter file; reads ten Service Records |

Two observations follow from the table. First, what the vendor has built into the product are gates of a particular kind: instructions in skill files and controls in artifacts that fire when the model follows them. A gate written in a plain-text skill is a policy, not a control, in the sense an auditor uses the words; it can be edited, and a model can fail to follow it. The Kitchen says of Gate 6 that a model's review of its own output in the same session is not verification and does not pass the gate, and the same logic holds for a model's compliance with its own instructions. The Kitchen's gates are held by humans for that reason, and the product's gates are welcome because they make the gates the Human holds faster to pass, not because they replace them. Second, the rows where the product does nothing, Gate 2, the Service Record and Gate 8, are the rows where the vendor could not do anything. Reading the cases, closing out the service and deciding what may run are not product features. They are the chef.

**Running the table against another vendor, or another plugin.** Read the vendor's skill or configuration files if they are open, as Anthropic's are. Open the product's sample, not its brochure. For each of the Kitchen's ten gates write down what you saw fire, the label it uses and the date. Leave the third column honest. A row you cannot fill from observation is a row that says Unknown.

## 22. The rules that apply, dated

Four documents govern a legal team's use of this product as at 1 November 2026, and each carries a date that will move.

**Anthropic's Usage Policy, effective 12 November 2026.** The High-risk Use Case Requirements apply to anyone who uses Anthropic's products to make a high-risk AI recommendation, one that can affect an individual's health, legal rights, finances, livelihood or access to housing, education or essential services. The listed areas include Legal, Employment and the separate area of Legal status and adjudication. Two requirements attach. A qualified person must meaningfully review the recommendation before it is delivered or used to implement a decision, with the authority to change or modify it. The affected individual must be clearly told that AI was used. Excluded, among other things, are general information and educational content not applied to the individual's circumstances; explaining advice a qualified person has already given; internal drafting, research, summarization or analysis that is not the ultimate recommendation; applying a fixed rule or formula where the model exercises no judgment about the individual; and business operations that do not advise or decide about a specific individual. Anthropic says the requirements did not change in this version; the section was rewritten to list which kinds of recommendations are covered and which are not. For a legal team the line falls where Section 19 drew it: a draft for a lawyer is excluded; an answer that reaches the individual as the final word is not.

**Anthropic's privilege guidance, 26 August 2026.** Summarized in Section 7. Its own framing is that the profession has been here before with email and cloud storage, that the bar opinions since ABA Formal Opinion 512 apply the existing duties, reasonable care in selecting and supervising the vendor among them, rather than prohibiting use, and that keeping a lawyer visibly directing the work, so that AI output is the attorney's draft and not a substitute for advice, strengthens both privilege and the answer to unauthorized-practice concerns. The guidance is Anthropic's perspective on its own products and the public record as at June 2026 and is not legal advice.

**The courts.** *Heppner* turned on a consumer account and the absence of counsel's direction; it said nothing about lawyers using enterprise tools. *Morgan v. V2X* approved protective-order language that reads like a registry entry: no training on inputs, no disclosure beyond service delivery, deletion on request, written documentation kept and the name of the platform disclosed on order. None of the decisions Anthropic reports is appellate, and a protective order binds the parties to it. Read yours.

**Your bar rules require more.** Competence, including technological competence; confidentiality in the selection and supervision of vendors; supervision of non-lawyer assistance, which is what a skill is; candor to the tribunal, which is what Recipe 3 protects; and, where a bar opinion or a Client asks for it, disclosure and consent in the engagement letter. The product's gates do not satisfy any of them. They make the lawyer's satisfaction of them faster to evidence.

## 23. Next steps: the first day, week, month and quarter

What to do, in order, with the section that explains each item.

**The first day: decide.**

1. Confirm which plan the organization is on, or will buy. If anyone is already using a personal account for Client work, stop that today (Section 6).
2. Name the AI Owner for Legal and the Executive Sponsor (Section 20). Nothing below happens until the AI Owner is named.
3. Read the privilege section with your General Counsel and decide where the most sensitive matters will run, or that they will not run here yet (Sections 6 and 7).
4. Ask Anthropic, or your reseller, the Exit question in writing: what leaves with you if you switch (Section 8).

**The first week: set up one plugin, with a lawyer in the room.**

5. Sign the data processing addendum; record the retention period; set artifact sharing to inside the organization (Section 6).
6. Write the registry entry, using Section 8 as the form, and get the AI Owner's signature on it.
7. Install commercial-legal in the desktop app (Section 9). Connect a research tool (Section 12).
8. Run the full cold-start interview with your commercial counsel present, with five to ten signed agreements to hand, and answer the side question deliberately (Section 10).
9. Read the practice profile in full and add the `NDA triage positions` section by hand, under the matching side of the Playbook, before the first triage (Sections 11 and 15).
10. Open the gallery, Try it on Cite check, Regulatory horizon scan and Ask legal, and look at the sample data before making anything yours (Section 13).

**The first month: one workflow, measured.**

11. Run NDA triage as Recipe 1 for four weeks: one lawyer owns every YELLOW and RED and rereads three GREENs a week; the misses are logged; a Service Record closes each week while the GREEN path is Tier 3 (Section 15).
12. Review one supplier MSA as Recipe 2 on a contract you have already reviewed by hand, so you can see what the review missed (Section 16).
13. Staff the brigade: the role matrix, the training record and the billing code for AI work (Section 20).
14. Write the first incident procedure before you need it: who pulls an output, who reads the profile, who writes the Service Record (Section 20).
15. If the team runs a horizon scan or a front door, start them as Recipes 4 and 5, one function at a time, with approved guidance written before the door opens (Sections 18 and 19).

**The first quarter: review, then widen.**

16. Hold the first quarterly review of the registry: what ran, what was prohibited and whether the GREEN path has earned Tier 2 (Sections 8 and 15).
17. Read the Service Records together; ten of them trigger a method review (Section 20).
18. Only now add a second plugin, and before relying on it run the gap table of Section 21 against its skill files and samples.
19. Reread Section 25. Anything whose status has moved since 1 November 2026 is a reason to recheck the matching instruction, and a reason to tell me.

**When to come back to this guide.** When a screen or a label differs from what Section 25 records; when Anthropic changes the Usage Policy, the privilege guidance or the plans; when a court issues a ruling that changes Section 7; and at every quarterly review. The guide is a dated snapshot; the method underneath it is not.

## 24. Where this guide is weakest

1. **Drift.** Every product fact here is dated 1 November 2026. The announcement named six artifacts and the gallery listed more than fifteen four days later. Labels, commands and fields will change; Section 25 is the instrument for knowing when.
2. **Team not observed.** The gallery was seen on a Max account. Team availability rests on the help center's feature table and one practitioner's report of testing on Max and Team, stated as such in Section 13.
3. **The Word sidebar untested.** Recipe 2's single-contract path rests on the repository's statement that contract-touching skills are authored for the Claude for Word sidebar with tracked changes. I did not run it.
4. **The tiers are mine.** Anthropic has no tiers. The assignment of NDA triage's GREEN path to Tier 3 and the front door's routing to Tier 2 is the author's judgment under the method. A function may set stricter tiers in its registry, never looser ones for Tier 3 work.
5. **United States assumptions.** Rule 11, ABA Formal Opinion 512, federal reporters and CourtListener are American. The method is not; the recipes' tests are. A reader in another jurisdiction replaces the citator, the certification rule and the bar opinion and keeps the gates.
6. **Policies are not controls.** Section 21 says it: the product's gates are instructions a model follows. I did not test how often it fails to. The method assumes it sometimes will.
7. **Repository age.** The plugin repository's default branch was last changed on 23 July 2026. The plugin facts here are three months older than the artifact facts, and a plugin release could move any of them.
8. **One plugin worked.** Eleven plugins are named and not worked. Their skill files are open and the gap table applies, but nothing here says how well they run.
9. **One day's product.** The gap table's third column may shorten as the vendor ships. The second observation of Section 21, that the empty rows are the chef's, will not change with a release.

## 25. Currency register

Every product and legal fact relied on, with its source and the date it was read (KST). Status is as at the edition date.

| Item | Source | Read on | Status |
|---|---|---|---|
| Claude for Legal launched "in May" (the article gives no year; 2026 from its date); artifacts gallery introduced 28 October 2026; "more than 60 legal connectors"; six gallery artifacts named; partner and access-to-justice artifacts; sharing with colleagues, Clients and partners, ethical walls; "Claude completes the first pass, and a lawyer applies their judgment to the results" | Anthropic, *Introducing artifacts for legal work*, 28 October 2026 | 1 November 2026 | current |
| Twelve practice-area plugins, Apache 2.0, cold-start interview (ten to twenty minutes, two-minute quick start), practice profile location, research-connector guardrail and `[verify]` tags, reviewer note on unverified sources, Cowork and Claude Code install steps, user scope, Word sidebar statement, Claude for Microsoft 365 install from AppSource, Reg Feed Watcher, deal-debrief and playbook-monitor agents | anthropics/claude-for-legal, README.md and QUICKSTART.md, default branch at commit 4a6c651 of 23 July 2026 | 1 November 2026 | current; repository unchanged since 23 July 2026 |
| Commercial-legal: sales or purchasing side and what it flips, `--side purchasing`, five to ten agreements (twenty clearer), customer assumed in most reviews, deal-debrief weekly on Monday, playbook-monitor at five or more overrides in a rolling twelve months after each debrief, `/commercial-legal:review-proposals`, stakeholder-summary, "GREEN means route to signature. It does not negotiate." | anthropics/claude-for-legal, commercial-legal/README.md and agents/ | 1 November 2026 | current |
| Practice profile structure and field names, reviewer note fields, decision posture, tag vocabulary, destination check, dual severity | anthropics/claude-for-legal, commercial-legal/CLAUDE.md | 1 November 2026 | current |
| NDA triage labels, `NDA triage positions`, no default positions, scope check and automatic YELLOW, checks, outputs, redline granularity, the non-lawyer gate before signature, jurisdiction flag | anthropics/claude-for-legal, commercial-legal/skills/nda-review/SKILL.md | 1 November 2026 | current |
| Regulatory-legal: reg-change-monitor agent, materiality threshold, weekly default | anthropics/claude-for-legal, regulatory-legal/README.md and agents/reg-change-monitor.md | 1 November 2026 | current |
| No training by default on Team and Enterprise; Enterprise admins set retention; Word and Outlook with tracked changes | claude.com/solutions/legal | 1 November 2026 | current |
| Retention, zero data retention, governed store for the most capable models, in-tenancy and safety monitoring, human review, Access Transparency, *Heppner* reading, the four later decisions, the four suggestions, "baseline expectation for legal technology", email and cloud analogy | Anthropic help center, *Using Claude for Legal Work: Privilege, Confidentiality, and How to Think About Configuration*, 26 August 2026 | 1 November 2026 | current; the article speaks as at June 2026 |
| Legal artifacts gallery: Anthropic and Partners sections, more than fifteen Anthropic artifacts, Try it view-only sample ("Sample data", "Content is user-generated and unverified.", "View only"), Make it yours; Cite check description, "31 citations. 7 need a reviewer.", flags and decisions; Regulatory horizon scan description, impact rating and next key date; Ask legal description, views, tabs, filters, tags, the Sensitive item, Guidance fields, "Colleagues see only what you approve.", "14% answered without a lawyer"; Playbook deviation board description; Tabular review's Mark checked control | The author's Claude account, Max plan, claude.ai/artifacts?templates=legal | 1 November 2026 | observed |
| Artifacts on Free, Pro, Max, Ultra, Team and Enterprise; connected apps in artifacts on Pro and above; Motion on Team and Enterprise; artifact capabilities under Organization settings, Capabilities; artifacts stay inside the organization on Team and Enterprise; viewers of an artifact made in a chat get the chat's attachments | Anthropic help center, *What are artifacts and how do I use them* and *Publish and share artifacts* | 1 November 2026 | current; pages carry no date |
| Audit logs: Enterprise only; export by Organization Owners and Primary Owners for the past 180 days; no chat titles or content, identifiers only; chat inputs and outputs by Primary Owner data export; audit events in the Compliance API | Anthropic help center, *Access audit logs*, 15 June 2026 | 1 November 2026 | current |
| Compliance API: Enterprise organizations and Claude Platform customers; activity feed events, chat data and file content; audit log events included | Anthropic help center, *Access the Compliance API* | 1 November 2026 | current; page carries no date |
| High-risk Use Case Requirements: listed areas, review and disclosure requirements, exclusions; requirements unchanged, section rewritten | Anthropic, Usage Policy, effective 12 November 2026, and *2026 Usage Policy update*, 8 October 2026 | 1 November 2026 | takes effect 12 November 2026 |
| *United States v. Heppner*, No. 25-cr-00503 (JSR) (S.D.N.Y.), bench ruling 10 February 2026, memorandum opinion 17 February 2026, consumer account, no counsel direction, terms, not at the behest of counsel | McDermott Will & Schulte alert of 19 February 2026 and Anthropic's guidance | 1 November 2026 | reported; opinion not read |
| *Morgan v. V2X, Inc.*, No. 25-cv-01991-SKC-MDB (D. Colo.), order of 30 March 2026 (Doc. 65): protective-order conditions, platform disclosure within ten days, motion granted in part | The order, via CourtListener's RECAP archive | 1 November 2026 | read at source |
| *Warner v. Gilbarco*, *Tate Group Automotive v. Legacy Automotive Capital*, *Assini v. Hayward* | Anthropic's privilege guidance | 1 November 2026 | reported; not read |
| Gallery tested on Max and Team | Stephen Smith, 28 October 2026 | 1 November 2026 | reported |
| Steps, gates, tiers, roles, Tier Application Map, whiteboard test, Service Record within a day, ten Service Records; Cookbook fields and the rule that recipes name capabilities, not models | Slow AI Kitchen v3.3.0, README.md, slow-ai-cookbook.md, service-record.md | 1 November 2026 | current |
| LinkedIn post and nine comments | linkedin.com/feed/update/urn:li:activity:7522632632627716096 | 1 November 2026 | live |

## Questions for discussion

1. Take the gap table in Section 21 to the product your team uses today. Which rows can you fill from observation, and which from the brochure?
2. Your NDA playbook: does it exist as positions, fallbacks and never-accept lines per clause, or does it exist as the memory of the lawyer who negotiates NDAs? Who writes it down, and when?
3. The front door's headline figure is the share answered without a lawyer. What would make that number too high for your function, and who decides?
4. Which of your workflows is Tier 3 under the method, and does the registry say so?
5. If you switched vendors next quarter, what would leave with you? Write the Exit row for your current tool.
6. Where does Final Liability sit for an answer the front door gives to an employee about their own situation, and does your policy say the same thing?

## This guide and the account

The guide reads work that already exists in this account. Each row points to where the argument is carried as an instrument. The full map is [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md).

| In this guide | Where the account carries it |
|---|---|
| Sections 14 to 19: the recipe form, and the rule it breaks once | [*Slow AI Cookbook*](https://github.com/rolldabones/slow-ai-kitchen/blob/main/slow-ai-cookbook.md), the eight fields, the One Sheet and the Starter Edition recipes |
| Sections 5 and 15 to 20: the steps, gates, tiers and roles | [Slow AI Kitchen README](https://github.com/rolldabones/slow-ai-kitchen), the twelve steps, the Tier Application Map and the role tables |
| Sections 15 to 17, 19 and 20: the Service Record | [service-record.md](https://github.com/rolldabones/slow-ai-kitchen/blob/main/service-record.md), the one-page close-out |
| Section 8: the registry entry | [*Law Firm AI Deployment Spec v2*](law-firm-ai-deployment-spec.md), sections 2 to 5, 14 and 16, where first-pass NDA review is the first production workflow and the evidence is preserved before it is asked for |
| Section 8: the Exit row | [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md) for the GRCnext™ primitives (Services, Tolerances, Pipes, Switches, Exits) and [GRCnext-Copilot](https://github.com/rolldabones/GRCnext-Copilot), which scores whether an Exit would execute |
| Section 20: evidence built into the system, and starting inside Legal | [*Slow AI for the Chief Legal Officer*](slow-ai-for-the-chief-legal-officer.md), sections 7 and 11 |
| Section 21: policies and controls | [Slow AI Kitchen README](https://github.com/rolldabones/slow-ai-kitchen), Step 8: a model's review of its own output is not verification; the gate is held by the human Reviewer against something outside the model |
| Section 23: one workflow in thirty days | [08-one-workflow-thirty-days.md](08-one-workflow-thirty-days.md), the engagement template in this pack, and the [Consultant Workbook](https://github.com/rolldabones/slow-ai-kitchen/blob/main/consultant-workbook.md) it draws on |
| Section 25: the currency register | [consultant-workbook.md](https://github.com/rolldabones/slow-ai-kitchen/blob/main/consultant-workbook.md), where sources are cited by name and versions pinned once in a resource register |
| Throughout: the three doctrines | [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md), sections 1 to 3 and 8 |

The Slow AI Kitchen also runs as a guided web application at [kitchen.grcskorea.com](https://kitchen.grcskorea.com/), in English, Korean, Vietnamese and Japanese. The repository is the text of record.

## Source basis and attribution

**Primary sources, read**

- Anthropic, [Claude for legal teams](https://claude.com/solutions/legal), read 1 November 2026.
- Anthropic, [*Introducing artifacts for legal work*](https://claude.com/resources/articles/introducing-artifacts-for-legal-work), 28 October 2026.
- Anthropic, [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal), default branch at commit 4a6c651 (23 July 2026): README.md, QUICKSTART.md, commercial-legal/README.md, commercial-legal/CLAUDE.md, commercial-legal/skills/nda-review/SKILL.md, commercial-legal/agents/deal-debrief.md and playbook-monitor.md, regulatory-legal/README.md and regulatory-legal/agents/reg-change-monitor.md, read 1 November 2026. Apache License 2.0.
- Anthropic help center, [*Using Claude for Legal Work: Privilege, Confidentiality, and How to Think About Configuration*](https://support.claude.com/en/articles/15707726-using-claude-for-legal-work-privilege-confidentiality-and-how-to-think-about-configuration), 26 August 2026.
- Anthropic help center, [*Access audit logs*](https://support.claude.com/en/articles/9970975-access-audit-logs), 15 June 2026, and [*Access the Compliance API*](https://support.claude.com/en/articles/13015708-access-the-compliance-api), read 1 November 2026.
- Anthropic help center, [*What are artifacts and how do I use them*](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them) and [*Publish and share artifacts*](https://support.claude.com/en/articles/9547008-publish-and-share-artifacts), read 1 November 2026.
- Anthropic, [Usage Policy](https://www.anthropic.com/legal/aup), version effective 12 November 2026, and [*2026 Usage Policy update*](https://www.anthropic.com/news/2026-usage-policy-update), 8 October 2026.
- *Morgan v. V2X, Inc.*, No. 25-cv-01991-SKC-MDB (D. Colo. Mar. 30, 2026), [order on the motion to amend the stipulated protective order, granted in part](https://storage.courtlistener.com/recap/gov.uscourts.cod.245077/gov.uscourts.cod.245077.65.0.pdf), Magistrate Judge Maritza Dominguez Braswell, via CourtListener.
- The legal artifacts gallery at [claude.ai/artifacts?templates=legal](https://claude.ai/artifacts?templates=legal), including the Ask legal, Cite check, Regulatory horizon scan and Playbook deviation board samples, read in the author's account on 1 November 2026.

**Secondary sources, read**

- *United States v. Heppner*, No. 25-cr-00503 (JSR) (S.D.N.Y. Feb. 17, 2026), as reported in McDermott Will & Schulte, [*Using AI without waiving privilege: Lessons from United States v. Heppner*](https://www.mcdermottlaw.com/insights/using-ai-without-waiving-privilege-lessons-from-heppner/), 19 February 2026, and in Anthropic's guidance. The opinion itself was not read.
- Justin Smith, Everlaw, [*Morgan v. V2X, Inc. Decision Sets Precedent on AI Disclosure in Discovery*](https://everlaw.com/blog/ai-and-law/morgan-v-v2x-ai-disclosure-in-discovery), 2 April 2026, read before the order.
- Stephen Smith, [*Claude's new legal artifacts put ready-made tools in front of your whole firm*](https://www.smithstephen.com/p/claudes-new-legal-artifacts-put-ready), 28 October 2026, for the report that the gallery worked on Max and Team plans.
- Slow AI Kitchen v3.3.0, [README.md](https://github.com/rolldabones/slow-ai-kitchen), [slow-ai-cookbook.md](https://github.com/rolldabones/slow-ai-kitchen/blob/main/slow-ai-cookbook.md) and [service-record.md](https://github.com/rolldabones/slow-ai-kitchen/blob/main/service-record.md), for the steps, gates, tiers, roles, recipe fields and the Service Record; and in this pack, [*Law Firm AI Deployment Spec v2*](law-firm-ai-deployment-spec.md), section 0, for the billing code.

**Stated from standard reference knowledge and not re-verified:** *Mata v. Avianca, Inc.* (S.D.N.Y. 2023), the sanctions order on fabricated citations; ABA Formal Opinion 512 (July 2024) on generative AI tools; Federal Rule of Civil Procedure 11(b) on the certification a signing attorney gives; the general description of Claude, its apps and plan names in Sections 2 and 3, beyond what the cited pages state.

**Considered and left out:** the partner-built artifacts in the gallery (Harvey Intake, Foley & Lardner's Obligations Checker, PwC's Subpoena Response Tool, Goodwin's AI Governance Benchmark, a Wilson Sonsini venture term sheet benchmark and the access-to-justice tools), none run; the eleven plugins other than commercial-legal, read in the README's tables and, for regulatory-legal, its own README only; the five Managed Agent cookbooks; the Tabular review, Jurisdiction survey matrix and Matter board artifacts, seen in the gallery and not worked as recipes; connectors other than research, not tested; pricing, seat counts and usage limits, which change too often to record here.

---

*This document is provided for general informational and discussion purposes regarding the governance and use of AI. It does not constitute legal advice with respect to any specific matter, jurisdiction or engagement. It describes a vendor's product as read on one day and is not a statement of the vendor's positions.*

**Final Liability rests with the Human.**
