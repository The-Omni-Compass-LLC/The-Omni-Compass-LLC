# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 924 | -0.2% | -2.89 to -0.738 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0235 to 0.0222 | EVEN, the same |
| cache hit rate | 0.617 | 0.616 | -0.2% | -0.00211 to -0.000128 | LOSS |
| latency, 95th percentile (ms) | 5.7 | 5.7 | -0.0% | -0.0231 to 0.0204 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.76 | 5.76 | +0.1% | -0.0192 to 0.0282 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 2.28 | +0.2% | -0.0143 to 0.0242 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.3% | 0.301 to 1.4 | power given |
| memory used, mean (MB) | 60.7 | 60.7 | -0.1% | -0.74 to 0.631 | EVEN, no difference beyond the noise |
| keys evicted | 243,157 | 245,027 | +0.8% | -2,955 to 6,695 | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.14 | +0.1% | -0.0223 to 0.0227 | EVEN, no difference beyond the noise |
| host CPU-seconds | 233 | 234 | +0.3% | -40.6 to 42.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.56 | 0.563 | +0.5% | -0.0971 to 0.103 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.7 |  | 15.5 to 29.8 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
