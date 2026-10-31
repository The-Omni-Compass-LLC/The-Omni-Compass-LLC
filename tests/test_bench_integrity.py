# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Incomplete watches cannot turn missing Ready transitions into measured waiting."""
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

import yaml
from tools import bench_integrity as integrity
from pilot.bench_report import pod_starts

ROOT = Path(__file__).resolve().parents[1]


def pod(ready=False, scheduled=False):
    conditions = []
    for name, yes in [('Ready', ready), ('PodScheduled', scheduled)]:
        if yes:
            conditions.append({'type': name, 'status': 'True', 'lastTransitionTime': '1970-01-01T00:01:50Z'})
    return {'metadata': {'uid': 'one', 'creationTimestamp': '1970-01-01T00:01:45Z', 'resourceVersion': '11'},
            'status': {'conditions': conditions}}


class PodEvidence(unittest.TestCase):
    def fixture(self, root, events, final=None):
        (root / 'window_start.txt').write_text('100\n')
        (root / 'window_end.txt').write_text('120\n')
        (root / 'pod_watch.json').write_text('\n'.join(json.dumps({'type': 'MODIFIED', 'object': p}) for p in events))
        (root / 'pods_end.json').write_text(json.dumps({'items': [final or pod(True, True)]}))
        (root / 'pod_watch_receipt.json').write_text(json.dumps(
            {'schema': 1, 'complete': True, 'started_at': 99, 'ended_at': 121, 'segments': 2}))

    def test_missing_ready_transition_rejects_gauge_instead_of_end_snapshot_imputation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); self.fixture(root, [pod(False, True)])
            with self.assertRaisesRegex(ValueError, 'missed Ready'):
                pod_starts(root)

    def test_missing_scheduled_transition_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); self.fixture(root, [pod(True, False)])
            with self.assertRaisesRegex(ValueError, 'missed PodScheduled'):
                integrity.validate(root)

    def test_complete_stream_uses_the_event_timestamp(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); self.fixture(root, [pod(), pod(True, True)])
            self.assertEqual(pod_starts(root)['pod start wait, total (s)'], 5)

    def test_transition_after_window_is_censored_at_window_end(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); late = pod(True, True)
            for condition in late['status']['conditions']:
                condition['lastTransitionTime'] = '1970-01-01T00:02:30Z'
            self.fixture(root, [pod(), late], late)
            self.assertEqual(pod_starts(root)['pod start wait, total (s)'], 15)

    def test_partial_json_and_api_error_are_rejected(self):
        for text in ['{"type": "ADDED"', '{"type":"ERROR","object":{"code":410}}']:
            with self.assertRaises(ValueError):
                list(integrity.read_events(text))

    def test_failed_collector_receipt_is_never_admitted(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); self.fixture(root, [pod(True, True)])
            (root / 'pod_watch_receipt.json').write_text('{"complete":false,"error":"expired history"}')
            with self.assertRaisesRegex(ValueError, 'expired history'):
                integrity.validate(root)

    def test_collector_continues_bookmark_version_without_relisting(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); urls = []
            listing = {'metadata': {'resourceVersion': '10'}, 'items': [pod()]}
            def run(args, **kwargs):
                return subprocess.CompletedProcess(args, 0, json.dumps(listing))
            class Process:
                def __init__(self, text):
                    self.stdout = io.StringIO(text)
                def wait(self, **kwargs): return 0
                def poll(self): return 0
            def popen(args, **kwargs):
                urls.append(args[3])
                if len(urls) == 1:
                    return Process(json.dumps({'type': 'BOOKMARK', 'object': {'metadata': {'resourceVersion': '11'}}}) + '\n')
                (root / 'pod_watch.stop').touch()
                return Process(json.dumps({'type': 'MODIFIED', 'object': pod(True, True)}) + '\n')
            integrity.collect(root, run=run, popen=popen)
            self.assertIn('resourceVersion=10', urls[0])
            self.assertIn('resourceVersion=11', urls[1])
            self.assertTrue(json.loads((root / 'pod_watch_receipt.json').read_text())['complete'])

    def collect_with(self, root, segments):
        """Run the collector over scripted watch requests: (stdout text, exit code, stderr text) each."""
        listing = {'metadata': {'resourceVersion': '10'}, 'items': [pod()]}
        urls = []
        def run(args, **kwargs):
            return subprocess.CompletedProcess(args, 0, json.dumps(listing))
        class Process:
            def __init__(self, text, code):
                self.stdout = io.StringIO(text); self.code = code
            def wait(self, **kwargs): return self.code
            def poll(self): return self.code
        def popen(args, stderr=None, **kwargs):
            urls.append(args[3])
            text, code, said = segments[len(urls) - 1]
            if said:
                stderr.write(said); stderr.flush()
            if len(urls) == len(segments):
                (root / 'pod_watch.stop').touch()
            return Process(text, code)
        integrity.collect(root, run=run, popen=popen, sleep=lambda s: None)
        return urls

    def test_client_timeout_resumes_at_the_last_version_and_drops_the_cut_line(self):
        # run 40938221203, repetition 360: one client timeout after 11 clean segments refused the whole arm
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            seen = json.dumps({'type': 'BOOKMARK', 'object': {'metadata': {'resourceVersion': '12'}}}) + '\n'
            urls = self.collect_with(root, [
                (seen + '{"type": "MODIFIED", "obj', 1, 'error: net/http: request canceled (Client.Timeout)\n'),
                (json.dumps({'type': 'MODIFIED', 'object': pod(True, True)}) + '\n', 0, '')])
            self.assertIn('resourceVersion=12', urls[1])
            receipt = json.loads((root / 'pod_watch_receipt.json').read_text())
            self.assertTrue(receipt['complete'])
            self.assertEqual((receipt['segments'], receipt['client_retries']), (1, 1))
            self.assertEqual(len((root / 'pod_watch.json').read_text().splitlines()), 3)

    def test_expired_history_is_never_resumed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaisesRegex(RuntimeError, 'expired'):
                self.collect_with(root, [('', 1, 'Error from server (Expired): too old resource version\n')])
            self.assertFalse(json.loads((root / 'pod_watch_receipt.json').read_text())['complete'])

    def test_repeated_client_failures_fail_the_receipt(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaisesRegex(RuntimeError, 'in a row'):
                self.collect_with(root, [('', 1, 'error: context deadline exceeded\n')] * integrity.RETRIES)
            self.assertFalse(json.loads((root / 'pod_watch_receipt.json').read_text())['complete'])

    def test_client_failure_writes_failed_receipt(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            def fail(args, **kwargs): raise subprocess.CalledProcessError(1, args)
            with self.assertRaises(subprocess.CalledProcessError):
                integrity.collect(root, run=fail)
            self.assertFalse(json.loads((root / 'pod_watch_receipt.json').read_text())['complete'])


class RolloutCleanup(unittest.TestCase):
    def test_owned_pause_is_restored_atomically_even_if_already_resumed(self):
        for paused in [True, False]:
            state = {'metadata': {'resourceVersion': '7', 'annotations': {integrity.PAUSE: 'true'}}, 'spec': {'paused': paused}}
            writes = []
            def run(args, **kwargs):
                if args[1] == 'patch':
                    patch = json.loads(args[args.index('-p') + 1]); writes.append(patch)
                    self.assertEqual(patch['metadata']['resourceVersion'], '7')
                    state['spec']['paused'] = False; state['metadata']['annotations'] = {}
                return subprocess.CompletedProcess(args, 0, json.dumps(state))
            self.assertTrue(integrity.restore_rollout('default/web', run=run))
            self.assertFalse(integrity.restore_rollout('default/web', run=run))
            self.assertEqual(len(writes), 1)

    def test_foreign_paused_deployment_is_untouched(self):
        state = {'metadata': {'resourceVersion': '7'}, 'spec': {'paused': True}}
        def run(args, **kwargs):
            self.assertEqual(args[1], 'get')
            return subprocess.CompletedProcess(args, 0, json.dumps(state))
        self.assertFalse(integrity.restore_rollout('default/web', run=run))

    def test_permission_or_concurrent_write_failure_propagates(self):
        state = {'metadata': {'resourceVersion': '7', 'annotations': {integrity.PAUSE: 'true'}}, 'spec': {'paused': False}}
        def run(args, **kwargs):
            if args[1] == 'patch': raise subprocess.CalledProcessError(1, args)
            return subprocess.CompletedProcess(args, 0, json.dumps(state))
        with self.assertRaises(subprocess.CalledProcessError):
            integrity.restore_rollout('default/web', run=run)

    def test_conflict_with_the_autoscaler_is_read_again_and_retried(self):
        # run 40938221203, repetition 349: the HPA wrote the Deployment between the reset's read and its patch
        state = {'metadata': {'resourceVersion': '7', 'annotations': {integrity.PAUSE: 'true'}}, 'spec': {'paused': True}}
        versions = []
        def run(args, **kwargs):
            if args[1] == 'patch':
                versions.append(json.loads(args[args.index('-p') + 1])['metadata']['resourceVersion'])
                if len(versions) == 1:
                    state['metadata']['resourceVersion'] = '8'
                    raise subprocess.CalledProcessError(1, args, stderr='Operation cannot be fulfilled on '
                        'deployments.apps "web": the object has been modified; please apply your changes')
                state['spec']['paused'] = False; state['metadata']['annotations'] = {}
            return subprocess.CompletedProcess(args, 0, json.dumps(state))
        self.assertTrue(integrity.restore_rollout('default/web', run=run))
        self.assertEqual(versions, ['7', '8'])


class SparseEngineCheckout(unittest.TestCase):
    def test_actual_matrix_checkout_can_identify_the_engine(self):
        # Exercise the YAML's patterns against a real sparse Git index, not a mirrored string assertion. A worktree of this
        # repository, never a clone of it: a clone copies every object (7 GB where the raw runs' pack is present), and a partial
        # or shallow clone, as a cloud session checks the repository out, cannot serve one at all (30 October 2026).
        workflow = yaml.safe_load((ROOT / '.github/workflows/six-kube.yml').read_text())
        checkout = next(s for s in workflow['jobs']['run']['steps'] if s.get('uses', '').startswith('actions/checkout@'))
        patterns = checkout['with']['sparse-checkout']
        with tempfile.TemporaryDirectory() as directory:
            tree = str(Path(directory) / 'sparse')
            def git(*args, **kwargs):
                return subprocess.run(['git', *args], check=True, capture_output=True, text=True, **kwargs)
            git('-C', str(ROOT), 'worktree', 'add', '--detach', '--no-checkout', tree, 'HEAD')
            try:
                git('-C', tree, 'sparse-checkout', 'init', '--no-cone')
                git('-C', tree, 'sparse-checkout', 'set', '--no-cone', '--stdin', input=patterns)
                git('-C', tree, 'checkout', 'HEAD')
                result = subprocess.run(['python3', 'tools/omni_version.py'], cwd=tree, capture_output=True, text=True)
            finally:
                subprocess.run(['git', '-C', str(ROOT), 'worktree', 'remove', '--force', tree], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            from tools.omni_version import VERSIONS
            self.assertIn(f"omni-{next(iter(VERSIONS))}", result.stdout, "the sparse checkout names the engine that stands")


class FailedArmEvidence(unittest.TestCase):
    def test_failed_arm_is_marked_and_all_diagnostic_hashes_verify(self):
        script = (ROOT / 'scripts/kind_bench.sh').read_text()
        start = script.index('finish_evidence() {')
        end = script.index('trap finish_evidence EXIT', start) + len('trap finish_evidence EXIT')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'diagnostic with spaces.txt').write_text('original failure details\n')
            result = subprocess.run(['bash', '-c', 'set -euo pipefail\nOUT_DIR="$1"\n' + script[start:end] + '\nexit 7',
                                     'arm', directory], capture_output=True, text=True)
            self.assertEqual(result.returncode, 7, result.stderr)
            self.assertIn('exit 7', (root / 'INVALID').read_text())
            checked = subprocess.run(['sha256sum', '-c', 'SHA256SUMS.txt'], cwd=root, capture_output=True, text=True)
            self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)


if __name__ == '__main__':
    unittest.main()
