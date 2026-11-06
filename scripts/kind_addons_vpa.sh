#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# The Vertical Pod Autoscaler in place, as a product Omni-Compass competes with (ADDONS=vpa in scripts/kind_bench.sh;
# docs/COMPETITORS_PREREGISTRATION.md). The VPA (Kubernetes SIG Autoscaling, kubernetes/autoscaler, Apache-2.0) at release
# 1.7.1: its CRDs, RBAC, recommender, updater and admission controller from the project's own manifests at the release tag,
# every file SHA-256 pinned, the admission controller's certificate made by the project's own gencerts.sh. The service's VPA
# runs in update mode InPlaceOrRecreate (always on in 1.7: the feature gate was removed) on the service's memory, beside the
# service's HPA on its processor: the pairing the VPA's documentation allows (it forbids the two on the same resource). The
# VPA keeps running through the window, recommending and resizing in place, as in service. Everything the VPA runs is pinned
# to the control plane beside metrics-server and CoreDNS, so the six measured workers carry only the service.
#   PHASE=install  before the load starts: the VPA, its certificate and the service's VPA object
#   PHASE=learn    with the load generator running: the load steps through LOAD_STEPS over VPA_LEARN seconds, then back
#                  to its first step; the VPA's first recommendation for the service is read and written down
set -euo pipefail
OUT_DIR="${OUT_DIR:?set OUT_DIR}"
PHASE="${PHASE:?set PHASE=install or PHASE=learn}"
VPA_VERSION="${VPA_VERSION:-1.7.1}"
VPA_CRD_SHA256="${VPA_CRD_SHA256:-92240d0f43a78bc9d64ce70825e84e0cd32d2793b0b605df4772cdcfc36d3fca}"
VPA_RBAC_SHA256="${VPA_RBAC_SHA256:-a5a1edd3221ca1e02bfb1bdb27eebb6897325cbb486b7b929df19894dd61749d}"
VPA_REC_SHA256="${VPA_REC_SHA256:-86641c249e43ba790acc6a099b719623f8e0ec05f713dfcd0a19c1f5cc50039c}"
VPA_UPD_SHA256="${VPA_UPD_SHA256:-046af55fb47f80062ab17b8faebcbc25ab60b76e0d8802eafd96cb9ce1ddb0a5}"
VPA_ADM_SHA256="${VPA_ADM_SHA256:-5d086a728333a1003c6b385e0b93442a1ea6745d7cba372ccdf81c4c34661949}"
VPA_ADMSVC_SHA256="${VPA_ADMSVC_SHA256:-1e1262ecb7faa2169946a26e50eacb9fa723fe21f39b26288f55e913c9e2fdff}"
VPA_CERTS_SHA256="${VPA_CERTS_SHA256:-c5fb592edbc4f19376720fa7f973082130ea97bb7c225b0dd84eac800832e8fb}"
VPA_RAW="https://raw.githubusercontent.com/kubernetes/autoscaler/vertical-pod-autoscaler-${VPA_VERSION}/vertical-pod-autoscaler"
VPA_NAME="php-apache"
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

if [ "$PHASE" = install ]; then
  DL=$(mktemp -d "${RUNNER_TEMP:-/tmp}/omni-vpa.XXXXXX")
  fetch "$VPA_RAW/deploy/vpa-v1-crd-gen.yaml" "$DL/vpa-crd.yaml" "$VPA_CRD_SHA256"
  fetch "$VPA_RAW/deploy/vpa-rbac.yaml" "$DL/vpa-rbac.yaml" "$VPA_RBAC_SHA256"
  fetch "$VPA_RAW/deploy/recommender-deployment.yaml" "$DL/vpa-recommender.yaml" "$VPA_REC_SHA256"
  fetch "$VPA_RAW/deploy/updater-deployment.yaml" "$DL/vpa-updater.yaml" "$VPA_UPD_SHA256"
  fetch "$VPA_RAW/deploy/admission-controller-deployment.yaml" "$DL/vpa-admission.yaml" "$VPA_ADM_SHA256"
  fetch "$VPA_RAW/deploy/admission-controller-service.yaml" "$DL/vpa-admission-service.yaml" "$VPA_ADMSVC_SHA256"
  fetch "$VPA_RAW/pkg/admission-controller/gencerts.sh" "$DL/gencerts.sh" "$VPA_CERTS_SHA256"

  echo "== Vertical Pod Autoscaler ${VPA_VERSION}: CRDs, RBAC, the admission controller's certificate, then its three parts"
  retry kubectl apply --server-side --force-conflicts -f "$DL/vpa-crd.yaml" >/dev/null
  kubectl wait --for=condition=Established crd/verticalpodautoscalers.autoscaling.k8s.io --timeout=120s
  retry kubectl apply -f "$DL/vpa-rbac.yaml" >/dev/null
  ( cd "$DL" && bash gencerts.sh ) > "$OUT_DIR/vpa_certs.log" 2>&1 || { tail -20 "$OUT_DIR/vpa_certs.log"; echo "the VPA admission controller's certificate could not be made"; exit 1; }
  retry kubectl apply -f "$DL/vpa-admission-service.yaml" >/dev/null
  for part in recommender updater admission; do
    retry kubectl apply -f "$DL/vpa-$part.yaml" >/dev/null
  done
  for d in vpa-recommender vpa-updater vpa-admission-controller; do
    kubectl -n kube-system patch deployment "$d" -p "$pin" >/dev/null
    kubectl -n kube-system rollout status deployment/"$d" --timeout=300s
  done

  echo "== the service's VPA: in place, on its memory (the HPA keeps its processor)"
  cat <<EOF | retry kubectl apply -f - >/dev/null
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata: {name: $VPA_NAME, namespace: default}
spec:
  targetRef: {apiVersion: apps/v1, kind: Deployment, name: php-apache}
  updatePolicy: {updateMode: InPlaceOrRecreate}
  resourcePolicy:
    containerPolicies:
      - {containerName: php-apache, controlledResources: [memory]}
EOF
  mode=$(kubectl get vpa "$VPA_NAME" -o jsonpath='{.spec.updatePolicy.updateMode}')
  res=$(kubectl get vpa "$VPA_NAME" -o jsonpath='{.spec.resourcePolicy.containerPolicies[0].controlledResources}')
  [ "$mode" = "InPlaceOrRecreate" ] || { echo "the service's VPA is in update mode '$mode', not InPlaceOrRecreate"; exit 1; }
  cp_node=$(kubectl get nodes -l node-role.kubernetes.io/control-plane -o jsonpath='{.items[0].metadata.name}')
  off=$(kubectl get pods -n kube-system -o json | jq --arg cp "$cp_node" '[.items[] | select(.metadata.deletionTimestamp == null)
    | select(.metadata.labels.app | IN("vpa-recommender", "vpa-updater", "vpa-admission-controller"))
    | select(.spec.nodeName != $cp)] | length')
  [ "$off" = "0" ] || { echo "$off VPA pods are not on the control plane ($cp_node)"; exit 1; }
  { echo "addons=vpa"
    echo "vpa=$VPA_VERSION crd_sha256=$VPA_CRD_SHA256 rbac_sha256=$VPA_RBAC_SHA256 recommender_sha256=$VPA_REC_SHA256 updater_sha256=$VPA_UPD_SHA256 admission_sha256=$VPA_ADM_SHA256 admission_service_sha256=$VPA_ADMSVC_SHA256 gencerts_sha256=$VPA_CERTS_SHA256"
    echo "vpa object: $VPA_NAME, update mode $mode, controlled resources $res (the HPA keeps the processor)"
    echo "license: Apache-2.0 (kubernetes/autoscaler's LICENSE)"
  } > "$OUT_DIR/addons.txt"
  exit 0
fi

[ "$PHASE" = learn ] || { echo "PHASE must be install or learn (got $PHASE)"; exit 1; }
LEARN="${VPA_LEARN:-600}"
read -r -a steps <<< "${LOAD_STEPS:-1 2 3 1 2 1}"
step_s=$(( LEARN / ${#steps[@]} ))
echo "== the VPA learns the service: the load through its steps (${steps[*]}), ${step_s} s each"
for r in "${steps[@]}"; do
  echo "$(date -u +%H:%M:%S) learning: load-generator replicas -> $r" | tee -a "$OUT_DIR/vpa_learn.log"
  for t in 1 2 3 4 5 6; do kubectl scale deployment/load-generator --replicas="$r" --request-timeout=20s >/dev/null && break; sleep 5; done || true
  sleep "$step_s"
done
kubectl scale deployment/load-generator --replicas="${steps[0]}" --request-timeout=20s >/dev/null
for i in $(seq 1 60); do
  rec=$(kubectl get vpa "$VPA_NAME" -o json | jq -c '[.status.recommendation.containerRecommendations[]? | select(.containerName == "php-apache")][0] // empty')
  [ -n "$rec" ] && [ "$(echo "$rec" | jq -r '.target.memory // empty')" != "" ] && break; sleep 10
done
[ -n "${rec:-}" ] || { echo "the VPA gave no recommendation for php-apache"; kubectl get vpa "$VPA_NAME" -o yaml; \
  kubectl -n kube-system logs deployment/vpa-recommender --tail=60; exit 1; }
echo "$rec" | jq . > "$OUT_DIR/vpa_recommendation_start.json"
echo "recommendation at the window's start (php-apache): $(echo "$rec" | jq -c '{target, lowerBound, upperBound}'); the VPA keeps acting through the window" | tee -a "$OUT_DIR/addons.txt"
