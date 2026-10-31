# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The grid's one page (tools/grid_v5.py): every square from the pooled receipts, nothing recomputed, a missing square
said, and the runs each half was pooled from named."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import grid_v5  # noqa: E402


def square(m, label="FEWER MISSES", runs=10):
    return {"runs": runs, "of": runs, "label": label, "band_first": "held", "viol_pp": [m, m - 0.01, m + 0.01],
            "work": [0.0, 0.0, 0.0], "energy": [0.0005, 0.0004, 0.0006], "primary": [0, 0, 0]}


class Grid(unittest.TestCase):
    def test_every_square_from_the_receipts(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            m = t / "run-111" / "six-pooled-v5-x10"; m.mkdir(parents=True)
            summary = {n: {o: square(-0.1, runs=int(n)) for o in grid_v5.ORGS} for n in grid_v5.RUNS}
            del summary["100"]["tower"]                                         # a square the receipt lacks
            (m / "SIX_v5-x10.json").write_text(json.dumps({"scale": 10, "summary": summary}))
            k = t / "run-222" / "six-kube-pooled-v5-x10"; k.mkdir(parents=True)
            row = lambda diff, lo, hi, **kw: {"n": 10, "native": 100.0, "omni": 100.0 + diff, "diff": diff, "lo": lo, "hi": hi,
                                              "pct": diff, "better": diff < 0, "neutral": False, "same": False, **kw}
            p95, fail, energy = "response time (ms), 95th percentile", "failed requests (%)", "organism energy (J)"
            host, cpu = "host CPU busy, the real machine under kind (%)", "CPU used with Omni's own (cores), mean"
            (k / "SIX_KUBE_v5-x10_r10.json").write_text(json.dumps({"organisms": {
                # the recorded verdicts carry the old words: the page reads the rows, never those words, and keeps the facts
                "stack@10": {"arm": "compass", "repetitions": 10, "verdict": "better on 1, worse on 0, inside the noise on 1",
                             "rows": {p95: row(-30, -40, -20), fail: row(1, -2, 4), host: row(1, 0.5, 1.5, neutral=True),
                                      cpu: row(-1.2, -2, -0.4, neutral=True)}},
                "tower@10": {"arm": "compass", "repetitions": 10, "verdict": "better on 1, worse on 1 (organism energy (J)), inside "
                             "the noise on 0; OFF THE CLOCK in 2 of 10 repetitions (late)",
                             "rows": {p95: row(-10, -15, -5), energy: row(0.05, 0.04, 0.06), host: row(2, 1, 3, neutral=True),
                                      cpu: row(-2.0, -3, -1, neutral=True)}}}}))
            out = t / "GRID.md"
            self.assertEqual(grid_v5.main(["--modelled", str(t / "run-111"), "--kube", str(t / "run-222"), "--out", str(out)]), 0)
            text = out.read_text()
            self.assertIn("10 copies: run 111", text)
            self.assertIn("10 copies: run 222", text)
            self.assertIn("GAIN (fewer misses): misses -0.100 pp, work +0.000%, power given +0.050% (10 of 10 runs)", text)
            self.assertIn("not in the receipt", text)                            # the tower at 100 runs
            self.assertIn("| 10 repetitions: GAIN on 1 (response time (ms), 95th percentile), LOSS on 0, power given on 0, STEADY (inside the noise) on 1 |", text)
            self.assertIn("10 repetitions: GAIN on 1 (response time (ms), 95th percentile), LOSS on 0, power given on 1 (organism energy (J)), "
                          "STEADY (inside the noise) on 0; OFF THE CLOCK in 2 of 10 repetitions (late) |", text)
            self.assertIn("not in the report", text)
            # the one line the front page reads, counted from the squares (27 modelled with the spine: 20 of 10, 100 and 500 runs, 7 single)
            self.assertIn("**Across the grid: modelled, 20 of 20 squares of 10 or more runs GAIN (fewer misses); the 7 single runs: "
                          "7 with fewer misses; work +0.000%; power given +0.050%; with the cluster "
                          "inside, 2 squares: 0 single repetitions (no reading); of the 2 of 10 or more repetitions, by gauge: "
                          "\"response time (ms), 95th percentile\" GAIN in 2, LOSS in 0, \"organism energy (J)\" GAIN in 0, "
                          "power given in 1; off the clock in 1; invalid in 0.**", text)
            # the test machine at each size, from native's own rows (the shown-only gauges)
            self.assertIn("### The test machine at each size", text)
            self.assertIn("| 10 copies (10 repetitions) | 100% | 100% | -2.0 to -1.2% | The whole tower 2 of 10 |", text)
            # the page never says better or worse, nor lower or higher as a reading, whatever words the recorded verdicts carry
            self.assertNotIn("better", text.lower())
            self.assertNotIn("worse", text.lower())
            self.assertNotIn("lower on", text)
            self.assertNotIn("higher on", text)
            self.assertIn("No outside party has reviewed or approved these results.", text)
            # every receipt's page linked from the grid page's own folder (a relative link resolves from the page)
            self.assertIn("](run-111/six-pooled-v5-x10/SIX_v5-x10.md)", text)
            self.assertIn("](run-222/six-kube-pooled-v5-x10/SIX_KUBE_v5-x10_r10.md)", text)
            data = json.loads(out.with_suffix(".json").read_text())
            self.assertIsNone(data["modelled"]["tower@10"]["100"])
            self.assertEqual(data["kube"]["stack@10"]["10"]["repetitions"], 10)


if __name__ == "__main__":
    unittest.main()
