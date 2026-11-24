# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 3912 | 3863 |
| response time (ms), 99th percentile | 6139 | 5905 |
| time over the response line (% of samples) | 54.04 | 55.15 |
| failed requests (%) | 37.75 | 41.48 |
| HPA replicas, mean | 9.804 | 11.33 |
| pods started | 4.318 | 7.203 |
| worker nodes in service, mean | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.9 | 276.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.9 | 276.8 |
| CPU used with Omni's own (cores), mean | 2.458 | 2.51 |
| host CPU busy, the real machine under kind (%) | 74.81 | 83.38 |
| organism work | 2.126e+12 | 2.126e+12 |
| organism energy (J) | 1.544e+12 | 1.545e+12 |
| organism time over the line (% of steps) | 1.963 | 1.892 |
| organism work per energy | 1.377 | 1.376 |
| organism behind its window (s) | 0.8097 | 1.2 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

217 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3912 | 3863 | -1.3% | -326.9 to +228.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6139 | 5905 | -3.8% | -479.4 to +10.94 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 54.04 | 55.15 | +2.1% | +0.2599 to +1.957 | LOSS |
| failed requests (%) | 37.75 | 41.48 | +9.9% | +2.515 to +4.935 | LOSS |
| HPA replicas, mean | 9.804 | 11.33 | +15.5% | +1.224 to +1.825 | power given |
| pods started | 4.318 | 7.203 | +66.8% | +2.433 to +3.336 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002837 to +0.001196 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.9 | 276.8 | -0.0% | -0.3422 to +0.1284 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.9 | 276.8 | -0.0% | -0.3833 to +0.1202 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.458 | 2.51 | +2.1% | +0.04301 to +0.06189 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.81 | 83.38 | +11.4% | +8.331 to +8.798 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.8097 | 1.2 | +48.3% | +0.3639 to +0.4177 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The spine, the muscles every stack runs on
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
