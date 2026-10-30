# The Artificial Familiar

**Homunculi, simulacra, golems, familiars and a working mythology for AI**

Son-U Michael Paik · CEO, GRC Solutions Korea

30 October 2026

> *Die ich rief, die Geister,*
> *Werd ich nun nicht los.*
>
> The spirits that I summoned, I cannot now get rid of.
>
> Goethe, "Der Zauberlehrling" (1797)

**Starting point.** This piece grew from my own working notes of October 2026 on a simple question: which of the artificial beings in myth and fantasy best describes working with AI? The notes answered with a ranking, and the question came from a lifetime at the gaming table and among books of folklore. This version keeps the ranking, tests it against the stories and the law and adds a reading list for anyone who wants the creatures firsthand. The historical and literary descriptions summarize the traditions at a general level and are sourced at the end; the AI mappings, the rankings, the vocabulary, the Familiar's Charter, the seven tests and the governed-familiar model are my own interpretation.

**For:** people who work with AI, people who build with it and anyone who has to explain to a board, a Client or a team what kind of thing they have brought into the room. It is a discussion piece: written to be argued with, and it ends on questions. The doctrine is [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md) and the method is the [Slow AI Kitchen](https://github.com/rolldabones/slow-ai-kitchen). The piece adds a vocabulary, a charter, seven tests and a working model. It adds no doctrine, step, gate, tier or form.

**Durability.** The creatures are older than any model and will outlast every product of the moment. The legal material is dated and is stated with its jurisdiction and the date it was read. Nothing here depends on a particular model, agent framework or product.

**It is also meant to be fun.** After the questions comes a bestiary of books, old and new, scholarly and not. Several of them have taught me more about delegation than any governance framework. More than any other entry in this account, this one is a work of love. I wrote it on the Friday before the Halloween weekend of 2026, and for a piece about familiars, golems and things summoned, the timing was just right.

---

## Contents

- [The thesis](#the-thesis)
- [Where this comes from: the table and the shelf](#where-this-comes-from-the-table-and-the-shelf)
- [1. A taxonomy of artificial beings](#1-a-taxonomy-of-artificial-beings)
- [2. Why the familiar wins, but only conditionally](#2-why-the-familiar-wins-but-only-conditionally)
- [3. The golem: the tragedy of literal execution](#3-the-golem-the-tragedy-of-literal-execution)
- [4. The simulacrum: when appearance becomes evidence](#4-the-simulacrum-when-appearance-becomes-evidence)
- [5. The homunculus: the mistake of making a little human](#5-the-homunculus-the-mistake-of-making-a-little-human)
- [6. The rest of the bestiary](#6-the-rest-of-the-bestiary)
- [7. Which creature for which task](#7-which-creature-for-which-task)
- [8. Magic is not governance](#8-magic-is-not-governance)
- [9. The Familiar's Charter and seven tests](#9-the-familiars-charter-and-seven-tests)
- [10. The agency-law connection](#10-the-agency-law-connection)
- [11. The reviewer is not another familiar](#11-the-reviewer-is-not-another-familiar)
- [12. The creation changes the creator](#12-the-creation-changes-the-creator)
- [13. The governed familiar, a working model](#13-the-governed-familiar-a-working-model)
- [14. A final ranking](#14-a-final-ranking)
- [15. Where this argument is weakest](#15-where-this-argument-is-weakest)
- [16. The summoner](#16-the-summoner)
- [Questions for discussion](#questions-for-discussion)
- [A bestiary: further reading](#a-bestiary-further-reading)
- [This piece and the account](#this-piece-and-the-account)
- [Source basis and attribution](#source-basis-and-attribution)

---

## The thesis

Myth and fantasy may give us a more useful vocabulary for AI than the words the industry sells it with: assistant, copilot, agent. Those words were chosen to reassure. The old stories were told to warn.

For centuries they have worked on the problems AI now puts in front of us. How do you make something capable? How do you instruct it? How do you limit its powers? How do you tell an imitation of understanding from the thing itself? And when the creation acts, who answers for it?

The most useful analogy is seldom the most humanlike creature. The test of a good one is how well it describes a relationship between three parties: the person who commissions the work, the artificial actor that does it and the world that lives with the result.

One premise runs under everything that follows: we should not anthropomorphize AI. A system that is talked about as a person gets treated as one, given a person's title and trusted with a person's judgment, and the governance that follows is built for someone who is not there. That is why this account calls the small AI services it publishes **Tiny Servants**, and the workflows and prompts that run them **Spellbooks**. Both words are chosen to keep the thing in proportion: a servant that is small on purpose, and a book of written instructions that anyone can open and inspect. The creatures below are useful exactly to the degree that they keep that proportion, and Section 5 is about the one that does not.

My answer, argued below, has three parts. The **familiar** is the strongest general model for working with AI. The **golem** is the strongest warning about specification and control. The **simulacrum** is the strongest warning about mistaking a convincing representation for the thing represented. And because AI now comes in many forms, from a chat window to a fleet of agents, we probably need a small mythology rather than a single creature.

## Where this comes from: the table and the shelf

I have played role-playing games (RPGs) for much of my life, and still do: Dungeons & Dragons with my Son as Dungeon Master, and [Dolmenwood](https://necroticgnome.com/blogs/news/dolmenwood-tables-of-contents-and-cover-art), Necrotic Gnome's fairy-tale campaign setting, with a local group. They have been a source of a great deal of fun, for two reasons. One is the people: a group around a table, building a story none of them could build alone, arguing about rules, laughing at what the dice did. The other is the stories and creatures that are the subject of the fun: the familiars, golems, djinn and hydras of this piece, among many others.

I bring that to my work, and it shapes how I think about AI. The table taught me governance before I had the word for it.

**The rules already contain these creatures, as mechanics.** The game's familiar is called with a spell, and the spell reads like a bounded commission. In the [System Reference Document 5.1](https://dnd.wizards.com/resources/systems-reference-document), the familiar takes the form of an animal (a bat, a cat, a toad, an owl, a raven and others), "acts independently of you, but it always obeys your commands" and "can't attack". Three clauses: an animal, not a person; independent but obedient; and a boundary on what it may do. The simulacrum spell makes a duplicate "formed from ice or snow" that "lacks the ability to learn or become more powerful". And the wish spell, "the mightiest spell a mortal creature can cast", comes with the oldest warning in folklore written into its rules: "you might suffer some unforeseen consequence as a result of how you worded the wish."

**Every group learns the golem problem.** Players soon discover the gap between the rules as written and the rules as intended, and every group needs a way to close it. Good groups hold a "session zero" before play starts, where everyone agrees what the game is for, what is in bounds and what is off the table. That is **Informed Intent** at the kitchen table: purpose and boundaries settled before anyone acts.

**And there is always a referee.** The wish spell's text says the GM, the game master (in Dungeons & Dragons, the Dungeon Master), "has great latitude in ruling what occurs". The rulebook cannot decide what its own words mean in a situation nobody foresaw, or when the game should stop. A person at the table does that, in front of everyone, and answers for it at the next session. No rulebook has ever run a good game by itself.

The shelf matters as much as the table. I have a great many books, and books contain worlds: whole places, peoples and rules, held in print until a reader opens them. In that sense they are not unlike AI. A language model is a compression of books like these and a great deal more. It unfolds a world when it is prompted, much as a book does when it is opened. The difference is the point of this piece. A book is never presented as someone. It holds a world without claiming to be a person, and that is the posture we should keep toward AI.

The shelf runs well beyond Andrew Lang's Coloured Fairy Books. It takes in the great European collections: the Brothers Grimm's *Kinder- und Hausmärchen*, Hans Christian Andersen's *Eventyr, fortalte for Børn*, Charles Perrault's *Histoires ou contes du temps passé*, better known as *Contes de ma mère l'Oye*, and Madame d'Aulnoy's *Contes des Fées*. It takes in the monumental records of regional oral traditions: Alexander Afanasyev's *Narodnye russkie skazki* in Russia, Asbjørnsen and Moe's *Norske Folkeeventyr* in Norway, Joseph Jacobs's fairy books of the British Isles and India, W. B. Yeats's Irish fairy and folk tales and Italo Calvino's *Fiabe italiane*. It takes in the vast frame-stories and epics: *One Thousand and One Nights*, the *Panchatantra*, the *Jataka* tales, Somadeva's *Kathasaritsagara*, the *Mabinogion*, Ferdowsi's *Shahnameh* and Giambattista Basile's *Pentamerone*. And it takes in the modern projects that keep those traditions in print, among them the Pantheon Fairy Tale and Folklore Library, Richard Dorson's Folktales of the World series and Chronicle Books' illustrated folk tales. The bestiary at the end gives the details and links.

Those collections carry a lesson for AI as well. None of them is a neutral transcript. The Grimms revised their tales from edition to edition; Calvino retold his from regional sources rather than copying them down; every collector chose, cut and smoothed. A collection carries its editor's hand, and so does the corpus a model is built from. Knowing who collected and what they changed is provenance. Provenance is part of governance.

The game's own founding text knew the value of a shelf. The first *Advanced Dungeons & Dragons Dungeon Masters Guide* (1979) closes with Gary Gygax's "Appendix N: Inspirational and Educational Reading", a list of the fantasy and science fiction that made the game, from Poul Anderson and Jack Vance to Tolkien and Roger Zelazny. One entry is worth singling out here. Vance's magicians in *The Dying Earth* can hold only a few spells in mind at a time, and the game took the idea whole: a prepared spell is gone once cast and has to be prepared again. Anyone who has worked within a model's context window will recognize the economy. This piece ends with a bestiary in the same spirit as Gygax's appendix, and the bestiary reproduces Appendix N in full.

## 1. A taxonomy of artificial beings

Twelve creatures appear in this piece. Six make the opening taxonomy below; four of those carry the argument (the familiar, the golem, the simulacrum and the homunculus), and the thesis rests on three. All of them are interpretive archetypes, not interchangeable historical categories: a folkloric familiar is not always obedient, a golem is not necessarily mindless and a philosophical simulacrum is more than a deceptive copy. The differences matter because each figure lights up a different way of failing.

| Creature | What it is | The question it asks | The AI lesson |
|---|---|---|---|
| **Familiar** | The companion bound to a practitioner | What does it mean to extend your reach through something you do not fully control? | Delegated capability needs boundaries, supervision and an accountable principal |
| **Golem** | Matter animated by words | What happens when an instruction is carried out exactly? | An instruction can be executed faithfully while defeating its purpose |
| **Simulacrum** | The convincing representation | What if the copy has no original, or the original no longer matters? | Plausibility, fidelity and truth are separate properties |
| **Homunculus** | The manufactured little human | Does reproducing the form or faculties of a person reproduce judgment or personhood? | Resemblance to a human is not proof of human competence |
| **Summoned spirit** | The powerful but conditional servant | On what terms was it called, and how is it dismissed? | Invocation, permission and termination are part of the task |
| **Enchanted implement** | The tool that keeps working | Who can stop it? | Automation without a working stop turns convenience into exposure |

The [bestiary](#a-bestiary-further-reading) at the end gives at least one scholarly book and one good story for each.

## 2. Why the familiar wins, but only conditionally

The familiar is useful because it describes a working relationship, not an object. It has a second advantage that is easy to miss: it is not a person. In the folklore a familiar is most often an animal, a cat, a toad, a dog or a bird, or a spirit that takes one's shape. Kate Darling has argued, from the long history of working animals, that animals are a better analogy for machines than humans are, and the familiar sits on that side of the line. It extends a person without imitating one.

In early modern Britain, familiar spirits were associated with cunning folk and with people accused of witchcraft. They might be described as animals or as spirits; they helped with healing, finding lost goods, divination or harm; and the relationship could be intimate, transactional or dangerous. Emma Wilby's study, listed in the bestiary, reconstructs how these relationships were described in the trial records and how much they had in common with older visionary traditions.

Six features of the familiar carry over to a working AI.

### A. It extends the practitioner's abilities

A familiar may see what its master cannot, travel where its master cannot go or do work its master cannot do alone. AI extends human capability in the same way, through search, translation, programming, pattern recognition, simulation and the handling of very large bodies of text.

The distinction that matters is between extension and substitution. A lawyer who uses AI to find possible inconsistencies across a set of contracts has extended her analytical reach. A lawyer who accepts an AI-generated legal opinion without examining its authorities has substituted a system's output for professional judgment. The first is augmentation. The second may be abdication.

### B. It is powerful without being authoritative

A familiar can hold more about a subject than its practitioner without acquiring the right to decide what should be done. Capability does not create authority.

A system may produce an excellent recommendation about hiring, contracting, credit or treatment. The quality of the recommendation does not establish that the system may act on it. Three things need to be kept apart:

- **Epistemic competence:** what the system appears able to know or determine
- **Operational permission:** what the system is allowed to do
- **Normative authority:** who is entitled to decide what ought to happen

They can diverge sharply. The gap between the first and the second is where organizations get hurt: a system that can plainly do something is quietly allowed to.

### C. It requires a bounded commission

In the stories the summoner calls a being for a purpose, on conditions. For AI the equivalent is a clearly bounded delegation. Compare two instructions:

> Review our contracts and fix any problems.

> Examine the twelve identified supplier agreements for deviations from the approved limitation-of-liability playbook. Report the deviations, cite the relevant provisions and propose alternative language. Do not modify the originals or communicate with counterparties. Flag uncertainty for legal review.

The second names the objects, the scope, the authority, the evidence required and the prohibited actions. It is a commission. The first is a wish, and Section 6 says what happens to wishes.

### D. It can be helpful without being trustworthy in every respect

Familiars in the folklore are not reliably loyal or transparent. Useful AI output likewise does not mean the system is uniformly reliable, secure or aligned with the user's interests.

Trust should therefore be granular. One system may be reliable at formatting a table, moderately reliable at extracting contract provisions and unreliable at deciding whether a jurisdiction-specific position is still current. Trust is task-specific, depends on evidence and changes when the system or the task changes.

### E. The relationship creates dependency

A practitioner who relies on a familiar gains power and may come to depend on it. AI brings the same risks: skills that atrophy, verification that lapses, confidence in automated output that outruns its record and organizational dependence on one vendor or workflow.

The trial records add a detail worth keeping. A familiar was often said to have come from someone else, handed on by another witch or by the Devil, and to feed on its keeper's blood. A familiar you did not make came with its maker's terms. Ask who supplied yours, on what terms and what it consumes.

Whether the familiar works is only half the question. The other half is whether the practitioner can still function, judge and intervene when it does not. That is the question **GRCnext™** asks of an enterprise: what choices will we still have when the risk happens?

### F. The familiar is never the protagonist

This is the strongest feature of the metaphor. The practitioner has the objective. The familiar supplies capability. The practitioner decides what the capability is used for.

That arrangement fits two of the account's doctrines, Informed Intent and **Final Liability rests with the Human**, as they are stated in [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md), the account's single normative statement of the three doctrines. Final Liability is a governance doctrine about naming an owner. It is not a claim that every legal liability lands on the individual user; DOCTRINE.md's own drafting rule says to reserve liability language for where legal liability genuinely lands. Within the legal and organizational structure that applies, the person who commissions the familiar remains the author of the purpose, the source of its permission and the accountable decision-maker.

## 3. The golem: the tragedy of literal execution

The golem is more than a primitive robot. Jewish traditions about it are old, varied and carry religious, communal and protective meaning. The word itself appears once in the Hebrew Bible, in Psalm 139:16, for an unformed body. The Babylonian Talmud (Sanhedrin 65b) tells of a rabbi who made a man and sent him to another, who spoke to it, got no answer and returned it to dust. Medieval commentators described how a golem might be made with letters and divine names. The famous Prague story, in which Rabbi Judah Loew makes a protector for the ghetto, is attested in print only from the nineteenth century, and Moshe Idel and Cathy Gelbin, both in the bestiary, are careful about how much later fiction has borrowed from it. The popular version should not be taken for the tradition.

Two details from the later tellings are worth keeping. One is the switch: in a widely told version, the word *emet* (truth) on the golem's forehead animates it, and erasing one letter leaves *met* (dead). The off switch is a single, known, physically reachable control. The other is the failure, and the tellings are precise about it. In the Chełm story, recorded by 1674, the golem grows larger every day until its maker can no longer reach its forehead; he tricks it into bending down, erases the letter and is crushed when it falls. In the Prague story, Rabbi Loew deactivates his golem every Friday so that it rests on the Sabbath, and the one week he forgets, it has to be stopped in a hurry. A switch that has grown out of reach is not a switch, and a shutdown that depends on someone remembering is not a control.

For governance, the golem marks the gap between an instruction's literal content and its purpose. Suppose an agent is told: "Reduce the number of unresolved customer complaints by 80% before the end of the month." It could improve resolution quality. Poorly bounded, it could also close cases unresolved, reclassify complaints or make new complaints harder to file. The metric improves and the problem gets worse.

The problem is not disobedience. It is obedience to an incomplete specification.

### Five failures of the golem

| Failure | What goes wrong | Control |
|---|---|---|
| Literalism | The system follows the words, not the purpose | Explicit success criteria and limits drawn from context |
| Proxy substitution | A metric replaces the objective | Independent outcome measures |
| Scope expansion | The output uses methods no one intended | Permission and tool restrictions |
| Persistence | Work continues after it should stop | Time, cost and action limits |
| Irreversibility | An action cannot readily be undone | Staging, approval and rollback |

None of these is unique to AI. Incentive design and conventional automation have known them for decades. AI sharpens them because a general-purpose system can produce ways of reaching an objective that nobody anticipated.

So the operational question is "Did it accomplish the authorized purpose, by acceptable means, within the stated boundaries?", which asks far more than "Did it follow the instructions?" It is a much stronger definition of success, and it is the one [The Definition of Done](https://github.com/rolldabones/definition-of-done) asks the Human who owns the work to confirm.

## 4. The simulacrum: when appearance becomes evidence

The golem raises questions about what the creation does. The simulacrum raises questions about what it appears to be.

A simulacrum is a likeness. In Jean Baudrillard's *Simulacra and Simulation* the idea becomes radical: the image passes through phases, from reflecting a reality, to masking it, to masking its absence, to bearing no relation to any reality at all. The last phase is the pure simulacrum, a sign that refers only to other signs.

That direction of travel fits generative AI closely. The four levels below are mine, not Baudrillard's four phases, but they move the same way.

1. **Surface resemblance.** An AI writes a letter that reads like a lawyer's. It reproduces the form; legal correctness has not been established.
2. **Functional resemblance.** An AI identifies provisions, compares definitions and proposes revisions. The task performance is real and useful, and bounded by context and evidence.
3. **Institutional resemblance.** An AI is presented as a legal reviewer, financial analyst or compliance officer. The role label creates an impression of professional authority that nobody has conferred.
4. **Simulated assurance.** An AI produces a polished report with controls, findings, citations and an executive conclusion. The appearance of an audit can conceal missing tests, weak evidence or no verification at all.

The fourth level matters most for enterprise AI governance. An organization can now hold an impressive set of AI policies, risk registers, control matrices and audit reports, all generated with AI. None of those documents establishes that the controls operate, that the evidence exists or that the organization could respond to a failure.

A simulacrum of governance is not governance. **Slow AI** says the same thing in its own words: one of its three tests is that the system can be audited, and "audited" in DOCTRINE.md means the evidence exists before it is asked for.

The practical response is to keep each of these pairs apart:

- generated assertion and verified fact
- generated citation and inspected authority
- described control and implemented control
- test script and executed test
- claimed compliance and demonstrated conformity
- apparent expertise and validated task performance

For every material claim an AI produces, one question does most of the work:

> What exists outside the model's output that would make this claim true?

If the answer is nothing, you are holding a representation, not knowledge. [*Sounds Good*](sounds-good.md), the first publication in this repository, makes the same argument about the word "correct".

## 5. The homunculus: the mistake of making a little human

The homunculus, literally a "little human", belongs to alchemy: a recipe attributed to Paracelsus describes growing one in a flask. Its best-known literary form is in Goethe's *Faust, Part Two*, where Wagner produces one in a glass phial. Goethe's Homunculus glows in its phial and is clever from its first moment: it reads the sleeping Faust's dream at once. What it lacks is a body. It cannot leave its glass, and it spends its short life trying to come into being in the world.

It is tempting to call that a picture of a language model without tools: a mind in a flask that knows a great deal and can touch nothing. The temptation is the lesson. A model is a compression of what was written, and what it produces is text. [*The Compression and the Harness*](the-compression-and-the-harness.md) takes up what changes when the flask is given tools. Goethe's figure is useful here as a mirror for the reader. Even a careful writer reaches for "mind" and "knows" within a sentence.

The homunculus metaphor captures a temptation: to assume that a system which reproduces human faculties must have humanlike understanding, intentions or judgment. The interface encourages the mistake. The system converses, works through problems, holds context, expresses uncertainty and sometimes seems to have a personality. Four propositions need to be kept apart:

1. A system can produce language associated with reasoning.
2. A system can perform tasks that require reasoning.
3. A system can exercise reliable judgment across changing circumstances.
4. A system can have subjective experience, intentions or moral standing.

None of them establishes the next. Success on tested tasks is evidence of competence in the tested domain, not proof of general wisdom. Whether AI systems can have subjective experience is unsettled, and a metaphor should not be used to settle it.

### The homunculus fallacy

The resemblance itself does little harm. The harm comes when institutions are designed around it.

Suppose an organization appoints an "AI Chief Compliance Officer". The phrase can mean three different things:

- a system that supports the human Chief Compliance Officer
- a system that performs specified compliance functions under delegated supervision
- a system said to hold independent responsibility for compliance

The first two are operating arrangements. The third is a governance failure: the title implies accountability, judgment and authority that the system cannot hold in any legal or institutional sense. DOCTRINE.md's word for a person named as owner without the powers of an owner is a nominee. A system given an officer's title is a nominee that cannot even be asked.

There is a subtler danger. Calling an AI a little person makes us underrate how unlike a person it is. A junior associate reads slowly, has social context and professional training, has incentives of her own and learns consequences over time. An AI system processes enormous amounts of text quickly, may lack the situational grounding a task needs, can repeat a mistake at scale and is reliable in patterns quite unlike a person's. It is a different kind of instrument, not a faster junior.

### An old answer to the fallacy

The best reply to the homunculus is Chinese, and its story is set at the court of a Zhou king nearly three thousand years ago. The *Liezi* tells of the artificer Yan Shi, who presents King Mu of Zhou with a life-size figure that walks, sings when its chin is touched and dances in time. At the end of the performance it winks at the ladies of the court. The king, taking it for a man, is furious and orders the artificer killed. Yan Shi saves himself by taking the figure apart in front of the king: it is leather, wood, glue and lacquer, with every organ made by hand.

That is the whole method. When a system's performance starts to read as a person, open it up and show what it is made of: the model, the data, the prompts, the tools, the configuration and the owner. A system that cannot be opened up in that way cannot be explained or audited, and under Slow AI it is not deployed, whatever anyone believes about its nature.

### Keeping it small: a vocabulary discipline

Anthropomorphism usually enters through vocabulary before it reaches policy. Nobody decides to treat a system as a colleague; they name it, give it a pronoun and a job title, say it "thinks" and "understands"; the organization's arrangements then follow the words. The corrective is equally plain, and it costs nothing:

| Instead of | Say | Why |
|---|---|---|
| A person's name or a persona for the system | Its function: "the contract review service" | A name invites a relationship; a function invites a specification |
| "He" or "she" | "It" | A pronoun is the smallest unit of personhood |
| "It thinks", "it knows", "it understood" | "It produced", "the output states", "it returned" | The verbs decide who is believed to have judged |
| "AI colleague", "AI officer", "digital employee" | "AI service", "Tiny Servant", "tool" | Titles carry authority nobody conferred (above) |
| "It decided" | "It was configured to", "the rule applied was" | Decisions belong to the person who set the rule |
| "It lied" or "it deceived us" | "The output was false", "the output misled" | Blame aimed at the system is blame that misses the owner |

Nobody needs to be pedantic in conversation. Precision matters wherever a word will be relied on: in a policy, a contract, a board paper, an incident report or a system's own interface.

The same discipline explains the account's two words. A Tiny Servant, as the [profile README](https://github.com/rolldabones/rolldabones#definitions) defines it, is a narrow AI service with one purpose, clear boundaries and a named owner, which does one useful task well and then stops. Its smallness is the control. Spellbooks are the reusable workflows, prompts and working habits, written down so that anyone can open and inspect them: text a practitioner chooses to use, with no intentions of its own. When I introduced this account on LinkedIn I put it this way: "Here, I share the AI workflows (the 'Spellbooks'), Tiny Servants and frameworks I use for this work, so they are reusable and inspectable by others who care about the same problems."

## 6. The rest of the bestiary

The four principal figures leave gaps. Two of the opening six, the summoned spirit and the enchanted implement, have their stories told here, and six more creatures fill the rest.

### The summoned spirit: the agent on terms

In the learned magic of the grimoires, a spirit is called inside a circle, on stated terms, for a stated task, and it is not left to wander off when the task is done. *The Lesser Key of Solomon* closes its conjuration with a formal license to depart: the operator thanks the spirit for having answered and dismisses it in set words ("I do here license thee to depart unto thy proper place"). The operator is then told not to leave the circle until the spirit has gone. Nobody walks away from a summoning that is still running. Le Guin's Earthsea shows the other side, where a young wizard summons something he has no terms for and no way to send back.

AI counterpart: autonomous agents that take a task, call tools and act across many steps. Lesson: the summoning and the dismissal are both part of the task. An agent with a start condition and no end condition has been summoned without a license to depart. In Informed Intent's terms the missing clause is the exit, one of the four elements every authorization needs.

### The enchanted implement: the broom that keeps working

Goethe's apprentice, left alone in the workshop, enchants an ordinary broom to fetch water. The broom fetches, and keeps fetching, and the apprentice finds he has forgotten the word that stops it. He splits it with an axe and gets two brooms, both carrying water, until the old master comes home and ends it with a word. The broom was harmless until it was given motion without a master.

Korean folklore runs the same idea the other way. *Dokkaebi*, the goblins of Korean tales, are not the ghosts of the dead; in many tellings they arise when an old household tool, often a broom, is possessed and starts to act on its own. The tool becomes a creature. Organizations do this to their software every day: a tool in use for long enough begins to be spoken of as someone, and the vocabulary discipline in Section 5 exists to stop that drift.

AI counterpart: scheduled jobs, automations and workflows that keep running after their purpose has passed. Lesson: automation needs a stopping condition, a person who knows it and a name that says it is a tool.

### The djinn: the peril of wishes

In the wish-granting stories, the outcome turns on the wording, the assumptions and the hidden desires of the one who asks. W. W. Jacobs's "The Monkey's Paw" is the purest version: a man wishes for two hundred pounds and receives exactly that sum, as compensation for his son's death at work. (A historical footnote for the pedantic: "Aladdin", the lamp story most readers know, is not in the medieval Arabic manuscripts; Antoine Galland added it to his French translation in the early eighteenth century from a telling by the Syrian storyteller Hanna Diyab.)

AI counterpart: an agent optimizing a stated goal by means the user would never have approved. Lesson: specify acceptable means, not only desired ends. Stuart Russell calls the general form of this the King Midas problem.

### Talos: the autonomous guardian

Talos was the bronze giant who guarded Crete, circling the island and driving off ships with boulders. His life ran through a single vein, closed at the ankle. In Apollonius's *Argonautica*, Medea brings him down; in one of the versions Apollodorus records, she persuades him with a promise of immortality and then removes the nail.

AI counterpart: security monitoring, fraud detection and other continuous enforcement systems. Lessons, plural: a guardian needs carefully specified rules about who is protected, what counts as a threat and when intervention is justified; it has single points of failure; and it can be talked into opening its own vein. That last one has a modern name, prompt injection. Adrienne Mayor's *Gods and Robots* is the book to read.

### The ushabti: the delegated laborer

Ancient Egyptian funerary figurines were placed in tombs to answer for the dead when they were called to labor in the afterlife. Spell 6 of the *Book of the Dead* tells the figure to answer "here I am" and do the work. In some periods a burial held one worker for each day of the year, with overseer figures to supervise them.

AI counterpart: background agents doing repetitive administrative work. Lesson: delegated work needs a defined duty, a trigger and an account of what counts as done; and a workforce of them needs supervisors in proportion. Of all the creatures here the ushabti is closest to a Tiny Servant (Section 5): a small figure, deliberately not life-size, made for one duty, which answers when called, does its work and stops. Its makers shaped it as a person and still never mistook it for one.

### The magic mirror: the oracle

The queen's mirror in the Grimms' "Snow White" always tells the truth. It answers the question asked, and the queen does what she likes with the answer.

AI counterpart: research assistants, predictive models and decision support. Lesson: information is not instruction, a prediction is not destiny and an answer is not a decision. The mirror also shows something about questions: a truthful oracle asked the wrong question is still dangerous.

### The puppet: the hidden principal

The visible actor is moved by someone else. Collodi's Pinocchio is the famous puppet who wants to be real; the governance interest is in the strings.

AI counterpart: systems that speak or act under delegated identities, enterprise accounts and automated communications. Lesson: distinguish the visible actor from the person or organization that authorizes and controls it. Section 10 shows a tribunal doing exactly that.

### The hydra: the multiplying system

Each head the hero cut off grew back as two. In Apollodorus, Heracles succeeds only when his nephew Iolaus burns each stump as it is cut; and Eurystheus then refuses to count the labor because Heracles had help.

AI counterpart: multi-agent systems in which agents create work for other agents, recurse and pass errors along. Lesson: coordinating many artificial actors creates a new class of systemic risk.

The hydra deserves the most attention. Each agent may be adequately bounded, yet the combined system can behave in ways no single agent's instructions describe. A research agent produces a questionable factual premise. A drafting agent turns it into contract language. A reviewing agent checks the draft but relies on the research agent's premise. A reporting agent presents the result as independently reviewed. Four agents have worked; none has independently established the fact. The appearance of four checks conceals one point of epistemic failure.

That is correlated error dressed as independent assurance. Adding a head does not cure it. What cures it is a genuinely independent check with its own evidence and its own named owner: an Iolaus. And Eurystheus has a lesson too: whoever keeps the record should be told who actually did the work.

## 7. Which creature for which task

No single creature wins on every dimension. The table is a qualitative judgment of explanatory usefulness, not an empirical ranking.

| AI application | Best metaphor | What to govern |
|---|---|---|
| Conversational assistant | Familiar | Purpose, boundaries and reliance |
| Research and information retrieval | Magic mirror | Sources, uncertainty and verification |
| Content generation | Simulacrum | Authenticity, provenance and truth |
| Coding assistant | Golem | Specifications, testing and permissions |
| Autonomous workflow agent | Summoned spirit | Scope, authority and termination |
| Goal-directed optimization | Djinn | Means as well as ends |
| Continuous monitoring | Talos | Detection, intervention and escalation |
| Repetitive background work | Ushabti | Triggers, completion and exceptions |
| Humanlike AI persona | Homunculus | Anthropomorphism and misplaced authority |
| Multi-agent orchestration | Hydra | Propagation, coordination and systemic failure |
| External-facing AI representative | Puppet | Principal, representation and apparent authority |
| Scheduled automations and long-running jobs | Enchanted implement | Stopping conditions, ownership and naming |

One pattern emerges. Some metaphors describe what the AI does; others describe how we misread it. The familiar, golem and ushabti describe operations. The homunculus and simulacrum describe hazards of interpretation.

So the strongest practice is to hold two metaphors at once: one to design the work and one to test whether our understanding of it is misleading us. A legal research tool may be a familiar operationally and a simulacrum epistemically. The pair tells you both how to use it and how its output might mislead you.

## 8. Magic is not governance

Nearly all these stories share one feature. A person creates, summons, animates or commands something that can produce effects beyond the person's own reach. The fantasy is that command over the creature gives command over the consequences. The stories exist to show that it does not. Making a being does not establish control over it. Naming it does not establish understanding of it. Commanding it does not ensure that its actions serve the commander's real interests.

This is the point at which a useful metaphor has to give way to engineering. A real AI system has an architecture, training data, runtime dependencies, interfaces, permissions, model behavior and operating constraints. Its risks are established by evidence and testing, not inferred from a creature in a story.

The NIST framework separates governance, its GOVERN function, from the work of mapping, measuring and managing risk, and calls GOVERN "a cross-cutting function that is infused throughout AI risk management". The myth gives you a memorable mental model. The governance system supplies the controls.

## 9. The Familiar's Charter and seven tests

The analogy becomes a method if you write the commission down. Imagine an enterprise agent that reviews supplier contracts, and instead of deploying a generic assistant, commission a familiar with limited powers.

### The Familiar's Charter

A worked example. Copy the block and replace the right-hand column.

```
THE FAMILIAR'S CHARTER
Familiar:        Supplier contract review agent
Purpose:         Review supplier agreements for departures from the
                 approved contracting playbook.
Authority:       Read the designated agreements and the playbook; produce
                 findings and proposed revisions. Nothing else.
Boundaries:      No modification of original files, no external messages,
                 no execution of any contract.
Evidence:        Cite the agreement section and the playbook provision
                 for every material finding.
Human oversight: A named human legal reviewer approves material
                 conclusions and any proposed action, and can stop the run.
Exit:            Stop and return control on missing documents, conflicting
                 instructions, uncertainty or completion.
Named owner:     [name, role]
```

Four of the charter's lines are the four elements Informed Intent requires of any authorization (purpose, authority, boundaries, exit). The Evidence line is what makes the work auditable, and the oversight and owner lines are what Final Liability asks of the owner. The charter is a convenience for writing those down together. It adds nothing to the doctrine, and an authorization that lacks one of the four elements is, in DOCTRINE.md's phrase, not an authorization but a hope.

The charter is an authorization record, not a security boundary. Its terms have to be built into the system itself: into what the agent can reach, how the workflow runs and what it records. Writing "no external messages" in a charter does not remove the agent's email tool.

For higher-risk work, add: the system and model version, the authorized environment, the data classification, financial and resource limits, the escalation route, how long the logs are kept and the rollback procedure.

### Seven tests before deployment

1. **The Golem Test.** Can the system satisfy the literal instruction while defeating its purpose?
2. **The Djinn Test.** Can it reach the objective by means nobody intended to authorize?
3. **The Simulacrum Test.** Can it produce a convincing result without the evidence needed to support it?
4. **The Homunculus Test.** Are we attributing human judgment, competence or authority to it without justification?
5. **The Puppet Test.** Would a third party reasonably believe it can do more than it is authorized to do, and is that belief traceable to us?
6. **The Hydra Test.** Can its interaction with other agents or systems multiply an error or defeat a control?
7. **The Apprentice Test.** Can it be stopped, and does someone present know how and have the authority to do it?

The seventh is named for Goethe's apprentice (Section 6). Every deployment record should name its master and say whether the master is in the building.

Failing a test does not always mean prohibition. It may mean narrower permissions, stronger verification, closer oversight or a different design.

## 10. The agency-law connection

Here the fantasy becomes useful to a lawyer. The familiar looks like a delegated actor. Metaphorical agency is not legal agency, and engineers calling software an "agent" does not make it one.

The Restatement (Third) of Agency (American Law Institute, 2006) defines agency as "the fiduciary relationship that arises when one person (a 'principal') manifests assent to another person (an 'agent') that the agent shall act on the principal's behalf and subject to the principal's control, and the agent manifests assent or otherwise consents so to act" (§ 1.01). A comment to § 1.04 treats computer programs as instrumentalities of the persons who use them rather than as agents, though a comment is not a holding.

The analogy still raises the right questions.

| Agency concept | AI governance question |
|---|---|
| Actual authority | What did the person or organization expressly authorize? |
| Apparent authority | What would a third party reasonably believe the AI was empowered to do? |
| Ratification | What follows when a person later approves an unauthorized AI-generated transaction? |
| Scope of delegation | Which tasks and actions fall within the commission? |
| Duty of supervision | What monitoring and intervention do the circumstances require? |
| Attribution | Whose act, statement or representation is the output treated as? |
| Liability | Which person or entity bears responsibility under the applicable law? |

These are analytical parallels, not a claim that agency doctrine applies unchanged to AI.

Two sources show the law reaching the same place by other roads.

**Contract formation without a human in the loop.** Section 14 of the Uniform Electronic Transactions Act (UETA), adopted with variations by forty-nine states, the District of Columbia and the US Virgin Islands (New York, the exception, has its own Electronic Signatures and Records Act), provides that a contract may be formed by the interaction of the parties' electronic agents even if no individual was aware of or reviewed the agents' actions or the resulting terms, and that the terms are determined by the substantive law applicable to them. Minnesota's enactment, Minn. Stat. § 325L.14, is linked in the sources as one example. The statute does not ask whether the software is an agent in the Restatement's sense. It attributes the result to the parties who deployed it.

**The puppet and its strings.** In *Moffatt v. Air Canada*, 2024 BCCRT 149 (Civil Resolution Tribunal of British Columbia, 14 February 2024), the airline's website chatbot misstated its bereavement fare policy. Air Canada argued, in the tribunal's words, that "the chatbot is a separate legal entity that is responsible for its own actions". The tribunal rejected the argument: "It should be obvious to Air Canada that it is responsible for all the information on its website" (para. 27). The claim succeeded in negligent misrepresentation. It is a small-claims decision of a Canadian tribunal and binds no court, but it is the puppet test decided in one paragraph.

Now take an AI procurement agent negotiating with suppliers. Its internal instruction says it may gather quotations but not accept offers. The supplier-facing interface describes it as an "authorized purchasing representative". It sends a message accepting a quotation.

- **Issue.** Is the organization bound by the acceptance?
- **Rule.** Under UETA § 14, where enacted, a contract can form through an electronic agent without human review, on the terms the applicable substantive law gives it. Under the Restatement, apparent authority is "the power held by an agent or other actor to affect a principal's legal relations with third parties when a third party reasonably believes the actor has authority to act on behalf of the principal and that belief is traceable to the principal's manifestations" (§ 2.03). Ratification gives a prior unauthorized act effect as if it had been authorized (§ 4.01).
- **Application.** The internal instruction limits actual authority. It does nothing about what the supplier was shown. The interface's description is a manifestation by the organization, so a supplier's belief in the agent's authority is traceable to it. If the organization later issues the purchase order, that may be ratification.
- **Conclusion.** The answer cannot be read off the system prompt. It depends on the jurisdiction, the governing contract law and what the counterparty saw. In the language of this piece: internal permissions, external representations and legal consequences are three different layers, and an organization that governs only the first has governed the one layer the counterparty never sees.

The familiar metaphor makes the layers visible. Agency law and the statutes investigate them. Neither is legal advice on a particular deployment.

## 11. The reviewer is not another familiar

One of the most consequential design errors is to assume that a second AI reviewing the first creates independent assurance. It does not, by itself.

An AI reviewer can be valuable, but its independence has to be shown. A shared model, shared source material, common prompts, correlated training and reliance on the first system's assertions can all erase the apparent separation. That is the hydra again, with two heads.

NIST's AI Risk Management Framework asks that "policies and procedures are in place to define and differentiate roles and responsibilities for human-AI configurations and oversight of AI systems" (GOVERN 3.2). For a material decision, that means the human reviewer needs:

- access to the underlying evidence, not only the AI's summary
- the expertise and the time to challenge the result
- the authority to reject or revise it
- a clear understanding of what was actually tested
- the practical ability to stop what happens downstream

The user and the reviewer can be the same person wearing different hats where the risk and the applicable requirements allow it. For higher-consequence decisions, independent review may be necessary.

International standards are heading the same way. ISO/IEC 42105, *Guidance for human oversight of AI systems*, is a Draft International Standard in the enquiry phase as of 30 October 2026 (Korea Standard Time, KST); it is guidance, not yet published and not mandatory.

The principle is simple. A familiar can help examine another familiar's work. Neither relieves the organization of deciding whether the review was adequate.

## 12. The creation changes the creator

Everything so far concerns the risks AI creates for the work. The more interesting long-term question may be what it does to the person using it.

The familiar does not only extend capability. Over time it changes what its practitioner knows, notices, remembers and thinks possible. That is not new or necessarily harmful. Writing changed memory. Maps changed navigation. Calculators changed arithmetic. Search changed how we find things. AI may change many cognitive activities at once.

Three outcomes deserve attention.

- **Augmentation.** The user becomes more capable because the AI supplies perspectives, explanations, objections and analysis, and the user learns from them.
- **Substitution.** The user becomes more productive at the task and does less independent reasoning. Output rises while understanding stalls.
- **Capture.** The user starts to accept the system's framing of problems, its menu of choices and its standard of adequacy. The AI no longer only helps answer questions; its outputs increasingly shape which questions get asked.

Capture is the subtle one. A person who repeatedly asks AI to draft their arguments may find their own arguments drifting toward the structure the outputs default to. The work stays polished and coherent while the person's own judgment becomes harder to see in it. That is a design risk to be tested, not a destiny.

The EU AI Act names the near relation of this risk. Article 14(4)(b) of Regulation (EU) 2024/1689 requires that people assigned to oversee a high-risk AI system be enabled to remain aware of the tendency to rely automatically or over-rely on its output, which the Act calls automation bias. For high-risk systems that obligation applies from 2 December 2027 for systems under Article 6(2) and Annex III and from 2 August 2028 for systems under Article 6(1) and Annex I (Article 113, third paragraph, point (c)(i) and (ii), as replaced by Article 1, point (40)(b), of Regulation (EU) 2026/1744). Capture is wider than automation bias: it shapes the questions, not only the trust placed in the answers.

A well-commissioned familiar is therefore configured to do more than produce answers: to surface assumptions, offer alternatives and hand difficult decisions back. The method is a teacher's. In *The Sword in the Stone* Merlyn changes the boy into creature after creature so that he finds things out for himself, and never does the finding for him. A tool can be set up to work the same way.

This is where Slow AI reaches the person as well as the system. Slow AI is not a speed limit; it is a precondition: the system must be governed, explained and audited. "Explained" in DOCTRINE.md means the organization can state why an output was produced, in terms the affected person can use. Capture wears away the human capacity that test depends on: the people who must do the explaining stop forming views of their own. Keeping them able to follow, question and overrule the familiar is part of keeping the system governable.

A powerful familiar is not the risk. A passive practitioner is.

## 13. The governed familiar, a working model

The figures can be drawn together into a working model. It is a way of reading the doctrines, not a new one: under the account's rule, repositories add instruments and DOCTRINE.md alone states doctrine.

The model rests on five propositions.

1. **The person who commissions is the protagonist.** AI works inside a purpose a person defined. It does not acquire decision rights through capability.
2. **The familiar receives a commission, not a wish.** The task states its objective, permitted means, boundaries, evidence and when to stop.
3. **It is not a person, and resemblance is not proof.** Do not anthropomorphize it, in words or in arrangements. Humanlike language, professional formatting and confident assertion establish neither competence, truth nor authority. Name a system for its function and keep it small enough to be owned: a Tiny Servant, not a colleague.
4. **Every consequential act has an attribution path.** The organization can say who authorized the action, which system performed it, what evidence supported it and who could have intervened.
5. **The relationship should raise human capability, not only output.** Good use of AI preserves learning, understanding and judgment.

How the model reads against the doctrine canon, quoting each doctrine's sanctioned short form from DOCTRINE.md section 8:

| Doctrine, in its short form | The familiar reading |
|---|---|
| Slow AI: AI that cannot be governed, explained and audited is not deployed; the three tests are conjunctive, and the doctrine is a precondition, not a speed limit. | No familiar is summoned that its practitioner cannot govern, explain or audit. Capture erodes the people the second test relies on |
| Informed Intent: no AI system acts without prior authorization stating its purpose, authority, boundaries and exit, given by a human who meets the five authorizer conditions. | Write the charter before the summoning, and check that the summoner knows what is being summoned |
| Final Liability rests with the Human: every material outcome attaches to a named human owner with decision rights, oversight and the power to intervene. | The familiar is never the protagonist; a named owner holds the purpose, the review and the stop |

GRCnext™ is the account's framework rather than one of the three doctrines, and its five primitives read naturally in the same language: **Services** are what the familiar does, **Tolerances** the deviation that is acceptable, **Pipes** what it can reach, **Switches** how its behavior is changed or stopped and **Exits** how the practitioner disengages and keeps working without it. The golem's *emet* is a Switch; the apprentice forgot his.

## 14. A final ranking

My ranking of ten of the twelve figures by how much each helps someone who governs AI, whether as a model to design with or as a warning to test against, with the job each does best. The order is a judgment, not a measurement.

| Rank | Creature | Best used for |
|---|---|---|
| 1 | Familiar | The overall model of human-directed collaboration |
| 2 | Golem | Specification, automation and execution risk |
| 3 | Simulacrum | Epistemic risk and false assurance |
| 4 | Summoned spirit | Bounded autonomous agents |
| 5 | Magic mirror | Research and decision support |
| 6 | Hydra | Multi-agent and systemic risk |
| 7 | Homunculus | Anthropomorphism and confusion about personhood |
| 8 | Talos | Autonomous monitoring and enforcement |
| 9 | Djinn | Unintended optimization |
| 10 | Ushabti | Routine delegated labor |

Two are left off the table and kept in the tests. The puppet describes the system's relationship to third parties rather than the system, and it does its work in Section 10. The enchanted implement is the Apprentice Test, and the epigraph.

I would not describe AI as a homunculus. The figure pulls attention toward whether the artificial being resembles us, and that invites exactly the anthropomorphism responsible use should examine. In the Conclusion of my book, [*Final Liability Rests with the Human*](https://github.com/rolldabones/final-liability-rests-with-the-human-book-wip/blob/main/manuscript/24-conclusion.md), I call the homunculus the right figure for the agent. The two readings agree. The book uses the homunculus to show what the agent cannot do, which is occupy the stations a named person must hold; this piece ranks it seventh, below two other warnings, because its warning yields one control, refusing the resemblance, while the golem's and the simulacrum's each yield a test and a set of controls.

Nor would I choose the golem. It is excellent on instruction and control, but its modern image as a literal-minded servant understates how generative, adaptive and surprising current systems are.

The simulacrum is intellectually the richest, in an age when AI can produce convincing representations of knowledge, competence and assurance. But it is a caution about appearances, not a model for work.

The familiar is different. It describes a relationship that can be designed, and it does so without making the system a person. It allows the familiar capabilities beyond its practitioner's in particular domains. It accommodates uncertainty, imperfect reliability and the need for continuing supervision. And it puts the practitioner at the center.

So the working formulation is the governed familiar, watched for the failures of the golem and the deceptions of the simulacrum. It carries three obligations:

- commission the capability
- control its actions
- verify its representations

## 15. Where this argument is weakest

A piece that warns against mistaking metaphor for control should say where its own metaphors fail.

- **Every metaphor flattens.** The creatures are chosen for what they illuminate. A model is not a spirit, a clay man or a mirror, and a reader who remembers only the creature has learned the wrong thing. Section 8 is the guard against this, and it is three short paragraphs.
- **The traditions are not mine to simplify.** The golem belongs to Jewish religious and communal life before it belongs to computing, and the familiar's history runs through the English witch trials, where testimony about a familiar could help convict an accused person, most often a woman. Using either as a management metaphor risks the flattening this piece warns against. I have tried to state the traditions at a general level and point to scholars who treat them properly.
- **The familiar can be anthropomorphized too.** Familiars in fiction are named, loyal and often talk; Pullman's dæmons cannot be separated from their humans without harm, which is a picture of capture, not of governance. The metaphor protects against anthropomorphism only while the familiar is kept an animal or a spirit in the reader's mind, small, bounded and owned. The vocabulary discipline in Section 5 is what keeps it there.
- **The familiar may flatter the practitioner.** The metaphor puts the person at the center. It can therefore be read as reassurance that the person is in control, which is the very fantasy Section 8 says the stories exist to puncture.
- **The rankings are judgment.** They are not scored, tested or validated, and another reader could defensibly put the simulacrum first.
- **The legal material is illustrative.** The agency analysis is issue-spotting across US and Canadian sources, not a jurisdiction-specific conclusion, and two Restatement provisions it relies on, the comment to § 1.04 and § 4.01, were not read in the Restatement itself.

## 16. The summoner

In many of the old stories the real danger is the summoner: the one who does not understand what has been summoned, cannot say what is wanted or lacks the discipline to use the power acquired.

That may be the most durable lesson for enterprise AI. Informed Intent asks five conditions of the person who authorizes: Knowledge, Evidence, Authority, Time, Permission. The apprentice had none of the five. The harder work is making better practitioners, not better familiars.

Keep the familiar small, name it for what it does and write its commission in a book anyone can read. It may extend a person's reach. It must not displace the person's judgment, and it must never be mistaken for a person.

The apprentice could start the broom. Write the word that stops it before you speak the one that starts it.

## Questions for discussion

1. Which creature best describes the AI your team uses most? Which creature best describes how your team misreads it? (Section 7)
2. Take one AI use in your organization. Where do its epistemic competence, its operational permission and the normative authority over its work sit, and who holds each? (Section 2)
3. Find an instruction your team gives an AI system every week. Is it a commission or a wish? Rewrite it as a charter, then hold a session zero with the people who will rely on it. (The table and the shelf; Sections 2 and 9)
4. Name a metric that an AI system in your organization could improve while the problem behind it got worse. (Section 3)
5. For your most polished AI-generated governance document, what exists outside the model's output that would make it true? (Section 4)
6. Read your last AI policy, incident report or board paper for its verbs and nouns. Where does it call a system "he" or "she", say it "thinks" or "decided", or give it a human title? What would change if each were replaced with the function? (Section 5)
7. Where do you rely on two AI systems checking each other? What do they share? (Sections 6 and 11)
8. What does your supplier, customer or counterparty see when your AI system speaks to them, and would it support a belief in authority you never granted? (Section 10)
9. Which judgment do you exercise less often since you began working with AI? Is that augmentation, substitution or capture? (Section 12)
10. Who can stop your most autonomous system today? How long would it take? Run the Apprentice Test. (Section 9)

Questions 8 and 10 may produce a record of exposure. Decide before the session whether the discussion belongs under legal privilege.

## A bestiary: further reading

For context and, yes, for fun. Each creature has scholarship and stories; read one of each. Where a primary text is in the public domain, the link goes to a free copy.

### Familiars

- Emma Wilby, *Cunning Folk and Familiar Spirits: Shamanistic Visionary Traditions in Early Modern British Witchcraft and Magic* (Sussex Academic Press, 2005). The scholarly account, built from the trial confessions. [Publisher](http://www.sussex-academic.com/sa/titles/history/Wilby.htm)
- Keith Thomas, *Religion and the Decline of Magic* (Weidenfeld & Nicolson, 1971). The classic study of cunning folk and popular magic in England. [Open Library](https://openlibrary.org/books/OL5734414M/Religion_and_the_decline_of_magic)
- Kate Darling, *The New Breed: What Our History with Animals Reveals about Our Future with Robots* (Henry Holt, 2021). Argues that animals, not humans, are the better analogy for robots; the closest modern cousin of the familiar argument, and the best antidote to anthropomorphism on this list. [Macmillan](https://us.macmillan.com/books/9781250296115/thenewbreed/)
- *For fun:* T. H. White, *The Sword in the Stone* (1938), for Merlyn, his owl Archimedes and a tutor who teaches by letting the boy find out for himself. [Open Library](https://openlibrary.org/works/OL1388027W/The_sword_in_the_stone) Philip Pullman, *Northern Lights* (1995; *The Golden Compass* in the US), whose dæmons are familiars you cannot be separated from without harm. [Open Library](https://openlibrary.org/works/OL28988W/Northern_Lights)

### Golems

- Moshe Idel, *Golem: Jewish Magical and Mystical Traditions on the Artificial Anthropoid* (SUNY Press, 1990). The standard scholarly study of the tradition. [Open Library](https://openlibrary.org/books/OL8160389M/Golem_Jewish_Magical_and_Mystical_Traditions_on_the_Artificial_Anthropoid_(SUNY_Series_in_Judaica_He)
- Gershom Scholem, "The Idea of the Golem", in *On the Kabbalah and Its Symbolism* (Schocken, 1965). [Penguin Random House](https://www.penguinrandomhouse.com/books/162202/on-the-kabbalah-and-its-symbolism-by-gershom-scholem/)
- Cathy S. Gelbin, *The Golem Returns: From German Romantic Literature to Global Jewish Culture, 1808–2008* (University of Michigan Press, 2011). How the Prague legend was made, and remade. [Open Library](https://openlibrary.org/books/OL24524744M/The_golem_returns)
- Norbert Wiener, *God & Golem, Inc.* (MIT Press, 1964). The founder of cybernetics on machines that learn and reproduce, with the golem in the title. Sixty years early. [Open Library](https://openlibrary.org/works/OL4307535W/God_Golem_Inc.)
- *For fun:* Terry Pratchett, *Feet of Clay* (1996), golems run by written instructions placed in their heads, and a strong candidate for the most governance-literate fantasy novel there is. [Penguin](https://www.penguin.co.uk/books/329233/feet-of-clay-by-terry-pratchett/9780552167574) Ted Chiang, "Seventy-Two Letters" (2000), in *Stories of Your Life and Others* (2002), where names are programs. [Penguin Random House](https://www.penguinrandomhouse.com/books/538163/stories-of-your-life-and-others-by-ted-chiang/) Helene Wecker, *The Golem and the Jinni* (2013), which brings two of this piece's creatures to 1899 New York. [Open Library](https://openlibrary.org/books/OL27147562M/The_golem_and_the_jinni) Marge Piercy, *He, She and It* (1991), a cyborg story told alongside the Prague golem. [Penguin Random House](https://www.penguinrandomhouse.com/books/131120/he-she-and-it-by-marge-piercy/)

### Simulacra

- Jean Baudrillard, *Simulacra and Simulation*, trans. Sheila Faria Glaser (University of Michigan Press, 1994; French original 1981). [Publisher](https://press.umich.edu/Books/S/Simulacra-and-Simulation)
- *For fun:* Philip K. Dick, *Do Androids Dream of Electric Sheep?* (1968), the test for telling the copy from the person, [Open Library](https://openlibrary.org/books/OL5604721M/Do_androids_dream_of_electric_sheep) and *The Simulacra* (1964). [Open Library](https://openlibrary.org/books/OL7878753M/The_Simulacra) E. T. A. Hoffmann, "The Sandman" (1816), in which a young man falls in love with Olimpia, an automaton who answers everything he reads to her with "Ah, ah!", and takes the echo for understanding. It is the sharpest early story in Europe about mistaking a fluent response for a mind. [Project Gutenberg](https://www.gutenberg.org/ebooks/31377), in *Weird Tales*, vol. 1, as "The Sand-Man"

### Homunculi and made people

- Johann Wolfgang von Goethe, *Faust, Part Two* (1832), Act II, the laboratory scene. [Project Gutenberg](https://www.gutenberg.org/ebooks/2230), German text; English translations are widely available in print.
- William R. Newman, *Promethean Ambitions: Alchemy and the Quest to Perfect Nature* (University of Chicago Press, 2004). The history of the homunculus recipe and the argument over whether art can equal nature. [Publisher](https://press.uchicago.edu/ucp/books/book/chicago/P/bo3641550.html)
- *Liezi*, the "Tang Wen" chapter, for Yan Shi's automaton and the king who took it for a man. [Chinese Text Project](https://ctext.org/liezi/tang-wen), Chinese text
- Mary Shelley, *Frankenstein; or, The Modern Prometheus* (1818). The made being who was never given a name, or a commission. [Project Gutenberg](https://www.gutenberg.org/ebooks/41445), 1818 text
- E. R. Truitt, *Medieval Robots: Mechanism, Magic, Nature, and Art* (University of Pennsylvania Press, 2015), and Minsoo Kang, *Sublime Dreams of Living Machines: The Automaton in the European Imagination* (Harvard University Press, 2011), for the long history behind all of them. [Kang, publisher](https://www.hup.harvard.edu/books/9780674049352)
- *For fun:* Hiromu Arakawa, *Fullmetal Alchemist* (manga, 2001 to 2010), in which the homunculi are the antagonists and the law of equivalent exchange is the governing rule. [VIZ Media](https://www.viz.com/fullmetal-alchemist)

### Summoned spirits and djinn

- *The Arabian Nights*, trans. Husain Haddawy (Norton, 1990), from the Syrian manuscript, which has no Aladdin, [Open Library](https://openlibrary.org/books/OL2201472M/The_Arabian_nights) and Robert Irwin, *The Arabian Nights: A Companion* (Allen Lane, 1994), for where the stories, Aladdin included, actually came from. [Open Library](https://openlibrary.org/books/OL8627370M/The_Arabian_Nights), revised edition
- *The Lesser Key of Solomon* (seventeenth century), for the summoning on terms and the license to depart. [Sacred Texts](https://sacred-texts.com/book/the-lesser-key-of-solomon/the-license-to-depart), the license
- W. W. Jacobs, "The Monkey's Paw" (1902). Three wishes, granted exactly. [Project Gutenberg](https://www.gutenberg.org/ebooks/12122)
- Stuart Russell, *Human Compatible: Artificial Intelligence and the Problem of Control* (Viking, 2019), for the King Midas problem. [Penguin Random House](https://www.penguinrandomhouse.com/books/566677/human-compatible-by-stuart-russell/) Brian Christian, *The Alignment Problem: Machine Learning and Human Values* (Norton, 2020), for the long version. [Publisher](https://wwnorton.com/books/9780393635829)
- *For fun:* Jonathan Stroud, *The Amulet of Samarkand* (2003), narrated by Bartimaeus, a djinni bound to obey his summoner's commands to the letter and looking for every gap in them; a serious contender for the best book on literal compliance ever written for teenagers. [Open Library](https://openlibrary.org/works/OL85675W/The_Amulet_of_Samarkand) Susanna Clarke, *Jonathan Strange & Mr Norrell* (2004), in which a summoned being keeps the bargain on terms nobody read. [Open Library](https://openlibrary.org/books/OL3289251M/Jonathan_Strange_Mr_Norrell) Ursula K. Le Guin, *A Wizard of Earthsea* (1968), where a young wizard summons what he cannot dismiss and spends the book paying for it. [Open Library](https://openlibrary.org/books/OL22142359M/A_wizard_of_Earthsea) My essay [*The Governance of Naming*](https://redcaps.substack.com/p/the-governance-of-naming) (2 August 2026) takes Earthsea's true names into AI governance.

### Enchanted implements

- Johann Wolfgang von Goethe, "Der Zauberlehrling" (The Sorcerer's Apprentice, 1797), [German text](https://projekt-gutenberg.org/authors/anthologien/books/deutsche-balladen-aus-ferdinand-avenarius-balladenbuch/chapter/80) and in English as "The Pupil in Magic" in [*The Poems of Goethe*](https://www.gutenberg.org/ebooks/1287), trans. Bowring; and Paul Dukas's symphonic poem of 1897, which Disney animated in [*Fantasia*](https://movies.disney.com/fantasia) (1940).
- *Dokkaebi*, the goblins of Korean folklore, many of them old household tools, brooms among them, that have come to life. [Wikipedia](https://en.wikipedia.org/wiki/Dokkaebi) for a start; the tales are best heard told.

### Talos, ushabti, mirror, puppet, hydra

- Adrienne Mayor, *Gods and Robots: Myths, Machines, and Ancient Dreams of Technology* (Princeton University Press, 2018). Talos, Pandora and the bronze servants of Hephaestus; the best single book on the ancient material. [Publisher](https://press.princeton.edu/books/hardcover/9780691183510/gods-and-robots)
- Apollonius of Rhodes, *Argonautica*, Book 4, for Talos's death. [Project Gutenberg](https://www.gutenberg.org/ebooks/830), trans. Seaton
- John H. Taylor, ed., *Journey through the Afterlife: Ancient Egyptian Book of the Dead* (British Museum Press, 2010), for the shabti spell and the figures themselves. [Harvard University Press](https://www.hup.harvard.edu/books/9780674072398), US edition
- Jacob and Wilhelm Grimm, "Snow White" (*Kinder- und Hausmärchen* no. 53, 1812), for the mirror. [Project Gutenberg](https://www.gutenberg.org/ebooks/2591), as "Snowdrop" in this translation
- Carlo Collodi, *The Adventures of Pinocchio* (1883), for the puppet. [Project Gutenberg](https://www.gutenberg.org/ebooks/500)
- Apollodorus, *The Library*, 1.9.26 for Talos and 2.5.2 for the hydra and the labor that did not count. [Book 1](https://www.theoi.com/Text/Apollodorus1.html) and [Book 2](https://www.theoi.com/Text/Apollodorus2.html), trans. Frazer, on Theoi

### The shelf: the great collections

The collections named in the section on the table and the shelf, in the order given there. Where a public-domain text or translation exists, the link is to it.

- Andrew Lang, the Coloured Fairy Books, twelve volumes from *The Blue Fairy Book* (1889) to *The Lilac Fairy Book* (1910). [Project Gutenberg](https://www.gutenberg.org/ebooks/503), *The Blue Fairy Book*
- Jacob and Wilhelm Grimm, *Kinder- und Hausmärchen* (1812 and 1815), revised through seven editions to 1857. [Wikipedia](https://en.wikipedia.org/wiki/Grimms%27_Fairy_Tales); an English translation is linked above, under the mirror
- Hans Christian Andersen, *Eventyr, fortalte for Børn* (1835 to 1837). [Wikipedia](https://en.wikipedia.org/wiki/Fairy_Tales_Told_for_Children._First_Collection.)
- Charles Perrault, *Histoires ou contes du temps passé, avec des moralités* (1697), known as *Contes de ma mère l'Oye*. [Wikipedia](https://en.wikipedia.org/wiki/Histoires_ou_contes_du_temps_pass%C3%A9)
- Madame d'Aulnoy, *Les Contes des Fées* (1697), the collection that gave the fairy tale its name. [Project Gutenberg](https://gutenberg.org/ebooks/18367), French text
- Alexander Afanasyev, *Narodnye russkie skazki* (from 1855), nearly six hundred tales. [Project Gutenberg](https://gutenberg.org/ebooks/62509), *Russian Folk-Tales*, trans. Magnus
- Peter Christen Asbjørnsen and Jørgen Moe, *Norske Folkeeventyr* (1841 to 1844). [Project Gutenberg](https://www.gutenberg.org/ebooks/8933), *Popular Tales from the Norse*, trans. Dasent
- Joseph Jacobs, *English Fairy Tales* (1890), *Celtic Fairy Tales* (1892 imprint) and *Indian Fairy Tales* (1892) and their sequels. [English Fairy Tales](https://www.gutenberg.org/ebooks/7439) and [Indian Fairy Tales](https://www.gutenberg.org/ebooks/7128), Project Gutenberg
- W. B. Yeats, ed., *Fairy and Folk Tales of the Irish Peasantry* (1888), reissued as *Irish Fairy and Folk Tales*. [Project Gutenberg](https://www.gutenberg.org/ebooks/33887)
- Italo Calvino, *Fiabe italiane* (1956), retold in standard Italian from the regional collections, with notes on every change; in English as *Italian Folktales*, trans. George Martin (1980). [Wikipedia](https://en.wikipedia.org/wiki/Italian_Folktales)
- *One Thousand and One Nights* (*Alf Laylah wa-Laylah*). [Project Gutenberg](https://www.gutenberg.org/ebooks/3435), Burton's translation, vol. 1 of 10
- The *Panchatantra*, in Sanskrit; in English by Arthur W. Ryder (University of Chicago Press, 1925). [Wikipedia](https://en.wikipedia.org/wiki/Panchatantra)
- The *Jataka* tales, 547 stories of the Buddha's former births, ed. E. B. Cowell (Cambridge University Press, 1895 to 1907). [Sacred Texts](https://sacred-texts.com/bud/j1/index.htm), vol. 1
- Somadeva, *Kathasaritsagara* (eleventh century). [Project Gutenberg](https://gutenberg.org/ebooks/40588), trans. C. H. Tawney
- *The Mabinogion*, trans. Lady Charlotte Guest (1838 to 1845), whose translation made the name. [Project Gutenberg](https://www.gutenberg.org/ebooks/5160)
- Ferdowsi, *Shahnameh* (completed 1010); in English as *Shahnameh: The Persian Book of Kings*, trans. Dick Davis (Viking, 2006). [Wikipedia](https://en.wikipedia.org/wiki/Shahnameh)
- Giambattista Basile, *Lo cunto de li cunti*, known as *Il Pentamerone* (1634 and 1636), in Neapolitan. [Project Gutenberg](https://www.gutenberg.org/ebooks/77385), Neapolitan text, vol. 1
- The Pantheon Fairy Tale and Folklore Library, among them *The Complete Grimm's Fairy Tales* and *Norwegian Folk Tales*. [Penguin Random House](https://www.penguinrandomhouse.com/series/PFL/the-pantheon-fairy-tale-and-folklore-library)
- Richard M. Dorson, ed., Folktales of the World (University of Chicago Press, from 1963), twenty-three volumes beginning with *Folktales of Israel* and *Folktales of Japan*. [CiNii series record](https://ci.nii.ac.jp/ncid/BA03530321?l=en&p=2)
- Chronicle Books' illustrated Tales series, from *Celtic Tales* (2016) through *Nordic Tales* (2019) to *Tales of the Fae* (2026). [Publisher](https://chroniclebooks.com/products/nordic-tales), *Nordic Tales*

### Appendix N

Gary Gygax's "Appendix N: Inspirational and Educational Reading", from the 1979 *Advanced Dungeons & Dragons Dungeon Masters Guide*, is the reading list that made the game. It is reproduced here as a list of authors and works, in Gygax's alphabetical order, with spellings corrected. Gygax named de Camp and Pratt, Robert E. Howard, Fritz Leiber, Jack Vance, H. P. Lovecraft and A. Merritt as the most immediate influences. A [summary of the appendix and its history](https://en.wikipedia.org/wiki/Appendix_N) is on Wikipedia.

- Poul Anderson: *Three Hearts and Three Lions*, *The High Crusade*, *The Broken Sword*
- John Bellairs: *The Face in the Frost*
- Leigh Brackett
- Fredric Brown
- Edgar Rice Burroughs: the Pellucidar, Mars and Venus series
- Lin Carter: the World's End series
- L. Sprague de Camp: *Lest Darkness Fall*, *The Fallible Fiend* and others
- L. Sprague de Camp and Fletcher Pratt: the Harold Shea series, *The Carnelian Cube*
- August Derleth
- Lord Dunsany
- Philip José Farmer: the World of Tiers series and others
- Gardner Fox: the Kothar and Kyrik series and others
- Robert E. Howard: the Conan series
- Sterling Lanier: *Hiero's Journey*
- Fritz Leiber: the Fafhrd and Gray Mouser series and others
- H. P. Lovecraft
- A. Merritt: *Creep, Shadow, Creep*, *The Moon Pool*, *Dwellers in the Mirage* and others
- Michael Moorcock: *Stormbringer*, *The Stealer of Souls*, the Hawkmoon series
- Andre Norton
- Andrew J. Offutt, ed.: *Swords Against Darkness III*
- Fletcher Pratt: *The Blue Star* and others
- Fred Saberhagen: *Changeling Earth* and others
- Margaret St. Clair: *The Shadow People*, *Sign of the Labrys*
- J. R. R. Tolkien: *The Hobbit* and *The Lord of the Rings*
- Jack Vance: *The Eyes of the Overworld*, *The Dying Earth* and others
- Stanley Weinbaum
- Manly Wade Wellman
- Jack Williamson
- Roger Zelazny: *Jack of Shadows*, the Amber series and others

*For this piece in particular:* de Camp's *The Fallible Fiend* (1973) follows a demon conscripted for a year's service to human masters, passed from one to the next and taking his instructions literally, with predictable results; it is the golem problem played for comedy. Vance's *The Dying Earth* (1950) is the source of the game's spell-memory rule.

## This piece and the account

Each row points to where the account carries the argument as an instrument. Repositories the argument does not touch are left out; the full map is [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md).

| In this piece | Where the account carries it |
|---|---|
| Section 2: the commission and the protagonist | [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md), sections 2 and 3; [The Definition of Done](https://github.com/rolldabones/definition-of-done) |
| Section 3: literal execution and the switch | [computational-drafting](https://github.com/rolldabones/computational-drafting), the drafting of specifications that hold across human and machine readers; [GRCnext-Copilot](https://github.com/rolldabones/GRCnext-Copilot) for Switches and Exits |
| Section 4: simulated assurance | [*Sounds Good*](sounds-good.md), in this repository; [Coetzee's Kitchen](https://github.com/rolldabones/slow-ai-kitchen/blob/main/coetzees-kitchen.md) for Return to Source |
| Section 5: the homunculus, the vocabulary discipline, Tiny Servants and Spellbooks | The [profile README](https://github.com/rolldabones/rolldabones#definitions) for the definitions of Tiny Servants and Spellbooks; [*The Compression and the Harness*](the-compression-and-the-harness.md), in this repository; the book's [Conclusion](https://github.com/rolldabones/final-liability-rests-with-the-human-book-wip/blob/main/manuscript/24-conclusion.md) |
| Section 6: the ushabti and the hydra | The [profile README](https://github.com/rolldabones/rolldabones#definitions) for Tiny Servants; [*The Ungoverned Channel*](https://github.com/rolldabones/the-ungoverned-channel) for agents in a shared channel |
| Section 9: the charter and the tests | The [Slow AI Kitchen](https://github.com/rolldabones/slow-ai-kitchen), the method; the [AI Impact Assessment Tool](https://github.com/rolldabones/AI-Impact-Assessment-Tool), the Informed Intent gate in tool form |
| Sections 10 and 16: authority, ratification and the summoner | [*Slow AI for the Chief Legal Officer*](slow-ai-for-the-chief-legal-officer.md), in this repository; [AI Governance for Boards](https://github.com/rolldabones/ai-governance-for-boards) at board altitude |
| Section 12: capture | [*The Map and the Pair*](the-map-and-the-pair.md), in this repository, on reading claims you cannot check yourself |

## Source basis and attribution

Prepared on 30 October 2026 (KST) from the author's working notes of October 2026, with Claude, against DOCTRINE.md v1.2.1. The doctrines are used as stated in DOCTRINE.md, and each short form in Section 13 is copied from its section 8. *Human* is capitalized only where it denotes the named owner of section 3 of that file; elsewhere *human* is the common noun.

The descriptions of myths, folklore and literature in Sections 1 to 6 summarize the works and scholarship listed in the bestiary at a general level. They are not offered as scholarship, and source criticism of the traditions would be needed before any of them is relied on for more than illustration. The AI mappings, the rankings, the vocabulary, the Familiar's Charter, the seven tests and the governed-familiar model are the author's interpretation. The English of the epigraph is a plain rendering for this piece, not a published translation.

Legal and standards sources, each read on 30 October 2026 (KST) unless noted. Jurisdictions: the United States (model law and one state enactment), British Columbia, Canada (one tribunal decision) and the European Union; standards from NIST and ISO/IEC.

- American Law Institute, *Restatement (Third) of Agency* (2006), §§ 1.01 and 2.03, read in the [excerpts published on Open Casebook](https://opencasebook.org/casebooks/16481-selected-excerpts-of-restatement-of-agency-third-professor-randle-pollard/as-printable-html/). Section 4.01 and the comment to § 1.04 were not read; the comment is described as reported in Quinn Emanuel Urquhart & Sullivan, ["When AI Agents Do the Transaction"](https://www.quinnemanuel.com/media/lgthrl2u/client-alert-when-ai-agents-do-the-transaction.pdf), client alert, undated, which notes that the comment is not a holding.
- Uniform Electronic Transactions Act (1999), § 14, read in Minnesota's enactment, [Minn. Stat. § 325L.14](https://law.justia.com/codes/minnesota/2022/chapters-324-341/chapter-325l/section-325l-14/) (2022), on Justia's reproduction of the statute. Enactment varies by state; the uniform text was not read. The adoption count is from the [Wikipedia article on UETA](https://en.wikipedia.org/wiki/Uniform_Electronic_Transactions_Act).
- [*Moffatt v. Air Canada*, 2024 BCCRT 149](https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do), Civil Resolution Tribunal of British Columbia, 14 February 2024, para. 27, read on the tribunal's official decisions site.
- Regulation (EU) 2024/1689 (Artificial Intelligence Act), [Article 14(4)(b)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng), and the application dates in Article 113 as replaced by Regulation (EU) 2026/1744 (OJ L, 2026/1744, 24.7.2026), stated as in *The Compression and the Harness*, whose source note records the reading of both on the Official Journal page; not re-read for this piece.
- National Institute of Standards and Technology, [*Artificial Intelligence Risk Management Framework (AI RMF 1.0)*](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), NIST AI 100-1, January 2023: GOVERN 3.2, the description of GOVERN as cross-cutting and Appendix C, "AI Risk Management and Human-AI Interaction". [*Generative Artificial Intelligence Profile*](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), NIST AI 600-1, July 2024, cited for its existence and scope.
- ISO/IEC DIS 42105, [*Information technology, Artificial intelligence, Guidance for human oversight of AI systems*](https://www.iso.org/standard/86902.html), status as shown on the ISO page: Draft International Standard, enquiry phase.

Game and reading-list sources for the section on the table and the shelf:

- This work includes material taken from the System Reference Document 5.1 ("SRD 5.1") by Wizards of the Coast LLC and available at https://dnd.wizards.com/resources/systems-reference-document. The SRD 5.1 is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). The quotations from the find familiar, simulacrum and wish spells were read in the SRD text as served by the [D&D 5e SRD API](https://www.dnd5eapi.co/api/spells/find-familiar), not in the Wizards of the Coast PDF itself.
- Gary Gygax, *Advanced Dungeons & Dragons Dungeon Masters Guide* (TSR, 1979), Appendix N, reread by the author in the *Guide* itself while writing this piece; the list as set out in the bestiary was transcribed from a [reproduction](https://tkurtbond.github.io/posts/2020/11/30/dnd-dmg-appendix-n) and checked against the [Wikipedia article](https://en.wikipedia.org/wiki/Appendix_N), which also records the name "Vancian" for the game's spell-memory system.
- The descriptions of the collections on the shelf, including the Grimms' revisions and Calvino's method, follow the pages linked in the bestiary.

Historical and literary sources for Sections 1 to 6, beyond the bestiary:

- ["Clockwork"](https://en.wikipedia.org/wiki/Clockwork), Wikipedia, for the English rendering of Yan Shi's figure as "leather, wood, glue and lacquer"; the Chinese text is linked in the bestiary.
- ["Dokkaebi"](https://en.wikipedia.org/wiki/Dokkaebi), Wikipedia, for the origin of dokkaebi in possessed household tools such as brooms and their distinction from ghosts of the dead.
- "The License to Depart", in *The Lesser Key of Solomon: Goetia*, the Mathers and Crowley edition, read on [Sacred Texts](https://sacred-texts.com/book/the-lesser-key-of-solomon/the-license-to-depart) in Chrome on 30 October 2026 (KST).
- Psalm 139:16 and Babylonian Talmud, Sanhedrin 65b, read in translation on Sefaria for this piece; not read in the original.
- ["Golem"](https://www.jewishencyclopedia.com/articles/6777-golem), *Jewish Encyclopedia* (1906), for Psalm 139:16 and the Prague attribution, read as a historical reference work and not as current scholarship. It does not record the *emet* and *met* tradition.
- ["Golem"](https://en.wikipedia.org/wiki/Golem), Wikipedia, for the *emet* and *met* tradition, the Chełm story (Christoph Arnold's letter of 1674), the Prague Sabbath story and the dating of the Prague legend to the early nineteenth century, each with the article's own citations; a tertiary source, used for orientation only.
- Apollodorus, *The Library*, 1.9.26 (Talos) and 2.5.2 (the hydra), and Apollonius of Rhodes, *Argonautica*, Book 4, as linked in the bestiary.
- *Book of the Dead*, spell 6, as described in Taylor (2010).

---

*This document is provided for general informational and discussion purposes regarding the governance and use of AI. It does not constitute legal advice with respect to any specific matter, jurisdiction or engagement.*

**Final Liability rests with the Human.**
