# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,263 | 1,283 | +1.6% | 9.34 to 30.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.231 to 0.371 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.857 | +1.5% | 0.00756 to 0.018 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.1% | -0.0118 to 0.00375 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.25 | 5.24 | -0.1% | -0.0278 to 0.0141 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.892 | 0.822 | -7.8% | -0.117 to -0.0223 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65 | +1.6% | -0.224 to 2.31 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.5 | +0.3% | -0.556 to 0.963 | EVEN, no difference beyond the noise |
| keys evicted | 103,620 | 95,124 | -8.2% | -11,992 to -5,000 | shown, not judged |
| host CPU busy (share of the run) | 0.0565 | 0.0543 | -4.0% | -0.0383 to 0.0339 | EVEN, no difference beyond the noise |
| host CPU-seconds | 99.4 | 95.7 | -3.8% | -71.4 to 64 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.175 | 0.166 | -5.3% | -0.126 to 0.107 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.7 |  | 21.2 to 24.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
