# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,196 | +1.1% | 8.65 to 18.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00581 to 0.000689 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.798 | +1.2% | 0.00658 to 0.0116 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.22 | +0.3% | -0.0307 to 0.0585 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.25 | 5.31 | +1.2% | -0.169 to 0.291 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.16 | 1.12 | -3.5% | -0.0529 to -0.0283 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 0.653 to 2.32 | power given |
| memory used, mean (MB) | 61.2 | 62.3 | +1.8% | 0.487 to 1.72 | power given |
| keys evicted | 138,403 | 133,377 | -3.6% | -6,607 to -3,446 | shown, not judged |
| host CPU busy (share of the run) | 0.0519 | 0.0633 | +22.0% | -0.0598 to 0.0826 | EVEN, no difference beyond the noise |
| host CPU-seconds | 91.6 | 112 | +22.0% | -113 to 154 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.172 | 0.208 | +20.7% | -0.215 to 0.286 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.3 |  | 16.2 to 26.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
