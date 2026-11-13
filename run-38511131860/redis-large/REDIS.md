# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,332 | +5.1% | -10.7 to 140 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0059 to 0.00287 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.888 | +5.1% | -0.00731 to 0.0937 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.73 | 5.71 | -0.2% | -0.042 to 0.0163 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.79 | -0.0% | -0.0268 to 0.0219 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.812 | -22.4% | -0.52 to 0.05 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 71.1 | +11.1% | 0.579 to 13.6 | power given |
| memory used, mean (MB) | 61.3 | 66.1 | +7.9% | -1.99 to 11.7 | EVEN, no difference beyond the noise |
| keys evicted | 103,471 | 74,806 | -27.7% | -62,176 to 4,846 | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.109 | +4.8% | -0.0195 to 0.0295 | EVEN, no difference beyond the noise |
| host CPU-seconds | 172 | 183 | +6.3% | -33.7 to 55.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.302 | 0.306 | +1.3% | -0.0869 to 0.0949 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 37.7 |  | 23.5 to 51.8 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 15.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
