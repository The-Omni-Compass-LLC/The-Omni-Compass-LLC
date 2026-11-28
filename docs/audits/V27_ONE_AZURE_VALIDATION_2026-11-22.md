# V27 targeted Azure validation: single bounded dispatch, no mass reruns

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## Purpose and scope

Preserve the measured **V26 Azure** results and historical **V21/V23 GPU** records as their own campaigns. V27 changes the Kubernetes cloud scheduling path (see `docs/OMNI_V27.md`). This targeted, new **V27 Azure AKS** check asks whether (a) pods without machines and pod-minutes waiting improve or at least do not regress against native, (b) goodput and SLOs remain safe, and (c) work per dollar remains favorable in the tested case. It is not a reissue of V26's receipts, not an A+ certification, and not a multi-cloud claim.

**Do not change** `scripts/azure_queue.txt` or `scripts/reruns.txt` from `switch=off`. Their backlogs are not authorized by this one-off test. Do not enable AWS, GCP, GPU, or a dispatcher.

## Launch ONE manually dispatched workflow

Workflow: [aks-metered](../../.github/workflows/aks-metered.yml), via [GitHub Actions / aks-metered](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/workflows/aks-metered.yml).

Select `main` **after** verifying its engine fingerprint is `omni-v27` and V27 controller/scheduling tests pass. Select **Run workflow exactly once** with the following explicit inputs (overriding the workflow's larger defaults):

| Input | Value |
|---|---|
| `reps` | `3` |
| `arms` | `native compass` |
| `duration_s` | `600` |
| `location` | `eastus` |
| `vm_size` | `Standard_D2s_v4` |
| `max_workers` | `4` |
| `tier` | `standard` |
| `dial` | `max` |
| `loadgen` | `meter` |
| `rate_steps` | `2 4 6 8 10 12 16 20` |
| `stop_looks` | empty |
| `organism` | empty |
| `replica_ceiling` | empty |
| `hpa_max` | empty |
| `worker_pools` | empty |
| `price_per_node_hour` | `0.096` |

This is a **small diagnostic campaign**, not statistically powered proof of V27 preserving the V26 +30.4% work-per-dollar headline. The shorter interval also precludes claiming an apples-to-apples V26 effect-size comparison without reanalysis of matched windows.

### Safety preflight before spending

1. Verify Azure credentials and authorization by the existing no-cost `cloud-check.yml` procedure; confirm that the Azure subscription is the owner's intended billable account. Never print or paste secrets into an issue or artifact.
2. Check live Azure quota and pricing; the `price_per_node_hour` input is a *reporting assumption*, not a hard spending cap. The workflow's `timeout-minutes: 300` is per repetition, and AKS provisioning, system-node and control-plane charges may be extra. Obtain an actual cost limit and alert at the Azure subscription level before starting.
3. Check no Azure run is pending/running and that the selected commit is stable. Run the current `python3 verify.py --quick`, `python3 tools/omni_version.py`, and `python3 tools/site_surface_contract.py --check` where available.
4. Confirm `scripts/aks_paired.sh` restores the native configuration and `scripts/azure_capacity.py cleanup` succeeds even on failures.
5. Do not run from this documentation branch: its purpose is a launch/evidence plan, not a new measured release.

### Required measurements and acceptance

Capture each paired repetition's native/Omni raw values, distributions and confidence intervals for:

- unplaced pods, pod-minutes without a machine, pod-start waiting time, pending pods and autoscaler readiness;
- useful completed work, goodput within SLA, P50/P95/P99 response latency and failed requests;
- work per dollar, actual Azure costs and node-hours; distinguish metered/billed amounts from list-price estimates;
- native vs Omni scheduling/actuator actions, rollback/fail-up and V27 fingerprint.

Predeclare safety limits and record any violated metric; a composite positive gain does **not** waive a harmful service or scheduling regression. In particular, relative percentages are unstable when native waiting is nearly zero: publish absolute count/time deltas too.

After the workflow completes, save the immutable GitHub run URL, SHA-256/source SHA, engine digest, complete inputs, environment, raw artifacts, all failures and paired tables. Preserve original V26 receipts and keep V27 measurements in a **new** version-named path. If credentials, cleanup, quota, or any safety gate fails, **stop** and record the failure; do not loop or rerun automatically.

## Evidence inheritance and public language

| Evidence | Status | Permissible publication |
|---|---|---|
| Physical A10/A100 GPU, V21/V23 | Historical physical measurements | Quote with their original version, card, workload, and adverse rows |
| Azure AKS V26 | Historical live cloud measurements | Quote work-per-dollar +30.4% campaign together with higher expenditure and pod-wait regressions |
| Kubernetes V26/V27 software tests | Version-specific live software receipts | Publish named version/test, without translating composite index into universal throughput |
| Azure V27 | Not measured by this document | Only claim a V27 physical result after this specific workflow yields admissible data |
| AWS EKS / Google GKE | Not certified by Azure | Do not infer three-cloud physical measurements from one provider |

A referee-grade physical claim requires an evidence row pointing to exact source commit, environment, protocol, raw data, computed uncertainty, limitations, complete runs and adverse cases. **Do not retroactively rename an old result V27.**

## Launch authority and release status

This file **does not start a paid benchmark**. The current GitHub connection cannot dispatch workflow runs. A human authorized on GitHub must execute the single workflow-dispatch action after checking the preflight. The queue switches remain off and no billable resource is authorized by merging this file alone.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
