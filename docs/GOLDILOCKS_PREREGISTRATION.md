# Goldilocks: Omni-Compass on top of a service rightsized with Goldilocks and the Vertical Pod Autoscaler (preregistration)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Declared on 12 October 2026, before any run of this test. It is register row 80, the first of the nine open-source pieces
the founder listed on 12 October (`docs/THE_SEAT.md`) to be built as a benchmark with Omni-Compass on top. Every earlier
Kubernetes set stays as it is; this is a new set beside them.

## The question

When the service's resource requests are set the way operators set them with Goldilocks (Fairwinds; Apache-2.0), from the
recommendation of the Vertical Pod Autoscaler's own recommender (Kubernetes SIG Autoscaling; Apache-2.0), does
Omni-Compass on top still make the service faster, use fewer machines or less energy, without a LOSS anywhere?

## What Goldilocks is, and so what native is

Goldilocks is "a utility that can help you identify a starting point for resource requests and limits". Its controller
gives each workload in a labelled namespace a Vertical Pod Autoscaler in recommendation mode (update mode "off", its
default; its own documentation calls any other mode advanced and not recommended), and its dashboard shows the
recommendation for an operator to apply. Native is therefore Goldilocks as shipped and as used: the recommendation applied
by the operator, with the service's own autoscaler (the HPA) running as in every set. Goldilocks and the recommender keep
running through the measured window, recommending, as they do in service.

## The arms (two, as always)

- **native**: Kubernetes with Goldilocks, the VPA's recommender and the recommendation applied; Omni-Compass is not started.
- **omni**: the same cluster, the same Goldilocks, the same recommendation applied, with Omni-Compass on top (`ARM=compass`):
  every live muscle as in the Kubernetes sets (the HPA, the node pool, the power cap, the rollout guard), the engine that
  stands at the run's commit (`python3 tools/omni_version.py`, recorded in every run). Omni-Compass writes nothing to the
  VPA, to Goldilocks or to the requests the operator applied: its identity cannot (`kubectl auth can-i` receipts in every
  run's `rbac_omni.txt`), and every reset check reads back the operator's settings after the run.

## Goldilocks and the VPA, frozen

- metrics-server v0.9.0 (as every set); the VPA **1.7.1** (the line its own compatibility table gives for Kubernetes
  1.35, the kind node image of every set): its CRDs, RBAC and the recommender alone, from the project's own manifests at
  the release tag, every file SHA-256 pinned; no updater and no admission webhook (Goldilocks needs only the recommender).
- Goldilocks **4.16.2**: its controller from the project's own manifests at the release tag, SHA-256 pinned, its image
  pinned to the full tag (`us-docker.pkg.dev/fairwinds-ops/oss/goldilocks:v4.16.2`). The namespace `default` labelled
  `goldilocks.fairwinds.com/enabled=true`; the run checks that Goldilocks's VPA for php-apache is in update mode Off.
- Every Goldilocks and VPA pod runs on the control plane beside metrics-server and CoreDNS, so the six measured workers
  carry only the service, as in every set (`scripts/kind_addons_goldilocks.sh`).

## The learning and the operator's rule, the same in every arm

1. With the load generator running, before the arms are told apart (Omni-Compass not started), the load steps through the
   benchmark's own steps (1 2 3 1 2 1) over 600 s, so the recommender sees the service at every load it will meet.
2. The recommendation for the container php-apache is read from Goldilocks's VPA and applied as the VPA itself applies
   one (its default, RequestsAndLimits): the CPU request at the target; the CPU limit kept in its proportion to the
   request (the operator's 200m request and 500m limit in `deploy/kind/demo.yaml`: limit = target x 500/200); the memory
   request at the target (the container has no memory limit to keep). The deployment is rolled out and the warm-up
   begins.
3. One recommendation for both arms of a repetition: each arm runs the same learning load (so both have the same
   warm-up), and the operator applies the recommendation learned in the repetition's first arm to both (the order of the
   arms rotates by repetition). Two short learnings differ by about a tenth on their own (the wiring run of 12 October,
   run 38303511766: 203m in one arm, 182m in the other), and two arms serving with different requests would not be the
   same native. Each arm's own learning is kept beside it.
4. The recommendation, what was applied and the learning schedule are written to every run's `addons.txt`,
   `goldilocks_recommendation.json` (applied), `goldilocks_own_recommendation.json` (the arm's own learning) and
   `goldilocks_apply.json`; the VPA as the window left it to `vpa_end.json`.

## The workload and the measure

As the KEDA add-on test (`docs/ADDONS_PREREGISTRATION.md`): the six-worker kind cluster, a fresh cluster per arm, both arms
back to back on the same runner in an order rotated by repetition; the closed-loop load generator stepping 1 2 3 1 2 1;
120 s warm-up, 900 s measured; ten paired repetitions (run A). Every gauge of `tools/live_reps.py` is reported, losses
included, with the paired mean difference and its 95% interval. A run whose checks fail (a pinned file that does not
match, a VPA not in mode Off, a pod of Goldilocks or the VPA off the control plane, a reset that does not hand back the
operator's settings) is invalid, kept in the raw files and not counted.

## How it is read

- A gauge whose 95% interval of the paired difference is clear of zero is a difference in this run; one whose interval
  includes zero is no difference beyond the noise, and that is the result.
- One run (A) is a first reading. A reading the same in all three of our runs needs runs B and C on the same commit
  (`tools/confirm_abc.py`): GAIN or LOSS in all three of our runs (judged by what the gauge is for; a resource spent that rose reads power given), no difference beyond the noise, or the runs disagree.
- Response times are class L (measured on live software). Machines in service are counted live; the watts are the
  declared model (class S), as in every kind set.

## Known limits, said before the result

- The recommendation is learned over ten minutes of this load, not the days an operator would give it; both arms of a
  repetition serve with the same recommendation, so the comparison is fair, and the recommendation itself is shown.
- On kind there is no node autoscaler for native (no cloud to add or remove machines), so native keeps all six workers in
  service; Omni-Compass's machine and energy gauges are measured against that.
- The VPA in a live mode (Auto, or in place) is not this test: Goldilocks ships recommendation mode, and a VPA changing CPU
  requests under an HPA that scales on CPU is the combination both projects' documentation warns against.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
