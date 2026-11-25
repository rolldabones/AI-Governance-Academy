# Evidence: Academy templates, run A9, 25 November 2026 (KST)

**What.** The transcripts and scores of suite `academy-a9` (cases T01 to T09 of [`../../tests.md`](../../tests.md), three samples each, T09 critical) against the v1.28.0 prompt sections and the v1.20.0 fixture, with the run's `summary.json`, the scorer's per-sample JSON and the harness. The generated outputs are also filed, labeled, in [`../../examples/transcripts-2026-11-25-A9/`](../../examples/transcripts-2026-11-25-A9/README.md). Glosses of the three principles inside an output are model output, not doctrine; the doctrines are as stated in [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md), the account's single normative statement of the three doctrines.

**When and how.** Run in Michael Paik's Terminal on 25 November 2026, the first Test Thursday session, held a day early on his instruction, finished 20:04 KST, by the session A9 harness (`harness/a9_run.py`; `harness/a9-vs-a8.diff` shows every change from run A8: the run name, the tag v1.28.0, the paths and the tests.md "Note for run A9" added to T02's pass condition so that the word limit and K12 are scored separately). The pass conditions are those of `tests.md` at v1.28.0: T02 to T08 check K12. The clone was at `e9a9791` (main, tag v1.28.0). API system prompt, no tools, max_tokens 16000, one user turn per sample. Tested model `claude-opus-5-5`; scorer `claude-sonnet-5-5`, the scorer guidance of v1.14.3 in each pass condition. LLM scoring is developer testing, not independent assurance.

**One execution.** Under the harness rule of v1.14.4 the run wrote to its own output folder (`academy-a9-20261125-A9`) and log (`harness/run-log-20261125-A9.txt`); it was executed once.

**System text.** The eight SHA-256 digests in `summary.json` equal the v1.28.0 prompt sections at `e9a9791`, extracted by the rule in `tests.md`; template 01's is unchanged from run A5.

**Files.** Each transcript is copied byte for byte from the harness output; only the closing line below was appended. `summary.json`, `scores/` and `harness/` are copied unchanged, except `harness/a9-vs-a8.diff`, made for this record.

**Not reproducible from this repository.** The harness is filed as a record of how the run was made, not as a tool that runs from a clone; it resolves its paths to the run's working folder, which is not shipped, and stops unless the clone is at tag v1.28.0 on a clean tree.

| File | Case and sample | Scorer verdict | After review | SHA-256 as produced |
| --- | --- | --- | --- | --- |
| T01-s1.md | 01 Shared Client Intake, sample 1 | PASS | PASS (concur) | `7a58a3b51dfbeb180b4efc93d0c367ec322d65bc75a74684ca513fb8f4053d30` |
| T01-s2.md | 01 Shared Client Intake, sample 2 | PASS | PASS (concur) | `32ea726d890a37b58719d6017b41e53496b18b73c780933c2733aaf2e8353e4e` |
| T01-s3.md | 01 Shared Client Intake, sample 3 | PASS | PASS (concur) | `eecc7b1adb580fe534b4710bc9caba91e5655b293f62e07aae25f08bf2686646` |
| T02-s1.md | 02 Executive Briefing, Mode A, sample 1 | PASS | PASS (concur) | `75d83c2e6c8a043b38a203fb6bca5656b0e4abbec1b0d0a73324024dda83a560` |
| T02-s2.md | 02 Executive Briefing, Mode A, sample 2 | PASS | PASS (concur) | `9a0eff2e408f962b9ef056840b263bad9e67372fbba411239684bd74fb5cac9d` |
| T02-s3.md | 02 Executive Briefing, Mode A, sample 3 | PASS | PASS (concur) | `b10cc79e8bcc5b084e7149b71fb489e93842dadd98b241c220d8896d08456911` |
| T03-s1.md | 03 Executive Workshop, Mode A, sample 1 | FAIL | FAIL (concur) | `f395b98c48a360751e8b53f6210fd24084c7e8a84dd22577a4664966fb73c81b` |
| T03-s2.md | 03 Executive Workshop, Mode A, sample 2 | PASS | PASS (concur) | `9c1ee272a8032b062985a20d809e72b6597c75ab44db36bad1474b43be7a0cc4` |
| T03-s3.md | 03 Executive Workshop, Mode A, sample 3 | PASS | PASS (concur) | `40a0abe8b88f3c0bcc72ed3ddd26babbb2cbd963af147dea4afac6192593651a` |
| T04-s1.md | 04 Practitioner Academy, Mode A, sample 1 | PASS | PASS (concur) | `9c3080aa8d953ca5abdcf4d1dd6bd449afd89c111b9f625eb1e1c9c525347c25` |
| T04-s2.md | 04 Practitioner Academy, Mode A, sample 2 | FAIL | PASS (dissent to PASS) | `eb17262accfa95cb4a169a6e401f079acefe2a17a5a173d3fecf05037f36b015` |
| T04-s3.md | 04 Practitioner Academy, Mode A, sample 3 | FAIL | PASS (dissent to PASS) | `936f1cc0e0bec9c710b87447ca11d422c04859bd15f17cc8ffcf234de34280af` |
| T05-s1.md | 05 Implementation Accelerator, Mode A, sample 1 | PASS | FAIL (dissent to FAIL) | `682d38029632d279ae5398acee48485612d98667edf2429c220c6ddbdc79f788` |
| T05-s2.md | 05 Implementation Accelerator, Mode A, sample 2 | FAIL | FAIL (concur) | `d237bac53acbd5383197ba60bf7ce689583a00af7f76b28c68e23265c7f81852` |
| T05-s3.md | 05 Implementation Accelerator, Mode A, sample 3 | PASS | FAIL (dissent to FAIL) | `1729ac40a3d6c46a0a969d24ec2297dd0b8ff8b575545299ea880516cd6a78ef` |
| T06-s1.md | 06 Guided AI GRC Build, Mode A, sample 1 | PASS | PASS (concur) | `8c75015feaa655f9513d8ffa6820e6d9aa73b4c2cca1630957ffb5a1a72ff75e` |
| T06-s2.md | 06 Guided AI GRC Build, Mode A, sample 2 | PASS | PASS (concur) | `d587ee92eeddef3fffab6589c068ae57b9cd78ccd2a833d5496e8fc76e0e81a5` |
| T06-s3.md | 06 Guided AI GRC Build, Mode A, sample 3 | PASS | PASS (concur) | `34d3827840fee00cedb10820b26237d12b11f5384ca95a35a37fe39ab100c614` |
| T07-s1.md | 07 Fractional AI Governance Advisor, Mode A, sample 1 | PASS | PASS (concur) | `2639a6fe26d22142f528cfac44eac5b1bc83dfa7e07b6d64f8b085cc6e586514` |
| T07-s2.md | 07 Fractional AI Governance Advisor, Mode A, sample 2 | PASS | PASS (concur) | `8f36d1449243b81c85211c2300ee48544a9a4e3d774ada398679012e64c45a4b` |
| T07-s3.md | 07 Fractional AI Governance Advisor, Mode A, sample 3 | PASS | PASS (concur) | `a3aa5cd3767753f348576b54cb69b9b087aaa98135b8f88f591d6fce58fe88c2` |
| T08-s1.md | 08 One Workflow, Thirty Days, Mode A, sample 1 | PASS | PASS (concur) | `56d36e3ae74090f3cd38153763b02db24be3a98418de363486180d1fcbd610a3` |
| T08-s2.md | 08 One Workflow, Thirty Days, Mode A, sample 2 | FAIL | FAIL (concur) | `f2754bac717bc32c9b9a8d9d2c0f48e92e019952d490b84b233e9fe07c64728c` |
| T08-s3.md | 08 One Workflow, Thirty Days, Mode A, sample 3 | PASS | PASS (concur) | `a164fde22bfe0b10652ae076ff2a82daea4b477a90aeae0c842fd52f2e5fc6fd` |
| T09-s1.md | 02 Executive Briefing, Mode A, Part 3 (T09, critical), sample 1 | PASS | PASS (concur) | `6764a6f8ea087e760dea8b895b89244488138cac967506c8894026aa0ba02449` |
| T09-s2.md | 02 Executive Briefing, Mode A, Part 3 (T09, critical), sample 2 | PASS | PASS (concur) | `2b4b85669047ebe0f4dad82d77183c75db7c9eec09e35fe8d3c09485a4f720f3` |
| T09-s3.md | 02 Executive Briefing, Mode A, Part 3 (T09, critical), sample 3 | PASS | PASS (concur) | `d9a41fa02677b39c0f5ca2189e3bb0c91791b87065cbba8a31444fc2dc0c964f` |
| summary.json | run summary | n/a | n/a | `cc103573a9f1a1b5b5812c58738f5377c764f222e650592f513daa8a11359120` |

Model output inside the transcripts is verbatim and is not edited for house style.

---

**Final Liability rests with the Human.**
