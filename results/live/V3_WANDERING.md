# Wandering demand: load that steps up and down by one (1 2 3 2 3 4 5 6 5 4 5 6 7 8 7 6 5 4 3 4 3 2 1 2 1): the A/B/C three-run table (Omni v3)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **STEADY, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38013208955 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| B | 38013212780 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| C | 38013217100 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -2.5% (-6.1 to +1.1) | -1.7% (-5.2 to +1.8) | -1.2% (-4.1 to +1.6) | STEADY, no difference beyond the noise (all three runs) |
| node-hours | -2.5% (-6.1 to +1.2) | -1.8% (-5.4 to +1.8) | -1.1% (-4.0 to +1.7) | STEADY, no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.3% (-0.5 to -0.1) | -0.4% (-0.7 to -0.2) | -0.1% (-0.2 to -0.0) | **GAIN in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -1.9% (-4.3 to +0.4) | -1.5% (-4.0 to +0.9) | -0.9% (-2.7 to +0.9) | STEADY, no difference beyond the noise (all three runs) |
| response time (ms), mean | -49.8% (-64.3 to -35.2) | -45.6% (-55.9 to -35.4) | -45.3% (-58.1 to -32.5) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -63.9% (-78.7 to -49.0) | -56.5% (-64.9 to -48.0) | -62.3% (-79.7 to -44.9) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -48.7% (-79.1 to -18.3) | -46.0% (-85.9 to -6.2) | -22.3% (-56.1 to +11.6) | STEADY, no difference beyond the noise in 1 of 3 runs |
| time over the response line (% of samples) | -41.6% (-56.0 to -27.2) | -37.4% (-45.9 to -28.8) | -36.4% (-45.3 to -27.6) | **GAIN in all three of our runs** |
| failed requests (%) | -11.5% (-19.4 to -3.6) | -13.3% (-18.8 to -7.8) | -12.0% (-17.7 to -6.3) | **GAIN in all three of our runs** |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -21.2% (-97.2 to +54.8) | +56.9% (-74.2 to +188.1) | -34.7% (-76.2 to +6.8) | shown, not judged |
| utilisation (used / allocatable) | -1.1% (-3.7 to +1.5) | -1.4% (-2.3 to -0.5) | -1.5% (-3.4 to +0.4) | shown, not judged |
| CPU used (cores), mean | -2.7% (-3.5 to -1.8) | -2.3% (-3.6 to -1.0) | -2.2% (-2.8 to -1.6) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00899 (+0.00782 to +0.01016) | +0.009567 (+0.008442 to +0.01069) | +0.00943 (+0.008467 to +0.01039) | shown, not judged |
| CPU used with Omni's own (cores), mean | -2.3% (-3.1 to -1.5) | -2.0% (-3.5 to -0.6) | -1.8% (-2.4 to -1.2) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +0.1% (-3.2 to +3.3) | +1.5% (+0.9 to +2.2) | +0.4% (-2.7 to +3.6) | shown, not judged |
| HPA replicas, mean | -1.2% (-3.0 to +0.7) | -0.2% (-2.4 to +2.1) | -0.6% (-1.9 to +0.6) | STEADY, no difference beyond the noise (all three runs) |
| pods started | -14.3% (-42.7 to +14.1) | -43.9% (-70.9 to -16.9) | -10.5% (-41.5 to +20.5) | STEADY, no difference beyond the noise in 2 of 3 runs |
| pod start wait, total (s) | -1.3% (-43.3 to +40.6) | -40.2% (-73.0 to -7.3) | -20.7% (-70.1 to +28.6) | STEADY, no difference beyond the noise in 2 of 3 runs |
| pod start wait, mean (s) | -2.8% (-29.8 to +24.3) | -25.0% (-58.4 to +8.4) | -14.5% (-44.7 to +15.7) | STEADY, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | -1.8% (-2.6 to -1.0) | -1.9% (-3.0 to -0.7) | -1.5% (-2.2 to -0.9) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 5 better in all three of our runs, 5 no difference beyond the noise, 1 no difference beyond the noise in 1 of 3 runs, 2 no difference beyond the noise in 2 of 3 runs, 2 same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
