# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 3.849 | 3.94 |
| node-hours | 2.512 | 2.515 | 1.615 | 1.651 |
| energy, parked workers still on at idle power (Wh, declared model) | 269.5 | 269.8 | 269.8 | 269.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.5 | 269.8 | 202.1 | 204.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 135.8 | 120.7 | 120.2 | 96.09 |
| response time (ms), 95th percentile | 333.7 | 223.6 | 383.5 | 223.7 |
| response time (ms), 99th percentile | 449.4 | 326.3 | 521.6 | 367.6 |
| time over the response line (% of samples) | 1.134 | 0.4223 | 1.903 | 0.6342 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 0.5 | 3.6 | 1.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 230.1 | 165.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 51.68 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.9 | 11.31 | 7.77 | 11.22 |
| utilisation (used / allocatable) | 0.05269 | 0.05262 | 0.08285 | 0.08043 |
| CPU used (cores), mean | 1.265 | 1.263 | 1.223 | 1.224 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06678 | 0.06692 |
| CPU used with Omni's own (cores), mean | 1.265 | 1.263 | 1.289 | 1.291 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 509.6 | 513.6 | 392.1 | 397.1 |
| HPA replicas, mean | 1.912 | 1.922 | 2.077 | 2.068 |
| pods started | 0 | 0.2 | 0.5 | 0.5 |
| pod start wait, total (s) | 0 | 0.4 | 1.1 | 1.4 |
| pod start wait, mean (s) | 0 | 0.4 | 0.8 | 0.6 |
| host CPU busy, the real machine under kind (%) | 35.9 | 37.36 | 39.2 | 39.66 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 723.1 | 729.4 | 727.2 | 728.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 2.89 | 2.883 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.008333 | 0.6375 | 0.02083 | 0.65 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 1 | 0.1 | 1 |
| queue: job turnaround, submitted to done, mean (s) | 29.85 | 35.36 | 32.22 | 35.57 |
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
| worker nodes in service, mean | 6 | 3.94 | −34.3% | −2.7743 to −1.3463 | yes: GAIN |
| node-hours | 2.515 | 1.651 | −34.4% | −1.1664 to −0.5616 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.8 | 269.2 | −0.2% | −1.4893 to +0.3014 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.8 | 204.5 | −24.2% | −88.2194 to −42.4185 | yes: GAIN |
| response time (ms), mean | 120.7 | 96.09 | −20.4% | −29.4472 to −19.8486 | yes: GAIN |
| response time (ms), 95th percentile | 223.6 | 223.7 | +0.0% | −23.0096 to +23.1626 | no |
| response time (ms), 99th percentile | 326.3 | 367.6 | +12.6% | −21.8390 to +104.3728 | no |
| time over the response line (% of samples) | 0.4223 | 0.6342 | +50.2% | −0.0775 to +0.5013 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.5 | 1.1 | +120.0% | −0.1689 to +1.3689 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 165.3 | +165.300 (native is 0) | +117.1312 to +213.4688 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.31 | 11.23 | −0.7% | −1.1064 to +0.9464 | no |
| utilisation (used / allocatable) | 0.05262 | 0.08043 | +52.8% | +0.0160 to +0.0397 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.263 | 1.224 | −3.1% | −0.0788 to +0.0003 | no |
| Omni's own CPU (cores), mean | 0 | 0.06692 | +0.067 (native is 0) | +0.0626 to +0.0712 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.263 | 1.291 | +2.2% | −0.0111 to +0.0665 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 513.6 | 397.1 | −22.7% | −168.5364 to −64.4666 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.922 | 2.068 | +7.6% | −0.1413 to +0.4324 | no |
| pods started | 0.2 | 0.5 | +150.0% | −0.5953 to +1.1953 | no |
| pod start wait, total (s) | 0.4 | 1.4 | +250.0% | −1.3604 to +3.3604 | no |
| pod start wait, mean (s) | 0.4 | 0.6 | +50.0% | −1.0526 to +1.4526 | no |
| host CPU busy, the real machine under kind (%) | 37.36 | 39.66 | +6.2% | +1.5352 to +3.0740 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 729.4 | 728.9 | −0.1% | −4.1200 to +3.1200 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 2.883 | −51.9% | −4.0047 to −2.2291 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6375 | 0.65 | +2.0% | −0.0828 to +0.1078 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 1 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job turnaround, submitted to done, mean (s) | 35.36 | 35.57 | +0.6% | −0.6741 to +1.0908 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.512 | 2.515 | +0.1% | −0.0040 to +0.0097 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 269.5 | 269.8 | +0.1% | −0.8448 to +1.3363 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.5 | 269.8 | +0.1% | −0.8448 to +1.3363 | no |
| response time (ms), mean | 135.8 | 120.7 | −11.1% | −25.5942 to −4.6236 | yes: GAIN |
| response time (ms), 95th percentile | 333.7 | 223.6 | −33.0% | −154.9439 to −65.2001 | yes: GAIN |
| response time (ms), 99th percentile | 449.4 | 326.3 | −27.4% | −185.5226 to −60.7244 | yes: GAIN |
| time over the response line (% of samples) | 1.134 | 0.4223 | −62.8% | −1.6119 to +0.1883 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 0.5 | −80.8% | −4.4471 to +0.2471 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.9 | 11.3 | +63.8% | +3.1838 to +5.6262 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05269 | 0.05262 | −0.1% | −0.0026 to +0.0024 | no |
| CPU used (cores), mean | 1.265 | 1.263 | −0.1% | −0.0613 to +0.0579 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.265 | 1.263 | −0.1% | −0.0613 to +0.0579 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 509.6 | 513.6 | +0.8% | −19.5215 to +27.3776 | no |
| HPA replicas, mean | 1.912 | 1.922 | +0.5% | −0.1272 to +0.1480 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2032 to +1.0032 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2032 to +1.0032 | no |
| host CPU busy, the real machine under kind (%) | 35.9 | 37.36 | +4.1% | +0.4562 to +2.4585 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 723.1 | 729.4 | +0.9% | −2.6472 to +15.2472 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.008333 | 0.6375 | +7550.0% | +0.5504 to +0.7080 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 1 | +900.0% | +0.6738 to +1.1262 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 29.85 | 35.36 | +18.4% | −2.0906 to +13.0989 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 3.849 | −35.8% | −2.8943 to −1.4071 | yes: GAIN |
| node-hours | 2.512 | 1.615 | −35.7% | −1.2063 to −0.5886 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.5 | 269.8 | +0.1% | −0.1611 to +0.6946 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.5 | 202.1 | −25.0% | −90.8701 to −43.9880 | yes: GAIN |
| response time (ms), mean | 135.8 | 120.2 | −11.5% | −24.2675 to −6.9672 | yes: GAIN |
| response time (ms), 95th percentile | 333.7 | 383.5 | +14.9% | +14.6113 to +85.0727 | yes: LOSS |
| response time (ms), 99th percentile | 449.4 | 521.6 | +16.1% | +18.7932 to +125.5738 | yes: LOSS |
| time over the response line (% of samples) | 1.134 | 1.903 | +67.8% | −0.4555 to +1.9929 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 3.6 | +38.5% | −0.6171 to +2.6171 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 230.1 | +230.100 (native is 0) | +176.5730 to +283.6270 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.9 | 7.77 | +12.6% | −0.7534 to +2.4934 | no |
| utilisation (used / allocatable) | 0.05269 | 0.08285 | +57.2% | +0.0183 to +0.0420 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.265 | 1.223 | −3.3% | −0.0867 to +0.0025 | no |
| Omni's own CPU (cores), mean | 0 | 0.06678 | +0.067 (native is 0) | +0.0627 to +0.0708 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.265 | 1.289 | +1.9% | −0.0225 to +0.0717 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 509.6 | 392.1 | −23.1% | −156.6277 to −78.3917 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.912 | 2.077 | +8.6% | +0.0086 to +0.3214 | yes: power given |
| pods started | 0 | 0.5 | +0.500 (native is 0) | −0.0058 to +1.0058 | no |
| pod start wait, total (s) | 0 | 1.1 | +1.100 (native is 0) | −0.2676 to +2.4676 | no |
| pod start wait, mean (s) | 0 | 0.8 | +0.800 (native is 0) | −0.0121 to +1.6121 | no |
| host CPU busy, the real machine under kind (%) | 35.9 | 39.2 | +9.2% | +2.8066 to +3.7802 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 723.1 | 727.2 | +0.6% | −2.5800 to +10.7800 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 2.89 | −51.8% | −4.0003 to −2.2194 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.008333 | 0.02083 | +150.0% | −0.0248 to +0.0498 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 29.85 | 32.22 | +7.9% | −1.0237 to +5.7570 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 3.849 | −35.8% | −2.8943 to −1.4071 | yes: GAIN |
| node-hours | 2.515 | 1.615 | −35.8% | −1.2144 to −0.5861 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.8 | 269.8 | +0.0% | −0.8903 to +0.9323 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.8 | 202.1 | −25.1% | −91.2010 to −44.1487 | yes: GAIN |
| response time (ms), mean | 120.7 | 120.2 | −0.4% | −6.1101 to +5.0932 | no |
| response time (ms), 95th percentile | 223.6 | 383.5 | +71.5% | +140.5608 to +179.2672 | yes: LOSS |
| response time (ms), 99th percentile | 326.3 | 521.6 | +59.9% | +157.2923 to +233.3217 | yes: LOSS |
| time over the response line (% of samples) | 0.4223 | 1.903 | +350.5% | +0.3373 to +2.6236 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.5 | 3.6 | +620.0% | +0.5891 to +5.6109 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 230.1 | +230.100 (native is 0) | +176.5730 to +283.6270 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.31 | 7.77 | −31.3% | −5.5553 to −1.5147 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05262 | 0.08285 | +57.4% | +0.0170 to +0.0434 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.263 | 1.223 | −3.2% | −0.0700 to −0.0109 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06678 | +0.067 (native is 0) | +0.0627 to +0.0708 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.263 | 1.289 | +2.1% | −0.0005 to +0.0532 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 513.6 | 392.1 | −23.6% | −174.5429 to −68.3326 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.922 | 2.077 | +8.0% | −0.0496 to +0.3587 | no |
| pods started | 0.2 | 0.5 | +150.0% | −0.3786 to +0.9786 | no |
| pod start wait, total (s) | 0.4 | 1.1 | +175.0% | −0.9537 to +2.3537 | no |
| pod start wait, mean (s) | 0.4 | 0.8 | +100.0% | −0.7778 to +1.5778 | no |
| host CPU busy, the real machine under kind (%) | 37.36 | 39.2 | +4.9% | +1.1311 to +2.5410 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 729.4 | 727.2 | −0.3% | −4.9765 to +0.5765 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 2.89 | −51.8% | −4.0003 to −2.2194 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6375 | 0.02083 | −96.7% | −0.6866 to −0.5467 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 0.1 | −90.0% | −1.1262 to −0.6738 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 35.36 | 32.22 | −8.9% | −7.3720 to +1.0970 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 3.94 | −34.3% | −2.7743 to −1.3463 | yes: GAIN |
| node-hours | 2.512 | 1.651 | −34.3% | −1.1591 to −0.5633 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.5 | 269.2 | −0.1% | −1.5716 to +0.8752 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.5 | 204.5 | −24.1% | −88.0383 to −42.1081 | yes: GAIN |
| response time (ms), mean | 135.8 | 96.09 | −29.3% | −49.0519 to −30.4618 | yes: GAIN |
| response time (ms), 95th percentile | 333.7 | 223.7 | −33.0% | −148.6368 to −71.3542 | yes: GAIN |
| response time (ms), 99th percentile | 449.4 | 367.6 | −18.2% | −172.9978 to +9.2846 | no |
| time over the response line (% of samples) | 1.134 | 0.6342 | −44.1% | −1.3756 to +0.3758 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 1.1 | −57.7% | −3.5855 to +0.5855 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 165.3 | +165.300 (native is 0) | +117.1312 to +213.4688 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.9 | 11.23 | +62.7% | +3.0850 to +5.5650 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05269 | 0.08043 | +52.6% | +0.0175 to +0.0380 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.265 | 1.224 | −3.2% | −0.0942 to +0.0123 | no |
| Omni's own CPU (cores), mean | 0 | 0.06692 | +0.067 (native is 0) | +0.0626 to +0.0712 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.265 | 1.291 | +2.1% | −0.0296 to +0.0816 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 509.6 | 397.1 | −22.1% | −148.9379 to −76.2091 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.912 | 2.068 | +8.2% | −0.0704 to +0.3824 | no |
| pods started | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| pod start wait, total (s) | 0 | 1.4 | +1.400 (native is 0) | −0.7380 to +3.5380 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.600 (native is 0) | −0.3656 to +1.5656 | no |
| host CPU busy, the real machine under kind (%) | 35.9 | 39.66 | +10.5% | +2.8643 to +4.6596 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 723.1 | 728.9 | +0.8% | −0.3515 to +11.9515 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 2.883 | −51.9% | −4.0047 to −2.2291 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.008333 | 0.65 | +7700.0% | +0.5740 to +0.7093 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 1 | +900.0% | +0.6738 to +1.1262 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 29.85 | 35.57 | +19.1% | −1.2678 to +12.6928 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*