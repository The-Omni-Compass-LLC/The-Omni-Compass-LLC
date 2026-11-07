#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Wire the tested stdlib artifact bundler inline, including sparse and collect-only jobs."""
import json
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def wire(text, runtime):
    document = yaml.compose(text)
    data = yaml.safe_load(text)
    nodes = dict((k.value, v) for k, v in document.value)
    edits, count = [], 0
    lines = text.splitlines(True)
    starts = [0]
    for line in lines:
        starts.append(starts[-1] + len(line))
    for job_key, job_node in nodes['jobs'].value:
        steps = dict((k.value, v) for k, v in job_node.value).get('steps')
        if steps is None:
            continue
        for index, node in enumerate(steps.value):
            step = data['jobs'][job_key.value]['steps'][index]
            if not str(step.get('uses', '')).startswith('actions/upload-artifact'):
                continue
            values = step.get('with') or {}
            if values.get('name') == 'legal-notice' or 'omni_legal_export_' in str(values.get('path', '')):
                continue
            count += 1
            identifier = f'omni_legal_export_{count}'
            mapping = dict((k.value, v) for k, v in node.value)
            fields = dict((k.value, v) for k, v in mapping['with'].value)
            path = fields['path']
            line = node.start_mark.line
            indent = ' ' * lines[line].index('-')
            block = [indent + '- name: Attach README, licenses and disclosures to this artifact',
                     indent + '  id: ' + identifier]
            if 'if' in step:
                block += [indent + '  if: ' + json.dumps(str(step['if']))]
            block += [indent + '  env:', indent + '    OMNI_EXPORT_PATHS: |']
            block += [indent + '      ' + p for p in str(values['path']).splitlines()]
            block += [indent + '  shell: python', indent + '  run: |']
            block += [indent + '    ' + p for p in runtime.splitlines()]
            edits.append((starts[line], starts[line], '\n'.join(block) + '\n'))
            original = text[path.start_mark.index:path.end_mark.index]
            replacement = json.dumps('${{ steps.' + identifier + '.outputs.paths }}')
            if original.endswith('\n'):
                replacement += '\n'
            edits.append((path.start_mark.index, path.end_mark.index, replacement))
    for start, end, value in sorted(edits, reverse=True):
        text = text[:start] + value + text[end:]
    return text, count


if __name__ == '__main__':
    runtime = (ROOT / 'tools/artifact_legal.py').read_text()
    total = 0
    for path in sorted((ROOT / '.github/workflows').glob('*.yml')):
        result, count = wire(path.read_text(), runtime)
        if count:
            yaml.safe_load(result)
            path.write_text(result)
            total += count
    print(f'{total} artifact uploads wired with embedded legal bundles')
