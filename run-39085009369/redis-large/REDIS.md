# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,287 | +1.6% | 16.1 to 23.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00141 to 0.0016 | EVEN, the same |
| cache hit rate | 0.845 | 0.858 | +1.5% | 0.0102 to 0.016 | GAIN |
| latency, 95th percentile (ms) | 5.5 | 5.49 | -0.0% | -0.0184 to 0.0163 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.61 | +0.1% | -0.0014 to 0.00831 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.957 | 0.889 | -7.1% | -0.0792 to -0.0576 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.7 | +1.1% | -2.56 to 4.01 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.6 | +0.6% | -2.97 to 3.65 | EVEN, no difference beyond the noise |
| keys evicted | 103,283 | 94,743 | -8.3% | -10,792 to -6,288 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.1 | -6.8% | -0.0331 to 0.0184 | EVEN, no difference beyond the noise |
| host CPU-seconds | 190 | 175 | -7.5% | -64.4 to 36 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.333 | 0.303 | -8.9% | -0.117 to 0.0583 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 9.85 to 36.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
