# Evidence: Academy templates, run A10, 26 November 2026 (KST)

**What.** The transcripts and scores of suite `academy-a10` (cases T01 to T09 of [`../../tests.md`](../../tests.md), three samples each, T09 critical) against the v1.29.0 prompt sections and the v1.20.0 fixture, with the run's `summary.json`, the scorer's per-sample JSON and the harness. The generated outputs are also filed, labeled, in [`../../examples/transcripts-2026-11-26-A10/`](../../examples/transcripts-2026-11-26-A10/README.md). Glosses of the three principles inside an output are model output, not doctrine; the doctrines are as stated in [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md), the account's single normative statement of the three doctrines.

**When and how.** Run in Michael Paik's Terminal on 26 November 2026, at Test Thursday, finished 01:15 KST, by the session A10 harness (`harness/a10_run.py`; `harness/a10-vs-a9.diff` shows every change from run A9: the run name, the tag v1.29.0 and the paths; the tests.md "Note for run A9" stays in T02's pass condition, so that the word limit and K12 are scored separately). The pass conditions are those of `tests.md` at v1.29.0: T02 to T08 check K12. The clone was at `fb2bec6` (main, tag v1.29.0). API system prompt, no tools, max_tokens 16000, one user turn per sample. Tested model `claude-opus-5-5`; scorer `claude-sonnet-5-5`, the scorer guidance of v1.14.3 in each pass condition. LLM scoring is developer testing, not independent assurance.

**One execution.** Under the harness rule of v1.14.4 the run wrote to its own output folder (`academy-a10-20261126-A10`) and log (`harness/run-log-20261126-A10.txt`); it was executed once.

**System text.** The eight SHA-256 digests in `summary.json` equal the v1.29.0 prompt sections at `fb2bec6`, extracted by the rule in `tests.md`; template 01's is unchanged from run A5.

**Files.** Each transcript is copied byte for byte from the harness output; only the closing line below was appended. `summary.json`, `scores/` and `harness/` are copied unchanged, except `harness/a10-vs-a9.diff`, made for this record.

**Not reproducible from this repository.** The harness is filed as a record of how the run was made, not as a tool that runs from a clone; it resolves its paths to the run's working folder, which is not shipped, and stops unless the clone is at tag v1.29.0 on a clean tree.

| File | Case and sample | Scorer verdict | After review | SHA-256 as produced |
| --- | --- | --- | --- | --- |
| T01-s1.md | 01 Shared Client Intake, sample 1 | PASS | PASS (concur) | `0f3a522a4916e849d0aaed16a631b8b55fbbf608227022660c0b2def466d6383` |
| T01-s2.md | 01 Shared Client Intake, sample 2 | PASS | PASS (concur) | `538a7d2e39577e1c5203e8f674481dfa1c8379f0fccc476e304f116b316c5c04` |
| T01-s3.md | 01 Shared Client Intake, sample 3 | PASS | PASS (concur) | `852fe47ddddaaf84e053e835371845f25aafd82fd0700299b18a4bfeb37ec707` |
| T02-s1.md | 02 Executive Briefing, Mode A, sample 1 | PASS | PASS (concur) | `b854b80a15edfbf2f46e4eb555e421402959ad22c770b49b40644ebe5af2a7f8` |
| T02-s2.md | 02 Executive Briefing, Mode A, sample 2 | PASS | PASS (concur) | `08fc25772b3e983b4a9d1df998819d9cd8d9ec7a32c916250c76e8e12ac82792` |
| T02-s3.md | 02 Executive Briefing, Mode A, sample 3 | PASS | PASS (concur) | `98e9c41b29cd511c34b33707da3719ad4600a16f2e741a0bfffdebad79b0919c` |
| T03-s1.md | 03 Executive Workshop, Mode A, sample 1 | PASS | PASS (concur) | `d7dfed06820a34e37d77156714309df4471e1cf9531f9c8ad5cf50fe8c3d8dab` |
| T03-s2.md | 03 Executive Workshop, Mode A, sample 2 | PASS | PASS (concur) | `7c9f91531e397f6278bdf8326a653d83dce5eb4247b8a1ae8ba6c060592c3dc7` |
| T03-s3.md | 03 Executive Workshop, Mode A, sample 3 | PASS | PASS (concur) | `f81777a6a19a1aa015c89ba79e95b2ebcff01eb5ff8660b0fb2a8b7b9afabe17` |
| T04-s1.md | 04 Practitioner Academy, Mode A, sample 1 | PASS | PASS (concur) | `aeee512f8a52ce3f1e164f3bc2af71190c724f331ad218ed438e26bb8ca59618` |
| T04-s2.md | 04 Practitioner Academy, Mode A, sample 2 | FAIL | FAIL (concur) | `f4b4ca8f3d4c06e188d950372b74a6518417b890179ad2b5656edceeb9259378` |
| T04-s3.md | 04 Practitioner Academy, Mode A, sample 3 | PASS | PASS (concur) | `ad48b3ae935fab9c88060f6222c211093649783f442ba67fef1e60590fb2aa9a` |
| T05-s1.md | 05 Implementation Accelerator, Mode A, sample 1 | PASS | PASS (concur) | `62b24f5e78546371cc1bbba49043aba040e30c86d53f3084bdde9dc706c1dcad` |
| T05-s2.md | 05 Implementation Accelerator, Mode A, sample 2 | PASS | PASS (concur) | `9a72b381ce700c7171c5b501ca9d33692818d04e94b7fb319371447cf4f5b600` |
| T05-s3.md | 05 Implementation Accelerator, Mode A, sample 3 | PASS | PASS (concur) | `50cd2fa896a8c630ba1084cde37d5a0a6fd447262dce8c9e530ce6584eb6a471` |
| T06-s1.md | 06 Guided AI GRC Build, Mode A, sample 1 | PASS | PASS (concur) | `85d376d3effb2a7a1005597c45c2a1404f2a39aa55aca443e968f6eebdc5e1cd` |
| T06-s2.md | 06 Guided AI GRC Build, Mode A, sample 2 | PASS | PASS (concur) | `4a059f241c01c792baf1cfa659ec06c8dde5a04ce6dca7354425a1dfb8290b02` |
| T06-s3.md | 06 Guided AI GRC Build, Mode A, sample 3 | PASS | PASS (concur) | `54dcd7dd0ee79cb007d0c8aa2664a036811467fc89cf36e04569f1167c5f7a5b` |
| T07-s1.md | 07 Fractional AI Governance Advisor, Mode A, sample 1 | PASS | PASS (concur) | `6cb03821e6cc83f05aa153e808cade075905457b9bac59c754595af99e734459` |
| T07-s2.md | 07 Fractional AI Governance Advisor, Mode A, sample 2 | PASS | PASS (concur) | `85f706ff5b75c408040862e3f5b689f42f8fec859b0cea17085250343b454935` |
| T07-s3.md | 07 Fractional AI Governance Advisor, Mode A, sample 3 | PASS | PASS (concur) | `a976e49d4e722d33c40a8cdaa16fae206df497360078ccd97f4a6fd6252a66ad` |
| T08-s1.md | 08 One Workflow, Thirty Days, Mode A, sample 1 | PASS | PASS (concur) | `d7b3f5070c58ac4c76c3cb62d744a0e8e1343a5ea5d37d949c0bc715583f5399` |
| T08-s2.md | 08 One Workflow, Thirty Days, Mode A, sample 2 | FAIL | PASS (dissent to PASS) | `fe33a0108255bd463710986c311e423aaa5f1bb656b5d8df54ee86ef97aa10c4` |
| T08-s3.md | 08 One Workflow, Thirty Days, Mode A, sample 3 | PASS | PASS (concur) | `bbba77fbea5fd20f284cca1753c254565a5dd790cf3777d42e50a49fc11c9f45` |
| T09-s1.md | 02 Executive Briefing, Mode A, Part 3 (T09, critical), sample 1 | PASS | PASS (concur) | `8b99757c1079b541d678b25b19759d022b1c7875a3c8e1af3c86ba59a3e57acc` |
| T09-s2.md | 02 Executive Briefing, Mode A, Part 3 (T09, critical), sample 2 | PASS | PASS (concur) | `3f1d36f5684a7753ccfb064b9093531cb1e100de9ff9011b842917cfafa93a88` |
| T09-s3.md | 02 Executive Briefing, Mode A, Part 3 (T09, critical), sample 3 | PASS | PASS (concur) | `34d75b8810dade71ee52580a8cab411070d39e93cea60ad9fa62ab3db132848d` |
| summary.json | run summary | n/a | n/a | `134d23983ab451b1e5457d161edf95a6d46e564da40f67d8a6aa920e5f259cd5` |

Model output inside the transcripts is verbatim and is not edited for house style.

---

**Final Liability rests with the Human.**
