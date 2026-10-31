# Batch queue: 240 CPU jobs, cruise and the emergency brake: the A/B/C three-run table (Omni v3)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **STEADY, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38013261196 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| B | 38013265986 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| C | 38013269850 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -17.4% (-24.6 to -10.3) | -20.0% (-26.2 to -13.8) | -15.7% (-19.6 to -11.8) | **GAIN in all three of our runs** |
| node-hours | -17.6% (-24.7 to -10.5) | -20.0% (-26.1 to -13.9) | -15.8% (-19.8 to -11.8) | **GAIN in all three of our runs** |
| energy, parked workers still on at idle power (Wh, declared model) | -0.2% (-0.7 to +0.2) | +0.0% (-0.3 to +0.4) | +0.1% (-0.3 to +0.5) | STEADY, no difference beyond the noise (all three runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -12.2% (-17.3 to -7.2) | -13.8% (-17.9 to -9.6) | -10.8% (-13.7 to -7.8) | **GAIN in all three of our runs** |
| response time (ms), mean | -13.1% (-15.3 to -11.0) | -11.2% (-14.9 to -7.5) | -12.6% (-15.3 to -10.0) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -2.4% (-5.3 to +0.5) | +0.2% (-4.7 to +5.1) | -1.9% (-5.0 to +1.2) | STEADY, no difference beyond the noise (all three runs) |
| response time (ms), 99th percentile | -1.9% (-6.4 to +2.6) | +0.3% (-3.0 to +3.5) | -1.4% (-4.4 to +1.5) | STEADY, no difference beyond the noise (all three runs) |
| time over the response line (% of samples) | -4.0% (-6.6 to -1.3) | -3.7% (-5.9 to -1.6) | -3.0% (-7.1 to +1.2) | STEADY, no difference beyond the noise in 1 of 3 runs |
| failed requests (%) | +0.01031 (-0.01301 to +0.03363) | -59.9% (-312.8 to +193.1) | +0 (+0 to +0) | STEADY, no difference beyond the noise (all three runs) |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +1.4% (-2.5 to +5.3) | +1.8% (-1.1 to +4.8) | +1.1% (-3.4 to +5.7) | shown, not judged |
| utilisation (used / allocatable) | +19.5% (+12.7 to +26.3) | +23.9% (+16.0 to +31.8) | +20.2% (+16.6 to +23.7) | shown, not judged |
| CPU used (cores), mean | -0.7% (-5.0 to +3.6) | -0.7% (-3.0 to +1.6) | +1.2% (-1.6 to +4.1) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01807 (+0.01178 to +0.02435) | +0.0182 (+0.01395 to +0.02245) | +0.0186 (+0.01519 to +0.02201) | shown, not judged |
| CPU used with Omni's own (cores), mean | -2.2% (-8.8 to +4.5) | +1.0% (-2.5 to +4.5) | +2.5% (-1.6 to +6.6) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -11.6% (-17.8 to -5.4) | -14.3% (-22.2 to -6.4) | -12.0% (-14.6 to -9.4) | shown, not judged |
| HPA replicas, mean | +5.2% (-10.8 to +21.2) | +5.0% (-7.4 to +17.5) | -7.0% (-21.1 to +7.1) | STEADY, no difference beyond the noise (all three runs) |
| pods started | +0.2 (-0.1016 to +0.5016) | +0.2 (-0.1016 to +0.5016) | -50.0% (-313.9 to +213.9) | STEADY, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | +8.3 (-4.227 to +20.83) | +10.8 (-5.5 to +27.1) | -98.1% (-324.8 to +128.6) | STEADY, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | +8.3 (-4.227 to +20.83) | +10.8 (-5.5 to +27.1) | -96.2% (-323.5 to +131.1) | STEADY, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +1.7% (+1.0 to +2.5) | +1.5% (+0.9 to +2.2) | +1.9% (+0.9 to +2.9) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +0.3% (-0.7 to +1.2) | +0.3% (-0.8 to +1.4) | +0.5% (-0.6 to +1.6) | STEADY, no difference beyond the noise (all three runs) |
| batch: worker machines in service after the queue finished, mean | -27.3% (-36.5 to -18.2) | -32.5% (-40.5 to -24.5) | -25.7% (-31.3 to -20.1) | **GAIN in all three of our runs** |

Readings: 5 better in all three of our runs, 9 no difference beyond the noise, 1 no difference beyond the noise in 1 of 3 runs, 2 same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
