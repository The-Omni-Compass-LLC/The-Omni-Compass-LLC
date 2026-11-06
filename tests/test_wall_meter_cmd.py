# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The wall meter's command (tools/wall_meter.py, `cmd:`) runs without a shell: plain words, or plain commands joined by a
pipe, each stage's output into the next; anything else only a shell reads is refused with the reason, never handed to one."""
import shutil
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import wall_meter as W  # noqa: E402


class MeterCommand(unittest.TestCase):
    def test_plain_words_and_a_pipe_read_the_watts(self):
        self.assertEqual(W.pipeline("echo 12.5"), [["echo", "12.5"]])
        self.assertEqual(W.read("cmd:echo 41.0"), 41.0)
        self.assertEqual(W.read("cmd:echo 41.0 | cat | cat"), 41.0)
        if shutil.which("awk"):
            # a quoted '$2' and a quoted '|' are the program's own words, never a shell's
            self.assertEqual(W.pipeline("printf 'a|7.25\\n' | awk -F'|' '{print $2}'"),
                             [["printf", "a|7.25\\n"], ["awk", "-F|", "{print $2}"]])
            self.assertEqual(W.read("cmd:printf 'a|7.25\\n' | awk -F'|' '{print $2}'"), 7.25)

    def test_what_only_a_shell_reads_is_refused_with_the_reason(self):
        for cmd in ("echo $HOME", 'echo "$X"', "echo `date`", "echo 1 > /tmp/x", "cat < /etc/hostname", "echo 1; echo 2",
                    "echo 1 && echo 2", "echo 1 &", "echo *", "echo ~", "(echo 1)", "A=1 echo 3", "echo 1 |", "echo 'open"):
            with self.subTest(cmd=cmd), self.assertRaises(ValueError) as e:
                W.pipeline(cmd)
            self.assertTrue(str(e.exception).startswith("cmd:"))

    def test_no_shell_is_ever_started(self):
        real = subprocess.Popen
        seen = []

        def spy(args, *a, **kw):
            seen.append((args, kw.get("shell", False)))
            return real(args, *a, **kw)
        with mock.patch.object(W.subprocess, "Popen", side_effect=spy), \
             mock.patch.object(W.subprocess, "run", side_effect=AssertionError("no subprocess.run for the meter")):
            self.assertEqual(W.read("cmd:echo 9.5 | cat"), 9.5)
        self.assertEqual([s for _, s in seen], [False, False])
        self.assertTrue(all(isinstance(args, list) for args, _ in seen))
        self.assertNotIn("shell=True", (ROOT / "tools" / "wall_meter.py").read_text(encoding="utf-8"))

    def test_a_stage_that_hangs_is_stopped_at_the_timeout(self):
        if not shutil.which("sleep"):
            self.skipTest("no sleep on this machine")
        with mock.patch.object(W, "run_pipeline", wraps=W.run_pipeline):
            with self.assertRaises(subprocess.TimeoutExpired):
                W.run_pipeline("sleep 30 | cat", timeout=-4.5)     # the meter's own timeout plus 5 s: half a second here


if __name__ == "__main__":
    unittest.main()

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
