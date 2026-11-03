# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.511 | 1.511 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159 | 159.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159 | 159.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 166.7 | 85.3 | 90.12 |
| response time (ms), 95th percentile | 377.8 | 124.6 | 124.9 |
| response time (ms), 99th percentile | 606.6 | 177.8 | 167.1 |
| time over the response line (% of samples) | 2.732 | 0.0122 | 0.2806 |
| failed requests (%) | 0 | 0 | 0.112 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 0 | 0.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.6 | 26.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 | 42.86 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4017 | 0.185 | 0 |
| utilisation (used / allocatable) | 0.04109 | 0.03955 | 0.04018 |
| CPU used (cores), mean | 0.9863 | 0.9491 | 0.9644 |
| Omni's own CPU (cores), mean | 0 | 0.03855 | 0.03885 |
| CPU used with Omni's own (cores), mean | 0.9863 | 0.9877 | 1.003 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 682.4 | 700 | 693.3 |
| HPA replicas, mean | 8.693 | 9.056 | 9.466 |
| pods started | 4.8 | 4.2 | 9.9 |
| pod start wait, total (s) | 7.4 | 6.7 | 16.8 |
| pod start wait, mean (s) | 1.393 | 1.553 | 1.721 |
| host CPU busy, the real machine under kind (%) | 30.04 | 30.26 | 30.98 |
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
| node-hours | 1.511 | 1.511 | +0.0% | −0.0013 to +0.0023 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159 | −0.2% | −0.7203 to +0.0764 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159 | −0.2% | −0.7203 to +0.0764 | no |
| response time (ms), mean | 166.7 | 85.3 | −48.8% | −103.6720 to −59.1143 | yes: GAIN |
| response time (ms), 95th percentile | 377.8 | 124.6 | −67.0% | −320.8351 to −185.5389 | yes: GAIN |
| response time (ms), 99th percentile | 606.6 | 177.8 | −70.7% | −535.4873 to −322.0759 | yes: GAIN |
| time over the response line (% of samples) | 2.732 | 0.0122 | −99.6% | −4.1848 to −1.2548 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 0 | −100.0% | −4.1717 to −1.2283 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.6 | +19.600 (native is 0) | +17.3837 to +21.8163 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4017 | 0.185 | −53.9% | −0.5533 to +0.1200 | no |
| utilisation (used / allocatable) | 0.04109 | 0.03955 | −3.8% | −0.0028 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9863 | 0.9491 | −3.8% | −0.0670 to −0.0073 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03855 | +0.039 (native is 0) | +0.0339 to +0.0432 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9863 | 0.9877 | +0.1% | −0.0257 to +0.0285 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 682.4 | 700 | +2.6% | +1.2016 to +34.1019 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.693 | 9.056 | +4.2% | −0.0269 to +0.7525 | no |
| pods started | 4.8 | 4.2 | −12.5% | −1.9572 to +0.7572 | no |
| pod start wait, total (s) | 7.4 | 6.7 | −9.5% | −3.2912 to +1.8912 | no |
| pod start wait, mean (s) | 1.393 | 1.553 | +11.4% | −0.1791 to +0.4976 | no |
| host CPU busy, the real machine under kind (%) | 30.04 | 30.26 | +0.7% | −0.2981 to +0.7307 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.511 | 1.515 | +0.3% | −0.0018 to +0.0098 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.5 | +0.1% | −0.4435 to +0.8203 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.5 | +0.1% | −0.4435 to +0.8203 | no |
| response time (ms), mean | 166.7 | 90.12 | −45.9% | −97.8738 to −55.2727 | yes: GAIN |
| response time (ms), 95th percentile | 377.8 | 124.9 | −66.9% | −320.7744 to −185.0096 | yes: GAIN |
| response time (ms), 99th percentile | 606.6 | 167.1 | −72.5% | −557.5924 to −321.4734 | yes: GAIN |
| time over the response line (% of samples) | 2.732 | 0.2806 | −89.7% | −3.9294 to −0.9735 | yes: GAIN |
| failed requests (%) | 0 | 0.112 | +0.112 (native is 0) | +0.0339 to +0.1901 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 0.4 | −85.2% | −4.0210 to −0.5790 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.3 | +26.300 (native is 0) | +21.3322 to +31.2678 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4017 | 0 | −100.0% | −0.6918 to −0.1116 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.04109 | 0.04018 | −2.2% | −0.0017 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9863 | 0.9644 | −2.2% | −0.0404 to −0.0034 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03885 | +0.039 (native is 0) | +0.0345 to +0.0432 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9863 | 1.003 | +1.7% | +0.0003 to +0.0336 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 682.4 | 693.3 | +1.6% | +0.7871 to +21.1222 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.693 | 9.466 | +8.9% | +0.5222 to +1.0247 | yes: power given |
| pods started | 4.8 | 9.9 | +106.2% | +3.8633 to +6.3367 | yes: power given |
| pod start wait, total (s) | 7.4 | 16.8 | +127.0% | +6.0756 to +12.7244 | yes: LOSS |
| pod start wait, mean (s) | 1.393 | 1.721 | +23.5% | −0.1519 to +0.8075 | no |
| host CPU busy, the real machine under kind (%) | 30.04 | 30.98 | +3.1% | +0.5093 to +1.3558 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.511 | 1.515 | +0.2% | −0.0030 to +0.0100 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 159.5 | +0.3% | −0.2567 to +1.2774 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 159.5 | +0.3% | −0.2567 to +1.2774 | no |
| response time (ms), mean | 85.3 | 90.12 | +5.7% | +1.7341 to +7.9056 | yes: LOSS |
| response time (ms), 95th percentile | 124.6 | 124.9 | +0.2% | −1.7197 to +2.3097 | no |
| response time (ms), 99th percentile | 177.8 | 167.1 | −6.0% | −31.2018 to +9.6992 | no |
| time over the response line (% of samples) | 0.0122 | 0.2806 | +2200.8% | +0.2152 to +0.3215 | yes: LOSS |
| failed requests (%) | 0 | 0.112 | +0.112 (native is 0) | +0.0339 to +0.1901 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 19.6 | 26.3 | +34.2% | +0.4182 to +12.9818 | yes, up (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 90 | 32.86 | −63.5% | −106.5797 to −7.7060 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.185 | 0 | −100.0% | −0.3132 to −0.0568 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03955 | 0.04018 | +1.6% | −0.0000 to +0.0013 | no |
| CPU used (cores), mean | 0.9491 | 0.9644 | +1.6% | −0.0005 to +0.0309 | no |
| Omni's own CPU (cores), mean | 0.03855 | 0.03885 | +0.8% | −0.0004 to +0.0010 | no |
| CPU used with Omni's own (cores), mean | 0.9877 | 1.003 | +1.6% | −0.0001 to +0.0312 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 700 | 693.3 | −1.0% | −16.6754 to +3.2812 | no |
| HPA replicas, mean | 9.056 | 9.466 | +4.5% | −0.1711 to +0.9925 | no |
| pods started | 4.2 | 9.9 | +135.7% | +4.5791 to +6.8209 | yes: power given |
| pod start wait, total (s) | 6.7 | 16.8 | +150.7% | +5.4957 to +14.7043 | yes: LOSS |
| pod start wait, mean (s) | 1.553 | 1.721 | +10.9% | −0.1900 to +0.5269 | no |
| host CPU busy, the real machine under kind (%) | 30.26 | 30.98 | +2.4% | +0.2552 to +1.1773 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*