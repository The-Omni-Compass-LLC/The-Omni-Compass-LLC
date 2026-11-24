# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 3600 | 2768 |
| response time (ms), 99th percentile | 5588 | 4754 |
| time over the response line (% of samples) | 51.44 | 50.8 |
| failed requests (%) | 37.04 | 39.51 |
| HPA replicas, mean | 9.814 | 11.82 |
| pods started | 3.959 | 8.449 |
| worker nodes in service, mean | 5.998 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.9 | 275.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.8 | 275.8 |
| CPU used with Omni's own (cores), mean | 2.393 | 2.451 |
| host CPU busy, the real machine under kind (%) | 73.86 | 80.79 |
| organism work | 6.65e+12 | 6.65e+12 |
| organism energy (J) | 1.098e+15 | 1.098e+15 |
| organism time over the line (% of steps) | 1.484 | 1.395 |
| organism work per energy | 0.006054 | 0.006054 |
| organism behind its window (s) | 0.7388 | 0.4163 |

## Each organism: omni against native, paired by repetition

### Energy / Facility / Industrial, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

49 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3600 | 2768 | -23.1% | -1536 to -127.1 | GAIN |
| response time (ms), 99th percentile | 5588 | 4754 | -14.9% | -1500 to -167.9 | GAIN |
| time over the response line (% of samples) | 51.44 | 50.8 | -1.3% | -1.855 to +0.5679 | STEADY, inside the noise (cut) |
| failed requests (%) | 37.04 | 39.51 | +6.7% | +0.05603 to +4.887 | LOSS |
| HPA replicas, mean | 9.814 | 11.82 | +20.4% | +1.353 to +2.653 | power given |
| pods started | 3.959 | 8.449 | +113.4% | +3.548 to +5.432 | power given |
| worker nodes in service, mean | 5.998 | 6 | +0.0% | -0.002 to +0.005958 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.9 | 275.8 | -0.0% | -0.5091 to +0.3983 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.8 | 275.8 | +0.0% | -0.4779 to +0.4861 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.393 | 2.451 | +2.4% | +0.03774 to +0.07763 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.86 | 80.79 | +9.4% | +6.39 to +7.464 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.7388 | 0.4163 | -43.6% | -0.3615 to -0.2834 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The spine, the muscles every stack runs on
- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Distribution / Specialized
- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
