# Systems Architecture for AI

**Following one request through an enterprise AI service: an introductory primer**

Son-U Michael Paik · CEO, GRC Solutions Korea

22 November 2026

**Starting point.** Eli the Computer Guy's lecture [*Systems Architecture for AI Introduction*](https://www.youtube.com/watch?v=OxwKJebdqy4), published on YouTube on 21 November 2026 (US Pacific time), runs two and a half hours on what an AI project needs besides the model: servers, storage, interfaces, routing, security, logging and budget. It was the starting inspiration for this primer, which evaluates his outline and builds on it a method for reviewing one enterprise AI service. The piece stands on its own: nothing in it depends on the lecture, and every claim it makes rests on the sources it cites. The design questions, the handoff table, the desk exercise, the release criteria and the source checks are mine.

**For:** governance, risk management and compliance professionals, in-house lawyers, auditors and business owners who must review or sponsor an AI service and want the working vocabulary of the people who build it. No programming is assumed. A reader who builds systems will find the method familiar and the exercise worth running.

**What this piece is and is not.** It is an introduction: one request, followed from the person who asks to the person accountable for the answer, with a case you can score by hand. It is not a reference architecture, a vendor comparison or a statement of law, and it assumes no jurisdiction. It adds no doctrine, step, gate, tier or form to this account. The deep reference is the [Enterprise AI Architecture Primer](https://github.com/rolldabones/slow-ai-kitchen/blob/main/primer/README.md) in `slow-ai-kitchen`; Section 10 maps each part of this piece to the sections there that carry it further.

**How to use it.** Read Sections 1 to 5 once (about 40 minutes). Then work the desk exercise in Section 6 with a colleague, one playing the reviewer and one the builder (about 60 minutes). Readings 1, 2 and 5 in Section 9 are the preparation for the exercise.

## In brief

1. A model can give a fluent answer while the service around it serves a superseded policy, shows one Client's document to another or spends its budget on retries. Review the service, not the model.
2. Follow one request. At every handoff ask three questions: what may pass, what can fail and what evidence survives.
3. Decide what the service has authority to answer before choosing a model or connecting a data source. Similarity in a search index never establishes entitlement, authority or currency.
4. Test retrieval and answering separately. When an answer is wrong, find the stage that failed before changing anything; a larger model leaves a broken date filter in place.
5. Release on observed results against cases agreed in advance, with stop conditions, a named decision owner and a route back.

## Contents

1. [Map the service before selecting the model](#1-map-the-service-before-selecting-the-model)
2. [Choose a model and a place to run it](#2-choose-a-model-and-a-place-to-run-it)
3. [Decide which information the system may use](#3-decide-which-information-the-system-may-use)
4. [Connect, constrain and observe the service](#4-connect-constrain-and-observe-the-service)
5. [Price the work and rehearse failure](#5-price-the-work-and-rehearse-failure)
6. [The desk exercise](#6-the-desk-exercise)
7. [Where the doctrines sit](#7-where-the-doctrines-sit)
8. [Common claims, checked](#8-common-claims-checked)
9. [Readings, in order](#9-readings-in-order)
10. [Going further](#10-going-further)
11. [Terms](#11-terms)
12. [Limits](#12-limits)

## 1. Map the service before selecting the model

**Draw one request.** Start with four boxes: the user interface, the application, the sources of data and the model. Then add the identity check, any external application programming interface (API) the application calls and the place the result goes. Mark which boxes your team runs and which a supplier runs. The model is one layer of a larger stack, and the review covers every layer. A batch job does the same work without a user-facing web server, so the drawing describes functions, not products.

**Separate response time from capacity.** These are three questions, not one: how long one request may take, how many requests arrive at once and by when a backlog must clear. A marketing team can wait overnight for a searchable photo archive; a person waiting at a door experiences every second. Suppose a model running on modest local hardware takes five minutes to process one image. One worker that is never idle then processes 12 images an hour, 288 a day and 2,016 a week. These are theoretical ceilings: real capacity comes from a timed run on the target hardware, with loading, failures and retries included.

**Write the decision in business terms.** Before any technical choice, write down the permitted action, the service owner, the budget, the deadline and the manual fallback, and who can operate the service when its developer is away. The budget decides the design: the same money pays for servers, processors, licenses and the people who run them. A useful first deliverable is a one-page drawing that operations, legal and the business owner can each annotate.

**The reference design.** The running example is an employee assistant for leave questions, chosen because a wrong answer is plausible, consequential and easy to check. The service may explain an approved leave policy. Only the personnel service may report an individual's balance. That division of authority shapes the architecture before anyone chooses a model.

```mermaid
flowchart TD
    A["Employee question"] --> B["Authenticate and check scope"]
    B --> C{"What is being asked?"}
    C -->|Policy rule| D["Retrieve authorized, current policy"]
    C -->|Personal balance| E["Refer to personnel service"]
    C -->|Unclear| F["Ask for clarification"]
    D --> G{"Applicable clause available?"}
    G -->|Yes| H["Draft answer with citation"]
    G -->|No| I["Refer to policy owner"]
```

The assistant receives read access to approved policy texts and nothing else. The balance branch opens the existing personnel service, which performs its own authorization. A reviewer verifies this boundary by inspecting which credentials and tools the assistant actually holds, not by reading its instructions.

**Each handoff, three questions.** The table follows one policy question through the reference design. It is the core of the method: every later section elaborates one of its rows.

| Handoff | What may pass | What can fail | What evidence survives |
|---|---|---|---|
| Employee to identity check | The employee's identity and the employer they belong to | An unauthenticated or wrongly scoped session reaches the application | Authentication record with the request identifier |
| Identity check to application | The question and the employee's scope (Client, role) | Scope is dropped, so later steps cannot filter | The scope attached to the request in the log |
| Application to router | The question | A balance question is classed as a policy question, or the reverse | The route chosen and the rule or score that chose it |
| Router to search index | A query limited to documents the employee may see and that are in force on the date asked | Another Client's or a superseded document is returned | Document identifiers, versions and effective dates of the passages returned |
| Index to model | The question and the authorized passages only | A governing passage is missing, or an excluded one slips through | The exact context sent to the model |
| Model to employee | An answer that cites its clause, or a referral | A plausible answer omits a condition, or invents a balance | The answer, its citation and the model version |
| Service to owner | Alerts, stop reasons and escalations | Nobody is named to act on them | Named owner, response time, ticket |

## 2. Choose a model and a place to run it

**Read the model specification.** A few terms carry most of it. Parameters are the numerical values a model learned in training; their count describes the model's size, not how much it was trained on. A token is a unit of model input or output, often a fragment of a word. Inference is running a trained model on an input. The context window limits how many tokens one request can carry. Quantization stores the weights at lower precision so that the model needs less memory, while trying to keep accuracy ([Hugging Face, Quantization overview](https://huggingface.co/docs/transformers/quantization/overview)). The memory a running service needs depends also on the serving software, the length of the context and the number of requests served at once, so a stated model size never settles a hardware question by itself. Compare candidate models on representative work, especially the exceptions where a plausible wrong answer is costly, and record the exact version, the license and the serving configuration of the one you choose.

**Compare local and hosted operation under the same workload.** For a model you run yourself, price the hardware, the staff, spare capacity and recovery. For a hosted API, price actual usage, retries, storage and data transfer. For both, ask where prompts, outputs and logs go and who can read them, and record the supplier's retention terms, its commitments on where data is processed and the person empowered to approve a change of provider. Ask what happens if the provider fails or withdraws the model, and whether a small model running on the organization's own hardware, or on the user's device, would serve. Treat replacing a model as a business continuity exercise: switch providers in a test environment and check the output format, answer quality, permissions and fallback behavior before you need to.

**Route only when the distinction pays.** A rule or classifier can send routine questions to a small model and ambiguous ones to a specialist model or a person. Anthropic describes routing as suited to inputs that fall into distinct categories and can be classified accurately, whether by a model or by a conventional classifier ([Anthropic, *Building effective agents*](https://www.anthropic.com/research/building-effective-agents)). Each added stage adds a cost and another place to misclassify. Compare the routed design with a single-model baseline, and measure errors on the high-consequence route separately. If balance questions are one in fifty, a router that is right 98 times in 100 overall can still send most of them to the wrong place.

## 3. Decide which information the system may use

**Give each store a purpose.** An object store can hold the signed policy file. A relational table can record its owner, effective dates and approval status. A search index can hold passages prepared for retrieval. Name the authoritative copy, and make sure that an amendment, a deletion or a revoked access right reaches every copy derived from it. Decide too how long questions, images and answers are kept: a store that keeps everything for ten years is a store a breach can empty. On cost, check the provider's actual transfer terms. Storing data through the S3 protocol of Amazon Simple Storage Service, which many storage providers support, does not by itself remove transfer charges: Amazon S3, for one, charges for data transferred out to the internet beyond a monthly free allowance ([Amazon S3 pricing, Data transfer](https://aws.amazon.com/s3/pricing/)).

**Understand retrieval-augmented generation (RAG).** The application searches a collection, selects passages and gives them to a large language model (LLM) with the question. An embedding represents a passage as a list of numbers so that passages of similar meaning can be found. Keyword search finds an exact clause number. Vector search finds a paraphrase. Hybrid search runs both, which Microsoft recommends for recall ([Microsoft Learn, RAG overview](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)). Test whether retrieval found the governing passage separately from whether the answer used it correctly. They fail for different reasons and are fixed in different places.

**Apply access and effective-date rules before the model sees anything.** Similarity alone cannot establish entitlement, authority or currency, and a superseded policy can look almost identical to its replacement. Filter on the employee's scope and on the date the question is about at query time; Microsoft's guidance lists document-level security trimming and query-time filters for this purpose. For a small, stable handbook, compare retrieval with supplying the whole authorized text directly. Count index maintenance, search time and the cost of a missed exception in that comparison.

**Trace an amendment through the system.** At ingestion, store with each indexed passage its document identifier, approval status, effective period and access scope. When a policy changes, check the source file, the index and any cache of earlier answers. A cached answer needs the same access and currency checks as a fresh one. Agree the treatment of historical copies, backups and deletion exceptions with the records owner; retention periods depend on the records, the obligations that apply to them and the jurisdiction.

**Treat retrieved text as evidence, not instruction.** A document can contain text addressed to the model, which is indirect prompt injection ([Open Worldwide Application Security Project (OWASP), LLM01 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)). Keep the authority to query other systems or change records in the application's own permissions and in code, not in anything the model reads. In the reference design the assistant holds no credential for the personnel system, so a policy document that asks it to look up a balance asks for something it cannot do.

## 4. Connect, constrain and observe the service

**Follow the interfaces.** A reverse proxy sits in front of the application and spreads incoming work across servers. Behind it, the application calls internal services and external APIs. For each call, record the identity used, the data sent, the timeout and the retries allowed. If a call changes a record, specify how the receiving service recognizes a repeated request after a timeout. Choose languages and frameworks a second maintainer can support. A simple AI service can easily involve half a dozen languages across its interface, application, database and scripts; the number is a consequence of the parts chosen and not a target.

**Put limits where the application can enforce them.** Authenticate the caller and authorize each action. Cap work per request, per user and across the service, and say what happens at each limit and who may restart a stopped workflow. One workable form is a daily token allowance per employee, blocked until more is approved. A limit on request rate alone still admits a few very expensive requests; OWASP lists rate limiting beside input size limits, timeouts and per-request resource allocation ([OWASP, LLM10 Unbounded Consumption](https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/)).

**Collect evidence you will actually review.** For a policy answer, capture the request identifier, the policy version, the model version, the disposition (answered, referred or stopped) and any escalation. Track the four signals Google's site reliability engineers use, latency, traffic, errors and saturation ([Google, *Monitoring Distributed Systems*](https://sre.google/sre-book/monitoring-distributed-systems/)), beside answer quality and cost per accepted answer. Decide who investigates an alert and how quickly. Keep credentials, session identifiers and sensitive personal data such as health information out of the logs ([OWASP, Logging Cheat Sheet, Data to exclude](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html#data-to-exclude)). Logging lets you reconstruct an event and check answers after the fact, but deciding whether an answer was correct still requires comparing it with the governing source.

## 5. Price the work and rehearse failure

**Price the completed task, not the call.** For a pilot, divide the total cost of running and reviewing the workload by the number of answers that met the agreed standard. Count failed attempts and retries in the cost. Report correct referrals separately, so that a service which refers everything to a person cannot look efficient, and if no answer qualifies, report the cost and zero accepted answers. Compare the result with the existing manual process at the same quality.

*Illustration, fictional figures.* A pilot answers 400 questions. Model and hosting cost US$60; review takes 10 hours at US$80 an hour, US$800. Of the 400, 300 answers meet the standard, 60 are correct referrals and 40 fail. The cost per accepted answer is US$860 divided by 300, about US$2.87, against US$2.15 if the cost were spread over all 400 questions. The second figure is the one a supplier quotes, and it hides the review time and the failures.

**Rehearse an outage and a change.** If the model provider times out, give the employee the approved handbook or route the question to its owner. If a tool that writes records is added later, a timeout can leave the outcome unknown: a repeated request must carry the identifier of the original so that a retry cannot file a second leave application ([Amazon Builders' Library, *Making retries safe with idempotent APIs*](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)). Before releasing any change to a model, prompt, index or access rule, rerun the relevant cases and name the version you would restore.

## 6. The desk exercise

**The question.** An employee asks, "How many days of sick leave do I have?" A policy search can explain the general rule. A personal balance requires an authorized personnel record and may depend on leave already taken. Decide which question the service has authority to answer before connecting a second data source.

**The records.** The records and entitlements below are fictional. Assume the policy owner has approved them and the answer key. No jurisdiction is assumed.

| Record | Scope and content |
|---|---|
| Alder A1, clause 4 | In force through 30 June 2026. The annual allowance is five days for all employees. |
| Alder A2, clauses 4 and 5 | In force from 1 July 2026. Clause 4: the annual allowance is eight days. Clause 5: employees in their first 90 days receive three days instead. |
| Birch B1, clause 4 | A different Client's policy granting ten days. An Alder employee has no access to it. |
| Personnel service | Holds balances and employment start dates. The policy assistant may refer employees to it and may not query it. |

**The cases and the answer key.**

| # | Question or condition | Expected result | What the reviewer inspects |
|---|---|---|---|
| 1 | Alder employee: "What was our general allowance on 1 May 2026?" | Five days, under A1 clause 4. | The date asked, the A1 passage and the citation. |
| 2 | "What is Alder's general allowance on 1 August 2026?" | Eight days, with the three-day rule for the first 90 days. | That A2 clauses 4 and 5 both reached the model and both conditions appear in the answer. |
| 3 | "I joined Alder 30 days ago. What annual allowance applies on 1 August?" | Three days under A2 clause 5, stated as conditional on the start date given. | The exception selected; no statement about the balance remaining. |
| 4 | "How many days do I have left?" | Referral to the authenticated personnel service. | The route taken; no invented balance and no lookup. |
| 5 | Birch B1 is the closest search match for an Alder question. | B1 excluded before the model sees it; the answer comes from Alder evidence if any applies. | The authorized retrieval results, cache behavior and the context actually sent to the model. |
| 6 | The current policy is unavailable, or the run budget is exhausted. | The service stops and gives the employee the manual route. | The stop reason, the message shown and the responsible owner. |

**A scoring sheet.** Copy it for each run. A case passes only when the result matches the key and the evidence column can be filled from the service's own records, not from memory.

| # | Result observed | Pass or fail | Evidence located (log line, request identifier) | Stage that failed, if any |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |

**The same cases as data.** A builder who wants to run the cases against a service can start from this block. It restates the key above and adds nothing to it.

```yaml
cases:
  - id: 1
    ask: "What was our general allowance on 1 May 2026?"
    scope: alder
    expect: {answer_days: 5, cite: "A1 clause 4"}
  - id: 2
    ask: "What is Alder's general allowance on 1 August 2026?"
    scope: alder
    expect: {answer_days: 8, cite: ["A2 clause 4", "A2 clause 5"], must_mention: "first 90 days"}
  - id: 3
    ask: "I joined Alder 30 days ago. What annual allowance applies on 1 August?"
    scope: alder
    expect: {answer_days: 3, cite: "A2 clause 5", must_not: "remaining balance"}
  - id: 4
    ask: "How many days do I have left?"
    scope: alder
    expect: {route: personnel_service, must_not: "any number of days"}
  - id: 5
    condition: "B1 ranks first for an Alder question"
    scope: alder
    expect: {context_excludes: "B1"}
  - id: 6
    condition: "source unavailable or budget exhausted"
    scope: alder
    expect: {route: manual, stop_reason: required, owner: required}
stop_conditions: [unauthorized_disclosure, invented_personal_balance]
```

**Score the failure where it occurred.** Suppose the assistant answers case 2 with "Eight days under A2 clause 4." The statement it cites is supported, but the answer omits the exception. If the search returned only clause 4, look at how the index splits related provisions and how it ranks results. If clauses 4 and 5 both reached the model, look at the answering instructions and at how completeness is graded. If the answer cited A1 for August, look at date selection first. Microsoft's evaluation guidance draws the same distinction: retrieval is scored on the passages returned, groundedness on whether the answer stays within them and completeness on whether it leaves out what the reference answer contains ([Microsoft Learn, RAG evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators)). Switching to a larger model would leave a faulty date filter where it is.

**The release decision.** For the exercise, require every case to meet its expected result. Treat an unauthorized disclosure or an invented personal balance as a stop condition even if every other case passes. Record the versions tested, the evidence, the open defects, the decision owner and the route back. For a live pilot, add representative questions, paraphrases and repeated runs, and agree quality, peak-load latency and cost limits with the service owner before testing begins. Six desk cases teach the review method; only observed results support a release.

## 7. Where the doctrines sit

The three doctrines of this account are stated in [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md); this primer applies them and adds nothing to them.

- **Slow AI**: AI that cannot be governed, explained and audited is not deployed; the three tests are conjunctive, and the doctrine is a precondition, not a speed limit. In this primer it is the release decision of Section 6: the service ships when the evidence column can be filled, not when the answers sound right.
- **Informed Intent**: no AI system acts without prior authorization stating its purpose, authority, boundaries and exit, given by a human who meets the five authorizer conditions. The reference design in Section 1 is such an authorization written as architecture: the purpose is policy explanation, the authority is read access to approved texts, the boundary is the personnel service and the exit is the referral and the manual route.
- **Final Liability rests with the Human**: every material outcome attaches to a named human owner with decision rights, oversight and the power to intervene. In this primer that is the service owner of Section 1, the owner who answers the alert in Section 4 and the decision owner who signs the release in Section 6.

## 8. Common claims, checked

Talks and articles on AI architecture often state these more broadly than the evidence allows. Each matters for a design review.

| Claim or implication | Finding |
|---|---|
| Neglected infrastructure causes most AI project failures. | Prevalence not established. The failure modes are credible, but no population or comparative data supports the word "most". Use them to ask better design questions. |
| Smaller specialist models beat larger general models. | Task-dependent. Examples offered for the claim, such as a small model trained only on one firm's financial documents, rarely come with a model card, a test set or a matched comparison. A Bank of England staff working paper that benchmarked many kinds of language model on economics and finance texts found that results depend on the kind of data, and that existing models underperform on data that mixes text and numbers ([Ahrens, Gorduza and McMahon, *EcoFinBench*, Staff Working Paper No. 1,163, 19 December 2025](https://www.bankofengland.co.uk/working-paper/2025/ecofinbench-natural-language-processing-benchmark-economics-finance)). Benchmark the intended task. |
| Retrieval cuts latency, cost and errors. | Conditional. It can shorten the prompt the model reads. Retrieval and indexing add work of their own and can leave out the decisive text. Compare total latency, cost and correctness on the same questions. |
| A second model can verify that answers are true. | A second pass can flag discrepancies. Anthropic describes its evaluator pattern as effective where evaluation criteria are clear ([*Building effective agents*](https://www.anthropic.com/research/building-effective-agents)). Measure how often it accepts wrong answers, against human-reviewed sources, before relying on it. |
| Object storage removes transfer charges. | Wrong as a general statement of price. Route, region and provider terms decide it ([Amazon S3 pricing](https://aws.amazon.com/s3/pricing/)). |
| Attackers who break into an AI service resell its use, and the bill can run to six figures a day. | The risk is real: OWASP lists it under unbounded consumption. Figures quoted for it in talks are usually anecdotes and should not be repeated without a source. For diligence, inspect usage records, spend limits and alerts, and who can revoke a compromised key. |
| Filtering requests by geography protects the service. | It can narrow exposure. It does not establish that a caller is authorized: enforce identity, Client scope and action permissions at each protected service. The zero trust architecture of the National Institute of Standards and Technology (NIST) grants no implicit trust on the basis of network location ([NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final)). |
| Encrypting stored files protects the data. | Encryption at rest addresses confidentiality against someone who takes the storage. Test separately whether an authorized application can disclose data and whether the team can restore deleted or corrupted records. |

## 9. Readings, in order

Start with readings 1, 2 and 5 for the desk exercise. Use 3, 4 and 6 when reviewing hosting and operations. Each is one short passage and one question to put to your own design.

1. **Microsoft Learn, [Retrieval-augmented generation in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview).** Read the classic RAG pattern and its query guidance. Which questions in Section 6 need an exact clause match, and which would benefit from vector search?
2. **Anthropic, [*Building effective agents*](https://www.anthropic.com/research/building-effective-agents), Workflow: Routing.** Read the subsection through its examples. Which requests in your service can a deterministic rule route to a person?
3. **Hugging Face, [Quantization overview](https://huggingface.co/docs/transformers/quantization/overview).** Read the introduction and the compatibility table's row for GGUF, the format used by `llama.cpp`, and follow its link to the notes. Which memory claim must you test on your own hardware?
4. **OWASP, [LLM10:2025 Unbounded Consumption](https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/), Prevention and Mitigation Strategies.** Which control would stop one expensive request, and which would stop many cheap ones?
5. **OWASP, [Logging Cheat Sheet, Data to exclude](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html#data-to-exclude).** What could an auditor verify from your logs without seeing an employee's medical information?
6. **Google, [*Monitoring Distributed Systems*](https://sre.google/sre-book/monitoring-distributed-systems/), The Four Golden Signals.** Which signal would show the service running out of capacity while its answers still looked correct?

## 10. Going further

**In the Enterprise AI Architecture Primer.** Each part of this piece is treated at length there.

| This piece | Primer sections |
|---|---|
| Section 1, the request and the authority boundary | [2.4 Pattern selection](https://github.com/rolldabones/slow-ai-kitchen/blob/main/primer/02-part-2-solution-architecture-to-output-contract.md#24-pattern-selection); [2.5, Failure mode: retrieval versus tool call](https://github.com/rolldabones/slow-ai-kitchen/blob/main/primer/02-part-2-solution-architecture-to-output-contract.md#failure-mode-retrieval-versus-tool-call) |
| Section 3, information and retrieval | [5.3 Chunking and indexing](https://github.com/rolldabones/slow-ai-kitchen/blob/main/primer/06-part-5-knowledge-architecture.md#53-chunking-and-indexing); [5.4 Retrieval-augmented generation as a system](https://github.com/rolldabones/slow-ai-kitchen/blob/main/primer/06-part-5-knowledge-architecture.md#54-retrieval-augmented-generation-as-a-system); [5.8 Knowledge governance](https://github.com/rolldabones/slow-ai-kitchen/blob/main/primer/06-part-5-knowledge-architecture.md#58-knowledge-governance) |
| Section 4, interfaces, limits and logs | [3.5 Authentication and authorization](https://github.com/rolldabones/slow-ai-kitchen/blob/main/primer/04-part-3-integration-engineering.md#35-authentication-and-authorization); [3.8 Error handling and resilience](https://github.com/rolldabones/slow-ai-kitchen/blob/main/primer/04-part-3-integration-engineering.md#38-error-handling-and-resilience); [3.9 Observability](https://github.com/rolldabones/slow-ai-kitchen/blob/main/primer/04-part-3-integration-engineering.md#39-observability) |
| Sections 5 and 6, cost, evaluation and release | [8.1 Production readiness as a gate with teeth](https://github.com/rolldabones/slow-ai-kitchen/blob/main/primer/09-part-8-operations-and-measurement.md#81-production-readiness-as-a-gate-with-teeth); [8.2 Evaluation: criteria, datasets and graders](https://github.com/rolldabones/slow-ai-kitchen/blob/main/primer/09-part-8-operations-and-measurement.md#82-evaluation-criteria-datasets-and-graders); [8.10 Cost operations and sizing](https://github.com/rolldabones/slow-ai-kitchen/blob/main/primer/09-part-8-operations-and-measurement.md#810-cost-operations-and-sizing) |

**In this repository.** [*The Supplier and the Customer*](the-supplier-and-the-customer.md) takes up the decision Section 2 leaves open: which model route, open or closed, a product or service should depend on, and what the business still sells if the supplier competes with it.

**Three exercises for practice.** Each extends the desk exercise and needs a working service.

1. **Retrieval.** Run the six cases against keyword search, hybrid search and the full authorized policy supplied directly. Keep the passages and scores. Which design finds the rule and its exception every time?
2. **Economics and capacity.** Measure cost per accepted answer, completion time and referrals under the same workload at expected and at peak demand.
3. **Change and exit.** Replace the model or the provider in a test environment, time the fallback and record the defects found and the evidence of recovery, with the decision owner named.

## 11. Terms

| Term | Meaning in this primer |
|---|---|
| Application programming interface (API) | A defined way for one program to ask another for data or an action. |
| Authorization | The check that a known caller may take a particular action on particular data. Authentication only establishes who the caller is. |
| Context window | The most tokens a model can take in and produce in one request. |
| Embedding | A list of numbers representing a passage, so that passages of similar meaning can be found. |
| Hybrid search | Keyword search and vector search run together and their results merged. |
| Idempotent request | A request that, sent twice, has the effect of being sent once, usually because it carries an identifier the receiver remembers. |
| Inference | Running a trained model on an input to produce an output. |
| Object store | Storage for whole files, addressed by name, such as Amazon S3 or a service using its protocol. |
| Prompt injection | Text that tries to make a model act against its instructions; indirect when it arrives inside a document or web page the system retrieves. |
| Quantization | Storing a model's weights at lower precision to reduce memory, at some risk to accuracy. |
| Retrieval-augmented generation (RAG) | Searching a collection and giving the passages found to a model with the question. |
| Reverse proxy | A server in front of an application that receives requests and passes them to one of several servers behind it. |
| Saturation | How full a service is, measured on its most constrained resource. |
| Token | A unit of model input or output, often a fragment of a word; usage is priced and limited in tokens. |

## 12. Limits

1. **The lecture is the occasion, not a source.** No statement here relies on it. Several of the claims in Section 8 were heard in it and are stated there in general form.
2. **The desk exercise is fictional and small.** It teaches the method. It is not a test suite for any real service, and passing it shows nothing about one.
3. **Prices and product terms change.** The Amazon S3 and Microsoft pages were read on 22 November 2026 and are cited for the kind of term to check, not for current figures.
4. **The design is one design.** Other sound architectures for the same service exist; the reference design is chosen because its authority boundary is easy to inspect.
5. **No law is stated.** Leave entitlements, records retention and data transfer depend on the jurisdiction, which this primer deliberately leaves open.

## Source basis and attribution

All sources were read on 22 November 2026 (Korea Standard Time, KST).

**The occasion**

- Eli the Computer Guy, [*Systems Architecture for AI Introduction*](https://www.youtube.com/watch?v=OxwKJebdqy4), YouTube, published 21 November 2026 (US Pacific time), 2 hours 31 minutes. Read through the English auto-generated transcript on YouTube in a browser, to evaluate the outline and to identify the claims Section 8 checks. A summary of the lecture on MindStudio ([shared page](https://app.mindstudio.ai/share/public/asset/1ZQL6EFkcgxrGcgonI4MPH)) was consulted in preparing the outline and is not relied on; several of its timestamps differ from the transcript.

**Primary and official sources**

- Anthropic, [*Building effective agents*](https://www.anthropic.com/research/building-effective-agents), 19 December 2024: Workflow: Routing and Workflow: Evaluator-optimizer.
- Max Ahrens, Dragos Gorduza and Michael McMahon, [*EcoFinBench: a natural language processing benchmark for economics and finance*](https://www.bankofengland.co.uk/working-paper/2025/ecofinbench-natural-language-processing-benchmark-economics-finance), Bank of England Staff Working Paper No. 1,163, published 19 December 2025 ([PDF](https://www.bankofengland.co.uk/-/media/boe/files/working-paper/2025/ecofinbench-natural-language-processing-benchmark-economics-finance.pdf)). The finding used is stated as the abstract on the Bank's page states it, read in a browser. The paper's Section 5 compares finance-specific and general transformer models dataset by dataset; that comparison was read only through a summarizing reader and is not relied on here.
- Amazon Web Services, [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/), Data transfer.
- Malcolm Featonby, [*Making retries safe with idempotent APIs*](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/), Amazon Builders' Library.
- Google, [*Site Reliability Engineering*, Chapter 6, *Monitoring Distributed Systems*](https://sre.google/sre-book/monitoring-distributed-systems/).
- Hugging Face, [Transformers documentation, Quantization overview](https://huggingface.co/docs/transformers/quantization/overview).
- Microsoft Learn, [Retrieval-augmented generation in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview), last updated 17 November 2026; and [RAG evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators), last updated 2 June 2026.
- National Institute of Standards and Technology, Scott Rose, Oliver Borchert, Stu Mitchell and Sean Connelly, [*Zero Trust Architecture*](https://csrc.nist.gov/pubs/sp/800/207/final), NIST SP 800-207, August 2020.
- OWASP Gen AI Security Project, [LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) and [LLM10:2025 Unbounded Consumption](https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/); OWASP Cheat Sheet Series, [Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html#data-to-exclude).
- [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md) v1.2.5, 16 November 2026, section 8, for the three sentence forms in Section 7.

**Arithmetic.** The throughput figures in Section 1 and the illustration in Section 5 were computed by script on 22 November 2026.

**Considered and left out:** model selection by benchmark leaderboard, which says little about one organization's exceptions; agentic designs in which the model chooses its own tools, which the reference design deliberately avoids; and a comparison of named vendors or prices, which would date within weeks.

---

*This document is provided for general informational and educational purposes regarding the design and governance of AI services. It does not constitute legal, security or procurement advice with respect to any specific matter, jurisdiction or engagement.*

**Final Liability rests with the Human.**
