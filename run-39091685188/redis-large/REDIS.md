# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,288 | +1.7% | 21.2 to 22.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00247 to 0.00211 | EVEN, the same |
| cache hit rate | 0.844 | 0.859 | +1.7% | 0.0139 to 0.0155 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.1% | -0.0193 to 0.00812 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.0% | -0.00953 to 0.0106 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.974 | -7.6% | -0.0875 to -0.0717 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.1% | 0.486 to 2.24 | power given |
| memory used, mean (MB) | 61.3 | 62.2 | +1.5% | 0.223 to 1.62 | power given |
| keys evicted | 103,704 | 93,997 | -9.4% | -10,243 to -9,170 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.124 | +3.4% | -0.00537 to 0.0136 | EVEN, no difference beyond the noise |
| host CPU-seconds | 201 | 210 | +4.2% | -9.8 to 26.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.353 | 0.362 | +2.4% | -0.023 to 0.0402 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 18.8 to 24.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
