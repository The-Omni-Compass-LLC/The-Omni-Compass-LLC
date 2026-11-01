# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.42 | 11.07 |
| node-hours | 5.028 | 5.029 | 4.365 | 4.635 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.6 | 526.9 | 526.7 | 525.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.6 | 526.9 | 476.8 | 496.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 599.3 | 828.5 | 614.7 | 959 |
| response time (ms), 95th percentile | 2339 | 3027 | 2591 | 3476 |
| response time (ms), 99th percentile | 3156 | 4052 | 3484 | 4806 |
| time over the response line (% of samples) | 22.33 | 29.38 | 22.29 | 33.25 |
| failed requests (%) | 0 | 0.01607 | 0.01423 | 0.08076 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 12.9 | 12 | 15.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 70.6 | 57.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | 33.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.21 | 27.69 | 16.39 | 60.26 |
| utilisation (used / allocatable) | 0.03422 | 0.03634 | 0.04094 | 0.03788 |
| CPU used (cores), mean | 1.643 | 1.744 | 1.684 | 1.677 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01279 | 0.01297 |
| CPU used with Omni's own (cores), mean | 1.643 | 1.744 | 1.696 | 1.69 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 783.4 | 744.4 | 684.8 | 724.3 |
| HPA replicas, mean | 3.926 | 4.07 | 4.274 | 4.221 |
| pods started | 0 | 0.1 | 0.7 | 1.3 |
| pod start wait, total (s) | 0 | 0.3 | 1.1 | 4.7 |
| pod start wait, mean (s) | 0 | 0.3 | 0.75 | 2.863 |
| host CPU busy, the real machine under kind (%) | 51.06 | 57.8 | 53.18 | 60.53 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 876.4 | 998.1 | 898.2 | 1031 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.518 | 10.25 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 21.43 | 0.0625 | 15.44 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 137.6 | 0.3 | 111.9 |
| queue: job turnaround, submitted to done, mean (s) | 185.1 | 260.1 | 199.7 | 317.5 |
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
| worker nodes in service, mean | 12 | 11.07 | −7.8% | −1.9918 to +0.1257 | no |
| node-hours | 5.029 | 4.635 | −7.8% | −0.8446 to +0.0572 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.9 | 525.9 | −0.2% | −4.0425 to +1.9162 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.9 | 496.6 | −5.8% | −63.6795 to +3.0490 | no |
| response time (ms), mean | 828.5 | 959 | +15.8% | +23.3653 to +237.6514 | yes: LOSS |
| response time (ms), 95th percentile | 3027 | 3476 | +14.8% | +57.5095 to +841.3615 | yes: LOSS |
| response time (ms), 99th percentile | 4052 | 4806 | +18.6% | +272.7692 to +1235.0298 | yes: LOSS |
| time over the response line (% of samples) | 29.38 | 33.25 | +13.2% | +1.5218 to +6.2116 | yes: LOSS |
| failed requests (%) | 0.01607 | 0.08076 | +402.5% | −0.0180 to +0.1474 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.9 | 15.6 | +20.9% | +0.0653 to +5.3347 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 57.8 | +57.800 (native is 0) | +25.2454 to +90.3546 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 27.69 | 60.26 | +117.6% | −29.1776 to +94.3143 | no |
| utilisation (used / allocatable) | 0.03634 | 0.03788 | +4.2% | −0.0048 to +0.0079 | no |
| CPU used (cores), mean | 1.744 | 1.677 | −3.8% | −0.3033 to +0.1691 | no |
| Omni's own CPU (cores), mean | 0 | 0.01297 | +0.013 (native is 0) | +0.0119 to +0.0141 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.744 | 1.69 | −3.1% | −0.2902 to +0.1820 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 744.4 | 724.3 | −2.7% | −135.9014 to +95.7371 | no |
| HPA replicas, mean | 4.07 | 4.221 | +3.7% | −0.1082 to +0.4117 | no |
| pods started | 0.1 | 1.3 | +1200.0% | −0.0526 to +2.4526 | no |
| pod start wait, total (s) | 0.3 | 4.7 | +1466.7% | −0.4538 to +9.2538 | no |
| pod start wait, mean (s) | 0.3 | 2.863 | +854.4% | −1.5099 to +6.6365 | no |
| host CPU busy, the real machine under kind (%) | 57.8 | 60.53 | +4.7% | +1.9006 to +3.5713 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 998.1 | 1031 | +3.3% | +11.2853 to +54.7147 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.25 | −14.6% | −3.7271 to +0.2206 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 21.43 | 15.44 | −28.0% | −28.4835 to +16.5002 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 137.6 | 111.9 | −18.7% | −156.4576 to +105.0576 | no |
| queue: job turnaround, submitted to done, mean (s) | 260.1 | 317.5 | +22.1% | +15.6067 to +99.1683 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.028 | 5.029 | +0.0% | −0.0103 to +0.0117 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.6 | 526.9 | +0.3% | −0.4018 to +3.1260 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.6 | 526.9 | +0.3% | −0.4018 to +3.1260 | no |
| response time (ms), mean | 599.3 | 828.5 | +38.2% | +93.9406 to +364.3273 | yes: LOSS |
| response time (ms), 95th percentile | 2339 | 3027 | +29.4% | +297.1920 to +1079.5510 | yes: LOSS |
| response time (ms), 99th percentile | 3156 | 4052 | +28.4% | +321.9848 to +1469.8440 | yes: LOSS |
| time over the response line (% of samples) | 22.33 | 29.38 | +31.6% | +2.8148 to +11.2807 | yes: LOSS |
| failed requests (%) | 0 | 0.01607 | +0.016 (native is 0) | −0.0082 to +0.0403 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 12.9 | +15.2% | +0.5295 to +2.8705 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.21 | 27.69 | +37.1% | −8.7001 to +23.6768 | no |
| utilisation (used / allocatable) | 0.03422 | 0.03634 | +6.2% | +0.0005 to +0.0038 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.643 | 1.744 | +6.2% | +0.0222 to +0.1810 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.643 | 1.744 | +6.2% | +0.0222 to +0.1810 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 783.4 | 744.4 | −5.0% | −66.7057 to −11.2869 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.926 | 4.07 | +3.6% | −0.1083 to +0.3948 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 51.06 | 57.8 | +13.2% | +4.7507 to +8.7176 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 876.4 | 998.1 | +13.9% | +53.7303 to +189.6697 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 21.43 | +24390.5% | +2.0080 to +40.6754 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 137.6 | +27420.0% | +23.3462 to +250.8538 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 185.1 | 260.1 | +40.5% | +33.0895 to +116.9271 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.42 | −13.2% | −3.3370 to +0.1696 | no |
| node-hours | 5.028 | 4.365 | −13.2% | −1.3961 to +0.0697 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.6 | 526.7 | +0.2% | −0.2900 to +2.5371 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.6 | 476.8 | −9.3% | −104.4175 to +6.7812 | no |
| response time (ms), mean | 599.3 | 614.7 | +2.6% | −24.3630 to +55.1536 | no |
| response time (ms), 95th percentile | 2339 | 2591 | +10.8% | +71.9369 to +432.0031 | yes: LOSS |
| response time (ms), 99th percentile | 3156 | 3484 | +10.4% | +45.5392 to +609.7432 | yes: LOSS |
| time over the response line (% of samples) | 22.33 | 22.29 | −0.2% | −1.1643 to +1.0744 | no |
| failed requests (%) | 0 | 0.01423 | +0.014 (native is 0) | −0.0180 to +0.0464 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 12 | +7.1% | +0.1427 to +1.4573 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 70.6 | +70.600 (native is 0) | +27.3264 to +113.8736 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.21 | 16.39 | −18.9% | −9.9528 to +2.3262 | no |
| utilisation (used / allocatable) | 0.03422 | 0.04094 | +19.6% | +0.0013 to +0.0122 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.643 | 1.684 | +2.5% | −0.0381 to +0.1203 | no |
| Omni's own CPU (cores), mean | 0 | 0.01279 | +0.013 (native is 0) | +0.0117 to +0.0139 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.643 | 1.696 | +3.3% | −0.0253 to +0.1331 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 783.4 | 684.8 | −12.6% | −178.4774 to −18.7210 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.926 | 4.274 | +8.9% | +0.0158 to +0.6793 | yes: power given |
| pods started | 0 | 0.7 | +0.700 (native is 0) | +0.1111 to +1.2889 | yes: power given |
| pod start wait, total (s) | 0 | 1.1 | +1.100 (native is 0) | +0.0634 to +2.1366 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.75 | +0.750 (native is 0) | +0.1363 to +1.3637 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.06 | 53.18 | +4.1% | +1.2129 to +3.0181 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 876.4 | 898.2 | +2.5% | +4.2016 to +39.3984 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.518 | −20.7% | −5.1929 to +0.2291 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 0.0625 | −28.6% | −0.1118 to +0.0618 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.3 | −40.0% | −0.8573 to +0.4573 | no |
| queue: job turnaround, submitted to done, mean (s) | 185.1 | 199.7 | +7.9% | +2.8976 to +26.3024 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.42 | −13.2% | −3.3370 to +0.1696 | no |
| node-hours | 5.029 | 4.365 | −13.2% | −1.3970 to +0.0692 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.9 | 526.7 | −0.0% | −1.4667 to +0.9895 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.9 | 476.8 | −9.5% | −105.0208 to +4.6603 | no |
| response time (ms), mean | 828.5 | 614.7 | −25.8% | −331.4423 to −96.0350 | yes: GAIN |
| response time (ms), 95th percentile | 3027 | 2591 | −14.4% | −725.3132 to −147.4898 | yes: GAIN |
| response time (ms), 99th percentile | 4052 | 3484 | −14.0% | −1045.8477 to −90.6987 | yes: GAIN |
| time over the response line (% of samples) | 29.38 | 22.29 | −24.1% | −11.5118 to −2.6737 | yes: GAIN |
| failed requests (%) | 0.01607 | 0.01423 | −11.4% | −0.0265 to +0.0229 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.9 | 12 | −7.0% | −2.3484 to +0.5484 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 70.6 | +70.600 (native is 0) | +27.3264 to +113.8736 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 27.69 | 16.39 | −40.8% | −30.3447 to +7.7413 | no |
| utilisation (used / allocatable) | 0.03634 | 0.04094 | +12.7% | −0.0015 to +0.0107 | no |
| CPU used (cores), mean | 1.744 | 1.684 | −3.5% | −0.1404 to +0.0193 | no |
| Omni's own CPU (cores), mean | 0 | 0.01279 | +0.013 (native is 0) | +0.0117 to +0.0139 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.744 | 1.696 | −2.7% | −0.1275 to +0.0320 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 744.4 | 684.8 | −8.0% | −142.3089 to +23.1031 | no |
| HPA replicas, mean | 4.07 | 4.274 | +5.0% | −0.0342 to +0.4428 | no |
| pods started | 0.1 | 0.7 | +600.0% | +0.0999 to +1.1001 | yes: power given |
| pod start wait, total (s) | 0.3 | 1.1 | +266.7% | +0.0612 to +1.5388 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 0.75 | +150.0% | −0.1909 to +1.0909 | no |
| host CPU busy, the real machine under kind (%) | 57.8 | 53.18 | −8.0% | −6.0314 to −3.2059 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 998.1 | 898.2 | −10.0% | −153.6401 to −46.1599 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.518 | −20.7% | −5.1929 to +0.2291 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 21.43 | 0.0625 | −99.7% | −40.7389 to −1.9944 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 137.6 | 0.3 | −99.8% | −251.2813 to −23.3187 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 260.1 | 199.7 | −23.2% | −95.0659 to −25.7508 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.07 | −7.8% | −1.9918 to +0.1257 | no |
| node-hours | 5.028 | 4.635 | −7.8% | −0.8433 to +0.0573 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.6 | 525.9 | +0.1% | −2.1294 to +2.7273 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.6 | 496.6 | −5.5% | −62.9749 to +5.0687 | no |
| response time (ms), mean | 599.3 | 959 | +60.0% | +154.8162 to +564.4685 | yes: LOSS |
| response time (ms), 95th percentile | 2339 | 3476 | +48.7% | +603.9404 to +1671.6736 | yes: LOSS |
| response time (ms), 99th percentile | 3156 | 4806 | +52.3% | +950.4220 to +2349.2058 | yes: LOSS |
| time over the response line (% of samples) | 22.33 | 33.25 | +48.9% | +6.7676 to +15.0613 | yes: LOSS |
| failed requests (%) | 0 | 0.08076 | +0.081 (native is 0) | −0.0125 to +0.1740 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 15.6 | +39.3% | +2.5779 to +6.2221 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 57.8 | +57.800 (native is 0) | +25.2454 to +90.3546 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.21 | 60.26 | +198.3% | −14.0689 to +94.1822 | no |
| utilisation (used / allocatable) | 0.03422 | 0.03788 | +10.7% | −0.0017 to +0.0090 | no |
| CPU used (cores), mean | 1.643 | 1.677 | +2.1% | −0.1603 to +0.2294 | no |
| Omni's own CPU (cores), mean | 0 | 0.01297 | +0.013 (native is 0) | +0.0119 to +0.0141 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.643 | 1.69 | +2.9% | −0.1473 to +0.2423 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 783.4 | 724.3 | −7.5% | −166.7429 to +48.5860 | no |
| HPA replicas, mean | 3.926 | 4.221 | +7.5% | −0.0288 to +0.6188 | no |
| pods started | 0 | 1.3 | +1.300 (native is 0) | +0.1295 to +2.4705 | yes: power given |
| pod start wait, total (s) | 0 | 4.7 | +4.700 (native is 0) | +0.0637 to +9.3363 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.863 | +2.863 (native is 0) | −1.0294 to +6.7561 | no |
| host CPU busy, the real machine under kind (%) | 51.06 | 60.53 | +18.5% | +7.0627 to +11.8775 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 876.4 | 1031 | +17.7% | +81.0438 to +228.3562 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.25 | −14.6% | −3.7271 to +0.2206 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 15.44 | +17542.9% | −3.3934 to +34.0934 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 111.9 | +22280.0% | −18.3385 to +241.1385 | no |
| queue: job turnaround, submitted to done, mean (s) | 185.1 | 317.5 | +71.5% | +63.3874 to +201.4043 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*