# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The four ways (docs/BATCH_QUEUE_PREREGISTRATION.md, amendment 6; the founder's order of 20 October): the organism alone,
the orchestrator on it as shipped, Omni-Compass on the organism alone and Omni-Compass on top of the orchestrator, all four
in every repetition. The aggregator pairs each comparison within the repetition; the three-run tool reads any one of them;
the paired runner runs an arm named ...bare on the organism alone; and on the batch rig the governor has its own core
(amendment 5), the kind nodes the others, in every arm."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
import tools.live_reps as LR
import tools.confirm_abc as CA

WAIT = "queue: job wait, submitted to its first pod running, mean (s)"
NODES = "worker nodes in service, mean"
G = {"nativebare": (40.0, 6.0), "native": (30.0, 6.0), "compassbare": (36.0, 4.5), "compass": (27.0, 4.2)}


def standin(d):
    arm, rep = d.name.split("-")[1], int(d.name.split("-")[2])
    wait, nodes = G[arm]
    g = {k: 0.0 for k in LR.KEYS}
    g.update({WAIT: wait + 0.1 * rep * (1 + (arm == "native")), NODES: nodes + 0.01 * rep})
    return g


class FourWays(unittest.TestCase):
    def test_every_comparison_is_paired_within_the_repetition(self):
        t = Path(tempfile.mkdtemp())
        for arm in G:
            for r in (1, 2, 3):
                d = t / f"bench-{arm}-{r}"; d.mkdir(); (d / "capture.csv").write_text("x\n")
        old = LR.arm_gauges
        try:
            LR.arm_gauges = standin
            LR.main(str(t))
        finally:
            LR.arm_gauges = old
        out = json.loads((t / "LIVE_REPS.json").read_text())
        for key in ("compass", "native|nativebare", "compassbare|nativebare", "compassbare|native", "compass|nativebare"):
            self.assertIn(key, out["paired"])
        self.assertAlmostEqual(out["paired"]["native|nativebare"][WAIT]["diff"], -10.0 + 0.2, places=6)   # the orchestrator's own effect
        self.assertAlmostEqual(out["paired"]["compassbare|native"][NODES]["diff"], -1.5, places=6)        # Omni alone against it
        md = (t / "LIVE_REPS.md").read_text()
        self.assertIn("the orchestrator as shipped vs the organism alone", md)
        self.assertIn("| Gauge | the organism alone (no orchestrator) | native |", md)

    def test_the_three_run_tool_reads_one_comparison(self):
        t = Path(tempfile.mkdtemp())
        j = {"repetitions": {"native": [1, 2], "nativebare": [1, 2]},
             "paired": {"compass": {}, "native|nativebare": {WAIT: {"native": 40.0, "omni": 30.0, "diff": -10.0, "ci95": [-11, -9]}}}}
        d = t / "run-123"; d.mkdir(); (d / "LIVE_REPS.json").write_text(json.dumps(j))
        old = CA.PAIR
        try:
            CA.PAIR = "native|nativebare"
            run, paired, n, _ = CA.load(d)
        finally:
            CA.PAIR = old
        self.assertEqual((run, n), ("123", 2))
        self.assertEqual(paired[WAIT]["diff"], -10.0)

    def test_the_runner_runs_a_bare_arm_on_the_organism_alone(self):
        text = (ROOT / "scripts" / "kind_paired.sh").read_text()
        self.assertIn('ARM="$base" BATCH_QUEUE="$queue" ADDONS="$addons" CRUISEKUBE="$cruise" OUT_DIR="bench-$arm-$REP"', text)
        start = text.index('  base="${arm%bare}"')
        split = text[start:text.index("\n", text.index('  if [ "$base" != "$arm" ]', start))]   # the runner's own two lines

        def arms(**env):
            r = subprocess.run(["bash", "-c", "for arm in native nativebare compass compassbare; do\n" + split
                                + '\necho "$arm $base ${queue:--} ${addons:--}"; done'],
                               env={"PATH": "/usr/bin:/bin", **env}, capture_output=True, text=True, check=True)
            return r.stdout.split("\n")[:4]
        # the batch rig: the bare arms' stream placed by the default scheduler
        self.assertEqual(arms(BATCH_QUEUE="kai"), ["native native kai -", "nativebare native vanilla -",
                                                   "compass compass kai -", "compassbare compass vanilla -"])
        # the serving rig with an add-on (Crane): the bare arms carry no add-on and start no stream
        self.assertEqual(arms(ADDONS="crane"), ["native native - crane", "nativebare native - -",
                                                "compass compass - crane", "compassbare compass - -"])

    def test_the_governor_has_its_own_core_on_the_batch_rig(self):
        text = (ROOT / "scripts" / "kind_bench.sh").read_text()
        self.assertIn('docker update --cpuset-cpus "$cluster_cpus" "$node"', text)
        self.assertIn('GOV_PIN="taskset -c $gov_cpu"', text)
        self.assertIn('$GOV_PIN nice -n "$OMNI_NICE" python -m omni_controller.controller', text)
        self.assertLess(text.index('GOV_PIN=""'), text.index("kubectl apply -f deploy/kind/bench-serving.yaml"))


if __name__ == "__main__":
    unittest.main()

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
