# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The orchestrators on the same organisms (tools/orchestrators_arm.py, docs/ORCHESTRATORS_PREREGISTRATION.md): the injection is
the same in every arm, each orchestrator's rule places as its release writes it, and the page is what its record gives."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import tools.orchestrators_arm as A  # noqa: E402


def organism(orch, setting="cloud", name="steady"):
    org = A.Organism(name, setting, orch, A.injection(name, setting, 0, 20261025))
    return org


class TheInjection(unittest.TestCase):
    def test_every_arm_of_a_repetition_meets_the_same_numbers(self):
        a = A.injection("one_body", "cloud", 3, 20261025)
        b = A.injection("one_body", "cloud", 3, 20261025)
        self.assertEqual(a, b)
        self.assertNotEqual(a["work"], A.injection("one_body", "cloud", 4, 20261025)["work"])

    def test_the_seed_is_the_jump_generator_of_the_engine_runs(self):
        self.assertEqual(A.seed_of(20261025, 0), 20261025)
        self.assertEqual(A.seed_of(20261025, 1), (20261025 + 0x9E3779B9) & 0xFFFFFFFF)

    def test_a_native_run_and_the_default_orchestrator_are_one_arm(self):
        self.assertEqual(A.run_one("steady", "cloud", "default", "native", 0),
                         A.run_one("steady", "cloud", "binpack", "native", 0))   # native ignores the orchestrator named


class TheRules(unittest.TestCase):
    def setUp(self):
        self.pod = {"name": "p", "kind": "svc", "owner": "x", "req": 200, "qos": "LS", "node": None}

    def two_machines(self, orch):
        org = organism(orch)
        org.nodes = [org._node(0), org._node(1)]
        org.pods = [{"name": "q", "kind": "batch", "owner": "b", "req": 1000, "qos": "LS", "node": "w0", "use": 0.0}]
        return org

    def test_the_default_scheduler_spreads_to_the_emptier_machine(self):
        org = self.two_machines("default")
        self.assertEqual(org.score(self.pod, org.feasible(self.pod, "default"), "default")["name"], "w1")

    def test_the_bin_packing_profile_and_kai_pack_onto_the_fuller_machine(self):
        for orch in ("binpack", "kai"):
            org = self.two_machines(orch)
            self.assertEqual(org.score(self.pod, org.feasible(self.pod, orch), orch)["name"], "w0", orch)

    def test_volcano_scores_tie_on_the_processor_and_avoids_an_idled_machine(self):
        org = self.two_machines("volcano")
        org.nodes[1]["idle"] = True
        self.assertEqual(org.score(self.pod, org.feasible(self.pod, "volcano"), "volcano")["name"], "w0")

    def test_kueue_admits_a_job_whole_within_its_quota(self):
        org = organism("kueue", name="batch")
        org.quota = 2500                                           # room for one job of 5 x 500m and nothing more
        org.jobs = [{"name": "job-0", "born": 0, "left": 10, "running": 0, "done_at": None, "admitted": False, "k": 0},
                    {"name": "job-1", "born": 1, "left": 10, "running": 0, "done_at": None, "admitted": False, "k": 1}]
        org.pods = []
        org.admit_kueue()
        self.assertEqual([j["admitted"] for j in org.jobs], [True, False])

    def test_koordinator_places_best_effort_pods_on_batch_resources_only(self):
        org = organism("koordinator", name="batch")
        org.nodes = [org._node(0)]
        org.batch_alloc = {"w0": 400.0}                            # less than one batch pod's 500
        be = {"name": "b", "kind": "batch", "owner": "s", "req": 500, "qos": "BE", "node": None}
        self.assertEqual(org.feasible(be, "koordinator"), [])
        org.batch_alloc = {"w0": 1200.0}
        self.assertEqual([n["name"] for n in org.feasible(be, "koordinator")], ["w0"])


class TheRecord(unittest.TestCase):
    def test_the_page_is_what_the_record_gives(self):
        if not (ROOT / "results" / "orchestrators" / "ORCHESTRATORS.json").exists():
            self.skipTest("no record yet")
        from tools.orchestrators_report import main
        self.assertEqual(main(["--check"]), 0)


if __name__ == "__main__":
    unittest.main()

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
