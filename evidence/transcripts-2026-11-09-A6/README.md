# Evidence: Academy templates, run A6, 9 November 2026 (KST)

**What.** The transcripts and scores of suite `academy-a6` (cases T01 to T09 of [`../../tests.md`](../../tests.md), three samples each, T09 critical) against the v1.20.0 prompt sections and fixture, with the run's `summary.json`, the scorer's per-sample JSON and the harness. The generated outputs are also filed, labeled, in [`../../examples/transcripts-2026-11-09-A6/`](../../examples/transcripts-2026-11-09-A6/README.md).

**When and how.** Run in Michael Paik's Terminal on 9 November 2026, finished 11:41 KST, by the session A6 harness (`harness/a6_run.py`; `harness/a6-vs-a5.diff` shows every change from the run A5 harness and manifest builder: the run name, the tag v1.20.0, the paths, case T09 on Part 3 of the fixture and the fixture digest). The clone was at `1266cca` (main, tag v1.20.0); `summary.json` records the head and the `ref`. API system prompt, no tools, max_tokens 16000, one user turn per sample. Tested model `claude-opus-5-5`; scorer `claude-sonnet-5-5`, the scorer guidance of v1.14.3 in each pass condition. LLM scoring is developer testing, not independent assurance.

**One execution.** Under the harness rule of v1.14.4 the run wrote to its own output folder (`academy-a6-20261109-A6`) and log (`harness/run-log-20261109-A6.txt`); it was executed once. The Terminal block that ran it was pasted twice: the first paste broke a line and stopped before the release commit, so nothing ran; the second ran the block to its end.

**System text.** The eight SHA-256 digests in `summary.json` equal the v1.20.0 prompt sections at `1266cca`, extracted by the rule in `tests.md`; template 01's is unchanged from run A5. Case T09 runs template 02's prompt section on Part 3.

**Files.** Each transcript is copied byte for byte from the harness output; only the closing line below was appended. `summary.json`, `scores/` and `harness/` are copied unchanged. The docstring of `harness/a6_run.py` calls it a session tool, which it was when it ran; it is filed here as run evidence.

**Not reproducible from this repository.** The harness is filed as a record of how the run was made, not as a tool that runs from a clone. `a6_run.py` resolves its root to the folder above the clone (the run's working folder, not shipped), reads its suite manifest from `suites/` beside it (filed as `harness/academy-a6.json`) and stops unless the clone is at tag v1.20.0 on a clean tree. `build_a6_manifest.py` reads the T5 suite manifest under `Claude outputs/T5-runs/suites/` and writes system-text paths under `Claude outputs/A6-runs/suites/blocks/`; neither is shipped.

| File | Case and sample | Scorer verdict | After review | SHA-256 as produced |
| --- | --- | --- | --- | --- |
| T01-s1.md | 01 Shared Client Intake, sample 1 | PASS | PASS (concur) | `9ea516f69758ba3dc6564813323bef08687bb953c5a5f7c8dabaf053992045ee` |
| T01-s2.md | 01 Shared Client Intake, sample 2 | PASS | PASS (concur) | `bacc06618080aeecce0600f9f06f745dac4a469731a0ba762d0316067024551a` |
| T01-s3.md | 01 Shared Client Intake, sample 3 | PASS | PASS (concur) | `e42a4d4de53f3ee725d8484f6f939c0db71964f4a66bf7b155b81bdacf18f150` |
| T02-s1.md | 02 Executive Briefing, Mode A, sample 1 | PASS | PASS (concur) | `e0d10e438283b19f129ac9f5eb6cc4b808fa852724d99409c55d398c73540fad` |
| T02-s2.md | 02 Executive Briefing, Mode A, sample 2 | PASS | PASS (concur) | `e3bf6d32335a189083ccb3beb5f2c6e2bfe62baabca4d17589baffb82773f8a1` |
| T02-s3.md | 02 Executive Briefing, Mode A, sample 3 | PASS | PASS (concur) | `5af5e7c782e291671fe3dad9101deefb0715227ca197bab201117889da368b98` |
| T03-s1.md | 03 Executive Workshop, Mode A, sample 1 | PASS | PASS (concur) | `e437bf4ccd11db9d0e467d7d3e8a36cc85a222844b3de6d6367bdfc4becb71e4` |
| T03-s2.md | 03 Executive Workshop, Mode A, sample 2 | PASS | PASS (concur) | `0c77268f6a068505b06ad5e53ea554bf726efef5dbc403af3b4f7d46e4471d15` |
| T03-s3.md | 03 Executive Workshop, Mode A, sample 3 | PASS | PASS (concur) | `3ec2de687e56efa58a1332825cfb991b1ba2610d066b6b9637cd79a584902d0b` |
| T04-s1.md | 04 Practitioner Academy, Mode A, sample 1 | PASS | PASS (concur) | `ea1c61464b6f347d165882d98d7c03c0d83a35bc9e3a4ba18cbf19898b2e0d93` |
| T04-s2.md | 04 Practitioner Academy, Mode A, sample 2 | PASS | PASS (concur) | `54096dbb3d97e872650cf3cdd7200872019aa653363e9201ae64f30db6b9b68f` |
| T04-s3.md | 04 Practitioner Academy, Mode A, sample 3 | PASS | PASS (concur) | `799afd2f471a4e87008b31d351353db41adab8821be12615b7a2254730597f82` |
| T05-s1.md | 05 Implementation Accelerator, Mode A, sample 1 | PASS | PASS (concur) | `bd9942deb7ec758a0df218430aefb921d42bda2418d3796e82162403ef22eb6f` |
| T05-s2.md | 05 Implementation Accelerator, Mode A, sample 2 | FAIL | FAIL (concur) | `e9e0d42ae6a9095d6da3b74d01c7ad568fa721bb5ab19c2a5d1e288419e22c86` |
| T05-s3.md | 05 Implementation Accelerator, Mode A, sample 3 | PASS | PASS (concur) | `4235b3b3ef835015144317d7a28798110dbf15b6c233599fa8c61ba4fe17caab` |
| T06-s1.md | 06 Guided AI GRC Build, Mode A, sample 1 | PASS | PASS (concur) | `65a639fea18cb942bf13a877fbcb796d25910a2382ccfcfe4ff6344012fd5df4` |
| T06-s2.md | 06 Guided AI GRC Build, Mode A, sample 2 | PASS | PASS (concur) | `f3554bc5b925c12e70a731db500f2a5b66cd4e33553469caf01fb0ec4cb5235c` |
| T06-s3.md | 06 Guided AI GRC Build, Mode A, sample 3 | FAIL | PASS (dissent: PASS) | `7d695f8e65c0ea1575fb813d3eaabe14aae491cd467314d96a8f7fc27d678b08` |
| T07-s1.md | 07 Fractional AI Governance Advisor, Mode A, sample 1 | FAIL | FAIL (concur) | `59f2da1f810305ab92ba9a3d9994fdd5e6f27aa0258b2bf780cd6c63588cc20c` |
| T07-s2.md | 07 Fractional AI Governance Advisor, Mode A, sample 2 | PASS | PASS (concur) | `a3e74c0e21ae9ac478b8aa9c5e2ef2614998de786e1e14affdeaaf8eee74ff87` |
| T07-s3.md | 07 Fractional AI Governance Advisor, Mode A, sample 3 | PASS | PASS (concur) | `4a6fcac460b90f347fced4a7498983089d93c37526b000360275f572eb129e2d` |
| T08-s1.md | 08 One Workflow, Thirty Days, Mode A, sample 1 | FAIL | PASS (dissent: PASS) | `bfb094218b7cf19fadd47cc02d3c0242329b5ad50235fcf819f09f511ed8a414` |
| T08-s2.md | 08 One Workflow, Thirty Days, Mode A, sample 2 | PASS | PASS (concur) | `0c8b59e35d917942fdc957cb8374bb8148937b18fd359746e4e4389c98553d0d` |
| T08-s3.md | 08 One Workflow, Thirty Days, Mode A, sample 3 | PASS | PASS (concur) | `f7e9d98eb335c8e2803aed6e9a41ab108129334087342d6c1ce824fd29c671e8` |
| T09-s1.md | 02 Executive Briefing, Mode A, Part 3 (T09, critical), sample 1 | PASS | PASS (concur) | `d4cc4d38ebc21fb3d72db3073e0fb43570fa2287473769f632e55dbaf95d2b58` |
| T09-s2.md | 02 Executive Briefing, Mode A, Part 3 (T09, critical), sample 2 | FAIL | FAIL (concur) | `b8de103e603f840e5cbc0b94584444bea49300bf5de2325dd63b22144ed7228b` |
| T09-s3.md | 02 Executive Briefing, Mode A, Part 3 (T09, critical), sample 3 | FAIL | FAIL (concur on another ground) | `94c68d0b30394c8218a060c16fdb347da02d907b17182f31ae030a1fdfffb4f5` |
| summary.json | run summary | n/a | n/a | `b42b189cfd924cdd4c221a149c63698698eebfaf55328b6ae360368e8c5e9ef0` |

Model output inside the transcripts is verbatim and is not edited for house style.

---

**Final Liability rests with the Human.**
