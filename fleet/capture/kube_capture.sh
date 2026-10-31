#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# Cluster capture for the Omni-Compass fleet harness. Read-only: uses get/top only.
# Requires kubectl (with metrics-server) and jq. Optional: POWER_CMD printing site power in watts.
# ACTIVE_ONLY=1 counts only nodes in service (open to work, or cordoned but still carrying work), and the usage on them.
# Usage: OUT=capture.csv INTERVAL=15 DURATION=21600 [POWER_CMD="..."] [ACTIVE_ONLY=1] bash kube_capture.sh
set -euo pipefail
OUT="${OUT:-capture.csv}"; INTERVAL="${INTERVAL:-15}"; DURATION="${DURATION:-21600}"
to_m() { awk '{v=$1; if (v ~ /m$/) {sub(/m$/,"",v); print v+0} else if (v ~ /n$/) {sub(/n$/,"",v); print v/1000000} else print v*1000}'; }
echo "timestamp,elapsed_seconds,nodes_ready,nodes_total,alloc_cpu_m,req_cpu_m,used_cpu_m,pods_pending,hpa_count,hpa_current_replicas,hpa_desired_replicas,power_w" > "$OUT"
start=$(date +%s); n=0
while :; do
  # the deadline ends the recording only after at least one reading: a recording with no row is never right (the
  # first reading used to be skipped when the clock ticked between the start and the first look, 21 October)
  now=$(date +%s); el=$((now - start)); [ "$el" -gt "$DURATION" ] && [ "$n" -gt 0 ] && break
  # a reading the API server does not answer (a swamped cluster, a managed control plane under load) is logged and
  # skipped; the recording goes on, so the moments a cluster struggles are kept, never the end of the run
  if ! nodes=$(kubectl get nodes -o json --request-timeout=20s 2>>"$OUT.errors") || \
     ! pods=$(kubectl get pods -A -o json --request-timeout=20s 2>>"$OUT.errors"); then
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) elapsed $el s: the API server did not answer; reading skipped" >> "$OUT.errors"
    sleep "$INTERVAL"; continue
  fi
  if [ "${ACTIVE_ONLY:-0}" = "1" ]; then
    # in service: open to new work, or closed (idle mark or cordon) but still carrying work (not a DaemonSet's), or held
    # by an add-on's own mark while still serving: a Ready worker carrying work whose only taints are NoSchedule marks
    # that are not Kubernetes' own (CruiseKube's cruisekube.truefoundry.com/overloaded, 19 October: it marks every worker
    # under load, and the workers kept serving every probe, so a reading of "no machine in service" was the recorder's
    # count, not the cluster). Kubernetes' own marks (node.kubernetes.io/*: unreachable, not ready, under pressure) and the
    # control plane's role mark still take a node out, as does any NoExecute mark.
    carrying=$(echo "$pods" | jq -r '[.items[] | select(.status.phase=="Running" or .status.phase=="Pending")
      | select(all(.metadata.ownerReferences[]?; .kind != "DaemonSet")) | .spec.nodeName // empty] | unique | join(" ")')
    nodes=$(echo "$nodes" | jq --arg c " $carrying " '.items |= map(select(
      ((.spec.unschedulable == true or any(.spec.taints[]?; .key == "omnicompass.io/idle")) as $closed
       | (.metadata.name as $n | $c | contains(" " + $n + " ")) as $carrying
       | [.spec.taints[]? | select(.effect=="NoSchedule" or .effect=="NoExecute")] as $held
       | ($closed | not) and ($held | length) == 0
         or ($closed and $carrying)
         or (($closed | not) and $carrying and ($held | length) > 0
             and all($held[]; .effect == "NoSchedule" and (.key | test("^node(-role)?[.]kubernetes[.]io/") | not))
             and any(.status.conditions[]?; .type == "Ready" and .status == "True")))))')
  fi
  names=$(echo "$nodes" | jq -r '[.items[].metadata.name] | join(" ")')
  ready=$(echo "$nodes" | jq '[.items[] | select(any(.status.conditions[]; .type=="Ready" and .status=="True"))] | length')
  total=$(echo "$nodes" | jq '.items | length')
  if [ "$total" = 0 ]; then   # no machine in service: why each node left it, kept for the record (its taints and conditions)
    { echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) elapsed $el s: no machine in service; the nodes as they stood:"
      kubectl get nodes -o json --request-timeout=20s 2>&1 | jq -c '.items[] | {name: .metadata.name, unschedulable: .spec.unschedulable,
        taints: [.spec.taints[]? | .key + ":" + .effect], conditions: [.status.conditions[] | select(.status != "False" or .type == "Ready") | .type + "=" + .status]}' 2>&1
    } >> "$OUT.errors"
  fi
  alloc=$(echo "$nodes" | jq -r '.items[].status.allocatable.cpu' | to_m | awk '{s+=$1} END {printf "%.0f", s}')
  req=$(echo "$pods" | jq -r '.items[] | select(.status.phase=="Running") | .spec.containers[].resources.requests.cpu // "0"' | to_m | awk '{s+=$1} END {printf "%.0f", s}')
  pending=$(echo "$pods" | jq '[.items[] | select(.status.phase=="Pending")] | length')
  used=$( { kubectl top nodes --no-headers --request-timeout=20s 2>>"$OUT.errors" || true; } | awk -v names="$names" 'BEGIN{n=split(names,a," "); for(i=1;i<=n;i++) on[a[i]]=1} ($1 in on){print $2}' | to_m | awk '{s+=$1} END {printf "%.0f", s}')
  hpa=$(kubectl get hpa -A -o json --request-timeout=20s 2>>"$OUT.errors") || hpa='{"items":[]}' 
  hc=$(echo "$hpa" | jq '.items | length'); hcur=$(echo "$hpa" | jq '[.items[].status.currentReplicas // 0] | add // 0'); hdes=$(echo "$hpa" | jq '[.items[].status.desiredReplicas // 0] | add // 0')
  if [ "$hc" = 0 ] && [ -n "${OWN_WORKLOADS:-}" ]; then   # by itself (ARM=solo): no autoscaler; the workloads' own counts
    hcur=0; for w in ${OWN_WORKLOADS//,/ }; do n=$(kubectl get deployment "${w#*/}" -n "${w%%/*}" -o jsonpath='{.spec.replicas}' --request-timeout=20s 2>>"$OUT.errors" || echo 0); hcur=$(( hcur + ${n:-0} )); done; hdes=$hcur
  fi
  pw=""; if [ -n "${POWER_CMD:-}" ]; then pw=$(eval "$POWER_CMD" 2>/dev/null || echo ""); fi
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ),$el,$ready,$total,$alloc,$req,$used,$pending,$hc,$hcur,$hdes,$pw" >> "$OUT"
  n=$((n + 1))
  sleep "$INTERVAL"
done
