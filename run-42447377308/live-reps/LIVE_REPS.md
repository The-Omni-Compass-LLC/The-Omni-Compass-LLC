# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.09 | 11.03 |
| node-hours | 5.03 | 5.029 | 4.236 | 4.621 |
| energy, parked workers still on at idle power (Wh, declared model) | 526.5 | 526.4 | 528.1 | 527 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.5 | 526.4 | 467.9 | 496.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 659.9 | 901.3 | 737.2 | 1155 |
| response time (ms), 95th percentile | 2618 | 3171 | 3053 | 4179 |
| response time (ms), 99th percentile | 3522 | 4305 | 4091 | 5460 |
| time over the response line (% of samples) | 22.58 | 31.55 | 25.32 | 40.39 |
| failed requests (%) | 0 | 0.0445 | 0.06204 | 0.3016 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.5 | 14.2 | 13 | 18.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 100.9 | 60.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 33.33 | 18.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.87 | 35.69 | 21.55 | 68.16 |
| utilisation (used / allocatable) | 0.0356 | 0.03543 | 0.04284 | 0.03923 |
| CPU used (cores), mean | 1.709 | 1.701 | 1.72 | 1.727 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05561 | 0.0561 |
| CPU used with Omni's own (cores), mean | 1.709 | 1.701 | 1.776 | 1.783 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 755.6 | 756.6 | 655.8 | 691.5 |
| HPA replicas, mean | 4.015 | 4.06 | 4.727 | 5.513 |
| pods started | 0.1 | 0.2 | 3.1 | 3.8 |
| pod start wait, total (s) | 0.2 | 0.7 | 9 | 10.8 |
| pod start wait, mean (s) | 0.2 | 0.7 | 2.551 | 2.544 |
| host CPU busy, the real machine under kind (%) | 52.39 | 58.92 | 57.92 | 65.9 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 895.2 | 1003 | 934.5 | 1079 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 8.63 | 9.795 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 14.8 | 0.125 | 9.262 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 108 | 0.7 | 50.3 |
| queue: job turnaround, submitted to done, mean (s) | 199.2 | 275.9 | 234.8 | 368 |
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
| worker nodes in service, mean | 12 | 11.03 | −8.1% | −1.8420 to −0.1012 | yes: GAIN |
| node-hours | 5.029 | 4.621 | −8.1% | −0.7714 to −0.0434 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.4 | 527 | +0.1% | −2.3491 to +3.5826 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.4 | 496.5 | −5.7% | −56.0291 to −3.7999 | yes: GAIN |
| response time (ms), mean | 901.3 | 1155 | +28.2% | +161.7944 to +346.4724 | yes: LOSS |
| response time (ms), 95th percentile | 3171 | 4179 | +31.8% | +587.0117 to +1429.8733 | yes: LOSS |
| response time (ms), 99th percentile | 4305 | 5460 | +26.8% | +460.4974 to +1848.0824 | yes: LOSS |
| time over the response line (% of samples) | 31.55 | 40.39 | +28.0% | +4.3327 to +13.3624 | yes: LOSS |
| failed requests (%) | 0.0445 | 0.3016 | +577.9% | −0.0466 to +0.5608 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.2 | 18.1 | +27.5% | +0.8568 to +6.9432 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 60.7 | +60.700 (native is 0) | +33.4368 to +87.9632 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 35.69 | 68.16 | +91.0% | −14.7699 to +79.7199 | no |
| utilisation (used / allocatable) | 0.03543 | 0.03923 | +10.7% | −0.0022 to +0.0098 | no |
| CPU used (cores), mean | 1.701 | 1.727 | +1.5% | −0.1808 to +0.2328 | no |
| Omni's own CPU (cores), mean | 0 | 0.0561 | +0.056 (native is 0) | +0.0493 to +0.0629 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.701 | 1.783 | +4.8% | −0.1228 to +0.2871 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 756.6 | 691.5 | −8.6% | −171.1669 to +40.9434 | no |
| HPA replicas, mean | 4.06 | 5.513 | +35.8% | −0.0886 to +2.9928 | no |
| pods started | 0.2 | 3.8 | +1800.0% | +2.3749 to +4.8251 | yes: power given |
| pod start wait, total (s) | 0.7 | 10.8 | +1442.9% | +6.2932 to +13.9068 | yes: LOSS |
| pod start wait, mean (s) | 0.7 | 2.544 | +263.5% | +0.7294 to +2.9591 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 58.92 | 65.9 | +11.9% | +6.4421 to +7.5340 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1003 | 1079 | +7.6% | +58.8354 to +93.3646 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.795 | −18.4% | −4.0908 to −0.3187 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 14.8 | 9.263 | −37.4% | −25.5343 to +14.4593 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 108 | 50.3 | −53.4% | −192.7612 to +77.3612 | no |
| queue: job turnaround, submitted to done, mean (s) | 275.9 | 368 | +33.4% | +56.9182 to +127.3568 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.03 | 5.029 | −0.0% | −0.0222 to +0.0189 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.5 | 526.4 | −0.0% | −2.6981 to +2.5579 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.5 | 526.4 | −0.0% | −2.6981 to +2.5579 | no |
| response time (ms), mean | 659.9 | 901.3 | +36.6% | +104.6100 to +378.0251 | yes: LOSS |
| response time (ms), 95th percentile | 2618 | 3171 | +21.1% | +234.5698 to +871.7902 | yes: LOSS |
| response time (ms), 99th percentile | 3522 | 4305 | +22.3% | +362.8212 to +1204.4804 | yes: LOSS |
| time over the response line (% of samples) | 22.58 | 31.55 | +39.7% | +5.1208 to +12.8162 | yes: LOSS |
| failed requests (%) | 0 | 0.0445 | +0.044 (native is 0) | −0.0194 to +0.1084 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.5 | 14.2 | +23.5% | +1.5295 to +3.8705 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.87 | 35.68 | +124.9% | +1.2671 to +38.3662 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0356 | 0.03543 | −0.5% | −0.0019 to +0.0016 | no |
| CPU used (cores), mean | 1.709 | 1.701 | −0.5% | −0.0924 to +0.0758 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.709 | 1.701 | −0.5% | −0.0924 to +0.0758 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 755.6 | 756.6 | +0.1% | −30.1653 to +32.2656 | no |
| HPA replicas, mean | 4.015 | 4.06 | +1.1% | −0.1456 to +0.2364 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.3060 to +0.5060 | no |
| pod start wait, total (s) | 0.2 | 0.7 | +250.0% | −0.8168 to +1.8168 | no |
| pod start wait, mean (s) | 0.2 | 0.7 | +250.0% | −0.8168 to +1.8168 | no |
| host CPU busy, the real machine under kind (%) | 52.39 | 58.92 | +12.5% | +4.7916 to +8.2562 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 895.2 | 1003 | +12.0% | +53.1312 to +161.8688 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 14.8 | +12148.3% | −0.5402 to +29.8985 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 108 | +15328.6% | −4.4600 to +219.0600 | no |
| queue: job turnaround, submitted to done, mean (s) | 199.2 | 275.9 | +38.4% | +34.2982 to +118.9184 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.09 | −15.9% | −3.4980 to −0.3287 | yes: GAIN |
| node-hours | 5.03 | 4.236 | −15.8% | −1.4531 to −0.1364 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.5 | 528.1 | +0.3% | −0.3809 to +3.7094 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.5 | 467.9 | −11.1% | −108.2650 to −8.9690 | yes: GAIN |
| response time (ms), mean | 659.9 | 737.2 | +11.7% | −5.5289 to +160.1400 | no |
| response time (ms), 95th percentile | 2618 | 3053 | +16.6% | +113.2531 to +756.6569 | yes: LOSS |
| response time (ms), 99th percentile | 3522 | 4091 | +16.2% | +98.1301 to +1039.8747 | yes: LOSS |
| time over the response line (% of samples) | 22.58 | 25.32 | +12.2% | +1.0855 to +4.4058 | yes: LOSS |
| failed requests (%) | 0 | 0.06204 | +0.062 (native is 0) | −0.0120 to +0.1361 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.5 | 13 | +13.0% | +0.5315 to +2.4685 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 100.9 | +100.900 (native is 0) | +42.2832 to +159.5168 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.87 | 21.55 | +35.8% | +1.7401 to +9.6165 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0356 | 0.04284 | +20.3% | +0.0022 to +0.0122 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.709 | 1.72 | +0.7% | −0.0641 to +0.0868 | no |
| Omni's own CPU (cores), mean | 0 | 0.05561 | +0.056 (native is 0) | +0.0506 to +0.0606 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.709 | 1.776 | +3.9% | −0.0120 to +0.1459 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 755.6 | 655.8 | −13.2% | −164.8508 to −34.6755 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.015 | 4.727 | +17.7% | +0.2422 to +1.1809 | yes: power given |
| pods started | 0.1 | 3.1 | +3000.0% | +1.4184 to +4.5816 | yes: power given |
| pod start wait, total (s) | 0.2 | 9 | +4400.0% | +3.9744 to +13.6256 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 2.551 | +1175.4% | +1.5325 to +3.1690 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.39 | 57.92 | +10.5% | +4.0239 to +7.0208 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 895.2 | 934.5 | +4.4% | +7.0097 to +71.5903 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.63 | −28.1% | −5.8161 to −0.9235 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 0.125 | +3.4% | −0.0492 to +0.0576 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.7 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 199.2 | 234.8 | +17.8% | +7.0630 to +63.9870 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.09 | −15.9% | −3.4980 to −0.3287 | yes: GAIN |
| node-hours | 5.029 | 4.236 | −15.8% | −1.4564 to −0.1298 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.4 | 528.1 | +0.3% | −0.7466 to +4.2154 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.4 | 467.9 | −11.1% | −109.0133 to −8.0805 | yes: GAIN |
| response time (ms), mean | 901.3 | 737.2 | −18.2% | −280.4895 to −47.5345 | yes: GAIN |
| response time (ms), 95th percentile | 3171 | 3053 | −3.7% | −379.4791 to +143.0291 | no |
| response time (ms), 99th percentile | 4305 | 4091 | −5.0% | −726.8185 to +297.5217 | no |
| time over the response line (% of samples) | 31.55 | 25.32 | −19.7% | −10.3139 to −2.1317 | yes: GAIN |
| failed requests (%) | 0.0445 | 0.06204 | +39.4% | −0.0778 to +0.1129 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.2 | 13 | −8.5% | −2.8101 to +0.4101 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 100.9 | +100.900 (native is 0) | +42.2832 to +159.5168 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 35.69 | 21.55 | −39.6% | −31.8124 to +3.5358 | no |
| utilisation (used / allocatable) | 0.03543 | 0.04284 | +20.9% | +0.0026 to +0.0123 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.701 | 1.72 | +1.2% | −0.0831 to +0.1225 | no |
| Omni's own CPU (cores), mean | 0 | 0.05561 | +0.056 (native is 0) | +0.0506 to +0.0606 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.701 | 1.776 | +4.4% | −0.0317 to +0.1822 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 756.6 | 655.8 | −13.3% | −162.9571 to −38.6694 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.06 | 4.727 | +16.4% | +0.2027 to +1.1296 | yes: power given |
| pods started | 0.2 | 3.1 | +1450.0% | +1.4914 to +4.3086 | yes: power given |
| pod start wait, total (s) | 0.7 | 9 | +1185.7% | +4.1012 to +12.4988 | yes: LOSS |
| pod start wait, mean (s) | 0.7 | 2.551 | +264.4% | +0.7378 to +2.9636 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 58.92 | 57.92 | −1.7% | −2.3605 to +0.3573 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1003 | 934.5 | −6.8% | −106.0262 to −30.3738 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 8.63 | −28.1% | −5.8161 to −0.9235 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 14.8 | 0.125 | −99.2% | −29.8985 to +0.5485 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 108 | 0.7 | −99.4% | −219.0600 to +4.4600 | no |
| queue: job turnaround, submitted to done, mean (s) | 275.9 | 234.8 | −14.9% | −72.3764 to −9.7903 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.03 | −8.1% | −1.8420 to −0.1012 | yes: GAIN |
| node-hours | 5.03 | 4.621 | −8.1% | −0.7688 to −0.0494 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.5 | 527 | +0.1% | −2.7007 to +3.7940 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.5 | 496.5 | −5.7% | −55.3541 to −4.6152 | yes: GAIN |
| response time (ms), mean | 659.9 | 1155 | +75.1% | +281.9340 to +708.9679 | yes: LOSS |
| response time (ms), 95th percentile | 2618 | 4179 | +59.7% | +1070.8408 to +2052.4042 | yes: LOSS |
| response time (ms), 99th percentile | 3522 | 5460 | +55.0% | +1316.0863 to +2559.7951 | yes: LOSS |
| time over the response line (% of samples) | 22.58 | 40.39 | +78.9% | +15.6368 to +19.9953 | yes: LOSS |
| failed requests (%) | 0 | 0.3016 | +0.302 (native is 0) | −0.0477 to +0.6509 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.5 | 18.1 | +57.4% | +3.5243 to +9.6757 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 60.7 | +60.700 (native is 0) | +33.4368 to +87.9632 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.87 | 68.16 | +329.5% | +8.0302 to +96.5531 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0356 | 0.03923 | +10.2% | −0.0021 to +0.0094 | no |
| CPU used (cores), mean | 1.709 | 1.727 | +1.0% | −0.1571 to +0.1925 | no |
| Omni's own CPU (cores), mean | 0 | 0.0561 | +0.056 (native is 0) | +0.0493 to +0.0629 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.709 | 1.783 | +4.3% | −0.0974 to +0.2451 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 755.6 | 691.5 | −8.5% | −168.2739 to +40.1506 | no |
| HPA replicas, mean | 4.015 | 5.513 | +37.3% | −0.0868 to +3.0819 | no |
| pods started | 0.1 | 3.8 | +3700.0% | +2.2283 to +5.1717 | yes: power given |
| pod start wait, total (s) | 0.2 | 10.8 | +5300.0% | +6.0735 to +15.1265 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 2.544 | +1172.1% | +1.5720 to +3.1166 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.39 | 65.9 | +25.8% | +11.7260 to +15.2980 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 895.2 | 1079 | +20.5% | +124.2671 to +242.9329 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.795 | −18.4% | −4.0908 to −0.3187 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 9.262 | +7565.5% | −2.4040 to +20.6874 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 50.3 | +7085.7% | −23.1930 to +122.3930 | no |
| queue: job turnaround, submitted to done, mean (s) | 199.2 | 368 | +84.7% | +114.2577 to +223.2340 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*