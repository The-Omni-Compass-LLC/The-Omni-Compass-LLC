# Goldilocks: Omni-Compass on top of a service rightsized with Goldilocks and the VPA's recommender: the A/B/C three-run table (Omni v6)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **STEADY, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38697567716 | `9a499b137e78` | omni-v6 (digest df6147466ef18046, 45 files) | 10 |
| B | 38708517967 | `afbac134f8a1` | omni-v6 (digest df6147466ef18046, 45 files) | 10 |
| C | 38721995611 | `63f29c3e20a5` | omni-v6 (digest df6147466ef18046, 45 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | 6 → 6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 6 → 6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 6 → 6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| node-hours | 1.514 → 1.519; raw +0.3% (95%: ±0.0% to +0.7%); STEADY | 1.517 → 1.514; raw −0.2% (95%: −0.7% to +0.4%); STEADY | 1.515 → 1.517; raw +0.2% (95%: −0.3% to +0.6%); STEADY | STEADY, under the floor (the three runs' mean 0.11%) |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 → 162.4; raw +2.7% (95%: +2.2% to +3.2%); power given | 158.2 → 161; raw +1.8% (95%: +1.2% to +2.4%); power given | 158.1 → 161.9; raw +2.4% (95%: +1.7% to +3.0%); power given | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 → 162.4; raw +2.7% (95%: +2.2% to +3.2%); power given | 158.2 → 161; raw +1.8% (95%: +1.2% to +2.4%); power given | 158.1 → 161.9; raw +2.4% (95%: +1.7% to +3.0%); power given | **power given in all three of our runs** |
| response time (ms), mean | 166.9 → 90.21; raw −46.0% (95%: −52.1% to −39.9%); GAIN | 138.7 → 76.47; raw −44.9% (95%: −57.6% to −32.1%); GAIN | 157.5 → 84.08; raw −46.6% (95%: −55.6% to −37.6%); GAIN | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | 340.7 → 143.3; raw −57.9% (95%: −65.0% to −50.9%); GAIN | 294.9 → 118.6; raw −59.8% (95%: −71.6% to −48.0%); GAIN | 331 → 128.2; raw −61.3% (95%: −70.6% to −51.9%); GAIN | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | 483.1 → 167.9; raw −65.2% (95%: −72.7% to −57.8%); GAIN | 437.8 → 135.3; raw −69.1% (95%: −81.2% to −57.0%); GAIN | 474.3 → 154.5; raw −67.4% (95%: −76.5% to −58.3%); GAIN | **GAIN in all three of our runs** |
| time over the response line (% of samples) | 0.9107 → 0.01212; raw −98.7% (95%: −138.5% to −58.8%), −0.8985 in the gauge's unit; GAIN | 0.8175 → 0; raw −100.0% (95%: −170.2% to −29.8%), −0.8175 in the gauge's unit; GAIN | 1.041 → 0; raw −100.0% (95%: −151.2% to −48.8%); GAIN | **GAIN in all three of our runs** |
| failed requests (%) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.6 → 0; raw −100.0% (95%: −200.5% to +0.5%), −0.6000 in the gauge's unit; GAIN | 1 → 0; raw −100.0% (95%: −201.2% to +1.2%); GAIN | 0.7 → 0; raw −100.0% (95%: −196.9% to −3.1%), −0.7000 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| settings commands the governor wrote on its own (no person touched either arm) | +15.1 (+13.33 to +16.87) | +16.4 (+13.44 to +19.36) | +16 (+13.64 to +18.36) | shown, not judged |
| pods with no machine to take them (unschedulable) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| time pods had no machine to take them, pod-minutes | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +0.08 (-0.01214 to +0.1721) | +33.3% (-42.1 to +108.7) | +200.0% (-101.6 to +501.6) | shown, not judged |
| utilisation (used / allocatable) | +47.9% (+43.5 to +52.2) | +40.6% (+31.7 to +49.4) | +44.6% (+37.0 to +52.3) | shown, not judged |
| CPU used (cores), mean | +47.9% (+43.5 to +52.2) | +40.6% (+31.7 to +49.4) | +44.6% (+37.0 to +52.3) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00854 (+0.007949 to +0.009131) | +0.00792 (+0.00717 to +0.00867) | +0.00816 (+0.007314 to +0.009006) | shown, not judged |
| CPU used with Omni's own (cores), mean | +48.9% (+44.5 to +53.3) | +41.6% (+32.6 to +50.5) | +45.6% (+37.9 to +53.4) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -30.8% (-33.8 to -27.8) | -26.7% (-30.0 to -23.4) | -28.8% (-32.2 to -25.3) | shown, not judged |
| HPA replicas, mean | 9.826 → 9.938; raw +1.1% (95%: −0.3% to +2.5%); power given | 9.77 → 9.799; raw +0.3% (95%: −2.1% to +2.6%); STEADY | 9.8 → 9.86; raw +0.6% (95%: −1.4% to +2.6%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pods started | 2.1 → 0.7; raw −66.7% (95%: −120.4% to −12.9%); GAIN | 1.9 → 1.1; raw −42.1% (95%: −108.0% to +23.8%); GAIN | 2 → 1.1; raw −45.0% (95%: −119.4% to +29.4%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pod start wait, total (s) | 2.8 → 1.2; raw −57.1% (95%: −113.9% to −0.4%); GAIN | 2.9 → 1.7; raw −41.4% (95%: −113.8% to +31.0%); GAIN | 3.1 → 1.8; raw −41.9% (95%: −133.6% to +49.8%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pod start wait, mean (s) | 1.083 → 0.85; raw −21.5% (95%: −90.6% to +47.5%); GAIN | 1.392 → 0.7333; raw −47.3% (95%: −107.5% to +12.9%); GAIN | 1.35 → 0.8; raw −40.7% (95%: −112.6% to +31.2%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy, the real machine under kind (%) | +44.2% (+40.8 to +47.7) | +37.3% (+29.7 to +44.9) | +41.1% (+34.0 to +48.2) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 4 GAIN by the mean of our three runs, 4 GAIN in all three of our runs, 4 STEADY, the same, 1 STEADY, under the floor, 1 power given by the mean of our three runs, 2 power given in all three of our runs, 9 shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
