#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Apply one explicitly requested AKS stop/cleanup/restart; never cancel unrelated runs."""
import contextlib
import datetime as dt
import io
import urllib.parse
import urllib.request
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def gh_api(path, method='GET', body=None):
    cmd = ['gh', 'api', path, '--method', method]
    if body is not None:
        cmd += ['--input', '-']
    r = subprocess.run(cmd, input=json.dumps(body) if body is not None else None,
                       text=True, capture_output=True)
    if r.returncode:
        raise RuntimeError(f'GitHub API {method} {path} failed: {r.stderr.strip()}')
    return json.loads(r.stdout) if r.stdout.strip() else None


def list_price(size, location):
    """Public Azure retail price only; never send subscription or resource metadata to this endpoint."""
    query = f"armRegionName eq '{location}' and armSkuName eq '{size}' and priceType eq 'Consumption'"
    url = 'https://prices.azure.com/api/retail/prices?' + urllib.parse.urlencode({'$filter': query, 'currencyCode': 'USD'})
    prices = []
    for _ in range(5):
        with urllib.request.urlopen(url, timeout=30) as response:
            data = json.load(response)
        for row in data.get('Items', []):
            if (row.get('armSkuName') == size and row.get('armRegionName') == location
                    and row.get('serviceName') == 'Virtual Machines' and row.get('type') == 'Consumption'
                    and row.get('currencyCode') == 'USD' and row.get('unitOfMeasure') == '1 Hour'
                    and row.get('isPrimaryMeterRegion', True)
                    and 'Windows' not in row.get('productName', '')
                    and not any(x in row.get('skuName', '') for x in ('Spot', 'Low Priority'))
                    and float(row.get('retailPrice', 0)) > 0):
                prices.append(float(row['retailPrice']))
        url = data.get('NextPageLink')
        if not url:
            break
    if not prices:
        raise RuntimeError('public list price could not be verified')
    return min(prices)


def private_capacity_inputs(request):
    # In-memory checks only. No quota counters, candidate readiness, group existence or inventory is exported.
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from scripts.azure_capacity import wait_capacity
    inputs = dict(request['inputs'])
    for size in request['vm_candidates']:
        try:
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                wait_capacity(inputs['location'], size, f"{size}:{inputs['max_workers']}", timeout=0)
                price = list_price(size, inputs['location'])
        except (RuntimeError, ValueError, OSError):
            continue
        if price > float(request['max_price_per_node_hour']):
            continue
        inputs.update(vm_size=size, price_per_node_hour=str(price))
        return inputs
    raise RuntimeError('no configured benchmark machine is currently available within the approved price ceiling')


def dispatch_free_checks(base, items):
    allowed = {'robustness.yml', 'redis.yml'}
    if any(item['workflow'] not in allowed for item in items):
        raise ValueError('repair checks may dispatch only the named free benchmark workflows')
    # Validate the entire request against the checked-out workflow contracts before dispatching any job.
    import yaml
    root = Path(__file__).resolve().parents[1]
    for item in items:
        workflow = yaml.load((root / '.github/workflows' / item['workflow']).read_text(), Loader=yaml.BaseLoader)
        declared = workflow['on']['workflow_dispatch'].get('inputs', {})
        unknown = set(item['inputs']) - set(declared)
        missing = {key for key, spec in declared.items()
                   if spec.get('required') == 'true' and 'default' not in spec and key not in item['inputs']}
        if unknown or missing:
            raise ValueError(f'{item["workflow"]}: unknown inputs {sorted(unknown)}; missing inputs {sorted(missing)}')
    receipt = []
    for item in items:
        started = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
        gh_api(f'{base}/actions/workflows/{item["workflow"]}/dispatches', 'POST',
               {'ref': 'main', 'inputs': item['inputs']})
        row = {**item, 'dispatch_accepted': True}
        for _ in range(6):
            data = gh_api(f'{base}/actions/workflows/{item["workflow"]}/runs?event=workflow_dispatch&per_page=10')
            matches = [r for r in data['workflow_runs'] if r['head_branch'] == 'main'
                       and dt.datetime.fromisoformat(r['created_at'].replace('Z', '+00:00')) >= started]
            if matches:
                run = max(matches, key=lambda r: r['id'])
                row.update(id=run['id'], url=run['html_url'], status=run['status'])
                break
            time.sleep(3)
        receipt.append(row)
    return receipt


def main(argv=None):
    request = json.loads(Path((argv or sys.argv[1:])[0]).read_text())
    repo = os.environ['GITHUB_REPOSITORY']
    base = f'repos/{repo}'
    receipt = {'request': request, 'cancelled': [], 'restart': None}
    out = Path('aks-restart-receipt.json')
    def save():
        out.write_text(json.dumps(receipt, indent=2) + '\n')
    save()
    if request.get('free_dispatches'):
        receipt['free_checks'] = dispatch_free_checks(base, request['free_dispatches'])
        save()
        print(json.dumps(receipt['free_checks']), flush=True)
        return 0
    # Cancel the obsolete pending run before freeing the active run's queue slot.
    for old in request['superseded_runs']:
        run = gh_api(f'{base}/actions/runs/{old["id"]}')
        if run['path'] != '.github/workflows/' + old['workflow'] or run['head_branch'] != 'main':
            raise RuntimeError('run identity did not match the explicit restart request')
        if run['status'] != 'completed':
            try:
                gh_api(f'{base}/actions/runs/{old["id"]}/cancel', 'POST')
            except subprocess.CalledProcessError:
                if gh_api(f'{base}/actions/runs/{old["id"]}')['status'] != 'completed':
                    raise
        receipt['cancelled'].append({'id': old['id'], 'previous_status': run['status']})
        save()
    # Give each cancelled job its normal always() cleanup before issuing the same bounded cleanup ourselves.
    deadline = time.monotonic() + 360
    while time.monotonic() < deadline:
        states = [gh_api(f'{base}/actions/runs/{x["id"]}')['status'] for x in request['superseded_runs']]
        if all(s == 'completed' for s in states):
            break
        time.sleep(10)
    else:
        raise RuntimeError('the cancelled runs have not finished cleanup; the new test was not started')
    groups = []
    for old in request['superseded_runs']:
        if old['workflow'] not in ('aks-metered.yml', 'aks-metered-full.yml'):
            raise ValueError('restart supports only the two named AKS benchmark workflows')
        prefix = 'omni-compass-bench-' if old['workflow'] == 'aks-metered.yml' else 'omni-compass-full-'
        for rep in range(1, old['reps'] + 1):
            group = f'{prefix}{old["id"]}-{rep}'
            exists = subprocess.check_output(['az', 'group', 'exists', '-n', group], text=True).strip()
            if exists == 'true':
                subprocess.run(['az', 'group', 'delete', '-n', group, '--yes', '--no-wait'], check=True, capture_output=True, text=True)
                groups.append(group)
    deadline = time.monotonic() + 900
    while groups and time.monotonic() < deadline:
        groups = [g for g in groups if subprocess.check_output(['az', 'group', 'exists', '-n', g], text=True).strip() == 'true']
        if groups:
            print('Waiting for superseded benchmark cleanup to complete.', flush=True)
            time.sleep(15)
    if groups:
        raise RuntimeError('Azure is still deleting the old resources; refusing a competing billed test')
    save()
    if request.get('private_capacity_dispatch'):
        request['inputs'] = private_capacity_inputs(request)
        save()
    started = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    gh_api(f'{base}/actions/workflows/aks-metered-full.yml/dispatches', 'POST',
           {'ref': 'main', 'inputs': request['inputs']})
    receipt['restart'] = {'dispatch_accepted': True, 'inputs': request['inputs']}
    for _ in range(12):
        d = gh_api(f'{base}/actions/workflows/aks-metered-full.yml/runs?event=workflow_dispatch&per_page=10')
        matches = [r for r in d['workflow_runs'] if dt.datetime.fromisoformat(r['created_at'].replace('Z', '+00:00')) >= started
                   and r['head_branch'] == 'main']
        if matches:
            r = max(matches, key=lambda x: x['id'])
            receipt['restart'].update({'id': r['id'], 'url': r['html_url'], 'status': r['status']})
            break
        time.sleep(3)
    save()
    summary = os.environ.get('GITHUB_STEP_SUMMARY')
    if summary:
        with open(summary, 'a') as f:
            f.write('\nSuperseded runs cancelled and their resource groups removed.\n\n')
            f.write('Replacement Azure run: ' + json.dumps(receipt['restart']) + '\n')
    print(json.dumps(receipt['restart']), flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
