# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 90 s | omni, a decision every 60 s |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 4.508 | 4.513 | 4.514 | 4.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 508.1 | 508 | 507.4 | 506.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 508.1 | 508 | 507.4 | 506.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 254.2 | 133.4 | 132.9 | 131.5 |
| response time (ms), 95th percentile | 681.8 | 289.8 | 245.5 | 254.1 |
| response time (ms), 99th percentile | 2201 | 977.5 | 1180 | 1055 |
| time over the response line (% of samples) | 13.82 | 8.143 | 6.921 | 7.182 |
| failed requests (%) | 5.899 | 6.017 | 5.203 | 5.318 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.3 | 16.1 | 14.6 | 14.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.4 | 43.1 | 39.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | 100 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4583 | 0.6633 | 0.7517 | 0.54 |
| utilisation (used / allocatable) | 0.08954 | 0.08864 | 0.08761 | 0.08732 |
| CPU used (cores), mean | 2.149 | 2.127 | 2.103 | 2.096 |
| Omni's own CPU (cores), mean | 0 | 0.04032 | 0.00683 | 0.0088 |
| CPU used with Omni's own (cores), mean | 2.149 | 2.168 | 2.109 | 2.104 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 343.5 | 348.6 | 350.7 | 353.4 |
| HPA replicas, mean | 9.509 | 11.57 | 9.818 | 10.68 |
| pods started | 5.5 | 10.2 | 7.5 | 8.3 |
| pod start wait, total (s) | 7.5 | 16.1 | 11.4 | 12.4 |
| pod start wait, mean (s) | 1.366 | 1.582 | 1.536 | 1.452 |
| host CPU busy, the real machine under kind (%) | 60.89 | 61.68 | 59.95 | 59.87 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 4.508 | 4.513 | +0.1% | −0.0029 to +0.0116 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 508.1 | 508 | −0.0% | −0.9892 to +0.7884 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 508.1 | 508 | −0.0% | −0.9892 to +0.7884 | no |
| response time (ms), mean | 254.2 | 133.4 | −47.5% | −161.4820 to −80.2292 | yes: GAIN |
| response time (ms), 95th percentile | 681.8 | 289.8 | −57.5% | −499.2132 to −284.8258 | yes: GAIN |
| response time (ms), 99th percentile | 2201 | 977.5 | −55.6% | −2069.1095 to −377.3177 | yes: GAIN |
| time over the response line (% of samples) | 13.82 | 8.143 | −41.1% | −8.0892 to −3.2718 | yes: GAIN |
| failed requests (%) | 5.899 | 6.017 | +2.0% | −0.1493 to +0.3858 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.3 | 16.1 | −27.8% | −8.9144 to −3.4856 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.4 | +50.400 (native is 0) | +40.2101 to +60.5899 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4583 | 0.6633 | +44.7% | −0.1300 to +0.5400 | no |
| utilisation (used / allocatable) | 0.08954 | 0.08864 | −1.0% | −0.0017 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.149 | 2.127 | −1.0% | −0.0402 to −0.0032 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04032 | +0.040 (native is 0) | +0.0334 to +0.0472 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.149 | 2.168 | +0.9% | −0.0046 to +0.0418 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 343.5 | 348.6 | +1.5% | +0.5986 to +9.5127 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.509 | 11.57 | +21.7% | +0.7826 to +3.3408 | yes: power given |
| pods started | 5.5 | 10.2 | +85.5% | +2.6475 to +6.7525 | yes: power given |
| pod start wait, total (s) | 7.5 | 16.1 | +114.7% | +4.5089 to +12.6911 | yes: LOSS |
| pod start wait, mean (s) | 1.366 | 1.582 | +15.8% | −0.0348 to +0.4673 | no |
| host CPU busy, the real machine under kind (%) | 60.89 | 61.68 | +1.3% | +0.0860 to +1.5011 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 4.508 | 4.514 | +0.1% | −0.0002 to +0.0112 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 508.1 | 507.4 | −0.1% | −1.2874 to −0.1162 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 508.1 | 507.4 | −0.1% | −1.2874 to −0.1162 | yes: GAIN |
| response time (ms), mean | 254.2 | 132.9 | −47.7% | −166.7331 to −75.8909 | yes: GAIN |
| response time (ms), 95th percentile | 681.8 | 245.5 | −64.0% | −569.3475 to −303.2065 | yes: GAIN |
| response time (ms), 99th percentile | 2201 | 1180 | −46.4% | −1982.7230 to −59.1650 | yes: GAIN |
| time over the response line (% of samples) | 13.82 | 6.921 | −49.9% | −9.9118 to −3.8944 | yes: GAIN |
| failed requests (%) | 5.899 | 5.203 | −11.8% | −1.1978 to −0.1924 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.3 | 14.6 | −34.5% | −11.0390 to −4.3610 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.1 | +43.100 (native is 0) | +28.2042 to +57.9958 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4583 | 0.7517 | +64.0% | −0.1542 to +0.7409 | no |
| utilisation (used / allocatable) | 0.08954 | 0.08761 | −2.2% | −0.0024 to −0.0015 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.149 | 2.103 | −2.2% | −0.0581 to −0.0349 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00683 | +0.007 (native is 0) | +0.0058 to +0.0078 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.149 | 2.109 | −1.8% | −0.0507 to −0.0286 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 343.5 | 350.7 | +2.1% | +3.8121 to +10.5186 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.509 | 9.818 | +3.3% | −0.4619 to +1.0809 | no |
| pods started | 5.5 | 7.5 | +36.4% | −1.0348 to +5.0348 | no |
| pod start wait, total (s) | 7.5 | 11.4 | +52.0% | −1.5939 to +9.3939 | no |
| pod start wait, mean (s) | 1.366 | 1.536 | +12.5% | −0.2987 to +0.6391 | no |
| host CPU busy, the real machine under kind (%) | 60.89 | 59.95 | −1.5% | −1.2857 to −0.5841 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 60 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 4.508 | 4.511 | +0.1% | −0.0048 to +0.0101 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 508.1 | 506.9 | −0.2% | −1.8331 to −0.5148 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 508.1 | 506.9 | −0.2% | −1.8331 to −0.5148 | yes: GAIN |
| response time (ms), mean | 254.2 | 131.5 | −48.3% | −165.4046 to −80.0455 | yes: GAIN |
| response time (ms), 95th percentile | 681.8 | 254.1 | −62.7% | −560.2741 to −295.1379 | yes: GAIN |
| response time (ms), 99th percentile | 2201 | 1055 | −52.1% | −2024.5138 to −267.4428 | yes: GAIN |
| time over the response line (% of samples) | 13.82 | 7.182 | −48.0% | −9.5362 to −3.7478 | yes: GAIN |
| failed requests (%) | 5.899 | 5.318 | −9.8% | −1.0166 to −0.1438 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.3 | 14.8 | −33.6% | −10.5018 to −4.4982 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.6 | +39.600 (native is 0) | +28.6517 to +50.5483 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4583 | 0.54 | +17.8% | −0.1047 to +0.2680 | no |
| utilisation (used / allocatable) | 0.08954 | 0.08732 | −2.5% | −0.0028 to −0.0016 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.149 | 2.096 | −2.5% | −0.0679 to −0.0391 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0088 | +0.009 (native is 0) | +0.0074 to +0.0102 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.149 | 2.104 | −2.1% | −0.0591 to −0.0303 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 343.5 | 353.4 | +2.9% | +3.1545 to +16.4661 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.509 | 10.68 | +12.3% | −0.0864 to +2.4194 | no |
| pods started | 5.5 | 8.3 | +50.9% | −0.0172 to +5.6172 | no |
| pod start wait, total (s) | 7.5 | 12.4 | +65.3% | −1.3035 to +11.1035 | no |
| pod start wait, mean (s) | 1.366 | 1.452 | +6.3% | −0.2693 to +0.4412 | no |
| host CPU busy, the real machine under kind (%) | 60.89 | 59.87 | −1.7% | −1.3989 to −0.6343 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 4.513 | 4.514 | +0.0% | −0.0063 to +0.0087 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 508 | 507.4 | −0.1% | −1.4191 to +0.2163 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 508 | 507.4 | −0.1% | −1.4191 to +0.2163 | no |
| response time (ms), mean | 133.4 | 132.9 | −0.3% | −11.2598 to +10.3471 | no |
| response time (ms), 95th percentile | 289.8 | 245.5 | −15.3% | −87.2487 to −1.2663 | yes: GAIN |
| response time (ms), 99th percentile | 977.5 | 1180 | +20.7% | −251.9713 to +656.5105 | no |
| time over the response line (% of samples) | 8.143 | 6.921 | −15.0% | −2.1038 to −0.3414 | yes: GAIN |
| failed requests (%) | 6.017 | 5.203 | −13.5% | −1.4786 to −0.1481 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16.1 | 14.6 | −9.3% | −2.5256 to −0.4744 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 50.4 | 43.1 | −14.5% | −21.4946 to +6.8946 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 100 | ±0.0% | ±nan to ±nan | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6633 | 0.7517 | +13.3% | −0.5934 to +0.7700 | no |
| utilisation (used / allocatable) | 0.08864 | 0.08761 | −1.2% | −0.0019 to −0.0002 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.127 | 2.103 | −1.2% | −0.0450 to −0.0045 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0.04032 | 0.00683 | −83.1% | −0.0395 to −0.0275 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.168 | 2.109 | −2.7% | −0.0837 to −0.0328 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 348.6 | 350.7 | +0.6% | −1.0777 to +5.2971 | no |
| HPA replicas, mean | 11.57 | 9.818 | −15.1% | −2.6806 to −0.8238 | yes: GAIN |
| pods started | 10.2 | 7.5 | −26.5% | −5.1560 to −0.2440 | yes: GAIN |
| pod start wait, total (s) | 16.1 | 11.4 | −29.2% | −9.0972 to −0.3028 | yes: GAIN |
| pod start wait, mean (s) | 1.582 | 1.536 | −2.9% | −0.4452 to +0.3533 | no |
| host CPU busy, the real machine under kind (%) | 61.68 | 59.95 | −2.8% | −2.5911 to −0.8657 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 60 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 4.513 | 4.511 | −0.0% | −0.0078 to +0.0045 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 508 | 506.9 | −0.2% | −1.9722 to −0.1749 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 508 | 506.9 | −0.2% | −1.9722 to −0.1749 | yes: GAIN |
| response time (ms), mean | 133.4 | 131.5 | −1.4% | −13.0174 to +9.2785 | no |
| response time (ms), 95th percentile | 289.8 | 254.1 | −12.3% | −86.4797 to +15.1067 | no |
| response time (ms), 99th percentile | 977.5 | 1055 | +7.9% | −200.7077 to +355.1783 | no |
| time over the response line (% of samples) | 8.143 | 7.182 | −11.8% | −1.7725 to −0.1505 | yes: GAIN |
| failed requests (%) | 6.017 | 5.318 | −11.6% | −1.3272 to −0.0697 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16.1 | 14.8 | −8.1% | −2.0578 to −0.5422 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 50.4 | 39.6 | −21.4% | −20.8359 to −0.7641 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6633 | 0.54 | −18.6% | −0.4572 to +0.2105 | no |
| utilisation (used / allocatable) | 0.08864 | 0.08732 | −1.5% | −0.0022 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.127 | 2.096 | −1.5% | −0.0531 to −0.0104 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0.04032 | 0.0088 | −78.2% | −0.0371 to −0.0260 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.168 | 2.104 | −2.9% | −0.0878 to −0.0387 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 348.6 | 353.4 | +1.4% | −1.6067 to +11.1160 | no |
| HPA replicas, mean | 11.57 | 10.68 | −7.7% | −1.9093 to +0.1189 | no |
| pods started | 10.2 | 8.3 | −18.6% | −3.9077 to +0.1077 | no |
| pod start wait, total (s) | 16.1 | 12.4 | −23.0% | −7.9925 to +0.5925 | no |
| pod start wait, mean (s) | 1.582 | 1.452 | −8.2% | −0.4512 to +0.1906 | no |
| host CPU busy, the real machine under kind (%) | 61.68 | 59.87 | −2.9% | −2.5136 to −1.1067 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*