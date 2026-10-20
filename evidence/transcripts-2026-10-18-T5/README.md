# Evidence: Academy templates, run T5, 18 October 2026 (KST)

**What.** The transcripts and scores of suite `academy-mode-a` (cases T01 to T07 of [`../../tests.md`](../../tests.md)), with the run's `summary.json`. The generated outputs are also filed, labeled, in [`../../examples/transcripts-2026-10-18-T5/`](../../examples/transcripts-2026-10-18-T5/).

**When and how.** Run in Michael Paik's Terminal on 18 October 2026, finished 10:07 KST, by the session T5 harness (`t5_run.py`, not shipped in this repository, nor its suite manifest; the run cannot be reproduced from the repository): API system prompt, no tools, max_tokens 16000, one user turn per case. Tested model `claude-opus-5-5`; scorer `claude-sonnet-5-5`, a different model scoring each transcript against the template's Acceptance Checklist and the case's fail indicators. LLM scoring is developer testing, not independent assurance.

**System text.** For each template, the text between `## PROMPT BEGINS` and `## PROMPT ENDS`, extracted byte for byte; the Acceptance Checklist was not loaded. The seven SHA-256 digests are in `summary.json`. `summary.json` records HEAD `a0f66c2`, the commit before v1.12.0; the prompt sections run are unchanged by v1.12.0, which changed only the header lines outside them.

**Files.** Each transcript is copied byte for byte from the harness output; only the closing line below was appended. `summary.json` is copied unchanged.

| File | Case | Scorer verdict | SHA-256 as produced |
| --- | --- | --- | --- |
| T01.md | 01 Shared Client Intake | PASS | `06cf6c8700535b9864a95441046475ef73ba5e004cbc3908e059ce334d6aeb14` |
| T02.md | 02 Executive Briefing, Mode A | PASS | `bc3a0dfb5a404d73db22b1b9a0828aa6bf5753875a90b14bd2f820b40ed120f5` |
| T03.md | 03 Executive Workshop, Mode A | PASS | `7217dd8076ca5f0063d305dcb051fccc5e1a36794a5e64b2fb1906b9ed2dfa46` |
| T04.md | 04 Practitioner Academy, Mode A | FAIL | `2c889288d34450c7d6e8edbd7cfb73cd79ef9cdef85f248c408830198cab6016` |
| T05.md | 05 Implementation Accelerator, Mode A | FAIL | `89ee12c4c3589ee4957a0aa39591b9ee0a29631c0113d551e5d3125c25360bee` |
| T06.md | 06 Guided AI GRC Build, Mode A | FAIL | `4f8c26594cd1002a4b853dd5b45189d8208498ca5ae5cb27851de9669d0d84a9` |
| T07.md | 07 Fractional AI Governance Advisor, Mode A | PASS | `fc6f382af9681b30e6589111fb4d54873e1731b4f84153d0bcf077669dbb8e47` |
| summary.json | run summary | n/a | `61b69e7ab90ac8b4e3b8a7d70f1d00a77853cb5bd8c5296ac3bef895f0680445` |

Model output inside the transcripts is verbatim and is not edited for house style.

---

Final Liability rests with the Human.
