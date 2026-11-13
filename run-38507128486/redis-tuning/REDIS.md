# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,254 | +5.9% | 60.1 to 79 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.00185 to 0.00309 | GAIN |
| cache hit rate | 0.789 | 0.836 | +5.9% | 0.04 to 0.0527 | GAIN |
| latency, 95th percentile (ms) | 5.53 | 5.51 | -0.4% | -0.0547 to 0.0113 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.61 | 5.6 | -0.1% | -0.0215 to 0.00823 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.24 | 0.994 | -19.8% | -0.286 to -0.205 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 86.6 | +35.3% | 19.2 to 26 | power given |
| memory used, mean (MB) | 61.2 | 79.8 | +30.3% | 17 to 20.1 | power given |
| keys evicted | 138,123 | 107,662 | -22.1% | -34,737 to -26,186 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.0934 | -8.2% | -0.0555 to 0.0387 | EVEN, no difference beyond the noise |
| host CPU-seconds | 179 | 163 | -8.7% | -108 to 76.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.336 | 0.29 | -13.8% | -0.215 to 0.122 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 51 |  | 28.2 to 73.8 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
