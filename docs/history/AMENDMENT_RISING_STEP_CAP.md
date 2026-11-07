# Amendment: a rising step adds only the pods already waiting

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written before the next capacity run. The run in progress (`benchmark-reps` 294, commit `5d2e238`) is the previous setting. Nothing in this file is a result.

Owner: The Omni-Compass LLC. Evaluation use. Not a change to the engine's law. A change to the live controller's HPA write on a rising step.

## What the last capacity run left

`results/live/CAPACITY_2.md`, run 37162457542, commit `199f350`, ten pairs, six workers, open-loop load rising in eight steps of 6 requests a second (1 to 8 generators, 48 requests a second offered).

Compass against native: 24.6 requests a second inside the line against 16.2, +51.9 percent (interval +6.2 to +10.6). p95 cut in half. Replicas down 10.7 percent. Pods started 5.1 against 3.8, +34.2 percent. The file does not label the arm better while that row stands.

CPU used over allocatable stayed about 0.10 in both arms. The line broke before the node filled. The load past 24.6 requests a second missed the 500 ms line.

## Why a wide cap is the wrong tweak

`deploy/kind/demo.yaml` stops at `maxReplicas: 10`. Past ten pods the next request has nowhere to go. A write that lifts the cap to the operator's max times the generators would start pods the line has not asked for. That is the same +34 percent pod-start row, made larger. The efficient write adds one place per pod that is already pending, and nothing else.

## The change

On a sensed HPA only (`--sensed`). An unsensed neighbour stays at the operator's target and the operator's replica range.

Demand `d` is the value the controller already reads from the autoscaler's own status (utilisation times pods). Demand is rising when the most of `d` over one autoscaler window exceeds the least by more than `DEMAND_RISE` (0.05).

One write, and only while demand is rising and a pod of that service is pending:

- set `spec.maxReplicas` to `max(current max, spec.replicas + pending)`. One pending pod, one extra place. Record the operator's original min and max in `omnicompass.io/original-replica-range` the first time it changes.
- set the CPU target to the least cover value that makes the autoscaler's desired replicas equal `spec.replicas + pending`. Do not drop to 60 percent unless that is the value the pending count needs. Do not wait the window. The window wait stays only for a raise of the target.

No second write in the same decision. No machine added in this amendment. The node lever stays as it is.

When demand has been steady for one window, the position is under the center, and no pod is pending:

- put `maxReplicas` back to the annotated original in one write.
- return the CPU target toward the operator's own as the compass already does.

The kill switch restores both. A restored arm must show the original target, the original replica range, and no annotation left.

## What is not changed

The compass gains, the center, the verdict, the shield, the fail-up on a blind probe or a dead machine, and the rule that an unsensed HPA is not moved. The allocation law is not given this write. It stays the control arm.

## The rerun

Same capacity test as `CAPACITY_2.md`: ten pairs, native / omni / compass, order rotated, eight steps, 200 seconds a step.

Label by the one rule. The row that failed last time is pods started. If capacity rises and pods started are not worse than native, the arm can be labelled. If capacity rises and pods started are still worse, report both and do not label it better.

The number to read is requests a second inside the line, compass against native, with the 95 percent interval of the paired difference. Last compass result 24.6. Offered load 48. The room this write is aimed at is the pending pods that had no place, not a full node, and not a power cut.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
