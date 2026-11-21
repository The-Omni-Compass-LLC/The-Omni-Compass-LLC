# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `a00031b9149c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,264 | 1,283 | +1.5% | 11.7 to 25.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0252 to 0.0363 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.857 | +1.5% | 0.00646 to 0.0187 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 5.23 | -0.2% | -0.0305 to 0.0133 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.33 | 5.27 | -1.1% | -0.287 to 0.167 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.9 | 0.831 | -7.6% | -0.078 to -0.0591 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.0% | -2.22 to 4.75 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.9 | +1.0% | -1.58 to 2.8 | EVEN, no difference beyond the noise |
| keys evicted | 103,696 | 95,334 | -8.1% | -12,811 to -3,913 | shown, not judged |
| host CPU busy (share of the run) | 0.0583 | 0.0621 | +6.4% | -0.0261 to 0.0335 | EVEN, no difference beyond the noise |
| host CPU-seconds | 102 | 109 | +7.1% | -49.7 to 64.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.179 | 0.19 | +5.6% | -0.09 to 0.11 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22 |  | 19.5 to 24.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
