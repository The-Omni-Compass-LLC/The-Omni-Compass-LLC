#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
#
# Crane on the kind rig (ADDONS=crane in scripts/kind_bench.sh; docs/CRANE_PREREGISTRATION.md; register row 90), installed the
# same way in every arm that carries it, before the arms are told apart: the Prometheus it reads its history from, as its
# installation guide installs it (the prometheus-community chart, Crane's own override values), then Crane 0.11.0 from its
# chart (each archive and the values file checked against its pinned SHA-256), its controllers on the control plane; then the
# service's autoscaler handed to Crane: the HPA deleted and an Effective HPA in auto mode applied with the operator's own
# settings (deploy/kind/crane-ehpa.yaml), from which Crane builds and owns the HPA ehpa-php-apache.
set -euo pipefail
OUT_DIR="${OUT_DIR:?set OUT_DIR}"
CRANE_VERSION="${CRANE_VERSION:-0.11.0}"          # released 25 July 2023, Crane's last (its chart, from gocrane/helm-charts)
CRANE_SHA256="${CRANE_SHA256:-1f3f163abc17c373e27380be42cf39d5041090ccad3c7af1597390550a8f7fe9}"
PROM_VERSION="${PROM_VERSION:-25.8.0}"            # the prometheus-community chart (Prometheus v2.48.0)
PROM_SHA256="${PROM_SHA256:-9f4fa3cc4e0f9e18b38fd8e754ad9bca36e021e8508b1169d5c6ad849ea37756}"
PROM_VALUES_SHA256="${PROM_VALUES_SHA256:-3fffcad0f166f4fae6f6d1444b65263f553dba4e7a169c692c69f59cf7f39452}"   # Crane's override values
NS=crane-system
DL=$(mktemp -d "${RUNNER_TEMP:-/tmp}/omni-crane.XXXXXX")
fetch() {   # url, file, sha256
  local t got
  for t in 1 2 3; do curl -fsSL --retry 5 --retry-delay 3 "$1" -o "$2" && break; sleep 10; done
  got=$(sha256sum "$2" | cut -d' ' -f1)
  [ "$got" = "$3" ] || { echo "INVALID RUN: $1 is not the pinned file (sha256 $got, pinned $3)"; exit 1; }
}
retry() {   # a step the API server or a webhook still starting may refuse: tried again, then the run fails with its words
  local t; for t in $(seq 1 30); do "$@" && return 0; sleep 5; done; echo "failed after 30 tries: $*"; return 1
}
fetch "https://github.com/prometheus-community/helm-charts/releases/download/prometheus-${PROM_VERSION}/prometheus-${PROM_VERSION}.tgz" \
  "$DL/prometheus.tgz" "$PROM_SHA256"
fetch "https://raw.githubusercontent.com/gocrane/helm-charts/main/integration/prometheus/override_values.yaml" \
  "$DL/prom-override.yaml" "$PROM_VALUES_SHA256"
fetch "https://github.com/gocrane/helm-charts/releases/download/crane-${CRANE_VERSION}/crane-${CRANE_VERSION}.tgz" \
  "$DL/crane.tgz" "$CRANE_SHA256"

load_images() {   # a chart's own images, pulled once onto the runner and loaded into every node (kind load), as busybox is
                  # (scripts/kind_bench.sh): a node's own pull of the Prometheus server image never finished in crane B, run
                  # 40359500118, repetition 2 (ImagePullBackOff; the install's ten minutes ran out and the arm was marked invalid).
                  # The same in every arm that carries Crane; where the load cannot be made, the nodes pull it themselves, as before
  local kname img t
  kname="${KIND_CLUSTER:-$(kubectl config current-context 2>/dev/null | sed -n 's/^kind-//p')}"
  for img in $(helm template "$@" | sed -n 's/^[[:space:]-]*image:[[:space:]]*"\{0,1\}\([^"[:space:]]*\)"\{0,1\}.*/\1/p' | sort -u); do
    for t in 1 2 3; do
      if docker image inspect "$img" >/dev/null 2>&1 || docker pull -q "$img" >/dev/null 2>&1; then break; fi
      echo "$img not pulled onto the runner (try $t)"; sleep 20
    done
    if [ -n "$kname" ] && kind load docker-image "$img" --name "$kname" >/dev/null 2>&1; then
      echo "$img: loaded into every node from the runner's own copy (kind load)" | tee -a "$OUT_DIR/preflight.txt"
    else
      echo "$img: not loaded from the runner; the nodes pull it themselves" | tee -a "$OUT_DIR/preflight.txt"
    fi
  done
}

echo "== Prometheus ${PROM_VERSION}, as Crane's installation guide installs it"
load_images prometheus "$DL/prometheus.tgz" --namespace "$NS" -f "$DL/prom-override.yaml" -f deploy/kind/crane-prometheus-values.yaml
helm install prometheus "$DL/prometheus.tgz" --namespace "$NS" --create-namespace -f "$DL/prom-override.yaml" \
  -f deploy/kind/crane-prometheus-values.yaml --wait --timeout 10m > "$OUT_DIR/crane_prometheus_helm.log" 2>&1 \
  || { tail -40 "$OUT_DIR/crane_prometheus_helm.log"; kubectl get pods -n "$NS" -o wide; exit 1; }
echo "== Crane ${CRANE_VERSION}"
load_images crane "$DL/crane.tgz" --namespace "$NS" -f deploy/kind/crane-values.yaml
helm install crane "$DL/crane.tgz" --namespace "$NS" -f deploy/kind/crane-values.yaml --wait --timeout 10m \
  > "$OUT_DIR/crane_helm.log" 2>&1 || { tail -40 "$OUT_DIR/crane_helm.log"; kubectl get pods -n "$NS" -o wide; exit 1; }
kubectl wait -n "$NS" --for=condition=Available deploy --all --timeout=600s >/dev/null
kubectl wait --for=condition=Available apiservice/v1beta1.external.metrics.k8s.io --timeout=300s >/dev/null

echo "== the service's autoscaler handed to Crane"
kubectl delete hpa php-apache --ignore-not-found --wait=true >/dev/null
sed "s/MAX_REPLICAS/${HPA_MAX:-10}/" deploy/kind/crane-ehpa.yaml > "$OUT_DIR/crane-ehpa.yaml"
retry kubectl apply -f "$OUT_DIR/crane-ehpa.yaml" >/dev/null   # Crane's webhook answers a little after its deployment
for i in $(seq 1 60); do
  owner=$(kubectl get hpa ehpa-php-apache -o json 2>/dev/null \
    | jq -r '[.metadata.ownerReferences[]? | select(.kind == "EffectiveHorizontalPodAutoscaler") | .name][0] // empty' || true)
  [ "$owner" = php-apache ] && break
  sleep 5
done
[ "$owner" = php-apache ] || { echo "INVALID RUN: Crane did not build the HPA ehpa-php-apache from its EHPA"; kubectl get hpa,effectivehorizontalpodautoscalers.autoscaling.crane.io -A -o wide; \
  kubectl -n "$NS" logs deployment/craned --tail=60; exit 1; }
cpu=$(kubectl get hpa ehpa-php-apache -o json | jq -r '[.spec.metrics[] | select(.type == "Resource" and .resource.name == "cpu") | .resource.target.averageUtilization][0] // empty')
[ "$cpu" = 50 ] || { echo "INVALID RUN: the HPA Crane built holds the processor at ${cpu:-nothing}, not 50"; exit 1; }
range=$(kubectl get hpa ehpa-php-apache -o jsonpath='{.spec.minReplicas},{.spec.maxReplicas}')
[ "$range" = "1,${HPA_MAX:-10}" ] || { echo "INVALID RUN: the HPA Crane built has the replica range $range, not 1,${HPA_MAX:-10}"; exit 1; }
cp_node=$(kubectl get nodes -l node-role.kubernetes.io/control-plane -o jsonpath='{.items[0].metadata.name}')
# every one of Crane's and its Prometheus's pods but the two node agents (Crane's and the node exporter, on every node as
# shipped) on the control plane; a pod on its way out for its grace period is not counted
away=$(kubectl -n "$NS" get pods -o json | jq -r --arg cp "$cp_node" '[.items[] | select(.metadata.deletionTimestamp == null)
  | select(([.metadata.ownerReferences[]?.kind] | index("DaemonSet")) | not) | select(.spec.nodeName != $cp) | .metadata.name] | join(" ")')
[ -z "$away" ] || { echo "INVALID RUN: Crane's pods on a measured worker: $away"; kubectl -n "$NS" get pods -o wide; exit 1; }
{
  echo "addons=crane"
  echo "crane=$CRANE_VERSION sha256=$CRANE_SHA256 (its chart; images docker.io/gocrane/*:v$CRANE_VERSION)"
  echo "prometheus_chart=$PROM_VERSION sha256=$PROM_SHA256; Crane's override values sha256=$PROM_VALUES_SHA256"
  echo "autoscaler: EHPA php-apache owns HPA ehpa-php-apache; ehpa spec: $(kubectl get effectivehorizontalpodautoscalers.autoscaling.crane.io php-apache -o json | jq -c '.spec')"
  echo "hpa metrics: $(kubectl get hpa ehpa-php-apache -o json | jq -c '.spec.metrics')"
  echo "hpa range: $range"
  echo "crane pods (namespace $NS):"
  kubectl -n "$NS" get pods -o json | jq -r '.items[] | select(.metadata.deletionTimestamp == null) | "  \(.metadata.name) \(.status.phase) node=\(.spec.nodeName)"'
  echo "images, with the digest each resolved to:"
  kubectl -n "$NS" get pods -o json | jq -r '[.items[].status.containerStatuses[]? | "  \(.image) \(.imageID)"] | unique[]'
} | tee "$OUT_DIR/addons.txt"
