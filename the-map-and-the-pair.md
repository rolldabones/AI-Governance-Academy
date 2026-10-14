# The Map and the Pair

**A working vocabulary for reading claims that a model has discovered something**

Son-U Michael Paik · former General Counsel, BABL AI Inc. · CEO, GRC Solutions Korea

October 15, 2026

**Starting point.** On 6 October 2026 (UTC) OpenAI published a repository of mathematical manuscripts produced by an internal model, [openai/math](https://github.com/openai/math), and I wrote about it on LinkedIn on 14 October 2026 ([post](https://lnkd.in/p/gn_XXNJM)). This piece develops the vocabulary from that post. It reads the release as dated evidence and takes no position on the mathematics, which I cannot follow. The repository is Apache-2.0 licensed and OpenAI has no involvement in this piece.

**For:** anyone who will be asked, by a board, a Client or a colleague, whether "the model discovered" something, and who has to answer without being able to check the work themselves. That is most of us, and it is the position this piece is written from. The doctrine is [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md) and the method is the [Slow AI Kitchen](https://github.com/rolldabones/slow-ai-kitchen). The piece adds a vocabulary and one test. It adds no doctrine, step, gate, tier or form.

**Durability.** The releases named here will be overtaken, some of them within weeks. The vocabulary is meant to outlast them and to be revised after it has been used on the next release. It is a work in progress and says so: the terms are in use and not settled, the author is still thinking and the piece is published to be argued with. Section 10 records where it is most likely to be wrong.

---

## Contents

- [1. The question](#1-the-question)
- [2. The map](#2-the-map)
- [3. Four positions](#3-four-positions)
- [4. The pair](#4-the-pair)
- [5. The asterisk](#5-the-asterisk)
- [6. Who set the question](#6-who-set-the-question)
- [7. Is any mountain undrawn?](#7-is-any-mountain-undrawn)
- [8. Base Camp](#8-base-camp)
- [9. Your field has no Lean](#9-your-field-has-no-lean)
- [10. Where this argument is weakest](#10-where-this-argument-is-weakest)
- [The vocabulary on one page](#the-vocabulary-on-one-page)
- [Questions for discussion](#questions-for-discussion)
- [This piece and the account](#this-piece-and-the-account)
- [Source basis and attribution](#source-basis-and-attribution)

---

A laboratory announces that its model has discovered something. The announcement is confident, the mathematics is beyond most of the people who will repeat it, and within days someone who can follow the mathematics says it was less than claimed, or more, or the laboratory itself withdraws part of it. This has now happened three times in twelve months, and the vocabulary for discussing it has not kept up. "Discovery", "breakthrough", "solved" and "superintelligence" are being used for things that differ in kind.

This piece offers a small set of terms and one test, so that the next release can be read with the same words as the last. The terms are a picture: a map, four positions on it, a pair that does the discovering, an asterisk, a question of who asked and a Base Camp to stand at.

## 1. The question

I am open to superintelligence. I cannot define it, which bothers me professionally, and I cannot follow the mathematics in the evidence now being offered for it, which pains me personally. I think we are not there, and I find it hard to say what "there" would mean. I suspect that many people who have to form a view are in the same position, and that the honest course is to say so and then do the work that can be done from here.

The nearest I can get to a definition is the last cell of the matrix that Donald Rumsfeld made famous at a Department of Defense briefing on February 12, 2002: the unknown unknowns. [*Slow AI for the Chief Legal Officer*](slow-ai-for-the-chief-legal-officer.md#2-know-what-you-know) uses the four cells to map an organization's risk, and [*The Compression and the Harness*](the-compression-and-the-harness.md#2-four-cells-three-knowers) uses them to sort what a model can and cannot do with knowledge, on the condition that we say who the knower is. This piece stays with the fourth cell and asks one question of it: when a model produces a result, how do we tell whether it reached something unknown to everyone, or did something else that looks like it from a distance?

The rest of the piece is a way of answering that question without being able to do the mathematics. The answer it reaches is that the question cannot be settled by looking at the result alone. It is settled by three other things: who set the question, what checked the answer and how much of the answer the check covered.

## 2. The map

The map is the record: everything written down, in any form, that a model can be trained on or can retrieve. Towns on the map are what is known. Blank space is what is not.

Three qualifications carry over from *The Compression and the Harness* and are stated once here. The map is not the world: a great deal that is known was never written down, and a great deal that was written down is wrong. The model has not read the whole map, though it has read more of it than any one of us. And "written down" now includes code, transcripts, images, measurements and material that machines produced and no person wrote, so the map is larger and stranger than a library, and it keeps growing while the model reads it.

A model's relation to the map is the thing that makes it look superintelligent from a distance. It can hold more of the map in view at once than any human can, and it can move across it faster. Speed, breadth and depth of recall are each beyond our capacity, and the combination is beyond it by a wide margin. We stand on the shoulders of giants; a model stands on all of them at once. Whether that is intelligence of a new kind or recall at a new scale is exactly what the vocabulary below is for, and the piece does not assume the answer.

One more term is needed before the positions. A **town** is a result that is on the map, which means it has been recorded and, in the cases that matter here, checked by someone. A result that has been proposed and not checked is not yet a town. It is a mark in pencil.

## 3. Four positions

Every result a model produces can, once it is checked, be placed in one of four positions relative to the map. Until it is checked it is a pencil mark and has no position. Three of the four lie on the drawn map, on questions that people had already asked. The fourth does not.

**A road.** A connection between two towns already on the map. Don Swanson named the material in 1986: undiscovered public knowledge, where the answer to a question already exists in two literatures that never cited each other. He found a dietary literature and a clinical one that together implied a treatment nobody had tried, and a trial reported the benefit two years later. A model builds roads fast and cheaply, because it has read more of the map than any one of us and a bad road fails quickly where there is something to fail against: the two towns are there to be checked. A road may also run from a town back to itself by another route, which is what a new proof of a known theorem is.

Roads are valuable, and they are the position most often announced as something else. In October 2025 an OpenAI executive posted that GPT-5 had "found solutions to 10 (!) previously unsolved Erdős problems" and made progress on eleven more. Thomas Bloom, who maintains the site that lists those problems, called the post "a dramatic misrepresentation": a problem was marked open on his site only because "I personally am unaware of a paper which solves it", and what the model had done was to find the papers. The post was deleted. Sébastien Bubeck of OpenAI conceded that "only solutions in the literature were found" and added, fairly, that he knew "how hard it is to search the literature". He was right on both counts. The model had built roads to towns that were already on the map, and the announcement had called them mountains. Nothing in the result was wrong. The grading was.

**Higher ground on a known hill.** A verified result on a question people had already asked, which leaves the map taller than we drew it. The hill was ours: we asked the question and sketched the summit. The model's answer improves on ours, either by proving what we had only conjectured, by improving a bound we had set or by finding the exact value we had been circling.

The bound-improving kind is the one *The Compression and the Harness* describes in its [Section 3](the-compression-and-the-harness.md#3-unknown-to-everyone), where a model paired with an evaluator found larger constructions and a faster algorithm than people had. The openai/math release carries the other two kinds, and the vocabulary should be able to place each. Family 088 of the release carries a formalized proof of a conjecture made by C. M. Petty in 1971, that among convex bodies in a space of four or more dimensions the ellipsoids minimize a ratio built from a body's volume and the volume of its projection body. Petty drew the hill; the model is said to have climbed it. Family 017 carries a formalized proof that the irrationality exponent of π is exactly two. The question is old. In December 2019 Doron Zeilberger and Wadim Zudilin had brought the known bound down to about 7.1032, and on 10 September 2026 a human paper brought it to about 7.1019, an improvement of about 0.0013. The model's manuscript is dated 24 September 2026 and claims the value two, which is the floor: every irrational number has exponent at least two, so if the result holds there is nowhere higher to go. That is the limiting case of higher ground, which is the summit itself.

Higher ground is real discovery, and the word should be used without embarrassment. It is not a new vista, because we drew the hill and we asked the question. The map said summit; the model found higher ground. The distinction is not a demotion. It is a statement about who set the question, which Section 6 takes up.

**A valley.** A hill on the map that is not there. A conjecture disproved, a belief lowered, a summit erased. The release carries several. Family 088 also carries a counterexample to a conjecture made by N. S. Brannen in 1996, that the simplex maximizes the same ratio of volumes in every dimension. The model's counterexample is the product of two ten-dimensional simplices, a body in twenty dimensions whose ratio exceeds the simplex's by about 1.5 percent. The hill that said "simplex" at the top is not there in dimension twenty. Family 249 carries a counterexample to the Eilenberg–Ganea conjecture in group theory, a construction that the conjecture said could not exist.

In my post I placed the Brannen result under higher ground, because a body with a larger ratio than the simplex is, literally, higher ground. On reflection it belongs here, and the reason is worth stating because it settles how the two positions differ. A counterexample erases a drawn summit. It does not draw a new one: nobody claims that the product of two simplices is the true maximizer, only that the simplex is not. Higher ground is for a verified improvement to an answer we had given. A valley is for the removal of an answer we had given. The Brannen result removes one and claims no replacement, so it is a valley, and so is every disproof whatever the shape of the conjecture it disproves.

Valleys matter as much as mountains and they are the easiest position to verify, because one checked instance is enough. A universal claim needs a proof that covers every case. A counterexample needs one case, checked all the way down. That asymmetry is why the Brannen counterexample can carry no asterisk at all in dimension twenty, while the proof of Petty's conjecture beside it in the same family, which covers every convex body in every dimension from four upward, is a far larger thing to have checked. The map after a valley is smaller and more honest. It is also, often, the first sign that the hill behind it was drawn in the wrong place.

**An undrawn mountain.** A result in blank space, on a question nobody asked, checked by something outside the model. This is the test. I have not seen one, and Section 7 asks whether one can exist.

The four positions are not a ranking of difficulty or of value. A road can save a life, as Swanson's did, and an undrawn mountain can be useless. They are a classification of what a result does to the map: it joins two drawn features, raises a drawn feature, erases a drawn feature or adds a feature where nothing was drawn. The first three happen on questions we set. Only the fourth does not.

## 4. The pair

Nothing in Section 3 is discovered by a model alone. Discovery belongs to the pair: a proposer and a verifier. *The Compression and the Harness* reached the same conclusion from the systems that pair a language model with an automated evaluator, and the two mathematics releases of 2026 put the point in a form a non-mathematician can see.

In mathematics the verifier available today is a proof assistant, and in these releases it is Lean. Lean's kernel checks that a formal proof proves a formal statement from stated axioms. It does so without opinion and without fatigue, and it does not care who wrote the proof. That is what makes a verified result a town rather than a pencil mark: the check was done by something that has no stake in the answer. The openai/math repository goes further than checking. It publishes a catalogue of what has been formalized and runs each formal result through a tool called the [Comparator](https://github.com/leanprover/comparator), developed by the Lean Focused Research Organization, which takes a challenge file stating the theorem with its proof left blank and confirms that the submitted solution proves exactly that statement, uses no axioms beyond the three standard ones the configuration permits and is accepted by the kernel. A proof with a gap left in it shows up as an extra axiom and fails. Of the 719 manuscripts now in the catalogue, OpenAI's history file records that about 42 percent of top-line results are formalized.

The remaining 58 percent are the point. On 6 October 2026 the repository was published with 722 manuscripts and a sentence in its README: "Some of the unformalized results could have issues." Thirty-one hours later, by the repository's own commit record, OpenAI withdrew three of them. A sign error in a manuscript on the algebraicity of Weil classes, in the words of the repository's history file, "invalidates a stabilization-trace cancellation argument and the construction used by two dependent papers", one of which claimed a case of the Hodge conjecture. The same update revised fourteen other manuscripts for repaired proofs, corrected statements and clearer hypotheses, and updated thirteen more to cite the revised editions. None of the three withdrawn manuscripts appears in the formalization catalogue. Remove the verifier and you get the sign error; and because the model's results build on each other, which the README says openly, the error did not stay where it was made. Two further results stood on it and fell with it.

Three things follow for the vocabulary.

First, **fast is not the same as reliable.** The model that built two further results on the flawed manuscript was the model that wrote it. A model checking its own arithmetic is one more plausible output. A proof checker someone else wrote is not. The release shows both at once, in the same catalogue, and the catalogue tells the reader which is which. That disclosure is the single most useful feature of the release and should become the norm.

Second, **the verifier has to be independent of the proposer and does not have to be smarter than it.** Lean's kernel understands nothing of projection bodies or the irrationality of π. It checks that each step follows from the last. The verifier in the pair is often the dumber party, and that is a feature: it cannot be argued with, flattered or misled by fluency. The method in this account states the same rule for professional work. Verification is "never a re-reading of one's own draft with warmer eyes", in the words of [*The Confirmation*](https://github.com/rolldabones/definition-of-done/blob/main/07-the-confirmation.md#who-confirms), and the adversarial pass "must be run by a different reviewer, a different model or at minimum a different context from the one that produced the claims", in the words of [*Proof-Carrying Analysis*](https://github.com/rolldabones/computational-drafting/blob/main/04-proof-carrying-analysis.md#what-this-is-not).

Third, **the distance between proposer and verifier is the governance problem in one measure.** In the release the formal check, once a formal proof existed, took the kernel minutes and cost next to nothing. In law the verifier is a court, a regulator, a counterparty or a market, and its verdict arrives years later at the Client's expense. A bad idea in mathematics dies fast, against arithmetic. A bad idea about a contract dies in court, long after the fee was paid. The vocabulary did not have a word for that distance when I posted. It has one now, borrowed from navigation. A navigator who cannot see land estimates position from speed, heading and time, and calls it **dead reckoning**; a position confirmed by an external observation is a **fix**. A model working alone works by dead reckoning, each step estimated from the last, and the error accumulates silently until a fix is taken. The sign error was caught and three manuscripts withdrawn within thirty-one hours; until then two further results had been traveling on dead reckoning from a wrong position. The **distance to fix** is how far a proposer travels, in time and in cost, before anything outside it confirms where it is. In formalized mathematics it is minutes. In litigation it is years. In most professional work the distance to fix is the thing to shorten first, and where it cannot be shortened, the output is a draft until the fix arrives.

## 5. The asterisk

A verifier checks what it was given. The asterisk is a result the verifier has reached only in part, and the release is full of them, disclosed.

The clearest illustration is the π result. The formal statement that the kernel checked says that for every exponent above two there is a threshold beyond which every rational approximation to π misses by at least the corresponding amount. It proves that the threshold exists. It does not say what the threshold is. That is not a defect. Results of this kind are often ineffective, in the mathematicians' sense of proving that a bound exists without giving it, and the exponent is exactly what the paper set out to establish. But a reader who hears "the irrationality exponent of π is two" and expects to compute something has been told less than they think, and the release's own scope note for the family says so, in two sentences, and adds that a further consequence in the paper, for a series known as the Flint Hills series, is "outside this selected statement".

The Brannen counterexample carries a different asterisk. The scope note says the paper also proves that the simplex fails to be the maximizer by an exponential factor in every sufficiently large dimension, and that this result "is not included" in the formalization. The valley is verified in dimension twenty and claimed, unverified, for every dimension beyond some unstated point. Dimension three, the case Brannen studied in a second paper in 2005, is not touched by the formal statement at all. The map lost one summit for certain and a range of them on the paper's word.

An asterisk, then, is a boundary, and the reader is owed its location. The release supplies it, in a form I had not seen before: a scope note for every formalized family, stating in prose what the formal statement covers and what it leaves out, with a link to the challenge file that states the theorem in Lean. That challenge file is short. The one for the Brannen counterexample is fewer than fifty lines, and a mathematician can read it in minutes and decide whether the formal definitions of "convex body", "projection body" and "ratio" mean what the paper means by them. Nothing mechanical can make that decision. The repository's own catalogue is candid about this: it records that the formalizations were produced by an agent and that their review status is "unchecked".

A paper from August 2026 by Maher Kallel and Mohamed El Louadi gives the layers a name. Checking that a proof proves its formal statement is one layer, and it is now nearly free. Checking that the formal statement, with every definition it rests on, means the informal question is a second layer, and only a human can do it. Judging whether the result matters is a third, and it is the referee's old job. Measuring the August release of ten Lean-certified results from OpenAI, they found about 20.6 megabytes of proof files against about 55.6 kilobytes of statement files, a ratio of roughly 379 to 1. The machine checks the large part. The human must read the small part, and there are not many humans who can. They call the bottleneck adjudication scarcity, and their line for it is the one to keep: engineering can shrink the audit surface and cannot manufacture the auditor. The same August release produced a dispute over whether one formal statement, concerning a conjecture of Alain Connes, captured the conjecture it was said to refute. The paper takes no position on the mathematics and neither does this piece. The dispute is the point: it arose at the second layer, where the kernel is silent.

Lean, in other words, behaves like a well-drafted contract. It covers exactly what it says and nothing it does not, and the drafting of the statement is where the risk lives. Fixes to the statement are amendments, and in my profession we bill for them.

## 6. Who set the question

A road and a mountain describe the answer. Setting the question is a separate act, and the release is explicit about who performed it. "Over the course of the evaluation, the model was posed approximately 4,000 problems," the README says. The problems were posed by OpenAI. Of roughly 4,000 problems, the catalogue carries 372 families of results, after OpenAI aggregated the output and applied what it calls "an appropriate level of significance". Each result used, on average, about three hours of thinking compute. The reader sees the families that survived. The reader does not see the problems that produced nothing, the problems that produced errors or the prompts in which the problems were put. Critics of the release noticed the last omission in its first week.

So the release records a model sent to roughly 4,000 places on the map by people who chose them, and returning with results from some. That is a great deal. It is not a model that chose the blank space. A model sent to blank space and finding a mountain there has done something. A model that chose the blank space has done something else, and until the second thing happens the undrawn mountain stays undrawn. The point is not that choosing is harder than climbing. It is that the two acts are separable and the vocabulary should keep them separate, because an announcement that merges them claims more than the evidence shows.

Problem provenance is therefore part of the evidence, and laboratories should disclose it. The disclosure has six parts, and openai/math supplies some of them: who posed each problem and when; in what words, which means the prompt; what the model was given to work with, including prior results of its own, which the README says it did build on; the denominator, meaning how many problems were posed and what became of the rest; the selection rule that decided what was published; and who wrote the formal statement that the verifier checked, since a statement written by the proposer is part of the proposal. The release discloses the count of problems, the average compute, the existence of a selection rule, the model's reliance on its own earlier results and the fact that the formalizations were produced by an agent. It does not disclose the prompts, the denominator per problem or the selection rule's content. That is a better record than the field has had, and it is not yet enough to grade a result.

The question of provenance also disposes of "survey", a word I considered for the act of setting the question. In mapmaking the survey is the measurement that produces the map, which is the verifier's work and not the questioner's. Setting the question is choosing where to send the expedition. The plain words will do: who set the question.

## 7. Is any mountain undrawn?

The test asks for a mountain nobody drew. The strongest objection to it is that no such mountain exists, for a model or for us.

The objection runs like this. A model seems superintelligent because it pulls together disparate pieces of information across a far larger compendium than any human can hold, with a speed, breadth and depth beyond our capacities. Individual humans cannot do this; we stand on the shoulders of giants, and even so our reach and our grasp are far shorter. But what the model does with that reach is synthesis, and I am as yet unconvinced that a language model can produce original material that is unrelated to its training corpus. Nor is it obvious that humans do anything different. The ideas an artist pulls together may be original, or may be a synthesis of parts of a lived experience that nobody else had, and I do not know how to tell those apart from the outside.

If that is right, two things follow and neither kills the test.

The first is that "unrelated to the record" is the wrong bar, because no human result clears it either. Newton built on Kepler and Galileo, and what he built was an undrawn mountain by any standard anyone has proposed. Relatedness to the record is not the question. The question is whether a result can be reconstructed as a join of things already recorded, a road however long and however many towns it passes through, or whether it cannot. Swanson's result could be: the two literatures were there, and once joined, the inference was immediate. A result that cannot be so reconstructed is in blank space whatever it was built from.

The second is that the first clause of the test cannot be proved. To show that a result is not a road is to show that no path through the record reaches it, which is a negative over the whole map, and nobody can check the whole map. So the three clauses of the test differ in kind. A mountain nobody drew is a direction: it says what we are looking for and cannot be certified. A question nobody set is a matter of record: it can be documented, and Section 6 says how. Checked by something the model did not write is a matter of audit: it can be inspected, and Sections 4 and 5 say where. The operative test, the part that a reader at Base Camp can apply, is the second and third clause. The first is the reason to apply them.

That leaves the speed, breadth and depth. They are real, and they are the roads position at scale. A model can build roads across the whole map at once, which no human can, and from a distance a thousand new roads look very much like a new mountain. The Erdős episode is the small version of this: literature search mistaken for solution. The large version is the one we have not learned to see yet, where a model joins so many towns so quickly that the joined result is not recognizable as a join. The vocabulary cannot prevent that mistake. It can require that before anyone says "mountain", someone has asked whether the towns were there.

Whether humans do anything other than this is a question the piece leaves open, as its author does.

## 8. Base Camp

Base Camp is where I stand: the observer who cannot make the climb and must still decide whether the summit claim is believed. Most of the people who will act on these results stand there too. The mathematicians who can read the challenge files are few, and the boards, Clients, regulators and journalists who will repeat what the mathematicians say are many.

Base Camp is not idle ground. The maps are kept there, with the oxygen and the radio. The climb is authorized there, the return is awaited there and the retreat is decided there. A summit claim is made by the only people who were on the summit, and the camp's answer to that has to be evidence the climber did not get to write: the photograph, the track, the time. In the release the camp's evidence is the formalization catalogue, the scope notes and the challenge files, and the camp's question is whether they cover the claim being repeated.

If **Final Liability** has a place in this picture, it is here, and the doctrine says which moment. Accountability has three moments in the account's statement of it ([DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md#31-the-allocation-lifecycle)). The owner is named when the work is specified. Accountability attaches when the named human confirms the output against criteria defined in advance. It then holds for as long as anyone relies on the output. Base Camp is the second moment. The Human there signs for a summit without having stood on it, and therefore insists on the verifier, because a signature on an unverified claim is a hope with a name attached. The confirmation has three lawful outcomes, confirm, refuse or amend and confirm, and the release shows all three in the field: results confirmed by formalization, results withdrawn and fourteen results amended with corrected statements and clearer hypotheses.

The third moment is the one the sign error illustrates. Two manuscripts relied on the withdrawn one and fell with it. Reliance is where accountability lives longest, and a result that is relied on before it is fixed carries everything built on it. For a laboratory, Base Camp is the decision to publish. For a mathematician, it is the decision to cite. For a General Counsel, it is the decision to let a model's reading of a contract reach a Client. Each is a confirmation, each should name who made it, and each is answerable for what stands on it afterward.

GRCnext™ adds one thing at Base Camp, which is the retreat. An expedition that cannot come down has not planned an expedition. A Client that has relied on a result it cannot now withdraw from has the same problem, and the exit is designed before the climb or not at all.

## 9. Your field has no Lean

Mathematics is the easy case, and that is why it is the case the laboratories chose. There is a verifier, it is cheap once a formal proof exists, it was written by someone else and it has no stake. The release shows what the pair looks like when all four conditions hold, and it still took the withdrawal of three manuscripts and the repair of fourteen to get to a catalogue that is 42 percent checked.

Professional work has none of the four conditions in that form. There is no kernel for a contract, a regulatory position or a board recommendation. The verifier is slow, expensive and human. It was not written by anyone; it is a court or a market or a consequence. And the distance to fix is measured in years, with the Client paying for the passage. A laboratory that hands you a model and tells you it discovers things has handed you the proposer. The verifier is your problem, and it was your problem before the model arrived.

What the mathematics releases teach, by contrast, is what to build in its place. Four practices in this account are the nearest thing to a kernel that professional work has, and each maps to a feature of the release.

**Decompose the output into claims and give each a status.** [*Proof-Carrying Analysis*](https://github.com/rolldabones/computational-drafting/blob/main/04-proof-carrying-analysis.md#status-values) allows five statuses and no others: verified, inferred, disputed, unverified and superseded. "Anything a model generated is Unverified until a human opens the source. Fluency is not a status." That is the formalization catalogue for a memorandum: a public record of which claims were checked and which were not. A memorandum without it is the 58 percent, and the reader cannot tell.

**Keep the dependency chain.** The same instrument requires every material claim to name the claims it stands on, so that "when a source claim is downgraded ... every claim downstream of it is unverified again, immediately and by construction". That is what OpenAI's history file did by hand on 7 October: three withdrawals, fourteen repairs, thirteen citation updates. An analysis that cannot do the same when a source turns out to be a draft has no chain, and the sign error in it will stay where it is.

**State the asterisk.** A stated gap is a claim in its own right, and the instrument treats it as the most valuable line in the analysis and the one most often lost between the working draft and the Client version. The scope notes in the release are asterisks written out. A professional output should carry the same: what was checked, the standard it was checked against and what the conclusion does not cover.

**Shorten the distance to fix where it can be shortened.** Where a check can be made deterministic, make it so: fetch the citation rather than trust it, recompute the number, compare the clause against the signed version. *The Compression and the Harness* calls this moving work from text the model predicts to results a tool computes, and Karpathy's Kitchen states the rule as [put determinism around probability](https://github.com/rolldabones/slow-ai-kitchen/blob/main/karpathys-kitchen.md#6-put-determinism-around-probability). Where the check cannot be made deterministic, the discipline is **Return to Source**: the ability to walk back from conclusion to evidence to source to observable reality, with verification proportional to consequence ([Coetzee's Kitchen](https://github.com/rolldabones/slow-ai-kitchen/blob/main/coetzees-kitchen.md#iii-return-to-source)). In the method it is performed at [Gate 6](https://github.com/rolldabones/slow-ai-kitchen/blob/main/README.md#step-8-taste-before-service-gate-6-verification-and-validation), before anyone relies on the result, and the release decision at [Gate 7](https://github.com/rolldabones/slow-ai-kitchen/blob/main/README.md#step-9-open-the-pass-gate-7-human-release-decision) is Base Camp with a form.

None of this makes professional analysis deductive, and the instrument that carries it says so. It makes the analysis inspectable, which is the property the release had and most professional output does not. The laboratories have shown the field what a disclosed verification status looks like. The field should be embarrassed into adopting one.

Until a release shows a mountain nobody drew, on a question nobody set, checked by something the model did not write, what we have is super-recall, super-patience and a verifier someone else wrote. That is a great deal. It is not the thing the word superintelligence is reaching for, and the people who will have to decide whether to rely on these systems deserve a vocabulary that keeps the two apart.

## 10. Where this argument is weakest

A discussion piece should say where it can be attacked. These are the objections I take most seriously, in the order I would raise them against myself.

**The author cannot check the examples.** Every mathematical statement in this piece is taken from the release's own scope notes, challenge files and history, read directly, and from the two human papers on the irrationality measure of π. I have not verified any of the mathematics and could not. If a scope note misdescribes its formal statement, this piece repeats the error. The piece's argument is about how to read such claims from Base Camp, and it is itself written from there.

**The positions may not be stable.** Section 3 places the Brannen counterexample as a valley and the π result as higher ground. A reader could argue that a counterexample which exhibits an explicit better body is higher ground, or that the Petty proof, which confirms a drawn hill rather than raising it, needs a position of its own. I have chosen to grade by what a result does to the drawn map and to accept that some results do two things. A fifth position, a confirmed hill, was considered and not added: a conjecture is a hill sketched without a measured height, and a proof gives it one, which is higher ground on the definition in Section 3. The vocabulary stays at four until a release produces a result the four cannot place, and that is the first thing the next release will be read for.

**"Checked by something the model did not write" is porous.** The kernel was written by others. The formal statement and the formal proof were written by the agent, and the catalogue says their review status is unchecked. A reader could say the test is already met in form and not in substance, and I would agree: the test's third clause has to be read with Section 5, where the statement is part of the proposal and a human still has to read it.

**The undrawn mountain may be a mirage.** Section 7 concedes that the first clause of the test cannot be proved and that human originality may be synthesis too. If so, the test's first clause is aspiration rather than criterion, and a reader who wants a criterion will find only the second and third clauses. I think that is the honest position. It is not a strong one.

**A model may already have set a question.** The README says that some outputs build on earlier results the models produced. If, inside those three hours, a model chose a lemma to pursue that no person had posed, the line between "sent to blank space" and "chose the blank space" is thinner than Section 6 makes it. Provenance disclosure would settle this and has not been given.

**The mathematics is the wrong field to learn from.** Section 9 says mathematics is the easy case. A reader could reply that it is therefore the wrong case, and that lessons from a field with a free verifier do not transfer to fields without one. The practices in Section 9 are my answer, and they are a design, not a proof that the transfer works.

**The August release is read second-hand.** This piece reads openai/math closely and the August release of ten results only through one paper about it. A reader of the August release's own repository may find that it discloses more than I have credited, or less.

**The vocabulary is mine and the metaphor is common.** Mountains, maps and summits are stock images, and the week of the release produced plenty of them. The terms here are useful to the extent they are defined and applied consistently, and the test is useful to the extent it is applied to the next release and the one after it. If it is not, this is a post that outstayed its welcome.

---

## The vocabulary on one page

| Term | What it means | What verifies it | Example in this piece |
|---|---|---|---|
| The map | The record: everything written down that a model can learn from or retrieve | Nothing; it is the given | Section 2 |
| A town | A result on the map, recorded and checked | Prior verification | Any theorem in the literature |
| A road | A connection between two towns already on the map | The two towns, which can be opened | The Erdős problems, October 2025 |
| Higher ground on a known hill | A verified improvement to an answer we had given, on a question we asked: a conjecture proved, a bound improved, an exact value found | A proof covering every case | Petty's conjecture for n ≥ 4; the irrationality exponent of π |
| A valley | A hill on the map that is not there: a conjecture disproved | One instance, checked all the way down | Brannen's conjecture in dimension 20; Eilenberg–Ganea |
| An undrawn mountain | A result in blank space, on a question nobody set, checked by something the model did not write | The test; not yet seen | None |
| The pair | A proposer and a verifier; discovery belongs to the pair | The verifier's independence from the proposer | Model plus Lean kernel plus a human who reads the statement |
| The asterisk | A result the verifier has reached only in part; a boundary the reader is owed | The scope note and the challenge file | The π threshold; the Brannen large-dimension claim |
| Dead reckoning | A model working alone, each step estimated from the last | Nothing, until a fix | The sign error before 7 October |
| A fix | A position confirmed by something outside the proposer | The verifier | The kernel check; a court's judgment |
| Distance to fix | How far a proposer travels, in time and cost, before a fix | Measured, not verified | Seconds in formalized mathematics; years in litigation |
| Who set the question | Problem provenance: who posed what, when, in what words, from what, selected how and who wrote the formal statement | Disclosure | About 4,000 problems posed by OpenAI |
| Base Camp | Where the observer who cannot climb decides whether the summit claim is believed; where Final Liability attaches, at confirmation | The three lawful outcomes: confirm; refuse; amend and confirm | The decision to publish, to cite, to rely |

The three navigation terms, dead reckoning, the fix and distance to fix, are the newest in the vocabulary and the first to be revised after use on the next release.

## Questions for discussion

1. Take the last AI result your organization repeated to a board or a Client. Which of the four positions was it, and who checked? (Section 3)
2. For one AI output you rely on weekly, what is the verifier, who wrote it and does it have a stake in the answer? (Section 4)
3. What is the distance to fix for that output, in time and in money, and who pays for the passage? (Section 4)
4. Where is its asterisk written down? If nowhere, what does the reader believe the output covers that it does not? (Section 5)
5. Who set the question the model answered, and in what words? What happened to the questions that produced nothing? (Section 6)
6. Can you name a result in your own field that could not be reconstructed as a join of things already recorded? How do you know? (Section 7)
7. Who stands at Base Camp for your organization's reliance on model output, and what evidence do they insist on before signing? (Section 8)
8. When a source your analysis rests on is withdrawn, how long does it take to find every conclusion that stood on it? (Section 9)
9. Which objection in Section 10, if it is right, would change how you read the next release?
10. The next laboratory announcement will use the word "discovered". Before repeating it, which two questions from this list will you ask?

## This piece and the account

The piece is a reading of work that already exists in this account. Each row points to where the argument is carried as an instrument. Repositories the argument does not touch are left out. The full map is [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md).

| In this piece | Where the account carries it |
|---|---|
| Sections 1 and 2: the four cells and the record | [*Slow AI for the Chief Legal Officer*](slow-ai-for-the-chief-legal-officer.md#2-know-what-you-know), Section 2; [*The Compression and the Harness*](the-compression-and-the-harness.md#1-a-compression-of-what-was-written), Sections 1 and 2; [*Sounds Good*](sounds-good.md#3-the-mechanism-why-sounds-good-is-technically-accurate) for why fluent output is not a status |
| Section 3: roads and the Swanson join | [*The Compression and the Harness*](the-compression-and-the-harness.md#2-four-cells-three-knowers), Section 2, on undiscovered public knowledge |
| Section 4: the pair, the evaluator and proportion in checking | [*The Compression and the Harness*](the-compression-and-the-harness.md#3-unknown-to-everyone), Section 3; [Karpathy's Kitchen](https://github.com/rolldabones/slow-ai-kitchen/blob/main/karpathys-kitchen.md#11-verifiability), Section 11; [*The Confirmation*](https://github.com/rolldabones/definition-of-done/blob/main/07-the-confirmation.md#who-confirms) on the independence of the verifier |
| Section 5: the asterisk, the stated gap | [*Proof-Carrying Analysis*](https://github.com/rolldabones/computational-drafting/blob/main/04-proof-carrying-analysis.md#six-claim-types), uncertainty as a claim type |
| Section 6: who set the question | [computational-drafting](https://github.com/rolldabones/computational-drafting), the objective element of a specification; [*The Definition of Done*](https://github.com/rolldabones/definition-of-done), where the Human defines before the work begins |
| Section 8: Base Camp and the three moments | [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md#31-the-allocation-lifecycle), section 3.1; [*The Confirmation*](https://github.com/rolldabones/definition-of-done/blob/main/07-the-confirmation.md#the-three-lawful-outcomes); Kitchen Step 9 (Gate 7); [GRCnext-Copilot](https://github.com/rolldabones/GRCnext-Copilot/blob/main/methodology/glossary.md) for the Exit |
| Section 9: the practices | [*Proof-Carrying Analysis*](https://github.com/rolldabones/computational-drafting/blob/main/04-proof-carrying-analysis.md), the whole file; [Coetzee's Kitchen](https://github.com/rolldabones/slow-ai-kitchen/blob/main/coetzees-kitchen.md#iii-return-to-source) for Return to Source; Kitchen Step 8 (Gate 6) and Step 9 (Gate 7); [AI Governance for Boards](https://github.com/rolldabones/ai-governance-for-boards) for the same questions at board altitude |

The Slow AI Kitchen also runs as a guided web application at [kitchen.grcskorea.com](https://kitchen.grcskorea.com/). The repository is the text of record.

## Source basis and attribution

Prepared on 15 October 2026 (KST) against DOCTRINE.md v1.1.1 and ECOSYSTEM.md v1.7.25, Slow AI Kitchen v2.11.1 at commit `05253ac`, computational-drafting v1.4.0 at commit `9b3c12a`, The Definition of Done v1.2.2 at commit `4bdc2cd`, GRCnext-Copilot v2.5.0 and AI Governance for Boards v1.5.3, and the sibling publications in this repository as at v1.9.0. Every link into the account was resolved against those releases, anchor included.

The doctrines are used as stated in DOCTRINE.md. *The Human* is capitalized only where it denotes the named owner of section 3 of that file, who in this piece stands at Base Camp. Elsewhere *human* is the common noun.

The vocabulary and the test are the author's, first stated in his LinkedIn post of 14 October 2026 on the openai/math release and developed here. The reclassification of the Brannen counterexample, the three navigation terms introduced in Section 4 and the whole of Section 7 are new in this piece.

Sources outside this account, each read on 14 or 15 October 2026 (KST) unless noted:

- OpenAI, [openai/math](https://github.com/openai/math), GitHub, Apache-2.0. Read directly: the README at the initial commit (`adc7f12`, 6 October 2026, 21:58 UTC, which is 7 October, 06:58 in Seoul) and at `main`; `history.md`, whose entry is dated 7 October 2026 and whose commit (`3014888`) is timestamped 8 October 2026, 05:03 UTC, 31 hours and 5 minutes after the initial commit; the scope notes `lean/docs/017.md`, `lean/docs/088.md` and `lean/docs/249.md`; `lean/formalization.yaml` (version v0.4, `automation: method: agent`, `review: status: unchecked`); `lean/README.md` and `lean/ComparatorChallenges/README.md`; and the challenge files `PiExponent.lean`, `ProjectionCounterexample.lean`, `PettyProjectionVolume.lean` and their `.json` configurations. Commit timestamps were read from the GitHub API. The manuscripts themselves were not read. The ratio 22,355,476 to 22,020,096 is as stated in the scope note; the 1.5 percent is the author's arithmetic. That none of the three withdrawn manuscripts appears in the formalization catalogue was checked by searching the catalogue for their titles.
- Lean FRO, [Comparator](https://github.com/leanprover/comparator), GitHub. The README was read for what the tool checks: statement equality against the challenge, permitted axioms and kernel acceptance, with a note that definition holes must be reviewed by a human. That a proof gap left as `sorry` registers as an axiom is standard Lean 4 behavior and is stated from general knowledge.
- Anthony Ha, ["OpenAI's 'embarrassing' math"](https://techcrunch.com/2025/10/19/openais-embarrassing-math/), TechCrunch, 19 October 2025. Source for the quotations from Kevin Weil (as reported from a deleted post), Thomas Bloom and Sébastien Bubeck. The deleted post and the replies were not read on X. Reports of the deleted post differ in minor wording; only the phrase common to them is quoted here, and Bloom's "misrepresentation" was confirmed against a second report, Sherwood News, 20 October 2025.
- OpenAI, ["Ten advances in mathematics and theoretical computer science"](https://openai.com/index/ten-advances-in-mathematics/), 1 August 2026, and the repository [openai/ten-proofs](https://github.com/openai/ten-proofs). The announcement was read. The repository was not read; it is described here only through the paper below.
- Maher Kallel and Mohamed El Louadi, ["Verification abundance, adjudication scarcity: what happens to mathematical knowledge when proof checking becomes free"](https://arxiv.org/abs/2608.28997), arXiv:2608.28997, 29 August 2026. A preprint, not peer reviewed. Read for the three layers, the 20.6 MB to 55.6 KB measurement, the phrase on the audit surface and the existence of the Connes dispute. The paper states that it takes no position on the mathematics of that dispute, and this piece follows it.
- Doron Zeilberger and Wadim Zudilin, ["The Irrationality Measure of π Is at Most 7.103205334137..."](https://arxiv.org/abs/1912.06345), arXiv:1912.06345, December 2019, revised January 2020. Abstract read.
- Yufei Bai, ["The irrationality measure of π is at most 7.101862832357"](https://arxiv.org/abs/2609.11276), arXiv:2609.11276, submitted 10 September 2026. Abstract read. A preprint, not peer reviewed. That every irrational number has irrationality exponent at least two is standard and is stated from general knowledge.
- C. M. Petty, "Isoperimetric problems," Proceedings of the Conference on Convexity and Combinatorial Geometry, University of Oklahoma, 1971, pp. 26–41; N. S. Brannen, "Volumes of projection bodies," Mathematika 43 (1996), 255–264, and "Three-dimensional projection bodies," Advances in Geometry 5 (2005), 1–13. All three are cited as given in the bibliography of Christos Saroglou, ["On the shape of a convex body with respect to its second projection body"](https://arxiv.org/abs/1409.4347), arXiv:1409.4347, which was read for the statement of both conjectures and the planar case, and were not read directly.
- Don R. Swanson, ["Undiscovered Public Knowledge"](https://www.journals.uchicago.edu/doi/10.1086/601720), Library Quarterly 56(2), 1986; ["Fish Oil, Raynaud's Syndrome, and Undiscovered Public Knowledge"](https://muse.jhu.edu/article/403510), Perspectives in Biology and Medicine 30(1), 1986; ["Medical literature as a potential source of new knowledge"](https://pmc.ncbi.nlm.nih.gov/articles/PMC225324), Bulletin of the Medical Library Association 78(1), 1990. Cited as in *The Compression and the Harness*, where the 1990 abstract was read for the two-year interval; not re-read for this piece.
- United States Department of Defense, news briefing by Secretary Rumsfeld and General Myers, 12 February 2002. Cited by date and not linked, as in the sibling publications.
- David H. Bailey, ["OpenAI stuns mathematicians with 722 new papers"](https://mathscholar.org/2026/10/openai-stuns-mathematicians-with-722-new-papers/), Math Scholar, 7 October 2026. Read for the reported objection that the prompts had not been released. A secondary report; the press coverage it draws on was not read.
- Son-U Michael Paik, [LinkedIn post of 14 October 2026](https://lnkd.in/p/gn_XXNJM) on the openai/math release, and its two comments. The post that led to this piece. The short link is the author's; it could not be resolved from the session that prepared this file and was clicked through and confirmed by the author on 15 October 2026 (KST) before upload, as the sibling publications' links were.

**Final Liability rests with the Human.**

---

*This document is provided for general informational and discussion purposes regarding the governance and use of AI. It does not constitute legal advice with respect to any specific matter, jurisdiction or engagement.*
