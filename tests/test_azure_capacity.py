# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Quota accounting and cleanup must not let sequential Azure arms overlap."""
import json
from pathlib import Path
import unittest
from unittest.mock import patch
from scripts import azure_capacity as cap


def usage(**values):
    return [{'name': {'value': k}, 'currentValue': v[0], 'limit': v[1]} for k, v in values.items()]


class AzureCapacity(unittest.TestCase):
    def test_shared_family_pools_and_system_are_added_once(self):
        specs = {'system': ('family', 2), 'work-a': ('family', 2), 'work-b': ('family', 4)}
        self.assertEqual(cap.demand('system', 'work-a:2,work-b:2', specs), {'family': 14})

    def test_standalone_vm_counts_one_machine_without_worker_pools(self):
        self.assertEqual(cap.demand('vm', '', {'vm': ('f', 8)}), {'f': 8})

    def test_pool_with_different_size_but_same_family_includes_system(self):
        self.assertEqual(cap.demand('system', 'workers:4', {'system': ('f', 2), 'workers': ('f', 2)}), {'f': 10})

    def test_occupied_family_waits_and_regional_limit_also_binds(self):
        self.assertFalse(cap.has_capacity({'f': 10}, usage(f=(8, 10), cores=(8, 200))))
        self.assertFalse(cap.has_capacity({'f': 10}, usage(f=(0, 10), cores=(195, 200))))
        self.assertTrue(cap.has_capacity({'f': 10}, usage(f=(0, 10), cores=(0, 200))))

    def test_unknown_or_permanently_insufficient_quota_is_not_treated_as_free(self):
        for rows in (usage(cores=(0, 200)), usage(f=(0, 8), cores=(0, 200))):
            with self.subTest(rows=rows), self.assertRaises(RuntimeError):
                cap.has_capacity({'f': 10}, rows)

    def test_capacity_wait_retries_without_allocating(self):
        sku = [{'name': 'worker', 'family': 'f', 'capabilities': [{'name': 'vCPUs', 'value': '2'}]}]
        with patch.object(cap, 'az', side_effect=[sku, usage(f=(8, 10), cores=(8, 200)),
                                                usage(f=(0, 10), cores=(0, 200))]) as az, patch.object(cap.time, 'sleep') as sleep:
            cap.wait_capacity('eastus', 'worker', 'worker:4')
            sleep.assert_called_once()
            self.assertEqual([c.args[:2] for c in az.call_args_list],
                             [('vm', 'list-skus'), ('vm', 'list-usage'), ('vm', 'list-usage')])

    def test_preflight_waits_for_nothing_and_fails_only_on_a_refusal(self):
        """The $0 check's pre-flight (cloud-check.yml): capacity another run holds now passes (a set waits its turn itself);
        an allowance that can never hold the fleet, or a machine not offered, fails closed; it prints no counter."""
        import contextlib
        import io
        sku = [{'name': 'worker', 'family': 'f', 'capabilities': [{'name': 'vCPUs', 'value': '2'}]}]
        for rows, note in ((usage(f=(0, 10), cores=(0, 200)), ''), (usage(f=(8, 10), cores=(8, 200)), 'another run holds')):
            out = io.StringIO()
            with self.subTest(note=note), patch.object(cap, 'az', side_effect=[sku, rows]), \
                    patch.object(cap.time, 'sleep') as sleep, contextlib.redirect_stdout(out):
                cap.preflight('eastus', 'worker', 'worker:4')
                sleep.assert_not_called()
            self.assertIn('nothing built, nothing billed', out.getvalue())
            self.assertIn(note, out.getvalue())
            self.assertFalse(any(ch.isdigit() for ch in out.getvalue()), out.getvalue())
        with patch.object(cap, 'az', side_effect=[sku, usage(f=(0, 8), cores=(0, 200))]), self.assertRaises(RuntimeError):
            cap.preflight('eastus', 'worker', 'worker:4')
        with patch.object(cap, 'az', side_effect=[[{**sku[0], 'restrictions': [{'type': 'Location'}]}]]), self.assertRaises(RuntimeError):
            cap.preflight('eastus', 'worker', 'worker:4')

    def test_cleanup_timeout_is_reported_as_a_failure(self):
        with patch.object(cap, 'az', side_effect=[True, None, True]), patch.object(cap.time, 'monotonic', side_effect=[0, 2]):
            with self.assertRaises(RuntimeError):
                cap.cleanup('omni-compass-full-123-1', timeout=1)

    def test_paid_suites_share_a_region_queue_and_wait_for_cleanup(self):
        import yaml
        root = Path(__file__).resolve().parents[1]
        groups = []
        for name in ('aks-metered.yml', 'aks-metered-full.yml', 'big-organism.yml'):
            text = (root / '.github/workflows' / name).read_text()
            workflow = yaml.safe_load(text)
            groups.append(workflow['concurrency']['group'])
            self.assertFalse(workflow['concurrency']['cancel-in-progress'])
            self.assertNotIn('az group delete -n', text)
            self.assertIn('azure_capacity.py cleanup', text)
        self.assertEqual(len(set(groups)), 1)

    def test_private_selection_exports_no_quota_or_candidate_status(self):
        import contextlib
        import io
        from scripts import restart_aks
        request = {'inputs': {'location': 'eastus', 'max_workers': '4'},
                   'vm_candidates': ['Standard_D2s_v4', 'Standard_D2s_v3'], 'max_price_per_node_hour': '0.096'}
        def probe(location, size, pools, timeout):
            print('private quota counters must never leave memory')
            if size.endswith('_v4'):
                raise RuntimeError('private quota unavailable')
        output = io.StringIO()
        with patch.object(cap, 'wait_capacity', side_effect=probe), patch.object(restart_aks, 'list_price', return_value=0.096):
            with contextlib.redirect_stdout(output):
                result = restart_aks.private_capacity_inputs(request)
        self.assertEqual(output.getvalue(), '')
        self.assertEqual(result['vm_size'], 'Standard_D2s_v3')
        self.assertEqual(result['price_per_node_hour'], '0.096')
        self.assertNotIn('quota', result)

    def test_private_selection_refuses_a_higher_price(self):
        from scripts import restart_aks
        request = {'inputs': {'location': 'eastus', 'max_workers': '4'},
                   'vm_candidates': ['Standard_D2s_v4'], 'max_price_per_node_hour': '0.096'}
        with patch.object(cap, 'wait_capacity'), patch.object(restart_aks, 'list_price', return_value=0.2):
            with self.assertRaises(RuntimeError):
                restart_aks.private_capacity_inputs(request)

    def test_retail_price_excludes_windows_and_spot(self):
        import io
        import json
        from scripts import restart_aks
        base = {'armSkuName': 'Standard_D2s_v3', 'armRegionName': 'eastus', 'serviceName': 'Virtual Machines',
                'type': 'Consumption', 'currencyCode': 'USD', 'unitOfMeasure': '1 Hour',
                'productName': 'Virtual Machines Dsv3 Series', 'skuName': 'D2s v3', 'retailPrice': 0.096}
        data = {'Items': [dict(base, skuName='D2s v3 Spot', retailPrice=0.01),
                          dict(base, productName='Virtual Machines Dsv3 Windows', retailPrice=0.18), base]}
        with patch.object(restart_aks.urllib.request, 'urlopen', return_value=io.BytesIO(json.dumps(data).encode())):
            self.assertEqual(restart_aks.list_price('Standard_D2s_v3', 'eastus'), 0.096)

    def test_free_repair_dispatch_rejects_cloud_before_any_mutation(self):
        from scripts import restart_aks
        with patch.object(restart_aks, 'gh_api') as api:
            with self.assertRaises(ValueError):
                restart_aks.dispatch_free_checks('repos/example/repo', [{'workflow': 'lambda-gpu.yml', 'inputs': {}}])
            api.assert_not_called()

    def test_free_repair_rejects_unknown_input_before_any_dispatch(self):
        from scripts import restart_aks
        items = [{'workflow': 'redis.yml', 'inputs': {'workloads': 'burst'}},
                 {'workflow': 'robustness.yml', 'inputs': {'arms': 'native compass'}}]
        with patch.object(restart_aks, 'gh_api') as api:
            with self.assertRaisesRegex(ValueError, 'unknown inputs.*arms'):
                restart_aks.dispatch_free_checks('repos/example/repo', items)
            api.assert_not_called()

    def test_current_repair_request_matches_real_workflow_contracts(self):
        from scripts import restart_aks
        import yaml
        root = Path(restart_aks.__file__).resolve().parents[1]
        request = json.loads((root / '.github/aks_restart_request.json').read_text())
        for item in request['free_dispatches']:
            workflow = yaml.load((root / '.github/workflows' / item['workflow']).read_text(), Loader=yaml.BaseLoader)
            self.assertFalse(set(item['inputs']) - set(workflow['on']['workflow_dispatch']['inputs']))

    def test_free_repair_dispatch_records_the_actual_run_reference(self):
        from scripts import restart_aks
        row = {'workflow': 'robustness.yml', 'inputs': {'scenario': 'kill', 'reps': '10'}}
        run = {'id': 123, 'head_branch': 'main', 'created_at': '2099-01-01T00:00:00Z',
               'html_url': 'https://github.com/example/repo/actions/runs/123', 'status': 'queued'}
        with patch.object(restart_aks, 'gh_api', side_effect=[None, {'workflow_runs': [run]}]) as api:
            receipt = restart_aks.dispatch_free_checks('repos/example/repo', [row])
        self.assertEqual(receipt[0]['id'], 123)
        self.assertEqual(api.call_args_list[0].args[1], 'POST')

    def test_cleanup_waits_for_resource_disappearance(self):
        with patch.object(cap, 'az', side_effect=[True, None, True, False]) as az, patch.object(cap.time, 'sleep') as sleep:
            cap.cleanup('omni-compass-full-123-1')
            self.assertEqual(az.call_count, 4)
            sleep.assert_called_once()

    def test_cleanup_missing_group_is_a_noop_and_failures_are_not_swallowed(self):
        with patch.object(cap, 'az', return_value=False) as az:
            cap.cleanup('omni-big-123-0')
            az.assert_called_once()
        with patch.object(cap, 'az', side_effect=RuntimeError('permission denied')), self.assertRaises(RuntimeError):
            cap.cleanup('omni-big-123-0')
        with self.assertRaises(ValueError):
            cap.cleanup('unrelated-production-group')

    def test_cluster_cleanup_deletes_only_the_named_existing_cluster(self):
        with patch.object(cap, 'az', side_effect=[[{'name': 'omni-native-1'}], None]) as az:
            cap.cleanup_cluster('omni-compass-full-123-1', 'omni-native-1')
            self.assertEqual(az.call_count, 2)
            self.assertNotIn('--no-wait', az.call_args.args)
        with patch.object(cap, 'az', return_value=[]) as az:
            cap.cleanup_cluster('omni-compass-full-123-1', 'absent')
            az.assert_called_once()


if __name__ == '__main__':
    unittest.main()
