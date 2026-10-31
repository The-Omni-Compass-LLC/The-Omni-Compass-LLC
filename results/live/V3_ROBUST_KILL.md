# Robustness: the governor killed outright mid-run (the lease), real Kubernetes, 10 pairs: the A/B/C three-run table (Omni v3)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **STEADY, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38013447217 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| B | 38013451990 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| C | 38013456955 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| node-hours | +0.0% (-0.3 to +0.4) | -0.1% (-0.3 to +0.2) | +0.0% (-0.4 to +0.5) | STEADY, no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.2% (-0.7 to +0.3) | -0.3% (-0.6 to -0.0) | -0.2% (-0.5 to +0.2) | STEADY, no difference beyond the noise in 2 of 3 runs |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.2% (-0.7 to +0.3) | -0.3% (-0.6 to -0.0) | -0.2% (-0.5 to +0.2) | STEADY, no difference beyond the noise in 2 of 3 runs |
| response time (ms), mean | -39.2% (-59.6 to -18.9) | -33.3% (-51.8 to -14.8) | -39.5% (-57.1 to -21.9) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -48.3% (-90.3 to -6.4) | -26.5% (-50.5 to -2.6) | -41.8% (-62.0 to -21.6) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -16.2% (-61.8 to +29.5) | -8.4% (-47.3 to +30.5) | -16.7% (-50.7 to +17.2) | STEADY, no difference beyond the noise (all three runs) |
| time over the response line (% of samples) | -36.0% (-50.8 to -21.3) | -35.6% (-52.5 to -18.8) | -32.4% (-46.0 to -18.8) | **GAIN in all three of our runs** |
| failed requests (%) | -9.4% (-23.2 to +4.4) | -14.3% (-26.1 to -2.5) | -8.6% (-16.1 to -1.0) | STEADY, no difference beyond the noise in 1 of 3 runs |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +19.1% (-113.4 to +151.6) | +20.9% (-153.8 to +195.6) | -31.8% (-103.2 to +39.6) | shown, not judged |
| utilisation (used / allocatable) | -1.7% (-2.7 to -0.7) | -2.1% (-2.9 to -1.4) | -1.4% (-2.7 to -0.0) | shown, not judged |
| CPU used (cores), mean | -1.7% (-2.7 to -0.7) | -2.1% (-2.9 to -1.4) | -1.4% (-2.7 to -0.0) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01241 (+0.01147 to +0.01335) | +0.01315 (+0.01194 to +0.01436) | +0.01324 (+0.01217 to +0.01431) | shown, not judged |
| CPU used with Omni's own (cores), mean | -1.2% (-2.2 to -0.2) | -1.6% (-2.3 to -0.9) | -0.8% (-2.2 to +0.5) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +1.5% (+0.0 to +3.0) | +2.3% (+0.8 to +3.8) | +0.5% (-1.1 to +2.1) | shown, not judged |
| HPA replicas, mean | +0.8% (-0.1 to +1.7) | +0.7% (-0.5 to +1.8) | +1.9% (+0.9 to +2.9) | STEADY, no difference beyond the noise in 2 of 3 runs |
| pods started | -16.0% (-34.8 to +2.8) | -14.0% (-36.4 to +8.4) | -32.1% (-59.8 to -4.3) | STEADY, no difference beyond the noise in 2 of 3 runs |
| pod start wait, total (s) | -19.7% (-50.6 to +11.2) | -26.7% (-66.0 to +12.6) | -31.3% (-75.6 to +13.0) | STEADY, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | -5.7% (-36.7 to +25.2) | -16.4% (-52.3 to +19.4) | -34.5% (-69.4 to +0.3) | STEADY, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | -1.0% (-2.2 to +0.1) | -0.7% (-1.6 to +0.1) | -0.2% (-1.3 to +1.0) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| robust: failed requests in the 120 s after the kill (%) | +0.7% (-18.2 to +19.6) | -5.5% (-24.0 to +12.9) | -0.9% (-16.6 to +14.8) | STEADY, no difference beyond the noise (all three runs) |
| robust: time over the line in the 120 s after the kill (% of samples) | -1.0% (-8.4 to +6.3) | -3.0% (-9.4 to +3.4) | -1.8% (-8.5 to +5.0) | STEADY, no difference beyond the noise (all three runs) |
| robust: every setting back at the operator's within 60 s of the kill, every repetition (the governor killed outright; the watchdog's hand-back) | yes (10 reps; mean 9 s, max 10 s) | yes (10 reps; mean 9 s, max 10 s) | yes (10 reps; mean 9 s, max 11 s) | **handed back within the allowance in every repetition, in all three of our runs** |
| robust: a second governor started after the hand-back and governed to the end, every repetition | yes | yes | yes | **the same in all three of our runs** |

Readings: 3 better in all three of our runs, 1 handed back within the allowance in every repetition, in all three of our runs, 6 no difference beyond the noise, 1 no difference beyond the noise in 1 of 3 runs, 4 no difference beyond the noise in 2 of 3 runs, 3 same, 8 shown, not judged, 1 the same in all three of our runs.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
