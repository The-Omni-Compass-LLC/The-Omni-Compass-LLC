# The capacity test, native and Omni-Compass on top at the same resource cap: the A/B/C three-run table (Omni v21)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Three separate GitHub runs of the same preregistered test on the same engine: A is the result, B and C are the replications. The cap is a quota on the served app's CPU, the same in both arms and enforced by the cluster; the load rises step by step past what the cap can serve. Each cell is omni against native at one cap, the paired change with its 95% interval (completed work in percent of native; capacity in requests a second). Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three runs move the same way and every interval is clear of zero; completed work and capacity are work done, so more is GAIN and less is LOSS. **STEADY, no difference beyond the noise**: in the runs counted, the interval includes zero; that is the result. **The runs disagree**: runs clear of the noise point different ways. Every row is shown, LOSS included. Evidence class **L** (the real thing: a real Kubernetes cluster, real requests, every answer counted).

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

| Run | GitHub run | Label | Commit | Engine | Pairs per cap |
|---|---|---|---|---|---:|
| A | 40222187614 | A | `f0c1c431231c` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |
| B | 40245495359 | B | `22138ecd5b5a` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |
| C | 40267236639 | C | `b659f0eebc58` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |

| Cap (cores) | Measure | A | B | C | Reading |
|---:|---|---|---|---|---|
| 1 | completed work (requests answered within the line over the window) | +11.2% (−7.0 to +29.4) | −5.4% (−13.9 to +3.2) | −16.5% (−59.4 to +26.4) | **the runs disagree** |
| 1 | work inside the response line (requests a second; the capacity test's own gauge) | +0.00 req/s (-1.76 to +1.76) | +0.40 req/s (-0.71 to +1.51) | -1.20 req/s (-3.42 to +1.02) | **the runs disagree** |
| 1.5 | completed work (requests answered within the line over the window) | −1.9% (−9.4 to +5.6) | +1.3% (−2.1 to +4.8) | −5.7% (−12.6 to +1.2) | **the runs disagree** |
| 1.5 | work inside the response line (requests a second; the capacity test's own gauge) | -0.40 req/s (-1.51 to +0.71) | -0.40 req/s (-1.51 to +0.71) | +0.40 req/s (-0.71 to +1.51) | **the runs disagree** |
| 2 | completed work (requests answered within the line over the window) | −0.2% (−4.1 to +3.6) | +0.8% (−3.1 to +4.7) | −0.9% (−3.1 to +1.2) | **the runs disagree** |
| 2 | work inside the response line (requests a second; the capacity test's own gauge) | +0.00 req/s (+0.00 to +0.00) | +0.00 req/s (+0.00 to +0.00) | +0.00 req/s (+0.00 to +0.00) | STEADY, the same |
| 3 | completed work (requests answered within the line over the window) | −0.6% (−1.4 to +0.2) | −1.1% (−3.6 to +1.4) | −0.2% (−0.7 to +0.4) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| 3 | work inside the response line (requests a second; the capacity test's own gauge) | -0.80 req/s (-2.16 to +0.56) | -0.40 req/s (-1.51 to +0.71) | +0.80 req/s (-0.56 to +2.16) | **the runs disagree** |

Readings: 1 LOSS by the mean of our three runs, 1 STEADY, the same, 6 the runs disagree.

How to read it: where the cap holds native back, a higher count for Omni-Compass on top at the same cap is more work from the same capacity, a GAIN; where neither arm can do more under the cap, the rows read STEADY, no difference beyond the noise, and that is the result. Each run's own table, with its audit lines and what each step up in the cap gives each arm: `CAPACITY.md` in its archived folder.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
