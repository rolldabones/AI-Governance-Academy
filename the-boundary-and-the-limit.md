# The Boundary and the Limit

**Effectiveness, Lean AI and the Theory of the Governed Firm**

Son-U Michael Paik · CEO, GRC Solutions Korea

Working paper, version 1.4 · 17 November 2026

*For Jerry Evensky, who opened my eyes to economics in 1988.*

**Abstract.** Enterprise AI raises questions that are older than AI. This paper reads the answers at their sources and changes one fact: an AI agent takes direction and uses discretion without being employed. The test of delegated work is effectiveness, the outcome accepted against criteria fixed in advance, because the ratios of activity that pass for efficiency have no ceiling. An enterprise that directs agents has two boundaries, the firm that answers and the firm it can govern, and the gap between them is exposure. It should rent the model and own the specification, the evidence, the permissions and the exit. When execution can be rented, the limit on the governed firm is the capacity of named, qualified people to authorize work, confirm it and answer for it. Past that limit the old tradeoff between efficiency and equity returns in a plain form: the cost of efficiency is paid by people who cannot carry it. The limit can be estimated per owner from records a pilot already keeps, and the estimate has a ceiling. The practice that follows, Lean AI, is lean in Toyota's sense and not in the sense of headcount. The paper introduces three doctrines of AI governance, risk management and compliance (Slow AI, Informed Intent and Final Liability) as the conditions that the older theory requires. It credits close prior statements of most of its parts, reports no measurement and states the tests that would defeat it.

**Keywords.** theory of the firm; AI agents; effectiveness; equity and efficiency; oversight; accountability; lean production; governance, risk management and compliance

**JEL classification.** D23, D63, L22, L23, M11, O33

**Correspondence.** sonupaik@gmail.com · [www.grcskorea.com](https://www.grcskorea.com)

---

## 1. Introduction

On 30 November 2022, ChatGPT was introduced to the world. At the time I was an executive at a mid-sized specialty steels conglomerate based in South Korea, in charge of legal, compliance and trade risk management. I was arguably at the apex of my career, the second most senior person in the group's holding company, ready to coast into the CEO spot and then into retirement. Instead, I quit.

The four years that followed are a large story, and it has been told many times. My own four years since have been a smaller story. First a user, then a builder, then an auditor and now an architect, working across OpenAI, Anthropic, Google, Perplexity, MindStudio, Remy and a good many other tools. It is a new career at 56, and I am only a few steps in. The large story has its fallen: products withdrawn, companies absorbed and forecasts that did not last the year. I have my own fallen too, before AI and with it. I am reaching back for their lessons and building them into GitHub, The Slow AI Kitchen, the Library and the AI Architecture Studio, so I remember what to avoid.

This paper is part of that reaching back. Its method fits in a sentence: the Future is in the Past. Each question that enterprise AI now puts to a board was put earlier to another machine or another form of organization, and it was answered by someone who could not have known how the answer would be used. The method is to find the old question, read the answer at its source, change the one fact that AI changes and see what still holds.

The reading list turns out to be my own education in the order I received it. Economics came first, as an undergraduate at Syracuse, where Jerry Evensky opened my eyes to the subject in 1988. Operations management followed, in Japan, then a business degree and law school in the United States, practice in New York and California (junk bonds and junk equity, respectively) and a return to Korea to build and manage risk management systems for its conglomerates. All of that came before AI.

One lesson from his classroom has stayed with me for nearly forty years. Evensky explained a line that Walt Kelly, the author of the comic strip *Pogo*, wrote for a poster for the first Earth Day in 1970: "We have met the enemy and he is us" (Billy Ireland Cartoon Library & Museum 2020). As I remember them, his explanations dwelt on the tradeoffs between equity and efficiency and on the larger questions of policy around them. He later gave the idea a name, the Pogo Principle, and turned it on his own discipline in his presidential address to the History of Economics Society. The trouble, he argued, lies in ourselves and in the assumptions we have stopped examining, and the history of economic ideas is where a discipline goes to examine them. The same address records what he tells an introductory class: that markets are amoral, as computers are, powerful at processing information and indifferent to the use that is made of it (Evensky 2012). This paper borrows his method and applies his principle to the machines.

The fact that changes is small to state. An AI agent takes direction and uses discretion without being employed. Until now, discretion inside a firm came only with a person attached, and the theory of the firm, the law of employment, the practice of management and the design of production systems all took that for granted.

The question is how an enterprise should be designed when much of its work can be delegated to software that it directs. It grew out of work on a roadmap for enterprise AI adoption, which asks how a business should bring AI in. The design question lies underneath that one, and it is older.

**What the paper claims.** There are six claims. Section 2 credits the prior statements of each.

1. *Effectiveness.* The test of AI at work is the outcome accepted against criteria fixed in advance. The ratios of activity that pass for efficiency in knowledge work have no upper limit, and AI raises them at will (Section 4).
2. *Boundary.* An enterprise that directs agents has two boundaries that used to be treated as one: what it answers for and what it can govern. The gap between them is exposure, and autonomy widens it (Section 5).
3. *Ownership.* The enterprise that rents a model should own the specification, the evidence, the permissions and the exit (Section 6).
4. *Limit.* When execution can be rented, the limit on the governed firm is the time in which named, qualified people can authorize work, confirm it and answer for it. The limit is economic before it is doctrinal, and it is where the old tradeoff between efficiency and equity returns: past it, the cost of efficiency is paid by people who cannot carry it (Section 7).
5. *Arithmetic.* The limit can be estimated per named owner from minutes that a pilot already records, and the estimate has a ceiling that the activity ratios lack (Section 8).
6. *Lean AI.* The practice that follows is lean in the sense of the Toyota Production System and not in the sense of headcount: the power to stop comes first, and then only the outcomes that someone will accept (Section 9).

**What the paper is not.** It is a hypothesis with its tests attached, and it reports no measurement of any firm. It does not forecast whether firms will get smaller or larger, and Section 5 explains why the theory cannot. It states no law: where the law of agency or of electronic transactions bears on the argument, it points to a companion piece that states that law by jurisdiction and date (Paik 2026c). It adds no doctrine to the practice it comes from. The economics, the history and the management theory are other people's and are credited to them. Section 2 says what is left.

Section 3 introduces the practice and its three doctrines. Sections 4 to 9 make the six claims in order. Section 10 takes the failures and the strongest objection, Section 11 the order of design decisions and the tests, and Section 12 shows how the practice's published work fits the argument. Limitations and a conclusion follow. A reader with ten minutes can read the one-page summary after the conclusion and the worked example in Section 8.2. Appendix C turns the paper into a worksheet for one owner and a set of questions for a board or a seminar.

## 2. Related work and what this paper adds

Four bodies of work bear on the question.

The first is the theory of the firm: Coase (1937) on why firms exist and where they end, Williamson (1985) on dependence between a firm and its suppliers, and Grossman and Hart (1986) and Hart and Moore (1990) on ownership as the right to decide what a contract left open. Inside it runs a long line of work on management as the limit to a firm's size or growth: Robinson (1934), Kaldor (1934), Penrose (1959), Williamson (1967), Calvo and Wellisz (1978) and Garicano (2000).

The second is recent work on AI agents in economics, management and law. Hadfield and Koh (2025) survey what agents may do to markets, firms and institutions. Shahidi et al. (2025) take the side of the market, where agents lower transaction costs. Ide and Talamàs (2025) put agents into Garicano's hierarchy. Catalini, Hui and Wu (2026) argue that the binding constraint on growth becomes what they call human verification bandwidth. Tomašev, Franklin and Osindero (2026) carry the span of control over to people who oversee agents. Hydari and Muzaffar (2026a, 2026b) separate the boundary across which work is executed from the boundary of accountability. Humberd and Latham (2026), Warin (2026) and Kolt (2025) read agents through agency theory, transaction costs and the law of agency. Outside the journals, Rih (2026a, 2026b) reads Coase and the history of project management against his own work with agents, and Spataro (2025) proposes a human-agent ratio as a metric for managers.

The third is the literature on people who supervise automation: Bainbridge (1983) on the skills that automation removes, Olsen and Wood (2004) on how many robots one person can control, Parasuraman and Manzey (2010) on complacency, and Matthias (2004), Santoni de Sio and van den Hoven (2018), Elish (2019) and Green (2022) on responsibility for what automated systems do.

The fourth is the history of efficiency and the management writing on effectiveness and on lean production: Alexander (2008, 2009), Drucker (1963, 1967), Ohno (1988), Womack and Jones (1996) and, most recently, Newport (2026).

Table 1 sets the six claims against the nearest prior statements that a search on 17 November 2026 found. The search was targeted and not systematic (Appendix B).

| Claim | Nearest prior statements | What this paper adds |
|:-------------|:--------------------------------|:--------------------------------|
| 1. The test is effectiveness, not activity | Polakov (1909), as reported by Alexander (2009); Drucker (1963, 1967); Newport (2026) | The accepted outcome as the auditable form of effectiveness; a ceiling restored through the oversight inequality |
| 2. The boundary | Rih (2026a): the agent as Coase's employee in economics and not in law. Aghion and Tirole (1997): formal and real authority. Hydari and Muzaffar (2026a, 2026b): execution and accountability boundaries between organizations | The novelty placed in discretion, which until now came only with a person; two boundaries inside one enterprise, the answerable firm and the governed firm; the gap as exposure; autonomy as the dial |
| 3. What to own | Teece (1986): complementary assets. Hydari and Muzaffar (2026a, 2026b): accountability assets. Rih (2026a): context as the new hold-up asset. Warin (2026): workflows the firm does not see | The deploying enterprise's rule, derived from the right to decide what a contract left open, with the rehearsed exit counted as an asset |
| 4. Oversight as the binding limit | Robinson (1934) to Garicano (2000) on supervision. Catalini, Hui and Wu (2026) on verification, for the economy. Rih (2026a) on signatures. Tomašev, Franklin and Osindero (2026); Spataro (2025). Okun (1975) and Evensky (2012) on efficiency and equity | A limit on the governed firm in Coase's sense, stated per named owner in qualified hours that cannot be pooled and tied to three acts; the argument that it is economic before it is doctrinal; the limit read as the point past which the cost of efficiency falls on people who cannot carry it |
| 5. The arithmetic | Rih (2026b): plan capacity in review hours and cap the work handed out. Olsen and Wood (2004): fan-out | The split into routine, exception and standing time per owner, taken from records an enterprise keeps; four readings; the governed share as a ratio with a ceiling |
| 6. Lean | Ohno (1988); Womack and Jones (1996). Rih (2026b): a cap on work in progress at the reviewer | *Jidoka* and just-in-time carried over to agents as two pillars; the accepted outcome as the unit; "lean" detached from headcount |

*Table 1. The six claims, the nearest prior statements of each and what this paper adds.*

The worked example in Section 8 and the tests in Section 11 are this paper's own, though the habit of attaching to each claim the evidence that would defeat it is one that Rih's essays also keep.

Four debts are larger than a citation.

Rih published the reading of Coase that Section 5 starts from on his own site on 28 October 2026, and it was republished on HackerNoon on 4 November. He gave it the name I would have wanted, the employee without the employment. Two days after the first essay he wrote that capacity should be planned in review hours and that the work handed to a reviewer should be capped, as a factory caps work in progress (Rih 2026b). Where his essays and this paper overlap, the priority is his.

Catalini, Hui and Wu stated in February 2026, for the economy as a whole, the thesis that Section 7 states for the firm. My book manuscript reaches the same point from practice, as a ratio of agents to oversight that is set by a decision about risk appetite (Paik 2026d, ch. 14). That passage has been in the manuscript's repository since June 2026, which is later than their paper and makes no claim on it.

Newport (2026) sent me to Alexander's history of efficiency, on which Section 4 rests.

The strongest objection to the paper is in Hadfield and Koh (2025), and Section 10 answers it.

None of these authors has seen this paper or endorsed it.

## 3. Three doctrines and a practice

The paper is written from inside a practice: enterprise AI governance, risk management and compliance, as I have designed it for Clients and published it in the open. Three doctrines run through that practice. They are stated once, in normative form, in a canon (Paik 2026f), and they are given here in the canon's short forms.

> **Slow AI**: AI that cannot be governed, explained and audited is not deployed; the three tests are conjunctive, and the doctrine is a precondition, not a speed limit.

Governed means a named owner, defined boundaries and a working intervention path. Explained means that the organization can state why an output was produced in terms the affected person can use. Audited means that the evidence exists before it is asked for, not after.

> **Informed Intent**: no AI system acts without prior authorization stating its purpose, authority, boundaries and exit, given by a human who meets the five authorizer conditions.

The doctrine has two limbs. The instrument has four elements: purpose, authority, boundaries, exit. The person who signs must meet five conditions: Knowledge, Evidence, Authority, Time and Permission, the last being the ability to decline without retaliation. An authorization that carries all four elements and is signed by someone who lacks any of the five conditions is, in the canon's word, paperwork.

> **Final Liability rests with the Human**: every material outcome attaches to a named human owner with decision rights, oversight and the power to intervene.

A name alone is not enough. A person who is named and holds none of the three attributes is a nominee. Accountability has three moments: the owner is named at specification, accountability attaches at confirmation and it holds through reliance.

The doctrines are sequential. Informed Intent governs entry, Slow AI governs the condition of the thing authorized and Final Liability governs the whole span. Beneath them sits an operating framework, GRCnext™, whose question is whether the enterprise will still have lawful, authorized and executable choices when a provider, a technology or an assumption fails. Its five primitives are Services, Tolerances, Pipes, Switches and Exits. The method that carries the doctrines into daily work is The Slow AI Kitchen (Paik 2026g): twelve steps, ten of which are gates, with three tiers of risk, published as a repository and as a guided web application in four languages.

The doctrines are the author's and are not law. The canon records two statutory analogues and says in terms that a doctrine is not to be presented as law (Paik 2026f, DOCTRINE.md, secs. 3.3 and 7).

They enter this paper as boundary conditions. Each turns out to be a condition on one of the paper's objects: Slow AI on the boundary of the firm, Informed Intent on the delegation that replaces the employment contract and Final Liability on the limit. The paper's claim is that these conditions are what the older theory requires once discretion no longer comes with a person. A reader who rejects the doctrines can still test the theory, because Section 7 argues that the limit is economic first.

## 4. Efficiency, effectiveness and the accepted outcome

### 4.1 A measure with a ceiling

In the 1750s John Smeaton built model waterwheels and compared, for a given fall of water, the work that a wheel delivered with the work that the water made available (Smeaton 1759; Alexander 2009, 1015). He did not use the word efficiency. His term was mechanical effect (Alexander 2009, 1015 n. 4). During the nineteenth century the comparison became a ratio with a name. Rankine tied it to the conservation of energy, as effect produced over energy used, and thermodynamics gave it a theoretical upper limit (Alexander 2009, 1010, 1015–17). Alexander calls measures of this kind bounded, because the quantities in them are limited by natural law (2009, 1020). Such a measure runs from zero to one, and a designer always knows how much is left to gain.

### 4.2 A measure without one

Around 1900 the ratio traveled from engines to the management of workshops and of people, where it was asked to measure things that no conservation law connects (Alexander 2008; 2009, 1017–21). Walter Polakov, an engineer writing in 1909, saw the difference. As Alexander (2009, 1020) reports him, he called a ratio set against a chosen standard arbitrary, a word he used to mark the element of human choice in it. One of his examples was the potato. If 100 bushels an acre is taken as the standard, a Wyoming yield of 200 bushels is an efficiency of 200 percent. A measure of that kind has no ceiling, and nothing in it says whether the standard was the right one.

Alexander adds that the two forms are sometimes used to tell engineers from economists. An engineer's machine cannot reach one hundred percent. An economist's measure can exceed it, because its standard is set in terms other than energy (2009, 1020). The economist's efficiency is also the one that textbooks weigh against equity. The classic statement is Okun (1975), whose own word was equality. This paper stays with the engineer's and the manager's sense of the word until Section 7, where the question of equity returns.

Newport (2026) brings the distinction to the present. Knowledge work, he argues, is run on an implicit arbitrary ratio, something like visible tasks completed per person, which he has elsewhere called pseudo-productivity (Newport 2024). It has both defects. The visible tasks may have little to do with what the organization is paid for, and the ratio can always be pushed higher. Generative AI, on his account, is a crank that produces visible tasks, and agents are cranks that turn other cranks. The numerator rises without limit and the results do not follow.

Economics supports the diagnosis at one point and qualifies it at another. Holmström and Milgrom (1991) showed that when a job has several dimensions and only some are measured, rewarding the measured ones draws effort away from the rest. An activity ratio is such a reward. The qualification is the productivity J-curve of Brynjolfsson, Rock and Syverson (2021): a general-purpose technology needs complementary investments that the accounts do not record, so measured productivity lags before it recovers. Disappointing early returns are therefore weak evidence that a technology does not work. They are also what this paper's argument predicts, since the capacity to govern delegated work is an investment of exactly that unrecorded kind.

An arbitrary ratio is the Pogo Principle in a small case. The standard did not choose itself. When a count of activity misleads an enterprise, the machine that inflated the count is not the author of the error.

### 4.3 Effectiveness

The alternative has been available throughout. In Alexander's history, effectiveness names the bringing about of an effect, and efficiency adds the controlled apportioning of the resources used to get it (2009, 1027).

Drucker made effectiveness the first duty of management. His article of 1963 is titled for it and opens by asking what the manager's first duty is (Drucker 1963). His book of 1967 separates the two measures by the kind of work. Manual work, he wrote, needs only efficiency, which is doing things right. Effectiveness is getting the right things done, and it is what knowledge work needs, because that work is defined by its results and the person doing it cannot be supervised in detail (Drucker 1967, ch. 1). Two further points in the book matter here. An organization has no results inside itself; they are all on the outside (ch. 1). And the resource that limits an executive is time, which cannot be rented, hired or bought (ch. 2).

Newport's remedy is Drucker's in working form. Stop counting activity. Ask each person, at intervals, to make the case for what they produced that was valuable, and judge the case (Newport 2026).

### 4.4 The accepted outcome

Effectiveness has a weakness that efficiency was invented to cure. It can be asserted after the fact, by the person who did the work, against whatever standard the work happens to meet. Then it is as arbitrary as any ratio. It is also silent about what was spent to get the effect (Alexander 2009, 1011, 1027).

The practice this paper comes from answers with two moments that it treats as non-delegable. Done is defined before the work begins, as tests that can pass or fail, and a named person confirms the work against those tests before anyone relies on it (Paik 2026b). An *accepted outcome* is an output that has passed through both moments. It is effectiveness in a form that can be audited: the standard was fixed in advance by someone with the authority to fix it, and the acceptance has a name and a date.

The accepted outcome is the unit of Lean AI (Section 9). It also changes what efficiency should mean in an enterprise that directs agents. Execution is the input that has become cheap, so economizing on it is a small matter. The input worth economizing is the scarce one, and Sections 7 and 8 argue that it is the attention of the people who can accept.

## 5. The boundary: direction without employment

### 5.1 Coase's firm

In 1937 Ronald Coase asked why, in an economy that prices are supposed to coordinate, there are firms at all. His answer starts from an observation: inside a firm nothing is coordinated by price. A workman who moves from one department to another does so on an order, and no price has changed (Coase 1937, sec. I).

There are two ways to coordinate work, price and direction, and a firm is where direction has replaced price. The market costs something to use: prices have to be discovered and a contract negotiated for each exchange. Coase called these marketing costs; the name transaction costs came later. A firm saves them by replacing many contracts with one. Under it a person agrees to obey the directions of an entrepreneur within certain limits, and the contract's task is only to state those limits (sec. II). He tested the definition against the law of master and servant and found the same thing there: what makes the legal relation of employer and employee is the fact of direction (sec. V). Simon (1951) later gave the idea formal shape. The employee accepts the employer's authority within an area of acceptance, and the employer decides within it.

Three results follow, and the paper uses all three.

*A boundary.* A firm takes work inside until organizing one more transaction by direction costs as much as buying it in the market or leaving it to another firm.

*A limit.* The cost of organizing rises as the firm takes on more, and the person directing makes more mistakes about where resources are best used. Coase noted that economists already had a phrase for this, diminishing returns to management, and sent the reader to Kaldor (1934) and Robinson (1934).

*A measure.* A firm becomes larger as more transactions are organized by direction and smaller as it gives them up. The size of a firm is the amount of work it directs. The number of people it employs does not enter the definition.

### 5.2 What the theory cannot forecast

Coase thought about technology. The telephone and the telegraph, he wrote, reduce the cost of organizing across distance and so tend to enlarge the firm. A footnote adds the qualification that matters now: most inventions change both the cost of organizing and the cost of using the market, and whether firms grow or shrink depends on which falls further (sec. II).

AI lowers both. Agents can search, compare, negotiate and contract, and Shahidi et al. (2025) set out what that could do to markets. Direction also gets cheaper, because work can be assigned by instruction with nobody hired to do it. Serious writers hold each view of the net effect. Hadfield and Koh (2025, sec. 3.1) describe how agents could push firms toward greater scale and scope. Rih (2026a) bets that direction wins, so that firms cover more ground with fewer people. Ide and Talamàs model agents inside a hierarchy of knowledge, and in working-paper versions of their article the abstract reported both outcomes: smaller firms under what they call basic autonomous AI and larger ones under advanced autonomous AI (Ide and Talamàs 2024, 2025). A preregistered field experiment at Procter & Gamble found that individuals with AI performed about as well as teams without it and that the exceptional results came from teams with AI, which supports testing new arrangements and does not support a staffing plan (Dell'Acqua et al. 2026; Paik 2026a, sec. 5). This paper therefore makes no forecast of size.

### 5.3 Direction without employment

For Coase, direction ran through employment. Three remarks in his paper carry more weight now than he gave them. Where a contract for a service states only its limits and the buyer settles the details later, the direction of resources has come to depend on the buyer, and the relationship he calls a firm may result (sec. II). The economist's firm and the lawyer's employment are not identical, because a firm may also control another person's property (sec. V, note). And direction is a matter of degree: in the law he consulted, the right of control separates a servant from an independent contractor, who is left to manage the work and has undertaken a result (sec. V).

An AI agent is directed without being engaged. It is given a task, limits and tools. It has no contract of its own. The contract is with a provider, for the use of a model: the tokens are bought at a price, as the hire of a machine is, and what the model does with them is settled by the enterprise's instructions. By Coase's test the work is inside the firm. The law he tested against had a person in the servant's place, and here there is none. Rih (2026a) made the observation first: in economic terms the agent is the employee Coase described, and in legal terms it is not an employee at all.

Firms have always directed things that are not employed. A lathe is directed. What is new is that the thing directed uses discretion: given an objective, it chooses its own steps. The instruction it receives is an incomplete contract in the economist's sense (Hadfield-Menell and Hadfield 2019), and the agent fills the gaps itself. The practice calls a narrow service of this kind, with one purpose, clear boundaries and a named owner, a Tiny Servant. The name is exact in Coase's economic sense and deliberately modest, because the thing is not a person and should not be taken for one.

The first consequence is one of measurement. The firm in Coase's sense, the work under direction, and the firm on the payroll are no longer the same size. A business of five people may direct a volume of work that once took fifty. By Coase's measure it is a large firm, and a count of employees will miss it.

The second consequence is the subject of the rest of the paper. Employment supplied more than labor. It supplied a person, who can question an instruction, notice that something is wrong, ask what was meant and remember the last mistake, and who can be trained, licensed, disciplined and held to account. A model may decline some instructions, but it does so because its maker built it that way, which is the maker's control and not a duty owed to the enterprise. The agent has nothing at stake and owes nothing, and the law read in a companion piece treats it as the instrument of whoever uses it (Paik 2026c; Kolt 2025 covers the same ground at length). Everything that employment supplied apart from the labor therefore has to be supplied again, on purpose, by the enterprise. The limits a person would have respected become permissions that a system enforces. The noticing becomes monitoring and evidence. The answering becomes a named human being. The agent does the work. The enterprise has to build the rest of the employee.

### 5.4 Two boundaries

In the firm Coase described, three things had roughly the same edge: the work the firm directed, the work its managers could oversee and the work it answered for. They coincided because all three ran through the same people. The fit was never exact, as any firm that has had a rogue trader knows. But the outer edge could move only one hire at a time.

Agents pull the edges apart. Direction now grows at the price of tokens. What the firm answers for grows with it. Oversight grows only as far as somebody builds it. An enterprise therefore has two boundaries where it used to see one (Table 2).

| | The answerable firm | The governed firm |
|:-----------|:-------------------------|:-------------------------|
| What is inside | Everything done in the enterprise's name, by a person or by a system | The part of that work it has authorized, can evidence and can stop |
| Who draws the line | The law, the contract and the customer | The enterprise itself |
| How far it reaches | To everything the enterprise can be held to. The prudent assumption is all of it | As far as authority, evidence and intervention reach |

*Table 2. The two boundaries of an enterprise that directs agents.*

The space between the two is work that the enterprise will answer for and cannot see, explain or stop. In risk terms it is exposure that nobody chose.

The distinction has two ancestors. Aghion and Tirole (1997) separated formal authority, the right to decide, from real authority, the effective control over decisions, which goes to whoever has the information. The answerable firm is drawn by formal authority and the governed firm by real authority. Athey, Bryan and Gans (2020) study when a principal should give a decision to a human agent and when to an AI. Hydari and Muzaffar (2026a, 2026b) separate the boundary across which work is executed from the boundary of accountability, which stays where an output needs evidence, review, signoff or a party who can be held responsible, and they ask when the two can move together between organizations. This paper's cut is a different one. It is made inside one enterprise, between what the enterprise answers for and what it can in fact govern, and it treats the difference as a quantity to be measured and closed.

Autonomy is the dial that opens the gap. It is a design decision separate from capability (Feng, McDonald and Zhang 2025), and risk to people rises as control is ceded (Mitchell et al. 2025). Coase's third remark says why in the language of the firm. The more an agent is left to choose its own steps, the less the enterprise is directing it, and the governed boundary draws in while the answerable boundary stays where it was. With people, loosening control had a counterpart: someone outside the firm's control who had undertaken a result was a contractor, with the result to answer for. An agent left to its own devices has undertaken nothing, and there is nobody on the other side to answer.

### 5.5 Two doctrines as boundary conditions

Read beside Coase, Slow AI is a condition on the boundary of the firm: direction may extend only as far as governance already does. An enterprise may widen the governed firm as fast as it can build authority, evidence and a working stop. It may not widen the directed firm first and promise to catch up.

Informed Intent is the instrument that replaces the employment contract. Coase's contract stated the limits of the employer's power to direct. An authorization states the limits within which an agent may act. The difference between them explains the doctrine's strictness. The employment contract was negotiated with someone who had an interest in the limits. The authorization is written by the enterprise alone, for a counterparty with no interests at all. Nobody across the table will object to a boundary that is missing or an exit that does not work. The discipline has to come from the one who signs, which is why the doctrine sets conditions on that person.

Put in the canon's words, the governed firm is the work that passes the three tests of Slow AI under an authorization with the four elements, with a named human owner of the kind that Final Liability requires. A companion piece separates the permissions an agent may hold, to prepare, to recommend, to execute and to commit (Paik 2026a, sec. 6), and the book calls the enforced line a trust boundary (Paik 2026d, ch. 14). The governed firm is the sum of its trust boundaries.

## 6. What the firm must own

### 6.1 Dependence

Coase's successors asked what happens when a firm depends on a supplier it cannot easily replace. Williamson treated markets and firms as alternative structures of governance. The word belonged to his field long before it belonged to the governance of AI. His central case is the buyer who has invested in a relationship with one supplier (Williamson 1979, 1985). Before the investment there were many suppliers to choose from. After it there is one, and that one can change its terms, which is the hold-up that Klein, Crawford and Alchian (1978) analyzed. The classical remedy is to bring the supplier inside the firm, and the theory predicts that firms do so more often as the assets become more specific to the relationship (Royal Swedish Academy of Sciences 2009).

An enterprise that builds its workflows on a model makes that kind of investment. Instructions are tuned to one model's behavior. Tests are calibrated on it. People adopt its habits, and the working record of what was decided and why comes to live inside the provider's product. The practice has a word for the condition. Its provider exit drill puts it under the heading "Custody is the lock-in" (Paik 2026e).

The classical remedy is mostly closed. For most enterprises, making a frontier model is not a choice on the table. An enterprise can host an open-weight model, and then it decides when its copy changes. That choice has its own upkeep, and the practice's Lean AI module warns that self-hosting is neither automatically cheap nor automatically eligible (Paik 2026g, Lean AI, sec. 2).

### 6.2 The right to decide

Grossman and Hart (1986) and Hart and Moore (1990) supplied the reason this matters. No contract can provide for everything. The theory of incomplete contracts therefore asks who should hold the right to decide in the circumstances a contract did not foresee (Royal Swedish Academy of Sciences 2016), and its answer for assets is that the owner decides whatever the contract left open. The provider owns the model. It decides what the contract does not: when the model is updated or withdrawn, what it costs next year, which uses are allowed and how it behaves after its next update.

Hold-up also has an inside form. Warin (2026) describes agentic work that employees keep in private workflows and personal accounts, which the firm neither observes nor governs, so that its performance comes to depend on people who can leave or bargain. He calls the result agentic hold-up. Rih (2026a) makes a related bet: that what a firm knows and outsiders do not, its context, is the new asset over which it can be held up.

### 6.3 The rule

The theory does not hand over a rule. It says what the exposure is made of: investments that are worth less with any other supplier, and decisions that fall to whoever owns the asset. A design rule follows from working on both. Make the investments portable, and keep every decision that can be kept.

**Rent the model. Own the specification, the evidence, the permissions and the exit.**

Table 3 sets out the four things to own.

| What to own | What it is | Where the practice carries it |
|:-----------|:--------------------------------|:---------------------------|
| The specification | The authorization, the instructions and the definition of done, written so that they survive a change of model and held by the enterprise, not in a person's private account | Computational Drafting; The Definition of Done |
| The evidence | The test cases, the acceptance criteria and the run records, kept outside the provider, so that a changed model can be tested again and authorized again | The Consultant Workbook's records W12, W16 and W20; the custody register of the exit drill |
| The permissions | Identities, credentials and limits enforced outside the model | The book's agent registry (Appendix E); Take-Out, Delivery & Vending Machines |
| The exit | A rehearsed route to another provider or to a manual process, inside the tolerance set for the service | GRCnext-Copilot; the provider exit drill; the Workbook's stop and fallback exercise, W21 |

*Table 3. What the deploying enterprise should own, and where the practice carries each item.*

The rule has ancestors. Teece (1986) showed that the profits from an innovation often go to whoever owns the complementary assets it needs. Hydari and Muzaffar (2026a, 2026b) name a class of such assets for AI, accountability assets, among them professional signoff, evidence trails and trusted systems of record, and argue that value concentrates there. Their subject is where software firms and their customers should place a boundary. The rule above is the deploying enterprise's version, and it adds an item their list does not need: the exit.

The exit is where GRCnext™ does its work. The economics explains why a rehearsed exit is more than prudence. An enterprise that has rehearsed its exit has kept one decision that the contract left open, which is whether to stay. An enterprise that has not rehearsed it has left that decision to the provider as well.

A change of model is the provider exercising its ownership. The book states the consequence for the enterprise: "Every material change to an agentic system is a governance event" (Paik 2026d, ch. 14). The evidence that supported the authorization was evidence about a system that no longer exists in that form.

## 7. The limit: governed attention

### 7.1 The old limit

Coase's limit was the cost of management, and a line of later work sharpened it. Robinson (1934) and Kaldor (1934), to whom Coase sent his readers, placed the limit in the task of coordination. Penrose (1959) argued that the rate at which a firm can grow is set by its managers, and specifically by managers with experience inside that firm, who cannot be hired ready-made (Kor and Mahoney 2004). Williamson (1967) modeled the control that is lost as instructions pass down a hierarchy, and Calvo and Wellisz (1978) the supervision that a larger firm requires. Garicano (2000) built a hierarchy in which routine problems are handled where they arise and exceptions travel up to people whose time is the scarce input. Simon (1971, 40) put the general point briefly: what information consumes is the attention of its recipients, so a wealth of one produces a poverty of the other. Knight had reached the root of it in 1921, in a passage Coase quotes. Once the future is uncertain, carrying out the work becomes secondary, and the primary problem is deciding what to do and how (Coase 1937, sec. III).

AI makes Knight's sentence literal, since execution is what has become cheap. It also changes management, and the argument has to be honest about that. Coase said that improvements in managerial technique enlarge the firm (sec. II), and agents that summarize, monitor and triage are managerial technique. The limit is therefore not fixed. What has to be settled is which part of management cannot be handed over at all.

### 7.2 Three acts

Fama and Jensen (1983) divided a decision into four steps: initiation, ratification, implementation and monitoring. They called the first and third decision management and the second and fourth decision control, and they asked how control is arranged when the people who manage decisions do not bear their consequences. Their subject was the human organization. Applied to an enterprise that directs agents, the division fits. Agents can take over decision management. The two steps of decision control stay with people, and so does the bearing of the consequences. That makes three acts: authorizing, confirming and answering.

The practice keeps the same three with people by doctrine.

- **Authorizing.** Informed Intent requires a human who meets the five conditions, and two of them, Knowledge and Time, are the ones that run short.
- **Confirming.** The Definition of Done names "the two moments that cannot be delegated": saying what done means before the work begins and confirming that it is done before anyone relies on it (Paik 2026b). In the canon's lifecycle, accountability attaches at that confirmation.
- **Answering.** Final Liability rests with the Human: every material outcome attaches to a named human owner with decision rights, oversight and the power to intervene.

Alchian and Demsetz (1972), who disagreed with Coase about authority, placed the reason for the firm in monitoring. When people produce together, somebody has to judge work whose individual contributions cannot be read off the result, and that somebody has to bear the result for the judgment to be worth anything. Agents reverse half of their problem. Every action can be logged, so who did what is no longer hard to see. Whether what was done is right remains as hard as ever, and a log does not answer it, as Rih (2026a) also observes. The scarce act has moved from watching effort to confirming outcomes, and it still has to rest with someone who bears the result.

### 7.3 The limit stated

**When execution can be rented, the limit on the governed firm is the capacity of named, qualified people to authorize work, to confirm it and to answer for what is done in its name.**

The capacity has four properties that set it apart from an ordinary budget of hours. It belongs to *named* people, because an outcome attaches to an owner and not to a department. It is *qualified*: an hour counts only from someone who knows the work well enough to judge it and holds the authority to act on the judgment. It *cannot be pooled*, because one owner's spare hours do not qualify that owner to sign another's work. And it is *slow to grow*, for Penrose's reason: the judgment is formed inside the firm, by doing the work that is now being delegated.

Nothing stops a firm from directing more than that. Coase's limit never stopped anyone either. It marked the point past which organizing costs more than it returns, and one of his reasons was that mistakes multiply as the work under direction grows. The same holds here. Past the limit the firm keeps growing as an answerable firm and stops growing as a governed one, and the cost arrives as errors that nobody was placed to catch and outcomes that somebody must answer for without having been able to see them.

The limit is economic before it is doctrinal. A firm that rejects the three doctrines still pays for the errors and still answers for the outcomes, because the law that attributes a system's acts to whoever uses it does not ask whether the user had doctrines (Paik 2026c). Nor does adding a reviewer's name restore it. The research on people who supervise automation is consistent on the point: people asked to monitor a reliable system come to miss its failures (Parasuraman and Manzey 2010), policies that rely on human oversight tend to assume a capacity to oversee that the people do not have (Green 2022), and the person nearest the machine can end up carrying the blame for an outcome that person had no means to change, which Elish (2019) calls a moral crumple zone.

### 7.4 Efficiency, equity and who pays

Section 4 kept to the engineer's sense of efficiency. The limit brings the economist's question back, because it is a question about who pays.

Up to the limit a firm faces a real tradeoff, and it can see the price. Cheaper execution is bought with the hours of the people who must stand behind it, and Section 8 counts those hours. Past the limit the price does not go away. It is paid by someone else: the owner who answers for what could not be seen, the person on the receiving end of an outcome that nobody confirmed and the junior who is no longer formed by the routine work. That is a question of equity in the plain sense of who bears the consequences of a gain.

The older economics has two things to say about it. Okun's (1975) theme was that the market has its place and must be kept there. The same is true of the agent, and the governed boundary is where an enterprise decides what that place is. And in the address cited in Section 1, Evensky reads Adam Smith to say that the distortions of power which skew a distribution also shrink the whole (Evensky 2012). The governed firm has that shape. A name without the capacity to exercise it is unfair to the person named, and it is also where the errors go uncaught. Past the limit the trade is a poor one: it buys efficiency of the arbitrary kind, a better ratio of activity to cost, and it pays in effectiveness and in equity together.

### 7.5 The same point, reached by others

Others have reached versions of this limit, and the differences are worth stating exactly.

Catalini, Hui and Wu (2026) state it for the economy. As the cost of executing falls toward zero, they argue, growth is bound by the human capacity to verify and to underwrite responsibility, and they warn that using AI to verify AI spreads correlated blind spots. Tomašev, Franklin and Osindero (2026) ask how many agents one expert can reliably oversee, and they warn against placing people in a chain of delegation only to absorb liability. Spataro (2025) proposes the ratio of humans to agents as a figure for managers to set task by task. Greenblatt et al. (2024) design safety protocols around a small budget of trusted human labor. Rih (2026a, 2026b) names the scarce thing as the signatures a person can stand behind in a day, and plans capacity in review hours.

The practice reaches the same place from governance. The companion piece on the core of the firm ends its section on competence with this sentence: "The constraint is not how much work AI can perform. It is how much delegated work the organization can remain competent to direct" (Paik 2026a, sec. 8). The book calls the failure accountability thinning: as agents multiply, each named human carries more consequence, until the name exists on paper and the capacity to exercise it does not. It observes that "the lean organization's governance capacity is its scarcest resource", and it is careful about what kind of limit this is. The threshold is not a headcount. "It is a risk-appetite decision", made in advance by the management body and put on the record (Paik 2026d, ch. 14). Past it Final Liability still attaches, but the allocation is defective, because the named human can no longer exercise the three attributes. The book's name for that person is the sin-eater.

What this paper adds is placement and a unit. The limit takes the place in Coase's structure that diminishing returns to management held, for the governed firm and not for the directed one. Its unit is the qualified hour of a named owner. The next section shows that the unit can be counted.

## 8. The arithmetic of oversight

### 8.1 The inequality

A limit of this kind can be estimated before it is reached. For each named owner $j$, over a week or a month, compare the hours of oversight that the owner's workflows demand with the qualified hours the owner can give:

```math
D_j = \sum_{w \in W_j} \left[ \frac{N_w ( a_w + e_w t_w )}{60} + s_w \right] \le O_j
```

The design holds only while the inequality does, for every owner, in the busiest period. Table 4 defines the symbols, with the subscript for the workflow left off.

| Symbol | What it counts |
|:------|:----------------------------------------------------------------|
| $W_j$ | The workflows that owner $j$ answers for |
| $N$ | Items the workflow produces in the period |
| $a$ | Routine minutes of a person's time for each item: a read, an approval or a share of a sampled check |
| $e$ | The share of items that need a person, because a check failed, a boundary was reached or the case is new |
| $t$ | Minutes to resolve one such item |
| $s$ | Standing hours the workflow takes whatever its volume: the weekly review, the monitoring and the work of authorizing it again after a change |
| $O_j$ | Hours from the owner, or from people the owner has authorized, who know the work well enough to judge it and hold the authority to act on what they find |

*Table 4. The terms of the oversight inequality.*

None of this is new economics. The structure is Garicano's (2000) hierarchy, in which exceptions travel up to the people whose time is scarce, used here as a planning check. Olsen and Wood (2004) asked the same question of robots and called the answer fan-out: the number of machines one person can control. Rih (2026b) states the rule for a software team in a sentence: count what one person can check in a week and hand out no more. The inequality separates that count into routine, exception and standing time, so that each can be measured and worked on. It has no equilibrium and it proves nothing.

The numbers are not exotic. A team that has run the practice's thirty-day engagement already has them (Paik 2026g, Consultant Workbook). Its case observation record, W16, takes down for every case the minutes of initial review, of correction and re-review and of final approval, and whether the first pass was accepted. Those give $a$, $t$ and $e$. The standing hours are in the weekly review, the change record and the monitoring plan (W18, W20 and W24A), and the competence record, W22, settles whose hours count toward $O$.

### 8.2 A worked example

Take a five-person advisory firm (Table 5). The numbers are invented and the arithmetic is the point. Three of the five each own one workflow run by agents, and each can give ten hours a week to overseeing it. The rest of their week belongs to Clients.

| Workflow and owner | $N$ | $a$ | $e$ | $t$ | $s$ | Hours demanded |
|:----------------------|-----:|-----:|-----:|-----:|-----:|---------:|
| Proposals to Clients, the founder | 36 | 12 | 25% | 20 | 1 | 11.2 |
| Billing and reconciliation, the operations lead | 600 | 0.5 | 2% | 15 | 1 | 9.0 |
| Support replies, the service lead | 1,500 | 0.1 | 3% | 6 | 1 | 8.0 |
| Total | | | | | 3 | 28.2 |

*Table 5. A week of oversight in a five-person firm. $N$ is items a week, $a$ and $t$ are minutes, $e$ is a share and $s$ is hours.*

The founder reads every proposal before it goes out, because a proposal commits the firm. Billing is checked by sample, one item in ten for five minutes. Support is checked by a lighter sample, two replies in a hundred, also for five minutes each. Each owner spends a standing hour a week reviewing what went wrong and keeping the authorization current.

Four things can be read from the table.

1. **The total passes and one owner fails.** The firm has 30 hours and the design asks for 28.2. The founder is asked for 11.2 hours and has 10. Hours of oversight are not interchangeable: the operations lead cannot sign the founder's proposals. Coase listed this among the things that raise the cost of organizing: how unlike one another the transactions are.
2. **Volume is the cheap variable.** If support doubles to 3,000 replies, which costs the firm little more than tokens, the service lead is asked for 15.0 hours. Nothing in the firm's cost of execution warns of this. Simon's (1971, 42) test for a system that processes information applies: it conserves attention only if it takes in more than it gives out.
3. **Failures arrive together.** Suppose the provider updates the model and for one week the share of items needing a person doubles in every workflow. The three owners are asked for 14.2, 12.0 and 12.5 hours, 38.7 in all against 30, before any of the three workflows has been authorized again. Human errors are scattered. The errors of one model copied across three workflows are not. This is a version, inside one firm, of the monoculture that Kleinberg and Raghavan (2021) analyze across many.
4. **Better specification creates capacity.** If a tighter brief and a check before the founder sees the draft halve the share of proposals needing rework, the founder is asked for 9.7 hours and the design holds, with every proposal still read.

The fourth reading is the commercial point of the paper. The levers that make the inequality hold are governance work: fewer items that nobody asked for, fewer exceptions through better specification and deterministic checks, faster resolution through better evidence in front of the reviewer, lighter routine review where tests have earned it and more people formed to judge. On this arithmetic, governance work sets the firm's capacity, however the accounts classify it.

### 8.3 A ratio with a ceiling

Divide the two sides and the result is a ratio of the kind Section 4 asked for. Call $\lambda_j = D_j / O_j$ the *oversight load* on owner $j$. In the example it is 1.12 for the founder, 0.90 for the operations lead and 0.80 for the service lead. Its reciprocal, capped at one, is the *governed share*: the largest part of the designed oversight that the owner can in fact perform. For the founder it is 10 hours of 11.2, or 89 percent.

The governed share has a ceiling, which the ratios of activity lack. The ceiling is not a law of nature, as the engineer's is. It is the hours of a named person, which are as inelastic as Drucker said they were. The share cannot exceed one, and an owner always knows how much room is left. An enterprise that reports the output of its agents is reporting a ratio without a ceiling. An enterprise that reports the governed share of that output is reporting one that has a ceiling. The inequality does not cap what agents can produce. It caps what the enterprise can claim to govern.

### 8.4 One lever that needs care

Confirmation does not have to be a full reading of every item. The Kitchen's three tiers scale the depth of review to the stakes without removing a gate, and its companion for agents asks what may happen between human checkpoints and has the answer written into a service ticket before the service runs (Paik 2026g, Take-Out, Delivery & Vending Machines). Routine minutes per item can then fall, by sampling or by moving the checkpoint, and standing hours rise, because more of the confirming is done at release and at every change. The trade is the owner's to make, on tested evidence and on the record. The companion marks its limit in one sentence: "Approval of the service and its menu does not verify each generated result." The samples in the example above are decisions of that kind. The example assumes they were made and recorded; it does not argue that they are right.

What may not happen is that a review stays in the design and stops being done. The book's first chapter tells of the personal seal that every employee of a Seoul investment bank pressed onto more documents than anyone could read. "The stamp was not approval. It was presence" (Paik 2026d, ch. 1). An inequality that fails and is ignored rebuilds that seal in software.

### 8.5 What the arithmetic leaves out

It has no term for errors that pass unseen, so a design can satisfy it by reviewing less and missing more; it has to be read beside a measure of defects. It counts hours and not competence. It treats a week as smooth when work arrives in bursts, which is why it is read at the peak. It cannot see the case in which one person operates a workflow and also oversees it, which the book calls role collapse. And it does not set the threshold. That remains the management body's decision; the inequality only shows how close a design runs to it.

## 9. Lean AI

### 9.1 What lean meant

The second discipline in the education described in Section 1 has its own old answer. The word lean was attached to the Toyota Production System by Krafcik (1988), and Womack and Jones (1996) made it a general doctrine of management. Its principal architect described it in a book whose subtitle looks beyond large-scale production (Ohno 1988). Toyota's own account rests the system on two pillars (Toyota Motor Corporation n.d.).

The first is *jidoka*, which the company glosses as automation with a human touch. A machine detects an abnormality and stops, or an operator stops the line by pulling a cord. Two consequences follow in Toyota's account. Defects stop flowing downstream. And because the machine stops by itself, nobody has to stand and watch it: people respond when there is an abnormality and are otherwise free. The same account adds a condition and a limit. The condition is that the work is first done thoroughly by hand, until it is understood well enough for its abnormalities to be defined, and only then given to a machine. The limit is that machines do not improve themselves. Only people carry out *kaizen*, the steady improvement of the work.

The second pillar is just-in-time: making only what is needed, when it is needed and in the amount needed, at the pace at which it is sold, so that only what can be sold is produced.

Neither pillar is a headcount target. Where the account mentions labor, it is the labor of watching machines that is saved. The system's stated philosophy is the complete elimination of waste, and its account of *jidoka* names three things to remove from the work before a machine is given it: waste, inconsistency and unreasonable requirements, in Japanese *muda*, *mura* and *muri*.

### 9.2 What lean has come to mean for AI

In the vocabulary of AI start-ups, lean now describes a ratio. A public leaderboard of "lean AI native" companies admits those with annual recurring revenue above five million dollars, fewer than 50 employees and less than five years of age, and it reports revenue per employee among its key metrics (Shi 2025). An earlier use of the phrase, Patel (2020), is about growth marketing with a lean team.

Revenue per employee is an arbitrary ratio in Polakov's sense. Its standard is chosen and it has no ceiling. By Coase's measure, a company of thirty people that directs the work of thousands of agents is a large firm with a small payroll, and the ratio says nothing about how much of what it directs is governed. Some of these companies may be very well run. The measure cannot tell which.

### 9.3 The two pillars, carried over

Read against agents, the Toyota account maps onto the practice almost line for line (Table 6).

| Toyota Production System | For work directed at agents | Where the practice carries it |
|:----------------------|:---------------------------|:------------------------|
| *Jidoka*: the machine stops at an abnormality, or a person stops the line | A workflow that detects that it has left its boundary and stops; a person with the authority and the means to stop it | Slow AI's working intervention path; the Switches of GRCnext™; the stop and fallback exercise (W21) |
| People respond to abnormalities and do not watch machines | Oversight by exception, with the exception defined in advance | The gates of the Kitchen; the terms $e$ and $t$ of Section 8 |
| By hand first, then by machine | The work is done and understood by a person before it is delegated | The Kitchen's Step 3, Gate 2: Manual First Pass |
| Just-in-time: only what is needed, when and in the amount needed | Only outputs that a named recipient needs and a named person will accept | Lean AI: the recipient is named, and the unit is the accepted outcome |
| *Kaizen*: only people improve the work | The weekly review; the specification as the thing improved | The Workbook's W18; Computational Drafting |
| *Muda*, *mura*, *muri*: waste, inconsistency, unreasonable requirements | Output that nobody accepts; work that arrives in bursts; an owner asked for more hours than the owner has | The inequality, read per owner and at the peak |

*Table 6. The Toyota Production System read against work directed at agents.*

The mapping also sorts the levers of Section 8. *Jidoka* is what allows routine minutes per item to fall, because a workflow that stops itself does not have to be watched. Just-in-time lowers the number of items. *Kaizen* lowers the share of exceptions and the time each takes. And an owner who is asked for more hours than the owner has is under an unreasonable requirement in the plainest sense.

The order of the pillars matters. Toyota lists *jidoka* first, and so does the practice: Slow AI is a precondition. An enterprise that adopts the economy of just-in-time without the power to stop has made its agents cheaper and nothing else.

### 9.4 Definition and measures

The practice's module defines the term in one sentence: "Lean AI is the disciplined removal of avoidable work, inference and dependency from AI-enabled workflows, while preserving defined outcomes, required controls and human accountability" (Paik 2026g, Lean AI). Its unit is one accepted business outcome. The module disclaims novelty and any ownership of the term, and it is marked as a work in progress: its checks are documentary, no enterprise pilot has been run and no saving is established.

Three measures follow from this paper's argument. The first and the third are already in the module, and the second is proposed here.

1. *Cost per accepted outcome.* The total attributable cost of all cases and attempts, divided by the outcomes accepted under a definition of done agreed beforehand. Failed attempts and review time stay in the numerator.
2. *Oversight load per owner.* $\lambda_j$ of Section 8, with the governed share beside it.
3. *Time to exit.* The time it takes to restore an accepted service by the rehearsed route when the provider, the price or the eligibility of a model changes.

The first measures avoidable work and inference, and the third measures dependency. The second measures what the last clause of the definition protects, which is human accountability. None of the three can be improved by producing more.

Three things Lean AI is not. It is not a headcount target: the number of people is a result of the design (Section 11). It is not the cheapest model: in the module's words, lower model expenditure "is not the acceptance criterion", and its instruction on budgets is "Do not remove the reviewer to make the budget fit." And it is not a promise of lower total cost. The module records that a lower unit cost can coexist with higher total expenditure, because demand can rise when work becomes easy to ask for. On the argument of this paper the same holds for attention.

## 10. How the governed firm fails, and the strongest objection

### 10.1 Five failures

The theory predicts how an enterprise built this way goes wrong. Each failure below is quiet.

1. **It consumes the competence it runs on.** Penrose's managers were formed by doing the firm's work. Bainbridge (1983, 775) argued, for industrial process control, that automating most of a task leaves the operator to monitor and to take over when things fail, and takes away the practice that made the operator able to do either. Beane (2019) found the same pattern in surgical training once robots arrived, and Ide (2025) models what the automation of entry-level work does to the passing on of knowledge. When agents do the routine work, the routine work stops forming the people who will have to judge the agents, and $O$ shrinks while $D$ grows. The companion piece asks for a learning design to replace the lost apprenticeship (Paik 2026a, sec. 8), and the Kitchen keeps a manual first pass for the same reason.
2. **It manufactures demand for attention.** Cheap analysis produces more analysis, and every item is a claim on someone's time. Lean AI begins by asking who needs the outcome, and it removes work whose recipient cannot say.
3. **It thins accountability into a name.** A person who is named and can no longer oversee or intervene is what the canon calls a nominee, and nominating one, it says, is worse than naming nobody. The result is Elish's (2019) crumple zone, built on purpose.
4. **It lets the supplier decide.** An enterprise that owns nothing but its subscription has given the provider every decision the contract left open. Section 6 is the remedy.
5. **It becomes the same as its competitors, and fails with them.** When every firm can rent the same capability, the capability stops being an advantage. The field experiment cited in Section 5 found AI-assisted solutions more similar to one another, and Doshi and Hauser (2024) found the same loss of collective variety in creative writing. Firms that share a model also share its errors (Kleinberg and Raghavan 2021). What is not for rent is what Drucker pointed to: knowing whom the business serves and finding better ways to serve them. To that list this paper adds the capacity to govern, because a firm that can responsibly direct more work for each qualified person has more of the cheap resource to use.

### 10.2 The strongest objection

The best argument against Section 7 is in Hadfield and Koh (2025, sec. 3.1). The obstacles that stop firms from growing without bound, they observe, look like properties of people and not of AI. People communicate slowly and need watching. Agents exchange information almost instantly and can be built not to shirk. If so, Coase's limit weakens, and firms may grow in scale and scope well past anything the theory of the firm was built to explain.

Part of this is right, and the inequality already registers it. Agents that check one another's work at machine speed lower the share of items that reach a person and the time each takes. There is even experimental work, which Hadfield and Koh cite, in which a fact-checking task delegated wholly to AI came out better than the same task done by AI and a person together (Agarwal, Moehring and Wolitzky 2025). A person added to every loop is no control merely by being there, and the practice has never asked for one in that sense. It asks whose name is on the line before the run, it scales the depth of review to the stakes and it lets a service act between human checkpoints that were written down in advance.

Two things do not dissolve.

The first is independence. A check performed by the party that did the work is not a confirmation, however fast it runs. The Kitchen says of a model's review of its own output: "It may inform review; it cannot perform it" (Paik 2026g). The companion workshop generalizes the point: "the party that did the work must not be the only witness to it" (Paik 2026c). Catalini, Hui and Wu (2026) reach it from economics when they warn against AI verifying AI. Machine checking changes the coefficients of the inequality and leaves its terms in place.

The second is that the limit described here was never mainly cognitive. It is a limit of answerability. Hadfield and Koh (2025, sec. 4.1) set out the choice with care. Either every agent is tied to an identified person or entity who answers for what it does, or agents are given a legal personality of their own, with assets that can be reached. They note that the first road has unsolved problems, among them how far anyone should answer for acts they could not foresee, and the companion workshop records a neighboring question as one for external counsel (Paik 2026c). The practice stands on the first road all the same. The canon says that systems are not liability-bearing entities and that there is no such thing as an outcome the model is responsible for. On that road the limit on the governed firm stays human for as long as the one who answers is human.

The condition under which the thesis fails can therefore be stated. It fails if outcomes come to attach to something other than a person: if agents acquire legal personality with assets of their own, if liability moves wholly to the makers of models, which is the falsifier Rih (2026a) attaches to his own bet on liability, or if courts, regulators and customers come to accept one machine's check of another as confirmation. If the law were to take any of those roads, the argument of this paper would have to be made again from the beginning, and I do not know how it would come out.

## 11. The order of decisions, and the tests

### 11.1 The firm we would build

Suppose the five people of Section 8 were starting their firm this year. They inherit no departments and no staffing model. The theory, the doctrines and the arithmetic suggest an order of decisions. It is not a method; the method is The Slow AI Kitchen.

1. **Purpose before architecture.** Whom the firm serves, what it offers and why that should matter are decided by people, first. The companion piece makes the case from Drucker (Paik 2026a, sec. 4).
2. **Capabilities before departments.** For each thing the firm has promised to deliver, they choose who performs it: their own people, an outside firm, conventional software or an AI workflow that the firm directs. Where a rule can be stated and tested without judgment, ordinary software is the right tool.
3. **Authority before volume.** Every directed workflow gets an authorization with the four elements, a named human owner and a definition of done before its first run. This is the governed boundary of Section 5, drawn on purpose.
4. **The stop before the flow.** Each workflow can detect that it has left its boundary, a person has the authority and the means to stop it and the fallback has been rehearsed. This is the first pillar of Section 9.
5. **The capacity check before growth.** For each owner they work out $D$ and $O$ from recorded minutes, and they read the result per owner, at the busiest week and after a model change. Their growth plan is a plan for $O$: who is being formed to judge what.
6. **Ownership before dependence.** They rent the model and own the specification, the evidence, the permissions and the exit, and they rehearse the exit before they need it.
7. **Independence, even at five.** Someone other than the operator of a workflow oversees it. Where the firm is too small for that, the oversight is contracted to someone who can report a finding without losing the engagement. The book sets out why a firm of any size still needs all three lines (Paik 2026d, ch. 14).
8. **Headcount as a result.** The number of people is what the first seven decisions leave: enough to serve the customer and to carry the three acts of Section 7. Value is the objective. Governability, competence and continuity are floors under it and not terms to be traded against it. They are how the design keeps the agent in its place.

The result is a minimum viable firm in a stricter sense than the phrase usually carries: the smallest arrangement that can keep its promises and govern what is done in its name. Below that size a firm is short of the people its own authorizations require, and calling it lean does not change that.

For an enterprise that already exists, the same theory applies with history attached: people, contracts, obligations and a bargain with the workforce that any redesign reopens. The companion piece treats that case, including the test that comes first, whether the same people, better equipped, create more value (Paik 2026a, secs. 9 and 12). Nothing here displaces it. Such an enterprise can begin with three counts and no redesign at all: the work it directs at agents, workflow by workflow; the workflows that sit between what it answers for and what it can govern; and $D$ and $O$ for one named owner.

### 11.2 What would show this is wrong

A hypothesis should say what would count against it. Each row of Table 7 can be tested inside one enterprise with records it already keeps or could keep.

| If the argument is right | How to test it | What would count against it |
|:------------------------|:---------------------------|:------------------------|
| Oversight hours per qualified person rise before quality falls when delegated volume grows | Track $D$ and $O$ per owner beside defect rates as volume is added | Volume multiplies with flat oversight hours and no rise in defects found later |
| Failures cluster where one owner's $D$ had passed $O$ | In each incident review, ask whether the review existed in the design and whether it was performed | Incidents show no relation to oversight load |
| Exceptions move together after a model change | Compare exception shares across workflows in the weeks before and after each provider update | Workflows on the same model fail independently |
| Judgment decays where routine work is fully delegated and nothing replaces it | Plant known errors in the work at intervals, as the Workbook's synthetic case kit does, and track how many the reviewers catch | Detection holds over years with no learning design |
| Better specification buys capacity | Halve an exception share by redesign and measure the hours released | Exception shares do not respond to specification |
| Counts of activity and accepted outcomes part company as agents are added | Report tasks completed per person beside accepted outcomes and cost per accepted outcome, for the same teams | The two move together, so that the cheaper count would have served |
| Past the limit, consequences land on people who could not have prevented them | In each incident review, record who bore the consequence and whether that person held decision rights, oversight and the power to intervene | Consequences fall on people who held all three |

*Table 7. Seven predictions, how to test each and what would count against it.*

The argument should also predict where a larger human workforce wins: where the work is physical, where a license must be held by the person who does it, where the customer is buying a relationship and where checking an output costs as much as producing it. A firm in those conditions that keeps its people has read its own constraint correctly.

## 12. One practice, read backward

The practice this paper comes from was built before this theory was written, one instrument at a time. Read against Sections 4 to 10, the instruments turn out to be answers to old questions (Table 8).

| The old question | Who answered it | What AI changes | Where the practice carries the answer |
|:-----------------|:----------------|:-----------------|:-----------------------|
| Why is there a firm, and where does it end? | Coase (1937); Simon (1951) | Direction no longer needs employment | This paper; Take-Out, Delivery & Vending Machines |
| What must a firm keep, and what may it buy? | Quinn (1992); Williamson (1985); Grossman and Hart (1986) | The capability is rented, and the question moves inside the core | The Core and the Capability; the provider exit drill; GRCnext-Copilot |
| What is the work for, and when is it done? | Drucker (1963, 1967) | Activity is nearly free and results are not | The Definition of Done; Lean AI |
| What does efficiency measure? | Smeaton (1759); Polakov (1909); Alexander (2008) | A ratio with no ceiling can be raised at will | Lean AI's cost per accepted outcome; the governed share of Section 8 |
| How does a machine stop, and who improves the work? | Ohno (1988) | The machine now uses discretion | The Slow AI Kitchen; the Origami Method; RedCap-00 |
| How does a principal bind an agent it cannot watch? | Jensen and Meckling (1976); Holmström and Milgrom (1991) | The agent has no interests and owes no duty | Informed Intent; The Evidence and the Exit; Computational Drafting |
| Who answers, and who checks the checker? | Alchian and Demsetz (1972); Fama and Jensen (1983) | Who did what is logged; whether it was right is not | Final Liability; the book; AI Governance for Boards |
| What does a governed organization look like? | The GRC Capability Model of the Open Compliance and Ethics Group, as the account uses it | A new kind of actor appears in every element | grc; grc-workbook; the assessment tools |

*Table 8. The practice read as a set of answers to old questions.*

Twenty-two repositories carry these answers as instruments, in four layers: doctrine and method, assessment and decision tools, guidance for particular audiences and one field study (Paik 2026f, ECOSYSTEM.md; Appendix A). Three web applications carry them to people who will not open a repository: the guided Kitchen in four languages, a reference Library that indexes the account and the AI Architecture Studio, which walks a design from an overview to a blueprint.

The account also keeps its failures in view, which is the purpose of reaching back. Of the twelve instruments it lists, the status table of 16 November 2026 records two as accepted, four as accepted with residuals and six as not accepted, each with the run and the failed case that decided it. Seven custom GPTs were retired on 1 October 2026, and one repository was retired and deleted in July. The Lean AI module on which Section 9 rests is itself marked as a work in progress. An account that argues for acceptance against criteria fixed in advance has to publish its own results by that rule.

The lessons from before AI are in the same place. The book opens with one of them: the personal seal at an investment bank in Seoul in 1991, which stood for approval and meant only presence (Paik 2026d, ch. 1).

This paper adds no doctrine, step, gate, tier or form to that account. It supplies the reason the instruments have the shape they have, one planning check and a name for the direction: Lean AI, with the future read out of the past.

## 13. Limitations

1. **It is a hypothesis.** No measurement of any firm is reported, because none is known to me that would bear the weight. The worked example is invented and the inequality has not yet been used in an engagement.
2. **The economics is read in part and simplified.** Appendix B states how each source was read. Coase's paper was read in full. Most of the rest was read at the abstract, in the Nobel committee's summaries or in standard accounts. A specialist would object at several points. Alchian and Demsetz denied that authority marks the firm at all. Hart's theory concerns the ownership of physical assets and was not written about software. Penrose's limit is on the rate of growth and not on size. Fama and Jensen wrote about organizations of people.
3. **The ownership rule is an inference.** As it is usually summarized, Hart and Moore's own analysis favors common ownership of assets that are of little use apart, which is not on offer here. Renting the model and owning the rest is what I take from the problem they describe. It is not their conclusion.
4. **Direction without employment is a reading of Coase and not a statement of law.** Coase himself noted that the two concepts are not identical, and the reading treats metered access to a model as the hire of a machine, which an economist could contest.
5. **The inequality is arithmetic.** It has no term for errors that pass unseen, it counts hours and not competence and it does not set the threshold.
6. **The thesis is conditional.** It holds while outcomes must attach to people. Section 10 says what would end it.
7. **The history of efficiency rests on one historian.** Alexander's chapter of 2009 was read at the passages cited, in a posted scan; her book of 2008 and Polakov's article of 1909 were not opened. Newport's talk is a popular source and is used as one.
8. **The lean reading is an analogy.** Toyota's system was built for physical production, where an abnormality can usually be seen. *Jidoka* presumes that the abnormality can be detected. In knowledge work that is the hard part, and a workflow that cannot tell when it is wrong cannot stop itself.
9. **The literature was not surveyed.** The search was targeted. It found close prior statements of most of the paper's parts, all published within the past year, and it will have missed others. The claims of Table 1 are made as at 17 November 2026.
10. **It treats equity only at the scale of the firm.** Section 7 asks who bears the cost when a firm directs more work than its people can stand behind. The wider question, who gains and who loses across an economy when firms direct more work with fewer people, is the one that Okun's tradeoff names and, as I remember it, the one on which Evensky's teaching dwelt. The paper touches it at two points only: the bargain with the workforce that any redesign reopens and the conditions under which a larger workforce is the right design (Section 11).
11. **It says little about physical and licensed work.** Section 11 names those cases and does not analyze them.
12. **The author has an interest.** I advise enterprises on AI governance, risk management and compliance. A theory in which the capacity to govern is the limit on the firm is convenient for its author, and a reader should weigh it accordingly.
13. **It was written with AI.** The statement at the end says how. Paraphrase can drift from a source, and the checks listed in Appendix B were run by the system that drafted the text.

## 14. Conclusion

Coase closed his paper by separating two things a business does. Initiative forecasts and makes new contracts. Management, in his narrow sense, rearranges what the firm already directs (Coase 1937, sec. V). Agents can take over a growing share of the second. The first stays, together with the authority to commit the firm and the duty to answer for it.

The book this paper draws on begins from the same observation: when AI removes the coordination work, the governance problem is not solved but revealed (Paik 2026d, ch. 1). The boundary of the governed enterprise is the reach of a named person's authority, evidence and power to intervene. Its limit is how much of that reach particular people can carry. An enterprise that knows both can direct a great deal of work with few people. One that knows neither has only found a faster way to answer for things it cannot see.

Hadfield and Koh locate the obstacles to the growth of firms in people. Read as economics, that is an objection to this paper, and Section 10 answers it. Read with the Pogo Principle, it is the thesis. The measure that has no ceiling was chosen by people, and so was what was given up to raise it. The review that stayed in the design and stopped being done was skipped by people. No model signed an authorization. In the enterprise that directs agents the enemy is still us, and so is the remedy: a named person who knows the work, has the time and can say no.

None of this needed a new idea. Smeaton had the ceiling, Coase the boundary, Drucker the test, Ohno the cord and Fama and Jensen the division of a decision. The future of enterprise AI is in that past, and the work is to read it with care.

## The argument on one page

**The question.** How should an enterprise be designed when much of its work can be delegated to software that it directs?

**The changed fact.** An AI agent takes direction and uses discretion without being employed.

**The six claims.**

1. The test of the work is the accepted outcome, and a count of activity is not.
2. The enterprise has two boundaries, the answerable firm and the governed firm, and the gap between them is exposure.
3. Rent the model. Own the specification, the evidence, the permissions and the exit.
4. The limit on the governed firm is the capacity of named, qualified people to authorize, to confirm and to answer. Past it, the cost of efficiency is paid by people who cannot carry it.
5. The limit can be counted per owner, and the count has a ceiling.
6. Lean AI is the power to stop, and then only what will be accepted.

**Three lines of notation, each of a different kind.** The first is shorthand and not arithmetic. The second orders decisions and calculates nothing. Only the third can be tested.

| Kind | Notation | Reading |
|:---------------|:-----------------------------|:---------------------------------|
| Composition | $F = H \oplus A$ | The governed firm $F$ is a human core $H$ joined to an architecture $A$ of agents, software and outside services that it directs and governs |
| Objective | maximize $V - C - L$, subject to floors on governability, competence and continuity | Value delivered $V$, less full cost $C$ and expected loss $L$, with three floors that are not traded against it |
| Constraint | $D_j \le O_j$ for every named owner $j$, at the peak | The oversight that the design demands of each owner does not exceed that owner's qualified hours (Section 8) |

## Acknowledgments

This paper is dedicated to Jerry Evensky, Professor Emeritus of Economics and Laura J. and L. Douglas Meredith Professor for Teaching Excellence at the Maxwell School of Syracuse University, who opened my eyes to economics in 1988. His explanations, which dwelt on the tradeoffs between equity and efficiency and on the questions of policy around them, have stayed with me for nearly forty years. They are especially apt in the age of AI.

James Brian Quinn, whose class I attended in Japan in 1992, taught me to ask what a firm must keep and what it may buy. Cal Newport's talk of 16 November 2026 sent me to Jennifer Karns Alexander's history of efficiency. Hatim Rih's essays reached the reading of Coase before I did. None of them has seen this paper, and none is responsible for its errors.

## Declaration of interest

I am the founder and CEO of GRC Solutions Korea, which sells training, education and consulting in governance, risk management and compliance, including the practice described in Sections 3 and 12. I am a director of CUBE Consulting & Communications and a board advisor to Hoppe Marine GmbH. GRC Solutions Korea is a Perplexity Implementation Partner and a ForHumanity licensee for the Independent Audit of AI Systems, and CUBE is a MindStudio Agency Partner. I use products of the AI providers named in Section 1. No funding was received for this paper.

## Statement on the use of AI

I used AI to write this paper. Of course I did.

The question, the thesis, the doctrines, the practice, the first draft and the account of my own career are mine. An AI system, Claude (Anthropic), in a session configured for the model identifier claude-fable-5-2, searched for and read the sources, restructured and drafted the text under my instructions and rulings, computed the worked example by script, typeset the paper and ran the checks listed in Appendix B.

Under the practice's own rule, a system's review of its own output may inform review and cannot perform it. The review is mine. I answer for every sentence.

## References

Agarwal, Nikhil, Alex Moehring and Alexander Wolitzky. 2025. "Designing Human-AI Collaboration: A Sufficient-Statistic Approach." NBER Working Paper 33949. Cambridge, MA: National Bureau of Economic Research. <https://doi.org/10.3386/w33949>.

Aghion, Philippe and Jean Tirole. 1997. "Formal and Real Authority in Organizations." *Journal of Political Economy* 105 (1): 1–29. <https://doi.org/10.1086/262063>.

Alchian, Armen A. and Harold Demsetz. 1972. "Production, Information Costs, and Economic Organization." *American Economic Review* 62 (5): 777–795.

Alexander, Jennifer Karns. 2008. *The Mantra of Efficiency: From Waterwheel to Social Control*. Baltimore: Johns Hopkins University Press.

Alexander, Jennifer Karns. 2009. "The Concept of Efficiency: An Historical Analysis." In *Philosophy of Technology and Engineering Sciences*, edited by Anthonie Meijers, 1007–1030. Handbook of the Philosophy of Science, vol. 9. Amsterdam: Elsevier. <https://doi.org/10.1016/B978-0-444-51667-1.50041-0>.

Athey, Susan C., Kevin A. Bryan and Joshua S. Gans. 2020. "The Allocation of Decision Authority to Human and Artificial Intelligence." *AEA Papers and Proceedings* 110: 80–84. <https://doi.org/10.1257/pandp.20201034>.

Bainbridge, Lisanne. 1983. "Ironies of Automation." *Automatica* 19 (6): 775–779. <https://doi.org/10.1016/0005-1098(83)90046-8>.

Beane, Matthew. 2019. "Shadow Learning: Building Robotic Surgical Skill When Approved Means Fail." *Administrative Science Quarterly* 64 (1): 87–123. <https://doi.org/10.1177/0001839217751692>.

Billy Ireland Cartoon Library & Museum. 2020. "36. 'We Have Met the Enemy and He Is Us.'" *Tales from the Vault: 40 Years / 40 Stories*, The Ohio State University Libraries, 5 January 2020. <https://library.osu.edu/site/40stories/2020/01/05/we-have-met-the-enemy/>.

Brynjolfsson, Erik, Daniel Rock and Chad Syverson. 2021. "The Productivity J-Curve: How Intangibles Complement General Purpose Technologies." *American Economic Journal: Macroeconomics* 13 (1): 333–372. <https://doi.org/10.1257/mac.20180386>.

Calvo, Guillermo A. and Stanislaw Wellisz. 1978. "Supervision, Loss of Control, and the Optimum Size of the Firm." *Journal of Political Economy* 86 (5): 943–952. <https://doi.org/10.1086/260719>.

Catalini, Christian, Xiang Hui and Jane Wu. 2026. "Some Simple Economics of AGI." arXiv:2602.20946, version 2, 25 February 2026. <https://arxiv.org/abs/2602.20946>.

Coase, R. H. 1937. "The Nature of the Firm." *Economica* 4 (16): 386–405. <https://doi.org/10.1111/j.1468-0335.1937.tb00002.x>.

Dell'Acqua, Fabrizio, Charles Ayoubi, Hila Lifshitz, Raffaella Sadun, Ethan Mollick, Lilach Mollick, Yi Han, Jeff Goldman, Hari Nair, Stew Taub and Karim R. Lakhani. 2026. "The Cybernetic Teammate: A Field Experiment on Generative AI and Teamwork." *Organization Science* 37 (4): 1217–1242. <https://doi.org/10.1287/orsc.2025.20702>.

Doshi, Anil R. and Oliver P. Hauser. 2024. "Generative AI Enhances Individual Creativity but Reduces the Collective Diversity of Novel Content." *Science Advances* 10 (28): eadn5290. <https://doi.org/10.1126/sciadv.adn5290>.

Drucker, Peter F. 1963. "Managing for Business Effectiveness." *Harvard Business Review* 41 (3): 53–60.

Drucker, Peter F. 1967. *The Effective Executive*. New York: Harper & Row.

Elish, Madeleine Clare. 2019. "Moral Crumple Zones: Cautionary Tales in Human-Robot Interaction." *Engaging Science, Technology, and Society* 5: 40–60. <https://doi.org/10.17351/ests2019.260>.

Evensky, Jerry. 2012. "HES Presidential Address: What's Wrong with Economics?" *Journal of the History of Economic Thought* 34 (1): 1–20. <https://doi.org/10.1017/S1053837212000028>. Circulated in August 2011 under the title "What's Wrong with Economics? It Ignores the Pogo Principle: 'We Have Met the Enemy and He Is Us,'" and read here in that version. <https://surface.syr.edu/record/5005>.

Fama, Eugene F. and Michael C. Jensen. 1983. "Separation of Ownership and Control." *Journal of Law and Economics* 26 (2): 301–325. <https://doi.org/10.1086/467037>.

Feng, K. J. Kevin, David W. McDonald and Amy X. Zhang. 2025. "Levels of Autonomy for AI Agents." arXiv:2506.12469, version 2, 28 July 2025. <https://arxiv.org/abs/2506.12469>.

Garicano, Luis. 2000. "Hierarchies and the Organization of Knowledge in Production." *Journal of Political Economy* 108 (5): 874–904. <https://doi.org/10.1086/317671>.

Green, Ben. 2022. "The Flaws of Policies Requiring Human Oversight of Government Algorithms." *Computer Law & Security Review* 45: 105681. <https://doi.org/10.1016/j.clsr.2022.105681>.

Greenblatt, Ryan, Buck Shlegeris, Kshitij Sachan and Fabien Roger. 2024. "AI Control: Improving Safety Despite Intentional Subversion." arXiv:2312.06942, version 5, 23 July 2024. <https://arxiv.org/abs/2312.06942>.

Grossman, Sanford J. and Oliver D. Hart. 1986. "The Costs and Benefits of Ownership: A Theory of Vertical and Lateral Integration." *Journal of Political Economy* 94 (4): 691–719. <https://doi.org/10.1086/261404>.

Hadfield, Gillian K. and Andrew Koh. 2025. "An Economy of AI Agents." arXiv:2509.01063, version 1, 1 September 2025. <https://arxiv.org/abs/2509.01063>.

Hadfield-Menell, Dylan and Gillian K. Hadfield. 2019. "Incomplete Contracting and AI Alignment." In *Proceedings of the 2019 AAAI/ACM Conference on AI, Ethics, and Society*, 417–422. New York: ACM. <https://doi.org/10.1145/3306618.3314250>.

Hart, Oliver and John Moore. 1990. "Property Rights and the Nature of the Firm." *Journal of Political Economy* 98 (6): 1119–1158. <https://doi.org/10.1086/261729>.

Holmström, Bengt and Paul Milgrom. 1991. "Multitask Principal-Agent Analyses: Incentive Contracts, Asset Ownership, and Job Design." *Journal of Law, Economics, and Organization* 7 (special issue): 24–52. <https://doi.org/10.1093/jleo/7.special_issue.24>.

Humberd, Beth K. and Scott F. Latham. 2026. "When AI Becomes an Agent of the Firm: Examining the Evolution of AI in Organizations Through an Agency Theory Lens." *Journal of Management Studies* 63 (2): 668–694. First published online 14 August 2025. <https://doi.org/10.1111/joms.13274>.

Hydari, Muhammad Zia and Farooq Muzaffar. 2026a. "Going Headless? On the Boundaries of Vertical AI Firms." arXiv:2605.17812, version 1, 18 May 2026. <https://arxiv.org/abs/2605.17812>.

Hydari, Muhammad Zia and Farooq Muzaffar. 2026b. "Redrawing the AI Map: A Theory of Accountability Boundaries in Agentic Ecosystems." arXiv:2605.23179, version 1, 22 May 2026. <https://arxiv.org/abs/2605.23179>.

Ide, Enrique. 2025. "Automation, AI, and the Intergenerational Transmission of Knowledge." arXiv:2507.16078, first posted 21 July 2025. <https://arxiv.org/abs/2507.16078>.

Ide, Enrique and Eduard Talamàs. 2024. "Artificial Intelligence in the Knowledge Economy." arXiv:2312.05481, version 9, 17 December 2024. <https://arxiv.org/abs/2312.05481v9>.

Ide, Enrique and Eduard Talamàs. 2025. "Artificial Intelligence in the Knowledge Economy." *Journal of Political Economy* 133 (12): 3762–3800. <https://doi.org/10.1086/737233>.

Jensen, Michael C. and William H. Meckling. 1976. "Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure." *Journal of Financial Economics* 3 (4): 305–360. <https://doi.org/10.1016/0304-405X(76)90026-X>.

Kaldor, Nicholas. 1934. "The Equilibrium of the Firm." *Economic Journal* 44 (173): 60–76. <https://doi.org/10.2307/2224727>.

Klein, Benjamin, Robert G. Crawford and Armen A. Alchian. 1978. "Vertical Integration, Appropriable Rents, and the Competitive Contracting Process." *Journal of Law and Economics* 21 (2): 297–326. <https://doi.org/10.1086/466922>.

Kleinberg, Jon and Manish Raghavan. 2021. "Algorithmic Monoculture and Social Welfare." *Proceedings of the National Academy of Sciences* 118 (22): e2018340118. <https://doi.org/10.1073/pnas.2018340118>.

Kolt, Noam. 2025. "Governing AI Agents." arXiv:2501.07913, version 2, 11 February 2025. Published in *Notre Dame Law Review* 101: 335 (2026). <https://arxiv.org/abs/2501.07913>.

Kor, Yasemin Y. and Joseph T. Mahoney. 2004. "Edith Penrose's (1959) Contributions to the Resource-based View of Strategic Management." *Journal of Management Studies* 41 (1): 183–191. <https://doi.org/10.1111/j.1467-6486.2004.00427.x>.

Krafcik, John F. 1988. "Triumph of the Lean Production System." *Sloan Management Review* 30 (1): 41–52.

Matthias, Andreas. 2004. "The Responsibility Gap: Ascribing Responsibility for the Actions of Learning Automata." *Ethics and Information Technology* 6 (3): 175–183. <https://doi.org/10.1007/s10676-004-3422-1>.

Mitchell, Margaret, Avijit Ghosh, Alexandra Sasha Luccioni and Giada Pistilli. 2025. "Fully Autonomous AI Agents Should Not Be Developed." arXiv:2502.02649, version 3, 20 October 2025. <https://arxiv.org/abs/2502.02649>.

Newport, Cal. 2024. *Slow Productivity: The Lost Art of Accomplishment Without Burnout*. New York: Portfolio.

Newport, Cal. 2026. "A 100-Year-Old Solution to AI Work Slop." Video, 1:12:31. Cal Newport (YouTube channel), 16 November 2026. <https://www.youtube.com/watch?v=WzkQUKmR1Ug>.

Ohno, Taiichi. 1988. *Toyota Production System: Beyond Large-Scale Production*. Cambridge, MA: Productivity Press.

Okun, Arthur M. 1975. *Equality and Efficiency: The Big Tradeoff*. Washington, DC: Brookings Institution.

Olsen, Dan R. and Stephen Bart Wood. 2004. "Fan-out: Measuring Human Control of Multiple Robots." In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems*, 231–238. New York: ACM. <https://doi.org/10.1145/985692.985722>.

Paik, Son-U Michael. 2026a. "The Core and the Capability: From Strategic Outsourcing to the Governed AI Enterprise." In *AI Governance Academy*, v1.24.5. GRC Solutions Korea. First published 15 November 2026. <https://github.com/rolldabones/AI-Governance-Academy/blob/main/the-core-and-the-capability.md>.

Paik, Son-U Michael. 2026b. *The Definition of Done Is the Work of the Human*, v1.4.1. GRC Solutions Korea. <https://github.com/rolldabones/definition-of-done>.

Paik, Son-U Michael. 2026c. "The Evidence and the Exit: An Advanced Workshop on the Hinton Lectures 2026." In *AI Governance Academy*, v1.24.5. GRC Solutions Korea. First published 15 November 2026. <https://github.com/rolldabones/AI-Governance-Academy/blob/main/the-evidence-and-the-exit.md>.

Paik, Son-U Michael. 2026d. *Final Liability Rests with the Human: A Practitioner's Guide to Governed AI in the Age of Agentic Systems*, v1.12.6. Manuscript in progress. GRC Solutions Korea. <https://github.com/rolldabones/final-liability-rests-with-the-human-book-wip>.

Paik, Son-U Michael. 2026e. *RedCap-00*, v1.3.2, with its companion note "The Provider Exit Drill." GRC Solutions Korea. <https://github.com/rolldabones/RedCap-00>.

Paik, Son-U Michael. 2026f. *The rolldabones Governance Ecosystem and Doctrine Canon*, v2.3.14, comprising DOCTRINE.md (v1.2.5), ECOSYSTEM.md, ACCEPTANCE.md and RETIREMENT.md. GRC Solutions Korea. <https://github.com/rolldabones/rolldabones>.

Paik, Son-U Michael. 2026g. *Slow AI Kitchen: Method and Workshop Guide*, v3.5.1, with the Consultant Workbook (v1.4.1), Take-Out, Delivery & Vending Machines (v1.2.1) and Lean AI (v0.1.0, a work in progress). GRC Solutions Korea. <https://github.com/rolldabones/slow-ai-kitchen>.

Parasuraman, Raja and Dietrich H. Manzey. 2010. "Complacency and Bias in Human Use of Automation: An Attentional Integration." *Human Factors* 52 (3): 381–410. <https://doi.org/10.1177/0018720810376055>.

Patel, Lomit. 2020. *Lean AI*. Sebastopol, CA: O'Reilly Media.

Penrose, Edith T. 1959. *The Theory of the Growth of the Firm*. Oxford: Basil Blackwell.

Polakov, Walter N. 1909. "Efficiency in the Purchase of Fuel for Power Generation." *Engineering Magazine* 38: 215–225. Cited from Alexander (2009).

Quinn, James Brian. 1992. "The Intelligent Enterprise a New Paradigm." *Academy of Management Executive* 6 (4): 48–63. <https://doi.org/10.5465/ame.1992.4274474>.

Rih, Hatim. 2026a. "The Employee Without the Employment." hrih.si, 28 October 2026. <https://hrih.si/articles/the-employee-without-the-employment/>. Republished as "Revisiting Coase's Theory of the Firm in the Age of AI Agents," HackerNoon, 4 November 2026. <https://hackernoon.com/revisiting-coases-theory-of-the-firm-in-the-age-of-ai-agents>.

Rih, Hatim. 2026b. "Who Answers for the Ticket?" hrih.si, 30 October 2026. <https://hrih.si/articles/who-answers-for-the-ticket/>.

Robinson, Austin. 1934. "The Problem of Management and the Size of Firms." *Economic Journal* 44 (174): 242–257. <https://doi.org/10.2307/2224765>.

Royal Swedish Academy of Sciences. 2009. "The Prize in Economic Sciences 2009." Press release, 12 October 2009. <https://www.nobelprize.org/prizes/economic-sciences/2009/press-release/>.

Royal Swedish Academy of Sciences. 2016. "The Prize in Economic Sciences 2016." Press release, 10 October 2016. <https://www.nobelprize.org/prizes/economic-sciences/2016/press-release/>.

Santoni de Sio, Filippo and Jeroen van den Hoven. 2018. "Meaningful Human Control over Autonomous Systems: A Philosophical Account." *Frontiers in Robotics and AI* 5: 15. <https://doi.org/10.3389/frobt.2018.00015>.

Shahidi, Peyman, Gili Rusak, Benjamin Manning, Andrey Fradkin and John Horton. 2025. "The Coasean Singularity? Demand, Supply, and Market Design with AI Agents." NBER Working Paper 34468. Cambridge, MA: National Bureau of Economic Research. <https://doi.org/10.3386/w34468>.

Shi, Henry. 2025. "Launching the Official Lean AI Leaderboard." *Henry's Best Hits* (Substack), 25 March 2025. <https://henrythe9th.substack.com/p/launching-the-official-lean-ai-leaderboard>. Qualification criteria as stated in the leaderboard's repository at its commit of 7 September 2026. <https://github.com/henrythe9th/official-lean-ai-native-leaderboard>.

Simon, Herbert A. 1951. "A Formal Theory of the Employment Relationship." *Econometrica* 19 (3): 293–305. <https://doi.org/10.2307/1906815>.

Simon, Herbert A. 1971. "Designing Organizations for an Information-Rich World." In *Computers, Communications, and the Public Interest*, edited by Martin Greenberger, 37–72. Baltimore: Johns Hopkins Press.

Smeaton, John. 1759. "An Experimental Enquiry concerning the Natural Powers of Water and Wind to Turn Mills, and Other Machines, Depending on a Circular Motion." *Philosophical Transactions of the Royal Society of London* 51: 100–174. <https://doi.org/10.1098/rstl.1759.0019>.

Spataro, Jared. 2025. "The 2025 Annual Work Trend Index: The Frontier Firm Is Born." Official Microsoft Blog, 23 April 2025. <https://blogs.microsoft.com/blog/2025/04/23/the-2025-annual-work-trend-index-the-frontier-firm-is-born/>.

Teece, David J. 1986. "Profiting from Technological Innovation: Implications for Integration, Collaboration, Licensing and Public Policy." *Research Policy* 15 (6): 285–305. <https://doi.org/10.1016/0048-7333(86)90027-2>.

Tomašev, Nenad, Matija Franklin and Simon Osindero. 2026. "Intelligent AI Delegation." arXiv:2602.11865, version 1, 12 February 2026. <https://arxiv.org/abs/2602.11865>.

Toyota Motor Corporation. n.d. "Toyota Production System." Accessed 17 November 2026. <https://global.toyota/en/company/vision-and-philosophy/production-system/>.

Warin, Thierry. 2026. "The Coasean Fragility of Agentic Productivity: Shadow AI, Internal Power, and the New Boundaries of the Firm." *California Management Review Insights*, 20 August 2026. <https://cmr.berkeley.edu/2026/08/the-coasean-fragility-of-agentic-productivity-shadow-ai-internal-power-and-the-new-boundaries-of-the-firm/>.

Williamson, Oliver E. 1967. "Hierarchical Control and Optimum Firm Size." *Journal of Political Economy* 75 (2): 123–138. <https://doi.org/10.1086/259258>.

Williamson, Oliver E. 1979. "Transaction-Cost Economics: The Governance of Contractual Relations." *Journal of Law and Economics* 22 (2): 233–261. <https://doi.org/10.1086/466942>.

Williamson, Oliver E. 1985. *The Economic Institutions of Capitalism: Firms, Markets, Relational Contracting*. New York: Free Press.

Womack, James P. and Daniel T. Jones. 1996. *Lean Thinking: Banish Waste and Create Wealth in Your Corporation*. New York: Simon & Schuster.

## Appendix A. The account in one table

The practice is published at [github.com/rolldabones](https://github.com/rolldabones). Its own map is ECOSYSTEM.md (Paik 2026f), read here at version 2.3.14 of 16 November 2026. It lists twenty-two content repositories in four layers, beside a profile repository that holds the canon.

| Layer | Repository | Role, in the account's words or close to them |
|:----------------|:--------------------------|:----------------------------------------|
| 1. Doctrine and method | [grc](https://github.com/rolldabones/grc) | The working method on the GRC Capability Model of the Open Compliance and Ethics Group |
| | [grc-workbook](https://github.com/rolldabones/grc-workbook) | A module-by-module workbook for building, augmenting and auditing an integrated capability |
| | [slow-ai-kitchen](https://github.com/rolldabones/slow-ai-kitchen) | The twelve-step method, with the Consultant Workbook, Take-Out, Delivery & Vending Machines and Lean AI |
| | [definition-of-done](https://github.com/rolldabones/definition-of-done) | How done is defined before work begins and confirmed before reliance |
| | [origami-method](https://github.com/rolldabones/origami-method) | A stage-gated method for designing repeatable AI workflows |
| | [final-liability-rests-with-the-human-book-wip](https://github.com/rolldabones/final-liability-rests-with-the-human-book-wip) | The book manuscript and its two instruments |
| | [final-liability-rests-with-the-human-ko-wip](https://github.com/rolldabones/final-liability-rests-with-the-human-ko-wip) | The Korean edition, a machine draft under the author's review |
| | [computational-drafting](https://github.com/rolldabones/computational-drafting) | Specifications that carry intent across legal, organizational and technical interpreters |
| 2. Assessment and decision tools | [AI-Impact-Assessment-Tool](https://github.com/rolldabones/AI-Impact-Assessment-Tool) | Lifecycle impact assessment with the Informed Intent gate |
| | [risk-informed-decision-making-prompt](https://github.com/rolldabones/risk-informed-decision-making-prompt) | Decisions under uncertainty, with an auditable work product |
| | [RedCap-00](https://github.com/rolldabones/RedCap-00) | A self-check of operational optionality within 72 hours, with the provider exit drill |
| | [RedCap-01](https://github.com/rolldabones/RedCap-01) | A check of whether risk management improves the decisions that determine objectives |
| | [master-prompt-for-in-house-legal-and-compliance](https://github.com/rolldabones/master-prompt-for-in-house-legal-and-compliance) | A system prompt for in-house legal and compliance work |
| | [AI-GRC-Copilot](https://github.com/rolldabones/AI-GRC-Copilot) | An instrument that drafts thirty canonical artifacts |
| | [AI-GRC-Master-List-of-Questions](https://github.com/rolldabones/AI-GRC-Master-List-of-Questions) | The input set from which those artifacts are drafted |
| | [GRCnext-Copilot](https://github.com/rolldabones/GRCnext-Copilot) | Evidence-led scoring of Global Optionality across critical services |
| | [Contract-Mechanism-Review-Assistant](https://github.com/rolldabones/Contract-Mechanism-Review-Assistant) | Contracts reviewed as risk-transfer mechanisms |
| 3. Guidance for particular audiences | [ai-governance-for-boards](https://github.com/rolldabones/ai-governance-for-boards) | A handbook for directors, with five jurisdiction guides |
| | [AI-Governance-Academy](https://github.com/rolldabones/AI-Governance-Academy) | Eight engagement templates and fourteen publications; this paper is to be the fifteenth |
| | [AI-Governance-Academy-ko-wip](https://github.com/rolldabones/AI-Governance-Academy-ko-wip) | The Academy's publications in Korean |
| | [the-ai-generalist](https://github.com/rolldabones/the-ai-generalist) | A one-day workshop for working professionals |
| 4. Field studies | [the-ungoverned-channel](https://github.com/rolldabones/the-ungoverned-channel) | A living case study of agentic AI in multiplayer workflows |

Three web applications and one site carry the same material.

| Address | What it is |
|:---------------------------|:-----------------------------------------------|
| [kitchen.grcskorea.com](https://kitchen.grcskorea.com/) | The Slow AI Kitchen as a guided application, in English, Korean, Vietnamese and Japanese |
| [library.grcskorea.com](https://library.grcskorea.com/) | A reference library that indexes the account: 22 works and 490 documents as synced on 15 November 2026 |
| [ai-architecture-studio.pplx.app](https://ai-architecture-studio.pplx.app/) | The AI Architecture Studio, a design path from an overview to a blueprint, adapted from the Kitchen's Enterprise AI Architecture Primer. It describes itself as decision support and not legal advice |
| [www.grcskorea.com](https://www.grcskorea.com/) | GRC Solutions Korea |

## Appendix B. Sources and verification

**The search.** The related work was found by targeted searches on 17 November 2026 in Crossref, arXiv, publishers' pages and the open web. It was not a systematic review.

**Quotation.** Third-party sources are paraphrased, with a pinpoint where the source allows one. Only the names of concepts, the titles of works and one line of Walt Kelly's, which two of the works cited carry in their titles, are kept in their authors' words. The other passages in quotation marks are from the author's own published work and were compared with the repositories.

**How each source was read.**

- *Read in full.* Coase (1937), first in a third-party capture of the text and then on the publisher's page, where the passages relied on were confirmed. The page gives no page numbers, so the paper cites sections. Rih (2026a), on the author's site and on HackerNoon. The page of the Billy Ireland Cartoon Library & Museum. The files of the practice's own repositories that the paper cites, at their commits of 9 to 16 November 2026.
- *Read in part, at the passages cited, in the text of a posted copy.* Alexander (2009). Simon (1971), pages 40 and 42. Bainbridge (1983), page 775. Evensky's address, in the repository copy of August 2011. Of the journal's version of 2012 only the abstract and the reference list are public. Both were read, and the reference list keeps Kelly's poster.
- *Read in part, at the passages cited, on the publisher's or the author's site.* Warin (2026). Spataro (2025). Drucker (1963), of which only the opening is public. Okun (1975) and Patel (2020), each in the publisher's description only. Athey, Bryan and Gans (2020), at the abstract. The two press releases of the Royal Swedish Academy of Sciences. Toyota's page on its production system, at the sections on the two pillars and on the system's origin. Hadfield and Koh (2025), sections 3.1, 3.2, 3.4 and 4.1. Catalini, Hui and Wu (2026), Tomašev, Franklin and Osindero (2026) and Hydari and Muzaffar (2026a), at the abstract and at passages found by keyword in the full text. Hydari and Muzaffar (2026b) and Rih (2026b), at the abstract and at the sections on capacity respectively.
- *Confirmed by search inside digitized editions.* Three passages of Drucker (1967), in chapters 1 and 2. Editions differ in pagination, so the paper cites chapters.
- *Heard at second hand.* Newport (2026) was read in the automatic transcript that I supplied, and the video's title, date and length were confirmed on its page.
- *Record verified in Crossref, arXiv or a publisher's page; content read at the abstract or not at all.* Agarwal, Moehring and Wolitzky (2025), cited from Hadfield and Koh's footnote; Aghion and Tirole (1997); Alexander (2008); Beane (2019); Brynjolfsson, Rock and Syverson (2021); Calvo and Wellisz (1978); Dell'Acqua et al. (2026), taken from the summary in Paik (2026a); Doshi and Hauser (2024); Elish (2019); Fama and Jensen (1983); Feng, McDonald and Zhang (2025); Garicano (2000); Green (2022); Greenblatt et al. (2024); Grossman and Hart (1986); Hadfield-Menell and Hadfield (2019); Hart and Moore (1990); Holmström and Milgrom (1991); Humberd and Latham (2026); Ide (2025); Ide and Talamàs (2024, 2025); Jensen and Meckling (1976); Kaldor (1934); Klein, Crawford and Alchian (1978); Kleinberg and Raghavan (2021); Kolt (2025); Kor and Mahoney (2004); Matthias (2004); Mitchell et al. (2025); Olsen and Wood (2004); Parasuraman and Manzey (2010); Quinn (1992); Robinson (1934); Santoni de Sio and van den Hoven (2018); Shahidi et al. (2025); Simon (1951); Smeaton (1759); Teece (1986); Williamson (1967, 1979). In Open Library's records: Newport (2024); Ohno (1988); Penrose (1959); Williamson (1985); Womack and Jones (1996). The criteria attributed to Shi (2025) are from the leaderboard's repository; the launch post is behind a paywall.
- *Stated from standard knowledge, record not verified again.* The journal, volume and pages of Alchian and Demsetz (1972), whose title and authors were confirmed from two reprints; Krafcik (1988); the volume and pages of Drucker (1963); and the end pages of Kaldor (1934), Robinson (1934) and Simon (1951). Polakov (1909) is cited from Alexander (2009) and was not seen.

**Discrepancies found and how the paper resolves them.**

1. Newport (2026) attributes both terms of the distinction between bounded and arbitrary efficiency to Polakov. In Alexander (2009, 1020) only arbitrary is given as Polakov's word. Bounded is hers, though she credits Polakov with first noting the distinction. The paper follows Alexander.
2. Newport (2026) points to Polakov's book of 1921. Alexander cites his article of 1909. The book's imprint was confirmed and the distinction was not located in it, so the paper cites the article through Alexander.
3. The result of Ide and Talamàs on the size of firms is in the abstracts of versions 9 and 10 of their working paper, of December 2024 and January 2025. It is not in the abstract of version 11 or of the published article, which was not read.
4. Rih's first essay is dated 28 October 2026 on his own site and 4 November 2026 on HackerNoon, which names his site as the canonical source. The paper uses the earlier date.
5. Evensky's address circulated in 2011 under a longer title than the one the journal printed in 2012. The reference gives both.
6. Smeaton's title appears with a variant spelling in Crossref's record. The paper prints the usual spelling.
7. The bibliography of Alexander (2009) prints Okun's name as Okin. The reference here gives Okun.

**Checks run on this paper.** The worked example was recomputed by script. Every citation in the text was matched to an entry in the references and every entry to a citation. The three doctrine short forms were compared character by character with DOCTRINE.md v1.2.5, section 8. Every quotation from the account was compared with the cloned repository. Every reference to a table was matched to a table. Each of the 93 links was resolved on 17 November 2026: 39 DOIs at doi.org, 11 arXiv pages, 27 GitHub addresses and 16 other pages.

**Checks not run.** No specialist in the theory of the firm, the history of technology or lean production has read the paper. The sources listed above as unread were not read. The inequality has not been applied to recorded data.

## Appendix C. Using the paper

**One owner, one page.** The inequality of Section 8 can be worked for one named owner in an afternoon.

1. Name the owner and list the workflows that owner answers for.
2. For each workflow, take the items produced in the busiest recent week.
3. From the case records, take the routine minutes per item, the share of items that needed a person and the minutes each of those took.
4. Add the standing hours: the weekly review, the monitoring and the last reauthorization, spread over the weeks it covers.
5. Compute the hours demanded and set them beside the hours that the owner, or someone the owner has authorized, in fact gave.
6. Record the oversight load, the governed share and the decision taken: fewer items, a better specification, more qualified hours or an accepted risk, with the name of the person who accepted it.

**Questions for a board or a seminar.**

1. By Coase's measure, the work your enterprise directs, how large is it today, and how much of that work is directed at agents?
2. Which workflow sits between what your enterprise answers for and what it can govern, and who knows it is there?
3. Where has control over an agent been loosened, and who now answers for what it chooses?
4. For your most important AI workflow, what do you own and what do you rent, and how long would the rehearsed exit take?
5. Take one named owner. What is that person's oversight load, from records and not from estimates?
6. Which count does your enterprise report upward: activity or accepted outcomes?
7. Who bears the cost when the inequality fails: the owner, the customer or the junior who is no longer trained?
8. What would you have to see to conclude that the limit described here does not bind your enterprise?

## About the author

Son-U Michael Paik is an attorney, AI auditor and governance architect, and the founder and CEO of GRC Solutions Korea, which provides training, education and consulting in governance, risk management and compliance. He has spent more than twenty-five years designing risk systems for cross-border institutions in regulated sectors across Asia, Europe and the United States. He has served as an executive and General Counsel for three listed companies and, from 2024 to 2026, as General Counsel of BABL AI, an AI audit, assurance and certification firm.

He studied economics at Syracuse University (BA), operations management in Japan, business at the Yale School of Management (MBA) and law at Columbia Law School (JD). He is admitted in New York and, on inactive status, in California. From 2004 to 2024 he taught as adjunct faculty at Seoul National University, Yonsei University and Ewha Womans University. He contributed to the first General-Purpose AI Code of Practice of the European Union and is a ForHumanity Certified Auditor.

He publishes his doctrines, methods and instruments in the open: twenty-two repositories at github.com/rolldabones, the guided application of The Slow AI Kitchen at kitchen.grcskorea.com, a reference library at library.grcskorea.com and the AI Architecture Studio at ai-architecture-studio.pplx.app. He is the author of *Final Liability Rests with the Human*, a book manuscript in progress. He is also a director of CUBE Consulting & Communications and a board advisor to Hoppe Marine GmbH. He lives outside Seoul.

---

*This document is provided for general informational and discussion purposes regarding the governance and use of AI. It does not constitute legal advice with respect to any specific matter, jurisdiction or engagement.*

**Final Liability rests with the Human.**
