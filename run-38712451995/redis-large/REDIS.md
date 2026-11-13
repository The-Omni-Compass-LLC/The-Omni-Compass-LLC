# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,324 | +4.5% | 24.5 to 90.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00337 to 0.00297 | EVEN, the same |
| cache hit rate | 0.845 | 0.883 | +4.5% | 0.0165 to 0.0602 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.3% | -0.0444 to 0.0147 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.8 | -0.1% | -0.0319 to 0.0197 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.842 | -20.1% | -0.34 to -0.0832 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 69.3 | +8.4% | -0.93 to 11.6 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 65.3 | +6.6% | -0.521 to 8.61 | EVEN, no difference beyond the noise |
| keys evicted | 103,587 | 78,139 | -24.6% | -40,305 to -10,590 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.109 | -9.7% | -0.0442 to 0.021 | EVEN, no difference beyond the noise |
| host CPU-seconds | 202 | 182 | -10.1% | -82.7 to 42 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.355 | 0.305 | -14.0% | -0.157 to 0.058 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 36 |  | 22.9 to 49.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 15.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
