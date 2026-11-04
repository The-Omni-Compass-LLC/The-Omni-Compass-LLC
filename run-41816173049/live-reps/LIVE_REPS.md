# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.59 | 10.21 |
| node-hours | 5.029 | 5.029 | 4.441 | 4.273 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.7 | 525.8 | 527.3 | 524.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.7 | 525.8 | 483 | 468.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 612.3 | 759.6 | 721.5 | 830.1 |
| response time (ms), 95th percentile | 2280 | 3110 | 2978 | 3443 |
| response time (ms), 99th percentile | 3162 | 4327 | 3978 | 4818 |
| time over the response line (% of samples) | 21.67 | 24.81 | 24.99 | 29.46 |
| failed requests (%) | 0 | 0.03524 | 0.007168 | 0.1576 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 14.7 | 13.8 | 16.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 134 | 71.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 16.67 | 13.56 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.35 | 40.2 | 19.37 | 69.7 |
| utilisation (used / allocatable) | 0.03441 | 0.03433 | 0.04075 | 0.04042 |
| CPU used (cores), mean | 1.652 | 1.648 | 1.736 | 1.621 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05616 | 0.04441 |
| CPU used with Omni's own (cores), mean | 1.652 | 1.648 | 1.792 | 1.666 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 780.3 | 774.2 | 676.3 | 694.4 |
| HPA replicas, mean | 4.076 | 3.964 | 4.764 | 5.35 |
| pods started | 0.4 | 0.1 | 2.9 | 3.4 |
| pod start wait, total (s) | 0.8 | 0.2 | 7.6 | 9.1 |
| pod start wait, mean (s) | 0.6 | 0.2 | 2.31 | 2.096 |
| host CPU busy, the real machine under kind (%) | 51.3 | 57.42 | 57.47 | 62.81 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 876 | 974.1 | 924.1 | 1020 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.194 | 8.66 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 5.846 | 0.09583 | 12.72 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 33 | 0.6 | 66.3 |
| queue: job turnaround, submitted to done, mean (s) | 184.5 | 286.1 | 225.8 | 330.5 |
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
| worker nodes in service, mean | 12 | 10.21 | −14.9% | −3.2213 to −0.3524 | yes: GAIN |
| node-hours | 5.029 | 4.273 | −15.0% | −1.3568 to −0.1552 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.8 | 524.8 | −0.2% | −2.8310 to +0.8892 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.8 | 468.7 | −10.8% | −101.5345 to −12.5072 | yes: GAIN |
| response time (ms), mean | 759.6 | 830.1 | +9.3% | −18.5915 to +159.4754 | no |
| response time (ms), 95th percentile | 3110 | 3443 | +10.7% | −213.0450 to +877.8460 | no |
| response time (ms), 99th percentile | 4327 | 4818 | +11.3% | +54.6755 to +926.1743 | yes: LOSS |
| time over the response line (% of samples) | 24.81 | 29.46 | +18.8% | +1.4798 to +7.8318 | yes: LOSS |
| failed requests (%) | 0.03524 | 0.1576 | +347.2% | −0.0322 to +0.2770 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.7 | 16.4 | +11.6% | +0.4361 to +2.9639 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 71.4 | +71.400 (native is 0) | +47.7547 to +95.0453 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 40.2 | 69.7 | +73.4% | −16.4487 to +75.4520 | no |
| utilisation (used / allocatable) | 0.03433 | 0.04042 | +17.7% | −0.0005 to +0.0127 | no |
| CPU used (cores), mean | 1.648 | 1.621 | −1.6% | −0.1500 to +0.0966 | no |
| Omni's own CPU (cores), mean | 0 | 0.04441 | +0.044 (native is 0) | +0.0369 to +0.0519 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.648 | 1.666 | +1.1% | −0.1044 to +0.1399 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 774.2 | 694.4 | −10.3% | −182.3319 to +22.7238 | no |
| HPA replicas, mean | 3.964 | 5.35 | +35.0% | +0.4487 to +2.3242 | yes: power given |
| pods started | 0.1 | 3.4 | +3300.0% | +1.4210 to +5.1790 | yes: power given |
| pod start wait, total (s) | 0.2 | 9.1 | +4450.0% | +3.5212 to +14.2788 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 2.096 | +947.9% | +1.0005 to +2.7912 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 57.42 | 62.81 | +9.4% | +4.0076 to +6.7848 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 974.1 | 1020 | +4.7% | +18.4973 to +72.9027 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.66 | −27.8% | −5.7841 to −0.8953 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 5.846 | 12.73 | +117.7% | −1.3857 to +15.1440 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 33 | 66.3 | +100.9% | −35.5770 to +102.1770 | no |
| queue: job turnaround, submitted to done, mean (s) | 286.1 | 330.5 | +15.5% | +12.3237 to +76.5763 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.029 | 5.029 | −0.0% | −0.0163 to +0.0149 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.7 | 525.8 | +0.0% | −1.7908 to +1.8717 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.7 | 525.8 | +0.0% | −1.7908 to +1.8717 | no |
| response time (ms), mean | 612.3 | 759.6 | +24.1% | +40.5884 to +254.1639 | yes: LOSS |
| response time (ms), 95th percentile | 2280 | 3110 | +36.4% | +261.7014 to +1398.5256 | yes: LOSS |
| response time (ms), 99th percentile | 3162 | 4327 | +36.8% | +537.4028 to +1792.6508 | yes: LOSS |
| time over the response line (% of samples) | 21.67 | 24.81 | +14.5% | −0.2619 to +6.5332 | no |
| failed requests (%) | 0 | 0.03524 | +0.035 (native is 0) | −0.0445 to +0.1150 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 14.7 | +44.1% | +2.1097 to +6.8903 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.35 | 40.2 | +131.7% | +2.0116 to +43.6884 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03441 | 0.03433 | −0.2% | −0.0020 to +0.0018 | no |
| CPU used (cores), mean | 1.652 | 1.648 | −0.2% | −0.0960 to +0.0881 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.652 | 1.648 | −0.2% | −0.0960 to +0.0881 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 780.3 | 774.2 | −0.8% | −41.6054 to +29.3761 | no |
| HPA replicas, mean | 4.076 | 3.964 | −2.7% | −0.3213 to +0.0982 | no |
| pods started | 0.4 | 0.1 | −75.0% | −0.8889 to +0.2889 | no |
| pod start wait, total (s) | 0.8 | 0.2 | −75.0% | −1.7778 to +0.5778 | no |
| pod start wait, mean (s) | 0.6 | 0.2 | −66.7% | −1.3048 to +0.5048 | no |
| host CPU busy, the real machine under kind (%) | 51.3 | 57.42 | +11.9% | +4.6481 to +7.5919 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 876 | 974.1 | +11.2% | +44.8146 to +151.3854 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 5.846 | +4737.9% | −0.9759 to +12.4259 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 33 | +6500.0% | −37.5102 to +102.5102 | no |
| queue: job turnaround, submitted to done, mean (s) | 184.5 | 286.1 | +55.0% | +46.6668 to +156.4749 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.59 | −11.7% | −2.5071 to −0.3080 | yes: GAIN |
| node-hours | 5.029 | 4.441 | −11.7% | −1.0512 to −0.1255 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.7 | 527.3 | +0.3% | +0.3778 to +2.7667 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.7 | 483 | −8.1% | −78.0684 to −7.2913 | yes: GAIN |
| response time (ms), mean | 612.3 | 721.5 | +17.8% | +17.7061 to +200.8441 | yes: LOSS |
| response time (ms), 95th percentile | 2280 | 2978 | +30.6% | +285.4880 to +1111.1060 | yes: LOSS |
| response time (ms), 99th percentile | 3162 | 3978 | +25.8% | +303.9307 to +1326.9715 | yes: LOSS |
| time over the response line (% of samples) | 21.67 | 24.99 | +15.3% | +1.1767 to +5.4701 | yes: LOSS |
| failed requests (%) | 0 | 0.007168 | +0.007 (native is 0) | −0.0090 to +0.0234 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 13.8 | +35.3% | +0.7950 to +6.4050 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 134 | +134.000 (native is 0) | +61.8891 to +206.1109 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.35 | 19.37 | +11.7% | +0.4401 to +3.6032 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03441 | 0.04075 | +18.4% | +0.0034 to +0.0093 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.652 | 1.736 | +5.1% | +0.0169 to +0.1508 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05616 | +0.056 (native is 0) | +0.0513 to +0.0611 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.652 | 1.792 | +8.5% | +0.0703 to +0.2098 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 780.3 | 676.3 | −13.3% | −156.5142 to −51.6021 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.076 | 4.764 | +16.9% | +0.3648 to +1.0114 | yes: power given |
| pods started | 0.4 | 2.9 | +625.0% | +1.1407 to +3.8593 | yes: power given |
| pod start wait, total (s) | 0.8 | 7.6 | +850.0% | +3.4483 to +10.1517 | yes: LOSS |
| pod start wait, mean (s) | 0.6 | 2.31 | +285.0% | +0.9027 to +2.5173 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.3 | 57.47 | +12.0% | +4.8895 to +7.4549 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 876 | 924.1 | +5.5% | +17.4066 to +78.7934 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.194 | −23.4% | −4.9284 to −0.6835 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 0.09583 | −20.7% | −0.0955 to +0.0455 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.6 | +20.0% | −0.4278 to +0.6278 | no |
| queue: job turnaround, submitted to done, mean (s) | 184.5 | 225.8 | +22.4% | +18.6438 to +63.9812 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.59 | −11.7% | −2.5071 to −0.3080 | yes: GAIN |
| node-hours | 5.029 | 4.441 | −11.7% | −1.0491 to −0.1262 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.8 | 527.3 | +0.3% | −0.5558 to +3.6194 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.8 | 483 | −8.1% | −78.6386 to −6.8020 | yes: GAIN |
| response time (ms), mean | 759.6 | 721.5 | −5.0% | −109.4552 to +33.2531 | no |
| response time (ms), 95th percentile | 3110 | 2978 | −4.2% | −449.9699 to +186.3369 | no |
| response time (ms), 99th percentile | 4327 | 3978 | −8.1% | −689.9756 to −9.1758 | yes: GAIN |
| time over the response line (% of samples) | 24.81 | 24.99 | +0.8% | −3.0076 to +3.3831 | no |
| failed requests (%) | 0.03524 | 0.007168 | −79.7% | −0.1112 to +0.0550 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.7 | 13.8 | −6.1% | −2.3871 to +0.5871 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 134 | +134.000 (native is 0) | +61.8891 to +206.1109 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 40.2 | 19.37 | −51.8% | −42.2493 to +0.5926 | no |
| utilisation (used / allocatable) | 0.03433 | 0.04075 | +18.7% | +0.0037 to +0.0092 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.648 | 1.736 | +5.3% | −0.0394 to +0.2150 | no |
| Omni's own CPU (cores), mean | 0 | 0.05616 | +0.056 (native is 0) | +0.0513 to +0.0611 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.648 | 1.792 | +8.7% | +0.0137 to +0.2743 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 774.2 | 676.3 | −12.7% | −142.2589 to −53.6282 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.964 | 4.764 | +20.2% | +0.4719 to +1.1274 | yes: power given |
| pods started | 0.1 | 2.9 | +2800.0% | +1.6417 to +3.9583 | yes: power given |
| pod start wait, total (s) | 0.2 | 7.6 | +3700.0% | +4.3058 to +10.4942 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 2.31 | +1055.0% | +1.2777 to +2.9423 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 57.42 | 57.47 | +0.1% | −0.7222 to +0.8266 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 974.1 | 924.1 | −5.1% | −79.9253 to −20.0747 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.194 | −23.4% | −4.9284 to −0.6835 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 5.846 | 0.09583 | −98.4% | −12.5054 to +1.0054 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 33 | 0.6 | −98.2% | −102.6882 to +37.8882 | no |
| queue: job turnaround, submitted to done, mean (s) | 286.1 | 225.8 | −21.1% | −101.3543 to −19.1624 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.21 | −14.9% | −3.2213 to −0.3524 | yes: GAIN |
| node-hours | 5.029 | 4.273 | −15.0% | −1.3591 to −0.1543 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.7 | 524.8 | −0.2% | −3.5516 to +1.6908 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.7 | 468.7 | −10.8% | −101.0175 to −12.9434 | yes: GAIN |
| response time (ms), mean | 612.3 | 830.1 | +35.6% | +78.6437 to +356.9925 | yes: LOSS |
| response time (ms), 95th percentile | 2280 | 3443 | +51.0% | +468.4487 to +1856.5793 | yes: LOSS |
| response time (ms), 99th percentile | 3162 | 4818 | +52.4% | +868.6385 to +2442.2649 | yes: LOSS |
| time over the response line (% of samples) | 21.67 | 29.46 | +36.0% | +3.1665 to +12.4164 | yes: LOSS |
| failed requests (%) | 0 | 0.1576 | +0.158 (native is 0) | −0.0450 to +0.3602 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 16.4 | +60.8% | +3.3427 to +9.0573 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 71.4 | +71.400 (native is 0) | +47.7547 to +95.0453 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.35 | 69.7 | +301.8% | −2.9397 to +107.6430 | no |
| utilisation (used / allocatable) | 0.03441 | 0.04042 | +17.5% | −0.0014 to +0.0134 | no |
| CPU used (cores), mean | 1.652 | 1.621 | −1.9% | −0.1699 to +0.1086 | no |
| Omni's own CPU (cores), mean | 0 | 0.04441 | +0.044 (native is 0) | +0.0369 to +0.0519 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.652 | 1.666 | +0.8% | −0.1217 to +0.1492 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 780.3 | 694.4 | −11.0% | −206.1879 to +34.3506 | no |
| HPA replicas, mean | 4.076 | 5.35 | +31.3% | +0.3108 to +2.2390 | yes: power given |
| pods started | 0.4 | 3.4 | +750.0% | +0.7380 to +5.2620 | yes: power given |
| pod start wait, total (s) | 0.8 | 9.1 | +1037.5% | +2.2112 to +14.3888 | yes: LOSS |
| pod start wait, mean (s) | 0.6 | 2.096 | +249.3% | +0.2761 to +2.7155 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.3 | 62.81 | +22.4% | +9.3791 to +13.6533 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 876 | 1020 | +16.4% | +75.6509 to +211.9491 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.66 | −27.8% | −5.7841 to −0.8953 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 12.73 | +10431.0% | −1.4952 to +26.7036 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 66.3 | +13160.0% | −30.2525 to +161.8525 | no |
| queue: job turnaround, submitted to done, mean (s) | 184.5 | 330.5 | +79.1% | +78.9413 to +213.1004 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*