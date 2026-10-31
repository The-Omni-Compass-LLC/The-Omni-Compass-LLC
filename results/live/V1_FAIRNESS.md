# Fairness: a noisy neighbour on the same workers: the A/B/C three-run table (Omni v1)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **STEADY, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 37384948340 | `f162ce8d74e8` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 10 |
| B | 37385649261 | `f162ce8d74e8` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 10 |
| C | 37391303438 | `029340abf30c` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, the same |
| node-hours | -0.1% (-0.5 to +0.2) | +0.1% (-0.2 to +0.4) | -0.0% (-0.6 to +0.6) | STEADY, no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | +0.0% (-0.5 to +0.5) | -0.0% (-0.3 to +0.2) | -0.1% (-0.6 to +0.5) | STEADY, no difference beyond the noise (all three runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +0.0% (-0.5 to +0.5) | -0.0% (-0.3 to +0.2) | -0.1% (-0.6 to +0.5) | STEADY, no difference beyond the noise (all three runs) |
| response time (ms), mean | -8.1% (-23.3 to +7.2) | -9.1% (-23.1 to +5.0) | -4.6% (-12.0 to +2.8) | STEADY, no difference beyond the noise (all three runs) |
| response time (ms), 95th percentile | +4.1% (-28.1 to +36.3) | -3.3% (-24.9 to +18.2) | +7.0% (-10.3 to +24.4) | STEADY, no difference beyond the noise (all three runs) |
| response time (ms), 99th percentile | +5.0% (-15.7 to +25.8) | +13.8% (-8.9 to +36.5) | -1.6% (-15.2 to +12.0) | STEADY, no difference beyond the noise (all three runs) |
| time over the response line (% of samples) | -4.9% (-13.9 to +4.0) | -6.0% (-13.4 to +1.5) | -6.1% (-10.2 to -1.9) | STEADY, no difference beyond the noise in 2 of 3 runs |
| failed requests (%) | +2.8% (-29.8 to +35.4) | -6.5% (-49.4 to +36.4) | -18.4% (-38.6 to +1.8) | STEADY, no difference beyond the noise (all three runs) |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +14.5% (-37.2 to +66.2) | +5.2% (-55.9 to +66.4) | +35.4% (-39.6 to +110.3) | shown, not judged |
| utilisation (used / allocatable) | +1.2% (-0.6 to +3.1) | -1.2% (-2.5 to +0.2) | -0.9% (-1.5 to -0.2) | shown, not judged |
| CPU used (cores), mean | +1.2% (-0.6 to +3.1) | -1.2% (-2.5 to +0.2) | -0.9% (-1.5 to -0.2) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01343 (+0.01071 to +0.01615) | +0.01333 (+0.01093 to +0.01573) | +0.01521 (+0.01308 to +0.01734) | shown, not judged |
| CPU used with Omni's own (cores), mean | +1.8% (+0.1 to +3.6) | -0.6% (-2.0 to +0.8) | -0.2% (-0.9 to +0.5) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -1.6% (-3.6 to +0.3) | +1.0% (-0.4 to +2.4) | +0.8% (+0.2 to +1.5) | shown, not judged |
| HPA replicas, mean | -0.7% (-2.0 to +0.6) | -0.7% (-3.3 to +2.0) | +0.7% (-1.3 to +2.8) | STEADY, no difference beyond the noise (all three runs) |
| pods started | +10.0% (-12.6 to +32.6) | -11.6% (-50.2 to +27.0) | -20.0% (-37.5 to -2.5) | STEADY, no difference beyond the noise in 2 of 3 runs |
| pod start wait, total (s) | +15.4% (-19.1 to +49.9) | +5.8% (-59.6 to +71.2) | -1.1% (-30.2 to +28.0) | STEADY, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | +6.3% (-24.0 to +36.7) | +9.0% (-45.2 to +63.2) | +23.8% (-3.3 to +50.9) | STEADY, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +1.1% (-0.1 to +2.2) | -0.2% (-1.5 to +1.1) | -0.4% (-1.1 to +0.2) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| second app: response time (ms), 95th percentile | +3.9% (-5.6 to +13.3) | +6.3% (-12.8 to +25.4) | -3.2% (-10.8 to +4.5) | STEADY, no difference beyond the noise (all three runs) |
| second app: response time (ms), 99th percentile | +51.0% (-60.6 to +162.6) | +14.6% (-39.6 to +68.9) | -26.5% (-73.2 to +20.3) | STEADY, no difference beyond the noise (all three runs) |
| second app: time over the response line (% of samples) | +1.7% (-1.3 to +4.6) | +0.6% (-5.8 to +7.0) | -3.7% (-6.9 to -0.5) | STEADY, no difference beyond the noise in 2 of 3 runs |
| second app: failed requests (%) | +2.7% (-0.4 to +5.9) | +0.2% (-4.3 to +4.7) | -1.2% (-4.8 to +2.4) | STEADY, no difference beyond the noise (all three runs) |

Readings: 13 no difference beyond the noise, 3 no difference beyond the noise in 2 of 3 runs, 3 same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
