# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The showing's organism: a service and a batch task, each doing real processor work whose result can be checked.

The work is a chain of k SHA-256 hashes from a seed; the digest is fixed by the seed and k, so a client that knows the
digest of a seed knows whether the answer it got is right.

  serve  an HTTP service on 127.0.0.1:<port>: GET /work?n=<seed> answers {"n", "digest", "unit"}, GET /health "ok".
         SIGTERM stops it taking new connections and lets the answer in hand finish.
  task   one batch task: the chain from seed job*1000+index, written to <out>/<job>-<index>.json; exit 0 when done.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import signal
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse


def chain(n: int, k: int) -> str:
    h = int(n).to_bytes(8, "big")
    for _ in range(k):
        h = hashlib.sha256(h).digest()
    return h.hex()[:16]


def calibrate(cpu_ms: float) -> int:
    """The chain length that takes about cpu_ms of processor time on this machine."""
    k = 2000
    while True:
        t0 = time.process_time()
        chain(1, k)
        dt = time.process_time() - t0
        if dt > 0.05:
            return max(1, int(k * cpu_ms / 1000.0 / dt))
        k *= 2


def serve(port: int, k: int, unit: str) -> None:
    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def do_GET(self):
            u = urlparse(self.path)
            if u.path == "/health":
                body, ctype = b"ok", "text/plain"
            elif u.path == "/work":
                n = int(parse_qs(u.query).get("n", ["0"])[0])
                body, ctype = json.dumps({"n": n, "digest": chain(n, k), "unit": unit}).encode(), "application/json"
            else:
                self.send_error(404)
                return
            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *a):
            pass

    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    srv.daemon_threads = True

    def stop(*_):
        threading.Thread(target=srv.shutdown, daemon=True).start()

    signal.signal(signal.SIGTERM, stop)
    srv.serve_forever(poll_interval=0.2)
    time.sleep(0.3)                                      # the answer in hand finishes before the process ends


def task(job: str, index: int, k: int, out: str) -> None:
    seed = (sum(job.encode()) % 1000) * 1000 + index
    d = chain(seed, k)
    p = Path(out)
    p.mkdir(parents=True, exist_ok=True)
    tmp = p / f".{job}-{index}.tmp"
    tmp.write_text(json.dumps({"job": job, "index": index, "seed": seed, "k": k, "digest": d}))
    os.replace(tmp, p / f"{job}-{index}.json")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("serve")
    s.add_argument("--port", type=int, required=True)
    s.add_argument("--k", type=int, required=True)
    s.add_argument("--unit", default=os.environ.get("OMNI_UNIT", "?"))
    t = sub.add_parser("task")
    t.add_argument("--job", required=True)
    t.add_argument("--index", type=int, required=True)
    t.add_argument("--k", type=int, required=True)
    t.add_argument("--out", required=True)
    c = sub.add_parser("calibrate")
    c.add_argument("--cpu-ms", type=float, required=True)
    a = ap.parse_args(argv)
    if a.cmd == "serve":
        serve(a.port, a.k, a.unit)
    elif a.cmd == "task":
        task(a.job, a.index, a.k, a.out)
    else:
        print(calibrate(a.cpu_ms))


if __name__ == "__main__":
    main()

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
