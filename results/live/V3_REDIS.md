# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number (a resource spent that rose reads **power given**, never a loss; the key: `docs/HOW_TO_READ_THE_RESULTS.md`)); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any increase in any run is marked. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 38054731163 | `ca745467845c` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| B | 38054735302 | `ca745467845c` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| C | 38054739168 | `ca745467845c` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,242 | +4.9% (+3.8 to +6.1) | +4.8% (+4.0 to +5.5) | +4.4% (+2.6 to +6.1) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (2 of 3 runs) |
| cache hit rate | 0.79 | 0.829 | +5.0% (+3.8 to +6.1) | +4.8% (+4.0 to +5.5) | +4.4% (+2.6 to +6.1) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.2% (-0.3 to -0.0) | -0.2% (-2.4 to +1.9) | -0.1% (-0.3 to +0.1) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 5.81 | 5.81 | -0.0% (-0.3 to +0.2) | +0.0% (-1.0 to +1.1) | +0.1% (-0.2 to +0.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.35 | 1.13 | -16.0% (-20.1 to -11.9) | -15.9% (-18.7 to -13.1) | -14.0% (-20.1 to -8.0) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 80.4 | +25.7% (+8.4 to +43.0) | +23.3% (+14.2 to +32.4) | +19.2% (+6.8 to +31.5) | **power given in all three of our runs** |
| memory used, mean (MB) | 61.2 | 73.8 | +20.7% (+7.9 to +33.5) | +19.5% (+16.2 to +22.9) | +16.3% (+4.5 to +28.1) | **power given in all three of our runs** |
| keys evicted | 138,054 | 113,055 | -18.1% (-22.7 to -13.5) | -17.2% (-18.9 to -15.6) | -15.9% (-21.7 to -10.0) | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.117 | -7.9% (-32.7 to +16.9) | -12.4% (-29.9 to +5.2) | -8.1% (-32.7 to +16.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 212.6 | 195.2 | -8.2% (-36.6 to +20.2) | -13.4% (-31.6 to +4.7) | -8.6% (-37.0 to +19.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.399 | 0.349 | -12.5% (-41.1 to +16.0) | -17.4% (-34.7 to -0.0) | -12.5% (-39.2 to +14.3) | STEADY, no difference beyond the noise (2 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 41.7 | +41.7 (+21 to +62.4) | +38.7 (+28.6 to +48.7) | +36.7 (+27.9 to +45.4) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 40 to 120 (19 trials, 10 allowed, 1 refused); acting: 56 to 96 (14 trials, 5 allowed, 2 refused); acting: 56 to 112 (18 trials, 7 allowed, 2 refused); run B: acting: 56 to 96 (15 trials, 5 allowed, 3 refused); acting: 48 to 88 (15 trials, 5 allowed, 2 refused); acting: 48 to 120 (18 trials, 9 allowed, 2 refused); run C: acting: 56 to 88 (16 trials, 4 allowed, 3 refused); acting: 48 to 96 (17 trials, 6 allowed, 2 refused); acting: 48 to 96 (17 trials, 6 allowed, 2 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,074 | 1,075 | +0.1% (-0.1 to +0.2) | -0.0% (-0.2 to +0.1) | -0.0% (-0.2 to +0.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.717 | 0.717 | -0.0% (-0.2 to +0.2) | -0.0% (-0.2 to +0.1) | -0.0% (-0.2 to +0.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.0% (-0.0 to +0.0) | -0.0% (-0.6 to +0.6) | +0.0% (-0.1 to +0.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.31 | 5.31 | -0.2% (-1.7 to +1.4) | +0.1% (-0.8 to +1.0) | +0.1% (+0.0 to +0.2) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 1.55 | 1.54 | -0.2% (-1.0 to +0.6) | +0.2% (-1.4 to +1.8) | +0.3% (-0.4 to +0.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 61.3 | -4.3% (-4.5 to -4.1) | -3.4% (-7.4 to +0.7) | -3.2% (-7.2 to +0.8) | STEADY, no difference beyond the noise (2 of 3 runs) |
| memory used, mean (MB) | 57.2 | 55.3 | -3.2% (-3.4 to -3.0) | -2.6% (-5.8 to +0.7) | -2.2% (-5.0 to +0.6) | STEADY, no difference beyond the noise (2 of 3 runs) |
| keys evicted | 71,745 | 71,777 | +0.0% (-0.4 to +0.4) | +0.1% (-0.4 to +0.6) | +0.1% (-0.3 to +0.4) | shown, not judged |
| host CPU busy (share of the run) | 0.0494 | 0.0532 | +7.6% (-198.8 to +214.1) | -5.9% (-22.3 to +10.5) | +8.0% (-34.7 to +50.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 34.4 | 37.4 | +8.8% (-208.8 to +226.4) | -6.7% (-26.1 to +12.7) | +8.7% (-40.8 to +58.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.178 | 0.194 | +8.8% (-208.8 to +226.3) | -6.7% (-26.2 to +12.8) | +8.8% (-40.7 to +58.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 10.0 | +10 (+10 to +10) | +8.67 (+2.93 to +14.4) | +8.67 (+2.93 to +14.4) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); run B: acting: 56 to 64 (4 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 1 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); run C: acting: 56 to 64 (4 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 1 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,268 | 1,342 | +5.9% (-1.7 to +13.5) | +2.6% (+2.2 to +3.0) | +2.9% (+1.8 to +3.9) | STEADY, no difference beyond the noise (1 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, the same |
| cache hit rate | 0.845 | 0.895 | +5.9% (-1.7 to +13.5) | +2.6% (+2.2 to +3.0) | +2.9% (+2.0 to +3.8) | STEADY, no difference beyond the noise (1 of 3 runs) |
| latency, 95th percentile (ms) | 5.74 | 5.72 | -0.4% (-1.2 to +0.5) | -0.2% (-0.3 to -0.1) | -0.6% (-1.6 to +0.3) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 5.81 | 5.81 | -0.1% (-0.5 to +0.4) | -0.0% (-0.2 to +0.2) | -0.9% (-4.5 to +2.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.05 | 0.775 | -26.1% (-60.5 to +8.3) | -11.6% (-13.0 to -10.2) | -13.4% (-20.6 to -6.3) | STEADY, no difference beyond the noise (1 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 73.1 | +14.2% (-8.9 to +37.4) | +3.4% (-3.5 to +10.4) | +2.7% (-0.4 to +5.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| memory used, mean (MB) | 61.3 | 67.6 | +10.3% (-8.8 to +29.4) | +2.2% (-4.8 to +9.2) | +0.9% (-1.6 to +3.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| keys evicted | 103,236 | 70,109 | -32.1% (-74.4 to +10.2) | -13.8% (-16.0 to -11.6) | -15.2% (-20.2 to -10.1) | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.107 | -10.2% (-31.0 to +10.7) | -7.0% (-19.6 to +5.6) | +6.2% (-12.0 to +24.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 198.6 | 177.6 | -10.6% (-32.8 to +11.6) | -7.4% (-21.2 to +6.5) | +8.0% (-14.8 to +30.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.348 | 0.294 | -15.5% (-43.6 to +12.5) | -9.7% (-23.0 to +3.6) | +5.0% (-17.3 to +27.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 45.3 | +45.3 (+25.1 to +65.6) | +28 (+14.9 to +41.1) | +33 (+30.5 to +35.5) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 56 to 104 (17 trials, 6 allowed, 4 refused); acting: 48 to 80 (22 trials, 4 allowed, 1 refused); acting: 48 to 96 (17 trials, 6 allowed, 2 refused); run B: acting: 40 to 72 (18 trials, 4 allowed, 2 refused); acting: 40 to 72 (18 trials, 4 allowed, 2 refused); acting: 64 to 80 (14 trials, 2 allowed, 5 refused); run C: acting: 48 to 80 (18 trials, 4 allowed, 2 refused); acting: 40 to 72 (18 trials, 4 allowed, 2 refused); acting: 40 to 72 (17 trials, 4 allowed, 2 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925.6 | 926.0 | +0.0% (-0.9 to +1.0) | -0.1% (-0.3 to +0.0) | +0.1% (-1.0 to +1.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.617 | 0.618 | +0.0% (-0.9 to +1.0) | -0.1% (-0.3 to -0.0) | +0.1% (-1.0 to +1.2) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.1% (-0.2 to +0.4) | -0.0% (-0.2 to +0.2) | +0.0% (-0.0 to +0.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.74 | 5.76 | +0.3% (-0.1 to +0.7) | +0.1% (-0.2 to +0.4) | +0.2% (+0.0 to +0.4) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 2.26 | 2.27 | +0.1% (-1.6 to +1.9) | +0.2% (-0.4 to +0.8) | -0.0% (-1.7 to +1.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 66.8 | +4.4% (-6.1 to +15.0) | +1.5% (-0.1 to +3.1) | +1.8% (-0.9 to +4.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| memory used, mean (MB) | 60.7 | 62.0 | +2.2% (-8.1 to +12.5) | +0.2% (+0.1 to +0.3) | +0.4% (-0.6 to +1.4) | STEADY, no difference beyond the noise (2 of 3 runs) |
| keys evicted | 243,086 | 245,111 | +0.8% (-0.8 to +2.5) | +0.7% (-1.0 to +2.4) | +0.3% (+0.2 to +0.4) | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.149 | +5.0% (-6.1 to +16.2) | +8.1% (-17.0 to +33.1) | -8.7% (-30.4 to +13.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 236.8 | 250.2 | +5.6% (-7.0 to +18.3) | +9.4% (-19.7 to +38.6) | -10.1% (-34.9 to +14.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.569 | 0.6 | +5.6% (-6.5 to +17.6) | +9.6% (-19.7 to +38.8) | -10.2% (-35.6 to +15.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 23.0 | +23 (+18 to +28) | +22.7 (+18.9 to +26.5) | +22 (+17.7 to +26.3) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 56 to 72 (13 trials, 2 allowed, 1 refused); acting: 56 to 88 (15 trials, 4 allowed, 0 refused); acting: 56 to 80 (15 trials, 3 allowed, 1 refused); run B: acting: 56 to 88 (15 trials, 4 allowed, 0 refused); acting: 56 to 72 (12 trials, 2 allowed, 1 refused); acting: 56 to 80 (13 trials, 3 allowed, 0 refused); run C: acting: 64 to 88 (13 trials, 3 allowed, 1 refused); acting: 56 to 80 (12 trials, 3 allowed, 0 refused); acting: 56 to 80 (14 trials, 3 allowed, 0 refused).

**Across 3 untouched workloads: 0 gauge-rows GAIN, 0 LOSS, 0 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 36 STEADY, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
