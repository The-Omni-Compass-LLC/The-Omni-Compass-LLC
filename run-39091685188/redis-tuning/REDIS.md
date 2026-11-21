# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,194 | +0.8% | 8.43 to 10.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00424 to 0.0019 | EVEN, the same |
| cache hit rate | 0.79 | 0.796 | +0.8% | 0.00564 to 0.00733 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 5.74 | +0.2% | -0.00354 to 0.023 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.81 | +0.3% | 0.00101 to 0.0393 | LOSS |
| latency, mean (ms) | 1.34 | 1.32 | -2.0% | -0.0309 to -0.0223 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.1% | 1.12 to 1.63 | power given |
| memory used, mean (MB) | 61.2 | 62.2 | +1.6% | 0.692 to 1.27 | power given |
| keys evicted | 137,970 | 134,687 | -2.4% | -5,007 to -1,558 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.128 | +8.6% | -0.015 to 0.0353 | EVEN, no difference beyond the noise |
| host CPU-seconds | 197 | 216 | +9.5% | -29.7 to 67.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.37 | 0.402 | +8.7% | -0.0584 to 0.122 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20 |  | 13.4 to 26.6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
