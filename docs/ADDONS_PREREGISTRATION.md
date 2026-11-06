# The add-on test: Omni-Compass on top of Kubernetes with its add-ons (preregistration)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Declared on 10 October 2026, before any run of this test. Ordered by the founder the same day: native must be the
setup clusters actually run, with its add-ons, not bare Kubernetes, and Omni-Compass must show what it adds on top of
that. Every earlier Kubernetes set stays as it is; this is a new set beside them.

## The question

With KEDA, the event-driven autoscaler most clusters add to Kubernetes, and its HTTP add-on owning the service's
autoscaler, does Omni-Compass on top still make the service faster, use fewer machines or less energy, without moving
anything power given?

## The arms (two, as always)

- **native**: Kubernetes with the add-ons below, nothing else. Omni-Compass is not started.
- **omni**: the same cluster and add-ons, with Omni-Compass on top: engine omni-v3 unchanged (`python3 tools/omni_version.py`),
  the compass law (`ARM=compass`), every live muscle as in the v3 Kubernetes sets. Its moves on the service's autoscaler
  reach KEDA's ScaledObject through the plug (`scripts/kubectl_keda.py`), because KEDA rebuilds the HPA from the
  ScaledObject and would undo a move written to the HPA itself (one writer per knob). The plug carries a move exactly or
  refuses it; a run in which any move did not reach KEDA whole is invalid.

## The add-ons, frozen

- metrics-server v0.9.0 (as every set), KEDA **2.21.0** and the KEDA HTTP add-on **0.16.0** from their release manifests,
  SHA-256 pinned (`scripts/kind_addons.sh`), every KEDA pod on the control plane.
- Two native setups, each its own set of paired runs:
  - **both**: KEDA scales php-apache on the HPA's own CPU target (50% of request, as `deploy/kind/demo.yaml`) and on the
    add-on's live requests in flight (target 1 per pod: one request fills a pod's 500m limit), whichever asks for more.
  - **http**: KEDA scales on the live requests in flight alone, as the add-on is set up for a web service.
- Replica range 1 to 10, the HPA's default behaviour, the interceptor at one replica (its own autoscaler, 200 requests
  waiting per replica, would hold one at this load).
- The load and the probe both enter through the add-on's interceptor (catch-all route to php-apache).

## The workload and the measure

As `benchmark-reps`: the six-worker kind cluster, a fresh cluster per arm, both arms back to back on the same runner in an
order rotated by repetition; the closed-loop load generator stepping 1 2 3 1 2 1; 120 s warm-up, 900 s measured; ten
paired repetitions per setup (run A). Every gauge of `tools/live_reps.py` is reported, losses included, with the paired
mean difference and its 95% interval.

## How it is read

- A gauge whose 95% interval of the paired difference is clear of zero is a difference in this run; one whose interval
  includes zero is no difference beyond the noise, and that is the result.
- One run (A) is a first reading. A reading the same in all three of our runs needs runs B and C on the same commit (`tools/confirm_abc.py`):
  GAIN or LOSS in all three of our runs (judged by what the gauge is for; a resource spent that rose reads power given), no difference beyond the noise, or the runs disagree.
- Response times are class L (measured on live software). Machines in service are counted live; the watts are the
  declared model (class S), as in every kind set.

## Known limits, said before the result

- On kind there is no node autoscaler for native (no cloud to add or remove machines), so native keeps all six workers
  in service; Omni-Compass's machine and energy gauges are measured against that. A node autoscaler (Cluster Autoscaler
  or Karpenter, as on the Azure set) is the next add-on test.
- The interceptor adds one hop to every request in both arms.

## The result: A, B and C on v3 (added 11 October 2026, after the runs; nothing above was changed)

Runs A 38096663118 (commit `175cc0f`), B 38099655092 and C 38099656930 (commit `85b1508`); the two commits differ only in
the legal notice in comments, and the engine is omni-v3 (digest `b53d05449ee04c4b`) in all three. Ten paired repetitions
per setup per run, 59 of 60 pairs valid: repetition 4 of setup both in run A is invalid by the preregistered rule (the
metrics-server rollout timed out before the measurement began, in both arms) and is shown in the raw files, not counted.
The raw files of every run are in `results/live/raw/addons-run-<id>/`, the wiring check run (38096658903, one 360 s
repetition per setup) beside them. The tables: [`V3_KEDA_CPU_REQUESTS.md`](../results/live/V3_KEDA_CPU_REQUESTS.md) (setup
both) and [`V3_KEDA_REQUESTS.md`](../results/live/V3_KEDA_REQUESTS.md) (setup http), every row, losses included.

| Gauge | Setup both: KEDA on the CPU target and the requests in flight | Setup http: KEDA's HTTP add-on on the requests in flight |
|---|---|---|
| Response time, 95th percentile | **−51% to −53%, GAIN in all three of our runs** | **−73% to −76%, GAIN in all three of our runs** |
| Response time, mean | −36% to −39%, GAIN in all three of our runs | −59% (−58.7% to −59.3%), GAIN in all three of our runs |
| Response time, 99th percentile | −60% to −62%, GAIN in all three of our runs | −70% to −72%, GAIN in all three of our runs |
| Time over the response line | −97% to −100%, GAIN in all three of our runs | −96% to −97%, GAIN in all three of our runs |
| Failed requests | no difference beyond the noise (none in either arm in B and C) | no difference beyond the noise |
| Worker nodes in service | −0.6% to −0.7%, no difference beyond the noise in 2 of 3 runs | **−5.9% to −7.8%, GAIN in all three of our runs** |
| Node-hours | −0.4% to −0.9%, no difference beyond the noise in 1 of 3 runs | −5.8% to −8.2%, GAIN in all three of our runs |
| HPA replicas (set by KEDA) | +0.3% to +3.1%, no difference beyond the noise in 2 of 3 runs | −13.7% to −14.5%, GAIN in all three of our runs |
| Energy, parked workers still on at idle power (declared model, class S) | **+1.0% to +1.6%, power given in all three of our runs** | **+1.4% to +2.6%, power given in all three of our runs** |
| Energy, parked workers at 25 W standby (declared model, class S) | +0.5% to +1.2%, no difference beyond the noise in 1 of 3 runs | −1.6% to −4.2%, no difference beyond the noise in 1 of 3 runs |
| CPU used by the service (shown, not judged) | +24% to +32% | +45% to +54% |
| Energy per core-hour of the service's CPU (shown, not judged) | −18% to −23% | −33% to −36% |

**What it says.** On top of KEDA, Omni-Compass made the service answer two to four times faster at the 95th percentile in
every run of both setups, and with the HTTP add-on alone it also ran on 6% to 8% fewer machines. The loss is the energy
counted with every parked worker still drawing idle power: 1% to 3% more. The load is closed-loop (each client sends its
next request when the last one returns), so faster answers bring more requests: the service's CPU, which php-apache spends
in a fixed amount per request, rose 24% to 54%, and the modelled watts rose with it, while the energy per core-hour fell 18%
to 36%. The total stands as a loss in all three of our runs, counted against Omni-Compass in the index; the work itself is not counted by
this test, so the claim "more work for the energy" is shown, not judged.

**Declared for the next run of this test (on Omni v4), before it runs:** the load generator counts the requests it
completes, and energy is also judged per request served, beside the total; native gains a node autoscaler where the
platform has one (Karpenter through Azure's node auto-provisioning on AKS, the next add-on test).

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
