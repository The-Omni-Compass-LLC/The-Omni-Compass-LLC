# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.523 | 1.514 | 1.509 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 160 | 158.7 | 160.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 160 | 158.7 | 160.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 147.2 | 151.3 | 145.1 | 151.5 |
| response time (ms), 95th percentile | 296.3 | 299.4 | 286.1 | 295.5 |
| response time (ms), 99th percentile | 421.6 | 418 | 398.9 | 400.1 |
| time over the response line (% of samples) | 0.527 | 0.5038 | 0.2822 | 0.3478 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.1 | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 6.5 | 7.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.35 | 0.1383 | 0.5067 | 0.08167 |
| utilisation (used / allocatable) | 0.03783 | 0.0428 | 0.03915 | 0.04403 |
| CPU used (cores), mean | 0.9079 | 1.027 | 0.9397 | 1.057 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.03227 | 0.051 |
| CPU used with Omni's own (cores), mean | 0.9079 | 1.027 | 0.9719 | 1.108 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 694.9 | 618.9 | 672.9 | 602.9 |
| HPA replicas, mean | 8.939 | 8.955 | 10.52 | 10.72 |
| pods started | 4.8 | 4.4 | 7.7 | 8 |
| pod start wait, total (s) | 7.4 | 7 | 11.2 | 12.6 |
| pod start wait, mean (s) | 1.53 | 1.602 | 1.47 | 1.575 |
| host CPU busy, the real machine under kind (%) | 27.34 | 31.51 | 29.28 | 34.23 |
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
| node-hours | 1.514 | 1.513 | −0.0% | −0.0096 to +0.0086 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160 | 160.2 | +0.1% | −0.7477 to +1.1743 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160 | 160.2 | +0.1% | −0.7477 to +1.1743 | no |
| response time (ms), mean | 151.3 | 151.5 | +0.1% | −4.6449 to +4.9635 | no |
| response time (ms), 95th percentile | 299.4 | 295.5 | −1.3% | −21.9719 to +14.1829 | no |
| response time (ms), 99th percentile | 418 | 400.1 | −4.3% | −40.9986 to +5.1922 | no |
| time over the response line (% of samples) | 0.5038 | 0.3478 | −31.0% | −0.3557 to +0.0438 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 7.2 | +7.200 (native is 0) | +5.0199 to +9.3801 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1383 | 0.08167 | −41.0% | −0.2623 to +0.1490 | no |
| utilisation (used / allocatable) | 0.0428 | 0.04403 | +2.9% | +0.0007 to +0.0018 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.027 | 1.057 | +2.9% | +0.0165 to +0.0427 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.051 | +0.051 (native is 0) | +0.0451 to +0.0569 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.027 | 1.108 | +7.8% | +0.0641 to +0.0971 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 618.9 | 602.9 | −2.6% | −22.3666 to −9.5080 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.955 | 10.72 | +19.7% | +0.9473 to +2.5841 | yes: power given |
| pods started | 4.4 | 8 | +81.8% | +2.0474 to +5.1526 | yes: power given |
| pod start wait, total (s) | 7 | 12.6 | +80.0% | +2.8982 to +8.3018 | yes: LOSS |
| pod start wait, mean (s) | 1.602 | 1.575 | −1.7% | −0.2211 to +0.1677 | no |
| host CPU busy, the real machine under kind (%) | 31.51 | 34.23 | +8.6% | +2.1791 to +3.2439 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.523 | 1.514 | −0.6% | −0.0154 to −0.0030 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 160 | +0.1% | −0.5312 to +0.8143 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 160 | +0.1% | −0.5312 to +0.8143 | no |
| response time (ms), mean | 147.2 | 151.3 | +2.8% | −1.1434 to +9.4442 | no |
| response time (ms), 95th percentile | 296.3 | 299.4 | +1.0% | −18.0697 to +24.2527 | no |
| response time (ms), 99th percentile | 421.6 | 418 | −0.8% | −36.3776 to +29.2422 | no |
| time over the response line (% of samples) | 0.527 | 0.5038 | −4.4% | −0.2615 to +0.2149 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.35 | 0.1383 | −60.5% | −0.5475 to +0.1242 | no |
| utilisation (used / allocatable) | 0.03783 | 0.0428 | +13.1% | +0.0042 to +0.0057 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9079 | 1.027 | +13.1% | +0.1006 to +0.1379 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.9079 | 1.027 | +13.1% | +0.1006 to +0.1379 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 694.9 | 618.9 | −10.9% | −86.1832 to −65.7787 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.939 | 8.955 | +0.2% | −0.1213 to +0.1539 | no |
| pods started | 4.8 | 4.4 | −8.3% | −1.3656 to +0.5656 | no |
| pod start wait, total (s) | 7.4 | 7 | −5.4% | −2.1260 to +1.3260 | no |
| pod start wait, mean (s) | 1.53 | 1.602 | +4.7% | −0.1654 to +0.3087 | no |
| host CPU busy, the real machine under kind (%) | 27.34 | 31.51 | +15.3% | +3.5209 to +4.8226 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.523 | 1.509 | −0.9% | −0.0209 to −0.0064 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 158.7 | −0.7% | −1.8588 to −0.4243 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 158.7 | −0.7% | −1.8588 to −0.4243 | yes: GAIN |
| response time (ms), mean | 147.2 | 145.1 | −1.5% | −6.0103 to +1.7367 | no |
| response time (ms), 95th percentile | 296.3 | 286.1 | −3.4% | −27.9885 to +7.6735 | no |
| response time (ms), 99th percentile | 421.6 | 398.9 | −5.4% | −50.7671 to +5.2689 | no |
| time over the response line (% of samples) | 0.527 | 0.2822 | −46.5% | −0.4767 to −0.0130 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6.5 | +6.500 (native is 0) | +5.4744 to +7.5256 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.35 | 0.5067 | +44.8% | −0.1943 to +0.5076 | no |
| utilisation (used / allocatable) | 0.03783 | 0.03915 | +3.5% | +0.0008 to +0.0018 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9079 | 0.9397 | +3.5% | +0.0196 to +0.0439 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03227 | +0.032 (native is 0) | +0.0290 to +0.0356 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9079 | 0.9719 | +7.0% | +0.0502 to +0.0778 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 694.9 | 672.9 | −3.2% | −30.0496 to −13.9050 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.939 | 10.52 | +17.7% | +0.8314 to +2.3319 | yes: power given |
| pods started | 4.8 | 7.7 | +60.4% | +1.5324 to +4.2676 | yes: power given |
| pod start wait, total (s) | 7.4 | 11.2 | +51.4% | +1.5180 to +6.0820 | yes: LOSS |
| pod start wait, mean (s) | 1.53 | 1.47 | −3.9% | −0.3099 to +0.1903 | no |
| host CPU busy, the real machine under kind (%) | 27.34 | 29.28 | +7.1% | +1.5322 to +2.3382 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.509 | −0.3% | −0.0128 to +0.0038 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160 | 158.7 | −0.8% | −2.1894 to −0.3767 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160 | 158.7 | −0.8% | −2.1894 to −0.3767 | yes: GAIN |
| response time (ms), mean | 151.3 | 145.1 | −4.2% | −10.5953 to −1.9791 | yes: GAIN |
| response time (ms), 95th percentile | 299.4 | 286.1 | −4.4% | −31.9407 to +5.4427 | no |
| response time (ms), 99th percentile | 418 | 398.9 | −4.6% | −49.7086 to +11.3458 | no |
| time over the response line (% of samples) | 0.5038 | 0.2822 | −44.0% | −0.4541 to +0.0109 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6.5 | +6.500 (native is 0) | +5.4744 to +7.5256 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1383 | 0.5067 | +266.3% | +0.0637 to +0.6730 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0428 | 0.03915 | −8.5% | −0.0042 to −0.0031 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.027 | 0.9397 | −8.5% | −0.1002 to −0.0748 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03227 | +0.032 (native is 0) | +0.0290 to +0.0356 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.027 | 0.9719 | −5.4% | −0.0673 to −0.0432 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 618.9 | 672.9 | +8.7% | +47.1599 to +60.8473 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.955 | 10.52 | +17.5% | +0.8589 to +2.2718 | yes: power given |
| pods started | 4.4 | 7.7 | +75.0% | +1.9491 to +4.6509 | yes: power given |
| pod start wait, total (s) | 7 | 11.2 | +60.0% | +1.3229 to +7.0771 | yes: LOSS |
| pod start wait, mean (s) | 1.602 | 1.47 | −8.2% | −0.5376 to +0.2747 | no |
| host CPU busy, the real machine under kind (%) | 31.51 | 29.28 | −7.1% | −2.6169 to −1.8561 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.523 | 1.513 | −0.6% | −0.0166 to −0.0027 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 160.2 | +0.2% | −0.3425 to +1.0522 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 160.2 | +0.2% | −0.3425 to +1.0522 | no |
| response time (ms), mean | 147.2 | 151.5 | +2.9% | +0.0930 to +8.5264 | yes: LOSS |
| response time (ms), 95th percentile | 296.3 | 295.5 | −0.3% | −16.8819 to +15.2759 | no |
| response time (ms), 99th percentile | 421.6 | 400.1 | −5.1% | −47.7035 to +4.7617 | no |
| time over the response line (% of samples) | 0.527 | 0.3478 | −34.0% | −0.4095 to +0.0510 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 | −100.0% | −0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 7.2 | +7.200 (native is 0) | +5.0199 to +9.3801 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.35 | 0.08167 | −76.7% | −0.5449 to +0.0082 | no |
| utilisation (used / allocatable) | 0.03783 | 0.04403 | +16.4% | +0.0054 to +0.0070 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9079 | 1.057 | +16.4% | +0.1295 to +0.1682 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.051 | +0.051 (native is 0) | +0.0451 to +0.0569 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9079 | 1.108 | +22.0% | +0.1756 to +0.2241 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 694.9 | 602.9 | −13.2% | −100.1396 to −83.6968 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.939 | 10.72 | +19.9% | +0.9295 to +2.6345 | yes: power given |
| pods started | 4.8 | 8 | +66.7% | +1.5208 to +4.8792 | yes: power given |
| pod start wait, total (s) | 7.4 | 12.6 | +70.3% | +2.3828 to +8.0172 | yes: LOSS |
| pod start wait, mean (s) | 1.53 | 1.575 | +2.9% | −0.1559 to +0.2459 | no |
| host CPU busy, the real machine under kind (%) | 27.34 | 34.23 | +25.2% | +5.9708 to +7.7958 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*