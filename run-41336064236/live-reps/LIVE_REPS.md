# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.517 | 1.514 | 1.513 | 1.509 |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 159.6 | 158.6 | 159.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 159.6 | 158.6 | 159.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 123.1 | 127.7 | 122.2 | 128.6 |
| response time (ms), 95th percentile | 251 | 261.7 | 242 | 265.5 |
| response time (ms), 99th percentile | 356.6 | 366.4 | 344 | 380.7 |
| time over the response line (% of samples) | 0.3198 | 0.2695 | 0.1905 | 0.4664 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | 0 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 1.4 | 1.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.345 | 0.1067 | 0.1067 | 0.2733 |
| utilisation (used / allocatable) | 0.03673 | 0.04113 | 0.03708 | 0.0418 |
| CPU used (cores), mean | 0.8815 | 0.987 | 0.89 | 1.003 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.00583 | 0.00934 |
| CPU used with Omni's own (cores), mean | 0.8815 | 0.987 | 0.8958 | 1.013 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 714.9 | 644.2 | 709.5 | 633.9 |
| HPA replicas, mean | 8.877 | 8.887 | 9.796 | 9.592 |
| pods started | 4.7 | 4.5 | 6 | 6.3 |
| pod start wait, total (s) | 7.1 | 7.1 | 9.6 | 9.8 |
| pod start wait, mean (s) | 1.515 | 1.575 | 1.641 | 1.566 |
| host CPU busy, the real machine under kind (%) | 26.29 | 30.06 | 27.02 | 31.11 |
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

Omni-Compass stayed native in 5 of 10 repetitions (repetitions 2, 5, 7, 8, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.509 | −0.3% | −0.0116 to +0.0020 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.6 | 159.2 | −0.2% | −1.0951 to +0.3912 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.6 | 159.2 | −0.2% | −1.0951 to +0.3912 | no |
| response time (ms), mean | 127.7 | 128.6 | +0.8% | −4.9391 to +6.8971 | no |
| response time (ms), 95th percentile | 261.7 | 265.5 | +1.4% | −23.6012 to +31.0632 | no |
| response time (ms), 99th percentile | 366.4 | 380.7 | +3.9% | −35.5248 to +64.1626 | no |
| time over the response line (% of samples) | 0.2695 | 0.4664 | +73.0% | −0.3994 to +0.7931 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.5 | +1.500 (native is 0) | +0.2271 to +2.7729 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.2733 | +156.2% | −0.1408 to +0.4741 | no |
| utilisation (used / allocatable) | 0.04113 | 0.0418 | +1.6% | +0.0002 to +0.0011 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.987 | 1.003 | +1.6% | +0.0054 to +0.0271 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00934 | +0.009 (native is 0) | +0.0073 to +0.0113 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.987 | 1.013 | +2.6% | +0.0147 to +0.0365 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 644.2 | 633.9 | −1.6% | −18.4350 to −2.1892 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.887 | 9.592 | +7.9% | +0.1371 to +1.2720 | yes: power given |
| pods started | 4.5 | 6.3 | +40.0% | +0.5028 to +3.0972 | yes: power given |
| pod start wait, total (s) | 7.1 | 9.8 | +38.0% | +0.5660 to +4.8340 | yes: LOSS |
| pod start wait, mean (s) | 1.575 | 1.566 | −0.6% | −0.2983 to +0.2804 | no |
| host CPU busy, the real machine under kind (%) | 30.06 | 31.11 | +3.5% | +0.5209 to +1.5632 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.517 | 1.514 | −0.2% | −0.0136 to +0.0066 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 159.6 | +0.4% | −0.5885 to +1.7848 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 159.6 | +0.4% | −0.5885 to +1.7848 | no |
| response time (ms), mean | 123.1 | 127.7 | +3.7% | +2.5539 to +6.6497 | yes: LOSS |
| response time (ms), 95th percentile | 251 | 261.7 | +4.3% | +0.3648 to +21.0642 | yes: LOSS |
| response time (ms), 99th percentile | 356.6 | 366.4 | +2.7% | −20.6435 to +40.1847 | no |
| time over the response line (% of samples) | 0.3198 | 0.2695 | −15.7% | −0.2178 to +0.1172 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.345 | 0.1067 | −69.1% | −0.4655 to −0.0112 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03673 | 0.04113 | +12.0% | +0.0033 to +0.0055 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8815 | 0.987 | +12.0% | +0.0780 to +0.1329 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.8815 | 0.987 | +12.0% | +0.0780 to +0.1329 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 714.9 | 644.2 | −9.9% | −85.6631 to −55.5879 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.877 | 8.887 | +0.1% | −0.1243 to +0.1445 | no |
| pods started | 4.7 | 4.5 | −4.3% | −0.5016 to +0.1016 | no |
| pod start wait, total (s) | 7.1 | 7.1 | ±0.0% | −1.9949 to +1.9949 | no |
| pod start wait, mean (s) | 1.515 | 1.575 | +4.0% | −0.4004 to +0.5204 | no |
| host CPU busy, the real machine under kind (%) | 26.29 | 30.06 | +14.4% | +2.9698 to +4.5797 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.517 | 1.513 | −0.3% | −0.0119 to +0.0042 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.6 | −0.2% | −1.2323 to +0.5119 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.6 | −0.2% | −1.2323 to +0.5119 | no |
| response time (ms), mean | 123.1 | 122.2 | −0.7% | −3.7126 to +1.9878 | no |
| response time (ms), 95th percentile | 251 | 242 | −3.6% | −24.8529 to +6.8019 | no |
| response time (ms), 99th percentile | 356.6 | 344 | −3.5% | −44.9214 to +19.7692 | no |
| time over the response line (% of samples) | 0.3198 | 0.1905 | −40.4% | −0.3614 to +0.1028 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.4 | +1.400 (native is 0) | +0.4952 to +2.3048 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.345 | 0.1067 | −69.1% | −0.5657 to +0.0891 | no |
| utilisation (used / allocatable) | 0.03673 | 0.03708 | +1.0% | −0.0002 to +0.0009 | no |
| CPU used (cores), mean | 0.8815 | 0.89 | +1.0% | −0.0052 to +0.0221 | no |
| Omni's own CPU (cores), mean | 0 | 0.00583 | +0.006 (native is 0) | +0.0049 to +0.0067 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8815 | 0.8958 | +1.6% | −0.0002 to +0.0288 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 714.9 | 709.5 | −0.8% | −15.4209 to +4.6121 | no |
| HPA replicas, mean | 8.877 | 9.796 | +10.4% | +0.2939 to +1.5446 | yes: power given |
| pods started | 4.7 | 6 | +27.7% | −0.4538 to +3.0538 | no |
| pod start wait, total (s) | 7.1 | 9.6 | +35.2% | −0.2446 to +5.2446 | no |
| pod start wait, mean (s) | 1.515 | 1.641 | +8.3% | −0.2613 to +0.5143 | no |
| host CPU busy, the real machine under kind (%) | 26.29 | 27.02 | +2.8% | +0.2779 to +1.1855 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.513 | −0.0% | −0.0096 to +0.0089 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.6 | 158.6 | −0.6% | −1.9179 to +0.0011 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.6 | 158.6 | −0.6% | −1.9179 to +0.0011 | no |
| response time (ms), mean | 127.7 | 122.2 | −4.3% | −8.7042 to −2.2241 | yes: GAIN |
| response time (ms), 95th percentile | 261.7 | 242 | −7.5% | −30.8374 to −8.6426 | yes: GAIN |
| response time (ms), 99th percentile | 366.4 | 344 | −6.1% | −46.8464 to +2.1530 | no |
| time over the response line (% of samples) | 0.2695 | 0.1905 | −29.3% | −0.2304 to +0.0723 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.4 | +1.400 (native is 0) | +0.4952 to +2.3048 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.1067 | 0.0% | raw −0.2379 to +0.2379 | STEADY, the same (to nine decimal places) |
| utilisation (used / allocatable) | 0.04113 | 0.03708 | −9.8% | −0.0048 to −0.0033 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.987 | 0.89 | −9.8% | −0.1144 to −0.0796 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00583 | +0.006 (native is 0) | +0.0049 to +0.0067 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.987 | 0.8958 | −9.2% | −0.1081 to −0.0743 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 644.2 | 709.5 | +10.1% | +54.5311 to +75.9111 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.887 | 9.796 | +10.2% | +0.3132 to +1.5050 | yes: power given |
| pods started | 4.5 | 6 | +33.3% | −0.2922 to +3.2922 | no |
| pod start wait, total (s) | 7.1 | 9.6 | +35.2% | +0.1577 to +4.8423 | yes: LOSS |
| pod start wait, mean (s) | 1.575 | 1.641 | +4.2% | −0.2645 to +0.3974 | no |
| host CPU busy, the real machine under kind (%) | 30.06 | 27.02 | −10.1% | −3.5534 to −2.5327 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.517 | 1.509 | −0.5% | −0.0182 to +0.0015 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 159.2 | +0.2% | −0.7851 to +1.2776 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 159.2 | +0.2% | −0.7851 to +1.2776 | no |
| response time (ms), mean | 123.1 | 128.6 | +4.5% | +0.4630 to +10.6986 | yes: LOSS |
| response time (ms), 95th percentile | 251 | 265.5 | +5.8% | −11.5559 to +40.4469 | no |
| response time (ms), 99th percentile | 356.6 | 380.7 | +6.8% | −30.8202 to +78.9992 | no |
| time over the response line (% of samples) | 0.3198 | 0.4664 | +45.8% | −0.3666 to +0.6597 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.3 | +200.0% | −0.5388 to +0.9388 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1.5 | +1.500 (native is 0) | +0.2271 to +2.7729 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.345 | 0.2733 | −20.8% | −0.4010 to +0.2576 | no |
| utilisation (used / allocatable) | 0.03673 | 0.0418 | +13.8% | +0.0041 to +0.0061 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8815 | 1.003 | +13.8% | +0.0973 to +0.1461 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00934 | +0.009 (native is 0) | +0.0073 to +0.0113 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8815 | 1.013 | +14.9% | +0.1048 to +0.1573 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 714.9 | 633.9 | −11.3% | −92.2980 to −69.5772 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.877 | 9.592 | +8.1% | +0.0924 to +1.3369 | yes: power given |
| pods started | 4.7 | 6.3 | +34.0% | +0.4222 to +2.7778 | yes: power given |
| pod start wait, total (s) | 7.1 | 9.8 | +38.0% | +0.7910 to +4.6090 | yes: LOSS |
| pod start wait, mean (s) | 1.515 | 1.566 | +3.4% | −0.2390 to +0.3412 | no |
| host CPU busy, the real machine under kind (%) | 26.29 | 31.11 | +18.3% | +3.9008 to +5.7328 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*