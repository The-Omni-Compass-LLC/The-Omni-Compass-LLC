#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# The add-on native for the Kubernetes benchmark (ADDONS=keda in scripts/kind_bench.sh), installed the same way in every
# arm, before the arm is told apart: Kubernetes as clusters run it, with its add-ons, not bare.
#   KEDA core and the KEDA HTTP add-on, from their release manifests at a pinned version and SHA-256, applied server-side as
#   KEDA's own instructions apply them. Every KEDA pod runs on the control plane beside metrics-server and CoreDNS, so the
#   six measured workers carry only the service, as in every other set.
#   demo.yaml's HPA is replaced by a KEDA ScaledObject that owns the service's HPA under the same name, php-apache:
#     ADDONS_PROFILE=both (default)  the HPA's own CPU target (50%) and the add-on's live requests in flight (1 per pod)
#     ADDONS_PROFILE=http            the add-on's live requests in flight alone
#   Every request, the load's and the probe's, goes through the add-on's interceptor (deploy/kind/addons/keda-route.yaml),
#   which counts what is in flight for the add-on's scaler; the probe reaches it on NodePort 30090.
#   The interceptor's own autoscaler (a ScaledObject in the add-on's manifest, 200 requests waiting per interceptor) is
#   removed and the interceptor runs the one replica that autoscaler would hold at this load, so the only autoscaler in
#   the cluster is the service's, as in every other set, and every count of HPA replicas counts the service's pods.
# Writes addons.txt (versions, SHA-256, the HPA KEDA built, where every KEDA pod runs) and keda-scaledobject.yaml into OUT_DIR.
set -euo pipefail
OUT_DIR="${OUT_DIR:?set OUT_DIR}"
PROFILE="${ADDONS_PROFILE:-both}"
case "$PROFILE" in both|http) ;; *) echo "ADDONS_PROFILE must be both or http (got $PROFILE)"; exit 1;; esac
KEDA_VERSION="${KEDA_VERSION:-2.21.0}"
KEDA_SHA256="${KEDA_SHA256:-b43c89ffeef81722d7e2dd2c079d74789767a0f89cae1336cff784994814f6d7}"
KEDA_HTTP_VERSION="${KEDA_HTTP_VERSION:-0.16.0}"
KEDA_HTTP_SHA256="${KEDA_HTTP_SHA256:-eea0e57bb2ede0ab712a918a24df09b1fa0e8948880773b16920c3fbf05d3953}"
fetch() {   # url, file, sha256
  curl -fsSL --retry 5 --retry-delay 3 "$1" -o "$2"
  local got; got=$(sha256sum "$2" | cut -d' ' -f1)
  [ "$got" = "$3" ] || { echo "SHA-256 mismatch for $1: $got (expected $3)"; exit 1; }
}
# the manifests (0.8 MB) stay out of the run's record: their versions and SHA-256 are in addons.txt
DL=$(mktemp -d "${RUNNER_TEMP:-/tmp}/omni-addons.XXXXXX")
fetch "https://github.com/kedacore/keda/releases/download/v${KEDA_VERSION}/keda-${KEDA_VERSION}.yaml" \
  "$DL/keda-${KEDA_VERSION}.yaml" "$KEDA_SHA256"
fetch "https://github.com/kedacore/http-add-on/releases/download/v${KEDA_HTTP_VERSION}/keda-add-ons-http-${KEDA_HTTP_VERSION}.yaml" \
  "$DL/keda-add-ons-http-${KEDA_HTTP_VERSION}.yaml" "$KEDA_HTTP_SHA256"
pin='{"spec":{"template":{"spec":{"nodeSelector":{"node-role.kubernetes.io/control-plane":""},"tolerations":[{"key":"node-role.kubernetes.io/control-plane","operator":"Exists","effect":"NoSchedule"}]}}}}'
retry() {   # a step the API server or a webhook still starting may refuse: tried again, then the run fails with its words
  local t; for t in $(seq 1 30); do "$@" && return 0; sleep 5; done; echo "failed after 30 tries: $*"; return 1
}

echo "== KEDA ${KEDA_VERSION}"
retry kubectl apply --server-side --force-conflicts -f "$DL/keda-${KEDA_VERSION}.yaml" >/dev/null
for d in keda-operator keda-metrics-apiserver keda-admission; do kubectl -n keda patch deployment "$d" -p "$pin" >/dev/null; done
for d in keda-operator keda-metrics-apiserver keda-admission; do kubectl -n keda rollout status deployment/"$d" --timeout=300s; done
kubectl wait --for=condition=Available apiservice/v1beta1.external.metrics.k8s.io --timeout=300s

echo "== KEDA HTTP add-on ${KEDA_HTTP_VERSION}"
retry kubectl apply --server-side --force-conflicts -f "$DL/keda-add-ons-http-${KEDA_HTTP_VERSION}.yaml" >/dev/null
retry kubectl -n keda delete scaledobject keda-add-ons-http-interceptor --ignore-not-found --wait=true >/dev/null
for d in keda-add-ons-http-operator keda-add-ons-http-scaler keda-add-ons-http-interceptor; do kubectl -n keda patch deployment "$d" -p "$pin" >/dev/null; done
kubectl -n keda scale deployment keda-add-ons-http-interceptor --replicas=1 >/dev/null
for d in keda-add-ons-http-operator keda-add-ons-http-scaler keda-add-ons-http-interceptor; do kubectl -n keda rollout status deployment/"$d" --timeout=300s; done
# a finished rollout can still leave the replaced pod stopping behind the service: KEDA's first call to the add-on's scaler
# then meets a refused connection and the HPA is built without its HTTP metric (18 Oct, the KEDA test, run 39108180989,
# profile both, repetition 2). The ScaledObject is applied only once the old pods are gone and the scaler has an address
for i in $(seq 1 60); do
  stopping=$(kubectl -n keda get pods --no-headers 2>/dev/null | grep -c Terminating || true)
  [ "$stopping" = 0 ] && [ -n "$(kubectl -n keda get endpoints keda-add-ons-http-external-scaler -o jsonpath='{.subsets[*].addresses[*].ip}' 2>/dev/null)" ] && break
  sleep 2
done

echo "== the service's autoscaler handed to KEDA (profile $PROFILE)"
kubectl delete hpa php-apache --ignore-not-found --wait=true >/dev/null
retry kubectl apply -f deploy/kind/addons/keda-route.yaml >/dev/null
sed "s/MAX_REPLICAS/${HPA_MAX:-10}/" "deploy/kind/addons/keda-scaledobject-${PROFILE}.yaml" > "$OUT_DIR/keda-scaledobject.yaml"
retry kubectl apply -f "$OUT_DIR/keda-scaledobject.yaml" >/dev/null
kubectl wait --for=condition=Ready scaledobject/php-apache --timeout=300s
want_metrics=2; [ "$PROFILE" = http ] && want_metrics=1
for i in $(seq 1 60); do
  n=$(kubectl get hpa php-apache -o json 2>/dev/null | jq '.spec.metrics | length' 2>/dev/null || echo 0)
  [ "$n" = "$want_metrics" ] && break
  # a reconcile that failed waits on KEDA's back-off: once a minute the ScaledObject is touched (an annotation of the
  # harness, never a setting), so KEDA builds the HPA again from the same spec
  [ $(( i % 12 )) -ne 0 ] || kubectl annotate scaledobject php-apache --overwrite "omni-harness/reconcile=$i" >/dev/null 2>&1 || true
  sleep 5
done
[ "$n" = "$want_metrics" ] || { echo "KEDA did not build the HPA php-apache with $want_metrics metrics"; kubectl get hpa -A -o wide; \
  kubectl -n keda logs deployment/keda-operator --tail=60; exit 1; }
owner=$(kubectl get hpa php-apache -o json | jq -r '[.metadata.ownerReferences[]? | select(.kind == "ScaledObject") | .name][0] // empty')
[ "$owner" = "php-apache" ] || { echo "the HPA php-apache is not owned by the ScaledObject php-apache (owner: ${owner:-none})"; exit 1; }
cpu=$(kubectl get hpa php-apache -o json | jq -r '[.spec.metrics[] | select(.type == "Resource" and .resource.name == "cpu") | .resource.target.averageUtilization][0] // empty')
if [ "$PROFILE" = both ]; then [ "$cpu" = "50" ] || { echo "the HPA's CPU target is ${cpu:-missing}, not 50"; exit 1; }
else [ -z "$cpu" ] || { echo "profile http has a CPU target ($cpu)"; exit 1; }; fi
range=$(kubectl get hpa php-apache -o jsonpath='{.spec.minReplicas},{.spec.maxReplicas}')
[ "$range" = "1,${HPA_MAX:-10}" ] || { echo "the HPA's replica range is $range, not 1,${HPA_MAX:-10}"; exit 1; }

edge=$(kubectl get nodes -l node-role.kubernetes.io/control-plane -o jsonpath='{.items[0].status.addresses[?(@.type=="InternalIP")].address}')
for i in $(seq 1 60); do curl -fsS -m 5 "http://${edge}:30090/" >/dev/null 2>&1 && break; sleep 2; done
curl -fsS -m 5 "http://${edge}:30090/" >/dev/null || { echo "the service is not reachable through the add-on's interceptor"; \
  kubectl -n keda logs deployment/keda-add-ons-http-interceptor --tail=60; exit 1; }
{
  echo "addons=keda profile=$PROFILE"
  echo "keda=$KEDA_VERSION sha256=$KEDA_SHA256"
  echo "keda_http_add_on=$KEDA_HTTP_VERSION sha256=$KEDA_HTTP_SHA256"
  echo "autoscaler: ScaledObject php-apache owns HPA php-apache; triggers: $(kubectl get scaledobject php-apache -o json | jq -c '[.spec.triggers[] | {type, metricType, metadata}]')"
  echo "hpa metrics: $(kubectl get hpa php-apache -o json | jq -c '.spec.metrics')"
  echo "hpa range: $range"
  echo "interceptor route: $(kubectl get interceptorroute php-apache -o json | jq -c '.spec')"
  echo "keda pods (namespace keda, all on the control plane):"
  kubectl -n keda get pods -o json | jq -r '.items[] | select(.metadata.deletionTimestamp == null) | "  \(.metadata.name) \(.status.phase) node=\(.spec.nodeName)"'
} | tee "$OUT_DIR/addons.txt"
cp_node=$(kubectl get nodes -l node-role.kubernetes.io/control-plane -o jsonpath='{.items[0].metadata.name}')
# a pod of the add-on started before the pin may still be on its way out (terminating) for its grace period: not counted
off=$(kubectl -n keda get pods -o json | jq --arg cp "$cp_node" '[.items[] | select(.metadata.deletionTimestamp == null and .spec.nodeName != $cp)] | length')
[ "$off" = "0" ] || { echo "$off KEDA pods are not on the control plane ($cp_node)"; exit 1; }
