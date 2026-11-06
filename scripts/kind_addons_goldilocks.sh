#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# The Goldilocks native for the Kubernetes benchmark (ADDONS=goldilocks in scripts/kind_bench.sh; register row 80;
# docs/GOLDILOCKS_PREREGISTRATION.md), installed and applied the same way in every arm, before the arms are told apart:
# the service's resource requests set as an operator sets them with Goldilocks (FairwindsOps/goldilocks, Apache-2.0).
# Goldilocks's controller gives the service a Vertical Pod Autoscaler in recommendation mode (its default, update mode
# "off"); the VPA's own recommender (kubernetes/autoscaler, Apache-2.0) learns the service's use while the load runs the
# benchmark's own steps; the operator then applies the recommendation as the VPA itself applies one (each request at the
# target, each limit kept in its proportion to its request: the VPA's default, RequestsAndLimits). Goldilocks and the
# recommender keep running through the window, recommending, as in service. The HPA, the load and the probe are those of
# every other set; Omni-Compass's moves are its own (the HPA, the node pool, the power cap), on top of the rightsized
# service. Everything Goldilocks and the VPA run is pinned to the control plane beside metrics-server and CoreDNS, so the
# six measured workers carry only the service, as in every other set.
#   PHASE=install  before the load starts: the VPA's CRDs, RBAC and recommender (pinned version, every file SHA-256
#                  checked), the Goldilocks controller (pinned version, SHA-256 checked, its image pinned to its full tag);
#                  the namespace default labelled for Goldilocks; waits for Goldilocks's VPA for php-apache
#   PHASE=learn    with the load generator running: the load steps through LOAD_STEPS over GOLDILOCKS_LEARN seconds (the
#                  benchmark's own steps, compressed), then back to its first step; the recommendation is read, applied
#                  to php-apache and rolled out. Writes addons.txt, goldilocks_recommendation.json and
#                  goldilocks_limit.txt (the operator's CPU limit after the recommendation, which every reset check expects)
set -euo pipefail
OUT_DIR="${OUT_DIR:?set OUT_DIR}"
PHASE="${PHASE:?set PHASE=install or PHASE=learn}"
VPA_VERSION="${VPA_VERSION:-1.7.1}"          # the VPA line for Kubernetes 1.35-1.37 (its own compatibility table)
GOLDILOCKS_VERSION="${GOLDILOCKS_VERSION:-4.16.2}"
VPA_CRD_SHA256="${VPA_CRD_SHA256:-92240d0f43a78bc9d64ce70825e84e0cd32d2793b0b605df4772cdcfc36d3fca}"
VPA_RBAC_SHA256="${VPA_RBAC_SHA256:-a5a1edd3221ca1e02bfb1bdb27eebb6897325cbb486b7b929df19894dd61749d}"
VPA_REC_SHA256="${VPA_REC_SHA256:-86641c249e43ba790acc6a099b719623f8e0ec05f713dfcd0a19c1f5cc50039c}"
GL_SA_SHA256="${GL_SA_SHA256:-458d2ebd89907a2645735bf7339953c7a1551caed92353d24347cb91a55ebbcf}"
GL_ROLE_SHA256="${GL_ROLE_SHA256:-994cddc0d50701c2267005c254c253dd3cd0a48974ab1c8299a0c44ef6b209a0}"
GL_BIND_SHA256="${GL_BIND_SHA256:-73cef537ff6f024f41489e5b3bd0abcafe969cb5a1f0afcd968c338770dc1177}"
GL_DEPLOY_SHA256="${GL_DEPLOY_SHA256:-e04dccc91f2ff045b44ae569470a4b58a03db3eb36df5009f8102a7175399f8d}"
VPA_RAW="https://raw.githubusercontent.com/kubernetes/autoscaler/vertical-pod-autoscaler-${VPA_VERSION}/vertical-pod-autoscaler/deploy"
GL_RAW="https://raw.githubusercontent.com/FairwindsOps/goldilocks/v${GOLDILOCKS_VERSION}/hack/manifests/controller"
GL_IMAGE="us-docker.pkg.dev/fairwinds-ops/oss/goldilocks:v${GOLDILOCKS_VERSION}"   # full tag: its floating tags are gone
VPA_NAME="goldilocks-php-apache"             # the name Goldilocks gives the VPA of a Deployment
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
  DL=$(mktemp -d "${RUNNER_TEMP:-/tmp}/omni-goldilocks.XXXXXX")
  fetch "$VPA_RAW/vpa-v1-crd-gen.yaml" "$DL/vpa-crd.yaml" "$VPA_CRD_SHA256"
  fetch "$VPA_RAW/vpa-rbac.yaml" "$DL/vpa-rbac.yaml" "$VPA_RBAC_SHA256"
  fetch "$VPA_RAW/recommender-deployment.yaml" "$DL/vpa-recommender.yaml" "$VPA_REC_SHA256"
  fetch "$GL_RAW/serviceaccount.yaml" "$DL/gl-sa.yaml" "$GL_SA_SHA256"
  fetch "$GL_RAW/clusterrole.yaml" "$DL/gl-role.yaml" "$GL_ROLE_SHA256"
  fetch "$GL_RAW/clusterrolebinding.yaml" "$DL/gl-bind.yaml" "$GL_BIND_SHA256"
  fetch "$GL_RAW/deployment.yaml" "$DL/gl-deploy.yaml" "$GL_DEPLOY_SHA256"

  echo "== Vertical Pod Autoscaler ${VPA_VERSION}: the recommender (Goldilocks needs only it; no updater, no admission webhook)"
  retry kubectl apply --server-side --force-conflicts -f "$DL/vpa-crd.yaml" >/dev/null
  kubectl wait --for=condition=Established crd/verticalpodautoscalers.autoscaling.k8s.io --timeout=120s
  retry kubectl apply -f "$DL/vpa-rbac.yaml" >/dev/null
  retry kubectl apply -f "$DL/vpa-recommender.yaml" >/dev/null
  kubectl -n kube-system patch deployment vpa-recommender -p "$pin" >/dev/null
  kubectl -n kube-system rollout status deployment/vpa-recommender --timeout=300s

  echo "== Goldilocks ${GOLDILOCKS_VERSION}: the controller"
  kubectl create namespace goldilocks --dry-run=client -o yaml | kubectl apply -f - >/dev/null
  retry kubectl -n goldilocks apply -f "$DL/gl-sa.yaml" -f "$DL/gl-role.yaml" -f "$DL/gl-bind.yaml" >/dev/null
  sed "s#us-docker.pkg.dev/fairwinds-ops/oss/goldilocks:v4\"#${GL_IMAGE}\"#" "$DL/gl-deploy.yaml" > "$DL/gl-deploy-pinned.yaml"
  grep -q "$GL_IMAGE" "$DL/gl-deploy-pinned.yaml" || { echo "the Goldilocks image was not pinned to $GL_IMAGE"; exit 1; }
  retry kubectl -n goldilocks apply -f "$DL/gl-deploy-pinned.yaml" >/dev/null
  kubectl -n goldilocks patch deployment goldilocks-controller -p "$pin" >/dev/null
  kubectl -n goldilocks rollout status deployment/goldilocks-controller --timeout=300s

  echo "== the service's namespace handed to Goldilocks (recommendation mode, its default)"
  kubectl label namespace default goldilocks.fairwinds.com/enabled=true --overwrite >/dev/null
  for i in $(seq 1 60); do kubectl get vpa "$VPA_NAME" >/dev/null 2>&1 && break; sleep 5; done
  kubectl get vpa "$VPA_NAME" >/dev/null 2>&1 || { echo "Goldilocks made no VPA for php-apache"; kubectl get vpa -A; \
    kubectl -n goldilocks logs deployment/goldilocks-controller --tail=60; exit 1; }
  mode=$(kubectl get vpa "$VPA_NAME" -o jsonpath='{.spec.updatePolicy.updateMode}')
  [ "$mode" = "Off" ] || { echo "Goldilocks's VPA for php-apache is in update mode '${mode}', not Off (recommendation only)"; exit 1; }
  cp_node=$(kubectl get nodes -l node-role.kubernetes.io/control-plane -o jsonpath='{.items[0].metadata.name}')
  off=$(kubectl get pods -A -o json | jq --arg cp "$cp_node" '[.items[] | select(.metadata.deletionTimestamp == null)
    | select((.metadata.namespace == "goldilocks") or (.metadata.labels.app == "vpa-recommender"))
    | select(.spec.nodeName != $cp)] | length')
  [ "$off" = "0" ] || { echo "$off Goldilocks or VPA pods are not on the control plane ($cp_node)"; exit 1; }
  { echo "addons=goldilocks"
    echo "vpa=$VPA_VERSION (recommender only) crd_sha256=$VPA_CRD_SHA256 rbac_sha256=$VPA_RBAC_SHA256 recommender_sha256=$VPA_REC_SHA256"
    echo "goldilocks=$GOLDILOCKS_VERSION image=$GL_IMAGE deployment_sha256=$GL_DEPLOY_SHA256 rbac_sha256=$GL_SA_SHA256,$GL_ROLE_SHA256,$GL_BIND_SHA256"
    echo "vpa object: $VPA_NAME, update mode $mode (Goldilocks's default: recommendations only)"
  } > "$OUT_DIR/addons.txt"
  exit 0
fi

[ "$PHASE" = learn ] || { echo "PHASE must be install or learn (got $PHASE)"; exit 1; }
LEARN="${GOLDILOCKS_LEARN:-600}"
read -r -a steps <<< "${LOAD_STEPS:-1 2 3 1 2 1}"
step_s=$(( LEARN / ${#steps[@]} ))
echo "== Goldilocks learns the service: the load through its steps (${steps[*]}), ${step_s} s each"
for r in "${steps[@]}"; do
  echo "$(date -u +%H:%M:%S) learning: load-generator replicas -> $r" | tee -a "$OUT_DIR/goldilocks_learn.log"
  for t in 1 2 3 4 5 6; do kubectl scale deployment/load-generator --replicas="$r" --request-timeout=20s >/dev/null && break; sleep 5; done || true
  sleep "$step_s"
done
kubectl scale deployment/load-generator --replicas="${steps[0]}" --request-timeout=20s >/dev/null
# the recommendation for the service's container (the recommender writes it once a minute; a first one may lag)
for i in $(seq 1 60); do
  rec=$(kubectl get vpa "$VPA_NAME" -o json | jq -c '[.status.recommendation.containerRecommendations[]? | select(.containerName == "php-apache")][0] // empty')
  [ -n "$rec" ] && [ "$(echo "$rec" | jq -r '.target.cpu // empty')" != "" ] && break; sleep 10
done
[ -n "${rec:-}" ] || { echo "the VPA gave no recommendation for php-apache"; kubectl get vpa "$VPA_NAME" -o yaml; \
  kubectl -n kube-system logs deployment/vpa-recommender --tail=60; exit 1; }
echo "$rec" | jq . > "$OUT_DIR/goldilocks_own_recommendation.json"
# one recommendation for both arms of a repetition: each arm runs the same learning load (the same warm-up), but the
# operator applies the recommendation the repetition's first arm learned to both, so the two arms serve with the same
# requests (two short learnings differ by about a tenth on their own: 203m and 182m in the wiring run of 12 October)
shared="${GOLDILOCKS_SHARED:-goldilocks-recommendation-rep${REP:-0}.json}"
if [ -s "$shared" ]; then
  cp "$shared" "$OUT_DIR/goldilocks_recommendation.json"; origin="the repetition's first arm (its own learning shown beside)"
else
  cp "$OUT_DIR/goldilocks_own_recommendation.json" "$shared"; cp "$shared" "$OUT_DIR/goldilocks_recommendation.json"
  origin="this arm, the repetition's first"
fi
# the operator's rule (tools/goldilocks_apply.py): each request at the target, each limit in its proportion to its request
python tools/goldilocks_apply.py "$OUT_DIR/goldilocks_recommendation.json" "$OUT_DIR/goldilocks_apply.json"
req=$(jq -r .cpu_request_m "$OUT_DIR/goldilocks_apply.json"); lim=$(jq -r .cpu_limit_m "$OUT_DIR/goldilocks_apply.json")
mem=$(jq -r '.memory_request_bytes // empty' "$OUT_DIR/goldilocks_apply.json")
patch="{\"spec\":{\"template\":{\"spec\":{\"containers\":[{\"name\":\"php-apache\",\"resources\":{\"requests\":{\"cpu\":\"${req}m\"${mem:+,\"memory\":\"$mem\"}},\"limits\":{\"cpu\":\"${lim}m\"}}}]}}}}"
echo "== the operator applies Goldilocks's recommendation to php-apache: CPU request ${req}m, limit ${lim}m${mem:+, memory request $mem bytes}"
kubectl patch deployment php-apache --type strategic -p "$patch" >/dev/null
kubectl rollout status deployment/php-apache --timeout=300s
now=$(kubectl get deployment php-apache -o json | jq -c '.spec.template.spec.containers[] | select(.name == "php-apache") | .resources')
# the limit as the API server keeps it (it writes 1000m as "1"): what every reset check reads back from the pods
echo "$now" | jq -r '.limits.cpu' > "$OUT_DIR/goldilocks_limit.txt"
[ -s "$OUT_DIR/goldilocks_limit.txt" ] && [ "$(cat "$OUT_DIR/goldilocks_limit.txt")" != null ] || { echo "php-apache has no CPU limit after the recommendation"; exit 1; }
{ echo "recommendation (php-apache): $(jq -c '{target, lowerBound, upperBound}' "$OUT_DIR/goldilocks_recommendation.json"), learned in $origin"
  echo "this arm's own learning: $(jq -c '{target}' "$OUT_DIR/goldilocks_own_recommendation.json")"
  echo "applied (the operator, as the VPA applies one): $now"
  echo "learning: ${LEARN} s through the load steps ${steps[*]}"
} | tee -a "$OUT_DIR/addons.txt"
