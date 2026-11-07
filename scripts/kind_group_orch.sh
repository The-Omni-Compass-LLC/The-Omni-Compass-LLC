#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
#
# The group's orchestrator and its stream (scripts/kind_group.sh; docs/GROUP_PREREGISTRATION.md). D is the arm's folder,
# N the members (kind clusters omni-m1 ... omni-mN, their kubeconfigs in D), ORCH karmada, ocm, armada or none (the group
# alone).
#   PHASE=install  (karmada) Karmada as its own CLI installs it on a cluster of its own (omni-host), from its pinned release
#                  (karmadactl and the CRD archive checked against their pinned SHA-256), every member joined to it in push
#                  mode, and the operator's one propagation policy for the stream (deploy/kind/karmada-propagation.yaml);
#                  (ocm) Open Cluster Management's hub as its own CLI installs it on omni-host (clusteradm, checked against
#                  its pinned SHA-256, the pinned bundle), every member registered by clusteradm join and accepted on the
#                  hub, and the default cluster set bound to the namespace the placements live in; (armada) Armada's control
#                  plane as its own local stack runs it (its server, scheduler, ingesters and the dependencies they need,
#                  from the pinned images, as containers on the runner's own network) and one executor per member, each
#                  reaching its member by the member's kubeconfig; one queue for the stream
#   PHASE=submit   once every member's window is open: the batch rig's stream, BATCH_JOBS jobs one every BATCH_EVERY_S
#                  seconds (deploy/kind/batch-stream-job.yaml, as scripts/kind_batch_queue.sh writes it), each sent to the
#                  orchestrator (Karmada: the job to its API server; OCM: a Placement of its own, OCM's decision, then the
#                  job as a ManifestWork in the chosen member's namespace; Armada: the job as a job set of its pods, each a
#                  job of the queue, placed by Armada's scheduler), or on the group alone to the members in turn;
#                  batch_done.txt once every job has succeeded
#   PHASE=end      the orchestrator's own record of every job (orch_jobs.json) and of where it placed each (orch_end.json)
# Credentials (Karmada's certificates, the members' kubeconfigs for it and for Armada's executors, OCM's bootstrap token)
# stay outside the run's files and are removed at the end.
set -euo pipefail
D="${D:?}"; N="${N:?}"; ORCH="${ORCH:?}"
KARMADA_VERSION="${KARMADA_VERSION:-v1.19.0}"   # released 31 August 2026
KARMADACTL_SHA256="${KARMADACTL_SHA256:-cf690eacc25ed13b6a27366c1b0b33e0e6edd2833e379922d420a5355550ef3d}"   # karmadactl-linux-amd64.tgz
KARMADA_CRDS_SHA256="${KARMADA_CRDS_SHA256:-e8d225a910924432f90d0e0397890d7d94b5a444b32e4586343570feeeafe100}" # crds.tar.gz
CLUSTERADM_VERSION="${CLUSTERADM_VERSION:-v1.4.0}"   # released 8 October 2026; its default bundle of OCM's components is 1.4.0
CLUSTERADM_SHA256="${CLUSTERADM_SHA256:-aa94241caf353a515a0778e0ce608b4c68ced9b3e7f6fb5fe23f48393926153b}"   # clusteradm_linux_amd64.tar.gz
OCM_BUNDLE="${OCM_BUNDLE:-1.4.0}"
ARMADA_VERSION="${ARMADA_VERSION:-0.22.14}"   # Armada's release v0.22.14; its images are tagged 0.22.14 and pinned here by digest
ARMADACTL_SHA256="${ARMADACTL_SHA256:-38fb81fe5b372400baa9c65096013fd44de0d1ab9e7178eb51f4c569bc40280e}"   # armadactl_0.22.14_linux_amd64.tar.gz
ARMADA_BUNDLE="gresearch/armada-bundle@sha256:f086b42e6d2b464e6ea44c4a2b04c909cbccfc85e784bd03d622db0fe39fd85d"           # gresearch/armada-bundle:0.22.14
ARMADA_LOOKOUT="gresearch/armada-lookout-bundle@sha256:e3861d0336c542bb2ad8da05dee6cb672705884d57d0d7b4a4107b19d0b58911"  # gresearch/armada-lookout-bundle:0.22.14
ARMADA_REDIS="redis@sha256:858f009f9709ce576febc734aa78b8f6d624b82571f9ddb6bda4377c833b3499"                   # redis:7.4-alpine, as Armada's local stack
ARMADA_POSTGRES="postgres@sha256:b0f9560a2de083e2cc7382e75f808c7381a32852a7ec49117deedb300e552b24"             # postgres:17-alpine, as Armada's local stack
ARMADA_PULSAR="apachepulsar/pulsar@sha256:188277e85d7287d6c4596ecc15f3c73a78beedb985db50d63dd130f6d393ec22"    # apachepulsar/pulsar:4.1.0, as Armada's local stack
JOBS="${BATCH_JOBS:-24}"; COMPLETIONS="${BATCH_COMPLETIONS:-10}"; PARALLELISM="${BATCH_PARALLELISM:-5}"
EVERY="${BATCH_EVERY_S:-30}"; MB="${BATCH_MB:-3000}"; DURATION="${DURATION:-1200}"
W="${RUNNER_TEMP:-/tmp}/omni-group-$(basename "$D")"   # Karmada's data and certificates, OCM's token, Armada's kubeconfigs: never in the run's files
KC="$W/data/karmada-apiserver.config"
HUB="$D/kubeconfig-host"                                   # the orchestrator's own cluster (removed with the run's kubeconfigs)
AR="$W/armada"                                             # Armada's configs and the members' kubeconfigs for its executors
ip_of() { docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' "$1"; }
fetch() {   # url, file, sha256
  local t got
  for t in 1 2 3; do curl -fsSL --retry 5 --retry-delay 3 "$1" -o "$2" && break; sleep 10; done
  got=$(sha256sum "$2" | cut -d' ' -f1)
  [ "$got" = "$3" ] || { echo "INVALID RUN: $1 is not the pinned file (sha256 $got, pinned $3)"; exit 1; }
}
ocm_place() {   # NAME: a Placement of its own for this job, in the namespace the default cluster set is bound to, with OCM's
  # default prioritizers (Steady and Balance, the latter spreading the decisions among the clusters); once OCM has decided,
  # the job as a ManifestWork in the chosen member's namespace on the hub, which its work agent applies there
  local name="$1" cluster="" t
  kubectl --kubeconfig "$HUB" apply -f - >/dev/null <<EOF
apiVersion: cluster.open-cluster-management.io/v1beta1
kind: Placement
metadata: {name: $name, namespace: default, labels: {app: omni-batch-stream}}
spec:
  numberOfClusters: 1
  clusterSets: [default]
EOF
  for t in $(seq 1 60); do
    cluster=$(kubectl --kubeconfig "$HUB" -n default get placementdecisions -l "cluster.open-cluster-management.io/placement=$name" -o json 2>/dev/null \
      | jq -r '[.items[].status.decisions[]?.clusterName] | first // empty')
    [ -n "$cluster" ] && break
    sleep 2
  done
  [ -n "$cluster" ] || { echo "$(date -u +%s) $name: no placement decision in 120 s" >> "$D/batch_submit.log"; return 1; }
  python3 - "$D/job.yaml" "$name" "$cluster" <<'PY' | kubectl --kubeconfig "$HUB" apply -f - >/dev/null
import sys, yaml
job = yaml.safe_load(open(sys.argv[1]))
print(yaml.safe_dump({"apiVersion": "work.open-cluster-management.io/v1", "kind": "ManifestWork",
                      "metadata": {"name": sys.argv[2], "namespace": sys.argv[3], "labels": {"app": "omni-batch-stream"}},
                      "spec": {"workload": {"manifests": [job]}}}, sort_keys=False))
PY
  echo "$cluster" > "$D/ocm_decision_$name"
}
armada_run() {   # name, then docker run's arguments: one of Armada's containers on the runner's own network (every service
  # at localhost, as Armada's local configs name them), on the cluster cores, as every member's nodes are
  local name="$1"; shift
  docker run -d --name "$name" --network host --cpuset-cpus "$cores" "$@" >/dev/null
}
armada_install() {   # Armada as its own local stack runs it (v0.22.14, _local/compose): redis, postgres and pulsar standalone,
  # the databases laid out, then its scheduler, scheduler ingester, server and event ingester from the pinned bundle; one
  # executor per member, reaching its member by the member's kubeconfig; Armada's two priority classes in every member;
  # one queue for the stream. Pulsar's web port is 8090, where Armada's local configs look for it; its heap is bounded so
  # the stack fits beside the clusters on one machine.
  local img i t
  mkdir -p "$AR"
  fetch "https://github.com/armadaproject/armada/releases/download/v${ARMADA_VERSION}/armadactl_${ARMADA_VERSION}_linux_amd64.tar.gz" \
    "$W/armadactl.tgz" "$ARMADACTL_SHA256"
  tar -xzf "$W/armadactl.tgz" -C "$W/bin" armadactl
  for img in "$ARMADA_BUNDLE" "$ARMADA_LOOKOUT" "$ARMADA_REDIS" "$ARMADA_POSTGRES" "$ARMADA_PULSAR"; do
    for t in 1 2 3; do docker pull -q "$img" >/dev/null 2>&1 && break; [ "$t" = 3 ] && { echo "INVALID RUN: $img could not be pulled"; exit 1; }; sleep 15; done
  done
  cp deploy/kind/armada/*.yaml "$AR/"
  armada_run armada-redis "$ARMADA_REDIS"
  armada_run armada-postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=psw -e POSTGRES_DB=postgres "$ARMADA_POSTGRES"
  armada_run armada-pulsar -e PULSAR_MEM="-Xms256m -Xmx1g -XX:MaxDirectMemorySize=512m" -e PULSAR_PREFIX_webServicePort=8090 \
    -e PULSAR_PREFIX_allowAutoTopicCreation=true -e PULSAR_PREFIX_allowAutoTopicCreationType=non-partitioned \
    -e PULSAR_PREFIX_autoSkipNonRecoverableData=true --entrypoint sh "$ARMADA_PULSAR" \
    -c "bin/apply-config-from-env.py conf/standalone.conf && bin/pulsar standalone"
  for t in $(seq 1 30); do docker exec armada-postgres pg_isready -U postgres >/dev/null 2>&1 && break; [ "$t" = 30 ] && { echo "INVALID RUN: Armada's postgres never answered"; exit 1; }; sleep 2; done
  docker exec armada-postgres psql -U postgres -q -c "CREATE DATABASE scheduler" -c "CREATE DATABASE lookout" >/dev/null
  for t in $(seq 1 90); do curl -fs http://localhost:8090/admin/v2/brokers/health >/dev/null 2>&1 && break; [ "$t" = 90 ] && { echo "INVALID RUN: Armada's pulsar never answered"; docker logs armada-pulsar 2>&1 | tail -20; exit 1; }; sleep 4; done
  docker run --rm --network host -v "$AR/scheduler.yaml:/config/config.yaml:ro" -w /app "$ARMADA_BUNDLE" ./scheduler migrateDatabase --config /config/config.yaml \
    > "$D/armada_migrate.log" 2>&1 || { tail -20 "$D/armada_migrate.log"; exit 1; }
  docker run --rm --network host -v "$AR/lookout.yaml:/config/config.yaml:ro" -w /app "$ARMADA_LOOKOUT" ./lookout --migrateDatabase --config /config/config.yaml \
    >> "$D/armada_migrate.log" 2>&1 || { tail -20 "$D/armada_migrate.log"; exit 1; }
  armada_run armada-scheduler -v "$AR/scheduler.yaml:/config/config.yaml:ro" -w /app "$ARMADA_BUNDLE" ./scheduler run --config /config/config.yaml
  armada_run armada-scheduleringester -v "$AR/scheduleringester.yaml:/config/config.yaml:ro" -w /app "$ARMADA_BUNDLE" ./scheduleringester --config /config/config.yaml
  armada_run armada-server -v "$AR/server.yaml:/config/config.yaml:ro" -w /app "$ARMADA_BUNDLE" ./server --config /config/config.yaml
  armada_run armada-eventingester -v "$AR/eventingester.yaml:/config/config.yaml:ro" -w /app "$ARMADA_BUNDLE" ./eventingester --config /config/config.yaml
  for i in $(seq 1 "$N"); do
    kubectl --kubeconfig "$D/kubeconfig-m$i" apply -f deploy/kind/armada/priorityclasses.yaml >/dev/null
    cp "$D/kubeconfig-m$i" "$AR/kubeconfig-m$i"
    armada_run "armada-executor-$i" -v "$AR/executor.yaml:/config/config.yaml:ro" -v "$AR/kubeconfig-m$i:/kube/config:ro" -w /app \
      -e KUBECONFIG=/kube/config -e "ARMADA_APPLICATION_CLUSTERID=omni-m$i" -e "ARMADA_HTTPPORT=$((8082 + i))" -e "ARMADA_METRIC_PORT=$((9010 + i))" \
      "$ARMADA_BUNDLE" ./executor --config /config/config.yaml
  done
  for t in $(seq 1 60); do "$W/bin/armadactl" --armadaUrl localhost:50051 get queues >/dev/null 2>&1 && break; [ "$t" = 60 ] && { echo "INVALID RUN: Armada's server never answered"; docker logs armada-server 2>&1 | tail -20; exit 1; }; sleep 5; done
  for t in 1 2 3; do "$W/bin/armadactl" --armadaUrl localhost:50051 create queue omni >> "$D/armada_queue.log" 2>&1 && break; [ "$t" = 3 ] && { tail -5 "$D/armada_queue.log"; exit 1; }; sleep 5; done
  sleep 15   # the scheduler reads its executors every second (deploy/kind/armada/scheduler.yaml); their first reports land
  {
    echo "orchestrator=armada $ARMADA_VERSION (its server, scheduler, ingesters and one executor per member as containers on the runner); armadactl sha256=$ARMADACTL_SHA256"
    echo "members: $(seq -s' ' -f 'omni-m%g' 1 "$N") (one executor each, pool default, Armada's two priority classes applied)"
    echo "placement: one queue (omni), one job set per batch of the stream, each pod a job Armada's scheduler places on a member of its choosing"
    echo "images, by the digest each was pulled by:"
    for c in armada-redis armada-postgres armada-pulsar armada-scheduler armada-server armada-executor-1; do echo "  $c $(docker inspect -f '{{.Config.Image}}' "$c")"; done
  } | tee "$D/orch.txt"
}
armada_submit() {   # NAME: the batch as one job set of Armada's queue, every pod of the batch one job (its requests equal to
  # its limits, as Armada requires: the pod's limit, one processor, stands for both), labelled as the stream's pods are
  local name="$1" t
  python3 - "$name" "$COMPLETIONS" "$MB" > "$AR/jobs-$name.yaml" <<'PY'
import copy, sys, yaml
name, n, mb = sys.argv[1], int(sys.argv[2]), sys.argv[3]
job = {"namespace": "default", "priority": 0,
       "labels": {"app": "omni-batch-stream", "job-name": name, "omni-stream": "1"},
       "podSpecs": [{"restartPolicy": "Never", "terminationGracePeriodSeconds": 30,
                     "containers": [{"name": "work", "image": "busybox:1.36", "imagePullPolicy": "IfNotPresent",
                                     "resources": {"requests": {"cpu": "1", "memory": "64Mi"}, "limits": {"cpu": "1", "memory": "64Mi"}},
                                     "command": ["/bin/sh", "-c", f"dd if=/dev/zero bs=1M count={mb} 2>/dev/null | sha256sum"]}]}]}
print(yaml.safe_dump({"queue": "omni", "jobSetId": name, "jobs": [copy.deepcopy(job) for _ in range(n)]}, sort_keys=False))
PY
  for t in 1 2 3 4 5 6; do "$W/bin/armadactl" --armadaUrl localhost:50051 submit "$AR/jobs-$name.yaml" >> "$D/armada_submit.log" 2>&1 && return 0; sleep 5; done
  return 1
}
armada_done() {   # batches whose COMPLETIONS pods have succeeded, summed over the members (Armada's pods carry the batch's name)
  local i
  for i in $(seq 1 "$N"); do kubectl --kubeconfig "$D/kubeconfig-m$i" get pods -l app=omni-batch-stream -o json --request-timeout=20s 2>/dev/null \
    | jq -r '.items[] | select(.status.phase == "Succeeded") | .metadata.labels["job-name"]' || true; done \
    | sort | uniq -c | awk -v n="$COMPLETIONS" '$1 >= n {c++} END {print c+0}'
}
armada_end() {   # Armada's record: every batch as sent (its job set, the moment it was submitted), done when its pods are;
  # where its pods ran; the scheduler's and the server's last words; then its containers removed
  local c i
  python3 - "$D" "$N" "$COMPLETIONS" <<'PY'
import datetime as dt, json, subprocess, sys
from pathlib import Path
d, n, need = Path(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
def iso(t): return dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
sent = {}
for ln in (d / "batch_submit.log").read_text().splitlines() if (d / "batch_submit.log").exists() else []:
    parts = ln.split()
    if len(parts) >= 3 and parts[1] == "submitted":
        sent[parts[2]] = float(parts[0])
pods = []
for i in range(1, n + 1):
    kc = d / f"kubeconfig-m{i}"
    if not kc.exists():
        continue
    r = subprocess.run(["kubectl", "--kubeconfig", str(kc), "get", "pods", "-l", "app=omni-batch-stream", "-o", "json"], capture_output=True, text=True)
    try:
        for p in json.loads(r.stdout).get("items", []):
            p["_member"] = f"omni-m{i}"; pods.append(p)
    except ValueError:
        pass
jobs, where = [], []
for name, t0 in sorted(sent.items()):
    mine = [p for p in pods if (p["metadata"].get("labels") or {}).get("job-name") == name]
    ok = [p for p in mine if (p.get("status") or {}).get("phase") == "Succeeded"]
    j = {"metadata": {"name": name, "creationTimestamp": iso(t0)}, "status": {"pods": len(mine), "succeeded": len(ok)}}
    ends = [((s.get("state") or {}).get("terminated") or {}).get("finishedAt") for p in ok for s in (p.get("status") or {}).get("containerStatuses", [])]
    if len(ok) >= need and ends and all(ends):
        j["status"]["completionTime"] = max(ends)
    jobs.append(j)
    counts = {}
    for p in mine:
        counts[p["_member"]] = counts.get(p["_member"], 0) + 1
    where.append({"job": name, "clusters": [{"name": k, "pods": v} for k, v in sorted(counts.items())]})
(d / "orch_jobs.json").write_text(json.dumps({"items": jobs}, indent=1) + "\n")
(d / "orch_end.json").write_text(json.dumps(where, indent=1) + "\n")
PY
  for c in armada-scheduler armada-server; do docker logs --tail 200 "$c" > "$D/$c.log" 2>&1 || true; done
  docker rm -f armada-redis armada-postgres armada-pulsar armada-scheduler armada-scheduleringester armada-server armada-eventingester >/dev/null 2>&1 || true
  for i in $(seq 1 "$N"); do docker rm -f "armada-executor-$i" >/dev/null 2>&1 || true; done
}
case "${PHASE:?set PHASE=install, submit or end}" in
install)
  case "$ORCH" in karmada|ocm|armada) ;; *) echo "nothing to install for $ORCH"; exit 0 ;; esac
  rm -rf "$W"; mkdir -p "$W/bin"
  ncpu=$(nproc); cores="0-$((ncpu - 2))"; [ "$ncpu" -ge 2 ] || cores=0   # the cluster cores; the governor's core stays its own
  if [ "$ORCH" = armada ]; then armada_install; exit 0; fi
  # the orchestrator's cluster on the cluster cores, as every member's nodes are; the governor's core stays its own
  [ "$ncpu" -lt 2 ] || docker update --cpuset-cpus "$cores" omni-host-control-plane >/dev/null
  host_ip=$(ip_of omni-host-control-plane)
  if [ "$ORCH" = ocm ]; then
    fetch "https://github.com/open-cluster-management-io/clusteradm/releases/download/${CLUSTERADM_VERSION}/clusteradm_linux_amd64.tar.gz" \
      "$W/clusteradm.tgz" "$CLUSTERADM_SHA256"
    tar -xzf "$W/clusteradm.tgz" -C "$W/bin" clusteradm
    # the hub (cluster manager) as clusteradm installs it, the components of the pinned bundle; the join command it hands
    # out holds the bootstrap token, kept outside the run's files
    "$W/bin/clusteradm" init --kubeconfig "$HUB" --bundle-version "$OCM_BUNDLE" --wait --output-join-command-file "$W/join.sh" \
      > "$D/ocm_init.log" 2>&1 || { tail -40 "$D/ocm_init.log"; exit 1; }
    token=$(grep -o -- '--hub-token [^ ]*' "$W/join.sh" | head -1 | cut -d' ' -f2 || true)
    [ -n "$token" ] || token=$("$W/bin/clusteradm" get token --kubeconfig "$HUB" 2>/dev/null | grep -o -- '--hub-token [^ ]*' | head -1 | cut -d' ' -f2 || true)
    [ -n "$token" ] || { echo "INVALID RUN: the hub handed out no bootstrap token"; exit 1; }
    # every member registered by clusteradm join (its klusterlet in its own namespaces, as OCM places it) by the address its
    # agents reach the hub at, then accepted on the hub; the arm waits until every member is Available
    for i in $(seq 1 "$N"); do
      for t in 1 2 3; do
        "$W/bin/clusteradm" join --kubeconfig "$D/kubeconfig-m$i" --hub-token "$token" --hub-apiserver "https://$host_ip:6443" \
          --cluster-name "omni-m$i" --bundle-version "$OCM_BUNDLE" --force-internal-endpoint-lookup --wait >> "$D/ocm_join.log" 2>&1 && break
        [ "$t" = 3 ] && { tail -20 "$D/ocm_join.log"; exit 1; }; sleep 10
      done
    done
    members=$(seq -s, -f 'omni-m%g' 1 "$N")
    for t in 1 2 3; do
      "$W/bin/clusteradm" accept --kubeconfig "$HUB" --clusters "$members" --wait >> "$D/ocm_accept.log" 2>&1 && break
      [ "$t" = 3 ] && { tail -20 "$D/ocm_accept.log"; exit 1; }; sleep 10
    done
    for t in $(seq 1 60); do
      ready=$(kubectl --kubeconfig "$HUB" get managedclusters -o json | jq '[.items[] | select(any(.status.conditions[]?; .type == "ManagedClusterConditionAvailable" and .status == "True"))] | length')
      [ "$ready" = "$N" ] && break
      [ "$t" = 60 ] && { echo "INVALID RUN: $ready of $N members Available in OCM"; kubectl --kubeconfig "$HUB" get managedclusters; exit 1; }
      sleep 5
    done
    # the default cluster set (every joined cluster is in it) bound to the namespace the placements live in
    kubectl --kubeconfig "$HUB" apply -f - >/dev/null <<EOF
apiVersion: cluster.open-cluster-management.io/v1beta2
kind: ManagedClusterSetBinding
metadata: {name: default, namespace: default}
spec: {clusterSet: default}
EOF
    {
      echo "orchestrator=ocm (Open Cluster Management) bundle $OCM_BUNDLE; clusteradm $CLUSTERADM_VERSION sha256=$CLUSTERADM_SHA256"
      echo "members: $(kubectl --kubeconfig "$HUB" get managedclusters -o jsonpath='{range .items[*]}{.metadata.name} {end}')"
      echo "placement: one Placement per job (numberOfClusters 1, cluster set default, OCM's default prioritizers Steady and Balance), the job as a ManifestWork in the member it decides"
      echo "images, with the digest each resolved to (the hub, then member omni-m1's agents):"
      kubectl --kubeconfig "$HUB" get pods -A -o json | jq -r '[.items[].status.containerStatuses[]? | "  \(.image) \(.imageID)"] | unique[]'
      kubectl --kubeconfig "$D/kubeconfig-m1" get pods -A -o json | jq -r '[.items[] | select(.metadata.namespace | startswith("open-cluster-management")) | .status.containerStatuses[]? | "  \(.image) \(.imageID)"] | unique[]'
    } | tee "$D/orch.txt"
    rm -f "$W/join.sh"
    exit 0
  fi
  rel="https://github.com/karmada-io/karmada/releases/download/${KARMADA_VERSION}"
  fetch "$rel/karmadactl-linux-amd64.tgz" "$W/karmadactl.tgz" "$KARMADACTL_SHA256"
  fetch "$rel/crds.tar.gz" "$W/crds.tar.gz" "$KARMADA_CRDS_SHA256"
  tar -xzf "$W/karmadactl.tgz" -C "$W/bin" karmadactl
  "$W/bin/karmadactl" init --kubeconfig "$D/kubeconfig-host" --karmada-data "$W/data" --karmada-pki "$W/pki" \
    --crds "$W/crds.tar.gz" --karmada-apiserver-advertise-address "$host_ip" --wait-component-ready-timeout 600 \
    > "$D/karmada_init.log" 2>&1 || { tail -40 "$D/karmada_init.log"; exit 1; }
  # every member joined in push mode by the address the orchestrator's pods reach it at (its control plane on the runner's
  # container network)
  for i in $(seq 1 "$N"); do
    ip=$(ip_of "omni-m$i-control-plane")
    kind get kubeconfig --internal --name "omni-m$i" | sed "s#https://omni-m$i-control-plane:6443#https://$ip:6443#" > "$W/m$i.kubeconfig"
    for t in 1 2 3; do
      "$W/bin/karmadactl" join "omni-m$i" --kubeconfig "$KC" --cluster-kubeconfig "$W/m$i.kubeconfig" >> "$D/karmada_join.log" 2>&1 && break
      [ "$t" = 3 ] && { tail -20 "$D/karmada_join.log"; exit 1; }; sleep 10
    done
  done
  for t in $(seq 1 60); do
    ready=$(kubectl --kubeconfig "$KC" get clusters -o json | jq '[.items[] | select(any(.status.conditions[]?; .type == "Ready" and .status == "True"))] | length')
    [ "$ready" = "$N" ] && break
    [ "$t" = 60 ] && { echo "INVALID RUN: $ready of $N members Ready in Karmada"; kubectl --kubeconfig "$KC" get clusters -o wide; exit 1; }
    sleep 5
  done
  members=$(seq -s, -f 'omni-m%g' 1 "$N")
  sed "s/MEMBER_CLUSTERS/[${members}]/" deploy/kind/karmada-propagation.yaml | kubectl --kubeconfig "$KC" apply -f - > /dev/null
  {
    echo "orchestrator=karmada $KARMADA_VERSION; karmadactl sha256=$KARMADACTL_SHA256; crds.tar.gz sha256=$KARMADA_CRDS_SHA256"
    echo "members: $(kubectl --kubeconfig "$KC" get clusters -o jsonpath='{range .items[*]}{.metadata.name} {end}')"
    echo "propagation policy: $(kubectl --kubeconfig "$KC" get propagationpolicy omni-batch-stream -o json | jq -c '.spec.placement')"
    echo "images, with the digest each resolved to:"
    kubectl --kubeconfig "$D/kubeconfig-host" get pods -A -o json | jq -r '[.items[].status.containerStatuses[]? | "  \(.image) \(.imageID)"] | unique[]'
  } | tee "$D/orch.txt"
  ;;
submit)
  for t in $(seq 1 480); do [ "$(find "$D/barrier" -name 'ready-*' | wc -l)" -ge "$N" ] && break; sleep 5; done
  [ "$(find "$D/barrier" -name 'ready-*' | wc -l)" -ge "$N" ] || { echo "the members' windows never opened"; exit 1; }
  START=$(date -u +%s); echo "$START" > "$D/stream_start.txt"
  for i in $(seq 1 "$JOBS"); do
    name="omni-batch-$(printf %03d "$i")"
    sed -e "s/JOB_NAME/$name/" -e "s/BATCH_COMPLETIONS/${COMPLETIONS}/" -e "s/BATCH_PARALLELISM/${PARALLELISM}/" \
        -e "s/BATCH_MB/${MB}/" -e 's|POD_QUEUE_LABEL|omni-stream: "1"|' -e 's|QUEUE_LABEL|omni-stream: "1"|' \
        -e "s|SCHEDULER_LINE|terminationGracePeriodSeconds: 30|" deploy/kind/batch-stream-job.yaml > "$D/job.yaml"
    if [ "$ORCH" = ocm ]; then
      where="ocm, placed in a member of its choosing"
      ocm_place "$name" || ocm_place "$name" || echo "$(date -u +%s) $name was not placed by OCM" >> "$D/batch_submit.log"
      [ ! -s "$D/ocm_decision_$name" ] || where="ocm, placed in $(cat "$D/ocm_decision_$name")"
    elif [ "$ORCH" = armada ]; then
      where="armada, its queue omni (a job set of $COMPLETIONS jobs)"
      armada_submit "$name" || echo "$(date -u +%s) $name was not accepted by Armada" >> "$D/batch_submit.log"
    else
      if [ "$ORCH" = none ]; then to="$D/kubeconfig-m$(( (i - 1) % N + 1 ))"; where="member $(( (i - 1) % N + 1 ))"; else to="$KC"; where="$ORCH"; fi
      for t in 1 2 3 4 5 6; do kubectl --kubeconfig "$to" apply -f "$D/job.yaml" --request-timeout=20s >/dev/null && break; sleep 5; done
    fi
    echo "$(date -u +%s) submitted $name to $where" >> "$D/batch_submit.log"
    [ "$i" = "$JOBS" ] || sleep "$EVERY"
  done
  done_jobs() {   # jobs that have succeeded: as Karmada reports them; Armada's by its pods in the members; or summed over the
    # members (the group alone; OCM, whose work agents run the jobs in the members)
    if [ "$ORCH" = karmada ]; then
      kubectl --kubeconfig "$KC" get jobs -l app=omni-batch-stream -o json --request-timeout=20s 2>/dev/null \
        | jq '[.items[] | select(any(.status.conditions[]?; .type == "Complete" and .status == "True"))] | length' || echo 0
    elif [ "$ORCH" = armada ]; then
      armada_done
    else
      for i in $(seq 1 "$N"); do kubectl --kubeconfig "$D/kubeconfig-m$i" get jobs -l app=omni-batch-stream -o json --request-timeout=20s 2>/dev/null \
        | jq '[.items[] | select((.status.succeeded // 0) >= .spec.completions)] | length' || echo 0; done | awk '{s+=$1} END {print s+0}'
    fi
  }
  until [ "$(done_jobs)" = "$JOBS" ]; do
    [ "$(date -u +%s)" -lt "$(( START + DURATION ))" ] || exit 0   # not done in the window: no time written, the window's end counts
    sleep 5
  done
  date -u +%s > "$D/batch_done.txt"
  ;;
end)
  if [ "$ORCH" = karmada ] && [ -s "$KC" ]; then
    kubectl --kubeconfig "$KC" get jobs -l app=omni-batch-stream -o json > "$D/orch_jobs.json" 2>/dev/null || echo '{"items": []}' > "$D/orch_jobs.json"
    kubectl --kubeconfig "$KC" get resourcebindings -A -o json 2>/dev/null \
      | jq '[.items[] | select(.spec.resource.kind == "Job") | {job: .spec.resource.name, clusters: .spec.clusters}]' > "$D/orch_end.json" || true
    for dep in karmada-scheduler karmada-controller-manager; do
      kubectl --kubeconfig "$D/kubeconfig-host" -n karmada-system logs "deployment/$dep" --tail=200 > "$D/$dep.log" 2>&1 || true
    done
  elif [ "$ORCH" = ocm ] && [ -s "$HUB" ]; then
    # every ManifestWork (the job as it was sent to OCM, named as the job) and every placement decision
    kubectl --kubeconfig "$HUB" get manifestworks -A -l app=omni-batch-stream -o json > "$D/orch_jobs.json" 2>/dev/null || echo '{"items": []}' > "$D/orch_jobs.json"
    kubectl --kubeconfig "$HUB" -n default get placementdecisions -o json 2>/dev/null \
      | jq '[.items[] | {job: .metadata.labels["cluster.open-cluster-management.io/placement"], clusters: [.status.decisions[]?.clusterName]}]' > "$D/orch_end.json" || true
    for dep in cluster-manager-placement-controller cluster-manager-registration-controller cluster-manager-work-webhook; do
      kubectl --kubeconfig "$HUB" -n open-cluster-management-hub logs "deployment/$dep" --tail=200 > "$D/$dep.log" 2>&1 || true
    done
    rm -f "$D"/ocm_decision_*
  elif [ "$ORCH" = armada ]; then
    armada_end
  fi
  rm -rf "$W"
  ;;
*) echo "PHASE must be install, submit or end"; exit 1 ;;
esac
# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
