# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.65 | 11.58 |
| node-hours | 5.035 | 5.02 | 4.458 | 4.848 |
| energy, parked workers still on at idle power (Wh, declared model) | 527.9 | 525.5 | 527.1 | 528.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.9 | 525.5 | 484.6 | 515.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 741.8 | 1099 | 761.8 | 1120 |
| response time (ms), 95th percentile | 2989 | 4035 | 3189 | 4258 |
| response time (ms), 99th percentile | 4048 | 5060 | 4283 | 5729 |
| time over the response line (% of samples) | 24.66 | 35.56 | 25.82 | 42.29 |
| failed requests (%) | 0 | 0.08424 | 0 | 0.3467 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.5 | 15.4 | 12.9 | 18.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 63 | 38.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.13 | 58.4 | 25.44 | 47.49 |
| utilisation (used / allocatable) | 0.03663 | 0.03567 | 0.04156 | 0.04051 |
| CPU used (cores), mean | 1.758 | 1.712 | 1.757 | 1.88 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01354 | 0.01279 |
| CPU used with Omni's own (cores), mean | 1.758 | 1.712 | 1.771 | 1.893 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 737.2 | 746.5 | 666.3 | 663.5 |
| HPA replicas, mean | 3.97 | 4.218 | 4.194 | 4.792 |
| pods started | 0.2 | 0.1 | 0.4 | 1.2 |
| pod start wait, total (s) | 0.4 | 0.3 | 0.6 | 3 |
| pod start wait, mean (s) | 0.4 | 0.3 | 0.6 | 1.6 |
| host CPU busy, the real machine under kind (%) | 53.87 | 61.22 | 56.2 | 64.63 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 924 | 1050 | 946.3 | 1100 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.734 | 11.01 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 9.083 | 0.1208 | 27.5 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 82.7 | 0.7 | 135.2 |
| queue: job turnaround, submitted to done, mean (s) | 227.7 | 341.8 | 245.9 | 366.9 |
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
| worker nodes in service, mean | 12 | 11.58 | −3.5% | −0.9195 to +0.0712 | no |
| node-hours | 5.02 | 4.848 | −3.4% | −0.3815 to +0.0369 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.5 | 528.7 | +0.6% | +0.1524 to +6.1718 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.5 | 515.4 | −1.9% | −25.6742 to +5.3525 | no |
| response time (ms), mean | 1099 | 1120 | +1.9% | −118.9284 to +160.7808 | no |
| response time (ms), 95th percentile | 4035 | 4258 | +5.5% | −428.3391 to +875.6951 | no |
| response time (ms), 99th percentile | 5060 | 5729 | +13.2% | +110.7676 to +1227.8474 | yes: LOSS |
| time over the response line (% of samples) | 35.56 | 42.29 | +18.9% | −1.1099 to +14.5763 | no |
| failed requests (%) | 0.08424 | 0.3467 | +311.5% | −0.0709 to +0.5958 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.4 | 18.5 | +20.1% | −0.3130 to +6.5130 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.5 | +38.500 (native is 0) | +30.3147 to +46.6853 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 58.4 | 47.49 | −18.7% | −61.6838 to +39.8571 | no |
| utilisation (used / allocatable) | 0.03567 | 0.04051 | +13.6% | +0.0012 to +0.0085 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.712 | 1.88 | +9.8% | +0.0218 to +0.3138 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01279 | +0.013 (native is 0) | +0.0118 to +0.0137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.712 | 1.893 | +10.5% | +0.0346 to +0.3266 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 746.5 | 663.5 | −11.1% | −148.9087 to −17.1170 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.218 | 4.792 | +13.6% | −0.4646 to +1.6132 | no |
| pods started | 0.1 | 1.2 | +1100.0% | −0.0410 to +2.2410 | no |
| pod start wait, total (s) | 0.3 | 3 | +900.0% | −0.6896 to +6.0896 | no |
| pod start wait, mean (s) | 0.3 | 1.6 | +433.3% | −0.0081 to +2.6081 | no |
| host CPU busy, the real machine under kind (%) | 61.22 | 64.63 | +5.6% | +1.3248 to +5.4998 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1050 | 1100 | +4.8% | +13.8961 to +86.1039 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.01 | −8.2% | −2.1535 to +0.1738 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 9.083 | 27.5 | +202.7% | −7.0430 to +43.8680 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 82.7 | 135.2 | +63.5% | −90.2656 to +195.2656 | no |
| queue: job turnaround, submitted to done, mean (s) | 341.8 | 366.9 | +7.3% | −27.3854 to +77.5854 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.035 | 5.02 | −0.3% | −0.0271 to −0.0035 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 527.9 | 525.5 | −0.5% | −4.3571 to −0.4362 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.9 | 525.5 | −0.5% | −4.3571 to −0.4362 | yes: GAIN |
| response time (ms), mean | 741.8 | 1099 | +48.2% | +158.8563 to +556.5478 | yes: LOSS |
| response time (ms), 95th percentile | 2989 | 4035 | +35.0% | +559.0279 to +1533.1491 | yes: LOSS |
| response time (ms), 99th percentile | 4048 | 5060 | +25.0% | +532.7345 to +1491.4391 | yes: LOSS |
| time over the response line (% of samples) | 24.66 | 35.56 | +44.2% | +6.9035 to +14.8924 | yes: LOSS |
| failed requests (%) | 0 | 0.08424 | +0.084 (native is 0) | −0.0532 to +0.2217 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.5 | 15.4 | +23.2% | +1.7590 to +4.0410 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.13 | 58.41 | +222.1% | +7.2298 to +73.3136 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03663 | 0.03567 | −2.6% | −0.0030 to +0.0011 | no |
| CPU used (cores), mean | 1.758 | 1.712 | −2.6% | −0.1434 to +0.0510 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.758 | 1.712 | −2.6% | −0.1434 to +0.0510 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 737.2 | 746.5 | +1.3% | −25.6119 to +44.1634 | no |
| HPA replicas, mean | 3.97 | 4.218 | +6.2% | −0.1722 to +0.6666 | no |
| pods started | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| pod start wait, total (s) | 0.4 | 0.3 | −25.0% | −1.0802 to +0.8802 | no |
| pod start wait, mean (s) | 0.4 | 0.3 | −25.0% | −1.0802 to +0.8802 | no |
| host CPU busy, the real machine under kind (%) | 53.87 | 61.22 | +13.6% | +5.1237 to +9.5744 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 924 | 1050 | +13.6% | +58.3125 to +193.8875 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 9.083 | +10800.0% | +0.1287 to +17.8713 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 82.7 | +16440.0% | −14.7333 to +179.1333 | no |
| queue: job turnaround, submitted to done, mean (s) | 227.7 | 341.8 | +50.1% | +53.7159 to +174.4508 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.65 | −11.3% | −2.9052 to +0.2009 | no |
| node-hours | 5.035 | 4.458 | −11.5% | −1.2283 to +0.0735 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.9 | 527.1 | −0.2% | −2.6359 to +0.8818 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.9 | 484.6 | −8.2% | −92.2284 to +5.5118 | no |
| response time (ms), mean | 741.8 | 761.8 | +2.7% | −7.7704 to +47.8934 | no |
| response time (ms), 95th percentile | 2989 | 3189 | +6.7% | −32.8842 to +432.8912 | no |
| response time (ms), 99th percentile | 4048 | 4283 | +5.8% | +5.1030 to +466.0740 | yes: LOSS |
| time over the response line (% of samples) | 24.66 | 25.82 | +4.7% | +0.5259 to +1.7986 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.5 | 12.9 | +3.2% | +0.0306 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 63 | +63.000 (native is 0) | +30.5885 to +95.4115 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.13 | 25.44 | +40.3% | −3.8466 to +18.4666 | no |
| utilisation (used / allocatable) | 0.03663 | 0.04156 | +13.5% | −0.0005 to +0.0104 | no |
| CPU used (cores), mean | 1.758 | 1.757 | −0.1% | −0.0675 to +0.0653 | no |
| Omni's own CPU (cores), mean | 0 | 0.01354 | +0.014 (native is 0) | +0.0123 to +0.0148 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.758 | 1.771 | +0.7% | −0.0537 to +0.0786 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 737.2 | 666.3 | −9.6% | −146.4050 to +4.5989 | no |
| HPA replicas, mean | 3.97 | 4.194 | +5.6% | −0.0182 to +0.4650 | no |
| pods started | 0.2 | 0.4 | +100.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.4 | 0.6 | +50.0% | −0.6793 to +1.0793 | no |
| pod start wait, mean (s) | 0.4 | 0.6 | +50.0% | −0.6793 to +1.0793 | no |
| host CPU busy, the real machine under kind (%) | 53.87 | 56.2 | +4.3% | +1.8096 to +2.8511 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 924 | 946.3 | +2.4% | +4.7850 to +39.8150 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.734 | −18.9% | −4.7623 to +0.2309 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.1208 | +45.0% | −0.0334 to +0.1084 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.7 | +40.0% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 227.7 | 245.9 | +8.0% | +8.9503 to +27.4247 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.65 | −11.3% | −2.9052 to +0.2009 | no |
| node-hours | 5.02 | 4.458 | −11.2% | −1.2132 to +0.0890 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.5 | 527.1 | +0.3% | −0.1367 to +3.1758 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.5 | 484.6 | −7.8% | −90.3926 to +8.4692 | no |
| response time (ms), mean | 1099 | 761.8 | −30.7% | −521.8524 to −153.4286 | yes: GAIN |
| response time (ms), 95th percentile | 4035 | 3189 | −21.0% | −1343.0806 to −349.0894 | yes: GAIN |
| response time (ms), 99th percentile | 5060 | 4283 | −15.3% | −1264.3416 to −288.6550 | yes: GAIN |
| time over the response line (% of samples) | 35.56 | 25.82 | −27.4% | −13.5922 to −5.8792 | yes: GAIN |
| failed requests (%) | 0.08424 | 0 | −100.0% | −0.2217 to +0.0532 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.4 | 12.9 | −16.2% | −3.5256 to −1.4744 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 63 | +63.000 (native is 0) | +30.5885 to +95.4115 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 58.4 | 25.44 | −56.4% | −64.6408 to −1.2826 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03567 | 0.04156 | +16.5% | +0.0012 to +0.0106 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.712 | 1.757 | +2.6% | −0.0597 to +0.1499 | no |
| Omni's own CPU (cores), mean | 0 | 0.01354 | +0.014 (native is 0) | +0.0123 to +0.0148 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.712 | 1.771 | +3.4% | −0.0458 to +0.1630 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 746.5 | 666.3 | −10.7% | −140.4053 to −19.9524 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.218 | 4.194 | −0.6% | −0.4148 to +0.3672 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.3 | 0.6 | +100.0% | −0.7144 to +1.3144 | no |
| pod start wait, mean (s) | 0.3 | 0.6 | +100.0% | −0.7144 to +1.3144 | no |
| host CPU busy, the real machine under kind (%) | 61.22 | 56.2 | −8.2% | −6.8566 to −3.1808 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1050 | 946.3 | −9.9% | −155.7788 to −51.8212 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.734 | −18.9% | −4.7623 to +0.2309 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 9.083 | 0.1208 | −98.7% | −17.8262 to −0.0988 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 82.7 | 0.7 | −99.2% | −178.9891 to +14.9891 | no |
| queue: job turnaround, submitted to done, mean (s) | 341.8 | 245.9 | −28.1% | −148.4321 to −43.3596 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.58 | −3.5% | −0.9195 to +0.0712 | no |
| node-hours | 5.035 | 4.848 | −3.7% | −0.3966 to +0.0213 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.9 | 528.7 | +0.1% | −0.9350 to +2.4659 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.9 | 515.4 | −2.4% | −27.3343 to +2.2194 | no |
| response time (ms), mean | 741.8 | 1120 | +51.0% | +243.2756 to +513.9809 | yes: LOSS |
| response time (ms), 95th percentile | 2989 | 4258 | +42.5% | +789.1653 to +1750.3677 | yes: LOSS |
| response time (ms), 99th percentile | 4048 | 5729 | +41.5% | +1122.6977 to +2240.0909 | yes: LOSS |
| time over the response line (% of samples) | 24.66 | 42.29 | +71.5% | +13.3604 to +21.9019 | yes: LOSS |
| failed requests (%) | 0 | 0.3467 | +0.347 (native is 0) | −0.0565 to +0.7499 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.5 | 18.5 | +48.0% | +2.7833 to +9.2167 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.5 | +38.500 (native is 0) | +30.3147 to +46.6853 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.13 | 47.49 | +161.9% | −5.0641 to +63.7808 | no |
| utilisation (used / allocatable) | 0.03663 | 0.04051 | +10.6% | +0.0005 to +0.0073 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.758 | 1.88 | +6.9% | +0.0142 to +0.2291 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01279 | +0.013 (native is 0) | +0.0118 to +0.0137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.758 | 1.893 | +7.6% | +0.0272 to +0.2416 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 737.2 | 663.5 | −10.0% | −144.8532 to −2.6209 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.97 | 4.792 | +20.7% | −0.2758 to +1.9188 | no |
| pods started | 0.2 | 1.2 | +500.0% | −0.1681 to +2.1681 | no |
| pod start wait, total (s) | 0.4 | 3 | +650.0% | −0.7585 to +5.9585 | no |
| pod start wait, mean (s) | 0.4 | 1.6 | +300.0% | +0.0417 to +2.3583 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 53.87 | 64.63 | +20.0% | +9.5853 to +11.9374 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 924 | 1100 | +19.1% | +135.5288 to +216.6712 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.01 | −8.2% | −2.1535 to +0.1738 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 27.5 | +32895.0% | +1.1754 to +53.6496 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 135.2 | +26940.0% | +22.6880 to +246.7120 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 227.7 | 366.9 | +61.1% | +104.2384 to +174.1283 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*