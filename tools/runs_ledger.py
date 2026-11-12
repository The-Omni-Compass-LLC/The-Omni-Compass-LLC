#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""One ledger of every set the jump generator ran: its three digests, the run on GitHub that made it, and what was proved of it.

A set is 500 runs from one base seed (seed_k = base + k·0x9E3779B9 mod 2³², the stream mulberry32). The Python runs it
(tools/engine_runs.py: the brain's RK4, the compass law, the verdict; tools/core_runs.py: the core's Monte Carlo), the C++ harness
runs the same draws through the engine's C++ twins, and the live engine page's own code runs the same set again; each writes one
SHA-256 digest of its receipts, and the three must be one. This tool reads every record in results/engine_runs/ and
results/core_runs/ and, with no network and nothing run again, proves of each what the record itself can prove:

  the receipts' digest    recomputed here from the record's own 500 receipts: it must be the digest the record states
  the seeds               every receipt's seed recomputed from the base by the jump generator: it must be the receipt's
  the ladder              the digest of the first 1, 10, 100 and 500 runs recomputed from the receipts: each must be its rung's
  the C++ harness         its digest must be the Python's, at the whole set and at every rung, every run agreeing
  the page                where the record carries the page's digest, it must be the Python's, rung by rung
  the run on GitHub       the run's number, its commit and its address, and no run or base written twice

and joins the newest re-proof (tools/runs_reproof.py: every set run again on another machine, the Python, the C++ and the page).

  python3 tools/runs_ledger.py            write results/RUNS_LEDGER.json and results/RUNS_LEDGER.md
  python3 tools/runs_ledger.py --check    exit 1 when a set fails a proof above, or the ledger on file is not what the records give
"""
from __future__ import annotations

import collections
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
E_DIR, C_DIR, R_DIR = ROOT / "results" / "engine_runs", ROOT / "results" / "core_runs", ROOT / "results" / "runs_reproof"
OUT_JSON, OUT_MD = ROOT / "results" / "RUNS_LEDGER.json", ROOT / "results" / "RUNS_LEDGER.md"
OWN_RANGES = "the engine's own ranges"
NOT_GITHUB = "not made on GitHub"


def version(text) -> str:
    m = re.search(r"omni-v\d+", str(text or ""))
    return m.group(0) if m else "not named"


def engine_set(path: Path) -> dict:
    from tools import engine_runs as E
    d = json.loads(path.read_text(encoding="utf-8"))
    rs, n, base = d.get("receipts") or [], d.get("runs"), d.get("base")
    cpp, page, gh, ladder = d.get("cpp") or {}, d.get("page") or {}, d.get("github") or {}, d.get("ladder") or []
    bad = []
    if not path.with_suffix(".md").exists():
        bad.append("the record's page (.md) is missing")
    if len(rs) != n:
        bad.append(f"{len(rs)} receipts for {n} runs")
    if E.digest(rs) != d.get("digest"):
        bad.append("the receipts' digest is not the digest the record states")
    if any(r.get("k") != k or r.get("seed") != E.jump(base, k) for k, r in enumerate(rs)):
        bad.append("a receipt's seed is not the jump generator's")
    for g in ladder:
        if E.digest(rs[:g["runs"]]) != g.get("digest"):
            bad.append(f"the rung of {g['runs']} is not its receipts' digest")
        if "cpp_digest" in g and g["cpp_digest"] != g["digest"]:
            bad.append(f"the C++ harness differs at the rung of {g['runs']}")
        if "page_digest" in g and g["page_digest"] != g["digest"]:
            bad.append(f"the page differs at the rung of {g['runs']}")
    if cpp and (cpp.get("digest") != d.get("digest") or cpp.get("same") is not True or cpp.get("agree") != n):
        bad.append("the C++ harness's digest is not the Python's")
    if page and (page.get("digest") != d.get("digest") or page.get("same") is not True):
        bad.append("the page's digest is not the Python's")
    return {"kind": "engine", "file": str(path.relative_to(ROOT)), "base": base, "runs": n, "written": d.get("written"),
            "engine": version(d.get("engine")), "digest": d.get("digest"), "draws": d.get("inputs_digest"),
            "cpp": cpp.get("digest"), "cpp_largest_difference": cpp.get("largest_difference"),
            "page": page.get("digest"), "page_sha256": page.get("page_sha256"),
            "ladder": [g["runs"] for g in ladder], "ladder_cpp": bool(ladder) and all("cpp_digest" in g for g in ladder),
            "ladder_page": bool(ladder) and all("page_digest" in g for g in ladder),
            "allowed": sum(r.get("allowed", 0) for r in rs),
            "run_id": gh.get("run_id"), "commit": gh.get("commit"), "ref": gh.get("ref"), "url": gh.get("url"), "failed": bad}


def core_set(path: Path) -> dict:
    d = json.loads(path.read_text(encoding="utf-8"))
    cpp, page, gh = d.get("cpp") or {}, d.get("page") or {}, d.get("github") or {}
    bad = []
    if not path.with_suffix(".md").exists():
        bad.append("the record's page (.md) is missing")
    if not re.fullmatch(r"[0-9a-f]{64}", str(d.get("digest") or "")):
        bad.append("no digest")
    if cpp and (cpp.get("digest") != d.get("digest") or cpp.get("same") is not True or cpp.get("agree") != cpp.get("of")):
        bad.append("the C++ harness's digest is not the Python's")
    if page and (page.get("digest") != d.get("digest") or page.get("same") is not True):
        bad.append("the page's digest is not the Python's")
    return {"kind": "core", "file": str(path.relative_to(ROOT)), "base": d.get("base"), "runs": d.get("runs"), "written": d.get("written"),
            "system": (d.get("system") or {}).get("name"), "digest": d.get("digest"), "draws": d.get("inputs_digest"),
            "cpp": cpp.get("digest"), "page": page.get("digest"),
            "run_id": gh.get("run_id"), "commit": gh.get("commit"), "ref": gh.get("ref"), "url": gh.get("url"), "failed": bad}


def reproof() -> dict:
    """The newest re-proof on file: {"written", "machine", "by": {record file: its row}}; empty when none is on file."""
    files = sorted(R_DIR.glob("REPROOF_*.json")) if R_DIR.is_dir() else []
    if not files:
        return {}
    d = json.loads(files[-1].read_text(encoding="utf-8"))
    return {"file": str(files[-1].relative_to(ROOT)), "written": d.get("written"), "machine": d.get("machine") or {},
            "by": {r["file"]: r for r in d.get("sets") or []}}


def build() -> dict:
    eng = sorted((engine_set(p) for p in E_DIR.glob("ENGINE_RUNS_*.json")), key=lambda r: (r["written"] or "", r["base"]), reverse=True)
    core = sorted((core_set(p) for p in C_DIR.glob("CORE_RUNS_*.json")), key=lambda r: (r["written"] or "", r["base"]), reverse=True)
    cross = []
    for what, rows, key in (("base", eng, "base"), ("digest", eng, "digest"), ("GitHub run", eng, "run_id")):
        seen = collections.Counter(r[key] for r in rows if r[key] is not None)
        cross += [f"engine sets: the {what} {k} is written {n} times" for k, n in seen.items() if n > 1]
    seen = collections.Counter((r["base"], r["system"]) for r in core)
    cross += [f"core sets: the base {k[0]} is written {n} times" for k, n in seen.items() if n > 1]
    rp = reproof()
    for r in eng + core:
        x = (rp.get("by") or {}).get(r["file"])
        if x:
            r["again"] = {k: x.get(k) for k in ("python_same", "cpp_same", "page_same", "draws_same", "ladder_same", "page_ladder_same",
                                                "own_system", "own_python_same", "own_commit", "error") if x.get(k) is not None}
    return {"tool": "tools/runs_ledger.py", "engine_sets": eng, "core_sets": core, "cross": cross,
            "reproof": {k: rp[k] for k in ("file", "written", "machine") if k in rp}}


def tally(d: dict) -> dict:
    e, c = d["engine_sets"], d["core_sets"]
    own = [r for r in c if r["system"]]
    ag = lambda rows, k: sum(1 for r in rows if (r.get("again") or {}).get(k) is True)
    tried = lambda rows, k: sum(1 for r in rows if (r.get("again") or {}).get(k) is not None)
    return {"engine": len(e), "engine_runs": sum(r["runs"] or 0 for r in e), "engine_cpp": sum(1 for r in e if r["cpp"]),
            "engine_page": sum(1 for r in e if r["page"]), "engine_ladder": sum(1 for r in e if r["ladder"]),
            "engine_github": sum(1 for r in e if r["run_id"]), "engine_failed": sum(1 for r in e if r["failed"]),
            "core": len(c), "core_own": len(own), "core_cpp": sum(1 for r in c if r["cpp"]), "core_page": sum(1 for r in c if r["page"]),
            "core_github": sum(1 for r in c if r["run_id"]), "core_failed": sum(1 for r in c if r["failed"]),
            "engines": dict(sorted(collections.Counter(r["engine"] for r in e).items(), key=lambda kv: -int(re.sub(r"\D", "", kv[0]) or 0))),
            "refs": dict(collections.Counter(r["ref"] or NOT_GITHUB for r in e)),
            "again": {f"{kind}_{k}": [ag(rows, f"{k}_same"), tried(rows, f"{k}_same")] for kind, rows in (("engine", e), ("core", c))
                      for k in ("python", "cpp", "page")}}


def short(h) -> str:
    return f"`{h[:12]}…`" if h else "not recorded"


def render(d: dict) -> str:
    from tools.legal import stamp
    from tools.company_attribution import normalize
    t, rp = tally(d), d.get("reproof") or {}
    e, c = d["engine_sets"], d["core_sets"]
    fails = [r for r in e + c if r["failed"]]
    first = min((r["written"] for r in e if r["written"]), default="")[:10]
    last = max((r["written"] for r in e if r["written"]), default="")[:10]
    L = ["# The jump generator's ledger: every set, its three digests and the run that made it", "",
         "Written by `tools/runs_ledger.py` from the records themselves (`results/engine_runs/`, `results/core_runs/`), with no network "
         "and nothing run again; `--check` (run by `verify.py`) fails a push where a set fails a proof below or this page is not what "
         "the records give. Our own models (class S): a set proves that three implementations of one mechanism compute the same "
         "numbers; it is never a benchmark result. Run and checked by Dubra Software Inc. / The Omni-Compass LLC's own code; no outside "
         "party has reviewed or approved it.", "",
         "## What a set is", "",
         "One base seed, 500 runs. Run k draws its seed from the jump generator, seed_k = base + k·0x9E3779B9 mod 2³², and feeds a "
         "mulberry32 stream through the mechanism. Three implementations run the same set and each writes one SHA-256 digest of its "
         "receipts (every number at six decimals, one line a run): **the Python** (`tools/engine_runs.py`: 288 decisions of the "
         "brain by RK4, 80 steps of the compass law, one give-back trial judged by the verdict; `tools/core_runs.py`: the core's "
         "Monte Carlo, four ways), **the C++ harness** (`cpp/tools/engine_runs.cpp`, `cpp/tools/core_runs.cpp`, the engine's C++ "
         "twins, fed the Python's draws) and **the live engine page's own code** (its ported engine and loop, run in node on "
         "GitHub and in the reader's browser). The three digests must be one, at the whole set and at its first 1, 10 and 100 runs "
         "(the ladder).", "",
         "## Where it stands", "",
         f"- **{t['engine']} sets of the engine's runs** ({t['engine_runs']:,} runs, {first} to {last}) and **{t['core']} sets of the "
         f"core's Monte Carlo** ({t['core_own']} of them a reader's own system).",
         f"- **The receipts' own digest**: recomputed here from each record's 500 receipts, with every seed recomputed from its base "
         f"by the jump generator and every rung of its ladder: {t['engine'] - t['engine_failed']} of {t['engine']} engine sets pass"
         + (f"; **{t['engine_failed']} fail**, named below." if t["engine_failed"] else "."),
         f"- **The C++ harness** wrote its digest into {t['engine_cpp']} of the {t['engine']} engine sets and {t['core_cpp']} of the "
         f"{t['core']} core sets; in every one it is the Python's (a set made before the harness existed carries none).",
         f"- **The page's own digest** stands in the record of {t['engine_page']} engine sets and {t['core_page']} core sets. On "
         "GitHub the page's own code has run every run of every set since 21 October (`engine-runs.yml`) and the run fails if it differs, but the record kept only "
         "the Python's and the C++ harness's digests until `tools/engine_runs.py --verify --all` began writing the page's beside them, rung by rung; "
         "for the sets made before that, the page's digest is the one the re-proof below computed.",
         f"- **The run on GitHub**: {t['engine_github']} of the {t['engine']} engine sets name the run that made them, its commit and "
         f"its address ({', '.join(f'{n} on `{k}`' for k, n in t['refs'].items() if k != NOT_GITHUB)}"
         + (f"; {t['refs'][NOT_GITHUB]} made before the runs were linked to GitHub" if t["refs"].get(NOT_GITHUB) else "")
         + "); no base, digest or run stands twice"
         + ("." if not d["cross"] else f": **{len(d['cross'])} do**, named below."),
         "- **By engine** (each set keeps the engine it ran on): " + ", ".join(f"{k} {n}" for k, n in t["engines"].items()) + "."]
    if rp:
        a, m = t["again"], rp.get("machine") or {}
        L += ["", "## Run again on another machine", "",
              f"`tools/runs_reproof.py` ran every recorded set again from its base on a machine that is not GitHub's ({rp.get('written')}, "
              f"`{rp.get('file')}`: {m.get('platform')}, Python {m.get('python')}, {m.get('compiler')}, node {m.get('node')}, the checkout "
              f"`{(m.get('checkout') or '')[:12]}` on {m.get('engine')}) and compared each digest with the record's:", "",
              "| Run again | The engine's runs | The core's Monte Carlo |", "|---|---:|---:|",
              f"| The Python gives the record's digest | {a['engine_python'][0]} of {a['engine_python'][1]} | {a['core_python'][0]} of {a['core_python'][1]} |",
              f"| The C++ harness gives the record's digest | {a['engine_cpp'][0]} of {a['engine_cpp'][1]} | {a['core_cpp'][0]} of {a['core_cpp'][1]} |",
              f"| The page's own code gives the record's digest | {a['engine_page'][0]} of {a['engine_page'][1]} | {a['core_page'][0]} of {a['core_page'][1]} |", ""]
        other = [r for r in e if (r.get("again") or {}).get("python_same") is False]
        own = [r for r in c if (r.get("again") or {}).get("own_system")]
        if other:
            ok = sum(1 for r in other if r["again"].get("own_python_same") is True)
            L += [f"{len(other)} engine sets were made on an engine whose law differs from the checkout's, so the checkout gives another "
                  f"digest: they read \"another engine's law\" below, and {ok} of them give their record's digest when run again from "
                  "their own commit.", ""]
        if own:
            L += [f"{len(own)} core sets are a reader's own system: their ranges are their records', and they are not run again here.", ""]
    if fails or d["cross"]:
        L += ["## What fails", ""] + [f"- `{r['file']}`: {'; '.join(r['failed'])}" for r in fails] + [f"- {x}" for x in d["cross"]] + [""]

    def again(r, kinds=("python", "cpp", "page")):
        g = r.get("again") or {}
        if g.get("own_system"):
            return "a reader's own system"
        if g.get("error"):
            return "could not be run again"
        if not g:
            return "not yet run again"
        if g.get("python_same") is False:
            return "another engine's law" + ("; its own commit gives the record's digest" if g.get("own_python_same") else "")
        return ", ".join(f"{k} {'yes' if g.get(f'{k}_same') else 'NO'}" for k in kinds if g.get(f"{k}_same") is not None)

    L += ["## Every set of the engine's runs, the newest first", "",
          "| Base | Written (UTC) | Engine | The Python's digest | The C++ harness's | The page's, in the record | The ladder | Run on GitHub | Run again: the same digest |",
          "|---:|---|---|---|---|---|---|---|---|"]
    for r in e:
        lad = ("not read" if not r["ladder"] else "/".join(map(str, r["ladder"]))
               + (", C++" if r["ladder_cpp"] else "") + (", page" if r["ladder_page"] else ""))
        run = f"[{r['run_id']}]({r['url']}) `{(r['commit'] or '')[:8]}` {r['ref']}" if r["run_id"] else "not made on GitHub"
        L.append(f"| {r['base']} | {(r['written'] or '')[:16].replace('T', ' ')} | {r['engine']} | {short(r['digest'])} | "
                 f"{'the same' if r['cpp'] == r['digest'] else 'not recorded' if not r['cpp'] else '**DIFFERENT**'} | "
                 f"{'the same' if r['page'] and r['page'] == r['digest'] else 'not recorded' if not r['page'] else '**DIFFERENT**'} | {lad} | {run} | {again(r)} |")
    L += ["", "## Every set of the core's Monte Carlo, the newest first", "",
          "| Base | Written (UTC) | System | The Python's digest | The C++ harness's | The page's, in the record | Run on GitHub | Run again: the same digest |",
          "|---:|---|---|---|---|---|---|---|"]
    for r in c:
        run = f"[{r['run_id']}]({r['url']}) `{(r['commit'] or '')[:8]}` {r['ref']}" if r["run_id"] else "not made on GitHub"
        L.append(f"| {r['base']} | {(r['written'] or '')[:16].replace('T', ' ')} | {r['system'] or OWN_RANGES} | {short(r['digest'])} | "
                 f"{'the same' if r['cpp'] == r['digest'] else 'not recorded' if not r['cpp'] else '**DIFFERENT**'} | "
                 f"{'the same' if r['page'] and r['page'] == r['digest'] else 'not recorded' if not r['page'] else '**DIFFERENT**'} | {run} | {again(r)} |")
    L += ["", "To run a set again yourself: `python3 tools/engine_runs.py --runs 500 --base <base> --cpp cpp/build/oc_engine_runs --out my_set.json`, "
          "then compare its digest with this page's; `python3 tools/engine_runs.py --verify docs/engine/OMNI_COMPASS_LIVE_ENGINE.html --all "
          "--runs 500 --base <base> --out my_set.json` runs the page's own code on the same set and writes its digest into `my_set.json`. One command "
          "does all of it and prints the three digests side by side: `scripts/prove_runs.sh [BASE]`."]
    return normalize("\n".join(stamp(L)) + "\n")


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    d = build()
    js, md = json.dumps(d, indent=1, ensure_ascii=False) + "\n", render(d)
    fails = [f"{r['file']}: {'; '.join(r['failed'])}" for r in d["engine_sets"] + d["core_sets"] if r["failed"]] + d["cross"]
    if "--check" in argv:
        stale = not OUT_JSON.exists() or OUT_JSON.read_text(encoding="utf-8") != js or not OUT_MD.exists() or OUT_MD.read_text(encoding="utf-8") != md
        for f in fails:
            print("FAIL", f)
        print(f"runs_ledger: {len(d['engine_sets'])} engine sets and {len(d['core_sets'])} core sets; {len(fails)} fail; the ledger on file "
              + ("is what the records give" if not stale else "is NOT what the records give: python3 tools/runs_ledger.py"))
        return 1 if fails or stale else 0
    OUT_JSON.write_text(js, encoding="utf-8")
    OUT_MD.write_text(md, encoding="utf-8")
    t = tally(d)
    print(f"results/RUNS_LEDGER.md: {t['engine']} engine sets ({t['engine_failed']} fail), {t['core']} core sets ({t['core_failed']} fail), "
          f"{len(d['cross'])} written twice")
    return 0


if __name__ == "__main__":
    sys.exit(main())
