# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,236 | +4.5% | -5.11 to 112 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0365 to 0.0556 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.825 | +4.6% | -0.00438 to 0.0763 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.0% | -0.0132 to 0.00921 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.25 | 5.25 | -0.0% | -0.0476 to 0.0457 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 0.985 | -15.6% | -0.37 to 0.00505 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 78.6 | +22.8% | -7.71 to 36.9 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 73.1 | +19.5% | -5.81 to 29.7 | EVEN, no difference beyond the noise |
| keys evicted | 138,173 | 115,008 | -16.8% | -51,523 to 5,193 | shown, not judged |
| host CPU busy (share of the run) | 0.0541 | 0.0471 | -13.0% | -0.0332 to 0.0191 | EVEN, no difference beyond the noise |
| host CPU-seconds | 94.9 | 82.1 | -13.5% | -60.5 to 34.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.178 | 0.148 | -17.1% | -0.118 to 0.0573 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 40 |  | 8.97 to 71 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
