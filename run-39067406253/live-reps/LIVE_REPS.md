# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.259 |
| node-hours | 2.513 | 2.204 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 273.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 250.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 558 | 503.4 |
| response time (ms), 95th percentile | 3354 | 3358 |
| response time (ms), 99th percentile | 5023 | 5017 |
| time over the response line (% of samples) | 16.13 | 15.45 |
| failed requests (%) | 0.01075 | 0.01036 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 197.1 | 198.6 |
| utilisation (used / allocatable) | 0.0635 | 0.07241 |
| CPU used (cores), mean | 1.524 | 1.516 |
| Omni's own CPU (cores), mean | 0 | 0.02413 |
| CPU used with Omni's own (cores), mean | 1.524 | 1.54 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 434.1 | 396.3 |
| HPA replicas, mean | 2.187 | 2.149 |
| pods started | 0.2 | 0.2 |
| pod start wait, total (s) | 9.1 | 0.2 |
| pod start wait, mean (s) | 9.1 | 0.2 |
| host CPU busy, the real machine under kind (%) | 44.05 | 44.88 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 604.4 | 608.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.772 |

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
| worker nodes in service, mean | 6 | 5.259 | -12.3% | -1.139 to -0.3429 | yes: GAIN |
| node-hours | 2.513 | 2.204 | -12.3% | -0.4769 to -0.1401 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 273.8 | +0.0% | -1.193 to +1.429 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 250.6 | -8.5% | -35.86 to -10.43 | yes: GAIN |
| response time (ms), mean | 558 | 503.4 | -9.8% | -71.63 to -37.56 | yes: GAIN |
| response time (ms), 95th percentile | 3354 | 3358 | +0.1% | -158.2 to +167.3 | no |
| response time (ms), 99th percentile | 5023 | 5017 | -0.1% | -328.5 to +317.4 | no |
| time over the response line (% of samples) | 16.13 | 15.45 | -4.2% | -1.116 to -0.236 | yes: GAIN |
| failed requests (%) | 0.01075 | 0.01036 | -3.6% | -0.036 to +0.03522 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.5 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.8 | +11.8 (native is 0) | +10.8 to +12.8 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 197.1 | 198.6 | +0.8% | -3.672 to +6.788 | no |
| utilisation (used / allocatable) | 0.0635 | 0.07241 | +14.0% | +0.003398 to +0.01443 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.524 | 1.516 | -0.5% | -0.0678 to +0.0516 | no |
| Omni's own CPU (cores), mean | 0 | 0.02413 | +0.0241 (native is 0) | +0.02039 to +0.02787 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.524 | 1.54 | +1.1% | -0.04279 to +0.07485 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 434.1 | 396.3 | -8.7% | -66.37 to -9.242 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.187 | 2.149 | -1.8% | -0.2921 to +0.2154 | no |
| pods started | 0.2 | 0.2 | +0.0% | -0.4769 to +0.4769 | no |
| pod start wait, total (s) | 9.1 | 0.2 | -97.8% | -22.83 to +5.025 | no |
| pod start wait, mean (s) | 9.1 | 0.2 | -97.8% | -22.83 to +5.025 | no |
| host CPU busy, the real machine under kind (%) | 44.05 | 44.88 | +1.9% | +0.5941 to +1.065 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 604.4 | 608.5 | +0.7% | +0.3993 to +7.801 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.772 | -20.5% | -1.844 to -0.6108 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*