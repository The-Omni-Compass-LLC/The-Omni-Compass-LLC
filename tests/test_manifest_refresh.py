# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""An automated page refresh must not silently re-seal engines or fabricate verification."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from tools import release_manifest as manifest
from tools.legal import normalize_markdown


class GeneratedManifest(unittest.TestCase):
    def fixture(self, root, old):
        record = {'files': {'fixture': {n: hashlib.sha256(s).hexdigest() for n, s in old.items()}},
                  'verification_receipt': {'passed': False, 'sha256': 'historical'}}
        for n, s in old.items():
            p = root / n; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(s)
        target = root / 'RELEASE_MANIFEST.json'; target.write_text(json.dumps(record))
        return target

    def test_real_legal_footer_case_refreshes_without_promoting_verification(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); name = 'docs/AZURE_REPAIR.md'
            old = {name: b'# Repair\n\nMeasured outcome remains unchanged.\n'}
            target = self.fixture(root, old)
            (root / name).write_text(normalize_markdown(old[name].decode())[0])
            with patch.object(manifest, 'ROOT', root), patch.object(manifest, 'MANIFEST', target):
                self.assertEqual(manifest.refresh_generated(old.__getitem__), [name])
                self.assertEqual(manifest.refresh_generated(old.__getitem__), [])
            record = json.loads(target.read_text())
            self.assertFalse(record['verification_receipt']['passed'])
            self.assertEqual(record['generated_refresh']['verification'], 'not run by this refresh')

    def test_source_change_rejects_entire_batch_before_any_hash_is_written(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            old = {'results/OMNI_INDEX.md': b'old derived table', 'omnicompass/core.py': b'original engine'}
            target = self.fixture(root, old); before = target.read_bytes()
            for n in old: (root / n).write_bytes(b'changed')
            with patch.object(manifest, 'ROOT', root), patch.object(manifest, 'MANIFEST', target):
                with self.assertRaisesRegex(ValueError, 'cannot re-seal'):
                    manifest.refresh_generated(old.__getitem__)
            self.assertEqual(target.read_bytes(), before)

    def test_preexisting_drift_requires_explicit_repair(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); name = 'results/OMNI_INDEX.md'
            target = self.fixture(root, {name: b'expected'})
            (root / name).write_bytes(b'new generated report')
            with patch.object(manifest, 'ROOT', root), patch.object(manifest, 'MANIFEST', target):
                with self.assertRaisesRegex(ValueError, 'baseline already differs'):
                    manifest.refresh_generated(lambda _: b'unverified baseline')


if __name__ == '__main__':
    unittest.main()
