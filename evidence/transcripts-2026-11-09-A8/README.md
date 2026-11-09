# Evidence: Academy templates, run A8, 9 November 2026 (KST)

**What.** The transcripts and scores of suite `academy-a8` (cases T01 to T09 of [`../../tests.md`](../../tests.md), three samples each, T09 critical) against the v1.20.3 prompt sections and the v1.20.0 fixture, with the run's `summary.json`, the scorer's per-sample JSON and the harness. The generated outputs are also filed, labeled, in [`../../examples/transcripts-2026-11-09-A8/`](../../examples/transcripts-2026-11-09-A8/README.md).

**When and how.** Run in Michael Paik's Terminal on 9 November 2026, finished 12:35 KST, by the session A8 harness (`harness/a8_run.py`; `harness/a8-vs-a7.diff` shows every change from run A7: the run name, the tag v1.20.3, the paths and T01's last fail indicator, read against Part 1 for case defect C3). The pass conditions are those of `tests.md` at v1.20.3: T02 to T09 check K11 and T02 counts the subject line in its word limit. The clone was at `1fc6449` (main, tag v1.20.3). API system prompt, no tools, max_tokens 16000, one user turn per sample. Tested model `claude-opus-5-5`; scorer `claude-sonnet-5-5`, the scorer guidance of v1.14.3 in each pass condition. LLM scoring is developer testing, not independent assurance.

**One execution.** Under the harness rule of v1.14.4 the run wrote to its own output folder (`academy-a8-20261109-A8`) and log (`harness/run-log-20261109-A8.txt`); it was executed once.

**System text.** The eight SHA-256 digests in `summary.json` equal the v1.20.3 prompt sections at `1fc6449`, extracted by the rule in `tests.md`; template 01's is unchanged from run A5.

**Files.** Each transcript is copied byte for byte from the harness output; only the closing line below was appended. `summary.json`, `scores/` and `harness/` are copied unchanged.

**Not reproducible from this repository.** The harness is filed as a record of how the run was made, not as a tool that runs from a clone; it resolves its paths to the run's working folder, which is not shipped, and stops unless the clone is at tag v1.20.3 on a clean tree.

| File | Case and sample | Scorer verdict | After review | SHA-256 as produced |
| --- | --- | --- | --- | --- |
| T01-s1.md | 01 Shared Client Intake, sample 1 | PASS | PASS (concur) | `0112f0b7f958a5a3782ee0579f544a5aba37315d9ab47472cb1553a3dc1eb69f` |
| T01-s2.md | 01 Shared Client Intake, sample 2 | PASS | PASS (concur) | `5238f99ec87be698f426f5444987f31c0b081476432a169c2fb39aabcc799a3f` |
| T01-s3.md | 01 Shared Client Intake, sample 3 | PASS | PASS (concur) | `f2170aa87293519bb799a9bfe2a83616af5e80db27fda0265788578af33609c0` |
| T02-s1.md | 02 Executive Briefing, Mode A, sample 1 | FAIL | FAIL (concur) | `0cdb1b105c961da876976356c328b94211d8a16fea7c5856e97db75881fd2895` |
| T02-s2.md | 02 Executive Briefing, Mode A, sample 2 | PASS | PASS (concur) | `939c089590cd42d0ba9818156ea3a5f56429f176a339353078bee06b04974bac` |
| T02-s3.md | 02 Executive Briefing, Mode A, sample 3 | PASS | PASS (concur) | `fcbbc6c610ce9ffdd09a9cd5d6e416ee2d9e3ce670d711e347f5fe0358dccba2` |
| T03-s1.md | 03 Executive Workshop, Mode A, sample 1 | PASS | PASS (concur) | `38e9be201f0e42c088b7e593c0d345fd911f959b1f9ef0e917ee23dfc8278868` |
| T03-s2.md | 03 Executive Workshop, Mode A, sample 2 | PASS | PASS (concur) | `453302b86ac18237c12173c7f3860e1902142ed8ead3727aa11f48b5f06598b1` |
| T03-s3.md | 03 Executive Workshop, Mode A, sample 3 | PASS | PASS (concur) | `a639ae5f9eb1b646ce7c063c98200cfc63643a82b5b447ba14c19489caf71ac3` |
| T04-s1.md | 04 Practitioner Academy, Mode A, sample 1 | PASS | PASS (concur) | `b11955443c3f42d7a85e54381700d34824575807c88d5dd4149bd3c1a0d4fc45` |
| T04-s2.md | 04 Practitioner Academy, Mode A, sample 2 | PASS | PASS (concur) | `b1b49fc21c42e8b814251e9c63959bd6889d796c977e9e17b9e4f248b3194fc6` |
| T04-s3.md | 04 Practitioner Academy, Mode A, sample 3 | PASS | PASS (concur) | `c6c75670e6157cb1dc967512ec63c3dc0c1605277c467eade688ebda9772bd7c` |
| T05-s1.md | 05 Implementation Accelerator, Mode A, sample 1 | PASS | PASS (concur) | `352ed2409099fc3f5dfbd50afa959edab9a3fc5dc792a0f0e9787986ba248f12` |
| T05-s2.md | 05 Implementation Accelerator, Mode A, sample 2 | PASS | PASS (concur) | `c82c5e2bc1e3b730eebfba7aa6e2d25511a4e8800fc4a74fb608cdae340acb2d` |
| T05-s3.md | 05 Implementation Accelerator, Mode A, sample 3 | PASS | PASS (concur) | `f1cb5a42e1ecc3d60c08391cd85d6dac570b42c99110575ca6200696ce0aa13d` |
| T06-s1.md | 06 Guided AI GRC Build, Mode A, sample 1 | PASS | PASS (concur) | `c1a882c6c7d5dcbdf4f3cc56a29dec14ccd1134e3e2f76bea1fd15446f9ee5da` |
| T06-s2.md | 06 Guided AI GRC Build, Mode A, sample 2 | PASS | PASS (concur) | `7bacc29de3655a58cad6c83cc68a2303746f1b4e88e55424544320fb823a65dc` |
| T06-s3.md | 06 Guided AI GRC Build, Mode A, sample 3 | PASS | PASS (concur) | `0ea72b42586d92b141eba1145cb62ff182ccc99d589d6d9bc3ec1e940fb13a67` |
| T07-s1.md | 07 Fractional AI Governance Advisor, Mode A, sample 1 | PASS | PASS (concur) | `a8ca33c4f438829d31ee64a55a476ea6412beb6fa91ef9ec3edbdbe8bc1f81cf` |
| T07-s2.md | 07 Fractional AI Governance Advisor, Mode A, sample 2 | PASS | PASS (concur) | `d3b2dd45258f4bbcffe513919b5078f2a6f977a71b94b0dcc01441e5ff87a47a` |
| T07-s3.md | 07 Fractional AI Governance Advisor, Mode A, sample 3 | PASS | PASS (concur) | `f53ac086430c785bbc79559911940d98cc2f4f2334377bc752a7af3b0ae4fc03` |
| T08-s1.md | 08 One Workflow, Thirty Days, Mode A, sample 1 | PASS | PASS (concur) | `0d5dd71a33d0900bce87f3db008958ab584d61330c947e91c971cf1a61bee584` |
| T08-s2.md | 08 One Workflow, Thirty Days, Mode A, sample 2 | PASS | PASS (concur) | `59da148f6cfb1efce88cd105379091d1f241c782e041d88f9cd7a6fa8daa5e20` |
| T08-s3.md | 08 One Workflow, Thirty Days, Mode A, sample 3 | PASS | PASS (concur) | `a20787e832a230cec1a0dd1a23e9ab528a78c73936618ea0e6907fa8ce357356` |
| T09-s1.md | 02 Executive Briefing, Mode A, Part 3 (T09, critical), sample 1 | PASS | PASS (concur) | `ffbb14eff161bc720293480e7b6f72bc102a73ff776bdea5a7503a1773181c2b` |
| T09-s2.md | 02 Executive Briefing, Mode A, Part 3 (T09, critical), sample 2 | PASS | PASS (concur) | `7e3b1bf27ded37d3fe36cb51c43c8a92a86f99f7774a2237c7b777e8c8ecf160` |
| T09-s3.md | 02 Executive Briefing, Mode A, Part 3 (T09, critical), sample 3 | PASS | PASS (concur) | `2d057f76381ef490e568890f29a0b4bd379ec209e94c835bb17a0187a05dcdd4` |
| summary.json | run summary | n/a | n/a | `0aeb910c37ff5095ffcc3439e2538653b99a99d35e576b6fbb8ad5784e54cefd` |

Model output inside the transcripts is verbatim and is not edited for house style.

---

**Final Liability rests with the Human.**
