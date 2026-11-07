# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The public-trace schedule (tools/trace_schedule.py, docs/TRACES_PREREGISTRATION.md) against synthetic parts, no
network: submits counted per hour inside the trace's first day only (stamps before the trace's start and other event
types are not counted), the min-max mapping onto 1..8 with half-up rounding, the one-step rule, parts read until the day
is covered, and the receipt naming every part with its SHA-256."""
import gzip
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import trace_schedule as T


def write_part(path, rows):
    """rows: (time_s, event_type) written the way the trace is (microseconds, event type in column 4)."""
    with gzip.open(path, "wt", newline="") as f:
        for t, ev in rows:
            f.write(f"{int(t * 1e6)},,1,{ev},u,0,n,l\n")


def main():
    # mapping and rounding: half up, a flat trace sits at the floor
    assert T.rnd(4.5) == 5 and T.rnd(4.49) == 4 and T.rnd(0.5) == 1
    assert T.levels([0, 70, 35]) == [1, 8, 5], T.levels([0, 70, 35])
    assert T.levels([3, 3, 3]) == [1, 1, 1]
    # the founder's rule: one step a bin toward the level, never skipping; the first bin at its own level
    assert T.one_step([1, 8, 5]) == [1, 2, 3]
    assert T.one_step([4, 4, 1, 1, 1, 6]) == [4, 4, 3, 2, 1, 2]
    assert T.one_step([8]) == [8]
    # counting: only SUBMIT (0), only inside [600, 600 + 86400), stamps before the trace's start left out
    rows = [(0, 0), (599, 0), (600, 0), (600, 1), (3600 + 599.9, 0), (3600 + 600, 0), (600 + 86399, 0), (600 + 86400, 0)]
    counts, last = T.bin_counts(rows)
    assert counts[0] == 2 and counts[1] == 1 and counts[23] == 1 and sum(counts) == 4 and last == 600 + 86400, (counts, last)
    with tempfile.TemporaryDirectory() as d:
        cache = Path(d)
        # three synthetic parts: the first two cover the day (hour k gets k+1 submits), the third is never fetched
        hours = {k: (k + 1) for k in range(24)}
        rows1 = [(600 + h * 3600 + 10 * j, 0) for h in range(12) for j in range(hours[h])] + [(0, 0), (100, 0)]
        rows2 = [(600 + h * 3600 + 10 * j, 0) for h in range(12, 24) for j in range(hours[h])] + [(600 + 86400 + 5, 0), (600 + 86400 + 6, 4)]
        write_part(cache / "part-00000-of-00500.csv.gz", rows1); write_part(cache / "part-00001-of-00500.csv.gz", rows2)
        fetched = []

        def fetch(i, c):
            fetched.append(i); p = c / f"part-{i:05d}-of-00500.csv.gz"
            assert p.exists(), f"part {i} was asked for after the day was covered"
            return p
        rec = T.derive(cache, max_parts=5, fetch=fetch)
        assert fetched == [0, 1] and rec["covered"], (fetched, rec["covered"])
        assert rec["submits"] == [k + 1 for k in range(24)], rec["submits"]
        assert rec["levels_raw"][0] == 1 and rec["levels_raw"][-1] == 8 and rec["levels_raw"][11] == T.rnd(1 + 7 * 11 / 23)
        assert rec["steps"] == T.one_step(rec["levels_raw"]) and all(abs(a - b) <= 1 for a, b in zip(rec["steps"], rec["steps"][1:]))
        assert len(rec["parts"]) == 2 and all(len(p["sha256"]) == 64 for p in rec["parts"]) and rec["parts"][0]["url"].endswith("part-00000-of-00500.csv.gz")
        assert rec["measured_s"] == 24 * 108 and rec["window"]["bin_s"] == 3600
        # a day not covered is said so (one part only)
        rec2 = T.derive(cache, max_parts=1, fetch=fetch)
        assert not rec2["covered"] and sum(rec2["submits"]) == sum(k + 1 for k in range(12))
        json.dumps(rec)                                     # the receipt is plain JSON
        # the same counts placed on 1..9 (the founder's words of 14 October): same rule, nothing downloaded, parts kept
        r9 = T.remap(rec, 1, 9)
        assert r9["submits"] == rec["submits"] and r9["parts"] == rec["parts"] and r9["load_max"] == 9
        assert r9["levels_raw"] == T.levels(rec["submits"], 1, 9) and r9["levels_raw"][-1] == 9
        assert r9["steps"] == T.one_step(r9["levels_raw"]) and r9["measured_s"] == 24 * 108
        assert T.remap(rec, 1, 8)["steps"] == rec["steps"]  # the 1..8 schedule re-derives unchanged
    # the repository's own 1..9 receipt is the Google day's counts on 1..9
    here = Path(__file__).resolve().parents[1] / "results" / "traces"
    g8, g9 = (json.loads((here / d / "schedule.json").read_text()) for d in ("google2011", "google2011_1to9"))
    assert g9["submits"] == g8["submits"] and g9["steps"] == T.one_step(T.levels(g8["submits"], 1, 9)), g9["steps"]
    assert (here / "google2011_1to9" / "LOAD_STEPS.txt").read_text().split() == [str(x) for x in g9["steps"]]
    print("PASS  public-trace schedule: submits counted per hour of the trace's first day only, min-max onto 1..8 with half-up "
          "rounding, one step a bin toward the level, parts read until the day is covered, every part named with its SHA-256; "
          "the same counts re-placed on 1..9 by the same rule with nothing downloaded")


if __name__ == "__main__":
    main()
