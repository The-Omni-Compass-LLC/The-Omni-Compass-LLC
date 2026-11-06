#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# One paired repetition on a real, billed Google Kubernetes Engine cluster (.github/workflows/gke-metered.yml): every
# arm back to back, each on a fresh cluster built the same way, in an order rotated by repetition, the same design as
# scripts/aks_paired.sh on Azure and scripts/kind_paired.sh on kind. Each cluster:
#   system pool  1 machine, tainted CriticalAddonsOnly=true:NoSchedule (GKE's add-ons, which tolerate that taint, and the
#                load generator; never measured, never governed)
#   work pool    omni-role=work, agentpool=work0, starts at GKE_MAX_NODES machines, under Google's own cluster
#                autoscaler (min 1, max GKE_MAX_NODES, the optimize-utilization profile), which deletes a machine once
#                it is empty. Native: the autoscaler alone. Omni on top: the same autoscaler, with Omni-Compass idling the
#                machines it gives back, which the autoscaler then deletes
# The measuring is scripts/kind_bench.sh in its managed-cluster mode (PLATFORM=gke reads as the same cloud-neutral mode
# AKS uses: kubectl only, the probe through the cloud's load balancer, the load generator on the tainted system machine,
# the bill counted from every work machine that exists every 15 s by its agentpool label). Each cluster is deleted
# when its arm ends, before the next is made, so nothing keeps billing.
# Written to the same design as the AKS run and not yet run on Google Cloud: its first repetition is a shakedown, and
# any arm that fails its own checks is marked INVALID and never counted.
# Usage: REP=n ARMS="native compass" GCP_PROJECT=... [GCP_ZONE=us-central1-a GKE_MACHINE=e2-standard-2
#        GKE_MAX_NODES=4 RUN_ID=...] bash scripts/gke_paired.sh
set -euo pipefail
echo "Omni-Compass: evaluation and Simulation use only. Commercial use requires a signed, paid Omni-Compass Enterprise License (LICENSE, NOTICE)."
REP="${REP:?set REP}"; read -r -a arms <<< "${ARMS:-native compass}"
PROJECT="${GCP_PROJECT:?set GCP_PROJECT}"; ZONE="${GCP_ZONE:-us-central1-a}"; MACHINE="${GKE_MACHINE:-e2-standard-2}"
MAX="${GKE_MAX_NODES:-4}"; RUNID="${RUN_ID:-local}"
export AKS_MAX_NODES="$MAX" WORKER_SEL="omni-role=work"          # kind_bench.sh's managed-cluster mode reads these names
k=${#arms[@]}; off=$(( (REP - 1) % k ))
order=( "${arms[@]:off}" "${arms[@]:0:off}" )
echo "repetition $REP, order: ${order[*]}, work pool $MACHINE x up to $MAX in $ZONE (project $PROJECT)"
# Pre-flight, before anything is built or billed: the machine type is offered in the zone, and Google's quotas have room
# for the system machine and the whole work pool: the region's processors (CPUS), the project's processors in every region
# (CPUS_ALL_REGIONS: Google's free trial holds it at 8, so the account's full activation comes first), the region's
# solid-state disk (SSD_TOTAL_GB: each machine's boot disk is GKE's default, 100 GB balanced) and its external addresses
# (IN_USE_ADDRESSES: one a machine and one for the load balancer). One refusal ends the repetition here, in a minute, with
# Google's own words or every short quota named. PREFLIGHT_ONLY=1 (.github/workflows/cloud-check.yml) stops after it.
region="${ZONE%-*}"
cpus=$(gcloud compute machine-types describe "$MACHINE" --zone "$ZONE" --project "$PROJECT" --format='value(guestCpus)' 2>/tmp/gke-preflight.err || true)
if [ -z "$cpus" ]; then
  why=$(tr '\n' ' ' < /tmp/gke-preflight.err | cut -c1-400)     # Google's words: a refusal is never read as "not offered"
  echo "pre-flight: Google gave no $MACHINE in $ZONE${why:+ (Google said: $why)}: nothing built, nothing billed"; exit 2
fi
gcloud compute regions describe "$region" --project "$PROJECT" --format=json > /tmp/gke-region.json 2>/tmp/gke-preflight.err \
  && gcloud compute project-info describe --project "$PROJECT" --format=json > /tmp/gke-project.json 2>>/tmp/gke-preflight.err \
  || { echo "pre-flight: Google's quotas could not be read (Google said: $(tr '\n' ' ' < /tmp/gke-preflight.err | cut -c1-400)): nothing built, nothing billed"; exit 2; }
MACHINES=$(( MAX + 1 )) CPUS_EACH="$cpus" DISK_GB="${GKE_DISK_GB:-100}" REGION="$region" python3 - <<'PY_QUOTA' || exit 2
import json, os
m, c, d, region = int(os.environ["MACHINES"]), int(os.environ["CPUS_EACH"]), int(os.environ["DISK_GB"]), os.environ["REGION"]
quotas = {("region", q["metric"]): q for q in json.load(open("/tmp/gke-region.json")).get("quotas", [])}
quotas.update({("project", q["metric"]): q for q in json.load(open("/tmp/gke-project.json")).get("quotas", [])})
needs = ((("region", "CPUS"), m * c, f"processors in {region}"), (("project", "CPUS_ALL_REGIONS"), m * c, "processors in all regions"),
         (("region", "SSD_TOTAL_GB"), m * d, f"GB of solid-state disk in {region}"),
         (("region", "IN_USE_ADDRESSES"), m + 1, f"external addresses in {region}"))
short = []
for key, need, what in needs:
    q = quotas.get(key)
    if q is None:
        print(f"pre-flight: {key[1]} not reported by Google; Google's own check decides it")
        continue
    free = int(q["limit"] - q["usage"])
    print(f"pre-flight: {key[1]}: needs {need} {what}, {free} free of {int(q['limit'])}: {'ok' if free >= need else 'SHORT'}")
    if free < need:
        short.append(f"{key[1]} needs {need}, {free} free of {int(q['limit'])}")
if short:
    hint = (" Google's free trial allows 8 processors at once: activate the full account (the credit stays and pays first)."
            if quotas.get(("project", "CPUS_ALL_REGIONS"), {}).get("limit") == 8 else "")
    print("pre-flight: short of Google's quota: " + "; ".join(short) + ". Nothing built, nothing billed. Raise it with Google "
          "(docs/GOOGLE_SETUP.md, section 6), never shrink the set." + hint)
    raise SystemExit(2)
PY_QUOTA
echo "pre-flight: $MACHINE ($cpus vCPU) x $(( MAX + 1 )) in $ZONE: ok"
if [ "${PREFLIGHT_ONLY:-0}" = 1 ]; then echo "pre-flight only: nothing built, nothing billed"; exit 0; fi
gone() { gcloud container clusters delete "$1" --zone "$ZONE" --project "$PROJECT" --quiet >/dev/null 2>&1 || true; }
for arm in "${order[@]}"; do
  name=$(echo "omni-$arm-$REP-$RUNID" | tr '[:upper:]_' '[:lower:]-' | cut -c1-40)     # GKE: lowercase, at most 40 characters
  gone "$name"
  echo "######## creating $name"
  gcloud container clusters create "$name" --zone "$ZONE" --project "$PROJECT" \
    --num-nodes 1 --machine-type "$MACHINE" --node-taints CriticalAddonsOnly=true:NoSchedule --node-labels omni-role=system \
    --autoscaling-profile optimize-utilization --release-channel regular --quiet
  gcloud container node-pools create work0 --cluster "$name" --zone "$ZONE" --project "$PROJECT" \
    --machine-type "$MACHINE" --num-nodes "$MAX" --enable-autoscaling --min-nodes 1 --max-nodes "$MAX" \
    --node-labels omni-role=work,agentpool=work0 --quiet
  gcloud container clusters get-credentials "$name" --zone "$ZONE" --project "$PROJECT"
  # 24 October: in 3 of the steady set's first 9 repetitions the work machines did not read Ready within 600 s and the
  # repetition ended before any measurement. The nodes' own conditions and the pools' states are kept in the repetition's
  # files whenever the wait runs out, so the cause is read from the run, and the wait is given once more before it fails
  if ! kubectl wait --for=condition=Ready nodes --all --timeout=900s; then
    mkdir -p "bench-$arm-$REP"
    kubectl get nodes -o wide > "bench-$arm-$REP/nodes_not_ready.txt" 2>&1 || true
    kubectl describe nodes > "bench-$arm-$REP/nodes_describe.txt" 2>&1 || true
    kubectl get events -A --sort-by=.lastTimestamp > "bench-$arm-$REP/events.txt" 2>&1 || true
    : # the node pools' states are in the cluster's own events above
    echo "######## $name: a node not Ready after 900 s (its conditions kept in bench-$arm-$REP); one more wait of 600 s"
    kubectl wait --for=condition=Ready nodes --all --timeout=600s
  fi
  gcloud container clusters describe "$name" --zone "$ZONE" --project "$PROJECT" --format=json > "/tmp/gke-$name.json"
  echo "######## ARM $arm (repetition $REP)"
  mkdir -p "bench-$arm-$REP"; cp "/tmp/gke-$name.json" "bench-$arm-$REP/gke_cluster.json"
  if ! PLATFORM=gke ARM="$arm" OUT_DIR="bench-$arm-$REP" bash scripts/kind_bench.sh; then
    echo "ARM $arm (repetition $REP) FAILED its checks: marked invalid" | tee "bench-$arm-$REP/INVALID"; fail=1
  fi
  gone "$name"
done
exit "${fail:-0}"
