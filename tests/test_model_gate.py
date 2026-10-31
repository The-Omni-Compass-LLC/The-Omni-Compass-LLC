# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The model gate (tools/model_gate.py) runs on this checkout: each model's workers run the shipped code against the model, write
every gauge, and the reading of a candidate against the standing engine follows the words rule (a resource spent that
rose is power given, never a LOSS; an interval across zero is STEADY)."""
import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import model_gate as tg  # noqa: E402


def captured(fn, *a):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn(*a)
    return json.loads(buf.getvalue().strip().splitlines()[-1])


class ModelGate(unittest.TestCase):
    def test_cluster_model_runs_both_arms(self):
        d = tempfile.mkdtemp()
        for arm in ("native", "omni"):
            r = captured(tg.worker, arm, 3, 0.1, 60.0, os.path.join(d, arm))
            for g in tg.GAUGES:
                self.assertIn(g, r)
            self.assertGreater(r["machine_hours"], 0.0)
        self.assertIn("steps_allowed", r)
        self.assertEqual(r["errors"], 0)

    def test_convey_model_runs_both_arms(self):
        d = tempfile.mkdtemp()
        nat = captured(tg.worker_convey, "native", 2, os.path.join(d, "n"))
        omni = captured(tg.worker_convey, "omni", 2, os.path.join(d, "o"))
        for g in tg.CONVEY_GAUGES:
            self.assertIn(g, nat); self.assertIn(g, omni)
        self.assertGreaterEqual(omni["limit_given_m"], nat["limit_given_m"])    # conveyance never lowers under native

    def test_convey_model_with_the_quota_unreadable_conveys_as_with_none(self):
        """The governor's role cannot list quotas (every kind test): no budget is known and conveyance is what it is with no
        quota at all. The first v7 trial (run 38825214203) read it as a zero budget and conveyed nothing; this model now catches that."""
        d = tempfile.mkdtemp()
        none = captured(tg.worker_convey, "omni", 2, os.path.join(d, "a"), "none")
        unread = captured(tg.worker_convey, "omni", 2, os.path.join(d, "b"), "unreadable")
        self.assertEqual(unread["limit_given_m"], none["limit_given_m"])
        self.assertEqual(unread["requests_served"], none["requests_served"])
        nat = captured(tg.worker_convey, "native", 2, os.path.join(d, "n"))
        self.assertGreater(unread["limit_given_m"], nat["limit_given_m"])        # something was conveyed

    def test_reading_follows_the_words_rule(self):
        self.assertEqual(tg.reading("machine_hours", [1.0, 1.1, 0.9, 1.2], [10.0] * 4)["word"], "power given")
        self.assertEqual(tg.reading("p95_ms", [1.0, 1.1, 0.9, 1.2], [10.0] * 4)["word"], "LOSS")
        self.assertEqual(tg.reading("p95_ms", [-1.0, -1.1, -0.9, -1.2], [10.0] * 4)["word"], "GAIN")
        # the founder's order of 24 October 2026: a mean change of 0.5% or more is a change, read by the aim, with whether it
        # stands beyond the seeds' noise beside it; STEADY only under 0.5%
        swing = tg.reading("p95_ms", [-1.0, 1.1, -0.9, 1.2], [10.0] * 4)
        self.assertEqual((swing["word"], swing["beyond_noise"]), ("LOSS", False))
        self.assertEqual(tg.reading("p95_ms", [-0.05, 0.06, -0.04, 0.05], [10.0] * 4)["word"], "STEADY")
        self.assertEqual(tg.reading("requests_served", [1.0, 1.1, 0.9, 1.2], [10.0] * 4, tg.CONVEY_GAUGES)["word"], "GAIN")


if __name__ == "__main__":
    unittest.main()
