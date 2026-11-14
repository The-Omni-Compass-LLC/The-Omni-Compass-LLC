# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.734 | 4.733 |
| node-hours | 2.513 | 2.518 | 1.987 | 1.985 |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.7 | 272.8 | 272.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 272.7 | 233 | 232.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 324.1 | 284.3 | 300.6 | 254.9 |
| response time (ms), 95th percentile | 1110 | 1036 | 1182 | 1090 |
| response time (ms), 99th percentile | 1539 | 1537 | 1601 | 1580 |
| time over the response line (% of samples) | 11.53 | 8.344 | 11.47 | 8.275 |
| failed requests (%) | 0 | 0.02235 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 4.7 | 7.8 | 5.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 141.1 | 99.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 16.37 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.71 | 16.86 | 13.32 | 20.16 |
| utilisation (used / allocatable) | 0.0594 | 0.05969 | 0.0759 | 0.07601 |
| CPU used (cores), mean | 1.425 | 1.432 | 1.427 | 1.437 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07613 | 0.07705 |
| CPU used with Omni's own (cores), mean | 1.425 | 1.432 | 1.503 | 1.514 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.6 | 462.9 | 392.4 | 390.1 |
| HPA replicas, mean | 1.948 | 1.997 | 2.194 | 2.081 |
| pods started | 0 | 0.1 | 0.7 | 0.7 |
| pod start wait, total (s) | 0 | 0.3 | 1.3 | 1.7 |
| pod start wait, mean (s) | 0 | 0.3 | 0.75 | 0.95 |
| host CPU busy, the real machine under kind (%) | 41.38 | 42.47 | 44.75 | 45.87 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 778.6 | 788.7 | 786.3 | 795.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.798 | 3.604 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1542 | 0.8125 | 0.2542 | 0.9333 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.8 | 1.9 | 2.9 |
| queue: job turnaround, submitted to done, mean (s) | 84.89 | 98.14 | 91.01 | 104.9 |
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
| worker nodes in service, mean | 6 | 4.733 | −21.1% | −1.8615 to −0.6726 | yes: GAIN |
| node-hours | 2.518 | 1.985 | −21.2% | −0.7782 to −0.2892 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.8 | +0.0% | −0.9915 to +1.2460 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 232.9 | −14.6% | −58.1751 to −21.3538 | yes: GAIN |
| response time (ms), mean | 284.3 | 254.9 | −10.3% | −44.8061 to −13.9679 | yes: GAIN |
| response time (ms), 95th percentile | 1036 | 1090 | +5.1% | −9.4376 to +116.1226 | no |
| response time (ms), 99th percentile | 1537 | 1580 | +2.8% | −81.0912 to +166.8014 | no |
| time over the response line (% of samples) | 8.344 | 8.275 | −0.8% | −1.1080 to +0.9690 | no |
| failed requests (%) | 0.02235 | 0 | −100.0% | −0.0729 to +0.0282 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.7 | 5.2 | +10.6% | −0.7729 to +1.7729 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 99.2 | +99.200 (native is 0) | +56.9709 to +141.4291 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.86 | 20.16 | +19.6% | −0.9027 to +7.5027 | no |
| utilisation (used / allocatable) | 0.05969 | 0.07601 | +27.3% | +0.0093 to +0.0233 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.432 | 1.437 | +0.3% | −0.0269 to +0.0351 | no |
| Omni's own CPU (cores), mean | 0 | 0.07705 | +0.077 (native is 0) | +0.0719 to +0.0822 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.432 | 1.514 | +5.7% | +0.0498 to +0.1125 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.9 | 390.1 | −15.7% | −103.9918 to −41.6291 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.997 | 2.081 | +4.2% | −0.1412 to +0.3082 | no |
| pods started | 0.1 | 0.7 | +600.0% | −0.3656 to +1.5656 | no |
| pod start wait, total (s) | 0.3 | 1.7 | +466.7% | −1.0595 to +3.8595 | no |
| pod start wait, mean (s) | 0.3 | 0.95 | +216.7% | −0.6122 to +1.9122 | no |
| host CPU busy, the real machine under kind (%) | 42.47 | 45.87 | +8.0% | +3.1108 to +3.6878 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 788.7 | 795.7 | +0.9% | +2.1252 to +11.8748 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.604 | −39.9% | −3.4463 to −1.3457 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8125 | 0.9333 | +14.9% | +0.0021 to +0.2396 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.8 | 2.9 | +61.1% | −0.5673 to +2.7673 | no |
| queue: job turnaround, submitted to done, mean (s) | 98.14 | 104.9 | +6.9% | +1.8249 to +11.7585 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.518 | +0.2% | −0.0024 to +0.0128 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.7 | +0.3% | −0.1832 to +1.6055 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 272.7 | +0.3% | −0.1832 to +1.6055 | no |
| response time (ms), mean | 324.1 | 284.3 | −12.3% | −62.5429 to −17.0277 | yes: GAIN |
| response time (ms), 95th percentile | 1110 | 1036 | −6.7% | −176.7549 to +28.7519 | no |
| response time (ms), 99th percentile | 1539 | 1537 | −0.1% | −278.6576 to +274.9704 | no |
| time over the response line (% of samples) | 11.53 | 8.344 | −27.6% | −5.4353 to −0.9270 | yes: GAIN |
| failed requests (%) | 0 | 0.02235 | +0.022 (native is 0) | −0.0282 to +0.0729 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 4.7 | −31.9% | −3.8450 to −0.5550 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.71 | 16.86 | +57.5% | +2.9941 to +9.3159 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0594 | 0.05969 | +0.5% | −0.0004 to +0.0010 | no |
| CPU used (cores), mean | 1.425 | 1.432 | +0.5% | −0.0101 to +0.0240 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.425 | 1.432 | +0.5% | −0.0101 to +0.0240 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.6 | 462.9 | −0.6% | −7.9045 to +2.4208 | no |
| HPA replicas, mean | 1.948 | 1.997 | +2.5% | −0.0847 to +0.1840 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 41.38 | 42.47 | +2.6% | +0.6613 to +1.5215 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 778.6 | 788.7 | +1.3% | +1.3299 to +18.8701 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1542 | 0.8125 | +427.0% | +0.4852 to +0.8314 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.8 | +50.0% | −0.0911 to +1.2911 | no |
| queue: job turnaround, submitted to done, mean (s) | 84.89 | 98.14 | +15.6% | +0.4692 to +26.0225 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.734 | −21.1% | −1.8827 to −0.6490 | yes: GAIN |
| node-hours | 2.513 | 1.987 | −20.9% | −0.7841 to −0.2675 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.8 | +0.3% | −0.1807 to +1.8511 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 233 | −14.3% | −58.4010 to −19.6203 | yes: GAIN |
| response time (ms), mean | 324.1 | 300.6 | −7.3% | −32.2575 to −14.7704 | yes: GAIN |
| response time (ms), 95th percentile | 1110 | 1182 | +6.5% | −9.7405 to +153.1455 | no |
| response time (ms), 99th percentile | 1539 | 1601 | +4.0% | −119.0848 to +243.4774 | no |
| time over the response line (% of samples) | 11.53 | 11.47 | −0.5% | −0.9304 to +0.8197 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 7.8 | +13.0% | −0.0204 to +1.8204 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 141.1 | +141.100 (native is 0) | +74.4518 to +207.7482 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.71 | 13.32 | +24.4% | −0.1670 to +5.4004 | no |
| utilisation (used / allocatable) | 0.0594 | 0.0759 | +27.8% | +0.0079 to +0.0251 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.425 | 1.427 | +0.1% | −0.0200 to +0.0230 | no |
| Omni's own CPU (cores), mean | 0 | 0.07613 | +0.076 (native is 0) | +0.0717 to +0.0806 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.425 | 1.503 | +5.4% | +0.0553 to +0.0999 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.6 | 392.4 | −15.7% | −108.2735 to −38.1540 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.948 | 2.194 | +12.6% | +0.0955 to +0.3961 | yes: power given |
| pods started | 0 | 0.7 | +0.700 (native is 0) | +0.0214 to +1.3786 | yes: power given |
| pod start wait, total (s) | 0 | 1.3 | +1.300 (native is 0) | +0.0361 to +2.5639 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.75 | +0.750 (native is 0) | +0.0498 to +1.4502 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.38 | 44.75 | +8.2% | +2.8143 to +3.9318 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 778.6 | 786.3 | +1.0% | +2.1896 to +13.2104 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.798 | −36.7% | −3.1053 to −1.2977 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1542 | 0.2542 | +64.9% | −0.0434 to +0.2434 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.9 | +58.3% | −0.6924 to +2.0924 | no |
| queue: job turnaround, submitted to done, mean (s) | 84.89 | 91.01 | +7.2% | +0.0375 to +12.2042 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.734 | −21.1% | −1.8827 to −0.6490 | yes: GAIN |
| node-hours | 2.518 | 1.987 | −21.1% | −0.7877 to −0.2742 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.8 | +0.0% | −0.2073 to +0.4554 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 233 | −14.6% | −59.0545 to −20.3890 | yes: GAIN |
| response time (ms), mean | 284.3 | 300.6 | +5.7% | −3.5832 to +36.1259 | no |
| response time (ms), 95th percentile | 1036 | 1182 | +14.1% | +97.6419 to +193.7661 | yes: LOSS |
| response time (ms), 99th percentile | 1537 | 1601 | +4.2% | −117.2467 to +245.3265 | no |
| time over the response line (% of samples) | 8.344 | 11.47 | +37.5% | +1.6760 to +4.5756 | yes: LOSS |
| failed requests (%) | 0.02235 | 0 | −100.0% | −0.0729 to +0.0282 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.7 | 7.8 | +66.0% | +1.2393 to +4.9607 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 141.1 | +141.100 (native is 0) | +74.4518 to +207.7482 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.86 | 13.32 | −21.0% | −5.2645 to −1.8122 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05969 | 0.0759 | +27.2% | +0.0080 to +0.0245 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.432 | 1.427 | −0.4% | −0.0378 to +0.0268 | no |
| Omni's own CPU (cores), mean | 0 | 0.07613 | +0.076 (native is 0) | +0.0717 to +0.0806 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.432 | 1.503 | +4.9% | +0.0374 to +0.1038 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.9 | 392.4 | −15.2% | −102.8095 to −38.1344 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.997 | 2.194 | +9.8% | +0.0338 to +0.3586 | yes: power given |
| pods started | 0.1 | 0.7 | +600.0% | −0.1689 to +1.3689 | no |
| pod start wait, total (s) | 0.3 | 1.3 | +333.3% | −0.5816 to +2.5816 | no |
| pod start wait, mean (s) | 0.3 | 0.75 | +150.0% | −0.6485 to +1.5485 | no |
| host CPU busy, the real machine under kind (%) | 42.47 | 44.75 | +5.4% | +2.0763 to +2.4869 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 788.7 | 786.3 | −0.3% | −6.3353 to +1.5353 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.798 | −36.7% | −3.1053 to −1.2977 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8125 | 0.2542 | −68.7% | −0.7475 to −0.3692 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.8 | 1.9 | +5.6% | −1.9077 to +2.1077 | no |
| queue: job turnaround, submitted to done, mean (s) | 98.14 | 91.01 | −7.3% | −14.9764 to +0.7264 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.733 | −21.1% | −1.8615 to −0.6726 | yes: GAIN |
| node-hours | 2.513 | 1.985 | −21.0% | −0.7752 to −0.2820 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.8 | +0.3% | −0.1891 to +1.8658 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 232.9 | −14.4% | −57.6235 to −20.4831 | yes: GAIN |
| response time (ms), mean | 324.1 | 254.9 | −21.3% | −100.1094 to −38.2352 | yes: GAIN |
| response time (ms), 95th percentile | 1110 | 1090 | −1.9% | −163.4482 to +122.1302 | no |
| response time (ms), 99th percentile | 1539 | 1580 | +2.7% | −223.8500 to +305.8730 | no |
| time over the response line (% of samples) | 11.53 | 8.275 | −28.2% | −6.2497 to −0.2516 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 5.2 | −24.6% | −3.4210 to +0.0210 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 99.2 | +99.200 (native is 0) | +56.9709 to +141.4291 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.71 | 20.16 | +88.3% | +3.5051 to +15.4049 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0594 | 0.07601 | +28.0% | +0.0093 to +0.0239 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.425 | 1.437 | +0.8% | −0.0210 to +0.0431 | no |
| Omni's own CPU (cores), mean | 0 | 0.07705 | +0.077 (native is 0) | +0.0719 to +0.0822 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.425 | 1.514 | +6.2% | +0.0565 to +0.1198 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.6 | 390.1 | −16.2% | −109.2736 to −41.8310 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.948 | 2.081 | +6.8% | −0.1009 to +0.3671 | no |
| pods started | 0 | 0.7 | +0.700 (native is 0) | −0.1953 to +1.5953 | no |
| pod start wait, total (s) | 0 | 1.7 | +1.700 (native is 0) | −0.5380 to +3.9380 | no |
| pod start wait, mean (s) | 0 | 0.95 | +0.950 (native is 0) | +0.0507 to +1.8493 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.38 | 45.87 | +10.9% | +3.9566 to +5.0248 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 778.6 | 795.7 | +2.2% | +3.8783 to +30.3217 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.604 | −39.9% | −3.4463 to −1.3457 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1542 | 0.9333 | +505.4% | +0.5282 to +1.0301 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 2.9 | +141.7% | −0.2385 to +3.6385 | no |
| queue: job turnaround, submitted to done, mean (s) | 84.89 | 104.9 | +23.6% | +2.8951 to +37.1799 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*