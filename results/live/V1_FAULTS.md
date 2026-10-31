# Faults: a machine down, a spike, a runaway pod, a blind probe: the A/B/C three-run table (Omni v1)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **STEADY, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 37384951397 | `f162ce8d74e8` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 10 |
| B | 37385651747 | `f162ce8d74e8` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 10 |
| C | 37391310157 | `029340abf30c` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +0.0% (-0.1 to +0.2) | +0.0% (-0.0 to +0.1) | -0.2% (-0.6 to +0.2) | STEADY, no difference beyond the noise (all three runs) |
| node-hours | +0.1% (-0.5 to +0.6) | -0.2% (-0.7 to +0.2) | +0.4% (-0.3 to +1.0) | STEADY, no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.2% (-0.7 to +0.4) | -0.3% (-0.7 to +0.2) | +0.3% (-0.3 to +0.8) | STEADY, no difference beyond the noise (all three runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.1% (-0.7 to +0.4) | -0.2% (-0.7 to +0.2) | +0.2% (-0.4 to +0.7) | STEADY, no difference beyond the noise (all three runs) |
| response time (ms), mean | -38.2% (-60.2 to -16.1) | -36.4% (-53.9 to -18.8) | -52.2% (-70.8 to -33.7) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -63.9% (-74.0 to -53.9) | -63.1% (-76.8 to -49.4) | -61.0% (-69.7 to -52.3) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -7.5% (-86.0 to +70.9) | -64.3% (-122.3 to -6.3) | -63.9% (-120.6 to -7.1) | STEADY, no difference beyond the noise in 1 of 3 runs |
| time over the response line (% of samples) | -18.8% (-26.6 to -11.0) | -28.6% (-40.4 to -16.7) | -44.8% (-56.5 to -33.0) | **GAIN in all three of our runs** |
| failed requests (%) | -5.6% (-14.3 to +3.1) | -4.4% (-20.5 to +11.7) | -17.0% (-29.7 to -4.2) | STEADY, no difference beyond the noise in 2 of 3 runs |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -14.7% (-91.4 to +62.0) | +18.1% (-84.5 to +120.7) | -1.0% (-77.4 to +75.3) | shown, not judged |
| utilisation (used / allocatable) | -1.7% (-3.4 to -0.1) | -0.3% (-2.4 to +1.7) | -2.9% (-4.7 to -1.1) | shown, not judged |
| CPU used (cores), mean | -1.7% (-3.3 to -0.1) | -0.3% (-2.3 to +1.8) | -3.0% (-4.8 to -1.2) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00881 (+0.007966 to +0.009654) | +0.00887 (+0.007728 to +0.01001) | +0.00844 (+0.007293 to +0.009587) | shown, not judged |
| CPU used with Omni's own (cores), mean | -1.2% (-2.7 to +0.4) | +0.3% (-1.8 to +2.3) | -2.4% (-4.2 to -0.7) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +1.1% (-0.9 to +3.1) | +0.0% (-1.7 to +1.8) | +2.2% (+1.0 to +3.4) | shown, not judged |
| HPA replicas, mean | +0.9% (-2.9 to +4.6) | +1.3% (-2.9 to +5.5) | +1.9% (-1.3 to +5.1) | STEADY, no difference beyond the noise (all three runs) |
| pods started | -13.0% (-48.4 to +22.3) | -10.6% (-45.2 to +24.0) | -16.3% (-40.9 to +8.3) | STEADY, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | -12.7% (-80.1 to +54.7) | -27.6% (-132.6 to +77.4) | +10.9% (-92.1 to +113.8) | STEADY, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | -5.5% (-56.6 to +45.6) | -27.7% (-130.5 to +75.1) | +5.3% (-82.8 to +93.4) | STEADY, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | -1.5% (-2.4 to -0.5) | +0.6% (-0.5 to +1.7) | -2.3% (-4.5 to -0.2) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 3 better in all three of our runs, 8 no difference beyond the noise, 1 no difference beyond the noise in 1 of 3 runs, 1 no difference beyond the noise in 2 of 3 runs, 2 same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
