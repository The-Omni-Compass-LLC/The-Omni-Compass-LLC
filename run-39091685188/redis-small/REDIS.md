# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 938 | +1.3% | 10.1 to 14 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.129 to 0.0497 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00691 to 0.00925 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.7 | +0.1% | -0.0183 to 0.0298 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.76 | +0.3% | -0.0166 to 0.0514 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.23 | -1.7% | -0.0585 to -0.0193 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.1% | 0.873 to 1.76 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.89 to 1.45 | power given |
| keys evicted | 243,177 | 236,722 | -2.7% | -14,963 to 2,054 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.14 | -3.6% | -0.0415 to 0.031 | EVEN, no difference beyond the noise |
| host CPU-seconds | 244 | 234 | -4.4% | -80.6 to 59 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.587 | 0.554 | -5.7% | -0.201 to 0.135 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15.3 |  | 13.9 to 16.8 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
