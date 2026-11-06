#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
#
# The Kubernetes benchmark on a rented bare-metal machine with the processor's own meter, in one command
# (docs/METAL_KIT.md; docs/METER_PREREGISTRATION.md; register row 79). The same paired repetitions as GitHub's
# (scripts/kind_paired.sh: native, and Omni-Compass on top of native, each on a fresh six-worker kind cluster, the order
# rotated by repetition; the closed-loop load stepping 1 2 3 1 2 1; 120 s warm-up, 900 s measured), with the machine's
# own meter read every 2 s over every measured window (tools/rapl.py) and Kepler, the shared meter, read beside it
# (scripts/kind_addons_kepler.sh). Needs root (the meter), Linux on bare metal (a virtual machine has no meter),
# an x86-64 Intel or AMD processor, 8 cores and 32 GB of memory or more, Ubuntu or Debian (Docker, jq and curl are
# installed from its own packages if missing), and an internet connection.
#
#   sudo bash scripts/metal_kind_run.sh [reps=10] [duration_s=900]
#
# Writes metal-<time>/ with every repetition's raw files, the table (LIVE_REPS.md) and SHA256SUMS.txt, and packs it into
# the one file to send back: metal-<time>.tar.gz. Three such runs on one commit (A, B, C) make the three-run table:
#   python3 tools/confirm_abc.py "TITLE" <A> <B> <C> --out results/live/V5_METAL.md
set -euo pipefail
cd "$(dirname "$0")/.."
[ "$(id -u)" = 0 ] || { echo "run with sudo: the processor's meter needs root"; exit 2; }
REPS="${1:-10}"; DURATION="${2:-900}"
case "$REPS$DURATION" in *[!0-9]*) echo "reps and duration_s are whole numbers"; exit 2;; esac

echo "== the machine"
v=$(systemd-detect-virt 2>/dev/null || true); v="${v:-unknown}"
[ "$v" = none ] || [ "$v" = unknown ] || { echo "this machine is a virtual machine ($v): the kit needs bare metal, where the processor's meter is the machine's own"; exit 2; }
python3 tools/rapl.py probe || { echo "no processor meter here (no readable RAPL package zone): the kit needs bare metal"; exit 2; }
cores=$(nproc); mem=$(awk '/MemTotal/ {printf "%d", $2 / 1048576}' /proc/meminfo)
echo "cores $cores, memory ${mem} GB, $(grep -m1 'model name' /proc/cpuinfo | cut -d: -f2 | sed 's/^ *//')"
[ "$cores" -ge 8 ] && [ "$mem" -ge 30 ] || { echo "the six-worker cluster needs 8 cores and 32 GB or more"; exit 2; }

echo "== the tools"
need=""; for b in docker jq curl git; do command -v "$b" >/dev/null || need="$need $b"; done
python3 -m venv --help >/dev/null 2>&1 || need="$need python3-venv"
if [ -n "$need" ]; then
  command -v apt-get >/dev/null || { echo "missing:$need (install them, then run again)"; exit 2; }
  apt-get update -q && DEBIAN_FRONTEND=noninteractive apt-get install -y -q $(echo "$need" | sed 's/docker/docker.io/')
fi
systemctl start docker 2>/dev/null || true
docker info >/dev/null || { echo "Docker is not running"; exit 2; }
# kind and kubectl at the versions of every set (kind v0.31.0, Kubernetes v1.35.0), each SHA-256 checked against its
# publisher's
bash scripts/kind_install.sh v0.31.0 v1.35.0 /usr/local/bin
python3 -m venv .venv-metal
.venv-metal/bin/pip install -q -r requirements.txt
export PATH="$(pwd)/.venv-metal/bin:/usr/local/bin:$PATH"
# the kernel limits a six-worker kind cluster needs (inotify), as kind's own documentation gives them
sysctl -q -w fs.inotify.max_user_watches=524288 fs.inotify.max_user_instances=512

echo "== the engine"; python tools/omni_version.py
ls -d bench-*-* >/dev/null 2>&1 && { echo "folders of an earlier run (bench-*) are here: move them away first"; exit 2; }
out="metal-$(date -u +%Y%m%dT%H%M%SZ)"; mkdir -p "$out"
{ echo "commit=$(git rev-parse HEAD 2>/dev/null || echo unknown)"; echo "engine=$(python tools/omni_version.py | head -n 1)"
  echo "machine=$(grep -m1 'model name' /proc/cpuinfo | cut -d: -f2 | sed 's/^ *//') cores=$cores memory_gb=$mem virtualization=$v"
  echo "kernel=$(uname -r) reps=$REPS duration_s=$DURATION"; } > "$out/RUN.txt"
python3 tools/rapl.py probe > "$out/meter_probe.json" || true
echo "== the run: $REPS paired repetitions, $DURATION s measured each, writing $out/"
# each repetition runs from the repository's own folder, as on GitHub's machines, and its two arms' folders are moved
# into the run's folder as soon as it ends
for rep in $(seq 1 "$REPS"); do
  REP="$rep" ARMS="native compass" DURATION="$DURATION" CLOSURE=tuning/GLOBAL_LEAGUE_PREREGISTRATION.json LOADGEN=closed \
    METER=rapl KEPLER=1 bash scripts/kind_paired.sh 2>&1 | tee -a "$out/paired.log" || true
  for d in bench-*-"$rep"; do [ -d "$d" ] && mv "$d" "$out/"; done
done
python tools/live_reps.py "$out" || echo "no table (every repetition invalid?)" | tee -a "$out/paired.log"
cp README.md LICENSE NOTICE DISCLOSURES.md "$out/" 2>/dev/null || true
( cd "$out" && find . -type f ! -name SHA256SUMS.txt -print0 | sort -z | xargs -0 sha256sum > SHA256SUMS.txt )
tar -czf "$out.tar.gz" "$out"
if [ -n "${SUDO_UID:-}" ]; then chown -R "$SUDO_UID:${SUDO_GID:-$SUDO_UID}" "$out" "$out.tar.gz"; fi
echo "== send this one file back: $(pwd)/$out.tar.gz"
