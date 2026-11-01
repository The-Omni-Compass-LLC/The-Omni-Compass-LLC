# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.286 | 5.451 |
| node-hours | 2.513 | 2.519 | 2.212 | 2.288 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 274 | 273.2 | 274.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 274 | 250.7 | 257.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 414.4 | 420.8 | 368.2 | 390.4 |
| response time (ms), 95th percentile | 1518 | 1539 | 1523 | 1657 |
| response time (ms), 99th percentile | 2065 | 2169 | 2125 | 2306 |
| time over the response line (% of samples) | 17.74 | 17.89 | 17.14 | 17.29 |
| failed requests (%) | 0.01105 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.6 | 9.7 | 9.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 42.9 | 47.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.05 | 10.36 | 10.38 | 11.37 |
| utilisation (used / allocatable) | 0.06338 | 0.06303 | 0.07168 | 0.07108 |
| CPU used (cores), mean | 1.521 | 1.513 | 1.504 | 1.531 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01627 | 0.01703 |
| CPU used with Omni's own (cores), mean | 1.521 | 1.513 | 1.52 | 1.548 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.8 | 439.9 | 402.2 | 403.6 |
| HPA replicas, mean | 1.97 | 2.089 | 2.112 | 2.216 |
| pods started | 0 | 0 | 0.2 | 0.5 |
| pod start wait, total (s) | 0 | 0 | 0.4 | 0.8 |
| pod start wait, mean (s) | 0 | 0 | 0.4 | 0.8 |
| host CPU busy, the real machine under kind (%) | 43.33 | 43.89 | 44.15 | 44.96 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 804.5 | 809.3 | 806 | 815.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.707 | 5.067 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 0.2125 | 0.04583 | 0.2625 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.9 | 0.3 | 0.8 |
| queue: job turnaround, submitted to done, mean (s) | 108.3 | 113.9 | 112.2 | 119.7 |
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
| worker nodes in service, mean | 6 | 5.451 | −9.1% | −1.1809 to +0.0839 | no |
| node-hours | 2.519 | 2.288 | −9.2% | −0.4961 to +0.0348 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 274.3 | +0.1% | −0.5020 to +1.1045 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 257.1 | −6.2% | −37.0302 to +3.1328 | no |
| response time (ms), mean | 420.8 | 390.4 | −7.2% | −43.8816 to −16.9764 | yes: GAIN |
| response time (ms), 95th percentile | 1539 | 1657 | +7.7% | +32.2392 to +203.4188 | yes: LOSS |
| response time (ms), 99th percentile | 2169 | 2306 | +6.3% | −36.1016 to +309.7652 | no |
| time over the response line (% of samples) | 17.89 | 17.29 | −3.4% | −1.5917 to +0.3851 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.9 | +3.1% | −1.5790 to +2.1790 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.7 | +47.700 (native is 0) | +22.6448 to +72.7552 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.36 | 11.37 | +9.7% | −0.8383 to +2.8483 | no |
| utilisation (used / allocatable) | 0.06303 | 0.07108 | +12.8% | −0.0009 to +0.0170 | no |
| CPU used (cores), mean | 1.513 | 1.531 | +1.2% | −0.0017 to +0.0373 | no |
| Omni's own CPU (cores), mean | 0 | 0.01703 | +0.017 (native is 0) | +0.0162 to +0.0179 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.513 | 1.548 | +2.3% | +0.0152 to +0.0545 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 439.9 | 403.6 | −8.3% | −69.5468 to −3.2060 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.089 | 2.216 | +6.1% | −0.0923 to +0.3472 | no |
| pods started | 0 | 0.5 | +0.500 (native is 0) | +0.1230 to +0.8770 | yes: power given |
| pod start wait, total (s) | 0 | 0.8 | +0.800 (native is 0) | +0.1427 to +1.4573 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8 | +0.800 (native is 0) | +0.1427 to +1.4573 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.89 | 44.96 | +2.4% | +0.7469 to +1.3931 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 809.3 | 815.7 | +0.8% | +0.0718 to +12.7282 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.067 | −15.5% | −1.9065 to +0.0414 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2125 | 0.2625 | +23.5% | −0.0531 to +0.1531 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.8 | −11.1% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 113.9 | 119.7 | +5.1% | +0.2462 to +11.3704 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.519 | +0.3% | −0.0004 to +0.0134 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 274 | +0.2% | −0.2123 to +1.2817 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 274 | +0.2% | −0.2123 to +1.2817 | no |
| response time (ms), mean | 414.4 | 420.8 | +1.5% | −5.9314 to +18.7481 | no |
| response time (ms), 95th percentile | 1518 | 1539 | +1.4% | −31.1595 to +73.9545 | no |
| response time (ms), 99th percentile | 2065 | 2169 | +5.0% | +3.7217 to +204.1087 | yes: LOSS |
| time over the response line (% of samples) | 17.74 | 17.89 | +0.9% | −0.6707 to +0.9782 | no |
| failed requests (%) | 0.01105 | 0 | −100.0% | −0.0360 to +0.0139 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.6 | −1.0% | −0.8113 to +0.6113 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.05 | 10.36 | −6.2% | −2.1134 to +0.7334 | no |
| utilisation (used / allocatable) | 0.06338 | 0.06303 | −0.5% | −0.0012 to +0.0005 | no |
| CPU used (cores), mean | 1.521 | 1.513 | −0.5% | −0.0295 to +0.0128 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.521 | 1.513 | −0.5% | −0.0295 to +0.0128 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.8 | 439.9 | +0.5% | −5.0847 to +9.3241 | no |
| HPA replicas, mean | 1.97 | 2.089 | +6.1% | −0.0453 to +0.2839 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 43.33 | 43.89 | +1.3% | +0.2325 to +0.8774 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 804.5 | 809.3 | +0.6% | −1.2112 to +10.8112 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 0.2125 | +142.9% | +0.0763 to +0.1737 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.9 | +80.0% | +0.0306 to +0.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 108.3 | 113.9 | +5.1% | −0.5098 to +11.5848 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.286 | −11.9% | −1.3686 to −0.0587 | yes: GAIN |
| node-hours | 2.513 | 2.212 | −12.0% | −0.5719 to −0.0289 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 273.2 | −0.1% | −1.1372 to +0.5231 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 250.7 | −8.3% | −43.2934 to −2.1791 | yes: GAIN |
| response time (ms), mean | 414.4 | 368.2 | −11.1% | −62.5927 to −29.6937 | yes: GAIN |
| response time (ms), 95th percentile | 1518 | 1523 | +0.3% | −54.9071 to +64.4811 | no |
| response time (ms), 99th percentile | 2065 | 2125 | +2.9% | −60.3055 to +179.6015 | no |
| time over the response line (% of samples) | 17.74 | 17.14 | −3.4% | −1.2466 to +0.0382 | no |
| failed requests (%) | 0.01105 | 0 | −100.0% | −0.0360 to +0.0139 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.7 | ±0.0% | −1.0116 to +1.0116 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.9 | +42.900 (native is 0) | +19.0387 to +66.7613 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.05 | 10.38 | −6.1% | −2.7520 to +1.3953 | no |
| utilisation (used / allocatable) | 0.06338 | 0.07168 | +13.1% | +0.0005 to +0.0161 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.521 | 1.504 | −1.1% | −0.0444 to +0.0104 | no |
| Omni's own CPU (cores), mean | 0 | 0.01627 | +0.016 (native is 0) | +0.0150 to +0.0175 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.521 | 1.52 | −0.0% | −0.0286 to +0.0272 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.8 | 402.2 | −8.1% | −67.9276 to −3.3105 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.97 | 2.112 | +7.2% | −0.0620 to +0.3472 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2032 to +1.0032 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2032 to +1.0032 | no |
| host CPU busy, the real machine under kind (%) | 43.33 | 44.15 | +1.9% | +0.4927 to +1.1426 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 804.5 | 806 | +0.2% | −2.6743 to +5.6743 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.707 | −21.5% | −2.3830 to −0.2027 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 0.04583 | −47.6% | −0.0788 to −0.0045 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.3 | −40.0% | −0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 108.3 | 112.2 | +3.6% | −2.0272 to +9.8189 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.286 | −11.9% | −1.3686 to −0.0587 | yes: GAIN |
| node-hours | 2.519 | 2.212 | −12.2% | −0.5792 to −0.0346 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 273.2 | −0.3% | −1.4736 to −0.2100 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 250.7 | −8.5% | −43.9293 to −2.6126 | yes: GAIN |
| response time (ms), mean | 420.8 | 368.2 | −12.5% | −67.2900 to −37.8132 | yes: GAIN |
| response time (ms), 95th percentile | 1539 | 1523 | −1.1% | −61.0782 to +27.8572 | no |
| response time (ms), 99th percentile | 2169 | 2125 | −2.0% | −178.4555 to +89.9211 | no |
| time over the response line (% of samples) | 17.89 | 17.14 | −4.2% | −1.5619 to +0.0459 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.7 | +1.0% | −1.2254 to +1.4254 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.9 | +42.900 (native is 0) | +19.0387 to +66.7613 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.36 | 10.38 | +0.1% | −1.8645 to +1.8878 | no |
| utilisation (used / allocatable) | 0.06303 | 0.07168 | +13.7% | +0.0011 to +0.0162 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.513 | 1.504 | −0.6% | −0.0443 to +0.0270 | no |
| Omni's own CPU (cores), mean | 0 | 0.01627 | +0.016 (native is 0) | +0.0150 to +0.0175 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.513 | 1.52 | +0.5% | −0.0286 to +0.0438 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 439.9 | 402.2 | −8.6% | −69.3729 to −6.1046 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.089 | 2.112 | +1.1% | −0.1810 to +0.2276 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2032 to +1.0032 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2032 to +1.0032 | no |
| host CPU busy, the real machine under kind (%) | 43.89 | 44.15 | +0.6% | +0.1219 to +0.4035 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 809.3 | 806 | −0.4% | −7.1306 to +0.5306 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.707 | −21.5% | −2.3830 to −0.2027 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2125 | 0.04583 | −78.4% | −0.2436 to −0.0897 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.3 | −66.7% | −0.9694 to −0.2306 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 113.9 | 112.2 | −1.4% | −4.7756 to +1.4923 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.451 | −9.1% | −1.1809 to +0.0839 | no |
| node-hours | 2.513 | 2.288 | −8.9% | −0.4895 to +0.0411 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 274.3 | +0.3% | −0.0299 to +1.7019 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 257.1 | −6.0% | −36.3892 to +3.5612 | no |
| response time (ms), mean | 414.4 | 390.4 | −5.8% | −41.4447 to −6.5966 | yes: GAIN |
| response time (ms), 95th percentile | 1518 | 1657 | +9.2% | +31.0834 to +247.3696 | yes: LOSS |
| response time (ms), 99th percentile | 2065 | 2306 | +11.7% | +18.1262 to +463.3678 | yes: LOSS |
| time over the response line (% of samples) | 17.74 | 17.29 | −2.5% | −1.2505 to +0.3514 | no |
| failed requests (%) | 0.01105 | 0 | −100.0% | −0.0360 to +0.0139 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.9 | +2.1% | −1.0064 to +1.4064 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.7 | +47.700 (native is 0) | +22.6448 to +72.7552 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.05 | 11.37 | +2.8% | −1.7965 to +2.4265 | no |
| utilisation (used / allocatable) | 0.06338 | 0.07108 | +12.1% | −0.0017 to +0.0171 | no |
| CPU used (cores), mean | 1.521 | 1.531 | +0.6% | −0.0089 to +0.0278 | no |
| Omni's own CPU (cores), mean | 0 | 0.01703 | +0.017 (native is 0) | +0.0162 to +0.0179 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.521 | 1.548 | +1.7% | +0.0081 to +0.0449 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.8 | 403.6 | −7.8% | −70.5048 to +1.9915 | no |
| HPA replicas, mean | 1.97 | 2.216 | +12.5% | +0.0873 to +0.4062 | yes: power given |
| pods started | 0 | 0.5 | +0.500 (native is 0) | +0.1230 to +0.8770 | yes: power given |
| pod start wait, total (s) | 0 | 0.8 | +0.800 (native is 0) | +0.1427 to +1.4573 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8 | +0.800 (native is 0) | +0.1427 to +1.4573 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.33 | 44.96 | +3.8% | +1.1968 to +2.0531 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 804.5 | 815.7 | +1.4% | +1.3240 to +21.0760 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.067 | −15.5% | −1.9065 to +0.0414 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 0.2625 | +200.0% | +0.0673 to +0.2827 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.8 | +60.0% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 108.3 | 119.7 | +10.5% | +1.3386 to +21.3531 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*