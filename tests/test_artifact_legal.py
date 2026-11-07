# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every artifact carries the legal files without relocating or replacing measured results."""
import json
from pathlib import Path
import tempfile
import unittest
from tools import artifact_legal as legal


class ArtifactLegal(unittest.TestCase):
    def test_directory_and_file_glob_keep_their_original_search_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in legal.BUNDLE:
                (root / name).write_text('exact legal bytes: ' + name)
            out = root / 'reps'; out.mkdir(); (out / 'LIVE_REPS.md').write_text('measured result')
            for pattern in ('reps', 'reps/LIVE_REPS.*'):
                result = legal.attach(pattern, root)
                self.assertEqual(result.splitlines()[0], pattern)
                self.assertTrue(all(Path(p).parent == out / '_omni_legal' for p in result.splitlines()[1:]))
                for name in legal.BUNDLE:
                    self.assertEqual((out / '_omni_legal' / name).read_bytes(), (root / name).read_bytes())
            self.assertEqual((out / 'LIVE_REPS.md').read_text(), 'measured result')
            self.assertEqual(len(json.loads((out / '_omni_legal/SHA256SUMS.json').read_text())), 6)

    def test_multiple_roots_and_negations_are_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in legal.BUNDLE:
                (root / name).write_text(name)
            pattern = 'bench-*\npaired.log\n!bench-*/unwanted'
            result = legal.attach(pattern, root)
            self.assertTrue(result.startswith(pattern + '\n'))
            self.assertEqual(Path(result.splitlines()[-1]).parent, root / '_omni_legal')

    def test_collect_without_checkout_uses_only_the_required_legal_names(self):
        with tempfile.TemporaryDirectory() as tmp:
            calls = []
            def load(name):
                calls.append(name)
                return b'public legal source'
            result = legal.attach('out/*.log\nout/unfinished\n!out/skip', Path(tmp), load)
            self.assertEqual(calls, list(legal.BUNDLE))
            self.assertIn('_omni_legal/README.md', result)

    def test_missing_legal_file_is_a_failure(self):
        with tempfile.TemporaryDirectory() as tmp, self.assertRaises(FileNotFoundError):
            legal.attach('out', Path(tmp))

    def test_every_workflow_artifact_uses_the_tested_bundle_and_same_condition(self):
        import re
        import yaml
        root = Path(__file__).resolve().parents[1]
        runtime = (root / 'tools/artifact_legal.py').read_text().strip()
        count = 0
        for path in (root / '.github/workflows').glob('*.yml'):
            workflow = yaml.safe_load(path.read_text())
            for job in workflow['jobs'].values():
                steps = job.get('steps', [])
                by_id = {s.get('id'): s for s in steps if s.get('id')}
                for step in steps:
                    if not str(step.get('uses', '')).startswith('actions/upload-artifact'):
                        continue
                    values = step.get('with') or {}
                    if values.get('name') == 'legal-notice':
                        continue
                    match = re.fullmatch(r'\$\{\{ steps\.(omni_legal_export_\d+)\.outputs\.paths \}\}', values['path'])
                    self.assertIsNotNone(match, path)
                    bundle = by_id[match.group(1)]
                    self.assertEqual(bundle.get('if'), step.get('if'), path)
                    self.assertEqual(bundle['run'].strip(), runtime, path)
                    self.assertTrue(bundle['env']['OMNI_EXPORT_PATHS'], path)
                    count += 1
        self.assertGreater(count, 0)


if __name__ == '__main__':
    unittest.main()
