# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.421 |
| node-hours | 2.511 | 2.271 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 255.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 486.1 | 439 |
| response time (ms), 95th percentile | 2808 | 2789 |
| response time (ms), 99th percentile | 3778 | 3769 |
| time over the response line (% of samples) | 17.04 | 16.45 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 10.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 190.2 | 186.1 |
| utilisation (used / allocatable) | 0.06289 | 0.06949 |
| CPU used (cores), mean | 1.509 | 1.492 |
| Omni's own CPU (cores), mean | 0 | 0.01608 |
| CPU used with Omni's own (cores), mean | 1.509 | 1.509 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.2 | 410 |
| HPA replicas, mean | 2.285 | 2.485 |
| pods started | 0.1 | 0.6 |
| pod start wait, total (s) | 0.6 | 0.8 |
| pod start wait, mean (s) | 0.6 | 0.8 |
| host CPU busy, the real machine under kind (%) | 43.62 | 43.88 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 591.8 | 589.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.102 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |

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
| worker nodes in service, mean | 6 | 5.421 | −9.6% | −1.1711 to +0.0141 | no |
| node-hours | 2.511 | 2.271 | −9.5% | −0.4883 to +0.0100 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273.3 | +0.0% | −0.8841 to +1.0478 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 255.2 | −6.6% | −37.0985 to +1.0163 | no |
| response time (ms), mean | 486.1 | 439 | −9.7% | −58.5247 to −35.5810 | yes: GAIN |
| response time (ms), 95th percentile | 2808 | 2789 | −0.7% | −108.8324 to +69.3904 | no |
| response time (ms), 99th percentile | 3778 | 3769 | −0.2% | −146.1420 to +127.5010 | no |
| time over the response line (% of samples) | 17.04 | 16.45 | −3.5% | −1.1115 to −0.0688 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 10.1 | −1.0% | −0.5060 to +0.3060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.7 | +11.700 (native is 0) | +10.9422 to +12.4578 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 190.2 | 186.1 | −2.1% | −9.3001 to +1.2034 | no |
| utilisation (used / allocatable) | 0.06289 | 0.06949 | +10.5% | −0.0005 to +0.0137 | no |
| CPU used (cores), mean | 1.509 | 1.492 | −1.1% | −0.0668 to +0.0328 | no |
| Omni's own CPU (cores), mean | 0 | 0.01608 | +0.016 (native is 0) | +0.0150 to +0.0171 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.509 | 1.509 | −0.1% | −0.0510 to +0.0492 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.2 | 410 | −6.0% | −56.6536 to +4.2454 | no |
| HPA replicas, mean | 2.285 | 2.485 | +8.8% | −0.2883 to +0.6897 | no |
| pods started | 0.1 | 0.6 | +500.0% | +0.1230 to +0.8770 | yes: power given |
| pod start wait, total (s) | 0.6 | 0.8 | +33.3% | −1.2226 to +1.6226 | no |
| pod start wait, mean (s) | 0.6 | 0.8 | +33.3% | −1.2226 to +1.6226 | no |
| host CPU busy, the real machine under kind (%) | 43.62 | 43.88 | +0.6% | −0.2485 to +0.7736 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 591.8 | 589.3 | −0.4% | −12.3266 to +7.3266 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.102 | −15.0% | −1.8096 to +0.0144 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*