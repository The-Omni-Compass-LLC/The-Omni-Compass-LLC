# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -1.52 to 0.597 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00781 to 0.00978 | EVEN, the same |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00104 to 0.000445 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.65 | 5.64 | -0.1% | -0.0238 to 0.0106 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.72 | 5.72 | -0.0% | -0.0255 to 0.0234 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.65 | 1.64 | -0.1% | -0.0131 to 0.00912 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.2 | -4.3% | -3.81 to -1.73 | GAIN |
| memory used, mean (MB) | 57.2 | 55.4 | -3.1% | -2.99 to -0.534 | GAIN |
| keys evicted | 71,722 | 71,800 | +0.1% | -115 to 271 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.114 | +6.5% | 0.00241 to 0.0115 | power given |
| host CPU-seconds | 75.3 | 81 | +7.6% | 1.86 to 9.6 | power given |
| host CPU-seconds per 1,000 requests inside the line | 0.389 | 0.418 | +7.7% | 0.00951 to 0.05 | power given |
| ceiling changes written (the knob's moves) | 0 | 9.67 |  | 8.23 to 11.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
