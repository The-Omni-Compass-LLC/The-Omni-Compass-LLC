# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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
