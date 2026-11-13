# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.0% | -2.1 to 1.6 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0231 to 0.0365 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.000742 to 0.000567 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.77 | 5.76 | -0.1% | -0.0201 to 0.0051 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.96 | 5.96 | +0.0% | -0.897 to 0.903 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.76 | 1.76 | -0.0% | -0.0316 to 0.0312 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.2 | -4.4% | -2.96 to -2.7 | GAIN |
| memory used, mean (MB) | 57.2 | 55.3 | -3.3% | -2.08 to -1.65 | GAIN |
| keys evicted | 71,790 | 71,823 | +0.0% | -141 to 207 | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.136 | -3.4% | -0.0272 to 0.0176 | EVEN, no difference beyond the noise |
| host CPU-seconds | 94.7 | 90.9 | -4.0% | -20.9 to 13.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.489 | 0.47 | -4.0% | -0.109 to 0.0698 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,318 | +4.0% | -25 to 126 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0107 to 0.00776 | EVEN, the same |
| cache hit rate | 0.845 | 0.879 | +4.0% | -0.0167 to 0.0843 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.72 | 5.71 | -0.3% | -0.0396 to 0.0084 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.78 | -0.2% | -0.0261 to 0.00646 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.04 | 0.858 | -17.8% | -0.459 to 0.0863 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 68.9 | +7.6% | -6.26 to 16 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 64 | +4.4% | -4.99 to 10.3 | EVEN, no difference beyond the noise |
| keys evicted | 103,266 | 80,926 | -21.6% | -55,943 to 11,263 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.11 | -4.6% | -0.0348 to 0.0241 | EVEN, no difference beyond the noise |
| host CPU-seconds | 194 | 185 | -4.6% | -65.6 to 47.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.341 | 0.312 | -8.3% | -0.109 to 0.0531 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 35 |  | 13.5 to 56.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 14.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 923 | -0.1% | -7.55 to 4.96 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0933 to 0.0199 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.616 | -0.2% | -0.00541 to 0.00323 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.2 | 5.21 | +0.1% | -0.00138 to 0.00956 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.33 | 5.3 | -0.7% | -0.083 to 0.00386 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.05 | 2.05 | -0.0% | -0.0214 to 0.0214 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 70.8 | +10.6% | 3.19 to 10.4 | power given |
| memory used, mean (MB) | 60.7 | 64.8 | +6.8% | 3.21 to 5.08 | power given |
| keys evicted | 243,107 | 248,140 | +2.1% | -1,517 to 11,585 | shown, not judged |
| host CPU busy (share of the run) | 0.0594 | 0.0683 | +14.9% | -0.00441 to 0.0221 | EVEN, no difference beyond the noise |
| host CPU-seconds | 105 | 121 | +15.9% | -8.52 to 41.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.251 | 0.292 | +16.0% | -0.0208 to 0.101 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.3 |  | 25.5 to 31.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 19.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,249 | +5.5% | 56.4 to 74.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0118 to 0.0121 | EVEN, the same |
| cache hit rate | 0.789 | 0.833 | +5.5% | 0.0377 to 0.0499 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.2% | -0.0312 to 0.0138 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.0% | -0.028 to 0.0291 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.11 | -17.8% | -0.284 to -0.198 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 85.5 | +33.6% | 16.7 to 26.3 | power given |
| memory used, mean (MB) | 61.2 | 77.5 | +26.6% | 12 to 20.6 | power given |
| keys evicted | 138,280 | 110,107 | -20.4% | -32,957 to -23,390 | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.117 | -8.1% | -0.0368 to 0.0162 | EVEN, no difference beyond the noise |
| host CPU-seconds | 214 | 196 | -8.5% | -69.3 to 32.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.402 | 0.348 | -13.4% | -0.154 to 0.0465 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 49 |  | 42.4 to 55.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
