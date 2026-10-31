# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Source: GitHub Actions workflow `big-organism-detached`, two rented Azure machines (eastus, `Standard_D8as_v4`, 8 vCPUs, 31 GB), each deleted after its collect. **The four stacked at 1,000 copies**: started by run 37564821425 and collected by run 37754612102 (`results/live/raw/run-37754612102/`), three paired repetitions one after another over 29 hours (2026-10-07 03:07 to 2026-10-08 07:41 UTC), commit `126b8941`. **The whole tower at 1,000 copies** (945,000 modelled muscles): started by run 37756284680 and collected by run 37945866426 (`results/live/raw/run-37945866426/`), three paired repetitions one after another over 25.4 hours (2026-10-08 09:29 to 2026-10-09 10:54 UTC), commit `6f0f93e5`. Both on **Omni v3** (`tools/omni_version.py --commit`), both with a 10,800 s window an arm (240 organism steps of 45 s), both arms of every repetition on the clock (the tower 14 to 15 s behind its window, the stack about 22 s: a fifth of one percent or less). Native: the stacks' own controllers and the cluster's HPA alone. Three repetitions give wide intervals on the paired rows; every row is shown.

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss; the key: `docs/HOW_TO_READ_THE_RESULTS.md`). The aim is lower for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). The aim is higher for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The whole tower, every muscle once, 1,000 copies: native | The whole tower, every muscle once, 1,000 copies: omni | The four stacked, duplicates kept, 1,000 copies: native | The four stacked, duplicates kept, 1,000 copies: omni |
|---|---:|---:|---:|---:|
| response time (ms), 95th percentile | 6690 | 160.2 | 2882 | 150 |
| response time (ms), 99th percentile | 9068 | 186.7 | 5405 | 165.2 |
| time over the response line (% of samples) | 76.04 | 0 | 50.99 | 0 |
| failed requests (%) | 4.76 | 0 | 0.1415 | 0 |
| HPA replicas, mean | 9.965 | 9.969 | 9.952 | 9.951 |
| pods started | 4 | 3.667 | 5 | 5 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 2041 | 2036 | 2005 | 1992 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 2041 | 2036 | 2005 | 1992 |
| CPU used with Omni's own (cores), mean | 4.514 | 4.4 | 3.839 | 3.634 |
| host CPU busy, the real machine under kind (%) | 67.63 | 66.84 | 60.66 | 60.06 |
| organism work | 6.658e+13 | 6.658e+13 | 1.293e+14 | 1.293e+14 |
| organism energy (J) | 1.109e+16 | 1.105e+16 | 1.112e+16 | 1.107e+16 |
| organism time over the line (% of steps) | 2.736 | 2.728 | 2.585 | 2.567 |
| organism work per energy | 0.006004 | 0.006025 | 0.01163 | 0.01167 |
| organism behind its window (s) | 14.33 | 13.97 | 21.8 | 22.37 |

## Each organism: omni against native, paired by repetition

### The whole tower, every muscle once, 1,000 copies: toward their aims on 7, away from them on 1 (organism work), inside the noise on 4

3 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 6690 | 160.2 | -97.6% | -6917 to -6143 | GAIN |
| response time (ms), 99th percentile | 9068 | 186.7 | -97.9% | -9321 to -8442 | GAIN |
| time over the response line (% of samples) | 76.04 | 0 | -100.0% | -77.3 to -74.77 | GAIN |
| failed requests (%) | 4.76 | 0 | -100.0% | -5.743 to -3.777 | GAIN |
| HPA replicas, mean | 9.965 | 9.969 | +0.0% | -0.009746 to +0.01694 | STEADY, inside the noise (up) |
| pods started | 4 | 3.667 | -8.3% | -1.768 to +1.101 | STEADY, inside the noise (cut) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.302e-16 to +3.983e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 2041 | 2036 | -0.3% | -13.6 to +2.606 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 2041 | 2036 | -0.3% | -13.6 to +2.606 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 4.514 | 4.4 | -2.5% | -0.2054 to -0.02198 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 67.63 | 66.84 | -1.2% | -1.794 to +0.2158 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 6.658e+13 | 6.658e+13 | -0.0% | -2.402e+08 to -2.402e+08 | LOSS |
| organism energy (J) | 1.109e+16 | 1.105e+16 | -0.4% | -4.016e+13 to -4.016e+13 | GAIN |
| organism time over the line (% of steps) | 2.736 | 2.728 | -0.3% | -0.007569 to -0.007569 | GAIN |
| organism work per energy | 0.006004 | 0.006025 | +0.4% | +2.18e-05 to +2.18e-05 | GAIN |
| organism behind its window (s) | 14.33 | 13.97 | -2.6% | -1.084 to +0.3505 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 1,000 copies: toward their aims on 7, away from them on 1 (organism work), inside the noise on 3

3 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2882 | 150 | -94.8% | -3113 to -2351 | GAIN |
| response time (ms), 99th percentile | 5405 | 165.2 | -96.9% | -5593 to -4887 | GAIN |
| time over the response line (% of samples) | 50.99 | 0 | -100.0% | -55.2 to -46.78 | GAIN |
| failed requests (%) | 0.1415 | 0 | -100.0% | -0.1485 to -0.1345 | GAIN |
| HPA replicas, mean | 9.952 | 9.951 | -0.0% | -0.01433 to +0.01248 | STEADY, inside the noise (cut) |
| pods started | 5 | 5 | +0.0% | +0 to +0 | STEADY, the same |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.318e-15 to +3.095e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 2005 | 1992 | -0.6% | -26.58 to +2.121 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 2005 | 1992 | -0.6% | -26.58 to +2.121 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 3.839 | 3.634 | -5.3% | -0.3784 to -0.03194 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 60.66 | 60.06 | -1.0% | -3.166 to +1.972 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.293e+14 | 1.293e+14 | -0.0% | -7.813e+08 to -7.813e+08 | LOSS |
| organism energy (J) | 1.112e+16 | 1.107e+16 | -0.4% | -4.07e+13 to -4.07e+13 | GAIN |
| organism time over the line (% of steps) | 2.585 | 2.567 | -0.7% | -0.01762 to -0.01762 | GAIN |
| organism work per energy | 0.01163 | 0.01167 | +0.4% | +4.267e-05 to +4.267e-05 | GAIN |
| organism behind its window (s) | 21.8 | 22.37 | +2.6% | -2.226 to +3.359 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
