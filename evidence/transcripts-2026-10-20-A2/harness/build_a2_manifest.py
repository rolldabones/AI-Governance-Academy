#!/usr/bin/env python3
"""Builds suites/academy-a2.json for run A2 (20 October 2026, KST) from the T5 manifest,
tests.md (v1.14.1, HEAD 11981fc) and the templates' Acceptance Checklists. Reads the clone; writes only here."""
import json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
REPO = ROOT / "AI-Governance-Academy"
T5 = json.loads((ROOT / "Claude Outputs/T5-runs/suites/academy-mode-a.json").read_text(encoding="utf-8"))
NAMES = ["01-client-intake", "02-executive-briefing", "03-executive-workshop", "04-practitioner-academy",
         "05-implementation-accelerator", "06-guided-ai-grc-build", "07-fractional-advisor",
         "08-one-workflow-thirty-days"]
BLK = "../Claude Outputs/A2-runs/suites/blocks/AI-Governance-Academy-{}.txt"
NEW_FI = ("A statement of a Client fact that Part 2 of the fixture (the Client Profile Block) does not "
          "contain, including any incumbent register, process, control or record beyond the framework names")
tests = (REPO / "tests.md").read_text(encoding="utf-8")
cases_sec = tests.split("\n## Cases\n", 1)[1].split("\n## Known defects\n", 1)[0]   # Cases table only, not Last run
rows = {m[0]: m[1].strip() for m in re.findall(r"^\| (T0\d) \|[^|]*\|[^|]*\|(.*)\|\s*$", cases_sec, re.M)}
assert sorted(rows) == [f"T0{i}" for i in range(1, 9)], rows.keys()
assert all(v.startswith("Checklist items") or v.startswith("Acceptance Checklist items") for v in rows.values()), rows
na_rule = next(l for l in tests.split("\n") if l.startswith("An item the checklist scopes"))
how = next(l for l in tests.split("\n") if l.startswith("**How a case is run.**"))
t5 = {c["id"]: c for c in T5["cases"]}
cases = []
for i, n in enumerate(NAMES, 1):
    cid = f"T0{i}"
    text = (REPO / f"{n}.md").read_text(encoding="utf-8")
    checklist = text.split("\n## PROMPT ENDS", 1)[1].split("\n", 1)[1].strip()
    if cid in t5:
        rule, turns, fi = t5[cid]["rule"], t5[cid]["turns"], list(t5[cid]["fail_indicators"])
    else:  # T08: same form as T02 to T07
        turns = t5["T02"]["turns"]
        fi = list(t5["T02"]["fail_indicators"])
    if cid in ("T02", "T08"):  # T02's Mode A line changed at v1.14.1: quote it fresh, as for T08
        mode_a = next(l for l in text.split("\n") if l.startswith("**MODE A – PROPOSAL.**"))
        rule = f'{n}.md Output Modes: "{mode_a}"'
    fi.append(NEW_FI)
    pas = (f"tests.md pass condition for {cid}: {rows[cid]}. {na_rule}\n\n"
           f"Acceptance Checklist of {n}.md (the text after \"## PROMPT ENDS\", quoted in full):\n<<<\n{checklist}\n>>>")
    cases.append({"id": cid, "rule": rule, "turns": turns, "pass": pas, "fail_indicators": fi,
                  "system_files": [BLK.format(n)]})
man = {"suite": "academy-a2", "samples": 3, "repo": "AI-Governance-Academy",
       "system_files": [BLK.format(NAMES[0])],   # every case overrides; keeps summary.json to the eight blocks
       "tested_model": "claude-opus-5-5", "scorer_model": "claude-sonnet-5-5", "max_tokens": 16000,
       "acceptance": "tests.md (v1.14.1): \"A run passes when every case it exercises passes; a case not "
                     "exercised in a run is recorded as not run, never as passed.\" " + how,
       "cases": cases}
(HERE / "suites").mkdir(exist_ok=True)
(HERE / "suites/academy-a2.json").write_text(json.dumps(man, indent=1, ensure_ascii=False), encoding="utf-8")
print("wrote suites/academy-a2.json:", [c["id"] for c in cases])
