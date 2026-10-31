# Fairness: a noisy neighbour on the same workers: the A/B/C three-run table (Omni v3)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **STEADY, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38013235441 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| B | 38013239864 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| C | 38013244591 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, the same |
| node-hours | -0.0% (-0.2 to +0.1) | -0.1% (-0.6 to +0.4) | -0.2% (-0.5 to +0.2) | STEADY, no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.1% (-0.3 to +0.1) | -0.1% (-0.6 to +0.4) | -0.2% (-0.5 to +0.2) | STEADY, no difference beyond the noise (all three runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.1% (-0.3 to +0.1) | -0.1% (-0.6 to +0.4) | -0.2% (-0.5 to +0.2) | STEADY, no difference beyond the noise (all three runs) |
| response time (ms), mean | -4.1% (-10.7 to +2.6) | -5.4% (-13.8 to +2.9) | -3.8% (-12.2 to +4.7) | STEADY, no difference beyond the noise (all three runs) |
| response time (ms), 95th percentile | +17.9% (+3.7 to +32.1) | +6.8% (-12.1 to +25.6) | +8.1% (-9.1 to +25.3) | STEADY, no difference beyond the noise in 2 of 3 runs |
| response time (ms), 99th percentile | +8.2% (-7.3 to +23.7) | +8.9% (-6.0 to +23.8) | +6.7% (-14.5 to +27.9) | STEADY, no difference beyond the noise (all three runs) |
| time over the response line (% of samples) | -4.2% (-12.5 to +4.1) | -5.5% (-12.1 to +1.0) | -2.9% (-6.6 to +0.9) | STEADY, no difference beyond the noise (all three runs) |
| failed requests (%) | -5.3% (-17.9 to +7.4) | -16.2% (-30.7 to -1.8) | -29.5% (-51.3 to -7.7) | STEADY, no difference beyond the noise in 1 of 3 runs |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -21.7% (-85.0 to +41.6) | +96.6% (-11.3 to +204.4) | +43.3% (+6.2 to +80.4) | shown, not judged |
| utilisation (used / allocatable) | -0.6% (-1.4 to +0.2) | -0.9% (-1.6 to -0.2) | -0.1% (-1.1 to +0.9) | shown, not judged |
| CPU used (cores), mean | -0.6% (-1.4 to +0.2) | -0.9% (-1.6 to -0.2) | -0.1% (-1.1 to +0.9) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01376 (+0.01158 to +0.01594) | +0.0142 (+0.01175 to +0.01665) | +0.01438 (+0.01232 to +0.01644) | shown, not judged |
| CPU used with Omni's own (cores), mean | -0.0% (-0.8 to +0.8) | -0.3% (-1.0 to +0.4) | +0.5% (-0.4 to +1.5) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +0.7% (-0.5 to +1.9) | +1.0% (+0.1 to +1.9) | -0.1% (-1.3 to +1.0) | shown, not judged |
| HPA replicas, mean | +0.5% (-1.8 to +2.8) | +0.2% (-2.0 to +2.3) | +0.5% (-1.2 to +2.3) | STEADY, no difference beyond the noise (all three runs) |
| pods started | -10.9% (-41.3 to +19.6) | -15.4% (-40.1 to +9.4) | -13.0% (-40.7 to +14.6) | STEADY, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | +17.0% (-38.9 to +73.0) | +8.8% (-41.1 to +58.7) | +2.3% (-46.5 to +51.1) | STEADY, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | +15.4% (-29.4 to +60.2) | +3.5% (-29.3 to +36.2) | +16.2% (-17.0 to +49.3) | STEADY, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +1.0% (+0.2 to +1.8) | +0.0% (-0.6 to +0.7) | +0.4% (-0.2 to +1.1) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| second app: response time (ms), 95th percentile | -7.3% (-25.7 to +11.1) | +6.3% (-5.0 to +17.7) | -1.3% (-21.0 to +18.5) | STEADY, no difference beyond the noise (all three runs) |
| second app: response time (ms), 99th percentile | -25.2% (-74.5 to +24.0) | -28.7% (-80.8 to +23.5) | -16.7% (-53.6 to +20.3) | STEADY, no difference beyond the noise (all three runs) |
| second app: time over the response line (% of samples) | -3.6% (-7.4 to +0.1) | -1.2% (-3.4 to +1.1) | +0.5% (-4.5 to +5.6) | STEADY, no difference beyond the noise (all three runs) |
| second app: failed requests (%) | +1.8% (-3.5 to +7.1) | -0.7% (-3.9 to +2.6) | +3.9% (-0.2 to +8.1) | STEADY, no difference beyond the noise (all three runs) |

Readings: 14 no difference beyond the noise, 1 no difference beyond the noise in 1 of 3 runs, 1 no difference beyond the noise in 2 of 3 runs, 3 same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
