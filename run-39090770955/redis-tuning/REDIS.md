# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `8e3f058da83e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,195 | +0.9% | 3.63 to 18.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00193 to 0.00364 | EVEN, the same |
| cache hit rate | 0.789 | 0.797 | +0.9% | 0.00252 to 0.0123 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.73 | -0.2% | -0.0217 to -0.00216 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.8 | -0.1% | -0.0162 to 0.00597 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.31 | -3.1% | -0.069 to -0.0135 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | -0.167 to 3.02 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 62.2 | +1.7% | -0.212 to 2.25 | EVEN, no difference beyond the noise |
| keys evicted | 138,126 | 133,934 | -3.0% | -7,503 to -881 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.123 | -1.6% | -0.0159 to 0.0119 | EVEN, no difference beyond the noise |
| host CPU-seconds | 209 | 207 | -1.3% | -28.5 to 23.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.393 | 0.384 | -2.2% | -0.0593 to 0.042 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20.3 |  | 12.7 to 27.9 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
