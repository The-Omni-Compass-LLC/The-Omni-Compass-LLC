# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The AMD chip's wires (scripts/apu/nvidia-smi): the harness's nvidia-smi commands answered through amd-smi. A stand-in
amd-smi (canned JSON, every write recorded) checks the translation: the power wire, the readings as one CSV line in the
order asked, the card list, the clock wire refused cleanly when amd-smi refuses it, and an unknown command refused."""
import json, os, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHIM = ROOT / "scripts" / "apu" / "nvidia-smi"

STANDIN = r'''#!/usr/bin/env python3
import json, os, sys
a = sys.argv[1:]
open(os.environ["STANDIN_AMD_LOG"], "a").write(" ".join(a) + "\n")
if a[:1] == ["version"]:
    print("AMDSMI Tool: 24.6.2"); sys.exit(0)
if a[:1] == ["list"]:
    print(json.dumps([{"gpu": 0, "bdf": "0000:01:00.0"}, {"gpu": 1, "bdf": "0000:02:00.0"}])); sys.exit(0)
if a[:1] == ["metric"]:
    print(json.dumps([{"gpu": int(a[a.index("--gpu") + 1]), "power": {"socket_power": {"value": 123.4, "unit": "W"},
          "power_cap": {"value": 150, "unit": "W"}}, "temperature": {"edge": {"value": 61, "unit": "C"}},
          "usage": {"gfx_activity": {"value": 77, "unit": "%"}}, "clock": {"gfx_0": {"clk": {"value": 1800, "unit": "MHz"}}}}]))
    sys.exit(0)
if a[:1] == ["static"]:
    print(json.dumps([{"gpu": 0, "asic": {"market_name": "AMD Instinct MI300A"},
          "limit": {"max_power_limit": {"value": 550, "unit": "W"}, "min_power_limit": {"value": 100, "unit": "W"},
                    "default_power_cap": {"value": 550, "unit": "W"}}}])); sys.exit(0)
if a[:1] == ["set"] and "--clk-limit" in a and os.environ.get("STANDIN_AMD_REFUSE_CLK"):
    print("not supported", file=sys.stderr); sys.exit(4)
if a[:1] in (["set"], ["reset"], ["process"]):
    print(json.dumps({"process_list": []}) if a[:1] == ["process"] else "ok"); sys.exit(0)
sys.exit(1)
'''


class ApuShim(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())
        standin = self.d / "amd-smi"
        standin.write_text(STANDIN); standin.chmod(0o755)
        self.log = self.d / "log.txt"
        self.env = dict(os.environ, AMD_SMI=str(standin), STANDIN_AMD_LOG=str(self.log))

    def run_shim(self, *args, env=None):
        return subprocess.run([sys.executable, str(SHIM), *args], capture_output=True, text=True, env=env or self.env)

    def test_power_wire(self):
        r = self.run_shim("-i", "0", "-pl", "150")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("set to 150.00 W", r.stdout)
        self.assertIn("set --gpu 0 --power-cap 150", self.log.read_text())

    def test_readings_in_order(self):
        r = self.run_shim("--query-gpu=power.draw,power.limit,temperature.gpu,utilization.gpu,power.max_limit,power.min_limit",
                          "--format=csv,noheader,nounits", "-i", "0")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(r.stdout.strip(), "123.40, 150.00, 61.00, 77.00, 550.00, 100.00")

    def test_card_list(self):
        r = self.run_shim("-L")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(len(r.stdout.strip().splitlines()), 2)

    def test_clock_wire_refused_cleanly(self):
        r = self.run_shim("-i", "0", "-lgc", "800,1800", env=dict(self.env, STANDIN_AMD_REFUSE_CLK="1"))
        self.assertEqual(r.returncode, 3)
        self.assertIn("not supported", r.stderr)

    def test_unknown_command_refused(self):
        self.assertEqual(self.run_shim("--bogus").returncode, 2)


def main():
    r = unittest.TextTestRunner(verbosity=0, stream=open(os.devnull, "w")).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(ApuShim))
    assert r.wasSuccessful(), f"{len(r.failures)} failures, {len(r.errors)} errors in tests/test_apu_shim.py"
    print("PASS  AMD chip wires (scripts/apu/nvidia-smi): power wire, readings in order, card list, clock wire refused cleanly")


if __name__ == "__main__":
    main()
