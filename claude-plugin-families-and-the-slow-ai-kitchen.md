# Claude's Plugin Families and The Slow AI Kitchen

**A beginner's field map: the industry verticals, the job-function plugins and the people at the center of each**

Son-U Michael Paik · CEO, GRC Solutions Korea

15 November 2026

*GRC Solutions Korea is not affiliated with Anthropic, and Anthropic has not reviewed or endorsed this map. Claude and the "Claude for" names are Anthropic's product names, used here to refer to the products.*

> AI is a tool in the kitchen, not the chef.
>
> Slow AI Kitchen, masthead

**Starting point.** On 12 November 2026 Anthropic launched Claude for Manufacturing, a plugin for plant teams. It joined a shelf that already held plugins for legal, finance, sales, healthcare, human resources and a dozen other kinds of work. This map lists that shelf in one place, as it stood on 15 November 2026 (Korea Standard Time, KST): every industry vertical Anthropic names and every job-function plugin it publishes, each with a link, what it contains and what its own maker says about human review. It then makes one proposal. Every one of these plugins is a stocked kitchen, and none of them is a chef. The [Slow AI Kitchen](https://github.com/rolldabones/slow-ai-kitchen), a twelve-step method for using AI on work that matters, is how an organization puts its people in charge of all of them, with the same discipline for each.

**For:** anyone deciding whether to turn one of these plugins on: an owner, a department head, a team lead or the person who will use it on Monday. No prior knowledge of Claude or of the method is assumed. Section 2 explains the words. A reader who wants one family worked from purchase to first quarterly review should go on to [*Using Claude for Legal with The Slow AI Kitchen*](using-claude-for-legal-with-the-slow-ai-kitchen.md), which does that for the legal plugins. This map is the wide view and that guide is the deep one. A reader asking what this shelf does to the organization itself, to its departments and its headcount, should read the companion piece, [*The Core and the Capability*](the-core-and-the-capability.md). A reader with ten minutes reads Sections 1, 6 and 7 and then finds their own family in Section 4 or 5.

**What this map adds.** One inventory, one table that sets the twelve steps beside any plugin and one page on artifacts (Section 11). It adds no doctrine, step, gate, tier or form. The method is vendor-neutral by design; like the legal guide, this map names one vendor on purpose, to show that the method survives contact with a real product line. Section 9 says how to run the same reading against any other vendor.

**Edition and durability.** First edition. The product facts are a snapshot of 15 November 2026 (Korea Standard Time, KST) and they move weekly: the manufacturing plugin was three days old when this was written. Section 13 lists every product fact relied on, with its source and the date it was read. If a screen you see differs from what is described here, the screen wins; tell me.

**A declared interest and a method note.** This map was prepared with Claude, a model made by Anthropic, and it concerns Anthropic's products. Anthropic had no part in it. The plugin repositories were read file by file from copies taken at the commits named in Section 13. Anthropic's product pages were opened in a browser on 15 November 2026; Section 13 says, page by page, which were read in full and which only for the statements relied on. Where a page was not read in full, this map says "the parts of the page read". No plugin was installed or run: the map reports what the published files and pages say, not how well anything works. One source is a securities filing; nothing here is a view on any offering of securities.

## Contents

1. [The short version](#1-the-short-version)
2. [Words you will meet](#2-words-you-will-meet)
3. [How the shelf is organized](#3-how-the-shelf-is-organized)
4. [The industry and sector families](#4-the-industry-and-sector-families)
5. [The job-function plugins](#5-the-job-function-plugins)
6. [What every family says about itself](#6-what-every-family-says-about-itself)
7. [The proposal: people first, then the plugin](#7-the-proposal-people-first-then-the-plugin)
8. [The twelve steps beside any plugin](#8-the-twelve-steps-beside-any-plugin)
9. [Policies are not controls](#9-policies-are-not-controls)
10. [Where to start](#10-where-to-start)
11. [A note on artifacts](#11-a-note-on-artifacts)
12. [Where this map is weakest](#12-where-this-map-is-weakest)
13. [Currency register](#13-currency-register)

- [Questions for discussion](#questions-for-discussion)
- [This map and the account](#this-map-and-the-account)
- [Source basis and attribution](#source-basis-and-attribution)

## 1. The short version

1. A plugin is a package of written instructions and system connections that makes Claude work like a specialist in one job or one industry. Anthropic publishes them in families.
2. There are two kinds of family. **Industry and sector families** are built for a sector: financial services, financial advisors, healthcare, life sciences, legal and manufacturing, with two more for small businesses and nonprofits. **Job-function plugins** are built for a role found in most organizations: sales, finance, human resources, engineering and so on.
3. Two things that carry a "Claude for" name are not plugins at all: Claude for Education is a plan for institutions and teachers, and Claude for Government is a separately authorized environment. They are listed here so that nobody goes looking for a plugin that does not exist.
4. Nearly every family says the same thing about itself in its own words: the plugin drafts and a person reviews, decides and answers. That sentence tells you where responsibility lies. It does not tell you how to carry it.
5. The Slow AI Kitchen is the how. The human steps come first: name the owner, define done, do a first pass by hand, read who is affected. Then the plugin is used. Then a person tests the result and a person releases it. The same twelve steps apply to every plugin on the shelf, which is why an organization needs to learn them only once.

## 2. Words you will meet

| Word | What it means here |
|---|---|
| Claude | Anthropic's AI assistant, used through a web app, desktop and mobile apps and add-ins for office software. |
| Plugin | A package that bundles skills, connectors and sometimes agents for one kind of work. Installing it changes how Claude works for you; it is not a new model and not a separate app. |
| Skill | A set of written instructions, in a plain-text file, that tells Claude how to do one task, such as drafting a quote or triaging a support ticket. |
| Connector | A link between Claude and another system, such as a customer database, an accounting package or a document store, built on the Model Context Protocol (MCP), an open standard. Once connected, Claude can read from that system and, where allowed, write to it. |
| Agent | A set of instructions that runs a whole workflow from start to finish, sometimes on a timetable and not only when asked. |
| Slash command | A command typed into Claude's message box beginning with a slash, such as `/sales:call-prep`. It runs the skill of that name. |
| Marketplace | A catalog of plugins that can be added to Claude. Anthropic curates several; an organization can also run its own. |
| Vertical solution | Anthropic's term for an offering aimed at one industry. Some are plugins, some are plans and one is a separate environment. |
| Plan | What you or your organization has bought. Pro, Max and Ultra are individual plans; Team and Enterprise are sold to organizations. |
| Cowork | The part of the Claude apps built for longer, multi-step work. Most of these plugins were written for it. |
| Claude Code | Anthropic's tool for developers, run from a terminal. Most of these plugins also install there. |
| Artifact | A document, sheet, deck, dashboard or small tool that Claude makes and that can be kept, edited and shared. Section 11. |
| Step, gate, tier | The Slow AI Kitchen's units. A step is one of twelve stages of the work; a gate is a checkpoint the work must pass; a tier sets how deep each gate goes for a task of given stakes. Section 8. |
| Owner | The method's word for the named human who answers for a piece of work. The Owner is never the AI. |
| AOTL | Ass on the line: the author's plain-speech way of saying Final Liability. It asks whose name is on the line before the work runs. Section 7. |

## 3. How the shelf is organized

**What a plugin is made of.** Anthropic's help center describes a plugin as a bundle of skills, connectors and sub-agents in one package. In the published repositories every part is a plain-text file: instructions in Markdown and settings in JSON. That matters for two reasons that return later in this map. Anyone can read what the plugin tells Claude to do, and anyone in the organization with permission can change it.

**Where plugins are found.** In the Claude apps, the help center gives the path as the Customize menu, then Plugins, then Discover. Anthropic curates four marketplaces that can be added there: Knowledge Work, which is added by default, and Life Sciences, Financial Services and Legal. A public directory is at [claude.com/plugins](https://claude.com/plugins); on 15 November 2026 it showed 531 plugins, most of them built by other companies and many of them for software developers. This map covers only the families Anthropic itself builds or names as a solution.

**Who can use them.** The help center says plugins are available on all paid plans. Individual offerings narrow that: the manufacturing launch article says Team or Enterprise, and the healthcare page says Enterprise and the developer platform. Check the page for the family you want.

**What an organization can control.** On Team and Enterprise plans, the help center says owners decide whether colleagues may share plugins and publish them to the organization's library, and that a published plugin can be offered as available, installed by default or required. On Enterprise plans it adds that an administrator may restrict which plugins can be installed and may have plugins scanned for malicious content. Those settings are the organization's real controls over this shelf. Section 9 explains why the distinction matters.

**How Anthropic counts.** A prospectus Anthropic filed in November 2026 says the company has launched seven vertical solutions and names them: Claude for Financial Services, Financial Advisors, Healthcare, Life Sciences, Legal, Education and Government. Manufacturing, launched two days after that text was filed, would be the eighth. Small business and nonprofits have plugins and product pages of their own and are not on the filing's list. This map follows the products, not the count.

## 4. The industry and sector families

Each entry gives what the offering is, where to find it, what it contains and what its maker says about review. "Repository" means Anthropic's public file store on GitHub, where the instruction files can be read. The whole section on one screen:

| Family | Form | Size, as read | Instruction files public? |
|---|---|---|---|
| 4.1 Financial Services | Plugins | 10 agents, 6 skill bundles, 2 partner plugins | Yes |
| 4.2 Financial Advisors | Plugin | 8 skills | Yes |
| 4.3 Healthcare | Plugin | 10 skills | Yes |
| 4.4 Life Sciences | Skills marketplace and a plugin | 4 skills and 6 skills | Yes |
| 4.5 Legal | Plugins and an artifact gallery | 12 plugins, 1 partner plugin | Yes |
| 4.6 Manufacturing | Plugin | 17 skills, 4 connectors | Not found |
| 4.7 Small Business | Plugin | 44 skills | Yes |
| 4.8 Nonprofits | Plan with a plugin | Unknown | Not found |
| 4.9 Education and Government | Plans and an environment | No plugin | Not applicable |

### 4.1 Claude for Financial Services

- **What it is:** agents, skills and data connectors for investment banking, equity research, private equity, fund administration and onboarding operations.
- **Where:** [product page](https://claude.com/solutions/financial-services) · [repository](https://github.com/anthropics/financial-services) (Apache 2.0 license). The Financial Services marketplace in the Claude apps.
- **What it contains,** as read in the repository:

| Kind | Name | What it does, in the repository's description |
|---|---|---|
| Agent | Pitch Agent | Comparable companies, precedents and a buyout model through to a branded pitch deck |
| Agent | Meeting Prep Agent | A briefing pack before each Client meeting |
| Agent | Market Researcher | A sector or theme turned into an industry overview, competitive landscape, peer comparison and ideas shortlist |
| Agent | Earnings Reviewer | An earnings call and filings turned into a model update and a draft note |
| Agent | Model Builder | Valuation and three-statement models in Excel |
| Agent | Valuation Reviewer | Takes in general partner packages, runs a valuation template and stages investor reporting |
| Agent | GL Reconciler | Finds reconciliation breaks, traces the cause and routes for sign-off |
| Agent | Month-End Closer | Accruals, roll-forwards and variance commentary |
| Agent | Statement Auditor | Audits investor statements before they are distributed |
| Agent | KYC Screener | Reads onboarding documents, runs a rules engine and flags gaps |
| Skill bundle | financial-analysis | The core: 13 skills for valuation models, comparables, deck checks and spreadsheet audit, plus the shared data connectors |
| Skill bundle | investment-banking | 9 skills: information memoranda, teasers, process letters, buyer lists, merger models, deal tracking |
| Skill bundle | equity-research | 9 skills: earnings notes, initiations, model updates, thesis and catalyst tracking |
| Skill bundle | private-equity | 10 skills: sourcing, screening, diligence checklists, investment committee memos, portfolio monitoring |
| Skill bundle | fund-admin | 6 skills: ledger reconciliation, break tracing, accruals, roll-forwards, net asset value tie-out |
| Skill bundle | operations | 2 skills: know-your-customer document reading and rules evaluation |
| Partner plugin | LSEG | Bond, rates, currency and options analysis on LSEG data |
| Partner plugin | S&P Global | Company tear sheets, earnings previews and funding digests on S&P Capital IQ data |

- **Connectors named in the core bundle:** Aiera, Box, Chronograph, Daloopa, Egnyte, FactSet, LSEG, Moody's, Morningstar, MT Newswires, PitchBook and S&P Global.
- **What its maker says about review:** the repository states that the agents draft analyst work product for review by a qualified professional, that they do not make investment recommendations, execute transactions, post to a ledger or approve onboarding, and that "every output is staged for human sign-off."

### 4.2 Claude for Financial Advisors

- **What it is:** a plugin for advisory practices, with emphasis on independent registered investment advisers.
- **Where:** [product page](https://claude.com/solutions/financial-advisors) · [repository](https://github.com/anthropics/claude-for-financial-advisors) (Apache 2.0 license). The Knowledge Work marketplace lists it under the name claude-for-financial-advisors.
- **The eight skills,** as the repository names them:

| Skill | What it does, shortened from the repository's description |
|---|---|
| onboarding | First-run setup: learns the firm, its priorities and its systems, connects the tools and runs a sample |
| pre-meeting | A Client review preparation document: snapshot, open items, portfolio review, planning topics, agenda |
| post-meeting | Turns a meeting record or transcript into a note for the Client record system |
| compliance | A pre-check of Client-facing material against United States adviser marketing and conduct rules, with findings and a redraft |
| prospect-intake | Turns a prospect's statements into a summary, an analyst handoff and a what-to-expect memo |
| portfolio-rebalance-review | Reviews performance and drift and drafts a rebalance plan for the advisor to evaluate, with a memo of the advisor's reasons |
| alts-brief | A meeting-ready read on a household's alternative investments |
| estate-and-tax-brief | Cross-checks the estate plan against account titling and beneficiaries, with a prior-year tax look-back |

- **Connectors named on the product page:** Addepar, BlackRock, Charles Schwab, Envestnet, iCapital, Orion, SS&C Black Diamond, Vanguard, Wealthbox, Wealth.com and Zocks, and it says the plugin also works with Microsoft 365, Salesforce, Docusign and Box. The repository lists more.
- **What its maker says about review:** the repository says the plugin holds no Client data, that every write to a Client system pauses for the advisor's approval and that the plugin is not investment, legal or tax advice. The product page adds that Claude does not place trades or move money, that review steps and audit trails are built in and that it recommends the Enterprise plan for registered investment advisers because that plan includes audit logs.

### 4.3 Claude for Healthcare

- **What it is:** one plugin for payer, provider and pharmaceutical work.
- **Where:** [product page](https://claude.com/solutions/healthcare) · [repository](https://github.com/anthropics/healthcare). The repository says it is provided under Anthropic's terms of service, not an open-source license.
- **The ten skills,** as the repository names them:

| Skill | What it does, in the repository's description |
|---|---|
| clinical-note-extract | Structured data from clinical notes, with the source passage recorded for each item |
| clinical-trial-protocol | Draft clinical trial protocols for devices or drugs |
| contracts | Answers a question across a set of contracts with verified citations |
| doc-extract | Plain text from PDF, Word, Excel, PowerPoint and similar files |
| fhir | Connects to a hospital's records server, pulls a patient's data and notes and extracts findings |
| fhir-developer | A development guide for building healthcare data endpoints |
| fraud-detection | Screens claims for fraud, waste and abuse and produces cited referrals for an investigations team |
| icd10-cm | Diagnosis codes from a clinical note |
| prior-auth | Payer review of prior authorization requests |
| procedure-coding | Procedure codes from clinical documentation |

- **Connected data sources:** the CMS Coverage database, ICD-10 codes, the NPI Registry, clinical trials data and PubMed, hosted by Anthropic, with a contracts analyzer and a records connector bundled in the plugin.
- **What its maker says about review:** the product page describes answers traced to their source and drafts ready for review. The prior authorization skill's own README is more direct: it says the skill produces draft recommendations only and that "No decision is finalized without human action." Section 9 returns to this skill, because its files say something else as well.
- **Access:** the product page says healthcare customers reach Claude through the Enterprise plan and the developer platform, on infrastructure it describes as ready for HIPAA, the United States health privacy law. This map makes no statement about what a given organization's obligations under that law are.

### 4.4 Claude for Life Sciences

- **What it is:** tools for research and regulatory teams, from analysis of laboratory data to protocol drafts.
- **Where:** [product page](https://claude.com/solutions/life-sciences) · [repository](https://github.com/anthropics/life-sciences), a marketplace of skills · the bio-research plugin in the [Knowledge Work repository](https://github.com/anthropics/knowledge-work-plugins).
- **The four skills in the life sciences marketplace:**

| Skill | What it does, in the repository's description |
|---|---|
| Clinical Trial Protocol | Draft clinical trial protocols for devices or drugs |
| Scientific Problem Selection | A framework for choosing research problems, assessing project risk and planning |
| Clinical Trial Forecast | An estimate of the probability that a registered trial meets its goal, with a cited report and the model behind the number |
| Binder Gauntlet | Checks of computationally designed protein binders, with a dossier that states what was not checked |

- **The bio-research plugin:** 6 skills for early-stage research, with connectors to PubMed, bioRxiv, ClinicalTrials.gov, ChEMBL, Open Targets, Benchling, BioRender, Synapse, Wiley, Owkin and Consensus.
- **What its maker says about review:** the product page says Claude is designed with verification in mind and describes protocol drafting with regulatory cross-referencing built in. The parts of the page read set out no review step. In the repository, the Binder Gauntlet entry says all its results are computational predictions.
- **One thing to know:** the life sciences repository says it was refocused on skills and no longer carries connector plugins, and it names four skills it removed. Those four are still present in the bio-research plugin in the other repository. Older write-ups that list more, or fewer, may be describing a different day.

### 4.5 Claude for Legal

- **What it is:** twelve practice-area plugins, a partner plugin, connectors to the systems legal teams use and a gallery of ready-made legal artifacts.
- **Where:** [product page](https://claude.com/solutions/legal) · [repository](https://github.com/anthropics/claude-for-legal) (Apache 2.0 license). The Legal marketplace in the Claude apps.
- **The twelve plugins,** with the number of skills and scheduled agents in each as read in the repository:

| Plugin | Skills | Agents | What it does, shortened from the repository's description |
|---|---|---|---|
| commercial-legal | 12 | 3 | Reviews vendor agreements and NDAs against your playbook, tracks renewals, routes escalations |
| corporate-legal | 13 | 1 | Diligence review in tables with citations, disclosure schedules, board consents, entity compliance deadlines |
| employment-legal | 20 | 1 | Reviews hires and terminations for risk flags, classifies workers, tracks leave, runs investigations, drafts policies |
| privacy-legal | 9 | 0 | Triage of processing activities, privacy impact assessments, data processing agreement review, data subject request responses |
| product-legal | 7 | 1 | Launch reviews against your risk settings, marketing claims checks, quick answers on product questions |
| regulatory-legal | 9 | 1 | Watches regulatory feeds, compares new rules with your policies, tracks comment deadlines and gaps |
| ai-governance-legal | 10 | 0 | Triage of proposed AI uses against your registry, impact assessments, review of vendor AI terms, AI policy upkeep |
| ip-legal | 12 | 1 | First-pass trademark clearance, patent screening, takedown and cease-and-desist drafting, open source checks, renewal tracking |
| litigation-legal | 19 | 1 | The matter portfolio, deadlines and holds, plus claim charts, chronologies, deposition preparation and privilege logs |
| legal-clinic | 16 | 0 | Runs a law school clinic: intake, deadlines, supervision queue and end-of-semester handover |
| law-student | 13 | 0 | Drills, case briefs, outlines and practice grading that coach the student and do not write the work |
| legal-builder-hub | 10 | 1 | Finds and installs community legal skills, with a security review before anything is installed |

- **Partner plugin:** CoCounsel Legal, for research reports with citations into Westlaw.
- **What its maker says about review:** the repository says "Every output from these plugins is a draft for attorney review" and that the attorney using a plugin, not the plugin and not Anthropic, is responsible for the legal positions taken.
- **Worked in full:** [*Using Claude for Legal with The Slow AI Kitchen*](using-claude-for-legal-with-the-slow-ai-kitchen.md).

### 4.6 Claude for Manufacturing

- **What it is:** a plugin for plant teams, launched 12 November 2026, with 17 skills and four connectors. It drafts quotes, quality reports, production reports and supplier requests from a manufacturer's own records.
- **Where:** [product page](https://claude.com/solutions/manufacturing) · [launch article](https://claude.com/resources/articles/claude-for-manufacturing). No public repository for this plugin was found, so its instruction files were not read; whether one exists is Unknown.
- **What it contains:** the launch article says the 17 skills cover sales, quality, operations, supply chain, design and setup, and names six processes, not all seventeen skills:

| Process | Who asks | What Claude drafts |
|---|---|---|
| Quoting a new job | Estimator | Reads the request, lists what is missing, compares similar jobs, drafts the quote |
| Investigating a failed inspection | Quality engineer | Documents the failure, checks past reports, ranks likely causes, drafts the corrective action report |
| Diagnosing a breakdown | Technician | Reads sensor exports, repair notes, photos and the manual, ranks likely causes to check |
| Sourcing from another supplier | Buyer | Prepares the request for quotes and compares the bids |
| Comparing designs | Engineer | Generates variations from an existing model, scores them and drafts a decision memo |
| Reporting on production | Plant manager | One report of output against target, downtime and its cost |

- **Connectors:** Autodesk Fusion, Infor, Microsoft 365 and Oracle NetSuite. Systems without a connector can be used through regular exports saved to Microsoft 365.
- **What its maker says about review:** the launch article says skills are built to end with a user's review and states "Claude for Manufacturing doesn’t operate equipment." The product page adds that Claude does not run production control or write to the manufacturer's systems of record, and that on Team and Enterprise plans owners can require approval before a connector changes anything, or block changes.
- **Where it fits:** the product page says the plugin fits best where each job has its own quote, drawing and routing, and that process manufacturers in food, consumer goods, chemicals and steel can use the production report, breakdown diagnosis and supplier skills at once and adapt the rest.
- **Two things to know.** First, the article says the plugin's Infor connector looks records up, and that a separate plugin from Infor lets Claude make changes in Infor once the user approves. An organization that installs both has a different risk from one that installs the first alone. Second, the article says Team or Enterprise plans; the product page says paid plans, with installation by an administrator. Check before you buy.

### 4.7 Claude for Small Business

- **What it is:** ready-made workflows for an owner-run business: bookkeeping, bills, payroll preparation, lead follow-up, proposals, marketing and customer service.
- **Where:** [product page](https://claude.com/solutions/small-business) · the small-business plugin in the [Knowledge Work repository](https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business).
- **What it contains:** 44 skills in the repository, among them cash-flow-snapshot, invoice-chase, pay-the-bills, payroll-prep, close-month, tax-prep, lead-triage, proposal-builder, hiring-screener, inventory-planner, contract-review and ticket-deflector. Its connector list runs to more than thirty systems, including QuickBooks, Xero, Stripe, Square, Shopify, Gusto, HubSpot and Canva.
- **What its maker says about review:** the plugin's own description says "You approve every step that touches money or customers." The product page says Claude shows its plan before it acts, that by default nothing is sent or paid without the owner's agreement and that payroll is prepared for the owner to submit.

### 4.8 Claude for Nonprofits

- **What it is:** a plan for verified nonprofit organizations that comes with a plugin for nonprofit work already installed.
- **Where:** [product page](https://claude.com/solutions/nonprofits). No public repository for this plugin was found, so its instruction files were not read.
- **What it contains:** the page describes the plugin as a set of skills and connectors built with about thirty nonprofits, links a fundraising tutorial and names Salesforce and nonprofit-specific connectors such as Blackbaud. The number and names of its skills are Unknown from the parts of the page read.
- **What its maker says about review:** the parts of the page read set out no review step.

### 4.9 Two names that are not plugins

**Claude for Education.** Anthropic's filing counts it among the seven verticals. The [higher education page](https://claude.com/solutions/education) describes a plan for a whole university, with a learning mode that asks guiding questions. The [K-12 teachers page](https://claude.com/solutions/teachers) describes free access for verified teachers in the United States, with teaching skills and connectors to curriculum sources. Neither page describes a plugin.

**Claude for Government.** Also counted among the seven. The [government page](https://claude.com/solutions/government) describes a separate environment for federal, state and local agencies in the United States, authorized at the FedRAMP High level. The parts of the page read describe no plugin.

**A related page.** Anthropic also has a [cybersecurity page](https://claude.com/solutions/cybersecurity). It names no plugin and is outside this map.

## 5. The job-function plugins

These seventeen plugins are in Anthropic's [Knowledge Work repository](https://github.com/anthropics/knowledge-work-plugins) (Apache 2.0 license) and in the Knowledge Work marketplace, which the help center says is added to Claude by default. The repository's opening page still speaks of eleven; seventeen folders built by Anthropic were present on the day it was read. Each links to its folder. The last column is this map's, not Anthropic's: it names the kind of decision that, under the Slow AI Kitchen, stays with a named person.

| Plugin | Skills | What it does, shortened from the repository's description | The decision that stays with a named person |
|---|---|---|---|
| [productivity](https://github.com/anthropics/knowledge-work-plugins/tree/main/productivity) | 4 | Tasks, daily planning and a memory of your working context, synced with calendar, email and chat | What you commit to and what you decline |
| [sales](https://github.com/anthropics/knowledge-work-plugins/tree/main/sales) | 36 | Call preparation, follow-up, account research, deal and pipeline reviews and the forecast; on request it can update customer records, send email and book meetings | What is promised to a customer, and the forecast that goes up the line |
| [customer-support](https://github.com/anthropics/knowledge-work-plugins/tree/main/customer-support) | 5 | Ticket triage, draft responses, escalations and knowledge base articles | What a customer is told, and any refund, credit or exception |
| [product-management](https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management) | 8 | Feature specifications, roadmaps, research synthesis and stakeholder updates | What gets built and what gets cut |
| [marketing](https://github.com/anthropics/knowledge-work-plugins/tree/main/marketing) | 8 | Content, campaign plans, brand review, email sequences and performance reports | Every public claim made in the organization's name |
| [legal](https://github.com/anthropics/knowledge-work-plugins/tree/main/legal) | 9 | Contract review, NDA triage, compliance checks and risk assessment for in-house teams | The legal position, and whether a contract is signed |
| [finance](https://github.com/anthropics/knowledge-work-plugins/tree/main/finance) | 8 | Journal entries, reconciliation, financial statements, variance analysis, close and audit support | What is posted to the books, and the sign-off on the close |
| [data](https://github.com/anthropics/knowledge-work-plugins/tree/main/data) | 10 | Database queries, statistical analysis, charts and dashboards | What the number means, and whether it is fit to be relied on |
| [enterprise-search](https://github.com/anthropics/knowledge-work-plugins/tree/main/enterprise-search) | 5 | One search across email, chat, documents and wikis | Who is allowed to see what the search can reach |
| [bio-research](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research) | 6 | Literature search, genomics analysis and target prioritization for early-stage research | Which experiment is run and which result is reported |
| [human-resources](https://github.com/anthropics/knowledge-work-plugins/tree/main/human-resources) | 9 | Recruiting, offers, onboarding, performance reviews, compensation analysis and policy answers | Every decision about a person: hire, pay, rating, exit |
| [engineering](https://github.com/anthropics/knowledge-work-plugins/tree/main/engineering) | 10 | Stand-ups, code review, architecture decisions, incident response and documentation | What is merged and deployed, and the call during an incident |
| [design](https://github.com/anthropics/knowledge-work-plugins/tree/main/design) | 7 | Design critique, design systems, interface wording, accessibility review and handoff | What ships to users, and whether it is accessible |
| [operations](https://github.com/anthropics/knowledge-work-plugins/tree/main/operations) | 9 | Vendor reviews, process documents, change requests, capacity plans, runbooks and compliance tracking | Vendor selection, and approval of a change to a live process |
| [small-business](https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business) | 44 | The owner's workflows; see Section 4.7 | Anything that moves money or reaches a customer |
| [pdf-viewer](https://github.com/anthropics/knowledge-work-plugins/tree/main/pdf-viewer) | 1 | View, annotate, fill and sign PDF files | The signature |
| [cowork-plugin-management](https://github.com/anthropics/knowledge-work-plugins/tree/main/cowork-plugin-management) | 2 | Create a new plugin or customize an existing one for your organization | What the organization's own plugins tell Claude to do |

**Partner-built plugins.** Five sit in the same repository: Apollo and Common Room for sales work, Brand Voice for brand guidelines, a Slack plugin and a Zoom plugin for developers building on Zoom. The marketplace's own list is much longer: on the day it was read it named 123 plugins, the seventeen above and about a hundred from other companies, most of them kept in those companies' own repositories. They are outside this map, and the method applies to each of them unchanged.

**Legal and finance appear twice, on purpose.** The legal and finance plugins in this table are general ones for an in-house team. The families in Sections 4.1 and 4.5 are the deep versions for banks, funds and legal departments. A small team starts here; a specialist team goes there.

**Customization is the point.** The repository's own page describes these plugins as generic starting points that become useful when an organization puts its own tools, terms and processes into them. Section 7 takes that sentence seriously.

## 6. What every family says about itself

Read the entries in Sections 4 and 5 again for one thing only: what each maker says about review.

- Legal: every output is a draft for attorney review, and the attorney answers for it.
- Financial services: every output is staged for human sign-off.
- Financial advisors: every write to a Client system waits for the advisor's approval.
- Healthcare prior authorization: no decision is final without human action.
- Manufacturing: skills end with a user's review, and the plugin does not operate equipment.
- Small business: the owner approves every step that touches money or customers.

Six families, one sentence. Two entries, life sciences and nonprofits, are missing from the list only because the parts of their pages read do not say it in so many words. The vendor is telling its customers, in public and in writing, that the person stays responsible. That is the right thing for a vendor to say, and it leaves the customer's hardest questions unanswered. Which person? Trained how? Checking against what? With how much time? Recording what? Able to stop the work by what means? A product cannot answer those, because the answers are facts about your organization and not about the product. They are the chef's.

## 7. The proposal: people first, then the plugin

**The order.** My approach to AI in an organization starts with people and ends with technology: Principles, People, Processes, Systems. A plugin is a System that arrives with a Process already inside it, one that Anthropic wrote for a typical team. Install it first and you have skipped two steps and borrowed a third. The proposal of this map is simple: for any plugin on this shelf, do the people's part first.

**The principles, in plain words.** Three doctrines sit under the method, and they are short enough to agree on in one meeting. **Informed Intent**: decide and write down what the tool may do, on whose authority, within what limits and how it is stopped, before it is used. **Slow AI**: do not deploy what you cannot govern, explain and audit. It is a precondition and not a speed limit; the aim is to keep the Human able to follow what the machine is doing. **Final Liability**: a named person answers for every output. The full statements are in [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md).

**AOTL, not HITL.** Most of the review language in Section 6 is a version of "human in the loop" (HITL). I no longer use that phrase. It pictures one person watching one process, and it has nothing to point at once a team runs a dozen plugins across a hundred tasks a day. The phrase I use in its place is AOTL, ass on the line. It is Final Liability in plain speech, and it changes the question. The question is not whether a human sits somewhere in the loop. It is whose name is on the line before the run. A name chosen afterward is not accountability; it is the selection of a scapegoat. So for every plugin on this shelf, ask the AOTL question first: when this quote, this denial, this offer letter or this filing goes out, whose is it? If nobody can answer before the work starts, the plugin is not ready to be used, however good its review steps look.

**The people.** "People at the center" is easy to say. For each plugin it comes down to six people you should be able to name before the first real task is run:

| The person | The question they answer | Where the method names them |
|---|---|---|
| The one who decides what may run | Which plugin, for which work, at what stakes, with which connectors? | AI Owner, Step 10 |
| The one who is trained and authorized | Who may use it, for what, and how do we know they can? | AI Operator, Step 11 |
| The one who frames the work and reads the material first | What is the task, and what did a person see before the machine did? | Preparer, Steps 1 to 3 |
| The one who checks | Does the output pass the tests written before it was made? | Reviewer, Step 8 |
| The one who releases it and answers for it | Does this go out, and who says so? | Owner and Approver, Steps 6 and 9 |
| The one it lands on | Who is affected if this is wrong: the customer, the patient, the employee, the supplier? | Step 4 |

In a small team one person holds several of the first five roles. In every team the Owner is a human, named before the run: that is the AOTL row, and it is the one that cannot be left blank. The sixth person is never in the room, which is why the method makes someone read the setting on their behalf.

**The process.** The plugin's instruction files are plain text, and each family invites you to rewrite them. That is where your organization's own way of working goes in: your playbook, your quoting rules, your escalation path. I hold that a team's own practices, written down and shared, are worth more than any vendor's or industry's version of them. So the people who do the work should write the plugin's local rules, and the plugin should not write theirs. A team that customizes a plugin together has done something useful before the AI has drafted a word: it has said out loud how it works.

**What this means for the person doing the work.** A method that puts people at the center has to be good for them and not only for the organization's risk register. Three commitments follow. The time spent learning the tool and writing the team's rules into it is work and is credited as work. The first pass by hand is kept, because it is how a person stays able to judge the machine's version. And nobody is asked to sign what they did not have time to read: if review time is not in the schedule, the review is not happening, whatever the plugin's documentation says.

## 8. The twelve steps beside any plugin

The Slow AI Kitchen has twelve steps and ten gates. Steps 1 to 9 govern one piece of work, called a dish. Steps 10 to 12, the Feast, govern a tool's use across a team. The table reads the same for every plugin in Sections 4 and 5; only the examples change. The method itself, with its forms, is in the [Slow AI Kitchen README](https://github.com/rolldabones/slow-ai-kitchen).

**Before anyone installs anything**

| Step | Kitchen name | In plain words | With a plugin, a person does this |
|---|---|---|---|
| 10 | Plan the Menu (Gate 8, the tool registry) | Decide what may run | Writes one entry: this plugin, these connectors, this work, this tier, these users, what is prohibited and what leaves with us if we stop using it |
| 11 | Staff the Brigade (Gate 9, competency and authorization) | Decide who may run it | Trains the users, records who is authorized for what and sets a date to look again |

**For each piece of work**

| Step | Kitchen name | In plain words | With a plugin, a person does this |
|---|---|---|---|
| 1 | Define the Dish | Frame the task and name the Owner | Writes two lines: what is wanted and who answers for it |
| 2 | Mise en Place (Gate 1, definition of done) | Say what "done" means before starting | Writes three to seven pass-or-fail tests for this output; one to three will do for low-stakes work |
| 3 | Knife Work (Gate 2, manual first pass) | Look at the material yourself first | Reads the request, the contract, the inspection report or the ledger before the plugin does |
| 4 | Read the Kitchen (Gate 3, context) | Ask who is affected and what follows | Notes who this lands on and what happens if it is wrong, and confirms the tier |
| 5 | Apply Heat (Gate 4, bounded AI use) | Use the AI inside those limits | Runs the plugin on this task, with the connectors the registry allows and no others |
| 6 | Name the Chef de Partie (Gate 5, Final Liability) | Confirm who answers | Confirms the named Owner, the Reviewer and where a problem is escalated |
| 7 | Build the Plate | Assemble the deliverable | Puts the draft into the form it will be used in |
| 8 | Taste Before Service (Gate 6, verification) | Test it against the tests | Checks the draft against the Step 2 tests and against something outside the model: the source record, the drawing, the statute, the bank statement |
| 9 | Open the Pass (Gate 7, release) | A person decides to let it go | Releases it or sends it back, and records which |

**Afterward**

| Step | Kitchen name | In plain words | With a plugin, a person does this |
|---|---|---|---|
| 12 | Run the Event (Gate 10, audit and review) | Keep the record and look back | Keeps enough evidence to reconstruct what happened, handles incidents and reviews the registry entry on a set cycle and whenever the plugin or the model changes |

**Tiers decide the depth, never the presence, of a gate.** Tier 1 is low-stakes internal work. Tier 2 is moderate work under review. Tier 3 is high-stakes work: decisions affecting customers, employees or regulated operations, legal or compliance determinations, statements made to outsiders and any automation tied to action. Much of what these plugins draft is Tier 3 the moment it is released: a quote, a denial, an offer letter, a filing, a payment. The tier is set before the work begins, by a named person.

**Running this against another vendor.** The table does not mention Anthropic. Put any vendor's product in the fourth column and ask the same question at each row: what does a person do here? Where the vendor's files are open, read them. Where they are not, a row you cannot fill from observation says Unknown.

## 9. Policies are not controls

A beginner needs one distinction more than any other on this shelf.

A **policy** is an instruction. A skill file that says "hold this draft for approval" is a policy: the model follows it, usually. It can be edited by anyone with access to the file, and a model can fail to follow it. A **control** is something the system enforces whatever the model does: a connector with no permission to write, a plugin an owner has not approved, a payment system that will not release without a second person.

One skill shows why this matters, and it shows it fairly. The healthcare plugin's prior authorization skill reviews requests for insurers. Its folder holds three files that a reader should set side by side. The README says recommendations are drafts, that human review is required and that no decision is final without human action. The rubric file, which the skill is told to read before every decision, defaults to what it calls lenient mode: approve only when every required criterion is met, and otherwise ask for more information; it never denies. The same file then explains how an organization can switch it to deny certain requests automatically, by editing a table. And the main instruction file offers, as part of the skill's value, automatic approval of a share of clear-cut cases. All three statements are true of the same skill. Which one describes your deployment depends on a text file and on who last changed it.

That is not a criticism of the vendor, which has published the files for anyone to read. It is the reason the method asks for three things that no skill file can supply:

1. **A named person decides the mode.** Whether anything is approved, denied, sent or paid without a person is a decision for the registry entry at Step 10, made by someone with authority, in writing.
2. **Controls where they exist.** Use the settings that enforce. Section 3 and Section 4.6 name the ones Anthropic documents: owner approval before a connector changes anything, or a block on changes; plugins set as required; and, on Enterprise plans, limits on which plugins may be installed. Treat everything else as policy.
3. **The method's gates are held by humans.** A model's check of its own output is not verification, and a model's compliance with its own instructions is not a control. The plugin's built-in review steps are welcome because they make the human gates faster to pass. They do not replace them.

## 10. Where to start

**On the first day.** Pick one plugin and one workflow, the most routine one you have. Name the six people in Section 7. Write the registry entry. The legal guide's [Section 8](using-claude-for-legal-with-the-slow-ai-kitchen.md#8-write-the-registry-entry) has a filled example that transfers to any family.

**In the first week.** Read the plugin's instruction files for that one workflow, or have someone read them to you. Write your own rules into them. Write the three to seven tests. Run the workflow on work that has already been done by hand, and compare.

**In the first month.** Run it on live work at the tier you set, with the review time scheduled. Keep the record. At the end of the month, ask the people using it what they would change, and change it.

**After that.** Add the second workflow. The steps do not change, so the second is faster than the first. The [Consultant Workbook](https://github.com/rolldabones/slow-ai-kitchen/blob/main/consultant-workbook.md) and the engagement template [*One Workflow, Thirty Days*](08-one-workflow-thirty-days.md) set out the same path in detail.

## 11. A note on artifacts

Plugins are one half of how this product line reaches people. Artifacts are the other, and a beginner will meet both in the same week.

**What an artifact is.** Anthropic's help center describes an artifact as something Claude makes that you would put in front of someone else: a document, a deck, a design, a dashboard or a small interactive tool. It opens beside the conversation and can be edited, kept and shared. The help center lists ready-made formats: Docs, Slides and Design on all plans; Data (for dashboards), Sheets and Whiteboards on paid plans; Motion on Team and Enterprise. Organization owners can switch formats on or off.

**How it differs from a plugin.** A plugin shapes how Claude works. An artifact is a thing Claude has made. The plugin stays with the person who uses it; the artifact travels. It can be opened next month by a colleague who never saw the request that produced it, or by a Client who has never used Claude.

**Where the two meet.** The legal family shows the pattern. On 28 October 2026 Anthropic introduced a gallery of ready-made legal artifacts, at [claude.ai/artifacts?templates=legal](https://claude.ai/artifacts?templates=legal): its announcement names Cite check, Jurisdiction survey matrix, Matter board, Playbook deviation board, Regulatory horizon scan and Tabular review, with others built by law firms, legal technology companies and legal aid organizations. As at 15 November 2026 I found no comparable gallery announced for any other family. Whether one is planned is Unknown.

**What the Kitchen asks of an artifact.** An artifact is a plate that keeps being served. Four consequences follow, and they apply to a sales dashboard as much as to a citation checker.

1. **Sharing is a release.** Sending an artifact to someone, or opening it to a team, is Step 9, the human release decision. It is made by a named person for each new audience and not once at creation.
2. **The tests travel with it.** The Step 2 tests and the Step 8 check belong to the artifact, not to the conversation that made it. A dashboard that passed its tests on Monday's data has not passed them on Friday's.
3. **The Owner's name stays on it.** A reader should be able to tell who answers for an artifact and when it was last checked. If the artifact cannot show that, a line of text at the top can.
4. **The registry lists it.** The Step 10 entry names the artifacts in use, who may share them and whether sharing outside the organization is allowed. Read the vendor's sharing rules before deciding: what else a viewer can see alongside a shared artifact is a setting to understand, not to assume.

A ready-made artifact from a gallery is someone else's plate. Treat it as you would a plugin: read what it does, try it on work already done by hand and write your own tests before anyone relies on it.

## 12. Where this map is weakest

1. **Nothing was run.** This is a reading of published files and pages. It says what the plugins are told to do and what their makers say. It does not say how well they do it.
2. **Drift.** Every product fact is dated 15 November 2026. Skill counts, connector lists and plan terms will change, and some entries here will be wrong within weeks.
3. **Some product pages were read in part.** The manufacturing and healthcare pages and the manufacturing announcement were read in full. The legal artifacts announcement, the two help center articles and the other product pages were read for the statements this map relies on and not from top to bottom, and the securities filing was read through a tool that summarizes. Section 13 marks each. A fine point on any of them should be checked on the page.
4. **Two plugins were not read at all.** No public repository was found for the manufacturing or nonprofits plugins. Their entries rest on Anthropic's descriptions.
5. **Counts are of files.** A skill count here is the number of skill folders in a plugin on the day it was read. It is a measure of breadth, not of quality.
6. **The last column of Section 5 is mine.** Anthropic does not assign decisions to people in that table. The assignments are the author's judgment under the method, and an organization may draw them differently.
7. **No law is stated.** Several of these plugins touch regulated decisions: credit, employment, health coverage, legal advice, investment advice. Which rules apply depends on the jurisdiction and the facts, and this map states none of them. Take advice before relying on any plugin for a regulated decision.
8. **United States defaults.** Many skills assume United States practice: its tax forms, its medical codes, its bar rules. A team elsewhere keeps the steps and replaces the references.
9. **One vendor.** Other companies publish comparable packages. The method applies to them; this inventory does not.

## 13. Currency register

Every product fact relied on, with its source and the date it was read (KST). "Repository" means a copy taken on the date shown, at the commit named.

| Item | Source | Read on | How read |
|---|---|---|---|
| A plugin bundles skills, connectors and sub-agents; available on paid plans; job functions named; the four Anthropic marketplaces, Knowledge Work added by default; the Customize, Plugins, Discover path; owner controls on Team and Enterprise | Anthropic help center, *Use plugins in Claude* | 15 November 2026 | browser, word for word as far as the section on publishing to an organization; the marketplace names from the page text returned by search; page carries no fixed date |
| Public plugin directory showing 531 plugins | claude.com/plugins | 15 November 2026 | browser |
| Seven vertical solutions launched; the seven names; Section 4.8.4, page 127 | Anthropic, PBC, issuer free writing prospectus of 11 November 2026, relating to the preliminary prospectus of 10 November 2026, on SEC EDGAR | 15 November 2026 | summarizing reader, with the sentence also seen in the page text returned by search; the page was too large to search in the browser, so the passage is paraphrased and not quoted |
| Financial services: ten agents, six skill bundles with skill counts, two partner plugins, connector names, the statement on review and sign-off, Apache 2.0 | anthropics/financial-services, commit 3e32c22 of 12 November 2026 | 15 November 2026 | repository |
| Financial services product page | claude.com/solutions/financial-services | 15 November 2026 | browser, in part |
| Financial advisors: eight skills, no Client data held, approval before any write, not advice, Apache 2.0 | anthropics/claude-for-financial-advisors, commit 0ceaf1f of 27 October 2026 | 15 November 2026 | repository |
| Financial advisors product page: no trades or money movement, review steps and audit trails, Enterprise recommended for its audit logs; connector names from a summarizing reader | claude.com/solutions/financial-advisors | 15 November 2026 | browser, in part; the statements relied on were found on the page |
| Healthcare: one plugin, ten skills, data sources, terms-of-service license line; the prior authorization skill's README.md, SKILL.md and references/rubric.md | anthropics/healthcare, commit c7ed150 of 27 August 2026 | 15 November 2026 | repository |
| Healthcare product page: access through Enterprise and the platform, HIPAA-ready wording, answers traced to source, drafts for review | claude.com/solutions/healthcare | 15 November 2026 | browser, word for word |
| Life sciences: four skills, refocus on skills, removed skills | anthropics/life-sciences, commit 0d38fe5 of 2 November 2026 | 15 November 2026 | repository |
| Life sciences product page | claude.com/solutions/life-sciences | 15 November 2026 | browser, in part |
| Legal: twelve plugins with skill and agent counts, CoCounsel partner plugin, the statements on attorney review and responsibility, Apache 2.0 | anthropics/claude-for-legal, commit 4a6c651 of 23 July 2026 | 15 November 2026 | repository |
| Manufacturing: launch date, 17 skills in six areas, six named processes, four connectors, exports through Microsoft 365, the Infor look-up connector and Infor's separate plugin, skills end with review, does not operate equipment, Team or Enterprise | Anthropic, *Introducing Claude for Manufacturing*, 12 November 2026 | 15 November 2026 | word for word, in a browser |
| Manufacturing product page: paid plans and installation by an administrator, no writing to systems of record, owner approval of connector changes, fit for discrete and process manufacturers | claude.com/solutions/manufacturing | 15 November 2026 | browser, word for word |
| Small business: 44 skills, connector list, the approval statement in the plugin's description | anthropics/knowledge-work-plugins, small-business folder, commit e91a134 of 13 November 2026 | 15 November 2026 | repository |
| Small business product page: plan shown before action, nothing sent or paid without agreement, payroll prepared for the owner to submit | claude.com/solutions/small-business | 15 November 2026 | browser, in part; the statements relied on were found on the page |
| Nonprofits: plugin installed for every verified nonprofit, built with about thirty nonprofits, Salesforce and Blackbaud connectors | claude.com/solutions/nonprofits | 15 November 2026 | browser, in part |
| Education and teachers; government; cybersecurity | claude.com/solutions/education, /teachers, /government, /cybersecurity | 15 November 2026 | browser, in part |
| Job-function plugins: seventeen Anthropic folders, skill counts, descriptions, connector files, five partner plugins in the repository, 123 entries in the marketplace file including claude-for-financial-advisors, the README's count of eleven, "starting points" | anthropics/knowledge-work-plugins, commit e91a134 of 13 November 2026 | 15 November 2026 | repository |
| Artifacts: definition, formats, plans; the legal gallery of 28 October 2026 | Anthropic help center, *What are artifacts and how do I use them*; Anthropic, *Introducing artifacts for legal work*, 28 October 2026 | 15 November 2026 | browser, word for word for the passages relied on |
| Steps, gates, tiers, roles, checked step by step against the method text | Slow AI Kitchen v3.5.0, README.md | 15 November 2026 | repository |
| Doctrine statements and the AOTL Register note | DOCTRINE.md v1.2.4 | 15 November 2026 | repository |

A second edition is owed when a new family is launched, when a cited repository changes its list of plugins or when the account's weekly link check reports a cited page dead.

## Questions for discussion

1. Take one plugin your team might turn on. Can you name the six people in Section 7 today? Which name is hardest to fill, and why?
2. Ask the AOTL question of one output that plugin would draft: whose name is on the line before the run? Did the answer come quickly?
3. Open the instruction file for one skill you would use. What in it is your team's way of working, and what is a stranger's?
4. Which of the outputs your team would draft with a plugin are Tier 3 the moment they are released? Does anyone outside the team know that?
5. Find one instruction in a skill file that says a person must approve. Is there a setting anywhere that enforces it? If not, what would?
6. How much review time per output have you scheduled? Who decided, and did they ask the reviewer?
7. If you stopped using this vendor next quarter, what would leave with you: the playbook, the tests, the records? Write that row of the registry now.

## This map and the account

The map reads work that already exists in this account. Each row points to where the argument is carried as an instrument. The full map of the account is [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md).

| In this map | Where the account carries it |
|---|---|
| Section 4.5: the legal family worked in full | [*Using Claude for Legal with The Slow AI Kitchen*](using-claude-for-legal-with-the-slow-ai-kitchen.md), all sections |
| Sections 7 and 8: the steps, gates, tiers and roles | [Slow AI Kitchen README](https://github.com/rolldabones/slow-ai-kitchen), the twelve steps, the Tier Application Map and the role tables |
| Section 7: the three doctrines and AOTL | [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md), sections 1 to 3, and the section 6 Register note, where AOTL is recorded as the vernacular form of Final Liability: a register, with no instrument depending on it |
| Section 8: recipes for single tasks | [*Slow AI Cookbook*](https://github.com/rolldabones/slow-ai-kitchen/blob/main/slow-ai-cookbook.md), where recipes name capabilities and not models |
| Section 8: the close-out of high-stakes work | [service-record.md](https://github.com/rolldabones/slow-ai-kitchen/blob/main/service-record.md) |
| Section 9: policies and controls | The legal guide, [Section 21](using-claude-for-legal-with-the-slow-ai-kitchen.md#21-what-the-product-does-for-you-and-what-it-does-not), the gate-by-gate table of what a product does and does not do |
| Section 10: one workflow in thirty days | [08-one-workflow-thirty-days.md](08-one-workflow-thirty-days.md) and the [Consultant Workbook](https://github.com/rolldabones/slow-ai-kitchen/blob/main/consultant-workbook.md) |
| Section 10 and question 7: what leaves with you | [GRCnext-Copilot](https://github.com/rolldabones/GRCnext-Copilot), for the GRCnext™ primitives (Services, Tolerances, Pipes, Switches, Exits) and whether an Exit would execute |
| What the shelf means for the organization: which capabilities to keep, what a smaller core must still be able to do and the duties owed to the people affected | [*The Core and the Capability*](the-core-and-the-capability.md), the companion piece, especially Sections 6, 8 and 9 |
| The cost of running many plugins | [Lean AI](https://github.com/rolldabones/slow-ai-kitchen/blob/main/lean-ai.md), a work in progress, on the total cost per accepted outcome |

The Slow AI Kitchen also runs as a guided web application at [kitchen.grcskorea.com](https://kitchen.grcskorea.com/), in English, Korean, Vietnamese and Japanese. The repository is the text of record.

## Source basis and attribution

**Primary sources, read in full from the repository**

- Anthropic, [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins), commit e91a134 (13 November 2026): README.md and each plugin's manifest, skills folder and connector file. Apache License 2.0.
- Anthropic, [anthropics/financial-services](https://github.com/anthropics/financial-services), commit 3e32c22 (12 November 2026): README.md and each plugin's manifest and skills folder. Apache License 2.0.
- Anthropic, [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal), commit 4a6c651 (23 July 2026): README.md and each plugin's manifest, skills and agents folders. Apache License 2.0.
- Anthropic, [anthropics/claude-for-financial-advisors](https://github.com/anthropics/claude-for-financial-advisors), commit 0ceaf1f (27 October 2026): README.md and the skills folder. Apache License 2.0.
- Anthropic, [anthropics/healthcare](https://github.com/anthropics/healthcare), commit c7ed150 (27 August 2026): README.md and the prior authorization skill's README.md, SKILL.md and references/rubric.md.
- Anthropic, [anthropics/life-sciences](https://github.com/anthropics/life-sciences), commit 0d38fe5 (2 November 2026): README.md.
- Slow AI Kitchen v3.5.0, [README.md](https://github.com/rolldabones/slow-ai-kitchen), and [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md) v1.2.4.

**Primary sources, read in a browser on 15 November 2026**

- Read in full: Anthropic, [*Introducing Claude for Manufacturing*](https://claude.com/resources/articles/claude-for-manufacturing), 12 November 2026; the [manufacturing](https://claude.com/solutions/manufacturing) and [healthcare](https://claude.com/solutions/healthcare) product pages.
- Read for the passages relied on: Anthropic help center, [*Use plugins in Claude*](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) and [*What are artifacts and how do I use them*](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them); Anthropic, [*Introducing artifacts for legal work*](https://claude.com/resources/articles/introducing-artifacts-for-legal-work), 28 October 2026; the product pages for [financial services](https://claude.com/solutions/financial-services), [financial advisors](https://claude.com/solutions/financial-advisors), [life sciences](https://claude.com/solutions/life-sciences), [small business](https://claude.com/solutions/small-business), [nonprofits](https://claude.com/solutions/nonprofits), [higher education](https://claude.com/solutions/education), [K-12 teachers](https://claude.com/solutions/teachers), [government](https://claude.com/solutions/government) and [cybersecurity](https://claude.com/solutions/cybersecurity); and the [plugin directory](https://claude.com/plugins).

**Primary sources, read through a summarizing reader**

- Anthropic, PBC, [issuer free writing prospectus of 11 November 2026](https://www.sec.gov/Archives/edgar/data/2130357/000162828026073040/anthropicpbc-fwpxeeaprospea.htm), Section 4.8.4, relating to the preliminary prospectus of 10 November 2026, on SEC EDGAR.
- The [legal product page](https://claude.com/solutions/legal), for its links only.

**Considered and left out:** the 500 and more plugins in the public directory built by other companies; plugins for software development; the managed-agent versions of the financial and legal agents, which run through Anthropic's developer platform and not the apps; Infor's own plugin; the Model Hardware Standard, a research preview on how AI might operate equipment; pricing, seat counts and usage limits, which change too often to record here.

---

*This document is provided for general informational and discussion purposes regarding the governance and use of AI. It does not constitute legal advice with respect to any specific matter, jurisdiction or engagement. It describes a vendor's products as read on one day and is not a statement of the vendor's positions.*

**Final Liability rests with the Human.**
