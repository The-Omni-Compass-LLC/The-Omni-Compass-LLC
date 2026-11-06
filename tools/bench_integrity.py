#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Collect continuous pod events and reconcile benchmark-owned rollout cleanup."""
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
import subprocess
import time
from urllib.parse import urlencode

PAUSE = 'omnicompass.io/paused-by-omni'
# A watch request cut by the client (its own timeout on a loaded API server, a reset connection) is resumed at the last
# resourceVersion written: the server replays every event after it, so nothing is lost (run 40938221203, repetitions 360
# and 371: one client timeout each, 11 and 26 clean segments before it, and the arm was refused for it). RETRIES failed
# requests in a row fail the receipt.
# History the API server's watch cache no longer holds (410 Expired) is a gap: the cache began again at a later version
# (kind's one API server rebuilds it when its own watch of etcd breaks; on a managed cloud another API server may answer).
# 36 of 32,525 arms on the branch raw were refused for it (6 November 2026), 30 of them in the Azure long set (run
# 40940616527, native and Omni-Compass alike) and 6 on kind, Koordinator's runs among them (41806648201, 41810789445,
# 42173251769); in each the last version delivered was 1 to 321 versions older than the rebuilt cache. A gap is bridged
# only by a fresh LIST that proves it empty (bridge): every pod it lists at the very version this watch last delivered
# for it, none gone, none new. Any other gap fails the receipt, as every gap did before.
EXPIRED = ('Expired', 'too old resource version', '(410)', 'Gone')
RETRIES = 5
LIST = ['get', 'pods', '-n', 'default', '-l', 'run=php-apache', '-o', 'json', '--request-timeout=20s']
# A write refused by its resourceVersion precondition is read again and retried while the object is still ours: on a
# live cluster the HPA and the Deployment controller write the same object (run 40938221203, repetition 349: the reset's
# one patch lost that race and the arm was refused for it).
CONFLICT = ('the object has been modified', 'Conflict')


def read_events(text, errors=False):
    """The watch's events in order; an API error event raises, unless the caller judges it itself (errors=True)."""
    decoder = json.JSONDecoder()
    while text.strip():
        event, end = decoder.raw_decode(text.lstrip())
        if event.get('type') == 'ERROR' and not errors:
            raise ValueError('pod watch API error: ' + str(event.get('object')))
        yield event
        text = text.lstrip()[end:]


def expired(status):
    """True for the API server's 410 on a watch: its watch cache no longer holds the resourceVersion asked for."""
    status = status if isinstance(status, dict) else {}
    return status.get('code') == 410 or status.get('reason') in ('Expired', 'Gone')


def number(version):
    """A resourceVersion as the integer the API server's own watch cache compares (etcd's revision); None if not one."""
    try:
        return int(version)
    except (TypeError, ValueError):
        return None


def bridge(listing, last, live):
    """Whether a gap in the watch is empty, read from a fresh LIST against the last resourceVersion the watch delivered
    (`last`) and the version it last delivered for each pod it holds (`live`, uid -> resourceVersion).

    Empty means: the LIST is not older than `last`; every pod it lists is one the watch holds, at the very version the
    watch last delivered for it, so nothing wrote it since; and every pod the watch holds is listed, so none was deleted.
    Then no event of a watched pod falls in the gap, and the watch resumes at the LIST's version. Anything else, a version
    that is not a number included, may hide a transition, and the receipt fails.
    """
    meta = listing.get('metadata') or {}
    listed = {}
    for pod in listing.get('items') or []:
        pod_meta = pod.get('metadata') or {}
        listed[pod_meta.get('uid')] = pod_meta.get('resourceVersion')
    after, before = number(meta.get('resourceVersion')), number(last)
    written = sorted(str(uid) for uid, version in listed.items()
                     if uid not in live or number(version) is None or number(version) != number(live[uid]))
    gone = sorted(uid for uid in live if uid not in listed)
    return {'from_resource_version': last, 'to_resource_version': meta.get('resourceVersion'), 'pods_listed': len(listed),
            'pods_written': written, 'pods_gone': gone,
            'empty': None not in (after, before) and after >= before and not written and not gone}


def collect(directory, kubectl='kubectl', run=subprocess.run, popen=subprocess.Popen, sleep=time.sleep):
    """A LIST followed by watches at its resourceVersion; a new LIST only across a gap it proves empty.

    Every clean server timeout resumes the last event/bookmark's resourceVersion, and so does a request the client
    cut, its unfinished last line dropped (the resumed watch delivers that event again). History the watch cache no
    longer holds (410) is bridged by a fresh LIST only when that LIST proves the gap empty (bridge); each gap is written
    in the receipt. A gap that is not empty, malformed JSON, any other API error, and RETRIES failed requests (or more
    than RETRIES expired histories) in a row fail the receipt.
    A stop file drains the current bounded request before the collector exits.
    """
    directory = Path(directory)
    receipt = {'schema': 1, 'complete': False, 'started_at': time.time(), 'segments': 0, 'client_retries': 0}
    stop = directory / 'pod_watch.stop'
    err_path = directory / 'pod_watch.err'
    for name in ('pod_watch.ready', 'pod_watch_receipt.json'):
        (directory / name).unlink(missing_ok=True)
    live = {}                                   # every pod the watch holds: uid -> the last resourceVersion delivered

    def listing():
        return json.loads(run([kubectl] + LIST, check=True, capture_output=True, text=True).stdout)

    try:
        first = listing()
        version = first['metadata']['resourceVersion']
        with (directory / 'pod_watch.json').open('w') as output:
            def keep(event):
                output.write(json.dumps(event) + '\n')
                output.flush()
                meta = event['object']['metadata']
                if event.get('type') == 'DELETED':
                    live.pop(meta.get('uid'), None)
                elif meta.get('uid'):
                    live[meta['uid']] = meta.get('resourceVersion')
                return meta['resourceVersion']

            def bridged(last):
                for attempt in range(1, RETRIES + 1):
                    try:
                        fresh = listing()
                        break
                    except (subprocess.CalledProcessError, ValueError):
                        if attempt == RETRIES:
                            raise
                        receipt['client_retries'] += 1
                        sleep(1)
                gap = bridge(fresh, last, live)
                gap['at'] = time.time()
                receipt.setdefault('gaps', []).append(gap)
                if not gap['empty']:
                    raise RuntimeError('pod watch history expired across a change to a watched pod; '
                                       'see pod_watch_receipt.json')
                return fresh['metadata']['resourceVersion']

            for pod in first['items']:
                keep({'type': 'ADDED', 'object': pod})
            (directory / 'pod_watch.ready').touch()
            failures = refusals = 0
            with err_path.open('w') as errors:
                while not stop.exists():
                    query = urlencode({'watch': 'true', 'labelSelector': 'run=php-apache',
                                       'resourceVersion': version, 'allowWatchBookmarks': 'true',
                                       'timeoutSeconds': 30})
                    errors.flush()
                    before = err_path.stat().st_size
                    process = popen([kubectl, 'get', '--raw', '/api/v1/namespaces/default/pods?' + query,
                                     '--request-timeout=60s'], stdout=subprocess.PIPE, stderr=errors, text=True)
                    cut, refused, code = '', None, None
                    try:
                        for line in process.stdout:
                            if not line.strip():
                                continue
                            if not line.endswith('\n'):
                                cut = line          # the stream's last line, unfinished: judged once the exit is known
                                continue
                            for event in read_events(line, errors=True):
                                if event.get('type') == 'ERROR':
                                    refused = event.get('object') or {}
                                    break
                                version = keep(event)
                            if refused is not None:
                                break
                        if refused is None:
                            code = process.wait()
                    finally:
                        process.stdout.close()
                        if process.poll() is None:
                            process.terminate()
                            process.wait(timeout=5)
                    if refused is not None and not expired(refused):
                        raise ValueError('pod watch API error: ' + str(refused))
                    said = ''
                    if refused is None and code != 0:
                        said = err_path.read_bytes()[before:].decode(errors='replace') if err_path.exists() else ''
                    if refused is not None or any(word in said for word in EXPIRED):
                        refusals += 1
                        if refusals > RETRIES:
                            raise RuntimeError('pod watch history expired %d times in a row; see pod_watch_receipt.json'
                                               % refusals)
                        version = bridged(version)
                        continue
                    if code != 0:
                        failures += 1
                        receipt['client_retries'] += 1
                        if failures >= RETRIES:
                            raise RuntimeError('pod watch client failed %d times in a row; see pod_watch.err' % failures)
                        sleep(1)
                        continue
                    for event in read_events(cut):
                        version = keep(event)
                    failures = refusals = 0
                    receipt['segments'] += 1
                    receipt['last_resource_version'] = version
        receipt['complete'] = True
    except Exception as error:
        receipt['error'] = str(error)
        raise
    finally:
        receipt['ended_at'] = time.time()
        (directory / 'pod_watch_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')


def validate(directory):
    directory = Path(directory)
    receipt = json.loads((directory / 'pod_watch_receipt.json').read_text())
    start = float((directory / 'window_start.txt').read_text())
    end = float((directory / 'window_end.txt').read_text())
    if not receipt.get('complete') or not receipt.get('segments'):
        raise ValueError('pod watch did not complete: ' + str(receipt.get('error', 'no segment')))
    for gap in receipt.get('gaps') or []:
        if gap.get('empty') is not True or gap.get('pods_written') or gap.get('pods_gone'):
            raise ValueError('pod watch history expired across a change to a watched pod: ' + json.dumps(gap, sort_keys=True))
    if int(receipt['started_at']) > start or receipt['ended_at'] < end or end < start:
        raise ValueError('pod watch does not cover the measured window')
    observed = {}
    for event in read_events((directory / 'pod_watch.json').read_text()):
        pod = event.get('object', event)
        uid = pod.get('metadata', {}).get('uid')
        if uid:
            transitions = observed.setdefault(uid, set())
            for condition in (pod.get('status') or {}).get('conditions', []) or []:
                if condition.get('status') == 'True':
                    transitions.add((condition.get('type'), condition.get('lastTransitionTime')))
    final = json.loads((directory / 'pods_end.json').read_text())
    for pod in final['items']:
        uid = pod['metadata']['uid']
        created = dt.datetime.fromisoformat(pod['metadata']['creationTimestamp'].replace('Z', '+00:00')).timestamp()
        if created > end:
            continue
        if uid not in observed:
            raise ValueError('pod missing from watch: ' + uid)
        for condition in (pod.get('status') or {}).get('conditions', []) or []:
            stamp = condition.get('lastTransitionTime')
            if condition.get('type') not in ('Ready', 'PodScheduled') or condition.get('status') != 'True' or not stamp:
                continue
            when = dt.datetime.fromisoformat(stamp.replace('Z', '+00:00')).timestamp()
            if when <= end and (condition['type'], stamp) not in observed[uid]:
                raise ValueError('pod watch missed ' + condition['type'] + ' transition: ' + uid)
    return receipt


def restore_rollout(target, kubectl='kubectl', run=subprocess.run):
    """Reset only the rollout this benchmark owns; one atomic, idempotent patch.

    A resourceVersion precondition rejects concurrent changes; a rejected patch is
    read again, checked still ours, and retried (RETRIES times). An API/permission
    error propagates, and the reread must confirm both unpaused and unannotated.
    """
    namespace, name = target.split('/', 1)
    def get():
        return json.loads(run([kubectl, 'get', 'deployment', name, '-n', namespace, '-o', 'json',
                               '--request-timeout=20s'], check=True, capture_output=True, text=True).stdout)
    for attempt in range(1, RETRIES + 1):
        deployment = get()
        if (deployment['metadata'].get('annotations') or {}).get(PAUSE) != 'true':
            if attempt == 1:
                return False
            break                   # another writer cleared the mark between our read and our patch: verified below
        patch = {'metadata': {'resourceVersion': deployment['metadata']['resourceVersion'],
                              'annotations': {PAUSE: None}}, 'spec': {'paused': False}}
        try:
            run([kubectl, 'patch', 'deployment', name, '-n', namespace, '--type=merge', '-p', json.dumps(patch),
                 '--request-timeout=20s'], check=True, capture_output=True, text=True)
            break
        except subprocess.CalledProcessError as error:
            if attempt == RETRIES or not any(word in (error.stderr or '') for word in CONFLICT):
                raise
    restored = get()
    if restored['spec'].get('paused') or PAUSE in (restored['metadata'].get('annotations') or {}):
        raise ValueError('rollout reset did not restore the deployment')
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('collect', 'validate', 'restore-rollout'))
    parser.add_argument('target')
    parser.add_argument('--kubectl', default='kubectl')
    args = parser.parse_args()
    if args.action == 'collect':
        collect(args.target, args.kubectl)
    elif args.action == 'validate':
        print(json.dumps(validate(args.target)))
    else:
        print(json.dumps({'rollout_reset': restore_rollout(args.target, args.kubectl)}))


if __name__ == '__main__':
    main()
