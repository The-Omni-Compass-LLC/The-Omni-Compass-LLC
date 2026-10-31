# All four in one run: more work, faster, fewer machines, less energy (load rising 1 to 8 and back): the A/B/C three-run table (Omni v1)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **STEADY, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 37384945573 | `f162ce8d74e8` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 10 |
| B | 37385646550 | `f162ce8d74e8` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 10 |
| C | 37394444337 | `68d9bd172605` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| work inside the response line (requests a second; the capacity test's own gauge, the aim is higher) | +48.4% (+32.1 to +64.7) | +44.7% (+29.2 to +60.2) | +42.1% (+28.9 to +55.3) | **GAIN in all three of our runs** |
| worker nodes in service, mean | -0.4% (-1.1 to +0.2) | -1.5% (-3.1 to +0.1) | -0.8% (-1.8 to +0.1) | STEADY, no difference beyond the noise (all three runs) |
| node-hours | -0.5% (-1.1 to +0.2) | -1.5% (-3.1 to +0.2) | -0.6% (-1.6 to +0.4) | STEADY, no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.3% (-0.4 to -0.1) | -0.2% (-0.3 to +0.0) | -0.0% (-0.2 to +0.1) | STEADY, no difference beyond the noise in 2 of 3 runs |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.6% (-1.0 to -0.1) | -1.1% (-2.2 to -0.1) | -0.6% (-1.2 to +0.0) | STEADY, no difference beyond the noise in 1 of 3 runs |
| response time (ms), mean | -47.3% (-58.2 to -36.3) | -43.8% (-59.6 to -27.9) | -46.6% (-62.8 to -30.4) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -63.2% (-77.1 to -49.4) | -57.3% (-77.3 to -37.4) | -60.4% (-77.7 to -43.0) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -38.7% (-55.3 to -22.1) | -39.4% (-67.3 to -11.5) | -45.5% (-79.2 to -11.7) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -40.0% (-52.5 to -27.4) | -42.6% (-61.4 to -23.7) | -39.4% (-57.3 to -21.4) | **GAIN in all three of our runs** |
| failed requests (%) | -12.1% (-17.1 to -7.1) | -13.0% (-22.3 to -3.7) | -11.6% (-20.3 to -3.0) | **GAIN in all three of our runs** |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +0.7% (-61.3 to +62.6) | -7.7% (-57.7 to +42.3) | +10.4% (-55.5 to +76.3) | shown, not judged |
| utilisation (used / allocatable) | -1.9% (-2.5 to -1.2) | -0.8% (-2.1 to +0.6) | -1.9% (-2.8 to -1.0) | shown, not judged |
| CPU used (cores), mean | -2.1% (-2.8 to -1.4) | -1.8% (-2.0 to -1.6) | -2.4% (-2.8 to -1.9) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00915 (+0.007784 to +0.01052) | +0.00846 (+0.007037 to +0.009883) | +0.00866 (+0.007273 to +0.01005) | shown, not judged |
| CPU used with Omni's own (cores), mean | -1.8% (-2.5 to -1.0) | -1.4% (-1.6 to -1.2) | -2.0% (-2.4 to -1.6) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +2.1% (+0.4 to +3.8) | +0.5% (-0.6 to +1.6) | +1.7% (+1.0 to +2.4) | shown, not judged |
| HPA replicas, mean | -0.9% (-3.3 to +1.5) | -2.9% (-6.6 to +0.8) | -3.2% (-6.6 to +0.3) | STEADY, no difference beyond the noise (all three runs) |
| pods started | -17.0% (-35.7 to +1.7) | -23.1% (-47.2 to +1.0) | -6.1% (-25.6 to +13.4) | STEADY, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | -7.2% (-42.2 to +27.7) | -37.7% (-62.1 to -13.2) | -17.0% (-43.2 to +9.2) | STEADY, no difference beyond the noise in 2 of 3 runs |
| pod start wait, mean (s) | -2.9% (-27.2 to +21.4) | -33.8% (-55.3 to -12.2) | -14.7% (-33.8 to +4.4) | STEADY, no difference beyond the noise in 2 of 3 runs |
| host CPU busy, the real machine under kind (%) | -1.8% (-2.6 to -1.1) | -1.4% (-1.7 to -1.1) | -1.5% (-2.2 to -0.9) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 6 better in all three of our runs, 4 no difference beyond the noise, 1 no difference beyond the noise in 1 of 3 runs, 3 no difference beyond the noise in 2 of 3 runs, 2 same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
