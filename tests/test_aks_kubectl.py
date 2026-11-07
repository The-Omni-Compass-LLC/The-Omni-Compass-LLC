# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The client that rejected the real resize must fail before a measured window starts."""
import hashlib
from pathlib import Path
import tempfile
import unittest
from scripts import aks_kubectl as client


class AksClient(unittest.TestCase):
    def test_original_client_and_server_are_rejected(self):
        with self.assertRaises(RuntimeError):
            client.validate_versions('v1.31.0', 'v1.36.4')
        with self.assertRaisesRegex(RuntimeError, 'resize requires'):
            client.validate_versions('v1.31.0', 'v1.32.0')
        client.validate_versions('v1.36.4', 'v1.36.4')

    def test_version_match_without_server_resize_is_not_a_full_control_pass(self):
        versions = {'clientVersion': {'gitVersion': 'v1.36.4'}, 'serverVersion': {'gitVersion': 'v1.36.4'}}
        with self.assertRaisesRegex(RuntimeError, 'does not advertise'):
            client.check(runner=lambda args: versions if args[0] == 'version' else {'resources': []})
        result = client.check(runner=lambda args: versions if args[0] == 'version' else
                              {'resources': [{'name': 'pods/resize', 'verbs': ['get', 'patch', 'update']}]})
        self.assertTrue(result['resize_required'])

    def test_download_is_verified_before_replacing_existing_client(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / 'kubectl'; target.write_bytes(b'working client')
            fetch = lambda url: b'0' * 64 if url.endswith('.sha256') else b'corrupt download'
            with self.assertRaisesRegex(RuntimeError, 'checksum mismatch'):
                client.install('1.36.4', directory, fetch)
            self.assertEqual(target.read_bytes(), b'working client')
            good = b'#!/bin/sh\nexit 0\n'
            fetch = lambda url: hashlib.sha256(good).hexdigest().encode() if url.endswith('.sha256') else good
            self.assertEqual(client.install('1.36.4', directory, fetch).read_bytes(), good)
            self.assertTrue(target.stat().st_mode & 0o111)

    def test_version_input_cannot_select_an_untrusted_download_path(self):
        for version in ('https://example.com/client', '../1.36.4', '1.36', '1.36.4/other'):
            with self.assertRaises(ValueError):
                client.release(version)


if __name__ == '__main__':
    unittest.main()
