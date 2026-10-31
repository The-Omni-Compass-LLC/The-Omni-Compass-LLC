# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""No workflow is started by every push to main, and the live benchmark engine never starts itself (20 October).

The live benchmark engine committed its rebuilt page to main, and its own push filter matched that page, so it rebuilt itself every
seven minutes; each of those commits also started 21 workflows that only skip on a push (they run when started by hand),
each skipped run started the front page, and each front page started the live benchmark engine and the raw sweep, which cancelled
one another: 320 cancelled runs and 300 skipped ones in an hour and a half, no benchmark among them. A push trigger here
is filtered by its paths or its branches, main and the level branches are ignored by every workflow that runs only when
started, and the live benchmark engine's own page is outside its filter."""
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WF = ROOT / ".github" / "workflows"


def triggers(p):
    d = yaml.safe_load(p.read_text(encoding="utf-8"))
    return d.get("on", d.get(True)) or {}


class Triggers(unittest.TestCase):
    def test_no_unfiltered_push(self):
        for p in sorted(WF.glob("*.yml")):
            if p.name == "verify.yml":
                continue        # the check every push must pass reads every push, by design
            on = triggers(p)
            if isinstance(on, (list, str)):
                self.assertNotIn("push", on if isinstance(on, list) else [on], p.name)
                continue
            if "push" not in on:
                continue
            push = on["push"] or {}
            self.assertTrue(any(k in push for k in ("paths", "branches", "branches-ignore", "tags")), f"{p.name}: every push starts it")

    def test_a_workflow_that_runs_only_when_started_has_no_push(self):
        """26 October: a push to any branch but main started 62 runs of the workflows that run only when started by hand, every
        one skipped (the cloud, chip and benchmark sets among them), so a pull request's checks read as a wall of skipped clouds.
        A start by hand needs the workflow on main alone, where every one of them is; so none of them carries a push trigger."""
        for p in sorted(WF.glob("*.yml")):
            on = triggers(p)
            push = on.get("push") if isinstance(on, dict) else None
            self.assertFalse(push and "branches-ignore" in push, f"{p.name}: a push to a branch starts it only to skip it")

    def test_the_live_engine_never_starts_itself(self):
        paths = triggers(WF / "live-engine.yml")["push"]["paths"]
        self.assertIn("!docs/engine/OMNI_COMPASS_LIVE_ENGINE.html", paths)
        self.assertLess(paths.index("docs/engine/**"), paths.index("!docs/engine/OMNI_COMPASS_LIVE_ENGINE.html"))


if __name__ == "__main__":
    unittest.main()
