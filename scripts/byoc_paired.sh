#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# One paired repetition on a managed Kubernetes cluster the tester built and handed over (.github/workflows/byoc-metered.yml):
# Oracle (OKE), DigitalOcean (DOKS), Alibaba (ACK), Linode (LKE), IBM (IKS) or any conformant cluster, the same design as the
# Azure, Google and Amazon runs (scripts/aks_paired.sh, gke_paired.sh, eks_paired.sh) on a cluster the provider's own console
# made instead of its command line. The cluster must have (docs/BYOC_SETUP.md):
#   system pool  1 machine labelled omni-role=system and tainted CriticalAddonsOnly=true:NoSchedule (the provider's add-ons
#                and the load generator; never measured, never governed)
#   work pool    machines labelled omni-role=work and agentpool=work0, under the provider's own cluster autoscaler (min 1,
#                max BYOC_MAX_NODES), which deletes a machine once it is empty
# Every arm runs on that one cluster, back to back, in an order rotated by repetition; before each arm the work pool is
# waited for until it stands at its start size, every work machine Ready (by default the autoscaler's own minimum, one
# machine: the provider's autoscaler removes the machines the arm before emptied, and this script has no cloud command to add
# or remove one), so each arm starts from the same machines. The measuring is scripts/kind_bench.sh in its managed-cluster mode (kubectl only,
# the probe through the cloud's load balancer, the load generator on the system machine, the work machines counted every
# 15 s by their agentpool label); the bill is that count times BYOC_PRICE_PER_NODE_HOUR, the provider's list price for one
# work machine, written beside the run. The tester deletes the cluster when the set ends; this script builds and deletes
# nothing, so it never bills more than the cluster the tester made.
# Written to the same design and not yet run on any of these clouds: its first repetition is a shakedown, and any arm that
# fails its own checks is marked INVALID and never counted.
# Usage: REP=n ARMS="native compass" CLOUD=oracle|digitalocean|alibaba|linode|ibm|other KUBECONFIG=... \
#        [BYOC_MAX_NODES=4 BYOC_START_NODES=1 BYOC_PRICE_PER_NODE_HOUR=0.0 RUN_ID=...] bash scripts/byoc_paired.sh
set -euo pipefail
echo "Omni-Compass: evaluation and Simulation use only. Commercial use requires a signed, paid Omni-Compass Enterprise License (LICENSE, NOTICE)."
REP="${REP:?set REP}"; read -r -a arms <<< "${ARMS:-native compass}"
CLOUD="${CLOUD:?set CLOUD}"; MAX="${BYOC_MAX_NODES:-4}"; START="${BYOC_START_NODES:-1}"; PRICE="${BYOC_PRICE_PER_NODE_HOUR:-0}"
: "${KUBECONFIG:?set KUBECONFIG to the kubeconfig file of the cluster}"
export AKS_MAX_NODES="$MAX" WORKER_SEL="omni-role=work"          # kind_bench.sh's managed-cluster mode reads these names
k=${#arms[@]}; off=$(( (REP - 1) % k ))
order=( "${arms[@]:off}" "${arms[@]:0:off}" )
echo "repetition $REP on $CLOUD, order: ${order[*]}, work pool up to $MAX machines, starting at $START"
# Pre-flight, before anything is measured: the cluster answers, it carries exactly one system machine with its taint and a
# work pool under its own label, and the pool can reach its start size. One refusal ends the repetition here, with what is
# missing named. PREFLIGHT_ONLY=1 (.github/workflows/cloud-check.yml) stops after it.
kubectl version --request-timeout=30s >/dev/null || { echo "pre-flight: the cluster did not answer with this kubeconfig: nothing measured"; exit 2; }
sys_n=$(kubectl get nodes -l omni-role=system --no-headers 2>/dev/null | wc -l)
taint=$(kubectl get nodes -l omni-role=system -o jsonpath='{range .items[*]}{.spec.taints[*].key}{"\n"}{end}' 2>/dev/null | grep -c CriticalAddonsOnly || true)
work_n=$(kubectl get nodes -l "omni-role=work,agentpool=work0" --no-headers 2>/dev/null | wc -l)
short=()
if [ "$sys_n" != 1 ]; then short+=("one system machine labelled omni-role=system (found $sys_n)"); fi
if [ "$taint" -lt 1 ]; then short+=("the system machine tainted CriticalAddonsOnly=true:NoSchedule"); fi
if [ "$work_n" -lt 1 ]; then short+=("work machines labelled omni-role=work,agentpool=work0 (found none)"); fi
if [ "$work_n" -gt "$MAX" ]; then short+=("at most $MAX work machines (found $work_n): set BYOC_MAX_NODES to the pool's maximum"); fi
if [ "${#short[@]}" -gt 0 ]; then
  printf 'pre-flight: the cluster is not in the shape docs/BYOC_SETUP.md sets: %s. Nothing measured.\n' "$(IFS='; '; echo "${short[*]}")"; exit 2
fi
echo "pre-flight: $CLOUD cluster answers; 1 system machine, tainted; $work_n work machines of up to $MAX: ok"
if [ "${PREFLIGHT_ONLY:-0}" = 1 ]; then echo "pre-flight only: nothing measured"; exit 0; fi
settle() {   # every arm from the same machines: the work pool at exactly its start size, every work machine Ready
  local want="$1" waited=0 all ready
  while :; do
    all=$(kubectl get nodes -l omni-role=work,agentpool=work0 --no-headers 2>/dev/null | wc -l)
    ready=$(kubectl get nodes -l omni-role=work,agentpool=work0 --no-headers 2>/dev/null | grep -c ' Ready' || true)
    [ "$all" -eq "$want" ] && [ "$ready" -eq "$want" ] && return 0
    [ "$waited" -ge 2400 ] && { echo "the work pool stands at $all machines ($ready Ready), not $want, after ${waited} s"; return 1; }
    sleep 15; waited=$(( waited + 15 ))
  done
}
for arm in "${order[@]}"; do
  echo "######## waiting for the work pool to stand at $START machine(s) before $arm"
  # what the arm before left (a parked machine's taint, the governor's own marks) is handed back first: the governor
  # restores what it wrote at its exit (its kill file, scripts/kind_bench.sh), and every work machine is schedulable again
  for n in $(kubectl get nodes -l omni-role=work -o name); do kubectl uncordon "$n" >/dev/null 2>&1 || true; done
  kubectl taint nodes -l omni-role=work omnicompass.io/idle- >/dev/null 2>&1 || true
  if ! settle "$START"; then
    mkdir -p "bench-$arm-$REP"
    kubectl get nodes -o wide > "bench-$arm-$REP/nodes_not_ready.txt" 2>&1 || true
    kubectl describe nodes > "bench-$arm-$REP/nodes_describe.txt" 2>&1 || true
    kubectl get events -A --sort-by=.lastTimestamp > "bench-$arm-$REP/events.txt" 2>&1 || true
    echo "ARM $arm (repetition $REP): the work pool did not reach $START Ready machines; its state kept" | tee "bench-$arm-$REP/INVALID"; fail=1
    continue
  fi
  echo "######## ARM $arm (repetition $REP)"
  mkdir -p "bench-$arm-$REP"
  kubectl get nodes -o json > "bench-$arm-$REP/byoc_nodes.json"
  printf '{"cloud": "%s", "price_per_node_hour": %s, "max_nodes": %s, "start_nodes": %s}\n' "$CLOUD" "$PRICE" "$MAX" "$START" > "bench-$arm-$REP/byoc_cluster.json"
  if ! PLATFORM=byoc ARM="$arm" OUT_DIR="bench-$arm-$REP" bash scripts/kind_bench.sh; then
    echo "ARM $arm (repetition $REP) FAILED its checks: marked invalid" | tee "bench-$arm-$REP/INVALID"; fail=1
  fi
done
exit "${fail:-0}"

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
