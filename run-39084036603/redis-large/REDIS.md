# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
