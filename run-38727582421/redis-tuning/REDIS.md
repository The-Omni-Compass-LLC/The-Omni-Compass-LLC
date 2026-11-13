# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,248 | +5.4% | 39.2 to 88.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00314 to 0.00638 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.832 | +5.4% | 0.0262 to 0.0589 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.75 | -0.1% | -0.013 to -0.00279 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.81 | +0.0% | -0.00237 to 0.00318 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.12 | -17.4% | -0.328 to -0.142 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 83.8 | +31.0% | 0.815 to 38.9 | power given |
| memory used, mean (MB) | 61.2 | 76.5 | +25.0% | 2.56 to 28 | power given |
| keys evicted | 138,187 | 110,015 | -20.4% | -42,237 to -14,106 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.11 | -3.0% | -0.0276 to 0.0209 | EVEN, no difference beyond the noise |
| host CPU-seconds | 187 | 182 | -2.6% | -50.7 to 41.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.351 | 0.325 | -7.6% | -0.104 to 0.0509 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 43.3 |  | 8.43 to 78.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 18.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
