#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# Paired live repetition: every arm runs back to back on the SAME runner (same CPUs, same host, same noise), each on a
# fresh kind cluster, in an order rotated by repetition so no arm always runs first or last. Differences between arms in
# one repetition are then differences between arms, not between machines (separate runners differ by about 15% in
# p95 on their own).
# Usage: REP=n ARMS="native omni" bash scripts/kind_paired.sh   (Omni governs the muscles it is given: native vs Omni on top)
set -euo pipefail
echo "Omni-Compass: evaluation and Simulation use only. Commercial use requires a signed, paid Omni-Compass Enterprise License (LICENSE, NOTICE)."
REP="${REP:?set REP}"; read -r -a arms <<< "${ARMS:-native omni}"
[ -z "${LOAD_STEPS_IN:-}" ] || export LOAD_STEPS="$LOAD_STEPS_IN"   # the capacity test's rising steps (benchmark-reps input)
# the window from a measured step (protocol 3, 13 Oct): with the organism inside, the heavier arm (the model with
# Omni-Compass's math for every modelled muscle) is timed on the core it will run on (scripts/kind_bench.sh), before
# either arm, and the window is lengthened, never shortened, so that arm makes its slowest step in time with a quarter
# to spare. Both arms use the one window; the measurement is written into each arm's preflight
if [ -n "${ORGANISM:-}" ] && [ "${PLATFORM:-kind}" = kind ]; then
  ncpu=$(nproc); pin=""
  [ "$ncpu" -ge 2 ] && command -v taskset >/dev/null 2>&1 && pin="taskset -c $((ncpu - 1))"
  CALIBRATION=$($pin python tools/run_kil.py --organism "$ORGANISM" --arm compass --duration "${DURATION:-1200}" \
                --out "calibration-$REP" --scale "${ORGANISM_SCALE:-1}" --calibrate "${CALIBRATE_STEPS:-6}" | tail -1)
  need=$(python3 -c 'import json, math, sys
c = json.loads(sys.argv[1]); print(int(math.ceil(c["steps_in_window"] * c["step_s_max"] * 1.25 / 60.0) * 60))' "$CALIBRATION")
  echo "calibration: $CALIBRATION; window needed ${need} s, given ${DURATION:-1200} s"
  if [ "$need" -gt "${DURATION:-1200}" ]; then export DURATION="$need"; fi
  export CALIBRATION
fi
# the cluster of every kind set; Koordinator's test alone runs the kubelet's cgroup root at /, as Koordinator's own kind
# configuration sets it, in both arms (deploy/kind/cluster-koordinator.yaml; docs/BATCH_QUEUE_PREREGISTRATION.md, amendment 4)
cluster=deploy/kind/cluster-full.yaml
[ "${BATCH_QUEUE:-}" = koordinator ] && cluster=deploy/kind/cluster-koordinator.yaml
echo "kind cluster configuration: $cluster"
k=${#arms[@]}; off=$(( (REP - 1) % k ))
order=( "${arms[@]:off}" "${arms[@]:0:off}" )
echo "repetition $REP, order: ${order[*]}"
for arm in "${order[@]}"; do
  # a fresh cluster for every arm; a creation that fails (the node image refused by its registry, a control plane not
  # Ready in time) is cleared and tried again, twice, before the job gives up
  for t in 1 2 3; do
    kind delete cluster --name omni-bench >/dev/null 2>&1 || true
    kind create cluster --name omni-bench --config "$cluster" ${KIND_NODE_IMAGE:+--image "$KIND_NODE_IMAGE"} --wait 120s && break
    [ "$t" = 3 ] && { echo "the kind cluster could not be created (3 tries)"; exit 1; }
    echo "kind cluster not created (try $t): trying again in 30 s"; sleep 30
  done
  echo "######## ARM $arm (repetition $REP)"
  mkdir -p "bench-$arm-$REP" && echo "$cluster${KIND_NODE_IMAGE:+ image=$KIND_NODE_IMAGE}" > "bench-$arm-$REP/kind_cluster.txt"
  # the four ways (docs/BATCH_QUEUE_PREREGISTRATION.md, amendment 6): an arm named ...bare runs on the organism alone, no
  # orchestrator installed (on the batch rig the stream placed by the cluster's own default scheduler, on the serving rig the
  # service's HPA as Kubernetes ships it, no add-on: docs/CRANE_PREREGISTRATION.md), native (nativebare) or with
  # Omni-Compass on top (compassbare); the same cluster as the orchestrator's arms, in the same repetition
  base="${arm%bare}"; queue="${BATCH_QUEUE:-}"; addons="${ADDONS:-}"; cruise="${CRUISEKUBE:-}"
  if [ "$base" != "$arm" ]; then [ -z "$queue" ] || queue=vanilla; addons=""; cruise=""; fi
  # the decision pace (docs/PACE_PREREGISTRATION.md): an arm named compassN (compass5, compass15, compass30, compass75, compass90,
  # compass120) is the compass arm deciding every N s, its fast checks every 5 s as always; compass alone decides at the main
  # engine's default, every 60 s (omni-v17)
  pace=""
  if [[ "$base" =~ ^compass([0-9]+)$ ]]; then pace="${BASH_REMATCH[1]}"; base=compass; fi
  if ! OMNI_INTERVAL="${pace:-${OMNI_INTERVAL:-60}}" ARM="$base" BATCH_QUEUE="$queue" ADDONS="$addons" CRUISEKUBE="$cruise" OUT_DIR="bench-$arm-$REP" bash scripts/kind_bench.sh; then
    # a run that fails its own checks is recorded as invalid and left out of the table, never silently counted
    echo "ARM $arm (repetition $REP) FAILED its checks: marked invalid"
    [ -f "bench-$arm-$REP/INVALID" ] || echo "arm failed before its evidence finalizer" > "bench-$arm-$REP/INVALID"
    fail=1
  fi
done
kind delete cluster --name omni-bench >/dev/null 2>&1 || true
exit "${fail:-0}"
