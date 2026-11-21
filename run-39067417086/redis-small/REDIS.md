# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 936 | +1.3% | 9.86 to 14.6 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0338 to 0.02 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00759 to 0.00871 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.0% | -0.0129 to 0.00953 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.31 | 5.29 | -0.4% | -0.171 to 0.132 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.05 | 2.01 | -2.1% | -0.0651 to -0.0231 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | 1.45 to 1.73 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.2% | 1.25 to 1.37 | power given |
| keys evicted | 243,333 | 234,692 | -3.6% | -9,091 to -8,191 | shown, not judged |
| host CPU busy (share of the run) | 0.0617 | 0.0546 | -11.4% | -0.0407 to 0.0266 | EVEN, no difference beyond the noise |
| host CPU-seconds | 109 | 95.4 | -12.1% | -76 to 49.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.261 | 0.226 | -13.3% | -0.185 to 0.116 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13.7 |  | 10.8 to 16.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 16.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
