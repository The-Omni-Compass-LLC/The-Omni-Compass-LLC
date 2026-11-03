# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The muscles and the seven organisms on the front page, written from their records, never typed (the founder's order of
2 November 2026: no number on any page that was not calculated from its record).

Three records, read as they stand:
  results/realms_v5/MUSCLES_V5.csv and REALMS_V5.json   the 1,107 muscles and the seven organisms (class S)
  results/grid_v5/GRID.md and results/grid_v*/            the grid: its one written report, and every engine it was sent on
  results/scenarios/SCENARIOS_20.json                     the twenty scenarios: ten organisms, native and Omni-Compass on native

The block stands in README.md between its markers. Every number in it is computed here: the muscles counted by their own
reading, the organisms' change in decisions over the line (Omni-Compass's count against native's, minus one), their work and
the power given, the grid's own summary quoted, the scenarios' words and mean changes as the record gives them.

  python3 tools/organism_words.py          write the block
  python3 tools/organism_words.py --check  exit 1 if the block differs from what the records give (run by verify.py)
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
MUSCLES = ROOT / "results" / "realms_v5" / "MUSCLES_V5.csv"
REALMS = ROOT / "results" / "realms_v5" / "REALMS_V5.json"
GRID = ROOT / "results" / "grid_v5" / "GRID.md"
SCEN = ROOT / "results" / "scenarios" / "SCENARIOS_20.json"
BEGIN = "<!-- the muscles and the seven organisms, written from their records (tools/organism_words.py) -->"
END = "<!-- end of the muscles and the seven organisms -->"
FLOOR = 0.5   # the founder's floor of 24 October: a change under 0.5% is STEADY (tools/readings.py)

ORGANISMS = [("spine", "The spine"), ("compute_ai_cloud", "Compute / AI / Cloud"),
             ("physics_robotics_autonomous", "Physics / Robotics / Autonomous"),
             ("energy_facility_industrial", "Energy / Facility / Industrial"),
             ("distribution_specialized", "Distribution / Specialized"), ("stack", "The four stacked"),
             ("tower", "The whole tower")]
LOADS = [("normal", "its own load"), ("climb", "the climb"), ("line", "work waiting in line")]


def pct(x: float, nd: int = 1) -> str:
    return f"{x:.{nd}f}%"


def by_word(word: str, x: float, nd: int = 1) -> str:
    """A number beside a word wears the word's sign (the founder's order of 22 October): GAIN +, LOSS −, power given +."""
    s = "+" if word in ("GAIN", "power given") else ("−" if word == "LOSS" else "")
    return f"{s}{abs(x):.{nd}f}%" if s else f"{abs(x):.{nd}f}%"


def said(word: str, x: float, nd: int = 1, what: str = "") -> str:
    """The word first, then the direction in words (the founder's order of 23 October: down 4.8%, a cut, GAIN)."""
    d = "down" if x < 0 else ("up" if x > 0 else "no change,")
    if word == "GAIN" and what == "power":
        return f"GAIN, a cut, down {abs(x):.{nd}f}%"
    return f"{word}, {d} {abs(x):.{nd}f}%"


def wrap(text: str, width: int = 128) -> list:
    import textwrap
    return textwrap.wrap(text, width=width, break_long_words=False, break_on_hyphens=False)


def muscles() -> dict:
    labels = {}
    with MUSCLES.open(encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            labels.setdefault(r["muscle_id"], r["label_all_loads"])
    c = Counter(labels.values())
    gain = {k: n for k, n in c.items() if "LOSS" not in k and any(w in k for w in ("FASTER", "FEWER MISSES", "MORE WORK"))}
    return {"total": len(labels),
            "gain": sum(gain.values()),
            "faster": sum(n for k, n in gain.items() if "FASTER" in k),
            "fewer": sum(n for k, n in gain.items() if "FEWER MISSES" in k),
            "more": sum(n for k, n in gain.items() if "MORE WORK" in k),
            "limit": c.get("AT ITS LIMIT ON NATIVE", 0),
            "same": c.get("SAME AS NATIVE", 0),
            "loss": sum(n for k, n in c.items() if "LOSS" in k),
            "other": len(labels) - sum(gain.values()) - c.get("AT ITS LIMIT ON NATIVE", 0) - c.get("SAME AS NATIVE", 0)
                     - sum(n for k, n in c.items() if "LOSS" in k)}


def organisms(d: dict) -> list:
    rows = []
    for key, name in ORGANISMS:
        cells, works, powers, n = [], [], [], None
        for load, _ in LOADS:
            o = d["organisms"][load][key]
            n = o["n"]
            t = o["totals"]
            cells.append(100.0 * (t["viol_max"] / t["viol_native"] - 1.0))
            works.append(100.0 * o["summary"]["work"][0])
            powers.append(100.0 * o["summary"]["energy"][0])
        rows.append((name, n, cells, max(works, key=abs), max(powers)))
    return rows


def grid() -> tuple:
    t = GRID.read_text(encoding="utf-8")
    m = re.search(r"\*\*Across the grid: (.+?)\*\*", t, re.S)
    summary = " ".join(m.group(1).split()) if m else None
    if summary and "; with the cluster inside" in summary:
        summary = summary.split("; with the cluster inside")[0]
    eng = re.search(r"engine (omni-v\d+)", t)
    sent = sorted(int(p.name.split("_v")[1]) for p in (ROOT / "results").glob("grid_v*")
                  if p.is_dir() and (p / "DISPATCHED.json").exists() and not (p / "GRID.md").exists())
    return summary, (eng.group(1) if eng else "not named"), sent


def scenarios() -> dict:
    d = json.loads(SCEN.read_text(encoding="utf-8"))
    out = {"run": d["run"], "rows": [], "whole": None}
    for o in d["organisms"]:
        r = o["readings"]["on_native_vs_native"]
        g = r.get("gauges")
        if isinstance(g, dict) and "over" in g:
            out["rows"].append((o["name"], {k: (g[k]["word"], 100.0 * g[k]["mean_change"]) for k in ("work", "over", "power")}))
        elif r.get("state") == "composed" or "composition" in r:
            c = r.get("composition", r)
            idx = c["scopes"]["without"]["index"]["whole"]["index"] if "without" in c.get("scopes", {}) else None
            out["whole"] = {"engines": c.get("engines", []), "index": idx, "name": o["name"]}
    return out


def whole_index(w: dict) -> str | None:
    """The whole organism's index by the index's rule, as the record carries it."""
    idx = (w or {}).get("index") or {}
    if "pct" in idx and "word" in idx:
        return f"{idx['word']} {abs(idx['pct']):.1f}%"
    return None


def realms_lines(link_prefix: str = "") -> list:
    """The 1,107 muscles and the seven organisms: the muscles counted by their reading, each organism under each load."""
    d = json.loads(REALMS.read_text(encoding="utf-8"))
    run = d["run"]
    m = muscles()
    rows = organisms(d)
    seeds = run["seeds"]
    L = [
         *wrap(f"**The 1,107 muscles and the seven organisms** ([`results/realms_v5/REALMS_V5.md`]({link_prefix}results/realms_v5/REALMS_V5.md)). "
               f"The newest record is engine {run['engine']}'s: run {run['started']}, commit `{run['commit'][:12]}`, preregistered seeds "
               f"{seeds[0]} to {seeds[-1]} (ten paired runs per muscle, per organism and per load), read again by the 0.5% rule on 24 "
               f"October 2026. It runs again on the engine that stands; until its table lands, this one is {run['engine']}'s."),
         "",
         f"| Every muscle alone, under its own load and with work waiting in line | Muscles of {m['total']:,} |",
         "|---|---:|",
         f"| **GAIN**: fewer misses, faster or more work, and no LOSS under either load | **{m['gain']}** |",
         f"| of them: the waiting line cleared sooner | {m['faster']} |",
         f"| of them: over the line less often | {m['fewer']} |",
         f"| of them: more work | {m['more']} |",
         f"| STEADY, at its limit on native (native already runs the knob at the top of its range; Omni-Compass writes nothing) "
         f"| {m['limit']} |",
         f"| STEADY, the same as native | {m['same']} |",
         f"| **LOSS**, or GAIN and LOSS | **{m['loss']}** |"]
    if m["other"]:
        L.append(f"| another reading | {m['other']} |")
    L += ["",
          "Each organism under each load: the change in decisions over the line (Omni-Compass's count against native's), the",
          "largest change in work over the three loads, and the largest power given (the organism's energy against native's).",
          "",
          "| Organism (muscles) | Over the line: " + " | ".join(n for _, n in LOADS) + " | Work, largest change | Power given, largest |",
          "|---|---:|---:|---:|---|---:|"]
    for name, n, cells, work, power in rows:
        cell = [said("GAIN" if c <= -FLOOR else ("LOSS" if c >= FLOOR else "STEADY"), c) for c in cells]
        wk = (f"STEADY, {abs(work):.3f}% (under the {FLOOR}% floor)" if abs(work) < FLOOR
              else said("GAIN" if work > 0 else "LOSS", work, 2))
        pw = said("power given", power, 2) if power >= 0 else said("GAIN", power, 2, "power")
        L.append(f"| {name} ({n:,}) | " + " | ".join(cell) + f" | {wk} | {pw} |")
    return L


def grid_lines(link_prefix: str = "") -> list:
    """The grid: its one written report quoted, and every later engine it was sent on with no report written."""
    gsum, geng, sent = grid()
    L = []
    if gsum:
        g = (f"**The grid** (the seven organisms at 1, 10 and 100 copies, each at 1, 10 and 100 runs). Its one written report is "
             f"engine {geng}'s ([`results/grid_v5/GRID.md`]({link_prefix}results/grid_v5/GRID.md)); its modelled squares read, in the report's own "
             f"words: \"{gsum}\". The squares with the real cluster inside are read gauge by gauge in the same report.")
        if sent:
            g += (f" The grid has been sent on every engine since, omni-v{sent[0]} to omni-v{sent[-1]} (`results/grid_v*/DISPATCHED.json`), "
                  f"and no report of those runs has been written yet; until one is, the grid is read only on {geng}.")
        L += wrap(g)
    return L


def scenarios_lines(link_prefix: str = "") -> list:
    """The twenty scenarios: the nine modelled organisms' words and the whole organism's composed index, as the record gives them."""
    sc = scenarios()
    L = []
    r = sc["run"]
    nine = sc["rows"]
    over = sorted(nine, key=lambda x: abs(x[1]["over"][1]))
    words = Counter(v["over"][0] for _, v in nine)
    work_words = Counter(v["work"][0] for _, v in nine)
    power = [(nm, v["power"]) for nm, v in nine]
    power_note = "; ".join(f"{n}: {said(w, x, 2, 'power')}" for n, (w, x) in power if w != "STEADY")
    lo, hi = over[0], over[-1]
    nm = lambda x: x.lower() if x.startswith("The ") else x
    para = (f"**The twenty scenarios** (ten organisms, each native and with Omni-Compass on native; engine {r['engine']}, run "
            f"{r['started']}, three runs, seeds {r['seeds'][0]} to {r['seeds'][-1]}; "
            f"[`results/scenarios/SCENARIOS_20.md`]({link_prefix}results/scenarios/SCENARIOS_20.md)). In the {len(nine)} modelled organisms the muscles "
            "over the line read " + ", ".join(f"{w} in {n}" for w, n in words.most_common())
            + f" (from {said(lo[1]['over'][0], lo[1]['over'][1], 2)} in {nm(lo[0])} to {said(hi[1]['over'][0], hi[1]['over'][1], 2)} "
            f"in {nm(hi[0])}); the work " + ", ".join(f"{w} in {n}" for w, n in work_words.most_common()) + "; the power STEADY in "
            + str(sum(1 for _, (w, _) in power if w == "STEADY"))
            + ("" if not power_note else f" ({power_note})") + ".")
    w = sc["whole"]
    wi = whole_index(w)
    if w and wi:
        para += (f" The whole organism without the card, composed from the real tables (class S, a composition of class P and class L "
                 f"measurements), reads {wi} by the index's rule; its tables come from {len(w['engines'])} engines "
                 f"({', '.join(w['engines'])}), so it is a composition across engines, never one engine's reading.")
    L += wrap(para)
    return L


def build() -> str:
    L = [BEGIN,
         "Every number in this section is computed from its record by `python3 tools/organism_words.py`, and `verify.py` fails a",
         "push where any of them differs from what the records give. Evidence class **S**: our own models of the plants, not",
         "meters; a plant written by the people who wrote the law is not an independent test.",
         ""]
    L += realms_lines() + [""]
    g = grid_lines()
    if g:
        L += g + [""]
    L += scenarios_lines() + [END]
    return "\n".join(L) + "\n"


def put(text: str) -> str:
    a, z = text.find(BEGIN), text.find(END)
    if a < 0 or z < 0:
        raise SystemExit("README.md carries no markers for the muscles and the seven organisms")
    return text[:a] + build().rstrip("\n") + text[z + len(END):]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    t = README.read_text(encoding="utf-8")
    new = put(t)
    if a.check:
        if new != t:
            print("README.md: the muscles and the seven organisms differ from their records (python3 tools/organism_words.py)")
            return 1
        print("the muscles and the seven organisms: in line with their records")
        return 0
    README.write_text(new, encoding="utf-8")
    print("README.md: the muscles and the seven organisms written from their records")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
