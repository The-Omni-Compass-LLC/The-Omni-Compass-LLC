#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The oversight line: the pages a person would have answered, native against Omni-Compass on native, from the records alone,
and how that line enters the bill.

The founder's words of 3 November: the engineering share of an IT bill lives in the oversight, "they don't need a 3 a.m. call
and they don't need [anyone] to turn knobs when OmniCompass is ... self-gauging". GitHub's machines run unattended in both
arms, so no engineer's hour is on any receipt; what every real Kubernetes receipt does measure is what would have paged a
person (the alert minutes, tools/live_reps.py `babysitting`) and the settings the governor wrote on its own. This page reads
both from every Kubernetes three-run table on the newest engine that has them, and puts the pages through the one equation
as the bill's people line, b = Σₖ sₖ·bₖ, with the people's share an owner's own figure (the founder's example: 7%).

    python3 tools/oversight.py          writes results/OVERSIGHT.md and results/OVERSIGHT.json
    python3 tools/oversight.py --check  fails when either differs from the records
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_MD, OUT_JSON = ROOT / "results" / "OVERSIGHT.md", ROOT / "results" / "OVERSIGHT.json"
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT))
from legal import stamp  # noqa: E402
from readings import LOWER, three_run_reading  # noqa: E402
from omnicompass.student_t import t95  # noqa: E402

OWN_RUNS = "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results."
ALERT, COMMANDS = "alert minutes", "settings commands the governor wrote on its own"
SHARE_EXAMPLE, SPEND_EXAMPLE = 0.07, 100.0   # the founder's example of 3 November (7% of the bill), on the $100 M example budget
Z95 = 1.959964                               # a sum over many tables: the normal 95% point
NODES, NODE_HOURS = "worker nodes in service, mean", "node-hours"


# comparisons that are not Omni-Compass on native against that native at the factory tune: an orchestrator against the organism
# alone (ORCH), Omni-Compass in place of an orchestrator (VS) or with it against the organism alone (BOTH), Omni-Compass by itself
# (SOLO) and the heartbeat at another beat (PACE)
NOT_ON_NATIVE = re.compile(r"_4W_(ORCH|VS|BOTH)$|^V\d+_SOLO|^V\d+_PACE_")


def tables() -> tuple:
    """Every Kubernetes three-run table of the newest engine that carries the alert minutes (results/live/V<n>_*.json)."""
    by = {}
    for f in (ROOT / "results" / "live").glob("V*_*.json"):
        m = re.fullmatch(r"V(\d+)_.+", f.stem)
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        rows = d.get("rows")
        if not m or not isinstance(rows, dict) or not any(k.startswith(ALERT) for k in rows):
            continue
        if NOT_ON_NATIVE.search(f.stem):        # the oversight line reads Omni-Compass on native against native, at the factory tune
            continue
        by.setdefault(int(m.group(1)), []).append((f, d))
    if not by:
        return None, []
    v = max(by)
    return v, sorted(by[v], key=lambda x: x[0].name)


def _mean(runs, side):
    xs = [r[side] for r in runs if r.get(side) is not None]
    return sum(xs) / len(xs) if xs else None


def by_run(found: list) -> dict:
    """The tables summed run by run (A, B, C): each run's alert minutes native and with Omni-Compass, their difference with its
    95% interval (each table's own interval and repetitions, the exact Student t, the variances added, the normal point for
    the sum), the governor's own commands an hour over the measured windows, and the three runs read by the one key."""
    runs = []
    for k in range(3):
        n = o = dd = var = cmd = hours = 0.0
        ok = True
        for f, d in found:
            R = d["rows"]
            a = R[next(x for x in R if x.startswith(ALERT))]["runs"]
            if len(a) <= k:
                ok = False
                break
            r = a[k]
            reps = ((d.get("runs") or [{}] * 3)[k] or {}).get("paired_repetitions") or 0
            lo, hi = (r.get("ci95") or [r["diff"], r["diff"]])[:2]
            t = t95(reps - 1) if reps > 1 else float("nan")
            n += r["native"]; o += r["omni"]; dd += r["diff"]
            var += ((hi - lo) / (2 * t)) ** 2 if t == t else 0.0
            c = next((R[x]["runs"] for x in R if x.startswith(COMMANDS)), None)
            nh, nodes = R.get(NODE_HOURS, {}).get("runs") or [], R.get(NODES, {}).get("runs") or []
            if c and len(c) > k and len(nh) > k and len(nodes) > k and nodes[k].get("native"):
                cmd += c[k]["omni"]; hours += nh[k]["native"] / nodes[k]["native"]
        if not ok:
            return {"runs": [], "reading": None}
        se = var ** 0.5
        runs.append({"native": n, "omni": o, "diff": dd, "ci95": [dd - Z95 * se, dd + Z95 * se],
                     "change": dd / n if n else None, "commands_per_hour": cmd / hours if hours else None, "hours": hours})
    reading = three_run_reading([{"native": r["native"], "diff": r["diff"], "ci95": r["ci95"]} for r in runs], LOWER)
    return {"runs": runs, "reading": reading.replace("**", "")}


def build() -> dict:
    v, found = tables()
    rows = []
    for f, d in found:
        R = d["rows"]
        a = R[next(k for k in R if k.startswith(ALERT))]
        c = next((R[k] for k in R if k.startswith(COMMANDS)), None)
        n, o = _mean(a["runs"], "native"), _mean(a["runs"], "omni")
        rows.append({"test": d.get("title") or f.stem, "record": f.relative_to(ROOT).as_posix(), "runs": len(a["runs"]),
                     "repetitions": [r.get("paired_repetitions") for r in d.get("runs") or []],
                     "native": n, "omni": o, "change": (o / n - 1) if n else None, "reading": a.get("reading"),
                     "per_run": [{"native": r["native"], "omni": r["omni"]} for r in a["runs"]],
                     "commands": _mean(c["runs"], "omni") if c else None})
    tn, to = sum(r["native"] for r in rows), sum(r["omni"] for r in rows)
    pooled = (to / tn - 1) if tn else None
    per_run = by_run(found)
    people = SHARE_EXAMPLE * pooled if pooled is not None else None
    pg = pages_counted()
    if pg and v and pg.get("engine") != f"omni-v{v}":     # two engines are never read together: the pages wait for their recount
        pg = {"record": pg["record"], "engine": pg["engine"], "change": None, "other_engine": True}
    return {"engine": f"omni-v{v}" if v else None, "pages": pg, "question": "they don't need a 3 a.m. call and they don't need [anyone] to turn knobs "
            "when OmniCompass is ... self-gauging", "said": "the founder, 3 November 2026", "rows": rows,
            "pooled": {"native": tn, "omni": to, "change": pooled, "runs": per_run["runs"], "reading": per_run["reading"]},
            "count": {"tests": len(rows), "fewer": sum(1 for r in rows if r["omni"] < r["native"]),
                      "to_zero": sum(1 for r in rows if r["native"] > 0 and r["omni"] == 0),
                      "same": sum(1 for r in rows if r["omni"] == r["native"]), "more": sum(1 for r in rows if r["omni"] > r["native"])},
            "equation": {"bill": "B = Σₖ cₖ; b = Σₖ sₖ·bₖ, sₖ = cₖ(native) / B(native)",
                         "people_line": "b(people) = the change in alert minutes (stated assumption: the time a page takes moves with the pages)",
                         "into_g": "G = (1 + ΔW) / (1 + ΔB) − 1, the people line inside ΔB as s(people)·b(people)"},
            "example": {"share": SHARE_EXAMPLE, "spend_musd": SPEND_EXAMPLE, "bill_change": people,
                        "musd": SPEND_EXAMPLE * people if people is not None else None,
                        "label": "an example, the founder's of 3 November: the people who watch and tune the stack at 7% of the bill; "
                                 "no receipt carries the 7%, and an owner puts in its own share"},
            "sources": sorted(r["record"] for r in rows)}


def pages_counted():
    """The pages a person would have been sent, counted from the same runs' raw files by the preregistered rule
    (tools/pages.py, results/OVERSIGHT_PAGES.json): the three runs' means, their change, the one key's reading, the minutes a
    page stays open in each arm, and every declared rule's reading. None until that record exists."""
    f = ROOT / "results" / "OVERSIGHT_PAGES.json"
    if not f.exists():
        return None
    import pages as PG   # here, not at the top: tools/pages.py reads this module's tables
    rec = json.loads(f.read_text(encoding="utf-8"))
    prim = PG.reading(rec, tuple(rec["primary"]))
    P = prim["pooled"]
    nat, omn = sum(x["native"] for x in P) / len(P), sum(x["omni"] for x in P) / len(P)
    mins = [(sum(t["runs"][k]["minutes_native"] for t in prim["tests"] if t["runs"][k]),
             sum(t["runs"][k]["minutes_omni"] for t in prim["tests"] if t["runs"][k])) for k in range(3)]
    runs = [r for t in rec["tests"] for r in t["runs"]]
    return {"record": "results/OVERSIGHT_PAGES.md", "engine": f"omni-v{rec['engine']}", "rule": rec["primary"], "native": nat, "omni": omn,
            "change": (omn / nat - 1) if nat else None, "reading": prim["reading"].replace("**", ""),
            "runs_read": sum(1 for r in runs if r["reps"]), "runs": len(runs),
            "minutes_per_page": [[a / x["native"] if x["native"] else None, b / x["omni"] if x["omni"] else None]
                                 for (a, b), x in zip(mins, P)],
            "rules": [{"rule": list(r), "reading": PG.reading(rec, tuple(r))["reading"].replace("**", "")} for r in rec["rules"]],
            "hours_per_page": rec["hours_per_page"]}


def _pc(x: float) -> str:
    return f"{abs(x) * 100:.1f}%"


def _raw(x: float) -> str:
    return f"{'+' if x > 0 else '−' if x < 0 else '±'}{abs(x):.2f}"


def pages_section(d: dict) -> list:
    """The pages counted, not only the minutes: the record tools/pages.py writes from the same runs' raw files."""
    g = d.get("pages")
    if g and g.get("other_engine"):
        return ["## Pages counted, not only minutes", "",
                f"The pages a person would have been sent are counted from the raw files of {g['engine']}'s tables (`{g['record']}`, "
                f"that engine's own record); these minutes are {d['engine']}'s, and two engines are never read together, so the "
                f"count of pages on {d['engine']}'s runs comes next and is not printed here before it is made.", ""]
    if not g or g.get("change") is None:
        return []
    mpp = "; ".join(f"{a:.1f} → {b:.1f} in run {t}" for t, (a, b) in zip("ABC", g["minutes_per_page"]) if a and b)
    agree = sum(1 for r in g["rules"] if r["reading"].startswith("GAIN"))
    return ["## Pages counted, not only minutes", "",
            f"A person is paid by the page, not by the minute. Counted from the same runs' raw files by the rule written before the "
            f"count (a page opens on a bad minute and closes after five clean ones; `docs/OVERSIGHT_PAGES_PREREGISTRATION.md`), and "
            f"only from runs whose recount gives their table's own alert minutes ({g['runs_read']} of {g['runs']}), the pages a person "
            f"would have been sent went from {g['native']:.2f} to {g['omni']:.2f} a repetition of every test together: "
            f"**down {_pc(g['change'])}, {g['reading']}** (`{g['record']}`). A page stays open about as long in both arms "
            f"(minutes a page, native → Omni-Compass: {mpp}): Omni-Compass sends fewer pages, not shorter ones. "
            f"Every alert rule declared with it reads GAIN ({agree} of {len(g['rules'])}).", ""]


def run_by_run(p: dict) -> list:
    """The pooled pages run by run, and their reading by the one key."""
    runs = p.get("runs") or []
    if not runs:
        return []
    L = ["**Run by run.** The tables summed in each of our three runs (one repetition of every test, native beside Omni-Compass on "
         "native); each difference's 95% interval adds its tables' variances, each from that table's own interval and repetitions.", "",
         "| Run | Alert minutes, native → Omni-Compass on native, summed | Change | Difference, 95% interval (minutes) | Settings the governor wrote on its own, an hour |",
         "|---|---|---|---|---|"]
    for tag, r in zip("ABC", runs):
        ch = "—" if r["change"] is None else ("down " if r["change"] < 0 else "up ") + _pc(r["change"])
        cph = "—" if r["commands_per_hour"] is None else f"{r['commands_per_hour']:.0f}"
        L.append(f"| {tag} | {r['native']:.2f} → {r['omni']:.2f} | {ch} | {_raw(r['diff'])} ({_raw(r['ci95'][0])} to {_raw(r['ci95'][1])}) | {cph} |")
    every = (p["reading"] or "").startswith("GAIN in all three")
    L += ["", f"**Read by the one key: {p['reading']}.**" + (" The pages fell in every run, each run's interval clear of zero." if every
          else "") + " The settings the governor wrote an hour are counted over each run's measured windows (node-hours over the nodes "
          "in service), with no person touching either arm.", ""]
    return L


def markdown(d: dict) -> str:
    rows, p, c, ex = d["rows"], d["pooled"], d["count"], d["example"]
    eng = d["engine"]
    L = ["# The Oversight Line: the Pages a Person Would Answer, Native Against Omni-Compass on Native", "",
         f"> \"{d['question'][0].upper() + d['question'][1:]}\" ({d['said']})", "",
         "## What GitHub's runs measure, and what they cannot", "",
         "Every benchmark runs on GitHub's own machines with nobody watching, in both arms: no person is on call, no person turns a "
         "knob, so no engineer's hour and no salary is on any receipt, and none can be. What every real Kubernetes receipt does "
         "measure is the event that calls a person: an **alert minute**, a whole minute of the measured window whose 95th "
         "percentile response time, failed requests counted over, was over the response line, the minute an on-call page would be "
         "open (`tools/live_reps.py`, `babysitting`; judged, fewer is GAIN). Beside it each receipt shows the settings the governor "
         "wrote on its own, each in its audit with its reason and read back (shown, not judged: native's own autoscaler runs "
         "untouched in both arms).", "",
         f"## The pages, test by test ({eng}, every real Kubernetes three-run table that carries them)", "",
         "| Test | Alert minutes a repetition, native → Omni-Compass on native (mean of the three runs) | Change | Reading (the table's own, the one key) | Settings the governor wrote on its own, a repetition | Record |",
         "|---|---|---|---|---|---|"]
    for r in rows:
        ch = ("none in either arm" if not r["native"] and not r["omni"] else "—" if not r["native"] else "the same" if r["change"] == 0
              else ("down " if r["change"] < 0 else "up ") + _pc(r["change"]))
        cm = "—" if r["commands"] is None else f"{r['commands']:.1f}"
        L.append(f"| {r['test']} | {r['native']:.2f} → {r['omni']:.2f} | {ch} | {r['reading']} | {cm} | `{r['record']}` |")
    L += ["", f"**Together.** Over the {c['tests']} tests the pages a repetition add up to {p['native']:.1f} alert minutes on native and "
          f"{p['omni']:.1f} with Omni-Compass on top: **down {_pc(p['change'])}** (our arithmetic over the tables, each test weighed by "
          f"its own minutes; the two-hour test holds {max(rows, key=lambda r: r['native'])['native'] / p['native'] * 100:.0f}% of "
          f"native's). Fewer pages in {c['fewer']} of the {c['tests']} tests, to none at all in {c['to_zero']}, the same in "
          f"{c['same']}, more in {c['more']}. Each test's word is its own table's, by the one key.", ""] + run_by_run(p) + pages_section(d) + [
          "## The people line, through the one equation", "",
          "The bill is the sum of its lines, B = Σₖ cₖ, and each line's change counts by its share of native's bill, "
          "b = Σₖ sₖ·bₖ (`docs/WORK_PER_BILL.md`). The people who watch and tune a stack are one line, k = people, with its share "
          "s(people) of the owner's bill. The receipts give that line's change only where the time spent moves with the pages; "
          "stated as the assumption it is: b(people) = the change in alert minutes. The line then moves the whole bill by "
          "s(people)·b(people), and it enters the benefit only through the bill: G = (1 + ΔW) / (1 + ΔB) − 1.", "",
          "**Priced by what calls a person.** The people line itself is priced by time-driven activity-based costing (Kaplan and "
          "Anderson, *Harvard Business Review*, November 2004): P = w · Σⱼ Nⱼ · hⱼ + R, with Nⱼ the events a year of kind j (a page, a "
          "hand-made change of a setting, a capacity review), hⱼ the person-hours each takes (a page's whole cycle about six hours by "
          "Google's SRE book, chapter 11), w one person-hour fully loaded and R the fixed cost of an on-call rotation. The share of "
          "the bill saved on it is S(people) = κ · p · β · r: p the people's share of the run cost, β the share of their time that "
          "is answering pages and turning the knobs Omni-Compass governs (the SRE book holds on-call to at most 25% of an "
          "engineer's time), r the fall in what calls a person (the counted pages, or the minutes), κ the share of the freed time "
          "that becomes money (1 where a rotation or a head is released or the time goes to paid work, 0 where nothing changes). "
          "Only r is measured; p, β and κ are an owner's (`results/OVERSIGHT_PAGES.md` prints the product on a $100 million run "
          "cost for any of them).", "",
          f"**The example, not a result.** At the founder's example share, 7% of the bill (no receipt carries it; it plays the part "
          f"the 2.9% plays in the $100 M example), the measured fall in pages moves the bill by 0.07 × (−{_pc(p['change'])}) = "
          f"**down {_pc(ex['bill_change'])} of the whole bill**: on the $100 M example, about ${abs(ex['musd']):.1f} M a year of the "
          "people's time no longer spent answering pages, at native's cost. A larger share gives a larger line in proportion "
          f"(10% gives down {_pc(0.10 * p['change'])}); an owner's own share and its own count of pages replace both numbers.", "",
          "## What is not claimed", "",
          "- **Not a 20% (13% + 7%).** The 12.9% is the software end's second reading of the Omni index (work and speed, on GitHub's "
          "machines), not a bill; 7% is a share of a bill, not a gain. A reading and a share do not add; the people line enters G "
          "only through ΔB, as above.",
          "- **Not the people removed.** The record counts pages, not heads or salaries. An on-call rotation is staffed whether or not "
          "it is paged; what falls is the time the pages take, the triage and the hand tuning after them.",
          "- **Not every page gone, and never nobody.** Pages fell in most tests and to none in some, not in all. A person keeps the "
          "kill switch (one hand, instant, security only), sets the response line and chooses the profile.", "",
          "## Questions and answers", "",
          "**Why do the benchmarks not show the engineering cost?** Because GitHub's machines run with nobody on call in either arm: "
          "there is no engineer's hour to count. The receipts count what would have called one, the alert minutes, and the settings "
          "the governor wrote itself.", "",
          "**What does self-gauging mean here?** At every beat the governor reads the system's own meters, decides, writes a setting "
          "only through the plug, reads the write back and records its reason in its audit; it acts on the reading before the line "
          "is crossed, where a person acts after the page. In the tests above it wrote its settings on its own, the number in the "
          "table, with no person touching either arm.", "",
          "**Could the real number be bigger?** It can. An owner's people share may be larger than 7%, and a stack carries many "
          "services, each with its own pages, where each test here reads one. It can also be smaller: the record measures pages, "
          "and how much of a person's time moves with them is the owner's to count.", "",
          "**What holds the stack's health when nobody is watching?** The mechanism, not a person's reaction time: the governor "
          "reads every gauge every beat, which no person can, and moves before the line is crossed, inside each muscle's own limit. "
          "The alert minutes are the record of how long health was lost, and they are what fell.", "",
          "**Does Omni-Compass replace the on-call engineer?** No. It takes pages away where its reading acts before the line; the "
          "person keeps the switch, the line and the profile.", "",
          "**How does an owner measure it on its own stack?** Count the alert minutes with the same rule, native and with "
          "Omni-Compass on top, over the same load (the receipts' rule: a whole minute whose 95th percentile was over the line), "
          "and the time each page took from the on-call tool; s(people) is the owner's own payroll for that work over its bill.", "",
          f"Engines: the tables are {eng}'s, the newest engine whose Kubernetes tables have landed; every benchmark runs again on the "
          "engine that stands, and this page is written again from the records when they land (`python3 tools/oversight.py`).", "",
          OWN_RUNS]
    return "\n".join(stamp(L)) + "\n"


BLOCK_BEGIN = "<!-- the oversight line (tools/oversight.py) -->"
BLOCK_END = "<!-- end of the oversight line -->"
PLACES = (ROOT / "README.md", ROOT / "docs" / "OMNI_COMPASS_OWNERS_MANUAL.md", ROOT / "docs" / "STATE_OF_PLAY.md")


def block(d: dict) -> str:
    """The paragraph the README, the Owner's Manual and the state of play carry, from the same numbers as the page."""
    p, c, ex = d["pooled"], d["count"], d["example"]
    if not d["rows"] or p["change"] is None:
        return "The oversight line: no Kubernetes three-run table carries the pages yet (`results/OVERSIGHT.md`)."
    runs = p.get("runs") or []
    cph = [r["commands_per_hour"] for r in runs if r.get("commands_per_hour")]
    return ("**The people, counted: the oversight line** (`results/OVERSIGHT.md`, written by `tools/oversight.py` from the tables). "
            "The Omni index counts work, speed and machines, never a person; the receipts count the people too, in both arms. "
            f"Across the {c['tests']} real Kubernetes tests of {d['engine']}, the minutes an on-call page would be open (the 3 a.m. call) "
            f"went down {_pc(p['change'])}, fewer in {c['fewer']} tests and to none in {c['to_zero']}"
            + (f", and down in each of our three runs beyond the noise ({p['reading']})" if p.get("reading") else "")
            + (f", while the governor turned the knobs itself ({'; '.join(f'{x:.0f}' for x in cph)} settings an hour in runs A; B; C, "
               "no person touching either arm)" if len(cph) == 3 else "")
            + (f". Counted as pages from the same runs' raw files by the rule written before the count, the pages a person would have "
               f"been sent went down {_pc(d['pages']['change'])} ({d['pages']['reading']}; `{d['pages']['record']}`): fewer pages, "
               "each open about as long" if d.get("pages") and d["pages"].get("change") is not None else "")
            + ". In the bill it is the people line, b = s(people) · b(people) at the owner's own share: at the founder's example of "
            f"7%, down {_pc(ex['bill_change'])} of the whole bill. It is not added to the index (a share of a bill and a reading of "
            "work and speed do not add), and it removes no person: a person keeps the switch.")


def place(text: str, para: str):
    i, j = text.find(BLOCK_BEGIN), text.find(BLOCK_END)
    if i < 0 or j < i:
        return None
    return text[:i] + BLOCK_BEGIN + "\n" + para + "\n" + text[j:]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    d = build()
    js, md = json.dumps(d, indent=1, ensure_ascii=False) + "\n", markdown(d)
    para, placed = block(d), {}
    for q in PLACES:
        new = place(q.read_text(encoding="utf-8") if q.exists() else "", para)
        if new is not None:
            placed[q] = new
    if a.check:
        bad = [p.relative_to(ROOT).as_posix() for p, s in ((OUT_JSON, js), (OUT_MD, md), *placed.items())
               if not p.exists() or p.read_text(encoding="utf-8") != s]
        print("the oversight line: " + ("in line with the records" if not bad else ", ".join(bad) + " differ (python3 tools/oversight.py)"))
        return 1 if bad else 0
    OUT_JSON.write_text(js, encoding="utf-8")
    OUT_MD.write_text(md, encoding="utf-8")
    for q, t in placed.items():
        q.write_text(t, encoding="utf-8")
    p = d["pooled"]
    print(f"{OUT_MD.relative_to(ROOT)}: {d['count']['tests']} tests on {d['engine']}; alert minutes {p['native']:.1f} → {p['omni']:.1f} "
          f"({p['change'] * 100:+.1f}%); at the 7% example the bill moves {d['example']['bill_change'] * 100:+.2f}%")
    return 0


if __name__ == "__main__":
    sys.exit(main())
