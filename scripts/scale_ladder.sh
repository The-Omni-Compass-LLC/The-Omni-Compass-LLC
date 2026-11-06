#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# The six organisms up the ladder of runs and sizes, on every core of this machine (tools/run_scale.py). Each rung
# writes results/scale/r<runs>-x<scale>/SCALE.md and is packed at the end. Free GitHub allows 1/10/100/500 copies and runs. Use the grid conductor for the full ladder,
# which checks memory and time budgets; this local script retains its shorter default.
# Override: RUNGS="100:1 100:10".
set -euo pipefail
cd "$(dirname "$0")/.."
PY="${PYTHON:-python3}"
STAMP=$(date -u +%Y%m%dT%H%M%SZ)
RUNGS="${RUNGS:-100:1 100:10 100:100}"
DIRS=()
for r in $RUNGS; do
  runs=${r%%:*}; scale=${r##*:}
  echo "== $runs runs, ${scale}x size, all six organisms, native and Omni"
  $PY tools/run_scale.py --runs "$runs" --scale "$scale" --out "results/scale/r$runs-x$scale" | tail -9
  DIRS+=("results/scale/r$runs-x$scale")
done
tar czf "results/scale/omni-scale-$STAMP.tar.gz" "${DIRS[@]}"
echo "== send this one file back: results/scale/omni-scale-$STAMP.tar.gz"
