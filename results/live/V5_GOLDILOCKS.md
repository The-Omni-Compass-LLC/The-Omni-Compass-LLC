# Goldilocks: Omni-Compass on top of a service rightsized with Goldilocks and the VPA's recommender: the A/B/C three-run table (Omni v5)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **STEADY, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38339821941 | `148565d2550d` | omni-v5 (digest 5648f2902f1fae68, 44 files) | 10 |
| B | 38339828150 | `148565d2550d` | omni-v5 (digest 5648f2902f1fae68, 44 files) | 10 |
| C | 38339834658 | `148565d2550d` | omni-v5 (digest 5648f2902f1fae68, 44 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| node-hours | -0.0% (-0.5 to +0.5) | +0.1% (-0.4 to +0.5) | +0.3% (-0.0 to +0.7) | STEADY, no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | +2.1% (+1.6 to +2.6) | +1.9% (+1.3 to +2.5) | +2.6% (+2.2 to +3.0) | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | +2.1% (+1.6 to +2.6) | +1.9% (+1.3 to +2.5) | +2.6% (+2.2 to +3.0) | **power given in all three of our runs** |
| response time (ms), mean | -47.5% (-56.5 to -38.5) | -43.5% (-58.2 to -28.8) | -46.6% (-55.7 to -37.6) | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | -62.1% (-71.6 to -52.5) | -58.6% (-70.3 to -46.8) | -58.6% (-67.5 to -49.7) | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | -69.0% (-80.7 to -57.2) | -68.0% (-82.8 to -53.1) | -67.7% (-76.4 to -59.1) | **GAIN in all three of our runs** |
| time over the response line (% of samples) | -98.7% (-179.7 to -17.7) | -100.0% (-173.0 to -27.0) | -100.0% (-143.6 to -56.4) | **GAIN in all three of our runs** |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +0.08 (-0.01214 to +0.1721) | +0.0% (-337.2 to +337.2) | +0.105 (+0.007976 to +0.202) | shown, not judged |
| utilisation (used / allocatable) | +44.2% (+35.8 to +52.5) | +37.8% (+27.3 to +48.3) | +45.9% (+38.5 to +53.2) | shown, not judged |
| CPU used (cores), mean | +44.2% (+35.8 to +52.5) | +37.8% (+27.3 to +48.3) | +45.9% (+38.5 to +53.2) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00813 (+0.007247 to +0.009013) | +0.00781 (+0.00701 to +0.00861) | +0.00833 (+0.007516 to +0.009144) | shown, not judged |
| CPU used with Omni's own (cores), mean | +45.2% (+36.7 to +53.7) | +38.8% (+28.2 to +49.4) | +46.9% (+39.5 to +54.3) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -28.6% (-32.3 to -24.9) | -25.0% (-29.3 to -20.7) | -29.5% (-33.3 to -25.7) | shown, not judged |
| HPA replicas, mean | +0.7% (-1.6 to +2.9) | +0.8% (+0.3 to +1.3) | +1.2% (-0.5 to +2.9) | STEADY, no difference beyond the noise in 2 of 3 runs |
| pods started | -52.0% (-107.7 to +3.7) | -41.2% (-61.5 to -20.9) | -72.7% (-146.6 to +1.1) | STEADY, no difference beyond the noise in 2 of 3 runs |
| pod start wait, total (s) | -55.6% (-114.8 to +3.7) | -13.6% (-59.7 to +32.5) | -76.5% (-155.9 to +3.0) | STEADY, no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | -46.2% (-94.8 to +2.4) | -21.0% (-104.1 to +62.1) | -57.4% (-131.7 to +16.9) | STEADY, no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +40.4% (+32.4 to +48.5) | +36.0% (+25.9 to +46.2) | +42.8% (+36.2 to +49.3) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 2 WORSE in all three of our runs, 4 better in all three of our runs, 3 no difference beyond the noise, 2 no difference beyond the noise in 2 of 3 runs, 4 same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
