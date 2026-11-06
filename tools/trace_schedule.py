#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""A public demand trace turned into the load schedule of the real Kubernetes test (docs/TRACES_PREREGISTRATION.md).

The six Kubernetes tests drive the cluster with load schedules of our own (1 2 3 2 3 4 ...). A referee may ask whether
the shape of our own schedules flatters the governor. This tool derives a schedule from a demand trace somebody else
published, by a rule written before the runs, and writes a receipt that lets anyone re-derive it:

  Google cluster-usage traces 2011 (clusterdata-2011-2, the job_events table, public): the number of jobs submitted
  (event type 0) in each hour of the trace's first day (the trace starts at 600 s; events stamped 0 are jobs that
  existed before the trace and are not counted). 24 hourly counts.

  Mapping (the rule the organism runs already use, docs/K8S_COMPASS_PREREGISTRATION.md): the counts are placed on the
  load generator's range by min and max, r_raw(k) = LOAD_MIN + round((LOAD_MAX - LOAD_MIN) (c_k - min c) / (max c - min c)),
  LOAD_MIN 1, LOAD_MAX 8 (the wandering test's peak). Then the founder's rule for real traffic (the amendment to the
  wandering test, 2026-10-04): the schedule moves one step a bin toward the trace's level, never skipping; the first bin
  starts at its own level. Each bin is replayed as one step of 108 s (the wandering test's step), 24 steps, 2,592 s a day:
  a day in 43 minutes. The raw levels and the stepped schedule are both in the receipt.

Usage: python tools/trace_schedule.py --out results/traces/google2011 [--cache DIR] [--max-parts 24] [--load-max 8]
       python tools/trace_schedule.py --out results/traces/google2011_1to9 --load-max 9 --counts-from results/traces/google2011
  --load-max sets the top of the load generator's range (the bottom stays 1); --counts-from takes the hourly counts from a
  receipt already derived (its parts and their SHA-256 are carried over, nothing is downloaded) and places them on the new
  range by the same rule.
  writes <out>/schedule.json (the receipt: source, parts, their SHA-256, the counts, the levels, the steps, the rule),
  <out>/LOAD_STEPS.txt (the one line the workflow takes as load_steps) and prints both. Needs the network for the
  download (about 0.8 MB a part, 16 parts for a day); a cache directory keeps the parts for re-derivation offline."""
from __future__ import annotations

import argparse, csv, datetime, gzip, hashlib, io, json, math, sys, urllib.request
from pathlib import Path

GOOGLE_URL = "https://storage.googleapis.com/clusterdata-2011-2/job_events/part-{i:05d}-of-00500.csv.gz"
SOURCE = ("Google cluster-usage traces 2011 (clusterdata-2011-2), table job_events, public bucket clusterdata-2011-2 on "
          "Google Cloud Storage; column 1 the time in microseconds, column 4 the event type; event type 0 is SUBMIT")
TRACE_START_S = 600            # the trace's own start; earlier stamps are jobs that existed before it
DAY_S = 86_400
BINS = 24                      # one bin an hour of the trace
STEP_S = 108                   # the wandering test's step
LOAD_MIN, LOAD_MAX = 1, 8      # the wandering test's range of load-generator replicas
SUBMIT = 0


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def fetch_part(i: int, cache: Path) -> Path:
    """The i-th part of job_events, downloaded once into the cache."""
    cache.mkdir(parents=True, exist_ok=True)
    p = cache / f"part-{i:05d}-of-00500.csv.gz"
    if not p.exists():
        with urllib.request.urlopen(GOOGLE_URL.format(i=i), timeout=120) as r, open(p, "wb") as f:
            f.write(r.read())
    return p


def read_part(path: Path):
    """(time in seconds, event type) for every row of one part."""
    with gzip.open(path, "rt", newline="") as f:
        for row in csv.reader(f):
            if len(row) < 4 or not row[0] or not row[3]:
                continue
            yield int(row[0]) / 1e6, int(row[3])


def rnd(x: float) -> int:
    """Round half up (the K8S preregistration's 'round'), the same on every machine."""
    return int(math.floor(x + 0.5))


def bin_counts(rows, bins=BINS, start_s=TRACE_START_S, span_s=DAY_S):
    """Submits per bin over [start_s, start_s + span_s); the last time seen (to know the day was covered)."""
    counts = [0] * bins; bin_s = span_s / bins; last = -1.0
    for t, ev in rows:
        last = max(last, t)
        if ev != SUBMIT or t < start_s or t >= start_s + span_s:
            continue
        counts[min(bins - 1, int((t - start_s) // bin_s))] += 1
    return counts, last


def levels(counts, lo=LOAD_MIN, hi=LOAD_MAX):
    """Counts placed on [lo, hi] by min and max; a flat trace sits at lo."""
    cmin, cmax = min(counts), max(counts)
    if cmax == cmin:
        return [lo] * len(counts)
    return [lo + rnd((hi - lo) * (c - cmin) / (cmax - cmin)) for c in counts]


def one_step(raw):
    """The founder's rule for real traffic: one step a bin toward the trace's level, never skipping."""
    out = [raw[0]]
    for want in raw[1:]:
        cur = out[-1]
        out.append(cur + (1 if want > cur else -1 if want < cur else 0))
    return out


def derive(cache: Path, max_parts=24, bins=BINS, start_s=TRACE_START_S, span_s=DAY_S, lo=LOAD_MIN, hi=LOAD_MAX,
           step_s=STEP_S, fetch=fetch_part):
    """Read parts until the day is covered (or max_parts), count, map, step; the receipt."""
    counts = [0] * bins; parts = []; last = -1.0
    for i in range(max_parts):
        p = fetch(i, cache)
        c, l = bin_counts(read_part(p), bins, start_s, span_s)
        counts = [a + b for a, b in zip(counts, c)]; last = max(last, l)
        parts.append({"part": p.name, "url": GOOGLE_URL.format(i=i), "sha256": sha256(p), "last_time_s": round(l, 3)})
        if last >= start_s + span_s:
            break
    raw = levels(counts, lo, hi); steps = one_step(raw)
    return {"source": SOURCE, "parts": parts, "covered": last >= start_s + span_s,
            "window": {"start_s": start_s, "span_s": span_s, "bins": bins, "bin_s": span_s / bins},
            "submits": counts, "levels_raw": raw, "steps": steps,
            "load_min": lo, "load_max": hi, "step_s": step_s, "measured_s": step_s * bins,
            "rule": ("r_raw(k) = LOAD_MIN + round((LOAD_MAX - LOAD_MIN) (c_k - min c) / (max c - min c)); then one step a bin toward "
                     "r_raw(k), never skipping (the founder's rule for real traffic, docs/K8S_COMPASS_PREREGISTRATION.md, the "
                     "amendment to the wandering test); each bin one step of step_s seconds"),
            "generated_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}


def remap(rec, lo=LOAD_MIN, hi=LOAD_MAX):
    """A receipt's own counts placed on [lo, hi] by the same rule: the new levels, steps and range; the source, the parts
    and their SHA-256 carried over, so the new schedule is re-derived from the same trace."""
    raw = levels(rec["submits"], lo, hi); steps = one_step(raw)
    out = dict(rec)
    out.update({"levels_raw": raw, "steps": steps, "load_min": lo, "load_max": hi,
                "measured_s": rec["step_s"] * len(steps), "remapped_from": rec.get("generated_utc"),
                "generated_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")})
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True, help="directory for schedule.json and LOAD_STEPS.txt")
    ap.add_argument("--cache", default=None, help="where the downloaded parts are kept (default: <out>/parts)")
    ap.add_argument("--max-parts", type=int, default=24)
    ap.add_argument("--load-max", type=int, default=LOAD_MAX, help="the top of the load generator's range (default 8)")
    ap.add_argument("--counts-from", default=None, help="a receipt directory already derived: its counts, no download")
    a = ap.parse_args(argv)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    if a.counts_from:
        rec = remap(json.loads((Path(a.counts_from) / "schedule.json").read_text()), LOAD_MIN, a.load_max)
    else:
        cache = Path(a.cache) if a.cache else out / "parts"
        rec = derive(cache, a.max_parts, hi=a.load_max)
    (out / "schedule.json").write_text(json.dumps(rec, indent=1) + "\n")
    (out / "LOAD_STEPS.txt").write_text(" ".join(str(s) for s in rec["steps"]) + "\n")
    print(f"{len(rec['parts'])} parts, day covered: {rec['covered']}")
    print("submits an hour:", rec["submits"])
    print("levels (raw):   ", rec["levels_raw"])
    print("LOAD_STEPS:     ", " ".join(str(s) for s in rec["steps"]))
    print(f"{len(rec['steps'])} steps of {rec['step_s']} s = {rec['measured_s']} measured seconds")
    return 0 if rec["covered"] else 2


if __name__ == "__main__":
    sys.exit(main())
