# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.514 | 1.516 | 1.51 | 1.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 160 | 158.3 | 159.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 160 | 158.3 | 159.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 131.9 | 135.6 | 128.8 | 132.4 |
| response time (ms), 95th percentile | 266.4 | 275.8 | 258.9 | 261.8 |
| response time (ms), 99th percentile | 386.2 | 398.4 | 364.8 | 375.6 |
| time over the response line (% of samples) | 0.3337 | 0.3485 | 0.2307 | 0.2686 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.2 | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 1.4 | 1.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3183 | 0.02667 | 0.16 | 0.4967 |
| utilisation (used / allocatable) | 0.03723 | 0.04182 | 0.03739 | 0.04224 |
| CPU used (cores), mean | 0.8934 | 1.004 | 0.8974 | 1.014 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.00589 | 0.00942 |
| CPU used with Omni's own (cores), mean | 0.8934 | 1.004 | 0.9033 | 1.023 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 705.8 | 632.5 | 704.1 | 628.1 |
| HPA replicas, mean | 8.901 | 8.939 | 9.368 | 9.718 |
| pods started | 4.6 | 4.4 | 6.1 | 7 |
| pod start wait, total (s) | 6.1 | 6.3 | 8.6 | 11.1 |
| pod start wait, mean (s) | 1.292 | 1.44 | 1.41 | 1.542 |
| host CPU busy, the real machine under kind (%) | 26.9 | 30.71 | 27.13 | 31.51 |
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

Omni-Compass stayed native in 5 of 10 repetitions (repetitions 2, 4, 5, 7, 8): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.516 | 1.51 | −0.4% | −0.0134 to +0.0018 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160 | 159.5 | −0.3% | −1.2859 to +0.2532 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160 | 159.5 | −0.3% | −1.2859 to +0.2532 | no |
| response time (ms), mean | 135.6 | 132.4 | −2.4% | −7.3290 to +0.8969 | no |
| response time (ms), 95th percentile | 275.8 | 261.8 | −5.1% | −36.9906 to +8.9626 | no |
| response time (ms), 99th percentile | 398.4 | 375.6 | −5.7% | −52.2168 to +6.5456 | no |
| time over the response line (% of samples) | 0.3485 | 0.2686 | −22.9% | −0.3967 to +0.2369 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 | −100.0% | −0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.3 | +1.300 (native is 0) | +0.2856 to +2.3144 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.4967 | +1762.5% | +0.2203 to +0.7197 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.04182 | 0.04224 | +1.0% | −0.0006 to +0.0014 | no |
| CPU used (cores), mean | 1.004 | 1.014 | +1.0% | −0.0137 to +0.0340 | no |
| Omni's own CPU (cores), mean | 0 | 0.00942 | +0.009 (native is 0) | +0.0076 to +0.0112 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.004 | 1.023 | +2.0% | −0.0057 to +0.0448 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 632.5 | 628.1 | −0.7% | −18.5356 to +9.8735 | no |
| HPA replicas, mean | 8.939 | 9.718 | +8.7% | −0.0663 to +1.6234 | no |
| pods started | 4.4 | 7 | +59.1% | +1.1225 to +4.0775 | yes: power given |
| pod start wait, total (s) | 6.3 | 11.1 | +76.2% | +1.3978 to +8.2022 | yes: LOSS |
| pod start wait, mean (s) | 1.44 | 1.542 | +7.1% | −0.2935 to +0.4972 | no |
| host CPU busy, the real machine under kind (%) | 30.71 | 31.51 | +2.6% | +0.0524 to +1.5462 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.516 | +0.1% | −0.0083 to +0.0120 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 160 | +0.8% | +0.1339 to +2.3492 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 160 | +0.8% | +0.1339 to +2.3492 | yes: power given |
| response time (ms), mean | 131.9 | 135.6 | +2.9% | −0.4703 to +7.9880 | no |
| response time (ms), 95th percentile | 266.4 | 275.8 | +3.5% | −3.6285 to +22.3285 | no |
| response time (ms), 99th percentile | 386.2 | 398.4 | +3.2% | −12.4035 to +36.8553 | no |
| time over the response line (% of samples) | 0.3337 | 0.3485 | +4.5% | −0.1624 to +0.1921 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.2 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3183 | 0.02667 | −91.6% | −0.5532 to −0.0302 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03723 | 0.04182 | +12.3% | +0.0040 to +0.0052 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8934 | 1.004 | +12.3% | +0.0958 to +0.1247 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.8934 | 1.004 | +12.3% | +0.0958 to +0.1247 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 705.8 | 632.5 | −10.4% | −83.2583 to −63.4754 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.901 | 8.939 | +0.4% | −0.1221 to +0.1994 | no |
| pods started | 4.6 | 4.4 | −4.3% | −1.1417 to +0.7417 | no |
| pod start wait, total (s) | 6.1 | 6.3 | +3.3% | −2.1796 to +2.5796 | no |
| pod start wait, mean (s) | 1.292 | 1.44 | +11.5% | −0.2225 to +0.5191 | no |
| host CPU busy, the real machine under kind (%) | 26.9 | 30.71 | +14.2% | +3.2638 to +4.3558 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.51 | −0.3% | −0.0112 to +0.0019 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 158.3 | −0.3% | −1.1336 to +0.2649 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 158.3 | −0.3% | −1.1336 to +0.2649 | no |
| response time (ms), mean | 131.9 | 128.8 | −2.3% | −5.6881 to −0.4387 | yes: GAIN |
| response time (ms), 95th percentile | 266.4 | 258.9 | −2.8% | −19.3732 to +4.3262 | no |
| response time (ms), 99th percentile | 386.2 | 364.8 | −5.5% | −56.2738 to +13.4362 | no |
| time over the response line (% of samples) | 0.3337 | 0.2307 | −30.9% | −0.3792 to +0.1732 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.4 | +1.400 (native is 0) | −0.2242 to +3.0242 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3183 | 0.16 | −49.7% | −0.3992 to +0.0826 | no |
| utilisation (used / allocatable) | 0.03723 | 0.03739 | +0.4% | −0.0004 to +0.0007 | no |
| CPU used (cores), mean | 0.8934 | 0.8974 | +0.4% | −0.0088 to +0.0166 | no |
| Omni's own CPU (cores), mean | 0 | 0.00589 | +0.006 (native is 0) | +0.0050 to +0.0068 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8934 | 0.9033 | +1.1% | −0.0034 to +0.0231 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 705.8 | 704.1 | −0.3% | −12.5198 to +8.9531 | no |
| HPA replicas, mean | 8.901 | 9.368 | +5.3% | +0.0311 to +0.9046 | yes: power given |
| pods started | 4.6 | 6.1 | +32.6% | −0.0174 to +3.0174 | no |
| pod start wait, total (s) | 6.1 | 8.6 | +41.0% | −0.3061 to +5.3061 | no |
| pod start wait, mean (s) | 1.292 | 1.41 | +9.1% | −0.1542 to +0.3901 | no |
| host CPU busy, the real machine under kind (%) | 26.9 | 27.13 | +0.9% | −0.2504 to +0.7102 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.516 | 1.51 | −0.4% | −0.0157 to +0.0027 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160 | 158.3 | −1.0% | −2.6339 to −0.7179 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160 | 158.3 | −1.0% | −2.6339 to −0.7179 | yes: GAIN |
| response time (ms), mean | 135.6 | 128.8 | −5.0% | −10.8349 to −2.8096 | yes: GAIN |
| response time (ms), 95th percentile | 275.8 | 258.9 | −6.1% | −32.4887 to −1.2583 | yes: GAIN |
| response time (ms), 99th percentile | 398.4 | 364.8 | −8.4% | −64.8545 to −2.4349 | yes: GAIN |
| time over the response line (% of samples) | 0.3485 | 0.2307 | −33.8% | −0.4602 to +0.2245 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.4 | +1.400 (native is 0) | −0.2242 to +3.0242 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.16 | +500.0% | −0.0520 to +0.3187 | no |
| utilisation (used / allocatable) | 0.04182 | 0.03739 | −10.6% | −0.0050 to −0.0039 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.004 | 0.8974 | −10.6% | −0.1202 to −0.0925 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00589 | +0.006 (native is 0) | +0.0050 to +0.0068 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.004 | 0.9033 | −10.0% | −0.1146 to −0.0863 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 632.5 | 704.1 | +11.3% | +58.4348 to +84.7322 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.939 | 9.368 | +4.8% | −0.0763 to +0.9348 | no |
| pods started | 4.4 | 6.1 | +38.6% | +0.5791 to +2.8209 | yes: power given |
| pod start wait, total (s) | 6.3 | 8.6 | +36.5% | −0.4196 to +5.0196 | no |
| pod start wait, mean (s) | 1.44 | 1.41 | −2.1% | −0.5056 to +0.4449 | no |
| host CPU busy, the real machine under kind (%) | 30.71 | 27.13 | −11.7% | −3.9976 to −3.1621 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.51 | −0.3% | −0.0100 to +0.0020 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 159.5 | +0.5% | −0.0179 to +1.4682 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 159.5 | +0.5% | −0.0179 to +1.4682 | no |
| response time (ms), mean | 131.9 | 132.4 | +0.4% | −1.5536 to +2.6392 | no |
| response time (ms), 95th percentile | 266.4 | 261.8 | −1.8% | −21.2656 to +11.9376 | no |
| response time (ms), 99th percentile | 386.2 | 375.6 | −2.7% | −38.1122 to +16.8928 | no |
| time over the response line (% of samples) | 0.3337 | 0.2686 | −19.5% | −0.2815 to +0.1514 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 | −100.0% | −0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.3 | +1.300 (native is 0) | +0.2856 to +2.3144 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3183 | 0.4967 | +56.0% | −0.0618 to +0.4185 | no |
| utilisation (used / allocatable) | 0.03723 | 0.04224 | +13.5% | +0.0040 to +0.0060 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8934 | 1.014 | +13.5% | +0.0967 to +0.1442 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00942 | +0.009 (native is 0) | +0.0076 to +0.0112 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8934 | 1.023 | +14.5% | +0.1045 to +0.1552 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 705.8 | 628.1 | −11.0% | −88.2627 to −67.1331 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.901 | 9.718 | +9.2% | +0.0679 to +1.5665 | yes: power given |
| pods started | 4.6 | 7 | +52.2% | +0.4280 to +4.3720 | yes: power given |
| pod start wait, total (s) | 6.1 | 11.1 | +82.0% | +0.9256 to +9.0744 | yes: LOSS |
| pod start wait, mean (s) | 1.292 | 1.542 | +19.4% | −0.0245 to +0.5249 | no |
| host CPU busy, the real machine under kind (%) | 26.9 | 31.51 | +17.1% | +3.6152 to +5.6030 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*