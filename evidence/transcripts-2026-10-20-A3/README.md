# Evidence: Academy templates, run A3, 20 October 2026 (KST)

**What.** The transcripts and scores of suite `academy-a3` (cases T01 to T08 of [`../../tests.md`](../../tests.md), three samples each) against the v1.14.2 prompt sections and fixture, with the run's `summary.json`, the scorer's per-sample JSON and the harness. The generated outputs are also filed, labeled, in [`../../examples/transcripts-2026-10-20-A3/`](../../examples/transcripts-2026-10-20-A3/).

**When and how.** Run in Michael Paik's Terminal on 20 October 2026, finished 11:57 KST, by the session A3 harness (`harness/a3_run.py`; `harness/a3-vs-a2.diff` shows every change from the run A2 harness: paths, the run name, the HEAD and the v1.14.2 blocks and fixture). The clone was detached at `7fe5751`, the head of pull request rolldabones/AI-Governance-Academy#1 before merge; `summary.json` records the head and the `ref`. API system prompt, no tools, max_tokens 16000, one user turn per sample. Tested model `claude-opus-5-5`; scorer `claude-sonnet-5-5`, scoring each sample separately with the A2 scorer prompt; the scorer guidance of v1.14.3 was not yet in force. LLM scoring is developer testing, not independent assurance.

**System text.** The eight SHA-256 digests in `summary.json` equal the v1.14.2 prompt sections at `7fe5751`, extracted by the rule in `tests.md`.

**Files.** Each transcript is copied byte for byte from the harness output; only the closing line below was appended. `summary.json`, `scores/` and `harness/` are copied unchanged.

| File | Case and sample | Scorer verdict | SHA-256 as produced |
| --- | --- | --- | --- |
| T01-s1.md | 01 Shared Client Intake, sample 1 | FAIL | `e4627ca7ae6d17903b67194570aa043b5a3cca716308ba9b95ebd43080480bf4` |
| T01-s2.md | 01 Shared Client Intake, sample 2 | PASS | `d6d770ac0dcab74c48d802e61cce80e57e9adb4d8837266ffe884fe0523f860b` |
| T01-s3.md | 01 Shared Client Intake, sample 3 | PASS | `a65875a66cf152bbed1c1a3d16d30ebe9604024278068b2a58e7f8891d2dc137` |
| T02-s1.md | 02 Executive Briefing, Mode A, sample 1 | FAIL | `c58df30dcdf6aed716050301a8f2b822586680f45164422cbc9f8009cb793459` |
| T02-s2.md | 02 Executive Briefing, Mode A, sample 2 | FAIL | `c20c79ccdf27792fa74fa9ad33bfb813c8115033864aa26791840598779ffbd8` |
| T02-s3.md | 02 Executive Briefing, Mode A, sample 3 | PASS | `6b838adad9f66334e19f44e236aaf7b7cfa9e4707b9a2c3e8cb8282ec394db8e` |
| T03-s1.md | 03 Executive Workshop, Mode A, sample 1 | FAIL | `674f7e3df87f477d9c65baa4df6586f126b747a39e9b47f0c04e4023efe7c248` |
| T03-s2.md | 03 Executive Workshop, Mode A, sample 2 | FAIL | `a9c4f2b4291451f6e8372115a2686dae9d0ab64b2e321a13dd2d30fb0c8ae95f` |
| T03-s3.md | 03 Executive Workshop, Mode A, sample 3 | FAIL | `ecbee4320296e5a2c4d6db363ed1e94ae52a5b2410b334209b021875f635cc3b` |
| T04-s1.md | 04 Practitioner Academy, Mode A, sample 1 | FAIL | `735c89456abbcc9550ddecf239edf2f1e5279fcb5fbf9aebf8cf65272558cf34` |
| T04-s2.md | 04 Practitioner Academy, Mode A, sample 2 | FAIL | `d0f6b38aeb56d25f179999ed1f9d19aca667323711dea5390fac2944bf2f6420` |
| T04-s3.md | 04 Practitioner Academy, Mode A, sample 3 | FAIL | `6abcd8f35eb838ec15245e4b7882699c6dfbf1c1ee43a42f673817183f78f7dc` |
| T05-s1.md | 05 Implementation Accelerator, Mode A, sample 1 | PASS | `126f0fae9f958946c3aba15b47f663f384e70fa59c36fe0050b65919fd3c1a94` |
| T05-s2.md | 05 Implementation Accelerator, Mode A, sample 2 | PASS | `d5a6aefe3ed80fbd0f8e3cc04ac2126113ca6363d79c0bae3f52ea4c3cab8a2d` |
| T05-s3.md | 05 Implementation Accelerator, Mode A, sample 3 | PASS | `05e1d634050d8b211fe104dbc04799f129ae1d408c33eec809f8c0a731cab9d7` |
| T06-s1.md | 06 Guided AI GRC Build, Mode A, sample 1 | FAIL | `7f248ddb8d3a7da550b9864cf41d8fac3e762ed0641bedd43e794680aa3c2529` |
| T06-s2.md | 06 Guided AI GRC Build, Mode A, sample 2 | PASS | `9f34357c1dbbba817e6f284722b24c4d6c6b7209a3ededd1206a1d2de8714310` |
| T06-s3.md | 06 Guided AI GRC Build, Mode A, sample 3 | FAIL | `0f8adb3587a3e26b63418cefaded954f655bcb34e70a40ed69147dd37a4d68f9` |
| T07-s1.md | 07 Fractional AI Governance Advisor, Mode A, sample 1 | PASS | `d8cb587406caa1e85261df4b285814cbf63187233f990bb407a106959aaf23e9` |
| T07-s2.md | 07 Fractional AI Governance Advisor, Mode A, sample 2 | PASS | `2c5403a648786479220125437b0a31b4d914ebcde3ca650d528d863a9c898836` |
| T07-s3.md | 07 Fractional AI Governance Advisor, Mode A, sample 3 | PASS | `cce018e296b334ff64bdd4438e8dfeff89856535d81116c05987adb3c95b1516` |
| T08-s1.md | 08 One Workflow, Thirty Days, Mode A, sample 1 | FAIL | `e11392e07c9abc3095f7e79e3cc6fb4530b2ba5069241dc35eeb357eb4a3d074` |
| T08-s2.md | 08 One Workflow, Thirty Days, Mode A, sample 2 | FAIL | `9f548c3b1bb8e4d88bd66ca9122bb3a07ac9a6e7e296cdc94e349b7f6dbe8646` |
| T08-s3.md | 08 One Workflow, Thirty Days, Mode A, sample 3 | FAIL | `c07f820d5d1a3fd47a29ae830bda681a0d5922ab60f8983f8db05aa6cb26864c` |
| summary.json | run summary | n/a | `abdd2c988148fd9d692a5eb0244430769a2bda0a305d5745348a90c73551b48d` |

Model output inside the transcripts is verbatim and is not edited for house style.

---

Final Liability rests with the Human.
