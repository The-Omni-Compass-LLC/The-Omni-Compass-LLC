#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# Kepler, the shared energy meter of the Kubernetes sets on a machine with the processor's own meter (KEPLER=1 in
# scripts/kind_bench.sh; register row 79; docs/METER_PREREGISTRATION.md). Kepler is not an arm: it reads both arms the
# same way, and its numbers sit beside the arms' own gauges. Kepler 0.11.4 (sustainable-computing-io/kepler, the CNCF
# Sustainable Computing project; Apache-2.0) from the project's own Kubernetes manifests at the release tag, every file
# SHA-256 checked, its image the release's (quay.io/sustainable_computing_io/kepler:v0.11.4, the tag its own README
# names; pulled once, its digest recorded); its ServiceMonitor left out (no Prometheus Operator runs here). Kepler 0.10 and
# later read the processor's RAPL counters themselves and carry no model: on a machine without them (a virtual machine,
# GitHub's runners among them) Kepler has only a standin development meter, so this script installs nothing there
# (tools/rapl.py probe decides), and the run's energy stays the declared model.
#   PHASE=install          before the load starts: the manifests applied, Kepler running on every node
#   PHASE=read TAG=start   at the window's opening, and TAG=end at its close: every Kepler pod's metrics, read through the
#                          API server and saved whole (kepler_<tag>_<node>.prom); on kind every node reads the same
#                          machine's counters, so the machine's energy is read from one, the control plane's
#   PHASE=end              the Kepler pods' last words
set -euo pipefail
OUT_DIR="${OUT_DIR:?set OUT_DIR}"
PHASE="${PHASE:?set PHASE=install, PHASE=read or PHASE=end}"
KEPLER_VERSION="v0.11.4"
KEPLER_IMAGE="quay.io/sustainable_computing_io/kepler:${KEPLER_VERSION}"
RAW="https://raw.githubusercontent.com/sustainable-computing-io/kepler/${KEPLER_VERSION}/manifests/k8s"
SHA_NAMESPACE="${KEPLER_SHA256_NAMESPACE:-afd21bf48331ac5a220332669a688a311c947969752ec5f713c2b27f96997663}"
SHA_RBAC="${KEPLER_SHA256_RBAC:-c874b60c11abec3acc2945679b1fef08dd575224756195a990fd91c1262511c0}"
SHA_CONFIGMAP="${KEPLER_SHA256_CONFIGMAP:-d6db44aeb88be7f90d2fd4b5b2f755360be1ad0d10628e2c673669b8cdb82e83}"
SHA_DAEMONSET="${KEPLER_SHA256_DAEMONSET:-d79739dd08a0e40c4bced5df725bf4bdfc7f5ad01949add83515ee67e1ba4656}"
SHA_SERVICE="${KEPLER_SHA256_SERVICE:-d77e6626e1053ee801422e1e6d0654f6aa1901a402074e1dd7ed004f3520b577}"
NS=kepler
fetch() {   # url, file, sha256: tried again when GitHub refuses it, then checked byte for byte
  local t got
  for t in 1 2 3 4 5; do curl -fsSL --retry 5 --retry-all-errors --retry-delay 5 --connect-timeout 20 --max-time 120 "$1" -o "$2" && break; sleep 10; done
  got=$(sha256sum "$2" | cut -d' ' -f1)
  [ "$got" = "$3" ] || { echo "SHA-256 mismatch for $1: $got (expected $3)"; exit 1; }
}
retry() { local t; for t in $(seq 1 30); do "$@" && return 0; sleep 5; done; echo "failed after 30 tries: $*"; return 1; }

if [ "$PHASE" = install ]; then
  python3 tools/rapl.py probe > "$OUT_DIR/meter_probe.json" \
    || { echo "no processor meter on this machine (tools/rapl.py probe): Kepler would have only its standin meter; nothing installed"; exit 1; }
  DL=$(mktemp -d "${RUNNER_TEMP:-/tmp}/omni-kepler.XXXXXX")
  fetch "$RAW/namespace.yaml" "$DL/namespace.yaml" "$SHA_NAMESPACE"
  fetch "$RAW/rbac.yaml" "$DL/rbac.yaml" "$SHA_RBAC"
  fetch "$RAW/configmap.yaml" "$DL/configmap.yaml" "$SHA_CONFIGMAP"
  fetch "$RAW/daemonset.yaml" "$DL/daemonset.yaml" "$SHA_DAEMONSET"
  fetch "$RAW/service.yaml" "$DL/service.yaml" "$SHA_SERVICE"
  # the release's image in the placeholder the project's README fills, pulled once (not at every restart)
  sed -e "s|<KEPLER_IMAGE>|$KEPLER_IMAGE|g" -e "s|imagePullPolicy: Always|imagePullPolicy: IfNotPresent|" "$DL/daemonset.yaml" > "$DL/daemonset.pinned.yaml"
  grep -q "image: $KEPLER_IMAGE" "$DL/daemonset.pinned.yaml" || { echo "the Kepler image was not set in its DaemonSet"; exit 1; }
  for f in namespace rbac configmap daemonset.pinned service; do retry kubectl apply -f "$DL/$f.yaml" >/dev/null; done
  kubectl -n "$NS" rollout status daemonset/kepler --timeout=600s
  want=$(kubectl get nodes --no-headers | wc -l)
  for _ in $(seq 1 60); do
    ready=$(kubectl -n "$NS" get daemonset kepler -o jsonpath='{.status.numberReady}')
    [ "${ready:-0}" = "$want" ] && break; sleep 5
  done
  [ "${ready:-0}" = "$want" ] || { echo "Kepler ready on ${ready:-0} of $want nodes"; kubectl -n "$NS" get pods -o wide; exit 1; }
  # Kepler's own word that it reads the processor's counters (and not a standin meter) on the control plane
  cp_pod=$(kubectl -n "$NS" get pods -o json | jq -r '.items[] | select(.spec.nodeName | test("control-plane")) | .metadata.name' | head -n 1)
  for _ in $(seq 1 30); do
    kubectl get --raw "/api/v1/namespaces/$NS/pods/$cp_pod:28282/proxy/metrics" 2>/dev/null | grep '^kepler_node_cpu_joules_total' >/dev/null && break; sleep 5
  done
  kubectl get --raw "/api/v1/namespaces/$NS/pods/$cp_pod:28282/proxy/metrics" | grep '^kepler_node_cpu_joules_total' >/dev/null \
    || { echo "Kepler reports no node energy"; kubectl -n "$NS" logs "$cp_pod" --tail=60; exit 1; }
  kubectl -n "$NS" get pods -o json | jq -r '.items[].status.containerStatuses[]? | "\(.image) \(.imageID)"' | sort -u > "$OUT_DIR/kepler_pins.txt"
  { echo "kepler=$KEPLER_VERSION image=$KEPLER_IMAGE manifests=namespace:$SHA_NAMESPACE rbac:$SHA_RBAC configmap:$SHA_CONFIGMAP daemonset:$SHA_DAEMONSET service:$SHA_SERVICE"
    echo "kepler_nodes=$want meter=$(jq -c '{counted, virtualization}' "$OUT_DIR/meter_probe.json")"; } | tee -a "$OUT_DIR/addons.txt"
  exit 0
fi

if [ "$PHASE" = read ]; then
  TAG="${TAG:?set TAG=start or TAG=end}"
  kubectl -n "$NS" get pods -o json | jq -r '.items[] | "\(.metadata.name) \(.spec.nodeName)"' | while read -r pod node; do
    kubectl get --raw "/api/v1/namespaces/$NS/pods/$pod:28282/proxy/metrics" --request-timeout=20s 2>>"$OUT_DIR/kepler_reads.err" \
      | grep -E '^kepler_(node|pod)_' > "$OUT_DIR/kepler_${TAG}_${node}.prom" || true
  done
  date -u +%s.%N > "$OUT_DIR/kepler_${TAG}.time"
  exit 0
fi

if [ "$PHASE" = end ]; then
  kubectl -n "$NS" get pods -o name | while read -r p; do
    kubectl -n "$NS" logs "$p" --tail=100 --request-timeout=20s > "$OUT_DIR/kepler-$(basename "$p").log" 2>&1 || true
  done
  exit 0
fi
echo "PHASE must be install, read or end (got $PHASE)"; exit 1
