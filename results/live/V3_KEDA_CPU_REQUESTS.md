# Kubernetes with KEDA on the CPU target and the live requests in flight: Omni-Compass on top: the A/B/C three-run table (Omni v3)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **STEADY, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38096663118 | `175cc0feda00` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 9 |
| B | 38099655092 | `85b150889152` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| C | 38099656930 | `85b150889152` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -0.6% (-1.2 to +0.1) | -0.6% (-1.2 to +0.1) | -0.7% (-1.4 to -0.1) | STEADY, no difference beyond the noise in 2 of 3 runs |
| node-hours | -0.8% (-1.3 to -0.3) | -0.4% (-1.3 to +0.5) | -0.9% (-1.4 to -0.5) | STEADY, no difference beyond the noise in 1 of 3 runs |
| energy, parked workers still on at idle power (Wh, declared model) | +1.4% (+1.0 to +1.8) | +1.6% (+0.9 to +2.4) | +1.0% (+0.2 to +1.8) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +1.0% (+0.4 to +1.7) | +1.2% (+0.1 to +2.3) | +0.5% (-0.3 to +1.4) | STEADY, no difference beyond the noise in 1 of 3 runs |
| response time (ms), mean | -38.5% (-47.3 to -29.7) | -35.8% (-49.1 to -22.5) | -36.2% (-51.2 to -21.1) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -53.4% (-62.6 to -44.3) | -50.8% (-62.3 to -39.4) | -52.9% (-66.2 to -39.7) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -62.3% (-69.9 to -54.7) | -60.3% (-73.0 to -47.5) | -60.0% (-73.1 to -46.9) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -97.2% (-159.4 to -35.0) | -100.0% (-172.1 to -27.9) | -100.0% (-173.6 to -26.4) | **GAIN in all three of our runs** |
| failed requests (%) | -0.6% (-345.5 to +344.2) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, no difference beyond the noise (all three runs) |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +141.1% (-70.0 to +352.2) | +27.3% (-180.3 to +235.0) | -76.2% (-125.3 to -27.1) | shown, not judged |
| utilisation (used / allocatable) | +32.7% (+24.8 to +40.7) | +28.2% (+20.6 to +35.8) | +25.2% (+15.6 to +34.9) | shown, not judged |
| CPU used (cores), mean | +32.0% (+23.6 to +40.5) | +27.6% (+19.4 to +35.7) | +24.4% (+14.5 to +34.3) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01499 (+0.0133 to +0.01668) | +0.01517 (+0.01309 to +0.01725) | +0.01432 (+0.01217 to +0.01647) | shown, not judged |
| CPU used with Omni's own (cores), mean | +33.7% (+25.2 to +42.3) | +29.3% (+20.9 to +37.7) | +26.0% (+15.9 to +36.2) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -22.5% (-26.7 to -18.2) | -19.8% (-23.2 to -16.3) | -17.6% (-22.5 to -12.7) | shown, not judged |
| HPA replicas, mean | +3.1% (+0.9 to +5.2) | +1.3% (-1.9 to +4.4) | +0.3% (-2.9 to +3.6) | STEADY, no difference beyond the noise in 2 of 3 runs |
| pods started | +0.0% (-16.1 to +16.1) | +4.3% (-13.0 to +21.5) | +4.1% (-2.1 to +10.2) | STEADY, no difference beyond the noise (all three runs) |
| pod start wait, total (s) | -13.6% (-48.1 to +20.9) | +21.6% (-36.1 to +79.2) | +14.5% (-1.0 to +30.0) | STEADY, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | -17.0% (-41.8 to +7.7) | +12.3% (-31.7 to +56.3) | +10.8% (-6.1 to +27.7) | STEADY, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +31.2% (+24.3 to +38.1) | +28.3% (+20.2 to +36.5) | +23.9% (+14.9 to +33.0) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 1 WORSE in all three of our runs, 4 better in all three of our runs, 4 no difference beyond the noise, 2 no difference beyond the noise in 1 of 3 runs, 2 no difference beyond the noise in 2 of 3 runs, 2 same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
