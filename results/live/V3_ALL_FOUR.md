# All four in one run: more work, faster, fewer machines, less energy (load rising 1 to 8 and back): the A/B/C three-run table (Omni v3)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **STEADY, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38013221512 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| B | 38013226173 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| C | 38013230522 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| work inside the response line (requests a second; the capacity test's own gauge, the aim is higher) | +53.6% (+35.5 to +71.6) | +55.6% (+36.8 to +74.3) | +67.9% (+53.4 to +82.4) | **GAIN in all three of our runs** |
| worker nodes in service, mean | -0.2% (-0.8 to +0.3) | -0.2% (-0.7 to +0.3) | -0.4% (-1.0 to +0.2) | STEADY, no difference beyond the noise (all three runs) |
| node-hours | -0.3% (-0.9 to +0.3) | -0.2% (-0.7 to +0.2) | -0.3% (-1.0 to +0.5) | STEADY, no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.3% (-0.4 to -0.2) | -0.3% (-0.5 to -0.1) | -0.1% (-0.4 to +0.1) | STEADY, no difference beyond the noise in 1 of 3 runs |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.5% (-0.9 to -0.1) | -0.4% (-0.6 to -0.2) | -0.4% (-1.0 to +0.2) | STEADY, no difference beyond the noise in 1 of 3 runs |
| response time (ms), mean | -48.4% (-58.2 to -38.5) | -43.0% (-52.8 to -33.2) | -47.0% (-55.3 to -38.7) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -61.9% (-75.7 to -48.0) | -57.4% (-71.2 to -43.6) | -62.5% (-74.2 to -50.7) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -48.3% (-69.3 to -27.3) | -33.1% (-56.6 to -9.5) | -40.0% (-80.1 to +0.1) | STEADY, no difference beyond the noise in 1 of 3 runs |
| time over the response line (% of samples) | -38.1% (-47.4 to -28.7) | -38.6% (-48.3 to -29.0) | -40.6% (-50.4 to -30.9) | **GAIN in all three of our runs** |
| failed requests (%) | -13.6% (-19.1 to -8.0) | -13.8% (-19.2 to -8.4) | -11.0% (-16.8 to -5.1) | **GAIN in all three of our runs** |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -10.1% (-106.5 to +86.3) | -5.9% (-48.2 to +36.5) | +20.2% (-56.4 to +96.9) | shown, not judged |
| utilisation (used / allocatable) | -1.8% (-2.2 to -1.3) | -1.8% (-2.9 to -0.7) | -1.8% (-2.6 to -1.0) | shown, not judged |
| CPU used (cores), mean | -1.9% (-2.3 to -1.6) | -1.9% (-2.7 to -1.1) | -2.1% (-2.8 to -1.5) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00931 (+0.00826 to +0.01036) | +0.009211 (+0.008043 to +0.01038) | +0.00906 (+0.008085 to +0.01004) | shown, not judged |
| CPU used with Omni's own (cores), mean | -1.6% (-1.9 to -1.2) | -1.5% (-2.4 to -0.7) | -1.8% (-2.5 to -1.1) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +1.7% (+1.2 to +2.1) | +1.0% (-0.7 to +2.8) | +2.2% (+0.4 to +3.9) | shown, not judged |
| HPA replicas, mean | -0.0% (-1.4 to +1.4) | -0.9% (-2.7 to +0.9) | -0.9% (-2.7 to +0.9) | STEADY, no difference beyond the noise (all three runs) |
| pods started | -21.3% (-45.1 to +2.5) | -13.0% (-32.7 to +6.6) | -12.0% (-27.4 to +3.4) | STEADY, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | -29.8% (-88.0 to +28.4) | -21.8% (-64.2 to +20.6) | -11.2% (-49.3 to +26.9) | STEADY, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | -17.9% (-62.3 to +26.5) | -15.7% (-51.0 to +19.5) | -5.1% (-34.1 to +23.8) | STEADY, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | -1.4% (-1.6 to -1.1) | -1.2% (-2.0 to -0.4) | -1.8% (-2.4 to -1.2) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 5 better in all three of our runs, 6 no difference beyond the noise, 3 no difference beyond the noise in 1 of 3 runs, 2 same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
