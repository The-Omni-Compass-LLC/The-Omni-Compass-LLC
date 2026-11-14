# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 60 s |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.514 | 1.515 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 171.6 | 171.4 | 171.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.6 | 171.4 | 171.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 484.7 | 438.2 | 399.3 |
| response time (ms), 95th percentile | 1979 | 1879 | 1753 |
| response time (ms), 99th percentile | 4818 | 4590 | 4421 |
| time over the response line (% of samples) | 21.87 | 21.64 | 20.34 |
| failed requests (%) | 1.945 | 1.652 | 2.342 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 7.7 | 7.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 136.4 | 49.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 80 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.505 | 1.488 | 1.212 |
| utilisation (used / allocatable) | 0.09398 | 0.09279 | 0.09326 |
| CPU used (cores), mean | 2.256 | 2.227 | 2.238 |
| Omni's own CPU (cores), mean | 0 | 0.05368 | 0.01309 |
| CPU used with Omni's own (cores), mean | 2.256 | 2.281 | 2.251 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 311.5 | 313.4 | 313.4 |
| HPA replicas, mean | 14.99 | 15.62 | 15.13 |
| pods started | 5.5 | 6 | 4.7 |
| pod start wait, total (s) | 9.8 | 11.2 | 7.9 |
| pod start wait, mean (s) | 1.791 | 1.871 | 1.52 |
| host CPU busy, the real machine under kind (%) | 64.9 | 66.21 | 64.75 |
| host cores (the real machine under kind) | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan |
| second app: response time (ms), 95th percentile | 253.2 | 270.5 | 300.5 |
| second app: response time (ms), 99th percentile | 2245 | 2322 | 2422 |
| second app: time over the response line (% of samples) | 13.03 | 13.25 | 13.39 |
| second app: failed requests (%) | 11.17 | 11.32 | 11.17 |

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
| node-hours | 1.514 | 1.515 | +0.1% | −0.0030 to +0.0050 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 171.6 | 171.4 | −0.1% | −0.7880 to +0.4570 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.6 | 171.4 | −0.1% | −0.7880 to +0.4570 | no |
| response time (ms), mean | 484.7 | 438.2 | −9.6% | −76.2437 to −16.7519 | yes: GAIN |
| response time (ms), 95th percentile | 1979 | 1879 | −5.1% | −287.5142 to +87.4352 | no |
| response time (ms), 99th percentile | 4818 | 4590 | −4.7% | −860.8521 to +405.0495 | no |
| time over the response line (% of samples) | 21.87 | 21.64 | −1.1% | −2.1002 to +1.6222 | no |
| failed requests (%) | 1.945 | 1.652 | −15.0% | −1.0033 to +0.4180 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 7.7 | −1.3% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 136.4 | +136.400 (native is 0) | +113.4551 to +159.3449 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.505 | 1.488 | −1.1% | −0.9260 to +0.8927 | no |
| utilisation (used / allocatable) | 0.09398 | 0.09279 | −1.3% | −0.0026 to +0.0002 | no |
| CPU used (cores), mean | 2.256 | 2.227 | −1.3% | −0.0632 to +0.0059 | no |
| Omni's own CPU (cores), mean | 0 | 0.05368 | +0.054 (native is 0) | +0.0459 to +0.0615 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.256 | 2.281 | +1.1% | −0.0067 to +0.0567 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 311.5 | 313.4 | +0.6% | −3.2308 to +7.0401 | no |
| HPA replicas, mean | 14.99 | 15.62 | +4.2% | −0.0670 to +1.3175 | no |
| pods started | 5.5 | 6 | +9.1% | −0.5256 to +1.5256 | no |
| pod start wait, total (s) | 9.8 | 11.2 | +14.3% | −2.2815 to +5.0815 | no |
| pod start wait, mean (s) | 1.791 | 1.871 | +4.5% | −0.3235 to +0.4844 | no |
| host CPU busy, the real machine under kind (%) | 64.9 | 66.21 | +2.0% | +0.6946 to +1.9349 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 253.2 | 270.5 | +6.8% | −28.0955 to +62.7135 | no |
| second app: response time (ms), 99th percentile | 2245 | 2322 | +3.4% | −1010.6474 to +1164.5024 | no |
| second app: time over the response line (% of samples) | 13.03 | 13.25 | +1.6% | −0.5062 to +0.9336 | no |
| second app: failed requests (%) | 11.17 | 11.32 | +1.4% | −0.3164 to +0.6181 | no |

## omni deciding every 60 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.516 | +0.2% | −0.0004 to +0.0054 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 171.6 | 171.8 | +0.1% | −0.2879 to +0.6767 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.6 | 171.8 | +0.1% | −0.2879 to +0.6767 | no |
| response time (ms), mean | 484.7 | 399.3 | −17.6% | −135.5684 to −35.3003 | yes: GAIN |
| response time (ms), 95th percentile | 1979 | 1753 | −11.4% | −472.7420 to +21.5080 | no |
| response time (ms), 99th percentile | 4818 | 4421 | −8.2% | −1268.6725 to +475.1149 | no |
| time over the response line (% of samples) | 21.87 | 20.34 | −7.0% | −3.5400 to +0.4698 | no |
| failed requests (%) | 1.945 | 2.342 | +20.4% | −0.0825 to +0.8772 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 7.9 | +1.3% | −0.5263 to +0.7263 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.2 | +49.200 (native is 0) | +36.1499 to +62.2501 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.505 | 1.212 | −19.5% | −0.8092 to +0.2225 | no |
| utilisation (used / allocatable) | 0.09398 | 0.09326 | −0.8% | −0.0022 to +0.0008 | no |
| CPU used (cores), mean | 2.256 | 2.238 | −0.8% | −0.0535 to +0.0189 | no |
| Omni's own CPU (cores), mean | 0 | 0.01309 | +0.013 (native is 0) | +0.0118 to +0.0144 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.256 | 2.251 | −0.2% | −0.0406 to +0.0321 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 311.5 | 313.4 | +0.6% | −2.5721 to +6.5017 | no |
| HPA replicas, mean | 14.99 | 15.13 | +0.9% | −0.2281 to +0.5042 | no |
| pods started | 5.5 | 4.7 | −14.5% | −2.1403 to +0.5403 | no |
| pod start wait, total (s) | 9.8 | 7.9 | −19.4% | −5.7217 to +1.9217 | no |
| pod start wait, mean (s) | 1.791 | 1.52 | −15.1% | −0.9178 to +0.3763 | no |
| host CPU busy, the real machine under kind (%) | 64.9 | 64.75 | −0.2% | −0.7825 to +0.4812 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 253.2 | 300.5 | +18.7% | −53.8521 to +148.5171 | no |
| second app: response time (ms), 99th percentile | 2245 | 2422 | +7.9% | −1469.1971 to +1823.3213 | no |
| second app: time over the response line (% of samples) | 13.03 | 13.39 | +2.7% | −0.7426 to +1.4562 | no |
| second app: failed requests (%) | 11.17 | 11.17 | +0.0% | −0.6044 to +0.6077 | no |

## omni deciding every 60 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.515 | 1.516 | +0.1% | −0.0037 to +0.0067 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 171.4 | 171.8 | +0.2% | −0.4119 to +1.1317 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.4 | 171.8 | +0.2% | −0.4119 to +1.1317 | no |
| response time (ms), mean | 438.2 | 399.3 | −8.9% | −80.2401 to +2.3670 | no |
| response time (ms), 95th percentile | 1879 | 1753 | −6.7% | −480.2592 to +229.1042 | no |
| response time (ms), 99th percentile | 4590 | 4421 | −3.7% | −874.4095 to +536.6545 | no |
| time over the response line (% of samples) | 21.64 | 20.34 | −6.0% | −3.0512 to +0.4589 | no |
| failed requests (%) | 1.652 | 2.342 | +41.8% | −0.2285 to +1.6085 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 7.9 | +2.6% | −0.3642 to +0.7642 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 136.4 | 49.2 | −63.9% | −110.6342 to −63.7658 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.488 | 1.212 | −18.6% | −0.8574 to +0.3041 | no |
| utilisation (used / allocatable) | 0.09279 | 0.09326 | +0.5% | −0.0008 to +0.0017 | no |
| CPU used (cores), mean | 2.227 | 2.238 | +0.5% | −0.0192 to +0.0419 | no |
| Omni's own CPU (cores), mean | 0.05368 | 0.01309 | −75.6% | −0.0476 to −0.0336 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.281 | 2.251 | −1.3% | −0.0558 to −0.0027 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 313.4 | 313.4 | +0.0% | −5.5680 to +5.6883 | no |
| HPA replicas, mean | 15.62 | 15.13 | −3.1% | −1.0218 to +0.0475 | no |
| pods started | 6 | 4.7 | −21.7% | −2.7717 to +0.1717 | no |
| pod start wait, total (s) | 11.2 | 7.9 | −29.5% | −8.1403 to +1.5403 | no |
| pod start wait, mean (s) | 1.871 | 1.52 | −18.8% | −1.0680 to +0.3656 | no |
| host CPU busy, the real machine under kind (%) | 66.21 | 64.75 | −2.2% | −1.8718 to −1.0590 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 270.5 | 300.5 | +11.1% | −29.7188 to +89.7658 | no |
| second app: response time (ms), 99th percentile | 2322 | 2422 | +4.3% | −1087.9744 to +1288.2436 | no |
| second app: time over the response line (% of samples) | 13.25 | 13.39 | +1.1% | −0.5736 to +0.8599 | no |
| second app: failed requests (%) | 11.32 | 11.17 | −1.3% | −0.5881 to +0.2897 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*