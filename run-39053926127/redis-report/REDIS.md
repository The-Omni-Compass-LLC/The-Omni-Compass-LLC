# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,074 | -0.1% | -2.76 to 0.381 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0446 to 0.0191 | EVEN, no difference beyond the noise |
| cache hit rate | 0.717 | 0.717 | -0.0% | -0.000537 to -0.000132 | LOSS |
| latency, 95th percentile (ms) | 5.55 | 5.56 | +0.1% | -0.0019 to 0.0113 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.61 | 5.62 | +0.3% | -0.00452 to 0.037 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.63 | 1.64 | +1.0% | -0.0125 to 0.0439 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.2 | -2.8% | -3.43 to -0.129 | GAIN |
| memory used, mean (MB) | 57.1 | 56.3 | -1.5% | -2.53 to 0.841 | EVEN, no difference beyond the noise |
| keys evicted | 71,743 | 71,857 | +0.2% | 97.7 to 130 | shown, not judged |
| host CPU busy (share of the run) | 0.0936 | 0.0957 | +2.2% | -0.0442 to 0.0484 | EVEN, no difference beyond the noise |
| host CPU-seconds | 64.9 | 66.1 | +1.8% | -34.2 to 36.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.335 | 0.342 | +2.0% | -0.176 to 0.19 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 1.6 to 13.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,283 | +1.3% | 7.49 to 25.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00401 to 0.00228 | EVEN, the same |
| cache hit rate | 0.845 | 0.856 | +1.3% | 0.00495 to 0.0172 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.1% | -0.0113 to 0.0047 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.1% | -0.0096 to 0.0155 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 0.998 | -5.5% | -0.0889 to -0.0278 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.8 | +1.2% | -1.89 to 3.46 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.5 | +0.4% | -2.37 to 2.82 | EVEN, no difference beyond the noise |
| keys evicted | 103,434 | 96,191 | -7.0% | -11,386 to -3,098 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.125 | +5.5% | -0.0434 to 0.0563 | EVEN, no difference beyond the noise |
| host CPU-seconds | 197 | 210 | +6.2% | -81.2 to 106 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.346 | 0.363 | +4.9% | -0.145 to 0.179 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 24 |  | 6.61 to 41.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 23.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.3% | 10 to 13.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0246 to 0.0234 | EVEN, the same |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00676 to 0.00877 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.68 | -0.0% | -0.0116 to 0.00673 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.1% | -0.00741 to 0.02 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.22 | -1.9% | -0.0525 to -0.0333 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.1% | 1.15 to 1.53 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.87 to 1.45 | power given |
| keys evicted | 243,156 | 236,906 | -2.6% | -14,854 to 2,354 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.141 | +2.5% | -0.0426 to 0.0497 | EVEN, no difference beyond the noise |
| host CPU-seconds | 230 | 237 | +3.4% | -81.1 to 96.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.551 | 0.563 | +2.1% | -0.2 to 0.223 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15 |  | 10 to 20 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 18.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,196 | +1.1% | 6.03 to 19.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00475 to 0.00321 | EVEN, the same |
| cache hit rate | 0.789 | 0.798 | +1.1% | 0.00376 to 0.013 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.0% | -0.00636 to 0.00349 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.34 | 5.31 | -0.5% | -0.133 to 0.0817 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.16 | 1.11 | -3.9% | -0.0638 to -0.0258 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.4% | 0.493 to 2.64 | power given |
| memory used, mean (MB) | 61.2 | 62.3 | +1.9% | 0.0598 to 2.21 | power given |
| keys evicted | 138,120 | 133,296 | -3.5% | -7,944 to -1,705 | shown, not judged |
| host CPU busy (share of the run) | 0.0536 | 0.0479 | -10.7% | -0.0311 to 0.0197 | EVEN, no difference beyond the noise |
| host CPU-seconds | 94.6 | 83.9 | -11.3% | -57.1 to 35.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.178 | 0.156 | -12.2% | -0.11 to 0.0662 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
