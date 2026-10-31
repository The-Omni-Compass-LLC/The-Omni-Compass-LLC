# Preregistration: the compass law on real Kubernetes (set 26)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written and committed before the run. The run's commit is the one that carries this file; nothing in the law, the
harness or this rule changes after it starts.

## What is run

Workflow `benchmark-reps` on `main`, 10 repetitions. Each repetition runs three arms back to back on the same runner,
each on a fresh six-worker kind cluster, in an order rotated by repetition (`scripts/kind_paired.sh`):

| Arm | What governs |
|---|---|
| native | Kubernetes alone (HPA at target 50, scheduler); Omni-Compass not started |
| omni | Omni-Compass on top with the engine's allocation law (`--law governor`, the law of sets 22 to 25) |
| compass | Omni-Compass on top with the compass law (`--law compass`, `omni_controller/controller.py`) |

Load: fixed rate (`loadgen=open`), the same work in every arm. 900 measured seconds per arm. SLO 500 ms at the 95th
percentile. Every Omni arm runs the six-state engine on every decision, the nervous system's authority and release
gate, the shield, the compass, and ends with the reset, which must return the HPA target, its replica range,
the pods' CPU limits and every worker to native, with no record left (`scripts/kind_bench.sh`).

## The compass law in the live controller

The service position is the 95th-percentile response time over the SLO (0 calm, 1 the line); a blind probe or a pod
waiting for a place reads as past the wall. The force is `A tanh((K_P (p - 0.5) + K_D v) / A)` with K[D] for critical
damping times the realm push factor 3, the same law and gains as on every realm muscle (`realms/compass_arm.py`):
up gain 0.10, down gain 0.02, release threshold -0.2. Two levers:

1. **HPA target**, cover from 60% of the operator's target to the operator's own: the up force lowers it (more pods),
   the down force returns it toward the operator's. It is never tighter than native.
2. **Node pool**: past the 0.95 wall one machine more at once; one machine back only while the force is below -0.2,
   the position is below the center, and the nervous system's release gate is open.

## Outcomes and the rule

Primary: **worker nodes in service** (mean) and **95th-percentile response time**, each arm against native, paired
over the 10 repetitions with a t-based 95% interval (`tools/live_reps.py`).

Band first: the compass arm is a win only if its p95 is not behind native's (the upper end of the 95% interval of the
paired difference at or under 0) **and** failed requests are not higher. If that holds and machines in service fall
with an interval wholly below 0, the label is **fewer machines within the band**. If machines fall but the band
condition fails, the label is **tradeoff**. Otherwise **not established**.

Secondary, reported, not used for the label: p99, mean response time, HPA replicas, pods started, pod start wait, CPU
including Omni-Compass's own, the declared energy models. The omni arm is reported against native and against the
compass arm by the same rule. A run that fails its own checks (reset, controller stopped early, missing permission)
is marked invalid and left out, never silently counted.

Evidence class **L**: real Kubernetes software on kind. Energy on kind is a declared model, not a meter.

## Set 26 result

Compass arm against native: machines in service -17.2% (-26.4% to -7.9% of native), p95 -64.8%, failed requests 0 on
both: **fewer machines within the band** (`results/live/LIVE_REPS_26.md`). The allocation law in the same set:
machines -35.8%, p95 -55.4%.

## Set 27 (written before the run)

The compass in the live controller now reads the service as the GPU compass does (`omni_controller/gpu_compass.py`, GPU
amendments 6 and 7): the mean response time of the latency window between the bare service time (a tenth of the SLO)
and the SLO, held at the compass's center 0.4 (the GPU service profile); p95 at or past the SLO, a blind probe or a pod
waiting for a place is past the wall. Everything else, the arms (native, omni, compass), the load, the duration, the
outcomes and the labelling rule above, is unchanged. The run's commit is the one that carries this section.

## Set 27 result

Compass arm, aligned with the GPU governor, against native: machines in service -15.9% (-1.462 to -0.450 machines),
p95 -65.5% (-311.8 to -156.1 ms), p99 -72.6%, failed requests 0 on both: **fewer machines within the band**
(`results/live/LIVE_REPS_27.md`, run 37071353971, commit `d46c959`). The allocation law in the same set: machines
-36.6%, p95 -53.1%.

## The verdict in the live controller (2026-10-03, before any further set)

The compass law gives a machine back only where it measures that the service is never behind for it
(`omnicompass/verdict.py`, stepwise, in `omni_controller/controller.py`). While the service is calm (inside the compass,
no pod waiting, no breach), one more machine is given back on trial. The response times of 200 requests served without
it are set against 200 served just before and against the cluster as it first ran on its own:
- at most 2% slower than both: the machine stays given back;
- slower than that: it is taken back and not tried again for 120 decisions.

Where no machine passes, the pool stays as the cluster runs it alone. The HPA target's cover is unchanged: from 60% of
the operator's target up to the operator's own, never looser than native. Every trial is in the audit. The next set
runs with this verdict; sets 26 and 27 ran before it and stay as they ran.

## Set 28 and set 29 (2026-10-03, set 29 written before its run)

Set 28 (run 37087620193, commit `24666d7`) ran the compass law with the verdict. With Omni-Compass on top against native:
- machines in service −4.7%;
- p95 −65.3%, p99 −68.6%;
- pods waiting 0;
- failed requests 0.

Total CPU including Omni-Compass's own came out **+2.2%** (+0.003 to +0.042 cores), more than the 2% the one rule
allows (`DISCLOSURES.md`, section 3). The cause is the controller's own cost: 0.063 cores, mostly a new kubectl process
for every read, about 20 a minute. The compass law with the verdict freed only 0.040 cores of work. The allocation law in
the same set: machines −29.6%, p95 −58.0%, total CPU including its own −1.2% (not significant). Set 28's receipt is
`results/live/LIVE_REPS_28.md`, published with this section.

**Set 29** runs the same arms, load, duration, outcomes and rule as set 28. One thing changes: the controller reads
through one `kubectl proxy` started once, under the same least-privilege identity, so a read is a local HTTP request
instead of a new kubectl process (`omni_controller/controller.py`, `Kube`; writes are unchanged; `tests/test_api_proxy.py`).
The label also requires total CPU including Omni-Compass's own to be no more than 2% above native.

Set 29 result (run 37094338955, commit `a3721cc`): the compass law with the verdict, total CPU including its own **−4.7%**
(−0.071 to −0.017 cores), passes; Omni-Compass's own CPU 0.011 cores (set 28: 0.063). Machines −5.1%, p95 −64.4%,
p99 −71.1%, HPA replicas −7.6%, failed requests 0. No measure significantly behind native in either arm. Receipt:
`results/live/LIVE_REPS_29.md`.

## The cost to match (written before its run)

The question a buyer asks: what would native Kubernetes have to spend to answer as fast as it does with Omni-Compass on
top? Each repetition runs, on the same runner and the same work, in rotated order:
- native (the operator's HPA target 50);
- native tuned harder by its operator, HPA target 40, 30 and 20 (more pods, faster answers), no Omni-Compass (`ARM=native40`, `native30`, `native20` in `scripts/kind_bench.sh`);
- native with Omni-Compass on top, the allocation law (`omni`);
- native with Omni-Compass on top, the compass law with the verdict (`compass`).

The report (`tools/live_reps.py`, "The cost to match") lists every arm's p95, p99, HPA replicas, CPU including
Omni-Compass's own, and machines in service. For each Omni-Compass arm it names the cheapest native setting (by CPU)
whose p95 is at or under Omni-Compass's, and that setting's extra replicas, CPU and machines over Omni-Compass. If no
native setting tried reaches it, the report says so and gives the lowest native p95. 10 repetitions, 900 measured
seconds per arm, fixed-rate load.

## The fault test (written before its run)

Health, security and the babysitting a cluster needs, measured. Every arm (native; native with Omni-Compass on top,
the allocation law; native with Omni-Compass on top, the compass law with the verdict) meets the same four faults at the
same moments (`scripts/kind_faults.sh`, `FAULTS=1`):
1. at 15% of the run, a worker machine dies (its kind container is stopped) and comes back two minutes later;
2. at 35%, traffic triples for two minutes;
3. at 55%, a pod with no CPU limit burns CPU for two minutes;
4. at 75%, the response-time probe goes blind for one minute.

For each fault the report (`tools/live_reps.py`, "The fault test") gives the time to recover (from the fault's start
until responses stay under the line for 30 s straight, at most 300 s) and the share of samples over the line or failed
in the 300 s after it, paired against native over 10 repetitions. All the usual gauges are reported as well, now
including the share of response samples over the line (`pilot/bench_report.py`). The aim is lower in each.

**The fault test, first run** (run 37094604580, commit `a149d4e`; `results/live/FAULTS.md`). Omni-Compass on top
recovered faster than native from every fault (allocation law: machine down −29%, runaway pod −35%, spike −7%; compass
law: −14%, −17%, −6%), p95 −53% and −55%, p99 −27% (not significant) and −57%. One measure read LOSS: with the compass law,
**HPA replicas +8.2%** (+0.41 to +0.99, significant), with CPU and machines unchanged and no energy saved, so outside
the one rule (`DISCLOSURES.md`, section 3). The cause: past the wall the compass lowers the HPA target at once (more pods,
the faster recovery), then handed the operator's target back step by step and held each step for the autoscaler's
window, so the extra pods outlived the fault.

**The change, written before the re-run** (`omni_controller/controller.py`, the compass's push and pull on the HPA target;
`tests/test_compass_controller.py`, "fault over"): once the responses are back inside the band (the compass's position under
its center), the response line is clean and no pod is waiting, the operator's own target returns at once and is not
held by the window. More pods only while the fault lasts. The re-run is the same fault test, arms, load, duration and
rule (set 30 F); set 30 runs the same code without faults, to show nothing else moved.

**Set 30 and set 30 F** (runs 37105047258 and 37105046042, commit `acc1c4e`; `results/live/LIVE_REPS_30.md`,
`results/live/FAULTS_30.md`). Set 30, no faults: no LOSS clear of the noise in either arm; the compass law's machines
−9.9%, p95 −64.9%, time over the line −98.7%, HPA replicas −32.2%, total CPU −6.5%. Set 30 F: recovery faster than native
from every fault in both arms; the compass law's HPA replicas **+5.6%** (first run +8.2%), still significant, with CPU and
machines unchanged. The allocation law, which recovers as fast or faster, held no extra pods (+2.0%, not significant).

**The second change, written before set 31 F** (`omni_controller/controller.py`; `tests/test_compass_controller.py`,
"blind"). Past the wall, the compass lowers the HPA target (more pods) only when the cause is load: the response line
breached with every sense live and no pod waiting. Past the wall from a blind sense, or from pods waiting for a machine
that is gone, more pods answer neither, so the target is the operator's own: fail up is native's own setting, as on the
card, where fail up is the card's own clock and limit. The machine reflex (one machine more past the wall) is unchanged.
Set 31 F is the same fault test, arms, load, duration and rule; set 31 the same without faults.

**Set 31 and set 31 F** (runs 37110007121 and 37110005322, commit `0a38e76`; `results/live/LIVE_REPS_31.md`,
`results/live/FAULTS_31.md`). Set 31 F: the compass law's HPA replicas under faults **−1.1%** (not significant): the extra
pods are gone. No LOSS clear of the noise in either arm; recovery faster than native from every fault (compass law,
machine down −49%). Set 31: no LOSS clear of the noise; the compass law's machines −10.4%, p95 −66.0%, p99 −73.0%, time over
the line −99.4%, HPA replicas −44.5%, pods started 0 against native's 4.3, total CPU −6.1%.

## The bill on a real cloud (written before its run)

The question a buyer pays for: the same work, a smaller bill? On kind every machine stays powered, so a machine given
back saves only a declared model's energy. On a real cloud the machine is deleted and stops being billed. The run
(`.github/workflows/aks-metered.yml`, `scripts/aks_paired.sh`, `scripts/kind_bench.sh` with `PLATFORM=aks`):

- **The cluster.** Azure Kubernetes Service, a fresh cluster for every arm, built the same way:
  - a system pool of one machine, tainted so no workload lands on it (AKS's add-ons and the load generator: kind's
    control plane);
  - a work pool starting at 4 machines (Standard_D2s_v5) under **Azure's own cluster autoscaler** (min 1, max 4; scale
    down after 2 minutes unneeded), which deletes a machine once it is empty.
- **The arms**, rotated in each repetition:
  - native: Kubernetes with Azure's autoscaler alone;
  - native with Omni-Compass on top, the compass law with the verdict (`compass`);
  - native with Omni-Compass on top, the allocation law (`omni`).

  With Omni-Compass on top, the machines it gives back are idled (new pods go elsewhere, their pods leave first), and
  Azure's autoscaler then deletes them. Omni-Compass never deletes a machine itself.
- **The same work** in every arm: the fixed-rate load of sets 22 onward, 900 measured seconds after 120 s of warm-up.
- **The bill.** Every 15 s, the number of work machines that exist (in service or idle, every one is billed),
  integrated over the measured window: billed machine-hours, priced at Azure's list price for the machine
  (USD 0.096 an hour for Standard_D2s_v5, Linux, pay as you go, set in the workflow's input). Omni-Compass never reads
  this count.
- **Outcomes.** Billed machine-hours and the bill (the aim is lower), and every gauge of sets 28 and 29 (response time,
  failures, pods waiting, CPU including Omni-Compass's own), paired against native with 95% intervals over 5
  repetitions. Labelled by the one rule (`DISCLOSURES.md`, section 3): no LOSS of more than 2%, and only where the
  bill or energy is saved.
- **Housekeeping.** One repetition at a time; each cluster deleted when its arm ends, before the next is made; the
  resource group deleted at the end of every repetition whatever happens. It needs the repository secret
  `AZURE_CREDENTIALS`.

## The capacity test (written before its run)

The question behind "more work for the same cost": on the same machines, how much more work does Kubernetes serve
with Omni-Compass on top before its answers break the line? Each repetition runs native, native with Omni-Compass on
top (the allocation law) and with the compass law and the verdict, in rotated order, on the same six workers, the
open-loop load rising in eight equal steps of one load generator each (6 requests a second per generator, 1 to 8
generators, 200 s a step, 1,600 measured seconds; `load_steps` in `benchmark-reps`). A run's capacity is the highest
step at which no more than 5% of the response samples (every 5 s, through the Service) are over the line (500 ms) or
failed, every lower step holding too, the first 30 s of each step left to settle (`tools/live_reps.py`, `capacity`).
Reported: each arm's mean capacity in requests a second, its change against native and the 95% interval of the paired
difference over 10 repetitions; every usual gauge beside it. Labelled by the one rule: no LOSS of more than 2%.


## The fairness test (written before its run)

The question a buyer with many tenants asks: when one application surges, does Omni-Compass on top protect its
neighbour, or starve it? Each repetition runs native, native with Omni-Compass on top (the allocation law) and with the
compass law and the verdict, in rotated order, on the same six workers, with two applications on them (`TWO_APP=1`,
`deploy/kind/noisy.yaml`): php-apache under its usual fixed-rate load, and a noisy neighbour, the same image and the
same HPA rule, whose own fixed-rate load surges in steps (0, 0, 6, 0, 6, 0 load generators of 6 requests a second, the
same moments in every arm). Each application's response time is probed through its own Service. Omni-Compass governs
both HPAs (`deploy/kind/rbac-omni-noisy.yaml`: the second HPA and nothing else more). Reported: every usual gauge for
php-apache, and the neighbour's p95, p99, time over the line and failed requests, each paired against native over 10
repetitions with its 95% interval. The label is the one rule, applied to both applications: no LOSS of more than 2%
for either.

## The capacity and fairness results, and the amendment they call for (2026-10-03 evening, before either is run again)

**Capacity** (`results/live/CAPACITY.md`, run 37150909816): the compass law served 33.0 requests a second within the line
against native's 24.6, **+34.1% (95% interval of the paired difference +6.2 to +10.6 requests a second)**, with
response times about half of native's and fewer failures. One measure significantly LOSS: pods started 7.3 against
5.6 (+30.4%) while the mean HPA replicas were 26.9% lower: churn, not more pods. **Fairness**
(`results/live/FAIRNESS.md`, run 37154210570): the neighbour unharmed under both laws; with the compass law php-apache's
failed requests 3.89% to 4.90% (+0.12 to +1.90 points), pending pods and pod start wait higher, no machine saved. By the
one rule neither result is labelled GAIN. Both causes are read from the controller's code; both corrections are
stated here, as law, before the tests run again.

**1. Only a sensed muscle moves (the fairness cause).** Let the probe measure the response time of the services in a
set S (`--sensed ns/deployment,...`; empty means every HPA, the single-service case). For each HPA h
scaling a deployment d(h) with the operator's target x^(op)ₕ, the target written is

xₕ(t) = the compass’s (or the allocation law’s) target, if d(h) ∈ S; x^(op)ₕ, if d(h) ∉ S

The probe's position p is a statement about S alone. A push on a muscle outside S answers no
sensed error and adds pods that compete with S for the same machines (the run's pending pods and failures).
It is the GPU law's own rule, applied to Kubernetes: where Omni-Compass cannot sense, it stands at native's own setting.

**2. Pods owed to a growing demand stay (the churn cause).** Let u(t) be the CPU the workers use and W the HPA's
scale-down window (W = 300 s unless the operator set one). The demand is *still growing* when

G(t) = [u(t) > (1 + ε) min[t − W ≤ s ≤ t] u(s)], ε = 0.05 .

After a breach the compass lowers the target to the bottom of its cover, x = x[lo] = 0.6 x^(op) (more pods, at once).
Before this amendment, the first decision with the position back under the centre, p < c = 0.4, no breach and no
pod waiting, returned x = x^(op) at once. Under a rising load the autoscaler then removed the extra pods one window
later and started them again at the next step: the run's churn. The return is now

x ← x^(op) only if p < c, no breach, no pod waiting, ¬ G(t),

and while G(t) holds the target stays where the breach put it. A fault or a spike that has passed has a flat or
falling u, so G is false and the operator's target returns at once, as the fault test requires (set 31 F:
HPA replicas under faults −1.1%); only a demand still climbing keeps its pods. ε = 0.05 is set above the
decision-to-decision noise of the node CPU reading. A rise too small to clear it leaves the rule as it was before this
amendment (the target returns at once), so the correction can remove churn but cannot add any.

Nothing else changes: the compass's band, gains and centre, the verdict, the fail-up rules, the release gate and the
node-pool law are as registered. Tests: `tests/test_compass_controller.py`, cases *demand* and *sensed*, beside the
existing *fault over*, *blind* and reset cases.

**The re-runs**, on the commit that carries this amendment, unchanged in design: the capacity test (`load_steps` 1 to
8, 1,600 s), the fairness test (`two_app` 1, 900 s) and the fault test (`faults` 1, 900 s), 10 paired repetitions
each, arms native / omni / compass. The second application is now probed and reported as before, and its HPA is held at
the operator's target. Labelled by the one rule. Every number, whatever it says, is published beside the runs above.

## The re-runs under the amendment: results (2026-10-04)

All three on commit `199f350`, 10 paired repetitions each, the design unchanged.

- **Fault test, set 32 F** (`results/live/FAULTS_32.md`, run 37162459956): **no LOSS clear of the noise under
  either law.** The compass law recovers from a lost machine 58% faster and starts 34% fewer pods; the amendment left the
  fault behaviour of set 31 F intact.
- **Fairness** (`results/live/FAIRNESS_2.md`, run 37162458834): **correction 1 holds.** With the compass law php-apache's
  failed requests are no longer lower (−14.0%, not significant; before +26.0%), pending pods −10.5% (before +65.2%);
  the neighbour unharmed under both laws. The compass law's response-time gains in this test are no longer significant.
  Still higher under both laws: the mean pod start wait (+1.1 s compass, +1.7 s allocation law).
- **Capacity** (`results/live/CAPACITY_2.md`, run 37162457542): the compass law served **24.6 against native's 16.2
  requests a second, +51.9% (+6.2 to +10.6)**, the same paired difference as the first run on slower runners;
  response times −28% to −56%, failures −9.6%, HPA replicas −10.7%. **Correction 2 did not remove the extra pod
  starts** (5.1 against 3.8, +34.2%; before +30.4%): its premise, that the extra starts were pods removed and started
  again between steps, is not borne out. With the mean replicas lower, the reading the data support is pods started
  earlier on a rising load, the mechanism of the added capacity. Correction 2 stays (it removes no gain and added no
  measure power given); the pod-start rows stand as measured, and by the one rule neither the capacity nor the fairness arm
  is labelled GAIN while they do.

## The pod record, and the second amendment (2026-10-04, before the next runs)

**What the pod record shows** (`tools/pod_report.py`, workflow `pod-report`, read from the stored artifacts of runs
37162457542 and 37162458834; nothing re-run). In the capacity test native started its pods once, early (33 of 38 in
the first fifth of the window), and removed none. With Omni-Compass on top, two minutes into the window the controller
raised the HPA target above the operator's (the conveyance: each pod given a larger CPU limit, the target raised by the
same factor so each pod stays as busy, x = g x^(op); 114% with the compass law, 190% with the allocation law). The
autoscaler then removed pods (14 with the compass law, 35 with the allocation law, over ten repetitions), and the next
load steps started them again. **The extra starts are exactly those removals.** Correction 2 above read the wrong
signal: the CPU used by the whole node, where one load step is lost in the node's own load.

**3. A raise of the target waits for a steady demand.** Let the demand on an HPA's service be read from the
autoscaler's own status, D(t) = ū(t) r(t): the pods' mean CPU utilisation of their request times the pods
running, the CPU used in units of one pod's request. With W the HPA's scale-down window and ε = 0.05,

S(t) = [t − t₀ ≥ 0.9 W ∧ max[[t−W, t]] D ≤ (1+ε)min[[t−W, t]] D]

(t₀ the oldest sample in the window). A new target above the one standing (fewer, larger pods) is written only
when S(t) holds; the autoscaler itself removes pods only after its scale-down window, and Omni-Compass now asks the
same of its own consolidation. A lower target (more pods) is never held, and the return of the operator's own target
after a fault (rule 2) is unchanged. Correction 2's growth test G(t) now reads the same D(t) of the HPA concerned,
not the node's CPU. Tests: `tests/test_compass_controller.py`, case *steady*.

The capacity, fairness and fault tests are run again on the commit that carries this amendment, unchanged in design,
and published beside the runs above whatever they show. The bill run on Azure (`aks-metered`, run 37171672509)
started on commit `199f350`, before this amendment, and is reported as of that commit.

## The third amendment, and a change considered and declined (2026-10-04, before the next runs)

**4. A lower target is never held.** Until now every new HPA target, in either direction, was held for one autoscaler
window W while the line was clean, so on a step up the compass's push (a lower target, more pods) could wait up to W
and the pods arrive after the line is missed. The hold exists because a raise inside the window removes pods the
autoscaler then starts again; a lower target asks for pods and removes none. The hold now applies to raises only:

write xₕ(t) ⇔ xₕ(t) < xₕ^(now) ∨ no write in [t−W, t) ∨ the operator’s own target returns,

with rule 3 still requiring a steady demand before any raise. Tests: `tests/test_convey.py` (a lower target written at
once inside the window).

**Declined: raising the replica cap above the operator's.** `deploy/kind/demo.yaml` sets `maxReplicas: 10`, and at
the top of the capacity test both arms meet it. Lifting it would let Omni-Compass run more pods than the operator
authorised, which is more resources, not the same resources doing more, and it would break the shield's standing
rule that Omni-Compass never moves past an operator's bound. Native would need the same cap for the comparison to
stay fair. It stays at the operator's value in every arm; a higher cap is the operator's decision, tested as its own
setting if ever asked for. Already in place and unchanged: a pod waiting for a place reads as past the wall and asks
for one machine more at once.

A narrower form was proposed the same day (`docs/history/AMENDMENT_RISING_STEP_CAP.md`): while the demand rises and a
pod of the sensed service is pending, raise `maxReplicas` by the pending count and lower the target to match. It is
declined for a mechanical reason as well as the one above. The replica cap does not make pods pending: at the cap the
autoscaler simply asks for no more pods, so the pending count there is zero and the write would never fire where it is
aimed. A pod is pending only when the scheduler finds no machine with room for it, and more places under the cap give
such a pod nowhere more to go; the answer to that is a machine, which the compass already asks for. The part of the
proposal that holds, asking for pods at once on a step up instead of after a window, is rule 4 above.

On the CPU fill (used over allocatable about 0.10 in every arm): on kind every worker reports all of the host's cores
as its own, so the allocatable counts the same cores once per worker and the fill reads far lower than the machine
doing the work. Every receipt from the next runs on carries the host's own busy share and core count
(`host_cpu.csv`, `tools/live_reps.py`), so the room left on the real machine is measured, not inferred.

The capacity, fairness and fault tests are run again on the commit that carries this amendment, beside the runs of
commit `5d2e238` (rule 3 alone), so each rule's effect stays separable.

## The second amendment's runs: results (2026-10-04)

`results/live/AMENDMENT_2_RUNS.md`, commit `5d2e238` (rule 3 alone), 10 paired repetitions each.

- **Capacity: no LOSS clear of the noise under either law.** Compass law 24.6 against native's 17.4 requests a
  second, +41.4% (+5.4 to +9.0); allocation law 25.2, +44.8% (+4.9 to +10.7). The compass law's pods started 5.7 against
  4.1, interval −0.64 to +3.84: no longer significant. Rule 3 removed the significant pod-start excess and lifted the
  allocation law's capacity from +0.0% to +44.8%.
- **Faults: no LOSS clear of the noise under either law.**
- **Fairness: the compass law, no LOSS clear of the noise for either application.** The allocation law: php-apache
  much lower, and the neighbour's failed requests **+0.74 points (+0.19 to +1.28), significant**. The allocation law
  conveys idle CPU to the service it senses; on machines shared with a surging neighbour that CPU is the neighbour's
  headroom. The allocation law is not labelled GAIN in this test.

**Standing after rule 3: the compass law is clean in all three tests** (no LOSS clear of the noise, capacity +41.4%).
Rule 4 (a lower target never held) runs next on commit `583c97f`, beside these, to see whether it adds capacity without
costing a row.

## The fourth amendment: the replica cap as a lever the operator grants (2026-10-04, before its run)

The founder's instruction: no number in the harness is hard-wired; every one moves where the system lets it. The cap
of 10 in `deploy/kind/demo.yaml` is the value of Kubernetes' own php-apache example, not a choice of any operator, and
an earlier session read it as an operator's bound. It becomes a lever, under the operator's grant.

**5. Replica room.** With `--replica-ceiling` N[max] granted (0, the default, leaves the cap untouched), for a
sensed HPA under the compass law, with r the pods running, c the cap, ū the pods' mean utilisation and x
the target, the autoscaler's own arithmetic asks for n = ⌈r ū/x⌉ replicas, and

c ← min(N[max], n) if r ≥ c, n > c, p ≥ centre or the line is breached;
c ← c^(op) if n ≤ c^(op), p < centre, no breach, S(t).

The cap is raised only while it binds and the line is threatened, to what the autoscaler asks and never past the grant,
and returns to the operator's once the demand has held still for a window. The operator's range is recorded before
the first change; the reset restores it. Tests: `tests/test_compass_controller.py`, case *room*.

**Its run** (a setting of its own, labelled as such): the capacity test unchanged, `replica_ceiling` 30, beside the
runs without it. Native keeps its cap of 10, as an operator who has not raised it would; the extra pods the compass uses
are counted in the HPA replicas row, so the receipt shows what the capacity cost in pods, not the gain alone.

## The third and fourth amendments, and the bill on a real cloud: results (2026-10-04)

**Rule 4** (`results/live/AMENDMENT_3_RUNS.md`, commit `583c97f`): **the compass law has no LOSS of more than 2% on any measure in
any of the three tests.** Capacity +48.1% (+5.7 to +9.9), no LOSS; fairness, no LOSS for either application (energy
per core-hour on the declared standby model +1.5%, inside the allowance); faults, no LOSS, lost-machine recovery
−61%. The allocation law: capacity +55.6%, no LOSS; in fairness the neighbour no longer LOSS. The first runs with
the real machine metered: a 4-core GitHub runner 48% to 70% busy, where kind's "used / allocatable" reads 0.07 to 0.10.

**Rule 5, the replica lever** (`results/live/REPLICA_ROOM.md`, commit `2101c3d`, ceiling 30): the compass law served 24.6
requests a second, the same as without the lever, with 78% more pods and 26 pod starts against native's 4.6, both
significant. **The replica cap was not what limited the service; the machine doing the work was.** The lever stays,
off by default, as the operator's to grant where machines have room; it is not part of Omni-Compass's default setting
and this setting is not labelled GAIN.

**The bill on a real cloud** (`results/live/AKS_BILL.md`, run 37187059424, commit `5b2832f`, four paired repetitions):
**no difference in the bill either way** (allocation law −0.6%, compass law +0.8%, intervals across zero) and no measure
significantly power given. Azure's own autoscaler already ran the workload on about 1.86 of 4 workers, so this light
workload leaves no machine to give back. The machine savings measured on kind, where native has no node autoscaler, do
not carry to a cloud with one at this load; that is the reading of record. The preregistered size `Standard_D2s_v5` is
not allowed in the subscription's region; `Standard_D2s_v4` (same 2 vCPU, 8 GiB and list price) was used. Three
earlier attempts stopped at the load generator's placement before any measurement and are not results.


## The burst bill test (written before its run, 2026-10-04)

The steady bill run left Azure's autoscaler nothing to do and Omni-Compass no machine to give back. The question a
buyer asks is the bill under load that moves: on a real cloud, with Azure's own cluster autoscaler underneath, does
native with Omni-Compass on top bill fewer machine-hours than native alone when demand rises and falls? Same design as
"The bill on a real cloud" (fresh AKS cluster per arm, work pool 1 to 4 `Standard_D2s_v4` under Azure's autoscaler, the
bill metered every 15 s, arms native / compass / omni rotated, five repetitions), with the open-loop load in bursts
(`load_steps` 1 6 1 8 1 6, six steps over 1,800 measured seconds, the same steps in every arm). Reported: machine-hours
and the bill at list price, paired against native with their 95% intervals, beside every service gauge. Labelled by the
one rule: a lower bill counts only if nothing is a LOSS of more than 2%.


## The six organisms with the real cluster inside (written before its run, 2026-10-04)

Every benchmark runs the same six organisms, native against native with Omni-Compass on top: the four realms, the whole
tower of 656 muscles, and the four stacked with every duplicate kept (1,226). Six organisms, two arms, twelve columns.
The model grid (`six`) and the card in the loop (`tools/run_hil.py`, single card and eight cards) already do. The
Kubernetes runs now do too (`tools/run_kil.py`, workflow `six-kube` on kind, input `organism` on `aks-metered`).

Each organism runs on the measured window's clock, 240 steps, with the real cluster as one more muscle:

- efferent: the organism's offered compute work at step k, D(k) = sum over its compute pools of lam_i(k) / sum of
  lam0_i, the seeded trace, identical in both arms. The load generator runs
  r(k) = 1 + round((LOAD_MAX - 1) (D(k) - min D) / (max D - min D)) replicas, LOAD_MAX = 6 declared here, open-loop load.
- afferent: the cluster's watts (capture.csv, the declared power model, every 15 s, identical accounting in both arms)
  are added to the organism's source, zone and site power, as the card's watts are in the card harness.
- the clock (stated 2026-10-07, after the 1,000-copy runs): the organism must keep the window's clock. `tools/run_kil.py`
  records how long after the window its last step ended (`behind_s`); the report (`tools/six_kube_report.py`) shows it as
  "organism behind its window (s)", shown and not judged, and marks a repetition OFF THE CLOCK when either arm ended more
  than 5% of the window late, because its last steps then saw a cluster whose load schedule had already ended. The pairing
  stands (both arms slip alike), the mark stays on the cell. The remedy is a longer window for that size on that machine
  (240 steps, each at least the machine's time to step the organism once), never a change to the organism or the law:
  the four stacked at 1,000 copies (1.7 million muscles) step in about 31 s on an 8-vCPU machine, so their window is
  10,800 s (45 s steps), against 2,880 s for the tower at 1,000 copies.

Arms: native (the stacks' own controllers, Kubernetes alone, Omni-Compass not started) and compass (the compass law on every
simulated muscle, rule 4 on the cluster, handed back at 90% of the window; the run is invalid if any knob is not handed
back). Five paired repetitions per organism, order rotated, each arm on a fresh six-worker kind cluster, 960 measured
seconds. Seed 6000 for every organism and arm.

Reported in `SIX_KUBE.md` (`tools/six_kube_report.py`): twelve columns of means, then per organism every gauge paired
against native with its 95% interval. Cluster rows are measured; organism rows are models (evidence S). Each organism is
labelled by the one rule: no LOSS of more than 2% on any measure (CPU and host load shown, not judged), and a gain counts only
where energy or the bill is lower with an interval wholly below zero.


### Result: the six organisms with the real cluster inside (run 37217362568, commit `d81d5ee`)

Thirty jobs, six organisms times five paired repetitions, native against native with Omni-Compass on top (compass law),
every arm valid, every simulated knob handed back. Full report `results/live/SIX_KUBE.md`; raw files
`results/live/raw/run-37217362568/`.

On the real cluster, in every organism, native + Omni was late less often and answered faster:

| Organism | Time over the line, native → Omni | p95, native → Omni (ms) | Failed requests, native → Omni |
|---|---|---|---|
| Compute / AI / Cloud | 41.0% → 26.7% (lower, -35%) | 3,967 → 2,653 (lower, -33%, inside the noise) | 14.9% → 13.3% |
| Physics / Robotics / Autonomous | 28.4% → 15.5% (lower, -45%) | 2,440 → 1,767 (lower, -28%) | 5.7% → 5.0% |
| Energy / Facility / Industrial | 21.6% → 10.4% (lower, -52%) | 1,951 → 1,482 (lower, -24%) | 3.8% → 3.2% |
| Distribution / Specialized | 40.7% → 21.1% (lower, -48%) | 2,830 → 1,943 (lower, -31%) | 11.1% → 9.3% |
| The whole tower (656) | 25.8% → 14.7% (lower, -43%, inside the noise) | 2,085 → 1,247 (lower, -40%, inside the noise) | 12.8% → 9.1% |
| The four stacked (1,226) | 55.6% → 43.0% (lower, -23%) | 3,703 → 2,803 (lower, -24%) | 31.7% → 27.6% |

No measure read LOSS beyond the noise in any organism. Energy (declared model) and CPU moved by under 3%, lower
with Omni in every organism. The modelled organisms around the cluster: work the same, energy 0.1-0.2% lower, time over
the line 0.5-2% lower, in every organism (evidence S).

Read with it: at a peak of six open-loop load generators the 4-core runner is past what the six workers can serve in
both arms (native late 22-56% of the time, 4-32% of requests failed; host 65-91% busy). The comparison is fair (same
load, same seed, same runner per pair); the absolute levels are an overloaded cluster, and a lower `load_max` is the
setting for a cluster inside its capacity.


## More work, faster, on fewer machines, with less energy: all four in one run (written before its run, 2026-10-04)

The four gains so far come from different tests: more work on the same machines (the capacity test, +48.1%), the same
work faster on fewer machines (sets 22-27), energy equal or lower in each. This test measures all four in one run.

Design: `benchmark-reps`, ten paired repetitions, arms native and compass (rule 4), order rotated, fresh six-worker kind
cluster per arm, open-loop load rising and then falling, `load_steps` 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1, 180 s a step
(2,700 measured seconds). The rise is the capacity test (`tools/live_reps.py capacity`, read on the way up to the
peak: the highest load step at which no more than 5% of response samples are over the 500 ms line or failed, every
lower step too). The fall is where machines are no longer needed and can be handed back. Over the whole window:
p95 response time, worker machines in service, energy (declared model; on kind it is not a meter), CPU with Omni's own.

Reported for each, native + Omni against native, paired, with the 95% interval and read in words (GAIN, EVEN or LOSS):
work (capacity, requests a second inside the line), speed (p95), machines (worker machines in service, mean), energy.

## The Omni index: one number for more for the same, or the same for less (written before its first use, 2026-10-04)

Each measure is turned into a ratio oriented so that above 1 is a GAIN for Omni-Compass:

- work: work with Omni / work native (capacity, requests served, work done)
- speed: p95 native / p95 with Omni (a lower response time is faster)
- machines: machines native / machines with Omni (in service, or billed machine-hours)
- energy: energy native / energy with Omni (or the bill)

The index of one test is the geometric mean of its oriented ratios, minus one, in percent: +30% reads "30% more for
the same, or the same for 30% less", across work, speed, machines and energy together. A measure a test did not take is
left out of that test, never filled in. A measure inside the noise is counted at its mean and flagged. A category
(real Kubernetes on GitHub, Azure, the card, the eight cards, the modelled muscles) is the geometric mean of its tests;
the headline is the geometric mean of the real categories, each weighted the same; the modelled muscles are shown
beside it, never inside it. Computed by `tools/omni_index.py` from each test's own paired results; nothing is typed in.

**The service reading, a second reading declared 2026-10-09 (the first unchanged).** The founder asked what a cache is
for. Redis is bought for speed and spends memory to deliver it; the index above counts that memory as a cost at the same
weight as the speed it buys, so the Redis category reads −24.9% while its work inside the line and its hit rate read
GAIN in all three of our runs in every run. The question is fair, and the answer is a second reading beside the first, never a change
to the first: the same tests, the same three-run rule, scored on the service the stack is bought for, **work and speed
only**, with the resources it spent or saved (machines, energy, memory, connections, consumers) shown beside it and not
scored. It is computed for every test alike by the same tool (`service_pct`, `service_headline_pct`), never for one
stack, and printed in the same tables as a second column; the resource reading above stays the headline this program
preregistered. The two readings say different true things: where the governor buys service with a resource (Redis's
memory ceiling, Kafka's consumers) the service reading is higher and the resource reading says what it cost; where it
gives a resource back for the same service (the database pools and caches) the service reading is nothing and the
resource reading carries the gain. On the day it was declared the service reading stood at +71.8% against the resource
reading's +20.5% (Kubernetes +83.2%, Kafka +1,192.8%, Redis +8.8%, the three database stacks exactly nothing; on the sets of
10 October, the brain's verdict on every stack knob, the two readings stand at +10.7% and +4.8%); Kafka's
hundredfold speed ratio is why the service headline is large, and the category table is where a reader sees it. A
loss in all three of our runs in work or speed counts against Omni in both readings; neither hides one.

**The wiring verdicts, declared 2026-10-09 (a reading of the tables, not a change to any rule).** The founder's order of
the same day: Omni need not be wired into every muscle; where it cannot beat native, the muscle stays native and Omni only
reads it, one wire out and no wire in. `tools/wiring_verdicts.py` reads every three-run table, the simulator tables, the
realms table and the organism tables by one rule into three words per knob and case: **write** (a judged gauge GAIN in all three of our runs, none LOSS or power given in all three of our runs), **watch** (nothing GAIN in all three of our runs, whether inside the noise, the runs
disagreeing, or a loss with nothing against it) and **operator's choice** (gains and losses both the same in all three of our runs, shown with both
readings of the index). Rows shown and not judged never count. Nothing is typed in, and `verify.py` fails if the page
(`docs/WIRING_VERDICTS.md`) differs from what the tables give. The verdicts change what an operator connects, never the
engine (Omni v3) or any rule written here, and every test on this page is read as before.


## Demand that wanders: up, spike, partway down, back up, down to idle (written before its run, 2026-10-04)

Real demand does not rise once and fall once. It climbs, spikes, eases part way, climbs again and finally settles to
idle. This test drives that shape and asks whether machines follow it in order: the emptiest machine idles first on the
way down (powered and Ready at its floor, never off), the warm machines wake first on the way up (no boot), one machine
always in service for the first burst (`scripts/kind_nodepool.sh`).

Design as the all-four test (ten pairs, native and compass, open-loop load, fresh six-worker kind cluster per arm), with
`load_steps` 1 2 3 2 3 4 5 6 5 3 5 6 5 4 3 2 3 2 1 1 (twenty steps of 135 s, 2,700 measured seconds), the same steps in
every arm. Reported, native + Omni against native, paired with the 95% interval and read in words: time over the 500 ms
line, failed requests, p95, worker machines in service (and its trace step by step), energy (declared model), CPU with
Omni's own, pods started. No capacity is read (the load does not only rise).


### Amendment to the wandering test, written before its run (2026-10-04)

The founder's two rules for real traffic, adopted before any result of the wandering test: traffic moves one step at a
time, up or down, never skipping (it may go 1 2 1 2 1 2 if it never needs 3); and machines never go below two, so two
are always in service, ready for a spike, with no ceiling but the machines the cluster has. The run started with the
earlier steps (which jumped 5 to 3 and 3 to 5) was cancelled before it finished; none of it is reported.

From this amendment: the machine floor is two in every arm Omni-Compass governs (`MIN_NODES`, default 2: the
controller's `--min-nodes`, the actuator `scripts/kind_nodepool.sh`, and every benchmark script). Native's own floor is
the cluster's: kind keeps all six workers. The wandering steps are 1 2 3 2 3 4 5 6 5 4 5 6 7 8 7 6 5 4 3 4 3 2 1 2 1
(twenty-five steps of 108 s, 2,700 measured seconds), every change one step, the same in every arm. Everything else
is as written above.


### Result: all four in one run (run 37226863122)

Ten paired repetitions, every arm valid. **Work +29.3%** (capacity 24.6 to 31.8 requests a second inside the line,
interval +5.4 to +9.0), **p95 -62.3%** (685.8 to 258.3 ms), time over the line -40.9%, failed requests -12.1%,
**machines in service -3.6%**, **energy -0.3%** (declared model), CPU with Omni's own -1.9%: each proven. No measure
power given beyond the noise (pending pod-minutes +19.6% and pods started +4.0%, both inside the noise). This run's machine
floor was one; the floor of two was adopted after it started. Report `results/live/ALL_FOUR.md`; raw files
`results/live/raw/run-37226863122/`; the Omni index updated (`results/OMNI_INDEX.md`).


### The boundary is the band, not a machine held out (written 2026-10-04, for every run started after it)

Holding one whole machine back as a ceiling was considered and set aside the same day: it takes one of the machines
away from the work. Every machine is usable (Omni-Compass's most is every machine that exists); the floor of two stays
for quiet times. The protection against running into the wall is the band inside every machine: capacity is added at
95% of the response line, before the line is reached, and a machine goes back only if the ones left still run at or
under the engine's utilisation target. An operator who wants whole machines held back can set `NODE_CUSHION` (off by
default). The wandering run under way (37235231963) uses every machine, as every run after it does.


## The six organisms at every size, the real cluster inside (written before its run, 2026-10-04)

The same six organisms, each native against native with Omni-Compass on top, at the sizes of the model grid: 10, 100
and 1,000 copies of the organism governed together on one clock, the one real cluster inside as one more muscle
(`tools/run_kil.py --scale`; size 1 is the run already recorded, `results/live/SIX_KUBE.md`). Workflow `six-kube`, one
job per organism, size and repetition, both arms on one runner, order rotated, fresh six-worker kind cluster per arm.

- Repetitions: 5 at 10 and 100 copies, 3 at 1,000. Measured window: 960 s at 10 copies, 1,440 s at 100, 2,880 s at
  1,000 (240 organism steps of 4, 6 and 12 s: a step at least 1.5 times what the organism takes to compute on this
  runner, measured: 0.18 s at 10 copies of the four stacked, 2.4 s at 100).
- The organism is built before the window opens (`organism.ready`); the window opens the moment it is built
  (`organism.go`), so the cluster and the organism start on one clock however long the build takes. If the organism
  falls behind its own clock, `organism.json` records by how much (`behind_s`).
- Machine floor two, every machine usable (the founder's rules above), open-loop load, peak six generators.
- Declared before the run: 1,000 copies of the whole tower (656,000 modelled muscles) and of the four stacked (1.2
  million) need about 6 and 11 GB of memory beside the cluster, past what one GitHub runner holds. They are run; if a
  runner cannot hold them, the job's failure is reported as that, never as a result.

Reported in `SIX_KUBE.md` by organism and size, every gauge paired against native with its 95% interval and read in
words.

The run dimension of the model grid (1, 10, 100, 1,000 runs) is a count of seeds; on the real cluster each repetition
is a real paired run of an hour or more, so the real cluster carries the repetitions above, and the model grid carries
1 to 1,000 runs.


### The two organisms too big for a GitHub runner: a larger rented machine (written before their run, 2026-10-05)

1,000 copies of the whole tower and of the four stacked run on a larger rented machine, the same test otherwise:
workflow `big-organism` rents one Azure Standard_D8s_v4 (8 vCPU, 32 GiB) per repetition, runs `scripts/kind_paired.sh`
on it (native against native with Omni-Compass on top, fresh six-worker kind cluster per arm, 2,880 measured seconds,
the organism at 1,000 copies with the real cluster inside), copies every file back and deletes the machine whatever
happens. Three paired repetitions per organism, two machines at a time. Its results join `SIX_KUBE.md` at 1,000 copies;
the same cells from GitHub runners count only if the runner held them.

*Result on Omni v3 (`results/live/V3_BIG_ORGANISM.md`, both organisms, written 9 October after the second collect).* The
machines were rented one at a time through `big-organism-detached` with a 10,800 s window an arm (the 2,880 s window of the
v1 runs put the compass arm off the clock; the clock rule and the longer window are declared in the robustness and v3
notes). The four stacked: three repetitions over 29 hours (collected by run 37754612102), p95 2,882 → 150 ms, time over the
line 51% → 0, failed requests 0.14% → 0, machines 6 in both arms, both arms 22 s behind the window. The whole tower: three
repetitions over 25 hours (started by run 37756284680, collected by run 37945866426), p95 6,690 → 160 ms, p99 9,068 → 187
ms, time over the line 76% → 0, failed requests 4.8% → 0, machines 6 in both arms, both arms 14 s behind the window. Every
cluster row that moved is clear of zero with three pairs; the organisms' own model rows are shown beside them and never
enter the index; the rounding-level model work loss reads LOSS by rule in both. Six repetitions, six on the clock.


### The burst bill test on Azure: two native arms lost to the harness, and the fix (2026-10-05)

Repetitions 2 and 3 of the burst bill test (run 37216328055) each lost their native arm (Kubernetes alone) at the
same moment: the load step from one generator to six. Native's two work machines were full, answers timed out, and the
API server stopped answering for minutes. The capture script ran with stop-on-first-error, so one unanswered reading
ended the recording, and the load schedule stopped at its next unanswered scale; the arm failed its checks and was
marked invalid. The Omni-Compass arms of the same repetitions ran every step. Those two arms are not counted.

That is a fault of the harness, and it threw away exactly the moments a cluster struggles. Fixed: a reading the API
server does not answer is logged (`capture.csv.errors`) and skipped, and the recording goes on; a scale the API server
does not answer is tried again, then logged, and the schedule goes on (`fleet/capture/kube_capture.sh`,
`scripts/kind_bench.sh`, `tools/run_kil.py`). Repetitions 4 and 5 started on the earlier code. When the run ends, three
more repetitions of the same test run on the fixed code, and the report counts every valid pair and names every
invalid arm with its cause.


## Amendment 6: a pinned gauge is not a steady demand (written before its run, 2026-10-05)

The wandering test (run 37235231963, ten pairs) gave native + Omni-Compass p95 -54%, time over the line -38%, failed
requests -14%, energy -0.3% and CPU -2%, each proven, and 1.5 more pod starts a run (+36%, proven). The founder holds
that result back until the cause is fixed and the test is run again.

The cause, read from the run's own audit (repetition 4, 12 pod starts against native's 7): at 972 s the load eased
from five generators to four, rule 3 found the demand steady, and the target was raised (50 to 190: fewer pods); the
load then climbed back to eight and the pods were started again. The demand was not steady. The autoscaler stood at its
replica cap, every pod as busy as it could be, so the reading (utilisation times pods) could not rise however much the
load did: a pinned gauge reads flat.

Rule 5 (amends rule 3): a decision at which the autoscaler stands at its replica cap marks the window pinned; a window
that touched the cap is not steady, so no raise of the target, and no return of a raised cap, until one whole
autoscaler window after the cap was last touched (`omni_controller/controller.py _steady`, `self.pinned`; tested in
`tests/test_compass_controller.py`). Nothing else changes.

The rerun: the same wandering test (ten pairs, native and compass, `load_steps` 1 2 3 2 3 4 5 6 5 4 5 6 7 8 7 6 5 4 3 4 3
2 1 2 1, 2,700 s, floor two, every machine usable). Reported in full, every gauge read in words; the first run is kept
in its raw files and named beside the rerun.


## Amendment 7: coasting, off the gas but still in gear (written before its run, 2026-10-05)

The founder's picture: a car in drive. At idle it creeps, ready (the floor of two machines). On the gas it speeds up at
once (more pods, machines woken, no boot). Off the gas it coasts down gradually toward idle; it does not drop into
neutral. The brake is for stopping (the reset hands everything back at once).

Rule 6: a raise of the HPA target (toward fewer pods) moves by at most `--coast-step` points of utilisation in one
autoscaler window (default 25, `COAST_STEP`; 0 turns it off). The first wandering run raised the target 50 to 190 in
one move; under rule 6 the same raise takes several calm windows (50, 75, 100, ...). A demand that comes back part way
finds the pods still running and is met at once by a lower target, with no pod started again. A lower target (more
pods) is never limited: the gas is always immediate. Rules 5 and 6 together: never ease off while the gauge is pinned,
and then ease off a step at a time (`omni_controller/controller.py`; tested in `tests/test_convey.py`).

The rerun with rule 5 alone (run 37255770249) was stopped before it finished, to run the test once with both rules;
none of it is reported. The rerun: the wandering test as written in amendment 6.


## Amendment 8: cruise and the emergency brake, and the batch test (written before its run, 2026-10-05)

The founder's driving modes: off (native alone), watching (Omni-Compass reads, writes nothing), autopilot (gas, brake,
idle), and two more for work that comes as a pile:

- **Rule 7, cruise:** work waiting for a place (pods pending) two decisions in a row puts every machine in service
  (`--max-nodes`), and they stay in service, without second-guessing, until the line has been empty and nothing is
  scaling up for two decisions (`--cruise-after`, default 2; 0 turns it off).
- **Rule 8, the emergency brake:** nothing waiting, no response-time breach, nothing scaling up, and the sensed
  services' demand at or under 0.05 of one pod's request (`--brake-demand`): the machines go straight to the floor
  (two) in one move. Every check of the release gate still holds (every sense live, the last command landed, the
  machines left at or under the utilisation target) except one machine per decision. Never below the floor.
- Tested through the live controller: `tests/test_cruise_idle.py` (in `verify.py`).

**The batch test:** a queue of jobs on the six-worker kind cluster (`WORKLOAD=batch`, `deploy/kind/batch-jobs.yaml`):
one Kubernetes Job of 240 pods, 60 at a time (more than the workers hold, so work waits for a place), each hashing
3,000 MB (real CPU work, identical in every arm), opened with the measured window (1,500 s); the service's load
generator stands at zero. Ten pairs, native and compass, order rotated. Reported, paired with the 95% interval and read in
words: how long the queue took to finish, the worker machines in service after it finished, machines in service and
energy over the whole window, CPU with Omni-Compass's own, pods started. Cruise must not slow the queue; the brake must
show in the machines held after it.

## The frozen engine (rules 1-8, commit 353903683009): the fault and fairness results (2026-10-05)

Both tests ran again with nothing changed but the engine: ten pairs each, native and omni, order rotated.

- The fault test (GitHub run 37262797634, `results/live/FAULTS.md`): a proven GAIN on p95 (−60.1%), mean response
  (−34.5%), time over the line (−22.6%) and pending pods (−76.5%). No LOSS beyond the noise. Recovery
  after the fault, paired means: machine down 42 s against 70 s, a blind probe 54 s against 66 s, a runaway pod 98 s
  against 105 s, a spike 266 s against 267 s.
- The fairness test (GitHub run 37262799317, `results/live/FAIRNESS.md`): a proven GAIN on mean response (−15.0%).
  No LOSS beyond the noise, the neighbour's app included.

These replace the earlier engine's fault and fairness sections of `results/live/AMENDMENT_3_RUNS.md` in the Omni index.
That file stays as first measured.

The Azure burst bill test and the big organisms, running them (2026-10-05): Azure no longer offers this subscription
Standard_D2s_v5 in eastus, so AKS workers are Standard_D2s_v4 (2 vCPU, 8 GiB, the same list price, USD 0.096 an
hour). Both arms use the same size; the steady-load result of record (`results/live/AKS_BILL.md`) stays as measured on
D2s_v5. The big-organism machine failed while seven kind nodes joined (kubelet-start). Fresh Ubuntu ships too few
inotify watchers for that; the rented machine now raises them as kind's own documentation advises. Neither change
touches the controller.

## Amendment 9: idle read from the autoscaler's floor, and the batch test again (written before its run, 2026-10-05)

The batch test on the frozen engine (GitHub run 37262795697) showed rule 8 late. The queue emptied 664 s into the
window, but the emergency brake fired at 1,574 s. The reason: a served service is never at zero CPU. The response
probe alone keeps one pod at about 10% of its request, which reads as demand 0.10, above the brake's 0.05. Rule 8 now
also counts a service as idle when its autoscaler stands at its least pods (`minReplicas`), wants no more, and runs at
no more than half its target utilisation. Every other condition of rule 8 holds as before: nothing waiting, no breach,
nothing scaling up, the release gate, every sense live, the last command landed, and the machines left carrying what
runs now under the utilisation target. Test: `tests/test_cruise_idle.py` (it lifts to the idle floor, and it does not
lift there above the floor or while busy).

Effect on what was already measured: none. The steady, fault, fairness, wandering and all-four runs on the frozen engine
had the service at one pod with nothing waiting in 0 of 5,102 readings, so the amended rule could not have fired in any
of them.

Three of the ten batch pairs stopped, all in the omni arm. The API server answered 500 under the batch load (60 jobs
asking for 30 cores on a 4-core runner), and the recording script ended on an unanswered `kubectl top nodes`. That is a
harness fault: a reading the API server does not answer is now logged and skipped, and the end-of-window reads are tried
again. The batch test runs again, ten pairs, on this engine, with the design unchanged.

## Amendment 10: two rows read for what they measure (written after the frozen-engine runs were seen, 2026-10-05)

Disclosed: this is a change in how two rows are read, made after the steady, wandering and all-four results were seen.
Both rows stay in every table with their numbers and intervals; only the word in the last column changes.

- **Pending pods.** The row counts pods pending in each 15 s snapshot. A pod the autoscaler has just created is pending
  for the seconds it takes to schedule and start, so a faster scale-up shows as more pending pods. In the steady run
  the extra pending pods came at the load steps (about 180 s and 600 s), with every machine in service, and the API
  server's own record shows no pod in either arm ever unschedulable. The row is now shown, not judged. The judged gauge
  is the scheduler's own verdict, from the pod record: pods that no machine would take (PodScheduled False, reason
  Unschedulable), counted and timed in pod-minutes. In the five frozen-engine runs it is 0 in every arm.
- **Energy per core-hour.** It is energy divided by CPU used. CPU used is shown, not judged (more or less is not toward an aim
  by itself), so a ratio over it is not judged either. Energy itself stays judged.

Nothing else changes. With these readings, no row of the steady, wandering, all-four, fault or fairness results is
behind native beyond the noise.

## Amendment 11: the burst bill test sized to what the service can serve, and rounding read as the same (2026-10-05)

Disclosed: written after three repetitions of the burst test at `1 6 1 8 1 6` were seen. In them about 41% of requests
failed in both arms. The service's own autoscaler sat pinned at its cap of 10 pods, and 6 and 8 load generators (36
and 48 requests a second) ask more than 10 pods can serve, whatever the machines. A test where neither arm can do the
work cannot show a difference. The burst test runs at `1 3 1 4 1 3`: the peak is one step above the steady test's peak
of 3, and inside what the capped service can serve. Everything else is as preregistered: five repetitions,
1,800 measured seconds, Azure's autoscaler underneath, the bill metered every 15 s, native against compass. The three
repetitions at the old steps stay in the archive (`results/live/raw/run-37294579764/`) and are reported as the reason
for this amendment, not as a result.

In every table a paired change under one part in a million of the value reads "same", the number still shown
(`SAME_REL`, `docs/MECHANISM_OF_ACTION.md` 9.5).

## Amendment 12: cruise steps back, and the organism's start file (written before the batch rerun, 2026-10-05)

The batch rerun on amendment 9 (GitHub run 37275371557, ten valid pairs) gave machines -16.9%, -27.2% once the queue
was done, and energy -11.6% on the standby model. The queue finished 10 s later (584 s against 594 s, +1.8%). Omni held
every machine in service throughout, so the time went elsewhere: every five seconds the floor step read every pod (240
batch pods), every node, node metrics and every HPA, on the one 4-core runner the queue was using. In cruise every
machine is already in service, so those reads can change no action. From this amendment, while cruising the floor step
makes no read and no write, and the service's target stays at the operator's own (`docs/MECHANISM_OF_ACTION.md` 9.3;
`tests/test_compass_controller.py`). Cruise never engaged in the steady, wandering, all-four, fault or fairness runs,
so this changes nothing there. The batch test runs again, ten pairs, design unchanged.

The organism with the real cluster inside waits for a start file. One repetition of six-kube (the four stacked, 1 copy,
repetition 2) read that file in the instant it existed but was still empty, and stopped. The file is now written whole
or not at all, and read only once it holds a number. That repetition is reported as stopped, never counted.

Also found and fixed on 2026-10-05, from the compass rename: each modelled muscle's compass was made fresh at every
decision (`docs/MECHANISM_OF_ACTION.md` 9.1). That touched the modelled organism rows of the runs started after the rename
(six-kube 37280090832, big organism 37287311224); their cluster rows are unaffected. The organism runs go again on the
fixed code.

The batch test on amendment 12 (GitHub run 37344765837, ten pairs, `results/live/BATCH.md`): machines in service -20.7%,
-32.4% once the queue was done, energy -14.3% on the standby model, mean response -11.7%, all proven. The queue finished
+1.1% later, inside the noise (it was +1.8% and proven before cruise stepped back). No pod was left without a machine.
No LOSS beyond the noise.

## The fleet that can show one machine: Azure at 11 and 15 workers (written before its run, 2026-10-07)

The Azure runs so far used a work pool of 1 to 4 machines. One machine is a quarter to a half of that fleet, and the
app's replica ceiling (10 pods of 200m, about one worker's worth) kept Azure's autoscaler at about 1.9 workers in both
arms, so nothing under a quarter of the fleet could show. The steady run on v1 (5 pairs) read even on every gauge. That
is a statement about the lever, not about the law. This run makes the lever big enough to see one machine.

- **Fleet.** The subscription allows 200 vCPUs in eastus but 10 vCPUs in each machine family (every family's request to
  raise it was refused through the API on 2026-10-07: the subscription's terms), so one family gives at most 5 machines.
  The fleet is therefore several work pools, one 2-vCPU machine family each, each capped at what its family allows:
  `worker_pools` = `Standard_D2s_v4:4,Standard_D2as_v4:5,Standard_D2_v4:5,Standard_D2a_v4:5,Standard_D2ds_v4:5,Standard_D2s_v3:5,Standard_E2s_v4:5,Standard_E2as_v4:5`,
  39 workers (the DSv4 family also carries the system machine, hence 4). Every pool carries the label `omni-role=work`,
  the worker selector in both arms; the first pool keeps one machine, the others may scale to zero; every pool starts
  full and Azure's own autoscaler trims, as before. One machine is then 2.6% of the fleet. Mixed machine families are how
  real cloud fleets run; the bill is each pool's machine-hours at its own list price (`pool_prices`), Azure's own count
  every 15 s. The same autoscaler profile, a fresh cluster per arm. (Written first for 11 then 15 workers of one family;
  the family allowance made that impossible and this replaces it before any such run.)
- **Ceiling.** `hpa_max` = 9 × workers = 351 at 39 workers: nine 200m pods fit one 2-vCPU worker, so the fleet can
  fill. The same ceiling in every arm; the restore checks expect it back untouched.
- **Load.** The load generator's replica steps scale with the fleet, the same in every arm (one load replica drove
  about five pods at 50% on the 4-worker runs). Steady: `18 35 53 18 35 18` over 900 s at 39 workers (the peak asks
  for about 265 pods, thirty workers' worth). Burst: `11 35 11 53 11 35` over 1,800 s (the 4-worker burst was
  `1 3 1 4 1 3`). A fleet of another size scales the steps by workers/39, rounded.
- **Everything else as preregistered**: native (Azure's autoscaler alone) against omni (Omni-Compass on top of it,
  rule 4 on the node pool, the HPA target inside its range, handed back at 90% of the window), 5 paired repetitions,
  order rotated, the bill Azure's own machine count every 15 s at list price, the reading by `tools/live_reps.py`'s
  paired interval, every gauge reported. Engine: Omni v3 first (the newest), v1 after if the credits allow.
- **What it can say.** Lower, clear of the noise, in bill or response time: Omni has value on the managed service when
  the fleet is big enough to see a machine. Even again: Omni's value there is nil at this size too, and that is the
  reading. Higher: our own wiring is suspected first, found, fixed, and the run is made again.
- **Cost.** About $8 for the steady set and $15 for the burst set at 15 workers, at list price.
- **Amendment (2026-10-07 07:18 UTC, before the counted run).** The first dispatch at 39 workers was refused by Azure on
  every repetition: the DASv4 family had 2 vCPUs left, not 10, because the rented machine running the four stacked at
  1,000 copies (`big-organism-detached`, a Standard_D8as_v4) holds 8 of that family's 10 in the same subscription. The
  run was cancelled (no arm ran) and dispatched again at **35 workers**: `Standard_D2as_v4:1`, the other seven pools as
  above; `hpa_max` 315; the steps scaled by 35/39 as this section says, steady `16 31 48 16 31 16`, burst
  `10 31 10 48 10 31`. One machine is 2.9% of this fleet. Nothing else changes. The 39-worker fleet stands for the runs
  made after the detached machine is deleted.
- **Amendment 2 (2026-10-07 09:40 UTC, before the counted run).** The 35-worker dispatch was refused too, on three
  repetitions: the DAv4 family (`Standard_D2a_v4`) has **no allowance at all** in this subscription ("remaining 0" is
  a limit of 0, not a holder), and the survey (`big-organism-detached`, mode survey, now listing every family's
  allowance and Azure's list prices) shows the same for the ESv4 and EAv4 families (`Standard_E2s_v4`,
  `Standard_E2as_v4`). Three of the eight pools could never be built. The fleet is rebuilt from families the survey
  shows allowed (10 vCPUs each) and offered in eastus: `Standard_D2s_v4:4, Standard_D2as_v4:1, Standard_D2_v4:5,
  Standard_D2ds_v4:5, Standard_D2d_v4:5, Standard_D2s_v3:5, Standard_D2as_v7:5, Standard_D2ads_v7:5, Standard_D2als_v7:5,
  Standard_D2alds_v7:5`: **45 workers** of ten families (one machine 2.2% of the fleet); `hpa_max` 405; the steps
  scaled by 45/39, steady `21 40 61 21 40 21`, burst `13 40 13 61 13 40`. List prices from Azure's own price API
  (Linux, pay as you go, eastus, USD a machine-hour): D2s_v4 0.096, D2as_v4 0.096, D2_v4 0.096, D2ds_v4 0.113, D2d_v4
  0.113, D2s_v3 0.096, D2as_v7 0.0908, D2ads_v7 0.114, D2als_v7 0.0804, D2alds_v7 0.0952 (the 0.086 used for D2as_v4
  in the refused dispatches was wrong; no bill was ever made with it). `scripts/aks_paired.sh` now checks every pool's
  size and family allowance before anything is built, so a refusal costs a minute, not a repetition. Nothing else
  changes.
- **Amendment 3 (2026-10-07 16:21 UTC, before the counted run).** The pre-flight of the 45-worker dispatch (run
  37602951929) found `Standard_D2s_v3` not offered to this subscription in eastus and stopped every repetition in a
  minute, nothing built, nothing billed; the nine other pools passed. That pool is dropped: **40 workers** of nine
  families (one machine 2.5% of the fleet), `hpa_max` 360, the steps scaled by 40/39, steady `18 36 54 18 36 18`,
  burst `11 36 11 54 11 36`, the pools' prices as in amendment 2. Nothing else changes.
- **Amendment 4 (2026-10-07 20:25 UTC, before the counted run).** Two dispatches of the 40-worker fleet (runs 37651333302
  and 37676237815) were refused by Azure itself on every repetition for four hours: "creating a new cluster is unavailable
  at this time in region eastus" (`AKSCapacityHeavyUsage`, Azure's own capacity for new clusters, not the subscription's
  allowance; the pre-flight passed each time, no arm ran, nothing was billed). Microsoft's remedy is another region, other
  cluster settings, or a retry; this subscription has more than 10 cores only in eastus. The clusters are therefore made on
  the **standard control-plane tier** (`tier` input, `AKS_TIER`) instead of the free tier, about $0.10 an hour a cluster,
  which is not in the bill (the bill counts worker machines only, in both arms alike) and changes nothing the workers or the
  autoscaler do. If the standard tier is refused too, the run waits for Azure. Nothing else changes.
- **Amendment 5 (2026-10-08 03:55 UTC, before the counted run).** The standard-tier dispatch (run 37703460186) was refused
  by Azure's own cluster capacity in eastus on all five repetitions too, over three hours (23:39 to 02:48 UTC), the same
  `AKSCapacityHeavyUsage` on each: 22 refusals in eleven hours across four dispatches, the pre-flight passing each time, no arm
  run, nothing billed but the resource groups' minutes. The fleet is dispatched again unchanged; it runs when the region
  admits a cluster. The alternative, a second region, needs the subscription's regional vCPU allowance raised there, which
  only the account holder can request in the portal. Nothing else changes.
- **Amendment 6 (2026-10-08 05:00 UTC, before the counted run).** The fifth dispatch (run 37724667075) was refused on its
  first repetition after a forty-minute wait, the same `AKSCapacityHeavyUsage` in eastus, the twenty-third refusal; the
  pre-flight passed, no arm ran. We cancelled the run ourselves at that point to weigh a second region, and the answer is in
  the 6 October survey already on record (`big-organism-detached`, mode survey): eastus allows this subscription 32 vCPUs
  and the v4 machine sizes, and every other region allows 10 vCPUs in all, which is five two-core workers, not a fleet of
  forty. No other region can take this fleet until the account holder raises its allowance there. The fleet is therefore
  dispatched a sixth time in eastus, unchanged in every input, and runs when the region admits a cluster. The cancellation
  and the reason are recorded here so the count of dispatches reads right. Nothing else changes.
- **Amendment 7 (2026-10-08 08:30 UTC, before the counted run).** The sixth dispatch (run 37730249970) was refused on all
  five repetitions too, the same `AKSCapacityHeavyUsage` in eastus, over three and a half hours (05:01 to 08:26 UTC): 29
  refusals in sixteen hours across six dispatches, the pre-flight passing each time, no arm run, nothing billed. The fleet
  is dispatched a seventh time, unchanged; nothing else changes. Each refused repetition costs GitHub runner minutes only.
- **Amendment 8 (2026-10-08 11:50 UTC, before the counted run).** The seventh dispatch (run 37750047768, 08:28 to 11:33 UTC)
  ran no arm either, but not for one reason. Repetitions 1 to 3 were refused as before (`AKSCapacityHeavyUsage` in eastus, the
  pre-flight passing each time): 32 refusals across seven dispatches. Repetitions 4 and 5 never reached Azure's cluster
  service: the pre-flight itself found only 2 of the 10 vCPUs free in two of the nine families (`standardDSv4Family`,
  `StandardDasv7Family`), and the fleet is dispatched only when every family has room, so it stopped with nothing built and
  nothing billed. An inventory of the subscription (`.github/workflows/azure-inventory.yml`, run 37773586107, 11:58 UTC)
  answered it: the subscription holds exactly four machines, all ours and all running, and no cluster, scale set or group
  left behind by any earlier repetition. The holders are the three machines of the 24-hour robustness run
  (`docs/ROBUSTNESS_PREREGISTRATION.md`, scenario 2b): the detached start job, which tries the size it is given and falls back
  through the eight-core sizes it may rent when the allowance refuses it (the four-core size asked for was refused because the
  tower's machine held its family's allowance), rented `Standard_D8as_v7`, `Standard_D8s_v7` and `Standard_D8s_v4`, eight vCPUs
  in each of the Dasv7, Dsv7 and DSv4 families, where the allowance is 10, and the fleet's pre-flight (which asks every one of
  its nine families for 10 free vCPUs) found 2. The tower's `Standard_D8as_v4` holds 8 of the DASv4 family's 10 the same way.
  Nothing is deleted. The eighth dispatch, unchanged in every input, follows the collect that deletes the 24-hour machines
  (each machine runs two arms of 86,400 s one after the other, so about 2026-10-10 12:00 UTC, and by their 60-hour limit at the
  latest); until then the fleet cannot pass its own pre-flight, and that is the pre-flight doing its job.


## The grid with the real cluster inside: protocol 2 (amendment, 2026-10-12, before the counted runs)

The grid's runs with the real cluster inside (workflow `six-kube`, every organism at 1, 10, 100 and 1,000 copies, every
size to 1,000 repetitions; `scripts/dispatch_grid.py`) began on the max at 06:56 UTC. By 15:00 UTC three causes had marked
repetitions invalid or ended jobs, all in the test rig and none in the engine (omni-v5, unchanged):

1. **The governor below the rig.** The four stacked at 100 copies, repetition 3 (job 114726933444): the governor made 47
   of its 60 decisions by the end of its 3,600 s window, one every 78 s against its cadence of one a minute, and the run
   was invalid by the rule above (80%). The governor runs at the lowest CPU priority (nice 19) since live set 11, so that
   its own work never takes the service's place; the modelled organism, the heaviest process of the test rig on the
   runner (186,800 muscles), ran at normal priority (nice 0) in the same cgroup, where niceness ranks processes against
   each other: the rig outranked the governor and took its share. A second fault hid it: the bench's `wait` for the
   governor could not see it (the governor is started in a subshell: "wait: pid ... is not a child of this shell"), so
   the decisions were counted while a late governor was still deciding, and the job's own cleanup ended it.
2. **A refused download of kind.** `helm/kind-action` got no checksum file from GitHub ("no properly formatted checksum
   lines found"): the job ended before either arm ran.
3. **A refused download of the metrics-server manifest** (HTTP 504): the arm was marked invalid before its cluster was
   used; the other arm ran.

The amendment, protocol 2, carried in each run's name (`... window <s> protocol 2`):

- With the organism inside, the governor runs at the organism's own priority (nice 0): no part of the test rig outranks
  it. Without the organism it stays at nice 19, as before. The service is not touched either way: it runs inside the
  kind nodes' containers, each its own cgroup, where a process's niceness on the runner does not reach.
- The decisions that count for validity are those inside the measured window (`window_start.txt` to `window_end.txt`),
  with the mean time between them shown; before, every decision record up to the reset counted, the kill switch's own
  included. The 80% rule stands. This rule, the governor's stop below and the downloads tried again hold for every run of
  `scripts/kind_bench.sh` from the commit carrying this amendment (the live sets, the add-on and robustness tests too);
  the governor's priority changes only where the organism runs beside it.
- A governor still running when the window has ended is stopped through the master switch (it hands every setting back
  and exits) and watched by its pid until it is gone, before any check reads the cluster.
- kind v0.31.0 (whose own node image is Kubernetes v1.35.0) and kubectl v1.35.0 are pinned at the versions every run so
  far used; a refused download is tried again with pauses and checked against its published SHA-256
  (`scripts/kind_install.sh`); the metrics-server manifest likewise, once per machine, its pinned SHA-256 checked as
  before; a kind cluster that fails to come up is tried again twice. The rented machines install the same pinned
  versions (before: whatever was newest).

Counting. Every square with the cluster inside is filled on protocol 2 alone. The runs of protocol 1 (before this
amendment: 100 repetitions of every organism at 1 and at 10 copies, 10 at 100 and at 1,000, and the first ten repetitions
of the tower and of the four stacked at 1,000 copies on rented machines) are kept as they stand, archived and shown
beside as a check, never pooled with protocol 2. A repetition whose job fails is started again, up to three times, and
is paired within one run (native and Omni from the same run's files, `tools/six_kube_report.py`); one that fails three
times is listed, never dropped. The modelled grid (`six`) is not touched by this amendment. Cost: GitHub's machines are
free for this public repository (about 1,340 jobs run again, some seven hours of its queue); the first ten repetitions of
the two rented squares run again cost about $110 at list price, within the founder's budget.

**The founder's order, 12 October evening: 1, 10 and 100 only.** The grid with the real cluster inside is every organism
at 1, 10 and 100 copies, each to 100 repetitions; no 1,000 copies and no 1,000 repetitions, to cut the time and the bill.
Every square runs on GitHub's own machines; the rented machines of the 1,000-copy squares are stopped and their
repetitions (protocol 1) are kept as recorded, counted in no square. Protocol 2 and the counting rules above stand.


## The grid with the real cluster inside: protocol 3, and the live controller's ranges read live (amendment, 2026-10-13, before the counted runs)

**What the card version's grid showed.** On the card version (omni-v5, digest `5648f290`, protocol 2) native's own
numbers show the test machine running out as the copies grew: GitHub's four-core machine busy 69 to 75% at 1 copy, 82
to 85% at 10 and 87 to 91% at 100; native's own failed requests 6 to 10%, 22 to 31% and 32 to 43%; the cluster's CPU in
Omni-Compass's arm 0.7 to 1.7%, 1.2 to 2.5% and 4.0 to 7.0% under native's; and at 100 copies the four stacked off the
window's clock in 49 of 100 repetitions, the tower in 1 of 100. The cause is the test rig, not the engine: the model of
the organism (one process, at most one full core) and, in Omni-Compass's arm, Omni-Compass's math for every modelled
muscle ran on the same four cores as the seven kind nodes, so the heavier the model, the less CPU the real cluster got,
and more of it in Omni-Compass's arm, whose model also carries the math. The 100-copy squares measured the machine, not
the governor; they stay as recorded and count in no square of the next grid.

**Protocol 3**, carried in each run's name (`... window <s> protocol 3`):

- **The rig's own cores.** With the organism inside on kind, the model runs on the runner's last core (`taskset`) and
  the kind nodes on the others (`docker update --cpuset-cpus`), the same in both arms; the placement is written into
  each arm's preflight (`scripts/kind_bench.sh`). The governor keeps the organism's own priority (protocol 2) and is not
  placed. The cluster then has the same cores at every size and in both arms, and the model's weight shows only on its
  own clock.
- **The window from a measured step.** Before either arm, the heavier arm (Omni-Compass's: the model with the math for
  every modelled muscle) is timed on the core it will run on, six steps (`tools/run_kil.py --calibrate`), and the window
  is lengthened, never shortened, to 240 steps of its slowest measured step with a quarter to spare, rounded up to the
  minute (`scripts/kind_paired.sh`). Both arms use the one window; the measurement is written into each arm's preflight.
  The conductor's windows (`scripts/dispatch_grid.py`) stay the least a square is given.

**The live controller's ranges, read live** (Omni v5 amendment 5, digest `6093b2b88aa911b9`; `docs/OMNI_V5.md`): the
machine lever's top is the operator's `--max-nodes` where given, else every ready worker plus what the cluster's own
autoscaler may still add, else (where Omni-Compass resizes the pool with the operator's command) one under the first
count the pool refuses; cruise (rule 7) climbs toward that top one step a decision; the replica room (rule 5) is on by
default, its ceiling what the machines can hold of the service's pods, one pod under it, read live (`--replica-ceiling
N` the operator's own, 0 keeps the cap unmoved); at the max the power cap is never set under native (the capped pods get
their machine's idle CPU, the frequency ceiling and the GPU limit stay at their top). The fourth amendment's text above
stands as the record of what ran before.

**Counting.** Every square with the cluster inside is filled again on protocol 3 and the new engine alone: six
organisms at 1, 10 and 100 copies, each to 100 repetitions, on GitHub's own machines (free for this public repository);
the runs of protocols 1 and 2 are kept as recorded, archived and shown in history, never pooled with protocol 3. The
modelled grid (`six`) is run again on the new engine too (its numbers are expected to be identical: the modelled code is
unchanged but for comments, headers and one label's name), because no result is read across engine versions.

---
*Evaluation and Simulation use only. Copyright (c) 2026 The Omni-Compass LLC. Commercial use, commercialization or
monetization of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC.
All rights reserved. See `LICENSE` and `NOTICE` at the root of this repository. All patents, copyrights and trademarks
filed in the USA. www.omni-compass.com*


## The burst back at `1 6 1 8 1 6` (the founder's order, 2026-10-14, before the counted runs)

The founder's order of 14 October: the Azure burst runs at the steps first preregistered, `1 6 1 8 1 6`. Amendment 11
(5 October) had set `1 3 1 4 1 3` after three repetitions at `1 6 1 8 1 6` were seen; that amendment was ours, written
after the results, and it is withdrawn for every run from this date. The run on the card version's engine at
`1 3 1 4 1 3` (run 38455393389) was stopped after its second repetition and part of its third; its repetitions stay in
the record as runs of the withdrawn setting and are counted in no burst result. The burst starts again at
`1 6 1 8 1 6` (run 38500160429): five repetitions, 1,800 measured seconds, four workers of Standard_D2_v4 in eastus under
Azure's autoscaler, the bill metered every 15 s, native against omni, then B and C. Disclosed beside it: at these steps
in October's first runs about 41% of requests failed in both arms, because the service's own autoscaler was pinned at
its cap of 10 pods; the table shows what each arm served at the steps the founder set.

## Two more burst shapes on Azure (the founder's words, 2026-10-14, written before any run of either)

The founder's words of 14 October named two more shapes for the Azure burst: the steps `1 4 1 6 1 9`, and bursts that
nobody picks, from 1 to 9. Both run beside the burst at `1 6 1 8 1 6`, each reported as its own setting, never in its
place. Neither arm reads a schedule: the load generator alone steps through it (`scripts/kind_bench.sh`, the load
generator's replica count set at each step), identically in both arms, and the governor sees only what the cluster
shows (its processor use, the requests waiting, the response times), as in every burst run.

| Setting | Load-generator replicas per step | Steps | Measured window | Machines (queue) |
|---|---|---:|---:|---|
| Burst `1 4 1 6 1 9` | `1 4 1 6 1 9` | 6 of 300 s | 1,800 s | four workers of Standard_D2_v4, eastus (after the `1 6 1 8 1 6` set, in its queue) |
| The real day on 1 to 9 | `2 3 3 4 3 4 4 3 2 2 2 2 2 3 2 3 4 5 4 5 6 7 6 5` | 24 of 108 s | 2,592 s | four workers of Standard_D2s_v4, eastus (after the steady set, in its queue) |

- **The real day on 1 to 9.** The 24 hourly counts of submitted jobs on the first day of Google's public 2011 cluster
  trace, the counts already derived for the trace test (`results/traces/google2011/schedule.json`, every part named with
  its SHA-256), placed on 1 to 9 by the same min-max rule with half-up rounding (`python3 tools/trace_schedule.py --out
  results/traces/google2011_1to9 --load-max 9 --counts-from results/traces/google2011`; receipt
  `results/traces/google2011_1to9/schedule.json`), then stepped by the founder's rule for real traffic, one step a bin
  toward the trace's level, never skipping. The demand is the trace's, not ours. Disclosed: the day touches 9 for one
  hour only (hour 21), and under the one-step rule the schedule climbs to 7 at most before the trace falls again; the
  schedule is run as derived, not stretched to reach 9.
- **Everything else as the burst bill test**: Azure Kubernetes Service with its own cluster autoscaler, a work pool of 1
  to 4 machines, a fresh cluster for each arm, five paired repetitions with the arms' order rotated, the control plane on
  the standard tier, the machines Azure bills counted every 15 s at the list price ($0.096 an hour for either size),
  every gauge reported; native is Azure's autoscaler and the HPA alone, omni is Omni-Compass on top on the engine that
  stands, its replica room read live (Omni v5 amendment 5).
- **Reading.** Three separate runs of each setting, A, B and C (`tools/confirm_abc.py`); each row GAIN or LOSS in all
  three of our runs, EVEN (no difference beyond the noise) or the runs disagree. Replicas, machines and the bill that
  rise are power given, shown beside the response times, the time over the line and the failed requests they bought.
- **Order and dispatch.** The grid conductor starts every Azure set from `scripts/azure_queue.txt`: A of every set, then
  B, then C, one at a time in each machine family's queue, read back by its run's title, never started twice.
- **Amendment of 16 October (the three clouds).** Google Cloud and Amazon carry the same four sets, at the same
  settings and on the same harness, from `scripts/google_queue.txt` and `scripts/amazon_queue.txt` (the workflows
  `gke-metered.yml` and `eks-metered.yml`, one set at a time per machine-family queue, read back by title as on Azure),
  each behind its own `switch=` line, off until that cloud's secrets are in the repository and the founder turns it on; a
  run without its secrets stops before anything is built or billed. The Azure run is the measure of the other two: nothing
  in a set differs between clouds but the machine type, the zone or region, and the list price. (18 October: both
  switched on by the founder, the secrets in the repository; nothing in a set changed.)
- **Disclosed.** At `1 6 1 8 1 6` in October's first runs about 41% of requests failed in both arms with the
  autoscaler pinned at its cap of 10 pods; a peak of 9 asks more of the four workers than 8 did. What each arm served at
  each shape is in its table. Cost: about $4 to $6 a set of five at list price; three sets of each shape, about $30 for
  both. Time: about nine hours a set.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## In the cloud, the bill at native's work (the founder's order, 2026-10-14, night, before any run of it)

The founder's order of 14 October: in the cloud Omni-Compass is to show one thing, a smaller bill for the same work as
native; the benefit of the max belongs where Omni-Compass sits in the engine before the cloud or in the chip at its other
end, not in the cloud's bill. The first Azure runs on the engine that stands were at the max and showed the opposite of
what the cloud needs: on the steady load, three repetitions of run 38455383137 raised the bill 49% at list price (machines
in service 2.9 against 1.8, replicas 19 against 9.5) to buy faster replies and fewer failed requests. From this order
every Azure set runs as follows, and nothing else changes:

- **Omni-Compass on top at the tune-down** (`dial save`, `OMNI_DIAL=save`): native's work on the least resource. Machines
  are given back only where the paired trial on the machines shows the response time no more than 2% slower (the
  verdict), through the release gate, one at a time; a breach puts one back at once.
- **Native's own replica cap** (`replica_ceiling 0`): Omni-Compass never raises the app's replica ceiling above the
  operator's. Inside that cap its HPA target still moves between 60% of the operator's target and the operator's own, so
  at a moment it can hold more pods than native's HPA would, and Azure's autoscaler may then add a machine: in a burst the
  bill can rise, and where it does the row reads power given and the setting is reported as failing its aim, never
  hidden. A setting in which the governor in a cloud only gives back (its HPA target never below the operator's) is a
  change to the engine and is proposed for the next version, not made here.
- **The aim, and the readings.** The bill (machine-hours at list price) and the machines in service aim lower: a cut is
  GAIN. Work served, response times, time over the line and failed requests must read EVEN or GAIN: a LOSS there is a
  LOSS of the test, its cause found and fixed. A rise in the bill is power given and is reported as the setting failing
  its aim.
- **Disclosed before the run.** Where native is short (at its cap and failing requests, as on the steady load), there is
  nothing to give back without costing work, and the bill is expected to read EVEN; the cuts are expected where native
  holds machines it does not need, in the quiet stretches between bursts and in the hours of a day's trough.
- **The runs of the max.** Steady A (run 38455383137: three repetitions finished at the max) and the burst at
  `1 6 1 8 1 6` (run 38500160429, its first repetition) are stopped and kept as runs of the max, counted in no bill result.
  Every Azure set starts again at the tune-down from `scripts/azure_queue.txt` (its run titles carry `dial save`), A of
  every set, then B, then C: the steady load, `1 4 1 6 1 9` (the founder's), `1 6 1 8 1 6`, and the real day on 1 to 9.

## The babysitting tax: three rows in the receipt (the founder's order, 2026-10-14, night, before any run at the tune-down)

The founder's order of 14 October: show that the governor is an autopilot, self-running and self-steering like a
self-driving car, acting ahead, so that nobody turns a knob and nobody has to react. Three rows join every Kubernetes and cloud receipt (`tools/live_reps.py`, `babysitting`), written
here before any run at the tune-down; nothing else in the receipt or the readings changes.

- **Alert minutes**: the whole minutes of the measured window whose 95th percentile response time (nearest rank, a failed
  request counted over the line) was over the line, the minutes an on-call page would be open. Measured from the probe's
  own records, in both arms; judged, the aim lower (time missed: a fall is GAIN).
- **Settings commands the governor wrote on its own**: the writes in the governor's audit inside the window (a dry run
  is none). Native and the watching arm write nothing and read 0. Shown, not judged.
- **The governor's additions decided while the service was still inside its line**: of its decisions inside the window
  that add (a machine more than it saw, or a lower HPA target than its last), the share made while the 95th percentile it
  read was at or under the line. Shown, not judged.

No person touches a setting in either arm of any run; that is stated in every receipt beside the rows.

## The decision period in the cloud, and two arms only (the founder's orders, 2026-10-14, night, before any run at the tune-down)

The founder's orders of 14 October: the governor is to move faster than every native controller under it (15 seconds,
then 10, then 5 seconds a decision were asked the same night), and a change is made only where it is known to hurt
nothing anywhere. Read against the governor before any run, a faster decision period is not a free setting today: four
of its rules count in decisions, not in seconds, and every one of them would change with the period:

| Rule (counted in decisions) | At 60 s (as built and tested) | At 15 s (native's own check) | At 5 s |
|---|---|---|---|
| a trial of giving one machine back (`max_trial`, 20 decisions a phase, written in the engine) | 20 minutes a phase, time to measure the 200 response times it needs | 5 minutes, barely the time those 200 take at the probe's rate | 100 seconds, while the probe gives at most one response time a second: every trial would be abandoned for too little work, no machine would ever be given back, and the bill could not fall |
| the cool-down after a breach (3 decisions, written in the engine) | nothing given back for 3 minutes | 45 seconds | 15 seconds |
| cruise (`--cruise-after`, 2 decisions) | work waiting for 2 minutes | 30 seconds | 10 seconds |
| the spacing of trials and the wait after a refusal (`--verdict-every` 10, `--verdict-recheck` 120) | 10 minutes; 2 hours | 150 seconds; 30 minutes | 50 seconds; 10 minutes |

Two of the four are written in the engine and have no setting, so no run can keep them at their tested seconds at any
period but 60: at native's own 15 seconds a machine would be given back after a trial a quarter as long, and given back
again 45 seconds after a breach instead of 3 minutes, which is the risk of a person woken that the cloud exists to rule
out. Native's own checks are never slowed by any of this: the HPA keeps its 15-second check and Azure's autoscaler its
10 seconds underneath, whatever Omni-Compass's period.

So every Azure set runs at the period the engine was built and tested at: the full decision every 60 seconds, the fast
checks (the scheduling floor, the pod reflex, conveyance on every third, run between decisions) every 5
seconds, three times as fast as the HPA's own 15-second check. The rig accepts other periods (`OMNI_INTERVAL`,
`OMNI_FLOOR_INTERVAL`, passed as `--interval` and `--floor-interval`), and a window in which the governor made no write
needs at least one decision a minute to count, whatever the period. The faster decision belongs to the next engine
version, with every rule above counted in seconds and the fast checks on their own clock, and is used only once a test
shows it reads no LOSS on any gauge anywhere; until then the order holds as the founder put it: native's speed at least, faster only where it hurts nothing. The cloud's arms are native and Omni-Compass on top, nothing else (`ARMS`
defaults to `native compass` in the workflow and in every cloud script); the steady run of the max had run those two.

## In the cloud, the machines alone: a bill that can only fall or stay (the founder's order, 2026-10-14, night, before any run at the tune-down)

The founder's order of 14 October: in the cloud Omni-Compass must never make the bill bigger. Read against the governor,
the tune-down with native's replica cap still allowed it in a burst: the pod target moved down to 60% of the operator's,
more pods than native's asked for machines, and Azure made them. From this order every Azure set runs the governor on the
machines alone (`OMNI_MACHINES_ONLY=1` in `aks-metered.yml`; `scripts/kind_bench.sh`):

- **No pod autoscaler is moved.** The governor is told it senses no service (`--sensed none/none`), so every HPA keeps
  the operator's own target, and the replica room stays shut; the pods are exactly native's.
- **No processor is conveyed and no power is capped** (no `--cap-deployments`, no `--power-cmd`): in a cloud neither
  buys a smaller bill, and a pod given more processor would read busier to the HPA and ask for more pods.
- **The machines.** The governor's machine lever only parks a machine that Azure already made and wakes it again
  (`scripts/kind_nodepool.sh` never asks for more machines than the cluster has, and never tells Azure to make one). A
  machine is parked only after its own trial shows the response time holds within 2% (the verdict, through the release
  gate, one at a time), and a breach wakes it at once; a parked machine with no work is deleted by Azure's own
  autoscaler. Azure's autoscaler alone makes machines, for native's own pods.

So the omni arm can hold no more pods and no more machines than native's autoscalers give it: the bill can only fall or
stay. The bill and the machines aim lower (a cut is GAIN); work, response time, failures and alert minutes must read EVEN
or GAIN. The receipt's commands row shows how often a machine was parked or woken.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## Amendment (2026-10-16): the spine, the seventh organism with the cluster inside

The founder's order of 16 October: the spine (the 267 catalog muscles in all four realms, the base every stack runs on;
`docs/THE_SPINE.md`) is an organism in its own right. With the real cluster inside it runs as `tools/run_kil.py --organism
spine`, on the same protocol (3), the same window rule, the same two arms and the same gauges as the other six; the grid
conductor starts its squares, reads them back and never starts one twice, as it does for every organism, and the workflows
`six-kube`, `aks-metered`, `gke-metered`, `eks-metered` and `cloud-organism` accept `spine`. The results already written on
six organisms stand as they were run; nothing is read across engines or across organism sets.

## Amendment (2026-10-18): a window with no machine in service is refused in either arm; the add-on's set-up waits for its scaler

Two repetitions of the omni-v10 reruns failed for causes outside Omni-Compass, and each is now caught in words that say so.
Neither change touches the engine, a setting, a gauge or a scored window.

- **No machine in service.** In the CruiseKube test (run 39120444653, repetition 8) every worker of the kind cluster left
  service for two minutes (eight of the capture's readings show no machine in service), while the service answered every probe.
  The omni arm's governor wrote nothing, and two of its fifteen decisions failed on that empty reading. The rig refused the
  window, correctly, but its words said the governor was not running. A reading with no machine in service leaves the
  window's machine count wrong in either arm, so such a window is now refused in both arms (`scripts/kind_bench.sh`). The
  capture records each node's taints and conditions at that moment (`fleet/capture/kube_capture.sh`), and a decision that
  failed is named by its error. The repetition runs again in place.
- **The add-on's scaler not yet answering.** In the KEDA test (run 39108180989, profile both, repetition 2), the native arm's
  set-up stopped before its window. KEDA's first call to the HTTP add-on's scaler met a pod still stopping after its rollout,
  and KEDA built the autoscaler without its HTTP metric within five minutes. The ScaledObject is now applied only once no
  KEDA pod is stopping and the scaler has an address. While the autoscaler lacks its metrics, the ScaledObject is touched
  once a minute with an annotation of the harness (never a setting), so KEDA builds the autoscaler again from the same spec
  (`scripts/kind_addons.sh`). The repetition runs again in place.


## Amendment (2026-10-18, omni-v11): the governor holds on a reading with no machine in service

omni-v11 (`docs/OMNI_V11.md`) changes one thing in the governor these tests run. When the cluster's reading shows no machine in
service, the decision is recorded as `held: the cluster's reading shows no machine in service; nothing decided, nothing written`.
Nothing is decided from that reading, nothing is written, and the floor check returns at once. omni-v10 read the same reading
as the highest overload and then divided by the empty capacity, so its decision failed and wrote nothing. The rig counts a held
decision as the governor running (it is a decision record), never among the decisions of a scored window (it is no decision of
the law). A window in which the capture saw no machine in service is refused in either arm (the amendment above), so no scored
window carries a held decision that the capture also saw. Every setting, gauge, load, window and pair is unchanged; every test
runs again on omni-v11.

## Amendment (2026-10-18): on kind, the served image pulled onto every worker before each arm

The KEDA add-on test's mean pod start wait read LOSS on omni-v10 under the http setup. The cause is the test machine
(`docs/POD_START_WAIT.md`, the receipt `results/live/POD_START_PHASES.md`, 741 starts in five runs). A serving pod placed on
a node that never served downloaded and unpacked its image (`registry.k8s.io/hpa-example`, untagged, pull policy Always)
inside the window, on the one runner every kind node shares, and the unpacking took longer the busier that runner was. On a
node already serving, a start took 1.3 to 1.7 s in both arms. On an empty node it took 7 to 12 s. Split exactly, the omni
arm's rise in the mean (+1.42 s on omni-v10, +0.65 s on omni-v11) is the shift of its starts into a busier host (+1.57 s,
+1.64 s), the host its conveyed processor keeps busy. At the same host load on the same kind of node its starts were as fast
or faster (−0.14 s, −0.98 s).

From this amendment on, every kind arm runs an image pre-puller (`deploy/kind/prepull.yaml`) before the governor starts or
the window opens. It is one pod on every worker, waited for on every worker and then deleted. A pre-puller that does not
finish fails the arm's checks. Each arm's `preflight.txt` records `images=pre-pulled on every worker before the arm` and the
digest each worker pulled. The rest stays as written: the operator's manifests, every setting, gauge, load, window and pair,
the engine (omni-v11's digest), and the cloud sets, where every node is its own machine. The kind workflows' three runs on
omni-v11 count only when their own commit carries the pre-puller (`RIG_FILE`, `scripts/dispatch_grid.py`). Their runs on the
rig before end as their own record, and `tools/confirm_abc.py` marks any table whose runs differ in rig. In the grid with the real cluster inside this
rig is protocol 4 (`KUBE_PROTOCOL`, carried in each run's name), and only its runs fill a square; no omni-v11 run with the
cluster inside had started on protocol 3. Expected before any run: a pod on an empty node
starts in about the time one beside a serving pod takes, in both arms. Whatever the runs read is reported.

## Amendment (2026-10-18): the extended fault test, the two faults that blind a governor (written before its run)

The fault test above meets four faults. None of them takes away what a governor reads or the path it writes through, and a
governor's worst hour is the one in which it cannot see. The extended test (`FAULTS=2`, `scripts/kind_faults.sh`) keeps the
four at their moments and adds two after them, the same in every arm:
5. at 82% of the run, the API server is frozen for 30 s: its process in the control-plane node is stopped, then continued.
   The service's own path (kube-proxy on every node) keeps carrying traffic; no controller, native's or Omni-Compass's, can
   read the cluster or write to it.
6. at 88%, the metrics server is scaled to none for two minutes, then back to one: every autoscaler reads no CPU metric.

Each outage is written to `faults.log` only once it took hold; one that did not take hold is written as failed, and the
report has no row for it. The report (`tools/live_reps.py`, "The fault test") reads the two like the four: the time to
recover from the fault's start until responses stay under the line for 30 s straight, at most 300 s, and the share of
samples over the line or failed in the 300 s after it, paired against native. The run's window is 2,500 s, so the second
outage's 300 s end inside it (12% of 2,500 s is 300 s); the four keep their shares of the window, so they fall later in
seconds than in the 900-second test, and its tables are not read beside this one's. Load (open, fixed rate), arms (native;
native with Omni-Compass on top), the engine (omni-v11's digest), the rig (the pre-puller above), the gauges and the ten
pairs are as written; three runs, A, B and C (`scripts/reruns.txt`, "kubernetes faults extended").

Two readings are named before the run. While the API server is frozen, the capture's readings are not answered and are
skipped (`fleet/capture/kube_capture.sh`), in both arms. While the metrics server is gone, the capture reads no CPU used:
the column records 0 for those two minutes in both arms, so the CPU row's change is diluted by that share of the window and
never reversed by it. Expected before any run: Omni-Compass on top holds every setting while it cannot read (omni-v11 holds
on a blind reading; a decision whose read fails writes nothing, and its lease runs 300 s), so it recovers from both as fast
as native or faster. Whatever the runs read is reported.

## Amendment (2026-10-19): a paid cloud set runs to its cap and stops when its bill is read (written before any run of it)

The founder's orders of 19 October: every cloud set gets a three-run reading, A, B and C on one engine, measured as finely as
the cap allows ("the cap we can run it to ... that's all we can run"), at the least cost that still tells what Omni-Compass
can do. Measured from the twelve Azure runs measured to the end (5 paired repetitions each), a run's bill swings about ±9%
of native's (the median half-width of its 95% interval, 1.5% to 36% run to run), so a cut under about 9% read EVEN.

- **Repetitions.** Every Azure set (the steady set, the bursts `1 4 1 6 1 9` and `1 6 1 8 1 6`, the real day on 1 to 9) runs
  up to 100 paired repetitions a run, the founder's cap for paid runs (12 October). At 100 the bill's interval is about ±2%:
  a cut of about 3% reads GAIN eight times in ten.
- **The stopping rule** (`tools/stop_rule.py`, `aks-metered.yml` input `stop_looks`, set to `10,20,40,70`). At each look, on
  repetitions 1 to that look only, the bill's paired change is read with its 99% interval (four looks at 1% each keep the
  rule's error under 5%). The run stops at the first look where the interval clears zero (a cut: GAIN; a rise: power given),
  or holds zero within ±2% of native's bill (EVEN, measured to that precision). It never stops while its 95th percentile or
  its failed requests read a LOSS at that look: a LOSS is measured to the cap. A stopped run's remaining repetitions start,
  read the rule, and spend nothing on Azure. The table is read as every table is (95% intervals, `tools/live_reps.py`); the
  run's summary carries every look (`STOP_RULE.txt`).
- **Unchanged.** The arms (native, then Omni-Compass on top at the tune-down, the machines alone, native's replica cap), the
  sets' loads and windows, the machine family and region, the control plane's tier (standard: amendment 4's way past the
  free tier's capacity refusals; about $0.10 an hour a cluster, not in the bill), and the three-run rule.
- **Both arms at once, on twin clusters,** would remove most of the swing (today the arms run one after the other on fresh
  clusters, each meeting Azure at a different moment). It waits for Azure's processor allowance: one cluster (a system machine
  and four workers of `Standard_D2s_v4`) is the whole 10-vCPU allowance of that machine family in `eastus`, so twins need it
  raised to 20 (asked of Azure, never shrunk to fit). It is written here before any run of it and switched on only by a
  further amendment once the allowance is raised.
- **Counted apart.** A run under the rule carries "to the cap, stopping rule" in its title (`aks-metered.yml` run-name,
  `scripts/dispatch_grid.py` `cloud_title`), so the conductor counts its A, B and C from zero. The omni-v11 steady run at
  5 repetitions (run 39162654399, finished 2026-10-19 01:46 UTC) and any set started before this landed stay as they ran,
  their own record; a set's three-run table pools only runs of one design and one engine.

## Amendment (2026-10-19): a worker held by an add-on's own mark while it serves is in service

Three native repetitions of the omni-v11 CruiseKube test were refused for "no machine in service" while the service answered
every probe: run 39171059299, repetitions 5 and 10, and run 39175670991, repetition 2. Each refused window's capture
(`capture.csv.errors`) records the same cluster:
- every node Ready, the control plane included;
- every node marked `cruisekube.truefoundry.com/overloaded:NoSchedule`. CruiseKube 0.3.4 puts this mark on a node it judges
  overloaded, so the scheduler sends that node no new pod; the pods already on it keep running.

The recorder (`fleet/capture/kube_capture.sh`, `ACTIVE_ONLY=1`) took any NoSchedule mark as a machine out of service. It read
0 machines, and the window was refused under the amendment of 18 October. The add-on's own mark is a scheduling hint, not a
machine leaving service. The recorder now counts a node in service when any one of these holds:
- it is open to new work;
- it is closed (cordoned, or marked idle by the governor) and still carries work that is not a DaemonSet's;
- it is Ready and carries such work, and its only marks are NoSchedule marks that are not Kubernetes' own.

Kubernetes' own marks still take a node out of service: `node.kubernetes.io/*` (unreachable, not ready, under pressure) and
the control plane's role mark `node-role.kubernetes.io/*`. Any NoExecute mark does too, and so does a node that carries no
such work. The power capture (`scripts/kind_power.sh`) already counted such a worker as active, so both captures now agree.
`tests/test_capture_in_service.py` runs the recorder on the cluster as the refused repetitions saw it: before this amendment
it read (0, 0), now (2, 2). The test also checks what still takes a machine out of service, and that the governor's own marks
read as before.

- **Unchanged.** The same rule holds in both arms. A window with truly no machine in service is still refused in either arm.
  Every setting, gauge, load, window and pair is unchanged, and no engine file changes.
- **Earlier runs.** Windows refused before this amendment stay refused. The CruiseKube tables of earlier runs stand as their
  own record. Where the add-on marked some workers, those runs' machine counts may read low in either arm: a stated threat to
  their validity. Repetition 8 of the omni-v10 run 39120444653 (the cause behind omni-v11) ran before the capture recorded
  marks, so its own files cannot say whether the same mark caused it; the same add-on was running.
- **The governor.** The governor (`omni_controller/controller.py`, an engine file of omni-v11) counts its machines by the
  recorder's old rule. Under the add-on's mark on every worker it reads no machine in service and holds; omni-v11 makes that
  hold safe, but the governor is blind there. Counting such a worker in service in the governor changes the engine. That is
  the next version's work, through the model gate, after the founder is told; this amendment does not touch it.
- **Run again.** The CruiseKube test runs again, A, B and C, on the corrected recorder (`scripts/reruns.txt`, block of
  19 October). The three-run table pools only runs of one recorder.

## Amendment (2026-10-22, omni-v16, written before any run of it): the full decision every 15 s

"The decision period in the cloud" above held every run at 60 s because four rules counted decisions. omni-v16 counts every
clock of the governor in seconds (`docs/OMNI_V16.md`: the give-back trial, the cool-down, cruise and the trial spacing
already counted seconds since omni-v7; now the brain's own minute, the compass's damping and smoothing, the edge's window and
rates, the additions past the floor, a command's minute to land and the rest do too), so a period changes only how often the
governor looks: at 15 s a give-back trial still lasts its 20 minutes, the wait after a breach its 3 minutes, and one machine is
still given back at most once a minute. On the founder's word of 22 October ("15 sec all over heart beat"), the default
decision period is 15 s, native's own pod autoscaler's pace, in every run from omni-v16's first on: the kind tests and the
cloud sets alike (`scripts/kind_bench.sh`, `OMNI_INTERVAL`), the fast checks every 5 s as before. A window in which the
governor made no write still needs its decisions to count, now one every 15 s. Runs before omni-v16 stand at the 60 s they
ran at; nothing is read across engines.

## Amendment (2026-10-22, omni-v17, written before any run of it): the main engine every 60 s, the beat a dial

On the founder's word of 22 October, afternoon, the heartbeat is a dial (`docs/OMNI_V17.md`): the main engine takes its full
decision every 60 s, and any beat may be set (5, 15, 30, 60, 75, 90, 120 s and every value between), each shown beside native
with what it buys and what it costs. From omni-v17's first run on, every run of this preregistration, the kind tests and the
cloud sets alike, decides every 60 s by default (`scripts/kind_bench.sh`, `OMNI_INTERVAL`), the fast checks every 5 s as
before; every clock counts seconds since omni-v16, so a give-back trial still lasts its 20 minutes, the wait after a breach its
3 minutes, and one machine is given back at most once a minute. The beats other than 60 s are read in their own runs
(`docs/PACE_PREREGISTRATION.md`, amendment 3). Runs on omni-v16 stand at the 15 s they ran at; nothing is read across engines.

## Amendment (2026-10-24, written before any run of it): Google's and Amazon's sets to the cap under the same stopping rule

On the founder's words of 24 October ("code it to wire it the same way that the Azure is running"), the Google and Amazon sets
(`scripts/google_queue.txt`, `scripts/amazon_queue.txt`: the steady set, the bursts `1 4 1 6 1 9` and `1 6 1 8 1 6`, the real day
on 1 to 9) run as Azure's do under the amendment of 19 October: up to 100 paired repetitions a run, the stopping rule's looks at
10, 20, 40 and 70 (`gke-metered.yml` and `eks-metered.yml` input `stop_looks`, `tools/stop_rule.py`, the same 99% intervals, never
stopping on a LOSS), and "to the cap, stopping rule" in each run's title so their A, B and C are counted from zero. Everything else
is as written for them: the arms, the loads, the windows, the machine families (`e2-standard-2` in `us-central1-a`;
`m5.large` in `us-east-1`), the tune-down on the machines alone and the 60 s beat of the amendment above. Both queues are switched
off and neither cloud has run a set on any engine since omni-v10's logins of 18 October; this is written before the first.


## Amendment (25 October 2026): the ladder is 1, 10, 100 and 500

The founder's order of 25 October: the grid's top rung is 500 copies and 500 runs, in line with the Python's 500-run Monte
Carlo (`tools/engine_runs.py`), replacing the 1,000 tier of 15 October. Every grid run started from this amendment on runs the
ladder 1, 10, 100 and 500 (`scripts/dispatch_grid.py`); runs started before it stay as their own record. Paid cloud and GPU runs
stay at 1, 10 and 100 copies with at most 100 repetitions.

## Amendment (31 October 2026, written before any set at the max starts): every cloud set runs the whole engine at the max; the machines alone of 14 October struck

The founder's words of 31 October ("Why is there any hard rule written ... Whatever the math does and falls out is whatever
happens. All we need to do is tune up what the math does to the best way we can and let whatever falls out fall out. And when it
falls out wrong, the tuning is wrong"; "What I care is to make the cloud the best it can be with Omni-Compass in it, as well as
on site with Omni-Compass on it, and we have to sit and tune and tweak both scenarios"). The section "In the cloud, the machines
alone" above is struck from this amendment on: no set started after it runs `OMNI_MACHINES_ONLY=1`, `dial save` or the
governor's `--give-back-only` (the switch is gone from the rig and the workflows; the flag leaves the governor with the next
engine version, and nothing passes it). Every cloud set runs Omni-Compass on top at the max, every muscle: the service sensed and
its pod target moved inside the autoscaler's cover, the processor conveyed, the declared power model read, the replica room read
live as on kind (`replica_ceiling` empty), and the machine lever parking and waking machines the cloud's own autoscaler made; the
autoscaler, native's machine controller, stays in every arm and alone adds machines (`scripts/kind_nodepool.sh` asks the cloud
for none). The bill (machine-hours at list price) is read by the one key beside work, response time, failures and alert
minutes, and the cloud's judged number is the work per dollar: the work answered within the line for each dollar of the bill.
The bill may rise where the work rises more, a rise read as power given beside the work it bought; a tune whose work per dollar
falls against native is not admissible (`docs/THE_TUNE.md`), a fault of the tune, root-caused in the model first
(`tools/model_gate.py`, whose cloud setting is the max from this amendment); the founder's order of 18 October, never raise its
bill, is read the same way, by judging, never by tying the engine's hands. Every set at
the max is its own A, B and C under the stopping rule of 19 October and the cap of 12 October (100 paired repetitions; 1, 10 and
100 copies); the sets started before this amendment (omni-v18's steady set; omni-v21's steady set, 25 of 100 repetitions when
this was written) finish as the tune-down's record and are read in no table with a set at the max. Google's and Amazon's queues
carry the same change behind their switches.

The same evening, before any set at the max started (the founder's words: "We never make the bill smaller ... they're looking to
do more work with the money they're spending"; and then, "We're pushing 1% more bill, but we're getting ~12% more work ... anybody
will pay 1% more for 10% more product"): the cloud is judged by its work per dollar, and these sets cannot read it as built. Each
sends a fixed rate of requests (`LOADGEN=open`), so its work is the same in both arms by design and a set at the max could show
only the bill beside a faster answer; the factory beat's ladder on omni-v23 reads the cloud setting at the max with the
machine-hours up 9% to 35% across the beats, 14% at 60 s, on a plant whose work is fixed the same way
(`results/model_gate/V23_LADDER.md`, our own models, class S). Azure's queue is held (`scripts/azure_queue.txt`, `switch=off`)
until its sets carry the load whose work grows with the speed (the work meter, `LOADGEN=meter`, `tools/capacity_report.py`, the
completed work counted in each arm), written into this preregistration before the switch goes on; then its sets start as written
here, on the engine that stands then.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
