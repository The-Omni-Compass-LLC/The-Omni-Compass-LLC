# Kubernetes with KEDA's HTTP add-on on the live requests in flight: Omni-Compass on top: the A/B/C three-run table (Omni v6)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **STEADY, no difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, LOSS included.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 38701101796 | `9a499b137e78` | omni-v6 (digest df6147466ef18046, 45 files) | 10 |
| B | 38712444594 | `afbac134f8a1` | omni-v6 (digest df6147466ef18046, 45 files) | 10 |
| C | 38725705826 | `63f29c3e20a5` | omni-v6 (digest df6147466ef18046, 45 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | 6 → 6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 6 → 6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 6 → 6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| node-hours | 1.517 → 1.512; raw −0.4% (95%: −0.8% to +0.1%); STEADY | 1.52 → 1.511; raw −0.6% (95%: −0.9% to −0.3%); GAIN | 1.52 → 1.511; raw −0.6% (95%: −0.8% to −0.4%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 → 161.3; raw +2.1% (95%: +1.5% to +2.7%); power given | 158.3 → 161; raw +1.7% (95%: +1.0% to +2.4%); power given | 158 → 160.5; raw +1.6% (95%: +1.0% to +2.3%); power given | **power given in all three of our runs** |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 → 161.3; raw +2.1% (95%: +1.5% to +2.7%); power given | 158.3 → 161; raw +1.7% (95%: +1.0% to +2.4%); power given | 158 → 160.5; raw +1.6% (95%: +1.0% to +2.3%); power given | **power given in all three of our runs** |
| response time (ms), mean | 204.3 → 83.71; raw −59.0% (95%: −68.8% to −49.3%); GAIN | 198.5 → 81.9; raw −58.7% (95%: −71.0% to −46.5%); GAIN | 181.9 → 73.63; raw −59.5% (95%: −74.3% to −44.8%); GAIN | **GAIN in all three of our runs** |
| response time (ms), 95th percentile | 493.4 → 125.4; raw −74.6% (95%: −85.5% to −63.7%); GAIN | 474.8 → 128.8; raw −72.9% (95%: −85.3% to −60.5%); GAIN | 455.4 → 114.6; raw −74.8% (95%: −92.2% to −57.5%); GAIN | **GAIN in all three of our runs** |
| response time (ms), 99th percentile | 653.3 → 207; raw −68.3% (95%: −78.3% to −58.4%); GAIN | 640.7 → 190.9; raw −70.2% (95%: −82.0% to −58.4%); GAIN | 608.7 → 158.2; raw −74.0% (95%: −90.9% to −57.1%); GAIN | **GAIN in all three of our runs** |
| time over the response line (% of samples) | 5.151 → 0.158; raw −96.9% (95%: −141.2% to −52.6%); GAIN | 4.676 → 0.1215; raw −97.4% (95%: −144.0% to −50.8%); GAIN | 4.071 → 0.03615; raw −99.1% (95%: −171.5% to −26.7%); GAIN | **GAIN in all three of our runs** |
| failed requests (%) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 → 0.1; raw −98.1% (95%: −142.7% to −53.4%); GAIN | 5 → 0.1; raw −98.0% (95%: −149.1% to −46.9%); GAIN | 3.5 → 0; raw −100.0% (95%: −168.3% to −31.7%); GAIN | **GAIN in all three of our runs** |
| settings commands the governor wrote on its own (no person touched either arm) | +4.3 (+3.954 to +4.646) | +4.3 (+3.954 to +4.646) | +4.7 (+3.579 to +5.821) | shown, not judged |
| pods with no machine to take them (unschedulable) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| time pods had no machine to take them, pod-minutes | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -12.6% (-100.8 to +75.7) | +11.6% (-66.1 to +89.3) | +11.8% (-33.3 to +56.8) | shown, not judged |
| utilisation (used / allocatable) | +55.4% (+47.6 to +63.3) | +51.3% (+41.7 to +60.9) | +52.5% (+41.6 to +63.3) | shown, not judged |
| CPU used (cores), mean | +55.4% (+47.6 to +63.3) | +51.3% (+41.7 to +60.9) | +52.5% (+41.6 to +63.3) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00915 (+0.008066 to +0.01023) | +0.00945 (+0.008233 to +0.01067) | +0.00886 (+0.007459 to +0.01026) | shown, not judged |
| CPU used with Omni's own (cores), mean | +56.7% (+48.7 to +64.6) | +52.6% (+42.8 to +62.3) | +53.7% (+42.6 to +64.8) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -33.6% (-36.5 to -30.8) | -31.6% (-33.8 to -29.3) | -32.1% (-35.2 to -29.1) | shown, not judged |
| HPA replicas, mean | 2.886 → 2.439; raw −15.5% (95%: −22.7% to −8.3%); GAIN | 2.925 → 2.411; raw −17.6% (95%: −23.5% to −11.6%); GAIN | 2.722 → 2.419; raw −11.1% (95%: −17.4% to −4.8%); GAIN | **GAIN in all three of our runs** |
| pods started | 2.7 → 2.3; raw −14.8% (95%: −33.3% to +3.7%); GAIN | 2.9 → 2.3; raw −20.7% (95%: −33.4% to −8.0%); GAIN | 2.6 → 2.3; raw −11.5% (95%: −24.8% to +1.8%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pod start wait, total (s) | 24.1 → 23.2; raw −3.7% (95%: −30.8% to +23.3%); GAIN | 23.8 → 21.2; raw −10.9% (95%: −33.1% to +11.2%); GAIN | 20.9 → 22.8; raw +9.1% (95%: −14.1% to +32.3%); LOSS | **the runs disagree** |
| pod start wait, mean (s) | 8.783 → 9.883; raw +12.5% (95%: +2.3% to +22.7%); LOSS | 8.167 → 9.15; raw +12.0% (95%: −5.1% to +29.2%); LOSS | 7.867 → 9.65; raw +22.7% (95%: +7.9% to +37.4%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU busy, the real machine under kind (%) | +49.1% (+41.4 to +56.9) | +47.1% (+38.2 to +55.9) | +47.6% (+38.4 to +56.9) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 2 GAIN by the mean of our three runs, 6 GAIN in all three of our runs, 1 LOSS by the mean of our three runs, 4 STEADY, the same, 2 power given in all three of our runs, 9 shown, not judged, 1 the runs disagree.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
