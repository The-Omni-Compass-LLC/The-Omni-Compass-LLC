# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Closed-loop clients stepping by one: each client sends its next request when the last one is answered and it has
thought for a moment, so a slower answer brings fewer requests, as people and programs do. The number of clients follows
the steps (1 2 3 2 3 4 ...). Every answer is checked: its digest must be the one known for its seed, computed here
before the first request. Every request is one row of the record: when it was sent, how long it took, its status, and
whether its answer was right."""
from __future__ import annotations

import argparse
import csv
import http.client
import json
import random
import threading
import time

from omni_orchestrator.workload import chain


def run(port: int, k: int, steps: list[int], step_s: float, think_s: float, out: str, start_at: float = 0.0) -> None:
    known = {n: chain(n, k) for n in range(100)}
    rows: list[tuple] = []
    lock = threading.Lock()
    active = [0]
    stop = threading.Event()
    if start_at > time.time():
        time.sleep(start_at - time.time())
    t0 = time.time()

    def client(i: int) -> None:
        rng = random.Random(i)
        conn = None
        while not stop.is_set():
            if i >= active[0]:
                time.sleep(0.05)
                continue
            n = rng.randrange(100)
            sent = time.time()
            status, right = 0, False
            try:
                if conn is None:
                    conn = http.client.HTTPConnection("127.0.0.1", port, timeout=60)
                conn.request("GET", f"/work?n={n}")
                r = conn.getresponse()
                body = r.read()
                status = r.status
                right = status == 200 and json.loads(body).get("digest") == known[n]
            except Exception:
                if conn is not None:
                    conn.close()
                conn = None
            with lock:
                rows.append((round(sent - t0, 3), round(1000.0 * (time.time() - sent), 2), status, int(right)))
            if status != 200:
                time.sleep(0.2)
            time.sleep(think_s)

    threads = [threading.Thread(target=client, args=(i,), daemon=True) for i in range(max(steps))]
    for t in threads:
        t.start()
    for c in steps:
        active[0] = c
        time.sleep(step_s)
    stop.set()
    for t in threads:
        t.join(70)
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["sent_s", "ms", "status", "right"])
        w.writerows(sorted(rows))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--port", type=int, required=True)
    ap.add_argument("--k", type=int, required=True)
    ap.add_argument("--steps", required=True, help="clients per step, e.g. 1,2,3,2,3,4")
    ap.add_argument("--step-s", type=float, default=30.0)
    ap.add_argument("--think-s", type=float, default=0.1)
    ap.add_argument("--start-at", type=float, default=0.0)
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    run(a.port, a.k, [int(x) for x in a.steps.split(",")], a.step_s, a.think_s, a.out, a.start_at)


if __name__ == "__main__":
    main()

# © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
