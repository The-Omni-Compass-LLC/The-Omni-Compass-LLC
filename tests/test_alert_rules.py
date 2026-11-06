# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The alert rules (deploy/prometheus/omni-compass-rules.yaml) read only gauges that are served, and every rule says how
severe it is, what it means and what to do."""
import re, sys, tempfile, unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
import tools.omni_exporter as EX
import tools.omni_control as C


def served():
    names = set(re.findall(r"^# TYPE (\S+)", EX.Gauges().page(), re.M))
    names |= {n + s for n in list(names) for s in ("_sum", "_count")}
    panel = C.Panel(["true"], Path(tempfile.mkdtemp()) / "k")
    names |= set(re.findall(r"^# TYPE (\S+)", panel.metrics(), re.M))
    return names


class Rules(unittest.TestCase):
    def test_every_rule_reads_served_gauges_and_says_what_to_do(self):
        doc = yaml.safe_load((ROOT / "deploy" / "prometheus" / "omni-compass-rules.yaml").read_text(encoding="utf-8"))
        have = served()
        rules = [r for g in doc["groups"] for r in g["rules"]]
        self.assertGreaterEqual(len(rules), 8)
        for r in rules:
            used = set(re.findall(r"\bomni_[a-z0-9_]+", r["expr"]))
            self.assertTrue(used, r["alert"])
            self.assertEqual(used - have, set(), r["alert"])
            self.assertIn(r["labels"]["severity"], ("critical", "warning", "info"))
            self.assertTrue(r["annotations"]["summary"] and r["annotations"]["action"])

    def test_the_rules_file_carries_the_notice(self):
        text = (ROOT / "deploy" / "prometheus" / "omni-compass-rules.yaml").read_text(encoding="utf-8")
        self.assertIn("www.omni-compass.com", text.splitlines()[4])
        self.assertTrue(text.rstrip().endswith("www.omni-compass.com"))


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
