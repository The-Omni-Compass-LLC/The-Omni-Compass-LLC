# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1479 | 1540 | 1740 | 1462 | 1885 | 1793 | 1577 | 1474 |
| response time (ms), 99th percentile | 4829 | 4927 | 5283 | 4886 | 5580 | 5319 | 4310 | 4217 |
| time over the response line (% of samples) | 26.14 | 18.16 | 18.2 | 12.81 | 19.24 | 14.26 | 22.74 | 16.45 |
| failed requests (%) | 11.27 | 9.244 | 5.578 | 5.023 | 6.496 | 5.666 | 7.41 | 6.695 |
| HPA replicas, mean | 9.657 | 12.97 | 9.606 | 13.43 | 9.623 | 13.38 | 9.58 | 13.27 |
| pods started | 5.065 | 10.29 | 5.344 | 9.967 | 5 | 9.435 | 5.242 | 9.742 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 181.5 | 181.3 | 180.3 | 179.6 | 180.7 | 179.8 | 180.8 | 180.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.5 | 181.3 | 180.3 | 179.6 | 180.7 | 179.8 | 180.8 | 180.3 |
| CPU used with Omni's own (cores), mean | 2.13 | 2.121 | 1.985 | 1.989 | 1.995 | 2 | 2.037 | 2.036 |
| host CPU busy, the real machine under kind (%) | 63.1 | 63.12 | 58.9 | 59.09 | 59.22 | 59.34 | 60.45 | 60.84 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 4

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1479 | 1540 | +4.1% | -116.3 to +237.7 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4829 | 4927 | +2.0% | -252.7 to +449.2 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 26.14 | 18.16 | -30.5% | -9.624 to -6.343 | GAIN |
| failed requests (%) | 11.27 | 9.244 | -18.0% | -2.71 to -1.345 | GAIN |
| HPA replicas, mean | 9.657 | 12.97 | +34.3% | +2.84 to +3.777 | power given |
| pods started | 5.065 | 10.29 | +103.2% | +4.614 to +5.838 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.382e-16 to +1.663e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.5 | 181.3 | -0.1% | -0.5412 to +0.1366 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.5 | 181.3 | -0.1% | -0.5412 to +0.1366 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.13 | 2.121 | -0.5% | -0.02061 to +0.0007271 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.1 | 63.12 | +0.0% | -0.272 to +0.3035 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.619e+05 to +8.623e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.147e-05 to -8.144e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 7 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 0

61 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1740 | 1462 | -16.0% | -473.9 to -81.57 | GAIN |
| response time (ms), 99th percentile | 5283 | 4886 | -7.5% | -640.7 to -152.9 | GAIN |
| time over the response line (% of samples) | 18.2 | 12.81 | -29.6% | -6.404 to -4.364 | GAIN |
| failed requests (%) | 5.578 | 5.023 | -9.9% | -1.024 to -0.08527 | GAIN |
| HPA replicas, mean | 9.606 | 13.43 | +39.8% | +3.359 to +4.296 | power given |
| pods started | 5.344 | 9.967 | +86.5% | +4.075 to +5.171 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.541e-16 to +2.376e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.3 | 179.6 | -0.4% | -1.025 to -0.3633 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.3 | 179.6 | -0.4% | -1.025 to -0.3633 | GAIN |
| CPU used with Omni's own (cores), mean | 1.985 | 1.989 | +0.2% | -0.003158 to +0.01043 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.9 | 59.09 | +0.3% | +0.02378 to +0.3483 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1885 | 1793 | -4.9% | -367 to +184 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5580 | 5319 | -4.7% | -598.1 to +77.35 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 19.24 | 14.26 | -25.9% | -5.798 to -4.158 | GAIN |
| failed requests (%) | 6.496 | 5.666 | -12.8% | -1.155 to -0.5059 | GAIN |
| HPA replicas, mean | 9.623 | 13.38 | +39.0% | +3.245 to +4.263 | power given |
| pods started | 5 | 9.435 | +88.7% | +3.784 to +5.086 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.625e-16 to +1.812e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.7 | 179.8 | -0.5% | -1.266 to -0.5885 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.7 | 179.8 | -0.5% | -1.266 to -0.5885 | GAIN |
| CPU used with Omni's own (cores), mean | 1.995 | 2 | +0.2% | -0.002695 to +0.01257 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.22 | 59.34 | +0.2% | -0.08498 to +0.3135 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1577 | 1474 | -6.5% | -247.9 to +42.4 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4310 | 4217 | -2.2% | -396.2 to +210.4 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 22.74 | 16.45 | -27.6% | -7.57 to -4.997 | GAIN |
| failed requests (%) | 7.41 | 6.695 | -9.7% | -0.99 to -0.4409 | GAIN |
| HPA replicas, mean | 9.58 | 13.27 | +38.5% | +3.176 to +4.199 | power given |
| pods started | 5.242 | 9.742 | +85.8% | +3.865 to +5.135 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.091e-16 to +1.08e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 180.3 | -0.3% | -0.7928 to -0.1199 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 180.3 | -0.3% | -0.7928 to -0.1199 | GAIN |
| CPU used with Omni's own (cores), mean | 2.037 | 2.036 | -0.0% | -0.007729 to +0.006381 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.45 | 60.84 | +0.6% | +0.1742 to +0.6091 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
