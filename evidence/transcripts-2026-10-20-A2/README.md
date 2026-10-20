# Evidence: Academy templates, run A2, 20 October 2026 (KST)

**What.** The transcripts and scores of suite `academy-a2` (cases T01 to T08 of [`../../tests.md`](../../tests.md), three samples each) against the v1.14.1 prompt sections, with the run's `summary.json`, the scorer's per-sample JSON and the harness. The generated outputs are also filed, labeled, in [`../../examples/transcripts-2026-10-20-A2/`](../../examples/transcripts-2026-10-20-A2/).

**When and how.** Run in Michael Paik's Terminal on 20 October 2026, finished 11:22 KST, by the session A2 harness (`harness/a2_run.py`; `harness/a2-vs-a1.diff` shows every change from the run A1 harness: paths, the run name, the v1.14.1 blocks, the HEAD, the `ref` field and three samples). The clone was detached at `11981fc`, the head of pull request rolldabones/AI-Governance-Academy#1, unmerged; `summary.json` records the head and the `ref`. API system prompt, no tools, max_tokens 16000, one user turn per sample. Tested model `claude-opus-5-5`; scorer `claude-sonnet-5-5`, scoring each sample separately against the template's Acceptance Checklist, the case's pass condition and the fail indicators. The fixture was `examples/fictional-client.md` as it stood at v1.14.1, before the Part 2 correction of v1.14.2. LLM scoring is developer testing, not independent assurance.

**System text.** The eight SHA-256 digests in `summary.json` equal the v1.14.1 prompt sections at `11981fc`, extracted by the rule in `tests.md`.

**Files.** Each transcript is copied byte for byte from the harness output; only the closing line below was appended. `summary.json`, `scores/` and `harness/` are copied unchanged. Because `harness/` is kept as run, the docstring of `harness/a2_run.py` still calls it a "Session tool, not shipped in any repository", which it was when it ran; it is filed here as run evidence. Its usage lines still name `t5_run.py`, the T5 harness it was copied from; the command for this run is `python3 a2_run.py`.

**Not reproducible from this repository.** The harness is filed as a record of how the run was made, not as a tool that runs from a clone. `a2_run.py` resolves its root to the folder above the clone (the run's working folder, not shipped), reads its suite manifest from `harness/suites/` (the manifest is filed as `harness/academy-a2.json`, outside that folder) and stops unless the clone's HEAD is `11981fc` (v1.14.1). `build_a2_manifest.py` reads the T5 suite manifest `Claude Outputs/T5-runs/suites/academy-mode-a.json` and writes system-text paths under `Claude Outputs/A2-runs/suites/blocks/`; neither is shipped, and the T5 harness `t5_run.py` is not shipped either. The digests in `summary.json` let a reader check that the system text equals the prompt sections, extracted by the rule in `tests.md`; the run cannot be reproduced from the repository.

| File | Case and sample | Scorer verdict | SHA-256 as produced |
| --- | --- | --- | --- |
| T01-s1.md | 01 Shared Client Intake, sample 1 | PASS | `16dd49a85bbc2db1d7de3134bea419802ec88342e33a39f637ecb4b8d93ec7ee` |
| T01-s2.md | 01 Shared Client Intake, sample 2 | PASS | `5f4ed193d1c3701b34fa5118956e04104daca0edafa25d8c5fa6244c8f63f919` |
| T01-s3.md | 01 Shared Client Intake, sample 3 | PASS | `1735e42cc00d9ac755bf529a203762806e068da6d1333b4903a6664eec54a5e1` |
| T02-s1.md | 02 Executive Briefing, Mode A, sample 1 | FAIL | `77076793060532dd1be4801ce9ae6d551c8522a034a3c700e7cd02b2224207e1` |
| T02-s2.md | 02 Executive Briefing, Mode A, sample 2 | FAIL | `b4824406762881a5a9fa8359a777dad59d6163c246eaba9d911d3662f88ec47b` |
| T02-s3.md | 02 Executive Briefing, Mode A, sample 3 | FAIL | `b4879709c23915d9772ffc7dbf0e4f38ba6365c52bdb2e1c7bdeff7cd79d617e` |
| T03-s1.md | 03 Executive Workshop, Mode A, sample 1 | FAIL | `bdf8f61fbe23b6dacc74cf340bad9c173b5ad0b4c9779e71bccd4befd570250c` |
| T03-s2.md | 03 Executive Workshop, Mode A, sample 2 | FAIL | `45a8b9e6363553ceb07f781cb1a4203d568c9ac8840bf9a9c9c1a12deda3f4c7` |
| T03-s3.md | 03 Executive Workshop, Mode A, sample 3 | FAIL | `8140fce5d2986da9df0a3077926470b79ccc673516d56aa3d31d7b7817c0bbcc` |
| T04-s1.md | 04 Practitioner Academy, Mode A, sample 1 | FAIL | `22f02cd02d8dae0195fdf2a794d651000f6542666149e780a330db33fd099a6b` |
| T04-s2.md | 04 Practitioner Academy, Mode A, sample 2 | FAIL | `5e545dbc7a5a55e71711b80548516d871597ee4147dd273218c1d101e6251fd0` |
| T04-s3.md | 04 Practitioner Academy, Mode A, sample 3 | FAIL | `3df5ab54619597bd6b5a287ca5b7d2bd6c5d3e3f6ddc6bff15fa1cce3476f544` |
| T05-s1.md | 05 Implementation Accelerator, Mode A, sample 1 | PASS | `03d09a8b557c065efc53ee578c7a78031bbb468f8766f7cba0f8ddac3514709f` |
| T05-s2.md | 05 Implementation Accelerator, Mode A, sample 2 | FAIL | `09d4f19f359b1d05cb0e7637106f6152b6108401e971b6e5a5cb801f9d0650f7` |
| T05-s3.md | 05 Implementation Accelerator, Mode A, sample 3 | FAIL | `3a372283fa77e29c192c261069b837ba4528a9e495d12390609f473f51ecfd9a` |
| T06-s1.md | 06 Guided AI GRC Build, Mode A, sample 1 | FAIL | `3e79aee25febad893f4cb2a922f65b53048088b9b427890a5185010de3a44c23` |
| T06-s2.md | 06 Guided AI GRC Build, Mode A, sample 2 | FAIL | `ba9872b45d1dd32a257cb11ca5a819c0477b7f54935bccd61a036adbab70143a` |
| T06-s3.md | 06 Guided AI GRC Build, Mode A, sample 3 | PASS | `db861c2ab7ee6a59737b5394e9c8f86f710fdc080a9a38362e7965d59a6f6664` |
| T07-s1.md | 07 Fractional AI Governance Advisor, Mode A, sample 1 | PASS | `a36301a1bb7d26e131223ed1ac2fe10bf7bf74eeb9cdcd869c2cf821faf38606` |
| T07-s2.md | 07 Fractional AI Governance Advisor, Mode A, sample 2 | PASS | `0066ccf8ba2dd0e8516c9ef6f4176ff10616841efb5f364b5a11ad002dd4847f` |
| T07-s3.md | 07 Fractional AI Governance Advisor, Mode A, sample 3 | PASS | `ed438b03c7b56ac80f1c59486064ca7708fb31df7b0a9b08d84cb535d6a60d06` |
| T08-s1.md | 08 One Workflow, Thirty Days, Mode A, sample 1 | FAIL | `024b04cf69d4cd04219e82dd7c89051f601c7b4c6e30c48dec0ad0407261230c` |
| T08-s2.md | 08 One Workflow, Thirty Days, Mode A, sample 2 | FAIL | `48e53cb2f48bed8f9030b10e07d7171734922e1f558ed393e84a99189ae05bda` |
| T08-s3.md | 08 One Workflow, Thirty Days, Mode A, sample 3 | FAIL | `90511e0f974ca32271a009a605324b6c98c5489bc8cdf5fde4eb26848c75c9a8` |
| summary.json | run summary | n/a | `a0f5522eda914b1aa002990490453e509d1d3588018ba66f8c32bde46ce09cfc` |

Model output inside the transcripts is verbatim and is not edited for house style.

---

Final Liability rests with the Human.
