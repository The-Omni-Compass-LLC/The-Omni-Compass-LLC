#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The static security scan of every Python file that runs, with every finding of high or medium severity reviewed by
name (docs/SECURITY_SCAN.md).

Bandit (PyCQA) reads the code for patterns that are often unsafe: a shell given a string, a hash or a TLS context weaker
than it could be, a folder anyone may write, a fixed /tmp path, a URL opened without its scheme checked. A pattern is not
a flaw by itself, so every finding of high or medium severity is either fixed or listed in REVIEWED with the reason it
stands. The scan fails when a finding of high or medium severity appears that no review names, and when a review names a
finding that is gone (so the list never keeps a stale reason). Findings of low severity are counted by kind.

  python3 tools/security_scan.py           scan, write docs/SECURITY_SCAN.md and results/SECURITY_SCAN.json
  python3 tools/security_scan.py --check   scan; exit 1 on an unreviewed or stale finding, or when the page's findings of
                                           high or medium severity are not the scan's (1 November: the lines scanned, the line
                                           numbers and the low counts move with every push of code, so they are refreshed
                                           whenever the page is written and never fail the check)
"""
from __future__ import annotations

import argparse, collections, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import stamp  # noqa: E402

PAGE = ROOT / "docs" / "SECURITY_SCAN.md"
DATA = ROOT / "results" / "SECURITY_SCAN.json"
TARGETS = ["omni_controller", "omnicompass", "realms", "tools", "scripts", "fleet", "k8s_controlplane"]
OPERATOR = ("the command is the operator's own configuration, run with the governor's own rights; it never holds text "
            "read from the cluster or the network, and an operator may use a pipe in it")
FIXED_URL = "every URL it opens is an https address written in the code or the operator's own endpoint, never one read from data"
CI_TMP = "a path on the benchmark's own throwaway machine (a GitHub runner), never on a machine Omni-Compass governs"
REVIEWED = {
    ("B602", "omni_controller/muscles.py"): OPERATOR + " (run_operator_cmd: the site power reading, --power-cmd, and a "
                                            "muscle's read command in the operator's wiring file; from omni-v14 a command "
                                            "with nothing only a shell reads runs without one, so the shell is reached only "
                                            "for a pipe, a redirect or a variable the operator wrote)",
    ("B310", "tools/tour_voice.py"): FIXED_URL + " (the tour voice's two model files from one fixed GitHub release, each checked "
                                     "against its pinned SHA-256 and deleted when it differs; run by hand or by the live page's "
                                     "build, never by the governor)",
    ("B103", "tools/run_pgbench.py"): "PgBouncer's folder on the benchmark machine is owned by postgres and set 0o755: others "
                                      "may read and enter it, never write it",
    ("B108", "k8s_controlplane/mechanism_harness.py"): CI_TMP,
    ("B108", "omni_controller/controller.py"): "a default file name for the audit log in the working folder, not /tmp; the "
                                               "operator sets --audit",
    ("B108", "omni_controller/gpu_compass.py"): "a default file name for the audit log, as above",
    ("B108", "omni_controller/gpu_governor.py"): "a default file name for the audit log, as above",
    ("B108", "omnicompass/master.py"): "the switch's registry folder under the operator's runtime folder; the watchdog trusts "
                                       "only its own registry (docs/THREAT_MODEL.md, T4)",
    ("B108", "scripts/dispatch_grid.py"): CI_TMP,
    ("B108", "tools/gpu_actuator_watchdog.py"): CI_TMP,
    ("B108", "tools/omni_control.py"): "the control panel's default kill file, under /tmp/omni-compass on the operator's own "
                                       "machine, where the panel and the governor it starts run as one user; the operator sets "
                                       "it with --kill-file or OMNI_CONTROL_KILL_FILE, and the governor reads only the file the "
                                       "panel hands it (docs/CONTROL_PLANE.md)",
    ("B108", "tools/run_kafka.py"): CI_TMP,
    ("B108", "tools/run_redis.py"): CI_TMP,
    ("B310", "omni_controller/controller.py"): FIXED_URL + " (the operator's metrics endpoint)",
    ("B310", "scripts/aks_kubectl.py"): FIXED_URL,
    ("B310", "scripts/dispatch_grid.py"): FIXED_URL + " (the GitHub API)",
    ("B310", "scripts/latency_probe.py"): FIXED_URL + " (the service under test)",
    ("B310", "scripts/restart_aks.py"): FIXED_URL + " (the GitHub API)",
    ("B310", "tools/artifact_legal.py"): FIXED_URL + " (raw.githubusercontent.com)",
    ("B310", "tools/health_watch.py"): FIXED_URL + " (the GitHub API)",
    ("B310", "tools/omni_alert_bridge.py"): FIXED_URL + " (the operator's own control panel, --panel)",
    ("B310", "tools/orchestrator_show.py"): FIXED_URL + " (the showing's own agents on 127.0.0.1, their ports written in the code)",
    ("B310", "tools/llm_workload.py"): FIXED_URL + " (the model server under test)",
    ("B310", "tools/prom_feed.py"): FIXED_URL + " (the operator's Prometheus)",
    ("B310", "tools/run_ycsb.py"): FIXED_URL + " (the YCSB release, checked against its published digest)",
    ("B310", "tools/trace_schedule.py"): FIXED_URL + " (the public trace)",
    ("B323", "tools/wall_meter.py"): "an unverified TLS context only when the operator sets REDFISH_INSECURE=1 for a "
                                     "management controller with its own self-signed certificate",
    ("B506", "scripts/restart_aks.py"): "yaml.load with BaseLoader, which builds strings only (stricter than SafeLoader), on "
                                        "the repository's own workflow files",
    ("B608", "tools/run_pgbench.py"): "SQL built from the benchmark's own fixed names to create its throwaway database, never "
                                      "from input",
    ("B608", "tools/run_sysbench.py"): "SQL built from the benchmark's own account name (SYSBENCH_USER, set by its own "
                                       "workflow) and its fixed statement names, read on the benchmark's throwaway database; "
                                       "never text read from the network",
    ("B610", "tools/live_reps.py"): "not Django: a local function named extra() inside an f-string",
}


def scan() -> dict:
    p = subprocess.run([sys.executable, "-m", "bandit", "-q", "-r", *TARGETS, "-f", "json"], capture_output=True,
                       text=True, cwd=ROOT)
    if not p.stdout.strip():
        raise SystemExit(f"bandit gave no report: {p.stderr.strip()[-400:]}")
    return json.loads(p.stdout)


def judge(report: dict) -> dict:
    found = collections.defaultdict(list)
    low = collections.Counter()
    for r in report["results"]:
        if r["issue_severity"] in ("HIGH", "MEDIUM"):
            found[(r["test_id"], r["filename"])].append(r)
        else:
            low[f"{r['test_id']} {r['test_name']}"] += 1
    unreviewed = sorted(k for k in found if k not in REVIEWED)
    stale = sorted(k for k in REVIEWED if k not in found)
    rows = [{"test": k[0], "file": k[1], "severity": max(x["issue_severity"] for x in v), "count": len(v),
             "lines": sorted(x["line_number"] for x in v), "what": v[0]["issue_text"], "why": REVIEWED.get(k, "")}
            for k, v in sorted(found.items())]
    return {"lines_scanned": report["metrics"]["_totals"]["loc"],
            "high": sum(1 for r in report["results"] if r["issue_severity"] == "HIGH"),
            "medium": sum(1 for r in report["results"] if r["issue_severity"] == "MEDIUM"),
            "low": sum(low.values()), "low_by_kind": dict(sorted(low.items(), key=lambda kv: -kv[1])),
            "reviewed": rows, "unreviewed": [list(k) for k in unreviewed], "stale": [list(k) for k in stale]}


def substance(text: str) -> str:
    """The page as the check reads it (1 November 2026): every finding of high or medium severity, its count and its review,
    without the parts every push of code moves (the lines scanned, the line numbers, the low counts). With the scan's step
    able to fail (pipefail, 31 October), the whole page read as out of date after any push that shifted a line."""
    import re
    text = re.sub(r"; [0-9,]+ lines\)", ")", text)
    text = re.sub(r"\| (\d+) \([0-9, ]+\) \|", r"| \1 |", text)
    text = re.sub(r"[0-9,]+ of low severity", "of low severity", text)
    head, sep, rest = text.partition("## Findings of low severity, by kind")
    tail = rest.split("The low-severity kinds", 1)[1] if "The low-severity kinds" in rest else rest
    return head + sep + tail


def page(j: dict) -> str:
    L = ["# The static security scan", "",
         "Generated by `python3 tools/security_scan.py` (Bandit, the Python security linter of PyCQA) over every Python file "
         f"that runs ({', '.join(f'`{t}/`' for t in TARGETS)}; {j['lines_scanned']:,} lines). The workflow "
         "`security-scan.yml` runs it on every push to main that touches code, and every week, with `pip-audit` over every "
         "pinned dependency; it fails on a finding of high or medium severity that no review below names.", "",
         f"**{j['high']} finding{'' if j['high'] == 1 else 's'} of high severity and {j['medium']} of medium severity, every one reviewed below; "
         f"{j['low']} of low severity, counted by kind.** Fixed on 19 October: a world-writable PgBouncer folder (now owned "
         "by postgres, 0o755) and the MD5 that PostgreSQL's own password method defines, now marked as not used for "
         "security. Fixed in omni-v14 (21 October): the operator's own commands (the site power reading, a muscle's read "
         "command, a wall meter's) run without a shell unless they hold a pipe, a redirect or a variable, so the governor's "
         "site power reading no longer reaches a shell at all and one high finding is gone. Fixed on 3 November: the wall "
         "meter's command (`tools/wall_meter.py`, `cmd:`) runs without a shell at all, a pipe included (each stage's output "
         "into the next), and anything else only a shell reads is refused with the reason, so a second high finding is "
         "gone.", "",
         "## Every finding of high or medium severity, and why it stands", "",
         "| Check | File | Severity | Findings (lines) | Why it stands |", "|---|---|---|---|---|"]
    for r in j["reviewed"]:
        why = r["why"] or "**not reviewed**"
        L.append(f"| {r['test']} ({r['what'].rstrip('.')}) | `{r['file']}` | {r['severity'].lower()} | {r['count']} "
                 f"({', '.join(map(str, r['lines']))}) | {why} |")
    L += ["", "## Findings of low severity, by kind", "", "| Kind | Findings |", "|---|---:|"]
    L += [f"| {k} | {n} |" for k, n in j["low_by_kind"].items()]
    L += ["", "The low-severity kinds are the patterns of a harness that drives other programs: a subprocess started with a "
          "list of arguments and no shell (B603, B607), the subprocess module imported (B404), an assert in a test helper "
          "(B101), a pseudo-random number for a modelled load (B311), and the throwaway passwords of the benchmark's own "
          "local databases (B105, B107).", ""]
    if j["unreviewed"] or j["stale"]:
        L += ["## Not reviewed", ""] + [f"- unreviewed: {t} in `{f}`" for t, f in j["unreviewed"]] + \
             [f"- stale review (finding gone): {t} in `{f}`" for t, f in j["stale"]] + [""]
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    j = judge(scan())
    text = "\n".join(stamp(page(j).split("\n"))) + "\n"
    bad = j["unreviewed"] or j["stale"]
    if a.check:
        current = PAGE.exists() and substance(PAGE.read_text(encoding="utf-8")) == substance(text)
        print(f"security scan: {j['high']} high, {j['medium']} medium (unreviewed {len(j['unreviewed'])}, stale "
              f"{len(j['stale'])}), {j['low']} low; page {'current' if current else 'out of date (python3 tools/security_scan.py)'}")
        return 1 if bad or not current else 0
    PAGE.write_text(text, encoding="utf-8")
    DATA.write_text(json.dumps(j, indent=1) + "\n", encoding="utf-8")
    print(f"security scan: {j['high']} high, {j['medium']} medium, {j['low']} low -> {PAGE.relative_to(ROOT)}"
          + (f"; NOT REVIEWED: {j['unreviewed']}; STALE: {j['stale']}" if bad else ""))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
