# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% | -2.73 to 0.708 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.016 to 0.0359 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00185 to 0.000691 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.75 | -0.0% | -0.00508 to 0.00463 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.2% | -0.00498 to 0.0226 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.74 | 1.75 | +0.4% | -0.00293 to 0.0186 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.4 | -2.5% | -1.97 to -1.2 | GAIN |
| memory used, mean (MB) | 57.2 | 56.5 | -1.1% | -0.989 to -0.234 | GAIN |
| keys evicted | 71,647 | 71,802 | +0.2% | -150 to 459 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.129 | -13.9% | -0.0365 to -0.00515 | GAIN |
| host CPU-seconds | 102 | 85.6 | -15.9% | -27.8 to -4.69 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.526 | 0.442 | -15.9% | -0.144 to -0.0231 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,285 | +1.4% | 5.01 to 31 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00348 to 0.00372 | EVEN, the same |
| cache hit rate | 0.845 | 0.857 | +1.4% | 0.00315 to 0.0209 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.0% | -0.0108 to 0.00542 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.81 | +0.1% | -0.00267 to 0.0109 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.988 | -6.1% | -0.118 to -0.00998 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.7 | +1.1% | -0.244 to 1.67 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.7 | +0.7% | 0.0865 to 0.753 | power given |
| keys evicted | 103,338 | 95,435 | -7.6% | -13,869 to -1,937 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.115 | -2.2% | -0.0307 to 0.0254 | EVEN, no difference beyond the noise |
| host CPU-seconds | 198 | 193 | -2.3% | -58.5 to 49.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.347 | 0.334 | -3.7% | -0.107 to 0.0818 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 15.9 to 27.4 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 24.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 11 to 11.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.021 to -0.00537 | LOSS |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00741 to 0.00767 | GAIN |
| latency, 95th percentile (ms) | 5.68 | 5.68 | -0.0% | -0.0204 to 0.0159 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.74 | +0.1% | -0.0136 to 0.025 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.25 | 2.21 | -1.8% | -0.0544 to -0.0258 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.38 to 1.43 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 1.19 to 1.26 | power given |
| keys evicted | 243,074 | 234,840 | -3.4% | -8,283 to -8,184 | shown, not judged |
| host CPU busy (share of the run) | 0.147 | 0.138 | -6.6% | -0.0304 to 0.0108 | EVEN, no difference beyond the noise |
| host CPU-seconds | 250 | 231 | -7.6% | -60.6 to 22.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.599 | 0.547 | -8.7% | -0.152 to 0.0477 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13.7 |  | 10.8 to 16.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,197 | +1.1% | 8.09 to 17.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00967 to 0.00448 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.798 | +1.1% | 0.00541 to 0.0118 | GAIN |
| latency, 95th percentile (ms) | 5.53 | 5.52 | -0.2% | -0.0638 to 0.041 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.6 | -0.1% | -0.0371 to 0.026 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.24 | 1.19 | -3.9% | -0.0601 to -0.0366 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.7% | 1.21 to 2.26 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +2.0% | 0.777 to 1.69 | power given |
| keys evicted | 138,176 | 133,192 | -3.6% | -7,139 to -2,829 | shown, not judged |
| host CPU busy (share of the run) | 0.0912 | 0.0884 | -3.0% | -0.0628 to 0.0573 | EVEN, no difference beyond the noise |
| host CPU-seconds | 158 | 153 | -3.3% | -118 to 107 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.297 | 0.284 | -4.3% | -0.223 to 0.197 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 19.5 to 25.2 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 24.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
