# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.07 | 5.007 |
| node-hours | 2.518 | 2.514 | 2.123 | 2.098 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.3 | 274.1 | 274.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 274.3 | 244.8 | 243.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 446.2 | 386.5 | 423 | 386.8 |
| response time (ms), 95th percentile | 1682 | 1478 | 1750 | 1768 |
| response time (ms), 99th percentile | 2367 | 2369 | 2403 | 2617 |
| time over the response line (% of samples) | 20.49 | 13.95 | 22.03 | 15.43 |
| failed requests (%) | 0 | 0.01005 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 9.7 | 10.8 | 9.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 103.8 | 84.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 3.333 | 66.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.1 | 21.89 | 14.35 | 24.29 |
| utilisation (used / allocatable) | 0.06478 | 0.06516 | 0.07668 | 0.07909 |
| CPU used (cores), mean | 1.555 | 1.564 | 1.553 | 1.56 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07523 | 0.07863 |
| CPU used with Omni's own (cores), mean | 1.555 | 1.564 | 1.628 | 1.639 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 429 | 428.8 | 380.1 | 373.5 |
| HPA replicas, mean | 2.014 | 2.049 | 2.295 | 2.274 |
| pods started | 0.1 | 0 | 1.1 | 1 |
| pod start wait, total (s) | 0.1 | 0 | 2.6 | 2.6 |
| pod start wait, mean (s) | 0.1 | 0 | 1.5 | 1.05 |
| host CPU busy, the real machine under kind (%) | 44.21 | 45.59 | 47.49 | 48.85 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 813.2 | 830.7 | 821.7 | 841.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.19 | 4.306 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.25 | 0.9 | 0.2042 | 0.925 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 2.3 | 1.4 | 2.1 |
| queue: job turnaround, submitted to done, mean (s) | 119 | 145.8 | 126.7 | 155.8 |
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
| worker nodes in service, mean | 6 | 5.007 | −16.5% | −1.7673 to −0.2184 | yes: GAIN |
| node-hours | 2.514 | 2.098 | −16.5% | −0.7437 to −0.0883 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 274.4 | +0.0% | −0.6310 to +0.8682 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 243.2 | −11.3% | −55.8310 to −6.3067 | yes: GAIN |
| response time (ms), mean | 386.5 | 386.8 | +0.1% | −96.1076 to +96.5599 | no |
| response time (ms), 95th percentile | 1478 | 1768 | +19.6% | −222.3920 to +801.7850 | no |
| response time (ms), 99th percentile | 2369 | 2617 | +10.4% | −184.9406 to +679.0350 | no |
| time over the response line (% of samples) | 13.95 | 15.43 | +10.6% | −1.3752 to +4.3383 | no |
| failed requests (%) | 0.01005 | 0 | −100.0% | −0.0328 to +0.0127 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.9 | +2.1% | −0.5388 to +0.9388 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 84.5 | +84.500 (native is 0) | +34.3465 to +134.6535 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.89 | 24.28 | +10.9% | −2.8763 to +7.6696 | no |
| utilisation (used / allocatable) | 0.06516 | 0.07909 | +21.4% | +0.0025 to +0.0253 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.564 | 1.56 | −0.2% | −0.0311 to +0.0240 | no |
| Omni's own CPU (cores), mean | 0 | 0.07863 | +0.079 (native is 0) | +0.0728 to +0.0845 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.564 | 1.639 | +4.8% | +0.0450 to +0.1051 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 428.8 | 373.5 | −12.9% | −100.6222 to −10.0066 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.049 | 2.274 | +11.0% | +0.0665 to +0.3835 | yes: power given |
| pods started | 0 | 1 | +1.000 (native is 0) | +0.0463 to +1.9537 | yes: power given |
| pod start wait, total (s) | 0 | 2.6 | +2.600 (native is 0) | +0.1405 to +5.0595 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.05 | +1.050 (native is 0) | +0.0733 to +2.0267 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.59 | 48.85 | +7.2% | +2.6339 to +3.8903 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 830.7 | 841.7 | +1.3% | −1.1906 to +23.1906 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.306 | −28.2% | −2.7476 to −0.6407 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9 | 0.925 | +2.8% | −0.1763 to +0.2263 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.3 | 2.1 | −8.7% | −1.9779 to +1.5779 | no |
| queue: job turnaround, submitted to done, mean (s) | 145.8 | 155.8 | +6.9% | −5.5654 to +25.5904 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.518 | 2.514 | −0.1% | −0.0121 to +0.0054 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.3 | −0.1% | −1.2414 to +0.7069 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 274.3 | −0.1% | −1.2414 to +0.7069 | no |
| response time (ms), mean | 446.2 | 386.5 | −13.4% | −120.9339 to +1.5759 | no |
| response time (ms), 95th percentile | 1682 | 1478 | −12.1% | −540.3622 to +133.3072 | no |
| response time (ms), 99th percentile | 2367 | 2369 | +0.1% | −274.9145 to +280.8247 | no |
| time over the response line (% of samples) | 20.49 | 13.95 | −31.9% | −10.5726 to −2.5167 | yes: GAIN |
| failed requests (%) | 0 | 0.01005 | +0.010 (native is 0) | −0.0127 to +0.0328 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 9.7 | −10.2% | −2.3367 to +0.1367 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.1 | 21.89 | +67.1% | +0.3606 to +17.2227 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06478 | 0.06516 | +0.6% | −0.0007 to +0.0015 | no |
| CPU used (cores), mean | 1.555 | 1.564 | +0.6% | −0.0168 to +0.0349 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.555 | 1.564 | +0.6% | −0.0168 to +0.0349 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 429 | 428.8 | −0.0% | −8.1208 to +7.7397 | no |
| HPA replicas, mean | 2.014 | 2.049 | +1.7% | −0.0771 to +0.1474 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, mean (s) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| host CPU busy, the real machine under kind (%) | 44.21 | 45.59 | +3.1% | +0.9766 to +1.7660 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 813.2 | 830.7 | +2.2% | +6.4172 to +28.5828 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.25 | 0.9 | +260.0% | +0.4392 to +0.8608 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 2.3 | +130.0% | −0.6090 to +3.2090 | no |
| queue: job turnaround, submitted to done, mean (s) | 119 | 145.8 | +22.5% | +7.6353 to +45.9564 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.07 | −15.5% | −1.4666 to −0.3930 | yes: GAIN |
| node-hours | 2.518 | 2.123 | −15.7% | −0.6186 to −0.1702 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.1 | −0.2% | −1.2839 to +0.2814 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 244.8 | −10.8% | −46.5435 to −12.9173 | yes: GAIN |
| response time (ms), mean | 446.2 | 423 | −5.2% | −82.0018 to +35.5237 | no |
| response time (ms), 95th percentile | 1682 | 1750 | +4.0% | −185.1954 to +320.5264 | no |
| response time (ms), 99th percentile | 2367 | 2403 | +1.5% | −316.7941 to +389.1621 | no |
| time over the response line (% of samples) | 20.49 | 22.03 | +7.5% | −1.2328 to +4.3092 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 10.8 | ±0.0% | −0.5840 to +0.5840 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 103.8 | +103.800 (native is 0) | +49.1303 to +158.4697 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.1 | 14.35 | +9.6% | −1.8248 to +4.3314 | no |
| utilisation (used / allocatable) | 0.06478 | 0.07668 | +18.4% | +0.0047 to +0.0191 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.555 | 1.553 | −0.1% | −0.0372 to +0.0331 | no |
| Omni's own CPU (cores), mean | 0 | 0.07523 | +0.075 (native is 0) | +0.0700 to +0.0805 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.555 | 1.628 | +4.7% | +0.0367 to +0.1097 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 429 | 380.1 | −11.4% | −79.9161 to −17.8498 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.014 | 2.295 | +14.0% | +0.1150 to +0.4473 | yes: power given |
| pods started | 0.1 | 1.1 | +1000.0% | +0.2460 to +1.7540 | yes: power given |
| pod start wait, total (s) | 0.1 | 2.6 | +2500.0% | +0.8056 to +4.1944 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.5 | +1400.0% | +0.4198 to +2.3802 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.21 | 47.49 | +7.4% | +2.4607 to +4.0904 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 813.2 | 821.7 | +1.0% | −3.0697 to +20.0697 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.19 | −30.2% | −2.7751 to −0.8451 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.25 | 0.2042 | −18.3% | −0.3032 to +0.2115 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 1.4 | +40.0% | −0.8251 to +1.6251 | no |
| queue: job turnaround, submitted to done, mean (s) | 119 | 126.7 | +6.5% | −4.3221 to +19.8138 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.07 | −15.5% | −1.4666 to −0.3930 | yes: GAIN |
| node-hours | 2.514 | 2.123 | −15.6% | −0.6159 to −0.1662 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 274.1 | −0.1% | −1.5026 to +1.0347 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 244.8 | −10.7% | −46.0670 to −12.8592 | yes: GAIN |
| response time (ms), mean | 386.5 | 423 | +9.4% | −73.2311 to +146.1109 | no |
| response time (ms), 95th percentile | 1478 | 1750 | +18.3% | −285.3917 to +827.7777 | no |
| response time (ms), 99th percentile | 2369 | 2403 | +1.4% | −549.5769 to +616.0347 | no |
| time over the response line (% of samples) | 13.95 | 22.03 | +57.9% | +2.1890 to +13.9767 | yes: LOSS |
| failed requests (%) | 0.01005 | 0 | −100.0% | −0.0328 to +0.0127 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 10.8 | +11.3% | −0.3871 to +2.5871 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 103.8 | +103.800 (native is 0) | +49.1303 to +158.4697 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.89 | 14.35 | −34.4% | −16.7774 to +1.7007 | no |
| utilisation (used / allocatable) | 0.06516 | 0.07668 | +17.7% | +0.0037 to +0.0193 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.564 | 1.553 | −0.7% | −0.0507 to +0.0284 | no |
| Omni's own CPU (cores), mean | 0 | 0.07523 | +0.075 (native is 0) | +0.0700 to +0.0805 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.564 | 1.628 | +4.1% | +0.0265 to +0.1017 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 428.8 | 380.1 | −11.4% | −85.4965 to −11.8883 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.049 | 2.295 | +12.0% | +0.0834 to +0.4086 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.3128 to +1.8872 | yes: power given |
| pod start wait, total (s) | 0 | 2.6 | +2.600 (native is 0) | +0.8414 to +4.3586 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.5 | +1.500 (native is 0) | +0.4884 to +2.5116 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.59 | 47.49 | +4.2% | +0.9096 to +2.8988 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 830.7 | 821.7 | −1.1% | −28.4321 to +10.4321 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.19 | −30.2% | −2.7751 to −0.8451 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9 | 0.2042 | −77.3% | −1.1332 to −0.2585 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.3 | 1.4 | −39.1% | −3.7899 to +1.9899 | no |
| queue: job turnaround, submitted to done, mean (s) | 145.8 | 126.7 | −13.1% | −46.4550 to +8.3550 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.007 | −16.5% | −1.7673 to −0.2184 | yes: GAIN |
| node-hours | 2.518 | 2.098 | −16.7% | −0.7457 to −0.0930 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.4 | −0.1% | −1.0527 to +0.7554 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 243.2 | −11.4% | −56.2704 to −6.4019 | yes: GAIN |
| response time (ms), mean | 446.2 | 386.8 | −13.3% | −100.6050 to −18.3007 | yes: GAIN |
| response time (ms), 95th percentile | 1682 | 1768 | +5.1% | −158.7416 to +331.0796 | no |
| response time (ms), 99th percentile | 2367 | 2617 | +10.6% | −189.6249 to +689.6295 | no |
| time over the response line (% of samples) | 20.49 | 15.43 | −24.7% | −7.8831 to −2.2431 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 9.9 | −8.3% | −1.6872 to −0.1128 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 84.5 | +84.500 (native is 0) | +34.3465 to +134.6535 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.1 | 24.28 | +85.4% | +4.3232 to +18.0535 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06478 | 0.07909 | +22.1% | +0.0038 to +0.0248 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.555 | 1.56 | +0.4% | −0.0346 to +0.0457 | no |
| Omni's own CPU (cores), mean | 0 | 0.07863 | +0.079 (native is 0) | +0.0728 to +0.0845 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.555 | 1.639 | +5.4% | +0.0398 to +0.1285 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 429 | 373.5 | −12.9% | −94.0992 to −16.9106 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.014 | 2.274 | +12.9% | +0.0979 to +0.4224 | yes: power given |
| pods started | 0.1 | 1 | +900.0% | +0.0436 to +1.7564 | yes: power given |
| pod start wait, total (s) | 0.1 | 2.6 | +2500.0% | +0.1336 to +4.8664 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.05 | +950.0% | +0.0230 to +1.8770 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.21 | 48.85 | +10.5% | +4.1433 to +5.1236 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 813.2 | 841.7 | +3.5% | +14.6123 to +42.3877 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.306 | −28.2% | −2.7476 to −0.6407 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.25 | 0.925 | +270.0% | +0.4498 to +0.9002 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 2.1 | +110.0% | +0.1796 to +2.0204 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 119 | 155.8 | +30.9% | +18.9194 to +54.6972 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*