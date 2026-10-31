#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# The fault test (FAULTS=1 in scripts/kind_bench.sh): the same four faults at the same moments of every arm, so native
# Kubernetes alone and Kubernetes with Omni-Compass on top meet exactly the same trouble. Times are shares of DURATION.
#   machine   at 15%: a worker machine dies (its kind container is stopped); it comes back two minutes later
#   spike     at 35%: traffic triples for two minutes (a second open-rate load generator, RATE 12, on the control plane)
#   runaway   at 55%: a pod with no CPU limit burns CPU on a worker for two minutes
#   blind     at 75%: the response-time probe stops reporting for one minute (paused, then resumed)
# FAULTS=2, the extended test (amendment of 18 October, docs/K8S_COMPASS_PREREGISTRATION.md), adds the two faults that blind
# a governor, after the four, which keep their moments:
#   api       at 82%: the API server is frozen for 30 s (its process stopped, then continued; the service's own path, kube-proxy
#             on every node, keeps carrying traffic), so no controller can read the cluster or write to it
#   metrics   at 88%: the metrics server is scaled to none for two minutes, so every autoscaler reads no CPU metric
# Every fault and its recovery is written to $OUT_DIR/faults.log with its time.
# Usage: OUT_DIR=... DURATION=... PROBE_PID=... bash scripts/kind_faults.sh
set -u
D="${DURATION:?}"; LOG="${OUT_DIR:?}/faults.log"; CLUSTER="${KIND_CLUSTER:-omni-bench}"
say() { echo "$(date -u +%s) $*" | tee -a "$LOG"; }
at() { sleep "$(( D * $1 / 100 ))"; }
t0=$(date +%s)
wait_until() { local s=$(( t0 + D * $1 / 100 )); local now; now=$(date +%s); (( s > now )) && sleep $(( s - now )); }
wait_until 15
victim=$(kubectl get nodes -l '!node-role.kubernetes.io/control-plane' -o jsonpath='{.items[-1].metadata.name}')
say "machine down: $victim"; docker stop "$victim" >/dev/null 2>&1 || say "machine down failed"
sleep 120; docker start "$victim" >/dev/null 2>&1; say "machine back: $victim"
wait_until 35
say "spike: traffic x3"
kubectl get deployment load-generator -o json | jq '.metadata.name="load-spike" | .spec.selector.matchLabels.app="load-spike"
  | .spec.template.metadata.labels.app="load-spike" | .spec.template.spec.containers[0].env=[{"name":"RATE","value":"12"}]
  | del(.metadata.uid,.metadata.resourceVersion,.metadata.creationTimestamp,.metadata.annotations,.metadata.generation,.status)' \
  | kubectl apply -f - >/dev/null
sleep 120; kubectl delete deployment load-spike --wait=false >/dev/null 2>&1; say "spike over"
wait_until 55
say "runaway pod started"
kubectl run runaway --image=busybox:1.36 --restart=Never --overrides='{"spec":{"nodeSelector":{"kubernetes.io/os":"linux"}}}' \
  -- /bin/sh -c 'while :; do :; done' >/dev/null 2>&1
sleep 120; kubectl delete pod runaway --grace-period=0 --force >/dev/null 2>&1; say "runaway pod removed"
wait_until 75
if [ -n "${PROBE_PID:-}" ]; then
  say "probe blind"; kill -STOP "$PROBE_PID" 2>/dev/null; sleep 60; kill -CONT "$PROBE_PID" 2>/dev/null; say "probe back"
fi
if [ "${FAULTS:-1}" = "2" ]; then
  cp="${CLUSTER}-control-plane"
  # every kube-apiserver process in the control-plane node, found by its name in /proc (no tool the node image may lack)
  apiserver_signal() { echo 'n=0; for p in /proc/[0-9]*; do [ "$p/ns/pid" -ef /proc/self/ns/pid ] || continue; [ "$(cat $p/comm 2>/dev/null)" = kube-apiserver ] || continue; q=; while read -r k ids; do [ "$k" = NSpid: ] || continue; for q in $ids; do :; done; break; done < "$p/status"; [ -n "$q" ] && kill -'"$1"' "$q" && n=$((n+1)); done; [ "$n" -gt 0 ]'; }
  wait_until 82
  if docker exec "$cp" sh -c "$(apiserver_signal STOP)" >/dev/null 2>&1; then
    say "api frozen"; sleep 30
    if docker exec "$cp" sh -c "$(apiserver_signal CONT)" >/dev/null 2>&1; then say "api back"
    else say "api back failed: the API server's process could not be continued"; fi
  else
    say "api freeze failed: the API server's process was not found"
  fi
  wait_until 88
  if kubectl -n kube-system scale deployment/metrics-server --replicas=0 >/dev/null 2>&1; then
    say "metrics down"; sleep 120
    if kubectl -n kube-system scale deployment/metrics-server --replicas=1 >/dev/null 2>&1 &&
       kubectl -n kube-system rollout status deployment/metrics-server --timeout=120s >/dev/null 2>&1; then say "metrics back"
    else say "metrics back failed: the metrics server did not return within two minutes"; fi
  else
    say "metrics outage failed: the metrics server could not be scaled"
  fi
fi
