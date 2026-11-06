#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Attach the exact legal bundle inside an artifact without changing its result-file layout."""
import glob
import hashlib
import json
import os
from pathlib import Path
import urllib.parse
import urllib.request
import uuid

BUNDLE = ('README.md', 'LICENSE', 'NOTICE', 'DISCLOSURES.md', 'PATENTS.md', 'TRADEMARKS.md')


def search_root(pattern, workspace):
    path = Path(os.path.expanduser(pattern))
    if not path.is_absolute():
        path = workspace / path
    prefix = Path(path.anchor)
    for part in path.parts[1:]:
        if glob.has_magic(part):
            return prefix
        prefix /= part
    return path if path.is_dir() or (not path.exists() and not path.suffix) else path.parent


def attach(paths, workspace, loader=None):
    workspace = Path(workspace).absolute()
    lines = [p.strip() for p in paths.splitlines() if p.strip()]
    roots = [search_root(p, workspace) for p in lines if not p.startswith('!')]
    if not roots:
        raise ValueError('artifact has no positive output path')
    root = Path(os.path.commonpath([str(p) for p in roots]))
    if root == Path(root.anchor):
        raise ValueError('refusing to write an export bundle at a filesystem root')
    legal = root / '_omni_legal'
    legal.mkdir(parents=True, exist_ok=True)
    hashes = {}
    for name in BUNDLE:
        source = workspace / name
        data = source.read_bytes() if source.is_file() else loader(name) if loader else None
        if data is None:
            raise FileNotFoundError('required export legal file is unavailable: ' + name)
        target = legal / name
        target.write_bytes(data)
        hashes[name] = hashlib.sha256(data).hexdigest()
    (legal / 'SHA256SUMS.json').write_text(json.dumps(hashes, indent=2) + '\n')
    return '\n'.join([*lines, *(str(legal / n) for n in (*BUNDLE, 'SHA256SUMS.json'))])


def main():
    workspace = Path(os.environ.get('GITHUB_WORKSPACE', '.')).absolute()
    def public_source(name):
        # Collect-only jobs may not check out source. Fetch only these public legal files, pinned to the run commit.
        repo, sha = os.environ['GITHUB_REPOSITORY'], os.environ['GITHUB_SHA']
        url = f'https://raw.githubusercontent.com/{repo}/{sha}/{urllib.parse.quote(name)}'
        with urllib.request.urlopen(url, timeout=30) as response:
            return response.read()
    paths = attach(os.environ['OMNI_EXPORT_PATHS'], workspace, public_source)
    delimiter = 'OMNI_LEGAL_' + uuid.uuid4().hex
    with open(os.environ['GITHUB_OUTPUT'], 'a') as out:
        out.write('paths<<' + delimiter + '\n' + paths + '\n' + delimiter + '\n')


if __name__ == '__main__':
    main()
