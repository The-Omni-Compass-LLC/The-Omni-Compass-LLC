# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.876 | 5.051 |
| node-hours | 2.51 | 2.514 | 2.042 | 2.118 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 274.2 | 273.8 | 274.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 274.2 | 238.5 | 244.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 439.6 | 363.9 | 430.3 | 377.7 |
| response time (ms), 95th percentile | 1650 | 1479 | 1844 | 1831 |
| response time (ms), 99th percentile | 2302 | 2421 | 2566 | 2815 |
| time over the response line (% of samples) | 20.13 | 14.06 | 20.05 | 15.21 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 8.8 | 9.4 | 8.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 113 | 78.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 75 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.29 | 19.53 | 14.8 | 26.56 |
| utilisation (used / allocatable) | 0.06461 | 0.06524 | 0.08105 | 0.07802 |
| CPU used (cores), mean | 1.551 | 1.566 | 1.539 | 1.555 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07362 | 0.07986 |
| CPU used with Omni's own (cores), mean | 1.551 | 1.566 | 1.613 | 1.635 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433 | 427.7 | 370.7 | 377.4 |
| HPA replicas, mean | 2.001 | 2.006 | 2.247 | 2.16 |
| pods started | 0 | 0.1 | 1.4 | 0.5 |
| pod start wait, total (s) | 0 | 0.2 | 2.8 | 1 |
| pod start wait, mean (s) | 0 | 0.2 | 1.425 | 0.55 |
| host CPU busy, the real machine under kind (%) | 44.24 | 45.53 | 47.46 | 49.17 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 820.4 | 838.1 | 833.6 | 852.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.264 | 4.517 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1875 | 0.8333 | 0.2208 | 1.054 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 2 | 1.2 | 3 |
| queue: job turnaround, submitted to done, mean (s) | 125.4 | 147.7 | 136.8 | 164.4 |
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
| worker nodes in service, mean | 6 | 5.051 | −15.8% | −1.8171 to −0.0802 | yes: GAIN |
| node-hours | 2.514 | 2.118 | −15.7% | −0.7617 to −0.0297 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 274.6 | +0.2% | −0.8889 to +1.7303 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 244.8 | −10.7% | −57.3679 to −1.4200 | yes: GAIN |
| response time (ms), mean | 363.9 | 377.7 | +3.8% | −15.7278 to +43.3362 | no |
| response time (ms), 95th percentile | 1479 | 1831 | +23.8% | +71.5913 to +632.5857 | yes: LOSS |
| response time (ms), 99th percentile | 2421 | 2815 | +16.3% | +75.9284 to +713.7494 | yes: LOSS |
| time over the response line (% of samples) | 14.06 | 15.21 | +8.2% | −0.5295 to +2.8263 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 8.9 | +1.1% | −0.8204 to +1.0204 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 78.1 | +78.100 (native is 0) | +27.0074 to +129.1926 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.53 | 26.56 | +36.0% | +1.5753 to +12.4781 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06524 | 0.07802 | +19.6% | +0.0020 to +0.0236 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.566 | 1.555 | −0.7% | −0.0579 to +0.0367 | no |
| Omni's own CPU (cores), mean | 0 | 0.07986 | +0.080 (native is 0) | +0.0746 to +0.0851 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.566 | 1.635 | +4.4% | +0.0173 to +0.1213 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 427.7 | 377.4 | −11.8% | −91.7359 to −8.9397 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.006 | 2.16 | +7.7% | −0.1149 to +0.4235 | no |
| pods started | 0.1 | 0.5 | +400.0% | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0.2 | 1 | +400.0% | −0.3583 to +1.9583 | no |
| pod start wait, mean (s) | 0.2 | 0.55 | +175.0% | −0.2353 to +0.9353 | no |
| host CPU busy, the real machine under kind (%) | 45.53 | 49.17 | +8.0% | +2.9606 to +4.3290 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 838.1 | 852.8 | +1.8% | +3.2648 to +26.1352 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.517 | −24.7% | −2.7484 to −0.2184 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8333 | 1.054 | +26.5% | −0.0443 to +0.4859 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2 | 3 | +50.0% | −0.5080 to +2.5080 | no |
| queue: job turnaround, submitted to done, mean (s) | 147.7 | 164.4 | +11.3% | +6.0874 to +27.1959 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.51 | 2.514 | +0.2% | −0.0059 to +0.0136 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 274.2 | +0.2% | −0.4930 to +1.4154 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 274.2 | +0.2% | −0.4930 to +1.4154 | no |
| response time (ms), mean | 439.6 | 363.9 | −17.2% | −127.2729 to −24.1412 | yes: GAIN |
| response time (ms), 95th percentile | 1650 | 1479 | −10.4% | −419.8705 to +76.6135 | no |
| response time (ms), 99th percentile | 2302 | 2421 | +5.1% | −94.2028 to +330.6856 | no |
| time over the response line (% of samples) | 20.13 | 14.06 | −30.1% | −9.9841 to −2.1461 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 8.8 | −7.4% | −1.6567 to +0.2567 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.29 | 19.53 | +58.8% | +2.8809 to +11.5891 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06461 | 0.06524 | +1.0% | −0.0001 to +0.0014 | no |
| CPU used (cores), mean | 1.551 | 1.566 | +1.0% | −0.0025 to +0.0329 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.551 | 1.566 | +1.0% | −0.0025 to +0.0329 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433 | 427.7 | −1.2% | −11.6686 to +1.0077 | no |
| HPA replicas, mean | 2.001 | 2.006 | +0.2% | −0.1864 to +0.1948 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 44.24 | 45.53 | +2.9% | +0.8901 to +1.6883 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 820.4 | 838.1 | +2.2% | +7.9676 to +27.4324 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1875 | 0.8333 | +344.4% | +0.4387 to +0.8529 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 2 | +66.7% | −0.2556 to +1.8556 | no |
| queue: job turnaround, submitted to done, mean (s) | 125.4 | 147.7 | +17.8% | +8.4327 to +36.1673 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.876 | −18.7% | −2.0596 to −0.1888 | yes: GAIN |
| node-hours | 2.51 | 2.042 | −18.7% | −0.8597 to −0.0780 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 273.8 | +0.0% | −0.6138 to +0.7609 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 238.5 | −12.9% | −64.8494 to −5.7035 | yes: GAIN |
| response time (ms), mean | 439.6 | 430.3 | −2.1% | −29.8082 to +11.2871 | no |
| response time (ms), 95th percentile | 1650 | 1844 | +11.7% | +28.2009 to +358.5941 | yes: LOSS |
| response time (ms), 99th percentile | 2302 | 2566 | +11.4% | +39.5817 to +487.3207 | yes: LOSS |
| time over the response line (% of samples) | 20.13 | 20.05 | −0.4% | −0.6525 to +0.4966 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 9.4 | −1.1% | −0.6278 to +0.4278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113 | +113.000 (native is 0) | +21.6296 to +204.3704 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.29 | 14.8 | +20.4% | −0.9831 to +5.9898 | no |
| utilisation (used / allocatable) | 0.06461 | 0.08105 | +25.5% | +0.0025 to +0.0304 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.551 | 1.539 | −0.7% | −0.0428 to +0.0196 | no |
| Omni's own CPU (cores), mean | 0 | 0.07362 | +0.074 (native is 0) | +0.0680 to +0.0793 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.551 | 1.613 | +4.0% | +0.0261 to +0.0980 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433 | 370.7 | −14.4% | −114.5298 to −10.1849 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.001 | 2.247 | +12.3% | +0.0569 to +0.4346 | yes: power given |
| pods started | 0 | 1.4 | +1.400 (native is 0) | +0.4344 to +2.3656 | yes: power given |
| pod start wait, total (s) | 0 | 2.8 | +2.800 (native is 0) | +0.9593 to +4.6407 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.425 | +1.425 (native is 0) | +0.7094 to +2.1406 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.24 | 47.46 | +7.3% | +2.7379 to +3.7103 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 820.4 | 833.6 | +1.6% | +4.6575 to +21.7425 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.264 | −28.9% | −2.9842 to −0.4870 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1875 | 0.2208 | +17.8% | −0.0189 to +0.0855 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.2 | ±0.0% | −0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 125.4 | 136.8 | +9.0% | +3.5116 to +19.1467 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.876 | −18.7% | −2.0596 to −0.1888 | yes: GAIN |
| node-hours | 2.514 | 2.042 | −18.8% | −0.8636 to −0.0817 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 273.8 | −0.1% | −1.2603 to +0.4850 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 238.5 | −13.0% | −65.4557 to −6.0197 | yes: GAIN |
| response time (ms), mean | 363.9 | 430.3 | +18.3% | +12.6857 to +120.2073 | yes: LOSS |
| response time (ms), 95th percentile | 1479 | 1844 | +24.7% | +113.2845 to +616.7675 | yes: LOSS |
| response time (ms), 99th percentile | 2421 | 2566 | +6.0% | −31.7644 to +322.1840 | no |
| time over the response line (% of samples) | 14.06 | 20.05 | +42.6% | +2.0947 to +9.8796 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 9.4 | +6.8% | −0.0911 to +1.2911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113 | +113.000 (native is 0) | +21.6296 to +204.3704 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.53 | 14.8 | −24.2% | −6.8439 to −2.6194 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06524 | 0.08105 | +24.2% | +0.0022 to +0.0294 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.566 | 1.539 | −1.7% | −0.0615 to +0.0080 | no |
| Omni's own CPU (cores), mean | 0 | 0.07362 | +0.074 (native is 0) | +0.0680 to +0.0793 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.566 | 1.613 | +3.0% | +0.0069 to +0.0869 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 427.7 | 370.7 | −13.3% | −105.2385 to −8.8153 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.006 | 2.247 | +12.0% | +0.0011 to +0.4821 | yes: power given |
| pods started | 0.1 | 1.4 | +1300.0% | +0.4047 to +2.1953 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.8 | +1300.0% | +0.9073 to +4.2927 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.425 | +612.5% | +0.4595 to +1.9905 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.53 | 47.46 | +4.3% | +1.6532 to +2.2168 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 838.1 | 833.6 | −0.5% | −6.6393 to −2.3607 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.264 | −28.9% | −2.9842 to −0.4870 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8333 | 0.2208 | −73.5% | −0.8200 to −0.4050 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2 | 1.2 | −40.0% | −1.6121 to +0.0121 | no |
| queue: job turnaround, submitted to done, mean (s) | 147.7 | 136.8 | −7.4% | −17.6220 to −4.3196 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.051 | −15.8% | −1.8171 to −0.0802 | yes: GAIN |
| node-hours | 2.51 | 2.118 | −15.6% | −0.7580 to −0.0258 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 274.6 | +0.3% | −0.0520 to +1.8158 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 244.8 | −10.6% | −56.7773 to −1.0882 | yes: GAIN |
| response time (ms), mean | 439.6 | 377.7 | −14.1% | −90.1022 to −33.7036 | yes: GAIN |
| response time (ms), 95th percentile | 1650 | 1831 | +10.9% | −31.4271 to +392.3471 | no |
| response time (ms), 99th percentile | 2302 | 2815 | +22.3% | +76.2372 to +949.9234 | yes: LOSS |
| time over the response line (% of samples) | 20.13 | 15.21 | −24.4% | −8.1498 to −1.6836 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 8.9 | −6.3% | −1.7285 to +0.5285 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 78.1 | +78.100 (native is 0) | +27.0074 to +129.1926 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.29 | 26.56 | +116.0% | +6.9792 to +21.5441 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06461 | 0.07802 | +20.8% | +0.0023 to +0.0245 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.551 | 1.555 | +0.3% | −0.0337 to +0.0430 | no |
| Omni's own CPU (cores), mean | 0 | 0.07986 | +0.080 (native is 0) | +0.0746 to +0.0851 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.551 | 1.635 | +5.4% | +0.0416 to +0.1274 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433 | 377.4 | −12.9% | −100.7718 to −10.5647 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.001 | 2.16 | +7.9% | +0.0062 to +0.3108 | yes: power given |
| pods started | 0 | 0.5 | +0.500 (native is 0) | −0.1079 to +1.1079 | no |
| pod start wait, total (s) | 0 | 1 | +1.000 (native is 0) | −0.3488 to +2.3488 | no |
| pod start wait, mean (s) | 0 | 0.55 | +0.550 (native is 0) | −0.1338 to +1.2338 | no |
| host CPU busy, the real machine under kind (%) | 44.24 | 49.17 | +11.2% | +4.0812 to +5.7867 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 820.4 | 852.8 | +3.9% | +14.2313 to +50.5687 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.517 | −24.7% | −2.7484 to −0.2184 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1875 | 1.054 | +462.2% | +0.6641 to +1.0692 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 3 | +150.0% | +0.6417 to +2.9583 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 125.4 | 164.4 | +31.0% | +16.4490 to +61.4343 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*