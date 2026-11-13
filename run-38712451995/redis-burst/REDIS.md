# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% | -2.43 to 1.04 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0625 to 0.0405 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00146 to 0.000419 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.76 | 5.75 | -0.1% | -0.0116 to 0.00166 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.95 | 5.86 | -1.4% | -0.5 to 0.329 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.76 | 1.76 | +0.1% | -0.0194 to 0.0223 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.6 | -3.8% | -5.8 to 0.914 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 57.2 | 55.4 | -3.0% | -4.24 to 0.769 | EVEN, no difference beyond the noise |
| keys evicted | 71,703 | 71,848 | +0.2% | -131 to 420 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.142 | +9.9% | -0.00562 to 0.0313 | EVEN, no difference beyond the noise |
| host CPU-seconds | 85.4 | 95.5 | +11.8% | -3.46 to 23.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.441 | 0.493 | +11.8% | -0.0182 to 0.123 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8.67 |  | 2.93 to 14.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 8.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
