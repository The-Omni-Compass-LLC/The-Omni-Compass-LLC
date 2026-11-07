#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The governor's response-time feed from the company's own Prometheus (the Operator's Manual, section 22.7).

Every --interval seconds it asks Prometheus, over its HTTP query API, for the requests the service served and failed in
the last --window, and for the served requests' response-time quantiles over the same window, and appends rows
elapsed_seconds,latency_ms,ok to --out, the format the governor reads (--latency-file):

  * one row with ok=1 for each quantile in --quantiles (by default the midpoints of ten equal shares of the requests,
    0.05, 0.15, ..., 0.95), so each row stands for an equal share of the window's served requests and the rows'
    own distribution is the window's, to the precision of the service's histogram buckets;
  * one row with ok=0 for each failed request, up to --fail-cap a window;
  * nothing for a window in which the service served and failed nothing, or in which Prometheus did not answer: the
    governor reads a feed with no new row for twice its window as blind, which is the right reading.

The clock (elapsed_seconds) continues across restarts: a restarted adapter reads the last row of --out and goes on from
it, so the governor's reading and its trials never see the clock go back. It never rewrites or truncates the file.

The queries are PromQL templates: {w} becomes the window (for example 30s) and, in --quantile, {q} the quantile. With the
NGINX ingress controller, for example:

  --served   'sum(increase(nginx_ingress_controller_requests{ingress="checkout",status!~"5.."}[{w}]))'
  --failed   'sum(increase(nginx_ingress_controller_requests{ingress="checkout",status=~"5.."}[{w}]))'
  --quantile 'histogram_quantile({q}, sum by (le) (increase(nginx_ingress_controller_request_duration_seconds_bucket{ingress="checkout"}[{w}])))'
  --unit-ms 1000   (the histogram is in seconds)

Usage: python3 tools/prom_feed.py --prometheus http://prometheus.monitoring:9090 --served ... --failed ... \\
         --quantile ... --out /feed/latency.csv [--interval 15] [--window 30s] [--once]
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
import urllib.parse
import urllib.request

HEADER = "elapsed_seconds,latency_ms,ok\n"
DEFAULT_QUANTILES = ",".join(f"{0.05 + 0.1 * i:.2f}" for i in range(10))


def query(base: str, promql: str, at: float, timeout: float = 10.0):
    """One instant query; the first sample's value as a float, or None (no data, NaN, or an error)."""
    url = base.rstrip("/") + "/api/v1/query?" + urllib.parse.urlencode({"query": promql, "time": f"{at:.3f}"})
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            body = json.loads(r.read().decode())
    except (OSError, ValueError) as e:
        print(f"prom_feed: query failed: {e}", file=sys.stderr, flush=True)
        return None
    if body.get("status") != "success":
        print(f"prom_feed: query refused: {body.get('error', body)}", file=sys.stderr, flush=True)
        return None
    res = (body.get("data") or {}).get("result") or []
    if not res:
        return None
    try:
        v = float(res[0]["value"][1])
    except (KeyError, IndexError, TypeError, ValueError):
        return None
    return v if math.isfinite(v) else None


def last_elapsed(path: str):
    """The elapsed_seconds of the file's last row, or None when the file is absent or has no rows."""
    try:
        with open(path, "rb") as f:
            f.seek(0, os.SEEK_END)
            size = f.tell()
            f.seek(max(0, size - 4096))
            lines = f.read().decode(errors="replace").strip().splitlines()
    except OSError:
        return None
    for line in reversed(lines):
        head = line.split(",")[0]
        try:
            return float(head)
        except ValueError:
            continue
    return None


def rows_for(base: str, a, at: float, elapsed: float):
    """The rows for the window ending at `at`: quantile rows if anything was served, failure rows up to the cap."""
    w = a.window
    served = query(base, a.served.replace("{w}", w), at)
    failed = query(base, a.failed.replace("{w}", w), at) if a.failed else 0.0
    out = []
    if served is not None and served > 0:
        for q in a.quantiles:
            v = query(base, a.quantile.replace("{w}", w).replace("{q}", f"{q:g}"), at)
            if v is not None and v >= 0:
                out.append(f"{elapsed:.1f},{v * a.unit_ms:.1f},1\n")
    if failed is not None and failed > 0:
        out.extend(f"{elapsed:.1f},0.0,0\n" for _ in range(min(int(round(failed)), a.fail_cap)))
    return out


def parser():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--prometheus", required=True, help="Prometheus base URL")
    ap.add_argument("--served", required=True, help="PromQL: requests served in the window ({w})")
    ap.add_argument("--failed", default="", help="PromQL: requests failed in the window ({w}); empty: none counted")
    ap.add_argument("--quantile", required=True, help="PromQL: the served requests' quantile {q} over the window {w}")
    ap.add_argument("--quantiles", default=DEFAULT_QUANTILES, help="comma-separated quantiles, one row each")
    ap.add_argument("--unit-ms", type=float, default=1000.0, help="milliseconds per unit of the quantile (1000: seconds)")
    ap.add_argument("--interval", type=float, default=15.0, help="seconds between windows read")
    ap.add_argument("--window", default="30s", help="PromQL range of each read; at least twice the scrape interval")
    ap.add_argument("--fail-cap", type=int, default=20, help="most failure rows written a window")
    ap.add_argument("--out", required=True, help="the feed file the governor reads")
    ap.add_argument("--once", action="store_true", help="read one window and exit")
    ap.add_argument("--duration", type=float, default=0.0, help="seconds to run (0: until stopped)")
    return ap


def main(argv=None):
    a = parser().parse_args(argv)
    a.quantiles = [float(x) for x in a.quantiles.split(",") if x.strip()]
    if not a.quantiles or any(not 0.0 < q < 1.0 for q in a.quantiles):
        raise SystemExit("prom_feed: every quantile must lie strictly between 0 and 1")
    prev = last_elapsed(a.out)
    offset = 0.0 if prev is None else prev + a.interval       # a restart continues the clock, never restarts it
    if prev is None and (not os.path.exists(a.out) or os.path.getsize(a.out) == 0):
        with open(a.out, "a") as f:
            f.write(HEADER)
    t0 = time.monotonic(); start = time.time(); k = 0
    while True:
        at = time.time()
        elapsed = offset + (time.monotonic() - t0)
        rows = rows_for(a.prometheus, a, at, elapsed)
        if rows:
            with open(a.out, "a") as f:
                f.writelines(rows)
        k += 1
        if a.once or (a.duration and time.time() - start >= a.duration):
            return 0
        time.sleep(max(0.0, t0 + k * a.interval - time.monotonic()))


if __name__ == "__main__":
    sys.exit(main())
