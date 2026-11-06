# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The organisms with the cluster inside (tools/run_kil.py): the same demand in both arms, the load across the whole
declared range, every simulated knob handed back in the Omni arm, and the report's twelve columns."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import run_kil
from tools.run_hil import NAMES


class SixKube(unittest.TestCase):
    def test_arms_share_demand_and_hand_back(self):
        with tempfile.TemporaryDirectory() as t:
            recs = {}
            for arm in ("native", "compass"):
                d = Path(t) / arm
                self.assertEqual(run_kil.main(["--organism", "compute_ai_cloud", "--arm", arm, "--duration", "0.5",
                                               "--out", str(d), "--dry", "--load-max", "6"]), 0)
                recs[arm] = json.loads((d / "organism.json").read_text())
            self.assertEqual(recs["native"]["demand"], recs["compass"]["demand"])
            self.assertEqual(recs["native"]["replicas"], recs["compass"]["replicas"])
            self.assertEqual((min(recs["compass"]["replicas"]), max(recs["compass"]["replicas"])), (1, 6))
            self.assertEqual(recs["native"]["sim_writes"], 0)
            self.assertGreater(recs["compass"]["sim_writes"], 0)
            self.assertTrue(recs["compass"]["sim_restore_ok"])
            log = (Path(t) / "compass" / "load_schedule.log").read_text()
            self.assertIn("load-generator replicas -> ", log)

    def test_seven_organisms_named(self):
        self.assertEqual(len(NAMES), 7)
        self.assertIn("spine", NAMES)
        self.assertEqual(sorted(run_kil.groups(1)), sorted(NAMES))
        from tools import six_kube_report             # the report orders every organism a run can carry (the spine's
        self.assertEqual(sorted(six_kube_report.ORDER), sorted(NAMES))   # reports crashed on 17 October without it)
        self.assertEqual(six_kube_report.ORDER[0], "spine")

    def test_gzipped_record_reads_the_same(self):
        """The archive stores a raw file over 50 MB gzipped (GitHub refuses a file over 100 MB); the report reads it
        exactly as the plain file."""
        import gzip
        from tools import six_kube_report
        with tempfile.TemporaryDirectory() as t:
            d = Path(t) / "bench-compass-1"
            self.assertEqual(run_kil.main(["--organism", "compute_ai_cloud", "--arm", "compass", "--duration", "0.5",
                                           "--out", str(d), "--dry", "--load-max", "6"]), 0)
            plain = six_kube_report.organism_record(d)
            raw = (d / "organism.json").read_bytes()
            (d / "organism.json.gz").write_bytes(gzip.compress(raw, mtime=0)); (d / "organism.json").unlink()
            self.assertEqual(six_kube_report.organism_record(d), plain)
            self.assertEqual(gzip.decompress((d / "organism.json.gz").read_bytes()), raw)
            (d / "organism.json.gz").unlink()
            self.assertIsNone(six_kube_report.organism_record(d))

    def test_repetition_paired_within_one_run(self):
        """A repetition started again after a failed job is paired within one run: the latest run where native and Omni
        are both valid, never native from one run and Omni from another."""
        from tools import six_kube_report as r
        saved = r.arm_gauges, r.organism_record, r.organism_gauges
        try:
            r.organism_record = lambda d: {"organism": "stack", "scale": 1, "src": d.parent.parent.name}
            r.organism_gauges = lambda rec: {"src": rec["src"]}
            r.arm_gauges = lambda d: {}
            with tempfile.TemporaryDirectory() as t:
                def arm(run, arm, rep, invalid=False):
                    d = Path(t) / run / f"six-stack-x1-{rep}" / f"bench-{arm}-{rep}"
                    d.mkdir(parents=True); (d / "capture.csv").write_text("")
                    if invalid:
                        (d / "INVALID").write_text("x")
                arm("run-1", "native", 7); arm("run-1", "compass", 7, invalid=True)    # the first try: Omni's arm failed
                arm("run-2", "native", 7); arm("run-2", "compass", 7)                  # the second: both valid
                arm("run-3", "native", 7); arm("run-3", "compass", 7, invalid=True)    # a third, failed again
                arm("run-1", "native", 8); arm("run-1", "compass", 8)
                runs = r.collect(t)
                self.assertEqual((runs["stack"]["native"]["7"]["src"], runs["stack"]["compass"]["7"]["src"]), ("run-2", "run-2"))
                self.assertEqual((runs["stack"]["native"]["8"]["src"], runs["stack"]["compass"]["8"]["src"]), ("run-1", "run-1"))
        finally:
            r.arm_gauges, r.organism_record, r.organism_gauges = saved

    def test_first_n_repetitions(self):
        """The grid's nested squares: --reps N keeps the first N repetitions of every organism, nothing past them."""
        import json as _json
        from tools import six_kube_report as r
        saved = r.arm_gauges, r.organism_record, r.organism_gauges
        try:
            r.organism_record = lambda d: {"organism": "stack", "scale": 1}
            r.organism_gauges = lambda rec: {}
            r.arm_gauges = lambda d: {"response time (ms), 95th percentile": 100.0 + int(d.name.rsplit("-", 1)[1]) * (d.name.startswith("bench-native") or -1)}
            with tempfile.TemporaryDirectory() as t:
                for rep in (1, 2, 3):
                    for arm in ("native", "compass"):
                        d = Path(t) / "run-9" / f"six-stack-x1-{rep}" / f"bench-{arm}-{rep}"
                        d.mkdir(parents=True); (d / "capture.csv").write_text("")
                counts = {}
                for n in (1, 2, None):
                    out = Path(t) / f"r{n}.md"
                    r.main(t, out=str(out), reps=n)
                    counts[n] = _json.loads(out.with_suffix(".json").read_text())["organisms"]["stack"]["repetitions"]
                    if n:
                        self.assertIn(f"its first {n} repetition", out.read_text())
                self.assertEqual(counts, {1: 1, 2: 2, None: 3})
        finally:
            r.arm_gauges, r.organism_record, r.organism_gauges = saved


if __name__ == "__main__":
    unittest.main()
