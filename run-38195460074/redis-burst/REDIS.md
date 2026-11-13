# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,045 | 1,044 | -0.1% | -4.23 to 2.13 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.84 to 0.522 | no difference beyond the noise |
| cache hit rate | 0.698 | 0.697 | -0.1% | -0.00169 to 0.000536 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.21 | 5.21 | +0.0% | -0.00449 to 0.00605 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.27 | +0.2% | -0.0871 to 0.109 | no difference beyond the noise |
| latency, mean (ms) | 1.64 | 1.65 | +0.8% | -0.0387 to 0.0663 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.4 | -0.9% | -0.595 to -0.595 | better |
| memory used, mean (MB) | 56.9 | 57 | +0.1% | 0.036 to 0.0987 | **WORSE** |
| keys evicted | 49,833 | 50,572 | +1.5% | 501 to 978 | shown, not judged |
| host CPU busy (share of the run) | 0.0484 | 0.0639 | +32.0% | 0.00198 to 0.029 | **WORSE** |
| host CPU-seconds | 22.5 | 30.1 | +34.1% | 1.12 to 14.2 | **WORSE** |
| host CPU-seconds per 1,000 requests inside the line | 0.179 | 0.24 | +34.2% | 0.00866 to 0.114 | **WORSE** |
| ceiling changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
