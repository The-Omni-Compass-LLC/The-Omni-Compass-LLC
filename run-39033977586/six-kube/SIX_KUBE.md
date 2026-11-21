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
| response time (ms), 95th percentile | 1673 | 1505 | 1783 | 1668 | 1680 | 1359 | 1823 | 1807 |
| response time (ms), 99th percentile | 4883 | 5008 | 5286 | 5212 | 4598 | 4260 | 5175 | 5185 |
| time over the response line (% of samples) | 29.55 | 20.44 | 18.77 | 13.76 | 15.56 | 11.23 | 28.13 | 20.76 |
| failed requests (%) | 13.17 | 11.06 | 6.149 | 5.464 | 4.849 | 4.567 | 9.278 | 8.404 |
| HPA replicas, mean | 9.678 | 12.74 | 9.621 | 13.4 | 9.559 | 12.68 | 9.612 | 13.86 |
| pods started | 4.968 | 9.903 | 5 | 10.06 | 5.435 | 9.468 | 5.129 | 10.02 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 182.4 | 182.1 | 180.5 | 179.8 | 178.8 | 178.3 | 182.5 | 182.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.4 | 182.1 | 180.5 | 179.8 | 178.8 | 178.3 | 182.5 | 182.1 |
| CPU used with Omni's own (cores), mean | 2.204 | 2.191 | 1.996 | 2.002 | 1.846 | 1.855 | 2.196 | 2.193 |
| host CPU busy, the real machine under kind (%) | 65.1 | 65.14 | 59.21 | 59.49 | 55.08 | 55.32 | 64.79 | 65.24 |
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
| response time (ms), 95th percentile | 1673 | 1505 | -10.0% | -354.5 to +19.25 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4883 | 5008 | +2.6% | -270.9 to +520.1 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 29.55 | 20.44 | -30.8% | -10.69 to -7.537 | GAIN |
| failed requests (%) | 13.17 | 11.06 | -16.0% | -2.788 to -1.425 | GAIN |
| HPA replicas, mean | 9.678 | 12.74 | +31.7% | +2.592 to +3.535 | power given |
| pods started | 4.968 | 9.903 | +99.4% | +4.36 to +5.511 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.435e-16 to +2.435e-16 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 182.4 | 182.1 | -0.2% | -0.7395 to +0.01489 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.4 | 182.1 | -0.2% | -0.7395 to +0.01489 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.204 | 2.191 | -0.6% | -0.02206 to -0.003909 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.1 | 65.14 | +0.1% | -0.1925 to +0.2806 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.62e+05 to +8.623e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.147e-05 to -8.144e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1783 | 1668 | -6.5% | -322.2 to +92.04 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5286 | 5212 | -1.4% | -375.5 to +226.6 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 18.77 | 13.76 | -26.7% | -5.913 to -4.095 | GAIN |
| failed requests (%) | 6.149 | 5.464 | -11.1% | -1.098 to -0.2736 | GAIN |
| HPA replicas, mean | 9.621 | 13.4 | +39.3% | +3.289 to +4.272 | power given |
| pods started | 5 | 10.06 | +101.3% | +4.423 to +5.706 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.957e-16 to -6.324e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.5 | 179.8 | -0.4% | -1.122 to -0.3867 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.5 | 179.8 | -0.4% | -1.122 to -0.3867 | GAIN |
| CPU used with Omni's own (cores), mean | 1.996 | 2.002 | +0.3% | -0.0009474 to +0.01328 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.21 | 59.49 | +0.5% | +0.1366 to +0.4422 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.245e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 7 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 0

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1680 | 1359 | -19.1% | -496.9 to -145.7 | GAIN |
| response time (ms), 99th percentile | 4598 | 4260 | -7.4% | -591.1 to -85.56 | GAIN |
| time over the response line (% of samples) | 15.56 | 11.23 | -27.8% | -5.268 to -3.391 | GAIN |
| failed requests (%) | 4.849 | 4.567 | -5.8% | -0.5074 to -0.05686 | GAIN |
| HPA replicas, mean | 9.559 | 12.68 | +32.7% | +2.555 to +3.691 | power given |
| pods started | 5.435 | 9.468 | +74.2% | +3.331 to +4.733 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.075e-16 to -5.146e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.8 | 178.3 | -0.3% | -0.793 to -0.1971 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.8 | 178.3 | -0.3% | -0.793 to -0.1971 | GAIN |
| CPU used with Omni's own (cores), mean | 1.846 | 1.855 | +0.5% | +0.0008878 to +0.01723 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.08 | 55.32 | +0.4% | +0.02064 to +0.4654 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1823 | 1807 | -0.9% | -153.9 to +121.6 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5175 | 5185 | +0.2% | -311.1 to +329.6 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 28.13 | 20.76 | -26.2% | -8.607 to -6.122 | GAIN |
| failed requests (%) | 9.278 | 8.404 | -9.4% | -1.339 to -0.4069 | GAIN |
| HPA replicas, mean | 9.612 | 13.86 | +44.2% | +3.81 to +4.69 | power given |
| pods started | 5.129 | 10.02 | +95.3% | +4.352 to +5.423 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.718e-16 to -1.255e-18 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.5 | 182.1 | -0.2% | -0.7662 to -0.08321 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.5 | 182.1 | -0.2% | -0.7662 to -0.08321 | GAIN |
| CPU used with Omni's own (cores), mean | 2.196 | 2.193 | -0.1% | -0.01057 to +0.004603 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.79 | 65.24 | +0.7% | +0.2641 to +0.6422 | shown, not judged |
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
