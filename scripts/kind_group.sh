#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
#
# One repetition of the group of clusters (docs/GROUP_PREREGISTRATION.md; register rows 94 to 96): the organism is a group of
# GROUP_MEMBERS kind clusters on one runner, each the batch rig's six-worker cluster, and the batch stream is sent to the
# group. Every arm runs on fresh clusters, back to back on the same runner, in an order rotated by repetition, as
# scripts/kind_paired.sh runs one cluster's arms:
#   nativebare   the group alone: no orchestrator; the harness sends the stream's jobs to the members in turn
#   native       the orchestrator as its project ships it (ORCH: karmada or ocm, on a cluster of its own beside the members;
#                armada, as containers on the runner with one executor per member), every job sent to it and placed by it
#                (OCM's agents run in the members, in their own namespaces)
#   compassbare  Omni-Compass on top of each member of the group alone (one governor per member, each on its own cluster)
#   compass      Omni-Compass on top of each member, the orchestrator on top of the group
# Every member runs the batch rig's bench (scripts/kind_bench.sh, BATCH_QUEUE=group) side by side, its window opened with the
# others'; the stream starts once every member's window is open (scripts/kind_group_orch.sh); the members' records and the
# orchestrator's are merged into the arm's own files (tools/merge_group.py), which tools/live_reps.py reads as any arm.
set -euo pipefail
REP="${REP:?set REP}"; read -r -a arms <<< "${ARMS:-nativebare native compassbare compass}"
ORCH="${ORCH:?set ORCH=karmada, ocm or armada}"
N="${GROUP_MEMBERS:-2}"
case "$ORCH" in karmada|ocm|armada) ;; *) echo "ORCH must be karmada, ocm or armada (got $ORCH)"; exit 1 ;; esac
# the namespaces the orchestrator's agents run in on a member (its pods allowed there by the bench's clean-cluster check):
# Karmada in push mode runs nothing in a member, Armada's executors run on the runner; OCM's klusterlet runs in its own
agent_ns=""; [ "$ORCH" != ocm ] || agent_ns="open-cluster-management open-cluster-management-agent open-cluster-management-agent-addon"
export WORKLOAD=batch
# the metrics-server manifest every member applies, fetched once before the members start (the bench caches it per runner;
# two members fetching it at once would write the same file)
ms_ver="${METRICS_SERVER_VERSION:-v0.9.0}"; ms_sha="${METRICS_SERVER_SHA256:-1cec29a5267809306a2c6ec74a3e449abbb705b4a8beed0c8a1963910f72c79b}"
ms_cache="${RUNNER_TEMP:-${TMPDIR:-/tmp}}/metrics-server-${ms_ver}-components.yaml"
for t in 1 2 3; do
  [ -s "$ms_cache" ] && [ "$(sha256sum "$ms_cache" | cut -d' ' -f1)" = "$ms_sha" ] && break
  curl -fsSL --retry 8 --retry-all-errors --retry-delay 15 "https://github.com/kubernetes-sigs/metrics-server/releases/download/${ms_ver}/components.yaml" \
    -o "$ms_cache.part" && mv "$ms_cache.part" "$ms_cache"
  [ "$t" = 3 ] && { echo "the metrics-server manifest could not be fetched whole"; exit 1; }; sleep 20
done
make_cluster() {   # name, config, kubeconfig: a creation that fails is cleared and tried again, twice
  local t
  for t in 1 2 3; do
    kind delete cluster --name "$1" >/dev/null 2>&1 || true
    kind create cluster --name "$1" --config "$2" --kubeconfig "$3" --wait 120s && return 0
    echo "kind cluster $1 not created (try $t): trying again in 30 s"; sleep 30
  done
  echo "the kind cluster $1 could not be created (3 tries)"; return 1
}
clear_all() { for c in $(kind get clusters 2>/dev/null | grep '^omni-'); do kind delete cluster --name "$c" >/dev/null 2>&1 || true; done; }
k=${#arms[@]}; off=$(( (REP - 1) % k ))
order=( "${arms[@]:off}" "${arms[@]:0:off}" )
echo "repetition $REP, order: ${order[*]}, the group: $N members, orchestrator $ORCH"
for arm in "${order[@]}"; do
  base="${arm%bare}"; orch="$ORCH"; [ "$base" = "$arm" ] || orch=none
  D="$(pwd)/bench-$arm-$REP"; rm -rf "$D"; mkdir -p "$D/barrier"
  echo "######## ARM $arm (repetition $REP): the group of $N, orchestrator: $orch"
  clear_all
  ok=1
  for i in $(seq 1 "$N"); do make_cluster "omni-m$i" deploy/kind/cluster-full.yaml "$D/kubeconfig-m$i" || ok=0; done
  case "$orch" in none|armada) ;; *) make_cluster omni-host deploy/kind/cluster-host.yaml "$D/kubeconfig-host" || ok=0 ;; esac   # Armada's control plane runs on the runner, not on a cluster
  [ "$ok" = 1 ] || { echo "ARM $arm (repetition $REP): a cluster could not be created: marked invalid" | tee "$D/INVALID"; fail=1; continue; }
  # the orchestrator on its own cluster and every member joined to it, before any member's bench starts
  if [ "$orch" != none ] && ! D="$D" ORCH="$orch" N="$N" PHASE=install bash scripts/kind_group_orch.sh > "$D/orch_install.log" 2>&1; then
    tail -40 "$D/orch_install.log"
    echo "ARM $arm (repetition $REP): the orchestrator did not stand: marked invalid" | tee "$D/INVALID"; fail=1; clear_all; continue
  fi
  # every member's bench, side by side: the same bench as one cluster's, its window opened with the others'
  pids=()
  for i in $(seq 1 "$N"); do
    mkdir -p "$D/m$i"
    ( export KUBECONFIG="$D/kubeconfig-m$i" KIND_CLUSTER="omni-m$i" GROUP_BARRIER="$D/barrier" GROUP_SIZE="$N" \
             OMNI_REGISTRY="$D/m$i/registry" ARM="$base" BATCH_QUEUE=group OUT_DIR="$D/m$i"
      [ "$orch" = none ] || export GROUP_AGENT_NS="$agent_ns"
      bash scripts/kind_bench.sh ) > "$D/m$i.log" 2>&1 &
    pids+=($!)
  done
  # the stream, sent to the group once every member's window is open
  D="$D" ORCH="$orch" N="$N" PHASE=submit bash scripts/kind_group_orch.sh > "$D/orch_submit.log" 2>&1 &
  sub_pid=$!
  bad=0
  for i in $(seq 1 "$N"); do wait "${pids[$((i - 1))]}" || { bad=1; echo "member $i of ARM $arm failed its checks"; tail -30 "$D/m$i.log"; }; done
  wait "$sub_pid" || { bad=1; echo "the stream of ARM $arm was not sent whole"; tail -30 "$D/orch_submit.log"; }
  D="$D" ORCH="$orch" N="$N" PHASE=end bash scripts/kind_group_orch.sh > "$D/orch_end.log" 2>&1 || true
  if [ "$bad" = 0 ] && python3 tools/merge_group.py "$D" "$N" "$orch" > "$D/merge.log" 2>&1; then
    echo "ARM $arm (repetition $REP): the group's records merged ($(tail -1 "$D/merge.log"))"
  else
    tail -20 "$D/merge.log" 2>/dev/null || true
    echo "ARM $arm (repetition $REP) FAILED its checks: marked invalid" | tee "$D/INVALID"; fail=1
  fi
  rm -f "$D"/kubeconfig-*   # no credentials in the run's files
  clear_all
done
exit "${fail:-0}"
# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
