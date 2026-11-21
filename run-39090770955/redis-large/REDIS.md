# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `8e3f058da83e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,288 | +1.6% | 18.7 to 22.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00949 to 0.00543 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.859 | +1.6% | 0.0126 to 0.0152 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.0% | -0.00371 to -0.000347 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.1% | 0.00223 to 0.00455 | LOSS |
| latency, mean (ms) | 1.05 | 0.973 | -7.1% | -0.0804 to -0.0686 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.1 | +1.7% | -0.593 to 2.76 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.9 | +1.0% | -0.14 to 1.34 | EVEN, no difference beyond the noise |
| keys evicted | 103,447 | 94,263 | -8.9% | -10,150 to -8,218 | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.109 | -13.9% | -0.0567 to 0.0217 | EVEN, no difference beyond the noise |
| host CPU-seconds | 214 | 181 | -15.5% | -107 to 40.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.375 | 0.312 | -16.8% | -0.191 to 0.0653 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 19.5 to 25.2 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
