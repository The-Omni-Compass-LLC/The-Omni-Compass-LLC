#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# The CruiseKube native for the Kubernetes benchmark (CRUISEKUBE=1 beside ADDONS=keda ADDONS_PROFILE=http in
# scripts/kind_bench.sh; register row 81; docs/CRUISEKUBE_PREREGISTRATION.md), installed and started the same way in every
# arm, before the arms are told apart:
# CruiseKube (truefoundry/cruisekube, TrueFoundry; Business Source License 1.1, which grants non-production use: a
# benchmark is non-production) right-sizes the service's CPU and memory itself, in place on the running pods and at
# admission through its webhook, from what Prometheus shows of the service's use. Its own knobs per workload are on or off
# (Cruise mode), an eviction rank and disruption windows; it acts only on workloads older than an hour (its shipped
# setting, kept). It leaves alone any workload whose autoscaler scales on CPU or memory, so the service's autoscaler is
# KEDA's HTTP add-on on requests in flight (row 68's KEDA set, its profile http: scripts/kind_addons.sh), with its load
# and its probe; Omni-Compass's moves are its own (the autoscaler's replica range, carried to KEDA's ScaledObject by the
# plug, the node pool, the rollout guard), on top, and never the CPU limit, which CruiseKube resizes itself.
# Everything CruiseKube and its Prometheus run is pinned to the control plane beside metrics-server and CoreDNS, so the
# six measured workers carry only the service, as in every other set; the one exception is node-exporter, one small pod
# per node (CruiseKube reads every node's own counters), the same in every arm.
#   PHASE=install  before the load starts: kube-state-metrics (pinned release, every file SHA-256 checked), node-exporter
#                  and a Prometheus of our own (deploy/kind/cruisekube-metrics.yaml: pinned images, the scrape jobs and
#                  labels CruiseKube's queries name), then CruiseKube's own chart (pinned version, its archive SHA-256
#                  checked) with its usage reports to its maker switched off, its dashboard and its login left out (the
#                  API answers inside the cluster only), its PostgreSQL its own chart's, on the control plane
#   PHASE=learn    with the load generator running: the service is put in Cruise mode through CruiseKube's own API once
#                  CruiseKube lists it; the load steps through LOAD_STEPS over CRUISEKUBE_LEARN seconds (the benchmark's
#                  own steps, repeated), long enough for the service to be older than CruiseKube's hour and for its
#                  statistics and its first applications to run; the start of the arms waits for CruiseKube's first
#                  applied change to the service (its audit events), or the run is marked INVALID: a native that never
#                  acted would be plain Kubernetes. Adds to addons.txt (after KEDA's lines); writes
#                  cruisekube_workloads.json, cruisekube_audit_start.json and cruisekube_resources_start.json
#   PHASE=end      after the window: CruiseKube's audit events, its workload view and its controller's last words
set -euo pipefail
OUT_DIR="${OUT_DIR:?set OUT_DIR}"
PHASE="${PHASE:?set PHASE=install, PHASE=learn or PHASE=end}"
CK_VERSION="${CK_VERSION:-0.3.4}"
CK_CHART="oci://tfy.jfrog.io/tfy-helm/cruisekube"
CK_CHART_SHA256="${CK_CHART_SHA256:-}"      # the chart archive's SHA-256; empty only in a shakedown run, which records it
KSM_VERSION="${KSM_VERSION:-v2.20.0}"
KSM_RAW="https://raw.githubusercontent.com/kubernetes/kube-state-metrics/${KSM_VERSION}/examples/standard"
KSM_SHA256_CRB="${KSM_SHA256_CRB:-afd513a9dba5ffe1a4128e4f612788dcccc314fb58afaef7a627c506229570df}"
KSM_SHA256_CR="${KSM_SHA256_CR:-4447544443859be7f70deca48e4cb75d30b0b7da090cb9e914c9c08f97f7e62c}"
KSM_SHA256_DEPLOY="${KSM_SHA256_DEPLOY:-08d57682c0117bda50b8e894be1669001e49ce0ff3e60c11fccc6f56dfbc9f2e}"
KSM_SHA256_SA="${KSM_SHA256_SA:-91f24588ac4f8944b9211fccefdce9ee70434676e8a4a55a14d69bc7f68ae0a5}"
KSM_SHA256_SVC="${KSM_SHA256_SVC:-efa9813fb6a6a2d11b509cf4f2eb0ab044935b4153b425e697d4b31c7f6f42a4}"
NS=cruisekube-system
WORKLOAD_ID="Deployment:default:php-apache"  # CruiseKube's own key for a workload: kind, namespace and name
API_PORT="${CRUISEKUBE_API_PORT:-18080}"
pin='{"spec":{"template":{"spec":{"nodeSelector":{"node-role.kubernetes.io/control-plane":""},"tolerations":[{"key":"node-role.kubernetes.io/control-plane","operator":"Exists","effect":"NoSchedule"}]}}}}'
fetch() {   # url, file, sha256: tried again when GitHub refuses it, then checked byte for byte
  local t got
  for t in 1 2 3 4 5; do curl -fsSL --retry 5 --retry-all-errors --retry-delay 5 --connect-timeout 20 --max-time 120 "$1" -o "$2" && break; sleep 10; done
  got=$(sha256sum "$2" | cut -d' ' -f1)
  [ "$got" = "$3" ] || { echo "SHA-256 mismatch for $1: $got (expected $3)"; exit 1; }
}
retry() {   # a step the API server or a controller still starting may refuse: tried again, then the run fails with its words
  local t; for t in $(seq 1 30); do "$@" && return 0; sleep 5; done; echo "failed after 30 tries: $*"; return 1
}
api_up() {  # CruiseKube's API, reached through a port-forward to its controller (it answers inside the cluster only)
  if ! curl -fsS -m 5 "http://127.0.0.1:$API_PORT/health" >/dev/null 2>&1; then
    pkill -f "port-forward -n $NS svc/cruisekube-controller $API_PORT:" 2>/dev/null || true
    kubectl -n "$NS" port-forward svc/cruisekube-controller "$API_PORT:8080" > "$OUT_DIR/cruisekube_port_forward.log" 2>&1 &
    for _ in $(seq 1 30); do curl -fsS -m 5 "http://127.0.0.1:$API_PORT/health" >/dev/null 2>&1 && return 0; sleep 2; done
    return 1
  fi
}
api() { curl -fsS -m 20 "http://127.0.0.1:$API_PORT/api/v1/clusters/default$1" "${@:2}"; }

if [ "$PHASE" = install ]; then
  DL=$(mktemp -d "${RUNNER_TEMP:-/tmp}/omni-cruisekube.XXXXXX")
  # kube-state-metrics, the shipped standard install, on the control plane
  fetch "$KSM_RAW/cluster-role-binding.yaml" "$DL/ksm-crb.yaml" "$KSM_SHA256_CRB"
  fetch "$KSM_RAW/cluster-role.yaml" "$DL/ksm-cr.yaml" "$KSM_SHA256_CR"
  fetch "$KSM_RAW/deployment.yaml" "$DL/ksm-deploy.yaml" "$KSM_SHA256_DEPLOY"
  fetch "$KSM_RAW/service-account.yaml" "$DL/ksm-sa.yaml" "$KSM_SHA256_SA"
  fetch "$KSM_RAW/service.yaml" "$DL/ksm-svc.yaml" "$KSM_SHA256_SVC"
  for f in ksm-sa ksm-cr ksm-crb ksm-deploy ksm-svc; do retry kubectl apply -f "$DL/$f.yaml"; done
  kubectl -n kube-system patch deployment kube-state-metrics -p "$pin"
  # node-exporter (one pod a node) and our own Prometheus, its scrape jobs named as CruiseKube's queries name them
  retry kubectl apply -f deploy/kind/cruisekube-metrics.yaml
  kubectl -n kube-system rollout status deployment/kube-state-metrics --timeout=300s
  kubectl -n cruisekube-metrics rollout status daemonset/node-exporter --timeout=300s
  kubectl -n cruisekube-metrics rollout status deployment/prometheus --timeout=300s
  # CruiseKube's own chart, at its pinned version; the archive is kept, its SHA-256 checked (or, in a shakedown run with
  # no pin yet, recorded for the pin)
  helm pull "$CK_CHART" --version "$CK_VERSION" --destination "$DL" > "$OUT_DIR/cruisekube_chart_pull.log" 2>&1 \
    || { sleep 20; helm pull "$CK_CHART" --version "$CK_VERSION" --destination "$DL" >> "$OUT_DIR/cruisekube_chart_pull.log" 2>&1; }
  chart="$DL/cruisekube-$CK_VERSION.tgz"
  got=$(sha256sum "$chart" | cut -d' ' -f1)
  echo "cruisekube_chart=$CK_VERSION sha256=$got" >> "$OUT_DIR/cruisekube_pins.txt"
  if [ -n "$CK_CHART_SHA256" ]; then
    [ "$got" = "$CK_CHART_SHA256" ] || { echo "SHA-256 mismatch for the CruiseKube chart $CK_VERSION: $got (expected $CK_CHART_SHA256)"; exit 1; }
  elif [ "${CRUISEKUBE_SHAKEDOWN:-}" != 1 ]; then
    echo "the CruiseKube chart has no pinned SHA-256 (CK_CHART_SHA256): only a shakedown run may record one"; exit 1
  fi
  retry kubectl create namespace "$NS" --dry-run=client -o yaml | kubectl apply -f -
  helm install cruisekube "$chart" --namespace "$NS" -f deploy/kind/cruisekube-values.yaml \
    ${CRUISEKUBE_NEW_WORKLOAD_HOURS:+--set-string cruisekubeController.env.CRUISEKUBE_RECOMMENDATIONSETTINGS_NEWWORKLOADTHRESHOLDHOURS=$CRUISEKUBE_NEW_WORKLOAD_HOURS} \
    --wait --timeout 15m > "$OUT_DIR/cruisekube_helm.log" 2>&1 || { tail -40 "$OUT_DIR/cruisekube_helm.log"; kubectl -n "$NS" get pods -o wide; exit 1; }
  # the controller and the webhook beside metrics-server and CoreDNS on the control plane (the chart has no placement
  # settings), so the six measured workers carry only the service
  for d in cruisekube-controller cruisekube-webhook; do
    kubectl -n "$NS" patch deployment "$d" -p "$pin"
    kubectl -n "$NS" rollout status deployment/"$d" --timeout=300s
  done
  kubectl -n "$NS" get pods -o wide > "$OUT_DIR/cruisekube_pods.txt"
  # every add-on pod but node-exporter on the control plane: a pod the move replaced is given two minutes to finish
  # shutting down on its worker, as a rollout leaves it, and a pod still serving on a worker fails the run
  offpods() {   # $1 true: count pods shutting down too; false: only pods still serving
    kubectl get pods -A -o json | jq -r --argjson terminating "$1" '[.items[]
      | select((.metadata.namespace | IN("cruisekube-system","cruisekube-metrics"))
               or (.metadata.namespace == "kube-system" and (.metadata.labels["app.kubernetes.io/name"] // "") == "kube-state-metrics"))
      | select((.metadata.labels.app // "") != "node-exporter")
      | select(.status.phase == "Running" or .status.phase == "Pending")
      | select($terminating or .metadata.deletionTimestamp == null)
      | select((.spec.nodeName // "") | test("control-plane") | not)
      | .metadata.namespace + "/" + .metadata.name] | join(" ")'
  }
  for _ in $(seq 1 24); do [ -z "$(offpods true)" ] && break; sleep 5; done
  off=$(offpods false)
  [ -z "$off" ] || { echo "add-on pods on a measured worker: $off"; exit 1; }
  left=$(offpods true)
  [ -z "$left" ] || echo "still shutting down on a worker two minutes after the move: $left" | tee -a "$OUT_DIR/addons.txt"
  # every image the add-ons run, as the cluster resolved it (tag and digest), in the run's own record
  kubectl get pods -A -o json | jq -r '.items[] | select((.metadata.namespace | IN("cruisekube-system","cruisekube-metrics")) or (.metadata.name | startswith("kube-state-metrics"))) | .status.containerStatuses[]? | "\(.image) \(.imageID)"' \
    | sort -u >> "$OUT_DIR/cruisekube_pins.txt"
  api_up || { echo "CruiseKube's API did not answer"; tail -20 "$OUT_DIR/cruisekube_port_forward.log"; exit 1; }
  # CruiseKube's own view of its inputs and its settings as they stand (its hour among them), in the run's record
  api /preflight > "$OUT_DIR/cruisekube_preflight.json" 2>>"$OUT_DIR/cruisekube_api.err" || true
  api /settings > "$OUT_DIR/cruisekube_settings.json" 2>>"$OUT_DIR/cruisekube_api.err" || true
  { echo "cruisekube=$CK_VERSION chart_sha256=$got kube_state_metrics=$KSM_VERSION"
    echo "cruisekube_new_workload_hours=${CRUISEKUBE_NEW_WORKLOAD_HOURS:-1 (shipped)} shakedown=${CRUISEKUBE_SHAKEDOWN:-0}"; } >> "$OUT_DIR/addons.txt"
  exit 0
fi

if [ "$PHASE" = learn ]; then
  LEARN="${CRUISEKUBE_LEARN:-4500}"
  api_up || { echo "CruiseKube's API did not answer"; exit 1; }
  # the service enters CruiseKube's list once its statistics task has seen it (every 15 minutes as shipped)
  t0=$(date -u +%s); listed=""
  for _ in $(seq 1 60); do
    api_up || true
    if api /workloads > "$OUT_DIR/cruisekube_workloads.json" 2>/dev/null \
       && jq -e --arg id "$WORKLOAD_ID" '[.[]? | select((.workload_id // "") | ascii_downcase == ($id | ascii_downcase))] | length > 0' "$OUT_DIR/cruisekube_workloads.json" >/dev/null 2>&1; then
      listed=1; break
    fi
    sleep 30
  done
  [ -n "$listed" ] || { echo "INVALID RUN: CruiseKube never listed the service ($WORKLOAD_ID)"; exit 1; }
  # Cruise mode on the service, through CruiseKube's own API (the operator's switch); nothing else is changed
  api "/workloads/$WORKLOAD_ID/overrides" -X POST -H 'Content-Type: application/json' -d '{"enabled": true}' \
    > "$OUT_DIR/cruisekube_cruise_on.json"
  echo "cruise mode on for $WORKLOAD_ID after $(( $(date -u +%s) - t0 )) s" | tee -a "$OUT_DIR/addons.txt"
  # the benchmark's own load steps, repeated until CRUISEKUBE_LEARN seconds have passed and CruiseKube has applied a
  # change to the service (its audit events); the arms start from there
  read -r -a steps <<< "${LOAD_STEPS:-1 2 3 1 2 1}"
  per=300   # five minutes a step
  end=$(( t0 + LEARN )); i=0; applied=""
  while :; do
    kubectl scale deployment/load-generator --replicas="${steps[$(( i % ${#steps[@]} ))]}" >/dev/null
    sleep "$per"; i=$(( i + 1 ))
    api_up || true
    if api "/audit-events/$WORKLOAD_ID?minutes=600" > "$OUT_DIR/cruisekube_audit_start.json" 2>/dev/null \
       && [ "$(jq '[.events[]? | select((.category // "") | test("RECOMMENDATION_APPLIED|WEBHOOK_MUTATION"))] | length' "$OUT_DIR/cruisekube_audit_start.json" 2>/dev/null || echo 0)" -gt 0 ]; then
      applied=1
    fi
    [ "$(date -u +%s)" -ge "$end" ] && { [ -n "$applied" ] || [ "$(date -u +%s)" -ge $(( end + 1800 )) ]; } && break
  done
  kubectl scale deployment/load-generator --replicas="${steps[0]}" >/dev/null
  [ -n "$applied" ] || { echo "INVALID RUN: CruiseKube made no change to the service in $(( $(date -u +%s) - t0 )) s of learning"; exit 1; }
  kubectl get pods -n default -l run=php-apache -o json | jq -c '[.items[] | {name: .metadata.name, resources: .spec.containers[0].resources}]' \
    > "$OUT_DIR/cruisekube_resources_start.json"
  echo "cruisekube applied a change to the service; learning $(( $(date -u +%s) - t0 )) s" | tee -a "$OUT_DIR/addons.txt"
  exit 0
fi

if [ "$PHASE" = end ]; then
  api_up || true
  api "/audit-events/$WORKLOAD_ID?minutes=600" > "$OUT_DIR/cruisekube_audit_end.json" 2>>"$OUT_DIR/end_reads.err" || true
  api /workloads > "$OUT_DIR/cruisekube_workloads_end.json" 2>>"$OUT_DIR/end_reads.err" || true
  kubectl -n "$NS" logs deployment/cruisekube-controller --tail=400 --request-timeout=20s > "$OUT_DIR/cruisekube-controller.log" 2>&1 || true
  kubectl -n "$NS" logs deployment/cruisekube-webhook --tail=200 --request-timeout=20s > "$OUT_DIR/cruisekube-webhook.log" 2>&1 || true
  pkill -f "port-forward -n $NS svc/cruisekube-controller $API_PORT:" 2>/dev/null || true
  exit 0
fi
echo "PHASE must be install, learn or end (got $PHASE)"; exit 1
