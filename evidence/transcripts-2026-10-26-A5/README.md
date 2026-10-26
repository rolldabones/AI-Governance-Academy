# Evidence: Academy templates, run A5, 26 October 2026 (KST)

**What.** The transcripts and scores of suite `academy-a5` (cases T01 to T08 of [`../../tests.md`](../../tests.md), three samples each) against the v1.14.8 prompt sections, in which K7, K8 and K9 are fixed in text, with the run's `summary.json`, the scorer's per-sample JSON and the harness. The generated outputs are also filed, labeled, in [`../../examples/transcripts-2026-10-26-A5/`](../../examples/transcripts-2026-10-26-A5/).

**When and how.** Run in Michael Paik's Terminal on 26 October 2026, finished 10:41 KST, by the session A5 harness (`harness/a5_run.py`; `harness/a5-vs-a4.diff` shows every change from the run A4 harness and manifest builder: the run name, the paths and a check that the clone is at tag v1.14.8 on a clean tree in place of a commit check, because v1.14.8 was committed in the same Terminal block). The clone was at `f0dab9d` (main, tag v1.14.8); `summary.json` records the head and the `ref`. API system prompt, no tools, max_tokens 16000, one user turn per sample. Tested model `claude-opus-5-5`; scorer `claude-sonnet-5-5`, with the scorer guidance of v1.14.3 in each pass condition. LLM scoring is developer testing, not independent assurance.

**One execution.** Under the harness rule of v1.14.4 the run wrote to its own output folder (`academy-a5-20261026-A5`) and log (`harness/run-log-20261026-A5.txt`); it was executed once.

**System text.** The eight SHA-256 digests in `summary.json` equal the v1.14.8 prompt sections at `f0dab9d`, extracted by the rule in `tests.md`. The fixture is unchanged from run A4.

**Files.** Each transcript is copied byte for byte from the harness output; only the closing line below was appended. `summary.json`, `scores/` and `harness/` are copied unchanged. The docstring of `harness/a5_run.py` calls it a session tool, which it was when it ran; it is filed here as run evidence.

**Not reproducible from this repository.** The harness is filed as a record of how the run was made, not as a tool that runs from a clone. `a5_run.py` resolves its root to the folder above the clone (the run's working folder, not shipped), reads its suite manifest from `suites/` beside it (filed as `harness/academy-a5.json`) and stops unless the clone is at tag v1.14.8 on a clean tree. `build_a5_manifest.py` reads the T5 suite manifest under `Claude outputs/T5-runs/suites/` and writes system-text paths under `Claude outputs/A5-runs/suites/blocks/`; neither is shipped, nor is the T5 harness `t5_run.py`. The digests in `summary.json` let a reader check that the system text equals the prompt sections; the run cannot be reproduced from the repository.

| File | Case and sample | Scorer verdict | After review | SHA-256 as produced |
| --- | --- | --- | --- | --- |
| T01-s1.md | 01 Shared Client Intake, sample 1 | PASS | PASS (concur) | `59eff33bfe2d05300f85f428f386979a04277f7bf15596fd0fffb9cef530686e` |
| T01-s2.md | 01 Shared Client Intake, sample 2 | FAIL | PASS (dissent: PASS) | `195394351915d2be732ca6d1d998eea51fe8bb0be0389829e6610789e56eb18e` |
| T01-s3.md | 01 Shared Client Intake, sample 3 | FAIL | PASS (dissent: PASS) | `746c8ee972ccf1d4670ab70a4eba7ff5b49d30df7b9cf6ca7d1c5cd173a40c26` |
| T02-s1.md | 02 Executive Briefing, Mode A, sample 1 | PASS | PASS (concur) | `f0f72302f29e2cdbd2f94ccf3da076f89cdff7ae6d5dd92de14e65a7ed09b88b` |
| T02-s2.md | 02 Executive Briefing, Mode A, sample 2 | PASS | PASS (concur) | `221bcb77fe3efe2b958fdf7c7ae65471fec087717ebb2f8937a4a0829c233e22` |
| T02-s3.md | 02 Executive Briefing, Mode A, sample 3 | FAIL | FAIL (concur) | `f985579dad4b68142bc95b9c45950968b1aceb7015bb7053943cbd07c9c91675` |
| T03-s1.md | 03 Executive Workshop, Mode A, sample 1 | FAIL | FAIL (concur) | `0028d6a938b70bb36026b8e452cf81dcb6d0c09163337edaab531fa1e6dc6508` |
| T03-s2.md | 03 Executive Workshop, Mode A, sample 2 | PASS | PASS (concur) | `a65cd5fec5c05674f4aaeb5a74bee27e33f24748e76d2df9b5be850411dd749a` |
| T03-s3.md | 03 Executive Workshop, Mode A, sample 3 | PASS | PASS (concur) | `500a17182bd71da0a828eb0736ec2cf68e04ca8d3b66aa8c06f4a0b066d79626` |
| T04-s1.md | 04 Practitioner Academy, Mode A, sample 1 | PASS | PASS (concur) | `5e5d31144d7b063c83d4e6d7a630528bf91022fb61ba85166d75c994cb6c568b` |
| T04-s2.md | 04 Practitioner Academy, Mode A, sample 2 | PASS | PASS (concur) | `71ff3b984f9dfafa88061d2127d473c35f57be6f27524d8c8eeb9a20c2f7267d` |
| T04-s3.md | 04 Practitioner Academy, Mode A, sample 3 | PASS | PASS (concur) | `0ddd3ea2eb83885874e5cca0161189e4d27de9dc39b3c4d5683c844e6fa44246` |
| T05-s1.md | 05 Implementation Accelerator, Mode A, sample 1 | PASS | PASS (concur) | `61185dfd608b90adaa107392b7208c5d4c6850636310aac24880c462ea0e7b7a` |
| T05-s2.md | 05 Implementation Accelerator, Mode A, sample 2 | PASS | PASS (concur) | `b78ba2d1bb968670ad28dc435376f113ef29e6573617ee66f38ca734c27807aa` |
| T05-s3.md | 05 Implementation Accelerator, Mode A, sample 3 | PASS | PASS (concur) | `66a30cd49522dd0e563ffbaa43ce92497de821aa91d214afcfbd2bdcd432ed2f` |
| T06-s1.md | 06 Guided AI GRC Build, Mode A, sample 1 | PASS | PASS (concur) | `2b93b62fdb9ecc6bec5bbe57260b3e5811cf2feb4715e10a9627bd506c6b61ae` |
| T06-s2.md | 06 Guided AI GRC Build, Mode A, sample 2 | FAIL | FAIL (concur) | `e14beddcbfce15e987976ff6cb16cec9a71e2f50f3db5cc768c2e6edab5a8366` |
| T06-s3.md | 06 Guided AI GRC Build, Mode A, sample 3 | PASS | FAIL (dissent: FAIL) | `eb3193a3c5b4946dec4602cb43cee26c8c85e4b981af43e74e64c9bcf7ae3901` |
| T07-s1.md | 07 Fractional AI Governance Advisor, Mode A, sample 1 | PASS | PASS (concur) | `01e62890eec96c1d4429c806932572b9a4c890b1c4f3e36ee3e9056157fc34a5` |
| T07-s2.md | 07 Fractional AI Governance Advisor, Mode A, sample 2 | PASS | PASS (concur) | `7c380c78a36f6f8e3769a31e2de82390b0d7594375a3796be77e1893a20af96d` |
| T07-s3.md | 07 Fractional AI Governance Advisor, Mode A, sample 3 | PASS | PASS (concur) | `4b1fcba541dc186796cdc7267ab0b22015201295383de7e3e95b0e0ea8263c2a` |
| T08-s1.md | 08 One Workflow, Thirty Days, Mode A, sample 1 | PASS | PASS (concur) | `a2f672afe1201edea5aa4c3a40f924e494843a45fe4f9867f7d318b5c73f2a25` |
| T08-s2.md | 08 One Workflow, Thirty Days, Mode A, sample 2 | PASS | PASS (concur) | `4a60bb9b2e231c3732315bb2fe350e54a06d937c4715a23aaf2b9c71f65903eb` |
| T08-s3.md | 08 One Workflow, Thirty Days, Mode A, sample 3 | PASS | PASS (concur) | `2d1eb75f7c7a8a073104e24833e77d30e842cd33303b303f307abcda06a6e4fa` |
| summary.json | run summary | n/a | n/a | `339f4e7c88a9015e947ecd00313a84eff0bc5a02cceb260671de81b52e7b2f68` |

Model output inside the transcripts is verbatim and is not edited for house style.

---

Final Liability rests with the Human.
