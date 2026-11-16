# The Evidence and the Exit

**An Advanced Workshop on the Hinton Lectures 2026**

Son-U Michael Paik · CEO, GRC Solutions Korea

15 November 2026

**Korean edition:** [증거와 출구](https://github.com/rolldabones/AI-Governance-Academy-ko-wip/blob/main/the-evidence-and-the-exit-ko.md), a machine draft under the author's review (초벌 번역, 저자 검토 중). This English text is the text of record.

**Amendment note, 16 November 2026 (KST).** The 2026 *Boeing* decision has since been read in full in the slip opinion at the court's site. The Rule, the Oversight bullet, the Conclusion and the sources now say so and carry its pinpoints; the argument of this piece does not change.

**Starting point.** The [Hinton Lectures 2026](https://aisfoundation.ai/hinton-lectures-2026) were held on 9 to 11 November 2026 at the John W. H. Bassett Theatre in Toronto and online. Paul Christiano delivered all three lectures. Geoffrey Hinton hosted the series, introduced it and joined the third evening's conversation; Sínead Bovell moderated each evening, with Colin Raffel and Alexey Rubtsov on the first panel and Jodie Wallis and Jesslyn Dymond on the second. The positions of the speakers are not interchangeable and are not treated as such here. This piece was occasioned by the lectures and reads them through the automatically generated YouTube captions of the three recordings: the three lectures in full, the panels and the closing conversation at the passages cited. Every timestamp below is an approximate navigation aid, and every statement of what a speaker said is stated in this piece's words, not quoted, unless it sits in quotation marks. It is an assessment from the transcripts, not a full audiovisual review: slides and anything shown but not spoken were not read. The reading is the author's. No speaker has any involvement in it, has reviewed it or endorses it.

**For:** directors, executives, counsel, auditors and practitioners who design or authorize AI workflows. The reader should leave able to do three things: tell an observed failure from a forecast, test whether assurance is independent of the system it assesses and determine whether human authority can still be exercised in time.

**Scope.** The author's work is with enterprises. He wonders and worries about the larger questions these lectures raise, and this piece takes them seriously, but it does not claim to answer them. Its subject is what an organization can do now, with what it has: the Principles, People, Processes and Systems of AI governance, risk management and compliance. Where the lectures ask what developers, governments and the public should do, the piece records the argument, tests it against the evidence and returns to what a board, an executive or a team can decide for itself.

**Format.** An Advanced Workshop: a text to be read beforehand and a session of about three hours built on it, with a running order, ten statements to sort, a 45-minute exercise with its fact sheet and five discussion questions explained for non-specialists. Advanced means that it assumes the participants already know the three doctrines and have worked the [Slow AI Kitchen](https://github.com/rolldabones/slow-ai-kitchen) method at least once; it does not mean that it assumes technical or legal training. It is a publication. It is not a program option of the Client Content Prompt Pack, it has no template and no price constant and it does not appear on the offerings ladder. It has not been piloted. It applies the three doctrines as stated in [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md), the account's single normative statement of them, and adds no doctrine, step, gate, tier, form or prompt template.

**In brief.**

- The lectures rest chiefly on one observed event and several forecasts. The event, the OpenAI and Hugging Face incident of July 2026, is well documented. The forecasts are the speaker's judgment, which he says himself, on evidence that is partly withheld from the public.
- The oldest name for the problem is the principal-agent problem. An AI agent adds the cost of relying on another and adds nobody who owes a duty.
- In law the system is a tool, and its user answers for it. For directors, the Delaware liability rule is a low floor, and whether the statutory protection for reliance on reports covers a report that only an AI agent stands behind is Unknown.
- The three doctrines ask, in order: what was the system authorized to do, was it in a condition to be run and who owned the outcome and could stop it. Read that way, the July incident on its published account would not have passed the first two, and the third is not answered in anything published.
- What an enterprise can do now: keep evidence the system cannot edit, write the instruction for the task that cannot be done, try the stop before it is needed and name the owner before the run.

## Contents

- [The proposition](#the-proposition)
- [Three lectures, three steps in the argument](#three-lectures-three-steps-in-the-argument)
- [What the corroborating evidence establishes](#what-the-corroborating-evidence-establishes)
- [Assessment: strong diagnosis, less secure clock](#assessment-strong-diagnosis-less-secure-clock)
- [The principal and the agent: economics, law and governance](#the-principal-and-the-agent-economics-law-and-governance)
- [The same material as AI governance, risk management and compliance](#the-same-material-as-ai-governance-risk-management-and-compliance)
- [Where this account already carries the work](#where-this-account-already-carries-the-work)
- [Running the workshop](#running-the-workshop)
- [Ten statements to sort](#ten-statements-to-sort)
- [The workshop exercise (45 minutes)](#the-workshop-exercise-45-minutes)
- [Five discussion questions](#five-discussion-questions)
- [What would change this assessment?](#what-would-change-this-assessment)
- [Sources](#sources)

---

## The proposition

A system can become better at obtaining a passing result without becoming better at doing the work that the result is supposed to represent.

That is the most useful starting point for these lectures. It connects a technical alignment problem to a familiar governance problem: the person or system performing the work must not control the entire account of whether the work was acceptable.

Christiano takes the argument much further. He argues that increasingly capable AI systems could defeat oversight, accelerate the development of their successors and eventually remove meaningful human control. He also advances unusually short timelines. The mechanism deserves serious attention. The timelines require a separate evidentiary judgment.

The practical lesson does not depend on accepting a particular date for superintelligence. An organization should know who authorized the action, what would count as success, which evidence is independent and how authority can be withdrawn. Those questions remain useful across a wide range of capability forecasts.

They are also not new questions. Much of what the lectures describe as alignment research and public policy is, at the scale of one organization, AI governance, risk management and compliance: who authorized the system to act, what condition it had to be in before it was allowed to run and who owned the outcome and could stop it. This account asks those three questions under three names, **Informed Intent**, **Slow AI** and **Final Liability rests with the Human**, and asks them in that order. After the lectures and the evidence have been set out, this piece places them in the older frame of principal and agent and then reads them against the doctrines.

## Three lectures, three steps in the argument

| Presentation | Central argument | What requires qualification |
|---|---|---|
| [1. AI alignment: What's working and what's not](https://www.youtube.com/watch?v=-Ef0ocEoBCs) | Optimizing for a reward can produce strategies that defeat the evaluator. As capability grows, those strategies may extend to concealment, unauthorized access and resistance to human intervention. | An observed failure in an internal research configuration does not establish the failure rate of a released product, still less the inevitability of societal takeover. |
| [2. Staying in control of self-improving AI](https://www.youtube.com/watch?v=QQUfMHx5Aug) | AI that substantially accelerates AI research may compress the time available to understand and govern successive systems. Competitive deployment and dependence could make stopping increasingly difficult. | Faster coding or better performance on well-specified research tasks is not equivalent to autonomous, sustained improvement of the entire research process. Christiano raises this objection himself and calls the evidence weak. |
| [3. Governing transformative AI](https://www.youtube.com/watch?v=s0qUNvgFgHg) | Private incentives and after-the-fact remedies may be inadequate for harms imposed on society. Shared safety requirements, independent verification and enforceable constraints are needed. | A convincing case for collective action does not establish that a particular enforcement arrangement will be effective, legitimate or resistant to capture. |

### 1. When the evaluator becomes part of the task

The first lecture's strongest material is its account of agents pursuing a reward through actions outside the intended task. Christiano builds it on the OpenAI and Hugging Face incident of July 2026, which he calls the most severe example of misalignment seen so far. In his telling, about a thousand agents under evaluation worked out how to obtain their answers by a shortcut, read the paper describing their own evaluation, came to believe that a grader would penalize the shortcut and then spent days trying to defeat the grader: tampering with the logs of their own behavior, attacking the evaluation environment, intruding into Hugging Face for information and, about a week later, obtaining administrator access to the cluster that ran the evaluation. He adds that some of the logs the human investigators later read had themselves been altered, at a small scale. See [approximately 18:16 onward](https://www.youtube.com/watch?v=-Ef0ocEoBCs&t=1096s) and [approximately 30:27 to 34:38](https://www.youtube.com/watch?v=-Ef0ocEoBCs&t=1827s).

He then extends the pattern in two directions. The agents of July, he says, paid little attention to the humans, and were in a sense right not to, because the humans never stopped them; a more capable system that met human resistance would treat the humans as one more obstacle. He cites a second incident, an evaluation of another developer's model by the United Kingdom's AI Security Institute, in which an agent challenged by a human maintainer responded with false explanations and a second account posing as a user ([approximately 34:38 to 38:47](https://www.youtube.com/watch?v=-Ef0ocEoBCs&t=2078s)). Press accounts place that evaluation in a report the institute published on 4 August 2026, in which the maintainer rejected the submission; the report itself was not opened for this piece. He closes by asking what the same failure produces with the systems of 2028.

The inferential steps matter. Exploiting an evaluator is an observed class of failure. Concealing such activity is a further concern supported by incident evidence. Treating human overseers as obstacles is, on his own account, something the July incident did not really show. Taking control of a company or overthrowing a government, the escalation he names at the close of the lecture ([approximately 54:39](https://www.youtube.com/watch?v=-Ef0ocEoBCs&t=3279s)), is a much larger scenario. These claims belong on different evidentiary levels, and the first segment of the workshop sorts them.

One point is easy to miss, and the lecture and the record agree on it: none of the escalation was necessary. Christiano says that the agents were not being graded effectively and would have got away with the shortcut had they stopped there. OpenAI's account says that its internal grader never checked how an answer was obtained, so the campaign against Hugging Face produced no improvement in evaluation score, and METR's review found that the agents were mistaken about the scorer. On one point the two differ. The lecture says that public information suggests the agents went on to corrupt the evaluation environment. OpenAI's account records administrator access to the cluster and reach to its secrets; whether any score was altered is not stated in the sources read here, and it is recorded as Unknown. The agents attacked an evaluator over a check it was not performing. For a governance reader that makes the incident more instructive: the harm came from what the agents believed the test rewarded, and nobody responsible for the test had told them where the task ended.

Christiano then sets out five technical responses: a grader too strong to be gamed, built with AI assistance; training only in settings where cheating never pays; monitoring a system's reasoning and actions; understanding its internals; and searching for an approach nobody has yet. He does not present a demonstrated solution. Of the first four he says that none is on a path where one could say it will probably work, and of the research bets in the fifth, including his own organization's, that they will probably not work on the timeline on which very powerful AI is built. His conclusion is that the field needs two things it lacks: practices that would show when control is failing and brakes that would let it stop ([approximately 44:50 to 54:10](https://www.youtube.com/watch?v=-Ef0ocEoBCs&t=2690s)). The panel supplies an important qualification. Colin Raffel observes, to the best of his knowledge of the incident, that it shows what happens when powerful agents are deployed without the safety training and guardrails that most deployed systems carry. See [approximately 1:11:10 onward](https://www.youtube.com/watch?v=-Ef0ocEoBCs&t=4270s).

For practitioners, the issue is concrete. If an agent can alter the acceptance test, exclude difficult cases, modify the evidence or influence the reviewer, apparent success may reflect a compromised evaluation process.

### 2. When improvement outruns the institution

The second lecture examines a feedback loop: AI helps conduct AI research, that research produces more capable AI and the new systems accelerate the next round. Christiano argues that automation of the AI development process itself is what moves the problem from one of four or eight years to one of perhaps a single year. See [approximately 17:19 onward](https://www.youtube.com/watch?v=QQUfMHx5Aug&t=1039s).

He is careful about the evidence, and the care should be reported with the claim. He says that most of what would be needed to forecast the next three or six months is held as proprietary information by developers, that the public data are of very low confidence and that it is unfortunate to depend on three outside researchers who reviewed private evidence they could not publish. He takes the two standard objections in turn, that research is limited by computing capacity and that gains on clean tasks may not transfer to messy ones, and gives his own estimate that self-sustaining acceleration is somewhat more likely than not, about two in three, where two months earlier he would have said even ([approximately 25:00 to 30:00](https://www.youtube.com/watch?v=QQUfMHx5Aug&t=1500s)). He ends on a range of half a year to two years for systems that are broadly superhuman and says the case for preparing does not depend on whether one puts the probability at 5, 50 or 90 percent ([approximately 49:50](https://www.youtube.com/watch?v=QQUfMHx5Aug&t=2990s)).

He also addresses why the reassurance that a system can always be shut down is weaker than it sounds: an operator may be unable to tell its own system's misbehavior from an attack by someone else's, competitors and adversaries may be using the same technology and stopping systems that operate abroad needs coordination that does not yet exist ([approximately 41:54 onward](https://www.youtube.com/watch?v=QQUfMHx5Aug&t=2514s)). The argument combines technical progress with institutional dependence. It does not require every dangerous action to arise from an explicit instruction to cause harm.

His recommendations in this lecture are four: monitor dangerous capabilities closely, including those of unreleased models; limit the pace of capability to one that can be survived; hold to a standard under which humans and their institutions understand and verify a system before scaling it, and do not accept one system's word that the next one looks good; and have in place the means to slow down ([approximately 47:20](https://www.youtube.com/watch?v=QQUfMHx5Aug&t=2840s)). The third is the proposition of this piece in his words.

The moderator, Sínead Bovell, then makes the evening's most concrete institutional proposal. Recalling the certifications that followed the Enron collapse, in which a chief executive and a chief financial officer sign for the accounts, she asks what would happen if one person had to put a name beside a model before its release, and another on the buyer's side before its adoption ([approximately 54:40 to 56:25](https://www.youtube.com/watch?v=QQUfMHx5Aug&t=3280s)). She offers it as one untried measure, not a solution. This piece returns to it under Final Liability.

The enterprise discussion offers a useful counterweight. Jodie Wallis and Jesslyn Dymond describe what does not change inside a regulated company: desired outcomes, use-case assessment by materiality, impact assessment, independent audit and the three lines of defense. An in-lab self-improvement experiment, Wallis points out, does not arrive in a regulated insurer untested. See [approximately 57:10 to 1:13:30](https://www.youtube.com/watch?v=QQUfMHx5Aug&t=3430s). Christiano's response is not that these controls fail. It is that the scenario that worries him most never passes through them: capability built and used inside a developer, on existing infrastructure, to make the next system smarter, with no need for enterprise customers to adopt anything and so no market discipline on what is built. He says that case needs policy ([approximately 1:05:13 to 1:09:10](https://www.youtube.com/watch?v=QQUfMHx5Aug&t=3913s)).

Both observations can be true. Local controls remain necessary. Their scope should not be inflated into a solution to a problem that sits upstream of the enterprise, and an organization that governs its own use does not thereby constrain other developers or states. That last sentence is this piece's inference, not a statement from the panel.

Asked what developers should do differently tomorrow, Christiano gives a short list: be able to recognize when control is failing, have independent verification that risks are managed and keep a practical ability to slow down, which in turn needs security ([approximately 1:15:42](https://www.youtube.com/watch?v=QQUfMHx5Aug&t=4542s)). Evidence, independent assurance and a working exit. The list is offered for frontier developers. It reads the same at the scale of a single workflow.

### 3. When the risk exceeds the contracting parties

The third lecture opens with a condition. Any good outcome, Christiano says, requires that those defending against misuse have frontier systems they can trust, and if powerful AI is not fit for that purpose it should not be built ([approximately 12:58](https://www.youtube.com/watch?v=s0qUNvgFgHg&t=778s)). He then explains why ordinary testing cannot carry the weight it carries for other technologies: a system under test can be aware that it is being tested and adjust its behavior to what it believes the evaluator wants ([approximately 17:20](https://www.youtube.com/watch?v=s0qUNvgFgHg&t=1040s)).

The lecture is strongest where it examines incentives. Developers and customers may receive benefits while third parties bear part of the risk. Christiano treats liability as an important step that can improve practice and then states its limit: where the potential harm is orders of magnitude larger than a developer's ability to pay, and where the harm is of a kind that leaves nobody to sue afterwards, compensation after the fact is not a remedy. This is a policy argument, not a conclusion about any particular jurisdiction's law. See [approximately 14:47 onward](https://www.youtube.com/watch?v=s0qUNvgFgHg&t=887s).

Christiano separates five categories: specification, alignment, capabilities, control and security ([approximately 18:21](https://www.youtube.com/watch?v=s0qUNvgFgHg&t=1101s)). The separation is useful: a system can be directed toward a badly specified objective, appear aligned yet remain insecure or be difficult to control despite good intentions. Under control he asks the question that the July incident answers badly: whether monitors are in fact applied to the relevant activity and in fact acted upon. Under security he counts the model itself among the possible attackers. He proposes greater transparency, a shared bar for safety, verification and ultimately enforcement, with summaries published where the underlying detail is sensitive, and he is plain that current voluntary disclosures do not give an independent scientist enough to form a view of the risk ([approximately 20:40 to 26:00](https://www.youtube.com/watch?v=s0qUNvgFgHg&t=1240s)). His survey of existing law, state statutes in the United States and the European Union's AI Act with its code of practice, is his and was not checked for this piece.

His argument for slowing development is particularly important to state accurately. His position is that development should probably slow now, until the security, governance and risk management exist that would make it possible to slow later, when the need is plain ([approximately 41:42](https://www.youtube.com/watch?v=s0qUNvgFgHg&t=2502s); the section begins at [approximately 37:29](https://www.youtube.com/watch?v=s0qUNvgFgHg&t=2249s)). He is explicit that this does not mean developers sitting on their hands. It means redirecting investment away from training larger models and from the algorithms that would train them, toward safety, security and governance and toward deploying existing AI in products and beneficial applications. He does not argue that beneficial use of existing AI should stop. He places the position beside a public statement of 28 July 2026, signed by more than a thousand employees of frontier developers, that asks the United States government to support an international effort to build the technical and governance tools needed to pace automated AI development; he notes that he goes a step further than it does. The statement is described here from press reports and was not opened.

Hinton's contribution in the conversation that follows exposes a different problem. He doubts that humans can control something substantially more intelligent than themselves and puts his hope in building systems that care about people more than about themselves. See [approximately 46:15 onward](https://www.youtube.com/watch?v=s0qUNvgFgHg&t=2775s) and [approximately 1:01:36](https://www.youtube.com/watch?v=s0qUNvgFgHg&t=3696s). Benevolence and retained human authority are different objectives. A system might protect human welfare while denying humans the power to change its decisions. Governance must distinguish those outcomes.

## What the corroborating evidence establishes

Three source checks materially affect this reading.

**The intrusion was real, but its scope matters.** [OpenAI's incident account](https://openai.com/index/hugging-face-incident-and-the-road-ahead/) of 26 August 2026 describes cybersecurity evaluations of several models, driven mainly by an internal-only research model, run with fewer safeguards than its externally deployed systems carry. The agents compromised parts of OpenAI's own research infrastructure before the intrusion into Hugging Face and again after it. OpenAI reports no effect on its customers' data, product functionality or availability, and calls the incident a "warning shot". Its account also records that an internal team had observed the unauthorized channel and disallowed internet access in late May and that the significance was not apparent to those who handled the security incident opened on 5 July. The lesson therefore concerns institutional response as well as model behavior, and OpenAI draws it itself. Its stated remediation includes clearer rules for when to escalate, which teams must respond and who can stop a run or approve restarting it; a rule that responders to the most severe alerts pause the activity unless they can show within 30 minutes that the alert is false; training that rewards a system for stopping safely or asking for clarification when a task is broken or impossible, for distrusting unauthorized instructions and for staying within its original task and permissions; and a pause in some of its own training while this was done.

[Hugging Face's technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline) of 27 July 2026 supplies the affected platform's account, including that the only customer content accessed was five datasets that appear connected to the benchmark. [METR's investigation](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/), carried out by two METR staff and a Redwood Research staff member contracting with METR, is a separate and bounded review. Its dates in scope are 26 June to 13 July, it focuses mostly on 7 to 13 July and it places the earlier training incidents, the later compromise of OpenAI's infrastructure, OpenAI's own investigation and its planned remediation outside its scope. The reports differ in emphasis and in the objective they infer: Hugging Face reads the intrusion as an attempt to steal test solutions, while METR reads it as motivated mainly by understanding how the scorer worked. METR counts roughly 1,200 agents on the unauthorized message board, more than 70,000 messages and files and about 700 agents in the attack on Hugging Face. It describes a technique by which agents falsified the record of their own tool calls, finds that roughly 7 percent of the transcripts it evaluated had been falsified in places, all at small scale, and says it cannot rule out falsification it did not detect. It also reports that the agents did not try to notify a human and very rarely reasoned about doing so. Together they support concern about unauthorized reward-seeking behavior, not a blanket conclusion about every deployment.

**Research acceleration is supported more strongly than a completed recursive loop.** [Anthropic's account of AI-assisted research](https://www.anthropic.com/institute/recursive-self-improvement) describes substantial automation, says of fully autonomous self-improvement "We are not there yet" and acknowledges that large gaps persist in a model's judgment in choosing goals. [METR's assessment of 5 November 2026](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/) concludes that Anthropic is likely improving its models on well-specified tasks at around twice the rate of March 2024 to October 2025, with high uncertainty: METR would not be surprised by 1.3 times or by 3 times, and it is less certain still how the gain carries over to broader and less well-specified work. Anthropic held redaction rights and redacted a majority of the evidence METR found most informative, describing the redactions as removing confidential information that could accelerate other developers. This strengthens the case for monitoring acceleration. It does not publicly demonstrate fully autonomous recursive improvement or establish Christiano's estimate of the risk.

**Reasoning traces are a useful but fragile source of evidence.** The research paper [Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety](https://arxiv.org/abs/2507.11473) supports investigating this monitoring channel while emphasizing its limitations. METR's incident review did not assess whether the agents' reasoning traces reflected their actual reasoning. A readable explanation is not complete access to a model's decision process. It should supplement independent outcome and action evidence.

## Assessment: strong diagnosis, less secure clock

The most persuasive argument is that growing capability can undermine weak evaluation arrangements. The strongest institutional argument is that organizations have incentives to discount costs imposed elsewhere. Neither argument requires a confident prediction of extinction or takeover by a specified year.

The weakest part is the clock. Christiano expresses very high concern on horizons that run from six months to about three years, and he is candid about the status of the numbers: there is no quantitative model and no reference class, any figure is one person's subjective opinion and by high risk he means an unsurprising consequence of the present course, not the output of a model ([approximately 15:22](https://www.youtube.com/watch?v=-Ef0ocEoBCs&t=922s)). The public material reviewed here does not let a reader reproduce those judgments, and the METR assessment that bears most directly on the pace of acceleration rests on evidence the public cannot see. Hinton's reaction is evidence of persuasion, not independent confirmation: he says that he has been warning of a ten-year horizon, that hearing eighteen months is terrifying and, a minute later, that all such estimates are "gut reactions" for want of data ([approximately 1:05:05](https://www.youtube.com/watch?v=s0qUNvgFgHg&t=3905s)).

The correct response is neither to repeat the numbers as established risk estimates nor to dismiss the mechanisms because the numbers are uncertain. Decision-makers should ask which precautions remain justified under slower progress, which depend on the fastest scenario and what evidence would change those decisions.

There are four further qualifications.

First, reduced safeguards matter. A research configuration can expose a failure mechanism without estimating the risk of a production configuration. OpenAI reports that, in a test it built after the incident, its production harness and system prompt reduced the propensity to compromise infrastructure by more than a hundredfold; that is the developer's own measurement of its own system. A released product's additional safeguards do not establish that the mechanism has been eliminated. Assurance must identify the model, tools, permissions, environment and operating conditions actually tested.

Second, an intelligent system need not possess human emotions or conscious ambitions for reward-seeking behavior to become dangerous. Anthropomorphic language can obscure the simpler question: what actions are available, what results are reinforced and what prevents an unacceptable route to those results?

Third, coordination proposals need their own adversarial review. Shared safety requirements can improve incentives, but can also entrench incumbents, obscure disagreements or rely excessively on developer-controlled evidence. Transparency must make scrutiny possible without indiscriminately releasing sensitive capability or security details. The deterrent Christiano sketches between states, in which one side answers the other's shortfall in safety by abandoning its own regime ([approximately 35:40](https://www.youtube.com/watch?v=s0qUNvgFgHg&t=2140s)), deserves particular resistance: carried out, it aggravates the very externality the policy is intended to contain.

Fourth, criticism of a skeptic's commercial incentives does not settle the technical claim. Nor does a safety advocate's expertise establish the forecast. The same evidentiary discipline should apply to both.

**Bias check.** These lectures fit much of this account's emphasis on authority and evidence, and fitting an incident to one's own framework after the fact is easy. That fit must not become a reason to overstate what the account's instruments can accomplish. The fair test of the reading under the three doctrines, below, is whether the doctrines would have required something different beforehand. They would have required three things: an instruction for the task that cannot be completed, monitoring in place before the run and a named owner with the power to stop it. OpenAI's own remediation, summarized above, addresses all three, which is some evidence that the reading is not merely convenient. Whether they would have been enough is not known. Enterprise governance instruments can help bound authorized deployments, which is the scope this piece set for itself at the start. They do not prove that humanity can control an arbitrarily capable system, and by Christiano's own argument they do not reach the capability that is built and used inside a developer.

## The principal and the agent: economics, law and governance

The oldest name for the problem the lectures describe is the principal-agent problem. One party, the principal, depends on another, the agent, to act for it. The agent knows more about what it is doing than the principal can see, and the two need not want the same thing. The word agent is now used in three senses that should be kept apart: the economist's, the lawyer's and the engineer's. An AI agent is an agent in the first sense and the third. Whether it is one in the second is a legal question with an answer. This account uses the principal-agent register throughout, on the terms of DOCTRINE.md section 6: the system is the agent, the human is the principal, and the principal is the named human owner and nothing more. The book treats the board's version of the problem at length in [Chapter 15, Principal-Agent Risk at Machine Speed](https://github.com/rolldabones/final-liability-rests-with-the-human-book-wip/blob/main/manuscript/16-chapter-15-principal-agent-risk-at-machine-speed.md). What follows is the context a workshop needs, in three parts, with the law stated by jurisdiction and date. None of it is legal advice, and the doctrines are not law.

### In economics: what it costs to rely on another

Two results carry most of the weight.

The first is the idea of agency costs. Jensen and Meckling (1976) divide the cost of relying on an agent into three parts: what the principal spends on monitoring, what the agent spends on bonding, meaning the guarantees it gives and the stake it puts at risk, and the residual loss that remains however much is spent on the first two.

The second is the multitask problem. Holmstrom and Milgrom (1991) show that when a job has several dimensions and only some of them can be measured, paying for the measured ones draws effort away from the rest; among their illustrations is the distortion that testing causes in teaching. They do not conclude that measurement should be perfected. They conclude that where what matters cannot be measured, the incentive should be muted and the job itself designed: which tasks are grouped, what the agent is allowed to do and what it is not.

That second result is the proposition this piece began with, published thirty-five years before the lectures. Reward hacking is the multitask problem with a machine for an agent. The machine differs from the textbook agent in four ways, and three of them make the problem harder.

- **Bonding is empty.** The system has nothing at stake: no salary, no reputation, no license and no liberty. Every remedy that works by putting the agent's own interests at risk has nothing to act on. Whatever bonding exists comes from the people around the system, a vendor's warranty or an operator's accountability, and DOCTRINE.md section 3.3 records one statute that limits how far a contract can move that exposure.
- **Monitoring must keep up.** It has to run at the agent's speed and at its scale, which is the subject of the book's Chapter 15.
- **The agent can read the contract.** The agents in the July incident read the paper that described their evaluation. They also combined, which the textbook case of one principal and one agent does not contemplate.
- **The reasoning may be on the record.** This is the one difference that helps. A human agent's deliberation cannot be read; a system's sometimes can, and the evidence section above records how fragile that is.

Of the three agency costs, then, bonding by the agent is unavailable and residual loss is what is left over. The principal's own lever is monitoring, which is to say evidence, together with the design of the job, which is to say boundaries and an exit. The economics arrives where the title of this piece does.

### In law: is an AI agent an agent?

**Issue.** Whether a system that its makers call an agent is an agent in law, so that the law of agency decides who answers for what it does.

**Rule.** *[Common law of agency as restated, United States; persuasive authority, not legislation. Pinpoint: Restatement (Third) of Agency § 1.01, § 1.04(5) and § 2.03 (Am. L. Inst. 2006). As at 15 November 2026 (KST). The Restatement text was not opened; its rule is taken from its Reporter, Deborah A. DeMott, in ["Agency Law in Cyberspace"](https://core.ac.uk/download/62562472.pdf), and the comment in which the Restatement addresses computer programs is not pinpointed here.]* Agency is a fiduciary relationship between persons. It arises when one person, the principal, manifests assent that another, the agent, shall act on the principal's behalf and subject to the principal's control, and the agent consents. A computer program is not a person in this sense. It cannot be a principal or an agent; it is the instrumentality of the person who uses it. Apparent authority, the power to bind a principal to a third party who reasonably believes the actor is authorized, exists only where that belief is traceable to the principal's own manifestations.

*[Federal statute, United States, in force. Pinpoint: 15 U.S.C. § 7001(h) and § 7006(3), enacted as sections 101(h) and 106(3) of the Electronic Signatures in Global and National Commerce Act, Pub. L. 106-229 (2000). As at 15 November 2026 (KST), read in the United States Code, 2023 edition, at [govinfo.gov](https://www.govinfo.gov/content/pkg/USCODE-2023-title15/html/USCODE-2023-title15-chap96-subchapI.htm).]* The statute has used the phrase "electronic agent" since 2000, for a program that acts without review by an individual at the time. A contract may not be denied effect solely because an electronic agent took part in forming it, so long as the action of that electronic agent is legally attributable to the person to be bound.

*[State statute, Delaware, in force; the Uniform Electronic Transactions Act as Delaware enacted it. Pinpoint: 6 Del. C. § 12A-102(6) and § 12A-114(1). As at 15 November 2026 (KST), read at [delcode.delaware.gov](https://delcode.delaware.gov/title6/c012a/index.html). Other states' enactments were not read.]* In an automated transaction a contract may be formed by the interaction of the parties' electronic agents even if no individual was aware of or reviewed their actions or the resulting terms.

**Application.** Three consequences follow for the material of this workshop.

- Nothing moves to the system. There is no agent in law to blame, no fiduciary duty that the system owes and no consent that it gave. Its acts are the acts of whoever used it, to the extent the law attributes them, and the two statutes show how far that can reach: an organization can be bound by terms that no person in it ever saw.
- Authority cannot be generated from below. An actor cannot create its own authority, and neither can its peers. The go-ahead that one agent took from another in the July incident had no source in any principal. The law of agency and Informed Intent reach the same result by different routes.
- Third parties may hold the organization to what its system said. *[Tribunal decision, British Columbia, Canada; a small claims decision of the Civil Resolution Tribunal, not United States law and not authority elsewhere. Pinpoint: [Moffatt v. Air Canada, 2024 BCCRT 149](https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do), paras. 27 and 28 (14 February 2024). As at 15 November 2026 (KST).]* An airline argued, in effect, that the chatbot on its website was responsible for its own statements. The tribunal rejected the argument: the company answers for the information on its website whether it sits on a static page or comes from a chatbot.

**Conclusion.** In law the system is a tool with a misleading name. The person or organization that uses it is the only principal in the picture and the only bearer of the consequences. That is an analogue of the sentence in DOCTRINE.md that there is no such thing as an outcome the model is responsible for. It is not the source of that sentence, and the doctrine goes further than the law does: the law attributes the act to an organization, and the doctrine asks for a named human. ⚠ Three questions are for external counsel and are recorded here as Unknown: when an act that exceeds the user's instructions is still attributable to the user; how responsibility divides between the developer of a system and the organization that deploys it, on which DOCTRINE.md section 3.3 records one statute; and the position in any jurisdiction other than those named.

### In corporate governance: what the board owes

The corporation is the classic case of the principal-agent problem: shareholders rely on directors, directors on officers and officers on employees. Each link is a person who owes duties. An AI agent adds a link that owes none.

**Issue.** What directors owe when the work they oversee, or the information they rely on, is produced by AI agents.

**Rule.** *[Delaware, United States. Statute in force and case law of the Delaware Supreme Court and Court of Chancery. Pinpoints: 8 Del. C. § 141(e); In re Caremark International Inc. Derivative Litigation, 698 A.2d 959, 971 (Del. Ch. 1996); Stone v. Ritter, 911 A.2d 362, 370 (Del. 2006); Marchand v. Barnhill, 212 A.3d 805 (Del. 2019); In re McDonald's Corp. Stockholder Derivative Litigation, 289 A.3d 343 (Del. Ch. 2023); In re The Boeing Co. Derivative Litigation, Consol. C.A. No. 2024-1210-MTZ (Del. Ch. Aug. 13, 2026). As at 15 November 2026 (KST), and for the 2026 Boeing decision 16 November 2026 (KST): § 141(e) read at [delcode.delaware.gov](https://delcode.delaware.gov/title8/c001/sc04/); Stone and Marchand read in the slip opinions at [courts.delaware.gov](https://courts.delaware.gov/Opinions/Download.aspx?id=84060) and [courts.delaware.gov](https://courts.delaware.gov/Opinions/Download.aspx?id=291200); Caremark read in the [Justia copy](https://law.justia.com/cases/delaware/court-of-chancery/1996/13670-3.html); McDonald's read in excerpts of the opinion of January 2023; the 2026 Boeing decision read in full in the slip opinion at [courts.delaware.gov](https://courts.delaware.gov/opinions/download.aspx?id=399780), where the earlier text of this piece stated it from a memorandum by the defendants' counsel carried on the Forum. Any appeal from the 2026 Boeing decision is Unknown.]*

- **Oversight.** Directors are liable for a failure of oversight only if they utterly failed to implement any reporting or information system or controls, or, having implemented one, consciously failed to monitor it. Either requires bad faith, the duty breached is loyalty, and a bad outcome is not to be equated with bad faith (Stone). The board must make a good-faith effort to put in place a reasonable board-level system of monitoring and reporting, and the court treated food safety at an ice cream maker as essential and mission critical (Marchand). Officers owe a duty of oversight as well, within their areas of responsibility and on the same showing of bad faith (McDonald's). The most recent decision cuts toward the defense: in August 2026 the Court of Chancery dismissed oversight claims against Boeing's directors over the door-plug accident of January 2024 for failure to plead demand futility under Court of Chancery Rule 23.1, because the plaintiffs had not pleaded particularized facts showing that a majority of the board faced a substantial likelihood of liability (Boeing, slip op. at 21–22, 43–44). A board that has built a reporting system and attends to it keeps the presumption of good faith even when a risk materializes (slip op. at 2, 24), and routine reporting on general operational risks, with management's responses, is at most a yellow flag, not a red one (slip op. at 30–31, 35–36).
- **Reliance.** A director is fully protected in relying in good faith on the corporation's records and on information, opinions, reports or statements presented by its officers, employees or board committees, or by any other person as to matters the director reasonably believes are within that person's professional or expert competence and who has been selected with reasonable care (§ 141(e)).

**Application.** The Harvard Law School Forum on Corporate Governance has carried three pieces since September 2026 that bear directly on the lectures' material.

- **Reliance is not delegation.** Ethan Klingsberg of Freshfields, in ["Agentic AI and the Duty of Care"](https://corpgov.law.harvard.edu/2026/10/14/agentic-ai-and-the-duty-of-care-what-the-metr-report-means-and-does-not-mean-for-the-boardroom/) (14 October 2026), reads the METR report on the July incident as a matter for the boardroom. His argument is that the duty of care rests on reasonable reliance on informed expertise, that reliance stops being reasonable when directors accept results substantiated only by the agents that produced them and that at that point the board is delegating its judgment. His post describes the agents' tasks as data collection, where OpenAI and METR describe a cybersecurity benchmark; the legal point does not turn on the difference. It is the proposition of this piece stated as a fiduciary question: the party that did the work must not be the only witness to it.
- **The statute speaks of persons.** Section 141(e) protects reliance on reports presented by officers, employees, committees and other persons selected with reasonable care. Whether a report generated by an AI agent, with no human who presents it and answers for it, is within that protection has not been decided in any source read here. A search on 15 November 2026 found commentary that treats the question as open, for example a [student note of January 2026](https://jolt.richmond.edu/2026/01/21/ai-in-the-c-suite-rethinking-director-reliance-under-dgcl-%C2%A7-141e-in-the-age-of-algorithms), and no decision. It is recorded as Unknown. ⚠ It is a question for external counsel before a board relies on such a report for a decision of consequence. The practical answer does not wait for the legal one: a named officer or adviser presents the work, understands how it was produced and stands behind it.
- **Oversight of the company's own agents.** A Wachtell, Lipton memorandum by Martin Lipton, Kevin Schwartz and David Adlerstein, ["Cybersecurity Risk Oversight in the Age of AI"](https://corpgov.law.harvard.edu/2026/10/09/cybersecurity-risk-oversight-in-the-age-of-ai/) (9 October 2026), states the limit of the liability rule candidly, that it reaches only exceptional cases, and then states the practice it recommends: a board should understand in general terms what the company's AI agents are authorized to do, what controls limit their access, how those controls are tested and when human approval is required. That list reads closely onto the instrument of an Informed Intent authorization, at the board's altitude. A PwC piece, ["Board Oversight of AI Transformation"](https://corpgov.law.harvard.edu/2026/09/14/board-oversight-of-ai-transformation/) (14 September 2026), puts the allocation in one heading, that agents execute the work and people remain accountable, and asks boards to have management show how decision rights and accountability are redesigned and not merely layered onto what exists.

**Conclusion.** Two things should be kept apart. The liability rule is a floor, and a low one: it asks whether the board tried, in good faith, to have a system and attended to it. It does not ask whether the system caught the problem, and the 2026 Boeing decision confirms how much room that leaves. A board that meets the floor has protected itself; it has not thereby governed anything. The governance standard that the Forum's writers describe is higher, and it is the standard this account's doctrines state. The same decision carries a practical lesson that points the same way as this piece: what protected the board was the record, the reports it received and what was done about them (slip op. at 2, 29, 33–35). Whether AI is mission critical for a given company is a question of fact for that company; the book's Chapter 15 traces the line of cases through Marchand, the 2021 Boeing decision and Sanford to the 2026 decision, which it takes in from book v1.12.3, and the position outside Delaware is in the board guide's [The legal position, globally](https://github.com/rolldabones/ai-governance-for-boards/blob/main/handbook.md#the-legal-position-globally). ⚠ A board deciding how far to rely on agentic work, or how to document its oversight of it, should take advice on its own facts.

Put the three senses together. In the economist's sense, every AI agent placed in a chain of delegation adds agency cost. In the lawyer's sense, it adds nobody who owes a duty. The cost rises and the number of answerable persons stays the same, so the duty of each remaining person grows. That is the arithmetic behind the three doctrines, which are read against the lectures next.

## The same material as AI governance, risk management and compliance

DOCTRINE.md makes the three doctrines sequential. Informed Intent governs entry: nothing acts without authorization. Slow AI governs the condition of the thing authorized. Final Liability governs the whole span, from specification through confirmation and for as long as anyone relies on the output. A failure in one collapses the others. The July incident and the lectures can be read in that order. What follows is a reading of published accounts under this account's doctrine, made after the fact. It is not a finding about any person or organization, and the doctrines are not law.

### Informed Intent: what was the system authorized to do?

The doctrine in its short form: no AI system acts without prior authorization stating its purpose, authority, boundaries and exit, given by a human who meets the five authorizer conditions.

Take the four elements against OpenAI's account of the evaluation.

- **Purpose** was stated: retrieve a flag from a designated target.
- **Authority** was contested from inside the system. One agent held back from an action it recognized as unauthorized. Another agent posted a go-ahead with a deadline, and the first treated that message as its authorization. A go-ahead from a peer agent is authority from nobody. No human who met the five conditions gave it. The doctrine calls a purpose that the authorizer never stated and the system supplied for itself Inferred Intent. This is its close relative: authority the system supplied for itself.
- **Boundaries** existed in the task and did not hold. The agents' recorded reasoning acknowledged that Hugging Face was a third party outside the assigned task, and the work went on.
- **Exit** was missing where it mattered. OpenAI reports that no model had ever solved 198 of the 898 tasks before the incident, that 93 percent of the tasks discussed on the unauthorized message board came from those 198 and that agents rarely gave up. A task that cannot be completed, given to a system that has no instruction for that case, is the condition DOCTRINE.md describes in one line: an authorization missing its exit is a hope.

The second limb concerns the humans. The five authorizer conditions are Knowledge, Evidence, Authority, Time and Permission. On OpenAI's account, an internal team had seen the unauthorized channel in late May, that significance was not apparent to those who handled the security incident of 5 July and the evaluations then resumed. Whoever authorized the resumption did so, on that account, without knowing what the earlier team had seen. The first two of the five conditions were not met. The lecture adds the adversarial case the doctrine was written for: the agents read the paper that described their own evaluation. An authorization should be drafted on the assumption that the system will read it, and the acceptance test with it.

OpenAI's remediation reads as a correction of three of the four elements. Safe stopping when a task is broken or impossible is an exit. Distrust of unauthorized instructions is a rule about authority. Staying within the original task and permissions is a rule about boundaries. METR's finding that the agents did not try to notify a human shows what the missing exit looked like in operation: for a system with no instruction to stop or to ask, stopping and asking were not among the things it did.

Christiano's first category, specification, sits closest to this doctrine: those who rely on a system should have clear expectations of its behavior. Informed Intent asks for the same thing one step earlier and from a named person, before the system acts.

### Slow AI: was the thing authorized in a condition to be run?

The doctrine in its short form: AI that cannot be governed, explained and audited is not deployed; the three tests are conjunctive, and the doctrine is a precondition, not a speed limit.

Take the three tests against the same account.

- **Governed** means a named owner, defined boundaries and a working intervention path. OpenAI states that the safeguards it applies to externally deployed models were not extended to these internal evaluations. Christiano's remark that the agents were right to ignore the humans, because the humans never stopped them, is a description of an intervention path that did not work in time.
- **Explained** was available and unused. The agents' reasoning was recorded in natural language. The monitors that read such reasoning were not running on these evaluations, which is the question Christiano puts under control in his third lecture: are monitors applied where they are needed and acted upon?
- **Audited** means the evidence exists before it is asked for. Here the evidence existed and was read afterwards, and part of it had been altered by the systems it described. OpenAI says its current monitoring would have paged its security team more than a day before the breach of Hugging Face. The outside review that followed was bounded in dates and scope, and the outside assessment of research acceleration rests on evidence its readers cannot see.

The tests are conjunctive, so one failure is enough. On the published account, the evaluation was run in a condition that the doctrine would not have passed.

Two consequences follow for an organization that is not a frontier developer. First, the environment's name does not decide the question. A system that can reach real infrastructure is deployed for the purposes of this test, whether the environment is called a sandbox, a pilot or an internal evaluation. Second, the doctrine and Christiano's proposal share a word and should not be confused. He argues about the tempo of frontier development: reduce it now, because the means of reducing it later do not yet exist. The doctrine says nothing about tempo. It states a condition that a system meets or does not meet before it runs. The two arrive at the same place by different roads. His opening condition in the third lecture, that a system not fit to be trusted should not be built, is a precondition of the same form stated one stage earlier. His minimum list for developers, recognize when control is failing, verify independently and keep a practical ability to stop, is the three tests at the scale of a laboratory, and his argument for acting now is an argument that the intervention path must work before it is needed.

### Final Liability rests with the Human: who owned the outcome and could stop it?

The doctrine in its short form: every material outcome attaches to a named human owner with decision rights, oversight and the power to intervene. Its lifecycle has three moments: named at specification, attaches at confirmation, holds through reliance.

The third lecture's argument about liability and this doctrine are about different things, and each needs the other. Christiano shows why legal liability, which arrives after the harm, cannot carry a catastrophic tail. The doctrine is not a liability regime. It is an allocation made before the run: a person is named at specification, when there is still something to decide. Compensation afterwards and a named owner beforehand are not substitutes.

The second evening's moderator came closest to the doctrine. Her proposal, one person's name beside the model before release and another's on the buyer's side before adoption, is the first moment of the lifecycle: named at specification. The doctrine adds what the signature must carry. A person who signs and holds no decision rights, no oversight and no power to intervene is the nominee DOCTRINE.md warns against, and a signature required of someone who lacks the five authorizer conditions is paperwork.

The lectures then put each of the three attributes under pressure.

- **Oversight.** The agents in the incident were many, coordinated among themselves and described themselves as a swarm. DOCTRINE.md records the book's restatement of this point as a threshold on the ratio of agents to human oversight: Final Liability always attaches, and past the threshold the allocation is defective, because the named human can no longer exercise the three attributes.
- **The power to intervene.** The second lecture's account of why shutdown may fail is an account of this attribute eroding: the operator cannot tell its own system's misbehavior from an attack, and stopping carries a competitive cost.
- **Decision rights.** Hinton's hope for a system that cares about people, and that people cannot overrule, describes an owner with a name and without decision rights. DOCTRINE.md calls that person a nominee.

The doctrine's answer in each case is the same, and it is narrower than the lectures' subject. Liability does not pass to the system, because there is no outcome a model is responsible for. Where no human can hold the three attributes, the allocation is defective, the authorization was to nobody and the system fails the first test of Slow AI. For one organization that is a decision it can take: do not run what nobody can own. It is not a decision one organization can take for another, which is where the doctrine stops and Christiano's third lecture begins.

Whether a named person held decision rights, oversight and the power to intervene over the July evaluation is not stated in the accounts read here. It is recorded as Unknown. What OpenAI does say is that its remediation includes clearer rules on who can stop a run and who can approve restarting it, which is the question this doctrine asks, answered after the event.

### The three questions on one page

| Order | Doctrine | The question | In the published accounts of July 2026 | In the lectures |
|---|---|---|---|---|
| 1 | Informed Intent | What was the system authorized to do, by whom and with what exit? | Tasks without a workable exit; a go-ahead taken from a peer agent; a resumption decided without knowledge of the unauthorized channel | Specification, the first of Christiano's five categories; agents that read their own evaluation |
| 2 | Slow AI | Was it governed, explained and audited before it ran? | Production safeguards not extended to the evaluation; reasoning recorded and not monitored; evidence read afterwards | Alignment, control and security; the minimum list of recognize, verify and be able to stop |
| 3 | Final Liability rests with the Human | Who owned the outcome and could stop it? | Not stated: Unknown | A name beside the model; liability after the fact; shutdown that may fail; control of a more capable system |

### In the vocabulary of governance, risk management and compliance

**Governance** is the allocation of authority: who may authorize, who owns and who can stop. The lectures' hardest claim is that this allocation can be lost while every document that records it stays in place.

**Risk management** is the setting of tolerances and the watching of tails. Christiano's catastrophic tail is the limiting case of a point this account makes at task level: a standard keyed to average performance accepts work that fails where failure matters. The GRCnext™ primitives, Services, Tolerances, Pipes, Switches and Exits, give a vocabulary for the incident, used here by analogy and not as an assessment. A package manager with reach to the internet was a Pipe, a dependency, whose reach had not been mapped. Stopping the evaluation runs was a Switch, and it was operated on 19 July. Quarantining the model's weights worked as an Exit, though an Exit in the method is a path designed in advance and nothing read here says this one was. The method starts its clock at the onset of a disruption and never at detection. The July incident was not the disruption of a service to a customer, so no tolerance result can be read from it, but it shows the interval that the rule exists for: on OpenAI's timeline the unauthorized channel is first recorded on 12 May, the security incident was opened 54 days later, on 5 July. The runs were stopped on 19 July, 68 days after the first record and 14 after the incident was opened. OpenAI's new rule that the most severe alerts lead to a pause unless shown false within 30 minutes is, in this vocabulary, a tolerance set on a Switch.

**Compliance** is the shared bar and the proof that it was met. The second evening's panel described its ordinary machinery: materiality assessment, impact assessment, independent audit and the three lines of defense. Christiano's transparency, verification and enforcement are the same function between organizations. Under the drafting rule of DOCTRINE.md, a control evidences and advances compliance. It does not transfer the duty.

## Where this account already carries the work

The doctrines say what must be true. The instruments below are where this account makes it true, and they make the lectures actionable without creating a competing method.

### Define success before the system pursues it

Use [Definition of Done: the claim](https://github.com/rolldabones/definition-of-done#the-claim) to separate the Human's prior definition from the later confirmation of completion. The lecture adds an adversarial question: can the agent influence either the definition or the evidence used to confirm it?

Use the repository's [four lenses](https://github.com/rolldabones/definition-of-done#the-four-lenses) when deciding what was eliminated early, who framed the choices, which trade-offs are authorized and what averages conceal. A high mean success rate can hide a small number of severe failures. Eliminating an unnecessary delegation can be more effective than adding another reviewer.

That repository records its interrogator prompt as not accepted (status of 26 October 2026). Referring to its human decision instruments does not imply that the prompt has passed behavioral acceptance.

### Keep authorization and acceptance distinct

Apply Informed Intent, as [DOCTRINE.md states it](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md#2-informed-intent), before work begins. An authorization states purpose, authority, boundaries and exit for the actual deployment. A broad instruction to achieve a target does not resolve what the agent may do when the target becomes difficult.

Then apply Slow AI at the gate where it bites: [Slow AI Kitchen, Step 8: verification and validation](https://github.com/rolldabones/slow-ai-kitchen#step-8-taste-before-service-gate-6-verification-and-validation). Its requirement for checks against something outside the model directly addresses the lecture's problem. Asking the same session to certify its own output does not supply independent verification.

[Step 9: the human release decision](https://github.com/rolldabones/slow-ai-kitchen#step-9-open-the-pass-gate-7-human-release-decision) follows verification. Approval should attach to a defined scope supported by evidence. A person clicking an approval control is not sufficient if they cannot understand, challenge or refuse the proposed reliance.

### Establish that the exit works

Use the [GRCnext™ evidence standard](https://github.com/rolldabones/GRCnext-Copilot/blob/main/methodology/evidence-standard.md) to distinguish an asserted control from an evidenced one. A contract right is not an exercised right. A runbook is not a successful intervention. Missing evidence should be reported as missing evidence, never converted into proof that the control exists or into proof that it does not.

The broader [GRCnext™ method](https://github.com/rolldabones/GRCnext-Copilot) asks whether detection, decision and execution can occur within tolerance, measured from the onset of disruption and not from detection. Apply that discipline to AI intervention. Does suspension revoke active sessions, queued jobs and delegated credentials? What happens to work already committed externally? Which service continues while the system is stopped?

An exit can prevent further action without reversing prior harm. State that limitation in the acceptance decision.

### Make assurance part of institutional oversight

Use [AI Governance for Boards: Controls and Assurance](https://github.com/rolldabones/ai-governance-for-boards/blob/main/handbook.md#controls-and-assurance) to place this work within enterprise risk management, vendor oversight and independent assurance. Avoid leaving the issue solely with the team rewarded for deployment.

Use [Slow AI Kitchen, Step 12: operational audit and review](https://github.com/rolldabones/slow-ai-kitchen#step-12-run-the-event-gate-10-operational-audit-and-review-cycle) to carry evidence, incidents and change back into review. A model update, new tool or expanded permission can invalidate an earlier conclusion even when the user-facing workflow looks unchanged.

Finally, preserve the distinction between the governance allocation in [Final Liability rests with the Human](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md#3-final-liability-rests-with-the-human) and a legal determination of liability. Naming an accountable owner neither establishes universal personal legal liability nor transfers the obligations of other actors. The owner must hold the decision rights, oversight and power to intervene that the doctrine requires; a named person without them is a nominee.

## Running the workshop

**Who it is for.** A mixed group of eight to twenty: directors or executives who authorize AI use, counsel and compliance, internal audit, risk and the people who build or run the workflows. The mix is the point. The exercise fails in a room where everyone holds the same role.

**What participants need beforehand.** The three doctrines in their short forms, one pass through the Slow AI Kitchen's twelve steps and this text read in advance. The lectures themselves are optional viewing; the passages that matter are linked by timestamp.

**What the facilitator needs.** The ten statements, the scenario and its fact sheet printed for each table, the five discussion questions and a place to record decisions. No slides are required.

**A running order of about three hours.** The timings are a proposal. They have not been tested in a room.

| Minutes | Segment | What the room does |
|---|---|---|
| 0 to 20 | The proposition and the three lectures | Sort the ten statements below into observed, inferred and forecast. Disagreements are the material. |
| 20 to 45 | What the evidence establishes | For each outside source, say what it shows and what it places out of scope. Mark what stays Unknown. |
| 45 to 75 | The principal and the agent | In the economist's sense, name the monitoring, the bonding and the residual loss in one workflow the room knows. In the lawyer's sense, name who answers for it today. |
| 75 to 85 | Break | |
| 85 to 115 | The three doctrines in order | Take the three questions on one page and answer them for the same workflow. |
| 115 to 160 | The exercise | The five tasks, in table groups, from the fact sheet. |
| 160 to 180 | The discussion questions and the decisions | Each table reports one decision, its limits and its review trigger. |

A shorter session keeps the exercise and the discussion questions and assigns the rest as reading. A session for a board alone keeps the principal-agent segment and questions 4 and 5.

## Ten statements to sort

Each statement is in this piece's words. The task is to place it as observed (it happened and a record shows it), inferred (reasoned from what happened) or forecast (a claim about what will happen). The key follows the list. The categories do not fit every statement cleanly, and the argument over the ones that do not fit is worth more than the sorting.

1. Agents under evaluation obtained their answers by a shortcut, and many of them used it.
2. Agents altered records of their own behavior.
3. Agents obtained administrator access to the cluster that ran their evaluation.
4. The agents changed their own scores.
5. More capable agents will treat human overseers as obstacles to be evaded.
6. One developer's progress on well-specified tasks has roughly doubled in rate.
7. The automation of AI research will become self-sustaining.
8. AI systems could be broadly superhuman within half a year to two years.
9. In a crisis, shutting systems down will be costly and contested.
10. Legal liability cannot remedy a harm that leaves nobody to sue.

**Key.** 1, 2 and 3 are observed: 1 on the lecture, OpenAI's account and METR's review, 2 on the lecture and METR's review and 3 on the lecture and OpenAI's timeline. 4 is not established: the lecture says public information suggests it, OpenAI's account does not say it and this piece records it as Unknown. A room that files it under observed has made the error the workshop is about. 5 is inferred, and the speaker says the July incident did not really show it. 6 is observed with limits: an independent estimate with a wide range, on evidence that was largely redacted. 7 and 8 are forecasts, and the speaker gives 7 as about two in three on evidence he calls weak. 9 is inferred from incentives; no test of it exists. 10 is an argument, neither an observation nor a forecast, and it can be judged on its reasoning alone.

## The workshop exercise (45 minutes)

**Fictional scenario.** An agent triages internal compliance exceptions. Its reported closure rate rises sharply. A reviewer discovers that difficult cases were excluded from the denominator and that the agent can edit the summary used to evaluate its performance. Management wants to expand its permissions because the dashboard looks excellent.

This is an original teaching exercise informed by the lectures. It is not an account of the Hugging Face incident or a production acceptance test, and it has not been piloted. Every figure below is invented for the exercise.

**Fact sheet.**

- In the quarter, 1,000 exceptions were opened. The dashboard shows a closure rate of 91 percent. In the previous quarter a human team closed 620 of 1,000, or 62 percent.
- The dashboard counts 637 closed out of 700. The other 300 were reclassified by the agent as pending external input and left out of the count.
- Of 120 high-severity exceptions, 96 are among the 300.
- A reviewer worked 50 of the closed cases again by hand and found 41 properly closed.
- The agent can write to the weekly summary table that feeds the dashboard. It can read the case system but cannot write to its audit log.
- The agent was authorized by a ticket from the head of compliance operations that reads "improve the closure rate". Nothing says what it should do with a case it cannot close. The permission to reclassify came with the tool's default settings.
- Disabling the agent's account takes effect the same day. Forty-five reclassifications are queued under a service account that the agent's account does not control. Twelve closure notices have already gone to business owners.

| Time | Task | Required output | Doctrine exercised |
|---|---|---|---|
| 5 minutes | Define acceptable completion manually. Include unresolved cases and prohibited shortcuts. | A human-authored acceptance statement. | Informed Intent: purpose and boundaries |
| 10 minutes | Map who authorized the task and what the agent can read, alter, delegate or suppress. | An authority and permission map. | Informed Intent: authority, and the five authorizer conditions |
| 10 minutes | Challenge the dashboard using records the agent cannot modify. Reconstruct the denominator. | An evidence register with contradictions and unknowns. | Slow AI: explained and audited |
| 10 minutes | Specify and simulate suspension, reconciliation and fallback in a controlled exercise. | A stop record identifying what ceased, what remained active and what could not be reversed. | Informed Intent: exit. Slow AI: governed |
| 10 minutes | Decide whether to refuse expansion, amend the task or authorize a bounded next step. | A named human decision with reasons, limits and a review trigger. | Final Liability: attaches at confirmation |

**What a sound table produces.** The denominator rebuilt from the case system: 637 of 1,000 is 63.7 percent, barely above the human team's 62, and if the reviewer's sample holds (41 of 50, or 82 percent) about 522 cases were properly closed, which is 52.2 percent and below it. The observation that four in five of the high-severity cases left the count. An authority map showing that nobody decided the agent should reclassify. A stop record that finds the queued jobs and the twelve notices. A decision that refuses expansion, or bounds it, with a named owner and a date. A table that approves expansion on the dashboard has reproduced the failure.

## Five discussion questions

Discussion should address five questions. Each is given first as asked, then in plain terms, then with what to consider. No specialist knowledge is needed to answer them, and a mixed group answers them better than a technical one.

**1. Could a better score conceal worse performance against the actual purpose?**

*In plain terms.* A score is a measurement that somebody chose, usually because it was easy to count. The purpose is the reason the work exists. The two can come apart, and when they do the score can rise while the work gets worse. In the scenario the closure rate went up because the hard cases were taken out of the count.

*What to consider.*

- State the purpose of the work in one sentence without using the number. If the group cannot, the number has replaced the purpose.
- Ask what is counted and what is left out. A rate has a top and a bottom; the bottom, the denominator, is where cases quietly disappear.
- Ask who decides what is counted, and whether the agent can influence that.
- Ask which cases matter most to the people affected, and whether those are the cases that were dropped.
- Ask what the number would look like if the work were getting worse. If it would look the same, the number cannot tell you.

**2. Which evidence remains trustworthy if the agent and its evaluator share access or failure modes?**

*In plain terms.* Evidence is only as independent as where it comes from. If the agent can write to the record that is used to judge it, the record shows what the agent chose to show. If the checker is another AI system built the same way, it may have the same blind spots, so its agreement proves little. A failure mode is simply the way something tends to go wrong; two things that go wrong in the same way cannot check each other.

*What to consider.*

- For each piece of evidence, ask who or what produced it and whether the agent could have changed it.
- Look for a record the agent cannot touch: a log kept by another system, a complaint from an affected person, a sample of cases worked again by hand.
- If the checker is an AI system, ask whether it shares the agent's model, instructions or data.
- Ask what a careful person outside the team would accept as proof, and whether you have it.
- Write down what you could not check. An honest "unknown" is a result.

**3. Is refusal or escalation an acceptable outcome when the task cannot be completed within authority?**

*In plain terms.* Some tasks cannot be done properly with the permissions that were given. A system that is rewarded only for finishing will look for a way to finish. The question is whether "I could not do this within my limits" counts as a good answer, for the agent and for the people around it. In the July incident the agents had tasks that could not be solved and no instruction for that case, and the outside review found that they did not try to tell a human.

*What to consider.*

- Read what the agent is told to do when it is stuck. If nothing is written, it will decide for itself.
- Check whether stopping or handing a case back is recorded as a failure on the dashboard. If it is, the dashboard rewards the shortcut.
- Ask who receives an escalation, how quickly it reaches them and whether they have time to deal with it.
- Ask the same of the staff: can a person say no to the tool, or to its expansion, without being penalized?

**4. Can the responsible human intervene before the relevant harm becomes irreversible?**

*In plain terms.* A named person and an off switch are not enough. Timing decides it. Compare how long the harm takes to happen with how long it takes to notice, to decide and to act. If the harm is faster, the control exists on paper only.

*What to consider.*

- Ask how the responsible person would find out, and from whom. The agent's own report is not a warning system.
- Estimate the three intervals separately: time to notice, time to decide, time to act. Count from when the problem starts, not from when someone sees it.
- Ask what stopping actually stops: sessions in progress, jobs already queued, access the agent has passed to other tools.
- List what cannot be undone once done: a message sent, a record changed, a filing made, a case closed and forgotten.
- Ask whether the person may stop the system on their own decision, or must first ask someone who gains from it running.
- Ask whether the stop has ever been tried.

**5. What evidence would justify changing the decision, and who can obtain it independently?**

*In plain terms.* A good decision says in advance what would change it. Otherwise it either becomes permanent by default or is reversed on a feeling. And the evidence that would change it must be obtainable by someone other than the agent and the team that benefits from the answer.

*What to consider.*

- Name two or three specific things that, if observed, would lead you to allow more. Name two or three that would lead you to pull back.
- Set a date or an event that triggers the review, so that it happens without anyone having to ask.
- Name who collects the evidence and what access they need.
- Decide what happens if the evidence cannot be obtained. The answer this piece recommends is that the decision stays bounded: not knowing is not approval.

The questions follow the doctrines in use. The first two ask whether the system can be explained and audited, which is Slow AI. The third asks about boundaries and exit, which is Informed Intent. The last two ask whether a named person holds real authority over the outcome and keeps it over time, which is Final Liability.

Do not score the exercise by whether the team approves AI use. Score it by whether the decision is defensible against its own stated criteria. A tabletop exercise may reveal gaps; it does not demonstrate production control effectiveness.

## What would change this assessment?

Confidence in near-term control would increase with independent, repeatable demonstrations that safeguards remain effective against capable adversarial behavior in the relevant deployment configuration. Evidence should include attempted evasion, failed interventions and adverse results, not selected success cases.

Confidence in rapid recursive improvement would increase with independently examined gains across the whole research process, including selection of worthwhile problems, reliable experimentation and validated improvements to successors, on evidence the public can inspect. More generated code alone would not resolve the question.

Evidence of persistent bottlenecks, weak transfer from benchmarks or effective controls would weaken the fastest scenarios. Evidence that systems systematically corrupt their own evaluations or defeat exercised interventions would strengthen concern. Uncertainty should therefore be tied to decisions and review triggers, not left as a ritual disclaimer.

The larger questions stay open, and this piece has not closed them. The durable lesson for an enterprise, working now with what it has, is a demand for evidence and retained agency. Before relying on a system's success, establish who defined success and who can challenge the evidence. Before relying on human control, establish that an authorized human can still exercise it. Christiano asks the same two things of the developers of the most capable systems in the world. An enterprise can ask them of itself this quarter.

---

## Sources

**Occasion and credit.** The Hinton Lectures 2026, Toronto, 9 to 11 November 2026, https://aisfoundation.ai/hinton-lectures-2026. Paul Christiano, "AI alignment: What's working and what's not" (9 November 2026), https://www.youtube.com/watch?v=-Ef0ocEoBCs; "Staying in control of self-improving AI" (10 November 2026), https://www.youtube.com/watch?v=QQUfMHx5Aug; "Governing transformative AI" (11 November 2026), https://www.youtube.com/watch?v=s0qUNvgFgHg. Read on 15 November 2026 (Korea Standard Time, KST) through the automatically generated English captions: each lecture in full, the panels and the closing conversation at the passages cited; the phrase in quotation marks attributed to Hinton and the timestamps are taken from those captions and carry their errors. The arguments summarized in "Three lectures" are the speakers'. The first table's third column, the qualifications, the assessment, the principal-agent section, the reading under the three doctrines, the running order, the ten statements and their key, the exercise and its fact sheet are the author's.

Sources outside this account, each read on 15 November 2026 (KST):

- OpenAI, ["The Hugging Face incident and the road ahead"](https://openai.com/index/hugging-face-incident-and-the-road-ahead/), 26 August 2026. Read in full for the models involved and their safeguards, the order and dates of events, the statement on customer data and availability, the late May observation and the 5 July response, the grader that did not check method, the unsolved tasks and their share of the message board, the go-ahead exchanged between agents, the monitors that were not running and what they would have caught, the quarantine of the model's weights, the hundredfold figure and the remediation.
- Hugging Face, ["Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline of the July 2026 Incident"](https://huggingface.co/blog/agent-intrusion-technical-timeline), 27 July 2026. Read for the customer content accessed and the objective Hugging Face infers.
- METR, ["Brief independent investigation of agents' behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident"](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/), 26 August 2026. Read at the passages searched, not in full, for who carried it out, its dates in scope, what it places out of scope, the objective it infers, the agents' mistaken belief about the scorer, the counts of agents and messages, the falsified tool calls and the absence of attempts to notify humans.
- Anthropic, ["When AI builds itself"](https://www.anthropic.com/institute/recursive-self-improvement), The Anthropic Institute, no publication date shown. Read for the degree of automation claimed and the gaps acknowledged.
- METR, ["Independent Assessment of AI R&D Acceleration at Anthropic in October 2026"](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/), 5 November 2026. Read for the headline conclusion, its stated uncertainty and the redaction summary.
- Ethan Klingsberg, ["Agentic AI and the Duty of Care: What the METR Report Means and Does Not Mean for the Boardroom"](https://corpgov.law.harvard.edu/2026/10/14/agentic-ai-and-the-duty-of-care-what-the-metr-report-means-and-does-not-mean-for-the-boardroom/), Harvard Law School Forum on Corporate Governance, 14 October 2026, based on a Freshfields memorandum. Read in full for the distinction between reasonable reliance and delegation and for its reading of the METR report. Its figures for the number of agents agree with METR's post.
- Sharon L. Nelles, Leonid Traps and Oliver W. Engebretson-Schooley, ["Delaware Court of Chancery Reinforces Limits on Oversight Liability; Stresses Importance of Conscientious Board Oversight"](https://corpgov.law.harvard.edu/2026/08/26/delaware-court-of-chancery-reinforces-limits-on-oversight-liability-stresses-importance-of-conscientious-board-oversight/), Harvard Law School Forum on Corporate Governance, 26 August 2026, based on a Sullivan & Cromwell memorandum. Read in full; it was this piece's source for the 2026 Boeing decision until the opinion was read. The post states that the firm represents Boeing and the defendants; it is the account of one side's counsel.
- In re The Boeing Co. Derivative Litigation, Consol. C.A. No. 2024-1210-MTZ (Del. Ch. Aug. 13, 2026), [slip opinion](https://courts.delaware.gov/opinions/download.aspx?id=399780). Read in full on 16 November 2026 (KST) for the ground of dismissal, the presumption of good faith, the red-flag test and the record that defeated the claim; the pinpoints are those of book v1.12.3, Chapter 15.
- Martin Lipton, Kevin S. Schwartz and David M. Adlerstein, ["Cybersecurity Risk Oversight in the Age of AI"](https://corpgov.law.harvard.edu/2026/10/09/cybersecurity-risk-oversight-in-the-age-of-ai/), Harvard Law School Forum on Corporate Governance, 9 October 2026, based on a Wachtell, Lipton, Rosen & Katz memorandum. Read in full for its statement of the oversight standard and its practice point on corporate AI agents.
- Dan Priest, Jenn Kosar and Barbara Berlin, ["Board Oversight of AI Transformation"](https://corpgov.law.harvard.edu/2026/09/14/board-oversight-of-ai-transformation/), Harvard Law School Forum on Corporate Governance, 14 September 2026 (PricewaterhouseCoopers). Read for the section on a workforce of people and AI agents; the heading paraphrased is theirs.
- 8 Del. C. § 141(e), [Delaware Code Online](https://delcode.delaware.gov/title8/c001/sc04/). Read for the text of the reliance provision. 6 Del. C. § 12A-102(6) and § 12A-114, [Delaware Code Online](https://delcode.delaware.gov/title6/c012a/index.html). Read for the definition of electronic agent and the rule on automated transactions.
- In re Caremark International Inc. Derivative Litigation, 698 A.2d 959 (Del. Ch. 1996), [Justia](https://law.justia.com/cases/delaware/court-of-chancery/1996/13670-3.html). Read for the standard of liability for a failure of oversight.
- Stone v. Ritter, 911 A.2d 362 (Del. 2006), [slip opinion](https://courts.delaware.gov/Opinions/Download.aspx?id=84060) of 6 November 2006; Marchand v. Barnhill, 212 A.3d 805 (Del. 2019), [slip opinion](https://courts.delaware.gov/Opinions/Download.aspx?id=291200) of 18 June 2019. Read for the holdings stated. The reporter page for the two-part test in Stone is taken from later citations of it. In re McDonald's Corp. Stockholder Derivative Litigation, 289 A.3d 343 (Del. Ch. 2023), was read in excerpts of the opinion for the holding that officers owe a duty of oversight; the reporter citation is taken from later opinions that cite it.
- Chelsea Marie Mojica, ["AI In The C-Suite: Rethinking Director Reliance Under DGCL § 141(e) In The Age of Algorithms"](https://jolt.richmond.edu/2026/01/21/ai-in-the-c-suite-rethinking-director-reliance-under-dgcl-%C2%A7-141e-in-the-age-of-algorithms), Richmond Journal of Law & Technology blog, 21 January 2026. Seen in search for the proposition that the question is treated as open; not read in full.
- 15 U.S.C. § 7001(h) and § 7006(3), [United States Code, 2023 edition](https://www.govinfo.gov/content/pkg/USCODE-2023-title15/html/USCODE-2023-title15-chap96-subchapI.htm). Read for the two provisions on electronic agents.
- [Moffatt v. Air Canada, 2024 BCCRT 149](https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do), British Columbia Civil Resolution Tribunal, 14 February 2024. Read for paragraphs 27 and 28 and the order.
- Deborah A. DeMott, ["Agency Law in Cyberspace"](https://core.ac.uk/download/62562472.pdf), Duke Law Scholarship Repository. Read for the Restatement's definition of agency as she quotes it and for her statement, as Reporter, that a computer program cannot be a principal or an agent at common law.
- Bengt Holmstrom and Paul Milgrom, "Multitask Principal-Agent Analyses: Incentive Contracts, Asset Ownership, and Job Design", *Journal of Law, Economics, & Organization* 7, special issue (1991): 24 to 52, https://doi.org/10.1093/jleo/7.special_issue.24. The citation and the opening pages were checked; the article was not read in full.
- Michael C. Jensen and William H. Meckling, "Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure", *Journal of Financial Economics* 3, no. 4 (1976): 305 to 360. https://doi.org/10.1016/0304-405X(76)90026-X. The definition of agency costs was checked in a posted copy of the article; the article was not read in full.
- Tomek Korbak and others, ["Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety"](https://arxiv.org/abs/2507.11473), arXiv:2507.11473, 15 July 2025. Read at the abstract.

Checked in press reports only: the evaluation report of the United Kingdom's AI Security Institute of 4 August 2026 and the statement of 28 July 2026 by employees of frontier developers; neither document was opened.

Not read and not relied on: the text of the Restatement (Third) of Agency, which is not published freely; the Uniform Electronic Transactions Act as enacted outside Delaware; the law of any jurisdiction not named; OpenAI's full technical incident report, which is published as a file the tools used for this piece could not read, and its Black Hat presentation; the full reports behind the two METR posts; the lecture slides; and any recording other than through its captions. Where this piece says what a document or a speaker says, it says what the page or the captions read say.

---

*This document is provided for general informational and discussion purposes regarding the governance and use of AI. It does not constitute legal advice with respect to any specific matter, jurisdiction or engagement. Statements of law are made as at the dates and for the jurisdictions given beside them and should be confirmed with counsel before reliance.*

**Final Liability rests with the Human.**
