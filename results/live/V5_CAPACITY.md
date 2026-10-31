# The capacity test, native and Omni-Compass on top at the same resource cap: the A/B/C three-run table (Omni v5)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three separate GitHub runs of the same preregistered test on the same engine: A is the result, B and C are the replications. The cap is a quota on the served app's CPU, the same in both arms and enforced by the cluster; the load rises step by step past what the cap can serve. Each cell is omni against native at one cap, the paired change with its 95% interval: native's value → Omni-Compass's, the raw change with its true sign, then the run's own word. Completed work and capacity are work done, so more is GAIN and less is LOSS. Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **STEADY, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Every row is shown, LOSS included. Evidence class **L** (the real thing: a real Kubernetes cluster, real requests, every answer counted).

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Label | Commit | Engine | Pairs per cap |
|---|---|---|---|---|---:|
| A | 38339841468 | A | `148565d2550d` | omni-v5 (digest 5648f2902f1fae68, 44 files) | 5 |
| B | 38339847249 | B | `148565d2550d` | omni-v5 (digest 5648f2902f1fae68, 44 files) | 5 |
| C | 38339853176 | C | `148565d2550d` | omni-v5 (digest 5648f2902f1fae68, 44 files) | 5 |

| Cap (cores) | Measure | A | B | C | Reading |
|---:|---|---|---|---|---|
| 1 | completed work (requests answered within the line over the window; the aim is higher) | 2063 → 2121; raw +2.8% (95%: −9.3% to +14.9%); GAIN | 3628 → 3623; raw −0.1% (95%: −5.3% to +5.0%); STEADY | 2440 → 2331; raw −4.4% (95%: −11.0% to +2.1%); LOSS | **the runs disagree** |
| 1 | work inside the response line (requests a second; the capacity test's own gauge, the aim is higher) | 4 → 4; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 6 → 6.4; raw +6.7% (95%: −11.8% to +25.2%); GAIN | 4.8 → 4.4; raw −8.3% (95%: −31.5% to +14.8%); LOSS | **the runs disagree** |
| 1.5 | completed work (requests answered within the line over the window; the aim is higher) | 6417 → 6118; raw −4.7% (95%: −10.1% to +0.8%); LOSS | 6895 → 6712; raw −2.7% (95%: −9.2% to +3.9%); LOSS | 7472 → 7303; raw −2.3% (95%: −10.2% to +5.7%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| 1.5 | work inside the response line (requests a second; the capacity test's own gauge, the aim is higher) | 8.8 → 8.4; raw −4.5% (95%: −28.2% to +19.1%); LOSS | 9.2 → 8.8; raw −4.3% (95%: −26.9% to +18.2%); LOSS | 9.2 → 10; raw +8.7% (95%: −15.4% to +32.8%); GAIN | **the runs disagree** |
| 2 | completed work (requests answered within the line over the window; the aim is higher) | 9857 → 9621; raw −2.4% (95%: −9.2% to +4.4%); LOSS | 9281 → 9117; raw −1.8% (95%: −3.4% to −0.1%); LOSS | 1.048e+04 → 1.067e+04; raw +1.9% (95%: −2.2% to +5.9%); GAIN | **the runs disagree** |
| 2 | work inside the response line (requests a second; the capacity test's own gauge, the aim is higher) | 12.8 → 12.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 11.2 → 11.6; raw +3.6% (95%: −6.3% to +13.5%); GAIN | 13.6 → 14; raw +2.9% (95%: −5.2% to +11.1%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| 3 | completed work (requests answered within the line over the window; the aim is higher) | 1.147e+04 → 1.141e+04; raw −0.5% (95%: −2.6% to +1.5%); LOSS | 1.181e+04 → 1.187e+04; raw +0.6% (95%: −2.0% to +3.1%); GAIN | 1.23e+04 → 1.21e+04; raw −1.6% (95%: −4.3% to +1.1%); LOSS | **the runs disagree** |
| 3 | work inside the response line (requests a second; the capacity test's own gauge, the aim is higher) | 13.2 → 12.4; raw −6.1% (95%: −16.4% to +4.2%); LOSS | 13.2 → 13.6; raw +3.0% (95%: −5.4% to +11.4%); GAIN | 14.4 → 14; raw −2.8% (95%: −10.5% to +4.9%); LOSS | **the runs disagree** |

Readings: 1 GAIN by the mean of our three runs, 1 LOSS by the mean of our three runs, 6 the runs disagree.

How to read it: where the cap holds native back, a higher count for Omni-Compass on top at the same cap is more work from the same capacity; where neither arm can do more under the cap, the rows show no difference beyond the noise, and that is the result. Each run's own table, with its audit lines and what each step up in the cap gives each arm: `CAPACITY.md` in its archived folder.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
