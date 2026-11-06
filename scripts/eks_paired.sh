#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# One paired repetition on a real, billed Amazon Elastic Kubernetes Service cluster (.github/workflows/eks-metered.yml):
# every arm back to back, each on a fresh cluster built the same way, in an order rotated by repetition, the same design
# as scripts/aks_paired.sh on Azure and scripts/gke_paired.sh on Google Cloud. Each cluster (eksctl, managed node groups):
#   system group 1 machine, tainted CriticalAddonsOnly=true:NoSchedule (EKS's add-ons, the Kubernetes cluster
#                autoscaler, metrics-server and the load generator; never measured, never governed)
#   work group   omni-role=work, agentpool=work0, starts at EKS_MAX_NODES machines, under the Kubernetes cluster
#                autoscaler (EKS has none built in: the upstream one is installed with the same scale-down profile the
#                AKS run uses: 2 minutes unneeded, 2 minutes after an add, a scan every 10 s), which removes a machine
#                once it is empty. Native: the autoscaler alone. Omni on top: the same autoscaler, with Omni-Compass idling
#                the machines it gives back, which the autoscaler then removes
# The measuring is scripts/kind_bench.sh in its managed-cluster mode (PLATFORM=eks: kubectl only; Amazon's load balancer
# answers with a host name, which that mode reads when no address is given). Each cluster is deleted when its arm ends.
# Written to the same design as the AKS run and not yet run on Amazon: its first repetition is a shakedown, and any arm
# that fails its own checks is marked INVALID and never counted.
# Usage: REP=n ARMS="native compass" [AWS_REGION=us-east-1 EKS_INSTANCE=m5.large EKS_MAX_NODES=4 RUN_ID=...]
#        bash scripts/eks_paired.sh            (credentials from the environment: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
set -euo pipefail
echo "Omni-Compass: evaluation and Simulation use only. Commercial use requires a signed, paid Omni-Compass Enterprise License (LICENSE, NOTICE)."
REP="${REP:?set REP}"; read -r -a arms <<< "${ARMS:-native compass}"
REGION="${AWS_REGION:-us-east-1}"; TYPE="${EKS_INSTANCE:-m5.large}"; MAX="${EKS_MAX_NODES:-4}"; RUNID="${RUN_ID:-local}"
K8S="${EKS_VERSION:-}"; MS_VERSION="${METRICS_SERVER_EKS:-v0.7.2}"   # EKS_VERSION empty: eksctl's default, a supported version
export AKS_MAX_NODES="$MAX" WORKER_SEL="omni-role=work"          # kind_bench.sh's managed-cluster mode reads these names
k=${#arms[@]}; off=$(( (REP - 1) % k ))
order=( "${arms[@]:off}" "${arms[@]:0:off}" )
echo "repetition $REP, order: ${order[*]}, work group $TYPE x up to $MAX in $REGION"
# Pre-flight, before anything is built or billed: the keys log in, the instance type is offered in the region, and the
# on-demand vCPU quota for standard instances (L-1216C47A) has room for the system machine and the whole work group.
# PREFLIGHT_ONLY=1 (.github/workflows/cloud-check.yml) stops after it; QUOTA_REQUEST=1 files the quota increase with
# Amazon when the quota is short (the founder's order of 18 October: a quota is raised with the cloud, never shrunk to fit).
# Amazon's own words for a run's public page: the account, organization and policy numbers it quotes are masked
aws_words() { tr '\n' ' ' < /tmp/eks-preflight.err | sed -E 's/[0-9]{12}/<account>/g; s/o-[a-z0-9]{10,32}/<organization>/g; s/p-[a-z0-9]{8,128}/<policy>/g' | cut -c1-400; }
aws sts get-caller-identity --query Arn --output text >/dev/null 2>/tmp/eks-preflight.err \
  || { echo "pre-flight: Amazon refused the keys (AWS said: $(aws_words)): nothing built, nothing billed"; exit 2; }
vcpu=$(aws ec2 describe-instance-types --region "$REGION" --instance-types "$TYPE" \
  --query 'InstanceTypes[0].VCpuInfo.DefaultVCpus' --output text 2>/tmp/eks-preflight.err || true)
case "$vcpu" in ''|None)
  # Amazon's own words, so a refusal (a new account not yet verified, a region not enabled, a missing permission) is
  # never read as "not offered"; the keys are never printed, only the error AWS returns
  why=$(aws_words)
  if grep -q "explicit deny in a service control policy" /tmp/eks-preflight.err; then
    # the limit Amazon puts on an account on its Free plan (18 October): every machine read is denied above the keys
    echo "pre-flight: the AWS account is on Amazon's Free plan, which denies every machine read; upgrade it to the Paid plan" \
         "(docs/AMAZON_SETUP.md, section 1a; the credits still pay first). Nothing built, nothing billed. (AWS said: $why)"; exit 2
  fi
  echo "pre-flight: AWS gave no $TYPE in $REGION${why:+ (AWS said: $why)}: nothing built, nothing billed"; exit 2;; esac
quota=$(aws service-quotas get-service-quota --region "$REGION" --service-code ec2 --quota-code L-1216C47A \
  --query 'Quota.Value' --output text 2>/dev/null | cut -d. -f1 || true)     # unread: Amazon's own check decides it
need=$(( (MAX + 1) * vcpu ))
if [ -n "$quota" ] && [ "$quota" != None ] && [ "$quota" -lt "$need" ]; then
  asked=""
  if [ "${QUOTA_REQUEST:-0}" = 1 ]; then
    open=$(aws service-quotas list-requested-service-quota-change-history-by-quota --region "$REGION" --service-code ec2 \
      --quota-code L-1216C47A --query "length(RequestedQuotas[?Status=='PENDING' || Status=='CASE_OPENED'])" --output text 2>/dev/null || echo 0)
    if [ "${open:-0}" != 0 ] && [ "${open:-0}" != None ]; then
      asked="; an increase is already asked of Amazon and waits for its answer"
    elif aws service-quotas request-service-quota-increase --region "$REGION" --service-code ec2 --quota-code L-1216C47A \
         --desired-value "$need" >/dev/null 2>/tmp/eks-quota.err; then
      asked="; an increase to $need was asked of Amazon now (it usually answers within a day)"
    else
      asked="; the increase could not be asked ($(tr '\n' ' ' < /tmp/eks-quota.err | cut -c1-300)): docs/AMAZON_SETUP.md, section 4"
    fi
  fi
  echo "pre-flight: needs $need on-demand vCPUs in $REGION, quota $quota$asked: nothing built, nothing billed"; exit 2
fi
echo "pre-flight: $TYPE ($vcpu vCPU) x $(( MAX + 1 )) needs $need vCPUs, quota ${quota:-unknown}: ok"
if [ "${PREFLIGHT_ONLY:-0}" = 1 ]; then echo "pre-flight only: nothing built, nothing billed"; exit 0; fi
gone() { eksctl delete cluster --name "$1" --region "$REGION" --wait >/dev/null 2>&1 || true; }
for arm in "${order[@]}"; do
  name=$(echo "omni-$arm-$REP-$RUNID" | tr '[:upper:]_' '[:lower:]-' | cut -c1-60)
  gone "$name"
  echo "######## creating $name"
  cat > "/tmp/eks-$name.yaml" <<YAML
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig
metadata: {name: $name, region: $REGION${K8S:+, version: "$K8S"}}
iam:
  withOIDC: true
  serviceAccounts:
    - metadata: {name: cluster-autoscaler, namespace: kube-system}
      wellKnownPolicies: {autoScaler: true}
managedNodeGroups:
  - name: system
    instanceType: $TYPE
    desiredCapacity: 1
    minSize: 1
    maxSize: 1
    labels: {omni-role: system}
    taints: [{key: CriticalAddonsOnly, value: "true", effect: NoSchedule}]
  - name: work0
    instanceType: $TYPE
    desiredCapacity: $MAX
    minSize: 1
    maxSize: $MAX
    labels: {omni-role: work, agentpool: work0}
    tags: {"k8s.io/cluster-autoscaler/enabled": "true", "k8s.io/cluster-autoscaler/$name": "owned"}
YAML
  eksctl create cluster -f "/tmp/eks-$name.yaml"
  aws eks update-kubeconfig --name "$name" --region "$REGION"
  # 24 October: in 3 of the steady set's first 9 repetitions the work machines did not read Ready within 600 s and the
  # repetition ended before any measurement. The nodes' own conditions and the pools' states are kept in the repetition's
  # files whenever the wait runs out, so the cause is read from the run, and the wait is given once more before it fails
  if ! kubectl wait --for=condition=Ready nodes --all --timeout=900s; then
    mkdir -p "bench-$arm-$REP"
    kubectl get nodes -o wide > "bench-$arm-$REP/nodes_not_ready.txt" 2>&1 || true
    kubectl describe nodes > "bench-$arm-$REP/nodes_describe.txt" 2>&1 || true
    kubectl get events -A --sort-by=.lastTimestamp > "bench-$arm-$REP/events.txt" 2>&1 || true
    : # the node groups' states are in the cluster's own events above
    echo "######## $name: a node not Ready after 900 s (its conditions kept in bench-$arm-$REP); one more wait of 600 s"
    kubectl wait --for=condition=Ready nodes --all --timeout=600s
  fi
  # the Kubernetes cluster autoscaler (EKS ships none): auto-discovery by the work group's tags, AKS's scale-down profile,
  # on the system machine (it tolerates the taint)
  helm repo add autoscaler https://kubernetes.github.io/autoscaler >/dev/null 2>&1 || true
  helm repo update >/dev/null
  # the autoscaler release that matches the cluster's own Kubernetes minor version (one release per minor)
  minor=$(kubectl version -o json | python3 -c "import json,sys; print(json.load(sys.stdin)['serverVersion']['minor'].rstrip('+'))")
  helm upgrade --install cluster-autoscaler autoscaler/cluster-autoscaler ${CA_CHART_VERSION:+--version "$CA_CHART_VERSION"} -n kube-system \
    --set image.tag="v1.${minor}.0" \
    --set autoDiscovery.clusterName="$name" --set awsRegion="$REGION" \
    --set rbac.serviceAccount.create=false --set rbac.serviceAccount.name=cluster-autoscaler \
    --set extraArgs.scale-down-unneeded-time=2m --set extraArgs.scale-down-delay-after-add=2m --set extraArgs.scan-interval=10s \
    --set "tolerations[0].key=CriticalAddonsOnly" --set "tolerations[0].operator=Exists" \
    --set "nodeSelector.omni-role=system" --wait
  # metrics-server (EKS ships none; AKS and GKE do): the pinned release, on the system machine
  kubectl apply -f "https://github.com/kubernetes-sigs/metrics-server/releases/download/$MS_VERSION/components.yaml"
  kubectl -n kube-system patch deployment metrics-server --type=merge -p \
    '{"spec":{"template":{"spec":{"nodeSelector":{"omni-role":"system"},"tolerations":[{"key":"CriticalAddonsOnly","operator":"Exists","effect":"NoSchedule"}]}}}}'
  kubectl -n kube-system rollout status deployment/metrics-server --timeout=300s
  aws eks describe-cluster --name "$name" --region "$REGION" --output json > "/tmp/eks-$name.json"
  echo "######## ARM $arm (repetition $REP)"
  mkdir -p "bench-$arm-$REP"; cp "/tmp/eks-$name.json" "bench-$arm-$REP/eks_cluster.json"
  if ! PLATFORM=eks ARM="$arm" OUT_DIR="bench-$arm-$REP" bash scripts/kind_bench.sh; then
    echo "ARM $arm (repetition $REP) FAILED its checks: marked invalid" | tee "bench-$arm-$REP/INVALID"; fail=1
  fi
  gone "$name"
done
exit "${fail:-0}"
