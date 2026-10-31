# A cluster you build in your own cloud's console: Oracle, DigitalOcean, Alibaba Cloud, Linode, IBM Cloud or any other

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The same benchmark Azure runs (`aks-metered.yml`), run on a managed Kubernetes cluster that you build in your provider's own
console and hand over by its kubeconfig: `byoc-metered.yml` with `scripts/byoc_paired.sh`. Native and Omni-Compass on top of
native run on that one cluster, back to back, in an order rotated by repetition. The measuring is `scripts/kind_bench.sh` in its
managed-cluster mode: kubectl only, the probe through the cloud's load balancer, the load generator on the system machine, and
the work machines counted every 15 s. The bill is that count times the list price you give for one work machine-hour. The same
four sets as Azure's (steady, the two bursts, the real day), at the tune-down with native's replica cap, 100 paired repetitions
a set under the preregistered stopping rule (`tools/stop_rule.py`).

**This is written and wired, and has not been run on any of these clouds.** Each cloud's queue
(`scripts/oracle_queue.txt`, `digitalocean_queue.txt`, `alibaba_queue.txt`, `linode_queue.txt`, `ibm_queue.txt`) reads
`switch=off`, and every page reads it "not yet run" until its first run lands. The first repetition of a first set is a
shakedown, and any arm that fails its own checks is marked INVALID and never counted.

**Who pays.** You do, on your own cloud account, for the cluster you build. This repository creates and deletes nothing in
your account: it reads and writes inside the cluster you hand it, and never makes a machine. Delete the cluster when the set ends.

## 1. The cluster's shape

Build one managed Kubernetes cluster with two node pools:

| Pool | Machines | Label | Taint | Autoscaling |
|---|---|---|---|---|
| system | exactly 1 | `omni-role=system` | `CriticalAddonsOnly=true:NoSchedule` | off |
| work | 1 up to N (4 in every queued set) | `omni-role=work` and `agentpool=work0` | none | the provider's own cluster autoscaler, minimum 1, maximum N, removing an empty machine |

The system machine carries the provider's add-ons and the load generator and is never measured or governed. Use the same
machine size for every work machine, and the smallest general-purpose size with 2 processors and 8 GB that your provider offers,
so the bill compares like with like.

Each provider's console names node pools differently (Oracle: node pools of an OKE cluster; DigitalOcean: node pools of a DOKS
cluster; Alibaba Cloud: node pools of an ACK cluster; Linode: node pools of an LKE cluster; IBM Cloud: worker pools of an IKS
cluster). Where the console has a field for node labels and taints, set them there. Where it does not, set them once the pools are
up, from a computer that holds the cluster's kubeconfig:

```
kubectl label nodes <system-node> omni-role=system
kubectl taint nodes <system-node> CriticalAddonsOnly=true:NoSchedule
kubectl label nodes <each-work-node> omni-role=work agentpool=work0
```

A label set by hand is not carried to a machine the autoscaler adds later. If the console cannot label the work pool itself,
the work machines the autoscaler adds will not be counted, so use a provider whose console labels a node pool.

## 2. Check it before anything is measured

`scripts/byoc_paired.sh` reads the cluster's shape before anything is measured, and stops with what is missing named when:
- the cluster does not answer;
- there is not exactly one system machine, or it does not carry its taint;
- there is no work machine;
- there are more work machines than the maximum you gave.

The same check runs on its own, at no cost (Actions, then **cloud-check**, then **Run workflow**, with `cloud` set to your cloud's
name). It reads the kubeconfig's shape (never a character of it is printed) and the cluster's shape, then stops.

## 3. The kubeconfig GitHub uses

A kubeconfig your provider's console downloads usually logs in through the provider's own command line (`oci`, `doctl`,
`aliyun`, `linode-cli`, `ibmcloud`), which GitHub's runner does not carry. The check refuses such a kubeconfig by name. Store
instead a kubeconfig whose user holds a service-account token:

```
kubectl create serviceaccount omni-bench -n kube-system
kubectl create clusterrolebinding omni-bench --clusterrole=cluster-admin --serviceaccount=kube-system:omni-bench
kubectl apply -f - <<'EOF'
apiVersion: v1
kind: Secret
metadata: {name: omni-bench-token, namespace: kube-system, annotations: {kubernetes.io/service-account.name: omni-bench}}
type: kubernetes.io/service-account-token
EOF
TOKEN=$(kubectl get secret omni-bench-token -n kube-system -o jsonpath='{.data.token}' | base64 -d)
SERVER=$(kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}')
CA=$(kubectl config view --minify --raw -o jsonpath='{.clusters[0].cluster.certificate-authority-data}')
cat > omni-kubeconfig.yaml <<EOF
apiVersion: v1
kind: Config
clusters: [{name: work, cluster: {server: $SERVER, certificate-authority-data: $CA}}]
users: [{name: omni-bench, user: {token: $TOKEN}}]
contexts: [{name: work, context: {cluster: work, user: omni-bench}}]
current-context: work
EOF
```

The account is the cluster's administrator because the benchmark installs its workload, its load generator and the governor,
and writes node taints. Delete the cluster, or the service account and its binding, when the set ends.

Store the whole file in the repository's secrets (Settings, then **Secrets and variables**, then **Actions**, then **New
repository secret**), named for your cloud: `KUBECONFIG_ORACLE`, `KUBECONFIG_DIGITALOCEAN`, `KUBECONFIG_ALIBABA`,
`KUBECONFIG_LINODE`, `KUBECONFIG_IBM`, or `KUBECONFIG_OTHER` for any other conformant cluster. The file as it is, or base64 of it,
are both read.

## 4. Start a set

By hand: Actions, then **byoc-metered**, then **Run workflow**. Set `cloud` to your cloud's name, `max_workers` to the work pool's
maximum, and `price_per_node_hour` to your provider's list price for one work machine-hour on the day (written beside the run).
The conductor (`scripts/dispatch_grid.py`) starts a cloud's sets in order, A of every set, then B, then C, only once that
cloud's queue reads `switch=on` (on the founder's word) and its newest **cloud-check** passed.

## 5. What is read

Every repetition's files are this run's artifacts, archived onto the branch `raw` by the archive bot. They are read with the same
tools as Azure's (`tools/live_reps.py`, `tools/confirm_abc.py`), by the one key (`tools/readings.py`), three runs, A, B and C.
In a cloud Omni-Compass shows that the engine holds on the cloud's machines as it does on site, and the work per dollar: more work
for the same bill, never a smaller bill as the aim (the founder's words of 31 October, which struck the order of 14 October). The engine is the same on every cloud; what differs is the wire to it: this workflow, the paired script, the
queue and the kubeconfig check.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
