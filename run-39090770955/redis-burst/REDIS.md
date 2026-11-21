# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `8e3f058da83e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% | -1.8 to 0.505 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0201 to 0.0124 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00121 to 0.000388 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.57 | 5.58 | +0.1% | -0.011 to 0.0182 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.65 | 5.66 | +0.1% | -0.00928 to 0.0191 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.62 | 1.63 | +0.3% | -0.00401 to 0.0149 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.6 | -2.2% | -1.69 to -1.13 | GAIN |
| memory used, mean (MB) | 57.1 | 56.7 | -0.8% | -0.701 to -0.253 | GAIN |
| keys evicted | 71,669 | 71,803 | +0.2% | -56.9 to 326 | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.109 | +4.5% | -0.00492 to 0.0143 | EVEN, no difference beyond the noise |
| host CPU-seconds | 74.3 | 77.9 | +4.9% | -3.91 to 11.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.383 | 0.402 | +5.0% | -0.0197 to 0.0576 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
