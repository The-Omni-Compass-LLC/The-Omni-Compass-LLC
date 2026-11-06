# Redis, a cache's operator-set memory ceiling: the A/B/C confirmation

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **confirmed better** or **confirmed WORSE**; a run whose interval includes zero reads **no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any increase in any run is WORSE. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 38013287665 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| B | 38013291972 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| C | 38013296599 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,181 | -0.2% (-0.3 to -0.1) | +0.5% (-2.0 to +3.1) | +1.5% (+0.7 to +2.4) | **the runs disagree** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.789 | 0.788 | -0.2% (-0.3 to -0.1) | +0.5% (-2.0 to +3.1) | +1.5% (+0.7 to +2.4) | **the runs disagree** |
| latency, 95th percentile (ms) | 5.74 | 5.75 | +0.1% (-0.0 to +0.2) | -0.1% (-0.2 to +0.0) | -0.2% (-1.1 to +0.7) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.2% (-0.1 to +0.5) | +0.1% (-0.1 to +0.3) | -0.0% (-0.5 to +0.4) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.35 | 1.36 | +1.0% (+0.5 to +1.4) | -1.5% (-9.5 to +6.5) | -5.3% (-7.2 to -3.4) | **the runs disagree** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 63.5 | -0.8% (-3.8 to +2.2) | +1.5% (-8.6 to +11.6) | +4.8% (+0.5 to +9.2) | no difference beyond the noise (2 of 3 runs) |
| memory used, mean (MB) | 61.2 | 60.8 | -0.7% (-3.2 to +1.8) | +1.7% (-8.4 to +11.8) | +5.1% (+0.5 to +9.7) | no difference beyond the noise (2 of 3 runs) |
| keys evicted | 138,149 | 140,340 | +1.6% (+0.3 to +2.8) | -0.8% (-10.6 to +9.1) | -5.0% (-7.8 to -2.2) | shown, not judged |
| host CPU busy (share of the run) | 0.13 | 0.122 | -5.9% (-24.0 to +12.1) | -9.5% (-36.7 to +17.6) | +7.2% (-18.6 to +32.9) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 218.1 | 202.9 | -6.9% (-27.6 to +13.8) | -10.8% (-41.2 to +19.6) | +8.2% (-20.6 to +37.0) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.409 | 0.382 | -6.7% (-27.4 to +13.9) | -11.2% (-43.6 to +21.3) | +6.5% (-22.5 to +35.6) | no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 22.0 | +22 (+15.4 to +28.6) | +22.7 (+10.9 to +34.4) | +21.7 (+17.9 to +25.5) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 56 to 72 (15 trials, 2 allowed, 1 refused); acting: 56 to 64 (16 trials, 1 allowed, 0 refused); acting: 56 to 72 (14 trials, 2 allowed, 1 refused); run B: acting: 56 to 72 (17 trials, 2 allowed, 0 refused); acting: 48 to 80 (17 trials, 4 allowed, 0 refused); acting: 56 to 64 (16 trials, 1 allowed, 0 refused); run C: acting: 56 to 72 (17 trials, 2 allowed, 0 refused); acting: 48 to 80 (15 trials, 4 allowed, 0 refused); acting: 56 to 72 (14 trials, 2 allowed, 2 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.0% (-0.1 to +0.0) | -0.0% (-0.2 to +0.2) | -0.1% (-0.3 to +0.1) | no difference beyond the noise (3 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.718 | 0.718 | -0.0% (-0.1 to +0.0) | -0.0% (-0.2 to +0.2) | -0.1% (-0.2 to +0.1) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 5.57 | 5.56 | -0.2% (-0.8 to +0.4) | -0.0% (-0.2 to +0.2) | +0.0% (-0.4 to +0.5) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.66 | 5.66 | -0.0% (-0.4 to +0.4) | +0.1% (-0.2 to +0.4) | +0.1% (-0.3 to +0.6) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.6 | 1.6 | -0.1% (-1.1 to +1.0) | +0.3% (-0.1 to +0.7) | +0.4% (-0.2 to +1.0) | no difference beyond the noise (3 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 61.2 | -4.3% (-5.5 to -3.1) | -4.6% (-5.3 to -3.9) | -3.7% (-8.6 to +1.2) | no difference beyond the noise (1 of 3 runs) |
| memory used, mean (MB) | 57.1 | 55.3 | -3.2% (-4.4 to -2.0) | -3.5% (-4.4 to -2.6) | -2.7% (-6.4 to +1.0) | no difference beyond the noise (1 of 3 runs) |
| keys evicted | 71,668 | 71,754 | +0.1% (-0.1 to +0.4) | +0.1% (-0.5 to +0.7) | +0.2% (-0.2 to +0.6) | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.109 | +6.7% (-87.7 to +101.2) | +2.4% (-68.4 to +73.2) | +5.5% (-5.6 to +16.5) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 72.8 | 78.5 | +7.8% (-97.3 to +112.8) | +2.4% (-80.2 to +85.0) | +6.4% (-5.9 to +18.6) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.376 | 0.405 | +7.8% (-97.2 to +112.8) | +2.4% (-80.3 to +85.2) | +6.4% (-5.7 to +18.6) | no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 10.0 | +10 (+10 to +10) | +10 (+10 to +10) | +8.67 (+2.93 to +14.4) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); run B: acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); run C: acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 1 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,287 | +1.6% (-1.4 to +4.6) | +2.1% (+2.0 to +2.2) | +3.2% (+1.1 to +5.3) | no difference beyond the noise (1 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | same |
| cache hit rate | 0.845 | 0.859 | +1.6% (-1.3 to +4.6) | +2.1% (+2.0 to +2.2) | +3.2% (+1.1 to +5.3) | no difference beyond the noise (1 of 3 runs) |
| latency, 95th percentile (ms) | 5.74 | 5.75 | +0.1% (-0.4 to +0.6) | -0.4% (-0.6 to -0.2) | -0.1% (-0.1 to -0.0) | no difference beyond the noise (1 of 3 runs) |
| latency, 99th percentile (ms) | 5.8 | 5.82 | +0.3% (-0.3 to +0.9) | -0.1% (-0.3 to +0.1) | -0.1% (-0.4 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.05 | 0.984 | -6.5% (-20.1 to +7.0) | -10.1% (-10.8 to -9.3) | -15.9% (-26.9 to -5.0) | no difference beyond the noise (1 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 64.0 | +0.0% (-5.2 to +5.3) | +0.5% (-0.1 to +1.0) | +3.6% (-2.5 to +9.7) | no difference beyond the noise (3 of 3 runs) |
| memory used, mean (MB) | 61.3 | 60.9 | -0.7% (-5.7 to +4.3) | +0.0% (-1.2 to +1.2) | +3.1% (-2.3 to +8.5) | no difference beyond the noise (3 of 3 runs) |
| keys evicted | 103,325 | 94,452 | -8.6% (-24.4 to +7.3) | -11.3% (-11.9 to -10.7) | -17.2% (-28.9 to -5.4) | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.122 | +3.4% (-24.6 to +31.4) | -21.1% (-36.8 to -5.4) | +33.0% (-40.5 to +106.5) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 197.5 | 204.9 | +3.8% (-27.8 to +35.4) | -23.1% (-40.7 to -5.5) | +35.4% (-43.3 to +114.0) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.346 | 0.354 | +2.1% (-31.8 to +36.0) | -24.7% (-42.3 to -7.0) | +31.0% (-43.4 to +105.5) | no difference beyond the noise (2 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 27.7 | +27.7 (+20.1 to +35.3) | +27 (+20.4 to +33.6) | +29.3 (+25.5 to +33.1) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 56 to 72 (17 trials, 2 allowed, 1 refused); acting: 40 to 80 (19 trials, 5 allowed, 1 refused); acting: 56 to 72 (18 trials, 2 allowed, 2 refused); run B: acting: 56 to 72 (17 trials, 2 allowed, 2 refused); acting: 56 to 72 (17 trials, 2 allowed, 2 refused); acting: 56 to 72 (19 trials, 2 allowed, 2 refused); run C: acting: 56 to 80 (20 trials, 3 allowed, 2 refused); acting: 56 to 72 (17 trials, 2 allowed, 3 refused); acting: 56 to 80 (18 trials, 3 allowed, 2 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925.0 | 926.1 | +0.1% (-3.0 to +3.2) | -0.6% (-0.7 to -0.5) | -0.4% (-0.6 to -0.2) | no difference beyond the noise (1 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.617 | 0.618 | +0.1% (-3.0 to +3.2) | -0.6% (-0.6 to -0.5) | -0.4% (-0.6 to -0.3) | no difference beyond the noise (1 of 3 runs) |
| latency, 95th percentile (ms) | 5.21 | 5.21 | +0.1% (-0.2 to +0.3) | +0.1% (-0.4 to +0.6) | -0.0% (-0.1 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.27 | 5.33 | +1.1% (-0.9 to +3.2) | +0.1% (-0.2 to +0.5) | +0.1% (+0.0 to +0.2) | no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 2.04 | 2.04 | +0.0% (-4.5 to +4.5) | +1.1% (+0.4 to +1.8) | +0.7% (+0.4 to +0.9) | no difference beyond the noise (1 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.5 | +2.4% (-11.2 to +16.0) | -0.9% (-1.1 to -0.7) | -0.1% (-0.8 to +0.5) | no difference beyond the noise (2 of 3 runs) |
| memory used, mean (MB) | 60.7 | 62.1 | +2.4% (-11.8 to +16.6) | -1.2% (-1.3 to -1.1) | -0.4% (-1.3 to +0.4) | no difference beyond the noise (2 of 3 runs) |
| keys evicted | 243,056 | 242,642 | -0.2% (-8.4 to +8.0) | +2.3% (+2.3 to +2.4) | +1.2% (-0.7 to +3.1) | shown, not judged |
| host CPU busy (share of the run) | 0.0646 | 0.0718 | +11.1% (-29.4 to +51.7) | +1.2% (-6.7 to +9.2) | -8.3% (-16.1 to -0.4) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 114.3 | 127.7 | +11.8% (-31.0 to +54.5) | +1.2% (-8.1 to +10.6) | -9.5% (-18.4 to -0.6) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.275 | 0.306 | +11.6% (-27.7 to +50.9) | +1.8% (-7.7 to +11.4) | -9.1% (-17.9 to -0.4) | no difference beyond the noise (2 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 21.0 | +21 (+7.85 to +34.1) | +25.7 (+22.8 to +28.5) | +22.3 (+13.6 to +31.1) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 56 to 64 (18 trials, 1 allowed, 0 refused); acting: 56 to 64 (16 trials, 1 allowed, 0 refused); acting: 56 to 72 (15 trials, 2 allowed, 0 refused); run B: acting: 56 to 64 (18 trials, 1 allowed, 0 refused); acting: 56 to 64 (18 trials, 1 allowed, 0 refused); acting: 56 to 64 (18 trials, 1 allowed, 0 refused); run C: acting: 56 to 64 (12 trials, 1 allowed, 0 refused); acting: 56 to 72 (15 trials, 2 allowed, 0 refused); acting: 56 to 64 (16 trials, 1 allowed, 0 refused).

**Across 3 untouched workloads: 0 gauge-rows confirmed better, 0 confirmed worse, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
