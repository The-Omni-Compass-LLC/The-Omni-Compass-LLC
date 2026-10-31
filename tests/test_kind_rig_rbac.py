# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The kind rig's identity for Omni-Compass grants every muscle the engine carries its own write, and nothing more.

The pod muscle of its own (--own-replicas, omni-v19) writes the named workload's scale subresource: `kubectl scale` patches
`deployments/scale`, which under RBAC is a resource of its own that a grant on `deployments` does not carry. Every solo arm
run on kind from 24 to 31 October had that write refused, 15 of 15 decisions a window, while the preflight proved only
`patch deployment/php-apache` and passed (docs/SOLO_PREREGISTRATION.md, amendment 1). The same amendment moved the solo
arm's end-of-window record from the pod autoscaler, which the arm removes by design, to the workload's own object: the
autoscaler's read ended every solo arm of the omni-v22 campaign's first two runs with exit 1 and no words.
"""
import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def rules(path, kind, name):
    docs = [d for d in yaml.safe_load_all((ROOT / path).read_text(encoding="utf-8"))
            if d and d.get("kind") == kind and d.get("metadata", {}).get("name") == name]
    assert len(docs) == 1, (path, kind, name, len(docs))
    return docs[0]["rules"]


class KindRigRbac(unittest.TestCase):
    def test_the_named_workloads_scale_is_granted_and_nothing_is_deleted(self):
        app = rules("deploy/kind/rbac-omni.yaml", "Role", "omni-compass-app")
        scale = [r for r in app if "deployments/scale" in r.get("resources", [])]
        self.assertEqual(len(scale), 1, "the pod muscle of its own needs the scale subresource, once, by name")
        self.assertEqual(scale[0]["apiGroups"], ["apps"])
        self.assertEqual(scale[0]["resourceNames"], ["php-apache"])
        self.assertEqual(sorted(scale[0]["verbs"]), ["get", "patch", "update"])
        own = rules("deploy/rbac-own-pods.yaml", "Role", "omni-compass-own-pods")
        self.assertEqual([r["resources"] for r in own], [["deployments/scale"]])
        self.assertEqual(own[0]["resourceNames"], ["php-apache"])
        for path in ("deploy/kind/rbac-omni.yaml", "deploy/rbac-own-pods.yaml"):
            for d in yaml.safe_load_all((ROOT / path).read_text(encoding="utf-8")):
                for r in (d or {}).get("rules", []):
                    self.assertNotIn("delete", r["verbs"], (path, r))
                    self.assertNotIn("*", r["verbs"], (path, r))

    def test_the_preflight_proves_the_scale_write_by_name_both_ways(self):
        rig = (ROOT / "scripts/kind_bench.sh").read_text(encoding="utf-8")
        self.assertEqual(rig.count('echo "== cannot"'), 1)
        can, cannot = rig.split('echo "== cannot"', 1)
        self.assertIn("$(can patch deployment/php-apache --subresource=scale -n default)", can)
        self.assertIn("$(can patch deployment/load-generator --subresource=scale -n default)", cannot)

    def test_the_solo_arms_end_record_is_the_workloads_own(self):
        rig = (ROOT / "scripts/kind_bench.sh").read_text(encoding="utf-8")
        self.assertIn('if [ "$ARM" = "solo" ]; then end_read "$OUT_DIR/workload_end.json" get deployment php-apache -o json', rig)
        # the autoscaler's end read is never unconditional: by itself there is no autoscaler to read
        self.assertIsNone(re.search(r'^\s*end_read "\$OUT_DIR/hpa_end\.json"', rig, re.M))

    def test_by_itself_a_failed_decision_refuses_the_window(self):
        # the founder's order of 31 October (docs/SOLO_PREREGISTRATION.md, amendment 2): by itself a knob Omni-Compass owns has
        # no other controller, so a window in which one of its decisions failed left a knob with no controller and is refused
        rig = (ROOT / "scripts/kind_bench.sh").read_text(encoding="utf-8")
        i = rig.find('if [ "$ARM" = "solo" ]; then\n    # by itself, a knob Omni-Compass owns has no other controller')
        self.assertGreater(i, 0)
        block = rig[i:i + 1400]
        self.assertIn("""grep -c '"consecutive_failures"' "$OUT_DIR/audit.jsonl\"""", block)
        self.assertIn("INVALID RUN: by itself", block)
        self.assertIn("exit 1", block)

    def test_the_hand_back_can_make_natives_autoscaler_and_the_window_that_needed_it_is_refused(self):
        # omni-v23 (the founder's order of 31 October): a knob whose scale writes the cluster refuses three times in a row goes
        # back to native's own pod autoscaler, so the identity may create one in the workload's namespace, the preflight proves
        # it, and a window of the arm by itself in which that happened is refused as a result of that arm
        app = rules("deploy/kind/rbac-omni.yaml", "Role", "omni-compass-app")
        create = [r for r in app if "horizontalpodautoscalers" in r.get("resources", []) and "create" in r["verbs"]]
        self.assertEqual(len(create), 1)
        self.assertEqual(create[0]["verbs"], ["create"])
        self.assertNotIn("resourceNames", create[0])
        rig = (ROOT / "scripts/kind_bench.sh").read_text(encoding="utf-8")
        can, _ = rig.split('echo "== cannot"', 1)
        self.assertIn("$(can create hpa -n default)", can)
        self.assertIn('"handed_back"', rig)
        self.assertIn("INVALID RUN: by itself, the knob", rig)
        self.assertIn("an autoscaler stands on the workload at the end", rig)


if __name__ == "__main__":
    unittest.main()
