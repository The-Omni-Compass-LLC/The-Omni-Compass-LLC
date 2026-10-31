# Steady load: the same fixed-rate work sent to both arms: the A/B/C three-run table (Omni v1)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **STEADY, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 37384939815 | `f162ce8d74e8` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 10 |
| B | 37385640601 | `f162ce8d74e8` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 10 |
| C | 37391296025 | `029340abf30c` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -1.9% (-2.0 to -1.9) | -1.5% (-2.1 to -0.9) | -3.4% (-6.3 to -0.5) | **GAIN in all three of our runs** |
| node-hours | -2.0% (-2.2 to -1.8) | -1.2% (-1.7 to -0.6) | -3.6% (-6.5 to -0.8) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | -0.3% (-0.5 to -0.0) | +0.1% (-0.2 to +0.5) | -0.5% (-0.9 to +0.0) | STEADY, no difference beyond the noise in 2 of 3 runs |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -1.7% (-1.9 to -1.4) | -1.0% (-1.3 to -0.6) | -2.9% (-4.9 to -0.9) | **GAIN in all three of our runs** |
| response time (ms), mean | -50.7% (-62.4 to -39.0) | -47.1% (-63.3 to -30.9) | -48.1% (-62.5 to -33.8) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -68.6% (-85.6 to -51.7) | -66.1% (-86.6 to -45.6) | -65.4% (-85.1 to -45.7) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -73.1% (-91.1 to -55.1) | -70.7% (-94.5 to -46.8) | -70.9% (-91.8 to -50.0) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -98.2% (-144.8 to -51.7) | -99.3% (-177.8 to -20.7) | -98.5% (-172.5 to -24.6) | **GAIN in all three of our runs** |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -14.2% (-75.6 to +47.3) | +10.4% (-38.8 to +59.6) | -53.0% (-99.1 to -6.9) | shown, not judged |
| utilisation (used / allocatable) | -2.9% (-4.8 to -1.0) | -2.6% (-5.5 to +0.3) | -2.2% (-5.3 to +0.9) | shown, not judged |
| CPU used (cores), mean | -4.8% (-6.8 to -2.8) | -4.0% (-7.1 to -1.0) | -5.5% (-7.8 to -3.1) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01063 (+0.009951 to +0.01131) | +0.00915 (+0.007819 to +0.01048) | +0.00972 (+0.008208 to +0.01123) | shown, not judged |
| CPU used with Omni's own (cores), mean | -3.8% (-5.7 to -1.8) | -3.0% (-5.9 to -0.0) | -4.4% (-6.6 to -2.2) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +3.0% (+1.0 to +5.0) | +1.8% (-0.5 to +4.0) | +2.1% (-0.3 to +4.5) | shown, not judged |
| HPA replicas, mean | -1.2% (-4.3 to +1.8) | -4.8% (-7.2 to -2.4) | -3.5% (-10.7 to +3.6) | STEADY, no difference beyond the noise in 2 of 3 runs |
| pods started | -23.7% (-52.4 to +5.0) | +7.0% (-6.7 to +20.7) | -30.0% (-56.3 to -3.7) | STEADY, no difference beyond the noise in 2 of 3 runs |
| pod start wait, total (s) | -22.6% (-73.5 to +28.2) | +8.1% (-20.6 to +36.8) | -52.2% (-102.2 to -2.1) | STEADY, no difference beyond the noise in 2 of 3 runs |
| pod start wait, mean (s) | -13.9% (-48.1 to +20.3) | +7.3% (-18.7 to +33.3) | -31.4% (-65.7 to +3.0) | STEADY, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | -3.1% (-4.8 to -1.3) | -2.1% (-4.3 to +0.1) | -3.5% (-5.5 to -1.6) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 7 better in all three of our runs, 1 no difference beyond the noise, 4 no difference beyond the noise in 2 of 3 runs, 3 same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
