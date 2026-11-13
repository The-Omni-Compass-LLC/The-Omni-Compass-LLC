# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,313 | +3.7% | -4.58 to 97.7 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000885 to 0.00384 | EVEN, the same |
| cache hit rate | 0.845 | 0.876 | +3.7% | -0.00283 to 0.0652 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.2% | -0.0428 to 0.0224 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.82 | -0.0% | -0.0378 to 0.0374 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 0.887 | -16.1% | -0.367 to 0.0258 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 67.6 | +5.6% | -4.3 to 11.5 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 63.8 | +4.0% | -5.3 to 10.2 | EVEN, no difference beyond the noise |
| keys evicted | 103,531 | 83,020 | -19.8% | -43,975 to 2,951 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.123 | +4.1% | -0.0105 to 0.0201 | EVEN, no difference beyond the noise |
| host CPU-seconds | 196 | 207 | +5.4% | -20 to 41.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.344 | 0.35 | +1.7% | -0.0362 to 0.0476 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 33.3 |  | 19.2 to 47.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 16.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
