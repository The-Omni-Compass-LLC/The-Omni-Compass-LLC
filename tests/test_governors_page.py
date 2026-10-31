# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The governors and orchestrators page (tools/governors_page.py): every one the founder named stands on it; a line reads
only from its own three-run table, every row counted by the one key, losses included; without a table it says where its
runs stand and writes no number."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
import tools.governors_page as G

FOUNDERS_LIST = ("Kueue", "Volcano", "Crane", "Open Cluster Management", "CruiseKube", "Gödel", "Armada", "Karmada",
                 "Kubernetes scheduler", "KAI", "Nephio", "KubeEdge", "KubeRay", "Koordinator")


class GovernorsPage(unittest.TestCase):
    def test_every_one_named_stands_on_the_page(self):
        text = G.render(runs={})
        for name in FOUNDERS_LIST:
            self.assertIn(name, text)
        self.assertIn("www.omni-compass.com", text.splitlines()[2])          # the notice under the title
        self.assertIn("www.omni-compass.com", text.rstrip().splitlines()[-1])  # and at the end

    def test_a_line_reads_only_from_its_table(self):
        table = {"runs": [{"tag": x, "run": i, "engine": "omni-v12 (digest d38b58fbe28939b8, 47 files)", "paired_repetitions": 10}
                          for x, i in zip("ABC", ("1", "2", "3"))], "rows": {
            "queue: job wait, submitted to its first pod running, mean (s)": {"reading": "GAIN in all three of our runs"},
            "queue: jobs unfinished at the window's end": {"reading": "LOSS in all three of our runs"},
            "machines in service, mean": {"reading": "power given in all three of our runs"},
            "energy (kWh)": {"reading": "STEADY, no difference beyond the noise (all three runs)"},
            "pods started": {"reading": "shown, not judged"}}}
        with tempfile.TemporaryDirectory() as t:
            live = Path(t) / "results" / "live"; live.mkdir(parents=True)
            (live / "V12_KAI.json").write_text(json.dumps(table))
            with mock.patch.object(G, "ROOT", Path(t)):
                text = G.render(runs={"koordinator": {"A": "9"}})
        kai = next(l for l in text.splitlines() if l.startswith("| KAI scheduler"))
        self.assertIn("1 GAIN, 1 LOSS, 1 power given, 1 STEADY, 0 where the runs disagree", kai)
        koord = next(l for l in text.splitlines() if l.startswith("| Koordinator"))
        self.assertIn("runs not yet finished", koord)
        self.assertIn("LOSS in all three of our runs", text)                  # every row counted and shown, losses included
        self.assertIn("A [1](", text); self.assertIn("(10 pairs)", text)      # the runs as tools/confirm_abc.py records them
        self.assertIn("omni-v12 (digest d38b58fbe28939b8, 47 files)", text)

    def test_the_scheduler_reads_each_setting_from_its_own_table(self):
        table = {"runs": ["1", "2", "3"], "engines": ["omni-v12"] * 3,
                 "rows": {"queue: jobs unfinished at the window's end": {"reading": "LOSS in all three of our runs"}}}
        with tempfile.TemporaryDirectory() as t:
            live = Path(t) / "results" / "live"; live.mkdir(parents=True)
            (live / "V12_BINPACK.json").write_text(json.dumps(table))
            with mock.patch.object(G, "ROOT", Path(t)):
                text = G.render(runs={"vanilla": {"A": "7", "B": "8", "C": "9"}})
        line = next(l for l in text.splitlines() if l.startswith("| The Kubernetes scheduler"))
        self.assertIn("as shipped: runs not yet finished", line)
        self.assertIn("bin-packing profile: 0 GAIN, 1 LOSS", line)
        self.assertIn("(V12_BINPACK.md)", line)
        self.assertIn("- **Readings (as shipped)**: none yet", text)

    def test_the_four_ways_read_each_comparison_from_its_own_table(self):
        table = {"runs": ["1", "2", "3"], "engines": ["omni-v12"] * 3,
                 "rows": {"queue: job wait, submitted to its first pod running, mean (s)": {"reading": "GAIN in all three of our runs"}}}
        with tempfile.TemporaryDirectory() as t:
            live = Path(t) / "results" / "live"; live.mkdir(parents=True)
            (live / "V12_KAI_4W_ORCH.json").write_text(json.dumps(table))
            with mock.patch.object(G, "ROOT", Path(t)):
                text = G.render(runs={"kai4": {"A": "4", "B": "5", "C": "6"}})
        section = text.split("## The four ways")[1].split("\n## ")[0]
        kai = next(l for l in section.splitlines() if l.startswith("| The KAI scheduler"))
        cells = [c.strip() for c in kai.strip().strip("|").split("|")]
        self.assertIn("[A](", cells[1])
        self.assertEqual(cells[2], "runs not yet finished")              # Omni-Compass on top of it: no table yet
        self.assertTrue(cells[3].startswith("1 GAIN, 0 LOSS"))           # it as shipped against the organism alone
        self.assertIn("(V12_KAI_4W_ORCH.md)", cells[3])
        volcano = next(l for l in section.splitlines() if l.startswith("| Volcano"))
        self.assertIn("not yet started", volcano)
        with mock.patch.object(G, "ROOT", Path(tempfile.mkdtemp())):
            text = G.render(runs={"kueue4": {"A": "7"}})
        kueue = next(l for l in text.splitlines() if l.startswith("| Kueue"))     # its line in the governors' table
        self.assertIn("running four ways (below)", kueue)

    def test_no_number_before_the_runs(self):
        text = G.render(runs={})
        crane = next(l for l in text.splitlines() if l.startswith("| Crane"))
        self.assertTrue(crane.endswith("| not yet run |"))

    def test_every_catalog_muscle_named_is_in_the_catalog(self):
        import csv
        rows = list(csv.DictReader((ROOT / "realms" / "catalog_v5.csv").open()))
        for slug, (fid, muscles) in G.CATALOG.items():
            family = {r["muscle"] for r in rows if r["family_id"] == str(fid)}
            for m in muscles:
                self.assertIn(m, family, f"{slug}: {m} is not in family {fid}")
        self.assertEqual(set(G.CATALOG), {g[0] for g in G.GOVERNORS})


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
