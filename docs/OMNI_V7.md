# Omni v7: tighter convergence on top of v6 (the engine of 16 to 17 October)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v7 stood on main from 16 to 17 October; on 17 October it was followed by Omni v8 (`docs/OMNI_V8.md`, the founder's
order), omni-v7 with one wire changed (the CityLearn runner: a battery whose building simulates outages stays native), and the
same day by Omni v9 (`docs/OMNI_V9.md`), and on 18 October by Omni v10 (`docs/OMNI_V10.md`), the engine that stands. This page and
v7's twenty-two three-run tables (`results/live/V7_*.md`) stay as that engine's record, read beside no other engine's.

Omni v7 was the engine that stood on main from 16 October (the founder's order: everything on the newest engine). Every benchmark ran again on it (`scripts/reruns.txt`; the grid conductor's reruns, grid and Azure queues restarted on it the same day), and every earlier table stands as its own engine's result until its three runs on v7 land; results from two versions are never pooled. v7 is v6 with five changes, each found from a v6 run's own files or from the governing rules themselves:

| # | Change | Where | What it tightens |
|---|---|---|---|
| 1 | CPU conveyance obeys the namespace quota | `omni_controller/quota.py`, `muscles.py` | no write Kubernetes would refuse |
| 2 | On a shared host, no limit raised while the machine is at or over 75% busy or unread (the replica room's guard) | `omni_controller/muscles.py` | the host's top, nothing else |
| 3 | The verdict reads a trial in the reports' own words (GAIN, STEADY, LOSS) | `omnicompass/verdict.py` | the do-no-harm trigger |
| 4 | Every rule counts in seconds, not decisions | `omni_controller/controller.py` | the same behaviour at any decision period |
| 5 | The cloud's rule in one word, `--give-back-only` | `omni_controller/controller.py`, `deploy/install/omni-compass-cloud.yaml`, `scripts/kind_bench.sh` | the bill can only fall or stay |

## 1. Quota-aware conveyance

The original capacity run 38722001872 tried to raise a pod CPU limit while its namespace CPU quota was already full. The candidate reads each namespace's ResourceQuota CPU-limit hard/used values, obeys the stricter pending spec/status ceiling, and reserves each accepted increase across all target deployments in one conveyance pass. It does not increase or delete an operator quota. PriorityClass scope selectors are matched from pod metadata, without deployment or quota names hardwired into the governor. Unknown quota state, read failures and unsupported scopes preserve native limits for expansion; reductions remain possible. Decreases do not create spendable headroom until observed by Kubernetes.

**What the first live trial found, and the correction (16 October).** The three trials of the candidate as first pushed (Goldilocks run 38825214203, the KEDA add-ons run 38825211370, the capacity test run 38825208939; one run of ten pairs each, so single runs, not three-run tables) read the candidate well short of omni-v6's three-run tables on the two add-on tests: Goldilocks response time at the 95th percentile -6% (STEADY) against v6's -58% GAIN in all three runs, HPA replicas +20% and pods started +200% (power given), the pod start wait +172% (LOSS); KEDA on the requests in flight p95 -2.7% (STEADY) against v6's -73%, replicas +17% (power given); KEDA on the CPU target and the requests p95 +3% (STEADY) against v6's -55%; the capacity test STEADY at every cap, as on v5. The governor wrote 5 commands a run against v6's 15 and the host was 4% busier against 40%: conveyance never raised a limit. The audit says why, 65 times in one repetition: `quota: CPU limit expansion blocked, reason: quota read unavailable: CalledProcessError`. The governor's role on every kind test (`deploy/kind/rbac-omni.yaml`, receipted in each run's `rbac_omni.txt`) cannot list ResourceQuotas, and the budget as first written read an unreadable quota as a zero allowance. The model gate had not seen it because its model of the cluster answered the quota read with an empty list. The correction: a namespace whose quotas cannot be read is **no budget known**, not a zero budget; the raise proceeds as it did on omni-v6 and Kubernetes' own admission, which refuses any write over a quota the governor cannot see, stays the authority (the plug reads every write back and a refused one is audited and never advertised); the audit says so once a pass. Where the role can read the quota, the budget bounds every raise as before. The model now runs the convey model a second time with the quota unreadable (section 6), the regression `test_an_unreadable_quota_holds_nothing` holds the v6 arithmetic under a forbidden read, and the three trials run again on the corrected candidate; the first trials stay in `results/live/raw/` on this branch as the record of the fault.

Kubernetes admission remains authoritative. A concurrent rejected write is audited and does not become an invented conveyance gain. The node's existing CPU cushion, operator CPU floor, security hold, workload schedule and benchmark validity checks remain intact. The separate runner shutdown in the historical run has no established cause and is not claimed fixed by this actuator change.

## 2. Conveyance on a shared host: one guard, two designs refused by the model

The v6 three-run KEDA table (`results/live/V6_KEDA_REQUESTS.md`) read the pod start wait, mean, +12.5%, +12.0% and +22.7% (STEADY on the three-run rule, LOSS in two single runs) beside response time -59% and CPU used +55%. The run's own files (`results/live/raw/addons-run-38725705826`): 149 raises, each pod's limit set to 1,850m (two serving pods on its node) or 3,700m (one), the HPA at 8.8 replicas on average, the host 0.27 busy under native and 0.34 under Omni-Compass, past 75% busy for 0.3% of its samples. On kind every node is a container on one 4-core machine and reports all four cores as its own, so the limits sum to about three machines: a ceiling, not a use; the kernel's fair scheduler arbitrates when the pods ask for more than the machine, as it does for native's pods.

Two repairs were written first and both were refused by the model gate (section 6) before any real run: **the host's CPU counted once** and shared by every serving pod (at the run's nine replicas 3,500m / 9 is under the operator's 500m, so nothing is ever conveyed: in the model the +64% work and -53% response time of conveyance are lost whole, requests served -16% against v6, LOSS); and **a hold while a pod starts on the host** (start wait 1.1% shorter for requests served -0.11% and response time +0.5%, both LOSS against v6 at the real regime). v7 keeps the one guard the model reads as no LOSS, the same as the replica room's (`omni_controller/capacity.py`): on a shared host no limit is raised while the machine's measured busy share is at or over 75% or cannot be read; limits already given stay; lowering is never held back; each hold is written to the audit (`"convey": "held"`). The slower pod start is the busier host serving more requests, the price of the work; it stays shown in every receipt and is judged as the table judges it.

## 3. The verdict in words

The verdict (`omnicompass/verdict.py`) is the engine's do-no-harm trigger: before a knob may move one step further from native, the step runs as a trial and its cost per piece of work is compared with the cost at the reference. Through v6 the comparison was the two medians alone: the step was allowed if m[trial] ≤ m[ref] · (1 + tolerance). On noisy work a median wanders, so a step that truly cost more than the allowance was often allowed by chance.

v7 (`judge="interval"`, the default) reads the trial exactly as a report reads a row (`tools/readings.py`). On the logarithm of each piece of work's cost, so that a heavy tail does not decide it, the change is

d = mean ln c[trial] − mean ln c[ref],  with the 95% interval  d ± 1.96 · √(s²[ref] / n[ref] + s²[trial] / n[trial])  (Welch's standard error),

and with τ = ln(1 + tolerance) the allowance in the same units:

- the interval wholly above zero is a **LOSS**: the step is refused and undone, whatever the allowance says;
- wholly below zero is a **GAIN**; across zero is **STEADY**;
- while the interval's half-width exceeds τ, the evidence is wider than the allowance, and the trial measures on, up to three times `min_samples`, before it decides;
- a GAIN or STEADY step is allowed only if both estimates are inside the allowance: the median (v6's guard, kept) and d ≤ τ;
- a stepwise knob is read the same way against the costs first measured at native as well, so a run of small steps cannot add up past the allowance.

Every judgement writes its reading and its intervals to the audit (`"reading"`, `"interval_ln"`). `judge="median"` reproduces v6 exactly.

On noisy work (log-normal costs, σ = 0.25, a 2% allowance, 300 trials each, seeded):

| True cost of the step | Allowed through v6 (medians) | Allowed in v7 (in words) |
|---|---|---|
| +0% (free) | 63% | 60% |
| +1% | 56% | 50% |
| +2% (at the allowance) | 47% | 39% |
| +3% | 40% | 28% |
| +5% | 26% | 14% |

A step that costs more than the allowance is allowed about a third less often at +3% and about half as often at +5%; a free step is kept almost as often. A step whose cost is clearly higher reads LOSS and is refused. These are properties of the rule on modelled costs (class S), not benchmark results (`tests/test_verdict_interval.py`).

## 4. Every rule counts in seconds

Five of the governor's rules counted decisions: the clear time after a breach (3), the cruise wait (2), the strict window (5), the verdict's probe spacing (10), recheck (120) and trial length (20). At a decision every 60 seconds those are 3, 2, 5, 10, 120 and 20 minutes; at 15 seconds they would silently shrink fourfold, and a give-back trial's 20 decisions would last 5 minutes instead of 20. v7 states each rule in seconds (`--slo-clear-s 180`, `--cruise-after-s 120`, `--strict-window-s 300`, `--verdict-every-s 600`, `--verdict-recheck-s 7200`, `--verdict-trial-s 1200`) and converts it to decisions at the running period, n = max(1, round(seconds / period)). At 60 s every count is v6's; an explicit count (`--slo-clear`, `--cruise-after`, `--strict-window`, `--verdict-every`, `--verdict-recheck`) still wins.

Two moves are made rates in time as well: the compass moves the HPA target by the same amount a minute at any period (its step is scaled by period / 60, and coasting likewise), and a node pool gives back at most one machine a minute (`RELEASE_PERIOD_S = 60`), however often the governor decides.

The default decision period stays 60 seconds. The governor core (`omnicompass/core.py`) still advances its own state by one fixed step (`MACRO_DT = 0.1`) per decision; a faster default waits for that clock to be stated in seconds too and for a test that shows no LOSS (`CLAUDE.md`, "Faster, but only where it hurts nothing"). The fast checks already run every 5 s; native's pod autoscaler runs its own 15-second check untouched underneath.

## 5. The cloud's rule in one word

In a cloud Omni-Compass shows one thing: the same work as native for a smaller bill, never a bigger one. Through v6 that rule was assembled from several settings in the workflow (`OMNI_MACHINES_ONLY=1`, the dial at the tune-down, the sensed and capped deployments left empty). v7 makes it one flag, enforced in the governor itself: `--give-back-only` turns off every pod-, processor-, power-, clock-, cooling- and batch-actuator, sets the replica ceiling to 0 and the dial to the tune-down, and leaves the node pool as the only knob. Whatever else is passed, the governor can then only park a machine the cloud already made, after its own trial, and wake it on a breach: no more pods and no more machines than native. The Azure, Google and Amazon install file (`deploy/install/omni-compass-cloud.yaml`) and the machines-only branch of `scripts/kind_bench.sh` pass it.

## 6. The model gate: every change run in our own models first

The founder's order of 15 October, night: every fix, knob and rule is tried in a model before it is pushed, and goes to a real run only where it shows promise there. `tools/model_gate.py` runs two checkouts, the engine that stands and the candidate, each in its own process, on the same seeds, and reads the candidate against the standing engine paired by seed (the mean change, its 95% interval over the seeds, the word by the gauge's aim). Three models, all evidence class S, our own models, never a benchmark result:

- **cluster**: the shipped Kubernetes controller in the cloud setting (node-pool mode, the compass law, the tune-down, `--give-back-only`) on the model cluster of `pilot/selfpilot.py` as the cloud meets it (the cloud's own autoscaler makes machines in both arms; the governor only parks one that exists, which the cloud deletes after ten minutes empty, and wakes it while it exists); a decision every 60 s and the fast check every 15 s; **cluster15** the same with a decision every 15 s.
- **convey**: one 4-core host carrying three kind nodes, php-apache under its HPA (200m request, 500m limit, 50%, 1 to 10), load generators stepping 1 2 3 1 2 1 as `deploy/kind/loadgen.yaml` runs them, set so the native arm sits where the v6 KEDA run's native arm did (host busy 0.28 and p95 0.40, response p95 229 ms, 8.3 pods against the run's 0.27, 0.42, 248 ms and 8.8); the candidate's own `Muscles.convey` called every 15 s. Since 16 October the model runs twice: once with the namespace's quota readable and empty (`convey`), once with the quota unreadable, as the governor's role finds it on every kind test (`convey_unreadable_quota`): the first trial's fault (section 1) is now the model's to catch.
- **verdict**: the do-no-harm trigger alone on noisy work.

What it read on v7 against v6, 10 seeds (`results/model_gate/`):

| Model | Reading |
|---|---|
| cluster, 60 s | v7 and v6 STEADY on every gauge; both against native: bill -1% (STEADY), energy per core-hour -2.4% GAIN, pods waiting for a place about three times native's (v6 LOSS, v7 STEADY). The cloud setting itself barely cuts the bill in this model and makes pods wait; checked against the Azure receipts' own pending-pod gauge before anything is concluded. |
| cluster, 15 s | v6: bill +43% (power given), pods waiting 10x (LOSS). v7: bill STEADY against native, pods waiting +111% LOSS, p95 +0.3% LOSS. Every rule now keeps its time, and faster is still not free: the default stays 60 s. |
| convey | v7 as first written (host once, start hold): requests served -16%, p95 +155% against v6, LOSS, nothing conveyed. The busy guard alone: identical to v6 at the real regime and at double load (the hold never binds under 75%). |
| convey, quota unreadable (added 16 October) | the candidate as first pushed (digest 1a0d1d1b91bc49ad): requests served -39% and p95 +113% against v6, LOSS, the host and the limits given identical to native: nothing conveyed, as the live trials found. The corrected candidate (digest d6d467b824c585f1): identical to v6 on every gauge (+64% requests and -53% p95 against native), with the quota readable and empty and with it unreadable alike. |
| verdict | a step costing 3% more allowed 28% of the time instead of 40%; 5% more, 14% instead of 26%; a free step 60% instead of 63%. |

## The first three-run tables on v7 (16 October)

Twelve runs on real Kubernetes, ten pairs each, every one omni-v7 (`results/live/V7_*.md`), native against Omni-Compass on top.
No row reads LOSS on the three-run rule.

| Benchmark | What moved, GAIN in all three of our runs | STEADY | Power given |
|---|---|---|---|
| Goldilocks and the VPA's recommender | response time −45% to −47% mean, −60% to −62% p95, −67% to −69% p99; time over the line −100% | machines, failed requests, replicas, pods started, pod start wait, alert minutes | parked-worker energy +1.6% to +2.3% |
| KEDA's HTTP add-on | response time −57% to −58% mean, −71% to −75% p95; alert minutes −93% to −96%; replicas −15% to −19%; pods started −17% to −23% | machines, failed requests, pod start wait | parked-worker energy +2.2% to +2.3% |
| KEDA on CPU and requests | response time −36% to −38% mean, −52% to −54% p95, −57% to −59% p99; time over the line −98% to −100% | machines, failed requests, replicas, alert minutes | parked-worker energy +1.1% to +1.7% |
| CruiseKube applying its own recommendations | nothing: no setting written | every gauge | none |
| Fixed capacity, four CPU caps | nothing: the cap blocks the one lever | completed work and work inside the line at every cap | none |

Single runs clear of the noise that the other two did not repeat, each STEADY on the rule: CruiseKube's 99th percentile +3.1% (run A)
and node-hours +1.0% (run B); Goldilocks replicas +3.4% (run C); capacity's completed work +3.8% at 1 core (run A).

## The room search (16 October): the muscles that read the same as native

The founder's standing question is whether every muscle runs at its own edge. On the realms table of the engine that stands
(`results/realms_v5/MUSCLES_V5.csv`, the preregistered seeds 3000-3009), 159 of the 1,107 muscles read SAME AS NATIVE on every
load. Measured muscle by muscle on development seeds (7100 and 7101) in our own models (class S, never a benchmark result):

| Muscles | Plant and knob | What the max does | Native's own misses | Room under the max's gauges |
|---|---|---|---|---|
| 111 | a process loop's setpoint (the process, irrigation, turbine, batch-reactor, pipeline, mill, district-heat and inverter presets) | writes nothing: the loop's actuator is native's full range, and the loop's work is the disturbance it handles, fixed by the load | median 0.00% of decisions, at most 0.56%; 6 of the 111 miss at all | none on work or speed; on misses, the 0.56% of six loops, which a setpoint eased toward the band's middle could touch: a card candidate for a later version, worth under one part in a hundred |
| 36 | a cooled zone's setpoint (the data-hall, building and hospital presets) | cools ahead of the heat (28 of the 36 wrote), and under native the room never nears its line either | 0.00% on all 36 | none: nothing above native to give |
| 12 | a battery's power knob (the UPS, microgrid and facility presets) | holds the charge for the line and gives native's full power once the line could need it | 2.1% to 24.3% of decisions | every miss falls while the charge sits at the operator's reserve (0.6 for a UPS, 0.2 for a microgrid), above the outage floor; the power knob may not spend the reserve, and the max keeps that boundary. The charge between the reserve and the floor belongs to the setpoint knob, where the engine's cards already read GAIN (8 of 8) |

The reading: the max already takes every muscle to the edge its own knob has. Where a muscle reads the same as native, the
measurement says there is nothing above native for that knob to give, and the max leaves it native by design (do no harm).
The one measurable room, six process loops' 0.56% of decisions, is noted for a later version's card search; it is not an
engine change, and no engine file moved for this measurement.

## Validation

Six shared-host regressions pass (`tests/test_convey_shared_host.py`: each node keeps its own arithmetic under the top, a busy or unread host holds every raise, a busy host still lowers, a start holds nothing, separate machines are never held, an unreadable quota holds nothing). Nine quota regressions pass (`tests/test_quota_convey.py`, among them: an unreadable quota is no budget known); the original source fails both the full-quota regression and the admission-rejection regression. Existing conveyance integration checks pass unchanged. The verdict's rule tests (`tests/test_verdict_interval.py`, `tests/test_verdict.py`: v6's medians kept under `judge="median"`, a noiseless 1.5% rise refused against a 1% allowance under v7), the time-correct tests (`tests/test_time_correct.py`, `tests/test_cloud_cadence.py`) and the cloud tests (`tests/test_cloud_machines_only.py`) pass, as do every verdict user's tests (Redis, Kafka, pgbench, sysbench, YCSB, CPU power, GPU). Live GitHub trials on the v7 commit (KEDA's add-ons, Goldilocks, CruiseKube, capacity) repeats the original cap 1500m / repetition 4 / 1200-second-per-arm case at the original request rates. Its completion and measured result must be read from its artifact, with any LOSS retained. The trial cannot launch Azure, Google, Amazon or GPUs.

The organisms the candidate is run on are the seven of 16 October (the spine, the 267 muscles every stack runs on, the seventh; `docs/THE_SPINE.md`): they are groupings of catalog rows made in the runners, so the candidate's fingerprint did not move for them, and every organism table on this engine lists the spine first.

Reference: Kubernetes [Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/) and [in-place container resource resizing](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/). The CPU budget helper is included in both the engine and actuator fingerprints. README.md, LICENSE, NOTICE, DISCLOSURES.md, PATENTS.md and TRADEMARKS.md accompany the trial artifact.

© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
