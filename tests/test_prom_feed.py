# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Prometheus feed adapter (tools/prom_feed.py) against a stand-in Prometheus: one ok row per quantile in the
governor's format, failure rows up to the cap, nothing for an empty window or an unreachable server, a clock that goes on
across a restart, and a file the governor's own reader takes."""
import json
import sys
import tempfile
import threading
import unittest
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))
import prom_feed  # noqa: E402
from omni_controller.muscles import latency_window, latency_p95  # noqa: E402

STATE = {"served": 100.0, "failed": 3.0}


class Standin(BaseHTTPRequestHandler):
    def do_GET(self):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)["query"][0]
        if q.startswith("served"):
            v = STATE["served"]
        elif q.startswith("failed"):
            v = STATE["failed"]
        else:                                    # "quantile 0.05 30s": the q-th quantile of a 100-600 ms spread, seconds
            v = (100 + 500 * float(q.split()[1])) / 1000.0
        res = [] if v is None else [{"metric": {}, "value": [0, str(v)]}]
        body = json.dumps({"status": "success", "data": {"resultType": "vector", "result": res}}).encode()
        self.send_response(200); self.send_header("Content-Type", "application/json"); self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):
        pass


class PromFeed(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = HTTPServer(("127.0.0.1", 0), Standin)
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()
        cls.base = f"http://127.0.0.1:{cls.srv.server_address[1]}"

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown(); cls.srv.server_close()

    def run_once(self, out, base=None):
        return prom_feed.main(["--prometheus", base or self.base, "--served", "served {w}", "--failed", "failed {w}",
                               "--quantile", "quantile {q} {w}", "--out", str(out), "--once", "--fail-cap", "5"])

    def test_rows_clock_and_reader(self):
        with tempfile.TemporaryDirectory() as t:
            out = Path(t) / "latency.csv"
            STATE.update(served=100.0, failed=3.0)
            self.run_once(out)
            lines = out.read_text().splitlines()
            self.assertEqual(lines[0], "elapsed_seconds,latency_ms,ok")
            ok = [l for l in lines[1:] if l.endswith(",1")]
            bad = [l for l in lines[1:] if l.endswith(",0")]
            self.assertEqual(len(ok), 10, "one row per default quantile")
            self.assertEqual(len(bad), 3, "one row per failed request")
            ms = sorted(float(l.split(",")[1]) for l in ok)
            self.assertAlmostEqual(ms[0], 125.0, places=1); self.assertAlmostEqual(ms[-1], 575.0, places=1)
            # the failure cap
            STATE.update(failed=40.0)
            self.run_once(out)
            last = out.read_text().splitlines()
            self.assertEqual(sum(1 for l in last if l.endswith(",0")), 3 + 5)
            # an empty window and an unreachable server write nothing
            STATE.update(served=0.0, failed=0.0)
            n = len(out.read_text().splitlines())
            self.run_once(out)
            self.run_once(out, base="http://127.0.0.1:9")
            self.assertEqual(len(out.read_text().splitlines()), n)
            # the clock goes on across a restart: never back, header written once
            t_rows = [float(l.split(",")[0]) for l in out.read_text().splitlines()[1:]]
            self.assertTrue(all(b >= a for a, b in zip(t_rows, t_rows[1:])))
            self.assertGreaterEqual(t_rows[-1], 15.0, "the second read continued from the first plus one interval")
            self.assertEqual(out.read_text().count("elapsed_seconds"), 1)
            # the governor's own reader takes the file: served rows, not blind, a p95 inside the spread
            w = latency_window(str(out), 60.0)
            self.assertFalse(w["blind"]); self.assertEqual(len(w["ms"]), 20)
            self.assertTrue(125.0 <= latency_p95(str(out), 60.0) <= 575.0)


def main():
    r = unittest.TextTestRunner(verbosity=0).run(unittest.defaultTestLoader.loadTestsFromTestCase(PromFeed))
    if not r.wasSuccessful():
        raise SystemExit(1)
    print("PASS prom feed: a row per quantile, failures capped, nothing for an empty window or a silent server, the clock "
          "never goes back, and the governor's reader takes the file")


if __name__ == "__main__":
    main()
