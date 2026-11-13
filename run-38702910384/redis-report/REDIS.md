# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `e842b63d0313`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,075 | -0.0% | -1.39 to 1.25 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0703 to 0.109 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | +0.0% | -0.000203 to 0.000207 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.0% | -0.00373 to 0.00451 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.29 | +0.4% | -0.0661 to 0.111 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.53 | 1.54 | +0.3% | -0.0248 to 0.0352 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.3% | -4.35 to 1.45 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 57.1 | 56.2 | -1.6% | -2.99 to 1.14 | EVEN, no difference beyond the noise |
| keys evicted | 71,712 | 71,698 | -0.0% | -112 to 84.2 | shown, not judged |
| host CPU busy (share of the run) | 0.0601 | 0.0516 | -14.2% | -0.0539 to 0.0368 | EVEN, no difference beyond the noise |
| host CPU-seconds | 42.5 | 36 | -15.4% | -40.2 to 27.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.22 | 0.186 | -15.5% | -0.208 to 0.14 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 1.6 to 13.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `e842b63d0313`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,355 | +7.0% | 85.5 to 91.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00207 to 0.00117 | EVEN, the same |
| cache hit rate | 0.845 | 0.904 | +7.0% | 0.0573 to 0.0609 | GAIN |
| latency, 95th percentile (ms) | 5.51 | 5.45 | -1.1% | -0.1 to -0.0201 | GAIN |
| latency, 99th percentile (ms) | 5.6 | 5.58 | -0.4% | -0.0301 to -0.00961 | GAIN |
| latency, mean (ms) | 0.961 | 0.645 | -32.9% | -0.331 to -0.3 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 76.9 | +20.1% | 9.24 to 16.5 | power given |
| memory used, mean (MB) | 61.3 | 69.4 | +13.2% | 7.98 to 8.19 | power given |
| keys evicted | 103,609 | 64,170 | -38.1% | -40,964 to -37,912 | shown, not judged |
| host CPU busy (share of the run) | 0.0833 | 0.094 | +12.9% | -0.00818 to 0.0296 | EVEN, no difference beyond the noise |
| host CPU-seconds | 143 | 165 | +15.0% | -16.1 to 59 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.251 | 0.27 | +7.4% | -0.0422 to 0.0797 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 47.3 |  | 38.6 to 56.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `e842b63d0313`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 924 | -0.2% | -3.11 to 0.155 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0219 to 0.00585 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.616 | -0.2% | -0.00188 to 5.97e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.69 | 5.69 | -0.0% | -0.0117 to 0.0091 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.1% | -0.00674 to 0.021 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.27 | +0.3% | -0.00502 to 0.0171 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.4% | 0.422 to 1.36 | power given |
| memory used, mean (MB) | 60.7 | 60.6 | -0.1% | -0.772 to 0.652 | EVEN, no difference beyond the noise |
| keys evicted | 243,246 | 244,998 | +0.7% | -2,334 to 5,838 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.141 | -2.6% | -0.0418 to 0.0343 | EVEN, no difference beyond the noise |
| host CPU-seconds | 242 | 235 | -3.0% | -82.6 to 68 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.582 | 0.565 | -2.8% | -0.198 to 0.165 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23.3 |  | 17.1 to 29.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `e842b63d0313`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,258 | +6.3% | 60.8 to 87.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00281 to 0.00596 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.839 | +6.3% | 0.0406 to 0.0581 | GAIN |
| latency, 95th percentile (ms) | 5.63 | 5.6 | -0.6% | -0.0952 to 0.0325 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.71 | 5.7 | -0.2% | -0.0574 to 0.0314 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.28 | 1.01 | -21.2% | -0.346 to -0.197 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 89 | +39.0% | 21 to 28.9 | power given |
| memory used, mean (MB) | 61.2 | 80.8 | +32.0% | 16.5 to 22.7 | power given |
| keys evicted | 138,230 | 105,761 | -23.5% | -38,387 to -26,553 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.112 | -2.0% | -0.0152 to 0.0107 | EVEN, no difference beyond the noise |
| host CPU-seconds | 201 | 199 | -1.3% | -25.2 to 20 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.378 | 0.351 | -7.1% | -0.074 to 0.0202 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 50.7 |  | 34.1 to 67.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
