# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `43a27376d80b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,075 | -0.0% | -0.958 to 0.823 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.172 to 0.158 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.000662 to 0.000245 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.23 | 5.23 | -0.0% | -0.0107 to 0.00702 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.33 | 5.39 | +1.0% | -0.0927 to 0.204 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.54 | 1.55 | +0.2% | -0.0132 to 0.0179 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61 | -4.7% | -3.2 to -2.76 | GAIN |
| memory used, mean (MB) | 57.2 | 55.1 | -3.6% | -2.28 to -1.79 | GAIN |
| keys evicted | 71,715 | 71,782 | +0.1% | -74.2 to 208 | shown, not judged |
| host CPU busy (share of the run) | 0.0679 | 0.0509 | -25.0% | -0.0571 to 0.0232 | EVEN, no difference beyond the noise |
| host CPU-seconds | 47.9 | 35.4 | -26.2% | -42.6 to 17.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.248 | 0.183 | -26.2% | -0.22 to 0.0906 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `43a27376d80b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,268 | 1,347 | +6.2% | 23.5 to 135 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00402 to 0.00334 | EVEN, the same |
| cache hit rate | 0.845 | 0.898 | +6.2% | 0.0158 to 0.0897 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 5.7 | -0.4% | -0.0484 to 0.00425 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.78 | -0.2% | -0.0171 to -0.00292 | GAIN |
| latency, mean (ms) | 1.04 | 0.75 | -27.9% | -0.495 to -0.0859 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 74.1 | +15.8% | -3.25 to 23.5 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 68.3 | +11.4% | -0.922 to 14.9 | EVEN, no difference beyond the noise |
| keys evicted | 103,223 | 68,241 | -33.9% | -60,114 to -9,850 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.0983 | -15.7% | -0.0702 to 0.0336 | EVEN, no difference beyond the noise |
| host CPU-seconds | 196 | 163 | -16.6% | -129 to 63.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.343 | 0.27 | -21.4% | -0.247 to 0.1 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 41.3 |  | 20.5 to 62.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 16.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `43a27376d80b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 924 | -0.2% | -2.09 to -1.08 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0129 to -0.00368 | LOSS |
| cache hit rate | 0.617 | 0.616 | -0.2% | -0.00136 to -0.00065 | LOSS |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% | -0.00289 to 0.00655 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.2% | 0.000742 to 0.0221 | LOSS |
| latency, mean (ms) | 2.26 | 2.27 | +0.4% | 0.00542 to 0.0117 | LOSS |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65 | +1.6% | 0.0547 to 1.97 | power given |
| memory used, mean (MB) | 60.7 | 60.8 | +0.2% | 0.0621 to 0.18 | power given |
| keys evicted | 243,097 | 244,896 | +0.7% | -2,627 to 6,226 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.147 | +7.2% | -0.024 to 0.0437 | EVEN, no difference beyond the noise |
| host CPU-seconds | 230 | 249 | +8.3% | -47.4 to 85.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.551 | 0.598 | +8.5% | -0.113 to 0.206 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22 |  | 17.7 to 26.3 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `43a27376d80b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,241 | +4.8% | 25.4 to 89.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00416 to 0.00534 | EVEN, the same |
| cache hit rate | 0.789 | 0.828 | +4.8% | 0.017 to 0.0595 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 5.73 | -0.1% | -0.0221 to 0.0127 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.1% | -0.0134 to 0.0243 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.13 | -15.6% | -0.333 to -0.084 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 78.5 | +22.7% | -3.82 to 32.9 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 73.2 | +19.6% | -1.27 to 25.3 | EVEN, no difference beyond the noise |
| keys evicted | 138,111 | 113,680 | -17.7% | -38,558 to -10,303 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.108 | -6.5% | -0.0282 to 0.0132 | EVEN, no difference beyond the noise |
| host CPU-seconds | 193 | 180 | -6.7% | -52 to 26.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.361 | 0.322 | -11.0% | -0.111 to 0.0316 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 36.3 |  | 17.7 to 55 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 19.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
