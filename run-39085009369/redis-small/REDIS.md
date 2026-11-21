# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 937 | +1.2% | 11 to 11.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0165 to -0.00336 | LOSS |
| cache hit rate | 0.618 | 0.625 | +1.2% | 0.00727 to 0.0077 | GAIN |
| latency, 95th percentile (ms) | 5.5 | 5.5 | +0.0% | -0.0161 to 0.0182 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.57 | 5.58 | +0.1% | -0.00592 to 0.0194 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.14 | 2.1 | -1.8% | -0.0479 to -0.0301 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.1% | 0.791 to 1.89 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.1% | 1.16 to 1.4 | power given |
| keys evicted | 243,012 | 234,832 | -3.4% | -8,357 to -8,003 | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.113 | +2.9% | -0.0159 to 0.0222 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 198 | +3.3% | -31.8 to 44.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.46 | 0.47 | +2.0% | -0.0817 to 0.1 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14.3 |  | 8.6 to 20.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
