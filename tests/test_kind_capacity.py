# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Tests for the kind shared-host replica ceiling."""
from omni_controller.capacity import HostCpuSampler, bounded_replica_cap, kind_replica_ceiling


def test_host_saturation_blocks_scale_out():
    assert kind_replica_ceiling(4000, 0, 100, 40, 0.90) == 40


def test_kind_busy_host_blocks_scale_out_before_the_90_percent_reserve():
    # The v5 four-core run was already 80.4% busy before Omni added replicas.
    # A 10% reserve alone still allowed scale-out; the stricter guard holds.
    assert kind_replica_ceiling(4000, 0, 100, 10, 0.804) == 10


def test_kind_host_below_busy_guard_can_use_measured_headroom():
    assert kind_replica_ceiling(4000, 0, 100, 10, 0.60) == 22
    assert kind_replica_ceiling(4000, 0, 100, 10, 0.74) == 16


def test_measured_headroom_caps_scale_out_at_reserve():
    # 8 cores, 80% busy and 10% reserved leaves 800m: eight 100m replicas.
    assert kind_replica_ceiling(8000, 0, 100, 40, 0.80, max_busy_share=0.85) == 48


def test_request_capacity_remains_the_outer_ceiling():
    assert kind_replica_ceiling(4000, 2500, 100, 5, 0.20) == 14


def test_missing_or_invalid_host_sample_fails_closed():
    assert kind_replica_ceiling(4000, 0, 100, 40, None) == 40
    assert kind_replica_ceiling(4000, 0, 100, 40, 1.1) == 40


def test_rechecks_and_clamps_previously_raised_cap():
    assert bounded_replica_cap(40, 60, 42, 46) == 46


def test_cap_never_drops_below_running_replicas():
    assert bounded_replica_cap(40, 60, 48, 44) == 48


def test_missing_live_measurement_clamps_to_operator_cap_or_running_count():
    assert bounded_replica_cap(40, 60, 35, None) == 40
    assert bounded_replica_cap(40, 60, 45, None) == 45


def test_sampler_uses_busy_delta_and_idle_plus_iowait(tmp_path):
    stat = tmp_path / "stat"
    stat.write_text("cpu 100 0 100 700 100 0 0 0 0 0\n")
    sampler = HostCpuSampler(stat)
    assert sampler.sample() is None
    stat.write_text("cpu 120 0 120 740 120 0 0 0 0 0\n")
    assert sampler.sample() == 0.4


def test_sampler_resets_after_unreadable_sample(tmp_path):
    stat = tmp_path / "stat"
    sampler = HostCpuSampler(stat)
    assert sampler.sample() is None
    stat.write_text("cpu 100 0 100 700 100 0 0 0 0 0\n")
    assert sampler.sample() is None

def test_controller_uses_measured_host_share_for_kind_ceiling():
    from types import SimpleNamespace
    from omni_controller.controller import Controller

    node = {
        "metadata": {"name": "kind-worker"},
        "spec": {"providerID": "kind://docker/kind-worker"},
        "status": {
            "conditions": [{"type": "Ready", "status": "True"}],
            "allocatable": {"cpu": "4"},
        },
    }
    deployment = {
        "spec": {
            "template": {"spec": {"containers": [
                {"resources": {"requests": {"cpu": "100m"}}}
            ]}},
            "selector": {"matchLabels": {"app": "web"}},
        }
    }
    class StandinKube:
        def get(self, *args):
            if args[1] == "deployment":
                return deployment
            if args[1] == "nodes":
                return {"items": [node]}
            if args[1] == "pods":
                return {"items": []}
            raise AssertionError(args)

    ctl = Controller.__new__(Controller)
    ctl.k = StandinKube()
    ctl.host_cpu = SimpleNamespace(busy_share=0.60)
    hpa = {
        "metadata": {"namespace": "default"},
        "status": {"currentReplicas": 10},
        "spec": {"scaleTargetRef": {"kind": "Deployment", "name": "web"}},
    }
    assert ctl._live_ceiling(hpa) == 22
    ctl.host_cpu.busy_share = None
    assert ctl._live_ceiling(hpa) == 10


def test_controller_rechecks_an_already_raised_replica_cap():
    import json
    from types import SimpleNamespace
    from omni_controller.controller import Controller, RANGE_ANN

    class StandinKube:
        writes = []
        def write(self, command, why):
            self.writes.append((command, why))

    ctl = Controller.__new__(Controller)
    ctl.a = SimpleNamespace(replica_ceiling=-1)
    ctl.compass_law = SimpleNamespace(p=0.4, band=SimpleNamespace(center=0.3))
    ctl.k = StandinKube()
    ctl._app_demand = lambda h: 25.2
    ctl._live_ceiling = lambda h: 46
    hpa = {
        "metadata": {"namespace": "default", "annotations": {RANGE_ANN: "1,40"}},
        "spec": {"minReplicas": 1, "maxReplicas": 60,
                 "metrics": [{"type": "Resource", "resource": {"name": "cpu", "target": {"averageUtilization": 50}}}]},
        "status": {"currentReplicas": 42},
    }

    ctl._replica_room(hpa, "default", "web", 300, {"slo_clean": True}, {})

    assert ctl.k.writes
    patch = json.loads(ctl.k.writes[0][0][-1])
    assert patch["spec"]["maxReplicas"] == 46
