# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.213 | 5.14 |
| node-hours | 2.515 | 2.511 | 2.183 | 2.154 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.8 | 274.1 | 274.5 | 274.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.8 | 274.1 | 249.8 | 247.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 486.6 | 465.8 | 502.9 | 510.4 |
| response time (ms), 95th percentile | 1866 | 1809 | 1954 | 2070 |
| response time (ms), 99th percentile | 2640 | 2656 | 2750 | 2956 |
| time over the response line (% of samples) | 21.68 | 19.99 | 21.92 | 20.51 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.5 | 11.6 | 12.9 | 12.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 36.2 | 30.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 25 | 60 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.45 | 22.57 | 21.38 | 28.19 |
| utilisation (used / allocatable) | 0.06732 | 0.06656 | 0.07676 | 0.07718 |
| CPU used (cores), mean | 1.616 | 1.598 | 1.592 | 1.586 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06426 | 0.06949 |
| CPU used with Omni's own (cores), mean | 1.616 | 1.598 | 1.657 | 1.656 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 412.7 | 418.4 | 377.3 | 376.4 |
| HPA replicas, mean | 2.015 | 2.033 | 2.406 | 2.409 |
| pods started | 0.1 | 0.1 | 0.8 | 0.9 |
| pod start wait, total (s) | 0.3 | 0.2 | 1.7 | 1.8 |
| pod start wait, mean (s) | 0.3 | 0.2 | 1.05 | 1.133 |
| host CPU busy, the real machine under kind (%) | 46.15 | 46.7 | 48.33 | 49.24 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 835 | 838.5 | 840.3 | 850.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.42 | 4.251 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2625 | 0.7875 | 0.3083 | 1.375 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 0.9 | 1.8 | 2 |
| queue: job turnaround, submitted to done, mean (s) | 140.9 | 145.2 | 145.9 | 160 |
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
| worker nodes in service, mean | 6 | 5.14 | −14.3% | −1.4394 to −0.2799 | yes: GAIN |
| node-hours | 2.511 | 2.154 | −14.2% | −0.6001 to −0.1151 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 274.5 | +0.1% | −0.6593 to +1.3491 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 247.5 | −9.7% | −44.9846 to −8.2922 | yes: GAIN |
| response time (ms), mean | 465.8 | 510.4 | +9.6% | +15.2486 to +73.9163 | yes: LOSS |
| response time (ms), 95th percentile | 1809 | 2070 | +14.4% | +59.0155 to +462.1935 | yes: LOSS |
| response time (ms), 99th percentile | 2656 | 2956 | +11.3% | +83.5855 to +516.6449 | yes: LOSS |
| time over the response line (% of samples) | 19.99 | 20.51 | +2.6% | −0.5557 to +1.6068 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 12.8 | +10.3% | −0.0526 to +2.4526 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.4 | +30.400 (native is 0) | +22.7760 to +38.0240 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 22.57 | 28.19 | +24.9% | +0.0971 to +11.1362 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06656 | 0.07718 | +16.0% | +0.0038 to +0.0175 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.598 | 1.586 | −0.7% | −0.0442 to +0.0220 | no |
| Omni's own CPU (cores), mean | 0 | 0.06949 | +0.069 (native is 0) | +0.0620 to +0.0770 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.598 | 1.656 | +3.7% | +0.0211 to +0.0956 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.4 | 376.4 | −10.0% | −70.2321 to −13.7607 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.033 | 2.409 | +18.5% | +0.2515 to +0.5020 | yes: power given |
| pods started | 0.1 | 0.9 | +800.0% | +0.0612 to +1.5388 | yes: power given |
| pod start wait, total (s) | 0.2 | 1.8 | +800.0% | −0.1586 to +3.3586 | no |
| pod start wait, mean (s) | 0.2 | 1.133 | +466.7% | −0.0124 to +1.8791 | no |
| host CPU busy, the real machine under kind (%) | 46.7 | 49.24 | +5.4% | +1.8982 to +3.1906 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 838.5 | 850.6 | +1.4% | +4.5641 to +19.6359 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.251 | −29.2% | −2.8250 to −0.6735 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7875 | 1.375 | +74.6% | −1.0367 to +2.2117 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 2 | +122.2% | −1.1733 to +3.3733 | no |
| queue: job turnaround, submitted to done, mean (s) | 145.2 | 160 | +10.3% | +3.6477 to +26.1273 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.511 | −0.2% | −0.0114 to +0.0037 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.8 | 274.1 | −0.2% | −1.5842 to +0.2543 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.8 | 274.1 | −0.2% | −1.5842 to +0.2543 | no |
| response time (ms), mean | 486.6 | 465.8 | −4.3% | −35.4886 to −6.0016 | yes: GAIN |
| response time (ms), 95th percentile | 1866 | 1809 | −3.0% | −173.6739 to +59.9619 | no |
| response time (ms), 99th percentile | 2640 | 2656 | +0.6% | −150.9126 to +182.4018 | no |
| time over the response line (% of samples) | 21.68 | 19.99 | −7.8% | −2.9445 to −0.4462 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.5 | 11.6 | −7.2% | −1.8204 to +0.0204 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.45 | 22.57 | +22.4% | +1.3829 to +6.8638 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06732 | 0.06656 | −1.1% | −0.0018 to +0.0003 | no |
| CPU used (cores), mean | 1.616 | 1.598 | −1.1% | −0.0444 to +0.0079 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.616 | 1.598 | −1.1% | −0.0444 to +0.0079 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 412.7 | 418.4 | +1.4% | −1.9290 to +13.3371 | no |
| HPA replicas, mean | 2.015 | 2.033 | +0.9% | −0.1201 to +0.1564 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.3 | 0.2 | −33.3% | −0.9564 to +0.7564 | no |
| pod start wait, mean (s) | 0.3 | 0.2 | −33.3% | −0.9564 to +0.7564 | no |
| host CPU busy, the real machine under kind (%) | 46.15 | 46.7 | +1.2% | +0.2035 to +0.8881 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 835 | 838.5 | +0.4% | −0.9639 to +7.9639 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2625 | 0.7875 | +200.0% | −0.2276 to +1.2776 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 0.9 | −47.1% | −2.0064 to +0.4064 | no |
| queue: job turnaround, submitted to done, mean (s) | 140.9 | 145.2 | +3.0% | −1.2006 to +9.6673 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.213 | −13.1% | −1.4144 to −0.1592 | yes: GAIN |
| node-hours | 2.515 | 2.183 | −13.2% | −0.5946 to −0.0692 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.8 | 274.5 | −0.1% | −1.0181 to +0.4301 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.8 | 249.8 | −9.1% | −44.8518 to −5.1696 | yes: GAIN |
| response time (ms), mean | 486.6 | 502.9 | +3.4% | −4.4910 to +37.1596 | no |
| response time (ms), 95th percentile | 1866 | 1954 | +4.7% | −20.6409 to +195.4869 | no |
| response time (ms), 99th percentile | 2640 | 2750 | +4.2% | −40.7592 to +261.7424 | no |
| time over the response line (% of samples) | 21.68 | 21.92 | +1.1% | −1.4124 to +1.8863 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.5 | 12.9 | +3.2% | −0.2911 to +1.0911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.2 | +36.200 (native is 0) | +24.3701 to +48.0299 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.45 | 21.38 | +15.9% | −0.2584 to +6.1284 | no |
| utilisation (used / allocatable) | 0.06732 | 0.07676 | +14.0% | +0.0019 to +0.0170 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.616 | 1.592 | −1.5% | −0.0588 to +0.0119 | no |
| Omni's own CPU (cores), mean | 0 | 0.06426 | +0.064 (native is 0) | +0.0574 to +0.0712 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.616 | 1.657 | +2.5% | +0.0015 to +0.0800 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 412.7 | 377.3 | −8.6% | −65.0395 to −5.7446 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.015 | 2.406 | +19.4% | +0.1682 to +0.6137 | yes: power given |
| pods started | 0.1 | 0.8 | +700.0% | −0.0578 to +1.4578 | no |
| pod start wait, total (s) | 0.3 | 1.7 | +466.7% | −0.3907 to +3.1907 | no |
| pod start wait, mean (s) | 0.3 | 1.05 | +250.0% | −0.5032 to +2.0032 | no |
| host CPU busy, the real machine under kind (%) | 46.15 | 48.33 | +4.7% | +1.4647 to +2.8973 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 835 | 840.3 | +0.6% | −2.0880 to +12.6880 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.42 | −26.3% | −2.7789 to −0.3805 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2625 | 0.3083 | +17.5% | −0.2253 to +0.3170 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 1.8 | +5.9% | −1.9358 to +2.1358 | no |
| queue: job turnaround, submitted to done, mean (s) | 140.9 | 145.9 | +3.5% | −2.5054 to +12.3971 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.213 | −13.1% | −1.4144 to −0.1592 | yes: GAIN |
| node-hours | 2.511 | 2.183 | −13.1% | −0.5881 to −0.0680 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 274.5 | +0.1% | −0.4036 to +1.1455 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 249.8 | −8.9% | −43.6987 to −4.9927 | yes: GAIN |
| response time (ms), mean | 465.8 | 502.9 | +8.0% | +8.5786 to +65.5802 | yes: LOSS |
| response time (ms), 95th percentile | 1809 | 1954 | +8.0% | −26.1400 to +314.6980 | no |
| response time (ms), 99th percentile | 2656 | 2750 | +3.6% | −69.5595 to +259.0535 | no |
| time over the response line (% of samples) | 19.99 | 21.92 | +9.7% | +0.0481 to +3.8165 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 12.9 | +11.2% | +0.0819 to +2.5181 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.2 | +36.200 (native is 0) | +24.3701 to +48.0299 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 22.57 | 21.38 | −5.3% | −4.0862 to +1.7095 | no |
| utilisation (used / allocatable) | 0.06656 | 0.07676 | +15.3% | +0.0023 to +0.0180 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.598 | 1.592 | −0.3% | −0.0303 to +0.0198 | no |
| Omni's own CPU (cores), mean | 0 | 0.06426 | +0.064 (native is 0) | +0.0574 to +0.0712 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.598 | 1.657 | +3.7% | +0.0320 to +0.0860 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.4 | 377.3 | −9.8% | −73.3276 to −8.8647 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.033 | 2.406 | +18.3% | +0.1009 to +0.6447 | yes: power given |
| pods started | 0.1 | 0.8 | +700.0% | +0.1111 to +1.2889 | yes: power given |
| pod start wait, total (s) | 0.2 | 1.7 | +750.0% | +0.2271 to +2.7729 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.05 | +425.0% | +0.0583 to +1.6417 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.7 | 48.33 | +3.5% | +1.0127 to +2.2576 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 838.5 | 840.3 | +0.2% | −5.0676 to +8.6676 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.42 | −26.3% | −2.7789 to −0.3805 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7875 | 0.3083 | −60.8% | −1.1276 to +0.1693 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 1.8 | +100.0% | −1.3227 to +3.1227 | no |
| queue: job turnaround, submitted to done, mean (s) | 145.2 | 145.9 | +0.5% | −5.8094 to +7.2344 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.14 | −14.3% | −1.4394 to −0.2799 | yes: GAIN |
| node-hours | 2.515 | 2.154 | −14.4% | −0.6064 to −0.1165 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.8 | 274.5 | −0.1% | −1.3359 to +0.6958 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.8 | 247.5 | −9.9% | −46.1454 to −8.4614 | yes: GAIN |
| response time (ms), mean | 486.6 | 510.4 | +4.9% | −0.9521 to +48.6267 | no |
| response time (ms), 95th percentile | 1866 | 2070 | +10.9% | +25.8702 to +381.6268 | yes: LOSS |
| response time (ms), 99th percentile | 2640 | 2956 | +12.0% | +61.7867 to +569.9329 | yes: LOSS |
| time over the response line (% of samples) | 21.68 | 20.51 | −5.4% | −2.3847 to +0.0452 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.5 | 12.8 | +2.4% | −0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.4 | +30.400 (native is 0) | +22.7760 to +38.0240 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.45 | 28.18 | +52.8% | +2.4036 to +17.0764 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06732 | 0.07718 | +14.6% | +0.0035 to +0.0163 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.616 | 1.586 | −1.8% | −0.0665 to +0.0078 | no |
| Omni's own CPU (cores), mean | 0 | 0.06949 | +0.069 (native is 0) | +0.0620 to +0.0770 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.616 | 1.656 | +2.5% | −0.0032 to +0.0835 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 412.7 | 376.4 | −8.8% | −60.8058 to −11.7788 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.015 | 2.409 | +19.6% | +0.2720 to +0.5178 | yes: power given |
| pods started | 0.1 | 0.9 | +800.0% | −0.0121 to +1.6121 | no |
| pod start wait, total (s) | 0.3 | 1.8 | +500.0% | −0.4444 to +3.4444 | no |
| pod start wait, mean (s) | 0.3 | 1.133 | +277.8% | −0.3941 to +2.0608 | no |
| host CPU busy, the real machine under kind (%) | 46.15 | 49.24 | +6.7% | +2.4824 to +3.6980 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 835 | 850.6 | +1.9% | +6.2176 to +24.9824 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.251 | −29.2% | −2.8250 to −0.6735 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2625 | 1.375 | +423.8% | −0.2750 to +2.5000 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.7 | 2 | +17.6% | −2.3775 to +2.9775 | no |
| queue: job turnaround, submitted to done, mean (s) | 140.9 | 160 | +13.6% | +6.1294 to +32.1122 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*