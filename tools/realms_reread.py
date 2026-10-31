#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The seven organisms and every muscle of the catalog read again by the one key that stands (the founder's order of 24
October 2026: a change of 0.5% or more either way is a change, STEADY only under it).

The realms runner (tools/run_realms_v5.py, frozen with the results it made) labels a muscle by its 95% intervals over the
seeds alone: a change of a thousandth of a percent clear of the noise was a GAIN, and a change of several percent inside it
was not counted. This reads every muscle's and every organism's own seeds again (results/realms_v5/REALMS_V5.json, the runs'
own numbers, nothing run again) and labels them by size: the mean change over the seeds of work, of the misses (in percent of
native's own share of decisions over the line) and of the time to clear a line, each counted toward or away from its aim from
0.5% up and not at all under it, whether or not it stands clear of the seeds' noise. The kinds are the runner's own (the gains
joined, the same as native, at its limit on native, GAIN AND LOSS, LOSS, INVALID), and the page is written by the runner's own
writer. The runner, its engine and its run's provenance are not touched; each page says it was read again.

  python3 tools/realms_reread.py            read the results again and write them
  python3 tools/realms_reread.py --check    exit 1 when any label differs from what the rule gives
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from tools import run_realms_v5 as R          # noqa: E402  (the runner's own kinds and writer)
from tools.readings import SIZE_FLOOR         # noqa: E402  (the one floor, written once)

OUT = ROOT / "results" / "realms_v5"
NOTE = ("Read again on 24 October 2026 by the one key (tools/realms_reread.py, the founder's order: a change of 0.5% or more "
        "either way is a change, STEADY only under it): each label counts the mean change over the seeds from 0.5% up, whether "
        "or not it stands clear of the seeds' noise; the numbers are the runs' own.")


def mean(xs):
    return sum(xs) / len(xs) if xs else 0.0


def gains_losses(per_seed, native_share):
    """What the max did against native, by size: more work (or less), its line cleared sooner (or later), fewer misses (or
    more), each counted from 0.5% of native up. Misses are read against native's own share of decisions over the line; where
    native had none, any change counts."""
    gains, losses = set(), set()
    w = mean([c["work"] for c in per_seed])
    if abs(w) >= SIZE_FLOOR:
        (gains if w > 0 else losses).add("MORE WORK" if w > 0 else "LESS WORK")
    v = mean([c["viol_pp"] for c in per_seed])
    rel = (v / 100.0) / native_share if native_share > 0 else (1.0 if v else 0.0)
    if v and abs(rel) >= SIZE_FLOOR:
        (gains if v < 0 else losses).add("FEWER MISSES" if v < 0 else "MORE MISSES")
    if per_seed and all("speed" in c for c in per_seed):
        s = mean([c["speed"] for c in per_seed])
        if abs(s) >= SIZE_FLOOR:
            (gains if s < 0 else losses).add("FASTER" if s < 0 else "SLOWER")
    return [g for g in R.GAINS if g in gains], sorted(losses)


def label_of(gains, losses, valid, at_limit):
    if not valid:
        return "INVALID"
    if losses:
        return R.BOTH if gains else R.AWAY
    if gains:
        return " + ".join(gains)
    return R.AT_LIMIT if at_limit else R.SAME


def reread(data):
    for m in data["muscles"]:
        all_g, all_l = set(), set()
        for load, o in m["loads"].items():
            g, l = gains_losses(o["per_seed"], float(o.get("native_viol_share") or 0.0))
            o["label"] = label_of(g, l, o["valid"], o["label"] == R.AT_LIMIT)
            all_g.update(g); all_l.update(l)
        if not m["valid"]:
            m["label"] = "INVALID"
        elif all_l:
            m["label"] = R.BOTH if all_g else R.AWAY
        elif all_g:
            m["label"] = " + ".join(g for g in R.GAINS if g in all_g)
        else:
            m["label"] = R.AT_LIMIT if all(o["label"] == R.AT_LIMIT for o in m["loads"].values()) else R.SAME
    for load, by_name in data["organisms"].items():
        for name, o in by_name.items():
            t = o.get("totals", {})
            share = t.get("viol_native", 0) / t["steps"] if t.get("steps") else 0.0
            g, l = gains_losses(o["per_seed"], share)
            o["label"] = label_of(g, l, o["valid"], False)
    data["run"]["reread"] = NOTE
    return data


def csv_rows(data):
    cols = ["muscle_id", "family", "muscle", "realm", "template", "preset", "knob", "label_all_loads", "load", "label",
            "work", "work_lo", "work_hi", "viol_pp", "viol_pp_lo", "viol_pp_hi", "line_native_min", "line_omni_min",
            "power_given", "wear", "work_per_energy", "writes_per_run", "native_viol_share", "valid"]
    out = [cols]
    for r in data["muscles"]:
        row = r["row"]
        for load, o in r["loads"].items():
            s, ln = o["summary"], o["line"]
            out.append([row["muscle_id"], row["family"], row["muscle"], row["realm"], row["template"], row["preset"],
                        row["knob"], r["label"], load, o["label"], *(f"{x:.5f}" for x in s["work"]),
                        *(f"{x:.3f}" for x in s["viol_pp"]), *((f"{ln[0]:.2f}", f"{ln[1]:.2f}") if ln else ("", "")),
                        f"{s['energy'][0]:.5f}", f"{o['wear']:.5f}", f"{s['primary'][0]:.5f}", f"{o['writes']:.1f}",
                        f"{o['native_viol_share']:.4f}", str(o["valid"])])
    return out


def main(argv) -> int:
    check = "--check" in argv
    js = OUT / "REALMS_V5.json"
    before = js.read_text(encoding="utf-8")
    data = reread(json.loads(before))
    labels_before = {(m["row"]["muscle_id"], ld): o["label"] for m in json.loads(before)["muscles"] for ld, o in m["loads"].items()}
    labels_after = {(m["row"]["muscle_id"], ld): o["label"] for m in data["muscles"] for ld, o in m["loads"].items()}
    moved = sum(1 for k in labels_after if labels_after[k] != labels_before.get(k))
    new_js = json.dumps(data, indent=1) + "\n"
    if check:
        same = new_js == before
        print(f"realms reread: {'every label reads by the rule that stands' if same else f'{moved} labels differ from the rule: run python3 tools/realms_reread.py'}")
        return 0 if same else 1
    js.write_text(new_js, encoding="utf-8")
    with (OUT / "MUSCLES_V5.csv").open("w", newline="") as f:
        csv.writer(f).writerows(csv_rows(data))
    R.write_md(OUT, data["muscles"], data["organisms"], data["run"])
    md = OUT / "REALMS_V5.md"
    t = md.read_text(encoding="utf-8")
    if NOTE not in t:
        head, _, rest = t.partition("\n\n")
        notice, _, rest2 = rest.partition("\n\n")
        md.write_text(f"{head}\n\n{notice}\n\n*{NOTE}*\n\n{rest2}", encoding="utf-8")
    files = sorted(p for p in OUT.iterdir() if p.is_file() and p.name != "SHA256SUMS.txt")
    (OUT / "SHA256SUMS.txt").write_text("".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n" for p in files))
    print(f"realms reread: {moved} of {len(labels_after)} muscle labels moved by the rule that stands")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
