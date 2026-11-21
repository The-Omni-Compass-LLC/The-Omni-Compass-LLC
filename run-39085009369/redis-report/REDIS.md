# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.0% | -1.05 to 0.257 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0056 to 0.00918 | EVEN, no difference beyond the noise |
| cache hit rate | 0.717 | 0.717 | -0.0% | -0.000626 to 0.000261 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.75 | -0.0% | -0.0162 to 0.0111 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.2% | -0.0013 to 0.0237 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.75 | 1.75 | +0.3% | 0.00259 to 0.00673 | LOSS |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.7 | -2.1% | -2.35 to -0.346 | GAIN |
| memory used, mean (MB) | 57.2 | 56.6 | -0.9% | -0.875 to -0.207 | GAIN |
| keys evicted | 71,797 | 71,853 | +0.1% | -59.5 to 172 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.134 | -7.7% | -0.0494 to 0.027 | EVEN, no difference beyond the noise |
| host CPU-seconds | 98.2 | 89.6 | -8.8% | -38.5 to 21.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.507 | 0.463 | -8.8% | -0.199 to 0.11 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,287 | +1.6% | 16.1 to 23.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00141 to 0.0016 | EVEN, the same |
| cache hit rate | 0.845 | 0.858 | +1.5% | 0.0102 to 0.016 | GAIN |
| latency, 95th percentile (ms) | 5.5 | 5.49 | -0.0% | -0.0184 to 0.0163 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.61 | +0.1% | -0.0014 to 0.00831 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.957 | 0.889 | -7.1% | -0.0792 to -0.0576 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.7 | +1.1% | -2.56 to 4.01 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.6 | +0.6% | -2.97 to 3.65 | EVEN, no difference beyond the noise |
| keys evicted | 103,283 | 94,743 | -8.3% | -10,792 to -6,288 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.1 | -6.8% | -0.0331 to 0.0184 | EVEN, no difference beyond the noise |
| host CPU-seconds | 190 | 175 | -7.5% | -64.4 to 36 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.333 | 0.303 | -8.9% | -0.117 to 0.0583 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 9.85 to 36.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 937 | +1.2% | 11 to 11.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0165 to -0.00336 | LOSS |
| cache hit rate | 0.618 | 0.625 | +1.2% | 0.00727 to 0.0077 | GAIN |
| latency, 95th percentile (ms) | 5.5 | 5.5 | +0.0% | -0.0161 to 0.0182 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.57 | 5.58 | +0.1% | -0.00592 to 0.0194 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.14 | 2.1 | -1.8% | -0.0479 to -0.0301 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.1% | 0.791 to 1.89 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.1% | 1.16 to 1.4 | power given |
| keys evicted | 243,012 | 234,832 | -3.4% | -8,357 to -8,003 | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.113 | +2.9% | -0.0159 to 0.0222 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 198 | +3.3% | -31.8 to 44.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.46 | 0.47 | +2.0% | -0.0817 to 0.1 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14.3 |  | 8.6 to 20.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,196 | +1.1% | 8.65 to 18.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00581 to 0.000689 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.798 | +1.2% | 0.00658 to 0.0116 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.22 | +0.3% | -0.0307 to 0.0585 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.25 | 5.31 | +1.2% | -0.169 to 0.291 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.16 | 1.12 | -3.5% | -0.0529 to -0.0283 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 0.653 to 2.32 | power given |
| memory used, mean (MB) | 61.2 | 62.3 | +1.8% | 0.487 to 1.72 | power given |
| keys evicted | 138,403 | 133,377 | -3.6% | -6,607 to -3,446 | shown, not judged |
| host CPU busy (share of the run) | 0.0519 | 0.0633 | +22.0% | -0.0598 to 0.0826 | EVEN, no difference beyond the noise |
| host CPU-seconds | 91.6 | 112 | +22.0% | -113 to 154 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.172 | 0.208 | +20.7% | -0.215 to 0.286 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.3 |  | 16.2 to 26.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
