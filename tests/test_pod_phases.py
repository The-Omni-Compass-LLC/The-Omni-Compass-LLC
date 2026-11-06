# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Where a pod's start wait goes (tools/pod_phases.py, docs/POD_START_WAIT.md): every serving pod started inside a measured
window is split from Kubernetes' own timestamps into scheduling, the node side and the app with its probe, placed by the
host's busy share and by whether its node already served, and the change in the mean wait between the arms is split
exactly in two: the shift of starts into busier bands and the wait at the same busy share."""
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock

from tools import pod_phases as P

T0 = 1_760_000_000


def iso(t):
    return datetime.fromtimestamp(t, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def pod(uid, node, created, running, ready):
    return {"type": "MODIFIED", "object": {
        "metadata": {"uid": uid, "creationTimestamp": iso(created)}, "spec": {"nodeName": node},
        "status": {"conditions": [{"type": "PodScheduled", "status": "True", "lastTransitionTime": iso(created)},
                                  {"type": "Ready", "status": "True", "lastTransitionTime": iso(ready)}],
                   "containerStatuses": [{"state": {"running": {"startedAt": iso(running)}}}]}}}


def arm(root, name, pods, busy):
    d = root / name
    d.mkdir(parents=True)
    (d / "window_start.txt").write_text(f"{T0}\n")
    (d / "window_end.txt").write_text(f"{T0 + 900}\n")
    (d / "pod_watch.json").write_text("\n".join(json.dumps(p) for p in pods) + "\n")
    (d / "host_cpu.csv").write_text("t,busy\n" + "".join(f"{T0 + s},{busy(s)}\n" for s in range(0, 901, 2)))


class PodPhases(unittest.TestCase):
    def test_the_change_splits_exactly_into_the_shift_and_the_wait_in_the_same_stratum(self):
        with tempfile.TemporaryDirectory() as t, mock.patch.object(P, "RAW", Path(t)):
            run = Path(t) / "addons-run-9" / "http"
            # native: two starts on empty nodes while the host is 30 % busy, 8 s each
            arm(run, "bench-native-1", [pod("n1", "w1", T0 + 100, T0 + 107, T0 + 108),
                                        pod("n2", "w2", T0 + 300, T0 + 307, T0 + 308)], lambda s: 0.3)
            # omni: one start at 30 % busy (8 s), one on an empty node at 80 % busy (12 s), one beside a pod already serving
            arm(run, "bench-compass-1", [pod("c1", "w1", T0 + 100, T0 + 107, T0 + 108),
                                         pod("c2", "w2", T0 + 500, T0 + 511, T0 + 512),
                                         pod("c3", "w1", T0 + 200, T0 + 201, T0 + 201)],
                lambda s: 0.8 if 480 <= s <= 530 else 0.3)
            rows = P.starts("addons-run-9")
            self.assertEqual(len(rows), 5)
            self.assertEqual({r[1] for r in rows}, {"http"})
            c2 = next(r for r in rows if r[0] == "compass" and r[2] == 12)
            self.assertEqual((c2[3], c2[4], c2[5], c2[7]), (0, 11, 1, False))      # scheduling, node side, app and probe, empty node
            self.assertTrue(next(r for r in rows if r[0] == "compass" and r[2] == 1)[7], "c3's node already carried a Ready pod")
            empty = [r for r in rows if not r[7]]
            dw, shift, same, mean = P.decompose(empty)
            self.assertAlmostEqual(dw, 2.0)                 # omni 10 s against native 8 s
            self.assertAlmostEqual(shift, 2.0)              # all of it the shift into the busier band
            self.assertAlmostEqual(same, 0.0)               # in the same stratum, the same wait
            self.assertAlmostEqual(dw, shift + same)
            out = Path(t) / "out.md"
            self.assertEqual(P.main(["addons-run-9", "--engine", "addons-run-9=omni-v11", "--out", str(out)]), 0)
            text = out.read_text()
            self.assertIn("omni-v11, test http", text)
            self.assertIn("| omni | 0.7 to 1.0 | empty | 1 | 12.00 |", text)


if __name__ == "__main__":
    unittest.main()
