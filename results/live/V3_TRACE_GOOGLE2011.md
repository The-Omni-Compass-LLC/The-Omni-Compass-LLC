# A public day of demand: the Google cluster trace of 2011 replayed one step at a time (2 3 3 3 3 4 4 3 2 2 2 2 2 3 2 3 4 4 3 4 5 6 5 4): the A/B/C three-run table (Omni v3)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **STEADY, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38013274685 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| B | 38013279107 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| C | 38013283518 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -7.3% (-13.2 to -1.4) | -7.5% (-13.8 to -1.1) | -9.2% (-14.8 to -3.7) | **GAIN in all three of our runs** |
| node-hours | -7.4% (-13.1 to -1.6) | -7.4% (-13.9 to -0.9) | -9.2% (-14.7 to -3.7) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | -0.4% (-0.7 to -0.2) | -0.3% (-0.5 to -0.1) | -0.4% (-0.7 to -0.0) | **GAIN in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -5.4% (-9.2 to -1.6) | -5.3% (-9.6 to -1.0) | -6.7% (-10.3 to -3.1) | **GAIN in all three of our runs** |
| response time (ms), mean | -52.7% (-67.1 to -38.3) | -51.4% (-67.6 to -35.2) | -51.8% (-78.2 to -25.4) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -65.1% (-80.6 to -49.5) | -64.1% (-82.8 to -45.4) | -66.5% (-96.4 to -36.5) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -61.6% (-79.4 to -43.9) | -60.1% (-78.0 to -42.2) | -61.4% (-90.9 to -31.9) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -82.2% (-121.5 to -42.8) | -81.4% (-122.8 to -40.0) | -81.2% (-143.1 to -19.3) | **GAIN in all three of our runs** |
| failed requests (%) | -15.1% (-30.1 to -0.1) | -17.8% (-32.2 to -3.5) | -11.4% (-22.7 to -0.1) | **GAIN in all three of our runs** |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +17.9% (-67.4 to +103.2) | +14.3% (-53.0 to +81.7) | +2.8% (-33.2 to +38.8) | shown, not judged |
| utilisation (used / allocatable) | +2.6% (-3.1 to +8.3) | +2.4% (-3.1 to +8.0) | +2.6% (-3.7 to +9.0) | shown, not judged |
| CPU used (cores), mean | -4.2% (-5.2 to -3.1) | -3.9% (-5.1 to -2.8) | -5.2% (-8.2 to -2.3) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00987 (+0.009063 to +0.01068) | +0.00966 (+0.008609 to +0.01071) | +0.00913 (+0.007257 to +0.011) | shown, not judged |
| CPU used with Omni's own (cores), mean | -3.6% (-4.7 to -2.6) | -3.4% (-4.5 to -2.3) | -4.7% (-7.5 to -1.8) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -2.3% (-7.1 to +2.6) | -3.4% (-10.0 to +3.3) | -4.1% (-9.6 to +1.5) | shown, not judged |
| HPA replicas, mean | -3.8% (-5.4 to -2.3) | -4.5% (-7.0 to -2.1) | -8.3% (-13.4 to -3.2) | **GAIN in all three of our runs** |
| pods started | +40.4% (+15.7 to +65.0) | +42.3% (+15.7 to +68.9) | +11.8% (-10.5 to +34.2) | STEADY, no difference beyond the noise in 1 of 3 runs |
| pod start wait, total (s) | +11.0% (-34.1 to +56.2) | +20.8% (-41.1 to +82.7) | +0.4% (-24.6 to +25.3) | STEADY, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | -21.8% (-46.8 to +3.2) | -20.1% (-60.9 to +20.6) | -16.4% (-46.1 to +13.2) | STEADY, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | -2.9% (-4.1 to -1.7) | -2.6% (-3.7 to -1.5) | -3.2% (-6.0 to -0.5) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 10 better in all three of our runs, 2 no difference beyond the noise, 1 no difference beyond the noise in 1 of 3 runs, 2 same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
