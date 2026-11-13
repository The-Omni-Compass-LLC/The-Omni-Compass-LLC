# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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
