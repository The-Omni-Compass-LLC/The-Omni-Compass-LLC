# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 924 | -0.2% | -1.97 to -0.956 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0198 to 0.00296 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.616 | -0.2% | -0.00122 to -0.000689 | LOSS |
| latency, 95th percentile (ms) | 5.68 | 5.68 | +0.1% | -0.0041 to 0.0114 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.2% | 0.0018 to 0.019 | LOSS |
| latency, mean (ms) | 2.26 | 2.27 | +0.3% | 0.00197 to 0.0134 | LOSS |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.7 | +1.1% | 0.318 to 1.1 | power given |
| memory used, mean (MB) | 60.7 | 60.6 | -0.1% | -0.813 to 0.678 | EVEN, no difference beyond the noise |
| keys evicted | 243,133 | 244,891 | +0.7% | -2,738 to 6,254 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.135 | -5.9% | -0.0597 to 0.0428 | EVEN, no difference beyond the noise |
| host CPU-seconds | 243 | 226 | -6.7% | -116 to 83.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.582 | 0.544 | -6.6% | -0.279 to 0.202 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 24.3 |  | 14 to 34.7 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
