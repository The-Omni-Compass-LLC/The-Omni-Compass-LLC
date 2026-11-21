# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,197 | +1.1% | 8.09 to 17.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00967 to 0.00448 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.798 | +1.1% | 0.00541 to 0.0118 | GAIN |
| latency, 95th percentile (ms) | 5.53 | 5.52 | -0.2% | -0.0638 to 0.041 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.6 | -0.1% | -0.0371 to 0.026 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.24 | 1.19 | -3.9% | -0.0601 to -0.0366 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.7% | 1.21 to 2.26 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +2.0% | 0.777 to 1.69 | power given |
| keys evicted | 138,176 | 133,192 | -3.6% | -7,139 to -2,829 | shown, not judged |
| host CPU busy (share of the run) | 0.0912 | 0.0884 | -3.0% | -0.0628 to 0.0573 | EVEN, no difference beyond the noise |
| host CPU-seconds | 158 | 153 | -3.3% | -118 to 107 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.297 | 0.284 | -4.3% | -0.223 to 0.197 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 19.5 to 25.2 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 24.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
