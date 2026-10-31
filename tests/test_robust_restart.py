# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The kill-drill replacement must inherit the same complete controller wiring."""
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RobustRestart(unittest.TestCase):
    def test_exported_restart_function_reaches_controller_with_full_cap_wiring(self):
        text = (ROOT / 'scripts/kind_bench.sh').read_text()
        start = text.index('start_controller()')
        end = text.index('\n}\n', start) + 3
        function = text[start:end]
        export = re.search(r'^    export .*\bDRY\b.*$', text, re.M).group(0)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'python').write_text('#!/usr/bin/env python3\nimport os,json,sys\nopen(os.environ["CAPTURE_ARGS"],"w").write(json.dumps(sys.argv[1:]))\n')
            (root / 'python').chmod(0o755)
            env = dict(os.environ, PATH=tmp + os.pathsep + os.environ['PATH'], CAPTURE_ARGS=str(root / 'args.json'))
            env.pop('CAP_ARGS', None)
            settings = dict(DRY='', KUBECTL='kubectl', WORKERS='4', SITE_LIMIT_W='200', OUT_DIR=tmp,
                            STRICT='', LAW='', CLOSURE='', REPLICA_CEILING='', OMNI_DIAL='save', MIN_NODES='2',
                            NODE_CUSHION='0', SLO_MS='500', OMNI_NICE='0', OMNI_SENSED='default/php-apache',
                            OMNI_POWER_CMD='', OMNI_INTERVAL='60', OMNI_FLOOR_INTERVAL='5', GIVE_BACK_ONLY='', GOV_PIN='', OWN='')
            env.update(settings)
            script = function + '\nCAP_ARGS="--cap-deployments default/php-apache"\nexport -f start_controller\n' + export
            script += '\nbash -uc \'start_controller 1 "$OUT_DIR/child.log" >/dev/null\'\n'
            script += 'for i in $(seq 1 100); do [ -s "$CAPTURE_ARGS" ] && break; sleep 0.01; done\n'
            result = subprocess.run(['bash', '-eu', '-c', script], env=env, capture_output=True, text=True)
            capture = root / 'args.json'
            details = (root / 'child.log').read_text() if (root / 'child.log').exists() else result.stderr
            self.assertTrue(capture.exists(), details)
            args = json.loads(capture.read_text())
            self.assertIn('--cap-deployments', args)
            self.assertEqual(args[args.index('--cap-deployments') + 1], 'default/php-apache')
            self.assertEqual(args[args.index('--iterations') + 1], '1')

    def test_every_variable_the_restart_reads_is_exported(self):
        # 17 Oct: GIVE_BACK_ONLY joined the command line on 15 October but not the export list, so under `set -u` the
        # second governor stopped before it began and every kill run of omni-v7 was invalid
        text = (ROOT / 'scripts/kind_bench.sh').read_text()
        start = text.index('start_controller()')
        function = text[start:text.index('\n}\n', start)]
        bare = set(re.findall(r'\$\{?([A-Z_][A-Z0-9_]*)\}?(?![:A-Z0-9_])', function))
        exported = set()
        for line in re.findall(r'^\s*export (.*)$', text, re.M):
            exported |= {w.split('=')[0] for w in line.split() if re.match(r'[A-Z_][A-Z0-9_]*(=|$)', w)}
        self.assertFalse(bare - exported, f'read by start_controller but not exported: {sorted(bare - exported)}')


if __name__ == '__main__':
    unittest.main()
