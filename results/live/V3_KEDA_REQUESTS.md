# Kubernetes with KEDA's HTTP add-on on the live requests in flight: Omni-Compass on top: the A/B/C three-run table (Omni v3)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **STEADY, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38096663118 | `175cc0feda00` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| B | 38099655092 | `85b150889152` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| C | 38099656930 | `85b150889152` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -7.8% (-11.4 to -4.1) | -5.9% (-9.7 to -2.1) | -7.6% (-11.4 to -3.8) | **GAIN in all three of our runs** |
| node-hours | -8.2% (-11.8 to -4.7) | -5.8% (-9.7 to -1.9) | -8.2% (-12.0 to -4.4) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | +1.4% (+0.5 to +2.3) | +2.6% (+2.2 to +3.0) | +1.7% (+1.1 to +2.3) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -4.2% (-6.9 to -1.5) | -1.6% (-4.4 to +1.1) | -3.7% (-6.8 to -0.7) | STEADY, no difference beyond the noise in 1 of 3 runs |
| response time (ms), mean | -59.0% (-73.7 to -44.4) | -58.7% (-65.0 to -52.4) | -59.3% (-71.9 to -46.7) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -75.9% (-89.0 to -62.8) | -72.6% (-79.8 to -65.5) | -73.2% (-86.6 to -59.9) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -72.1% (-81.3 to -62.9) | -70.6% (-77.6 to -63.7) | -69.9% (-83.5 to -56.2) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -96.3% (-185.3 to -7.3) | -97.0% (-131.5 to -62.4) | -96.3% (-145.8 to -46.8) | **GAIN in all three of our runs** |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0.01227 (-0.01548 to +0.04002) | STEADY, no difference beyond the noise (all three runs) |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -11.9% (-85.7 to +62.0) | +19.5% (-42.5 to +81.4) | -4.4% (-71.2 to +62.4) | shown, not judged |
| utilisation (used / allocatable) | +58.0% (+47.1 to +68.8) | +64.5% (+55.3 to +73.7) | +64.3% (+55.1 to +73.5) | shown, not judged |
| CPU used (cores), mean | +45.3% (+35.7 to +54.9) | +54.4% (+49.2 to +59.5) | +52.0% (+42.6 to +61.4) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00912 (+0.008026 to +0.01021) | +0.01235 (+0.0112 to +0.0135) | +0.01096 (+0.009652 to +0.01227) | shown, not judged |
| CPU used with Omni's own (cores), mean | +46.6% (+37.0 to +56.3) | +56.0% (+50.8 to +61.1) | +53.5% (+44.0 to +63.0) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -33.2% (-35.6 to -30.8) | -36.2% (-39.3 to -33.1) | -35.7% (-37.9 to -33.6) | shown, not judged |
| HPA replicas, mean | -14.4% (-23.9 to -4.9) | -13.7% (-23.4 to -4.0) | -14.5% (-19.3 to -9.6) | **GAIN in all three of our runs** |
| pods started | -12.0% (-31.3 to +7.3) | -13.8% (-34.6 to +7.0) | -14.3% (-32.1 to +3.6) | STEADY, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | -6.2% (-29.4 to +16.9) | -4.7% (-29.5 to +20.0) | -4.3% (-22.4 to +13.8) | STEADY, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | +6.3% (-8.4 to +21.0) | +11.7% (-1.0 to +24.5) | +11.8% (-0.5 to +24.0) | STEADY, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +41.6% (+34.6 to +48.7) | +50.2% (+45.3 to +55.1) | +48.8% (+40.1 to +57.5) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 1 WORSE in all three of our runs, 7 better in all three of our runs, 4 no difference beyond the noise, 1 no difference beyond the noise in 1 of 3 runs, 2 same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
