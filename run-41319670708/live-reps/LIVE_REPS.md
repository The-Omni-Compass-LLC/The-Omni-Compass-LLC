# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.868 | 4.894 |
| node-hours | 2.512 | 2.519 | 2.041 | 2.052 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 273.6 | 273.1 | 273.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 273.6 | 237.4 | 238.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 380.9 | 434.4 | 354.9 | 407.9 |
| response time (ms), 95th percentile | 1429 | 1863 | 1490 | 1931 |
| response time (ms), 99th percentile | 1985 | 2580 | 2123 | 2566 |
| time over the response line (% of samples) | 17.04 | 14.97 | 16.68 | 14.54 |
| failed requests (%) | 0 | 0.01212 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 9 | 8.4 | 8.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 43.6 | 33.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.43 | 24.84 | 11.02 | 26.77 |
| utilisation (used / allocatable) | 0.06181 | 0.06163 | 0.07678 | 0.07636 |
| CPU used (cores), mean | 1.484 | 1.479 | 1.467 | 1.474 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01627 | 0.01628 |
| CPU used with Omni's own (cores), mean | 1.484 | 1.479 | 1.484 | 1.491 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.4 | 455.7 | 388.4 | 388.7 |
| HPA replicas, mean | 1.964 | 2.052 | 2.059 | 1.927 |
| pods started | 0.1 | 0 | 0.3 | 0.2 |
| pod start wait, total (s) | 0.2 | 0 | 0.4 | 0.2 |
| pod start wait, mean (s) | 0.2 | 0 | 0.4 | 0.2 |
| host CPU busy, the real machine under kind (%) | 42.05 | 44.62 | 42.98 | 45.63 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 800.8 | 843.5 | 806.7 | 849.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.185 | 4.228 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 1.154 | 0.075 | 1.071 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 3 | 0.4 | 3.3 |
| queue: job turnaround, submitted to done, mean (s) | 106.9 | 144 | 110.8 | 148.1 |
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
| worker nodes in service, mean | 6 | 4.894 | −18.4% | −2.0138 to −0.1986 | yes: GAIN |
| node-hours | 2.519 | 2.052 | −18.5% | −0.8459 to −0.0875 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.5 | −0.1% | −0.8152 to +0.4853 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 238.6 | −12.8% | −63.5044 to −6.4546 | yes: GAIN |
| response time (ms), mean | 434.4 | 407.9 | −6.1% | −59.2203 to +6.3382 | no |
| response time (ms), 95th percentile | 1863 | 1931 | +3.7% | −130.1920 to +266.6140 | no |
| response time (ms), 99th percentile | 2580 | 2566 | −0.5% | −152.9444 to +125.5830 | no |
| time over the response line (% of samples) | 14.97 | 14.54 | −2.8% | −1.2087 to +0.3555 | no |
| failed requests (%) | 0.01212 | 0 | −100.0% | −0.0395 to +0.0153 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 8.9 | −1.1% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.8 | +33.800 (native is 0) | +17.8131 to +49.7869 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 24.84 | 26.77 | +7.8% | −2.8362 to +6.6929 | no |
| utilisation (used / allocatable) | 0.06163 | 0.07636 | +23.9% | +0.0030 to +0.0265 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.479 | 1.474 | −0.3% | −0.0296 to +0.0198 | no |
| Omni's own CPU (cores), mean | 0 | 0.01628 | +0.016 (native is 0) | +0.0149 to +0.0177 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.479 | 1.491 | +0.8% | −0.0143 to +0.0370 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.7 | 388.7 | −14.7% | −119.7559 to −14.2638 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.052 | 1.927 | −6.1% | −0.2601 to +0.0102 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| host CPU busy, the real machine under kind (%) | 44.62 | 45.63 | +2.3% | +0.5072 to +1.5090 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 843.5 | 849.5 | +0.7% | −2.5771 to +14.5771 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.228 | −29.5% | −3.1941 to −0.3505 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.154 | 1.071 | −7.2% | −0.3518 to +0.1851 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3 | 3.3 | +10.0% | −1.1326 to +1.7326 | no |
| queue: job turnaround, submitted to done, mean (s) | 144 | 148.1 | +2.8% | −2.3277 to +10.4444 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.512 | 2.519 | +0.3% | +0.0016 to +0.0121 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 273.6 | +0.3% | +0.2895 to +1.2729 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 273.6 | +0.3% | +0.2895 to +1.2729 | yes: power given |
| response time (ms), mean | 380.9 | 434.4 | +14.0% | +9.3585 to +97.5394 | yes: LOSS |
| response time (ms), 95th percentile | 1429 | 1863 | +30.3% | +88.1352 to +778.3928 | yes: LOSS |
| response time (ms), 99th percentile | 1985 | 2580 | +30.0% | +110.1215 to +1080.2769 | yes: LOSS |
| time over the response line (% of samples) | 17.04 | 14.97 | −12.1% | −4.3967 to +0.2570 | no |
| failed requests (%) | 0 | 0.01212 | +0.012 (native is 0) | −0.0153 to +0.0395 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 9 | +12.5% | +0.2460 to +1.7540 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.43 | 24.84 | +117.4% | +4.6765 to +22.1535 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06181 | 0.06163 | −0.3% | −0.0015 to +0.0011 | no |
| CPU used (cores), mean | 1.484 | 1.479 | −0.3% | −0.0350 to +0.0264 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.484 | 1.479 | −0.3% | −0.0350 to +0.0264 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.4 | 455.7 | +1.0% | −7.4356 to +16.0445 | no |
| HPA replicas, mean | 1.964 | 2.052 | +4.5% | −0.0116 to +0.1885 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 42.05 | 44.62 | +6.1% | +1.3810 to +3.7515 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 800.8 | 843.5 | +5.3% | +13.0053 to +72.3947 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 1.154 | +1285.0% | +0.7230 to +1.4187 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 3 | +650.0% | +1.2854 to +3.9146 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 106.9 | 144 | +34.7% | +12.0885 to +62.1198 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.868 | −18.9% | −2.0363 to −0.2280 | yes: GAIN |
| node-hours | 2.512 | 2.041 | −18.8% | −0.8478 to −0.0955 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 273.1 | +0.1% | −0.5486 to +1.0005 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 237.4 | −13.0% | −63.8846 to −6.9343 | yes: GAIN |
| response time (ms), mean | 380.9 | 354.9 | −6.8% | −36.5274 to −15.5621 | yes: GAIN |
| response time (ms), 95th percentile | 1429 | 1490 | +4.3% | −4.7130 to +126.8430 | no |
| response time (ms), 99th percentile | 1985 | 2123 | +7.0% | −53.1980 to +329.6632 | no |
| time over the response line (% of samples) | 17.04 | 16.68 | −2.1% | −1.0659 to +0.3446 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 8.4 | +5.0% | −0.1001 to +0.9001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.6 | +43.600 (native is 0) | +19.6869 to +67.5131 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.43 | 11.02 | −3.6% | −2.0437 to +1.2303 | no |
| utilisation (used / allocatable) | 0.06181 | 0.07678 | +24.2% | +0.0035 to +0.0265 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.484 | 1.467 | −1.1% | −0.0571 to +0.0246 | no |
| Omni's own CPU (cores), mean | 0 | 0.01627 | +0.016 (native is 0) | +0.0145 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.484 | 1.484 | +0.0% | −0.0418 to +0.0418 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.4 | 388.4 | −13.9% | −111.4165 to −14.4840 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.964 | 2.059 | +4.9% | −0.0757 to +0.2664 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.2 | 0.4 | +100.0% | −0.5388 to +0.9388 | no |
| pod start wait, mean (s) | 0.2 | 0.4 | +100.0% | −0.5388 to +0.9388 | no |
| host CPU busy, the real machine under kind (%) | 42.05 | 42.98 | +2.2% | +0.4177 to +1.4370 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 800.8 | 806.7 | +0.7% | +0.9967 to +10.8033 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.185 | −30.2% | −3.1770 to −0.4524 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.075 | −10.0% | −0.0476 to +0.0309 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job turnaround, submitted to done, mean (s) | 106.9 | 110.8 | +3.7% | +0.2104 to +7.7063 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.868 | −18.9% | −2.0363 to −0.2280 | yes: GAIN |
| node-hours | 2.519 | 2.041 | −19.0% | −0.8554 to −0.1016 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.1 | −0.2% | −1.2603 to +0.1498 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 237.4 | −13.2% | −64.4522 to −7.9292 | yes: GAIN |
| response time (ms), mean | 434.4 | 354.9 | −18.3% | −128.7930 to −30.1943 | yes: GAIN |
| response time (ms), 95th percentile | 1863 | 1490 | −20.0% | −687.9138 to −56.4842 | yes: GAIN |
| response time (ms), 99th percentile | 2580 | 2123 | −17.7% | −832.3941 to −81.5391 | yes: GAIN |
| time over the response line (% of samples) | 14.97 | 16.68 | +11.4% | −0.3046 to +3.7230 | no |
| failed requests (%) | 0.01212 | 0 | −100.0% | −0.0395 to +0.0153 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 8.4 | −6.7% | −0.9694 to −0.2306 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.6 | +43.600 (native is 0) | +19.6869 to +67.5131 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 24.84 | 11.02 | −55.6% | −22.4304 to −5.2129 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06163 | 0.07678 | +24.6% | +0.0027 to +0.0276 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.479 | 1.467 | −0.8% | −0.0311 to +0.0072 | no |
| Omni's own CPU (cores), mean | 0 | 0.01627 | +0.016 (native is 0) | +0.0145 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.479 | 1.484 | +0.3% | −0.0153 to +0.0240 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.7 | 388.4 | −14.8% | −123.2585 to −11.2510 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.052 | 2.059 | +0.3% | −0.1550 to +0.1687 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| host CPU busy, the real machine under kind (%) | 44.62 | 42.98 | −3.7% | −2.5752 to −0.7026 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 843.5 | 806.7 | −4.4% | −62.1546 to −11.4454 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.185 | −30.2% | −3.1770 to −0.4524 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.154 | 0.075 | −93.5% | −1.4191 to −0.7392 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3 | 0.4 | −86.7% | −3.9146 to −1.2854 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 144 | 110.8 | −23.0% | −55.2610 to −11.0307 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.894 | −18.4% | −2.0138 to −0.1986 | yes: GAIN |
| node-hours | 2.512 | 2.052 | −18.3% | −0.8383 to −0.0814 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 273.5 | +0.2% | +0.0543 to +1.1783 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 238.6 | −12.5% | −62.9287 to −5.4679 | yes: GAIN |
| response time (ms), mean | 380.9 | 407.9 | +7.1% | −19.4618 to +73.4775 | no |
| response time (ms), 95th percentile | 1429 | 1931 | +35.1% | +85.7446 to +917.2054 | yes: LOSS |
| response time (ms), 99th percentile | 1985 | 2566 | +29.3% | +107.7173 to +1055.3197 | yes: LOSS |
| time over the response line (% of samples) | 17.04 | 14.54 | −14.7% | −4.7653 to −0.2277 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 8.9 | +11.3% | +0.2737 to +1.5263 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.8 | +33.800 (native is 0) | +17.8131 to +49.7869 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.43 | 26.77 | +134.3% | +3.8925 to +26.7942 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06181 | 0.07636 | +23.5% | +0.0038 to +0.0253 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.484 | 1.474 | −0.6% | −0.0546 to +0.0361 | no |
| Omni's own CPU (cores), mean | 0 | 0.01628 | +0.016 (native is 0) | +0.0149 to +0.0177 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.484 | 1.491 | +0.5% | −0.0396 to +0.0537 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.4 | 388.7 | −13.9% | −107.8126 to −17.5982 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.964 | 1.927 | −1.9% | −0.1660 to +0.0931 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.3060 to +0.5060 | no |
| pod start wait, total (s) | 0.2 | 0.2 | ±0.0% | −0.5840 to +0.5840 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.5840 to +0.5840 | no |
| host CPU busy, the real machine under kind (%) | 42.05 | 45.63 | +8.5% | +2.0753 to +5.0733 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 800.8 | 849.5 | +6.1% | +14.9211 to +82.4789 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.228 | −29.5% | −3.1941 to −0.3505 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 1.071 | +1185.0% | +0.6529 to +1.3221 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 3.3 | +725.0% | +1.0701 to +4.7299 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 106.9 | 148.1 | +38.5% | +13.6819 to +68.6431 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*