#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
#
# The batch queue under a queueing system of its own (docs/BATCH_QUEUE_PREREGISTRATION.md; register rows 63, 88, 89, 91, 92,
# 93): Kueue (Kubernetes SIG Scheduling, Apache-2.0), Volcano (the CNCF, Apache-2.0), the KAI scheduler (NVIDIA, Apache-2.0),
# Koordinator (the CNCF, Apache-2.0) or the Gödel scheduler (ByteDance, Apache-2.0) admits and places a stream of jobs, KubeRay
# (the Ray project, Apache-2.0) runs the same work as Ray jobs on one Ray cluster that the Ray autoscaler scales, or the
# Kubernetes scheduler alone places it,
# as shipped (vanilla) or with the operator's bin-packing profile (binpack), the same in every arm, installed from its own release on the fresh cluster of each
# arm before the arms are told apart. Native is the queueing system as its project ships it, on Kubernetes alone;
# Omni-Compass sits on top with its own levers and never writes the queueing system's objects.
#   PHASE=install  install it from its release (its SHA-256 pinned), every piece of it on the control plane (the measured
#                  workers carry only the work, as with every add-on), wait until it answers; (Kueue) the operator's
#                  queue: one ClusterQueue whose quota is the workers' allocatable CPU and memory, read live, and one
#                  LocalQueue; (Volcano, KAI) its default queues as shipped; (Koordinator) the operator's colocation
#                  profile, the jobs best effort on batch resources; (KubeRay) its operator, the Ray image loaded into
#                  every node, and the one Ray cluster, KubeRay's own autoscaling sample with the operator's settings,
#                  its head ready; (Gödel) its image, built by this runner from its pinned source
#                  (scripts/kind_godel_build.sh), loaded into the control plane and its own manifests applied; the
#                  stream's image pulled onto every worker
#   PHASE=submit   the stream: BATCH_JOBS jobs of BATCH_COMPLETIONS pods, BATCH_PARALLELISM at a time, one every
#                  BATCH_EVERY_S seconds from the window's opening, each pod hashing BATCH_MB MB; batch_done.txt when the
#                  last job has succeeded
#   PHASE=end      every job's and every pod's times (jobs.json, pods.json; KubeRay: every Ray job's, rayjobs.json, and
#                  its first and last task's, from its own driver's last line, ray_times.json) and the queueing system's
#                  own objects (batch_queue_end.json)
set -euo pipefail
OUT_DIR="${OUT_DIR:?}"
Q="${BATCH_QUEUE:?set BATCH_QUEUE=kueue, volcano, kai, koordinator, kuberay, godel, group, vanilla or binpack}"
KUEUE_VERSION="${KUEUE_VERSION:-v0.20.2}"       # released 15 October 2026
VOLCANO_VERSION="${VOLCANO_VERSION:-v1.16.0}"   # released 14 October 2026
KAI_VERSION="${KAI_VERSION:-v0.18.6}"           # released 15 October 2026 (its chart, oci://ghcr.io/kai-scheduler/...)
KOORD_VERSION="${KOORD_VERSION:-1.8.0}"         # released 16 April 2026 (its chart, from its charts repository's release)
KUBERAY_VERSION="${KUBERAY_VERSION:-1.7.1}"     # released 18 September 2026 (its operator's chart, from kuberay-helm's release)
RAY_IMAGE="rayproject/ray:2.52.0"               # the Ray its autoscaling sample names (rayVersion 2.52.0), amd64 893 MB packed
RAY_DIGEST="sha256:5c31da4180403f2d5f4590d05fbd46c1345e91e8d33dd4ff616de2702b611b31"   # that tag's index, pinned
# Gödel publishes no release: its source at this commit (its main branch on 20 October 2026), built by the runner from the
# project's own Dockerfile (scripts/kind_godel_build.sh, into GODEL_SRC, which records the image it built)
GODEL_COMMIT="${GODEL_COMMIT:-90de2d0dd7e8e4dc99ef36b34b91a30fc171b368}"
GODEL_SRC="${GODEL_SRC:-${RUNNER_TEMP:-/tmp}/godel-src}"
# each release file's SHA-256, pinned when this test was preregistered (a different version names its own)
KUEUE_SHA256="${KUEUE_SHA256:-1ab14ecd590575ac57f50fa4cbcf529766bc2c32ba974bda1614381281ec52b4}"     # manifests.yaml, v0.20.2
VOLCANO_SHA256="${VOLCANO_SHA256:-9aa62e15541f5e955d73353da9321ab233a2cbe0f8fbac4b4a4d38ba497303ee}" # volcano-development.yaml, v1.16.0
KAI_SHA256="${KAI_SHA256:-dff53248c4a044249a1f62ca8d35bd8dfc02719b99e302b35c69f946f4c5b7ff}"         # the chart archive, v0.18.6
KOORD_SHA256="${KOORD_SHA256:-766011e7c797a5b2ea0ed2091b31efb4eb16ba14699189db304022336fc48e06}"     # the chart archive, 1.8.0
KUBERAY_SHA256="${KUBERAY_SHA256:-fd057c207a6be038f2fe1475abb87f43a8c091b77f1f563b4e8547a2404b5bc8}" # the chart archive, 1.7.1
JOBS="${BATCH_JOBS:-24}"; COMPLETIONS="${BATCH_COMPLETIONS:-10}"; PARALLELISM="${BATCH_PARALLELISM:-5}"
EVERY="${BATCH_EVERY_S:-30}"; MB="${BATCH_MB:-3000}"
case "$Q" in kueue) NS=kueue-system ;; volcano) NS=volcano-system ;; kai) NS=kai-scheduler ;; koordinator) NS=koordinator-system ;;
  kuberay) NS=kuberay-system ;; godel) NS=godel-system ;; vanilla|binpack|group) NS=kube-system ;;
  *) echo "BATCH_QUEUE must be kueue, volcano, kai, koordinator, kuberay, godel, group, vanilla or binpack (got $Q)"; exit 1 ;; esac
# group: this cluster is one member of a group of clusters (scripts/kind_group.sh, docs/GROUP_PREREGISTRATION.md); the stream is
# sent to the group, by its orchestrator or, on the group alone, by the harness to each member in turn, never by this script;
# here it is the member's record of the jobs and pods that ran on it
# every serving pod of a Helm-installed system on the control plane: a pod a move replaced is given two minutes to finish
# on its worker; a finished install hook and a node agent of a DaemonSet are not counted, the same in both arms
off() { kubectl get pods -n "$NS" -o json | jq -r --argjson term "$1" '[.items[]
    | select(.status.phase == "Running" or .status.phase == "Pending")
    | select(([.metadata.ownerReferences[]?.kind] | index("DaemonSet")) | not)
    | select($term or .metadata.deletionTimestamp == null)
    | select((.spec.nodeName // "") | test("control-plane") | not) | .metadata.name] | join(" ")'; }
placed() {   # $1 the record file
  for _ in $(seq 1 24); do [ -z "$(off true)" ] && break; sleep 5; done
  away=$(off false)
  [ -z "$away" ] || { echo "INVALID RUN: $Q's pods on a measured worker: $away"; kubectl get pods -n "$NS" -o wide; exit 1; }
  kubectl get pods -n "$NS" -o wide >> "$1"
}

case "${PHASE:?set PHASE=install, submit or end}" in
install)
  W=$(mktemp -d)   # the release and its placed copy stay off the run's files (1 to 2 MB each); its SHA-256 is kept
  if [ "$Q" = kai ]; then
  # KAI's chart at its pinned version, its archive checked against the pinned SHA-256, installed by Helm with the chart's
  # own placement setting (deploy/kind/kai-values.yaml), which its operator applies to every component it runs; the
  # components stand once their number has held for half a minute and every one is available
  url="oci://ghcr.io/kai-scheduler/kai-scheduler/kai-scheduler"
  for t in 1 2 3; do
    helm pull "$url" --version "$KAI_VERSION" --destination "$W" > "$OUT_DIR/kai_chart_pull.log" 2>&1 && break
    [ "$t" = 3 ] && { echo "INVALID RUN: KAI's chart could not be fetched ($url $KAI_VERSION)"; cat "$OUT_DIR/kai_chart_pull.log"; exit 1; }; sleep 10
  done
  chart=$(ls "$W"/kai-scheduler-*.tgz | head -1)
  got=$(sha256sum "$chart" | cut -d' ' -f1)
  [ "$got" = "$KAI_SHA256" ] || { echo "INVALID RUN: KAI's chart is not the one pinned (sha256 $got, pinned $KAI_SHA256)"; exit 1; }
  helm install kai-scheduler "$chart" --namespace "$NS" --create-namespace -f deploy/kind/kai-values.yaml --wait --timeout 15m \
    > "$OUT_DIR/kai_helm.log" 2>&1 || { tail -40 "$OUT_DIR/kai_helm.log"; kubectl get pods -n "$NS" -o wide; exit 1; }
  last=-1; held=0
  for t in $(seq 1 90); do
    d=$(kubectl get deploy -n "$NS" -o json)
    n=$(echo "$d" | jq '.items | length')
    short=$(echo "$d" | jq '[.items[] | select((.status.availableReplicas // 0) < (.spec.replicas // 1))] | length')
    if [ "$n" = "$last" ] && [ "$short" = 0 ] && [ "$n" -ge 2 ]; then held=$((held + 1)); else held=0; fi
    last=$n
    [ "$held" -ge 3 ] && kubectl get queues.scheduling.run.ai default-queue -o name >/dev/null 2>&1 && break
    [ "$t" = 90 ] && { echo "INVALID RUN: KAI's components did not all stand within 15 minutes"; kubectl get deploy,pods -n "$NS" -o wide; exit 1; }
    sleep 10
  done
  # a deployment the chart's setting does not reach is placed on the control plane after install, as CruiseKube's are
  for dep in $(kubectl get deploy -n "$NS" -o json | jq -r '.items[] | select((.spec.template.spec.nodeSelector // {}) | has("node-role.kubernetes.io/control-plane") | not) | .metadata.name'); do
    kubectl patch -n "$NS" "deployment/$dep" --type=merge -p '{"spec":{"template":{"spec":{"nodeSelector":{"node-role.kubernetes.io/control-plane":""},"tolerations":[{"key":"node-role.kubernetes.io/control-plane","operator":"Exists","effect":"NoSchedule"},{"key":"node-role.kubernetes.io/master","operator":"Exists","effect":"NoSchedule"}]}}}}' >/dev/null
    kubectl rollout status -n "$NS" "deployment/$dep" --timeout=300s >/dev/null
    echo "placed on the control plane after install: $dep" >> "$OUT_DIR/kai_placement.txt"
  done
  placed "$OUT_DIR/kai_placement.txt"
  elif [ "$Q" = koordinator ]; then
  # the archive is asked for with the patience the group rig gives the metrics-server manifest (scripts/kind_group.sh): on
  # 8 November GitHub's release download answered 504 for this archive from about 07:00 to 10:30 UTC, and a fetch that gave up
  # inside a minute marked every arm with Koordinator invalid in runs 42457078253 and 42461424873; nothing is measured yet here
  # Koordinator's chart at its pinned version, the release archive checked against its pinned SHA-256, installed by Helm as
  # its own guide installs it, with the operator's two settings for one control plane (deploy/kind/koordinator-values.yaml)
  url="https://github.com/koordinator-sh/charts/releases/download/koordinator-${KOORD_VERSION}/koordinator-${KOORD_VERSION}.tgz"
  for t in 1 2 3; do
    curl -fsSL --retry 8 --retry-all-errors --retry-delay 15 -o "$W/chart.tgz" "$url" && break
    [ "$t" = 3 ] && { echo "INVALID RUN: Koordinator's chart could not be fetched ($url)"; exit 1; }; sleep 10
  done
  got=$(sha256sum "$W/chart.tgz" | cut -d' ' -f1)
  [ "$got" = "$KOORD_SHA256" ] || { echo "INVALID RUN: Koordinator's chart is not the one pinned (sha256 $got, pinned $KOORD_SHA256)"; exit 1; }
  # koordlet's own words when it does not stand, kept in the run's files (the last start's and the one before)
  koordlet_logs() { { kubectl -n "$NS" logs daemonset/koordlet --previous --tail=80 2>&1 || true
                      kubectl -n "$NS" logs daemonset/koordlet --tail=80 2>&1 || true; } > "$OUT_DIR/koordlet.log"
                    tail -30 "$OUT_DIR/koordlet.log"; }
  helm install koordinator "$W/chart.tgz" -f deploy/kind/koordinator-values.yaml --wait --timeout 15m \
    > "$OUT_DIR/koord_helm.log" 2>&1 || { tail -40 "$OUT_DIR/koord_helm.log"; kubectl get pods -n "$NS" -o wide; koordlet_logs; exit 1; }
  kubectl wait -n "$NS" --for=condition=Available deploy --all --timeout=600s >/dev/null
  kubectl -n "$NS" rollout status daemonset/koordlet --timeout=600s >/dev/null \
    || { echo "INVALID RUN: koordlet did not run on every node"; kubectl get pods -n "$NS" -o wide; koordlet_logs; exit 1; }
  placed "$OUT_DIR/koord_placement.txt"
  # the operator's colocation profile, as Koordinator's colocation guide writes it, on the namespace the jobs run in
  kubectl label namespace default koordinator.sh/enable-colocation=true --overwrite >/dev/null
  for t in $(seq 1 20); do
    kubectl apply -f deploy/kind/koordinator-colocation.yaml >/dev/null 2>&1 && break
    [ "$t" = 20 ] && { echo "INVALID RUN: Koordinator's colocation profile was refused"; exit 1; }; sleep 6
  done
  # its webhook mutates before the window opens: a server-side dry run of a labelled pod comes back best effort, for
  # koord-scheduler, on batch resources (the webhook fails open, so an unready one would let the stream through untouched)
  printf '%s\n' 'apiVersion: v1' 'kind: Pod' \
    'metadata: {name: omni-colocation-probe, namespace: default, labels: {koordinator.sh/enable-colocation: "true"}}' \
    'spec: {containers: [{name: probe, image: "busybox:1.36", resources: {requests: {cpu: 500m, memory: 64Mi}, limits: {cpu: "1", memory: 64Mi}}}]}' \
    > "$W/probe.yaml"
  for t in $(seq 1 30); do
    m=$( { kubectl create --dry-run=server -o json -f "$W/probe.yaml" 2>/dev/null \
           | jq -r '[.spec.schedulerName, (.metadata.labels["koordinator.sh/qosClass"] // "-"), (.spec.containers[0].resources.requests["kubernetes.io/batch-cpu"] // "-")] | join(" ")'; } || true )
    case "$m" in "koord-scheduler BE "[0-9]*) break ;; esac
    [ "$t" = 30 ] && { echo "INVALID RUN: Koordinator's colocation profile did not mutate a labelled pod (got: $m)"; exit 1; }
    sleep 10
  done
  echo "colocation probe (scheduler, QoS class, batch-cpu asked): $m" >> "$OUT_DIR/koord_placement.txt"
  elif [ "$Q" = kuberay ]; then
  # KubeRay's operator chart at its pinned version, the release archive checked against its pinned SHA-256, installed by Helm
  # with the chart's own placement settings (deploy/kind/kuberay-values.yaml)
  url="https://github.com/ray-project/kuberay-helm/releases/download/kuberay-operator-${KUBERAY_VERSION}/kuberay-operator-${KUBERAY_VERSION}.tgz"
  for t in 1 2 3; do
    curl -fsSL --retry 8 --retry-all-errors --retry-delay 15 -o "$W/chart.tgz" "$url" && break
    [ "$t" = 3 ] && { echo "INVALID RUN: KubeRay's chart could not be fetched ($url)"; exit 1; }; sleep 10
  done
  got=$(sha256sum "$W/chart.tgz" | cut -d' ' -f1)
  [ "$got" = "$KUBERAY_SHA256" ] || { echo "INVALID RUN: KubeRay's chart is not the one pinned (sha256 $got, pinned $KUBERAY_SHA256)"; exit 1; }
  helm install kuberay-operator "$W/chart.tgz" --namespace "$NS" --create-namespace -f deploy/kind/kuberay-values.yaml --wait --timeout 10m \
    > "$OUT_DIR/kuberay_helm.log" 2>&1 || { tail -40 "$OUT_DIR/kuberay_helm.log"; kubectl get pods -n "$NS" -o wide; exit 1; }
  placed "$OUT_DIR/kuberay_placement.txt"
  # the Ray image by its pinned digest, pulled once by this runner (the first arm that needs it), then loaded into every
  # node of this arm's fresh cluster: no node downloads it, so a job's wait is never a download on the one shared machine
  docker image inspect "rayproject/ray@${RAY_DIGEST}" >/dev/null 2>&1 || {
    for t in 1 2 3; do docker pull -q "rayproject/ray@${RAY_DIGEST}" > "$OUT_DIR/ray_image_pull.log" 2>&1 && break
      [ "$t" = 3 ] && { echo "INVALID RUN: the Ray image could not be pulled ($RAY_DIGEST)"; cat "$OUT_DIR/ray_image_pull.log"; exit 1; }; sleep 20
    done; }
  docker tag "rayproject/ray@${RAY_DIGEST}" "$RAY_IMAGE"
  kind load docker-image "$RAY_IMAGE" --name "${KIND_CLUSTER:-omni-bench}" > "$OUT_DIR/ray_image_load.log" 2>&1 \
    || { echo "INVALID RUN: the Ray image could not be loaded into the cluster's nodes"; tail -20 "$OUT_DIR/ray_image_load.log"; exit 1; }
  # the stream's job script on the head, then the one Ray cluster: KubeRay's own autoscaling sample with the operator's
  # settings (deploy/kind/kuberay-cluster.yaml), its worker group's ceiling the workers' allocatable processors over one
  # worker pod's half, and no more workers of 1 GiB each than the one machine has free less 3 GiB kept for the head and the
  # systems, both read live (every kind node reports the whole machine's memory as its own, so Kubernetes alone would admit
  # more workers than the machine holds: the trial of 20 October took the runner down, amendment 9); it stands once its head
  # answers
  kubectl create configmap omni-ray-stream --from-file=stream_job.py=deploy/kind/kuberay_stream_job.py --dry-run=client -o yaml \
    | kubectl apply -f - >/dev/null
  max=$(kubectl get nodes -l '!node-role.kubernetes.io/control-plane' -o json | python3 -c '
import json, sys
def cpu(v): return float(v[:-1]) / 1000 if v.endswith("m") else float(v)
by_cpu = int(sum(cpu(x["status"]["allocatable"]["cpu"]) for x in json.load(sys.stdin)["items"]) / 0.5)
free_gib = next(int(l.split()[1]) for l in open("/proc/meminfo") if l.startswith("MemAvailable:")) / 2 ** 20
by_mem = int(free_gib - 3)                       # a worker is 1 GiB; 3 GiB stay for the head and the systems
print(max(1, min(by_cpu, by_mem)))')
  for t in $(seq 1 20); do
    sed "s/MAX_WORKERS/${max}/" deploy/kind/kuberay-cluster.yaml | kubectl apply -f - >/dev/null 2>&1 && break
    [ "$t" = 20 ] && { echo "INVALID RUN: the Ray cluster was refused"; exit 1; }; sleep 6
  done
  for t in $(seq 1 60); do
    head=$(kubectl get pods -l ray.io/cluster=omni-ray,ray.io/node-type=head -o jsonpath='{.items[0].metadata.name}' 2>/dev/null || true)
    [ -n "$head" ] && kubectl wait --for=condition=Ready "pod/$head" --timeout=10s >/dev/null 2>&1 \
      && kubectl exec "$head" -c ray-head -- ray status > "$OUT_DIR/ray_status_start.txt" 2>&1 && break
    [ "$t" = 60 ] && { echo "INVALID RUN: the Ray cluster's head did not answer in 10 minutes"; kubectl get raycluster,pods -o wide; exit 1; }
    sleep 10
  done
  node=$(kubectl get "pod/$head" -o jsonpath='{.spec.nodeName}')
  case "$node" in *control-plane*) ;; *) echo "INVALID RUN: the Ray head is not on the control plane ($node)"; exit 1 ;; esac
  elif [ "$Q" = godel ]; then
  # Gödel as its own setup guide installs it on a cluster of its own: the image built from the pinned source (the same image
  # in every arm of the job) loaded into the control plane, where its own manifests place every one of its components (its
  # scheduler, dispatcher, binder and controller manager), then its CRDs, roles and deployments applied from that source
  # (kustomize, manifests/base), as shipped; it stands once every component is available
  [ "$(git -C "$GODEL_SRC" rev-parse HEAD 2>/dev/null)" = "$GODEL_COMMIT" ] || { echo "INVALID RUN: Gödel's source is not the pinned commit $GODEL_COMMIT"; exit 1; }
  img=$(docker image inspect godel-local:latest --format '{{.Id}}' 2>/dev/null || true)
  [ -n "$img" ] && [ "$img" = "$(cat "$GODEL_SRC/IMAGE_ID" 2>/dev/null)" ] \
    || { echo "INVALID RUN: the image godel-local:latest is not the one built from the pinned source (${img:-none})"; exit 1; }
  kind load docker-image godel-local:latest --name "${KIND_CLUSTER:-omni-bench}" --nodes "${KIND_CLUSTER:-omni-bench}-control-plane" \
    > "$OUT_DIR/godel_image_load.log" 2>&1 || { echo "INVALID RUN: Gödel's image could not be loaded into the control plane"; tail -20 "$OUT_DIR/godel_image_load.log"; exit 1; }
  for t in 1 2 3; do   # server-side: its custom resource definitions are larger than a client-side apply may annotate
    kubectl apply --server-side -k "$GODEL_SRC/manifests/base" > "$OUT_DIR/godel_apply.log" 2>&1 && break
    [ "$t" = 3 ] && { echo "INVALID RUN: Gödel's manifests could not be applied"; tail -20 "$OUT_DIR/godel_apply.log"; exit 1; }; sleep 10
  done
  kubectl wait -n "$NS" --for=condition=Available deploy --all --timeout=600s >/dev/null \
    || { echo "INVALID RUN: Gödel's components did not all stand"; kubectl get deploy,pods -n "$NS" -o wide; exit 1; }
  placed "$OUT_DIR/godel_placement.txt"
  url="kubewharf/godel-scheduler at $GODEL_COMMIT, built from its own docker/godel-local.Dockerfile"; got="$img"
  elif [ "$Q" = group ]; then
  # a member of a group of clusters: nothing is installed here; the group's orchestrator, where there is one, runs on its
  # own cluster beside the members (scripts/kind_group.sh), and this member's own scheduler places every pod sent to it
  url="the group's (scripts/kind_group.sh)"
  got=$(kubectl -n kube-system get pod -l component=kube-scheduler -o jsonpath='{.items[0].spec.containers[0].image}')
  elif [ "$Q" = vanilla ]; then
  # the Kubernetes scheduler as shipped: nothing is installed; the cluster's own default scheduler places the stream
  url="the cluster's own default scheduler"
  got=$(kubectl -n kube-system get pod -l component=kube-scheduler -o jsonpath='{.items[0].spec.containers[0].image}')
  elif [ "$Q" = binpack ]; then
  # the operator's bin-packing profile: a second scheduler from the cluster's own release (the image the control plane
  # already runs), its one profile scoring a node higher the fuller it is (deploy/kind/binpack-scheduler.yaml)
  img=$(kubectl -n kube-system get pod -l component=kube-scheduler -o jsonpath='{.items[0].spec.containers[0].image}')
  [ -n "$img" ] || { echo "INVALID RUN: the control plane's scheduler image could not be read"; exit 1; }
  sed "s|KUBE_SCHEDULER_IMAGE|${img}|" deploy/kind/binpack-scheduler.yaml | kubectl apply -f - >/dev/null
  kubectl -n kube-system rollout status deployment/omni-binpack-scheduler --timeout=300s >/dev/null \
    || { echo "INVALID RUN: the bin-packing scheduler did not start"; kubectl -n kube-system get pods -l app=omni-binpack-scheduler -o wide; exit 1; }
  node=$(kubectl -n kube-system get pods -l app=omni-binpack-scheduler -o jsonpath='{.items[0].spec.nodeName}')
  case "$node" in *control-plane*) ;; *) echo "INVALID RUN: the bin-packing scheduler is not on the control plane ($node)"; exit 1 ;; esac
  url="deploy/kind/binpack-scheduler.yaml, the image $img"
  got=$(sha256sum deploy/kind/binpack-scheduler.yaml | cut -d' ' -f1)
  else
  # the project's own release file, fetched whole and checked against its pinned SHA-256; every Deployment and Job of the
  # queueing system is placed on the control plane before the file is applied (Volcano's certificate Job ships with no
  # placement and would otherwise run once on a measured worker), the file otherwise applied as shipped
  if [ "$Q" = kueue ]; then url="https://github.com/kubernetes-sigs/kueue/releases/download/${KUEUE_VERSION}/manifests.yaml"
  else url="https://raw.githubusercontent.com/volcano-sh/volcano/${VOLCANO_VERSION}/installer/volcano-development.yaml"; fi
  for t in 1 2 3; do
    curl -fsSL --retry 3 -o "$W/release.yaml" "$url" && break
    [ "$t" = 3 ] && { echo "INVALID RUN: $Q's release file could not be fetched ($url)"; exit 1; }; sleep 10
  done
  want="$VOLCANO_SHA256"; [ "$Q" = kueue ] && want="$KUEUE_SHA256"
  got=$(sha256sum "$W/release.yaml" | cut -d' ' -f1)
  [ "$got" = "$want" ] || { echo "INVALID RUN: $Q's release file is not the one pinned (sha256 $got, pinned $want)"; exit 1; }
  python3 - "$W/release.yaml" "$NS" > "$W/applied.yaml" <<'PY'
import sys, yaml
docs = [d for d in yaml.safe_load_all(open(sys.argv[1])) if d]
for d in docs:
    if d.get("kind") in ("Deployment", "Job", "DaemonSet", "StatefulSet") and d["metadata"].get("namespace") == sys.argv[2]:
        spec = d["spec"]["template"]["spec"]
        spec["nodeSelector"] = {**(spec.get("nodeSelector") or {}), "node-role.kubernetes.io/control-plane": ""}
        spec["tolerations"] = (spec.get("tolerations") or []) + [
            {"key": "node-role.kubernetes.io/control-plane", "operator": "Exists", "effect": "NoSchedule"},
            {"key": "node-role.kubernetes.io/master", "operator": "Exists", "effect": "NoSchedule"}]
print(yaml.safe_dump_all(docs, sort_keys=False), end="")
PY
  for t in 1 2 3; do   # server-side: the custom resource definitions are larger than a client-side apply may annotate
    kubectl apply --server-side -f "$W/applied.yaml" >/dev/null && break
    [ "$t" = 3 ] && { echo "INVALID RUN: $Q could not be applied"; exit 1; }; sleep 10
  done
  kubectl wait -n "$NS" --for=condition=Available deploy --all --timeout=600s >/dev/null
  [ "$Q" = kueue ] || kubectl wait -n "$NS" --for=condition=complete job --all --timeout=600s >/dev/null
  away=$(kubectl get pods -n "$NS" -o json | jq '[.items[] | select(.spec.nodeName != null and (.spec.nodeName | test("control-plane") | not))] | length')
  [ "$away" = 0 ] || { echo "INVALID RUN: $away of $Q's pods are not on the control plane"; kubectl get pods -n "$NS" -o wide; exit 1; }
  fi
  if [ "$Q" = kueue ]; then
    # the operator's queue, as Kueue's own single-ClusterQueue setup writes it, its quota the workers' capacity read live;
    # the API version is the one the installed release serves first
    ver=$(kubectl get --raw /apis/kueue.x-k8s.io | jq -r '.preferredVersion.groupVersion')
    read -r cpu mem < <(kubectl get nodes -l '!node-role.kubernetes.io/control-plane' -o json | python3 -c '
import json, sys
def cpu(v): return float(v[:-1]) / 1000 if v.endswith("m") else float(v)
def mib(v):
    for s, f in (("Ki", 1 / 1024), ("Mi", 1), ("Gi", 1024), ("Ti", 1024 ** 2)):
        if v.endswith(s): return float(v[:-2]) * f
    return float(v) / 2 ** 20
n = json.load(sys.stdin)["items"]
c = sum(cpu(x["status"]["allocatable"]["cpu"]) for x in n)
m = int(sum(mib(x["status"]["allocatable"]["memory"]) for x in n))
print("%g %dMi" % (c, m))')
    for t in $(seq 1 20); do   # the webhook answers a little after its deployment is Available
      kubectl apply -f - >/dev/null 2>&1 <<EOF && break
apiVersion: ${ver}
kind: ResourceFlavor
metadata: {name: default-flavor}
---
apiVersion: ${ver}
kind: ClusterQueue
metadata: {name: omni-cluster-queue}
spec:
  namespaceSelector: {}
  resourceGroups:
    - coveredResources: ["cpu", "memory"]
      flavors:
        - name: default-flavor
          resources:
            - {name: cpu, nominalQuota: "${cpu}"}
            - {name: memory, nominalQuota: "${mem}"}
---
apiVersion: ${ver}
kind: LocalQueue
metadata: {namespace: default, name: omni-queue}
spec: {clusterQueue: omni-cluster-queue}
EOF
      [ "$t" = 20 ] && { echo "INVALID RUN: Kueue's queue objects were refused"; exit 1; }; sleep 6
    done
    echo "kueue ${KUEUE_VERSION} (${ver}); ClusterQueue quota cpu ${cpu}, memory ${mem}" > "$OUT_DIR/batch_queue.txt"
  elif [ "$Q" = group ]; then
    echo "group: a member of a group of clusters ${KIND_CLUSTER:-}; the stream sent by the group, this member's scheduler as shipped ($got)" > "$OUT_DIR/batch_queue.txt"
  elif [ "$Q" = vanilla ]; then
    echo "vanilla: the Kubernetes scheduler as shipped ($got), no queueing system" > "$OUT_DIR/batch_queue.txt"
  elif [ "$Q" = binpack ]; then
    echo "binpack: a second scheduler from the cluster's release with the operator's bin-packing profile (MostAllocated)" > "$OUT_DIR/batch_queue.txt"
  elif [ "$Q" = koordinator ]; then
    echo "koordinator ${KOORD_VERSION}; the operator's colocation profile (deploy/kind/koordinator-colocation.yaml), the jobs best effort on batch resources" > "$OUT_DIR/batch_queue.txt"
    kubectl get nodes -o json | jq '[.items[] | {node: .metadata.name, batch_cpu: .status.allocatable["kubernetes.io/batch-cpu"], batch_memory: .status.allocatable["kubernetes.io/batch-memory"]}]' \
      > "$OUT_DIR/koord_batch_allocatable_start.json" || true
  elif [ "$Q" = kuberay ]; then
    echo "kuberay ${KUBERAY_VERSION}; one Ray cluster (Ray 2.52.0, $(docker image inspect "$RAY_IMAGE" --format '{{index .RepoDigests 0}}')), KubeRay's autoscaling sample, its worker group up to ${max} pods" > "$OUT_DIR/batch_queue.txt"
    kubectl get raycluster omni-ray -o json > "$OUT_DIR/raycluster_start.json"
  elif [ "$Q" = godel ]; then
    echo "godel ${GODEL_COMMIT}; its scheduler, dispatcher, binder and controller manager as its own manifests deploy them" > "$OUT_DIR/batch_queue.txt"
  elif [ "$Q" = kai ]; then
    echo "kai ${KAI_VERSION}; its chart's default queues as shipped ($(kubectl get queues.scheduling.run.ai -o jsonpath='{range .items[*]}{.metadata.name} {end}'))" > "$OUT_DIR/batch_queue.txt"
    kubectl get queues.scheduling.run.ai -o json > "$OUT_DIR/kai_queues.json"
  else
    for t in $(seq 1 20); do   # Volcano's own default queue, as shipped, made by its controllers once they run
      kubectl get queues.scheduling.volcano.sh default -o name >/dev/null 2>&1 && break
      [ "$t" = 20 ] && { echo "INVALID RUN: Volcano's default queue never appeared"; exit 1; }; sleep 6
    done
    echo "volcano ${VOLCANO_VERSION}; the default queue as shipped" > "$OUT_DIR/batch_queue.txt"
  fi
  case "$Q" in
    vanilla|group) ;;
    binpack) echo "the scheduler's manifest: $url; its SHA-256 $got" >> "$OUT_DIR/batch_queue.txt" ;;
    godel) echo "source $url; image $got" >> "$OUT_DIR/batch_queue.txt" ;;
    *) echo "release $url sha256 $got (the pinned file)" >> "$OUT_DIR/batch_queue.txt" ;;
  esac
  # the stream's image on every worker before the window, as the served image is (deploy/kind/prepull.yaml): a job's wait is
  # the queueing system's and the scheduler's, never a download on the one machine all kind nodes share
  kubectl apply -f - >/dev/null <<'EOF'
apiVersion: apps/v1
kind: DaemonSet
metadata: {name: rig-prepull-batch, namespace: kube-system, labels: {app: rig-prepull-batch}}
spec:
  selector: {matchLabels: {app: rig-prepull-batch}}
  template:
    metadata: {labels: {app: rig-prepull-batch}}
    spec:
      terminationGracePeriodSeconds: 0
      initContainers:
        - {name: stream, image: "busybox:1.36", command: ["true"], resources: {requests: {cpu: 1m, memory: 8Mi}}}
      containers:
        - {name: done, image: "registry.k8s.io/pause:3.10", resources: {requests: {cpu: 1m, memory: 4Mi}}}
EOF
  # (the image is already on every node when the runner's copy was loaded into the cluster, scripts/kind_bench.sh; a pull
  # that still never finishes leaves what each puller pod says in the arm's own files)
  kubectl -n kube-system rollout status daemonset/rig-prepull-batch --timeout=300s >/dev/null \
    || { { kubectl -n kube-system get pods -l app=rig-prepull-batch -o wide; kubectl -n kube-system describe pods -l app=rig-prepull-batch; } \
           > "$OUT_DIR/prepull_batch_failed.txt" 2>&1 || true
         echo "INVALID RUN: the stream's image was not pulled onto every worker (prepull_batch_failed.txt)"; exit 1; }
  kubectl -n kube-system delete daemonset rig-prepull-batch --wait=true --timeout=120s >/dev/null
  kubectl -n kube-system wait --for=delete pod -l app=rig-prepull-batch --timeout=120s >/dev/null 2>&1 || true
  echo "busybox:1.36 pre-pulled on every worker" >> "$OUT_DIR/batch_queue.txt"
  kubectl get deploy -n "$NS" -o jsonpath='{range .items[*]}{.metadata.name}={.spec.template.spec.containers[0].image}{"\n"}{end}' >> "$OUT_DIR/batch_queue.txt"
  cat "$OUT_DIR/batch_queue.txt"
  ;;
submit)
  [ "$Q" = group ] && exit 0   # the group sends the stream (scripts/kind_group.sh)
  START=$(date -u +%s); label=""; podlabel=""; sched=""; podann=""
  if [ "$Q" = kuberay ]; then
    # the same stream as Ray jobs: one RayJob of the same tasks every BATCH_EVERY_S seconds, sent to the one Ray cluster by
    # KubeRay's operator (deploy/kind/kuberay-job.yaml); batch_done.txt once every Ray job has succeeded
    for i in $(seq 1 "$JOBS"); do
      sed -e "s/JOB_NAME/omni-ray-$(printf %03d "$i")/" -e "s/BATCH_COMPLETIONS/${COMPLETIONS}/" -e "s/BATCH_PARALLELISM/${PARALLELISM}/" \
          -e "s/BATCH_MB/${MB}/" deploy/kind/kuberay-job.yaml > "$OUT_DIR/job.yaml"
      for t in 1 2 3 4 5 6; do kubectl apply -f "$OUT_DIR/job.yaml" --request-timeout=20s >/dev/null && break; sleep 5; done
      echo "$(date -u +%s) submitted omni-ray-$(printf %03d "$i")" >> "$OUT_DIR/batch_submit.log"
      [ "$i" = "$JOBS" ] || sleep "$EVERY"
    done
    until [ "$(kubectl get rayjobs -l app=omni-ray-stream -o json --request-timeout=20s 2>/dev/null \
              | jq '[.items[] | select(.status.jobStatus == "SUCCEEDED")] | length')" = "$JOBS" ]; do
      [ "$(date -u +%s)" -lt "$(( START + ${DURATION:?} ))" ] || exit 0; sleep 5
    done
    date -u +%s > "$OUT_DIR/batch_done.txt"
    exit 0
  fi
  [ "$Q" = kueue ] && label="kueue.x-k8s.io/queue-name: omni-queue"
  [ "$Q" = volcano ] && sched="schedulerName: volcano"
  [ "$Q" = kai ] && { label="kai.scheduler/queue: default-queue"; podlabel="$label"; sched="schedulerName: kai-scheduler"; }
  [ "$Q" = koordinator ] && { label='koordinator.sh/enable-colocation: "true"'; podlabel="$label"; }   # the profile sets the rest
  [ "$Q" = binpack ] && sched="schedulerName: binpack-scheduler"
  # Gödel: its scheduler's name and the three annotations its own guide puts on every pod it schedules
  [ "$Q" = godel ] && { sched="schedulerName: godel-scheduler"
    podann=", annotations: {godel.bytedance.com/pod-state: pending, godel.bytedance.com/pod-resource-type: guaranteed, godel.bytedance.com/pod-launcher: kubelet}"; }
  for i in $(seq 1 "$JOBS"); do
    sed -e "s/JOB_NAME/omni-batch-$(printf %03d "$i")/" -e "s/BATCH_COMPLETIONS/${COMPLETIONS}/" -e "s/BATCH_PARALLELISM/${PARALLELISM}/" \
        -e "s/BATCH_MB/${MB}/" -e "s|, POD_QUEUE_LABEL}}|, POD_QUEUE_LABEL}${podann}}|" \
        -e "s|POD_QUEUE_LABEL|${podlabel:-omni-stream: \"1\"}|" -e "s|QUEUE_LABEL|${label:-omni-stream: \"1\"}|" \
        -e "s|SCHEDULER_LINE|${sched:-terminationGracePeriodSeconds: 30}|" \
        deploy/kind/batch-stream-job.yaml > "$OUT_DIR/job.yaml"
    for t in 1 2 3 4 5 6; do kubectl apply -f "$OUT_DIR/job.yaml" --request-timeout=20s >/dev/null && break; sleep 5; done
    echo "$(date -u +%s) submitted omni-batch-$(printf %03d "$i")" >> "$OUT_DIR/batch_submit.log"
    [ "$i" = "$JOBS" ] || sleep "$EVERY"
  done
  # batch_done.txt once the last job has succeeded; the wait ends with the window (DURATION from its opening), so a stream
  # not done in the window leaves no time written and the scorer counts the window's end
  until [ "$(kubectl get jobs -l app=omni-batch-stream -o json --request-timeout=20s 2>/dev/null \
            | jq '[.items[] | select((.status.succeeded // 0) >= .spec.completions)] | length')" = "$JOBS" ]; do
    [ "$(date -u +%s)" -lt "$(( START + ${DURATION:?} ))" ] || exit 0; sleep 5
  done
  date -u +%s > "$OUT_DIR/batch_done.txt"
  ;;
end)
  if [ "$Q" = kuberay ]; then
    # every Ray job as KubeRay recorded it, and each one's first and last task from its own driver's last line (the head's
    # job logs), in ray_times.json; the cluster as the window left it
    kubectl get rayjobs -l app=omni-ray-stream -o json > "$OUT_DIR/rayjobs.json" 2>/dev/null || echo '{"items": []}' > "$OUT_DIR/rayjobs.json"
    kubectl get raycluster omni-ray -o json > "$OUT_DIR/batch_queue_end.json" 2>/dev/null || true
    kubectl get pods -l ray.io/cluster=omni-ray -o json > "$OUT_DIR/ray_pods.json" 2>/dev/null || echo '{"items": []}' > "$OUT_DIR/ray_pods.json"
    head=$(kubectl get pods -l ray.io/cluster=omni-ray,ray.io/node-type=head -o jsonpath='{.items[0].metadata.name}' 2>/dev/null || true)
    : > "$OUT_DIR/ray_job_logs.txt"
    for id in $(jq -r '.items[] | .status.jobId // empty' "$OUT_DIR/rayjobs.json"); do
      echo "== $id" >> "$OUT_DIR/ray_job_logs.txt"
      kubectl exec "$head" -c ray-head -- ray job logs --address http://127.0.0.1:8265 "$id" 2>&1 | tail -5 >> "$OUT_DIR/ray_job_logs.txt" || true
    done
    python3 - "$OUT_DIR" <<'PY'
import json, sys
from pathlib import Path
d = Path(sys.argv[1]); times, cur = {}, None
for ln in (d / "ray_job_logs.txt").read_text(errors="replace").splitlines():
    if ln.startswith("== "):
        cur = ln[3:].strip()
    elif cur and ln.startswith("OMNI_TIMES "):
        times[cur] = json.loads(ln[len("OMNI_TIMES "):])
out = []
for j in json.loads((d / "rayjobs.json").read_text()).get("items", []):
    st = j.get("status") or {}
    t = times.get(st.get("jobId") or "", {})
    out.append({"name": j["metadata"]["name"], "submitted": j["metadata"]["creationTimestamp"], "status": st.get("jobStatus"),
                "end": st.get("endTime"), "first_task": t.get("first"), "last_task": t.get("last"), "tasks": t.get("tasks")})
(d / "ray_times.json").write_text(json.dumps({"items": out}, indent=1) + "\n")
PY
    echo '{"items": []}' > "$OUT_DIR/jobs.json"; echo '{"items": []}' > "$OUT_DIR/pods.json"
    exit 0
  fi
  kubectl get jobs -l app=omni-batch-stream -o json > "$OUT_DIR/jobs.json" 2>/dev/null || echo '{"items": []}' > "$OUT_DIR/jobs.json"
  kubectl get pods -l app=omni-batch-stream -o json > "$OUT_DIR/pods.json" 2>/dev/null || echo '{"items": []}' > "$OUT_DIR/pods.json"
  if [ "$Q" = kueue ]; then
    kubectl get clusterqueues,localqueues,workloads -A -o json > "$OUT_DIR/batch_queue_end.json" 2>/dev/null || true
  elif [ "$Q" = kai ]; then
    kubectl get queues.scheduling.run.ai,podgroups.scheduling.run.ai -A -o json > "$OUT_DIR/batch_queue_end.json" 2>/dev/null || true
  elif [ "$Q" = godel ]; then   # where Gödel put every pod, node by node, and its components' last words
    jq '[.items[] | .spec.nodeName] | group_by(.) | map({node: .[0], pods: length})' "$OUT_DIR/pods.json" > "$OUT_DIR/batch_queue_end.json" 2>/dev/null || true
    for d in scheduler dispatcher binder controller-manager; do
      kubectl -n "$NS" logs "deployment/$d" --tail=200 --request-timeout=20s > "$OUT_DIR/godel_$d.log" 2>&1 || true
    done
  elif [ "$Q" = vanilla ] || [ "$Q" = binpack ] || [ "$Q" = group ]; then   # where the scheduler put every pod, node by node
    jq '[.items[] | .spec.nodeName] | group_by(.) | map({node: .[0], pods: length})' "$OUT_DIR/pods.json" > "$OUT_DIR/batch_queue_end.json" 2>/dev/null || true
  elif [ "$Q" = koordinator ]; then   # every node's batch resources as the window left them, and koordlet's own node metrics
    kubectl get nodes -o json | jq '[.items[] | {node: .metadata.name, batch_cpu: .status.allocatable["kubernetes.io/batch-cpu"], batch_memory: .status.allocatable["kubernetes.io/batch-memory"]}]' \
      > "$OUT_DIR/batch_queue_end.json" 2>/dev/null || true
    kubectl get nodemetrics.slo.koordinator.sh -o json > "$OUT_DIR/koord_nodemetrics_end.json" 2>/dev/null || true
  else
    kubectl get queues,podgroups -A -o json > "$OUT_DIR/batch_queue_end.json" 2>/dev/null || true
  fi
  ;;
*) echo "PHASE must be install, submit or end"; exit 1 ;;
esac

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
