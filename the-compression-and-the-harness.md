# The Compression and the Harness

**A discussion piece on what a language model is, what a harness does and what stays with the Human**

Son-U Michael Paik · CEO, GRC Solutions Korea

October 12, 2026

**Starting point.** This piece grew out of Stephen Wolfram's interview with Jon Hernandez, "The future with AI will be very different from what we're being sold" ([video](https://youtu.be/6wc3OuLUiOk), 102 minutes), and my LinkedIn post on it, ["Nobody had to explain the horse."](https://lnkd.in/p/gJTMeq9g) (12 October 2026). Credit for the frames I borrow belongs to Wolfram: the ridden horse, the stone wall, the two branches of AI and the restate-and-confirm workflow. I paraphrase him and quote nothing. The paraphrases were checked against the video's auto-generated English captions on 12 October 2026 (KST). Wolfram and Hernandez have no involvement in this piece, have not reviewed it and do not endorse it. The interview is not covered by this repository's license.

**For:** anyone who has to explain to a board, a Client or a team what these systems are and what working with them requires. It is written to be argued with, and it ends on questions. The doctrine is [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md) and the method is the [Slow AI Kitchen](https://github.com/rolldabones/slow-ai-kitchen). The piece adds a reading of both and ten questions. It adds no doctrine, step, gate, tier or form.

**Durability.** The research systems named in Section 3 are dated evidence and will be overtaken. The argument does not rest on them, and the practices in Section 7 depend on no model, vendor or agent framework.

---

## Contents

- [1. A compression of what was written](#1-a-compression-of-what-was-written)
- [2. Four cells, three knowers](#2-four-cells-three-knowers)
- [3. Unknown to everyone](#3-unknown-to-everyone)
- [4. The harness](#4-the-harness)
- [5. Mess and upkeep](#5-mess-and-upkeep)
- [6. Where the metaphor breaks](#6-where-the-metaphor-breaks)
- [7. Meeting the model halfway](#7-meeting-the-model-halfway)
- [8. Where this argument is weakest](#8-where-this-argument-is-weakest)
- [9. What stays with the driver](#9-what-stays-with-the-driver)
- [Questions for discussion](#questions-for-discussion)
- [This piece and the account](#this-piece-and-the-account)
- [Source basis and attribution](#source-basis-and-attribution)

---

A language model is a lossy compression of what humans have written down, and of much else that has been recorded. A harness is what turns that compression from something that answers into something that works. The two ideas meet at one point, which is the argument of this piece. A harness can check an answer only against a test someone has already written. Neither the model nor the harness can decide what the test should be, or whether passing it was the point.

That work stays with the Human. In the picture it belongs to the driver. The driver has two jobs no harness can do: saying where to go and judging whether we got there. The first is a drafting problem, and Section 7 takes it up.

Wolfram's horse is ridden: you learn to ride it by learning how it behaves. My post added that somebody has to answer for where it goes. That post was about the rider. This piece is about the next step, which is hitching the horse to a load.

## 1. A compression of what was written

I think of a large language model as a compression of human knowledge, expressed in language and refined through training. The idea is not original. Ted Chiang called ChatGPT "a blurry JPEG of all the text on the Web" in [The New Yorker](https://www.newyorker.com/tech/annals-of-technology/chatgpt-is-a-blurry-jpeg-of-the-web) in February 2023. This account already works from the same idea: [Karpathy's Kitchen](https://github.com/rolldabones/slow-ai-kitchen/blob/main/karpathys-kitchen.md#1-intro-to-large-language-models) records Andrej Karpathy's version of it and concludes that compression is the mechanism and that it does not announce its own edges.

There is a technical claim underneath the metaphor. A language model is trained to predict the next word, and it has long been established that a predictor can be turned into a compressor and a compressor into a predictor. [Delétang and colleagues](https://proceedings.iclr.cc/paper_files/paper/2024/hash/3cbf627fa24fb6cb576e04e689b9428b-Abstract-Conference.html) showed in a paper presented in 2024 that large language models are strong general-purpose compressors, of images and audio as well as text. That result concerns lossless compression with the model as the engine. Chiang's point is about something else: what comes back when we ask the model a question, which is a reconstruction. The metaphor needs five qualifications before it can carry weight.

First, the model compresses what was documented, not what is known. A great deal of human knowledge was never written down: the judgment of a senior practitioner, the reason a clause is drafted the way it is, anything kept in a private file or spoken in a language with a thin written record. Michael Polanyi called this **tacit knowledge** and put it in one line: "we can know more than we can tell." My first instinct was that nearly all Known Knowns are in there. That overstates it. A large share of what has been widely published is in there, which is a narrower thing.

Second, the compression is **lossy**. For the most part the model does not store text and retrieve it. It reconstructs, and where the original detail was lost it fills the gap with whatever is most plausible. The output does not mark which is which. In this frame, what we call **hallucination** is a decompression artifact, delivered in the same confident sentence as the fact beside it. The Academy's memo [*Sounds Good*](sounds-good.md#3-the-mechanism-why-sounds-good-is-technically-accurate) sets out the mechanism and why fabricated output is the ordinary operation of the system and not a malfunction.

Third, the compression is **frequency-weighted**. It largely reflects how often something was said, not whether it was true. Common errors compress as well as common truths. A vague question gets the common answer, a point Section 7 returns to.

Fourth, "compression" undersells the thing. To compress that much text the model had to learn procedures as well as facts: how an argument runs, how a proof proceeds, how code executes. It can therefore produce answers that nobody wrote down, some of them right. That cuts against the blurry-JPEG reading, and it is what makes discovery possible.

Fifth, "written down" is too narrow, and the gap is widening. Models are trained on code, transcribed speech, images, audio and video as well as prose, and on data that machines produced and no person wrote. A model at work also reads what was never in its training and is not compressed at all: retrieved documents, databases, search results and the output of tools, which *Sounds Good* takes up in [Section 4](sounds-good.md#4-augmented-configurations-relocation-not-resolution). "The record" in this piece means all of it. The wider record makes the model more useful and makes some checks cheaper, because a retrieved source can be opened and compared. It does not change who checks. A retrieved document can be misread as fluently as a remembered one.

The second and fourth points pull against each other. The model can say new things, and it cannot tell me which of its new things are true.

## 2. Four cells, three knowers

The matrix that Donald Rumsfeld made famous at a Department of Defense briefing on February 12, 2002 sorts knowledge into known knowns, known unknowns and unknown unknowns. The fourth cell, the unknown knowns, he did not name. [*Slow AI for the Chief Legal Officer*](slow-ai-for-the-chief-legal-officer.md#2-know-what-you-know) uses the four cells to map an organization's risk. There the knower is the organization. Here the matrix is useful on one condition: we say who the knower is. There are three candidates: me, the record and the model. Most confusion about what an AI "knows" comes from sliding between them.

**Known Knowns** are what I know and the record holds. Here the model is a fast index with the lossiness described above.

**Known Unknowns** are what I know I do not know, and can therefore ask about. The model draws on a base far larger than any one person can hold. The limit is my ability to say what I want. This is where **Informed Intent** begins. The doctrine requires that purpose, authority, boundaries and exit be stated before a system acts ([DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md#2-informed-intent)). At the scale of a single question the same logic holds: the answer can be no better specified than the question.

**Unknown Knowns** come in two kinds. The first is what I know but have not articulated. Working with a model draws it out, and redlining its draft reveals preferences I could not have listed in advance.

The second kind matters more for this piece: what the record contains but no one has assembled. Don Swanson named this **undiscovered public knowledge** in 1986. He found one medical literature showing that dietary fish oil changes the blood in certain ways, and another suggesting that such changes might help patients with Raynaud's syndrome. The two had never cited each other. By [Swanson's own account](https://pmc.ncbi.nlm.nih.gov/articles/PMC225324), a clinical trial reported the benefit two years after he published the inference. Swanson joined the two by hand. A model has been trained on both literatures, and on thousands of other pairs that no one has put side by side. This is where I expect a model to be most useful, and it is an expectation: whether a model makes such a join unprompted is a claim to test, and the join still needs a trial.

**Unknown Unknowns, relative to me,** are often Known Knowns to the record. I do not know to ask. A model asked what I am not asking can move them across.

| Cell | Who knows | What the model can do | What it cannot do |
|---|---|---|---|
| Known Knowns | I do, and the record does | Retrieve and restate, quickly | Mark which details it rebuilt |
| Known Unknowns | The record does and I do not | Answer the question I can frame | Supply the intent I left out |
| Unknown Knowns | I do and have not said so, or the record does in pieces | Draw out what I had not said and propose a join no one has made | Confirm that the join is real |
| Unknown Unknowns | Not I, and sometimes no one | Show me what I did not know to ask | Settle a question the record cannot settle |

The third knower, the model, has a problem of its own. It does not reliably know what it knows. A human expert has a reputation that punishes overreach. Nothing punishes the model for overreach, and the edge of its knowledge is unmarked in what it writes.

Nor can the model be asked to show its working as a substitute. Wolfram's image for a trained model is a stone wall, not a brick one: each stone sits where it does because it fit. If there is no short account of why an answer came out as it did, the model's own explanation cannot be the check.

So the model can carry knowledge across every boundary in the matrix except one. It can help me say what I had not articulated, hand me what the record held and show me what I did not know to ask. It cannot turn a plausible answer into a verified one. That crossing needs something outside the model.

## 3. Unknown to everyone

That leaves the things unknown to everyone and absent from the record. My first thought was that a model could reach them only by serendipity. I now think that was wrong in both directions.

The model alone cannot discover them. Text cannot settle a question about a world not yet observed. The model can conjecture, tirelessly, but a conjecture is not knowledge until it is checked against something outside the model.

Nor is it luck. In December 2023 Google DeepMind published [FunSearch in Nature](https://pmc.ncbi.nlm.nih.gov/articles/PMC10794145). It pairs a pretrained language model with a systematic evaluator in an evolutionary loop. The model proposes programs, the evaluator scores them and the best are fed back. On the cap set problem in combinatorics it found constructions larger than the best previously known.

In May 2025 the same laboratory announced [AlphaEvolve](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/), built on the same pairing. It found a way to multiply 4×4 complex-valued matrices in 48 scalar multiplications, improving on a result of Strassen's that had stood since 1969.

In both systems the model supplies candidates and cannot confirm which are good. The **evaluator** can confirm, and has no ideas of its own. The discovery belongs to the pair.

Wolfram draws the same line from the other side. He describes two branches of AI. One imitates us and is right most of the time. The other formalizes the world in exact computation. Where any failure is a disaster, he says, the imitative branch is not a good idea. The middle ground he sees emerging puts exact computation underneath it as a hard layer. He sells the exact branch, so the pitch should be discounted. The frame holds, and FunSearch and AlphaEvolve are that arrangement built. Karpathy's Kitchen reaches a parallel rule from the governance side: [put determinism around probability](https://github.com/rolldabones/slow-ai-kitchen/blob/main/karpathys-kitchen.md#6-put-determinism-around-probability).

The same arrangement is now ordinary in everyday harnesses, at smaller scale. A model given a code interpreter does arithmetic by running code and not by predicting digits. A model that writes software runs the compiler and the tests. Where the model wrote the tests as well, they are one more conjecture until a person has read them. A model that answers from a database runs the query, and one that cites a document can be made to fetch it. For that segment of the work the computation is correct because a deterministic tool performed it, and a wrong step often fails with an error the model can read and correct. This is the everyday way a harness reduces error: it moves work from text the model predicts to results a tool computes. The limit is the one *Sounds Good* sets out under [tool use](sounds-good.md#42-tool-use). The model still decides whether to call the tool, what to pass it and what the result means, and a correct engine answers the wrong query exactly. The tool settles the sum and leaves open whether it was the sum to do.

The pairing of a model with an evaluator is a harness in the working sense of the word. Discovery of Unknown Unknowns is a property of the harnessed model, and the part that matters most is the one that checks. Someone wrote that check. For the mathematical problems above it can be written once and run a million times.

Most professional judgment is not like that. Karpathy gives the general rule in a short post that [Karpathy's Kitchen](https://github.com/rolldabones/slow-ai-kitchen/blob/main/karpathys-kitchen.md#11-verifiability) reads for governance: hand-written software automates what can be specified, and learned software automates what can be verified. In law, strategy and governance the verifier is slow, expensive and human: a court, a market, a regulator, a consequence. There the model's conjectures stay conjectures until someone accountable tests them. Where no automated score exists, a human does the scoring. A second model's review is one more plausible answer until it is itself tested.

Two things therefore govern how far a model can be trusted in a kind of work: what a check costs and what an error costs. Where the check is cheap, let the model run and check everything. Where the check is expensive, the model's output is a draft, and the effort saved in writing is owed back in verifying. This account calls the discipline **Return to Source**: keep the ability to walk back from conclusion to evidence to source to observable reality, with verification proportional to consequence. Its statement is in [Coetzee's Kitchen](https://github.com/rolldabones/slow-ai-kitchen/blob/main/coetzees-kitchen.md#iii-return-to-source). In the method it is prepared at Gate 2 and performed at [Gate 6](https://github.com/rolldabones/slow-ai-kitchen/blob/main/README.md#step-8-taste-before-service-gate-6-verification-and-validation), verification before reliance.

Beyond the reach of any search the old answer still holds. We cannot plan for what we cannot name. *Slow AI for the Chief Legal Officer* gives the only answer I know, which is slack kept ready. GRCnext™ adds real choices: lawful, authorized and executable options held before they are needed. [GRCnext-Copilot](https://github.com/rolldabones/GRCnext-Copilot) and [RedCap-00](https://github.com/rolldabones/RedCap-00) exist to test whether they would execute.

## 4. The harness

"Harness" is now a working term for the software around a model: the loop, the tools, the context and the permissions. The word evokes a horse and carriage. I am no expert in tack, and I had assumed the harness was mainly about control, with some mechanical function on the side. It is the reverse. A horse does not so much pull a carriage as push into a collar, and the traces carry that force back to the load. A harness is first a device for transmitting power.

That is also the difference between riding and driving. A ridden horse carries one person. A harnessed horse moves a load, and the rider's skill of knowing the animal's habits is no longer enough on its own.

| Part | What it does | Equivalent around a model |
|---|---|---|
| Collar and traces | Carry the horse's push back to the carriage | Tools and connections that turn output into action |
| Bit and reins | The driver's line to the horse: steer, slow and stop | Instructions, approval gates and the human stop |
| Breeching | Lets the horse hold the load back on a descent | What holds the load back: permissions and scopes |
| Blinkers | Keep the horse from being distracted or frightened | Curation of context |

Three things follow.

First, a harness creates capability before it limits anything. An unharnessed model answers questions. A harnessed one does work: it sends the message and moves the money. Every trace added increases what can be done and what can go wrong. [Newton's Kitchen](https://github.com/rolldabones/slow-ai-kitchen/blob/main/newtons-kitchen.md#law-ii-motion) states it as a law: the consequence an agent can produce is bounded by its authority and its reach, not by its intelligence. Governance that treats the harness only as restraint misses that the harness is first what lets the horse pull.

Second, the parts have to be designed together. Pulling power without a way to hold the load back is a carriage that cannot stop on a hill. Enterprises tend to attach the **traces** first, by connecting tools, and to think about stopping later. The security community has names for the result. The [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) lists **excessive agency** as a risk in its own right, and its guidance on prompt injection recommends **least privilege** and human approval for high-risk actions. Least privilege is **breeching** and human approval is the reins. The driver's stop is one kind of what GRCnext™ calls a Switch, an authorized action that, among other things, alters, pauses or stops service delivery ([glossary](https://github.com/rolldabones/GRCnext-Copilot/blob/main/methodology/glossary.md)).

Third, a harness can carry an evaluator where the work allows one to be written. It cannot decide what the evaluator should test. No strap or buckle tells the driver whether the carriage has arrived at the right place. On a carriage, and in most professional work, that judgment is the driver's.

## 5. Mess and upkeep

Horses shit, sometimes on the driver. They need grooming and shoeing. The less dignified half of the metaphor is accurate.

The mess is output nobody asked for, confident errors, the side effects of actions taken and files left behind. None of it is malfunction. It is the byproduct of the animal working, and the cleanup has to be budgeted.

The upkeep is evaluation, monitoring for drift, context hygiene and the periodic review of permissions that have quietly accumulated. The harness wears too. One fitted to last year's horse chafes this year's: controls written for a weaker model may restrain the wrong things and miss the new ones. The Kitchen gives the upkeep a gate of its own, the [operational audit and review cycle](https://github.com/rolldabones/slow-ai-kitchen/blob/main/README.md#step-12-run-the-event-gate-10-operational-audit-and-review-cycle).

A harness lowers the odds of a runaway without removing them, and the driver stays on the box.

## 6. Where the metaphor breaks

The metaphor fails in five places. Each one marks a piece of governance work.

**The horse has a stake.** A horse will usually refuse a cliff. It will also bolt. Either way it has something to lose in what happens next, and the model has nothing. On a hill the horse does the holding back, through the breeching. Around a model the holding back cannot be left to the animal. The book makes the same point about reputation in [Chapter 13](https://github.com/rolldabones/final-liability-rests-with-the-human-book-wip/blob/main/manuscript/14-chapter-13-agents-have-no-reputational-skin-in-the-game.md): a human agent has something to lose, and an agent built from a model does not. No part of the stop can rest on the model's own interest. Limits go where the model cannot argue with them, in permissions and not in prose, and the stop is assigned to a person.

**The reins and the load share a channel.** A horse is steered by leather and hauls a load. Nobody steers a horse by writing on the load. A model is steered in language and its work is language, so an instruction buried in a document it reads can be taken for a command. This is **prompt injection**, and the buried kind is **indirect prompt injection**, which [OWASP](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) describes as arising when a model accepts input from external sources such as websites or files. OWASP is candid that it is unclear whether any foolproof prevention exists. The working rule is that whatever the model reads is part of the load and only the driver gives orders. Because the rule can fail, it is backed by limits on what the horse can reach. [*The Ungoverned Channel*](https://github.com/rolldabones/the-ungoverned-channel/blob/main/06-threat-surface.md) records the attack as demonstrated in a shared workspace and draws the consequence: scope is the only variable in the blast radius that the deployer fully controls.

**The horse can be swapped overnight.** A driver knows a horse over years. A vendor replaces the model on its own schedule. A change of model is a material change, and what was tested on the old one has to be tested again. The Enterprise AI Architecture Primer treats a model swap as a code deployment and [gates it like one](https://github.com/rolldabones/slow-ai-kitchen/blob/main/primer/02-part-2-solution-architecture-to-2-8-entry-points-and.md#the-eval-gate-on-a-model-swap). The Chief Legal Officer's version of the question is whether the thing running today is the thing that was approved.

**The numbers do not match.** One driver manages one team of horses. One person can launch a thousand instances of a model, and human attention does not scale with them. An error a person would have caught is complete before any person can look. This is the ground **Slow AI** stands on. Its rule is that a system that cannot be governed, explained and audited should not be deployed ([DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md#1-slow-ai)). Slow AI slows the horse only to the pace at which the Human can follow it and intervene where intervention matters.

**The horse was never a library.** A horse knows the way home and little else. The driver supplies the destination. A model supplies force and knowledge together, and often knows the terrain better than the driver does. The temptation to let it choose the destination has only a faint equivalent on a carriage, the horse that turns for home. The compression is what makes the animal worth harnessing, and it is also what makes the driver inclined to defer to it.

That inclination has a name, **automation bias**, and the EU AI Act writes it into the oversight requirement for high-risk systems. The provider must supply the system so that the people assigned to oversee it can, as appropriate and proportionate, remain aware of the possible tendency of automatically relying or over-relying on its output. The deployer in turn must assign oversight to people who have the necessary competence, training and authority. *[In force; Articles 14 and 26 not yet applicable. Pinpoints: Articles 14(4)(b) and 26(2), Regulation (EU) 2024/1689. For systems that are high-risk under Article 6(2) and Annex III, Sections 1 to 3 of Chapter III apply from 2 December 2027 under Regulation (EU) 2026/1744. As at 12 October 2026 (KST).]*

Awareness alone does not fix it. The book's [Chapter 12](https://github.com/rolldabones/final-liability-rests-with-the-human-book-wip/blob/main/manuscript/13-chapter-12-the-human-in-the-loop-is-not-a-shaman.md) is about the human placed in a loop without the knowledge, authority, time, evidence and permission to change the outcome. That human oversees nothing. Wolfram holds that what humans choose to do is almost by definition unautomatable. On a carriage that choice is the destination, and the driver settles it before setting out.

## 7. Meeting the model halfway

The human side has to think harder about communicating intent. "Halfway" is the right word, because the model's half has moved a long way. Current models follow plain language and can be asked to question an instruction before acting on it.

Wolfram describes the meeting point as a workflow he sees emerging. The human says loosely what is wanted. The model writes a precise version in a form a human can read. It might not be what was meant. The human reads it and confirms, and the confirmed version becomes a solid brick to build on. Neither side produces that brick alone. In my post I called this Informed Intent: the purpose, the authority, the boundaries and the exit are stated before the action, by a human in a position to give the authorization, and are not inferred afterwards.

The human half cannot be skipped, for two reasons.

The first is that my intent is not in the compression. What I want, for whom, why and what I would count as done exist only in my head. To the model my intent is an Unknown Known: I hold it and have not said it. No improvement in the model supplies information it was never given. Context that a harness supplies narrows the guess without stating the purpose. A better model guesses better, and its guess is the frequency-weighted one: what most people who typed those words wanted. Professionals are hired for the cases where the Client is not most people. The doctrine has a name for the guess. It is **Inferred Intent**: the purpose the authorizer never stated, supplied afterwards by the system or its vendor.

The second is absence. An instruction given to an agent is carried out many times, over many steps, when I am not there. A conversation can be repaired in the next turn. An instruction that runs in my absence has to hold on its own. The Kitchen's agent companion asks the practical question: [what may happen between human checkpoints?](https://github.com/rolldabones/slow-ai-kitchen/blob/main/take-out-delivery-and-vending-machines.md#the-order-travels)

Lawyers know that situation. A contract is written for readers who are not in the room: a counterparty looking for room to move, a successor who never met the parties, a court reading it years later. The drafter cannot lean over and explain. That is why contracts have defined terms, precedence clauses, conditions and remedies.

**Computational drafting** is my name for the discipline that carries this over. It is the design of specifications that translate human and institutional intent into behavior across legal, organizational and technical interpreters ([repository](https://github.com/rolldabones/computational-drafting)). A model is one more interpreter. It is literal in some places and inventive in others, it lacks my context and it has no stake. An instruction to such a reader should be drafted the way a delegation of authority is drafted. The repository's [interpreter map](https://github.com/rolldabones/computational-drafting/blob/main/02-interpreter-map.md) states the difference that matters: a human who finds a gap can stop and ask, and a model fills the gap with an inference.

Wolfram makes a point a drafter will recognize. A specific prohibition, a button that must never be pressed, is probably not hard to enforce. A general ban on doing wrong means nothing until someone defines wrong.

### The eight elements, applied to an instruction

Computational drafting holds that a complete specification states eight things. The first two columns below abridge the repository's [eight elements](https://github.com/rolldabones/computational-drafting/blob/main/README.md#the-eight-elements), which the [anatomy](https://github.com/rolldabones/computational-drafting/blob/main/01-specification-anatomy.md) develops in full. The third column is this piece's application of them to the everyday act of instructing a model.

| Element | The question it answers | When instructing a model |
|---|---|---|
| Objective | What is this for | State the purpose as well as the task: who the work is for and what decision it serves. Purpose lets the model fill a gap closer to the way I would |
| Authority | Who may act, with which decisions reserved | Say what the model may do on its own, what it may only draft and what needs my approval. Grant only the access the task needs |
| Constraints | What must never happen | Write the specific prohibitions and put the ones that matter in permissions as well. A prompt-only constraint is a preference |
| Precedence | Which instruction wins | Say which instruction wins in a conflict. Say that material the model reads is part of the load and never an order |
| Exceptions | What departures are allowed, by whom | Say what to do when the rule does not fit: stop, ask and note the departure |
| Evidence | What must be kept | Ask for sources I can open. Keep the instruction and its version with the output. Flagged uncertainty and shown working are leads for my check and are not the check |
| Escalation | What forces a stop | Name conditions I can observe and the person to call. The model's own uncertainty is a useful signal and an unreliable one |
| Acceptance | What proves the work is done | Define done before starting, as tests I could apply without the model's help, and say what share of the output a person will check |

An element left out is delegated, silently, to whichever interpreter meets the gap first. The acceptance element has a repository of its own, [*The Definition of Done*](https://github.com/rolldabones/definition-of-done), and the [system prompt template](https://github.com/rolldabones/computational-drafting/blob/main/templates/system-prompt-as-delegated-authority.md) shows the eight drafted as an instrument of delegation. The computational-drafting [quick start](https://github.com/rolldabones/computational-drafting/blob/main/00-quick-start.md) puts the whole loop on one page.

Guidance from outside this account starts in the same place. Anthropic's [prompt engineering guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview), to take one vendor's, assumes a clear definition of success criteria and a way to test against them before any prompt is written.

### Four habits around the specification

- **Hand over the context the model cannot have.** Unless the harness supplies it, the model starts each task blank. The file, the Client's position and the house style have to be given.
- **Use one word for one thing.** Define the terms that carry weight and do not vary them for style. A model may read a new word as a new thing, and so may a court.
- **Read the instruction as a hostile reader would.** The [hostile-case checklist](https://github.com/rolldabones/computational-drafting/blob/main/03-hostile-case-checklist.md) gives seven patterns, beginning with the reader who follows the letter and defeats the purpose. Run the instruction on the hard cases, and run it again when the model changes.
- **Redline the draft and keep the redline.** Edits, too, reveal intent. Judgment that cannot be listed on request surfaces when an expert reacts to a draft, which is the method in [Section 12 of the Law Firm AI Deployment Spec](law-firm-ai-deployment-spec.md#12-convert-tacit-legal-judgment-into-evaluation-rubrics). A redline that recurs is a standing instruction waiting to be written.

### Where Slow AI comes in

The doctrine's three tests apply to an instruction as they apply to a system. Governed: the instruction has a named owner, boundaries and a stop that works. Audited: the instruction, its version and the evidence exist before anyone asks for them. Explained is harder. The doctrine asks that the organization be able to state why an output was produced, in terms the affected person can use. Wolfram's stone wall says the model cannot give that account from the inside. The account has to come from the outside: what was asked, on what material, against what test and who confirmed the result. Whether that satisfies a particular legal duty to explain is a question for the jurisdiction and is not answered here. The Kitchen's ownership test at [Gate 7](https://github.com/rolldabones/slow-ai-kitchen/blob/main/README.md#step-9-open-the-pass-gate-7-human-release-decision) is a neighboring account given in person: the owner stands at a whiteboard and explains to another human what was done, how and why, with no model in the room.

On proportion, this is more work at the start and not every task earns it. A question asked once for my own use needs a sentence. An instruction that will run unattended or reach a Client needs a specification. The Kitchen's [three risk tiers](https://github.com/rolldabones/slow-ai-kitchen/blob/main/README.md#risk-tiers) set the depth, and its own account of itself is that it slows AI to the speed of human verification and no further. Good enough is good enough.

A better model makes tricks of phrasing matter less. It does not supply intent, and the more authority a model is given the more the specification carries. Writing the specification is also where I most often find out that I did not know what I wanted.

## 8. Where this argument is weakest

A discussion piece should say where it can be attacked. These are the objections I take most seriously.

**Compression is a frame, not a finding.** The technical result in Section 1 is about prediction and lossless compression. The claim that asking a model a question is lossy decompression is an analogy. My fourth and fifth qualifications already concede that the model does more than store and reads more than it stored. A reader who holds that these systems build working models of the world will find the frame too small.

**The unmarked edge may not stay unmarked.** I say the model does not reliably know what it knows. If models come to signal the limits of their own knowledge dependably, the third knower's problem in Section 2 shrinks and the cost of checking falls with it.

**A second model can check the first.** Reviewer models and model-graded evaluations are common practice. Section 3 treats a second model's review as one more plausible answer. That is an assumption. If independent models reliably catch each other's errors, the line Section 3 draws between cheap and expensive checks moves a long way.

**The human check is weak.** Section 6 describes a driver who is inclined to defer and is outnumbered. Section 9 then rests on that driver's check. The piece says confirmation stays with the Human. It does not show that human review can keep up at volume. Tiers and a gate before release are the method's answer, a sampling regime is the specification's, and they are a design, not a proof.

**The saving may be owed back.** Section 3 says the effort saved in writing is owed back in verifying. If it is owed back in full, the case for using a model in work that is expensive to check rests on quality and not on time, and this piece has not made that case.

**The maker is absent.** The piece puts everything on the driver. The party that bred the horse and swaps it on its own schedule carries nothing here. Final Liability says a named human answers for the outcome. It does not say the maker answers for nothing. Product liability and most of the provider duties in the EU AI Act are about the maker, and apart from the one provider provision cited in Section 6 this piece does not address them.

**The picture has one driver.** An organization has a chain of them: one person approved the use, another configured the system and a third relied on the output. A picture with a single driver can hide the question of which of them holds the reins.

**The evidence is narrow.** Two systems from one laboratory, both in mathematics, carry Section 3. The paragraph on everyday tools rests on common practice and cites no study.

**The analogy is an analogy.** The cases in Section 9 concern domestic animals. A court could as easily treat an AI system as a product, or as an animal that is not domestic at all.

## 9. What stays with the driver

The model is a lossy, frequency-weighted compression of the record that also learned how to reason over it. It is well placed to connect what is already recorded and to surface what I did not know to ask. It reaches what is new only when something outside it checks the work. The harness supplies the pull and the control. It wears and leaves a mess. It can run a check that someone has written. It supplies neither the destination nor the judgment that the destination was reached. Those are the driver's, and they sit at the two ends of the work: intent stated before, confirmation after.

**Final Liability** follows that sequence. The owner is named when the work is specified, accountability attaches when the owner confirms the result and it holds for as long as anyone relies on it ([DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md#31-the-allocation-lifecycle)). The test of a driver is whether they can explain to another human where the carriage went, by what road and why.

The common law of animals puts two questions to an owner. I offer New York as an analogy and not as a statement of how liability for AI will be decided. In [*Collier v. Zambito*](https://www.nycourts.gov/reporter/3dseries/2004/2004_00960.htm), 1 N.Y.3d 444, 446 (2004), the Court of Appeals restated the rule that an owner who knows or should have known of a domestic animal's vicious propensities is liable for the harm they cause. It drew its definition of such a propensity from an 1868 horse case, *Dickson v. McCoy*, 39 N.Y. 400, 403. Once that knowledge is shown the owner's liability is strict (*id.* at 448). The owners in *Collier* won all the same. Their dog had barked and run about, which the court called what dogs do, and that did not show a propensity they knew or should have known of (*id.* at 447). The court added that its ruling gave owners no automatic free bite (*id.* at 448). In [*Flanders v. Goodfellow*](https://www.nycourts.gov/reporter/3dseries/2025/2025_02261.htm), 44 N.Y.3d 57 (2025), the court opened a second route, ordinary negligence, overruling *Bard v. Jahnke*, 6 N.Y.3d 592 (2006), to the extent that case barred it. *[Binding New York common law on domestic animals. Analogy only, not authority on AI. Pinpoints: Collier, 1 N.Y.3d at 446 to 448; Flanders, 44 N.Y.3d at 60. As at 12 October 2026 (KST).]*

The cases put two separate questions. The first is what the owner knew or should have known of this animal. The second, since *Flanders*, is what care the owner took. Both carry over to the driver, with a caution from *Collier*: knowing what the species does was not enough there. General knowledge of what language models do is therefore not the test. The test is what this deployer knew or should have known of its own system, and "should have known" narrows the route of not looking. That knowledge sits in the deployer's logs, evaluations and incidents. Care is what this piece has described: a harness fitted to the animal, a destination stated before setting out and a check before anyone relies on the result.

---

## Questions for discussion

1. What does your team know that has never been written down? What does the model say when asked about it? (Section 1)
2. Pick one AI use in your organization. Which cell of the matrix does it mostly serve, and who is the knower? (Section 2)
3. What is the verifier for that use? Is it mechanical or human, how long does it take and who pays for it? (Section 3)
4. List what the system can act on and what can stop it. Which was installed first? (Section 4)
5. When the vendor last changed the model, what was tested again and who decided it was enough? (Section 6)
6. Has the model known the terrain better than you did? How did you find out? (Section 6)
7. Take an instruction your team gives a model every week. Which of the eight elements does it state, and which has it left to the model? (Section 7)
8. Have the model restate that instruction before working. What differed between the restatement and what you meant? (Section 7)
9. Which objection in Section 8, if it is right, would change your practice?
10. If something went wrong tomorrow, what would the record show of what you knew about your system and what care you took? (Section 9)

Question 10 produces a record. Decide before the session whether the discussion belongs under legal privilege.

## This piece and the account

The piece is a reading of work that already exists in this account. Each row points to where the argument is carried as an instrument, and the table adds some neighbors the body does not name and omits some links the body carries. Repositories the argument does not touch are left out. The full map is [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md).

| In this piece | Where the account carries it |
|---|---|
| Section 1: lossy reconstruction and hallucination | [*Sounds Good*](sounds-good.md), in this repository; [Karpathy's Kitchen](https://github.com/rolldabones/slow-ai-kitchen/blob/main/karpathys-kitchen.md), the technical derivation; [The AI Generalist](https://github.com/rolldabones/the-ai-generalist), Section 3, for a one-day introduction |
| Section 2: the four cells | [*Slow AI for the Chief Legal Officer*](slow-ai-for-the-chief-legal-officer.md), Section 2, where the knower is the organization |
| Section 3: checking, and proportion in checking | [Coetzee's Kitchen](https://github.com/rolldabones/slow-ai-kitchen/blob/main/coetzees-kitchen.md) for Return to Source; Kitchen Step 3 (Gate 2) and Step 8 (Gate 6); [GRCnext-Copilot](https://github.com/rolldabones/GRCnext-Copilot) and [RedCap-00](https://github.com/rolldabones/RedCap-00) for the choices kept in reserve |
| Sections 4 and 5: authority, reach and upkeep | [Newton's Kitchen](https://github.com/rolldabones/slow-ai-kitchen/blob/main/newtons-kitchen.md), Law II; Kitchen Step 5 (Gate 4: Bounded AI Use), Step 10 (Gate 8: Authorized Tool Registry) and Step 12 (Gate 10) |
| Section 6: the five breaks | The book, [Chapters 12 and 13](https://github.com/rolldabones/final-liability-rests-with-the-human-book-wip/blob/main/manuscript/README.md); [*The Ungoverned Channel*](https://github.com/rolldabones/the-ungoverned-channel), file 06; the [Enterprise AI Architecture Primer](https://github.com/rolldabones/slow-ai-kitchen/blob/main/primer/README.md) on model swaps and [re-tiering triggers](https://github.com/rolldabones/slow-ai-kitchen/blob/main/primer/05-part-4-governance-by-design.md#tier-drift-self-tiering-and-re-tiering-triggers); [*Slow AI for the Chief Legal Officer*](slow-ai-for-the-chief-legal-officer.md#10-govern-change-as-well-as-state), Section 10; the hostile-case checklist, [Pattern 6](https://github.com/rolldabones/computational-drafting/blob/main/03-hostile-case-checklist.md#pattern-6-machine-speed), on machine speed |
| Section 7: stating intent | [computational-drafting](https://github.com/rolldabones/computational-drafting), the whole repository; [*The Definition of Done*](https://github.com/rolldabones/definition-of-done); [Take-Out, Delivery & Vending Machines](https://github.com/rolldabones/slow-ai-kitchen/blob/main/take-out-delivery-and-vending-machines.md) for the service ticket; the [AI Impact Assessment Tool](https://github.com/rolldabones/AI-Impact-Assessment-Tool), the Informed Intent gate in tool form |
| Section 9: the named Human | [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md), section 3; Kitchen Step 6 (Gate 5: Final Liability) and Step 9 (Gate 7); [AI Governance for Boards](https://github.com/rolldabones/ai-governance-for-boards) for the same conversation at board altitude |

The Slow AI Kitchen also runs as a guided web application at [kitchen.grcskorea.com](https://kitchen.grcskorea.com/). The repository is the text of record.

## Source basis and attribution

Prepared on 12 October 2026 (KST) against DOCTRINE.md v1.1.1 and ECOSYSTEM.md v1.7.24, Slow AI Kitchen v2.11.1 at commit [`05253ac`](https://github.com/rolldabones/slow-ai-kitchen/tree/05253ac6b4ae4ea51c17e8939b9390868bd4a64b) and computational-drafting v1.4.0 at commit [`9b3c12a`](https://github.com/rolldabones/computational-drafting/tree/9b3c12af7eebae2ea408efd8c78cf545dff8aa5d). The other repositories linked were read at these releases: the book repository v1.7.0, *The Ungoverned Channel* v1.4.4, The Definition of Done v1.2.2, GRCnext-Copilot v2.2.5, RedCap-00 v1.1.4, The AI Generalist v1.1.2, the AI Impact Assessment Tool v1.2.10, AI Governance for Boards v1.5.3 and the sibling publications in this repository as at v1.8.0. Every link into the account was resolved against those releases, anchor included.

The doctrines are used as stated in DOCTRINE.md. *The Human* is capitalized only where it denotes the named owner of section 3 of that file, who in this piece is the driver: the person who states the destination and confirms the arrival, following The Definition of Done, where the Human holds both moments, define and confirm. Elsewhere *human* is the common noun.

Sources outside this account, each read on 12 October 2026 (KST) unless noted:

- Stephen Wolfram, interviewed by Jon Hernandez, ["The future with AI will be very different from what we're being sold"](https://youtu.be/6wc3OuLUiOk), YouTube, 102 minutes. Checked against the auto-generated English captions, which are approximate. Paraphrased throughout and not quoted.
- Son-U Michael Paik, ["Nobody had to explain the horse."](https://lnkd.in/p/gJTMeq9g), LinkedIn, 12 October 2026. The post that led to this piece. Read on the live page.
- Ted Chiang, ["ChatGPT Is a Blurry JPEG of the Web"](https://www.newyorker.com/tech/annals-of-technology/chatgpt-is-a-blurry-jpeg-of-the-web), The New Yorker, 9 February 2023. Read on the publisher's page.
- Grégoire Delétang et al., ["Language Modeling Is Compression"](https://proceedings.iclr.cc/paper_files/paper/2024/hash/3cbf627fa24fb6cb576e04e689b9428b-Abstract-Conference.html), International Conference on Learning Representations, 2024. Abstract read.
- Michael Polanyi, *The Tacit Dimension* (Garden City, NY: Doubleday, 1966), p. 4, as cited in several scholarly works. The line was not read in the book itself.
- United States Department of Defense, news briefing by Secretary Rumsfeld and General Myers, 12 February 2002. Cited by date and not linked, as in *Slow AI for the Chief Legal Officer*.
- Don R. Swanson, ["Undiscovered Public Knowledge"](https://www.journals.uchicago.edu/doi/10.1086/601720), Library Quarterly 56(2): 103–118, April 1986; ["Fish Oil, Raynaud's Syndrome, and Undiscovered Public Knowledge"](https://muse.jhu.edu/article/403510), Perspectives in Biology and Medicine 30(1): 7–18, 1986; ["Medical literature as a potential source of new knowledge"](https://pmc.ncbi.nlm.nih.gov/articles/PMC225324), Bulletin of the Medical Library Association 78(1): 29–37, 1990. The 1990 abstract was read and is the source for the two-year interval.
- Bernardino Romera-Paredes et al., ["Mathematical discoveries from program search with large language models"](https://pmc.ncbi.nlm.nih.gov/articles/PMC10794145), Nature 625: 468–475, published 14 December 2023. Abstract read.
- Google DeepMind, ["AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms"](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/), 14 May 2025. A company announcement and not a peer-reviewed paper.
- Andrej Karpathy, ["Verifiability"](https://karpathy.bearblog.dev/verifiability/), read through Karpathy's Kitchen and on the author's page.
- OWASP Gen AI Security Project, ["LLM01:2025 Prompt Injection"](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) and the [Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/).
- Regulation (EU) 2024/1689 (Artificial Intelligence Act), [Articles 14(4)(b) and 26(2)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng). Article 14(4)(b) and the opening of Article 26(2) were read on the Official Journal page, and Article 26(2) in full on a consolidated reproduction. The application date was read in Regulation (EU) 2026/1744 (OJ L, 2026/1744, 24.7.2026) on the Official Journal page and agrees with [AI Governance for Boards](https://github.com/rolldabones/ai-governance-for-boards/blob/main/05-jurisdictions/eu.md).
- Anthropic, ["Prompt engineering overview"](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview), Claude Platform Docs. One vendor's guidance, cited as an example and not as a standard.
- [*Collier v. Zambito*](https://www.nycourts.gov/reporter/3dseries/2004/2004_00960.htm), 1 N.Y.3d 444 (2004), and [*Flanders v. Goodfellow*](https://www.nycourts.gov/reporter/3dseries/2025/2025_02261.htm), 44 N.Y.3d 57 (2025), New York Court of Appeals, both read on the court's official reporter pages. *Dickson v. McCoy*, 39 N.Y. 400 (1868), is cited as quoted in *Collier* and as described in *Flanders* and was not read directly.
- ["Horse harness"](https://en.wikipedia.org/wiki/Horse_harness), Wikipedia, for the collar, traces, breeching, blinkers and reins. That a driver slows and stops through the reins, and what horses do at cliffs and on the way home, are general knowledge and are not drawn from the article. The mapping of each part to a component around a model is the author's.

**Final Liability rests with the Human.**

---

*This document is provided for general informational and discussion purposes regarding the governance and use of AI. It does not constitute legal advice with respect to any specific matter, jurisdiction or engagement.*
