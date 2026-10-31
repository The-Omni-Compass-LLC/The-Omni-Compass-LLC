# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The audit of 30 October 2026 (docs/AUDIT_2026-10-30.md): the card's three-run tables read by the one key, the card's
power-capped share read as power held, the secrets diagnostic that never hands a job every secret, and the omni-v21
three-arm table with its recipe."""
import json
from pathlib import Path
import tempfile
import unittest

import yaml

from tools import gpu_abc, gpu_reps
from tools.readings import SPENT

ROOT = Path(__file__).resolve().parents[1]


def run(work_native, work_omni, served=100.0):
    """One GPU_REPS.json as tools/gpu_reps.py writes it, with the paired rows the three-run table reads."""
    def row(n, o, half):
        return {"native": n, "omni": o, "base": n, "diff": o - n, "ci95": [o - n - half, o - n + half]}
    return {"receipt": {"gpu_name": "card", "reps": 10},
            "headline": {"verdict": "NONINFERIOR / INCONCLUSIVE"},
            "paired": {"omni": {gpu_reps.PRIMARY: row(work_native, work_omni, 0.2),
                                "requests served": row(served, served, 0.0),
                                "power-capped share of samples": row(0.71, 0.60, 0.01)}},
            "means": {"native": {gpu_reps.PRIMARY: work_native}, "omni": {gpu_reps.PRIMARY: work_omni}}}


class CardTables(unittest.TestCase):
    def test_power_capped_share_is_power_held_never_work(self):
        self.assertIn("power-capped share of samples", gpu_reps.SPENT)
        self.assertEqual(gpu_abc.gauge_aim("power-capped share of samples"), SPENT)
        self.assertTrue(gpu_reps.verdict("power-capped share of samples", -0.11, 0.01, 10, base=0.71).startswith("GAIN"))

    def test_three_runs_read_by_the_one_key_with_the_engine_beside_them(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); dirs = []
            for i, (n, o) in enumerate([(43.5, 43.9), (41.5, 41.8), (42.1, 42.4)]):
                d = root / f"run-20261027T10200{i}Z"; d.mkdir()
                (d / "GPU_REPS.json").write_text(json.dumps(run(n, o)))
                (root / f"engine-20261027T10200{i}Z.txt").write_text("omni-v21 (digest b658f05d43c1e602, 63 files)\ndial: save\n")
                dirs.append(d)
            text, record = gpu_abc.table("card", dirs, ["1", "2", "3"])
            self.assertIn("omni-v21", text)
            self.assertTrue(record["rows"][gpu_reps.PRIMARY]["reading"].startswith("GAIN"))
            self.assertEqual(record["rows"]["requests served"]["reading"], "STEADY, the same")
            self.assertTrue(record["rows"]["power-capped share of samples"]["reading"].startswith("GAIN"))

    def test_three_runs_of_different_engines_are_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); dirs = []
            for i, engine in enumerate(["omni-v21 (digest a)", "omni-v20 (digest b)", "omni-v21 (digest a)"]):
                d = root / f"run-20261027T10200{i}Z"; d.mkdir()
                (d / "GPU_REPS.json").write_text(json.dumps(run(40.0, 40.4)))
                (root / f"engine-20261027T10200{i}Z.txt").write_text(engine + "\ndial: save\n")
                dirs.append(d)
            with self.assertRaises(SystemExit):
                gpu_abc.table("card", dirs, ["1", "2", "3"])

    def test_the_card_tables_on_disk_name_the_engine_that_stands(self):
        stands = json.loads((ROOT / "OMNI_V21.json").read_text())
        for f in sorted((ROOT / "results" / "gpu").glob("V21_*_ABC.json")):
            record = json.loads(f.read_text())
            engine = record["engine"][0] if isinstance(record["engine"], list) else record["engine"]
            self.assertTrue(engine.startswith("omni-v21"), f)
            self.assertIn(stands.get("digest", "b658f05d43c1e602")[:16], engine, f)


class SecretNames(unittest.TestCase):
    def test_no_job_is_handed_every_secret_and_every_name_is_tested_in_both_jobs(self):
        text = (ROOT / ".github/workflows/secret-names.yml").read_text()
        self.assertNotIn("toJSON(secrets)", text)
        workflow = yaml.safe_load(text)
        names = workflow["env"]["NAMES"].split()
        used = set()
        for wf in (ROOT / ".github/workflows").glob("*.yml"):
            if wf.name == "secret-names.yml":
                continue
            for part in wf.read_text().split("secrets.")[1:]:
                name = part.split()[0].rstrip("}),'\"")
                if name.isupper() and not name.startswith(("GITHUB_TOKEN", "KUBECONFIG_")):
                    used.add(name)
        self.assertLessEqual(used, set(names), "a secret the workflows read is missing from the diagnostic")
        for job in ("repository", "environment"):
            step = next(s for s in workflow["jobs"][job]["steps"] if "WHERE" in (s.get("env") or {}))
            for n in names:
                self.assertEqual(step["env"]["S_" + n], "${{ secrets.%s != '' }}" % n)


class ThreeArmsV21(unittest.TestCase):
    def test_the_engine_that_stands_has_its_three_arm_table_and_recipe(self):
        recipes = json.loads((ROOT / "results/live/RECIPES.json").read_text())
        flat = {k: v for k, v in recipes.items()} if "V21_THREE_ARMS_ABC" in recipes else \
            next(v for v in recipes.values() if isinstance(v, dict) and "V21_THREE_ARMS_ABC" in v)
        self.assertEqual(flat["V21_THREE_ARMS_ABC"]["runs"], ["run-40474220398", "run-40474223636", "run-40474227699"])
        record = json.loads((ROOT / "results/orchestrator/V21_THREE_ARMS_ABC.json").read_text())
        self.assertIn("omni-v21", json.dumps(record)[:4000])


class StoreNotch(unittest.TestCase):
    def test_a_dispatch_left_at_its_defaults_runs_the_counted_notch(self):
        # omni-v21's run C of all five data-store tables (40400868003, 40401042132, 40400989005, 40400963499, 40401032384) ran
        # at the workflows' default of 20 s a notch, runs A and B at the counted 30 s (scripts/reruns.txt)
        import re
        reruns = (ROOT / "scripts/reruns.txt").read_text()
        for wf in ("kafka", "ycsb", "redis", "pgbench", "sysbench"):
            workflow = yaml.safe_load((ROOT / f".github/workflows/{wf}.yml").read_text())
            on = workflow.get("on") or workflow.get(True)
            default = str(on["workflow_dispatch"]["inputs"]["step_s"]["default"])
            counted = set(re.findall(rf"\|{wf}\.yml\|[^\n]*step_s=(\d+)", reruns))
            self.assertEqual(counted, {default}, f"{wf}.yml: default {default}, counted {counted}")


if __name__ == "__main__":
    unittest.main()
