# Evidence: Academy templates, run A4, 26 October 2026 (KST)

**What.** The transcripts and scores of suite `academy-a4` (cases T01 to T08 of [`../../tests.md`](../../tests.md), three samples each) against the v1.14.6 prompt sections and fixture, with the run's `summary.json`, the scorer's per-sample JSON and the harness. The generated outputs are also filed, labeled, in [`../../examples/transcripts-2026-10-26-A4/`](../../examples/transcripts-2026-10-26-A4/).

**When and how.** Run in Michael Paik's Terminal on 26 October 2026, finished 10:06 KST, by the session A4 harness (`harness/a4_run.py`; `harness/a4-vs-a3.diff` shows every change from the run A3 harness and manifest builder: the run name, the HEAD, the paths, the scorer guidance and the acceptance text). The clone was at `88e655c` (main, tag v1.14.6); `summary.json` records the head and the `ref`. API system prompt, no tools, max_tokens 16000, one user turn per sample. Tested model `claude-opus-5-5`; scorer `claude-sonnet-5-5`, scoring each sample separately, with the scorer guidance of v1.14.3 added to each pass condition. LLM scoring is developer testing, not independent assurance.

**One execution.** Under the harness rule of v1.14.4 the run wrote to its own output folder (`academy-a4-20261026-A4`) and log (`harness/run-log-20261026-A4.txt`); it was executed once.

**System text.** The eight SHA-256 digests in `summary.json` equal the v1.14.6 prompt sections at `88e655c`, extracted by the rule in `tests.md`; the digests of templates 03 and 08 differ from run A3 because v1.14.3 removed their prose-only rule.

**Files.** Each transcript is copied byte for byte from the harness output; only the closing line below was appended. `summary.json`, `scores/` and `harness/` are copied unchanged. The docstring of `harness/a4_run.py` calls it a session tool, which it was when it ran; it is filed here as run evidence.

**Not reproducible from this repository.** The harness is filed as a record of how the run was made, not as a tool that runs from a clone. `a4_run.py` resolves its root to the folder above the clone (the run's working folder, not shipped), reads its suite manifest from `suites/` beside it (the manifest is filed as `harness/academy-a4.json`) and stops unless the clone's HEAD is `88e655c`. `build_a4_manifest.py` reads the T5 suite manifest under `Claude outputs/T5-runs/suites/` and writes system-text paths under `Claude outputs/A4-runs/suites/blocks/`; neither is shipped, and the T5 harness `t5_run.py` is not shipped either. The digests in `summary.json` let a reader check that the system text equals the prompt sections; the run cannot be reproduced from the repository.

| File | Case and sample | Scorer verdict | After review | SHA-256 as produced |
| --- | --- | --- | --- | --- |
| T01-s1.md | 01 Shared Client Intake, sample 1 | FAIL | FAIL (concur) | `07acdac1fe19a61b1e029a6f76eadd6c367e48cfeb27de1d076a8e9a3ba5d255` |
| T01-s2.md | 01 Shared Client Intake, sample 2 | FAIL | FAIL (concur) | `b3a4cf4b02ec5314e0a60ce8e38b9c5987ae6af2684e8cac244dcd8dc5a63dcd` |
| T01-s3.md | 01 Shared Client Intake, sample 3 | FAIL | FAIL (concur) | `174a290d6084e65534e7330cf83f6a5bb59b0961a974d2c7676068cec2c5a158` |
| T02-s1.md | 02 Executive Briefing, Mode A, sample 1 | PASS | FAIL (dissent: FAIL) | `2fe3910b99b621ba49f4ee3e078cb68baa3fff6fc80d45cdffd0c859b286cf5e` |
| T02-s2.md | 02 Executive Briefing, Mode A, sample 2 | PASS | FAIL (dissent: FAIL) | `66d09580dda32d7f4bbdbeb7446b5bfe7a247837c42d3367e071eab25ab871ca` |
| T02-s3.md | 02 Executive Briefing, Mode A, sample 3 | FAIL | FAIL (concur) | `9cd0d254dfe3505e4b630a15cb1e1044d52c78c3eeeca3333837d6b02330187e` |
| T03-s1.md | 03 Executive Workshop, Mode A, sample 1 | PASS | PASS (concur) | `2d7b6b9469ca946babb526f18876634e1397e21a4222b6308f1b87fb3c58e57a` |
| T03-s2.md | 03 Executive Workshop, Mode A, sample 2 | FAIL | FAIL (concur) | `453472ca9808ce260b1080dfa9a523cc450fe5d5d94d1d3fde5e657164eda9a1` |
| T03-s3.md | 03 Executive Workshop, Mode A, sample 3 | PASS | PASS (concur) | `4b15d00034d7a2559edfd829791521ef2a17fb60413466000a89c2fe4a5d7fee` |
| T04-s1.md | 04 Practitioner Academy, Mode A, sample 1 | FAIL | FAIL (concur) | `2123d349e072bd0cab0f9bd1955c2a4ee9de0bc65004418f76b328bf66f3a0d3` |
| T04-s2.md | 04 Practitioner Academy, Mode A, sample 2 | PASS | FAIL (dissent: FAIL) | `9cfe60e76424ed60e0432a8f0fb15bc08db7eb2226e9cf921ca940f971963ee1` |
| T04-s3.md | 04 Practitioner Academy, Mode A, sample 3 | PASS | PASS (concur) | `f0c7b993bef9e22724b37e333e3f139b761d04c67d0718d8f677499916df0c2d` |
| T05-s1.md | 05 Implementation Accelerator, Mode A, sample 1 | PASS | FAIL (dissent: FAIL) | `a81f5e363ef1d3424770281d1f3e8b0c2061faf7203156532ffcd9835c9503c9` |
| T05-s2.md | 05 Implementation Accelerator, Mode A, sample 2 | PASS | PASS (concur) | `e108b8030e93c7f4b06d5c27349ec4560b3c5b1662957340c8e74d198e09331b` |
| T05-s3.md | 05 Implementation Accelerator, Mode A, sample 3 | PASS | PASS (concur) | `2bbd4414e3db8bb15eb96c8cefcd007219af8670c4e37d850d04b6ee162650b6` |
| T06-s1.md | 06 Guided AI GRC Build, Mode A, sample 1 | FAIL | FAIL (concur) | `74357980079d968919279c18bdb147046b11a020d993f27ec34f3fcdac556d44` |
| T06-s2.md | 06 Guided AI GRC Build, Mode A, sample 2 | PASS | FAIL (dissent: FAIL) | `519ba1dfc7812d1cc61a881715856bd4805a59cdbf1e472405d2b77ad47fcc1a` |
| T06-s3.md | 06 Guided AI GRC Build, Mode A, sample 3 | FAIL | FAIL (concur) | `64b7359b6da3a012c4a0e8026e00446883286bd24f1f31d64e04e2c957254db4` |
| T07-s1.md | 07 Fractional AI Governance Advisor, Mode A, sample 1 | PASS | FAIL (dissent: FAIL) | `84c484b53f595541d8bdd4a276675c9a17b798368e4a5c5c24a1e0c676c67a0e` |
| T07-s2.md | 07 Fractional AI Governance Advisor, Mode A, sample 2 | PASS | PASS (concur) | `98232ee753ab58a67d3631e7109c5b0bf9fa27810c17e23306da1e27f4c087e0` |
| T07-s3.md | 07 Fractional AI Governance Advisor, Mode A, sample 3 | FAIL | FAIL (concur) | `c273c73ecf0813aa1eafec687f7a67af8bab22b93f5e3ea05e560eae6bda6c52` |
| T08-s1.md | 08 One Workflow, Thirty Days, Mode A, sample 1 | PASS | PASS (concur) | `6c7a37ff612331cb5deb098fa112d17a47f88cd821e2ee4f1041fa2075bafc35` |
| T08-s2.md | 08 One Workflow, Thirty Days, Mode A, sample 2 | PASS | FAIL (dissent: FAIL) | `bb5753567c3de8b90a0ecc7e1a3b695c5ef90ad8ec19af7e7839ea43afe67ca7` |
| T08-s3.md | 08 One Workflow, Thirty Days, Mode A, sample 3 | FAIL | FAIL (concur on another ground) | `17a8c97baeacecb9be43bf9f27c21ab8814e3caab895337737be162cf5a254a7` |
| summary.json | run summary | n/a | n/a | `64186ddb92c5a4492da2e121d259a1a9db117a39d33bec81e2e7887c89fd225f` |

Model output inside the transcripts is verbatim and is not edited for house style.

---

Final Liability rests with the Human.
