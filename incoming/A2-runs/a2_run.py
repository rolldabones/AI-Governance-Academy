#!/usr/bin/env python3
"""A2 suite runner, 20 October 2026 (KST): a1_run.py with run label A2, HEAD 11981fc (v1.14.1)
and three independent samples per case (manifest key "samples"); a case passes only when every sample passes.
Session tool, not shipped in any repository.

Runs each case of a suite manifest against a tested model with the repository's
published instruction text as the system prompt, then has a different model score
the transcript against the case's pass condition (D7: no model grades itself).
Writes one transcript per case, one score file per case and a summary per suite.

Usage:
    python3 t5_run.py --check                 # validate manifests, no API calls
    python3 t5_run.py [--only SUITE[,SUITE]] [--cases ID,ID] [--jobs 4]

Manifest (suites/<name>.json):
  {"suite": "<name>", "repo": "<clone folder>",
   "system_files": ["instructions.md", ...],   # concatenated in order; files after the
                                                # first are framed as attached knowledge
   "tested_model": "claude-opus-5-5", "scorer_model": "claude-sonnet-5-5",
   "max_tokens": 16000,
   "acceptance": "<the suite's acceptance rule, quoted>",
   "cases": [{"id": "C1", "rule": "<quoted rule>", "turns": ["<user turn>", ...],
              "pass": "<pass condition>", "fail_indicators": ["..."],
              "system_files": ["optional per-case override of the suite's system_files"]}]}
The key is read from ANTHROPIC_API_KEY and never printed or written.
"""
import argparse, concurrent.futures as cf, datetime, hashlib, json, os, re, subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent            # the GitHub Update folder
SUITES = HERE / "suites"
OUT = HERE / "out"
KST = datetime.timezone(datetime.timedelta(hours=9))
RUN = "A2"
EXPECTED_HEAD = "11981fc"   # AI-Governance-Academy v1.14.1
REF = "claude/brave-newton-hitgxj (PR #1, unmerged)"
SCORER_SYSTEM = (
    "You score one test case of a published AI instrument. You did not produce the response "
    "under test. Score strictly against the pass condition and the quoted rule, nothing else. "
    "A case passes only if every element of the pass condition is met and no fail indicator "
    "appears; partial compliance is FAIL. Where an element cannot be decided without judgment, "
    "decide it, say so in judgment_calls and state that another scorer could decide otherwise. "
    "Quote the response as evidence. Reply with one JSON object and nothing else: "
    '{"verdict": "PASS" | "FAIL" | "UNSCORABLE", "elements": [{"element": str, "met": bool, '
    '"evidence": str}], "fail_indicators_seen": [str], "judgment_calls": [str], "reasoning": str}'
)


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load(name: str) -> dict:
    m = json.loads((SUITES / f"{name}.json").read_text(encoding="utf-8"))
    for k in ("suite", "repo", "system_files", "tested_model", "scorer_model", "cases"):
        if k not in m:
            raise SystemExit(f"ERROR - Guardrail Violation: {name}.json lacks {k}")
    if m["tested_model"] == m["scorer_model"]:
        raise SystemExit(f"ERROR - Guardrail Violation: {name} scores with the tested model")
    repo = ROOT / m["repo"]
    for f in m["system_files"]:
        if not (repo / f).is_file():
            raise SystemExit(f"ERROR - Guardrail Violation: {m['repo']}/{f} missing")
    ids = [c["id"] for c in m["cases"]]
    if len(ids) != len(set(ids)):
        raise SystemExit(f"ERROR - Guardrail Violation: duplicate case IDs in {name}")
    for c in m["cases"]:
        for f in c.get("system_files", []):
            if not (repo / f).is_file():
                raise SystemExit(f"ERROR - Guardrail Violation: {m['repo']}/{f} missing ({c['id']})")
        if not c.get("turns") or not c.get("pass"):
            raise SystemExit(f"ERROR - Guardrail Violation: {name} {c.get('id')} lacks turns or pass")
    return m


def system_text(m: dict, files=None) -> str:
    repo = ROOT / m["repo"]
    parts = []
    for i, f in enumerate(files or m["system_files"]):
        t = (repo / f).read_text(encoding="utf-8")
        parts.append(t if i == 0 else f"\n\n# Attached knowledge file: {f}\n\n{t}")
    return "".join(parts)


def head(repo: Path) -> str:
    try:
        return subprocess.run(["git", "-C", str(repo), "rev-parse", "--short=7", "HEAD"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "Unknown"


def call(client, **kw):
    import anthropic
    for attempt in range(7):
        try:
            with client.messages.stream(**kw) as st:   # streaming: required by the SDK for long max_tokens
                return st.get_final_message()
        except (anthropic.RateLimitError, anthropic.APIConnectionError, anthropic.InternalServerError) as e:
            wait = min(120, 5 * 2 ** attempt)
            print(f"    retry {attempt + 1} in {wait}s ({type(e).__name__})", flush=True)
            time.sleep(wait)
        except anthropic.APIStatusError as e:
            if e.status_code in (429, 500, 502, 503, 529):
                wait = min(120, 5 * 2 ** attempt)
                print(f"    retry {attempt + 1} in {wait}s (HTTP {e.status_code})", flush=True)
                time.sleep(wait)
            else:
                raise
    raise RuntimeError("API retries exhausted")


def text_of(resp) -> str:
    return "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")


def run_case(client, m, sysmsg, c, outdir: Path):
    sid = f"{c['id']}-s{c['sample']}"
    msgs, log = [], []
    for i, turn in enumerate(c["turns"], 1):
        msgs.append({"role": "user", "content": turn})
        r = call(client, model=m["tested_model"], max_tokens=m.get("max_tokens", 16000),
                 system=sysmsg, messages=msgs)
        reply = text_of(r)
        msgs.append({"role": "assistant", "content": reply or "(no text)"})
        log.append({"turn": i, "user": turn, "reply": reply, "stop_reason": r.stop_reason,
                    "input_tokens": r.usage.input_tokens, "output_tokens": r.usage.output_tokens,
                    "model_returned": getattr(r, "model", m["tested_model"])})
    convo = "\n\n".join(f"### Turn {t['turn']}, user\n\n{t['user']}\n\n### Turn {t['turn']}, "
                        f"assistant (stop_reason {t['stop_reason']})\n\n{t['reply']}" for t in log)
    ask = (f"Instrument under test (system prompt as published):\n<<<\n{sysmsg}\n>>>\n\n"
           f"Case {c['id']}.\nRule quoted from the instrument: {c.get('rule', '(none)')}\n"
           f"Pass condition: {c['pass']}\nFail indicators: {json.dumps(c.get('fail_indicators', []))}\n"
           f"Suite acceptance rule: {m.get('acceptance', '(none)')}\n\nTranscript:\n<<<\n{convo}\n>>>")
    s = call(client, model=m["scorer_model"], max_tokens=16000, system=SCORER_SYSTEM,
             messages=[{"role": "user", "content": ask}])
    raw = text_of(s)
    try:
        score = json.loads(re.search(r"\{.*\}", raw, re.S).group(0))
    except Exception:
        score = {"verdict": "UNSCORABLE", "reasoning": "scorer reply was not JSON", "raw": raw}
    score.update({"case": sid, "scorer_model": m["scorer_model"],
                  "scorer_model_returned": getattr(s, "model", m["scorer_model"]),
                  "scorer_stop_reason": s.stop_reason,
                  "truncated": any(t["stop_reason"] == "max_tokens" for t in log)})
    if score["truncated"] and score.get("verdict") == "PASS":
        score["verdict"] = "UNSCORABLE"
        score["reasoning"] = "tested response truncated at max_tokens; " + score.get("reasoning", "")
    stamp = datetime.datetime.now(KST).strftime("%Y-%m-%d %H:%M KST")
    md = (f"# {m['suite']} {sid}\n\n**Tested model:** {m['tested_model']} · **Scorer:** "
          f"{m['scorer_model']} (LLM scoring, developer testing, not independent assurance) · "
          f"**Run:** {RUN}, {stamp} · **max_tokens:** {m.get('max_tokens', 16000)}\n\n"
          f"**Rule:** {c.get('rule', '')}\n\n**Pass condition:** {c['pass']}\n\n## Transcript\n\n{convo}\n\n"
          f"## Score\n\n**Verdict: {score.get('verdict')}.** {score.get('reasoning', '')}\n")
    (outdir / f"{sid}.md").write_text(md, encoding="utf-8")
    (outdir / f"{sid}.json").write_text(json.dumps({"log": log, "score": score}, indent=1,
                                                        ensure_ascii=False), encoding="utf-8")
    return sid, score.get("verdict"), score["truncated"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--only", default="")
    ap.add_argument("--cases", default="")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--max-tokens", type=int, default=0, help="override the manifest max_tokens for the tested model")
    ap.add_argument("--out-suffix", default="", help="write to out/<suite>-<suffix>/ so an earlier run is kept")
    a = ap.parse_args()
    h = head(ROOT / "AI-Governance-Academy")
    if h != EXPECTED_HEAD:
        raise SystemExit(f"ERROR - Guardrail Violation: AI-Governance-Academy HEAD {h}, expected {EXPECTED_HEAD}")
    names = [n.strip() for n in a.only.split(",") if n.strip()] or sorted(p.stem for p in SUITES.glob("*.json"))
    suites = [load(n) for n in names]
    total = sum(len(s["cases"]) for s in suites)
    for s in suites:
        print(f"{s['suite']}: {len(s['cases'])} cases, {s['tested_model']} scored by {s['scorer_model']}, "
              f"system {' + '.join(s['system_files'])} ({len(system_text(s))} chars)")
    print(f"{len(suites)} suites, {total} cases")
    if a.check:
        print("check OK, no API call made")
        return
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise SystemExit("ERROR - Guardrail Violation: ANTHROPIC_API_KEY not set")
    import anthropic
    client = anthropic.Anthropic(timeout=900, max_retries=0)
    only_cases = {x.strip() for x in a.cases.split(",") if x.strip()}
    for s in suites:
        repo = ROOT / s["repo"]
        if a.max_tokens:
            s["max_tokens"] = a.max_tokens
        outdir = OUT / (s["suite"] + (f"-{a.out_suffix}" if a.out_suffix else ""))
        outdir.mkdir(parents=True, exist_ok=True)
        sysmsg = system_text(s)
        cases = [dict(c, sample=k) for c in s["cases"] if not only_cases or c["id"] in only_cases
                 for k in range(1, s.get("samples", 1) + 1)]
        print(f"=== {s['suite']} ({len(cases)} cases)", flush=True)
        results = []
        with cf.ThreadPoolExecutor(max_workers=a.jobs) as ex:
            futs = {ex.submit(run_case, client, s, system_text(s, c.get("system_files")) if c.get("system_files") else sysmsg,
                              c, outdir): f"{c['id']}-s{c['sample']}" for c in cases}
            for f in cf.as_completed(futs):
                try:
                    cid, v, tr = f.result()
                except Exception as e:
                    cid, v, tr = futs[f], f"ERROR {type(e).__name__}", False
                print(f"  {cid}: {v}{' (truncated)' if tr else ''}", flush=True)
                results.append({"case": cid, "verdict": v, "truncated": tr})
        by_case = {}
        for r in results:
            by_case.setdefault(r["case"].rsplit("-s", 1)[0], []).append(r["verdict"])
        case_verdicts = {k: ("PASS" if len(v) == s.get("samples", 1) and all(x == "PASS" for x in v) else "FAIL")
                         for k, v in sorted(by_case.items())}
        summ = {"run": RUN, "suite": s["suite"], "repo": s["repo"], "head": head(repo), "ref": REF,
                "samples": s.get("samples", 1),
                "system_files": {f: sha(repo / f) for f in sorted(set(s["system_files"] + [x for c in s["cases"] for x in c.get("system_files", [])]))},
                "tested_model": s["tested_model"], "scorer_model": s["scorer_model"],
                "max_tokens": s.get("max_tokens", 16000),
                "finished": datetime.datetime.now(KST).isoformat(timespec="minutes"),
                "results": sorted(results, key=lambda r: r["case"]), "case_verdicts": case_verdicts}
        (outdir / "summary.json").write_text(json.dumps(summ, indent=1), encoding="utf-8")
        p = sum(r["verdict"] == "PASS" for r in results)
        print(f"  {s['suite']}: {p} of {len(results)} samples PASS; "
              f"{sum(v == 'PASS' for v in case_verdicts.values())} of {len(case_verdicts)} cases PASS", flush=True)


if __name__ == "__main__":
    main()
