# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The governor's gauges for Prometheus (tools/omni_exporter.py): each gauge read from the audit records the governor
writes, the page in Prometheus's text format, the server read-only, and the Grafana screen reading only gauges the
exporter serves."""
import json, re, sys, tempfile, threading, time, unittest, urllib.error, urllib.request
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
import tools.omni_exporter as EX


def decision(t, hpa, nodes=6, cap=1.0, pos=0.5, force=0.0):
    return {"time": t, "decision": {"nodes_observed": nodes, "nodes_recommended": nodes, "hpa_target_recommended": hpa,
                                    "power_cap": cap, "compass_law": {"position": pos, "force": force}}, "mode": "nodepool"}


AUDIT = [
    {"time": 1.0, "authority": {"senses": {"blind": {"power": False, "latency": True}}}},
    decision(1.1, 0.70, cap=0.695),
    {"time": 1.2, "write": ["kubectl", "patch"], "why": "HPA target to rho* = 75%", "dry_run": False},
    {"time": 1.3, "decision_ms": 500.0},
    decision(61.1, 0.75, cap=1.0),                              # up
    {"time": 61.3, "decision_ms": 700.0},
    decision(121.1, 0.72, cap=0.695, pos=0.6, force=-0.2),      # down: a reversal on both
    {"time": 121.2, "write": ["kubectl", "annotate"], "why": "convey: record original CPU limit", "dry_run": False},
    {"time": 121.3, "decision_ms": 600.0},
    {"time": 150.0, "verdict": {"verdict": "trial", "step": 1}, "state": "trial", "machines_given_back_allowed": 0,
     "machines_native": 6},
    {"time": 181.0, "decision": "master switch: OFF; every setting handed back; exiting"},
    {"time": 181.1, "overhead": {"cpu_s": 1.0, "wall_s": 181.0, "cores_mean": 0.0055}},
]


def gauges(lines):
    g = EX.Gauges()
    for ln in lines:
        g.feed(ln if isinstance(ln, str) else json.dumps(ln))
    return g


def value(page, name, labels=""):
    m = re.search(rf"^{re.escape(name)}{re.escape(labels)} (\S+)$", page, re.M)
    return None if m is None else float(m.group(1))


class Exporter(unittest.TestCase):
    def test_every_gauge_from_its_record(self):
        p = gauges(AUDIT).page()
        self.assertEqual(value(p, "omni_decisions_total"), 3)
        self.assertEqual(value(p, "omni_decision_seconds_count"), 3)
        self.assertAlmostEqual(value(p, "omni_decision_seconds_sum"), 1.8)
        self.assertAlmostEqual(value(p, "omni_decision_seconds_last"), 0.6)
        self.assertAlmostEqual(value(p, "omni_last_decision_timestamp_seconds"), 121.3)
        self.assertAlmostEqual(value(p, "omni_heartbeat_seconds"), 60.0)
        self.assertEqual(value(p, "omni_writes_total", '{why="HPA target"}'), 1)
        self.assertEqual(value(p, "omni_writes_total", '{why="convey"}'), 1)
        self.assertAlmostEqual(value(p, "omni_recommended", '{setting="hpa_target"}'), 0.72)
        self.assertEqual(value(p, "omni_recommended_moves_total", '{setting="hpa_target"}'), 2)
        self.assertEqual(value(p, "omni_recommended_reversals_total", '{setting="hpa_target"}'), 1)
        self.assertEqual(value(p, "omni_recommended_reversals_total", '{setting="power_cap"}'), 1)
        self.assertEqual(value(p, "omni_recommended_moves_total", '{setting="nodes"}'), 0)
        self.assertEqual(value(p, "omni_sense_blind", '{sense="latency"}'), 1)
        self.assertEqual(value(p, "omni_sense_blind", '{sense="power"}'), 0)
        self.assertEqual(value(p, "omni_verdict_state", '{state="trial"}'), 1)
        self.assertEqual(value(p, "omni_master_switch"), 0)
        self.assertAlmostEqual(value(p, "omni_own_cpu_cores"), 0.0055)
        self.assertAlmostEqual(value(p, "omni_compass_position"), 0.6)
        self.assertEqual(value(p, "omni_audit_unreadable_total"), 0)

    def test_a_steady_setting_never_counts_a_reversal(self):
        p = gauges([decision(t, 0.7) for t in range(10)]).page()
        self.assertEqual(value(p, "omni_recommended_moves_total", '{setting="hpa_target"}'), 0)
        self.assertEqual(value(p, "omni_recommended_reversals_total", '{setting="hpa_target"}'), 0)
        self.assertEqual(value(p, "omni_master_switch"), 1)

    def test_a_climb_is_moves_without_reversals(self):
        p = gauges([decision(t, 0.5 + 0.05 * t) for t in range(6)]).page()
        self.assertEqual(value(p, "omni_recommended_moves_total", '{setting="hpa_target"}'), 5)
        self.assertEqual(value(p, "omni_recommended_reversals_total", '{setting="hpa_target"}'), 0)

    def test_the_control_quality_figures(self):
        lines = [decision(0, 0.70, pos=0.02), decision(60, 0.72, pos=0.5), decision(120, 0.70, pos=0.97),
                 decision(180, 0.75, pos=1.0), decision(240, 0.75, pos=0.6), decision(300, 0.75, pos=0.99),
                 decision(360, 0.75, pos=0.4),
                 {"time": 361, "error": "convey resize rejected: CalledProcessError: exceeded quota", "pod": "default/web"}]
        p = gauges(lines).page()
        self.assertEqual(value(p, "omni_compass_decisions_total", '{zone="slack"}'), 1)
        self.assertEqual(value(p, "omni_compass_decisions_total", '{zone="band"}'), 3)
        self.assertEqual(value(p, "omni_compass_decisions_total", '{zone="wall"}'), 3)
        self.assertEqual(value(p, "omni_wall_recovery_seconds_count"), 2)        # two visits to the wall, each recovered
        self.assertAlmostEqual(value(p, "omni_wall_recovery_seconds_sum"), 120 + 60)
        self.assertAlmostEqual(value(p, "omni_wall_recovery_seconds_max"), 120)
        self.assertAlmostEqual(value(p, "omni_recommended_travel_total", '{setting="hpa_target"}'), 0.02 + 0.02 + 0.05)
        self.assertEqual(value(p, "omni_errors_total", '{kind="convey resize rejected"}'), 1)

    def test_a_broken_line_is_counted_never_fatal(self):
        p = gauges(["{not json", "[1, 2]", "", json.dumps(decision(1, 0.7))]).page()
        self.assertEqual(value(p, "omni_audit_unreadable_total"), 2)
        self.assertEqual(value(p, "omni_decisions_total"), 1)

    def test_every_sample_line_is_prometheus_text(self):
        line = re.compile(r'^[a-zA-Z_:][a-zA-Z0-9_:]*(\{([a-zA-Z_][a-zA-Z0-9_]*="([^"\\]|\\.)*",?)*\})? (NaN|[-+]?[0-9.eE+-]+)$')
        for ln in gauges(AUDIT).page().splitlines():
            if ln.startswith("# HELP ") or ln.startswith("# TYPE "):
                continue
            self.assertRegex(ln, line)
        # an unset gauge reads NaN, never a made-up zero
        self.assertIn("omni_own_cpu_cores NaN", EX.Gauges().page())

    def test_the_server_serves_metrics_only_and_follows_the_file(self):
        d = Path(tempfile.mkdtemp()); audit = d / "audit.jsonl"
        audit.write_text(json.dumps(decision(1, 0.7)) + "\n")
        g, stop = EX.Gauges(), threading.Event()
        threading.Thread(target=EX.follow, args=(audit, g, stop, 0.05), daemon=True).start()
        srv = EX.server(g, "127.0.0.1", 0)
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        base = f"http://127.0.0.1:{srv.server_address[1]}"
        try:
            with audit.open("a") as f:
                f.write(json.dumps(decision(61, 0.8)) + "\n")
            deadline = time.time() + 5
            while time.time() < deadline and value(g.page(), "omni_decisions_total") != 2:
                time.sleep(0.05)
            with urllib.request.urlopen(base + "/metrics", timeout=5) as r:
                self.assertTrue(r.headers["Content-Type"].startswith("text/plain; version=0.0.4"))
                self.assertEqual(value(r.read().decode(), "omni_decisions_total"), 2)
            with self.assertRaises(urllib.error.HTTPError) as e:
                urllib.request.urlopen(base + "/", timeout=5)
            self.assertEqual(e.exception.code, 404)
            req = urllib.request.Request(base + "/metrics", data=b"x", method="POST")
            with self.assertRaises(urllib.error.HTTPError) as e:
                urllib.request.urlopen(req, timeout=5)
            self.assertEqual(e.exception.code, 501)                  # no method but GET: nothing can be changed through it
        finally:
            stop.set(); srv.shutdown(); srv.server_close()

    def test_the_beat_is_measured_at_any_setting(self):
        """The heartbeat is a dial (omni-v17): the exporter serves the beat the governor runs at, the median spacing of its last
        eleven decisions, so a skipped slot or a slow decision moves it little, and nothing before two decisions."""
        one = value(gauges([{"time": 5.0, "decision_ms": 9.0}]).page(), "omni_heartbeat_seconds")
        self.assertTrue(one != one)                                                                # NaN: not yet measured
        for beat in (5.0, 15.0, 30.0, 60.0, 75.0, 90.0, 120.0):
            ts = [beat * k for k in range(12) if k != 7]                                         # one slot skipped
            p = gauges([{"time": t, "decision_ms": 40.0} for t in ts]).page()
            self.assertAlmostEqual(value(p, "omni_heartbeat_seconds"), beat)

    def test_the_grafana_screen_reads_only_what_the_exporter_serves(self):
        dash = json.loads((ROOT / "deploy" / "grafana" / "omni-compass.json").read_text(encoding="utf-8"))
        served = set(re.findall(r"^# TYPE (\S+)", gauges(AUDIT).page(), re.M))
        served |= {n + s for n in list(served) for s in ("_sum", "_count")}
        used = set()
        for p in dash["panels"]:
            for t in p["targets"]:
                used |= set(re.findall(r"\bomni_[a-z_]+", t["expr"]))
        self.assertTrue(used)
        self.assertEqual(used - served, set())
        self.assertIn("www.omni-compass.com", dash["description"])


if __name__ == "__main__":
    unittest.main()

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
