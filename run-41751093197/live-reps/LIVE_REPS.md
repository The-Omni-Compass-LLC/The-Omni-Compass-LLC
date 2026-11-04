# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.511 | 1.513 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.2 | 158.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.2 | 158.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 141.5 | 75.17 | 78.07 |
| response time (ms), 95th percentile | 317.1 | 108.7 | 109.3 |
| response time (ms), 99th percentile | 497.5 | 152.8 | 142 |
| time over the response line (% of samples) | 1.548 | 0.01212 | 0.2903 |
| failed requests (%) | 0 | 0 | 0.07416 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | 0.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.2 | 29.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 | 42.86 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.21 | 0.1033 |
| utilisation (used / allocatable) | 0.03664 | 0.0352 | 0.0362 |
| CPU used (cores), mean | 0.8793 | 0.8449 | 0.8688 |
| Omni's own CPU (cores), mean | 0 | 0.03392 | 0.03522 |
| CPU used with Omni's own (cores), mean | 0.8793 | 0.8788 | 0.9041 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 767.9 | 788.7 | 765.6 |
| HPA replicas, mean | 8.392 | 8.427 | 9.297 |
| pods started | 5.2 | 5 | 10.7 |
| pod start wait, total (s) | 7.3 | 7.3 | 19.1 |
| pod start wait, mean (s) | 1.463 | 1.433 | 1.869 |
| host CPU busy, the real machine under kind (%) | 26.79 | 26.99 | 27.83 |
| host cores (the real machine under kind) | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan |

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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.511 | 1.513 | +0.1% | −0.0003 to +0.0036 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.2 | −0.1% | −0.5622 to +0.1520 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.2 | −0.1% | −0.5622 to +0.1520 | no |
| response time (ms), mean | 141.5 | 75.17 | −46.9% | −87.3925 to −45.3114 | yes: GAIN |
| response time (ms), 95th percentile | 317.1 | 108.7 | −65.7% | −271.9365 to −144.6965 | yes: GAIN |
| response time (ms), 99th percentile | 497.5 | 152.8 | −69.3% | −444.7728 to −244.6072 | yes: GAIN |
| time over the response line (% of samples) | 1.548 | 0.01212 | −99.2% | −2.7978 to −0.2749 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | −100.0% | −3.6986 to −0.1014 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.2 | +19.200 (native is 0) | +17.8597 to +20.5403 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.21 | +31.2% | −0.2891 to +0.3891 | no |
| utilisation (used / allocatable) | 0.03664 | 0.0352 | −3.9% | −0.0022 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8793 | 0.8449 | −3.9% | −0.0538 to −0.0149 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03392 | +0.034 (native is 0) | +0.0290 to +0.0389 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8793 | 0.8788 | −0.0% | −0.0158 to +0.0149 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 767.9 | 788.7 | +2.7% | +7.0129 to +34.6343 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.392 | 8.427 | +0.4% | −0.1775 to +0.2479 | no |
| pods started | 5.2 | 5 | −3.8% | −1.5821 to +1.1821 | no |
| pod start wait, total (s) | 7.3 | 7.3 | ±0.0% | −2.9396 to +2.9396 | no |
| pod start wait, mean (s) | 1.463 | 1.433 | −2.1% | −0.4096 to +0.3496 | no |
| host CPU busy, the real machine under kind (%) | 26.79 | 26.99 | +0.7% | −0.3188 to +0.7083 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.514 | +0.2% | −0.0043 to +0.0103 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.6 | +0.1% | −0.4756 to +0.8554 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.6 | +0.1% | −0.4756 to +0.8554 | no |
| response time (ms), mean | 141.5 | 78.07 | −44.8% | −84.4468 to −42.4553 | yes: GAIN |
| response time (ms), 95th percentile | 317.1 | 109.3 | −65.5% | −272.4935 to −143.1005 | yes: GAIN |
| response time (ms), 99th percentile | 497.5 | 142 | −71.5% | −468.5693 to −242.3943 | yes: GAIN |
| time over the response line (% of samples) | 1.548 | 0.2903 | −81.2% | −2.5684 to +0.0522 | no |
| failed requests (%) | 0 | 0.07416 | +0.074 (native is 0) | −0.0005 to +0.1488 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0.5 | −73.7% | −3.3720 to +0.5720 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.4 | +29.400 (native is 0) | +21.1115 to +37.6885 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.1033 | −35.4% | −0.3193 to +0.2060 | no |
| utilisation (used / allocatable) | 0.03664 | 0.0362 | −1.2% | −0.0013 to +0.0004 | no |
| CPU used (cores), mean | 0.8793 | 0.8688 | −1.2% | −0.0316 to +0.0107 | no |
| Omni's own CPU (cores), mean | 0 | 0.03522 | +0.035 (native is 0) | +0.0303 to +0.0401 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8793 | 0.9041 | +2.8% | +0.0056 to +0.0440 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 767.9 | 765.6 | −0.3% | −26.9020 to +22.4317 | no |
| HPA replicas, mean | 8.392 | 9.297 | +10.8% | +0.5352 to +1.2736 | yes: power given |
| pods started | 5.2 | 10.7 | +105.8% | +3.3082 to +7.6918 | yes: power given |
| pod start wait, total (s) | 7.3 | 19.1 | +161.6% | +9.4687 to +14.1313 | yes: LOSS |
| pod start wait, mean (s) | 1.463 | 1.869 | +27.8% | +0.0102 to +0.8021 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 26.79 | 27.83 | +3.9% | +0.6472 to +1.4315 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.514 | +0.1% | −0.0061 to +0.0088 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 158.6 | +0.2% | −0.3306 to +1.1206 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 158.6 | +0.2% | −0.3306 to +1.1206 | no |
| response time (ms), mean | 75.17 | 78.07 | +3.9% | +1.1441 to +4.6577 | yes: LOSS |
| response time (ms), 95th percentile | 108.7 | 109.3 | +0.5% | −1.2144 to +2.2534 | no |
| response time (ms), 99th percentile | 152.8 | 142 | −7.1% | −27.0869 to +5.5033 | no |
| time over the response line (% of samples) | 0.01212 | 0.2903 | +2295.2% | +0.1216 to +0.4349 | yes: LOSS |
| failed requests (%) | 0 | 0.07416 | +0.074 (native is 0) | −0.0005 to +0.1488 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.5 | +0.500 (native is 0) | +0.1230 to +0.8770 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 19.2 | 29.4 | +53.1% | +1.3310 to +19.0690 | yes, up (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 90 | 32.86 | −63.5% | −106.5797 to −7.7060 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.21 | 0.1033 | −50.8% | −0.3480 to +0.1347 | no |
| utilisation (used / allocatable) | 0.0352 | 0.0362 | +2.8% | +0.0004 to +0.0016 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8449 | 0.8688 | +2.8% | +0.0103 to +0.0376 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03392 | 0.03522 | +3.8% | +0.0002 to +0.0024 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8788 | 0.9041 | +2.9% | +0.0114 to +0.0391 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 788.7 | 765.6 | −2.9% | −38.9520 to −7.1655 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.427 | 9.297 | +10.3% | +0.5207 to +1.2177 | yes: power given |
| pods started | 5 | 10.7 | +114.0% | +3.5928 to +7.8072 | yes: power given |
| pod start wait, total (s) | 7.3 | 19.1 | +161.6% | +8.9828 to +14.6172 | yes: LOSS |
| pod start wait, mean (s) | 1.433 | 1.869 | +30.4% | +0.1182 to +0.7541 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 26.99 | 27.83 | +3.1% | +0.3509 to +1.3383 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*