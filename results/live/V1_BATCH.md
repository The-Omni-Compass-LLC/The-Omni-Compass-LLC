# Batch queue: 240 CPU jobs, cruise and the emergency brake: the A/B/C three-run table (Omni v1)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **STEADY, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 37385637932 | `f162ce8d74e8` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 10 |
| B | 37385654462 | `f162ce8d74e8` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 10 |
| C | 37394452486 | `68d9bd172605` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -23.3% (-28.7 to -18.0) | -23.9% (-30.8 to -17.0) | -15.0% (-18.7 to -11.3) | **GAIN in all three of our runs** |
| node-hours | -23.5% (-28.8 to -18.2) | -23.9% (-30.8 to -17.0) | -15.3% (-19.0 to -11.6) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | -0.1% (-0.4 to +0.3) | -0.0% (-0.4 to +0.4) | -0.3% (-0.6 to +0.0) | STEADY, no difference beyond the noise (all three runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -16.2% (-19.9 to -12.6) | -16.6% (-21.5 to -11.8) | -10.6% (-13.1 to -8.0) | **GAIN in all three of our runs** |
| response time (ms), mean | -12.8% (-15.5 to -10.0) | -10.6% (-14.7 to -6.5) | -11.1% (-13.4 to -8.7) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -1.2% (-7.1 to +4.6) | +0.6% (-5.4 to +6.6) | +0.3% (-2.9 to +3.6) | STEADY, no difference beyond the noise (all three runs) |
| response time (ms), 99th percentile | +1.4% (-4.5 to +7.2) | +0.4% (-6.7 to +7.5) | +2.5% (-1.2 to +6.1) | STEADY, no difference beyond the noise (all three runs) |
| time over the response line (% of samples) | -3.9% (-7.9 to +0.0) | -3.4% (-6.8 to +0.1) | -3.5% (-5.5 to -1.5) | STEADY, no difference beyond the noise in 2 of 3 runs |
| failed requests (%) | +0 (+0 to +0) | -100.0% (-326.2 to +126.2) | -100.0% (-326.2 to +126.2) | STEADY, no difference beyond the noise (all three runs) |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +2.6% (-0.5 to +5.7) | +1.4% (-1.5 to +4.3) | +1.9% (-0.9 to +4.8) | shown, not judged |
| utilisation (used / allocatable) | +28.3% (+22.4 to +34.2) | +29.2% (+20.2 to +38.3) | +18.1% (+13.4 to +22.9) | shown, not judged |
| CPU used (cores), mean | -1.2% (-2.2 to -0.1) | -1.6% (-3.5 to +0.3) | +0.3% (-1.7 to +2.3) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01914 (+0.01619 to +0.02209) | +0.01743 (+0.01501 to +0.01985) | +0.02258 (+0.01955 to +0.02561) | shown, not judged |
| CPU used with Omni's own (cores), mean | +0.2% (-0.9 to +1.2) | -0.3% (-2.2 to +1.7) | +1.8% (-0.4 to +3.9) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -15.9% (-22.4 to -9.4) | -16.0% (-22.2 to -9.9) | -10.7% (-14.0 to -7.4) | shown, not judged |
| HPA replicas, mean | +3.4% (-10.6 to +17.3) | +1.7% (-11.0 to +14.4) | +11.0% (-2.1 to +24.1) | STEADY, no difference beyond the noise (all three runs) |
| pods started | +0.3 (-0.1828 to +0.7828) | +0.0% (-337.2 to +337.2) | +0.2 (-0.1016 to +0.5016) | STEADY, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | +10.7 (-6.481 to +27.88) | -39.0% (-316.7 to +238.7) | +9.7 (-5.006 to +24.41) | STEADY, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | +7.15 (-3.633 to +17.93) | -39.0% (-316.7 to +238.7) | +9.7 (-5.006 to +24.41) | STEADY, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +2.2% (+1.4 to +2.9) | +1.9% (+0.9 to +2.9) | +2.1% (+1.3 to +2.9) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +0.9% (+0.3 to +1.5) | +0.8% (-0.3 to +1.8) | +0.7% (+0.0 to +1.4) | STEADY, no difference beyond the noise in 1 of 3 runs |
| batch: worker machines in service after the queue finished, mean | -36.4% (-42.4 to -30.4) | -36.2% (-45.1 to -27.4) | -25.8% (-31.6 to -20.0) | **GAIN in all three of our runs** |

Readings: 5 better in all three of our runs, 8 no difference beyond the noise, 1 no difference beyond the noise in 1 of 3 runs, 1 no difference beyond the noise in 2 of 3 runs, 2 same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
