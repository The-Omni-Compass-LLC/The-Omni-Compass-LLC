# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,068 | 1,068 | -0.0% | -4 to 3.68 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.296 to 0.198 | EVEN, no difference beyond the noise |
| cache hit rate | 0.717 | 0.717 | -0.0% | -0.000644 to 0.00023 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.15 | 5.88 | -4.3% | -1.44 to 0.908 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 9 | 8.64 | -4.1% | -2.25 to 1.52 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.88 | 1.84 | -1.9% | -0.212 to 0.139 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 60.7 | -5.1% | -4.23 to -2.35 | GAIN |
| memory used, mean (MB) | 57.2 | 54.8 | -4.2% | -3.39 to -1.36 | GAIN |
| keys evicted | 71,988 | 72,037 | +0.1% | -92.5 to 191 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.15 | +2.9% | -0.0319 to 0.0404 | EVEN, no difference beyond the noise |
| host CPU-seconds | 102 | 107 | +4.5% | -24.2 to 33.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.533 | 0.557 | +4.5% | -0.127 to 0.175 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
