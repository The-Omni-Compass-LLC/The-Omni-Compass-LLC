# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The heartbeat dial's ladder (tools/beat_ladder.py, omni-v17): pace reports merged into one ladder only where what they share
reads the same seed by seed, every beat paired against its own report's 60 s and against native, the page written with the
notice."""
import copy, json, sys, tempfile, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
import tools.beat_ladder as BL
from tools.model_gate import PACE_GAUGES


def gauges(scale, cpu):
    """One seed's gauges: every modelled gauge scaled, the governor's processor timed apart."""
    g = {k: 10.0 * scale for k in PACE_GAUGES}
    g["governor_cpu_s_per_hour"] = cpu
    return g


def report(beats, cpu=1.0):
    """A pace report as tools/model_gate.py writes it, in both settings, seeds 1 to 3, read against 60 s."""
    models = {}
    for model, setting, _ in BL.SETTINGS:
        per = {"native": {s: {k: v for k, v in gauges(1.0, 0.0).items() if k not in ("governor_cpu_s_per_hour", "reads_per_hour")}
                          for s in ("1", "2", "3")}}
        for b in beats:
            per[b] = {s: gauges((60.0 / float(b)) * (1 + 0.01 * int(s)), cpu * 60.0 / float(b)) for s in ("1", "2", "3")}
        models[model] = {"setting": setting, "periods": [float(b) for b in beats], "reference": "60", "per_seed": per,
                     "counts": {"decisions": {b: int(86400 / float(b)) for b in beats}}}
    return {"seeds": [1, 2, 3], "days": 1.0, "models": models}


class Ladder(unittest.TestCase):
    def test_two_reports_make_one_ladder(self):
        lad = BL.ladder([report(["60", "15", "5"]), report(["60", "30", "120"], cpu=1.7)])
        t = lad["models"]["pace_cloud"]
        self.assertEqual(t["beats"], ["5", "15", "30", "60", "120"])
        self.assertEqual(t["report_of_beat"], {"5": 0, "15": 0, "30": 1, "60": 0, "120": 1})
        r = t["rows"]["30"]
        self.assertIsNone(t["rows"]["60"]["governor_cpu_s_per_hour"]["vs_main"])          # the main engine is the reference
        # the processor is paired inside its own report: 30 s against the second report's 60 s, not the first's
        self.assertAlmostEqual(r["governor_cpu_s_per_hour"]["main"], 1.7)
        self.assertAlmostEqual(r["governor_cpu_s_per_hour"]["vs_main"]["relative"], 1.0)
        self.assertIsNone(r["reads_per_hour"]["vs_native"])                                 # native has no governor to read with
        self.assertIn(r["pending_pod_minutes_per_hour"]["vs_native"]["word"], ("LOSS", "STEADY"))
        self.assertEqual(t["counts"]["decisions"]["120"], 720)

    def test_reports_that_disagree_are_refused(self):
        a, b = report(["60", "15"]), report(["60", "30"])
        bad = copy.deepcopy(b)
        bad["models"]["pace_kind"]["per_seed"]["60"]["2"]["alert_minutes"] += 1.0          # a modelled gauge differs: not one ladder
        with self.assertRaises(SystemExit):
            BL.ladder([a, bad])
        last_bits = copy.deepcopy(b)
        last_bits["models"]["pace_kind"]["per_seed"]["60"]["2"]["power_cap_travel"] *= 1 + 1e-15   # a float sum's last bits: one ladder
        self.assertEqual(BL.ladder([a, last_bits])["models"]["pace_kind"]["beats"], ["15", "30", "60"])
        bad = copy.deepcopy(b)
        bad["seeds"] = [1, 2]
        with self.assertRaises(SystemExit):
            BL.ladder([a, bad])

    def test_the_page_carries_the_notice_and_every_beat(self):
        with tempfile.TemporaryDirectory() as d:
            for i, beats in enumerate((["60", "15"], ["60", "90"])):
                (Path(d) / f"r{i}.json").write_text(json.dumps(report(beats)))
            out = Path(d) / "LADDER"
            BL.main([str(Path(d) / "r0.json"), str(Path(d) / "r1.json"), "--out", str(out), "--source-names", "a.json", "b.json"])
            md = out.with_suffix(".md").read_text()
            self.assertIn("All patents, copyrights and trademarks filed in the USA", md)
            self.assertIn("every 60 s (the main engine)", md)
            self.assertIn("### Every 90 s", md)
            self.assertIn("No outside party has reviewed or approved these results.", md)
            self.assertEqual(json.loads(out.with_suffix(".json").read_text())["sources"], ["a.json", "b.json"])

    def test_a_first_reading_is_kept_beside_the_corrected_beat(self):
        """A beat a fix changed is read from the corrected report, and its first reading stays on the page, from a report
        whose native and 60 s are the ladder's own."""
        with tempfile.TemporaryDirectory() as d:
            first = report(["60", "90"])
            first["models"]["pace_kind"]["per_seed"]["90"]["1"]["alert_minutes"] += 5.0
            for i, rep in enumerate((report(["60", "15"]), report(["60", "90"]), first)):
                (Path(d) / f"r{i}.json").write_text(json.dumps(rep))
            out = Path(d) / "LADDER"
            BL.main([str(Path(d) / "r0.json"), str(Path(d) / "r1.json"), "--out", str(out), "--first", str(Path(d) / "r2.json"),
                     "--first-beats", "90", "--first-name", "first.json", "--first-note", "Before the fix."])
            md = out.with_suffix(".md").read_text()
            self.assertIn("## The first reading of every 90 s, before the fix", md)
            self.assertIn("| every 90 s, first |", md)
            lad = json.loads(out.with_suffix(".json").read_text())
            self.assertNotEqual(lad["first"]["models"]["pace_kind"]["90"]["alert_minutes"]["value"],
                                lad["models"]["pace_kind"]["rows"]["90"]["alert_minutes"]["value"])
            bad = report(["60", "90"])
            bad["models"]["pace_cloud"]["per_seed"]["native"]["2"]["p95_ms"] += 1.0      # another plant: refused
            (Path(d) / "r3.json").write_text(json.dumps(bad))
            with self.assertRaises(SystemExit):
                BL.main([str(Path(d) / "r0.json"), "--out", str(out), "--first", str(Path(d) / "r3.json"), "--first-beats", "90"])


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
