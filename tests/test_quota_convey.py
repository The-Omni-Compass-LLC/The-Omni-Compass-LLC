# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Quota is an input to conveyance, never a quota increase or an invented CPU gain."""
import copy
import json
from types import SimpleNamespace
import unittest
from unittest.mock import Mock
from omni_controller.muscles import Muscles
from omni_controller.quota import CpuLimitBudget, cpu_milli, matches


def quota(hard='1500m', used='1500m', **spec):
    return {'metadata': {'name': 'operator-budget'}, 'spec': {'hard': {'limits.cpu': hard}, **spec},
            'status': {'hard': {'limits.cpu': hard}, 'used': {'limits.cpu': used}}}


def pod(name='web', priority='served'):
    return {'metadata': {'name': name, 'namespace': 'default', 'labels': {'app': 'web'}},
            'spec': {'nodeName': 'worker', 'priorityClassName': priority,
                     'containers': [{'resources': {'limits': {'cpu': '500m'}, 'requests': {'cpu': '200m'}}}]},
            'status': {'phase': 'Running'}}


class Cluster:
    def __init__(self, quotas, pods=None, reject=False):
        self.quotas, self.pods, self.reject, self.writes = quotas, pods or [pod()], reject, []

    def get(self, *args):
        if args[1] == 'resourcequota':
            return {'items': copy.deepcopy(self.quotas)}
        if args[1] == 'nodes':
            return {'items': [{'metadata': {'name': 'worker'}, 'status': {'allocatable': {'cpu': '4'}}}]}
        if args[1] == 'pods':
            return {'items': copy.deepcopy(self.pods)}
        if args[1] == 'deployment':
            return {'metadata': {'annotations': {}}, 'spec': {'selector': {'matchLabels': {'app': 'web'}},
                    'template': {'spec': {'containers': [{'resources': {'limits': {'cpu': '500m'}}}]}}}}
        raise AssertionError(args)

    def write(self, args, why):
        self.writes.append(args)
        if args[0] == 'patch':
            if self.reject:
                raise RuntimeError('admission changed concurrently')
            target = next(p for p in self.pods if p['metadata']['name'] == args[2])
            target['spec']['containers'][0]['resources']['limits']['cpu'] = json.loads(args[-1])[0]['value']


class QuotaConvey(unittest.TestCase):
    def convey(self, cluster):
        events = []
        m = Muscles(cluster, SimpleNamespace(cap_deployments='default/web', cap_min_change_m=10), events.append)
        m._convey_engaged = lambda: True
        return m, m.convey(), events

    def test_exact_failed_case_full_quota_leaves_native_and_gain_one(self):
        c = Cluster([quota()])
        m, result, events = self.convey(c)
        self.assertEqual(result, {})
        self.assertEqual(m.gain[('default', 'web')], 1)
        self.assertFalse(any(w[0] == 'patch' for w in c.writes))
        self.assertTrue(any(e.get('quota') == 'CPU limit expansion bounded' for e in events))

    def test_one_allowance_shared_across_pods_without_double_spend(self):
        c = Cluster([quota(used='1000m')], [pod('one'), pod('two')])
        m, result, _ = self.convey(c)
        self.assertEqual(result, {'default/one': 1000})
        self.assertEqual(m.gain[('default', 'web')], 1.5)
        self.assertEqual(c.quotas[0]['spec']['hard']['limits.cpu'], '1500m')

    def test_multiple_quotas_use_smallest_headroom(self):
        b = CpuLimitBudget(Cluster([quota(used='1'), quota(hard='1.2', used='1')]), lambda e: None)
        value, entries = b.limit('default', pod(), 500, 3800)
        self.assertEqual(value, 700)
        self.assertEqual(len(entries), 2)

    def test_priority_class_scopes_match_the_pod_not_a_hardwired_name(self):
        q = quota(scopeSelector={'matchExpressions': [{'scopeName': 'PriorityClass', 'operator': 'In', 'values': ['served']}]})
        self.assertTrue(matches(q, pod()))
        self.assertFalse(matches(q, pod(priority='other')))
        m, result, _ = self.convey(Cluster([q], [pod(priority='other')]))
        self.assertEqual(result, {'default/web': 3800})

    def test_unknown_scope_or_status_block_only_expansion(self):
        q = quota(); q.pop('status')
        for quotas in ([q], [quota(scopes=['NotTerminating'])]):
            b = CpuLimitBudget(Cluster(quotas), lambda e: None)
            self.assertEqual(b.limit('default', pod(), 500, 3800)[0], 500)
            self.assertEqual(b.limit('default', pod(), 500, 400)[0], 400)

    def test_an_unreadable_quota_is_no_budget_known(self):
        """The role cannot list quotas (every kind test; the first v7 trial, run 38825214203, read this as a zero budget and
        never raised a limit): the raise proceeds as on omni-v6, Kubernetes admission is the authority, the audit says so
        once a pass (docs/OMNI_V7.md, section 1)."""
        kube = Mock(); kube.get.side_effect = PermissionError('forbidden')
        events = []
        b = CpuLimitBudget(kube, events.append)
        self.assertEqual(b.limit('default', pod(), 500, 3800)[0], 3800)
        self.assertEqual(b.limit('default', pod(), 500, 3800)[0], 3800)
        self.assertEqual(b.limit('default', pod(), 500, 400)[0], 400)
        self.assertEqual(len(events), 1)
        self.assertIn('no budget known', events[0]['quota'])
        self.assertIn('quota read unavailable: PermissionError', events[0]['reason'])

    def test_rejected_resize_does_not_report_phantom_gain(self):
        c = Cluster([], reject=True)
        m, result, events = self.convey(c)
        self.assertEqual(result, {})
        self.assertEqual(m.gain[('default', 'web')], 1)
        self.assertTrue(any('error' in e for e in events))

    def test_no_quota_retains_original_convey_arithmetic(self):
        m, result, _ = self.convey(Cluster([]))
        self.assertEqual(result, {'default/web': 3800})
        self.assertEqual(m.gain[('default', 'web')], 7.6)

    def test_cpu_quantities_and_spec_status_change(self):
        self.assertEqual(cpu_milli('1.5'), 1500)
        self.assertEqual(cpu_milli('1e-3'), 1)
        self.assertEqual(cpu_milli('1000000n'), 1)
        for value in ('NaN', '-1', 'bad'):
            with self.assertRaises(ValueError):
                cpu_milli(value)
        q = quota(hard='2', used='1'); q['spec']['hard']['limits.cpu'] = '1.1'
        b = CpuLimitBudget(Cluster([q]), lambda e: None)
        self.assertEqual(b.limit('default', pod(), 500, 3800)[0], 600)


if __name__ == '__main__':
    unittest.main()
