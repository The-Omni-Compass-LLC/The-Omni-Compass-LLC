#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
#
# The CPU power benchmark on this machine, in one command (docs/CPU_POWER_PREREGISTRATION.md): the kernel's own frequency
# governor as native, Omni-Compass on the frequency ceiling on top, energy from the processor's own meter. Needs root (the
# ceiling and the meter), Linux on the metal (not a virtual machine), Python 3.10 or later.
#
#   sudo bash scripts/cpu_power_run.sh [workloads=all] [reps=3] [step_s=60] [objective=resource]
#   sudo WALL_METER=shelly2:192.168.1.50 bash scripts/cpu_power_run.sh        # with a smart plug on the whole machine
#
# Writes cpu-power-<time>/ with every raw file, CPU_POWER.md and SHA256SUMS.txt. Three such runs (A, B, C) make the table:
#   python3 tools/cpu_power_abc.py <A> <B> <C> --out V3_CPU_POWER.md
set -euo pipefail
cd "$(dirname "$0")/.."
if [ "$(id -u)" != 0 ]; then echo "run with sudo: the frequency ceiling and the energy meter need root"; exit 2; fi
PY=${PY:-python3}
echo "== the engine"; $PY tools/omni_version.py
echo "== the machine"; $PY tools/run_cpu_power.py --probe
out="cpu-power-$(date -u +%Y%m%dT%H%M%SZ)"
echo "== the run: workloads ${1:-all}, ${2:-3} paired repetitions, ${3:-60} s a step, the verdict's objective ${4:-resource}; writing $out/"
$PY tools/run_cpu_power.py --workloads "${1:-all}" --reps "${2:-3}" --step-s "${3:-60}" --objective "${4:-resource}" --out "$out" 2>&1 | tee "$out.log"
mv "$out.log" "$out/run.log"
( cd "$out" && find . -type f -print0 | sort -z | xargs -0 sha256sum > SHA256SUMS.txt )
if [ -n "${SUDO_UID:-}" ]; then chown -R "$SUDO_UID:${SUDO_GID:-$SUDO_UID}" "$out"; fi
echo "== done: $out/CPU_POWER.md (every raw file beside it, SHA-256 sums in SHA256SUMS.txt)"
echo "   Zip the folder and add it to the repository under results/live/raw/; three runs make the table with tools/cpu_power_abc.py."
