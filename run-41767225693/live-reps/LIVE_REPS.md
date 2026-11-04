# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.514 | 1.512 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 157.4 | 157.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 157.4 | 157.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 118.4 | 66.61 | 69.07 |
| response time (ms), 95th percentile | 255.7 | 91.95 | 93.34 |
| response time (ms), 99th percentile | 413.4 | 120.1 | 119.9 |
| time over the response line (% of samples) | 0.956 | 0 | 0.2263 |
| failed requests (%) | 0 | 0 | 0.02469 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.9 | 0 | 0.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.4 | 33.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | 44.44 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.3467 | 0.025 |
| utilisation (used / allocatable) | 0.03291 | 0.03215 | 0.03255 |
| CPU used (cores), mean | 0.7897 | 0.7716 | 0.7811 |
| Omni's own CPU (cores), mean | 0 | 0.03298 | 0.03444 |
| CPU used with Omni's own (cores), mean | 0.7897 | 0.8045 | 0.8155 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 847.2 | 856.9 | 848.5 |
| HPA replicas, mean | 8.093 | 8.158 | 8.913 |
| pods started | 5.2 | 4.9 | 11.3 |
| pod start wait, total (s) | 7.6 | 8.8 | 20.3 |
| pod start wait, mean (s) | 1.423 | 1.576 | 1.827 |
| host CPU busy, the real machine under kind (%) | 24.58 | 25.13 | 25.65 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.512 | −0.1% | −0.0064 to +0.0030 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 157.4 | −0.2% | −0.8302 to +0.1263 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 157.4 | −0.2% | −0.8302 to +0.1263 | no |
| response time (ms), mean | 118.4 | 66.61 | −43.7% | −73.9971 to −29.5705 | yes: GAIN |
| response time (ms), 95th percentile | 255.7 | 91.95 | −64.0% | −223.5907 to −103.9233 | yes: GAIN |
| response time (ms), 99th percentile | 413.4 | 120.1 | −71.0% | −393.8885 to −192.8113 | yes: GAIN |
| time over the response line (% of samples) | 0.956 | 0 | −100.0% | −2.0226 to +0.1105 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.9 | 0 | −100.0% | −1.9366 to +0.1366 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.4 | +19.400 (native is 0) | +17.6414 to +21.1586 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.3467 | +333.3% | −0.0698 to +0.6032 | no |
| utilisation (used / allocatable) | 0.03291 | 0.03215 | −2.3% | −0.0017 to +0.0002 | no |
| CPU used (cores), mean | 0.7897 | 0.7716 | −2.3% | −0.0410 to +0.0047 | no |
| Omni's own CPU (cores), mean | 0 | 0.03298 | +0.033 (native is 0) | +0.0289 to +0.0370 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7897 | 0.8045 | +1.9% | −0.0058 to +0.0354 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 847.2 | 856.9 | +1.1% | −3.7361 to +23.1752 | no |
| HPA replicas, mean | 8.093 | 8.158 | +0.8% | −0.0746 to +0.2037 | no |
| pods started | 5.2 | 4.9 | −5.8% | −1.0578 to +0.4578 | no |
| pod start wait, total (s) | 7.6 | 8.8 | +15.8% | −1.1796 to +3.5796 | no |
| pod start wait, mean (s) | 1.423 | 1.576 | +10.7% | −0.2620 to +0.5668 | no |
| host CPU busy, the real machine under kind (%) | 24.58 | 25.13 | +2.2% | +0.0865 to +1.0011 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.515 | +0.1% | −0.0071 to +0.0098 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 157.8 | +0.0% | −0.8080 to +0.9073 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 157.8 | +0.0% | −0.8080 to +0.9073 | no |
| response time (ms), mean | 118.4 | 69.07 | −41.7% | −71.3758 to −27.2895 | yes: GAIN |
| response time (ms), 95th percentile | 255.7 | 93.34 | −63.5% | −221.6454 to −103.0876 | yes: GAIN |
| response time (ms), 99th percentile | 413.4 | 119.9 | −71.0% | −397.1965 to −189.8903 | yes: GAIN |
| time over the response line (% of samples) | 0.956 | 0.2263 | −76.3% | −1.8054 to +0.3461 | no |
| failed requests (%) | 0 | 0.02469 | +0.025 (native is 0) | −0.0125 to +0.0619 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.9 | 0.5 | −44.4% | −1.6251 to +0.8251 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.8 | +33.800 (native is 0) | +26.6565 to +40.9435 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.025 | −68.8% | −0.1732 to +0.0632 | no |
| utilisation (used / allocatable) | 0.03291 | 0.03255 | −1.1% | −0.0012 to +0.0005 | no |
| CPU used (cores), mean | 0.7897 | 0.7811 | −1.1% | −0.0291 to +0.0118 | no |
| Omni's own CPU (cores), mean | 0 | 0.03444 | +0.034 (native is 0) | +0.0306 to +0.0383 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7897 | 0.8155 | +3.3% | +0.0066 to +0.0450 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 847.2 | 848.5 | +0.2% | −14.9720 to +17.5333 | no |
| HPA replicas, mean | 8.093 | 8.913 | +10.1% | +0.5286 to +1.1116 | yes: power given |
| pods started | 5.2 | 11.3 | +117.3% | +4.6516 to +7.5484 | yes: power given |
| pod start wait, total (s) | 7.6 | 20.3 | +167.1% | +9.0675 to +16.3325 | yes: LOSS |
| pod start wait, mean (s) | 1.423 | 1.827 | +28.4% | −0.0118 to +0.8200 | no |
| host CPU busy, the real machine under kind (%) | 24.58 | 25.65 | +4.3% | +0.6753 to +1.4523 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.512 | 1.515 | +0.2% | −0.0032 to +0.0092 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.4 | 157.8 | +0.3% | −0.2795 to +1.0828 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.4 | 157.8 | +0.3% | −0.2795 to +1.0828 | no |
| response time (ms), mean | 66.61 | 69.07 | +3.7% | +1.4285 to +3.4738 | yes: LOSS |
| response time (ms), 95th percentile | 91.95 | 93.34 | +1.5% | −0.9448 to +3.7258 | no |
| response time (ms), 99th percentile | 120.1 | 119.9 | −0.2% | −10.9302 to +10.5432 | no |
| time over the response line (% of samples) | 0 | 0.2263 | +0.226 (native is 0) | +0.1173 to +0.3354 | yes: LOSS |
| failed requests (%) | 0 | 0.02469 | +0.025 (native is 0) | −0.0125 to +0.0619 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.5 | +0.500 (native is 0) | +0.1230 to +0.8770 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 19.4 | 33.8 | +74.2% | +8.0808 to +20.7192 | yes, up (shown, not judged) |
| governor's additions decided while the service was still inside its line (% of its additions) | 100 | 44.44 | −55.6% | −96.0678 to −15.0433 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3467 | 0.025 | −92.8% | −0.6417 to −0.0016 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03215 | 0.03255 | +1.2% | −0.0000 to +0.0008 | no |
| CPU used (cores), mean | 0.7716 | 0.7811 | +1.2% | −0.0010 to +0.0200 | no |
| Omni's own CPU (cores), mean | 0.03298 | 0.03444 | +4.4% | +0.0006 to +0.0023 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8045 | 0.8155 | +1.4% | +0.0004 to +0.0216 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 856.9 | 848.5 | −1.0% | −23.2555 to +6.3777 | no |
| HPA replicas, mean | 8.158 | 8.913 | +9.3% | +0.3928 to +1.1183 | yes: power given |
| pods started | 4.9 | 11.3 | +130.6% | +5.2222 to +7.5778 | yes: power given |
| pod start wait, total (s) | 8.8 | 20.3 | +130.7% | +7.4082 to +15.5918 | yes: LOSS |
| pod start wait, mean (s) | 1.576 | 1.827 | +16.0% | −0.3837 to +0.8872 | no |
| host CPU busy, the real machine under kind (%) | 25.13 | 25.65 | +2.1% | +0.0622 to +0.9779 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*