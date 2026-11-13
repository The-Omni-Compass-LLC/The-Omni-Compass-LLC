# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,331 | +5.1% | 2.68 to 125 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00224 to 0.00248 | EVEN, the same |
| cache hit rate | 0.845 | 0.888 | +5.0% | 0.00203 to 0.0832 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.72 | -0.3% | -0.0365 to -0.000294 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.8 | -0.1% | -0.0295 to 0.0175 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.817 | -22.5% | -0.465 to -0.00838 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 71 | +11.0% | -1.7 to 15.7 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 66 | +7.6% | -1.87 to 11.2 | EVEN, no difference beyond the noise |
| keys evicted | 103,336 | 75,073 | -27.4% | -55,502 to -1,023 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.112 | -3.2% | -0.042 to 0.0346 | EVEN, no difference beyond the noise |
| host CPU-seconds | 194 | 188 | -2.9% | -79.3 to 67.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.34 | 0.315 | -7.6% | -0.161 to 0.109 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 36 |  | 27 to 45 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 17.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
