# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `8e3f058da83e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 937 | +1.2% | 10.9 to 12.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0298 to 0.0185 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00744 to 0.00806 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.1% | 0.000445 to 0.00634 | LOSS |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.2% | 0.0102 to 0.0173 | LOSS |
| latency, mean (ms) | 2.26 | 2.22 | -1.7% | -0.0412 to -0.0348 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.36 to 1.4 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 1.18 to 1.25 | power given |
| keys evicted | 243,247 | 234,861 | -3.4% | -8,592 to -8,180 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.139 | -9.3% | -0.0383 to 0.00979 | EVEN, no difference beyond the noise |
| host CPU-seconds | 259 | 232 | -10.6% | -74 to 18.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.622 | 0.549 | -11.7% | -0.183 to 0.0374 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 11.7 |  | 8.8 to 14.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
