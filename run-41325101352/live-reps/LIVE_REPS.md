# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.949 | 5.948 |
| node-hours | 2.511 | 2.513 | 2.493 | 2.496 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.4 | 276.5 | 276.7 | 277.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.4 | 276.5 | 275.1 | 275.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 655.9 | 601.2 | 619.5 | 566.5 |
| response time (ms), 95th percentile | 2612 | 2742 | 2646 | 2880 |
| response time (ms), 99th percentile | 3634 | 3853 | 3747 | 4039 |
| time over the response line (% of samples) | 30.51 | 22.88 | 29.94 | 22.21 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.3 | 14.2 | 14 | 14 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 17.6 | 26 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.24 | 22.44 | 24.21 | 21.32 |
| utilisation (used / allocatable) | 0.07166 | 0.07174 | 0.07234 | 0.07229 |
| CPU used (cores), mean | 1.72 | 1.722 | 1.723 | 1.722 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01724 | 0.0175 |
| CPU used with Omni's own (cores), mean | 1.72 | 1.722 | 1.741 | 1.74 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 387.2 | 386.9 | 384.5 | 384 |
| HPA replicas, mean | 2.048 | 2.121 | 2.074 | 2.24 |
| pods started | 0.1 | 0.2 | 0.3 | 0.7 |
| pod start wait, total (s) | 0.2 | 0.4 | 0.4 | 1.1 |
| pod start wait, mean (s) | 0.2 | 0.2 | 0.4 | 0.75 |
| host CPU busy, the real machine under kind (%) | 48.9 | 49.29 | 49.97 | 50.08 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 878.5 | 884.1 | 887.7 | 887.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.9 | 5.898 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4542 | 0.4333 | 0.5125 | 0.3958 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.3 | 2.5 | 2.4 | 2.6 |
| queue: job turnaround, submitted to done, mean (s) | 184 | 193.3 | 189.9 | 194.1 |
| queue: jobs unfinished at the window's end | 0 | 0 | 0 | 0 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan | nan |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.948 | −0.9% | −0.1602 to +0.0569 | no |
| node-hours | 2.513 | 2.496 | −0.7% | −0.0661 to +0.0324 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 276.5 | 277.1 | +0.2% | −0.3690 to +1.4792 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.5 | 275.5 | −0.4% | −5.0293 to +2.8895 | no |
| response time (ms), mean | 601.2 | 566.5 | −5.8% | −69.7422 to +0.4222 | no |
| response time (ms), 95th percentile | 2742 | 2880 | +5.0% | −37.3253 to +312.6353 | no |
| response time (ms), 99th percentile | 3853 | 4039 | +4.8% | +13.5248 to +359.1588 | yes: LOSS |
| time over the response line (% of samples) | 22.88 | 22.21 | −2.9% | −2.1139 to +0.7715 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.2 | 14 | −1.4% | −0.6524 to +0.2524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26 | +26.000 (native is 0) | +12.2532 to +39.7468 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 22.44 | 21.32 | −5.0% | −5.7801 to +3.5401 | no |
| utilisation (used / allocatable) | 0.07174 | 0.07229 | +0.8% | −0.0004 to +0.0015 | no |
| CPU used (cores), mean | 1.722 | 1.722 | +0.0% | −0.0158 to +0.0173 | no |
| Omni's own CPU (cores), mean | 0 | 0.0175 | +0.017 (native is 0) | +0.0162 to +0.0188 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.722 | 1.74 | +1.1% | +0.0022 to +0.0344 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 386.9 | 384 | −0.7% | −7.5861 to +1.9543 | no |
| HPA replicas, mean | 2.121 | 2.24 | +5.6% | −0.1625 to +0.4009 | no |
| pods started | 0.2 | 0.7 | +250.0% | −0.3430 to +1.3430 | no |
| pod start wait, total (s) | 0.4 | 1.1 | +175.0% | −0.8471 to +2.2471 | no |
| pod start wait, mean (s) | 0.2 | 0.75 | +275.0% | −0.3171 to +1.4171 | no |
| host CPU busy, the real machine under kind (%) | 49.29 | 50.08 | +1.6% | +0.3119 to +1.2606 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 884.1 | 887.2 | +0.4% | −8.0605 to +14.2605 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.898 | −1.7% | −0.3129 to +0.1087 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4333 | 0.3958 | −8.7% | −0.1635 to +0.0885 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.5 | 2.6 | +4.0% | −0.9366 to +1.1366 | no |
| queue: job turnaround, submitted to done, mean (s) | 193.3 | 194.1 | +0.4% | −15.5896 to +17.2062 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.511 | 2.513 | +0.1% | −0.0059 to +0.0085 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 276.4 | 276.5 | +0.1% | −0.5565 to +0.8509 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.4 | 276.5 | +0.1% | −0.5565 to +0.8509 | no |
| response time (ms), mean | 655.9 | 601.2 | −8.3% | −87.5388 to −21.8691 | yes: GAIN |
| response time (ms), 95th percentile | 2612 | 2742 | +5.0% | −73.4928 to +333.4908 | no |
| response time (ms), 99th percentile | 3634 | 3853 | +6.0% | +17.9719 to +419.4029 | yes: LOSS |
| time over the response line (% of samples) | 30.51 | 22.88 | −25.0% | −9.9093 to −5.3483 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.3 | 14.2 | −0.7% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.24 | 22.44 | +10.9% | −0.9842 to +5.3775 | no |
| utilisation (used / allocatable) | 0.07166 | 0.07174 | +0.1% | −0.0004 to +0.0005 | no |
| CPU used (cores), mean | 1.72 | 1.722 | +0.1% | −0.0085 to +0.0122 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.72 | 1.722 | +0.1% | −0.0085 to +0.0122 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 387.2 | 386.9 | −0.1% | −2.1453 to +1.4392 | no |
| HPA replicas, mean | 2.048 | 2.121 | +3.6% | −0.1145 to +0.2609 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.4278 to +0.6278 | no |
| pod start wait, total (s) | 0.2 | 0.4 | +100.0% | −0.8556 to +1.2556 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 48.9 | 49.29 | +0.8% | +0.0163 to +0.7592 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 878.5 | 884.1 | +0.6% | −0.6468 to +11.8468 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4542 | 0.4333 | −4.6% | −0.1153 to +0.0737 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.3 | 2.5 | +8.7% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 184 | 193.3 | +5.0% | +2.0327 to +16.5339 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.949 | −0.9% | −0.1355 to +0.0331 | no |
| node-hours | 2.511 | 2.493 | −0.7% | −0.0556 to +0.0186 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 276.4 | 276.7 | +0.1% | −0.5760 to +1.1663 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.4 | 275.1 | −0.5% | −4.3556 to +1.7250 | no |
| response time (ms), mean | 655.9 | 619.5 | −5.5% | −67.2799 to −5.4649 | yes: GAIN |
| response time (ms), 95th percentile | 2612 | 2646 | +1.3% | −104.1575 to +171.2445 | no |
| response time (ms), 99th percentile | 3634 | 3747 | +3.1% | −11.8621 to +238.3685 | no |
| time over the response line (% of samples) | 30.51 | 29.94 | −1.9% | −1.0322 to −0.1011 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.3 | 14 | −2.1% | −0.7828 to +0.1828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.6 | +17.600 (native is 0) | +8.4074 to +26.7926 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.24 | 24.21 | +19.6% | −3.2928 to +11.2195 | no |
| utilisation (used / allocatable) | 0.07166 | 0.07234 | +1.0% | −0.0002 to +0.0016 | no |
| CPU used (cores), mean | 1.72 | 1.723 | +0.2% | −0.0166 to +0.0238 | no |
| Omni's own CPU (cores), mean | 0 | 0.01724 | +0.017 (native is 0) | +0.0159 to +0.0185 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.72 | 1.741 | +1.2% | −0.0004 to +0.0421 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 387.2 | 384.5 | −0.7% | −6.0968 to +0.7016 | no |
| HPA replicas, mean | 2.048 | 2.074 | +1.3% | −0.1116 to +0.1644 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.2 | 0.4 | +100.0% | −0.5388 to +0.9388 | no |
| pod start wait, mean (s) | 0.2 | 0.4 | +100.0% | −0.5388 to +0.9388 | no |
| host CPU busy, the real machine under kind (%) | 48.9 | 49.97 | +2.2% | +0.5655 to +1.5668 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 878.5 | 887.7 | +1.0% | −0.1008 to +18.5008 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.9 | −1.7% | −0.2573 to +0.0566 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4542 | 0.5125 | +12.8% | −0.1115 to +0.2282 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.3 | 2.4 | +4.3% | −0.7564 to +0.9564 | no |
| queue: job turnaround, submitted to done, mean (s) | 184 | 189.9 | +3.2% | −2.8338 to +14.6672 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.949 | −0.9% | −0.1355 to +0.0331 | no |
| node-hours | 2.513 | 2.493 | −0.8% | −0.0593 to +0.0197 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 276.5 | 276.7 | +0.1% | −0.9256 to +1.2215 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.5 | 275.1 | −0.5% | −4.8699 to +1.9449 | no |
| response time (ms), mean | 601.2 | 619.5 | +3.0% | −17.3053 to +53.9685 | no |
| response time (ms), 95th percentile | 2742 | 2646 | −3.5% | −256.6956 to +63.7846 | no |
| response time (ms), 99th percentile | 3853 | 3747 | −2.7% | −283.0476 to +72.1792 | no |
| time over the response line (% of samples) | 22.88 | 29.94 | +30.9% | +4.8392 to +9.2851 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.2 | 14 | −1.4% | −0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.6 | +17.600 (native is 0) | +8.4074 to +26.7926 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 22.44 | 24.21 | +7.9% | −2.9021 to +6.4355 | no |
| utilisation (used / allocatable) | 0.07174 | 0.07234 | +0.8% | −0.0001 to +0.0013 | no |
| CPU used (cores), mean | 1.722 | 1.723 | +0.1% | −0.0165 to +0.0200 | no |
| Omni's own CPU (cores), mean | 0 | 0.01724 | +0.017 (native is 0) | +0.0159 to +0.0185 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.722 | 1.741 | +1.1% | +0.0000 to +0.0380 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 386.9 | 384.5 | −0.6% | −5.2472 to +0.5582 | no |
| HPA replicas, mean | 2.121 | 2.074 | −2.2% | −0.2088 to +0.1152 | no |
| pods started | 0.2 | 0.3 | +50.0% | −0.5263 to +0.7263 | no |
| pod start wait, total (s) | 0.4 | 0.4 | ±0.0% | −1.1184 to +1.1184 | no |
| pod start wait, mean (s) | 0.2 | 0.4 | +100.0% | −0.5388 to +0.9388 | no |
| host CPU busy, the real machine under kind (%) | 49.29 | 49.97 | +1.4% | +0.3410 to +1.0158 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 884.1 | 887.7 | +0.4% | −2.1244 to +9.3244 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.9 | −1.7% | −0.2573 to +0.0566 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4333 | 0.5125 | +18.3% | −0.1527 to +0.3111 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.5 | 2.4 | −4.0% | −0.7263 to +0.5263 | no |
| queue: job turnaround, submitted to done, mean (s) | 193.3 | 189.9 | −1.7% | −8.9695 to +2.2362 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.948 | −0.9% | −0.1602 to +0.0569 | no |
| node-hours | 2.511 | 2.496 | −0.6% | −0.0620 to +0.0310 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 276.4 | 277.1 | +0.3% | −0.0803 to +1.4848 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.4 | 275.5 | −0.3% | −4.5201 to +2.6746 | no |
| response time (ms), mean | 655.9 | 566.5 | −13.6% | −121.1902 to −57.5378 | yes: GAIN |
| response time (ms), 95th percentile | 2612 | 2880 | +10.2% | +101.2871 to +434.0209 | yes: LOSS |
| response time (ms), 99th percentile | 3634 | 4039 | +11.1% | +164.0790 to +645.9794 | yes: LOSS |
| time over the response line (% of samples) | 30.51 | 22.21 | −27.2% | −10.2789 to −6.3210 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.3 | 14 | −2.1% | −0.9786 to +0.3786 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26 | +26.000 (native is 0) | +12.2532 to +39.7468 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.24 | 21.32 | +5.3% | −1.8373 to +3.9906 | no |
| utilisation (used / allocatable) | 0.07166 | 0.07229 | +0.9% | −0.0004 to +0.0017 | no |
| CPU used (cores), mean | 1.72 | 1.722 | +0.2% | −0.0144 to +0.0197 | no |
| Omni's own CPU (cores), mean | 0 | 0.0175 | +0.017 (native is 0) | +0.0162 to +0.0188 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.72 | 1.74 | +1.2% | +0.0030 to +0.0373 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 387.2 | 384 | −0.8% | −8.3578 to +2.0198 | no |
| HPA replicas, mean | 2.048 | 2.24 | +9.4% | −0.0363 to +0.4210 | no |
| pods started | 0.1 | 0.7 | +600.0% | −0.0032 to +1.2032 | no |
| pod start wait, total (s) | 0.2 | 1.1 | +450.0% | −0.2410 to +2.0410 | no |
| pod start wait, mean (s) | 0.2 | 0.75 | +275.0% | −0.1742 to +1.2742 | no |
| host CPU busy, the real machine under kind (%) | 48.9 | 50.08 | +2.4% | +0.8267 to +1.5213 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 878.5 | 887.2 | +1.0% | +0.5928 to +16.8072 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.898 | −1.7% | −0.3129 to +0.1087 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4542 | 0.3958 | −12.8% | −0.2223 to +0.1056 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.3 | 2.6 | +13.0% | −0.9639 to +1.5639 | no |
| queue: job turnaround, submitted to done, mean (s) | 184 | 194.1 | +5.5% | −2.2533 to +22.4367 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*