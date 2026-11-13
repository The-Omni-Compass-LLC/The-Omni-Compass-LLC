# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
