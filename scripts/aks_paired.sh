#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# One paired repetition on a real, billed Azure Kubernetes Service cluster (.github/workflows/aks-metered.yml): every
# arm back to back, each on a fresh cluster built the same way, in an order rotated by repetition, the same as
# scripts/kind_paired.sh on kind. Each cluster:
#   system pool  1 machine, tainted CriticalAddonsOnly=true:NoSchedule (AKS's add-ons and the load generator; never
#                measured, never governed: kind's control plane)
#   work pool    agentpool=work, starts at AKS_MAX_NODES machines, under Azure's own cluster autoscaler (min 1, max
#                AKS_MAX_NODES), which deletes a machine once it is empty. Native: the autoscaler alone. Omni on top: the
#                same autoscaler, with Omni-Compass idling the machines it gives back, which the autoscaler then deletes
# The bill (scripts/kind_bench.sh, PLATFORM=aks) counts every work machine that exists, every 15 s. Each cluster is
# deleted when its arm ends, before the next is made, so nothing keeps billing and the subscription's core quota holds.
# Usage: REP=n ARMS="native compass" AZ_RG=... bash scripts/aks_paired.sh
set -euo pipefail
echo "Omni-Compass: evaluation and Simulation use only. Commercial use requires a signed, paid Omni-Compass Enterprise License (LICENSE, NOTICE)."
REP="${REP:?set REP}"; read -r -a arms <<< "${ARMS:-native compass}"
RG="${AZ_RG:?set AZ_RG}"; LOC="${AZ_LOCATION:-eastus}"; SIZE="${AKS_VM_SIZE:-Standard_D2s_v4}"
MAX="${AKS_MAX_NODES:-4}"
# The work pools: one or several, each its own machine family with its own ceiling ("size:max,size:max,..."). Several
# families are how a fleet gets past a subscription's per-family core allowance (10 vCPUs a family here, 200 in the
# region) and how real cloud fleets run anyway. Every pool carries the label omni-role=work (the worker selector), the
# first pool keeps one machine, the others may scale to zero; every pool starts full, Azure's autoscaler trims.
POOLS="${AKS_WORKER_POOLS:-$SIZE:$MAX}"
TOTAL=0; for p in ${POOLS//,/ }; do TOTAL=$(( TOTAL + ${p##*:} )); done
export AKS_MAX_NODES="$TOTAL" WORKER_SEL="omni-role=work"
PROFILE="${AKS_AUTOSCALER_PROFILE:-scale-down-unneeded-time=2m scale-down-delay-after-add=2m scan-interval=10s}"
k=${#arms[@]}; off=$(( (REP - 1) % k ))
order=( "${arms[@]:off}" "${arms[@]:0:off}" )
echo "repetition $REP, order: ${order[*]}, work pools $POOLS (up to $TOTAL workers) in $LOC"
# Reserve no resources until the complete fleet fits both family and regional CPU allowances.
# Aggregate repeated pool families; wait for confirmed cleanup rather than racing quota release.
wait_capacity() {
  python3 scripts/azure_capacity.py wait --location "$LOC" --system-size "$SIZE" --pools "$POOLS" \
    --timeout "${AZURE_CAPACITY_WAIT_S:-1800}"
}
wait_capacity
az group create -n "$RG" -l "$LOC" -o none
gone() { python3 scripts/azure_capacity.py cleanup-cluster --group "$RG" --name "$1"; }
for arm in "${order[@]}"; do
  name="omni-$arm-$REP"
  gone "$name"
  wait_capacity
  echo "######## creating $name"
  # shellcheck disable=SC2086
  # the control plane's tier (AKS_TIER): free, or standard (about $0.10 an hour a cluster, Azure's uptime SLA). Neither is in
  # the bill, which counts worker machines only; standard is the way past "creating a new cluster is unavailable at this
  # time in region", which Azure's free tier returned for hours on 2026-10-07 (docs/K8S_COMPASS_PREREGISTRATION.md, amendment 4)
  az aks create -g "$RG" -n "$name" -l "$LOC" --tier "${AKS_TIER:-free}" --node-count 1 --node-vm-size "$SIZE" \
    --nodepool-name system --nodepool-taints CriticalAddonsOnly=true:NoSchedule \
    --cluster-autoscaler-profile $PROFILE --generate-ssh-keys -o none
  i=0
  for p in ${POOLS//,/ }; do
    psize="${p%%:*}"; pmax="${p##*:}"; pmin=$([ "$i" = 0 ] && echo 1 || echo 0)
    az aks nodepool add -g "$RG" --cluster-name "$name" -n "work$i" --mode User --node-vm-size "$psize" --labels omni-role=work \
      --node-count "$pmax" --enable-cluster-autoscaler --min-count "$pmin" --max-count "$pmax" -o none   # AKS also labels its nodes agentpool=work$i
    i=$(( i + 1 ))
  done
  az aks get-credentials -g "$RG" -n "$name" --admin --overwrite-existing
  # azure/setup-kubectl's former default installed 1.31, which cannot address pods/resize.
  # Install the actual control-plane release, verify its official checksum, then check the wire.
  server_version=$(az aks show -g "$RG" -n "$name" --query currentKubernetesVersion -o tsv)
  client_bin="${RUNNER_TEMP:-/tmp}/omni-aks-kubectl"
  python3 scripts/aks_kubectl.py install --version "$server_version" --directory "$client_bin"
  export PATH="$client_bin:$PATH"
  python3 scripts/aks_kubectl.py check   # the full wiring on every cloud (the founder's order of 31 October): the resize wire checked
  # 24 October: in 3 of the steady set's first 9 repetitions the work machines did not read Ready within 600 s and the
  # repetition ended before any measurement. The nodes' own conditions and the pools' states are kept in the repetition's
  # files whenever the wait runs out, so the cause is read from the run, and the wait is given once more before it fails
  if ! kubectl wait --for=condition=Ready nodes --all --timeout=900s; then
    mkdir -p "bench-$arm-$REP"
    kubectl get nodes -o wide > "bench-$arm-$REP/nodes_not_ready.txt" 2>&1 || true
    kubectl describe nodes > "bench-$arm-$REP/nodes_describe.txt" 2>&1 || true
    kubectl get events -A --sort-by=.lastTimestamp > "bench-$arm-$REP/events.txt" 2>&1 || true
    az aks nodepool list -g "$RG" --cluster-name "$name" -o json > "bench-$arm-$REP/nodepools.json" 2>&1 || true
    echo "######## $name: a node not Ready after 900 s (its conditions kept in bench-$arm-$REP); one more wait of 600 s"
    kubectl wait --for=condition=Ready nodes --all --timeout=600s
  fi
  az aks show -g "$RG" -n "$name" -o json > "/tmp/aks-$name.json"
  echo "######## ARM $arm (repetition $REP)"
  mkdir -p "bench-$arm-$REP"; cp "/tmp/aks-$name.json" "bench-$arm-$REP/aks_cluster.json"
  if ! PLATFORM=aks ARM="$arm" OUT_DIR="bench-$arm-$REP" bash scripts/kind_bench.sh; then
    echo "ARM $arm (repetition $REP) FAILED its checks: marked invalid"
    [ -f "bench-$arm-$REP/INVALID" ] || echo "arm failed before its evidence finalizer" > "bench-$arm-$REP/INVALID"
    fail=1
  fi
  gone "$name"
done
exit "${fail:-0}"
