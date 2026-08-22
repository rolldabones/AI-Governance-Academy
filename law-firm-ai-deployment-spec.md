# Law Firm AI Deployment Spec v2

**How to Build a Governed, Useful and Auditable AI Capability in 90 Days**

Son-U Michael Paik · former General Counsel, BABL AI Inc. · CEO, GRC Solutions Korea

August 22, 2026

**Version note.** Version 1 of this specification is Seth Fenster's LinkedIn post "If an Am Law 100 firm hired me as their Chief AI Officer tomorrow, here's exactly what I'd do in the first 90 days" (Founder & CEO, Litvue; August 2026): [original post](https://www.linkedin.com/posts/seth-fenster_if-an-am-law-100-firm-hired-me-as-their-chief-share-7496334818847248384-etxj/). Credit for the inspiration and for the 90-day brief belongs there. Version 2 is this document: an independent answer to the same brief, built on the governance frameworks maintained at [github.com/rolldabones](https://github.com/rolldabones).

---

## Contents

- [0. Create the economic incentive to participate](#0-create-the-economic-incentive-to-participate)
- [1. Establish Informed Intent](#1-establish-informed-intent)
- [2. Inventory actual AI use](#2-inventory-actual-ai-use)
- [3. Classify AI by what it does](#3-classify-ai-by-what-it-does)
- [4. Establish the AI data-processing baseline](#4-establish-the-ai-data-processing-baseline)
- [5. Build the minimum governance system](#5-build-the-minimum-governance-system)
- [6. Build a small engineering team](#6-build-a-small-engineering-team)
- [7. Map the firm's information architecture](#7-map-the-firms-information-architecture)
- [8. Establish a centralized AI gateway](#8-establish-a-centralized-ai-gateway)
- [9. Connect identity and authorization](#9-connect-identity-and-authorization)
- [10. Build the firm's governed knowledge layer](#10-build-the-firms-governed-knowledge-layer)
- [11. Find expensive operational bottlenecks](#11-find-expensive-operational-bottlenecks)
- [12. Convert tacit legal judgment into evaluation rubrics](#12-convert-tacit-legal-judgment-into-evaluation-rubrics)
- [13. Test before trusting](#13-test-before-trusting)
- [14. Deploy a bounded production workflow](#14-deploy-a-bounded-production-workflow)
- [15. Measure economics, quality and risk together](#15-measure-economics-quality-and-risk-together)
- [16. Preserve the evidence](#16-preserve-the-evidence)
- [The 90 Days and the Slow AI Kitchen](#the-90-days-and-the-slow-ai-kitchen)
- [Day 90: Definition of Done](#day-90-definition-of-done)

---

If I were asked to build an AI capability for a major law firm in 90 days, I would not begin with an AI product.

I would begin with the firm's work, its information, its people and its obligations.

The objective is not maximum AI adoption. It is to create an AI capability that makes the firm demonstrably better while preserving confidentiality, professional responsibility, security and human accountability.

The governing principles are simple:

**Informed Intent.** Know what we are trying to accomplish, why AI is appropriate, on whose authority it acts, within what boundaries and with what exit, before we build.

**Slow AI.** Move deliberately where consequences matter. Make material AI use visible, controlled, explainable, testable and auditable.

**Final Liability rests with the Human.** Every material AI system, workflow and output has a named human owner with decision rights, oversight and the power to intervene.

The three doctrines are stated normatively in [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md). This specification restates them at deployment altitude and adds instruments, not doctrine.

One emphasis is specific to law firms: the durable capability is trained users. I hold that view from practice, having created and taught the [AI for Legal Professionals course](https://courses.babl.ai/l/pdp/ai-for-legal-professionals) at BABL AI within its AI Governance for Legal Professionals certification program. Lawyers are formed by a training culture built on supervision, markup and review. The 90 days should convert that culture into the firm's AI discipline, not work around it.

The first 90 days build the rails.

## 0. Create the economic incentive to participate.

Establish an internal billing or innovation code that gives lawyers and staff credit for AI work: testing systems, developing evaluation rubrics, identifying failures, documenting workflows, providing feedback and learning approved tools.

If experimentation competes with billable-hour expectations, experimentation will lose.

Treat participation as productive firm work and measure the investment.

Structured learning counts too. The [Slow AI Kitchen's workshop](https://github.com/rolldabones/slow-ai-kitchen#the-workshop) is a training method as much as a control architecture: it runs teams through the twelve steps on real tasks, so the discipline is learned by cooking rather than by policy memo. [The AI Generalist](https://github.com/rolldabones/the-ai-generalist) is the one-day on-ramp: LLM foundations, a repeatable prompting workflow and the minimum AI governance, risk management and compliance control set.

## 1. Establish Informed Intent.

Before selecting technology, define what the firm wants AI to accomplish.

Identify initial objectives, constraints, prohibited uses, material risks and measurable outcomes.

For each proposed use case ask:

**What are we trying to improve? What may the AI do? What may it access? What may it never do? What constitutes acceptable performance? Who decides whether it is ready? Who owns the result? What is the exit?**

The last question is not optional. DOCTRINE.md states it plainly: an authorization missing its exit is not an authorization; it is a hope.

Informed Intent is also a user skill, and it is trainable. Teach lawyers to state intent to the model before the work begins: the task, the audience, the constraints, the form of the answer and what done looks like. Prefer workflows that force that clarification before any output is produced. The Kitchen opens this way by design, Define the Dish and then Mise en Place with a Definition of Done before AI touches the task, and a well-built operating prompt halts on missing inputs rather than inventing them.

The [AI Impact Assessment Tool](https://github.com/rolldabones/AI-Impact-Assessment-Tool) is the Informed Intent gate in tool form, aligned to the EU AI Act, NIST AI RMF, ISO/IEC 42001 and ISO/IEC 42005.

This becomes the baseline against which architecture, controls and return on investment are evaluated.

## 2. Inventory actual AI use.

Identify every AI system currently used or requested across the firm, including approved, experimental and unsanctioned tools.

Record the provider, model, users, matters, information accessed, integrations, contractual terms and purpose.

Do not begin with the assumption that the firm's AI environment is what procurement records say it is. For what ungoverned agentic use actually looks like, [The Ungoverned Channel](https://github.com/rolldabones/the-ungoverned-channel) is a living field study: agentic AI loose in multiplayer workflows, observed in the wild.

Ask, Look & Listen.

The people already experimenting responsibly are also likely to become the firm's first AI champions.

## 3. Classify AI by what it does.

Do not classify AI merely by vendor or model.

**Classify the agent by its verb.**

Searching is different from summarizing. Summarizing is different from drafting. Drafting is different from advising. Advising is different from filing, sending, committing or executing.

For every material use case identify:

**the verb, the information boundary and the consequence.**

Higher-consequence actions require stronger controls, testing and human authority. This is the Slow AI Kitchen's [risk-tier logic](https://github.com/rolldabones/slow-ai-kitchen#risk-tiers) applied to a firm: not every task needs the same depth of control, and the verb tells you the tier.

For lawyers the verb also carries the duty. Searching and summarizing engage competence and verification. Drafting engages supervision and review. Advising engages judgment the profession reserves to lawyers. Filing and sending engage candor to tribunals and accuracy to counterparties. The rules of professional conduct already classify by consequence; the AI classification should land in the same places.

## 4. Establish the AI data-processing baseline.

Require appropriate enterprise agreements with every model and infrastructure provider.

Zero data retention should be strongly preferred where appropriate, but it is one control, not the control.

Evaluate training and secondary use, retention, telemetry, subprocessors, data residency, encryption, authentication, incident notification, deletion, backups, legal holds, cross-border transfers and contractual liability.

Ask separately what the arrangement does to privilege and work product. Whether disclosure to a provider risks waiver is jurisdiction-specific, and it must be answered before the first privileged document moves, not after.

Read the agreements as what they are: risk-transfer mechanisms and executable business plans. The [Contract Mechanism Review Assistant](https://github.com/rolldabones/Contract-Mechanism-Review-Assistant) exists for exactly this review. And observe the drafting rule in DOCTRINE.md: a vendor can assume contractual risk between the parties; it cannot assume a duty the firm owes a regulator. In a law firm the logic reaches further: the professional duties owed a Client are the lawyer's under the rules of professional conduct and do not delegate to a vendor.

Client-specific restrictions must also be capable of overriding firm-wide permissions, and the firm must be able to evidence each override when the Client asks. Outside counsel guidelines increasingly say so expressly.

Confidentiality is an architecture, not a checkbox.

## 5. Build the minimum governance system.

Create a lightweight AI governance structure before scaling deployment.

At minimum maintain:

- AI system and use-case inventory
- risk classification
- approved and prohibited uses
- named business or practice owner
- technical owner
- information owner
- required human review
- evaluation criteria
- approval record
- incident and escalation process
- change history
- monitoring evidence
- retirement or decommissioning process.

Governance should produce decisions and proof, not paperwork for its own sake.

Two instruments shortcut the build. The [AI GRC Master List of Questions](https://github.com/rolldabones/AI-GRC-Master-List-of-Questions) captures the firm's facts once, in 17 sections of mostly yes/no answers, and the [AI GRC Spellbook Copilot](https://github.com/rolldabones/AI-GRC-Copilot) converts them into the 30 canonical AI governance artifacts with owners, evidence and systems of record. The [GRC Workbook's](https://github.com/rolldabones/grc-workbook) thirty-seven item Governance Test is then the audit of whether the resulting system actually governs.

## 6. Build a small engineering team.

A large bureaucracy is unnecessary.

A small multidisciplinary team should combine AI engineering, enterprise architecture, information security, knowledge management and lawyers who understand the work being automated.

Engineers do not need to be senior lawyers.

They do need enough understanding of legal work to know when the technology has crossed from assisting a lawyer into exercising judgment or taking consequential action.

The same test applies to the architect. The [Practice Primer](https://github.com/rolldabones/slow-ai-kitchen/blob/main/enterprise-ai-architecture-primer.md), the Kitchen's companion architecture reference, organizes the role as ten competencies, from workflow architecture to enterprise systems thinking, with governance by design as the spine running through the other nine. Its organizing claim is the hiring standard: the gap between an AI engineer and an enterprise AI architect is not technical depth but scope of accountability. An engineer optimizes the system in front of them. An architect decides whether the system should exist, who owns it, what it costs over three years, what evidence it produces, who is answerable when it is wrong and what survives when it is switched off.

If the firm hires a Chief AI Officer, that is the job description.

Name the roles the way the Kitchen [names its brigade](https://github.com/rolldabones/slow-ai-kitchen#roles): Preparer, Builder, Owner, Reviewer, Approver, with an Executive Sponsor and an AI Owner at the deployment layer. Titles vary; the separation of duties does not.

## 7. Map the firm's information architecture.

Determine where authoritative information actually lives: document management systems, SharePoint, OneDrive, email, matter systems, financial systems, precedent libraries and specialist databases.

Then determine permissions, information classifications, ethical walls, Client restrictions and systems of record.

Do not automatically copy everything into a new AI repository.

Where possible, leave authoritative information in governed systems and retrieve it through controlled interfaces.

The goal is centralized intelligence, not necessarily centralized copies.

This is where most retrieval programs actually fail: not at the model but at the estate. The Practice Primer treats it as two competencies of its own, knowledge architecture and data architecture, with quality, lineage and residency as preconditions rather than afterthoughts.

## 8. Establish a centralized AI gateway.

Route approved AI access through a controlled gateway in the firm's enterprise environment.

The gateway should provide model access, authentication, policy enforcement, logging, cost visibility, model routing and the ability to change providers without rebuilding the firm's architecture.

Models should be replaceable.

The firm's knowledge, controls, evaluations and workflows should not be.

That is optionality, and optionality is the core safety property of the [GRCnext™](https://github.com/rolldabones/GRCnext-Copilot) framework, which supplies the operating primitives: Services, Tolerances, Pipes, Switches, Exits. The gateway is a Pipe. A provider change is an Exit. [RedCap-00](https://github.com/rolldabones/RedCap-00) tests whether the Exit would actually execute under disruption, before the day the firm needs it.

## 9. Connect identity and authorization.

Integrate the AI environment with the firm's identity provider.

Authentication is only the beginning.

AI systems must respect the same or stricter authorization boundaries as the people using them: matter access, ethical walls, Client restrictions, role, geography, information classification and need-to-know permissions.

An agent should never acquire authority merely because it is technically capable of exercising it.

**No AI receives greater authority than the human or system principal on whose behalf it acts.**

That is the authority element of Informed Intent, enforced in infrastructure rather than in policy.

## 10. Build the firm's governed knowledge layer.

Create controlled interfaces through which approved AI systems can retrieve institutional knowledge and matter information.

Use secure application programming interfaces and, where appropriate, Model Context Protocol (MCP) interfaces to make systems interoperable.

But treat interoperability and security separately.

Every connection needs authentication, authorization, logging, data boundaries and revocation. In GRCnext™ terms, every interface is a Pipe and every revocation path is a Switch. Build them as such.

For a law firm one boundary dominates: the knowledge layer must enforce ethical walls and Client restrictions at retrieval time, so that one matter's information cannot surface in another's work product, however useful the model would find it.

The durable institutional asset is not the model.

It is the firm's governed combination of **knowledge + permissions + precedent + evaluation + workflow**.

## 11. Find expensive operational bottlenecks.

Now examine how lawyers actually work.

Look for high-volume, repetitive or cognitively expensive tasks where AI might materially improve speed, quality or capacity.

Start with workflows where mistakes are detectable and intervention remains possible.

Measure the baseline before introducing AI. This is [Gate 2 of the Kitchen](https://github.com/rolldabones/slow-ai-kitchen#step-3-knife-work-gate-2-manual-first-pass), the Manual First Pass, run at firm scale: the humans do the work first, so the firm knows what good looks like and what it costs.

Otherwise there is no credible return-on-investment calculation later.

[RedCap-01](https://github.com/rolldabones/RedCap-01) carries the same discipline into target selection: pick work whose improvement changes the decisions that determine objective achievement, not work that is merely frequent.

## 12. Convert tacit legal judgment into evaluation rubrics.

This may become one of the firm's most valuable AI assets.

Partners and experienced lawyers possess enormous amounts of undocumented judgment about what constitutes good work.

Use precedent and expert review to convert some of that judgment into explicit evaluation criteria.

For a drafting workflow, for example, evaluate:

factual fidelity, authority accuracy, citation integrity, issue coverage, analytical quality, jurisdictional fit, Client requirements, tone, structure and formatting.

Compare AI output with junior work, reviewed work and final partner-approved work.

The extraction method matters. Expertise does not live in stated preferences; it lives in tacit judgment calls, and those are not listed on request. They surface when an expert reacts to a draft. The firm already owns this mechanism: it is the red pencil, the markup tradition by which lawyers have always been trained. Put AI drafts through it. A rubric built from a questionnaire captures what partners say they want. A rubric built from redlines captures what they actually do.

Edits reveal intent. What the lawyer states before the work begins is one half of Informed Intent, and what the redline discloses afterward is the other. I have made the same argument for [building AI Skills by redlining the model](https://www.linkedin.com/posts/sonupaik_%F0%9D%90%93%F0%9D%90%A1%F0%9D%90%9E-%F0%9D%90%9F%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%AD%F0%9D%90%9E%F0%9D%90%AC%F0%9D%90%AD-%F0%9D%90%B0%F0%9D%90%9A%F0%9D%90%B2-%F0%9D%90%AD%F0%9D%90%A8-%F0%9D%90%A0%F0%9D%90%9E%F0%9D%90%AD-activity-7450795738436964353-OW-z): the engine is a mid-session draft the expert marks up in their own hand.

The objective is not merely to teach AI how the firm writes.

It is to make the firm's definition of quality measurable.

A rubric written this way is a specification, and specification design is its own discipline: [computational drafting](https://github.com/rolldabones/computational-drafting), the design of specifications that translate human and institutional intent into behavior across legal, organizational and technical interpreters. Write the rubric before the work begins and it becomes a [Definition of Done](https://github.com/rolldabones/definition-of-done): acceptance criteria fixed in advance, confirmed before reliance.

## 13. Test before trusting.

Run controlled evaluations before production deployment.

Test normal cases, difficult cases, adversarial inputs, missing information, conflicting authority, permission boundaries and foreseeable failure conditions.

Measure both capability and failure.

Record the results.

The operating rule is in [Sounds Good](sounds-good.md), this repository's companion memorandum: AI output is optimized to sound good, correctness is a byproduct rather than a property, and verification is a human obligation wherever generated content enters the work product.

Where consequences are material, require explicit acceptance thresholds and human approval before deployment. In the Kitchen this is Gate 6, Taste Before Service, and no plate reaches Gate 7, the human release decision, without passing it. The Practice Primer's Practice Layer supplies the review instruments: a twelve-question sequence for interrogating a proposed or live system and a defect catalog pairing each failure mode with its symptom and its architectural fix.

Slow AI does not mean slow technology.

It means slowing down at the decision points where errors become consequential.

## 14. Deploy a bounded production workflow.

By approximately day 90, deploy one useful production workflow with:

a defined objective, approved information sources, bounded permissions, tested models, evaluation thresholds, logging, escalation rules and a named human owner.

A concrete first candidate: first-pass review of inbound nondisclosure agreements against the firm's playbook. The volume is high, the playbook already states the evaluation criteria, deviations are detectable by a reviewing lawyer and nothing leaves the firm without one.

Do not make "autonomy" the goal.

Give the system only as much autonomy as the consequence justifies.

The first production system should be capable of demonstrating measurable improvement while remaining observable, reversible and interruptible.

A workflow like this is what I have elsewhere called a [Tiny Servant](https://redcaps.substack.com/p/made-to-hold): narrow purpose, clear boundaries, a named owner, one useful task done well, then it stops. The [Origami Method](https://github.com/rolldabones/origami-method) is the design discipline for folding one: stage-gated, with creases, gates and a fold log.

## 15. Measure economics, quality and risk together.

Compare the production workflow against the pre-AI baseline.

Measure:

time invested, time saved, adoption, output quality, correction rates, write-offs, realization, Client value, model and infrastructure cost, exceptions and incidents.

A faster workflow that creates more review work is not necessarily an improvement.

A cheaper workflow that introduces unacceptable professional risk is not an improvement.

AI return on investment must include the cost of governing the AI.

The GRC Workbook builds on OCEG's Principled Performance: the reliable achievement of objectives, the addressing of uncertainty and the conduct of business with integrity. Measured that way, governance cost is not overhead on the return. It is part of how the return is produced.

The 90 days should also surface, without pretending to solve, the pricing question. AI compresses the time that hourly billing prices. Whether the firm bills the hour, the value or the outcome is a decision to make with Clients, not a default to inherit, and the internal credit code from Section 0 is not a substitute for that external answer.

## 16. Preserve the evidence.

For every material system, retain enough evidence to reconstruct:

**What did we intend? What did we build? What information could it access? What model was used? What controls applied? How was it tested? What happened? Who reviewed it? Who decided?**

That evidence is what converts governance from assertion into something auditable. The Practice Primer's evidence register is the instrument for it: the artifact that proves each control exists, named in advance.

Slow AI's audit test is that the evidence exists before it is asked for, not after. Gate 10 of the Kitchen, the Operational Audit and Review Cycle, is where the firm proves it on a schedule rather than under subpoena.

## The 90 Days and the Slow AI Kitchen

The [Slow AI Kitchen](https://github.com/rolldabones/slow-ai-kitchen) is the method beneath this specification: twelve steps in two registers, with ten gates. Steps 1 through 9, the Kitchen, govern the production of individual and team work product. Steps 10 through 12, the Feast, govern the organizational deployment of AI tools across users and functions.

The 90-day build is the Feast, constructed once at firm scale. Every workflow it deploys then cooks in the Kitchen, task by task.

| This specification | Slow AI Kitchen |
|---|---|
| Sections 1 through 5 and 11: intent, inventory, classification, data baseline, governance system, use-case selection | Step 10: Plan the Menu (Gate 8: Authorized Tool Registry) |
| Sections 7 through 10: information architecture, gateway, identity, knowledge layer | The Practice Primer, the Feast's companion architecture reference |
| Sections 0, 6 and 12: incentives, roles, rubrics | Step 11: Staff the Brigade (Gate 9: Competency and Authorization Record) |
| Sections 13 through 16 and Day 90: testing, bounded deployment, measurement, evidence | Step 12: Run the Event (Gate 10: Operational Audit and Review Cycle) |
| Every production workflow deployed under Section 14 | Steps 1 through 9 (Gates 1 through 7), per task |

The Kitchen's warning holds at both scales: a gate that is skipped does not disappear; it becomes a liability.

A guided implementation of the twelve steps runs at [slow-ai-kitchen.msagent.ai](https://slow-ai-kitchen.msagent.ai/).

## Day 90: Definition of Done

"Definition of Done" is not a figure of speech here. It is the [acceptance doctrine](https://github.com/rolldabones/definition-of-done): done is defined before the work begins and confirmed before reliance.

At the end of 90 days, the firm should not merely have "AI."

It should have:

a governed AI inventory, defined use cases, contractual and data controls, centralized access, identity and authorization controls, a governed knowledge layer, trained users under a competency and authorization record, evaluation rubrics, production testing, measurable baselines, monitoring, audit evidence and at least one bounded workflow demonstrating real value.

Most importantly, every material capability should have a named human owner with the information, authority and ability to intervene.

Name what was built honestly. It is a digital transformation, with an AI management system, the ISO/IEC 42001 construct, at its center. But it is fundamentally a knowledge management program as well: the firm has mapped where its knowledge lives, governed who and what may retrieve it, converted tacit judgment into explicit criteria and preserved the evidence of its decisions. The models were never the asset. The knowledge layer is, and it outlasts every vendor on the roadmap.

From there, the firm can expand deliberately.

New models can come and go. New vendors can be tested against the same data boundaries and evaluation standards. New agents can be given progressively greater capability where the evidence supports it.

The objective is not to predict which AI vendor wins.

It is to build a firm that can safely use whichever technology proves best.

The instruments referenced throughout are maintained and mapped in [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md).

**Informed Intent determines what we ask AI to do. Slow AI governs how we allow it to do it. Final Liability determines who remains responsible when it does.**

That is the foundation worth building in the first 90 days.

**Final Liability rests with the Human.**

---

*This document is provided for general informational purposes regarding the governance of AI deployment in professional services organizations. It does not constitute legal advice with respect to any specific matter, jurisdiction or engagement.*
