# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.248 | 4.955 |
| node-hours | 2.511 | 2.516 | 2.2 | 2.076 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273.6 | 273.8 | 273.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 273.6 | 250.2 | 240.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 428.7 | 352.6 | 406.5 | 352.1 |
| response time (ms), 95th percentile | 1599 | 1456 | 1713 | 1642 |
| response time (ms), 99th percentile | 2319 | 2367 | 2496 | 2605 |
| time over the response line (% of samples) | 18.78 | 13.84 | 18.57 | 14.56 |
| failed requests (%) | 0 | 0.01176 | 0 | 0.02352 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.333 | 8.556 | 9.889 | 8.667 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 96.56 | 82.22 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.73 | 17.83 | 12.01 | 21.51 |
| utilisation (used / allocatable) | 0.06346 | 0.06281 | 0.07309 | 0.07557 |
| CPU used (cores), mean | 1.523 | 1.507 | 1.508 | 1.493 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07202 | 0.07512 |
| CPU used with Omni's own (cores), mean | 1.523 | 1.507 | 1.58 | 1.568 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 442.7 | 450.5 | 399.5 | 393.8 |
| HPA replicas, mean | 1.898 | 2.017 | 2.396 | 2.149 |
| pods started | 0.2222 | 0 | 1.444 | 0.4444 |
| pod start wait, total (s) | 0.5556 | 0 | 3.667 | 1.222 |
| pod start wait, mean (s) | 0.5556 | 0 | 1.472 | 0.6296 |
| host CPU busy, the real machine under kind (%) | 43.18 | 43.89 | 45.98 | 47.16 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 812.3 | 826.9 | 819.9 | 837.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.882 | 4.299 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.8333 | 0.125 | 1.046 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5556 | 1.889 | 0.5556 | 3.222 |
| queue: job turnaround, submitted to done, mean (s) | 117.9 | 136.8 | 123.9 | 148.6 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.955 | −17.4% | −2.0086 to −0.0815 | yes: GAIN |
| node-hours | 2.516 | 2.076 | −17.5% | −0.8384 to −0.0423 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.3 | −0.1% | −1.3899 to +0.8074 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 240.5 | −12.1% | −63.3108 to −2.9384 | yes: GAIN |
| response time (ms), mean | 352.6 | 352.1 | −0.1% | −35.7373 to +34.7304 | no |
| response time (ms), 95th percentile | 1456 | 1642 | +12.8% | −125.2297 to +497.1519 | no |
| response time (ms), 99th percentile | 2367 | 2605 | +10.1% | −27.2153 to +503.3107 | no |
| time over the response line (% of samples) | 13.84 | 14.56 | +5.2% | +0.0747 to +1.3703 | yes: LOSS |
| failed requests (%) | 0.01176 | 0.02352 | +100.0% | −0.0155 to +0.0390 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.556 | 8.667 | +1.3% | −0.6991 to +0.9214 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 82.22 | +82.222 (native is 0) | +20.8410 to +143.6035 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.83 | 21.51 | +20.6% | +0.1166 to +7.2315 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06281 | 0.07557 | +20.3% | +0.0011 to +0.0244 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.507 | 1.493 | −1.0% | −0.0786 to +0.0493 | no |
| Omni's own CPU (cores), mean | 0 | 0.07512 | +0.075 (native is 0) | +0.0664 to +0.0839 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.507 | 1.568 | +4.0% | −0.0104 to +0.1313 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.5 | 393.8 | −12.6% | −108.3368 to −5.0920 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.017 | 2.149 | +6.5% | −0.1184 to +0.3821 | no |
| pods started | 0 | 0.4444 | +0.444 (native is 0) | −0.3348 to +1.2237 | no |
| pod start wait, total (s) | 0 | 1.222 | +1.222 (native is 0) | −0.8750 to +3.3195 | no |
| pod start wait, mean (s) | 0 | 0.6296 | +0.630 (native is 0) | −0.3329 to +1.5921 | no |
| host CPU busy, the real machine under kind (%) | 43.89 | 47.16 | +7.4% | +2.5341 to +3.9932 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 826.9 | 837.7 | +1.3% | +2.7916 to +18.7639 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.299 | −28.3% | −3.1340 to −0.2677 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8333 | 1.046 | +25.6% | −0.0655 to +0.4915 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.889 | 3.222 | +70.6% | −0.7717 to +3.4384 | no |
| queue: job turnaround, submitted to done, mean (s) | 136.8 | 148.6 | +8.7% | +1.7801 to +21.9513 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.511 | 2.516 | +0.2% | −0.0042 to +0.0153 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273.6 | +0.1% | −1.0216 to +1.6994 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 273.6 | +0.1% | −1.0216 to +1.6994 | no |
| response time (ms), mean | 428.7 | 352.6 | −17.7% | −121.9020 to −30.2103 | yes: GAIN |
| response time (ms), 95th percentile | 1599 | 1456 | −8.9% | −336.9169 to +51.8313 | no |
| response time (ms), 99th percentile | 2319 | 2367 | +2.1% | −212.5377 to +308.2899 | no |
| time over the response line (% of samples) | 18.78 | 13.84 | −26.3% | −8.2913 to −1.5986 | yes: GAIN |
| failed requests (%) | 0 | 0.01176 | +0.012 (native is 0) | −0.0154 to +0.0389 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.333 | 8.556 | −8.3% | −2.3044 to +0.7488 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.73 | 17.83 | +66.2% | +1.4315 to +12.7722 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06346 | 0.06281 | −1.0% | −0.0020 to +0.0007 | no |
| CPU used (cores), mean | 1.523 | 1.507 | −1.0% | −0.0489 to +0.0174 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.523 | 1.507 | −1.0% | −0.0489 to +0.0174 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 442.7 | 450.5 | +1.8% | −5.4235 to +21.0339 | no |
| HPA replicas, mean | 1.898 | 2.017 | +6.2% | +0.0411 to +0.1959 | yes: power given |
| pods started | 0.2222 | 0 | −100.0% | −0.5612 to +0.1167 | no |
| pod start wait, total (s) | 0.5556 | 0 | −100.0% | −1.4244 to +0.3133 | no |
| pod start wait, mean (s) | 0.5556 | 0 | −100.0% | −1.4244 to +0.3133 | no |
| host CPU busy, the real machine under kind (%) | 43.18 | 43.89 | +1.6% | +0.0894 to +1.3268 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.3 | 826.9 | +1.8% | +3.1020 to +26.0091 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.8333 | +900.0% | +0.5724 to +0.9276 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5556 | 1.889 | +240.0% | +0.6676 to +1.9990 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 117.9 | 136.8 | +16.0% | +4.7069 to +33.0801 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.248 | −12.5% | −1.6919 to +0.1878 | no |
| node-hours | 2.511 | 2.2 | −12.4% | −0.7060 to +0.0853 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273.8 | +0.2% | −0.5328 to +1.5741 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 250.2 | −8.5% | −52.9681 to +6.7686 | no |
| response time (ms), mean | 428.7 | 406.5 | −5.2% | −38.3271 to −6.0786 | yes: GAIN |
| response time (ms), 95th percentile | 1599 | 1713 | +7.1% | −5.8822 to +234.1344 | no |
| response time (ms), 99th percentile | 2319 | 2496 | +7.6% | +12.5805 to +341.5320 | yes: LOSS |
| time over the response line (% of samples) | 18.78 | 18.57 | −1.1% | −1.0366 to +0.6242 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.333 | 9.889 | +6.0% | −0.2237 to +1.3348 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 96.56 | +96.556 (native is 0) | +25.5047 to +167.6064 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.73 | 12.01 | +12.0% | −1.6590 to +4.2294 | no |
| utilisation (used / allocatable) | 0.06346 | 0.07309 | +15.2% | −0.0027 to +0.0220 | no |
| CPU used (cores), mean | 1.523 | 1.508 | −1.0% | −0.0425 to +0.0127 | no |
| Omni's own CPU (cores), mean | 0 | 0.07202 | +0.072 (native is 0) | +0.0644 to +0.0797 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.523 | 1.58 | +3.8% | +0.0233 to +0.0909 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 442.7 | 399.5 | −9.7% | −99.3710 to +13.0867 | no |
| HPA replicas, mean | 1.898 | 2.396 | +26.2% | +0.3060 to +0.6892 | yes: power given |
| pods started | 0.2222 | 1.444 | +550.0% | −0.0968 to +2.5412 | no |
| pod start wait, total (s) | 0.5556 | 3.667 | +560.0% | −0.0452 to +6.2674 | no |
| pod start wait, mean (s) | 0.5556 | 1.472 | +165.0% | +0.0153 to +1.8180 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.18 | 45.98 | +6.5% | +2.2853 to +3.3130 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.3 | 819.9 | +0.9% | +0.3951 to +14.7160 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.882 | −18.6% | −2.4350 to +0.1994 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.125 | +50.0% | −0.0596 to +0.1429 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5556 | 0.5556 | ±0.0% | −0.3843 to +0.3843 | no |
| queue: job turnaround, submitted to done, mean (s) | 117.9 | 123.9 | +5.1% | +0.5498 to +11.5243 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 9 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.248 | −12.5% | −1.6919 to +0.1878 | no |
| node-hours | 2.516 | 2.2 | −12.6% | −0.7057 to +0.0740 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.8 | +0.1% | −0.8810 to +1.2446 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 250.2 | −8.6% | −52.2936 to +5.4164 | no |
| response time (ms), mean | 352.6 | 406.5 | +15.3% | +4.9392 to +102.7673 | yes: LOSS |
| response time (ms), 95th percentile | 1456 | 1713 | +17.6% | +17.5303 to +495.8074 | yes: LOSS |
| response time (ms), 99th percentile | 2367 | 2496 | +5.5% | +14.8384 to +243.5218 | yes: LOSS |
| time over the response line (% of samples) | 13.84 | 18.57 | +34.3% | +1.8521 to +7.6255 | yes: LOSS |
| failed requests (%) | 0.01176 | 0 | −100.0% | −0.0389 to +0.0154 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.556 | 9.889 | +15.6% | −0.5883 to +3.2550 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 96.56 | +96.556 (native is 0) | +25.5047 to +167.6064 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.83 | 12.01 | −32.6% | −10.2311 to −1.4023 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06281 | 0.07309 | +16.4% | −0.0031 to +0.0236 | no |
| CPU used (cores), mean | 1.507 | 1.508 | +0.1% | −0.0114 to +0.0131 | no |
| Omni's own CPU (cores), mean | 0 | 0.07202 | +0.072 (native is 0) | +0.0644 to +0.0797 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.507 | 1.58 | +4.8% | +0.0596 to +0.0861 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.5 | 399.5 | −11.3% | −116.8598 to +14.9651 | no |
| HPA replicas, mean | 2.017 | 2.396 | +18.8% | +0.1858 to +0.5723 | yes: power given |
| pods started | 0 | 1.444 | +1.444 (native is 0) | +0.1633 to +2.7256 | yes: power given |
| pod start wait, total (s) | 0 | 3.667 | +3.667 (native is 0) | +0.5681 to +6.7653 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.472 | +1.472 (native is 0) | +0.3833 to +2.5612 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.89 | 45.98 | +4.8% | +1.6667 to +2.5155 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 826.9 | 819.9 | −0.8% | −14.6771 to +0.6771 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.882 | −18.6% | −2.4350 to +0.1994 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8333 | 0.125 | −85.0% | −0.8603 to −0.5564 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.889 | 0.5556 | −70.6% | −1.8769 to −0.7898 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 136.8 | 123.9 | −9.4% | −24.4709 to −1.2421 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.955 | −17.4% | −2.0086 to −0.0815 | yes: GAIN |
| node-hours | 2.511 | 2.076 | −17.3% | −0.8398 to −0.0298 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273.3 | +0.0% | −1.1281 to +1.2234 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 240.5 | −12.0% | −64.1127 to −1.4587 | yes: GAIN |
| response time (ms), mean | 428.7 | 352.1 | −17.9% | −103.3870 to −49.7322 | yes: GAIN |
| response time (ms), 95th percentile | 1599 | 1642 | +2.7% | −122.0416 to +208.8783 | no |
| response time (ms), 99th percentile | 2319 | 2605 | +12.3% | −83.1196 to +654.9672 | no |
| time over the response line (% of samples) | 18.78 | 14.56 | −22.5% | −7.0344 to −1.4106 | yes: GAIN |
| failed requests (%) | 0 | 0.02352 | +0.024 (native is 0) | −0.0124 to +0.0594 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.333 | 8.667 | −7.1% | −1.9414 to +0.6080 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 82.22 | +82.222 (native is 0) | +20.8410 to +143.6035 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.73 | 21.51 | +100.4% | +3.1439 to +18.4079 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06346 | 0.07557 | +19.1% | +0.0016 to +0.0226 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.523 | 1.493 | −2.0% | −0.1097 to +0.0490 | no |
| Omni's own CPU (cores), mean | 0 | 0.07512 | +0.075 (native is 0) | +0.0664 to +0.0839 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.523 | 1.568 | +2.9% | −0.0423 to +0.1318 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 442.7 | 393.8 | −11.0% | −89.8270 to −7.9914 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.898 | 2.149 | +13.2% | +0.0537 to +0.4470 | yes: power given |
| pods started | 0.2222 | 0.4444 | +100.0% | −0.4183 to +0.8628 | no |
| pod start wait, total (s) | 0.5556 | 1.222 | +120.0% | −1.2550 to +2.5883 | no |
| pod start wait, mean (s) | 0.5556 | 0.6296 | +13.3% | −1.0915 to +1.2397 | no |
| host CPU busy, the real machine under kind (%) | 43.18 | 47.16 | +9.2% | +3.0611 to +4.8824 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.3 | 837.7 | +3.1% | +8.2792 to +42.3875 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.299 | −28.3% | −3.1340 to −0.2677 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 1.046 | +1155.6% | +0.6494 to +1.2765 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5556 | 3.222 | +480.0% | +0.6696 to +4.6637 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 117.9 | 148.6 | +26.1% | +10.7453 to +50.7732 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*