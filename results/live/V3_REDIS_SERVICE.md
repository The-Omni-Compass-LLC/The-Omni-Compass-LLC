# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number (a resource spent that rose reads **power given**, never a loss; the key: `docs/HOW_TO_READ_THE_RESULTS.md`)); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any increase in any run is marked. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 38054791688 | `ca745467845c` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| B | 38054795871 | `ca745467845c` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| C | 38054800068 | `ca745467845c` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,248 | +5.4% (+3.7 to +7.2) | +5.9% (+5.1 to +6.7) | +5.9% (+5.0 to +6.8) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.789 | 0.832 | +5.4% (+3.7 to +7.2) | +5.9% (+5.0 to +6.7) | +5.9% (+5.0 to +6.8) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.2% (-0.3 to -0.0) | -0.6% (-1.0 to -0.2) | -0.1% (-0.1 to -0.0) | **GAIN in all three of our runs** |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.0% (-0.2 to +0.2) | -0.2% (-0.5 to +0.1) | -0.0% (-0.1 to +0.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.35 | 1.11 | -17.6% (-22.9 to -12.4) | -20.0% (-23.1 to -16.9) | -21.0% (-23.9 to -18.0) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 82.7 | +29.2% (+3.1 to +55.3) | +33.9% (+27.0 to +40.8) | +34.5% (+26.2 to +42.8) | **power given in all three of our runs** |
| memory used, mean (MB) | 61.2 | 75.7 | +23.7% (+6.0 to +41.4) | +28.8% (+22.0 to +35.6) | +30.1% (+20.1 to +40.0) | **power given in all three of our runs** |
| keys evicted | 138,098 | 110,491 | -20.0% (-27.5 to -12.5) | -21.9% (-25.1 to -18.8) | -22.1% (-25.9 to -18.2) | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.114 | -6.2% (-26.8 to +14.4) | +10.3% (+0.5 to +20.1) | +24.3% (-55.4 to +104.0) | STEADY, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 203.6 | 191.2 | -6.1% (-29.9 to +17.7) | +12.1% (+2.0 to +22.2) | +25.8% (-57.4 to +109.0) | STEADY, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.382 | 0.34 | -10.9% (-33.2 to +11.3) | +5.9% (-5.2 to +17.0) | +18.7% (-61.0 to +98.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 46.0 | +46 (+17.3 to +74.7) | +54.3 (+48.1 to +60.6) | +38.7 (+22.9 to +54.4) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 56 to 136 (18 trials, 10 allowed, 1 refused); acting: 56 to 96 (14 trials, 5 allowed, 2 refused); acting: 48 to 104 (20 trials, 7 allowed, 2 refused); run B: acting: 56 to 128 (17 trials, 9 allowed, 1 refused); acting: 56 to 112 (16 trials, 7 allowed, 2 refused); acting: 56 to 120 (19 trials, 8 allowed, 1 refused); run C: acting: 56 to 120 (16 trials, 8 allowed, 2 refused); acting: 56 to 112 (14 trials, 7 allowed, 2 refused); acting: 48 to 128 (18 trials, 10 allowed, 1 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% (-0.2 to +0.1) | -0.1% (-0.2 to +0.1) | -0.0% (-0.3 to +0.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to -0.0) | -0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (2 of 3 runs) |
| cache hit rate | 0.718 | 0.717 | -0.1% (-0.2 to +0.1) | -0.0% (-0.1 to +0.1) | -0.0% (-0.3 to +0.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 5.62 | 5.63 | +0.2% (-0.8 to +1.2) | +0.0% (-0.3 to +0.4) | +0.0% (-0.2 to +0.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.67 | 5.68 | +0.2% (-0.5 to +0.9) | +0.1% (-0.2 to +0.4) | +0.2% (+0.1 to +0.2) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 1.65 | 1.67 | +0.8% (-1.9 to +3.4) | +0.2% (+0.1 to +0.4) | +0.3% (-0.3 to +0.9) | STEADY, no difference beyond the noise (2 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 61.2 | -4.3% (-4.6 to -4.0) | -4.1% (-4.7 to -3.6) | -4.4% (-5.2 to -3.5) | **GAIN in all three of our runs** |
| memory used, mean (MB) | 57.2 | 55.3 | -3.2% (-3.4 to -3.0) | -3.0% (-3.7 to -2.2) | -3.3% (-4.3 to -2.3) | **GAIN in all three of our runs** |
| keys evicted | 71,660 | 71,788 | +0.2% (-0.2 to +0.6) | +0.1% (-0.2 to +0.4) | +0.2% (-0.4 to +0.8) | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.107 | +5.3% (-29.0 to +39.5) | +2.8% (-62.7 to +68.3) | -2.1% (-47.5 to +43.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 70.0 | 73.9 | +5.6% (-31.6 to +42.8) | +2.9% (-71.7 to +77.5) | -2.3% (-55.4 to +50.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.361 | 0.382 | +5.7% (-31.6 to +42.9) | +2.9% (-71.6 to +77.4) | -2.3% (-55.4 to +50.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 10.0 | +10 (+10 to +10) | +10 (+10 to +10) | +10 (+10 to +10) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); run B: acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); run C: acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,268 | 1,358 | +7.1% (+6.4 to +7.7) | +6.7% (+5.1 to +8.3) | +6.9% (+6.2 to +7.6) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.845 | 0.905 | +7.1% (+6.4 to +7.7) | +6.7% (+5.0 to +8.4) | +6.9% (+6.3 to +7.5) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.53 | 5.45 | -1.4% (-1.9 to -0.9) | -0.2% (-0.5 to +0.1) | -1.1% (-1.5 to -0.7) | STEADY, no difference beyond the noise (1 of 3 runs) |
| latency, 99th percentile (ms) | 5.65 | 5.62 | -0.5% (-0.7 to -0.4) | -0.2% (-0.6 to +0.2) | -0.4% (-0.5 to -0.3) | STEADY, no difference beyond the noise (1 of 3 runs) |
| latency, mean (ms) | 0.958 | 0.635 | -33.7% (-36.5 to -30.8) | -32.7% (-41.1 to -24.3) | -32.4% (-36.0 to -28.9) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 77.9 | +21.7% (+17.2 to +26.1) | +19.4% (+6.7 to +32.1) | +20.4% (+14.3 to +26.5) | **power given in all three of our runs** |
| memory used, mean (MB) | 61.3 | 70.3 | +14.7% (+8.7 to +20.7) | +13.4% (+8.5 to +18.3) | +13.1% (+10.8 to +15.3) | **power given in all three of our runs** |
| keys evicted | 103,134 | 63,197 | -38.7% (-42.5 to -35.0) | -36.2% (-45.2 to -27.3) | -37.5% (-41.2 to -33.8) | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.102 | -2.6% (-38.6 to +33.5) | +2.3% (-15.1 to +19.6) | +8.3% (-6.6 to +23.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 188.0 | 183.5 | -2.4% (-42.8 to +38.1) | +2.9% (-15.8 to +21.5) | +9.9% (-6.2 to +25.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.329 | 0.3 | -8.8% (-49.0 to +31.3) | -3.7% (-16.8 to +9.4) | +2.8% (-14.5 to +20.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 47.7 | +47.7 (+35.4 to +59.9) | +45.3 (+15 to +75.7) | +49.3 (+44.2 to +54.5) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 64 to 112 (14 trials, 6 allowed, 4 refused); acting: 56 to 120 (16 trials, 8 allowed, 3 refused); acting: 56 to 112 (16 trials, 7 allowed, 3 refused); run B: acting: 56 to 120 (17 trials, 8 allowed, 3 refused); acting: 40 to 96 (18 trials, 7 allowed, 3 refused); acting: 64 to 104 (14 trials, 5 allowed, 4 refused); run C: acting: 48 to 112 (18 trials, 8 allowed, 2 refused); acting: 56 to 120 (16 trials, 8 allowed, 3 refused); acting: 56 to 112 (16 trials, 7 allowed, 3 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925.5 | 925.1 | -0.0% (-1.2 to +1.1) | -0.2% (-0.2 to -0.1) | +0.1% (-1.1 to +1.4) | STEADY, no difference beyond the noise (2 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.617 | 0.617 | -0.0% (-1.2 to +1.1) | -0.2% (-0.2 to -0.1) | +0.1% (-1.1 to +1.4) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 5.52 | 5.51 | -0.2% (-0.5 to +0.0) | +0.0% (-0.2 to +0.3) | +0.0% (-0.1 to +0.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.59 | 5.58 | -0.1% (-0.4 to +0.1) | +0.2% (-0.1 to +0.5) | +0.2% (+0.0 to +0.3) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 2.15 | 2.14 | -0.2% (-1.9 to +1.5) | +0.4% (-0.1 to +0.9) | -0.1% (-2.0 to +1.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 69.2 | +8.2% (+0.8 to +15.5) | +1.3% (+0.8 to +1.7) | +1.9% (-0.4 to +4.3) | STEADY, no difference beyond the noise (1 of 3 runs) |
| memory used, mean (MB) | 60.7 | 63.5 | +4.6% (-5.2 to +14.3) | +0.2% (+0.2 to +0.2) | +0.4% (-0.6 to +1.4) | STEADY, no difference beyond the noise (2 of 3 runs) |
| keys evicted | 243,151 | 247,083 | +1.6% (+0.4 to +2.8) | +0.3% (+0.2 to +0.3) | +0.2% (+0.0 to +0.5) | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.109 | -2.4% (-12.0 to +7.2) | +14.7% (-10.7 to +40.1) | +7.7% (+2.5 to +12.9) | STEADY, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 195.9 | 191.2 | -2.4% (-12.9 to +8.2) | +17.3% (-12.0 to +46.7) | +9.1% (+3.1 to +15.1) | STEADY, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.47 | 0.459 | -2.3% (-12.8 to +8.1) | +17.5% (-11.9 to +46.9) | +9.0% (+1.7 to +16.3) | STEADY, no difference beyond the noise (2 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 27.3 | +27.3 (+25.9 to +28.8) | +22 (+17.7 to +26.3) | +23 (+20.5 to +25.5) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 56 to 96 (17 trials, 5 allowed, 0 refused); acting: 56 to 96 (16 trials, 5 allowed, 0 refused); acting: 56 to 80 (16 trials, 3 allowed, 1 refused); run B: acting: 56 to 80 (14 trials, 3 allowed, 0 refused); acting: 56 to 80 (12 trials, 3 allowed, 0 refused); acting: 56 to 80 (13 trials, 3 allowed, 0 refused); run C: acting: 64 to 88 (13 trials, 3 allowed, 1 refused); acting: 56 to 80 (12 trials, 3 allowed, 0 refused); acting: 56 to 80 (13 trials, 3 allowed, 0 refused).

**Across 3 untouched workloads: 5 gauge-rows GAIN, 0 LOSS, 2 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 29 STEADY, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
