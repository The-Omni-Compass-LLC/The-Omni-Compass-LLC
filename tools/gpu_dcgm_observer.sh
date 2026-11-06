#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# Passive DCGM observer for the GPU evidence harness. It never writes configuration.
# Numeric field IDs are recorded beside the local dcgmi catalogue so renamed display
# labels across DCGM releases do not destroy provenance.
set -euo pipefail
GPU="${1:-0}"
OUT="${2:?output file required}"
DELAY_MS="${3:-200}"
DCGMI="${DCGMI:-dcgmi}"
FIELDS="${DCGM_FIELDS:-112,150,155,156,160,164,203,240,241,243}"
{
  echo "# utc_start $(date -u +%Y-%m-%dT%H:%M:%S.%NZ)"
  echo "# gpu $GPU"
  echo "# delay_ms $DELAY_MS"
  echo "# field_ids $FIELDS"
  echo "# 112 clocks-event reasons; 150 GPU temp; 155 board power W; 156 total energy mJ; 160 requested limit W; 164 enforced limit W; 203 GPU util; 240 power-violation time; 241 thermal-violation time; 243 board-limit violation"
  echo "# local field catalogue follows"
  "$DCGMI" dmon --list 2>&1 || true
  echo "# samples"
} > "$OUT"
exec "$DCGMI" dmon --entity-id "gpu:$GPU" --field-id "$FIELDS" --delay "$DELAY_MS" >> "$OUT" 2>&1
