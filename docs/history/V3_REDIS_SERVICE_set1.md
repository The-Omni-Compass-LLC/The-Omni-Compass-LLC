# Redis, a cache's operator-set memory ceiling: the A/B/C confirmation

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **confirmed better** or **confirmed WORSE**; a run whose interval includes zero reads **no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any increase in any run is WORSE. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 38013357351 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| B | 38013361862 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| C | 38013366329 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,194 | +0.8% (-1.7 to +3.4) | +0.4% (-1.6 to +2.3) | +1.3% (-1.4 to +4.1) | no difference beyond the noise (3 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.79 | 0.796 | +0.8% (-1.7 to +3.3) | +0.4% (-1.6 to +2.3) | +1.4% (-1.3 to +4.0) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 5.73 | 5.73 | -0.1% (-0.3 to +0.1) | -0.0% (-0.1 to +0.1) | +0.0% (-0.1 to +0.1) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.79 | 5.79 | +0.0% (-0.2 to +0.2) | +0.1% (-0.1 to +0.2) | +0.1% (-0.3 to +0.4) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.34 | 1.31 | -2.5% (-10.9 to +5.8) | -1.0% (-7.6 to +5.6) | -4.4% (-15.6 to +6.8) | no difference beyond the noise (3 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.3 | +2.0% (-6.4 to +10.4) | +1.4% (-4.4 to +7.2) | +5.4% (-5.7 to +16.4) | no difference beyond the noise (3 of 3 runs) |
| memory used, mean (MB) | 61.2 | 62.5 | +2.2% (-6.1 to +10.5) | +1.2% (-4.4 to +6.8) | +5.0% (-5.4 to +15.3) | no difference beyond the noise (3 of 3 runs) |
| keys evicted | 137,957 | 135,118 | -2.1% (-11.7 to +7.6) | -0.5% (-7.5 to +6.5) | -4.3% (-15.2 to +6.6) | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.116 | -4.6% (-48.3 to +39.0) | +4.9% (-71.7 to +81.4) | -6.9% (-31.7 to +17.9) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 203.6 | 193.0 | -5.2% (-55.2 to +44.8) | +5.4% (-80.8 to +91.6) | -7.4% (-33.3 to +18.6) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.382 | 0.359 | -6.1% (-53.7 to +41.6) | +5.1% (-82.8 to +93.0) | -8.5% (-35.7 to +18.6) | no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 21.7 | +21.7 (+12.3 to +31.1) | +25.3 (+19.1 to +31.6) | +23 (-2.82 to +48.8) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 56 to 72 (19 trials, 2 allowed, 1 refused); acting: 56 to 72 (15 trials, 2 allowed, 0 refused); acting: 56 to 64 (18 trials, 1 allowed, 0 refused); run B: acting: 56 to 72 (16 trials, 2 allowed, 1 refused); acting: 56 to 72 (19 trials, 2 allowed, 0 refused); acting: 56 to 72 (14 trials, 2 allowed, 1 refused); run C: acting: 56 to 80 (17 trials, 3 allowed, 1 refused); acting: 48 to 72 (17 trials, 3 allowed, 0 refused); acting: 56 to 80 (21 trials, 3 allowed, 0 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% (-0.1 to +0.0) | -0.0% (-0.3 to +0.3) | -0.1% (-0.2 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.718 | 0.717 | -0.0% (-0.1 to +0.0) | -0.0% (-0.2 to +0.2) | -0.1% (-0.2 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 5.73 | 5.73 | +0.0% (-0.3 to +0.3) | -0.1% (-0.2 to +0.1) | +0.1% (-0.2 to +0.3) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.79 | 5.79 | +0.1% (-0.2 to +0.4) | +0.0% (-2.8 to +2.8) | +0.2% (+0.1 to +0.3) | no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 1.73 | 1.74 | +0.2% (-0.2 to +0.7) | +0.1% (-1.9 to +2.0) | +0.5% (-0.2 to +1.2) | no difference beyond the noise (3 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 61.2 | -4.3% (-5.4 to -3.2) | -3.1% (-7.3 to +1.1) | -4.8% (-5.0 to -4.5) | no difference beyond the noise (1 of 3 runs) |
| memory used, mean (MB) | 57.2 | 55.3 | -3.2% (-4.6 to -1.8) | -2.2% (-5.3 to +0.9) | -3.7% (-4.1 to -3.3) | no difference beyond the noise (1 of 3 runs) |
| keys evicted | 71,743 | 71,798 | +0.1% (-0.2 to +0.4) | +0.0% (-0.4 to +0.5) | +0.2% (-0.1 to +0.4) | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.139 | +3.6% (-6.7 to +13.9) | +0.3% (-69.1 to +69.7) | +9.0% (-27.3 to +45.3) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 90.2 | 93.8 | +4.0% (-7.5 to +15.5) | +0.4% (-74.6 to +75.4) | +9.9% (-31.9 to +51.7) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.465 | 0.484 | +4.0% (-7.5 to +15.6) | +0.5% (-74.2 to +75.1) | +10.0% (-31.9 to +51.8) | no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 10.0 | +10 (+10 to +10) | +8.67 (+2.93 to +14.4) | +10 (+10 to +10) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 1 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); run C: acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,295 | +2.3% (+1.6 to +2.9) | +1.6% (-1.0 to +4.3) | +1.2% (-1.6 to +4.1) | no difference beyond the noise (2 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | same |
| cache hit rate | 0.845 | 0.864 | +2.3% (+1.7 to +2.9) | +1.7% (-1.1 to +4.4) | +1.2% (-1.6 to +4.1) | no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 5.73 | 5.74 | +0.1% (-0.5 to +0.7) | -0.0% (-0.1 to +0.1) | +0.1% (-0.3 to +0.4) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.79 | 5.81 | +0.3% (-0.3 to +0.9) | +0.1% (+0.0 to +0.1) | +0.2% (-0.1 to +0.5) | no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 1.05 | 0.948 | -9.6% (-12.9 to -6.3) | -7.1% (-19.3 to +5.1) | -5.1% (-18.4 to +8.2) | no difference beyond the noise (2 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.4 | +2.2% (-3.3 to +7.6) | +1.0% (-8.1 to +10.1) | +0.6% (-6.7 to +7.8) | no difference beyond the noise (3 of 3 runs) |
| memory used, mean (MB) | 61.3 | 62.3 | +1.6% (-5.4 to +8.6) | +0.7% (-9.0 to +10.4) | -0.1% (-8.6 to +8.3) | no difference beyond the noise (3 of 3 runs) |
| keys evicted | 103,554 | 91,070 | -12.1% (-14.9 to -9.2) | -8.7% (-23.8 to +6.3) | -6.5% (-22.1 to +9.0) | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.122 | -0.2% (-14.6 to +14.3) | +4.4% (-32.4 to +41.2) | +9.7% (-25.7 to +45.0) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 205.9 | 205.4 | -0.2% (-17.1 to +16.6) | +5.1% (-36.5 to +46.8) | +10.8% (-28.4 to +50.1) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.361 | 0.353 | -2.4% (-19.1 to +14.2) | +3.4% (-36.4 to +43.2) | +9.5% (-31.7 to +50.7) | no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 27.7 | +27.7 (+8.86 to +46.5) | +24 (+8.49 to +39.5) | +26.7 (+4.96 to +48.4) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 56 to 72 (18 trials, 2 allowed, 1 refused); acting: 40 to 80 (20 trials, 5 allowed, 1 refused); acting: 64 to 72 (17 trials, 1 allowed, 2 refused); run B: acting: 64 to 72 (16 trials, 1 allowed, 3 refused); acting: 56 to 72 (19 trials, 2 allowed, 1 refused); acting: 56 to 72 (16 trials, 2 allowed, 2 refused); run C: acting: 48 to 72 (19 trials, 3 allowed, 1 refused); acting: 56 to 80 (18 trials, 3 allowed, 1 refused); acting: 64 to 72 (13 trials, 1 allowed, 3 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924.3 | 927.3 | +0.3% (-2.6 to +3.2) | -0.5% (-0.9 to +0.0) | -0.4% (-1.4 to +0.6) | no difference beyond the noise (3 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to -0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | no difference beyond the noise (2 of 3 runs) |
| cache hit rate | 0.617 | 0.619 | +0.3% (-2.6 to +3.2) | -0.5% (-0.8 to -0.1) | -0.4% (-1.4 to +0.6) | no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 5.2 | 5.2 | -0.0% (-0.2 to +0.2) | -0.0% (-0.2 to +0.2) | +0.0% (-0.1 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.26 | 5.26 | +0.1% (-0.8 to +1.0) | +0.4% (-0.3 to +1.1) | +0.1% (-0.0 to +0.1) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 2.05 | 2.03 | -0.6% (-5.4 to +4.1) | +0.7% (-0.3 to +1.8) | +0.7% (-0.7 to +2.1) | no difference beyond the noise (3 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.7 | +2.7% (-9.7 to +15.1) | -0.7% (-1.5 to +0.1) | -0.3% (-2.4 to +1.7) | no difference beyond the noise (3 of 3 runs) |
| memory used, mean (MB) | 60.7 | 62.3 | +2.6% (-10.9 to +16.1) | -1.0% (-2.0 to +0.1) | -0.7% (-2.6 to +1.3) | no difference beyond the noise (3 of 3 runs) |
| keys evicted | 243,120 | 241,958 | -0.5% (-8.7 to +7.7) | +1.7% (-0.8 to +4.2) | +1.6% (-2.0 to +5.1) | shown, not judged |
| host CPU busy (share of the run) | 0.0597 | 0.0638 | +7.0% (-77.3 to +91.2) | -15.7% (-56.7 to +25.3) | +3.0% (-5.1 to +11.2) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 105.3 | 113.4 | +7.8% (-80.8 to +96.3) | -16.8% (-60.2 to +26.7) | +3.2% (-6.2 to +12.7) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.253 | 0.271 | +7.2% (-80.7 to +95.2) | -16.4% (-59.6 to +26.8) | +3.7% (-5.6 to +13.0) | no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 19.0 | +19 (+1.61 to +36.4) | +23.7 (+17.4 to +29.9) | +21.7 (+4.76 to +38.6) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (14 trials, 0 allowed, 1 refused); acting: 56 to 64 (18 trials, 1 allowed, 0 refused); acting: 56 to 72 (15 trials, 2 allowed, 0 refused); run B: acting: 56 to 64 (17 trials, 1 allowed, 0 refused); acting: 56 to 64 (16 trials, 1 allowed, 0 refused); acting: 56 to 64 (17 trials, 1 allowed, 0 refused); run C: acting: 56 to 64 (17 trials, 1 allowed, 0 refused); left native (15 trials, 0 allowed, 1 refused); acting: 56 to 64 (18 trials, 1 allowed, 0 refused).

**Across 3 untouched workloads: 0 gauge-rows confirmed better, 0 confirmed worse, 0 where the runs disagree.**

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
