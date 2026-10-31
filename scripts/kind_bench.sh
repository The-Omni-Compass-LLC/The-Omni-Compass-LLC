#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# One arm of the native-vs-Omni benchmark on the six-worker kind cluster (deploy/kind/cluster-full.yaml).
# Both arms are wired identically: same cluster, add-ons, workload, HPA (target 50), load schedule, capture and
# power model. The only difference:
#   ARM=native  Omni-Compass is not started at all. Kubernetes (HPA, scheduler) runs alone on all workers.
#   ARM=omni    Omni-Compass runs in nodepool mode with every live muscle: HPA target, node pool (prefer-not idle mark, first-to-go order),
#               power cap (CPU limit of php-apache, enforced by the kernel), heat (harness law on live power), security
#               (ConfigMap hold), rollout guard, and the latency afferent: 95th-percentile response time over SLO_MS
#               (declared before the run, default 500 ms) enters the engine as queue pressure. The power cap never goes
#               below pod usage x 1.3. Parked workers stay powered and Ready at their idle floor (STANDBY_W =
#               park_frac x idle, never off).
#   ARM=watch   Omni-Compass runs exactly as in ARM=omni (same process, same reads, same senses, same decisions) with
#               --dry-run: every write is logged, none is executed. Any difference from native in this arm is the cost of
#               Omni-Compass being there (its CPU on the shared runner, its API reads) plus run-to-run noise, never a
#               decision. The run fails if one write reached the cluster.
# The controller runs at the lowest CPU priority (nice 19) in every Omni arm: on a real cluster it runs on its own node,
# here all seven kind nodes share one 4-core runner with the service being measured. With the organism inside (ORGANISM
# set) it runs at the organism's own priority instead (nice 0; amendment of 12 Oct): the modelled organism is the
# heaviest process of the test rig on the runner, and a governor ranked below the rig is starved by the rig itself (the
# four stacked at 100 copies: 47 of the governor's 60 decisions by the end of its window). The service is not touched
# either way: it runs inside the kind nodes' containers, each its own cgroup, where a process's niceness on the runner
# does not reach (niceness ranks a process only against the processes of its own cgroup).
# Both arms: a real response-time probe times HTTP requests to php-apache every 5 s (latency.csv).
# Load schedule: the load-generator replica count steps through LOAD_STEPS, each step DURATION/steps seconds,
# identical in both arms. Results in $OUT_DIR: capture.csv (every 15 s), nodes timeline, Omni audit (omni arm).
# Evidence discipline (adopted from the ChatGPT-built harness, extended to every muscle): pinned, SHA-256-checked
# metrics-server; preflight record of tool versions; clean-cluster check; Omni-Compass runs as a least-privilege service
# account (deploy/kind/rbac-omni.yaml) with `kubectl auth can-i` receipts for what it can and cannot do; the run fails if
# Omni's governor recorded no decisions or if the reset leaves any record behind (a window in which the governor decided
# and made no write is valid: it stayed native, and the table counts such windows); SHA256SUMS.txt fingerprints every
# output file.
set -euo pipefail
ARM="${ARM:?set ARM=native, ARM=watch (Omni watches, writes nothing), ARM=omni (B: Omni on top), ARM=compass (B with the compass law), ARM=strict (C: Omni decides replicas and nodes) or ARM=solo (Omni-Compass by itself: the pod autoscaler removed, the pod muscle of Omni-Compass on the workload)}"
STRICT=""; [ "$ARM" = "strict" ] && STRICT="--strict-replicas"
LAW=""; { [ "$ARM" = "compass" ] || [ "$ARM" = "solo" ]; } && LAW="--law compass"
OWN=""   # ARM=solo: the workload Omni-Compass scales itself (omni-v19's pod muscle of its own; docs/SOLO_PREREGISTRATION.md)
DRY=""; [ "$ARM" = "watch" ] && DRY="--dry-run"
# native tuned harder (the cost-to-match test): ARM=native40, native30, native20 is Kubernetes alone with its HPA target
# lowered to that value by the operator, no Omni-Compass; it shows what native needs to reach Omni-Compass's response times
TUNE=""; [[ "$ARM" =~ ^native([0-9]+)$ ]] && TUNE="${BASH_REMATCH[1]}"
NATIVE=""; { [ "$ARM" = "native" ] || [ -n "$TUNE" ]; } && NATIVE=1
OMNI_NICE=19; [ -z "${ORGANISM:-}" ] || OMNI_NICE=0   # the governor's CPU priority (header): never below the rig beside it
OUT_DIR="${OUT_DIR:-bench_$ARM}"; DURATION="${DURATION:-1200}"; WARMUP="${WARMUP:-120}"
LOAD_STEPS="${LOAD_STEPS:-1 2 3 1 2 1}"
export DRAIN_TIMEOUT="${DRAIN_TIMEOUT:-45s}"   # a drain blocked by the disruption budget gives up and the node stays in service
IDLE_W="${IDLE_W:-100}"; DYN_W="${DYN_W:-150}"
# no machine is ever powered off: an idle worker (marked prefer-not, its work gone) stays Ready and powered, gauged down
# to its idle floor, and is back in service the instant its mark is removed (muscle tone). It draws park_frac x idle power, the
# simulator's declared hardware property (fleet/harness.py park_frac = 0.25); the same accounting in every arm
PARK_FRAC="${PARK_FRAC:-0.25}"
STANDBY_W="${STANDBY_W:-$(python -c "print($IDLE_W * $PARK_FRAC)")}"; export IDLE_W DYN_W STANDBY_W
mkdir -p "$OUT_DIR"
# Preserve every failed arm and its diagnostics, including failures before the final checks.
finish_evidence() {
  local code=$?
  trap - EXIT
  if [ -n "${watch_pid:-}" ]; then
    touch "$OUT_DIR/pod_watch.stop"
    wait "$watch_pid" || { [ "$code" -ne 0 ] || code=1; }
  fi
  if [ "$code" -ne 0 ] && declare -F stop_governors >/dev/null; then
    stop_governors || true
  fi
  [ "$code" -eq 0 ] || echo "arm failed with exit $code; measurements not admitted" >> "$OUT_DIR/INVALID"
  (cd "$OUT_DIR" && find . -type f ! -name SHA256SUMS.txt -print0 | sort -z | xargs -0 sha256sum > SHA256SUMS.txt) || code=1
  exit "$code"
}
trap finish_evidence EXIT
# PLATFORM=kind (default): the kind cluster on one runner. PLATFORM=aks: a real Azure Kubernetes Service cluster
# (.github/workflows/aks-metered.yml): workers are the user pool (agentpool=work) under Azure's own cluster autoscaler,
# which deletes a machine once it is empty, so a machine given back is a machine no longer billed; the system pool
# carries the NoSchedule taint kind's control plane carries, so every count below is the same on both
PLATFORM="${PLATFORM:-kind}"
# Google (GKE) and Amazon (EKS) clusters are built to the AKS shape (a tainted system pool; work pools labelled
# omni-role=work and agentpool=<pool>: scripts/gke_paired.sh, scripts/eks_paired.sh), so they run the same managed mode
# (kubectl only); CLOUD keeps the provider's name. A cluster the tester built in any other provider's console to the same
# shape (PLATFORM=byoc: Oracle, DigitalOcean, Alibaba, Linode, IBM; scripts/byoc_paired.sh, docs/BYOC_SETUP.md) runs the same mode
CLOUD="$PLATFORM"; case "$PLATFORM" in gke|eks|byoc) PLATFORM=aks;; esac; export CLOUD
if [ "$PLATFORM" = aks ]; then export WORKER_SEL="${WORKER_SEL:-omni-role=work}"; else export WORKER_SEL="!node-role.kubernetes.io/control-plane"; fi   # every AKS work pool carries omni-role=work (scripts/aks_paired.sh)
# ADDONS=keda, the add-on test: in every arm KEDA and its HTTP add-on own the service's autoscaler (scripts/kind_addons.sh;
# ADDONS_PROFILE=both: the CPU target and the live requests in flight, the default; http: the requests in flight alone),
# the load and the probe enter through the add-on's interceptor, and Omni-Compass's autoscaler moves reach KEDA's
# ScaledObject through the plug (scripts/kubectl_keda.py). ADDONS=goldilocks (register row 80): in every arm the service's
# requests are set as an operator sets them with Goldilocks and the VPA's recommender, learned while the load runs its own
# steps and applied before the warm-up (scripts/kind_addons_goldilocks.sh); the HPA, the load and the probe are unchanged,
# and Omni-Compass's moves are its own, on top. CRUISEKUBE=1 (register row 81), with ADDONS=keda and ADDONS_PROFILE=http:
# in every arm CruiseKube right-sizes the service itself, in place and at admission, from a Prometheus of its own, beside
# KEDA's HTTP add-on scaling it on requests in flight (CruiseKube skips any workload whose HPA scales on CPU or memory, by
# its own design), learning longer than its hour before the arms are told apart (scripts/kind_addons_cruisekube.sh);
# Omni-Compass's moves are its own, on top, the CPU limit left to CruiseKube, which resizes it itself. ADDONS=vpa
# (docs/COMPETITORS_PREREGISTRATION.md): in every arm that carries it the Vertical Pod Autoscaler resizes the service's
# memory in place (update mode InPlaceOrRecreate) beside the HPA on its processor, learning while the load runs its own
# steps before the warm-up and acting through the window (scripts/kind_addons_vpa.sh); Omni-Compass's moves are its own, on
# top, the VPA and the memory it sets left to it. Empty (the default): every other set, unchanged
ADDONS="${ADDONS:-}"
case "$ADDONS" in ""|keda|goldilocks|crane|vpa) ;; *) echo "ADDONS must be empty, keda, goldilocks, crane or vpa (got $ADDONS)"; exit 1;; esac
# BATCH_QUEUE=kueue, volcano, kai, koordinator, kuberay, godel, vanilla or binpack, with WORKLOAD=batch
# (docs/BATCH_QUEUE_PREREGISTRATION.md; register rows 63, 88, 89, 91, 92, 93): the batch test's work arrives as a stream of jobs
# and a queueing system of its own admits and places it (kuberay: the same work as Ray jobs on one Ray cluster, scaled by
# the Ray autoscaler; vanilla: the Kubernetes scheduler alone; binpack: with the operator's bin-packing profile),
# installed from its own release in every arm before the arms are told apart (scripts/kind_batch_queue.sh); Omni-Compass
# sits on top with its own levers and never writes the queueing system's objects. Empty: the batch test's one Job on
# Kubernetes alone
BATCH_QUEUE="${BATCH_QUEUE:-}"
case "$BATCH_QUEUE" in ""|kueue|volcano|kai|koordinator|kuberay|godel|group|vanilla|binpack) ;; *) echo "BATCH_QUEUE must be empty, kueue, volcano, kai, koordinator, kuberay, godel, group, vanilla or binpack (got $BATCH_QUEUE)"; exit 1;; esac
[ -z "$BATCH_QUEUE" ] || { [ "${WORKLOAD:-web}" = batch ] && [ -z "$ADDONS" ]; } \
  || { echo "BATCH_QUEUE=$BATCH_QUEUE runs the batch test (WORKLOAD=batch) with no other add-on"; exit 1; }
CRUISEKUBE="${CRUISEKUBE:-}"
# METER=rapl: the machine's own meter beside the declared model, on a machine with the processor's RAPL counters (a
# rented bare-metal machine: scripts/metal_kind_run.sh; register row 79): sampled every 2 s over the measured window
# (tools/rapl.py, rapl.csv). KEPLER=1 adds Kepler, the shared meter, read at the window's opening and close
# (scripts/kind_addons_kepler.sh). Neither is an arm: both read every arm the same way. Empty: no meter (every other set)
METER="${METER:-}"; KEPLER="${KEPLER:-}"
[ -z "$KEPLER" ] || METER=rapl
case "$METER" in ""|rapl) ;; *) echo "METER must be empty or rapl (got $METER)"; exit 1;; esac
[ -z "$CRUISEKUBE" ] || { [ "$ADDONS" = keda ] && [ "${ADDONS_PROFILE:-both}" = http ]; } \
  || { echo "CRUISEKUBE=1 runs beside KEDA's HTTP add-on alone (ADDONS=keda ADDONS_PROFILE=http): CruiseKube skips a service whose HPA scales on CPU"; exit 1; }
# the power cap writes the service's CPU limit; with CruiseKube the limit is CruiseKube's own (it resizes the running
# pods in place), so the cap is left out of that set and its reset checks read the operator's limit on the Deployment
CAP_ARGS="--cap-deployments default/php-apache"; [ -z "$CRUISEKUBE" ] || CAP_ARGS=""
# The same wiring on every platform, the whole engine at the max (the founder's order of 31 October: no hard rule; the
# cloud's tune-down on the machines alone of 14 October, its machines-only switch and the governor's give-back-only flag, is
# struck): the service sensed, the processor conveyed, the declared power model read, and the machine lever on top of the
# cloud's own autoscaler, which makes and deletes machines in every arm; the lever parks a machine that exists and wakes
# it, and asks the cloud for none (scripts/kind_nodepool.sh). The bill is judged beside the work by the one key, never ruled
OMNI_SENSED="default/php-apache"; OMNI_POWER_CMD="bash scripts/kind_power.sh"
limits_now() {   # the CPU limit the operator's record holds: the pods' own, or with CruiseKube the Deployment's template
  if [ -n "$CRUISEKUBE" ]; then
    kubectl get deployment php-apache -o jsonpath='{.spec.template.spec.containers[0].resources.limits.cpu}'
  else
    kubectl get pods -l run=php-apache -o jsonpath='{range .items[*]}{.spec.containers[0].resources.limits.cpu}{"\n"}{end}' | sort -u | tr '\n' ' ' | sed 's/ $//'
  fi
}
KEDA=""; [ "$ADDONS" = keda ] && KEDA=1
# ADDONS=crane (register row 90; docs/CRANE_PREREGISTRATION.md): in every arm that carries it, Crane and the Prometheus it
# reads own the service's autoscaler (scripts/kind_addons_crane.sh): its Effective HPA in auto mode, from which it builds and
# owns the HPA ehpa-php-apache; Omni-Compass's autoscaler moves reach Crane's EHPA through the plug (scripts/kubectl_crane.py)
CRANE=""; [ "$ADDONS" = crane ] && CRANE=1
HPA_NAME=php-apache; [ -z "$CRANE" ] || HPA_NAME=ehpa-php-apache   # the service's HPA, as the arm's autoscaler names it
if [ -n "$ADDONS" ]; then
  { [ -z "${TWO_APP:-}" ] && [ "$PLATFORM" = kind ] && [ -z "$TUNE" ]; } || { echo "ADDONS=$ADDONS runs on kind, with one app and the operator's own target"; exit 1; }
fi
EXPECT_LIMIT=500m   # the operator's CPU limit on php-apache (deploy/kind/demo.yaml); with Goldilocks, the one its recommendation set
# the CPU target the HPA holds when nothing has moved it, and how it is read: metrics[0] as demo.yaml writes it; KEDA lists
# the requests-in-flight metric first, so with the add-on it is found by name, and profile http has none
EXPECT_TARGET=50; [ -n "$KEDA" ] && [ "${ADDONS_PROFILE:-both}" = http ] && EXPECT_TARGET=""
hpa_cpu_target() {
  if [ -n "$KEDA" ] || [ -n "$CRANE" ]; then   # an add-on's HPA can carry other metrics; the processor's is found by name
    kubectl get hpa "$1" -o json | jq -r '[.spec.metrics[] | select(.type == "Resource" and .resource.name == "cpu") | .resource.target.averageUtilization][0] // empty'
  else
    kubectl get hpa "$1" -o jsonpath='{.spec.metrics[0].resource.target.averageUtilization}'
  fi
}
WORKERS=${AKS_MAX_NODES:-$(kubectl get nodes -l "$WORKER_SEL" --no-headers | wc -l)}
SITE_LIMIT_W=$(( WORKERS * (IDLE_W + DYN_W) ))

METRICS_SERVER_VERSION="${METRICS_SERVER_VERSION:-v0.9.0}"
METRICS_SERVER_SHA256="${METRICS_SERVER_SHA256:-1cec29a5267809306a2c6ec74a3e449abbb705b4a8beed0c8a1963910f72c79b}"
server_minor=$(kubectl version -o json | jq -r '.serverVersion.minor' | tr -cd '0-9')
# the oldest Kubernetes each metrics-server line supports, from its own compatibility table (the Crane rig runs 1.25 with v0.6.4,
# Gödel's 1.24 with v0.5.2)
case "$METRICS_SERVER_VERSION" in v0.5.*) ms_floor=8 ;; v0.6.*) ms_floor=25 ;; v0.7.*) ms_floor=27 ;; v0.8.*) ms_floor=31 ;; *) ms_floor=34 ;; esac
[ "$PLATFORM" = aks ] || { [ -n "$server_minor" ] && [ "$server_minor" -ge "$ms_floor" ]; } || { echo "metrics-server $METRICS_SERVER_VERSION needs Kubernetes 1.$ms_floor+ (minor=$server_minor)"; exit 1; }
# the power cap and the processor conveyance resize the serving pods in place (the pods/resize subresource); a cluster that
# does not serve it (the Crane rig's Kubernetes 1.25, docs/CRANE_PREREGISTRATION.md) has neither lever, so both are off in
# every arm and the preflight says so
NO_RESIZE=""
api_v1=$(kubectl get --raw /api/v1)   # unread, the arm stops here: a lever is never switched off by a failed read
if [ -n "$CAP_ARGS" ] && ! jq -e '.resources[] | select(.name == "pods/resize")' <<<"$api_v1" >/dev/null; then
  CAP_ARGS=""; NO_RESIZE=1
fi
{
  echo "date_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"; echo "arm=$ARM"; echo "git_commit=$(git rev-parse HEAD 2>/dev/null || echo unknown)"
  echo "docker=$(docker --version 2>/dev/null || echo n/a)"; echo "kind=$(kind version 2>/dev/null || echo n/a)"
  echo "kubectl=$(kubectl version --client=true -o json | jq -r '.clientVersion.gitVersion')"
  kubectl version -o json | jq -r '"server=" + .serverVersion.gitVersion'; echo "python=$(python --version 2>&1)"
  echo "metrics_server=$METRICS_SERVER_VERSION sha256=$METRICS_SERVER_SHA256"; echo "workers=$WORKERS"
  [ -z "$NO_RESIZE" ] || echo "in_place_resize=not served by this cluster: the power cap and the processor conveyance are off in every arm"
} | tee "$OUT_DIR/preflight.txt"
if [ "$PLATFORM" = kind ]; then
# the pinned manifest, fetched once per machine (both arms of a repetition use the same file) and tried again with a pause
# when GitHub refuses it (12 Oct: a 504 marked an arm invalid before its cluster was used); the SHA-256 check below
# decides, as before
ms_cache="${RUNNER_TEMP:-${TMPDIR:-/tmp}}/metrics-server-${METRICS_SERVER_VERSION}-components.yaml"
if [ ! -s "$ms_cache" ] || [ "$(sha256sum "$ms_cache" | cut -d' ' -f1)" != "$METRICS_SERVER_SHA256" ]; then
  for t in 1 2 3; do
    curl -fsSL --retry 8 --retry-all-errors --retry-delay 15 --connect-timeout 20 --max-time 120 \
      "https://github.com/kubernetes-sigs/metrics-server/releases/download/${METRICS_SERVER_VERSION}/components.yaml" -o "$ms_cache.part" \
      && [ "$(sha256sum "$ms_cache.part" | cut -d' ' -f1)" = "$METRICS_SERVER_SHA256" ] && mv "$ms_cache.part" "$ms_cache" && break
    echo "metrics-server manifest: not the pinned file yet (round $t)"; sleep 30
  done
fi
cp "$ms_cache" "$OUT_DIR/metrics-server-components.yaml" 2>/dev/null || cp "$ms_cache.part" "$OUT_DIR/metrics-server-components.yaml" 2>/dev/null || true
actual_sha=$(sha256sum "$OUT_DIR/metrics-server-components.yaml" 2>/dev/null | cut -d' ' -f1 || true)
[ "$actual_sha" = "$METRICS_SERVER_SHA256" ] || { echo "metrics-server manifest SHA-256 mismatch: $actual_sha"; exit 1; }
# the pinned manifest applied once with the rig's settings written into it, so the server rolls out once: the kubelet's
# certificate unverified (kind's nodes have no CA-signed one), the server on the control plane beside the other systems'
# controllers, and its image by the registry that serves it (the 0.5 line's manifest names k8s.gcr.io, which only redirects
# to registry.k8s.io). Patching the applied manifest twice made two rollouts, and on Kubernetes 1.24 the first pod, deleted
# while its image was still coming through the redirect, stayed terminating past the wait (the Gödel trial of 20 October).
python3 - "$OUT_DIR/metrics-server-components.yaml" > "$OUT_DIR/metrics-server-rig.yaml" <<'EOF'
import sys, yaml
docs = [d for d in yaml.safe_load_all(open(sys.argv[1])) if d]
for d in docs:
    if d.get("kind") == "Deployment" and d["metadata"]["name"] == "metrics-server":
        spec = d["spec"]["template"]["spec"]
        c = spec["containers"][0]
        c["args"] = list(c.get("args", [])) + ["--kubelet-insecure-tls"]
        c["image"] = c["image"].replace("k8s.gcr.io/", "registry.k8s.io/")
        spec["nodeSelector"] = {"node-role.kubernetes.io/control-plane": ""}
        spec["tolerations"] = [{"key": "node-role.kubernetes.io/control-plane", "operator": "Exists", "effect": "NoSchedule"},
                               {"key": "node-role.kubernetes.io/master", "operator": "Exists", "effect": "NoSchedule"}]   # 1.24 carries both taints
print(yaml.safe_dump_all(docs, sort_keys=False))
EOF
kubectl apply -f "$OUT_DIR/metrics-server-rig.yaml"
pin='{"spec":{"template":{"spec":{"nodeSelector":{"node-role.kubernetes.io/control-plane":""},"tolerations":[{"key":"node-role.kubernetes.io/control-plane","operator":"Exists","effect":"NoSchedule"},{"key":"node-role.kubernetes.io/master","operator":"Exists","effect":"NoSchedule"}]}}}}'
kubectl -n kube-system patch deployment coredns -p "$pin"
kubectl -n kube-system rollout status deployment/metrics-server --timeout=300s
kubectl -n kube-system rollout status deployment/coredns --timeout=300s
# the served image pulled onto every worker before the arm, then the puller deleted, before the governor starts or the
# window opens (deploy/kind/prepull.yaml; amendment of 18 October, docs/POD_START_WAIT.md): a serving pod started inside
# the window no longer downloads and unpacks the image on the one machine every kind node shares. The same in every arm;
# a puller not finished on every worker fails the arm's checks (marked invalid), so no arm runs on the other rig
# busybox:1.36 (the load generator, the batch stream, the probe) is pulled once onto the runner and loaded from that copy into
# every node of this cluster (kind load), so no node asks Docker Hub for it: Docker Hub limits anonymous pulls, and the fresh
# clusters of one repetition asked it six times each (repetition 10 of run 39666341432, the bin-packing set's A, lost its
# third and fourth arms to a pull that never finished in 300 s). The same in every arm; where the load cannot be made, the
# nodes pull it themselves, as before, and the preflight says so
kname="${KIND_CLUSTER:-$(kubectl config current-context 2>/dev/null | sed -n 's/^kind-//p')}"
for t in 1 2 3; do
  docker image inspect busybox:1.36 >/dev/null 2>&1 || docker pull -q busybox:1.36 >/dev/null 2>&1 && break
  echo "busybox:1.36 not pulled onto the runner (try $t)"; sleep 20
done
if [ -n "$kname" ] && kind load docker-image busybox:1.36 --name "$kname" >/dev/null 2>&1; then
  echo "busybox: loaded into every node from the runner's own copy (kind load)" | tee -a "$OUT_DIR/preflight.txt"
else
  echo "busybox: not loaded from the runner; the nodes pull it themselves" | tee -a "$OUT_DIR/preflight.txt"
fi
kubectl apply -f deploy/kind/prepull.yaml >/dev/null
for t in 1 2 3; do
  kubectl -n kube-system rollout status daemonset/rig-prepull --timeout=300s && break
  if [ "$t" = 3 ]; then
    # what each puller pod says, kept in the arm's own files, so a pull that never finishes is read from its own record
    { kubectl -n kube-system get pods -l app=rig-prepull -o wide; kubectl -n kube-system describe pods -l app=rig-prepull; } \
      > "$OUT_DIR/prepull_failed.txt" 2>&1 || true
    echo "the image pre-puller did not finish on every worker (3 tries; prepull_failed.txt)"; exit 1
  fi
  echo "image pre-puller not finished on every worker (try $t): waiting again"; sleep 20
done
echo "images=pre-pulled on every worker before the arm (deploy/kind/prepull.yaml)" | tee -a "$OUT_DIR/preflight.txt"
echo "image_ids=$(kubectl -n kube-system get pods -l app=rig-prepull -o jsonpath='{range .items[*]}{.status.initContainerStatuses[0].imageID}{"\n"}{end}' | sort | uniq -c | tr -s ' \n' ' ')" \
  | tee -a "$OUT_DIR/preflight.txt"
kubectl -n kube-system delete daemonset rig-prepull --wait=true --timeout=120s >/dev/null
kubectl -n kube-system wait --for=delete pod -l app=rig-prepull --timeout=120s >/dev/null 2>&1 || true
fi   # AKS runs its own metrics-server and CoreDNS on the system pool; each cloud machine unpacks on its own processor
if [ -n "${CAP_CPU_M:-}" ]; then
  # the capacity test (docs/CAPACITY_PREREGISTRATION.md): the same resource cap in every arm, set by the cluster itself, not
  # by either controller: a quota on the CPU limits of the served app's pods (CAP_CPU_M millicores in all), counted for the
  # pods of one priority class, so the load generator and the probe are outside it. Neither arm can pass it: a new pod or
  # a raised limit past it is refused by the API server
  kubectl apply -f - <<YAML
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata: {name: omni-capped}
value: 0
globalDefault: false
description: "the capacity test's cap counts the served app's pods only (the same in every arm)"
---
apiVersion: v1
kind: ResourceQuota
metadata: {name: omni-cap, namespace: default}
spec:
  hard: {limits.cpu: "${CAP_CPU_M}m"}
  scopeSelector:
    matchExpressions: [{scopeName: PriorityClass, operator: In, values: [omni-capped]}]
YAML
  echo "cap_cpu_m=$CAP_CPU_M (a quota on the served app's CPU limits, the same in every arm)" | tee -a "$OUT_DIR/preflight.txt"
fi
kubectl apply -f deploy/kind/demo.yaml
[ -z "${CAP_CPU_M:-}" ] || kubectl patch deployment php-apache --type merge -p '{"spec":{"template":{"spec":{"priorityClassName":"omni-capped"}}}}' >/dev/null
# a bigger fleet needs a higher replica ceiling or its machines stay empty (9 pods of 200m fit one 2-vCPU worker): the
# ceiling scales with the fleet when HPA_MAX is set, the same in every arm; the restore checks below expect that range
HPA_RANGE="1,${HPA_MAX:-10}"
if [ -n "${HPA_MAX:-}" ]; then
  kubectl patch hpa php-apache --type merge -p "{\"spec\":{\"maxReplicas\":${HPA_MAX}}}" >/dev/null
  echo "hpa_max=$HPA_MAX (the fleet's ceiling, the same in every arm)" | tee -a "$OUT_DIR/preflight.txt"
fi
if [ -n "$TUNE" ]; then
  kubectl patch hpa php-apache --type=json -p "[{\"op\":\"replace\",\"path\":\"/spec/metrics/0/resource/target/averageUtilization\",\"value\":$TUNE}]"
  echo "native tuned by the operator: HPA target $TUNE (no Omni-Compass)" | tee "$OUT_DIR/tuned.txt"
fi
# the governor's own core on the batch rig (docs/BATCH_QUEUE_PREREGISTRATION.md, amendment 5), the same in every arm: the
# kind nodes on every core but the last, the governor alone on the last. On a real cluster it runs on its own machine;
# here every node is a container on one runner and the governor's group competes with them as a peer (its niceness ranks
# it only inside its own group), so its own work and its commands came out of the measured pods' processor time (the
# scheduler's first runs: the same placement and the same start waits in both arms, each pod's hashing 1.4% longer with
# Omni-Compass on top). GOV_CORE=1 gives it its own core on the serving rig too (the governors' serving tests: Crane,
# docs/CRANE_PREREGISTRATION.md), the same in every arm
GOV_PIN=""
if { [ -n "$BATCH_QUEUE" ] || [ "${GOV_CORE:-}" = 1 ]; } && [ "$PLATFORM" = kind ] && [ "$(nproc)" -ge 2 ] && command -v taskset >/dev/null 2>&1; then
  ncpu=$(nproc); gov_cpu=$((ncpu - 1)); cluster_cpus="0-$((ncpu - 2))"; pinned=0
  for node in $(kind get nodes --name "${KIND_CLUSTER:-omni-bench}" 2>/dev/null); do
    docker update --cpuset-cpus "$cluster_cpus" "$node" >/dev/null && pinned=$((pinned + 1))
  done
  [ "$pinned" -gt 0 ] || { echo "INVALID RUN: no kind node could be placed on its cores"; exit 1; }
  GOV_PIN="taskset -c $gov_cpu"
  echo "cores: the $pinned kind nodes on cores $cluster_cpus, the governor alone on core $gov_cpu (of $ncpu), in every arm" | tee -a "$OUT_DIR/preflight.txt"
fi
kubectl apply -f deploy/kind/bench-serving.yaml
kubectl rollout status deployment/php-apache --timeout=300s
if [ -n "$KEDA" ]; then
  # the add-on native, installed the same way in every arm before the arms are told apart
  OUT_DIR="$OUT_DIR" bash scripts/kind_addons.sh
  echo "addons=$ADDONS profile=${ADDONS_PROFILE:-both} (addons.txt)" | tee -a "$OUT_DIR/preflight.txt"
elif [ -n "$CRANE" ]; then
  # Crane and its Prometheus, installed the same way in every arm that carries them, before the arms are told apart
  OUT_DIR="$OUT_DIR" HPA_MAX="${HPA_MAX:-10}" bash scripts/kind_addons_crane.sh
  echo "addons=crane (addons.txt)" | tee -a "$OUT_DIR/preflight.txt"
elif [ "$ADDONS" = goldilocks ]; then
  # Goldilocks and the VPA's recommender installed the same way in every arm; the recommendation is learned and applied
  # once the load runs (below), before the warm-up
  OUT_DIR="$OUT_DIR" PHASE=install bash scripts/kind_addons_goldilocks.sh
elif [ "$ADDONS" = vpa ]; then
  # the Vertical Pod Autoscaler, installed the same way in every arm that carries it, before the arms are told apart
  OUT_DIR="$OUT_DIR" PHASE=install bash scripts/kind_addons_vpa.sh
fi
if [ -n "$CRUISEKUBE" ]; then
  # CruiseKube, its Prometheus and its exporters installed the same way in every arm, beside KEDA's HTTP add-on; it is
  # put in Cruise mode on the service and learns once the load runs (below), before the warm-up
  OUT_DIR="$OUT_DIR" PHASE=install bash scripts/kind_addons_cruisekube.sh
fi
if [ -n "$BATCH_QUEUE" ]; then
  # the queueing system, installed the same way in every arm before the arms are told apart
  OUT_DIR="$OUT_DIR" PHASE=install bash scripts/kind_batch_queue.sh
  echo "batch queue: $(head -1 "$OUT_DIR/batch_queue.txt") (batch_queue.txt)" | tee -a "$OUT_DIR/preflight.txt"
fi
if [ -n "$METER" ]; then
  # the machine's own meter: there must be one (a virtual machine has none, and the run would say nothing new)
  [ "$PLATFORM" = kind ] || { echo "METER=rapl reads the machine under a kind cluster"; exit 1; }
  python3 tools/rapl.py probe > "$OUT_DIR/meter_probe.json" \
    || { echo "no processor meter on this machine (tools/rapl.py probe; it needs root and bare metal)"; cat "$OUT_DIR/meter_probe.json"; exit 1; }
  echo "meter=rapl counted=$(jq -c .counted "$OUT_DIR/meter_probe.json") virtualization=$(jq -r .virtualization "$OUT_DIR/meter_probe.json") kepler=${KEPLER:-0}" | tee -a "$OUT_DIR/preflight.txt"
  [ -z "$KEPLER" ] || OUT_DIR="$OUT_DIR" PHASE=install bash scripts/kind_addons_kepler.sh
fi
if [ -n "${TWO_APP:-}" ]; then
  # the fairness test: a noisy neighbour on the same workers, its own HPA, its own surging load (deploy/kind/noisy.yaml)
  kubectl apply -f deploy/kind/noisy.yaml
  kubectl rollout status deployment/php-noisy --timeout=300s
  echo "two_app=1 (php-apache and the noisy neighbour php-noisy)" | tee -a "$OUT_DIR/preflight.txt"
fi
if [ "$PLATFORM" = aks ]; then
  # the runner is outside Azure's network: the probe reaches the Service through Azure's load balancer, still
  # load-balanced across every ready endpoint, as a client outside the cluster sees it
  kubectl patch service php-apache-edge -p '{"spec":{"type":"LoadBalancer"}}'
  for i in $(seq 1 60); do EDGE_IP=$(kubectl get service php-apache-edge -o jsonpath='{.status.loadBalancer.ingress[0].ip}'); [ -n "$EDGE_IP" ] || EDGE_IP=$(kubectl get service php-apache-edge -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'); [ -n "$EDGE_IP" ] && break; sleep 5; done   # EKS: a host name
  PROBE_URL="http://${EDGE_IP}:80/"
else
EDGE_IP=$(kubectl get nodes -l node-role.kubernetes.io/control-plane -o jsonpath='{.items[0].status.addresses[?(@.type=="InternalIP")].address}')
PROBE_URL="http://${EDGE_IP}:30080/"
[ -z "$KEDA" ] || PROBE_URL="http://${EDGE_IP}:30090/"   # the add-on's interceptor, where the load enters too
fi
for i in $(seq 1 30); do curl -fsS -m 5 "$PROBE_URL" >/dev/null && break; sleep 2; done
curl -fsS -m 5 "$PROBE_URL" >/dev/null || { echo "serving path $PROBE_URL not reachable"; exit 1; }
if [ -n "$KEDA" ]; then
  echo "probe_url=$PROBE_URL (the add-on's interceptor, NodePort on the control plane, on to php-apache)" | tee -a "$OUT_DIR/preflight.txt"
else
echo "probe_url=$PROBE_URL (Service via kube-proxy on the control plane)" | tee -a "$OUT_DIR/preflight.txt"
fi
kubectl create configmap omni-security --from-literal=hold=false --dry-run=client -o yaml | kubectl apply -f -
# LOADGEN=closed (default, every set before 22): waits for each answer. LOADGEN=open: a fixed rate, the same work in every arm.
# LOADGEN=meter (the capacity test): one generator at the scheduled rates RATE_STEPS (requests per second), counting every
# answer (within the line, late, failed, not sent: deploy/kind/loadgen-meter.yaml)
LOADGEN="${LOADGEN:-closed}"
if [ "$LOADGEN" = meter ]; then
  { [ -z "$ADDONS" ] && [ "$PLATFORM" = kind ] && [ -z "${ORGANISM:-}" ] && [ "${WORKLOAD:-web}" = web ]; } \
    || { echo "LOADGEN=meter runs on kind, alone (no add-on, organism or batch)"; exit 1; }
  RATE_STEPS="${RATE_STEPS:?set RATE_STEPS (requests per second per step) for LOADGEN=meter}"
  sed -e "s#RATE_STEPS_VALUE#$RATE_STEPS#" -e "s#DURATION_VALUE#$DURATION#" -e "s#SLO_MS_VALUE#${SLO_MS:-500}#" \
    deploy/kind/loadgen-meter.yaml > "$OUT_DIR/loadgen-meter.yaml"
fi
if [ -n "$KEDA" ]; then
  # the same load generator, its requests sent through the add-on's interceptor, which counts them for the scaler
  lg=deploy/kind/loadgen.yaml; [ "$LOADGEN" = "open" ] && lg=deploy/kind/loadgen-open.yaml
  sed 's#http://php-apache #http://keda-add-ons-http-interceptor-proxy.keda:8080/ #' "$lg" > "$OUT_DIR/loadgen.yaml"
  grep -q 'keda-add-ons-http-interceptor-proxy' "$OUT_DIR/loadgen.yaml" || { echo "the load generator was not routed through the add-on"; exit 1; }
  kubectl apply -f "$OUT_DIR/loadgen.yaml"
elif [ "$LOADGEN" = "meter" ]; then kubectl apply -f "$OUT_DIR/loadgen-meter.yaml"
elif [ "$LOADGEN" = "open" ]; then kubectl apply -f deploy/kind/loadgen-open.yaml; else kubectl apply -f deploy/kind/loadgen.yaml; fi
if [ "$PLATFORM" = aks ]; then   # the load generator lives where kind keeps it, off the measured workers: the system pool
  # machine, found by the taint aks_paired.sh gives it (CriticalAddonsOnly) and pinned by its host name (no pool label
  # guessed); kind's control-plane selector in the manifest is removed in the same patch (null), since AKS has no such
  # machine and a merge patch otherwise keeps it beside the new one; replaced in place (Recreate)
  sysnode=$(kubectl get nodes -o json | jq -r '[.items[] | select(any(.spec.taints[]?; .key == "CriticalAddonsOnly")) | .metadata.labels["kubernetes.io/hostname"]][0] // empty')
  [ -n "$sysnode" ] || { echo "no system-pool machine (taint CriticalAddonsOnly) found"; kubectl get nodes -o wide; exit 1; }
  echo "loadgen_node=$sysnode" | tee -a "$OUT_DIR/preflight.txt"
  kubectl patch deployment load-generator --type=merge -p "{\"spec\":{\"strategy\":{\"type\":\"Recreate\",\"rollingUpdate\":null},\"template\":{\"spec\":{\"nodeSelector\":{\"node-role.kubernetes.io/control-plane\":null,\"kubernetes.io/hostname\":\"$sysnode\"},\"tolerations\":[{\"key\":\"CriticalAddonsOnly\",\"operator\":\"Exists\",\"effect\":\"NoSchedule\"}]}}}}"
fi
echo "loadgen=$LOADGEN" | tee -a "$OUT_DIR/preflight.txt"
if ! kubectl rollout status deployment/load-generator --timeout=300s; then
  # why it did not start, in the run's own record
  { kubectl get nodes --show-labels; kubectl describe pods -l app=load-generator; kubectl get events --sort-by=.lastTimestamp | tail -30; } \
    > "$OUT_DIR/loadgen_failed.txt" 2>&1; tail -40 "$OUT_DIR/loadgen_failed.txt"; exit 1
fi
for i in $(seq 1 30); do kubectl top nodes >/dev/null 2>&1 && break; sleep 10; done
if [ "$ADDONS" = goldilocks ]; then
  # Goldilocks learns the service while the load runs its own steps, and the operator applies its recommendation; the
  # same in every arm, before the arms are told apart (Omni-Compass is not started yet)
  OUT_DIR="$OUT_DIR" PHASE=learn LOAD_STEPS="$LOAD_STEPS" bash scripts/kind_addons_goldilocks.sh
  EXPECT_LIMIT=$(cat "$OUT_DIR/goldilocks_limit.txt")
  echo "addons=goldilocks: requests from Goldilocks's recommendation, CPU limit $EXPECT_LIMIT (addons.txt)" | tee -a "$OUT_DIR/preflight.txt"
fi
if [ "$ADDONS" = vpa ]; then
  # the VPA learns the service while the load runs its own steps, the same in every arm that carries it, before the arms
  # are told apart (Omni-Compass is not started yet); it keeps resizing the memory in place through the window
  OUT_DIR="$OUT_DIR" PHASE=learn LOAD_STEPS="$LOAD_STEPS" bash scripts/kind_addons_vpa.sh
  echo "addons=vpa: in place on the service's memory beside the HPA on its processor (addons.txt)" | tee -a "$OUT_DIR/preflight.txt"
fi
if [ -n "$CRUISEKUBE" ]; then
  # CruiseKube in Cruise mode on the service, learning while the load runs its own steps until it has applied a change;
  # the same in every arm, before the arms are told apart (Omni-Compass is not started yet)
  OUT_DIR="$OUT_DIR" PHASE=learn LOAD_STEPS="$LOAD_STEPS" bash scripts/kind_addons_cruisekube.sh
  echo "cruisekube: Cruise mode on the service, a change applied before the window (addons.txt)" | tee -a "$OUT_DIR/preflight.txt"
fi
hpa_count=$(kubectl get hpa -A -o json | jq '.items | length')
want_hpa=1; [ -z "${TWO_APP:-}" ] || want_hpa=2
[ "$hpa_count" = "$want_hpa" ] || { echo "expected exactly $want_hpa HPA, found $hpa_count"; exit 1; }
SOLO_RANGE=""
if [ "$ARM" = "solo" ]; then
  # Omni-Compass by itself (docs/SOLO_PREREGISTRATION.md): the plain serving rig only; the pod autoscaler is removed after the
  # deploy, its own target and range written on the workload as the operator's (they are the operator's settings, not Omni's
  # records), the workload at the range's floor, the count its manifest ships; Kubernetes' own scheduler and kubelet stay
  [ -z "$KEDA$CRANE$CRUISEKUBE${TWO_APP:-}${BATCH_QUEUE:-}" ] || { echo "ARM=solo runs on the plain serving rig only"; exit 1; }
  SOLO_TARGET=$(hpa_cpu_target "$HPA_NAME"); SOLO_RANGE=$(kubectl get hpa "$HPA_NAME" -o jsonpath='{.spec.minReplicas},{.spec.maxReplicas}')
  kubectl delete hpa "$HPA_NAME" >/dev/null
  kubectl annotate deployment php-apache --overwrite "omnicompass.io/target-utilization=$SOLO_TARGET" "omnicompass.io/replica-range=$SOLO_RANGE" >/dev/null
  kubectl scale deployment php-apache --replicas="${SOLO_RANGE%%,*}" >/dev/null
  OWN="--own-replicas default/php-apache"; export OWN_WORKLOADS="default/php-apache"
  echo "solo: the pod autoscaler removed; the operator's target ${SOLO_TARGET}% and range $SOLO_RANGE written on the workload, $((${SOLO_RANGE%%,*})) replica(s) to start" | tee -a "$OUT_DIR/preflight.txt"
fi
if [ -n "$KEDA" ]; then   # the add-on's own pods, all on the control plane (scripts/kind_addons.sh checks where); with
  # CruiseKube beside it, CruiseKube's, its PostgreSQL's and its metrics' too (scripts/kind_addons_cruisekube.sh checks where)
  ck=false; [ -z "$CRUISEKUBE" ] || ck=true
  foreign=$(kubectl get pods -A -o json | jq --argjson ck "$ck" '[.items[] | select(.metadata.namespace | (IN("kube-system","local-path-storage","default","omni-compass","gatekeeper-system","keda") or ($ck and IN("cruisekube-system","cruisekube-metrics"))) | not)] | length')
elif [ "$ADDONS" = goldilocks ]; then   # Goldilocks's controller; the VPA's recommender is in kube-system (both on the control plane)
  foreign=$(kubectl get pods -A -o json | jq '[.items[] | select(.metadata.namespace | IN("kube-system","local-path-storage","default","omni-compass","gatekeeper-system","goldilocks") | not)] | length')
elif [ -n "$CRANE" ]; then   # Crane and its Prometheus (scripts/kind_addons_crane.sh checks where they run)
  foreign=$(kubectl get pods -A -o json | jq '[.items[] | select(.metadata.namespace | IN("kube-system","local-path-storage","default","omni-compass","gatekeeper-system","crane-system") | not)] | length')
else   # with a queueing system, its own namespace too (scripts/kind_batch_queue.sh checks its pods are on the control plane)
qns=""; [ "$BATCH_QUEUE" = kueue ] && qns=kueue-system; [ "$BATCH_QUEUE" = volcano ] && qns=volcano-system; [ "$BATCH_QUEUE" = kai ] && qns=kai-scheduler; [ "$BATCH_QUEUE" = koordinator ] && qns=koordinator-system; [ "$BATCH_QUEUE" = kuberay ] && qns=kuberay-system; [ "$BATCH_QUEUE" = godel ] && qns=godel-system
[ "$BATCH_QUEUE" = group ] && qns="${GROUP_AGENT_NS:-}"   # a group member: the orchestrator's agents, where it runs them here (OCM's klusterlet: several namespaces, space-separated)
foreign=$(kubectl get pods -A -o json | jq --arg q "$qns" '($q | split(" ")) as $qs | [.items[] | select(.metadata.namespace | (IN("kube-system","local-path-storage","default","omni-compass","gatekeeper-system") or IN($qs[])) | not)] | length')
fi
[ "$foreign" = "0" ] || { echo "cluster contains non-harness pods"; exit 1; }
if [ -z "$NATIVE" ]; then
  kubectl apply -f deploy/kind/rbac-omni.yaml
  [ -z "${TWO_APP:-}" ] || kubectl apply -f deploy/kind/rbac-omni-noisy.yaml
  [ -z "$KEDA" ] || kubectl apply -f deploy/kind/rbac-omni-keda.yaml
  [ -z "$CRANE" ] || kubectl apply -f deploy/kind/rbac-omni-crane.yaml
  SA="system:serviceaccount:omni-compass:omni-compass"
  can() { kubectl auth can-i "$@" --as="$SA"; }
  {
    echo "== can (each muscle's push)"
    echo "patch hpa/$HPA_NAME (hpa): $(can patch "hpa/$HPA_NAME" -n default)"
    echo "create hpa (omni-v23: the hand-back of a knob Omni-Compass cannot move to native's own autoscaler): $(can create hpa -n default)"
    echo "patch nodes (node pool: idle mark): $(can patch nodes)"
    echo "create pods/eviction (node pool: drain): $(can create pods --subresource=eviction -n default)"
    echo "patch pods/resize (power cap, in place): $(can patch pods --subresource=resize -n default)"
    echo "patch pods (make before break: which pods leave first): $(can patch pods -n default)"
    echo "get pods/resize (power cap reads before it writes): $(can get pods --subresource=resize -n default)"
    echo "patch deployment/php-apache (rollout guard, cap record): $(can patch deployment/php-apache -n default)"
    echo "patch deployment/php-apache --subresource=scale (pod muscle of its own, --own-replicas: what kubectl scale writes): $(can patch deployment/php-apache --subresource=scale -n default)"
    echo "get configmap/omni-security (security afferent): $(can get configmap/omni-security -n default)"
    [ -z "$KEDA" ] || echo "patch scaledobject/php-apache (the add-on's knob: KEDA rebuilds the HPA from it): $(can patch scaledobjects.keda.sh/php-apache -n default)"
    [ -z "$CRANE" ] || echo "patch ehpa/php-apache (Crane's knob: Crane rebuilds the HPA from it): $(can patch effectivehorizontalpodautoscalers.autoscaling.crane.io/php-apache -n default)"
    echo "== cannot"
    echo "delete nodes: $(can delete nodes)"
    echo "create pods: $(can create pods -n default)"
    echo "delete pods: $(can delete pods -n default)"
    echo "delete deployments: $(can delete deployments -n default)"
    echo "patch deployment/load-generator: $(can patch deployment/load-generator -n default)"
    echo "patch deployment/load-generator --subresource=scale (the pod muscle of its own writes the named workload alone): $(can patch deployment/load-generator --subresource=scale -n default)"
    echo "patch deployments in kube-system: $(can patch deployments -n kube-system)"
    echo "patch hpa in kube-system: $(can patch hpa -n kube-system)"
    echo "get secrets (any namespace): $(can get secrets -A)"
    echo "create namespaces: $(can create namespaces)"
    echo "patch configmap/omni-security: $(can patch configmap/omni-security -n default)"
    [ -z "$KEDA" ] || echo "delete scaledobject/php-apache: $(can delete scaledobjects.keda.sh/php-apache -n default)"
    [ -z "$KEDA" ] || echo "patch scaledobjects in keda (the add-on's own): $(can patch scaledobjects.keda.sh -n keda)"
    [ -z "$KEDA" ] || echo "patch deployments in keda (the add-on itself): $(can patch deployments -n keda)"
    [ -z "$CRANE" ] || echo "delete ehpa/php-apache: $(can delete effectivehorizontalpodautoscalers.autoscaling.crane.io/php-apache -n default)"
    [ -z "$CRANE" ] || echo "patch deployments in crane-system (Crane itself): $(can patch deployments -n crane-system)"
    [ "$ADDONS" != goldilocks ] || echo "patch verticalpodautoscalers (Goldilocks's VPA: its recommendation is the operator's): $(can patch verticalpodautoscalers.autoscaling.k8s.io -n default)"
    [ "$ADDONS" != goldilocks ] || echo "patch deployments in goldilocks (Goldilocks itself): $(can patch deployments -n goldilocks)"
    [ "$ADDONS" != vpa ] || echo "patch verticalpodautoscalers (the VPA's own object): $(can patch verticalpodautoscalers.autoscaling.k8s.io -n default)"
    [ -z "$CRUISEKUBE" ] || echo "patch deployments in cruisekube-system (CruiseKube itself): $(can patch deployments -n cruisekube-system)"
    [ -z "$CRUISEKUBE" ] || echo "get secrets in cruisekube-system (CruiseKube's database): $(can get secrets -n cruisekube-system)"
  } | tee "$OUT_DIR/rbac_omni.txt"
  ! sed -n '/== can/,/== cannot/p' "$OUT_DIR/rbac_omni.txt" | grep ": no$" >/dev/null || { echo "Omni identity is missing a permission it needs"; exit 1; }
  ! sed -n '/== cannot/,$p' "$OUT_DIR/rbac_omni.txt" | grep ": yes$" >/dev/null || { echo "Omni identity has a permission it must not have"; exit 1; }
  export KUBECTL="$(pwd)/scripts/kubectl_omni.sh"
  if [ -n "$KEDA" ]; then
    # the plug: the same service account underneath; the HPA moves carried to the ScaledObject KEDA builds the HPA from
    export OMNI_KUBECTL="$KUBECTL" KUBECTL="$(pwd)/scripts/kubectl_keda.py" OMNI_PLUG_LOG="$(cd "$OUT_DIR" && pwd)/plug_keda.jsonl"
  elif [ -n "$CRANE" ]; then
    # the plug: the same service account underneath; the HPA moves carried to the EHPA Crane builds the HPA from
    export OMNI_KUBECTL="$KUBECTL" KUBECTL="$(pwd)/scripts/kubectl_crane.py" OMNI_PLUG_LOG="$(cd "$OUT_DIR" && pwd)/plug_crane.jsonl"
  fi
fi
kil_pid=""
if [ -n "${ORGANISM:-}" ]; then
  # the organism test: one of the six organisms (tools/run_kil.py) runs on the measured window's clock with this cluster
  # inside as one more muscle; its own compute demand sets the load generator (peak LOAD_MAX), the cluster's watts come
  # back as its heat and load. Built during the warm-up, it starts with the window; the same seed and demand in every arm
  echo "organism=$ORGANISM load_max=${LOAD_MAX:-6}" | tee -a "$OUT_DIR/preflight.txt"
  [ -z "${CALIBRATION:-}" ] || echo "window=${DURATION} calibration=${CALIBRATION}" | tee -a "$OUT_DIR/preflight.txt"
  # the rig's own cores (protocol 3, 13 Oct): the model of the organism runs on the runner's last core and the kind nodes
  # on the others, the same in both arms. The model is the rig's heaviest process and grows with its copies (in
  # Omni-Compass's arm it also carries Omni-Compass's math for every modelled muscle); on cores shared with the cluster it
  # took the cluster's CPU (the 100-copy squares of the card version: the machine 87 to 91% busy, native's own failed
  # requests 32 to 43%, the cluster's CPU 4 to 7% lower in Omni-Compass's arm). Kept apart, the cluster has the same cores
  # at every size and in both arms, and the model's weight shows only on its own clock (behind the window, off the clock)
  PIN=""
  ncpu=$(nproc)
  if [ "$PLATFORM" = kind ] && [ "$ncpu" -ge 2 ] && command -v taskset >/dev/null 2>&1; then
    org_cpu=$((ncpu - 1)); cluster_cpus="0-$((ncpu - 2))"; pinned=0
    for node in $(kind get nodes --name "${KIND_CLUSTER:-omni-bench}" 2>/dev/null); do
      docker update --cpuset-cpus "$cluster_cpus" "$node" >/dev/null && pinned=$((pinned + 1))
    done
    if [ "$pinned" -gt 0 ]; then
      PIN="taskset -c $org_cpu"
      echo "cores: the organism on core $org_cpu, the $pinned kind nodes on cores $cluster_cpus (of $ncpu)" | tee -a "$OUT_DIR/preflight.txt"
    else
      echo "cores: not separated (no kind node found to place)" | tee -a "$OUT_DIR/preflight.txt"
    fi
  fi
  $PIN python tools/run_kil.py --organism "$ORGANISM" --arm "$ARM" --duration "$DURATION" --out "$OUT_DIR" \
    --scale "${ORGANISM_SCALE:-1}" --go-file "$OUT_DIR/organism.go" > "$OUT_DIR/organism.log" 2>&1 &
  kil_pid=$!
fi
echo "== warm-up ${WARMUP}s (both arms)"; sleep "$WARMUP"
# LIST first, then continue from its resourceVersion across bounded API watches.
# Start before the workload and measured window; never infer missing events from a final snapshot.
rm -f "$OUT_DIR/pod_watch.stop" "$OUT_DIR/pod_watch.ready"
python3 tools/bench_integrity.py collect "$OUT_DIR" > "$OUT_DIR/pod_collector.log" 2>&1 &
watch_pid=$!
for i in $(seq 1 60); do
  [ -f "$OUT_DIR/pod_watch.ready" ] && break
  kill -0 "$watch_pid" 2>/dev/null || { echo "pod collector failed before the window"; exit 1; }
  sleep 1
done
[ -f "$OUT_DIR/pod_watch.ready" ] || { echo "pod collector did not become ready"; exit 1; }
if [ -n "${GROUP_BARRIER:-}" ]; then
  # a member of a group of clusters (scripts/kind_group.sh): every member opens its window together, so the group's stream,
  # sent when the last member is ready, falls inside every member's window; a member not ready in 30 minutes fails the arm
  touch "$GROUP_BARRIER/ready-${KIND_CLUSTER:?}"
  for i in $(seq 1 360); do [ "$(find "$GROUP_BARRIER" -name 'ready-*' | wc -l)" -ge "${GROUP_SIZE:?}" ] && break; sleep 5; done
  [ "$(find "$GROUP_BARRIER" -name 'ready-*' | wc -l)" -ge "$GROUP_SIZE" ] || { echo "INVALID RUN: the group's other members did not open their windows"; exit 1; }
  echo "group: member $KIND_CLUSTER of $GROUP_SIZE, the windows opened together at $(date -u +%s)" | tee -a "$OUT_DIR/preflight.txt"
fi
if [ -n "$kil_pid" ]; then
  # a large organism (100 copies) may take longer to build than the warm-up: the window opens when it is built
  until [ -f "$OUT_DIR/organism.ready" ] || ! kill -0 "$kil_pid" 2>/dev/null; do sleep 5; done
  [ -f "$OUT_DIR/organism.ready" ] || { echo "INVALID RUN: the organism stopped before it was built"; tail -20 "$OUT_DIR/organism.log"; exit 1; }
  echo "organism built at epoch $(cat "$OUT_DIR/organism.ready"), scale ${ORGANISM_SCALE:-1}; window opens $(date -u +%s)" | tee -a "$OUT_DIR/preflight.txt"
  date -u +%s > "$OUT_DIR/organism.go.tmp" && mv "$OUT_DIR/organism.go.tmp" "$OUT_DIR/organism.go"   # whole or absent, never half-written
fi

if [ "${WORKLOAD:-web}" = batch ] && [ -n "$BATCH_QUEUE" ]; then
  # the batch stream under a queueing system: the load generator stands at zero; the jobs arrive one every BATCH_EVERY_S
  # seconds from the window's opening, the same schedule in every arm (scripts/kind_batch_queue.sh, PHASE=submit)
  kubectl scale deployment/load-generator --replicas=0 >/dev/null 2>&1 || true
  unit=pods; [ "$BATCH_QUEUE" = kuberay ] && unit="Ray tasks"
  echo "batch: ${BATCH_JOBS:-24} jobs of ${BATCH_COMPLETIONS:-10} $unit, ${BATCH_PARALLELISM:-5} at a time, one every ${BATCH_EVERY_S:-30} s, ${BATCH_MB:-3000} MB hashed each, through $BATCH_QUEUE" | tee -a "$OUT_DIR/preflight.txt"
  OUT_DIR="$OUT_DIR" DURATION="$DURATION" PHASE=submit bash scripts/kind_batch_queue.sh > "$OUT_DIR/batch_submit.out" 2>&1 &
  ( sleep "$DURATION" ) &
  load_pid=$!
elif [ "${WORKLOAD:-web}" = batch ]; then
  # the batch test: the service's load generator stands at zero; a queue of jobs (deploy/kind/batch-jobs.yaml) opens the
  # window, the same queue in every arm. When the last job finishes, the time is written (batch_done.txt); the window
  # runs on to its end, so what each arm does after the work is done (idle, or still holding machines) is measured too
  kubectl scale deployment/load-generator --replicas=0 >/dev/null 2>&1 || true
  sed -e "s/BATCH_COMPLETIONS/${BATCH_COMPLETIONS:-240}/" -e "s/BATCH_PARALLELISM/${BATCH_PARALLELISM:-60}/" \
      -e "s/BATCH_MB/${BATCH_MB:-3000}/" deploy/kind/batch-jobs.yaml | kubectl apply -f - >/dev/null
  echo "batch: ${BATCH_COMPLETIONS:-240} jobs, ${BATCH_PARALLELISM:-60} at a time, ${BATCH_MB:-3000} MB hashed each" | tee -a "$OUT_DIR/preflight.txt"
  ( until [ "$(kubectl get job omni-batch -o jsonpath='{.status.succeeded}' --request-timeout=20s 2>/dev/null)" = "${BATCH_COMPLETIONS:-240}" ]; do sleep 5; done
    date -u +%s > "$OUT_DIR/batch_done.txt" ) &
  ( sleep "$DURATION" ) &
  load_pid=$!
elif [ -n "$kil_pid" ]; then
  load_pid=$kil_pid
elif [ "$LOADGEN" = meter ]; then
  # the work meter steps through its own rates from the moment the window opens (one pod, nothing scaled), the same
  # rates in every arm; its warm-up requests are not counted
  for t in 1 2 3 4 5 6; do kubectl exec deploy/load-generator --request-timeout=20s -- touch /tmp/go && break; sleep 5; done
  echo "$(date -u +%H:%M:%S) work meter: rates $RATE_STEPS per second, $DURATION s, line ${SLO_MS:-500} ms" > "$OUT_DIR/load_schedule.log"
  ( sleep "$DURATION" ) &
  load_pid=$!
else
read -r -a steps <<< "$LOAD_STEPS"
step_s=$(( DURATION / ${#steps[@]} ))
( for r in "${steps[@]}"; do
    echo "$(date -u +%H:%M:%S) load-generator replicas -> $r"
    # the same load in every arm: a scale the API server does not answer is tried again, and a failure is logged,
    # never the end of the schedule
    for t in 1 2 3 4 5 6; do kubectl scale deployment/load-generator --replicas="$r" --request-timeout=20s >/dev/null && break
      echo "$(date -u +%H:%M:%S) scale to $r not answered (try $t)"; sleep 5; done || true
    sleep "$step_s"
  done ) > "$OUT_DIR/load_schedule.log" 2>&1 &
load_pid=$!
fi

# The probe reaches the app through the Service (NodePort on the control plane, deploy/kind/bench-serving.yaml), so a
# drain that moves a pod is seen exactly as a client sees it: kube-proxy sends the request to another ready endpoint.
INTERVAL=5 DURATION="$DURATION" python scripts/latency_probe.py "$PROBE_URL" "$OUT_DIR/latency.csv" &
probe_pid=$!
probe2_pid=""
if [ -n "${TWO_APP:-}" ]; then
  # the noisy neighbour's own response time, and its load surging in steps (the same steps in every arm)
  INTERVAL=5 DURATION="$DURATION" python scripts/latency_probe.py "${PROBE_URL%:30080/}:30081/" "$OUT_DIR/latency_noisy.csv" &
  probe2_pid=$!
  read -r -a nsteps <<< "${NOISY_STEPS:-0 0 6 0 6 0}"
  ( for r in "${nsteps[@]}"; do
      echo "$(date -u +%H:%M:%S) load-noisy replicas -> $r"
      kubectl scale deployment/load-noisy --replicas="$r" >/dev/null
      sleep $(( DURATION / ${#nsteps[@]} ))
    done ) > "$OUT_DIR/noisy_schedule.log" 2>&1 &
fi
fault_pid=""
if [ -n "${FAULTS:-}" ]; then
  # the fault test: the same faults at the same moments in every arm (scripts/kind_faults.sh)
  OUT_DIR="$OUT_DIR" DURATION="$DURATION" PROBE_PID="$probe_pid" bash scripts/kind_faults.sh > "$OUT_DIR/faults.out" 2>&1 &
  fault_pid=$!
fi
# every start of a serving pod, timed exactly: the API server's own record of each pod from creation to Ready, streamed
# for the whole measured window (pilot/bench_report.py pod_starts), in every arm alike
rapl_pid=""
if [ -n "$METER" ]; then   # the machine's own meter, from just before the window opens to just after it closes
  python3 tools/rapl.py sample --out "$OUT_DIR/rapl.csv" --interval 2 > "$OUT_DIR/rapl_sampler.log" 2>&1 &
  rapl_pid=$!; sleep 3
  [ "$(wc -l < "$OUT_DIR/rapl.csv" 2>/dev/null || echo 0)" -ge 2 ] || { echo "the machine's meter did not start"; cat "$OUT_DIR/rapl_sampler.log"; exit 1; }
  [ -z "$KEPLER" ] || OUT_DIR="$OUT_DIR" PHASE=read TAG=start bash scripts/kind_addons_kepler.sh
fi
date -u +%s > "$OUT_DIR/window_start.txt"
meter_pid=""
if [ "$PLATFORM" = aks ]; then
  # the bill: every worker machine that exists is billed, in service or idle; every 15 s, how many exist (Omni never
  # reads this file)
  # ... and how many in each work pool (pool=count;...), so a fleet of several machine families is billed at each family's price
  ( echo "epoch_s,machines,pools"; while :; do
      nodes=$(kubectl get nodes -l "$WORKER_SEL" -o jsonpath='{range .items[*]}{.metadata.labels.agentpool}{"\n"}{end}' 2>/dev/null)
      echo "$(date -u +%s),$(echo -n "$nodes" | grep -c .),$(echo -n "$nodes" | grep . | sort | uniq -c | awk '{printf "%s=%s;", $2, $1}')"; sleep 15; done ) > "$OUT_DIR/billed_nodes.csv" &
  meter_pid=$!
fi
# the real machine under the cluster: on kind every worker reports all of the host's cores as its own, so "used /
# allocatable" counts the same cores once per worker. The host's own busy share (/proc/stat, every 5 s) and its real core
# count say how full the machine that does the work actually is (Omni never reads this file)
host_pid=""
if [ "$PLATFORM" != aks ]; then
  # (and the memory the machine has left, every 5 s: 22 October, a runner went silent with no file left, run 39657032525)
  ( echo "epoch_s,busy,cores,mem_avail_mb"; read -r _ a b c d e f g h _ < /proc/stat; pt=$((a+b+c+d+e+f+g+h)); pi=$((d+e))
    while sleep 5; do read -r _ a b c d e f g h _ < /proc/stat; t=$((a+b+c+d+e+f+g+h)); i=$((d+e))
      echo "$(date -u +%s),$(awk -v dt=$((t-pt)) -v di=$((i-pi)) 'BEGIN{printf "%.4f", (dt > 0 ? 1 - di / dt : 0)}'),$(nproc),$(awk '/^MemAvailable:/ {printf "%d", $2 / 1024}' /proc/meminfo)"; pt=$t; pi=$i; done ) > "$OUT_DIR/host_cpu.csv" &
  host_pid=$!
fi
omni_pid=""
# the governor's full decision every OMNI_INTERVAL seconds and its fast checks (the scheduling floor, the pod reflex, and
# the conveyance every 15 s) every OMNI_FLOOR_INTERVAL seconds: 60 and 5 by default (omni-v17, the founder's word of 22
# October, afternoon: the main engine at 60 s, the heartbeat a dial). Every clock of the governor counts seconds, so the
# decision period changes only how often it looks (docs/PACE_PREREGISTRATION.md; the pace arms compass5 to compass120 of
# scripts/kind_paired.sh set it); the fast checks' period stays under the decision's. The period is written beside the
# run's files, so a receipt reads each run at its own (tools/live_reps.py)
export OMNI_INTERVAL="${OMNI_INTERVAL:-60}" OMNI_FLOOR_INTERVAL="${OMNI_FLOOR_INTERVAL:-5}"
mkdir -p "$OUT_DIR" && printf '%s\n' "$OMNI_INTERVAL" > "$OUT_DIR/omni_interval.txt"
# the governor's command line, once, so the robustness test (below) can start a second governor with the same wiring
start_controller() {   # $1 decisions to make, $2 log file
  $GOV_PIN nice -n "$OMNI_NICE" python -m omni_controller.controller $DRY --kubectl "$KUBECTL" --mode nodepool --active-nodes-only --interval "$OMNI_INTERVAL" --floor-interval "$OMNI_FLOOR_INTERVAL" --reflex-window-s 15 \
    --iterations "$1" --min-nodes "${MIN_NODES:-2}" --max-nodes "$(( WORKERS - ${NODE_CUSHION:-0} ))" --max-node-step 1 \
    --node-scale-cmd "bash scripts/kind_nodepool.sh {n}" --node-restore-cmd "bash scripts/kind_nodepool.sh $WORKERS" \
    ${OMNI_POWER_CMD:+--power-cmd "$OMNI_POWER_CMD"} --site-limit-w "$SITE_LIMIT_W" \
    $CAP_ARGS --thermal-model --security-configmap default/omni-security \
    --rollout-guard default/php-apache --sensed "$OMNI_SENSED" --latency-file "$OUT_DIR/latency.csv" --slo-ms "${SLO_MS:-500}" \
    --audit "$OUT_DIR/audit.jsonl" --kill-file "$OUT_DIR/kill" $STRICT $LAW $OWN ${CLOSURE:+--closure "$CLOSURE"} ${REPLICA_CEILING:+--replica-ceiling "$REPLICA_CEILING"} ${OMNI_DIAL:+--dial "$OMNI_DIAL"} > "$2" 2>&1 &
  echo $!
}
# the window's governor is not a child of this shell (start_controller runs in a subshell), so `wait` cannot see it (12
# Oct: "wait: pid ... is not a child of this shell"; a governor behind its cadence was still deciding at the reset). A
# governor still running when the window has ended is stopped through the master switch (SIGTERM: it hands every
# setting back and exits) and watched by its pid until it is gone, before any check reads the cluster
stop_governors() {
  local p i
  for p in "$omni_pid" $(cat "$OUT_DIR/omni2.pid" 2>/dev/null); do
    { [ -n "$p" ] && kill -0 "$p" 2>/dev/null; } || continue
    echo "the governor (pid $p) was still deciding when the window ended: stopped through the master switch" | tee -a "$OUT_DIR/governor_end.txt"
    kill -TERM "$p" 2>/dev/null || true
    for i in $(seq 1 60); do kill -0 "$p" 2>/dev/null || break; sleep 1; done
    if kill -0 "$p" 2>/dev/null; then
      echo "the governor (pid $p) did not stop in 60 s: stopped outright" | tee -a "$OUT_DIR/governor_end.txt"; kill -KILL "$p" 2>/dev/null || true
    fi
  done
}
watchdog_pid=""
if [ -z "$NATIVE" ]; then
  echo "== ARM $ARM: Omni-Compass driving HPA target + node pool + power sensing${DRY:+ (dry run: watches only, writes nothing)}"
  if [ -n "${ROBUST:-}" ]; then
    # the robustness test (docs/ROBUSTNESS_PREREGISTRATION.md): the governor registers its lease in this arm's own
    # registry, and the watchdog runs beside it from the start, as it would in service
    export OMNI_REGISTRY="$OUT_DIR/registry"
    python tools/omni_switch.py watchdog --every 5 > "$OUT_DIR/watchdog.log" 2>&1 &
    watchdog_pid=$!
  fi
  omni_pid=$(start_controller $(( DURATION / OMNI_INTERVAL )) "$OUT_DIR/controller.log")
else
  echo "== ARM native: Omni-Compass not running; Kubernetes alone"
fi
robust_pid=""
if [ -n "${ROBUST:-}" ]; then
  # scenario 1 (ROBUST=kill): at 40% of the window the governor is killed outright (SIGKILL, no chance to hand back); the
  # harness then asks the cluster every 2 s until every setting is back at the operator's (the watchdog's doing), and at
  # 50% starts a second governor that governs to the end. Native gets the same time marks and nothing else. Scenario 2
  # (ROBUST=long): no kill; the governor runs the whole long window. In both the governor's resident memory is sampled
  # every 15 s from the process table (never by the governor itself: no engine file changes).
  if [ -z "$NATIVE" ]; then
    # the second governor is started by the robustness script when its moment comes, with the same command line: the
    # function and what it reads are exported before the script starts
    export -f start_controller
    # (17 Oct: a variable added on 15 October, the cloud's GIVE_BACK_ONLY, struck on 31 October, was missing here, so the second
    # governor stopped on an unbound variable before it began and every kill run of omni-v7 was marked invalid;
    # tests/test_robust_restart.py now checks the list, and caught GOV_PIN, the governor's own core, on 20 October before any
    # run, and OWN, omni-v19's pod muscle of its own, on 24 October before any run of ARM=solo)
    export CAP_ARGS DRY KUBECTL WORKERS SITE_LIMIT_W OUT_DIR STRICT LAW CLOSURE REPLICA_CEILING OMNI_DIAL MIN_NODES NODE_CUSHION SLO_MS OMNI_NICE OMNI_SENSED OMNI_POWER_CMD GOV_PIN OWN
  fi
  OUT_DIR="$OUT_DIR" DURATION="$DURATION" ROBUST="$ROBUST" OMNI_PID="$omni_pid" WORKERS="$WORKERS" HPA_RANGE="$HPA_RANGE" \
    WORKER_SEL="$WORKER_SEL" NATIVE="$NATIVE" bash scripts/kind_robust.sh > "$OUT_DIR/robust.out" 2>&1 &
  robust_pid=$!
fi

ACTIVE_ONLY=1 INTERVAL=15 DURATION="$DURATION" POWER_CMD="bash scripts/kind_power.sh" OUT="$OUT_DIR/capture.csv" \
  bash fleet/capture/kube_capture.sh
if [ -n "$kil_pid" ]; then
  wait "$kil_pid" || { echo "INVALID RUN: the organism did not hand every simulated knob back (organism.log)"; tail -5 "$OUT_DIR/organism.log"; exit 1; }
  tail -1 "$OUT_DIR/organism.log"
else
  wait "$load_pid" || true
fi
wait "$probe_pid" || true
[ -n "$probe2_pid" ] && { wait "$probe2_pid" || true; }
[ -n "$fault_pid" ] && { wait "$fault_pid" || true; }
date -u +%s > "$OUT_DIR/window_end.txt"
if [ -n "$rapl_pid" ]; then
  [ -z "$KEPLER" ] || OUT_DIR="$OUT_DIR" PHASE=read TAG=end bash scripts/kind_addons_kepler.sh
  sleep 3; kill "$rapl_pid" 2>/dev/null || true; wait "$rapl_pid" 2>/dev/null || true
  python3 tools/rapl.py window "$OUT_DIR/rapl.csv" "$(cat "$OUT_DIR/window_start.txt")" "$(cat "$OUT_DIR/window_end.txt")" > "$OUT_DIR/rapl_window.json" || true
fi
[ -n "$meter_pid" ] && { kill "$meter_pid" 2>/dev/null || true; }
[ -n "$host_pid" ] && { kill "$host_pid" 2>/dev/null || true; }
# the end-of-window record: a read the API server does not answer is tried again, never the end of the run
end_read() { local f="$1"; shift; for t in 1 2 3 4 5 6; do kubectl "$@" --request-timeout=20s > "$f" 2>>"$OUT_DIR/end_reads.err" && return 0; sleep 10; done
  echo "the API server did not answer: kubectl $*" >> "$OUT_DIR/end_reads.err"; return 1; }
end_read "$OUT_DIR/pods_end.json" get pods -n default -l run=php-apache -o json
touch "$OUT_DIR/pod_watch.stop"
wait "$watch_pid"
watch_pid=""
python3 tools/bench_integrity.py validate "$OUT_DIR" > "$OUT_DIR/pod_watch_validation.json"
if [ -n "$robust_pid" ]; then
  wait "$robust_pid" || { echo "INVALID RUN: robustness helper failed; see robust.out"; exit 1; }
  # the second governor of the kill scenario was started by the robustness script: wait for it to finish its decisions
  if [ -f "$OUT_DIR/omni2.pid" ]; then
    p2=$(cat "$OUT_DIR/omni2.pid"); while kill -0 "$p2" 2>/dev/null; do sleep 2; done
  fi
fi
if [ "$LOADGEN" = meter ]; then
  # the meter's final count (it prints it once its last requests have had their full time to answer)
  for t in $(seq 1 30); do
    kubectl logs deploy/load-generator --request-timeout=20s 2>/dev/null | grep '"final": true' | tail -1 > "$OUT_DIR/work_meter.json" || true
    [ -s "$OUT_DIR/work_meter.json" ] && break; sleep 5
  done
  [ -s "$OUT_DIR/work_meter.json" ] || { echo "INVALID RUN: the work meter gave no final count"; exit 1; }
  echo "work meter: $(jq -c .total "$OUT_DIR/work_meter.json")" | tee -a "$OUT_DIR/preflight.txt"
fi
end_read "$OUT_DIR/nodes_end.txt" get nodes -o wide
# by itself the pod autoscaler is removed by design, so its read is the workload's own (this read of the autoscaler, added
# 29 October, ended every solo arm of the omni-v22 campaign's first two runs with exit 1: docs/SOLO_PREREGISTRATION.md, amendment 1)
if [ "$ARM" = "solo" ]; then end_read "$OUT_DIR/workload_end.json" get deployment php-apache -o json
else end_read "$OUT_DIR/hpa_end.json" get hpa "$HPA_NAME" -o json; fi
if [ -n "$KEDA" ]; then   # the add-on's own record of the window: its ScaledObject and the last words of each part
  end_read "$OUT_DIR/scaledobject_end.json" get scaledobject php-apache -o json
  for d in keda-operator keda-add-ons-http-scaler keda-add-ons-http-interceptor; do
    kubectl -n keda logs deployment/"$d" --tail=300 --request-timeout=20s > "$OUT_DIR/$d.log" 2>&1 || true
  done
elif [ -n "$CRANE" ]; then   # Crane's own record of the window: its EHPA, its forecast and the last words of craned
  end_read "$OUT_DIR/ehpa_end.json" get effectivehorizontalpodautoscalers.autoscaling.crane.io php-apache -o json
  end_read "$OUT_DIR/crane_predictions_end.json" get timeseriespredictions.prediction.crane.io -A -o json
  kubectl -n crane-system logs deployment/craned --tail=300 --request-timeout=20s > "$OUT_DIR/craned.log" 2>&1 || true
elif [ "$ADDONS" = goldilocks ]; then   # Goldilocks's VPA as the window left it (its recommendation, still in mode Off)
  end_read "$OUT_DIR/vpa_end.json" get vpa goldilocks-php-apache -o json
  kubectl -n goldilocks logs deployment/goldilocks-controller --tail=300 --request-timeout=20s > "$OUT_DIR/goldilocks-controller.log" 2>&1 || true
  kubectl -n kube-system logs deployment/vpa-recommender --tail=300 --request-timeout=20s > "$OUT_DIR/vpa-recommender.log" 2>&1 || true
elif [ "$ADDONS" = vpa ]; then   # the VPA's own record of the window: its object, the pods it resized, its three parts' last words
  end_read "$OUT_DIR/vpa_end.json" get vpa php-apache -o json
  end_read "$OUT_DIR/vpa_pods_end.json" get pods -n default -l run=php-apache -o json
  for d in vpa-recommender vpa-updater vpa-admission-controller; do
    kubectl -n kube-system logs deployment/"$d" --tail=300 --request-timeout=20s > "$OUT_DIR/$d.log" 2>&1 || true
  done
fi
if [ -n "$CRUISEKUBE" ]; then   # CruiseKube's own record of the window: its audit events, its workload view, its logs
  OUT_DIR="$OUT_DIR" PHASE=end bash scripts/kind_addons_cruisekube.sh || true
  end_read "$OUT_DIR/cruisekube_resources_end.json" get pods -n default -l run=php-apache -o json
fi
[ -z "$KEPLER" ] || { OUT_DIR="$OUT_DIR" PHASE=end bash scripts/kind_addons_kepler.sh || true; }
[ -z "$BATCH_QUEUE" ] || { OUT_DIR="$OUT_DIR" PHASE=end bash scripts/kind_batch_queue.sh || true; }   # every job's and pod's times

if [ "$ARM" = "watch" ]; then
  echo "== watch arm: nothing may have reached the cluster"
  executed=$(grep '"write"' "$OUT_DIR/audit.jsonl" | grep -c '"dry_run": false' || true)
  logged=$(grep -c '"write"' "$OUT_DIR/audit.jsonl" || true)
  echo "writes Omni would have made: $logged; writes executed: $executed" | tee "$OUT_DIR/omni_writes.txt"
  stop_governors        # counted first: a stopped governor's hand-back is logged as writes (dry, none executed)
  cpu_limit=$(limits_now)
  target=$(hpa_cpu_target "$HPA_NAME")
  range_now=$(kubectl get hpa "$HPA_NAME" -o jsonpath='{.spec.minReplicas},{.spec.maxReplicas}')
  back=$(kubectl get nodes -l "$WORKER_SEL" -o json | jq '[.items[] | select(.spec.unschedulable != true and (any(.spec.taints[]?; .key == "omnicompass.io/idle") | not))] | length')
  echo "cluster after the run: target $target, range $range_now, CPU limits $cpu_limit, workers $back of $WORKERS" | tee "$OUT_DIR/kill_switch.txt"
  exist=$(kubectl get nodes -l "$WORKER_SEL" --no-headers | wc -l); [ "$PLATFORM" = aks ] || exist="$WORKERS"
  test "$executed" = "0" && test "$target" = "$EXPECT_TARGET" && test "$range_now" = "$HPA_RANGE" && test "$cpu_limit" = "$EXPECT_LIMIT" && test "$back" = "$exist"
elif [ -z "$NATIVE" ]; then
  echo "== reset"
  touch "$OUT_DIR/kill"
  omni_writes=$(grep -c '"write"' "$OUT_DIR/audit.jsonl" || true)
  echo "omni writes during the run: $omni_writes" | tee "$OUT_DIR/omni_writes.txt"
  if [ "$omni_writes" -eq 0 ]; then
    # staying native is the governor's own decision, made at every step (the founder's order of 10 October): a window
    # with no write is valid when the governor recorded its decisions, each with its reasons in the audit, and the reset
    # below still checks every setting is the operator's; a governor that recorded no decisions was not running
    decisions=$(grep -c '"decision"' "$OUT_DIR/audit.jsonl" || true)
    failed=$(grep -c '"consecutive_failures"' "$OUT_DIR/audit.jsonl" || true)
    want=$(( DURATION / 60 - 1 )); [ "$want" -ge 1 ] || want=1
    # a decision that failed wrote nothing and left its error in the audit: the window is still refused, in the words of
    # what happened (18 Oct, the CruiseKube test, run 39120444653, repetition 8: the cluster showed no machine in service
    # for two minutes, two decisions failed on it, and the old words said the governor was not running)
    [ "$decisions" -ge "$want" ] || [ "$failed" -eq 0 ] || { echo "Omni made no write and recorded $decisions decisions (at least $want expected); $failed more failed and wrote nothing, the last with $(grep '"consecutive_failures"' "$OUT_DIR/audit.jsonl" | tail -n 1 | jq -r .error)"; exit 1; }
    [ "$decisions" -ge "$want" ] || { echo "Omni made no write and recorded $decisions decisions (at least $want expected): the governor was not running"; exit 1; }
    echo "Omni-Compass stayed native: $decisions decisions recorded, no write" | tee "$OUT_DIR/omni_stayed_native.txt"
  fi
  stop_governors        # no write of the window's governor can land after the reset is checked
  # Reconcile the benchmark-owned pause atomically even when another writer already resumed it.
  python3 tools/bench_integrity.py restore-rollout default/php-apache --kubectl "$KUBECTL" > "$OUT_DIR/rollout_reset.json"
  python -m omni_controller.controller --kubectl "$KUBECTL" --mode nodepool --active-nodes-only --iterations 1 \
    $CAP_ARGS --rollout-guard default/php-apache $OWN \
    --node-restore-cmd "bash scripts/kind_nodepool.sh $WORKERS" --audit "$OUT_DIR/audit_kill.jsonl" --kill-file "$OUT_DIR/kill"
  cpu_limit=$(limits_now)
  if [ -n "$CAP_ARGS" ]; then echo "pod CPU limits after kill: $cpu_limit" | tee -a "$OUT_DIR/kill_switch.txt"
  elif [ -n "$CRUISEKUBE" ]; then echo "the operator's CPU limit on the Deployment after kill: $cpu_limit (CruiseKube owns the pods' own)" | tee -a "$OUT_DIR/kill_switch.txt"
  elif [ -n "$NO_RESIZE" ]; then echo "pod CPU limits after kill: $cpu_limit (the cluster serves no in-place resize: no processor conveyed, no power capped)" | tee -a "$OUT_DIR/kill_switch.txt"
  else echo "the operator's CPU limit on the Deployment after kill: $cpu_limit (the governor moved the machines alone: no processor conveyed)" | tee -a "$OUT_DIR/kill_switch.txt"; fi
  if [ -n "$KEDA" ] || [ -n "$CRANE" ]; then   # the add-on rebuilds the HPA from its own object: the operator's settings must show on it
    for i in $(seq 1 15); do
      [ "$(hpa_cpu_target "$HPA_NAME")" = "$EXPECT_TARGET" ] && [ "$(kubectl get hpa "$HPA_NAME" -o jsonpath='{.spec.minReplicas},{.spec.maxReplicas}')" = "$HPA_RANGE" ] && break
      sleep 2
    done
  fi
  if [ "$ARM" = "solo" ]; then
    # by itself: no autoscaler; the workload back at the count it started at and no record of Omni's left on it (the
    # operator's own target and range stay, written before the window)
    restored="$EXPECT_TARGET"; range_now="$HPA_RANGE"
    rep_now=$(kubectl get deployment php-apache -o jsonpath='{.spec.replicas}')
    echo "the workload's replicas after kill: $rep_now (the count it started at: ${SOLO_RANGE%%,*})" | tee -a "$OUT_DIR/kill_switch.txt"
    test "$rep_now" = "${SOLO_RANGE%%,*}"
    hpa_left=$(kubectl get hpa -n default --no-headers 2>/dev/null | wc -l)
    [ "$hpa_left" -eq 0 ] || { echo "INVALID RUN: by itself, an autoscaler stands on the workload at the end ($hpa_left): the knob was handed back to native's own autoscaler (omni-v23), so Omni-Compass did not run the arm by itself"; exit 1; }
  else
  restored=$(hpa_cpu_target "$HPA_NAME")
  range_now=$(kubectl get hpa "$HPA_NAME" -o jsonpath='{.spec.minReplicas},{.spec.maxReplicas}')
  echo "HPA replica range after kill: $range_now" | tee -a "$OUT_DIR/kill_switch.txt"
  test "$range_now" = "$HPA_RANGE"
  fi
  back=$(kubectl get nodes -l "$WORKER_SEL" -o json | jq '[.items[] | select(.spec.unschedulable != true and (any(.spec.taints[]?; .key == "omnicompass.io/idle") | not))] | length')
  { echo "restored target: $restored"; echo "workers in service: $back of $WORKERS"; } | tee "$OUT_DIR/kill_switch.txt"
  if [ "$ARM" = "solo" ]; then   # no autoscaler to read; the operator's own target and range on the workload are not Omni's records
    leftover=$(kubectl get deployment php-apache -o json | jq -r '.metadata.annotations // {} | keys[] | select(startswith("omnicompass.io/")) | select(. != "omnicompass.io/target-utilization" and . != "omnicompass.io/replica-range")')
  else
  leftover=$(kubectl get hpa "$HPA_NAME" -o json | jq -r '.metadata.annotations // {} | keys[] | select(startswith("omnicompass.io/"))'; kubectl get deployment php-apache -o json | jq -r '.metadata.annotations // {} | keys[] | select(startswith("omnicompass.io/"))')
  fi
  if [ -n "$KEDA" ]; then   # the add-on's ScaledObject: the operator's own settings back, and no record left on it either
    leftover="$leftover$(kubectl get scaledobject php-apache -o json | jq -r '.metadata.annotations // {} | keys[] | select(startswith("omnicompass.io/"))')"
    so_now=$(kubectl get scaledobject php-apache -o json | jq -c '{min: .spec.minReplicaCount, max: .spec.maxReplicaCount, cpu: ([.spec.triggers[] | select(.type == "cpu") | .metadata.value][0] // "")}')
    so_want=$(jq -cn --argjson max "${HPA_MAX:-10}" --arg cpu "$EXPECT_TARGET" '{min: 1, max: $max, cpu: $cpu}')
    echo "add-on's ScaledObject after kill: $so_now (the operator's: $so_want)" | tee -a "$OUT_DIR/kill_switch.txt"
    test "$so_now" = "$so_want"
  fi
  if [ -n "$CRANE" ]; then   # Crane's EHPA: the operator's own settings back, and no record left on it either
    leftover="$leftover$(kubectl get effectivehorizontalpodautoscalers.autoscaling.crane.io php-apache -o json | jq -r '.metadata.annotations // {} | keys[] | select(startswith("omnicompass.io/"))')"
    ehpa_now=$(kubectl get effectivehorizontalpodautoscalers.autoscaling.crane.io php-apache -o json | jq -c '{min: .spec.minReplicas, max: .spec.maxReplicas, cpu: ([.spec.metrics[] | select(.type == "Resource" and .resource.name == "cpu") | .resource.target.averageUtilization][0] // "" | tostring)}')
    ehpa_want=$(jq -cn --argjson max "${HPA_MAX:-10}" --arg cpu "$EXPECT_TARGET" '{min: 1, max: $max, cpu: $cpu}')
    echo "Crane's EHPA after kill: $ehpa_now (the operator's: $ehpa_want)" | tee -a "$OUT_DIR/kill_switch.txt"
    test "$ehpa_now" = "$ehpa_want"
  fi
  echo "Omni records left after kill: ${leftover:-none}" | tee -a "$OUT_DIR/kill_switch.txt"
  if [ -n "${TWO_APP:-}" ]; then   # the fairness test: the neighbour's HPA handed back too
    n_restored=$(kubectl get hpa php-noisy -o jsonpath='{.spec.metrics[0].resource.target.averageUtilization}')
    echo "noisy neighbour's restored target: $n_restored" | tee -a "$OUT_DIR/kill_switch.txt"; test "$n_restored" = "50"
  fi
  exist=$(kubectl get nodes -l "$WORKER_SEL" --no-headers | wc -l); [ "$PLATFORM" = aks ] || exist="$WORKERS"
  test "$restored" = "$EXPECT_TARGET" && test "$back" = "$exist" && test "$cpu_limit" = "$EXPECT_LIMIT" && test -z "$leftover"
fi
[ -n "$watchdog_pid" ] && { kill "$watchdog_pid" 2>/dev/null || true; }
echo "rows captured: $(( $(wc -l < "$OUT_DIR/capture.csv") - 1 ))"
( cd "$OUT_DIR" && sha256sum $(ls -1 -p | grep -v '/$' | grep -v '^SHA256SUMS.txt$') > SHA256SUMS.txt )
if [ -z "$NATIVE" ]; then
  # Evidence discipline: the run counts only if the engine decided for the whole run. Its decisions inside the measured
  # window (window_start.txt to window_end.txt) are counted, never one made after the window ended (amendment of 12 Oct;
  # before, every decision record up to the reset counted, the kill switch's own included), with the mean time between
  # them (the cadence is one a minute)
  dec=$(python - "$OUT_DIR/audit.jsonl" "$(cat "$OUT_DIR/window_start.txt")" "$(cat "$OUT_DIR/window_end.txt")" <<'PY' || echo "0 n/a 0"
import json, sys
ws, we = float(sys.argv[2]), float(sys.argv[3])
t_all = []
for line in open(sys.argv[1]):
    try:
        r = json.loads(line)
    except ValueError:
        continue                      # a line cut short by a governor stopped outright is not a decision
    if isinstance(r, dict) and isinstance(r.get("decision"), dict):
        t_all.append(float(r["time"]))
t_in = [t for t in t_all if ws <= t <= we]
print(len(t_in), f"{(t_in[-1] - t_in[0]) / (len(t_in) - 1):.1f}" if len(t_in) > 1 else "n/a", len(t_all))
PY
)
  read -r decisions period all_decisions <<< "$dec"; expected=$(( DURATION / OMNI_INTERVAL ))
  errors=$(grep -c '"error"' "$OUT_DIR/audit.jsonl" || true)
  echo "== controller: decisions inside the window $decisions of $expected (one every $period s; $all_decisions in all), failed decisions or checks $errors"
  echo "-- controller's own cost (CPU of the process and every command it ran): $(grep '"overhead"' "$OUT_DIR/audit.jsonl" | tail -n 1)"
  echo "-- my writes by muscle (count, first words of why)"
  jq -r 'select(.write) | .why // "?" | split(":")[0] + ": " + (split(":")[1] // "" | ltrimstr(" ") | split(" ")[0:3] | join(" "))' "$OUT_DIR/audit.jsonl" | sort | uniq -c | sort -rn | head -n 20 || true
  echo "-- conveyed CPU limits (last 8)"; grep '"convey:' "$OUT_DIR/audit.jsonl" | jq -r '.why' | tail -n 8 || true
  echo "-- pod reflex (last 8)"; grep '"pod reflex:' "$OUT_DIR/audit.jsonl" | jq -r '.why' | tail -n 8 || true
  echo "-- controller.log (last 40 lines)"; tail -n 40 "$OUT_DIR/controller.log" || true
  echo "-- audit errors (last 10)"; grep '"error"\|"failsafe"' "$OUT_DIR/audit.jsonl" | tail -n 10 || true
  echo "-- decision trail (nodes seen -> recommended | p95 ms | SLO clean | calm | node-view calm | node gate)"
  python - "$OUT_DIR/audit.jsonl" <<'PY' || true
import json, sys
sys.path.insert(0, ".")
from omnicompass.compass import say
auth = None
for line in open(sys.argv[1]):
    r = json.loads(line)
    if "compass" in r:
        print("  compass:", say(r["compass"]))
    elif "authority" in r:
        auth = r["authority"]
    elif isinstance(r.get("decision"), dict):
        d = r["decision"]; a = auth or {}
        print(f"  {d['nodes_observed']} -> {d['nodes_recommended']} | p95 {d.get('latency_p95_ms')} | clean {d.get('slo_clean')} | "
              f"calm {a.get('calm')} | node calm {a.get('node_view', {}).get('calm')} | gate {a.get('node_gate', {}).get('reason')} | "
              f"queue {d.get('queue_ratio')} | U {d['U']:.3f} | blind {[k for k, v in a.get('senses', {}).get('blind', {}).items() if v]} | "
              f"latency age {a.get('senses', {}).get('latency_age_s')} s | proprioception {a.get('proprioception')}")
PY
  [ $(( decisions * 10 )) -ge $(( expected * 8 )) ] || { echo "INVALID RUN: the controller made $decisions of its $expected decisions inside the window (under 80%)"; exit 1; }
  ! grep -q '"failsafe"' "$OUT_DIR/audit.jsonl" || { echo "INVALID RUN: the fail-safe handed control back to native"; exit 1; }
  if [ "$ARM" = "solo" ]; then
    # by itself, a knob Omni-Compass owns has no other controller (the founder's order of 31 October: every muscle Omni-Compass
    # cannot be stays; a knob left with no working controller fails the whole system): a decision that failed left that knob
    # unmoved, so the window is refused (docs/SOLO_PREREGISTRATION.md, amendment 2). omni-v23: a knob whose writes the cluster
    # refused three times in a row was handed back to native's own autoscaler, so the organism kept a controller, but
    # Omni-Compass did not run this arm by itself: refused as a result of the arm, with the words
    ! grep -q '"handed_back"' "$OUT_DIR/audit.jsonl" || { echo "INVALID RUN: by itself, the knob was handed back to native's own autoscaler (omni-v23; the cluster refused the muscle's writes): the organism kept a controller, and Omni-Compass did not run the arm by itself ($(grep '"handed_back"' "$OUT_DIR/audit.jsonl" | tail -1 | cut -c1-300))"; exit 1; }
    refused=$(grep -c '"consecutive_failures"' "$OUT_DIR/audit.jsonl" || true)
    [ "$refused" -eq 0 ] || { echo "INVALID RUN: by itself, $refused decisions of Omni-Compass failed and left a knob it owns with no controller (the last: $(grep '"consecutive_failures"' "$OUT_DIR/audit.jsonl" | tail -1 | cut -c1-300))"; exit 1; }
  fi
  if [ -n "$KEDA" ]; then
    # the add-on test counts only if every move Omni-Compass made on the autoscaler reached KEDA whole
    pl="$OUT_DIR/plug_keda.jsonl"
    echo "-- the plug: $(grep -c '"hpa_shows"' "$pl" 2>/dev/null || true) writes carried to the add-on's ScaledObject," \
      "$(grep -c '"hpa_shows": true' "$pl" 2>/dev/null || true) shown on the HPA, $(grep -c '"refused"' "$pl" 2>/dev/null || true) refused"
    ! grep -q '"refused"\|"hpa_shows": false' "$pl" 2>/dev/null || { echo "INVALID RUN: a move of Omni-Compass did not reach the add-on whole ($pl)"; exit 1; }
  fi
fi
# a reading in which the cluster had no machine in service leaves the window's machine count wrong, in either arm (18 Oct,
# the CruiseKube test, run 39120444653, repetition 8: every worker of the kind cluster left service for two minutes while
# the service answered every probe): the window is refused, never scored. The nodes as they stood are in capture.csv.errors
blank=$(awk -F, 'NR > 1 && $4 == 0' "$OUT_DIR/capture.csv" | wc -l)
[ "$blank" -eq 0 ] || { echo "INVALID RUN: the cluster showed no machine in service in $blank of the window's readings"; exit 1; }
