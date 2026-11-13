# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `43a27376d80b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,241 | +4.8% | 25.4 to 89.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00416 to 0.00534 | EVEN, the same |
| cache hit rate | 0.789 | 0.828 | +4.8% | 0.017 to 0.0595 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 5.73 | -0.1% | -0.0221 to 0.0127 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.1% | -0.0134 to 0.0243 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.13 | -15.6% | -0.333 to -0.084 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 78.5 | +22.7% | -3.82 to 32.9 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 73.2 | +19.6% | -1.27 to 25.3 | EVEN, no difference beyond the noise |
| keys evicted | 138,111 | 113,680 | -17.7% | -38,558 to -10,303 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.108 | -6.5% | -0.0282 to 0.0132 | EVEN, no difference beyond the noise |
| host CPU-seconds | 193 | 180 | -6.7% | -52 to 26.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.361 | 0.322 | -11.0% | -0.111 to 0.0316 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 36.3 |  | 17.7 to 55 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 19.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
