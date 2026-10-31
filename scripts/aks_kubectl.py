#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Match the AKS server's kubectl release and refuse a missing resize wire before measurement."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import urllib.request


def release(value):
    match = re.fullmatch(r'v?(1)\.(\d+)\.(\d+)', value)
    if not match:
        raise ValueError('expected a stable Kubernetes release, such as 1.36.4')
    return tuple(map(int, match.groups()))


def install(version, directory, fetch=None):
    parts = release(version)
    version = 'v' + '.'.join(map(str, parts))
    arch = {'x86_64': 'amd64', 'aarch64': 'arm64'}.get(platform.machine())
    if platform.system() != 'Linux' or arch is None:
        raise RuntimeError('benchmark kubectl installer supports Linux amd64/arm64 only')
    def download(url):
        with urllib.request.urlopen(url, timeout=120) as response:
            return response.read()
    fetch = fetch or download
    url = f'https://dl.k8s.io/release/{version}/bin/linux/{arch}/kubectl'
    expected = fetch(url + '.sha256').decode('ascii').strip().lower()
    if not re.fullmatch('[0-9a-f]{64}', expected):
        raise RuntimeError('official kubectl checksum is malformed')
    destination = Path(directory) / 'kubectl'
    if destination.is_file() and hashlib.sha256(destination.read_bytes()).hexdigest() == expected:
        return destination
    data = fetch(url)
    if hashlib.sha256(data).hexdigest() != expected:
        raise RuntimeError('kubectl checksum mismatch; installed client was not replaced')
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix('.download')
    temporary.write_bytes(data)
    temporary.chmod(0o755)
    os.replace(temporary, destination)
    return destination


def validate_versions(client, server, resize=True):
    client_version, server_version = release(client), release(server)
    if client_version[0] != server_version[0] or abs(client_version[1] - server_version[1]) > 1:
        raise RuntimeError('kubectl/server minor versions are outside supported skew')
    if resize and client_version < (1, 32, 0):
        raise RuntimeError('CPU resize requires kubectl 1.32 or newer')


def check(kubectl='kubectl', resize=True, runner=None):
    def run(args):
        return json.loads(subprocess.check_output([kubectl, *args], text=True))
    run = runner or run
    versions = run(['version', '-o', 'json'])
    client, server = versions['clientVersion']['gitVersion'], versions['serverVersion']['gitVersion']
    validate_versions(client, server, resize)
    if resize:
        resources = run(['get', '--raw', '/api/v1'])['resources']
        if not any(r['name'] == 'pods/resize' and 'patch' in r.get('verbs', []) for r in resources):
            raise RuntimeError('server does not advertise patch on pods/resize; refusing an unwired full-control run')
    return {'client': client, 'server': server, 'resize_required': resize}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    setup = sub.add_parser('install'); setup.add_argument('--version', required=True); setup.add_argument('--directory', required=True)
    sub.add_parser('check')   # the resize wire is always checked: every cloud runs the whole engine (the founder's order of 31 October)
    args = parser.parse_args()
    if args.command == 'install':
        print(install(args.version, args.directory))
    else:
        print(json.dumps(check()))


if __name__ == '__main__':
    main()
