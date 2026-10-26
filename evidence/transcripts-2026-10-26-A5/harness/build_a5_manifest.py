#!/usr/bin/env python3
"""Builds suites/academy-a5.json and suites/blocks/ for run A5 (26 October 2026, KST), from build_a4_manifest.py (from build_a3_manifest.py); built for run A3 from the T5 manifest
(fail indicators only), tests.md (v1.14.2, HEAD 7fe5751), the templates' prompt sections and Acceptance
Checklists, and examples/fictional-client.md read fresh. Reads the clone; writes only here."""
import hashlib, json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
REPO = ROOT / "AI-Governance-Academy"
T5 = json.loads((ROOT / "Claude outputs/T5-runs/suites/academy-mode-a.json").read_text(encoding="utf-8"))
NAMES = ["01-client-intake", "02-executive-briefing", "03-executive-workshop", "04-practitioner-academy",
         "05-implementation-accelerator", "06-guided-ai-grc-build", "07-fractional-advisor",
         "08-one-workflow-thirty-days"]
DIGESTS = None   # computed from the templates of v1.14.8 and printed
FIXTURE_SHA = "3461cc538378e190412d0b0a508bdd3764fcbf1d5b6d2c4831f95822a9ba5c1b"
BLK = "../Claude outputs/A5-runs/suites/blocks/AI-Governance-Academy-{}.txt"
NEW_FI = ("A statement of a Client fact that Part 2 of the fixture (the Client Profile Block) does not "
          "contain, including any incumbent register, process, control or record beyond the framework names")
SELECT = "Select exactly one OUTPUT MODE: MODE A – PROPOSAL."
NO_PRIOR = "Prior program report: none. The Client has not completed a prior Academy program."
fx_bytes = (REPO / "examples/fictional-client.md").read_bytes()
assert hashlib.sha256(fx_bytes).hexdigest() == FIXTURE_SHA, "fixture SHA-256 mismatch"
fx = fx_bytes.decode("utf-8")
raw = re.search(r"<!-- fixture:raw:start -->\n```text\n(.*?)```\n<!-- fixture:raw:end -->", fx, re.S).group(1)
profile = re.search(r"<!-- fixture:profile:start -->\n```\n(.*?)```\n<!-- fixture:profile:end -->", fx, re.S).group(1)
assert "(stated as budget holder)" in profile and "(Dana Whitfield)" in profile and "Ravi Okafor" in profile
tests = (REPO / "tests.md").read_text(encoding="utf-8")
cases_sec = tests.split("\n## Cases\n", 1)[1].split("\n## Known defects\n", 1)[0]   # Cases table only, not Last run
rows = {m[0]: m[1].strip() for m in re.findall(r"^\| (T0\d) \|[^|]*\|[^|]*\|(.*)\|\s*$", cases_sec, re.M)}
assert sorted(rows) == [f"T0{i}" for i in range(1, 9)], rows.keys()
assert all(v.startswith("Checklist items") or v.startswith("Acceptance Checklist items") for v in rows.values()), rows
na_rule = next(l for l in tests.split("\n") if l.startswith("An item the checklist scopes"))
guide = next(l for l in tests.split("\n") if l.startswith("**Scorer guidance (from v1.14.3).**"))
how = next(l for l in tests.split("\n") if l.startswith("**How a case is run.**"))
t5 = {c["id"]: c for c in T5["cases"]}
(HERE / "suites/blocks").mkdir(parents=True, exist_ok=True)
cases = []
for i, n in enumerate(NAMES, 1):
    cid = f"T0{i}"
    text = (REPO / f"{n}.md").read_text(encoding="utf-8")
    L = text.split("\n")   # prompt-section rule of tests.md "How a case is run"
    b = next(k for k, l in enumerate(L) if l.startswith("## PROMPT BEGINS"))
    e = next(k for k, l in enumerate(L) if l.startswith("## PROMPT ENDS"))
    body = L[b + 1:e]
    body = body[1:] if body and body[0] == "" else body
    blk = "".join(x + "\n" for x in body)
    print(n, hashlib.sha256(blk.encode("utf-8")).hexdigest())
    (HERE / "suites/blocks" / f"AI-Governance-Academy-{n}.txt").write_text(blk, encoding="utf-8", newline="\n")
    checklist = text.split("\n## PROMPT ENDS", 1)[1].split("\n", 1)[1].strip()
    fi = list((t5.get(cid) or t5["T02"])["fail_indicators"])   # T08: same form as T02 to T07
    if cid == "T01":
        rule = t5[cid]["rule"]
        turns = ["Raw Client Material:\n\n" + raw]
    else:  # Mode A line quoted fresh for T02 to T08 (T5 quotes predate v1.14.x)
        mode_a = next(l for l in L if l.startswith("**MODE A – PROPOSAL.**"))
        rule = f'{n}.md Output Modes: "{mode_a}"'
        turn = "Client Profile Block:\n\n```\n" + profile + "```\n\n"
        turns = [turn + (NO_PRIOR + "\n\n" if cid == "T07" else "") + SELECT]
    fi.append(NEW_FI)
    pas = (f"tests.md pass condition for {cid}: {rows[cid]}. {na_rule}\n\n{guide}\n\n"
           f"Acceptance Checklist of {n}.md (the text after \"## PROMPT ENDS\", quoted in full):\n<<<\n{checklist}\n>>>")
    cases.append({"id": cid, "rule": rule, "turns": turns, "pass": pas, "fail_indicators": fi,
                  "system_files": [BLK.format(n)]})
man = {"suite": "academy-a5", "samples": 3, "repo": "AI-Governance-Academy",
       "system_files": [BLK.format(NAMES[0])],   # every case overrides; keeps summary.json to the eight blocks
       "tested_model": "claude-opus-5-5", "scorer_model": "claude-sonnet-5-5", "max_tokens": 16000,
       "acceptance": "ACCEPTANCE.md in the rolldabones repository (from 26 October 2026); a case run in several samples passes only when every sample passes. " + how,
       "cases": cases}
(HERE / "suites/academy-a5.json").write_text(json.dumps(man, indent=1, ensure_ascii=False), encoding="utf-8")
print("wrote suites/academy-a5.json and 8 blocks:", [c["id"] for c in cases])
