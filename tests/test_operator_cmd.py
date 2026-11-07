# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""omni-v14: the operator's own command (the site power reading, a muscle's read command, a wall meter's `cmd:`) runs
without a shell when it holds nothing only a shell reads, and through the shell as before when it does, so no operator's
wiring changes (docs/OMNI_V14.md; the static scan's three high findings, docs/SECURITY_SCAN.md)."""
import subprocess
import unittest
from unittest import mock

from omni_controller.muscles import run_operator_cmd


class OperatorCommand(unittest.TestCase):
    def calls(self, cmd):
        real = subprocess.run
        seen = []

        def spy(*a, **k):
            seen.append((a[0], bool(k.get("shell"))))
            return real(*a, **k)
        with mock.patch("omni_controller.muscles.subprocess.run", spy):
            out = run_operator_cmd(cmd).stdout.strip()
        return out, seen[0]

    def test_a_plain_command_runs_without_a_shell(self):
        out, (args, shell) = self.calls("echo 412.5")
        self.assertEqual(out, "412.5")
        self.assertFalse(shell)
        self.assertEqual(args, ["echo", "412.5"])

    def test_quotes_are_read_as_a_shell_reads_them(self):
        out, (args, shell) = self.calls("printf '%s\\n' '7 W'")
        self.assertFalse(shell)
        self.assertEqual(out, "7 W")

    def test_a_pipe_a_variable_or_an_assignment_keeps_the_shell(self):
        for cmd in ("echo 3 | cat", "echo $((1+2))", "X=3 sh -c 'echo $X'", "echo 3 > /dev/stdout"):
            out, (args, shell) = self.calls(cmd)
            self.assertTrue(shell, cmd)
            self.assertEqual(out, "3", cmd)


if __name__ == "__main__":
    unittest.main()
