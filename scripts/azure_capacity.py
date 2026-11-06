#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Wait for benchmark CPU capacity and confirmed resource deletion; never export inventory."""
import argparse
import json
import re
import subprocess
import time


def az(*args):
    result = subprocess.run(['az', *args, '-o', 'json'], capture_output=True, text=True)
    if result.returncode:
        # Credentials, subscription IDs and unrelated infrastructure never enter the public report.
        raise RuntimeError('Azure operation failed; capacity or cleanup could not be confirmed')
    return json.loads(result.stdout) if result.stdout.strip() else None


def demand(system_size, pools, specs):
    """Count the system node once and aggregate every worker pool by Azure CPU family."""
    wanted = [(system_size, 1)]
    for pool in filter(None, pools.split(',')):
        size, count = pool.rsplit(':', 1)
        count = int(count)
        if count < 1:
            raise ValueError('worker pool ceilings must be positive')
        wanted.append((size, count))
    result = {}
    for size, count in wanted:
        family, cpus = specs[size]
        if not family or cpus < 1:
            raise ValueError('machine family or CPU count is unknown')
        result[family] = result.get(family, 0) + count * cpus
    return result


def has_capacity(required, usage):
    """Unknown or permanently insufficient allowances fail closed; occupied capacity can be waited out."""
    available = {x['name']['value'].lower(): (int(x['currentValue']), int(x['limit'])) for x in usage}
    needed = {}
    for family, count in required.items():
        needed[family.lower()] = needed.get(family.lower(), 0) + count
    needed['cores'] = sum(required.values())
    ready = True
    for family, count in needed.items():
        if family not in available or available[family][1] < count:
            raise RuntimeError('requested fleet exceeds a known Azure CPU allowance; no resources created')
        used, limit = available[family]
        ready &= limit - used >= count
    return ready


def machine_specs(location, system_size, pools):
    """{size: (family, vCPUs)} for every machine the fleet asks for; a size not offered to this subscription fails closed."""
    sizes = {system_size, *(p.rsplit(':', 1)[0] for p in filter(None, pools.split(',')))}
    specs = {}
    for size in sorted(sizes):
        rows = az('vm', 'list-skus', '-l', location, '--size', size, '--resource-type', 'virtualMachines')
        rows = [x for x in rows if x['name'].lower() == size.lower()]
        if len(rows) != 1 or rows[0].get('restrictions'):
            raise RuntimeError('requested machine is unavailable to this subscription; no resources created')
        row = rows[0]
        cpus = next((int(c['value']) for c in row['capabilities'] if c['name'] == 'vCPUs'), 0)
        specs[size] = row['family'], cpus
    return specs


def preflight(location, system_size, pools):
    """The $0 check's pre-flight (.github/workflows/cloud-check.yml, 22 October): the machine is offered to this
    subscription and every CPU allowance can hold the complete fleet. Capacity another run holds now is no refusal (each
    set waits for it itself), so nothing waits here and nothing is created."""
    required = demand(system_size, pools, machine_specs(location, system_size, pools))
    free_now = has_capacity(required, az('vm', 'list-usage', '-l', location))
    print('pre-flight: the machine is offered and every Azure CPU allowance holds the complete fleet'
          + ('' if free_now else ' (another run holds part of it now; a set waits its turn)')
          + '. pre-flight only: nothing built, nothing billed.', flush=True)


def wait_capacity(location, system_size, pools, timeout=1800, interval=20):
    required = demand(system_size, pools, machine_specs(location, system_size, pools))
    deadline = time.monotonic() + timeout
    while True:
        if has_capacity(required, az('vm', 'list-usage', '-l', location)):
            print('Azure CPU capacity confirmed for the complete requested fleet.', flush=True)
            return
        if time.monotonic() >= deadline:
            raise RuntimeError('Azure CPU capacity remained occupied; no resources created')
        print('Waiting for Azure CPU capacity; no resources allocated by this check.', flush=True)
        time.sleep(interval)


def cleanup(group, timeout=1800, interval=15):
    if not re.fullmatch(r'omni-(?:compass-(?:full|bench)-\d+-\d+|big-\d+-\d+)', group):
        raise ValueError('refusing cleanup outside an explicitly named benchmark resource group')
    if not az('group', 'exists', '-n', group):
        return
    az('group', 'delete', '-n', group, '--yes', '--no-wait')
    deadline = time.monotonic() + timeout
    while az('group', 'exists', '-n', group):
        if time.monotonic() >= deadline:
            raise RuntimeError('Azure benchmark deletion remains unconfirmed; cleanup failed')
        print('Waiting for Azure benchmark deletion to complete.', flush=True)
        time.sleep(interval)
    print('Azure benchmark resource deletion confirmed.', flush=True)


def cleanup_cluster(group, name):
    rows = az('aks', 'list', '-g', group)
    if any(x['name'] == name for x in rows):
        # Synchronous, and failure is not swallowed. The next arm must not inherit a live cluster.
        az('aks', 'delete', '-g', group, '-n', name, '--yes')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest='action', required=True)
    cap = sub.add_parser('wait')
    cap.add_argument('--location', required=True)
    cap.add_argument('--system-size', required=True)
    cap.add_argument('--pools', required=True)
    cap.add_argument('--timeout', type=int, default=1800)
    clean = sub.add_parser('cleanup')
    clean.add_argument('--group', required=True)
    clean.add_argument('--timeout', type=int, default=1800)
    cluster = sub.add_parser('cleanup-cluster')
    cluster.add_argument('--group', required=True)
    cluster.add_argument('--name', required=True)
    pre = sub.add_parser('preflight')
    pre.add_argument('--location', required=True)
    pre.add_argument('--system-size', required=True)
    pre.add_argument('--pools', required=True)
    a = ap.parse_args()
    if a.action == 'preflight':
        try:
            preflight(a.location, a.system_size, a.pools)
        except (RuntimeError, ValueError, KeyError) as e:
            print(f'pre-flight: {e}', flush=True)
            raise SystemExit(2)
    elif a.action == 'wait':
        wait_capacity(a.location, a.system_size, a.pools, a.timeout)
    elif a.action == 'cleanup':
        cleanup(a.group, a.timeout)
    else:
        cleanup_cluster(a.group, a.name)


if __name__ == '__main__':
    main()
