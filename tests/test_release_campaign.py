# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The approved campaign's dispatch boundaries and the v6 capacity regressions."""
import inspect
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
import unittest.mock
import yaml
from scripts import dispatch_grid as grid
from tests import test_kind_capacity as capacity

ROOT = Path(__file__).resolve().parents[1]


class ReleaseCampaign(unittest.TestCase):
    def test_capacity_regressions(self):
        for name, fn in vars(capacity).items():
            if name.startswith('test_') and callable(fn):
                with self.subTest(test=name), tempfile.TemporaryDirectory() as tmp:
                    fn(**({'tmp_path': Path(tmp)} if inspect.signature(fn).parameters else {}))

    def test_queue_is_complete_and_excluded_providers_cannot_dispatch(self):
        queue = grid.rerun_queue()
        self.assertEqual(len(queue), 195)        # 65 entries, A, B and C (Omni-Compass by itself a second time, on the rig as
                                                 # amended on 31 October; the steady and wandering tests back since omni-v8;
                                                 # MySQL, Redis and MongoDB with native as shipped beside the operator's, 17 October;
                                                 # every data store at the max beside the tune-down, 18 October;
                                                 # the extended fault test, 18 October; CruiseKube on the recorder that
                                                 # counts the add-on's marked workers in service, 19 October;
                                                 # the cost to match, native tuned harder beside Omni on top, 19 October;
                                                 # the batch stream through Kueue and through Volcano, 19 October, night;
                                                 # through the KAI scheduler and through Koordinator, in their own workflow,
                                                 # 20 October; through the Kubernetes scheduler alone, as shipped and with
                                                 # its bin-packing profile, 20 October; Koordinator again, on the
                                                 # kubelet's cgroup root its own tests use, 20 October; the governors
                                                 # four ways, 20 October; KubeRay, Crane, Gödel, Karmada and OCM four
                                                 # ways, each in its own rig, 20 October; the decision pace,
                                                 # docs/PACE_PREREGISTRATION.md, 22 October, eight arms on the heartbeat
                                                 # dial since omni-v17; omni-v16's second levers block, its rig fixed
                                                 # before the omni-v17 campaign opened, is not carried into it; Omni-Compass
                                                 # by itself, the steady load with three arms, written before the omni-v19
                                                 # campaign opened, 24 October)
        shipped = [row for row in queue if row[3].get('native') == 'shipped']
        for wf in ('redis.yml', 'kafka.yml', 'sysbench.yml', 'ycsb.yml', 'pgbench.yml'):   # the max is the default brain (12 October)
            self.assertEqual({row[3].get('objective') for row in queue if row[2] == wf and row[3].get('native') != 'shipped'},
                             {'resource', 'service'}, wf)
        self.assertEqual({row[2] for row in shipped}, {'sysbench.yml', 'redis.yml', 'ycsb.yml'})
        self.assertEqual({row[0] for row in queue}, set('ABC'))
        workflows = {row[2] for row in queue}
        self.assertTrue({'capacity.yml', 'pandapower.yml', 'swarm.yml', 'cpu-power.yml',
                         'realms-v5.yml', 'kind-cruisekube.yml', 'aks-metered-full.yml'} <= workflows)
        self.assertFalse({'gke-metered.yml', 'eks-metered.yml', 'cloud-organism.yml',
                          'gpu-bench.yml', 'lambda-gpu.yml'} & workflows)
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'reruns.txt'
            p.write_text('unapproved|gke-metered.yml|\n')
            old = grid.RERUNS
            try:
                grid.RERUNS = p
                with self.assertRaises(ValueError):
                    grid.rerun_queue()
            finally:
                grid.RERUNS = old

    def test_every_block_stands_as_it_was_when_its_runs_began(self):
        # a run is read back by its count in its workflow, so an entry put among entries already under way takes a started
        # run's place (18 October); each block is frozen here as it stood, and an entry added later opens a new block
        frozen = [
            ['core benchmark', 'Kubernetes baseline', 'Kubernetes full controls', 'Kubernetes levers',
             'Kubernetes observe-only check', 'Kubernetes CruiseKube', 'Kubernetes Goldilocks', 'Kubernetes fixed capacity',
             'Kubernetes scale control plane', 'every catalog muscle', '1107 muscles and seven organisms',
             'Linux CPU governor and meter capability', 'Azure full-control six-stage burst', 'large organisms on Azure',
             'kubernetes steady', 'kubernetes by itself', 'kubernetes decision pace', 'kubernetes wandering', 'kubernetes all four', 'kubernetes fairness', 'kubernetes faults',
             'kubernetes batch', 'kubernetes google 2011 trace', 'kubernetes keda add-ons', 'redis resource', 'kafka resource',
             'postgresql resource', 'mysql resource', 'mongodb resource', 'redis service', 'kafka service',
             'mysql resource, native as shipped', 'redis resource, native as shipped', 'mongodb resource, native as shipped',
             'robot arms', 'power grids', 'buildings and batteries', 'drone swarms', 'robustness kill', 'robustness long',
             'kubernetes batch through kueue', 'kubernetes batch through volcano'],   # written before the omni-v12 campaign opened;
                                                                                      # Omni-Compass by itself before the omni-v19
                                                                                      # campaign opened (24 October), no run of it started;
                                                                                      # the decision pace before the omni-v16 campaign
                                                                                      # opened (22 October), when no run of it had started,
                                                                                      # its eight arms before the omni-v17 campaign opened
            ['mysql service', 'mongodb service', 'postgresql service', 'kubernetes faults extended'],   # added 18 October, night
            ['Kubernetes CruiseKube, recorder in service'],                                               # added 19 October
            ['kubernetes cost to match'],                                                                 # added 19 October, evening
            ['kubernetes batch through kai'],                                                             # added 20 October
            ['kubernetes batch through koordinator'],                                                     # added 20 October
            ['kubernetes batch through the default scheduler',
             'kubernetes batch through the bin-packing scheduler'],                                       # added 20 October
            ['kubernetes batch through koordinator, on the cgroup root its own tests use'],              # added 20 October
            [f"kubernetes batch four ways through {n}" for n in ("the KAI scheduler", "Koordinator", "Kueue", "Volcano",
                                                                 "the bin-packing scheduler")],             # added 20 October
        ]
        blocks = grid.rerun_blocks()
        self.assertEqual([[n for n, _, _ in b] for b in blocks[:len(frozen)]], frozen)
        self.assertTrue(all(len(b) > 0 for b in blocks))

    def test_a_labelled_run_is_started_with_its_own_letter(self):
        # 19 October: a workflow whose run records its label is passed the rerun's own A, B or C; every other is passed
        # the queue's inputs alone, which it would refuse with an input it does not declare
        queued = {row[2] for row in grid.rerun_queue()}
        for wf in sorted(queued):
            inputs = yaml.safe_load((ROOT / ".github" / "workflows" / wf).read_text())
            declared = set(((inputs.get("on") or inputs.get(True) or {}).get("workflow_dispatch") or {}).get("inputs") or {})
            with self.subTest(workflow=wf):
                self.assertEqual(wf in grid.LABELLED, "label" in declared)

    def test_started_work_is_not_queued_again(self):
        queue = grid.rerun_queue()
        counts = {}
        for _, _, wf, _ in queue:
            counts[wf] = counts.get(wf, 0) + 1
        self.assertEqual(grid.reruns_to_start(queue, counts), [])

    def test_the_kind_rig_amendment_counts_only_runs_on_the_amended_rig(self):
        # 18 October: the served image pre-pulled on every kind worker (docs/POD_START_WAIT.md); a kind workflow's run counts
        # only when its own commit carries the pre-puller, every other workflow's as before, and an unreadable commit raises
        queue = grid.rerun_queue()
        workflows = {row[2] for row in queue}
        self.assertTrue(set(grid.RIG_WORKFLOWS) <= workflows)
        self.assertTrue((ROOT / grid.RIG_FILE).exists())
        for wf in grid.RIG_WORKFLOWS:
            self.assertRegex((ROOT / '.github' / 'workflows' / wf).read_text(), r'kind_paired\.sh|kind_bench\.sh', wf)
        for wf in workflows - set(grid.RIG_WORKFLOWS):  # no other workflow that runs the kind bench is left on two rigs
            text = (ROOT / '.github' / 'workflows' / wf).read_text()
            self.assertNotRegex(text, r'kind_paired\.sh|kind_bench\.sh', f'{wf} runs the kind bench: it must count by rig too')
        runs = [{'head_sha': 'old', 'conclusion': 'success'}, {'head_sha': 'new', 'conclusion': None},
                {'head_sha': 'new', 'conclusion': 'cancelled'}, {'head_sha': 'new2', 'conclusion': 'failure'}]
        asked = []

        def api(url, **_):
            asked.append(url)
            if '/contents/' in url:
                if url.endswith('ref=old') and grid.RIG_FILE in url:
                    raise RuntimeError('gh api ...: gh: Not Found (HTTP 404)')
                return {'name': 'file'}
            return {'workflow_runs': runs}
        with unittest.mock.patch.object(grid, 'api', side_effect=api):
            got = grid.reruns_started([('A', 'x', 'kind-addons.yml', {}), ('A', 'y', 'redis.yml', {})])
        self.assertEqual(got, {'kind-addons.yml': 2, 'redis.yml': 3})   # the old rig's run, and the cancelled one, count for nothing
        self.assertEqual(sum('/contents/' in u for u in asked), 6)        # each commit read once for the engine, once for the rig
        self.assertTrue(all(f'created=>={grid.RERUN_SINCE}' in u for u in asked if '/runs?' in u))

        def broken(url, **_):
            if '/contents/' in url:
                raise RuntimeError('gh api ...: connection reset')
            return {'workflow_runs': runs}
        with unittest.mock.patch.object(grid, 'api', side_effect=broken), self.assertRaises(RuntimeError):
            grid.reruns_started([('A', 'x', 'kind-addons.yml', {})])     # never counted on a rig it was not read on

    def test_a_run_counts_in_the_campaign_only_on_the_engine_that_stands(self):
        # 24 October: runs started after the campaign opened but before the engine reached main ran the engine before it
        self.assertTrue((ROOT / grid.ENGINE_FILE).exists(), grid.ENGINE_FILE)
        runs = [{'head_sha': 'before', 'conclusion': 'success'}, {'head_sha': 'after', 'conclusion': 'success'}]

        def api(url, **_):
            if '/contents/' in url:
                if url.endswith('ref=before') and grid.ENGINE_FILE in url:
                    raise RuntimeError('gh api ...: gh: Not Found (HTTP 404)')
                return {'name': 'file'}
            return {'workflow_runs': runs}
        with unittest.mock.patch.object(grid, 'api', side_effect=api):
            self.assertEqual(grid.reruns_started([('A', 'y', 'redis.yml', {}), ('A', 'x', 'kind-addons.yml', {})]),
                             {'redis.yml': 1, 'kind-addons.yml': 1})

    def test_nothing_starts_before_the_campaign_opens(self):
        # every count reads from SINCE: a run the new conductor started before it would be counted in no campaign
        self.assertRegex(grid.SINCE, r'^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$')
        self.assertEqual(grid.RERUN_SINCE, grid.SINCE)
        self.assertEqual(grid.AZURE_SINCE, grid.SINCE)
        self.assertFalse(grid.campaign_open('2000-01-01T00:00:00Z'))
        self.assertTrue(grid.campaign_open(grid.SINCE))
        self.assertTrue(grid.campaign_open('2999-01-01T00:00:00Z'))

    def test_the_engine_is_read_from_the_commit_the_runs_start_on(self):
        def fetched(d):                    # FETCH_HEAD as a fetch writes it (git 2.55 refuses update-ref on a pseudoref)
            sha = subprocess.run(['git', '-C', d, 'rev-parse', 'HEAD'], capture_output=True, text=True, check=True).stdout.strip()
            (Path(d) / '.git' / 'FETCH_HEAD').write_text(f"{sha}\t\tbranch 'main' of origin\n")
        # on GitHub each tick fetches the branch's newest commit; its engine, read by that commit's own version tool over the
        # tool's whole scope, decides. A tree with this checkout's engine (the late wires of omni-v15 among its files) reads
        # as the version tool reads it: the conductor's old copy of the scope left them out, read omni-v15 and omni-v16 as
        # unknown and started nothing (22 October)
        from tools import omni_version as V
        files = V.engine_files()
        want = V.version_of(files) or 'unknown'
        self.assertTrue(set(V.LATE_WIRES) <= set(files))
        prints = [p.name for p in V.VERSIONS.values() if p.exists()]
        with tempfile.TemporaryDirectory() as d:
            for n in [*files, 'tools/omni_version.py', *prints]:
                (Path(d) / n).parent.mkdir(parents=True, exist_ok=True)
                (Path(d) / n).write_bytes((ROOT / n).read_bytes())
            git = ['git', '-C', d, '-c', 'user.name=t', '-c', 'user.email=t@t', '-c', 'commit.gpgsign=false']
            subprocess.run(['git', 'init', '-q', d], check=True)
            subprocess.run(git + ['add', '-A'], check=True)
            subprocess.run(git + ['commit', '-q', '-m', 'x'], check=True)
            fetched(d)
            old = grid.ROOT
            try:
                grid.ROOT = Path(d)
                with unittest.mock.patch.dict(os.environ, {'GITHUB_ACTIONS': 'true'}):
                    self.assertEqual(grid.engine(), want)
                    if want != 'unknown':
                        # a tick that began before the engine landed: its own files hold an older version tool and no
                        # fingerprint of the newest engine, and the fetched commit is still read by its own
                        (Path(d) / 'tools' / 'omni_version.py').write_text('raise SystemExit(3)\n')
                        (Path(d) / f'OMNI_V{want[6:]}.json').unlink()
                        self.assertEqual(grid.engine(), want)
                        subprocess.run(git + ['checkout', '-q', '--', '.'], check=True)
                    (Path(d) / V.LATE_WIRES[0]).write_text('changed\n')
                    subprocess.run(git + ['commit', '-q', '-am', 'y'], check=True)
                    fetched(d)
                    self.assertEqual(grid.engine(), 'unknown')          # a commit no fingerprint matches starts nothing
            finally:
                grid.ROOT = old

    def test_a_conductor_that_failed_before_its_ticks_starts_no_successor(self):
        # 24 October: the receipt failed in seconds on omni-v18 and each failed conductor started the next, one every 15 s
        steps = yaml.safe_load((ROOT / '.github/workflows/grid.yml').read_text())['jobs']['tick']['steps']
        nxt = next(s for s in steps if s.get('name', '').startswith('The next conductor'))
        self.assertIn('success()', nxt['if'])
        self.assertNotIn('!cancelled()', nxt['if'])

    def test_six_stage_burst_is_the_workflow_and_queue_default(self):
        text = (ROOT / '.github/workflows/aks-metered-full.yml').read_text()
        w = yaml.safe_load(text)
        trigger = w.get('on', w.get(True))
        self.assertEqual(trigger['workflow_dispatch']['inputs']['load_steps']['default'], '1 4 1 6 1 9')
        azure = [r[3] for r in grid.rerun_queue() if r[2] == 'aks-metered-full.yml']
        self.assertTrue(all(r['load_steps'] == '1 4 1 6 1 9' for r in azure))

    def test_gpu_profiles_do_not_launch_or_claim_extra_physical_devices(self):
        d = json.loads((ROOT / 'scripts/gpu_campaign_profiles.json').read_text())
        self.assertFalse(d['launch'])
        self.assertEqual(d['profiles']['one-card']['physical_gpus'], 1)
        self.assertEqual(d['profiles']['eight-card']['physical_gpus'], 8)
        self.assertEqual(len(d['organisms']), 7)
        self.assertEqual(d['reported_run_prefixes'], [1, 10, 100])
        self.assertEqual(grid.SIZES, (1, 10, 100, 500))
        self.assertEqual(grid.RUNS, 500)
        for p in d['profiles'].values():
            self.assertEqual(p['environment']['HIL_SCALES'], '1,10,100')
            self.assertEqual(p['environment']['HIL_REPS_BY_SCALE'], '100,100,100')

    def test_gpu_prefixes_keep_missing_early_pairs_missing(self):
        from unittest.mock import patch
        from tools import run_hil
        with tempfile.TemporaryDirectory() as tmp:
            value = {part: {"primary": 0.0, "work": 0.0, "energy": 0.0, "viol_pp": 0.0, "p95": 0.0}
                     for part in ("sim", "card", "all")}
            with patch.object(run_hil, "contrast", return_value=value):
                run_hil.write_prefixes(tmp, {(1, "tower"): {1: {"native": {}, "omni": {}}}})
            rows = json.loads((Path(tmp) / "HIL_PREFIXES.json").read_text())
            self.assertTrue(all(r['paired_runs'] == 0 for r in rows if r['prefix'] == 1))
            self.assertTrue(all(r['paired_runs'] == 1 for r in rows if r['prefix'] in (10, 100)))
            self.assertFalse(any(r['complete'] for r in rows))

    def test_gpu_rejects_paid_oversize_before_hardware_access(self):
        from unittest.mock import patch
        from tools import run_hil
        with patch.object(run_hil, "limit", side_effect=AssertionError("hardware accessed")):
            for args in (["--scales", "1000"], ["--reps", "1000"]):
                with self.subTest(args=args), self.assertRaises(SystemExit) as cm:
                    run_hil.main(["--out", "/tmp/omni-paid-rejected", *args])
                self.assertEqual(cm.exception.code, 2)

    def test_jobs_held_by_a_runs_own_max_parallel_are_not_counted_as_queue(self):
        """A 100-repetition Azure set at max-parallel 1 lists 99 jobs queued that wait for its own slot, not for a runner;
        counted as queue they held every grid dispatch back. Only the slots its max-parallel leaves free count."""
        runs = {"workflow_runs": [{"id": 1, "path": ".github/workflows/aks-metered.yml", "name": "aks-metered",
                                   "display_title": "aks-metered"}]}
        jobs = {"jobs": [{"status": "in_progress"}] + [{"status": "queued"}] * 99}
        def api(url):
            if "/jobs" in url:                          # a full first page of 100, then the empty page GitHub returns
                return jobs if "page=1" in url.split("&") or url.endswith("page=1") else {"jobs": []}
            return runs if "status=queued" in url else {"workflow_runs": []}
        with unittest.mock.patch.object(grid, "api", side_effect=api), \
             unittest.mock.patch.object(grid, "waits_for_a_runner", return_value=False):
            queued, running, _ = grid.jobs_in_flight()
        self.assertEqual(grid.max_parallel(".github/workflows/aks-metered.yml"), 1)
        self.assertEqual((queued, running), (0, 1))

    def test_a_job_list_that_never_ends_stops_at_ten_pages(self):
        """A list that hands back a full page every time (a broken answer) once read forever and filled the memory; the
        reader stops at ten pages, more than the 256 jobs a run can hold."""
        runs = {"workflow_runs": [{"id": 2, "path": ".github/workflows/grid.yml", "name": "grid", "display_title": "grid"}]}
        calls = []
        def api(url):
            if "/jobs" in url:
                calls.append(url)
                return {"jobs": [{"status": "in_progress"}] * 100}
            return runs if "status=queued" in url else {"workflow_runs": []}
        with unittest.mock.patch.object(grid, "api", side_effect=api), \
             unittest.mock.patch.object(grid, "waits_for_a_runner", return_value=False):
            _, running, _ = grid.jobs_in_flight()
        self.assertEqual(len(calls), 10)
        self.assertEqual(running, 1000)


if __name__ == '__main__':
    unittest.main()
