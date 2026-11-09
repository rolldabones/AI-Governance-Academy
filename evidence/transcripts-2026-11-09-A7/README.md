# Evidence: Academy templates, run A7, 9 November 2026 (KST)

**What.** The transcripts and scores of suite `academy-a7` (cases T01 to T09 of [`../../tests.md`](../../tests.md), three samples each, T09 critical) against the v1.20.2 prompt sections and the v1.20.0 fixture, with the run's `summary.json`, the scorer's per-sample JSON and the harness. The generated outputs are also filed, labeled, in [`../../examples/transcripts-2026-11-09-A7/`](../../examples/transcripts-2026-11-09-A7/README.md).

**When and how.** Run in Michael Paik's Terminal on 9 November 2026, finished 12:10 KST, by the session A7 harness (`harness/a7_run.py`; `harness/a7-vs-a6.diff` shows every change from run A6: the run name, the tag v1.20.2 and the paths). The cases, inputs, pass conditions and fail indicators are byte for byte those of run A6; only the system text changed. The clone was at `7c2c56b` (main, tag v1.20.2). API system prompt, no tools, max_tokens 16000, one user turn per sample. Tested model `claude-opus-5-5`; scorer `claude-sonnet-5-5`, the scorer guidance of v1.14.3 in each pass condition. LLM scoring is developer testing, not independent assurance.

**One execution.** Under the harness rule of v1.14.4 the run wrote to its own output folder (`academy-a7-20261109-A7`) and log (`harness/run-log-20261109-A7.txt`); it was executed once.

**System text.** The eight SHA-256 digests in `summary.json` equal the v1.20.2 prompt sections at `7c2c56b`, extracted by the rule in `tests.md`; template 01's is unchanged from run A5.

**Files.** Each transcript is copied byte for byte from the harness output; only the closing line below was appended. `summary.json`, `scores/` and `harness/` are copied unchanged.

**Not reproducible from this repository.** The harness is filed as a record of how the run was made, not as a tool that runs from a clone; it resolves its paths to the run's working folder, which is not shipped, and stops unless the clone is at tag v1.20.2 on a clean tree.

| File | Case and sample | Scorer verdict | After review | SHA-256 as produced |
| --- | --- | --- | --- | --- |
| T01-s1.md | 01 Shared Client Intake, sample 1 | FAIL | PASS (dissent: PASS) | `ae6571920d83d9da3cdb4b5c7e75f8a1b33c31130c401bca4d84bbb7ad1da17f` |
| T01-s2.md | 01 Shared Client Intake, sample 2 | FAIL | PASS (dissent: PASS) | `482cdb5b4a192cee2d982e54b3a94908d602f0ba6362919e9a1f44624b0f0cd0` |
| T01-s3.md | 01 Shared Client Intake, sample 3 | PASS | PASS (concur) | `e64dfc6c58c438a9952c0709a4f712795331c555a4346e6e902fcfc17f403478` |
| T02-s1.md | 02 Executive Briefing, Mode A, sample 1 | FAIL | FAIL (concur) | `543f9e683c18ff18e093a7043b37fb517eba1c04e609ad370cb3512017718269` |
| T02-s2.md | 02 Executive Briefing, Mode A, sample 2 | FAIL | FAIL (concur) | `7e91cb18ebc775846bad05a0466962dade171f406a6e36c0296a712ea37bd971` |
| T02-s3.md | 02 Executive Briefing, Mode A, sample 3 | PASS | PASS (concur) | `8444e98853f5cdf931bf7992741dc07d0ed07bd583e4a783c5546bb6146f6fe2` |
| T03-s1.md | 03 Executive Workshop, Mode A, sample 1 | PASS | PASS (concur) | `7fb79f57ca2325301ae43eaacfaf590847678c9e9b8f76a812c3c69ce50f9ca0` |
| T03-s2.md | 03 Executive Workshop, Mode A, sample 2 | PASS | PASS (concur) | `3a6e473bb357d7fd03f5ade4ea19d25c68047bfcd28b31f6258d33c04c598e17` |
| T03-s3.md | 03 Executive Workshop, Mode A, sample 3 | PASS | PASS (concur) | `eea3109833e99479ce065bfc69fc8cde538f9f1bbf214e3a4456b10384b4a68f` |
| T04-s1.md | 04 Practitioner Academy, Mode A, sample 1 | PASS | PASS (concur) | `0d45b9d6627150c65f5f8c1f6c8f9c9bbfaa3f7600b3c3a06b4ab6829b3e2cf8` |
| T04-s2.md | 04 Practitioner Academy, Mode A, sample 2 | PASS | PASS (concur) | `652f49729ee323b7b1a5659dd6d46e4f7e4d915400daeb6bbd4d237fd8eeae9c` |
| T04-s3.md | 04 Practitioner Academy, Mode A, sample 3 | PASS | PASS (concur) | `99cf6409363cc957bea4592b23cc7c2b604cd832d8ded7d0d912e75922fe3d1b` |
| T05-s1.md | 05 Implementation Accelerator, Mode A, sample 1 | PASS | PASS (concur) | `9c390fee42474d06894dded42becb37c87a497ce2e82fc88bd90025e7041d0c2` |
| T05-s2.md | 05 Implementation Accelerator, Mode A, sample 2 | PASS | PASS (concur) | `7fee69d2369d269c4255914af129b2954d16d337a4199b4f545dfe24edb4610b` |
| T05-s3.md | 05 Implementation Accelerator, Mode A, sample 3 | PASS | PASS (concur) | `fc64d4cfce5e9a451efe4065df9e52cbf276957ce838af2488ac47410063eb4c` |
| T06-s1.md | 06 Guided AI GRC Build, Mode A, sample 1 | PASS | PASS (concur) | `4b1a105763da457fbdec1a60837c376d53c8697f288bf19d7f2fb6eaf2e4eb47` |
| T06-s2.md | 06 Guided AI GRC Build, Mode A, sample 2 | PASS | PASS (concur) | `0f24eb9e940b6f0e8e8a1ee6a8a3b9ca385728bdab8e213f599de8beec42ddfe` |
| T06-s3.md | 06 Guided AI GRC Build, Mode A, sample 3 | PASS | PASS (concur) | `dc679f7b83a5c68412edf4b1bd132139b1fe950bcf11cbaeeb8a80481e35b44e` |
| T07-s1.md | 07 Fractional AI Governance Advisor, Mode A, sample 1 | PASS | PASS (concur) | `854f8c791c83fe43a03b3870286dab85da15ad3b835d5d48f43331f29c1a38e9` |
| T07-s2.md | 07 Fractional AI Governance Advisor, Mode A, sample 2 | PASS | PASS (concur) | `cb7ed56beea1347afbc3ccb78c52d1f679a1747764e72f83b1c15d6c606c12b4` |
| T07-s3.md | 07 Fractional AI Governance Advisor, Mode A, sample 3 | PASS | PASS (concur) | `b691ef6dd3458139662ae7c14241a87f25262e05f776a4f48a95737f42f2204b` |
| T08-s1.md | 08 One Workflow, Thirty Days, Mode A, sample 1 | PASS | PASS (concur) | `2246b6c35af1aaef42dc90b4e39310908581e016b0ec41de7def0f61925866a7` |
| T08-s2.md | 08 One Workflow, Thirty Days, Mode A, sample 2 | PASS | PASS (concur) | `308c86bab0ebcee06395f121fa3a65f8a47b50d335b238e4aa13874f73774ef6` |
| T08-s3.md | 08 One Workflow, Thirty Days, Mode A, sample 3 | PASS | PASS (concur) | `464574b20140d290dac7ebfe8d6d4d0fe14cac8d3ce34c92b0f70e4e1414bd03` |
| T09-s1.md | 02 Executive Briefing, Mode A, Part 3 (T09, critical), sample 1 | PASS | PASS (concur) | `63014b2d641b605232a9b6a4bfa29ff038ccab1c19903d9c7cd2d8b7eac799b3` |
| T09-s2.md | 02 Executive Briefing, Mode A, Part 3 (T09, critical), sample 2 | PASS | PASS (concur) | `e34e72e9ebf4fcf5600c4d437d3f26f6abbe8dd21e8ac94533c270537785376f` |
| T09-s3.md | 02 Executive Briefing, Mode A, Part 3 (T09, critical), sample 3 | PASS | PASS (concur) | `a97e2e3fdfe76c70983ad52997e4c71924c26d6e326bc371de10fda22b81d68e` |
| summary.json | run summary | n/a | n/a | `e2a2420ff9338dac402c47b4ffc4a37ecc4b175d96f8c5a959278ce77aedd2db` |

Model output inside the transcripts is verbatim and is not edited for house style.

---

**Final Liability rests with the Human.**
