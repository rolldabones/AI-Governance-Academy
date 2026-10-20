# Evidence: Academy templates, run A1, 20 October 2026 (KST)

**What.** The transcripts and scores of suite `academy-a1` (cases T01 to T08 of [`../../tests.md`](../../tests.md)) against the v1.14.0 prompt sections, with the run's `summary.json`, the scorer's per-case JSON and the harness. The generated outputs are also filed, labeled, in [`../../examples/transcripts-2026-10-20-A1/`](../../examples/transcripts-2026-10-20-A1/).

**When and how.** Run in Michael Paik's Terminal on 20 October 2026, finished 10:57 KST, by the session A1 harness (`harness/a1_run.py`, a copy of the T5 harness changed only for paths, the run name, case T08, the v1.14.0 blocks and the HEAD). The clone was detached at `e4f3a97`, the head of pull request rolldabones/AI-Governance-Academy#1, unmerged; `summary.json` records `"head": "e4f3a97"` and no `ref` field, though the session prompt asked for one. API system prompt, no tools, max_tokens 16000, one user turn per case. Tested model `claude-opus-5-5`; scorer `claude-sonnet-5-5`, a different model scoring each transcript against the template's Acceptance Checklist, the case's pass condition and the fail indicators, including any Client fact that Part 2 of the fixture does not contain. One sample per case. LLM scoring is developer testing, not independent assurance.

**System text.** For each template, the lines strictly between `## PROMPT BEGINS` and `## PROMPT ENDS`, less the blank line after `## PROMPT BEGINS`, each ending in a newline (the rule stated in `tests.md`). The eight SHA-256 digests in `summary.json` equal the v1.14.0 prompt sections at `e4f3a97`.

**Attempt 1, superseded.** The first attempt read each case's pass condition from the T5 results table of `tests.md` instead of the Cases table, because both tables carry rows in the form `| T0n |`. Its manifest and builder are kept as `attempt-1-superseded/academy-a1.v1-defective.json` and `build_a1_manifest.v1-defective.py`; its verdicts (4 PASS, 3 FAIL, 1 UNSCORABLE, on different samples) are not a run of record. The second attempt reads the Cases table only and asserts that it did. Both are kept so that no attempt is lost.

**Files.** Each transcript is copied byte for byte from the harness output; only the closing line below was appended. `summary.json`, `scores/` and `harness/` are copied unchanged. Because `harness/` is kept as run, the docstring of `harness/a1_run.py` still calls it a "Session tool, not shipped in any repository", which it was when it ran; it is filed here as run evidence. Its usage lines still name `t5_run.py`, the T5 harness it was copied from; the command for this run is `python3 a1_run.py`.

**Not reproducible from this repository.** The harness is filed as a record of how the run was made, not as a tool that runs from a clone. `a1_run.py` resolves its root to the folder above the clone (the run's working folder, not shipped), reads its suite manifest from `harness/suites/` (the manifest is filed as `harness/academy-a1.json`, outside that folder) and stops unless the clone's HEAD is `e4f3a97` (v1.14.0). `build_a1_manifest.py` reads the T5 suite manifest `Claude Outputs/T5-runs/suites/academy-mode-a.json` and writes system-text paths under `Claude Outputs/A1-runs/suites/blocks/`; neither is shipped, and the T5 harness `t5_run.py` is not shipped either. The digests in `summary.json` let a reader check that the system text equals the prompt sections, extracted by the rule in `tests.md`; the run cannot be reproduced from the repository.

| File | Case | Scorer verdict | SHA-256 as produced |
| --- | --- | --- | --- |
| T01.md | 01 Shared Client Intake | PASS | `56ecf1528e9e7f32e5bfa8dbc05f6678a4453c934f5a0dcb482e4daa929f7d3b` |
| T02.md | 02 Executive Briefing, Mode A | FAIL | `10de3b295c8045db66cbeff54ca980062100ae370cbaf594686e49ba708d60c9` |
| T03.md | 03 Executive Workshop, Mode A | FAIL | `bd37158a3dab656e05549ff677a03c2c8e58c9f3f5ea5151c29e6ce962648114` |
| T04.md | 04 Practitioner Academy, Mode A | FAIL | `c3d9c302cdc6854a1d7c228a1c83090e562aca2c144019fcff38831d14fe8111` |
| T05.md | 05 Implementation Accelerator, Mode A | PASS | `3e97c7b002236302ae1bf6fb85d55d5176eed70574917e660ad92fb197fe6db0` |
| T06.md | 06 Guided AI GRC Build, Mode A | FAIL | `56a648fb4fd6c3fde54dc920cd878b84d0b1fd13efba23961f229ded077beeca` |
| T07.md | 07 Fractional AI Governance Advisor, Mode A | FAIL | `dada8e4dc184cb42dc37f9fee3ab52bd4dd4d0d20576db7b01a0e37de22f91ef` |
| T08.md | 08 One Workflow, Thirty Days, Mode A | FAIL | `97cc7a787c5216cdb3c86f54b29a77d70b013e70c4a327836440995a5943b981` |
| summary.json | run summary | n/a | `ce86cdf0cbf0425ad54dbdaab1c9464431410c14f95894fcbb8cc3428f466b14` |

Model output inside the transcripts is verbatim and is not edited for house style.

---

Final Liability rests with the Human.
