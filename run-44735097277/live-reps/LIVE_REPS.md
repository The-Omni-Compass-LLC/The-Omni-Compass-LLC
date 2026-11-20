# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 9.473 | 9.58 |
| node-hours | 5.025 | 5.03 | 3.975 | 4.018 |
| energy, parked workers still on at idle power (Wh, declared model) | 523.9 | 524.3 | 524.3 | 524.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.9 | 524.3 | 444.9 | 448.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 481 | 570.4 | 514.6 | 665.4 |
| response time (ms), 95th percentile | 1780 | 2304 | 1984 | 2661 |
| response time (ms), 99th percentile | 2401 | 3181 | 2722 | 3821 |
| time over the response line (% of samples) | 15.15 | 18.77 | 18.55 | 24.5 |
| failed requests (%) | 0 | 0.05782 | 0.0156 | 0.1204 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 12.3 | 10.8 | 14.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 270.7 | 50.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 33.88 | 18.12 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.54 | 30.87 | 33.86 | 56.03 |
| utilisation (used / allocatable) | 0.03265 | 0.03231 | 0.04093 | 0.04083 |
| CPU used (cores), mean | 1.567 | 1.551 | 1.501 | 1.533 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05717 | 0.04012 |
| CPU used with Omni's own (cores), mean | 1.567 | 1.551 | 1.558 | 1.573 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 821.1 | 824.6 | 705.6 | 700.5 |
| HPA replicas, mean | 4.059 | 4.142 | 4.627 | 4.678 |
| pods started | 0.1 | 0.4 | 2.7 | 2.3 |
| pod start wait, total (s) | 0.3 | 0.7 | 5.5 | 5.4 |
| pod start wait, mean (s) | 0.3 | 0.3667 | 1.58 | 1.858 |
| host CPU busy, the real machine under kind (%) | 48.91 | 53.95 | 53.83 | 60.06 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 841 | 908.7 | 865.6 | 970.3 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 7.94 | 7.468 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 7.092 | 0.09167 | 11.24 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 64.3 | 0.4 | 97.1 |
| queue: job turnaround, submitted to done, mean (s) | 149.5 | 215.5 | 177.8 | 266.9 |
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
| worker nodes in service, mean | 12 | 9.58 | −20.2% | −3.8587 to −0.9810 | yes: GAIN |
| node-hours | 5.03 | 4.018 | −20.1% | −1.6178 to −0.4054 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.3 | 524.6 | +0.1% | −3.5231 to +4.2099 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.3 | 448.6 | −14.4% | −120.5630 to −30.8419 | yes: GAIN |
| response time (ms), mean | 570.4 | 665.4 | +16.6% | +12.5897 to +177.3064 | yes: LOSS |
| response time (ms), 95th percentile | 2304 | 2661 | +15.5% | −26.3564 to +739.7814 | no |
| response time (ms), 99th percentile | 3181 | 3821 | +20.1% | +124.8723 to +1155.3969 | yes: LOSS |
| time over the response line (% of samples) | 18.77 | 24.5 | +30.6% | +2.6910 to +8.7779 | yes: LOSS |
| failed requests (%) | 0.05782 | 0.1204 | +108.3% | −0.1035 to +0.2288 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.3 | 14.6 | +18.7% | −0.1093 to +4.7093 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.9 | +50.900 (native is 0) | +31.8865 to +69.9135 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 30.87 | 56.03 | +81.5% | −31.3423 to +81.6557 | no |
| utilisation (used / allocatable) | 0.03231 | 0.04083 | +26.4% | +0.0008 to +0.0162 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.551 | 1.533 | −1.2% | −0.2203 to +0.1836 | no |
| Omni's own CPU (cores), mean | 0 | 0.04012 | +0.040 (native is 0) | +0.0318 to +0.0485 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.551 | 1.573 | +1.4% | −0.1785 to +0.2221 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 824.6 | 700.5 | −15.0% | −249.0815 to +1.0529 | no |
| HPA replicas, mean | 4.142 | 4.678 | +12.9% | +0.0086 to +1.0622 | yes: power given |
| pods started | 0.4 | 2.3 | +475.0% | +0.1989 to +3.6011 | yes: power given |
| pod start wait, total (s) | 0.7 | 5.4 | +671.4% | +0.2006 to +9.1994 | yes: LOSS |
| pod start wait, mean (s) | 0.3667 | 1.858 | +406.8% | +0.3710 to +2.6123 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 53.95 | 60.06 | +11.3% | +4.7965 to +7.4115 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 908.7 | 970.3 | +6.8% | +31.9644 to +91.2356 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 7.468 | −37.8% | −7.0201 to −2.0437 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 7.092 | 11.24 | +58.5% | −5.0492 to +13.3492 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 64.3 | 97.1 | +51.0% | −42.1506 to +107.7506 | no |
| queue: job turnaround, submitted to done, mean (s) | 215.5 | 266.9 | +23.9% | +25.3735 to +77.4849 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.025 | 5.03 | +0.1% | −0.0034 to +0.0134 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 523.9 | 524.3 | +0.1% | −1.1363 to +1.8479 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.9 | 524.3 | +0.1% | −1.1363 to +1.8479 | no |
| response time (ms), mean | 481 | 570.4 | +18.6% | +7.5398 to +171.2513 | yes: LOSS |
| response time (ms), 95th percentile | 1780 | 2304 | +29.4% | +52.5763 to +995.0277 | yes: LOSS |
| response time (ms), 99th percentile | 2401 | 3181 | +32.5% | +217.9686 to +1341.2136 | yes: LOSS |
| time over the response line (% of samples) | 15.15 | 18.77 | +23.8% | +0.8676 to +6.3552 | yes: LOSS |
| failed requests (%) | 0 | 0.05782 | +0.058 (native is 0) | −0.0215 to +0.1371 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 12.3 | +50.0% | +0.8578 to +7.3422 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.54 | 30.87 | +112.3% | −15.4011 to +48.0645 | no |
| utilisation (used / allocatable) | 0.03265 | 0.03231 | −1.0% | −0.0030 to +0.0023 | no |
| CPU used (cores), mean | 1.567 | 1.551 | −1.0% | −0.1448 to +0.1127 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.567 | 1.551 | −1.0% | −0.1448 to +0.1127 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 821.1 | 824.6 | +0.4% | −45.8203 to +52.6662 | no |
| HPA replicas, mean | 4.059 | 4.142 | +2.0% | −0.2065 to +0.3720 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.4578 to +1.0578 | no |
| pod start wait, total (s) | 0.3 | 0.7 | +133.3% | −1.0385 to +1.8385 | no |
| pod start wait, mean (s) | 0.3 | 0.3667 | +22.2% | −0.8791 to +1.0124 | no |
| host CPU busy, the real machine under kind (%) | 48.91 | 53.95 | +10.3% | +3.4618 to +6.6189 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 841 | 908.7 | +8.0% | +17.7307 to +117.6693 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 7.092 | +6708.0% | −3.4719 to +17.4469 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 64.3 | +10616.7% | −31.5186 to +158.9186 | no |
| queue: job turnaround, submitted to done, mean (s) | 149.5 | 215.5 | +44.2% | +21.6753 to +110.3664 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.473 | −21.1% | −4.3056 to −0.7485 | yes: GAIN |
| node-hours | 5.025 | 3.975 | −20.9% | −1.8005 to −0.2989 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523.9 | 524.3 | +0.1% | −2.0178 to +2.6610 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.9 | 444.9 | −15.1% | −135.1256 to −22.9853 | yes: GAIN |
| response time (ms), mean | 481 | 514.6 | +7.0% | −13.6199 to +80.7767 | no |
| response time (ms), 95th percentile | 1780 | 1984 | +11.5% | −10.7203 to +418.5673 | no |
| response time (ms), 99th percentile | 2401 | 2722 | +13.4% | +88.5056 to +553.7568 | yes: LOSS |
| time over the response line (% of samples) | 15.15 | 18.55 | +22.4% | +1.0416 to +5.7540 | yes: LOSS |
| failed requests (%) | 0 | 0.0156 | +0.016 (native is 0) | −0.0079 to +0.0391 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 10.8 | +31.7% | −0.0163 to +5.2163 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 270.7 | +270.700 (native is 0) | +141.4045 to +399.9955 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.54 | 33.86 | +132.9% | −4.2580 to +42.9080 | no |
| utilisation (used / allocatable) | 0.03265 | 0.04093 | +25.4% | +0.0006 to +0.0160 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.567 | 1.501 | −4.2% | −0.1425 to +0.0108 | no |
| Omni's own CPU (cores), mean | 0 | 0.05717 | +0.057 (native is 0) | +0.0527 to +0.0617 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.567 | 1.558 | −0.6% | −0.0839 to +0.0665 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 821.1 | 705.6 | −14.1% | −225.2489 to −5.7889 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.059 | 4.627 | +14.0% | +0.1128 to +1.0220 | yes: power given |
| pods started | 0.1 | 2.7 | +2600.0% | +1.2428 to +3.9572 | yes: power given |
| pod start wait, total (s) | 0.3 | 5.5 | +1733.3% | +1.7978 to +8.6022 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.58 | +426.7% | +0.3591 to +2.2009 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 48.91 | 53.83 | +10.1% | +3.7689 to +6.0719 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 841 | 865.6 | +2.9% | −0.4442 to +49.6442 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 7.94 | −33.8% | −6.7388 to −1.3809 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.09167 | −12.0% | −0.0613 to +0.0363 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.4 | −33.3% | −0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 149.5 | 177.8 | +18.9% | +5.5868 to +51.0549 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.473 | −21.1% | −4.3056 to −0.7485 | yes: GAIN |
| node-hours | 5.03 | 3.975 | −21.0% | −1.8052 to −0.3042 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.3 | 524.3 | −0.0% | −2.7693 to +2.7010 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.3 | 444.9 | −15.1% | −135.8723 to −22.9502 | yes: GAIN |
| response time (ms), mean | 570.4 | 514.6 | −9.8% | −95.9787 to −15.6556 | yes: GAIN |
| response time (ms), 95th percentile | 2304 | 1984 | −13.9% | −705.4623 to +65.7053 | no |
| response time (ms), 99th percentile | 3181 | 2722 | −14.4% | −871.9899 to −44.9299 | yes: GAIN |
| time over the response line (% of samples) | 18.77 | 18.55 | −1.1% | −2.5658 to +2.1385 | no |
| failed requests (%) | 0.05782 | 0.0156 | −73.0% | −0.1072 to +0.0228 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.3 | 10.8 | −12.2% | −2.6802 to −0.3198 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 270.7 | +270.700 (native is 0) | +141.4045 to +399.9955 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 30.87 | 33.86 | +9.7% | −26.0420 to +32.0287 | no |
| utilisation (used / allocatable) | 0.03231 | 0.04093 | +26.7% | +0.0012 to +0.0161 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.551 | 1.501 | −3.2% | −0.1576 to +0.0580 | no |
| Omni's own CPU (cores), mean | 0 | 0.05717 | +0.057 (native is 0) | +0.0527 to +0.0617 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.551 | 1.558 | +0.5% | −0.1011 to +0.1159 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 824.6 | 705.6 | −14.4% | −222.5631 to −15.3205 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.142 | 4.627 | +11.7% | +0.0439 to +0.9253 | yes: power given |
| pods started | 0.4 | 2.7 | +575.0% | +0.8283 to +3.7717 | yes: power given |
| pod start wait, total (s) | 0.7 | 5.5 | +685.7% | +1.0786 to +8.5214 | yes: LOSS |
| pod start wait, mean (s) | 0.3667 | 1.58 | +330.9% | +0.4098 to +2.0168 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 53.95 | 53.83 | −0.2% | −1.1086 to +0.8686 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 908.7 | 865.6 | −4.7% | −71.4076 to −14.7924 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 7.94 | −33.8% | −6.7388 to −1.3809 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 7.092 | 0.09167 | −98.7% | −17.4471 to +3.4471 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 64.3 | 0.4 | −99.4% | −159.0430 to +31.2430 | no |
| queue: job turnaround, submitted to done, mean (s) | 215.5 | 177.8 | −17.5% | −63.2542 to −12.1458 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.58 | −20.2% | −3.8587 to −0.9810 | yes: GAIN |
| node-hours | 5.025 | 4.018 | −20.0% | −1.6151 to −0.3981 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523.9 | 524.6 | +0.1% | −2.6291 to +4.0274 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.9 | 448.6 | −14.4% | −119.8715 to −30.8219 | yes: GAIN |
| response time (ms), mean | 481 | 665.4 | +38.3% | +59.3464 to +309.3407 | yes: LOSS |
| response time (ms), 95th percentile | 1780 | 2661 | +49.5% | +425.1101 to +1335.9189 | yes: LOSS |
| response time (ms), 99th percentile | 2401 | 3821 | +59.1% | +719.2695 to +2120.1819 | yes: LOSS |
| time over the response line (% of samples) | 15.15 | 24.5 | +61.7% | +5.3445 to +13.3472 | yes: LOSS |
| failed requests (%) | 0 | 0.1204 | +0.120 (native is 0) | −0.1111 to +0.3520 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 14.6 | +78.0% | +2.7965 to +10.0035 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.9 | +50.900 (native is 0) | +31.8865 to +69.9135 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.54 | 56.03 | +285.4% | −5.4288 to +88.4055 | no |
| utilisation (used / allocatable) | 0.03265 | 0.04083 | +25.1% | +0.0006 to +0.0158 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.567 | 1.533 | −2.2% | −0.1792 to +0.1104 | no |
| Omni's own CPU (cores), mean | 0 | 0.04012 | +0.040 (native is 0) | +0.0318 to +0.0485 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.567 | 1.573 | +0.4% | −0.1338 to +0.1453 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 821.1 | 700.5 | −14.7% | −246.5158 to +5.3331 | no |
| HPA replicas, mean | 4.059 | 4.678 | +15.2% | +0.1137 to +1.1227 | yes: power given |
| pods started | 0.1 | 2.3 | +2200.0% | +0.8597 to +3.5403 | yes: power given |
| pod start wait, total (s) | 0.3 | 5.4 | +1700.0% | +1.0473 to +9.1527 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.858 | +519.4% | +0.6786 to +2.4380 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 48.91 | 60.06 | +22.8% | +9.0332 to +13.2555 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 841 | 970.3 | +15.4% | +60.0164 to +198.5836 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 7.468 | −37.8% | −7.0201 to −2.0437 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 11.24 | +10692.0% | −1.7065 to +23.9815 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 97.1 | +16083.3% | −14.1071 to +207.1071 | no |
| queue: job turnaround, submitted to done, mean (s) | 149.5 | 266.9 | +78.6% | +58.9408 to +175.9592 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*