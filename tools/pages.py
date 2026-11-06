#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The pages a person would have been sent, native against Omni-Compass on native: the oversight line's second reading,
counted from the raw files of its own tables by the rule written before the first count
(docs/OVERSIGHT_PAGES_PREREGISTRATION.md, committed on 4 November 2026 ahead of this tool's first run).

A person on call is paid by the page, not by the minute. Every repetition of every arm kept each sampled request's response
time (latency.csv) and its measured window; the bad minutes are the oversight line's alert minutes exactly (the 95th
percentile of the minute, a failed request counted over, over the line), and a page opens after FOR bad minutes in a row
and closes after RESET clean minutes in a row. Before any page is counted, the recount of the bad minutes must give each
run's printed alert minutes and their 95% interval; a run that does not is named and left out, never fitted.

    python3 tools/pages.py           counts from the branch raw (each file read through git, nothing checked out) and writes
                                     results/OVERSIGHT_PAGES.json and results/OVERSIGHT_PAGES.md
    python3 tools/pages.py --check   writes the page again from the record alone (no network) and exits 1 where it differs
"""
from __future__ import annotations

import argparse
import json
import math
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))
from legal import stamp  # noqa: E402
from readings import LOWER, three_run_reading  # noqa: E402
from omnicompass.student_t import t95  # noqa: E402
import oversight  # noqa: E402

RAW = "refs/remotes/origin/raw"
OUT_MD, OUT_JSON = ROOT / "results" / "OVERSIGHT_PAGES.md", ROOT / "results" / "OVERSIGHT_PAGES.json"
PREREG = "docs/OVERSIGHT_PAGES_PREREGISTRATION.md"
LINE_MS = 500.0                       # the line in all thirteen tables (no workflow behind them sets SLO_MS to another)
PRIMARY = (1, 5)                      # FOR 1 bad minute, RESET 5 clean minutes (Alertmanager's default resolve_timeout)
RULES = ((1, 5), (1, 15), (2, 5), (2, 15), (5, 5), (5, 15))   # the sensitivity declared with it, the primary first
Z95 = 1.959964                        # the normal point for a sum of the tables' differences, as the oversight line sums
ARMS = {"native": "native", "compass": "omni", "bowl": "omni"}  # runs recorded before the rename call the compass arm 'bowl'
HOURS_PER_PAGE = 6.0                  # Beyer et al., Site Reliability Engineering (2016), ch. 11: an incident's whole cycle


def git(*args: str, data: bytes | None = None) -> bytes:
    return subprocess.run(["git", *args], cwd=ROOT, input=data, capture_output=True, check=True).stdout


def bad_minutes(latency: str, start: str | None, end: str | None) -> list:
    """The minutes of one arm's measured window, each True where it is an alert minute, exactly as tools/live_reps.py
    (babysitting) counts them: a minute's 95th percentile by nearest rank, a failed request counted over the line, minutes
    past the window's last whole minute left out; a minute with no sample is not bad."""
    mins: dict = {}
    lines = latency.splitlines()
    head = [h.strip() for h in lines[0].split(",")] if lines else []
    ix = {h: i for i, h in enumerate(head)}
    for ln in lines[1:]:
        f = ln.split(",")
        try:
            m = int(float(f[ix["elapsed_seconds"]]) // 60)
            ok, lat = f[ix["ok"]].strip(), f[ix["latency_ms"]].strip()
            v = float(lat) if ok == "1" and lat else float("inf")
        except (KeyError, ValueError, IndexError):
            continue
        mins.setdefault(m, []).append(v)
    try:
        full = int((float(end.split()[0]) - float(start.split()[0])) // 60)
    except (AttributeError, ValueError, IndexError):
        full = max(mins) if mins else 0
    lo = min(min(mins), 0) if mins else 0

    def p95(v):
        v = sorted(v)
        return v[max(0, math.ceil(0.95 * len(v)) - 1)]
    return [(m in mins and p95(mins[m]) > LINE_MS) for m in range(lo, full)]


def pages(bad: list, hold: int, reset: int) -> int:
    """The pages a rule sends over one window: a page opens after `hold` bad minutes in a row while none is open, stays
    open through bad minutes and gaps of fewer than `reset` clean minutes, and closes after `reset` clean minutes in a row."""
    n, open_, run_bad, run_clean = 0, False, 0, 0
    for b in bad:
        if not open_:
            run_bad = run_bad + 1 if b else 0
            if run_bad >= hold:
                open_, n, run_clean = True, n + 1, 0
        else:
            run_clean = 0 if b else run_clean + 1
            if run_clean >= reset:
                open_, run_bad = False, 0
    return n


def paired(nat: list, omn: list) -> dict:
    """Paired repetitions: the means, the mean difference and its 95% interval on the exact Student t."""
    n = len(nat)
    d = [o - a for a, o in zip(nat, omn)]
    md = sum(d) / n
    sd = math.sqrt(sum((x - md) ** 2 for x in d) / (n - 1)) if n > 1 else 0.0
    h = t95(n - 1) * sd / math.sqrt(n) if n > 1 else 0.0
    return {"native": sum(nat) / n, "omni": sum(omn) / n, "diff": md, "ci95": [md - h, md + h], "n": n}


def _folders() -> dict:
    out = {}
    for name in git("ls-tree", "--name-only", RAW).decode().split():
        m = re.search(r"(?:^|-)run-(\d+)$", name)
        if m:
            out[m.group(1)] = name
    return out


def _arms(folder: str) -> dict:
    """{part: {rep: {arm: directory}}} for every bench-<arm>-<rep> folder under a run that holds a latency.csv."""
    out: dict = {}
    for p in git("ls-tree", "-r", "--name-only", RAW, "--", folder).decode().splitlines():
        if not p.endswith("/latency.csv"):
            continue
        parts = p.split("/")
        m = re.fullmatch(r"bench-([a-z]+)-(\d+)", parts[-2])
        if not m or m.group(1) not in ARMS:
            continue
        part = "/".join(x for x in parts[1:-2] if not re.fullmatch(r"paired-\d+", x))
        out.setdefault(part, {}).setdefault(int(m.group(2)), {})[ARMS[m.group(1)]] = "/".join(parts[:-1])
    return out


def _read(paths: list) -> dict:
    """Each path's text from the branch raw, in one git call (a file the clone lacks is fetched as git reads it)."""
    data = "".join(f"{RAW}:{p}\n" for p in paths).encode()
    out, buf, i = {}, git("cat-file", "--batch", data=data), 0
    for p in paths:
        nl = buf.index(b"\n", i)
        head = buf[i:nl].split()
        i = nl + 1
        if len(head) < 3 or head[1] != b"blob":
            out[p] = None
            continue
        size = int(head[2])
        out[p] = buf[i:i + size].decode("utf-8", "replace")
        i += size + 1
    return out


def count() -> dict:
    """Every table, run and repetition: the recount of the alert minutes checked against the table, then the pages."""
    subprocess.run(["bash", "scripts/raw_archive.sh", "fetch"], cwd=ROOT, check=False)
    engine, found = oversight.tables()
    folders = _folders()
    tests = []
    for f, d in found:
        R = d["rows"]
        rec_rows = R[next(x for x in R if x.startswith(oversight.ALERT))]["runs"]
        t = {"file": f.relative_to(ROOT).as_posix(), "title": d.get("title", f.stem), "runs": []}
        for k, run in enumerate(d.get("runs") or []):
            rid, rec = str(run.get("run")), (rec_rows[k] if k < len(rec_rows) else None)
            one = {"tag": run.get("tag", "ABC"[k]), "run": rid, "folder": folders.get(rid), "part": None, "check": "no folder", "reps": []}
            t["runs"].append(one)
            if not one["folder"] or rec is None:
                continue
            groups = _arms(one["folder"])
            tried = []
            for part, reps in sorted(groups.items()):
                both = sorted(r for r, a in reps.items() if "native" in a and "omni" in a)
                if not both:
                    continue
                paths = []
                for r in both:
                    for arm in ("native", "omni"):
                        base = reps[r][arm]
                        paths += [f"{base}/latency.csv", f"{base}/window_start.txt", f"{base}/window_end.txt"]
                txt = _read(paths)
                rows = []
                for r in both:
                    row = {"rep": r}
                    for arm in ("native", "omni"):
                        base = reps[r][arm]
                        bad = bad_minutes(txt[f"{base}/latency.csv"] or "", txt[f"{base}/window_start.txt"], txt[f"{base}/window_end.txt"])
                        row[arm] = {"alert_minutes": sum(bad), "minutes": len(bad),
                                    "pages": {f"{h},{s}": pages(bad, h, s) for h, s in RULES}}
                    rows.append(row)
                alert = paired([x["native"]["alert_minutes"] for x in rows], [x["omni"]["alert_minutes"] for x in rows])
                same = (abs(alert["native"] - rec["native"]) <= 0.05 + 1e-9 and abs(alert["omni"] - rec["omni"]) <= 0.05 + 1e-9
                        and all(abs(a - b) <= 1e-6 for a, b in zip(alert["ci95"], rec.get("ci95") or alert["ci95"])))
                tried.append(part or "(one part)")
                if same:
                    one.update(part=part, check="the recount gives the table's alert minutes and interval", reps=rows)
                    break
            else:
                one["check"] = f"the recount does not give the table's alert minutes (parts tried: {', '.join(tried) or 'none'}); left out"
        tests.append(t)
    return {"source": "tools/pages.py", "prereg": PREREG, "engine": engine, "line_ms": LINE_MS, "primary": list(PRIMARY),
            "rules": [list(r) for r in RULES], "hours_per_page": HOURS_PER_PAGE, "tests": tests}


def reading(rec: dict, rule: tuple) -> dict:
    """Each test's three runs and all the tests together, run by run, for one rule."""
    key, out, tot = f"{rule[0]},{rule[1]}", [], [dict(native=0.0, omni=0.0, diff=0.0, var=0.0, ok=True, n=0) for _ in range(3)]
    for t in rec["tests"]:
        rs = []
        for k, r in enumerate(t["runs"][:3]):
            if not r["reps"]:
                rs.append(None)
                tot[k]["ok"] = False
                continue
            p = paired([x["native"]["pages"][key] for x in r["reps"]], [x["omni"]["pages"][key] for x in r["reps"]])
            p["minutes_native"] = sum(x["native"]["alert_minutes"] for x in r["reps"]) / len(r["reps"])
            p["minutes_omni"] = sum(x["omni"]["alert_minutes"] for x in r["reps"]) / len(r["reps"])
            rs.append(p)
            T = tot[k]
            T["native"] += p["native"]
            T["omni"] += p["omni"]
            T["diff"] += p["diff"]
            T["n"] += 1
            se = (p["ci95"][1] - p["ci95"][0]) / 2 / t95(p["n"] - 1) if p["n"] > 1 else 0.0
            T["var"] += se * se
        out.append({"file": t["file"], "title": t["title"], "runs": rs,
                    "reading": three_run_reading(rs, LOWER) if all(rs) and len(rs) == 3 else "no value"})
    pooled = []
    for T in tot:
        h = Z95 * math.sqrt(T["var"])
        pooled.append({"native": T["native"], "omni": T["omni"], "diff": T["diff"], "ci95": [T["diff"] - h, T["diff"] + h],
                       "tests": T["n"], "ok": T["ok"]})
    ok = all(p["ok"] for p in pooled)
    return {"rule": list(rule), "tests": out, "pooled": pooled, "reading": three_run_reading(pooled, LOWER) if ok else "no value"}


def _chg(native: float, diff: float) -> str:
    if not native:
        return "no page in either arm" if not diff else f"up {diff:.2f} pages from none"
    x = 100 * diff / native
    return "no change" if abs(x) < 0.005 else f"{'down' if x < 0 else 'up'} {abs(x):.1f}%"


def _word(s: str) -> str:
    return s.replace("**", "")


NAMES = {"V21_ROBUST_KILL": "Robustness: the governor killed mid-run", "V21_ROBUST_LONG": "Robustness: the two-hour run"}


def _name(t: dict) -> str:
    """A test's short name: its title before the colon, or the name that tells two tests with one first word apart."""
    stem = pathlib.Path(t["file"]).stem
    return NAMES.get(stem) or NAMES.get(re.sub(r"^V\d+_", "V21_", stem)) or t["title"].split(":")[0]


def markdown(rec: dict) -> str:
    prim = reading(rec, tuple(rec["primary"]))
    runs = [r for t in rec["tests"] for r in t["runs"]]
    passed = [r for r in runs if r["reps"]]
    L = ["# The pages a person would have been sent: native against Omni-Compass on native", ""]
    L += [f"The oversight line's second reading, counted from the raw files of its own {len(rec['tests'])} tables (omni-v{rec['engine']}) "
          f"by the rule written and committed before the first count (`{rec['prereg']}`). A person on call is paid by the page, not by "
          "the minute: a page wakes someone, is answered, mitigated and written up. The alert minutes say how long a page would be "
          "open; this page says how many pages there would be. Class L: real software on GitHub's own machines, measured; no person "
          "is on those machines, so no hour or salary is on any receipt.", ""]
    L += ["## The rule and the check", ""]
    L += [f"A bad minute is the oversight line's alert minute exactly: a whole minute of the measured window whose 95th percentile "
          f"response time (nearest rank, a failed request counted over the line) was over the line, {rec['line_ms']:.0f} ms in every "
          f"table. A page opens after FOR bad minutes in a row while no page is open, and closes after RESET clean minutes in a row. "
          f"The primary rule is FOR {rec['primary'][0]} minute, RESET {rec['primary'][1]} minutes (Alertmanager's default "
          f"`resolve_timeout`); every pair of FOR 1, 2 and 5 and RESET 5 and 15 is printed below, declared with it.", ""]
    L += [f"Before any page was counted, the bad minutes recounted from the raw files had to give each run's printed alert minutes "
          f"and their 95% interval: **{len(passed)} of {len(runs)} runs** do, and only those are read."]
    for t in rec["tests"]:
        for r in t["runs"]:
            if not r["reps"]:
                L.append(f"- Left out: {_name(t)}, run {r['tag']} (#{r['run']}): {r['check']}.")
    L += [""]
    L += ["## The pages, test by test (the primary rule)", ""]
    L += ["| Test | Run A: pages per repetition, native → Omni-Compass | Run B | Run C | The three runs, by the one key |", "|---|---|---|---|---|"]
    for t, rt in zip(rec["tests"], prim["tests"]):
        cells = []
        for r, p in zip(t["runs"], rt["runs"]):
            cells.append("left out" if p is None else f"{p['native']:.2f} → {p['omni']:.2f}, {_chg(p['native'], p['diff'])} (#{r['run']})")
        while len(cells) < 3:
            cells.append("—")
        L.append(f"| {_name(t)} | " + " | ".join(cells) + f" | {_word(rt['reading'])} |")
    P = prim["pooled"]
    L.append("| **All the tests together** (each test's pages per repetition summed) | " + " | ".join(
        f"{p['native']:.2f} → {p['omni']:.2f}, {_chg(p['native'], p['diff'])}" for p in P) + f" | **{_word(prim['reading'])}** |")
    nat, omn = sum(p["native"] for p in P) / len(P), sum(p["omni"] for p in P) / len(P)
    r_pages = 1 - omn / nat if nat else 0.0     # the change of the three runs' means, as the oversight line reads its minutes
    mins = [(sum(p["minutes_native"] for p in (rt["runs"][k] for rt in prim["tests"]) if p),
             sum(p["minutes_omni"] for p in (rt["runs"][k] for rt in prim["tests"]) if p)) for k in range(3)]
    L += ["", f"Together, the three runs' means: **{nat:.2f} → {omn:.2f} pages**, down **{100 * r_pages:.1f}%** with Omni-Compass on "
          f"native, read **{_word(prim['reading'])}**. Fewer pages, not only shorter ones: the minutes a page stays open, native → "
          "Omni-Compass, " + ", ".join(f"{a / p['native']:.1f} → {b / p['omni']:.1f} in run {'ABC'[k]}" if p["native"] and p["omni"] else f"— in run {'ABC'[k]}"
                                        for k, ((a, b), p) in enumerate(zip(mins, P)))
          + "; the alert minutes over the same runs, " + ", ".join(f"{a:.1f} → {b:.1f}" for a, b in mins) + ".", ""]
    L += ["## Every rule declared with it", ""]
    L += ["| Rule (FOR bad minutes to open, RESET clean minutes to close) | Run A, together | Run B | Run C | The three runs |", "|---|---|---|---|---|"]
    for rule in [tuple(x) for x in rec["rules"]]:
        rr = reading(rec, rule)
        L.append(f"| FOR {rule[0]}, RESET {rule[1]}{' (the primary)' if list(rule) == rec['primary'] else ''} | "
                 + " | ".join(f"{p['native']:.2f} → {p['omni']:.2f}, {_chg(p['native'], p['diff'])}" for p in rr["pooled"])
                 + f" | {_word(rr['reading'])} |")
    L += ["", "## How it enters the bill", ""]
    L += ["The bill is the sum of its lines: C = M + P + O, with M the machines, P the people who run the stack and O the rest, "
          "held fixed. The people line is priced by time-driven activity-based costing (Kaplan and Anderson, *Harvard Business "
          "Review*, November 2004): P = w · Σⱼ Nⱼ · hⱼ + R, with Nⱼ the events a year of kind j (a page, a hand-made change of a "
          "setting, a capacity review), hⱼ the person-hours each takes (a page's whole cycle about "
          f"{rec['hours_per_page']:.0f} hours by Google's SRE book, chapter 11), w one person-hour fully loaded and R the fixed cost of "
          "an on-call rotation. Omni-Compass's share of the bill saved on the people line is S(people) = κ · p · β · r: p the "
          "people's share of the run cost, β the share of their time that is answering pages and turning the knobs Omni-Compass "
          "governs (the SRE book holds on-call to at most 25% of an engineer's time), r the fall in the events that call a person, "
          "κ the share of the freed time that becomes money (1 where a rotation or a head is released or the time goes to paid "
          "work, 0 where nothing changes). Only r is measured here; p, β and κ are an owner's. With the machines' line, the live "
          "page's one equation reads G = (1 + ΔW) ⁄ (1 + m · ΔM + p · ΔP) − 1, ΔP = −κ · β · r.", ""]
    try:                       # the alert minutes beside the pages only from the same engine's tables, never another's
        ov = json.loads(oversight.OUT_JSON.read_text(encoding="utf-8"))
        r_min = -float(ov["pooled"]["change"]) if ov.get("engine") == f"omni-v{rec['engine']}" else None
    except (OSError, ValueError, KeyError, TypeError):
        r_min = None
    L += [f"On a run cost of $100 million, κ = 1, r = {100 * r_pages:.1f}% (the pages above, the change of the three runs' means)"
          + (f" and, beside it, r = {100 * r_min:.1f}% (the alert minutes):" if r_min is not None else ":"), ""]
    hdr = "| People's share of the run cost, p | β = 25% (on-call time only) | β = 100% (every people hour) |"
    L += [hdr, "|---|---|---|"]
    for p in (0.07, 0.10, 0.20):
        def cell(beta):
            s = f"${100 * p * beta * r_pages:.1f} million ({100 * p * beta * r_pages:.1f}%)"
            if r_min is not None:
                s += f"; by the minutes ${100 * p * beta * r_min:.1f} million"
            return s
        L.append(f"| {100 * p:.0f}% | {cell(0.25)} | {cell(1.0)} |")
    L += ["", "These are the arithmetic of a measured fall and an owner's own shares, not a measured saving: the people cost itself, "
          "in hours, is measured only in a paired pilot on an owner's own records, their pager history and their log of changes to "
          "the governed settings, before and with Omni-Compass on native (`docs/PILOT_PROTOCOL.md`). The machines' line is read on "
          "the chip and through the cloud (`results/TWO_BILLS.md`), and the two lines are never added as percentages of different "
          "bills: each enters the one equation with its own share.", ""]
    L += ["Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.", ""]
    return "\n".join(stamp(L)) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="write the page from the record alone; exit 1 where it differs")
    a = ap.parse_args(argv)
    if a.check:
        if not OUT_JSON.exists():
            print(f"{OUT_JSON.relative_to(ROOT)}: no record yet")
            return 1
        rec = json.loads(OUT_JSON.read_text(encoding="utf-8"))
        same = OUT_MD.exists() and OUT_MD.read_text(encoding="utf-8") == markdown(rec)
        print(f"{OUT_MD.relative_to(ROOT)}: {'current' if same else 'differs from its record'}")
        return 0 if same else 1
    rec = count()
    OUT_JSON.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_MD.write_text(markdown(rec), encoding="utf-8")
    prim = reading(rec, tuple(rec["primary"]))
    runs = [r for t in rec["tests"] for r in t["runs"]]
    print(f"{OUT_MD.relative_to(ROOT)}: {sum(1 for r in runs if r['reps'])} of {len(runs)} runs reproduce their tables; "
          f"pages together: " + "; ".join(f"{p['native']:.2f} → {p['omni']:.2f}" for p in prim["pooled"]) + f"; {_word(prim['reading'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
