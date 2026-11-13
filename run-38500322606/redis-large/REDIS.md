# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `43a27376d80b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,268 | 1,347 | +6.2% | 23.5 to 135 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00402 to 0.00334 | EVEN, the same |
| cache hit rate | 0.845 | 0.898 | +6.2% | 0.0158 to 0.0897 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 5.7 | -0.4% | -0.0484 to 0.00425 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.78 | -0.2% | -0.0171 to -0.00292 | GAIN |
| latency, mean (ms) | 1.04 | 0.75 | -27.9% | -0.495 to -0.0859 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 74.1 | +15.8% | -3.25 to 23.5 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 68.3 | +11.4% | -0.922 to 14.9 | EVEN, no difference beyond the noise |
| keys evicted | 103,223 | 68,241 | -33.9% | -60,114 to -9,850 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.0983 | -15.7% | -0.0702 to 0.0336 | EVEN, no difference beyond the noise |
| host CPU-seconds | 196 | 163 | -16.6% | -129 to 63.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.343 | 0.27 | -21.4% | -0.247 to 0.1 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 41.3 |  | 20.5 to 62.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 16.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
