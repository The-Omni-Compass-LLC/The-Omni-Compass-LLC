# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3462 | 3571 | 2884 | 2317 | 3031 | 2587 | 3447 | 3751 |
| response time (ms), 99th percentile | 5630 | 5402 | 4658 | 4587 | 5166 | 5467 | 5491 | 5545 |
| time over the response line (% of samples) | 51.94 | 45.05 | 41.06 | 33.82 | 49.04 | 44.03 | 44.03 | 40.66 |
| failed requests (%) | 25.77 | 30.01 | 25.29 | 24.95 | 31.89 | 31.07 | 27.32 | 28.04 |
| HPA replicas, mean | 9.83 | 9.845 | 9.775 | 9.8 | 9.825 | 9.822 | 9.805 | 9.804 |
| pods started | 4 | 3.3 | 4.6 | 4.3 | 3.7 | 3.8 | 3.8 | 4 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 285.4 | 282.9 | 280.9 | 279.5 | 281.7 | 280.4 | 282.6 | 281 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.4 | 282.9 | 280.9 | 279.5 | 281.7 | 280.4 | 282.6 | 281 |
| CPU used with Omni's own (cores), mean | 3.029 | 2.886 | 2.723 | 2.648 | 2.82 | 2.727 | 2.856 | 2.787 |
| host CPU busy, the real machine under kind (%) | 88.9 | 92.02 | 81.44 | 84.02 | 84.81 | 87.27 | 84.66 | 89.21 |
| organism work | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 1.49 | 1.79 | 0.67 | 0.67 | 1.18 | 0.7 | 0.85 | 1.52 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 100 copies: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3462 | 3571 | +3.2% | -1893 to +2111 | WORSE (inside the noise) |
| response time (ms), 99th percentile | 5630 | 5402 | -4.1% | -2166 to +1710 | better (inside the noise) |
| time over the response line (% of samples) | 51.94 | 45.05 | -13.3% | -8.716 to -5.063 | better |
| failed requests (%) | 25.77 | 30.01 | +16.5% | -1.652 to +10.14 | WORSE (inside the noise) |
| HPA replicas, mean | 9.83 | 9.845 | +0.2% | -0.02111 to +0.05081 | WORSE (inside the noise) |
| pods started | 4 | 3.3 | -17.5% | -1.769 to +0.369 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | +8.169e-16 to +2.558e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 285.4 | 282.9 | -0.9% | -4.238 to -0.6241 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.4 | 282.9 | -0.9% | -4.238 to -0.6241 | better |
| CPU used with Omni's own (cores), mean | 3.029 | 2.886 | -4.7% | -0.2429 to -0.04276 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 88.9 | 92.02 | +3.5% | +0.8103 to +5.423 | shown, not judged (more or less is not better by itself) |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.56e+08 to +8.56e+08 | WORSE |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07147 to -0.07147 | better |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007629 to -0.0007629 | WORSE |
| organism behind its window (s) | 1.49 | 1.79 | +20.1% | -0.1648 to +0.7648 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2884 | 2317 | -19.7% | -1673 to +538.4 | better (inside the noise) |
| response time (ms), 99th percentile | 4658 | 4587 | -1.5% | -724.8 to +583.6 | better (inside the noise) |
| time over the response line (% of samples) | 41.06 | 33.82 | -17.6% | -11.35 to -3.126 | better |
| failed requests (%) | 25.29 | 24.95 | -1.3% | -2.413 to +1.745 | better (inside the noise) |
| HPA replicas, mean | 9.775 | 9.8 | +0.3% | -0.01311 to +0.06227 | WORSE (inside the noise) |
| pods started | 4.6 | 4.3 | -6.5% | -1.129 to +0.5294 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.846e-16 to +2.028e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 280.9 | 279.5 | -0.5% | -2.77 to -0.1304 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 280.9 | 279.5 | -0.5% | -2.77 to -0.1304 | better |
| CPU used with Omni's own (cores), mean | 2.723 | 2.648 | -2.8% | -0.1517 to +0.001619 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 81.44 | 84.02 | +3.2% | +0.7494 to +4.416 | shown, not judged (more or less is not better by itself) |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.783e+08 to +8.783e+08 | WORSE |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09381 to -0.09381 | better |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004956 to -0.0004956 | WORSE |
| organism behind its window (s) | 0.67 | 0.67 | +0.0% | -0.3724 to +0.3724 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: better on 4, worse on 0, inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3031 | 2587 | -14.7% | -1528 to +639.9 | better (inside the noise) |
| response time (ms), 99th percentile | 5166 | 5467 | +5.8% | -681.4 to +1285 | WORSE (inside the noise) |
| time over the response line (% of samples) | 49.04 | 44.03 | -10.2% | -7.847 to -2.172 | better |
| failed requests (%) | 31.89 | 31.07 | -2.6% | -2.897 to +1.249 | better (inside the noise) |
| HPA replicas, mean | 9.825 | 9.822 | -0.0% | -0.03015 to +0.02434 | better (inside the noise) |
| pods started | 3.7 | 3.8 | +2.7% | -0.4278 to +0.6278 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.441e-15 to +3.755e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 281.7 | 280.4 | -0.5% | -2.64 to -0.02179 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 281.7 | 280.4 | -0.5% | -2.64 to -0.02179 | better |
| CPU used with Omni's own (cores), mean | 2.82 | 2.727 | -3.3% | -0.1619 to -0.02423 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 84.81 | 87.27 | +2.9% | +0.805 to +4.1 | shown, not judged (more or less is not better by itself) |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.755e+08 to +8.755e+08 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08823 to -0.08823 | better |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.826e-09 to -4.826e-09 | same (under one part in a million) |
| organism behind its window (s) | 1.18 | 0.7 | -40.7% | -0.7408 to -0.2192 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: better on 2, worse on 2 (organism energy (J); organism work per energy), inside the noise on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3447 | 3751 | +8.8% | -142.8 to +751.1 | WORSE (inside the noise) |
| response time (ms), 99th percentile | 5491 | 5545 | +1.0% | -1016 to +1123 | WORSE (inside the noise) |
| time over the response line (% of samples) | 44.03 | 40.66 | -7.6% | -6.444 to -0.2838 | better |
| failed requests (%) | 27.32 | 28.04 | +2.6% | -1.82 to +3.246 | WORSE (inside the noise) |
| HPA replicas, mean | 9.805 | 9.804 | -0.0% | -0.04915 to +0.04629 | better (inside the noise) |
| pods started | 3.8 | 4 | +5.3% | -0.7417 to +1.142 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.507e-15 to +2.04e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 282.6 | 281 | -0.6% | -3.39 to +0.199 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 282.6 | 281 | -0.6% | -3.39 to +0.199 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.856 | 2.787 | -2.4% | -0.2074 to +0.06927 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 84.66 | 89.21 | +5.4% | +0.7456 to +8.345 | shown, not judged (more or less is not better by itself) |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.905e+08 to +8.905e+08 | WORSE |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | better |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.902e-05 to -5.902e-05 | WORSE |
| organism behind its window (s) | 0.85 | 1.52 | +78.8% | +0.3664 to +0.9736 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
