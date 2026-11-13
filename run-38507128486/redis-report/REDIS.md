# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% | -2.01 to 0.849 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.159 to 0.275 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.000934 to 0.000291 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.76 | 5.76 | -0.0% | -0.0148 to 0.0123 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.86 | +0.7% | -0.106 to 0.185 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.75 | 1.76 | +0.4% | -0.0125 to 0.0271 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.1 | -4.6% | -3.23 to -2.64 | GAIN |
| memory used, mean (MB) | 57.2 | 55.2 | -3.5% | -2.45 to -1.51 | GAIN |
| keys evicted | 71,765 | 71,845 | +0.1% | -99.9 to 259 | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.137 | +0.9% | -0.0678 to 0.0702 | EVEN, no difference beyond the noise |
| host CPU-seconds | 91.2 | 92.1 | +0.9% | -52.5 to 54.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.471 | 0.476 | +1.0% | -0.271 to 0.28 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,318 | +4.1% | 8.11 to 95 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000215 to 0.00102 | EVEN, the same |
| cache hit rate | 0.844 | 0.879 | +4.1% | 0.00558 to 0.0634 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.73 | -0.2% | -0.0318 to 0.00372 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.81 | -0.0% | -0.0359 to 0.0318 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 0.868 | -17.9% | -0.342 to -0.0368 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 67.9 | +6.2% | -2.4 to 10.3 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 64.1 | +4.6% | -2.99 to 8.63 | EVEN, no difference beyond the noise |
| keys evicted | 103,656 | 80,984 | -21.9% | -41,999 to -3,345 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.118 | -3.3% | -0.0225 to 0.0145 | EVEN, no difference beyond the noise |
| host CPU-seconds | 205 | 199 | -2.9% | -42.1 to 30.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.36 | 0.336 | -6.6% | -0.0935 to 0.0456 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 33.7 |  | 21.9 to 45.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 17.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 926 | +0.0% | -6.67 to 6.98 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00826 to -0.00188 | LOSS |
| cache hit rate | 0.617 | 0.618 | +0.0% | -0.00458 to 0.00471 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.51 | 5.51 | +0.1% | -0.00578 to 0.012 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.57 | 5.57 | +0.1% | -0.000429 to 0.00838 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.13 | 2.14 | +0.1% | -0.0302 to 0.0347 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 71.5 | +11.7% | 5.48 to 9.55 | power given |
| memory used, mean (MB) | 60.7 | 65.1 | +7.2% | 3.86 to 4.9 | power given |
| keys evicted | 243,086 | 246,275 | +1.3% | 4.01 to 6,374 | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.104 | -4.5% | -0.0295 to 0.0197 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 182 | -5.2% | -57.2 to 37.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.46 | 0.436 | -5.2% | -0.141 to 0.0932 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28 |  | 21.4 to 34.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 20.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,254 | +5.9% | 60.1 to 79 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.00185 to 0.00309 | GAIN |
| cache hit rate | 0.789 | 0.836 | +5.9% | 0.04 to 0.0527 | GAIN |
| latency, 95th percentile (ms) | 5.53 | 5.51 | -0.4% | -0.0547 to 0.0113 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.61 | 5.6 | -0.1% | -0.0215 to 0.00823 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.24 | 0.994 | -19.8% | -0.286 to -0.205 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 86.6 | +35.3% | 19.2 to 26 | power given |
| memory used, mean (MB) | 61.2 | 79.8 | +30.3% | 17 to 20.1 | power given |
| keys evicted | 138,123 | 107,662 | -22.1% | -34,737 to -26,186 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.0934 | -8.2% | -0.0555 to 0.0387 | EVEN, no difference beyond the noise |
| host CPU-seconds | 179 | 163 | -8.7% | -108 to 76.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.336 | 0.29 | -13.8% | -0.215 to 0.122 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 51 |  | 28.2 to 73.8 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
