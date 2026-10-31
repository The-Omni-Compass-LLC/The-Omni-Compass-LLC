# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The capacity test's table (tools/capacity_report.py): arms paired within one job, completed work and capacity read
from the work meter's counts, each row's reading and audit line, and the row that shows speed and not more work."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import capacity_report as cr  # noqa: E402

RATES = [10.0, 20.0, 40.0, 60.0]


def arm(root, cap, rep, name, served, slo=500.0, invalid=False):
    """A repetition's arm: served[i] is the share of step i answered within the line (the rest late)."""
    d = Path(root) / f"cap-{cap}-{rep}" / f"bench-{name}-{rep}"
    d.mkdir(parents=True)
    steps, tot = [], dict.fromkeys(("sent", "in_time", "late", "failed", "not_sent"), 0)
    for rate, sh in zip(RATES, served):
        sent = int(rate * 100)
        s = {"sent": sent, "in_time": int(sent * sh), "late": sent - int(sent * sh), "failed": 0, "not_sent": 0}
        steps.append(s)
        for k in tot:
            tot[k] += s[k]
    (d / "work_meter.json").write_text(json.dumps({"final": True, "total": tot, "steps": steps, "rate_steps": RATES,
                                                   "slo_ms": slo}) + "\n")
    (d / "preflight.txt").write_text(f"arm={name}\ncap_cpu_m={cap} (a quota)\n")
    (d / "latency.csv").write_text("elapsed_seconds,latency_ms,ok\n" + "".join(f"{i},{100 + i},1\n" for i in range(20)))
    if invalid:
        (d / "INVALID").write_text("ARM failed its checks")
    return d


class CapacityReport(unittest.TestCase):
    def test_rows_readings_and_audit_lines(self):
        with tempfile.TemporaryDirectory() as t:
            for rep, bump in ((1, 0.02), (2, 0.03), (3, 0.025)):
                # 1 core: native serves the first two steps, Omni on top three, and more of the rest
                arm(t, 1000, rep, "native", [1.0, 0.97, 0.5, 0.3])
                arm(t, 1000, rep, "compass", [1.0, 0.99, 0.96, 0.3 + bump])
                # 4 cores: the cap is never reached, both serve everything
                arm(t, 4000, rep, "native", [1.0, 1.0, 1.0, 1.0])
                arm(t, 4000, rep, "compass", [1.0, 1.0, 1.0, 1.0])
            arm(t, 1000, 4, "native", [1.0, 1.0, 1.0, 1.0], invalid=True)     # left out, and listed
            out = Path(t) / "CAPACITY.md"
            cr.main([t, "--out", str(out)])
            d = json.loads(out.with_suffix(".json").read_text())
            one, four = d["rows"]
            self.assertEqual((one["cap_m"], one["pairs"], four["cap_m"]), (1000, 3, 4000))
            self.assertEqual(one["work_reading"], "GAIN")
            self.assertEqual((one["capacity_native"], one["capacity_omni"]), (20.0, 40.0))
            self.assertIn("more work from the same cap", one["audit"])
            self.assertIn("never reached", four["audit"])
            self.assertIn("not more work", four["audit"])
            self.assertEqual(four["work_reading"], "one pair (no reading)" if four["pairs"] < 2 else "STEADY, no difference beyond the noise")
            self.assertTrue(any("INVALID" in x or "failed its checks" in x for x in d["left_out"]))
            text = out.read_text()
            self.assertIn("No outside party has reviewed or approved these results.", text)
            self.assertIn("www.omni-compass.com", text)

    def test_capacity_stops_at_the_first_broken_step(self):
        rec = {"rates": RATES, "steps": [{"sent": 100, "in_time": 99, "late": 1, "failed": 0, "not_sent": 0},
                                         {"sent": 100, "in_time": 90, "late": 10, "failed": 0, "not_sent": 0},
                                         {"sent": 100, "in_time": 99, "late": 1, "failed": 0, "not_sent": 0},
                                         {"sent": 100, "in_time": 50, "late": 0, "failed": 50, "not_sent": 0}]}
        self.assertEqual(cr.capacity(rec), 10.0)       # the second step broke the latency limit: the third does not count
        rec["steps"][1] = {"sent": 100, "in_time": 97, "late": 1, "failed": 2, "not_sent": 0}
        self.assertEqual(cr.capacity(rec), 10.0)       # 2% failed breaks the failure limit (1%)


class CapacityThreeRuns(unittest.TestCase):
    """tools/capacity_abc.py: three runs' tables read row by row with the three readings every three-run table uses."""

    @staticmethod
    def run_dir(root, run_id, label, work, capacity):
        """One archived run: work[cap] and capacity[cap] are (difference, low, high) of omni against native."""
        d = Path(root) / f"capacity-run-{run_id}"
        d.mkdir(parents=True)
        rows = [{"cap_m": cap, "pairs": 5, "work_native": 1000.0, "work_omni": 1000.0 + w[0], "work_diff": w[0],
                 "work_lo": w[1], "work_hi": w[2], "capacity_native": 10.0, "capacity_omni": 10.0 + capacity[cap][0],
                 "capacity_diff": capacity[cap][0], "capacity_lo": capacity[cap][1], "capacity_hi": capacity[cap][2]}
                for cap, w in work.items()]
        (d / "CAPACITY.json").write_text(json.dumps({"rows": rows}))
        (d / "RUN.txt").write_text(f"label={label}\ncommit=0000000\n")
        return d

    def test_readings_by_cap(self):
        from tools import capacity_abc as ca
        with tempfile.TemporaryDirectory() as t:
            runs = []
            for i, (lab, w2) in enumerate((("A", (-24, -92, 44)), ("B", (-18, -34, -1)), ("C", (19, -22, 59)))):
                runs.append(self.run_dir(t, 100 + i, lab,
                                         {1000: (50, 10, 90), 2000: w2},             # 1 core: more work in all three
                                         {1000: (1.0, 0.5, 1.5), 2000: (0.0, 0.0, 0.0)}))
            out = Path(t) / "V5_CAPACITY.md"
            ca.main([str(r) for r in runs] + ["--out", str(out)])
            rows = json.loads(out.with_suffix(".json").read_text())["rows"]
            self.assertEqual(rows["1000:work"]["reading"], "GAIN in all three of our runs")
            self.assertEqual(rows["1000:capacity"]["reading"], "GAIN in all three of our runs")
            # two runs down and one up, each by 0.5% or more: the runs disagree (the founder's order of 24 October 2026)
            self.assertEqual(rows["2000:work"]["reading"], "the runs disagree")
            self.assertEqual(rows["2000:capacity"]["reading"], "STEADY, the same")
            text = out.read_text()
            self.assertIn("No outside party has reviewed or approved these results.", text)
            self.assertIn("www.omni-compass.com", text)


if __name__ == "__main__":
    unittest.main()
